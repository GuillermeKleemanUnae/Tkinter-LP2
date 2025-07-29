#!/usr/bin/env python3
"""
Componente de Lista de Estudiantes
=================================

Este módulo contiene la clase StudentList que maneja
la visualización y gestión de la lista de estudiantes.

Incluye:
- Treeview para mostrar estudiantes en formato tabla
- Funcionalidad de búsqueda y filtrado
- Selección y eventos de interacción
- Exportación de datos

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox


class StudentList:
    """
    Clase que maneja la lista de estudiantes y su visualización
    """
    
    def __init__(self, parent, students_data=None):
        """
        Inicializa la lista de estudiantes
        
        Args:
            parent: Widget padre donde se colocará la lista
            students_data: Lista de estudiantes (opcional)
        """
        self.parent = parent
        self.students_data = students_data or []
        self.filtered_students = self.students_data.copy()
        
        self.init_variables()
        self.create_search_section()
        self.create_list()
        
    def init_variables(self):
        """
        Inicializa las variables de control
        """
        self.search_var = tk.StringVar()
        self.search_var.trace_add('write', self.on_search_change)
        
    def create_search_section(self):
        """
        Crea la sección de búsqueda
        """
        # Frame para búsqueda
        search_frame = tk.LabelFrame(
            self.parent,
            text="🔍 Búsqueda y Filtros",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=10,
            relief='groove',
            borderwidth=2
        )
        search_frame.pack(fill='x', pady=(0, 10))
        
        # Container para búsqueda
        search_container = tk.Frame(search_frame, bg='#2D2D30')
        search_container.pack(fill='x')
        
        # Icono de búsqueda
        tk.Label(
            search_container,
            text="🔎",
            font=("Arial", 14),
            bg='#2D2D30',
            fg='#0078D4'
        ).pack(side='left', padx=(0, 5))
        
        # Campo de búsqueda
        self.search_entry = tk.Entry(
            search_container,
            textvariable=self.search_var,
            font=("Arial", 11),
            borderwidth=2,
            relief='sunken',
            bg='#3C3C3C',
            fg='#FFFFFF',
            insertbackground='#FFFFFF',
            selectbackground='#0078D4',
            selectforeground='#FFFFFF'
        )
        self.search_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        # Botón limpiar búsqueda
        clear_btn = tk.Button(
            search_container,
            text="✖",
            font=("Arial", 10, "bold"),
            bg='#6C757D',
            fg='black',
            activebackground='#5A6268',
            activeforeground='black',
            width=3,
            relief='raised',
            borderwidth=1,
            command=self.clear_search
        )
        clear_btn.pack(side='right')
        
    def create_list(self):
        """
        Crea la lista principal con Treeview
        """
        # Frame para la lista
        list_frame = tk.LabelFrame(
            self.parent,
            text="👥 Lista de Estudiantes Registrados",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=10,
            relief='groove',
            borderwidth=2
        )
        list_frame.pack(fill='both', expand=True)
        
        # Container para Treeview
        tree_container = tk.Frame(list_frame, bg='#2D2D30')
        tree_container.pack(fill='both', expand=True)
        
        # Configurar columnas
        columns = ("ID", "Nombre", "Email", "Edad", "Curso", "Género", "Estado")
        self.tree = ttk.Treeview(tree_container, columns=columns, show="headings", height=12)
        
        # Configurar encabezados y anchos
        column_widths = {
            "ID": 50, "Nombre": 150, "Email": 180, "Edad": 60,
            "Curso": 120, "Género": 80, "Estado": 80
        }
        
        for col in columns:
            self.tree.heading(col, text=col, anchor='w')
            self.tree.column(col, width=column_widths.get(col, 100), anchor='w')
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(tree_container, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(tree_container, orient=tk.HORIZONTAL, command=self.tree.xview)
        
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Grid layout
        self.tree.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        # Configurar expansión
        tree_container.grid_rowconfigure(0, weight=1)
        tree_container.grid_columnconfigure(0, weight=1)
        
        # Eventos
        self.tree.bind('<Double-1>', self.on_double_click)
        self.tree.bind('<Button-3>', self.show_context_menu)
        
    def add_student(self, student_data):
        """
        Agrega un estudiante a la lista
        
        Args:
            student_data: Datos del estudiante
        """
        self.students_data.append(student_data)
        self.refresh_list()
        
    def remove_student(self, student_id):
        """
        Elimina un estudiante de la lista
        
        Args:
            student_id: ID del estudiante a eliminar
        """
        self.students_data = [s for s in self.students_data if s.get('id') != student_id]
        self.refresh_list()
        
    def update_student(self, student_id, new_data):
        """
        Actualiza los datos de un estudiante
        
        Args:
            student_id: ID del estudiante
            new_data: Nuevos datos del estudiante
        """
        for i, student in enumerate(self.students_data):
            if student.get('id') == student_id:
                self.students_data[i] = new_data
                break
        self.refresh_list()
        
    def get_selected_student(self):
        """
        Obtiene el estudiante seleccionado
        
        Returns:
            dict: Datos del estudiante seleccionado o None
        """
        selection = self.tree.selection()
        if not selection:
            return None
            
        item = self.tree.item(selection[0])
        values = item['values']
        
        if not values:
            return None
            
        # Buscar el estudiante completo por ID
        student_id = values[0]
        for student in self.students_data:
            if student.get('id') == student_id:
                return student
                
        return None
        
    def refresh_list(self):
        """
        Refresca la visualización de la lista
        """
        # Limpiar vista actual
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Aplicar filtro de búsqueda
        search_term = self.search_var.get().lower()
        self.filtered_students = []
        
        for student in self.students_data:
            if self.matches_search(student, search_term):
                self.filtered_students.append(student)
                
        # Agregar estudiantes filtrados
        for student in self.filtered_students:
            self.tree.insert("", tk.END, values=(
                student.get('id', ''),
                student.get('name', ''),
                student.get('email', ''),
                student.get('age', ''),
                student.get('course', ''),
                student.get('gender', ''),
                student.get('status', '')
            ))
            
    def matches_search(self, student, search_term):
        """
        Verifica si un estudiante coincide con el término de búsqueda
        
        Args:
            student: Datos del estudiante
            search_term: Término de búsqueda
            
        Returns:
            bool: True si coincide
        """
        if not search_term:
            return True
            
        searchable_fields = ['name', 'email', 'course', 'gender', 'status']
        for field in searchable_fields:
            value = str(student.get(field, '')).lower()
            if search_term in value:
                return True
                
        return False
        
    def on_search_change(self, *args):
        """
        Maneja el cambio en el campo de búsqueda
        """
        self.refresh_list()
        
    def clear_search(self):
        """
        Limpia el campo de búsqueda
        """
        self.search_var.set("")
        
    def on_double_click(self, event):
        """
        Maneja el doble clic en un estudiante
        """
        student = self.get_selected_student()
        if student:
            self.show_student_details(student)
            
    def show_student_details(self, student):
        """
        Muestra los detalles de un estudiante
        
        Args:
            student: Datos del estudiante
        """
        details = f"""Información del Estudiante:

