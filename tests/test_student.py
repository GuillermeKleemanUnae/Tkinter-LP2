"""
Pruebas unitarias para el modelo Student
"""

import unittest
import sys
import os

# Agregar el directorio raíz al path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models.student import Student

class TestStudent(unittest.TestCase):
    """
    Clase para probar el modelo Student
    """
    
    def setUp(self):
        """
        Configuración inicial para cada prueba
        """
        # Resetear el contador de IDs
        Student._id_counter = 1
        
    def test_student_creation(self):
        """
        Prueba la creación básica de un estudiante
        """
        student = Student("Juan Pérez", "juan@example.com", 20, "Programación II")
        
        self.assertEqual(student.name, "Juan Pérez")
        self.assertEqual(student.email, "juan@example.com")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.course, "Programación II")
        self.assertEqual(student.student_id, 1)
        
    def test_student_id_increment(self):
        """
        Prueba que los IDs se incrementen correctamente
        """
        student1 = Student("Juan", "juan@example.com", 20, "Curso A")
        student2 = Student("María", "maria@example.com", 21, "Curso B")
        
        self.assertEqual(student1.student_id, 1)
        self.assertEqual(student2.student_id, 2)
        
    def test_student_str_representation(self):
        """
        Prueba la representación en string del estudiante
        """
        student = Student("Ana García", "ana@example.com", 19, "Base de Datos")
        expected = "ID: 1, Nombre: Ana García, Email: ana@example.com, Edad: 19, Curso: Base de Datos"
        self.assertEqual(str(student), expected)
        
    def test_student_to_dict(self):
        """
        Prueba la conversión a diccionario
        """
        student = Student("Carlos López", "carlos@example.com", 22, "Algoritmos")
        expected_dict = {
            'id': 1,
            'name': 'Carlos López',
            'email': 'carlos@example.com',
            'age': 22,
            'course': 'Algoritmos'
        }
        self.assertEqual(student.to_dict(), expected_dict)
        
    def test_student_from_dict(self):
        """
        Prueba la creación desde diccionario
        """
        data = {
            'id': 5,
            'name': 'Laura Martín',
            'email': 'laura@example.com',
            'age': 23,
            'course': 'Estructuras de Datos'
        }
        student = Student.from_dict(data)
        
        self.assertEqual(student.student_id, 5)
        self.assertEqual(student.name, 'Laura Martín')
        self.assertEqual(student.email, 'laura@example.com')
        self.assertEqual(student.age, 23)
        self.assertEqual(student.course, 'Estructuras de Datos')

if __name__ == '__main__':
    unittest.main()
