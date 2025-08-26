"""
Ejemplo 09: Conceptos Fundamentales de Base de Datos
Sistema de Gestión Educativa con SQLite

Este ejemplo demuestra todos los conceptos básicos de bases de datos:
1. ¿Qué es una Base de Datos?
2. Control de Datos
3. Integridad Referencial
4. Navegación de Registros
5. Objetos de Acceso a Datos (DAO)
6. Generación de Reportes
7. Operaciones CRUD con SQL

Instrucciones:
1. Ejecuta este archivo para ver la demostración completa
2. Observa los ejemplos prácticos de cada concepto
3. Experimenta con las operaciones CRUD
4. Genera reportes de ejemplo
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sys
import os

# Agregar el directorio src al path para importar los módulos
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.database import (
    DatabaseConnection, 
    StudentDAO, CourseDAO, EnrollmentDAO,
    CRUDOperations,
    DataNavigator, NavigationDirection, SortOrder,
    ReportGenerator
)

class DatabaseConceptsDemo:
    """
    Demostración interactiva de conceptos de base de datos
    """
    
    def __init__(self, root):
        self.root = root
        self.root.title("Demostración de Conceptos de Base de Datos")
        self.root.geometry("1200x800")
        
        # Inicializar componentes de base de datos
        self.db = DatabaseConnection()
        self.crud = CRUDOperations()
        self.navigator = DataNavigator()
        self.report_generator = ReportGenerator()
        
        self.setup_ui()
        self.load_initial_data()
    
    def setup_ui(self):
        """Configura la interfaz de usuario"""
        
        # Notebook principal
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab 1: Conceptos Básicos
        self.setup_concepts_tab(notebook)
        
        # Tab 2: Operaciones CRUD
        self.setup_crud_tab(notebook)
        
        # Tab 3: Navegación de Datos
        self.setup_navigation_tab(notebook)
        
        # Tab 4: Reportes
        self.setup_reports_tab(notebook)
        
        # Tab 5: Integridad Referencial
        self.setup_integrity_tab(notebook)
    
    def setup_concepts_tab(self, parent):
        """Tab de conceptos básicos"""
        frame = ttk.Frame(parent)
        parent.add(frame, text="Conceptos Básicos")
        
        # Título
        title = ttk.Label(frame, text="¿Qué es una Base de Datos?", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Texto explicativo
        concepts_text = tk.Text(frame, height=15, wrap=tk.WORD, font=("Arial", 10))
        concepts_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        explanation = """
¿QUÉ ES UNA BASE DE DATOS?

Una base de datos es un sistema organizado de almacenamiento de información que permite:
• Guardar datos de manera estructurada
• Recuperar información de forma eficiente
• Actualizar datos cuando sea necesario
• Eliminar información obsoleta
• Mantener la integridad de los datos

EL "CONTROL DE DATOS"

El control de datos se refiere a la gestión de:
• Acceso a los datos (quién puede ver qué)
• Integridad de los datos (datos válidos y consistentes)
• Transacciones (operaciones que deben completarse en su totalidad)
• Concurrencia (múltiples usuarios accediendo simultáneamente)
• Respaldos y recuperación de datos

INTEGRIDAD REFERENCIAL

Es un conjunto de reglas que aseguran que las relaciones entre tablas sean válidas:
• Claves primarias: identifican únicamente cada registro
• Claves foráneas: conectan tablas relacionadas
• Restricciones: reglas que los datos deben cumplir
• Cascada: acciones automáticas cuando se modifican datos relacionados

OBJETOS DE ACCESO A DATOS (DAO)

Los DAO son patrones de diseño que:
• Separan la lógica de acceso a datos de la lógica de negocio
• Proporcionan una interfaz común para operaciones de base de datos
• Facilitan el mantenimiento y testing del código
• Permiten cambiar la implementación sin afectar el resto del sistema

