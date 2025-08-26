"""
Módulo de Conexión a Base de Datos

¿Qué es una Base de Datos?
Una base de datos es un sistema organizado de almacenamiento de información que permite
guardar, recuperar, actualizar y eliminar datos de manera eficiente. En este proyecto
utilizamos SQLite, que es una base de datos relacional liviana.

El "Control de Datos":
Se refiere a la gestión del acceso, integridad y manipulación de los datos en la base
de datos. Esto incluye transacciones, control de concurrencia y validación de datos.
"""

import sqlite3
import os
from typing import Optional, Any, List, Tuple
from contextlib import contextmanager

class DatabaseConnection:
    """
    Clase para manejar la conexión a la base de datos SQLite.
    Implementa el patrón Singleton para garantizar una sola conexión.
    """
    
    _instance = None
    _connection = None
    
    def __new__(cls, db_path: str = "school_database.db"):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.db_path = db_path
        return cls._instance
    
    def __init__(self, db_path: str = "school_database.db"):
        if not hasattr(self, 'initialized'):
            self.db_path = db_path
            self.initialized = True
            self._create_tables()
    
    def connect(self) -> sqlite3.Connection:
        """Establece una conexión a la base de datos"""
        if self._connection is None:
            try:
                self._connection = sqlite3.connect(
                    self.db_path,
                    check_same_thread=False,
                    timeout=30.0
                )
                # Habilitar claves foráneas para integridad referencial
                self._connection.execute("PRAGMA foreign_keys = ON")
                self._connection.row_factory = sqlite3.Row
                print(f"✓ Conexión establecida con la base de datos: {self.db_path}")
            except sqlite3.Error as e:
                print(f"✗ Error al conectar con la base de datos: {e}")
                raise
        return self._connection
    
    def disconnect(self):
        """Cierra la conexión a la base de datos"""
        if self._connection:
            self._connection.close()
            self._connection = None
            print("✓ Conexión a la base de datos cerrada")
    
    @contextmanager
    def get_cursor(self):
        """
        Context manager para obtener un cursor de base de datos
        Garantiza que las operaciones se ejecuten de forma segura
        """
        conn = self.connect()
        cursor = conn.cursor()
        try:
            yield cursor
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            print(f"✗ Error en la operación de base de datos: {e}")
            raise
        finally:
            cursor.close()
    
    def execute_query(self, query: str, params: Tuple = ()) -> List[sqlite3.Row]:
        """
        Ejecuta una consulta SELECT y retorna los resultados
        """
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
    
    def execute_non_query(self, query: str, params: Tuple = ()) -> int:
        """
        Ejecuta una consulta INSERT, UPDATE o DELETE
        Retorna el número de filas afectadas
        """
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            return cursor.rowcount
    
    def execute_scalar(self, query: str, params: Tuple = ()) -> Any:
        """
        Ejecuta una consulta que retorna un solo valor
        """
        with self.get_cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result[0] if result else None
    
    def _create_tables(self):
        """
        Crea las tablas necesarias para el sistema escolar
        Implementa Integridad Referencial con claves foráneas
        """
        tables_sql = [
            # Tabla de Estudiantes
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                birth_date DATE,
                enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
                status TEXT CHECK(status IN ('active', 'inactive', 'graduated')) DEFAULT 'active',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            
            # Tabla de Cursos
            """
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                code TEXT UNIQUE NOT NULL,
                description TEXT,
                credits INTEGER NOT NULL DEFAULT 3,
                semester TEXT,
                instructor TEXT,
                capacity INTEGER DEFAULT 30,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
            
            # Tabla de Inscripciones (Integridad Referencial)
            """
            CREATE TABLE IF NOT EXISTS enrollments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course_id INTEGER NOT NULL,
                enrollment_date DATE NOT NULL DEFAULT CURRENT_DATE,
                grade REAL CHECK(grade >= 0 AND grade <= 100),
                status TEXT CHECK(status IN ('enrolled', 'completed', 'dropped')) DEFAULT 'enrolled',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
                FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
                UNIQUE(student_id, course_id)
            )
            """,
            
            # Tabla de Auditoría
            """
            CREATE TABLE IF NOT EXISTS audit_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                table_name TEXT NOT NULL,
                operation TEXT NOT NULL,
                record_id INTEGER,
                old_values TEXT,
                new_values TEXT,
                user_id TEXT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        ]
        
        # Crear triggers para actualizar updated_at automáticamente
        triggers_sql = [
            """
            CREATE TRIGGER IF NOT EXISTS update_students_timestamp 
            AFTER UPDATE ON students
            FOR EACH ROW
            BEGIN
                UPDATE students SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
            END
            """,
            
            """
            CREATE TRIGGER IF NOT EXISTS update_courses_timestamp 
            AFTER UPDATE ON courses
            FOR EACH ROW
            BEGIN
                UPDATE courses SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
            END
            """,
            
            """
            CREATE TRIGGER IF NOT EXISTS update_enrollments_timestamp 
            AFTER UPDATE ON enrollments
            FOR EACH ROW
            BEGIN
                UPDATE enrollments SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
            END
            """
        ]
        
        try:
            with self.get_cursor() as cursor:
                # Crear tablas
                for table_sql in tables_sql:
                    cursor.execute(table_sql)
                
                # Crear triggers
                for trigger_sql in triggers_sql:
                    cursor.execute(trigger_sql)
                
                print("✓ Tablas y triggers creados exitosamente")
                
                # Insertar datos de ejemplo si no existen
                self._insert_sample_data()
                
        except sqlite3.Error as e:
            print(f"✗ Error al crear las tablas: {e}")
            raise
    
    def _insert_sample_data(self):
        """Inserta datos de ejemplo si las tablas están vacías"""
        try:
            # Verificar si ya existen datos
            student_count = self.execute_scalar("SELECT COUNT(*) FROM students")
            
            if student_count == 0:
                # Insertar estudiantes de ejemplo
                students_data = [
                    ("Juan", "Pérez", "juan.perez@email.com", "123-456-7890", "1995-03-15"),
                    ("María", "García", "maria.garcia@email.com", "123-456-7891", "1996-07-20"),
                    ("Carlos", "López", "carlos.lopez@email.com", "123-456-7892", "1994-11-10"),
                    ("Ana", "Martínez", "ana.martinez@email.com", "123-456-7893", "1997-02-28"),
                    ("Luis", "Rodríguez", "luis.rodriguez@email.com", "123-456-7894", "1995-09-05")
                ]
                
                for student in students_data:
                    self.execute_non_query(
                        "INSERT INTO students (first_name, last_name, email, phone, birth_date) VALUES (?, ?, ?, ?, ?)",
                        student
                    )
                
                # Insertar cursos de ejemplo
                courses_data = [
                    ("Programación I", "PROG101", "Introducción a la programación", 4, "2024-1", "Prof. Smith"),
                    ("Base de Datos", "BD201", "Fundamentos de bases de datos", 3, "2024-1", "Prof. Johnson"),
                    ("Matemáticas", "MAT101", "Matemáticas básicas", 3, "2024-1", "Prof. Brown"),
                    ("Inglés", "ENG101", "Inglés básico", 2, "2024-1", "Prof. Davis"),
                    ("Algoritmos", "ALG201", "Algoritmos y estructuras de datos", 4, "2024-2", "Prof. Wilson")
                ]
                
                for course in courses_data:
                    self.execute_non_query(
                        "INSERT INTO courses (name, code, description, credits, semester, instructor) VALUES (?, ?, ?, ?, ?, ?)",
                        course
                    )
                
                # Insertar algunas inscripciones de ejemplo
                enrollments_data = [
                    (1, 1, 85.5),  # Juan en Programación I
                    (1, 2, 90.0),  # Juan en Base de Datos
                    (2, 1, 78.0),  # María en Programación I
                    (2, 3, 92.5),  # María en Matemáticas
                    (3, 2, 88.0),  # Carlos en Base de Datos
                ]
                
                for enrollment in enrollments_data:
                    self.execute_non_query(
                        "INSERT INTO enrollments (student_id, course_id, grade, status) VALUES (?, ?, ?, 'completed')",
                        enrollment
                    )
                
                print("✓ Datos de ejemplo insertados exitosamente")
                
        except sqlite3.Error as e:
            print(f"✗ Error al insertar datos de ejemplo: {e}")
    
    def get_database_info(self) -> dict:
        """Retorna información sobre la base de datos"""
        info = {
            'database_path': self.db_path,
            'database_size': os.path.getsize(self.db_path) if os.path.exists(self.db_path) else 0,
            'tables': [],
            'total_records': 0
        }
        
        try:
            # Obtener lista de tablas
            tables = self.execute_query("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
            
            for table in tables:
                table_name = table['name']
                count = self.execute_scalar(f"SELECT COUNT(*) FROM {table_name}")
                info['tables'].append({
                    'name': table_name,
                    'records': count
                })
                info['total_records'] += count
                
        except sqlite3.Error as e:
            print(f"✗ Error al obtener información de la base de datos: {e}")
        
        return info
