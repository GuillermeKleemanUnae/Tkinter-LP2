#!/usr/bin/env python3
"""
Inicialización del paquete components
===================================

Este archivo permite que el directorio components sea
tratado como un paquete de Python.
"""

from .student_form import StudentForm
from .student_list import StudentList
from .config_panel import ConfigurationPanel

__all__ = ['StudentForm', 'StudentList', 'ConfigurationPanel']