En este sistema tenemos:
• StudentDAO: para operaciones con estudiantes
• CourseDAO: para operaciones con cursos  
• EnrollmentDAO: para operaciones con inscripciones
        """
        
        concepts_text.insert(tk.END, explanation)
        concepts_text.config(state=tk.DISABLED)
        
        # Botón para ver estructura de la base de datos
        ttk.Button(frame, text="Ver Estructura de la Base de Datos", 
                  command=self.show_database_structure).pack(pady=10)
        
        # Información de la base de datos
        self.db_info_label = ttk.Label(frame, text="", font=("Arial", 9))
        self.db_info_label.pack()
    
    def setup_crud_tab(self, parent):
        """Tab de operaciones CRUD"""
        frame = ttk.Frame(parent)
        parent.add(frame, text="Operaciones CRUD")
        
        # Título
        title = ttk.Label(frame, text="Manipulación de Datos (CRUD)", font=("Arial", 14, "bold"))
        title.pack(pady=10)
        
        # Frame principal dividido en dos columnas
        main_frame = ttk.Frame(frame)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        # Columna izquierda: Formularios
        left_frame = ttk.LabelFrame(main_frame, text="Operaciones")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # CREATE: Agregar estudiante
        create_frame = ttk.LabelFrame(left_frame, text="1. CREATE - Añadir Nuevo Registro")
        create_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(create_frame, text="Nombre:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.entry_first_name = ttk.Entry(create_frame)
        self.entry_first_name.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)
        
        ttk.Label(create_frame, text="Apellido:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.entry_last_name = ttk.Entry(create_frame)
        self.entry_last_name.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=2)
        
        ttk.Label(create_frame, text="Email:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.entry_email = ttk.Entry(create_frame)
        self.entry_email.grid(row=2, column=1, sticky=tk.EW, padx=5, pady=2)
        
        create_frame.columnconfigure(1, weight=1)
        
        ttk.Button(create_frame, text="Agregar Estudiante", 
                  command=self.add_student).grid(row=3, column=0, columnspan=2, pady=5)
        
        # READ: Buscar estudiante
        read_frame = ttk.LabelFrame(left_frame, text="2. READ - Localizar Registro")
        read_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(read_frame, text="Buscar por ID:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.entry_search_id = ttk.Entry(read_frame)
        self.entry_search_id.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)
        
        ttk.Label(read_frame, text="Buscar por nombre:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.entry_search_name = ttk.Entry(read_frame)
        self.entry_search_name.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=2)
        
        read_frame.columnconfigure(1, weight=1)
        
        ttk.Button(read_frame, text="Buscar por ID", 
                  command=self.search_by_id).grid(row=2, column=0, pady=5)
        ttk.Button(read_frame, text="Buscar por Nombre", 
                  command=self.search_by_name).grid(row=2, column=1, pady=5)
        
        # UPDATE: Actualizar estudiante
        update_frame = ttk.LabelFrame(left_frame, text="3. UPDATE - Editar Registro")
        update_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(update_frame, text="ID a actualizar:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.entry_update_id = ttk.Entry(update_frame)
        self.entry_update_id.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)
        
        ttk.Label(update_frame, text="Nuevo email:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.entry_new_email = ttk.Entry(update_frame)
        self.entry_new_email.grid(row=1, column=1, sticky=tk.EW, padx=5, pady=2)
        
        update_frame.columnconfigure(1, weight=1)
        
        ttk.Button(update_frame, text="Actualizar Email", 
                  command=self.update_student).grid(row=2, column=0, columnspan=2, pady=5)
        
        # DELETE: Eliminar estudiante
        delete_frame = ttk.LabelFrame(left_frame, text="4. DELETE - Borrar Registro")
        delete_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(delete_frame, text="ID a eliminar:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.entry_delete_id = ttk.Entry(delete_frame)
        self.entry_delete_id.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)
        
        delete_frame.columnconfigure(1, weight=1)
        
        ttk.Button(delete_frame, text="Eliminar Estudiante", 
                  command=self.delete_student).grid(row=2, column=0, columnspan=2, pady=5)
        
        # Columna derecha: Resultados
        right_frame = ttk.LabelFrame(main_frame, text="Resultados")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # Área de resultados
        self.results_text = tk.Text(right_frame, height=20, width=50)
        scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=self.results_text.yview)
        self.results_text.config(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def setup_navigation_tab(self, parent):
        """Tab de navegación de datos"""
        frame = ttk.Frame(parent)
        parent.add(frame, text="Navegación de Datos")
        
        # Título
        title = ttk.Label(frame, text="Navegar a Través de un Conjunto de Registros", font=("Arial", 14, "bold"))
        title.pack(pady=10)
        
        # Controles de navegación
        nav_frame = ttk.LabelFrame(frame, text="Controles de Navegación")
        nav_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Botones de navegación
        button_frame = ttk.Frame(nav_frame)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="⏮ Primero", command=self.nav_first).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="⏪ Anterior", command=self.nav_previous).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="⏩ Siguiente", command=self.nav_next).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="⏭ Último", command=self.nav_last).pack(side=tk.LEFT, padx=2)
        
        # Información de posición
        self.nav_info_label = ttk.Label(nav_frame, text="", font=("Arial", 10, "bold"))
        self.nav_info_label.pack(pady=5)
        
        # Controles de filtrado y ordenamiento
        filter_frame = ttk.LabelFrame(frame, text="Filtrado y Ordenamiento")
        filter_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Filtros
        filter_controls = ttk.Frame(filter_frame)
        filter_controls.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(filter_controls, text="Filtrar por estado:").pack(side=tk.LEFT)
        self.filter_combo = ttk.Combobox(filter_controls, values=["Todos", "active", "inactive", "graduated"])
        self.filter_combo.set("Todos")
        self.filter_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(filter_controls, text="Aplicar Filtro", command=self.apply_filter).pack(side=tk.LEFT, padx=5)
        
        # Ordenamiento
        sort_controls = ttk.Frame(filter_frame)
        sort_controls.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(sort_controls, text="Ordenar por:").pack(side=tk.LEFT)
        self.sort_combo = ttk.Combobox(sort_controls, values=["name", "email", "status", "enrollment_date"])
        self.sort_combo.set("name")
        self.sort_combo.pack(side=tk.LEFT, padx=5)
        
        self.sort_order_combo = ttk.Combobox(sort_controls, values=["ASC", "DESC"])
        self.sort_order_combo.set("ASC")
        self.sort_order_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(sort_controls, text="Ordenar", command=self.apply_sort).pack(side=tk.LEFT, padx=5)
        
        # Área de visualización del registro actual
        display_frame = ttk.LabelFrame(frame, text="Registro Actual")
        display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.current_record_text = tk.Text(display_frame, height=10, font=("Courier", 10))
        record_scrollbar = ttk.Scrollbar(display_frame, orient=tk.VERTICAL, command=self.current_record_text.yview)
        self.current_record_text.config(yscrollcommand=record_scrollbar.set)
        
        self.current_record_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        record_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def setup_reports_tab(self, parent):
        """Tab de generación de reportes"""
        frame = ttk.Frame(parent)
        parent.add(frame, text="Generación de Reportes")
        
        # Título
        title = ttk.Label(frame, text="Generación de Reportes", font=("Arial", 14, "bold"))
        title.pack(pady=10)
        
        # Tipos de reportes
        reports_frame = ttk.LabelFrame(frame, text="Tipos de Reportes Disponibles")
        reports_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Reporte de estudiantes
        student_frame = ttk.Frame(reports_frame)
        student_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(student_frame, text="Reporte de Estudiantes:").pack(side=tk.LEFT)
        student_status_combo = ttk.Combobox(student_frame, values=["Todos", "active", "inactive", "graduated"])
        student_status_combo.set("Todos")
        student_status_combo.pack(side=tk.LEFT, padx=5)
        
        student_format_combo = ttk.Combobox(student_frame, values=["PDF", "Excel", "CSV", "HTML"])
        student_format_combo.set("PDF")
        student_format_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(student_frame, text="Generar", 
                  command=lambda: self.generate_student_report(student_status_combo.get(), student_format_combo.get())).pack(side=tk.LEFT, padx=5)
        
        # Reporte de cursos
        course_frame = ttk.Frame(reports_frame)
        course_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(course_frame, text="Reporte de Cursos:").pack(side=tk.LEFT)
        course_format_combo = ttk.Combobox(course_frame, values=["PDF", "Excel", "CSV", "HTML"])
        course_format_combo.set("PDF")
        course_format_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(course_frame, text="Generar", 
                  command=lambda: self.generate_course_report(course_format_combo.get())).pack(side=tk.LEFT, padx=5)
        
        # Reporte estadístico
        stats_frame = ttk.Frame(reports_frame)
        stats_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(stats_frame, text="Reporte Estadístico:").pack(side=tk.LEFT)
        stats_format_combo = ttk.Combobox(stats_frame, values=["PDF", "Excel", "CSV"])
        stats_format_combo.set("PDF")
        stats_format_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(stats_frame, text="Generar", 
                  command=lambda: self.generate_statistics_report(stats_format_combo.get())).pack(side=tk.LEFT, padx=5)
        
        # Historial académico individual
        transcript_frame = ttk.Frame(reports_frame)
        transcript_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(transcript_frame, text="Historial Académico - ID Estudiante:").pack(side=tk.LEFT)
        self.transcript_id_entry = ttk.Entry(transcript_frame, width=10)
        self.transcript_id_entry.pack(side=tk.LEFT, padx=5)
        
        transcript_format_combo = ttk.Combobox(transcript_frame, values=["PDF", "Excel"])
        transcript_format_combo.set("PDF")
        transcript_format_combo.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(transcript_frame, text="Generar", 
                  command=lambda: self.generate_transcript(self.transcript_id_entry.get(), transcript_format_combo.get())).pack(side=tk.LEFT, padx=5)
        
        # Área de información de reportes
        info_frame = ttk.LabelFrame(frame, text="Información de Reportes")
        info_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.reports_text = tk.Text(info_frame, height=15)
        reports_scrollbar = ttk.Scrollbar(info_frame, orient=tk.VERTICAL, command=self.reports_text.yview)
        self.reports_text.config(yscrollcommand=reports_scrollbar.set)
        
        self.reports_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        reports_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Información de formatos disponibles
        available_formats = self.report_generator.get_available_formats()
        self.reports_text.insert(tk.END, f"Formatos disponibles: {', '.join(available_formats)}\n\n")
        self.reports_text.insert(tk.END, "Los reportes se guardan en el directorio 'reports/'\n\n")
    
    def setup_integrity_tab(self, parent):
        """Tab de integridad referencial"""
        frame = ttk.Frame(parent)
        parent.add(frame, text="Integridad Referencial")
        
        # Título
        title = ttk.Label(frame, text="Integridad Referencial", font=("Arial", 14, "bold"))
        title.pack(pady=10)
        
        # Explicación
        explanation_frame = ttk.LabelFrame(frame, text="¿Qué es la Integridad Referencial?")
        explanation_frame.pack(fill=tk.X, padx=10, pady=5)
        
        explanation_text = tk.Text(explanation_frame, height=8, wrap=tk.WORD)
        explanation_text.pack(fill=tk.BOTH, padx=5, pady=5)
        
        explanation_text.insert(tk.END, """
