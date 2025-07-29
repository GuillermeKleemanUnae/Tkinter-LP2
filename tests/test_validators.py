"""
Pruebas unitarias para las funciones de validación
"""

import unittest
import sys
import os

# Agregar el directorio raíz al path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils.validators import validate_email, validate_name, validate_age, validate_required_field

class TestValidators(unittest.TestCase):
    """
    Clase para probar las funciones de validación
    """
    
    def test_validate_email_valid(self):
        """
        Prueba emails válidos
        """
        valid_emails = [
            "test@example.com",
            "user.name@domain.org",
            "user+tag@example.co.uk",
            "123@number.com"
        ]
        
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(validate_email(email))
                
    def test_validate_email_invalid(self):
        """
        Prueba emails inválidos
        """
        invalid_emails = [
            "invalidemail",
            "@example.com",
            "user@",
            "user@.com",
            "user@domain",
            "",
            "user space@example.com"
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(validate_email(email))
                
    def test_validate_name_valid(self):
        """
        Prueba nombres válidos
        """
        valid_names = [
            "Juan Pérez",
            "María García",
            "José Luis",
            "Ana",
            "Carlos Alberto Rodríguez"
        ]
        
        for name in valid_names:
            with self.subTest(name=name):
                self.assertTrue(validate_name(name))
                
    def test_validate_name_invalid(self):
        """
        Prueba nombres inválidos
        """
        invalid_names = [
            "Juan123",
            "María@García",
            "José-Luis",
            "",
            "   ",
            "Juan_Pérez"
        ]
        
        for name in invalid_names:
            with self.subTest(name=name):
                self.assertFalse(validate_name(name))
                
    def test_validate_age_valid(self):
        """
        Prueba edades válidas
        """
        valid_ages = ["18", "25", "1", "120", "50"]
        
        for age in valid_ages:
            with self.subTest(age=age):
                self.assertTrue(validate_age(age))
                
    def test_validate_age_invalid(self):
        """
        Prueba edades inválidas
        """
        invalid_ages = ["0", "121", "-5", "abc", "", "25.5"]
        
        for age in invalid_ages:
            with self.subTest(age=age):
                self.assertFalse(validate_age(age))
                
    def test_validate_required_field_valid(self):
        """
        Prueba campos requeridos válidos
        """
        valid_fields = ["texto", "123", "a", "campo con espacios"]
        
        for field in valid_fields:
            with self.subTest(field=field):
                self.assertTrue(validate_required_field(field))
                
    def test_validate_required_field_invalid(self):
        """
        Prueba campos requeridos inválidos
        """
        invalid_fields = ["", "   ", None]
        
        for field in invalid_fields:
            with self.subTest(field=field):
                self.assertFalse(validate_required_field(field))

if __name__ == '__main__':
    unittest.main()
