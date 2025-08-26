"""
Navegar a Través de un Conjunto de Registros

La navegación de registros permite moverse a través de un conjunto de datos
de manera secuencial, similar a como se hace con un cursor en bases de datos.
Esto es especialmente útil en interfaces de usuario donde se necesita mostrar
registros uno a la vez con botones de navegación (Primero, Anterior, Siguiente, Último).

Esta implementación proporciona funcionalidades de navegación para cualquier
conjunto de registros, manteniendo el estado actual y permitiendo operaciones
de filtrado y ordenamiento.
"""

from typing import List, Any, Optional, Callable, Dict
from enum import Enum
from datetime import datetime
import sqlite3
from .connection import DatabaseConnection
from .dao import Student, Course, Enrollment, StudentDAO, CourseDAO, EnrollmentDAO

class SortOrder(Enum):
    """Enum para definir el orden de clasificación"""
    ASC = "ASC"
    DESC = "DESC"

class NavigationDirection(Enum):
    """Enum para definir la dirección de navegación"""
    FIRST = "FIRST"
    PREVIOUS = "PREVIOUS"
    NEXT = "NEXT"
    LAST = "LAST"

class RecordSet:
    """
    Clase base para manejar conjuntos de registros con navegación
    """
    
    def __init__(self, records: List[Any] = None):
        self._records = records or []
        self._current_index = 0
        self._filter_function = None
        self._sort_key = None
        self._sort_order = SortOrder.ASC
        self._original_records = self._records.copy()
    
    @property
    def records(self) -> List[Any]:
        """Obtiene la lista actual de registros"""
        return self._records
    
    @property
    def current_index(self) -> int:
        """Obtiene el índice actual"""
        return self._current_index
    
    @property
    def current_record(self) -> Any:
        """Obtiene el registro actual"""
        if 0 <= self._current_index < len(self._records):
            return self._records[self._current_index]
        return None
    
    @property
    def is_first(self) -> bool:
        """Verifica si está en el primer registro"""
        return self._current_index == 0
    
    @property
    def is_last(self) -> bool:
        """Verifica si está en el último registro"""
        return self._current_index == len(self._records) - 1
    
    @property
    def record_count(self) -> int:
        """Obtiene el número total de registros"""
        return len(self._records)
    
    @property
    def position_info(self) -> str:
        """Obtiene información de posición como string"""
        if self.record_count == 0:
            return "No hay registros"
        return f"Registro {self._current_index + 1} de {self.record_count}"
    
    def first(self) -> Any:
        """Navega al primer registro"""
        if self._records:
            self._current_index = 0
            return self.current_record
        return None
    
    def previous(self) -> Any:
        """Navega al registro anterior"""
        if self._current_index > 0:
            self._current_index -= 1
        return self.current_record
    
    def next(self) -> Any:
        """Navega al siguiente registro"""
        if self._current_index < len(self._records) - 1:
            self._current_index += 1
        return self.current_record
    
    def last(self) -> Any:
        """Navega al último registro"""
        if self._records:
            self._current_index = len(self._records) - 1
            return self.current_record
        return None
    
    def go_to(self, index: int) -> Any:
        """Navega a un índice específico"""
        if 0 <= index < len(self._records):
            self._current_index = index
            return self.current_record
        return None
    
    def find_record(self, predicate: Callable[[Any], bool]) -> Any:
        """
        Busca el primer registro que cumple con la condición
        y navega a él
        """
        for i, record in enumerate(self._records):
            if predicate(record):
                self._current_index = i
                return record
        return None
    
    def filter(self, filter_function: Callable[[Any], bool]):
        """
        Aplica un filtro a los registros
        """
        self._filter_function = filter_function
        self._apply_filter()
        self._current_index = 0
    
    def sort(self, key_function: Callable[[Any], Any], order: SortOrder = SortOrder.ASC):
        """
        Ordena los registros según una función de clave
        """
        self._sort_key = key_function
        self._sort_order = order
        self._apply_sort()
        self._current_index = 0
    
    def clear_filter(self):
        """
        Elimina el filtro actual y restaura todos los registros
        """
        self._filter_function = None
        self._records = self._original_records.copy()
        self._apply_sort()
        self._current_index = 0
    
    def refresh(self, new_records: List[Any]):
        """
        Actualiza el conjunto de registros manteniendo filtros y orden
        """
        self._original_records = new_records.copy()
        self._records = new_records.copy()
        self._apply_filter()
        self._apply_sort()
        self._current_index = min(self._current_index, max(0, len(self._records) - 1))
    
    def _apply_filter(self):
        """Aplica el filtro actual si existe"""
        if self._filter_function:
            self._records = [r for r in self._original_records if self._filter_function(r)]
        else:
            self._records = self._original_records.copy()
    
    def _apply_sort(self):
        """Aplica el ordenamiento actual si existe"""
        if self._sort_key:
            self._records.sort(
                key=self._sort_key,
                reverse=(self._sort_order == SortOrder.DESC)
            )

