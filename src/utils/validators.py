"""
Funciones de validación para la aplicación
"""

import re

def validate_email(email):
    """
    Valida el formato de un email
    
    Args:
        email (str): Email a validar
        
    Returns:
        bool: True si el email es válido, False en caso contrario
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_name(name):
    """
    Valida que el nombre solo contenga letras y espacios
    
    Args:
        name (str): Nombre a validar
        
    Returns:
        bool: True si el nombre es válido, False en caso contrario
    """
    pattern = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$'
    return re.match(pattern, name) is not None and len(name.strip()) > 0

def validate_age(age):
    """
    Valida que la edad sea un número entero válido
    
    Args:
        age (str): Edad a validar
        
    Returns:
        bool: True si la edad es válida, False en caso contrario
    """
    try:
        age_int = int(age)
        return 1 <= age_int <= 120
    except ValueError:
        return False

def validate_required_field(field):
    """
    Valida que un campo requerido no esté vacío
    
    Args:
        field (str): Campo a validar
        
    Returns:
        bool: True si el campo no está vacío, False en caso contrario
    """
    return field is not None and len(field.strip()) > 0