ID: {student.get('id', 'N/A')}
Nombre: {student.get('name', 'N/A')}
Email: {student.get('email', 'N/A')}
Edad: {student.get('age', 'N/A')}
Curso: {student.get('course', 'N/A')}
Género: {student.get('gender', 'N/A')}
Estado: {student.get('status', 'N/A')}"""
        
        messagebox.showinfo("Detalles del Estudiante", details)
        
    def show_context_menu(self, event):
        """
        Muestra menú contextual (placeholder)
        """
        # Aquí se podría implementar un menú contextual
        pass
        
    def get_student_count(self):
        """
        Obtiene el número total de estudiantes
        
        Returns:
            int: Número de estudiantes
        """
        return len(self.students_data)
        
    def get_filtered_count(self):
        """
        Obtiene el número de estudiantes filtrados
        
        Returns:
            int: Número de estudiantes en la vista actual
        """
        return len(self.filtered_students)
        
    def export_data(self):
        """
        Exporta los datos de los estudiantes (placeholder)
        """
        if not self.students_data:
            messagebox.showwarning("Sin datos", "No hay estudiantes para exportar")
            return
            
        # Aquí se implementaría la lógica de exportación
        messagebox.showinfo("Exportar", f"Se exportarían {len(self.students_data)} estudiantes")
        
    def set_students_data(self, students_data):
        """
        Establece los datos de estudiantes
        
        Args:
            students_data: Lista de estudiantes
        """
        self.students_data = students_data or []
        self.refresh_list()
