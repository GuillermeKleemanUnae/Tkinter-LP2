#!/usr/bin/env python3
"""
Componente de Formulario de Estudiante
====================================

Este módulo contiene la clase StudentForm que maneja
el formulario de entrada de datos del estudiante.

Incluye:
- Campos de entrada (Entry widgets)
- Validaciones en tiempo real
- Combobox para selección de cursos
- Información personal con radiobuttons

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox
from ...utils.validators import validate_name, validate_email


class StudentForm:
    """
    Clase que maneja el formulario de entrada de datos del estudiante
    """
    
    def __init__(self, parent, on_student_added=None):
        """
        Inicializa el formulario de estudiante
        
        Args:
            parent: Widget padre donde se colocará el formulario
            on_student_added: Callback que se ejecuta cuando se agrega un estudiante
        """
        self.parent = parent
        self.on_student_added = on_student_added
        self.init_variables()
        self.create_form()
        
    def init_variables(self):
        """
        Inicializa las variables de control del formulario
        """
        # Variables para Entry widgets
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.course_var = tk.StringVar()
        
        # Variables para información personal
        self.gender_var = tk.StringVar(value="no_especifica")
        self.status_var = tk.StringVar(value="activo")
        
    def create_form(self):
        """
        Crea la interfaz del formulario
        """
        # Frame contenedor principal
        self.form_frame = tk.LabelFrame(
            self.parent,
            text="📝 Información del Estudiante",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        self.form_frame.pack(fill='x', pady=(0, 10))
        
        self.create_basic_fields()
        self.create_personal_info()
        
    def create_basic_fields(self):
        """
        Crea los campos básicos del formulario
        """
        # Campo Nombre
        tk.Label(
            self.form_frame,
            text="Nombre completo:",
            font=("Arial", 10, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).grid(row=0, column=0, sticky='w', pady=(0, 5))
        
        self.name_entry = tk.Entry(
            self.form_frame,
            textvariable=self.name_var,
            font=("Arial", 11),
            width=25,
            borderwidth=2,
            relief='sunken',
            bg='#3C3C3C',
            fg='#FFFFFF',
            insertbackground='#FFFFFF',
            selectbackground='#0078D4',
            selectforeground='#FFFFFF'
        )
        self.name_entry.grid(row=0, column=1, sticky='ew', pady=(0, 5), padx=(10, 0))
        
        # Campo Email
        tk.Label(
            self.form_frame,
            text="Correo electrónico:",
            font=("Arial", 10, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).grid(row=1, column=0, sticky='w', pady=(0, 5))
        
        self.email_entry = tk.Entry(
            self.form_frame,
            textvariable=self.email_var,
            font=("Arial", 11),
            width=25,
            borderwidth=2,
            relief='sunken',
            bg='#3C3C3C',
            fg='#FFFFFF',
            insertbackground='#FFFFFF',
            selectbackground='#0078D4',
            selectforeground='#FFFFFF'
        )
        self.email_entry.grid(row=1, column=1, sticky='ew', pady=(0, 5), padx=(10, 0))
        
        # Campo Edad
        tk.Label(
            self.form_frame,
            text="Edad:",
            font=("Arial", 10, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).grid(row=2, column=0, sticky='w', pady=(0, 5))
        
        # Registrar función de validación
        validate_age_cmd = self.form_frame.register(self.validate_age_input)
        
        self.age_entry = tk.Entry(
            self.form_frame,
            textvariable=self.age_var,
            font=("Arial", 11),
            width=25,
            borderwidth=2,
            relief='sunken',
            bg='#3C3C3C',
            fg='#FFFFFF',
            insertbackground='#FFFFFF',
            selectbackground='#0078D4',
            selectforeground='#FFFFFF',
            validate='key',
            validatecommand=(validate_age_cmd, '%P')
        )
        self.age_entry.grid(row=2, column=1, sticky='ew', pady=(0, 5), padx=(10, 0))
        
        # Campo Curso - Combobox
        tk.Label(
            self.form_frame,
            text="Curso:",
            font=("Arial", 10, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).grid(row=3, column=0, sticky='w', pady=(0, 5))
        
        self.course_combo = ttk.Combobox(
            self.form_frame,
            textvariable=self.course_var,
            font=("Arial", 11),
            width=23,
            state="readonly",
            values=[
                "Programación I - Fundamentos",
                "Programación II - Estructuras",
                "Base de Datos - Diseño y Consultas",
                "Algoritmos y Complejidad",
                "Desarrollo Web Frontend",
                "Desarrollo Web Backend",
                "Ingeniería de Software",
                "Sistemas Operativos",
                "Redes de Computadoras",
                "Inteligencia Artificial"
            ]
        )
        self.course_combo.grid(row=3, column=1, sticky='ew', pady=(0, 5), padx=(10, 0))
        self.course_combo.set("Seleccionar curso...")
        
        # Configurar expansión
        self.form_frame.grid_columnconfigure(1, weight=1)
        
    def create_personal_info(self):
        """
        Crea la sección de información personal
        """
        # Frame para información personal
        personal_frame = tk.LabelFrame(
            self.form_frame,
            text="👤 Información Personal",
            font=("Arial", 10, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=5
        )
        personal_frame.grid(row=4, column=0, columnspan=2, sticky='ew', pady=(10, 0))
        
        # Radiobuttons para género
        tk.Label(
            personal_frame,
            text="Género:",
            font=("Arial", 9, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).grid(row=0, column=0, sticky='w', pady=2)
        
        gender_frame = tk.Frame(personal_frame, bg='#2D2D30')
        gender_frame.grid(row=0, column=1, sticky='w', padx=(10, 0))
        
        tk.Radiobutton(
            gender_frame,
            text="Masculino",
            variable=self.gender_var,
            value="masculino",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#FFFFFF',
            activebackground='#404040',
            selectcolor='#0078D4'
        ).pack(side='left', padx=(0, 10))
        
        tk.Radiobutton(
            gender_frame,
            text="Femenino",
            variable=self.gender_var,
            value="femenino",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#FFFFFF',
            activebackground='#404040',
            selectcolor='#0078D4'
        ).pack(side='left', padx=(0, 10))
        
        tk.Radiobutton(
            gender_frame,
            text="No especifica",
            variable=self.gender_var,
            value="no_especifica",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#FFFFFF',
            activebackground='#404040',
            selectcolor='#0078D4'
        ).pack(side='left')
        
        # Radiobuttons para estado
        tk.Label(
            personal_frame,
            text="Estado:",
            font=("Arial", 9, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).grid(row=1, column=0, sticky='w', pady=2)
        
        status_frame = tk.Frame(personal_frame, bg='#2D2D30')
        status_frame.grid(row=1, column=1, sticky='w', padx=(10, 0))
        
        tk.Radiobutton(
            status_frame,
            text="Activo",
            variable=self.status_var,
            value="activo",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#4CAF50',
            activebackground='#404040',
            selectcolor='#4CAF50'
        ).pack(side='left', padx=(0, 10))
        
        tk.Radiobutton(
            status_frame,
            text="Inactivo",
            variable=self.status_var,
            value="inactivo",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#F44336',
            activebackground='#404040',
            selectcolor='#F44336'
        ).pack(side='left', padx=(0, 10))
        
        tk.Radiobutton(
            status_frame,
            text="Graduado",
            variable=self.status_var,
            value="graduado",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#9C27B0',
            activebackground='#404040',
            selectcolor='#9C27B0'
        ).pack(side='left')
        
    def validate_age_input(self, value):
        """
        Valida la entrada de edad en tiempo real
        
        Args:
            value (str): Valor introducido
            
        Returns:
            bool: True si es válido
        """
        if value == "":
            return True
        try:
            age = int(value)
            return 0 <= age <= 120 and len(value) <= 3
        except ValueError:
            return False
            
    def get_data(self):
        """
        Obtiene los datos del formulario
        
        Returns:
            dict: Diccionario con los datos del formulario
        """
        return {
            'name': self.name_var.get().strip(),
            'email': self.email_var.get().strip(),
            'age': self.age_var.get().strip(),
            'course': self.course_var.get().strip(),
            'gender': self.gender_var.get(),
            'status': self.status_var.get()
        }
        
    def validate_data(self):
        """
        Valida todos los datos del formulario
        
        Returns:
            bool: True si todos los datos son válidos
        """
        data = self.get_data()
        
        # Validar nombre
        if not data['name']:
            messagebox.showerror("Error", "El nombre es obligatorio")
            self.name_entry.focus()
            return False
            
        if not validate_name(data['name']):
            messagebox.showerror("Error", "El nombre solo debe contener letras y espacios")
            self.name_entry.focus()
            return False
            
        # Validar email
        if not data['email']:
            messagebox.showerror("Error", "El email es obligatorio")
            self.email_entry.focus()
            return False
            
        if not validate_email(data['email']):
            messagebox.showerror("Error", "El formato del email no es válido")
            self.email_entry.focus()
            return False
            
        # Validar edad
        if not data['age']:
            messagebox.showerror("Error", "La edad es obligatoria")
            self.age_entry.focus()
            return False
            
        try:
            age_int = int(data['age'])
            if age_int < 1 or age_int > 120:
                messagebox.showerror("Error", "La edad debe estar entre 1 y 120 años")
                self.age_entry.focus()
                return False
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número")
            self.age_entry.focus()
            return False
            
        # Validar curso
        if not data['course'] or data['course'] == "Seleccionar curso...":
            messagebox.showerror("Error", "Debe seleccionar un curso")
            self.course_combo.focus()
            return False
            
        return True
        
    def clear_form(self):
        """
        Limpia todos los campos del formulario
        """
        self.name_var.set("")
        self.email_var.set("")
        self.age_var.set("")
        self.course_var.set("")
        self.course_combo.set("Seleccionar curso...")
        self.gender_var.set("no_especifica")
        self.status_var.set("activo")
        self.name_entry.focus()
        
    def focus_first_field(self):
        """
        Coloca el foco en el primer campo del formulario
        """
        self.name_entry.focus()
