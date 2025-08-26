"""
Manipulación de Datos (Operaciones CRUD con SQL)

CRUD es un acrónimo que representa las cuatro operaciones básicas de manipulación de datos:
- CREATE: Crear nuevos registros (INSERT)
- READ: Leer/consultar registros existentes (SELECT)
- UPDATE: Actualizar registros existentes (UPDATE)
- DELETE: Eliminar registros (DELETE)

Este módulo proporciona una interfaz unificada para realizar operaciones CRUD
utilizando SQL (Structured Query Language).

SQL es un lenguaje estándar para manejar bases de datos relacionales.
Permite crear, modificar y consultar datos de manera eficiente y flexible.
"""

from typing import List, Dict, Any, Optional, Tuple
import sqlite3
from datetime import datetime
from .connection import DatabaseConnection
from .dao import Student, Course, Enrollment, StudentDAO, CourseDAO, EnrollmentDAO

class CRUDOperations:
    """
    Clase que encapsula todas las operaciones CRUD del sistema
    Proporciona una interfaz unificada para la manipulación de datos
    """
    
    def __init__(self):
        self.db = DatabaseConnection()
        self.student_dao = StudentDAO()
        self.course_dao = CourseDAO()
        self.enrollment_dao = EnrollmentDAO()
    
    # ========================================
    # 1. AÑADIR NUEVOS REGISTROS (INSERT)
    # ========================================
    
    def add_student(self, first_name: str, last_name: str, email: str, 
                   phone: str = "", birth_date: str = None, status: str = "active") -> int:
        """
        Añadir un nuevo estudiante a la base de datos
        
        SQL equivalente:
        INSERT INTO students (first_name, last_name, email, phone, birth_date, status) 
        VALUES (?, ?, ?, ?, ?, ?)
        """
        student = Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            birth_date=birth_date,
            status=status
        )
        
        try:
            student_id = self.student_dao.create(student)
            print(f"✓ Estudiante agregado exitosamente. ID: {student_id}")
            return student_id
        except ValueError as e:
            print(f"✗ Error al agregar estudiante: {e}")
            raise
        except Exception as e:
            print(f"✗ Error inesperado: {e}")
            raise
    
    def add_course(self, name: str, code: str, description: str = "", 
                  credits: int = 3, semester: str = "", instructor: str = "", 
                  capacity: int = 30) -> int:
        """
        Añadir un nuevo curso a la base de datos
        
        SQL equivalente:
        INSERT INTO courses (name, code, description, credits, semester, instructor, capacity) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        course = Course(
            name=name,
            code=code,
            description=description,
            credits=credits,
            semester=semester,
            instructor=instructor,
            capacity=capacity
        )
        
        try:
            course_id = self.course_dao.create(course)
            print(f"✓ Curso agregado exitosamente. ID: {course_id}")
            return course_id
        except ValueError as e:
            print(f"✗ Error al agregar curso: {e}")
            raise
        except Exception as e:
            print(f"✗ Error inesperado: {e}")
            raise
    
    def enroll_student(self, student_id: int, course_id: int, 
                      grade: float = None, status: str = "enrolled") -> int:
        """
        Inscribir un estudiante en un curso
        
        SQL equivalente:
        INSERT INTO enrollments (student_id, course_id, grade, status) 
        VALUES (?, ?, ?, ?)
        """
        enrollment = Enrollment(
            student_id=student_id,
            course_id=course_id,
            grade=grade,
            status=status
        )
        
        try:
            enrollment_id = self.enrollment_dao.create(enrollment)
            print(f"✓ Inscripción creada exitosamente. ID: {enrollment_id}")
            return enrollment_id
        except ValueError as e:
            print(f"✗ Error al crear inscripción: {e}")
            raise
        except Exception as e:
            print(f"✗ Error inesperado: {e}")
            raise
    
    # ========================================
    # 2. EDITAR REGISTROS (UPDATE)
    # ========================================
    
    def update_student(self, student_id: int, **kwargs) -> bool:
        """
        Editar la información de un estudiante
        
        SQL equivalente:
        UPDATE students SET first_name = ?, last_name = ?, email = ?, 
                           phone = ?, birth_date = ?, status = ?
        WHERE id = ?
        """
        student = self.student_dao.get_by_id(student_id)
        if not student:
            print(f"✗ Estudiante con ID {student_id} no encontrado")
            return False
        
        # Actualizar los campos proporcionados
        for field, value in kwargs.items():
            if hasattr(student, field):
                setattr(student, field, value)
        
        try:
            success = self.student_dao.update(student)
            if success:
                print(f"✓ Estudiante ID {student_id} actualizado exitosamente")
            else:
                print(f"✗ No se pudo actualizar el estudiante ID {student_id}")
            return success
        except ValueError as e:
            print(f"✗ Error al actualizar estudiante: {e}")
            raise
        except Exception as e:
            print(f"✗ Error inesperado: {e}")
            raise
    
    def update_course(self, course_id: int, **kwargs) -> bool:
        """
        Editar la información de un curso
        
        SQL equivalente:
        UPDATE courses SET name = ?, code = ?, description = ?, credits = ?, 
                          semester = ?, instructor = ?, capacity = ?
        WHERE id = ?
        """
        course = self.course_dao.get_by_id(course_id)
        if not course:
            print(f"✗ Curso con ID {course_id} no encontrado")
            return False
        
        # Actualizar los campos proporcionados
        for field, value in kwargs.items():
            if hasattr(course, field):
                setattr(course, field, value)
        
        try:
            success = self.course_dao.update(course)
            if success:
                print(f"✓ Curso ID {course_id} actualizado exitosamente")
            else:
                print(f"✗ No se pudo actualizar el curso ID {course_id}")
            return success
        except ValueError as e:
            print(f"✗ Error al actualizar curso: {e}")
            raise
        except Exception as e:
            print(f"✗ Error inesperado: {e}")
            raise
    
    def update_enrollment(self, enrollment_id: int, **kwargs) -> bool:
        """
        Editar una inscripción (principalmente para actualizar calificaciones)
        
        SQL equivalente:
        UPDATE enrollments SET grade = ?, status = ?
        WHERE id = ?
        """
        enrollment = self.enrollment_dao.get_by_id(enrollment_id)
        if not enrollment:
            print(f"✗ Inscripción con ID {enrollment_id} no encontrada")
            return False
        
        # Actualizar los campos proporcionados
        for field, value in kwargs.items():
            if hasattr(enrollment, field):
                setattr(enrollment, field, value)
        
        try:
            success = self.enrollment_dao.update(enrollment)
            if success:
                print(f"✓ Inscripción ID {enrollment_id} actualizada exitosamente")
            else:
                print(f"✗ No se pudo actualizar la inscripción ID {enrollment_id}")
            return success
        except ValueError as e:
            print(f"✗ Error al actualizar inscripción: {e}")
            raise
        except Exception as e:
            print(f"✗ Error inesperado: {e}")
            raise
    
    # ========================================
    # 3. BORRAR REGISTROS (DELETE)
    # ========================================
    
    def delete_student(self, student_id: int) -> bool:
        """
        Borrar un estudiante de la base de datos
        
        SQL equivalente:
        DELETE FROM students WHERE id = ?
        
        Nota: También eliminará automáticamente todas las inscripciones del estudiante
        debido a la integridad referencial (ON DELETE CASCADE)
        """
        try:
            success = self.student_dao.delete(student_id)
            if success:
                print(f"✓ Estudiante ID {student_id} eliminado exitosamente")
            else:
                print(f"✗ Estudiante con ID {student_id} no encontrado")
            return success
        except Exception as e:
            print(f"✗ Error al eliminar estudiante: {e}")
            raise
    
    def delete_course(self, course_id: int) -> bool:
        """
        Borrar un curso de la base de datos
        
        SQL equivalente:
        DELETE FROM courses WHERE id = ?
        
        Nota: También eliminará automáticamente todas las inscripciones del curso
        debido a la integridad referencial (ON DELETE CASCADE)
        """
        try:
            success = self.course_dao.delete(course_id)
            if success:
                print(f"✓ Curso ID {course_id} eliminado exitosamente")
            else:
                print(f"✗ Curso con ID {course_id} no encontrado")
            return success
        except Exception as e:
            print(f"✗ Error al eliminar curso: {e}")
            raise
    
    def delete_enrollment(self, enrollment_id: int) -> bool:
        """
        Borrar una inscripción de la base de datos
        
        SQL equivalente:
        DELETE FROM enrollments WHERE id = ?
        """
        try:
            success = self.enrollment_dao.delete(enrollment_id)
            if success:
                print(f"✓ Inscripción ID {enrollment_id} eliminada exitosamente")
            else:
                print(f"✗ Inscripción con ID {enrollment_id} no encontrada")
            return success
        except Exception as e:
            print(f"✗ Error al eliminar inscripción: {e}")
            raise
    
    # ========================================
    # 4. LOCALIZAR REGISTROS (SELECT ... WHERE)
    # ========================================
    
    def find_student_by_id(self, student_id: int) -> Optional[Student]:
        """
        Localizar un estudiante por ID
        
        SQL equivalente:
        SELECT * FROM students WHERE id = ?
        """
        try:
            student = self.student_dao.get_by_id(student_id)
            if student:
                print(f"✓ Estudiante encontrado: {student.full_name}")
            else:
                print(f"✗ Estudiante con ID {student_id} no encontrado")
            return student
        except Exception as e:
            print(f"✗ Error al buscar estudiante: {e}")
            raise
    
    def find_students_by_name(self, name: str) -> List[Student]:
        """
        Localizar estudiantes por nombre (búsqueda parcial)
        
        SQL equivalente:
        SELECT * FROM students WHERE first_name LIKE '%name%' OR last_name LIKE '%name%'
        """
        try:
            students = self.student_dao.search_by_name(name)
            print(f"✓ Encontrados {len(students)} estudiantes con el nombre '{name}'")
            return students
        except Exception as e:
            print(f"✗ Error al buscar estudiantes: {e}")
            raise
    
    def find_student_by_email(self, email: str) -> Optional[Student]:
        """
        Localizar un estudiante por email
        
        SQL equivalente:
        SELECT * FROM students WHERE email = ?
        """
        try:
            student = self.student_dao.search_by_email(email)
            if student:
                print(f"✓ Estudiante encontrado: {student.full_name}")
            else:
                print(f"✗ Estudiante con email '{email}' no encontrado")
            return student
        except Exception as e:
            print(f"✗ Error al buscar estudiante: {e}")
            raise
    
    def find_course_by_code(self, code: str) -> Optional[Course]:
        """
        Localizar un curso por código
        
        SQL equivalente:
        SELECT * FROM courses WHERE code = ?
        """
        try:
            course = self.course_dao.search_by_code(code)
            if course:
                print(f"✓ Curso encontrado: {course.name}")
            else:
                print(f"✗ Curso con código '{code}' no encontrado")
            return course
        except Exception as e:
            print(f"✗ Error al buscar curso: {e}")
            raise
    
    def find_courses_by_name(self, name: str) -> List[Course]:
        """
        Localizar cursos por nombre (búsqueda parcial)
        
        SQL equivalente:
        SELECT * FROM courses WHERE name LIKE '%name%'
        """
        try:
            courses = self.course_dao.search_by_name(name)
            print(f"✓ Encontrados {len(courses)} cursos con el nombre '{name}'")
            return courses
        except Exception as e:
            print(f"✗ Error al buscar cursos: {e}")
            raise
    
    def find_enrollments_by_student(self, student_id: int) -> List[Enrollment]:
        """
        Localizar todas las inscripciones de un estudiante
        
        SQL equivalente:
        SELECT * FROM enrollments WHERE student_id = ?
        """
        try:
            enrollments = self.enrollment_dao.get_by_student(student_id)
            print(f"✓ Encontradas {len(enrollments)} inscripciones para el estudiante ID {student_id}")
            return enrollments
        except Exception as e:
            print(f"✗ Error al buscar inscripciones: {e}")
            raise
    
    def find_enrollments_by_course(self, course_id: int) -> List[Enrollment]:
        """
        Localizar todas las inscripciones de un curso
        
        SQL equivalente:
        SELECT * FROM enrollments WHERE course_id = ?
        """
        try:
            enrollments = self.enrollment_dao.get_by_course(course_id)
            print(f"✓ Encontradas {len(enrollments)} inscripciones para el curso ID {course_id}")
            return enrollments
        except Exception as e:
            print(f"✗ Error al buscar inscripciones: {e}")
            raise
    
    # ========================================
    # CONSULTAS AVANZADAS CON SQL
    # ========================================
    
    def get_student_transcript(self, student_id: int) -> Dict[str, Any]:
        """
        Obtener el historial académico completo de un estudiante
        
        SQL equivalente:
        SELECT s.first_name, s.last_name, c.name, c.code, c.credits, 
               e.grade, e.status, e.enrollment_date
        FROM students s
        JOIN enrollments e ON s.id = e.student_id
        JOIN courses c ON e.course_id = c.id
        WHERE s.id = ?
        """
        query = """
        SELECT 
            s.first_name,
            s.last_name,
            s.email,
            c.name as course_name,
            c.code as course_code,
            c.credits,
            e.grade,
            e.status,
            e.enrollment_date
        FROM students s
        JOIN enrollments e ON s.id = e.student_id
        JOIN courses c ON e.course_id = c.id
        WHERE s.id = ?
        ORDER BY e.enrollment_date
        """
        
        try:
            rows = self.db.execute_query(query, (student_id,))
            if not rows:
                return None
            
            # Organizar los datos
            student_info = {
                'first_name': rows[0]['first_name'],
                'last_name': rows[0]['last_name'],
                'email': rows[0]['email'],
                'courses': []
            }
            
            total_credits = 0
            total_grade_points = 0
            
            for row in rows:
                course_data = {
                    'course_name': row['course_name'],
                    'course_code': row['course_code'],
                    'credits': row['credits'],
                    'grade': row['grade'],
                    'status': row['status'],
                    'enrollment_date': row['enrollment_date']
                }
                student_info['courses'].append(course_data)
                
                # Calcular GPA
                if row['grade'] is not None and row['status'] == 'completed':
                    total_credits += row['credits']
                    total_grade_points += row['grade'] * row['credits']
            
            # Calcular GPA
            student_info['gpa'] = total_grade_points / total_credits if total_credits > 0 else 0
            student_info['total_credits'] = total_credits
            
            return student_info
            
        except Exception as e:
            print(f"✗ Error al obtener historial académico: {e}")
            raise
    
    def get_course_roster(self, course_id: int) -> Dict[str, Any]:
        """
        Obtener la lista de estudiantes inscritos en un curso
        
        SQL equivalente:
        SELECT c.name, c.code, c.instructor, s.first_name, s.last_name, 
               s.email, e.grade, e.status, e.enrollment_date
        FROM courses c
        JOIN enrollments e ON c.id = e.course_id
        JOIN students s ON e.student_id = s.id
        WHERE c.id = ?
        """
        query = """
        SELECT 
            c.name as course_name,
            c.code as course_code,
            c.instructor,
            c.capacity,
            s.first_name,
            s.last_name,
            s.email,
            e.grade,
            e.status,
            e.enrollment_date
        FROM courses c
        JOIN enrollments e ON c.id = e.course_id
        JOIN students s ON e.student_id = s.id
        WHERE c.id = ?
        ORDER BY s.last_name, s.first_name
        """
        
        try:
            rows = self.db.execute_query(query, (course_id,))
            if not rows:
                return None
            
            # Organizar los datos
            course_info = {
                'course_name': rows[0]['course_name'],
                'course_code': rows[0]['course_code'],
                'instructor': rows[0]['instructor'],
                'capacity': rows[0]['capacity'],
                'enrolled_count': len(rows),
                'students': []
            }
            
            for row in rows:
                student_data = {
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'grade': row['grade'],
                    'status': row['status'],
                    'enrollment_date': row['enrollment_date']
                }
                course_info['students'].append(student_data)
            
            return course_info
            
        except Exception as e:
            print(f"✗ Error al obtener lista de estudiantes: {e}")
            raise
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Obtener estadísticas generales del sistema
        
        Utiliza múltiples consultas SQL para generar estadísticas
        """
        stats = {}
        
        try:
            # Contar estudiantes
            stats['total_students'] = self.db.execute_scalar("SELECT COUNT(*) FROM students")
            stats['active_students'] = self.db.execute_scalar("SELECT COUNT(*) FROM students WHERE status = 'active'")
            
            # Contar cursos
            stats['total_courses'] = self.db.execute_scalar("SELECT COUNT(*) FROM courses")
            
            # Contar inscripciones
            stats['total_enrollments'] = self.db.execute_scalar("SELECT COUNT(*) FROM enrollments")
            stats['active_enrollments'] = self.db.execute_scalar("SELECT COUNT(*) FROM enrollments WHERE status = 'enrolled'")
            
            # Promedio de calificaciones
            avg_grade = self.db.execute_scalar("SELECT AVG(grade) FROM enrollments WHERE grade IS NOT NULL")
            stats['average_grade'] = round(avg_grade, 2) if avg_grade else 0
            
            # Curso más popular
            popular_course = self.db.execute_query("""
                SELECT c.name, c.code, COUNT(e.id) as enrollment_count
                FROM courses c
                LEFT JOIN enrollments e ON c.id = e.course_id
                GROUP BY c.id, c.name, c.code
                ORDER BY enrollment_count DESC
                LIMIT 1
            """)
            
            if popular_course:
                stats['most_popular_course'] = {
                    'name': popular_course[0]['name'],
                    'code': popular_course[0]['code'],
                    'enrollments': popular_course[0]['enrollment_count']
                }
            
            return stats
            
        except Exception as e:
            print(f"✗ Error al obtener estadísticas: {e}")
            raise
    
    # ========================================
    # OPERACIONES BATCH
    # ========================================
    
    def batch_update_grades(self, grade_updates: List[Tuple[int, float]]) -> int:
        """
        Actualizar múltiples calificaciones en una sola operación
        
        SQL equivalente:
        UPDATE enrollments SET grade = ? WHERE id = ?
        (ejecutado múltiples veces en una transacción)
        """
        updated_count = 0
        
        try:
            with self.db.get_cursor() as cursor:
                for enrollment_id, grade in grade_updates:
                    cursor.execute(
                        "UPDATE enrollments SET grade = ? WHERE id = ?",
                        (grade, enrollment_id)
                    )
                    if cursor.rowcount > 0:
                        updated_count += 1
            
            print(f"✓ {updated_count} calificaciones actualizadas exitosamente")
            return updated_count
            
        except Exception as e:
            print(f"✗ Error en actualización batch: {e}")
            raise
    
    def cleanup_data(self) -> Dict[str, int]:
        """
        Operación de limpieza de datos
        Elimina registros huérfanos o inconsistentes
        """
        cleanup_stats = {}
        
        try:
            # Eliminar inscripciones sin estudiante o curso válido (no debería pasar con FK)
            orphaned_enrollments = self.db.execute_non_query("""
                DELETE FROM enrollments 
                WHERE student_id NOT IN (SELECT id FROM students)
                   OR course_id NOT IN (SELECT id FROM courses)
            """)
            cleanup_stats['orphaned_enrollments_removed'] = orphaned_enrollments
            
            # Actualizar estudiantes inactivos que no tienen inscripciones recientes
            inactive_students = self.db.execute_non_query("""
                UPDATE students 
                SET status = 'inactive'
                WHERE id NOT IN (
                    SELECT DISTINCT student_id 
                    FROM enrollments 
                    WHERE enrollment_date >= date('now', '-1 year')
                )
                AND status = 'active'
            """)
            cleanup_stats['students_marked_inactive'] = inactive_students
            
            print(f"✓ Limpieza completada: {cleanup_stats}")
            return cleanup_stats
            
        except Exception as e:
            print(f"✗ Error en limpieza de datos: {e}")
            raise