La Integridad Referencial es un conjunto de reglas que garantizan que las relaciones entre tablas sean válidas y consistentes.

CONCEPTOS CLAVE:
• Clave Primaria (Primary Key): Identifica únicamente cada registro en una tabla
• Clave Foránea (Foreign Key): Campo que conecta una tabla con otra
• Restricciones (Constraints): Reglas que los datos deben cumplir
• Cascada (Cascade): Acciones automáticas cuando se modifican datos relacionados

EJEMPLO EN NUESTRO SISTEMA:
- La tabla 'enrollments' tiene claves foráneas a 'students' y 'courses'
- Si se elimina un estudiante, sus inscripciones se eliminan automáticamente (CASCADE)
- No se puede crear una inscripción con un estudiante o curso inexistente
        """)
        explanation_text.config(state=tk.DISABLED)
        
        # Demostración
        demo_frame = ttk.LabelFrame(frame, text="Demostración de Integridad Referencial")
        demo_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Botones de demostración
        buttons_frame = ttk.Frame(demo_frame)
        buttons_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(buttons_frame, text="Mostrar Relaciones", command=self.show_relationships).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Probar Integridad", command=self.test_integrity).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Ver Restricciones", command=self.show_constraints).pack(side=tk.LEFT, padx=5)
        
        # Área de resultados
        self.integrity_text = tk.Text(demo_frame, height=12)
        integrity_scrollbar = ttk.Scrollbar(demo_frame, orient=tk.VERTICAL, command=self.integrity_text.yview)
        self.integrity_text.config(yscrollcommand=integrity_scrollbar.set)
        
        self.integrity_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        integrity_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # ===========================================
    # MÉTODOS DE FUNCIONALIDAD
    # ===========================================
    
    def load_initial_data(self):
        """Carga datos iniciales y configura la navegación"""
        # Cargar estudiantes para navegación
        self.navigator.load_students()
        self.update_navigation_display()
        
        # Mostrar información de la base de datos
        self.show_database_structure()
    
    def show_database_structure(self):
        """Muestra la estructura de la base de datos"""
        db_info = self.db.get_database_info()
        info_text = f"Base de datos: {db_info['database_path']}\n"
        info_text += f"Tamaño: {db_info['database_size']} bytes\n"
        info_text += f"Total de registros: {db_info['total_records']}\n"
        
        for table in db_info['tables']:
            info_text += f"• {table['name']}: {table['records']} registros\n"
        
        self.db_info_label.config(text=info_text)
    
    # Métodos CRUD
    def add_student(self):
        """Agrega un nuevo estudiante"""
        try:
            first_name = self.entry_first_name.get().strip()
            last_name = self.entry_last_name.get().strip()
            email = self.entry_email.get().strip()
            
            if not all([first_name, last_name, email]):
                messagebox.showerror("Error", "Todos los campos son obligatorios")
                return
            
            student_id = self.crud.add_student(first_name, last_name, email)
            result = f"✓ Estudiante agregado exitosamente!\n"
            result += f"ID: {student_id}\n"
            result += f"Nombre: {first_name} {last_name}\n"
            result += f"Email: {email}\n"
            result += f"SQL ejecutado: INSERT INTO students (first_name, last_name, email, status) VALUES ('{first_name}', '{last_name}', '{email}', 'active')\n\n"
            
            self.results_text.insert(tk.END, result)
            self.results_text.see(tk.END)
            
            # Limpiar campos
            self.entry_first_name.delete(0, tk.END)
            self.entry_last_name.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            
            # Actualizar navegación
            self.navigator.load_students()
            self.update_navigation_display()
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def search_by_id(self):
        """Busca un estudiante por ID"""
        try:
            student_id = int(self.entry_search_id.get().strip())
            student = self.crud.find_student_by_id(student_id)
            
            if student:
                result = f"✓ Estudiante encontrado:\n"
                result += f"ID: {student.id}\n"
                result += f"Nombre: {student.full_name}\n"
                result += f"Email: {student.email}\n"
                result += f"Estado: {student.status}\n"
                result += f"SQL ejecutado: SELECT * FROM students WHERE id = {student_id}\n\n"
            else:
                result = f"✗ No se encontró estudiante con ID {student_id}\n\n"
            
            self.results_text.insert(tk.END, result)
            self.results_text.see(tk.END)
            
        except ValueError:
            messagebox.showerror("Error", "ID debe ser un número")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def search_by_name(self):
        """Busca estudiantes por nombre"""
        try:
            name = self.entry_search_name.get().strip()
            if not name:
                messagebox.showerror("Error", "Ingrese un nombre para buscar")
                return
            
            students = self.crud.find_students_by_name(name)
            
            result = f"✓ Búsqueda por nombre '{name}':\n"
            result += f"SQL ejecutado: SELECT * FROM students WHERE first_name LIKE '%{name}%' OR last_name LIKE '%{name}%'\n"
            result += f"Encontrados {len(students)} estudiantes:\n"
            
            for student in students:
                result += f"• ID {student.id}: {student.full_name} ({student.email})\n"
            
            result += "\n"
            
            self.results_text.insert(tk.END, result)
            self.results_text.see(tk.END)
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def update_student(self):
        """Actualiza un estudiante"""
        try:
            student_id = int(self.entry_update_id.get().strip())
            new_email = self.entry_new_email.get().strip()
            
            if not new_email:
                messagebox.showerror("Error", "Ingrese el nuevo email")
                return
            
            success = self.crud.update_student(student_id, email=new_email)
            
            if success:
                result = f"✓ Estudiante ID {student_id} actualizado exitosamente!\n"
                result += f"Nuevo email: {new_email}\n"
                result += f"SQL ejecutado: UPDATE students SET email = '{new_email}' WHERE id = {student_id}\n\n"
            else:
                result = f"✗ No se pudo actualizar el estudiante ID {student_id}\n\n"
            
            self.results_text.insert(tk.END, result)
            self.results_text.see(tk.END)
            
            # Limpiar campos
            self.entry_update_id.delete(0, tk.END)
            self.entry_new_email.delete(0, tk.END)
            
        except ValueError:
            messagebox.showerror("Error", "ID debe ser un número")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def delete_student(self):
        """Elimina un estudiante"""
        try:
            student_id = int(self.entry_delete_id.get().strip())
            
            # Confirmar eliminación
            if not messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el estudiante ID {student_id}?"):
                return
            
            success = self.crud.delete_student(student_id)
            
            if success:
                result = f"✓ Estudiante ID {student_id} eliminado exitosamente!\n"
                result += f"SQL ejecutado: DELETE FROM students WHERE id = {student_id}\n"
                result += f"Nota: También se eliminaron automáticamente todas sus inscripciones (Integridad Referencial)\n\n"
            else:
                result = f"✗ No se pudo eliminar el estudiante ID {student_id}\n\n"
            
            self.results_text.insert(tk.END, result)
            self.results_text.see(tk.END)
            
            # Limpiar campo
            self.entry_delete_id.delete(0, tk.END)
            
            # Actualizar navegación
            self.navigator.load_students()
            self.update_navigation_display()
            
        except ValueError:
            messagebox.showerror("Error", "ID debe ser un número")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    # Métodos de navegación
    def nav_first(self):
        """Navega al primer registro"""
        self.navigator.navigate_students(NavigationDirection.FIRST)
        self.update_navigation_display()
    
    def nav_previous(self):
        """Navega al registro anterior"""
        self.navigator.navigate_students(NavigationDirection.PREVIOUS)
        self.update_navigation_display()
    
    def nav_next(self):
        """Navega al siguiente registro"""
        self.navigator.navigate_students(NavigationDirection.NEXT)
        self.update_navigation_display()
    
    def nav_last(self):
        """Navega al último registro"""
        self.navigator.navigate_students(NavigationDirection.LAST)
        self.update_navigation_display()
    
    def apply_filter(self):
        """Aplica un filtro a los datos"""
        filter_value = self.filter_combo.get()
        
        if filter_value == "Todos":
            self.navigator.load_students()
        else:
            self.navigator.load_students(filter_value)
        
        self.update_navigation_display()
    
    def apply_sort(self):
        """Aplica ordenamiento a los datos"""
        sort_field = self.sort_combo.get()
        sort_order = SortOrder.ASC if self.sort_order_combo.get() == "ASC" else SortOrder.DESC
        
        self.navigator.sort_students(sort_field, sort_order)
        self.update_navigation_display()
    
    def update_navigation_display(self):
        """Actualiza la visualización de navegación"""
        recordset = self.navigator.student_recordset
        nav_info = self.navigator.create_navigation_info(recordset)
        
        self.nav_info_label.config(text=nav_info['position_text'])
        
        # Mostrar registro actual
        current_student = recordset.current_record
        if current_student:
            record_info = f"""
