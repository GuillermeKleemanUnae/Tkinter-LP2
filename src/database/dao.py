"""
Objetos de Acceso a Datos (DAO - Data Access Objects)

Los DAO son objetos que proporcionan una interfaz abstracta para algún tipo de base de datos
u otro mecanismo de persistencia. Los DAO mapean las llamadas de aplicación a la capa de
persistencia y proporcionan operaciones específicas de datos sin exponer detalles de la BD.

Ventajas de usar DAO:
1. Separación de responsabilidades
2. Facilita el mantenimiento del código
3. Permite cambiar la implementación de la BD sin afectar la lógica de negocio
4. Facilita las pruebas unitarias
"""

from typing import List, Optional, Dict, Any
from datetime import datetime, date
import sqlite3
from .connection import DatabaseConnection

class BaseDAO:
    """Clase base para todos los DAO"""
    
    def __init__(self):
        self.db = DatabaseConnection()
    
    def _dict_to_object(self, row: sqlite3.Row, obj_class) -> Any:
        """Convierte una fila de BD a un objeto"""
        if row:
            return obj_class(**dict(row))
        return None
    
    def _log_operation(self, table_name: str, operation: str, record_id: int = None, 
                      old_values: str = None, new_values: str = None):
        """Registra la operación en el log de auditoría"""
        try:
            self.db.execute_non_query(
                """INSERT INTO audit_log (table_name, operation, record_id, old_values, new_values, user_id) 
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (table_name, operation, record_id, old_values, new_values, "system")
            )
        except sqlite3.Error:
            pass  # No fallar si no se puede registrar el log

class Student:
    """Modelo de datos para Estudiante"""
    
    def __init__(self, id: int = None, first_name: str = "", last_name: str = "", 
                 email: str = "", phone: str = "", birth_date: str = None, 
                 enrollment_date: str = None, status: str = "active",
                 created_at: str = None, updated_at: str = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.birth_date = birth_date
        self.enrollment_date = enrollment_date
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
    
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"Student({self.id}, {self.full_name}, {self.email})"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'birth_date': self.birth_date,
            'enrollment_date': self.enrollment_date,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

class Course:
    """Modelo de datos para Curso"""
    
    def __init__(self, id: int = None, name: str = "", code: str = "", 
                 description: str = "", credits: int = 3, semester: str = "",
                 instructor: str = "", capacity: int = 30,
                 created_at: str = None, updated_at: str = None):
        self.id = id
        self.name = name
        self.code = code
        self.description = description
        self.credits = credits
        self.semester = semester
        self.instructor = instructor
        self.capacity = capacity
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __str__(self):
        return f"Course({self.id}, {self.code}, {self.name})"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'description': self.description,
            'credits': self.credits,
            'semester': self.semester,
            'instructor': self.instructor,
            'capacity': self.capacity,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

class Enrollment:
    """Modelo de datos para Inscripción"""
    
    def __init__(self, id: int = None, student_id: int = None, course_id: int = None,
                 enrollment_date: str = None, grade: float = None, status: str = "enrolled",
                 created_at: str = None, updated_at: str = None):
        self.id = id
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date
        self.grade = grade
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __str__(self):
        return f"Enrollment({self.id}, Student:{self.student_id}, Course:{self.course_id})"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'enrollment_date': self.enrollment_date,
            'grade': self.grade,
            'status': self.status,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

class StudentDAO(BaseDAO):
    """DAO para operaciones con Estudiantes"""
    
    def create(self, student: Student) -> int:
        """Crea un nuevo estudiante (CREATE)"""
        query = """
        INSERT INTO students (first_name, last_name, email, phone, birth_date, status) 
        VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            with self.db.get_cursor() as cursor:
                cursor.execute(query, (
                    student.first_name, student.last_name, student.email,
                    student.phone, student.birth_date, student.status
                ))
                student_id = cursor.lastrowid
                self._log_operation("students", "CREATE", student_id, None, str(student.to_dict()))
                return student_id
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed: students.email" in str(e):
                raise ValueError("El email ya existe en el sistema")
            raise
    
    def get_by_id(self, student_id: int) -> Optional[Student]:
        """Obtiene un estudiante por ID (READ)"""
        query = "SELECT * FROM students WHERE id = ?"
        rows = self.db.execute_query(query, (student_id,))
        return self._dict_to_object(rows[0] if rows else None, Student)
    
    def get_all(self) -> List[Student]:
        """Obtiene todos los estudiantes (READ)"""
        query = "SELECT * FROM students ORDER BY last_name, first_name"
        rows = self.db.execute_query(query)
        return [self._dict_to_object(row, Student) for row in rows]
    
    def update(self, student: Student) -> bool:
        """Actualiza un estudiante (UPDATE)"""
        old_student = self.get_by_id(student.id)
        if not old_student:
            return False
        
        query = """
        UPDATE students 
        SET first_name = ?, last_name = ?, email = ?, phone = ?, 
            birth_date = ?, status = ?
        WHERE id = ?
        """
        try:
            affected = self.db.execute_non_query(query, (
                student.first_name, student.last_name, student.email,
                student.phone, student.birth_date, student.status, student.id
            ))
            
            if affected > 0:
                self._log_operation("students", "UPDATE", student.id, 
                                  str(old_student.to_dict()), str(student.to_dict()))
            return affected > 0
            
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed: students.email" in str(e):
                raise ValueError("El email ya existe en el sistema")
            raise
    
    def delete(self, student_id: int) -> bool:
        """Elimina un estudiante (DELETE)"""
        old_student = self.get_by_id(student_id)
        if not old_student:
            return False
        
        query = "DELETE FROM students WHERE id = ?"
        affected = self.db.execute_non_query(query, (student_id,))
        
        if affected > 0:
            self._log_operation("students", "DELETE", student_id, str(old_student.to_dict()), None)
        return affected > 0
    
    def search_by_name(self, name: str) -> List[Student]:
        """Busca estudiantes por nombre (SELECT ... WHERE)"""
        query = """
        SELECT * FROM students 
        WHERE first_name LIKE ? OR last_name LIKE ?
        ORDER BY last_name, first_name
        """
        name_pattern = f"%{name}%"
        rows = self.db.execute_query(query, (name_pattern, name_pattern))
        return [self._dict_to_object(row, Student) for row in rows]
    
    def search_by_email(self, email: str) -> Optional[Student]:
        """Busca un estudiante por email (SELECT ... WHERE)"""
        query = "SELECT * FROM students WHERE email = ?"
        rows = self.db.execute_query(query, (email,))
        return self._dict_to_object(rows[0] if rows else None, Student)
    
    def get_by_status(self, status: str) -> List[Student]:
        """Obtiene estudiantes por estado (SELECT ... WHERE)"""
        query = "SELECT * FROM students WHERE status = ? ORDER BY last_name, first_name"
        rows = self.db.execute_query(query, (status,))
        return [self._dict_to_object(row, Student) for row in rows]

class CourseDAO(BaseDAO):
    """DAO para operaciones con Cursos"""
    
    def create(self, course: Course) -> int:
        """Crea un nuevo curso (CREATE)"""
        query = """
        INSERT INTO courses (name, code, description, credits, semester, instructor, capacity) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        try:
            with self.db.get_cursor() as cursor:
                cursor.execute(query, (
                    course.name, course.code, course.description, course.credits,
                    course.semester, course.instructor, course.capacity
                ))
                course_id = cursor.lastrowid
                self._log_operation("courses", "CREATE", course_id, None, str(course.to_dict()))
                return course_id
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed: courses.code" in str(e):
                raise ValueError("El código del curso ya existe en el sistema")
            raise
    
    def get_by_id(self, course_id: int) -> Optional[Course]:
        """Obtiene un curso por ID (READ)"""
        query = "SELECT * FROM courses WHERE id = ?"
        rows = self.db.execute_query(query, (course_id,))
        return self._dict_to_object(rows[0] if rows else None, Course)
    
    def get_all(self) -> List[Course]:
        """Obtiene todos los cursos (READ)"""
        query = "SELECT * FROM courses ORDER BY name"
        rows = self.db.execute_query(query)
        return [self._dict_to_object(row, Course) for row in rows]
    
    def update(self, course: Course) -> bool:
        """Actualiza un curso (UPDATE)"""
        old_course = self.get_by_id(course.id)
        if not old_course:
            return False
        
        query = """
        UPDATE courses 
        SET name = ?, code = ?, description = ?, credits = ?, 
            semester = ?, instructor = ?, capacity = ?
        WHERE id = ?
        """
        try:
            affected = self.db.execute_non_query(query, (
                course.name, course.code, course.description, course.credits,
                course.semester, course.instructor, course.capacity, course.id
            ))
            
            if affected > 0:
                self._log_operation("courses", "UPDATE", course.id,
                                  str(old_course.to_dict()), str(course.to_dict()))
            return affected > 0
            
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed: courses.code" in str(e):
                raise ValueError("El código del curso ya existe en el sistema")
            raise
    
    def delete(self, course_id: int) -> bool:
        """Elimina un curso (DELETE)"""
        old_course = self.get_by_id(course_id)
        if not old_course:
            return False
        
        query = "DELETE FROM courses WHERE id = ?"
        affected = self.db.execute_non_query(query, (course_id,))
        
        if affected > 0:
            self._log_operation("courses", "DELETE", course_id, str(old_course.to_dict()), None)
        return affected > 0
    
    def search_by_code(self, code: str) -> Optional[Course]:
        """Busca un curso por código (SELECT ... WHERE)"""
        query = "SELECT * FROM courses WHERE code = ?"
        rows = self.db.execute_query(query, (code,))
        return self._dict_to_object(rows[0] if rows else None, Course)
    
    def search_by_name(self, name: str) -> List[Course]:
        """Busca cursos por nombre (SELECT ... WHERE)"""
        query = "SELECT * FROM courses WHERE name LIKE ? ORDER BY name"
        name_pattern = f"%{name}%"
        rows = self.db.execute_query(query, (name_pattern,))
        return [self._dict_to_object(row, Course) for row in rows]
    
    def get_by_semester(self, semester: str) -> List[Course]:
        """Obtiene cursos por semestre (SELECT ... WHERE)"""
        query = "SELECT * FROM courses WHERE semester = ? ORDER BY name"
        rows = self.db.execute_query(query, (semester,))
        return [self._dict_to_object(row, Course) for row in rows]

class EnrollmentDAO(BaseDAO):
    """DAO para operaciones con Inscripciones"""
    
    def create(self, enrollment: Enrollment) -> int:
        """Crea una nueva inscripción (CREATE)"""
        query = """
        INSERT INTO enrollments (student_id, course_id, grade, status) 
        VALUES (?, ?, ?, ?)
        """
        try:
            with self.db.get_cursor() as cursor:
                cursor.execute(query, (
                    enrollment.student_id, enrollment.course_id, 
                    enrollment.grade, enrollment.status
                ))
                enrollment_id = cursor.lastrowid
                self._log_operation("enrollments", "CREATE", enrollment_id, None, str(enrollment.to_dict()))
                return enrollment_id
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed: enrollments.student_id, enrollments.course_id" in str(e):
                raise ValueError("El estudiante ya está inscrito en este curso")
            elif "FOREIGN KEY constraint failed" in str(e):
                raise ValueError("Estudiante o curso no válido")
            raise
    
    def get_by_id(self, enrollment_id: int) -> Optional[Enrollment]:
        """Obtiene una inscripción por ID (READ)"""
        query = "SELECT * FROM enrollments WHERE id = ?"
        rows = self.db.execute_query(query, (enrollment_id,))
        return self._dict_to_object(rows[0] if rows else None, Enrollment)
    
    def get_all(self) -> List[Enrollment]:
        """Obtiene todas las inscripciones (READ)"""
        query = "SELECT * FROM enrollments ORDER BY enrollment_date DESC"
        rows = self.db.execute_query(query)
        return [self._dict_to_object(row, Enrollment) for row in rows]
    
    def update(self, enrollment: Enrollment) -> bool:
        """Actualiza una inscripción (UPDATE)"""
        old_enrollment = self.get_by_id(enrollment.id)
        if not old_enrollment:
            return False
        
        query = """
        UPDATE enrollments 
        SET student_id = ?, course_id = ?, grade = ?, status = ?
        WHERE id = ?
        """
        try:
            affected = self.db.execute_non_query(query, (
                enrollment.student_id, enrollment.course_id, 
                enrollment.grade, enrollment.status, enrollment.id
            ))
            
            if affected > 0:
                self._log_operation("enrollments", "UPDATE", enrollment.id,
                                  str(old_enrollment.to_dict()), str(enrollment.to_dict()))
            return affected > 0
            
        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed" in str(e):
                raise ValueError("El estudiante ya está inscrito en este curso")
            elif "FOREIGN KEY constraint failed" in str(e):
                raise ValueError("Estudiante o curso no válido")
            raise
    
    def delete(self, enrollment_id: int) -> bool:
        """Elimina una inscripción (DELETE)"""
        old_enrollment = self.get_by_id(enrollment_id)
        if not old_enrollment:
            return False
        
        query = "DELETE FROM enrollments WHERE id = ?"
        affected = self.db.execute_non_query(query, (enrollment_id,))
        
        if affected > 0:
            self._log_operation("enrollments", "DELETE", enrollment_id, str(old_enrollment.to_dict()), None)
        return affected > 0
    
    def get_by_student(self, student_id: int) -> List[Enrollment]:
        """Obtiene inscripciones de un estudiante (SELECT ... WHERE)"""
        query = "SELECT * FROM enrollments WHERE student_id = ? ORDER BY enrollment_date DESC"
        rows = self.db.execute_query(query, (student_id,))
        return [self._dict_to_object(row, Enrollment) for row in rows]
    
    def get_by_course(self, course_id: int) -> List[Enrollment]:
        """Obtiene inscripciones de un curso (SELECT ... WHERE)"""
        query = "SELECT * FROM enrollments WHERE course_id = ? ORDER BY enrollment_date DESC"
        rows = self.db.execute_query(query, (course_id,))
        return [self._dict_to_object(row, Enrollment) for row in rows]
    
    def get_enrollment_details(self) -> List[Dict[str, Any]]:
        """Obtiene detalles completos de inscripciones con JOIN"""
        query = """
        SELECT 
            e.id as enrollment_id,
            e.enrollment_date,
            e.grade,
            e.status as enrollment_status,
            s.id as student_id,
            s.first_name,
            s.last_name,
            s.email,
            c.id as course_id,
            c.name as course_name,
            c.code as course_code,
            c.credits,
            c.instructor
        FROM enrollments e
        JOIN students s ON e.student_id = s.id
        JOIN courses c ON e.course_id = c.id
        ORDER BY e.enrollment_date DESC
        """
        rows = self.db.execute_query(query)
        return [dict(row) for row in rows]
