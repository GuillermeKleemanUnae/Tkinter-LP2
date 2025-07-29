#!/usr/bin/env python3
"""
Versión refactorizada de la ventana principal que utiliza
componentes modulares para una mejor organización del código.

Esta versión demuestra:
- Separación de responsabilidades
- Composición de componentes
- Código más mantenible y legible
- Arquitectura modular

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from ..models.student import Student
from .components.student_form import StudentForm
from .components.student_list import StudentList
from .components.config_panel import ConfigurationPanel


class MainWindow:
    """
    Clase principal de la ventana de la aplicación
    
    Esta versión refactorizada utiliza componentes modulares
    para mantener el código organizado y fácil de mantener.
    """
    
    def __init__(self, root):
        """
        Inicializa la ventana principal
        
        Args:
            root: Ventana raíz de Tkinter
        """
        self.root = root
        self.students = []
        self.current_student_id = 1
        
        self.setup_window()
        self.create_layout()
        self.setup_components()
        
    def setup_window(self):
        """
        Configura las propiedades básicas de la ventana
        """
        self.root.title("Sistema de Gestión de Estudiantes - Versión Modular")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        self.root.minsize(800, 600)
        self.root.configure(bg='#1E1E1E')  # Fondo oscuro principal
        
        # Centrar ventana
        self.center_window()
        
        # Protocolo de cierre
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def center_window(self):
        """
        Centra la ventana en la pantalla
        """
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_layout(self):
        """
        Crea el layout principal de la aplicación
        """
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#1E1E1E', padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configurar expansión
        main_frame.grid_rowconfigure(1, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        
        # Header
        self.create_header(main_frame)
        
        # Sección izquierda - Formulario y configuración
        self.left_frame = tk.Frame(main_frame, bg='#1E1E1E')
        self.left_frame.grid(row=1, column=0, sticky='nsew', padx=(0, 5))
        
        # Sección derecha - Lista de estudiantes
        self.right_frame = tk.Frame(main_frame, bg='#1E1E1E')
        self.right_frame.grid(row=1, column=1, sticky='nsew', padx=(5, 0))
        
        # Botones de acción
        self.create_action_buttons(main_frame)
        
    def create_header(self, parent):
        """
        Crea el header de la aplicación
        """
        header_frame = tk.Frame(parent, bg='#2D2D30', height=60)
        header_frame.grid(row=0, column=0, columnspan=2, sticky='ew', pady=(0, 10))
        header_frame.grid_propagate(False)
        
        # Título
        title_label = tk.Label(
            header_frame,
            text="🎓 Sistema de Gestión de Estudiantes",
            font=("Arial", 16, "bold"),
            fg='#FFFFFF',
            bg='#2D2D30'
        )
        title_label.pack(expand=True)
        
    def setup_components(self):
        """
        Inicializa y configura los componentes modulares
        """
        # Componente de formulario
        self.student_form = StudentForm(
            parent=self.left_frame,
            on_student_added=self.on_student_added
        )
        
        # Componente de configuración
        self.config_panel = ConfigurationPanel(
            parent=self.left_frame,
            on_config_changed=self.on_config_changed
        )
        
        # Componente de lista de estudiantes
        self.student_list = StudentList(
            parent=self.right_frame,
            students_data=self.students
        )
        
    def create_action_buttons(self, parent):
        """
        Crea los botones de acción principales
        """
        button_frame = tk.Frame(parent, bg='#1E1E1E', pady=15)
        button_frame.grid(row=2, column=0, columnspan=2, sticky='ew')
        
        # Container centrado para botones
        button_container = tk.Frame(button_frame, bg='#1E1E1E')
        button_container.pack()
        
        # Botón agregar
        add_btn = tk.Button(
            button_container,
            text="➕ Agregar Estudiante",
            font=("Arial", 11, "bold"),
            bg='#4CAF50',
            fg='black',
            activebackground='#45A049',
            activeforeground='black',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.add_student
        )
        add_btn.pack(side='left', padx=5)
        
        # Botón editar
        edit_btn = tk.Button(
            button_container,
            text="✏️ Editar",
            font=("Arial", 11),
            bg='#0078D4',
            fg='black',
            activebackground='#106EBE',
            activeforeground='black',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.edit_student
        )
        edit_btn.pack(side='left', padx=5)
        
        # Botón eliminar
        delete_btn = tk.Button(
            button_container,
            text="🗑️ Eliminar",
            font=("Arial", 11),
            bg='#F44336',
            fg='black',
            activebackground='#DA190B',
            activeforeground='black',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.delete_student
        )
        delete_btn.pack(side='left', padx=5)
        
        # Botón limpiar
        clear_btn = tk.Button(
            button_container,
            text="🧹 Limpiar",
            font=("Arial", 11),
            bg='#6C757D',
            fg='black',
            activebackground='#5A6268',
            activeforeground='black',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.clear_form
        )
        clear_btn.pack(side='left', padx=5)
        
        # Botón diálogos
        dialogs_btn = tk.Button(
            button_container,
            text="💬 Diálogos",
            font=("Arial", 11),
            bg='#9C27B0',
            fg='black',
            activebackground='#7B1FA2',
            activeforeground='black',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.show_dialogs
        )
        dialogs_btn.pack(side='left', padx=5)
        
    def add_student(self):
        """
        Agrega un nuevo estudiante
        """
        # Validar datos del formulario
        if not self.student_form.validate_data():
            return
            
        # Verificar términos si es necesario
        if not self.config_panel.is_terms_accepted():
            if not messagebox.askyesno(
                "Términos y Condiciones",
                "Para registrar estudiantes debe aceptar los términos y condiciones.\n¿Desea aceptarlos ahora?"
            ):
                return
                
        # Obtener datos del formulario
        form_data = self.student_form.get_data()
        
        try:
            # Crear estudiante
            student = Student(
                name=form_data['name'],
                email=form_data['email'],
                age=int(form_data['age']),
                course=form_data['course']
            )
            
            # Crear datos completos para la lista
            student_data = {
                'id': self.current_student_id,
                'name': student.name,
                'email': student.email,
                'age': student.age,
                'course': student.course,
                'gender': form_data['gender'],
                'status': form_data['status']
            }
            
            # Agregar a la lista interna
            self.students.append(student_data)
            self.current_student_id += 1
            
            # Actualizar lista visual
            self.student_list.set_students_data(self.students)
            
            # Limpiar formulario
            self.student_form.clear_form()
            
            messagebox.showinfo("Éxito", f"Estudiante '{student.name}' agregado correctamente")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al agregar estudiante: {str(e)}")
            
    def edit_student(self):
        """
        Edita el estudiante seleccionado
        """
        selected_student = self.student_list.get_selected_student()
        
        if not selected_student:
            messagebox.showwarning("Selección requerida", "Por favor selecciona un estudiante para editar")
            return
            
        # Aquí se podría implementar una ventana de edición
        messagebox.showinfo("Editar", f"Editando estudiante: {selected_student['name']}")
        
    def delete_student(self):
        """
        Elimina el estudiante seleccionado
        """
        selected_student = self.student_list.get_selected_student()
        
        if not selected_student:
            messagebox.showwarning("Selección requerida", "Por favor selecciona un estudiante para eliminar")
            return
            
        # Confirmar eliminación
        if messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Estás seguro de que deseas eliminar a '{selected_student['name']}'?"
        ):
            # Eliminar de la lista
            self.students = [s for s in self.students if s['id'] != selected_student['id']]
            
            # Actualizar lista visual
            self.student_list.set_students_data(self.students)
            
            messagebox.showinfo("Éxito", "Estudiante eliminado correctamente")
            
    def clear_form(self):
        """
        Limpia el formulario
        """
        self.student_form.clear_form()
        
    def show_dialogs(self):
        """
        Demuestra diferentes tipos de diálogos
        """
        # Menú de opciones
        dialog_type = simpledialog.askstring(
            "Tipo de Diálogo",
            "¿Qué tipo de diálogo deseas ver?\n(info/warning/error/question/file)"
        )
        
        if not dialog_type:
            return
            
        dialog_type = dialog_type.lower()
        
        if dialog_type == "info":
            messagebox.showinfo("Información", "Este es un diálogo informativo")
        elif dialog_type == "warning":
            messagebox.showwarning("Advertencia", "Este es un diálogo de advertencia")
        elif dialog_type == "error":
            messagebox.showerror("Error", "Este es un diálogo de error")
        elif dialog_type == "question":
            result = messagebox.askyesno("Pregunta", "¿Te gusta esta aplicación?")
            response = "¡Excelente!" if result else "Trabajaremos para mejorar"
            messagebox.showinfo("Respuesta", response)
        elif dialog_type == "file":
            filename = filedialog.askopenfilename(
                title="Seleccionar archivo",
                filetypes=[("Todos los archivos", "*.*")]
            )
            if filename:
                messagebox.showinfo("Archivo", f"Seleccionaste: {filename}")
        else:
            messagebox.showwarning("Tipo no válido", "Tipo de diálogo no reconocido")
            
    def on_student_added(self, student_data):
        """
        Callback ejecutado cuando se agrega un estudiante
        
        Args:
            student_data: Datos del estudiante agregado
        """
        print(f"Estudiante agregado: {student_data}")
        
    def on_config_changed(self, config):
        """
        Callback ejecutado cuando cambia la configuración
        
        Args:
            config: Nueva configuración
        """
        print(f"Configuración cambiada: {config}")
        
        # Aplicar tema si cambió
        if 'theme' in config:
            self.apply_theme(config['theme'])
            
    def apply_theme(self, theme_name):
        """
        Aplica un tema a la aplicación
        
        Args:
            theme_name: Nombre del tema a aplicar
        """
        # Aquí se implementaría la lógica de cambio de tema
        print(f"Aplicando tema: {theme_name}")
        
    def on_closing(self):
        """
        Maneja el cierre de la aplicación
        """
        if self.students:
            if messagebox.askyesno(
                "Guardar cambios",
                f"Tienes {len(self.students)} estudiante(s) registrado(s).\n¿Deseas guardar antes de salir?"
            ):
                # Aquí se implementaría la lógica de guardado
                messagebox.showinfo("Guardado", "Datos guardados correctamente")
                
        if messagebox.askokcancel("Salir", "¿Deseas cerrar la aplicación?"):
            self.root.destroy()
            
    def get_student_count(self):
        """
        Obtiene el número total de estudiantes
        
        Returns:
            int: Número de estudiantes registrados
        """
        return len(self.students)
        
    def export_students(self):
        """
        Exporta la lista de estudiantes
        """
        if not self.students:
            messagebox.showwarning("Sin datos", "No hay estudiantes para exportar")
            return
            
        filename = filedialog.asksaveasfilename(
            title="Exportar estudiantes",
            defaultextension=".txt",
            filetypes=[("Archivo de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("Lista de Estudiantes\n")
                    f.write("=" * 50 + "\n\n")
                    
                    for student in self.students:
                        f.write(f"ID: {student['id']}\n")
                        f.write(f"Nombre: {student['name']}\n")
                        f.write(f"Email: {student['email']}\n")
                        f.write(f"Edad: {student['age']}\n")
                        f.write(f"Curso: {student['course']}\n")
                        f.write(f"Género: {student['gender']}\n")
                        f.write(f"Estado: {student['status']}\n")
                        f.write("-" * 30 + "\n")
                        
                messagebox.showinfo("Éxito", f"Estudiantes exportados a: {filename}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error al exportar: {str(e)}")
                
    def show_statistics(self):
        """
        Muestra estadísticas de los estudiantes
        """
        if not self.students:
            messagebox.showinfo("Estadísticas", "No hay estudiantes registrados")
            return
            
        # Calcular estadísticas básicas
        total = len(self.students)
        active = len([s for s in self.students if s['status'] == 'activo'])
        inactive = len([s for s in self.students if s['status'] == 'inactivo'])
        graduated = len([s for s in self.students if s['status'] == 'graduado'])
        
        # Edad promedio
        ages = [int(s['age']) for s in self.students if s['age'].isdigit()]
        avg_age = sum(ages) / len(ages) if ages else 0
        
        stats_text = f"""📊 Estadísticas de Estudiantes

Total de estudiantes: {total}

Por estado:
• Activos: {active}
• Inactivos: {inactive}
• Graduados: {graduated}

Edad promedio: {avg_age:.1f} años"""

        messagebox.showinfo("Estadísticas", stats_text)