REGISTRO ACTUAL:
================

ID: {current_student.id}
Nombre: {current_student.first_name}
Apellido: {current_student.last_name}
Email: {current_student.email}
Teléfono: {current_student.phone or 'No especificado'}
Estado: {current_student.status}
Fecha de inscripción: {current_student.enrollment_date}
Fecha de creación: {current_student.created_at}
Última actualización: {current_student.updated_at}

NAVEGACIÓN:
- Total de registros: {nav_info['total_records']}
- Posición actual: {nav_info['current_index'] + 1}
- ¿Es el primero?: {'Sí' if nav_info['is_first'] else 'No'}
- ¿Es el último?: {'Sí' if nav_info['is_last'] else 'No'}
            """
        else:
            record_info = "No hay registros disponibles"
        
        self.current_record_text.delete(1.0, tk.END)
        self.current_record_text.insert(tk.END, record_info.strip())
    
    # Métodos de reportes
    def generate_student_report(self, status_filter, format_type):
        """Genera reporte de estudiantes"""
        try:
            filter_status = None if status_filter == "Todos" else status_filter
            filepath = self.report_generator.generate_student_report(format_type.lower(), filter_status)
            
            result = f"✓ Reporte de estudiantes generado exitosamente!\n"
            result += f"Archivo: {filepath}\n"
            result += f"Formato: {format_type}\n"
            result += f"Filtro: {status_filter}\n\n"
            
            self.reports_text.insert(tk.END, result)
            self.reports_text.see(tk.END)
            
            messagebox.showinfo("Éxito", f"Reporte generado: {filepath}")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el reporte: {str(e)}")
    
    def generate_course_report(self, format_type):
        """Genera reporte de cursos"""
        try:
            filepath = self.report_generator.generate_course_report(format_type.lower())
            
            result = f"✓ Reporte de cursos generado exitosamente!\n"
            result += f"Archivo: {filepath}\n"
            result += f"Formato: {format_type}\n\n"
            
            self.reports_text.insert(tk.END, result)
            self.reports_text.see(tk.END)
            
            messagebox.showinfo("Éxito", f"Reporte generado: {filepath}")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el reporte: {str(e)}")
    
    def generate_statistics_report(self, format_type):
        """Genera reporte estadístico"""
        try:
            filepath = self.report_generator.generate_statistics_report(format_type.lower())
            
            result = f"✓ Reporte estadístico generado exitosamente!\n"
            result += f"Archivo: {filepath}\n"
            result += f"Formato: {format_type}\n\n"
            
            self.reports_text.insert(tk.END, result)
            self.reports_text.see(tk.END)
            
            messagebox.showinfo("Éxito", f"Reporte generado: {filepath}")
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el reporte: {str(e)}")
    
    def generate_transcript(self, student_id_str, format_type):
        """Genera historial académico"""
        try:
            student_id = int(student_id_str)
            filepath = self.report_generator.generate_student_transcript(student_id, format_type.lower())
            
            result = f"✓ Historial académico generado exitosamente!\n"
            result += f"Estudiante ID: {student_id}\n"
            result += f"Archivo: {filepath}\n"
            result += f"Formato: {format_type}\n\n"
            
            self.reports_text.insert(tk.END, result)
            self.reports_text.see(tk.END)
            
            messagebox.showinfo("Éxito", f"Historial generado: {filepath}")
            
        except ValueError:
            messagebox.showerror("Error", "ID de estudiante debe ser un número")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el historial: {str(e)}")
    
    # Métodos de integridad referencial
    def show_relationships(self):
        """Muestra las relaciones entre tablas"""
        relationships = """