class DataNavigator:
    """
    Navegador de datos que proporciona funcionalidades de navegación
    para diferentes tipos de registros del sistema educativo
    """
    
    def __init__(self):
        self.db = DatabaseConnection()
        self.student_dao = StudentDAO()
        self.course_dao = CourseDAO()
        self.enrollment_dao = EnrollmentDAO()
        
        # Recordsets para cada tipo de entidad
        self.student_recordset = RecordSet()
        self.course_recordset = RecordSet()
        self.enrollment_recordset = RecordSet()
    
    # ========================================
    # NAVEGACIÓN DE ESTUDIANTES
    # ========================================
    
    def load_students(self, filter_criteria: str = None) -> RecordSet:
        """
        Carga todos los estudiantes en el recordset de navegación
        """
        try:
            if filter_criteria:
                if filter_criteria.lower() == "active":
                    students = self.student_dao.get_by_status("active")
                elif filter_criteria.lower() == "inactive":
                    students = self.student_dao.get_by_status("inactive")
                elif "@" in filter_criteria:  # Búsqueda por email
                    student = self.student_dao.search_by_email(filter_criteria)
                    students = [student] if student else []
                else:  # Búsqueda por nombre
                    students = self.student_dao.search_by_name(filter_criteria)
            else:
                students = self.student_dao.get_all()
            
            self.student_recordset.refresh(students)
            print(f"✓ Cargados {len(students)} estudiantes")
            return self.student_recordset
            
        except Exception as e:
            print(f"✗ Error al cargar estudiantes: {e}")
            return self.student_recordset
    
    def navigate_students(self, direction: NavigationDirection) -> Optional[Student]:
        """
        Navega por los estudiantes según la dirección especificada
        """
        if direction == NavigationDirection.FIRST:
            return self.student_recordset.first()
        elif direction == NavigationDirection.PREVIOUS:
            return self.student_recordset.previous()
        elif direction == NavigationDirection.NEXT:
            return self.student_recordset.next()
        elif direction == NavigationDirection.LAST:
            return self.student_recordset.last()
        return self.student_recordset.current_record
    
    def sort_students(self, sort_by: str, order: SortOrder = SortOrder.ASC):
        """
        Ordena los estudiantes por el campo especificado
        """
        sort_functions = {
            'name': lambda s: f"{s.last_name} {s.first_name}",
            'email': lambda s: s.email,
            'status': lambda s: s.status,
            'enrollment_date': lambda s: s.enrollment_date or ""
        }
        
        if sort_by in sort_functions:
            self.student_recordset.sort(sort_functions[sort_by], order)
            print(f"✓ Estudiantes ordenados por {sort_by}")
        else:
            print(f"✗ Campo de ordenamiento inválido: {sort_by}")
    
    # ========================================
    # NAVEGACIÓN DE CURSOS
    # ========================================
    
    def load_courses(self, filter_criteria: str = None) -> RecordSet:
        """
        Carga todos los cursos en el recordset de navegación
        """
        try:
            if filter_criteria:
                # Puede ser búsqueda por nombre, código o semestre
                if filter_criteria.startswith("20"):  # Probablemente un semestre
                    courses = self.course_dao.get_by_semester(filter_criteria)
                else:  # Búsqueda por nombre o código
                    courses_by_name = self.course_dao.search_by_name(filter_criteria)
                    course_by_code = self.course_dao.search_by_code(filter_criteria)
                    courses = courses_by_name
                    if course_by_code and course_by_code not in courses:
                        courses.append(course_by_code)
            else:
                courses = self.course_dao.get_all()
            
            self.course_recordset.refresh(courses)
            print(f"✓ Cargados {len(courses)} cursos")
            return self.course_recordset
            
        except Exception as e:
            print(f"✗ Error al cargar cursos: {e}")
            return self.course_recordset
    
    def navigate_courses(self, direction: NavigationDirection) -> Optional[Course]:
        """
        Navega por los cursos según la dirección especificada
        """
        if direction == NavigationDirection.FIRST:
            return self.course_recordset.first()
        elif direction == NavigationDirection.PREVIOUS:
            return self.course_recordset.previous()
        elif direction == NavigationDirection.NEXT:
            return self.course_recordset.next()
        elif direction == NavigationDirection.LAST:
            return self.course_recordset.last()
        return self.course_recordset.current_record
    
    def sort_courses(self, sort_by: str, order: SortOrder = SortOrder.ASC):
        """
        Ordena los cursos por el campo especificado
        """
        sort_functions = {
            'name': lambda c: c.name,
            'code': lambda c: c.code,
            'credits': lambda c: c.credits,
            'instructor': lambda c: c.instructor or "",
            'semester': lambda c: c.semester or ""
        }
        
        if sort_by in sort_functions:
            self.course_recordset.sort(sort_functions[sort_by], order)
            print(f"✓ Cursos ordenados por {sort_by}")
        else:
            print(f"✗ Campo de ordenamiento inválido: {sort_by}")
    
    # ========================================
    # NAVEGACIÓN DE INSCRIPCIONES
    # ========================================
    
    def load_enrollments(self, student_id: int = None, course_id: int = None) -> RecordSet:
        """
        Carga las inscripciones en el recordset de navegación
        """
        try:
            if student_id:
                enrollments = self.enrollment_dao.get_by_student(student_id)
            elif course_id:
                enrollments = self.enrollment_dao.get_by_course(course_id)
            else:
                enrollments = self.enrollment_dao.get_all()
            
            self.enrollment_recordset.refresh(enrollments)
            print(f"✓ Cargadas {len(enrollments)} inscripciones")
            return self.enrollment_recordset
            
        except Exception as e:
            print(f"✗ Error al cargar inscripciones: {e}")
            return self.enrollment_recordset
    
    def navigate_enrollments(self, direction: NavigationDirection) -> Optional[Enrollment]:
        """
        Navega por las inscripciones según la dirección especificada
        """
        if direction == NavigationDirection.FIRST:
            return self.enrollment_recordset.first()
        elif direction == NavigationDirection.PREVIOUS:
            return self.enrollment_recordset.previous()
        elif direction == NavigationDirection.NEXT:
            return self.enrollment_recordset.next()
        elif direction == NavigationDirection.LAST:
            return self.enrollment_recordset.last()
        return self.enrollment_recordset.current_record
    
    # ========================================
    # BÚSQUEDA Y FILTRADO AVANZADO
    # ========================================
    
    def search_students_advanced(self, criteria: Dict[str, Any]) -> List[Student]:
        """
        Búsqueda avanzada de estudiantes con múltiples criterios
        """
        query_parts = ["SELECT * FROM students WHERE 1=1"]
        params = []
        
        if criteria.get('name'):
            query_parts.append("AND (first_name LIKE ? OR last_name LIKE ?)")
            name_pattern = f"%{criteria['name']}%"
            params.extend([name_pattern, name_pattern])
        
        if criteria.get('email'):
            query_parts.append("AND email LIKE ?")
            params.append(f"%{criteria['email']}%")
        
        if criteria.get('status'):
            query_parts.append("AND status = ?")
            params.append(criteria['status'])
        
        if criteria.get('phone'):
            query_parts.append("AND phone LIKE ?")
            params.append(f"%{criteria['phone']}%")
        
        query_parts.append("ORDER BY last_name, first_name")
        query = " ".join(query_parts)
        
        try:
            rows = self.db.execute_query(query, tuple(params))
            students = [Student(**dict(row)) for row in rows]
            print(f"✓ Búsqueda avanzada encontró {len(students)} estudiantes")
            return students
        except Exception as e:
            print(f"✗ Error en búsqueda avanzada: {e}")
            return []
    
    def get_student_statistics(self, student_id: int) -> Dict[str, Any]:
        """
        Obtiene estadísticas detalladas de un estudiante específico
        """
        query = """
        SELECT 
            s.first_name,
            s.last_name,
            s.email,
            s.status,
            COUNT(e.id) as total_enrollments,
            COUNT(CASE WHEN e.status = 'completed' THEN 1 END) as completed_courses,
            AVG(CASE WHEN e.grade IS NOT NULL THEN e.grade END) as avg_grade,
            SUM(CASE WHEN e.status = 'completed' THEN c.credits ELSE 0 END) as total_credits
        FROM students s
        LEFT JOIN enrollments e ON s.id = e.student_id
        LEFT JOIN courses c ON e.course_id = c.id
        WHERE s.id = ?
        GROUP BY s.id, s.first_name, s.last_name, s.email, s.status
        """
        
        try:
            rows = self.db.execute_query(query, (student_id,))
            if rows:
                stats = dict(rows[0])
                stats['avg_grade'] = round(stats['avg_grade'], 2) if stats['avg_grade'] else 0
                return stats
            return {}
        except Exception as e:
            print(f"✗ Error al obtener estadísticas del estudiante: {e}")
            return {}
    
    # ========================================
    # UTILIDADES DE NAVEGACIÓN
    # ========================================
    
    def create_navigation_info(self, recordset: RecordSet) -> Dict[str, Any]:
        """
        Crea información de navegación para la interfaz de usuario
        """
        return {
            'current_index': recordset.current_index,
            'total_records': recordset.record_count,
            'position_text': recordset.position_info,
            'is_first': recordset.is_first,
            'is_last': recordset.is_last,
            'has_records': recordset.record_count > 0,
            'can_navigate_previous': not recordset.is_first and recordset.record_count > 0,
            'can_navigate_next': not recordset.is_last and recordset.record_count > 0
        }
    
    def bookmark_position(self, recordset_type: str) -> Dict[str, Any]:
        """
        Guarda la posición actual como un marcador
        """
        recordset_map = {
            'students': self.student_recordset,
            'courses': self.course_recordset,
            'enrollments': self.enrollment_recordset
        }
        
        recordset = recordset_map.get(recordset_type)
        if recordset:
            return {
                'type': recordset_type,
                'index': recordset.current_index,
                'record_id': getattr(recordset.current_record, 'id', None) if recordset.current_record else None,
                'timestamp': str(datetime.now())
            }
        return {}
    
    def restore_bookmark(self, bookmark: Dict[str, Any]) -> bool:
        """
        Restaura una posición desde un marcador
        """
        recordset_map = {
            'students': self.student_recordset,
            'courses': self.course_recordset,
            'enrollments': self.enrollment_recordset
        }
        
        recordset = recordset_map.get(bookmark.get('type'))
        if recordset and 'index' in bookmark:
            record = recordset.go_to(bookmark['index'])
            return record is not None
        return False
    
    def get_navigation_summary(self) -> Dict[str, Any]:
        """
        Obtiene un resumen del estado de navegación de todos los recordsets
        """
        return {
            'students': {
                'loaded': self.student_recordset.record_count,
                'current_position': self.student_recordset.current_index + 1 if self.student_recordset.record_count > 0 else 0,
                'current_record': str(self.student_recordset.current_record) if self.student_recordset.current_record else None
            },
            'courses': {
                'loaded': self.course_recordset.record_count,
                'current_position': self.course_recordset.current_index + 1 if self.course_recordset.record_count > 0 else 0,
                'current_record': str(self.course_recordset.current_record) if self.course_recordset.current_record else None
            },
            'enrollments': {
                'loaded': self.enrollment_recordset.record_count,
                'current_position': self.enrollment_recordset.current_index + 1 if self.enrollment_recordset.record_count > 0 else 0,
                'current_record': str(self.enrollment_recordset.current_record) if self.enrollment_recordset.current_record else None
            }
        }