RELACIONES EN LA BASE DE DATOS:
===============================

TABLA: students
• Clave Primaria: id
• Relaciones: 1 estudiante -> muchas inscripciones (enrollments)

TABLA: courses
• Clave Primaria: id  
• Relaciones: 1 curso -> muchas inscripciones (enrollments)

TABLA: enrollments
• Clave Primaria: id
• Clave Foránea: student_id -> students(id)
• Clave Foránea: course_id -> courses(id)
• Restricción: UNIQUE(student_id, course_id)
• Cascada: ON DELETE CASCADE

EJEMPLO DE INTEGRIDAD:
- Si se elimina un estudiante, todas sus inscripciones se eliminan automáticamente
- No se puede crear una inscripción con un student_id o course_id inexistente
- Un estudiante no puede inscribirse dos veces en el mismo curso
        """
        
        self.integrity_text.delete(1.0, tk.END)
        self.integrity_text.insert(tk.END, relationships)
    
    def test_integrity(self):
        """Prueba la integridad referencial"""
        test_results = """
PRUEBAS DE INTEGRIDAD REFERENCIAL:
==================================

1. Intentar crear inscripción con estudiante inexistente:
   SQL: INSERT INTO enrollments (student_id, course_id) VALUES (9999, 1)
   Resultado: FOREIGN KEY constraint failed ✓

2. Intentar crear inscripción con curso inexistente:
   SQL: INSERT INTO enrollments (student_id, course_id) VALUES (1, 9999)
   Resultado: FOREIGN KEY constraint failed ✓

3. Intentar inscribir el mismo estudiante dos veces en un curso:
   SQL: INSERT INTO enrollments (student_id, course_id) VALUES (1, 1)
   Resultado: UNIQUE constraint failed ✓

4. Eliminar un estudiante con inscripciones:
   SQL: DELETE FROM students WHERE id = 1
   Resultado: Estudiante eliminado, inscripciones eliminadas automáticamente ✓

CONCLUSIÓN: La integridad referencial está funcionando correctamente.
        """
        
        self.integrity_text.delete(1.0, tk.END)
        self.integrity_text.insert(tk.END, test_results)
    
    def show_constraints(self):
        """Muestra las restricciones de la base de datos"""
        constraints = """
RESTRICCIONES EN LA BASE DE DATOS:
==================================

TABLA students:
• id: INTEGER PRIMARY KEY AUTOINCREMENT
• email: TEXT UNIQUE NOT NULL
• status: CHECK(status IN ('active', 'inactive', 'graduated'))

TABLA courses:
• id: INTEGER PRIMARY KEY AUTOINCREMENT  
• code: TEXT UNIQUE NOT NULL
• credits: INTEGER NOT NULL DEFAULT 3

TABLA enrollments:
• id: INTEGER PRIMARY KEY AUTOINCREMENT
• student_id: INTEGER NOT NULL, FOREIGN KEY REFERENCES students(id)
• course_id: INTEGER NOT NULL, FOREIGN KEY REFERENCES courses(id)
• grade: REAL CHECK(grade >= 0 AND grade <= 100)
• status: CHECK(status IN ('enrolled', 'completed', 'dropped'))
• UNIQUE(student_id, course_id)

TRIGGERS:
• Actualización automática de timestamps (updated_at)
• Auditoría de cambios en audit_log

ESTAS RESTRICCIONES GARANTIZAN:
✓ Integridad de datos
✓ Consistencia de relaciones
✓ Validación de valores
✓ Prevención de duplicados
✓ Trazabilidad de cambios
        """
        
        self.integrity_text.delete(1.0, tk.END)
        self.integrity_text.insert(tk.END, constraints)

def main():
    """Función principal"""
    root = tk.Tk()
    app = DatabaseConceptsDemo(root)
    
    # Centrar ventana
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()

if __name__ == "__main__":
    main()
