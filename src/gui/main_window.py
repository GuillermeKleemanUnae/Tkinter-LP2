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
from tkinter import messagebox, filedialog, simpledialog, colorchooser
import os
import datetime
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
        
        # Variables para funcionalidades avanzadas
        self.open_windows = []
        self.app_settings = {
            'theme': 'dark',
            'notifications': True,
            'auto_save': False,
            'selected_color': '#0078D4',
            'export_format': 'json'
        }
        
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
        
        # Botón configuración avanzada
        advanced_config_btn = tk.Button(
            button_container,
            text="⚙️ Configuración",
            font=("Arial", 11),
            bg='#FF9800',
            fg='white',
            activebackground='#F57C00',
            activeforeground='white',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.open_advanced_config
        )
        advanced_config_btn.pack(side='left', padx=5)
        
        # Botón exportar datos
        export_btn = tk.Button(
            button_container,
            text="📤 Exportar",
            font=("Arial", 11),
            bg='#795548',
            fg='white',
            activebackground='#5D4037',
            activeforeground='white',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.export_data
        )
        export_btn.pack(side='left', padx=5)
        
        # Botón estadísticas
        stats_btn = tk.Button(
            button_container,
            text="📊 Estadísticas",
            font=("Arial", 11),
            bg='#607D8B',
            fg='white',
            activebackground='#455A64',
            activeforeground='white',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.show_statistics
        )
        stats_btn.pack(side='left', padx=5)
        
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
        
    def open_advanced_config(self):
        """
        Abre ventana de configuración avanzada con múltiples opciones
        """
        config_window = tk.Toplevel(self.root)
        config_window.title("⚙️ Configuración Avanzada")
        config_window.geometry("500x600")
        config_window.configure(bg='#1E1E1E')
        config_window.resizable(False, False)
        
        # Hacer ventana modal
        config_window.transient(self.root)
        config_window.grab_set()
        
        # Centrar ventana
        self.center_modal_window(config_window, 500, 600)
        
        # Variables locales para configuración
        theme_var = tk.StringVar(value=self.app_settings['theme'])
        notifications_var = tk.BooleanVar(value=self.app_settings['notifications'])
        auto_save_var = tk.BooleanVar(value=self.app_settings['auto_save'])
        export_format_var = tk.StringVar(value=self.app_settings['export_format'])
        
        # Header
        header_frame = tk.Frame(config_window, bg='#2D2D30', relief='raised', borderwidth=2)
        header_frame.pack(fill='x', padx=10, pady=(10, 0))
        
        tk.Label(
            header_frame,
            text="⚙️ Configuración Avanzada del Sistema",
            font=("Arial", 16, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            pady=15
        ).pack()
        
        # Notebook para organizar configuraciones
        from tkinter import ttk
        notebook = ttk.Notebook(config_window)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === TAB 1: APARIENCIA ===
        appearance_frame = tk.Frame(notebook, bg='#1E1E1E')
        notebook.add(appearance_frame, text="🎨 Apariencia")
        
        # Tema
        theme_group = tk.LabelFrame(
            appearance_frame,
            text="🌓 Tema de la Aplicación",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        theme_group.pack(fill='x', padx=10, pady=10)
        
        for theme in ['light', 'dark', 'auto']:
            tk.Radiobutton(
                theme_group,
                text=f"{theme.capitalize()}",
                variable=theme_var,
                value=theme,
                font=("Arial", 11),
                bg='#2D2D30',
                fg='#FFFFFF',
                selectcolor='#0078D4'
            ).pack(anchor='w', pady=2)
            
        # Color personalizado
        color_group = tk.LabelFrame(
            appearance_frame,
            text="🎨 Color Principal",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        color_group.pack(fill='x', padx=10, pady=10)
        
        color_display = tk.Label(
            color_group,
            text="■ Color Actual",
            font=("Arial", 11),
            bg='#2D2D30',
            fg=self.app_settings['selected_color']
        )
        color_display.pack(anchor='w', pady=5)
        
        tk.Button(
            color_group,
            text="🎨 Cambiar Color",
            font=("Arial", 10),
            bg='#9C27B0',
            fg='white',
            command=lambda: self.change_app_color(color_display),
            width=15
        ).pack(anchor='w', pady=5)
        
        # === TAB 2: COMPORTAMIENTO ===
        behavior_frame = tk.Frame(notebook, bg='#1E1E1E')
        notebook.add(behavior_frame, text="⚙️ Comportamiento")
        
        # Opciones de comportamiento
        behavior_group = tk.LabelFrame(
            behavior_frame,
            text="🔔 Opciones Generales",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        behavior_group.pack(fill='x', padx=10, pady=10)
        
        tk.Checkbutton(
            behavior_group,
            text="🔔 Habilitar notificaciones",
            variable=notifications_var,
            font=("Arial", 11),
            bg='#2D2D30',
            fg='#FFFFFF',
            selectcolor='#4CAF50'
        ).pack(anchor='w', pady=5)
        
        tk.Checkbutton(
            behavior_group,
            text="💾 Guardado automático",
            variable=auto_save_var,
            font=("Arial", 11),
            bg='#2D2D30',
            fg='#FFFFFF',
            selectcolor='#4CAF50'
        ).pack(anchor='w', pady=5)
        
        # === TAB 3: EXPORTACIÓN ===
        export_frame = tk.Frame(notebook, bg='#1E1E1E')
        notebook.add(export_frame, text="📤 Exportación")
        
        export_group = tk.LabelFrame(
            export_frame,
            text="📁 Formato de Exportación",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        export_group.pack(fill='x', padx=10, pady=10)
        
        formats = [
            ('json', 'JSON (JavaScript Object Notation)'),
            ('csv', 'CSV (Comma Separated Values)'),
            ('xml', 'XML (eXtensible Markup Language)'),
            ('txt', 'TXT (Texto Plano)')
        ]
        
        for value, text in formats:
            tk.Radiobutton(
                export_group,
                text=text,
                variable=export_format_var,
                value=value,
                font=("Arial", 10),
                bg='#2D2D30',
                fg='#FFFFFF',
                selectcolor='#0078D4'
            ).pack(anchor='w', pady=2)
        
        # Botones de acción
        button_frame = tk.Frame(config_window, bg='#1E1E1E')
        button_frame.pack(fill='x', padx=10, pady=10)
        
        def save_config():
            self.app_settings['theme'] = theme_var.get()
            self.app_settings['notifications'] = notifications_var.get()
            self.app_settings['auto_save'] = auto_save_var.get()
            self.app_settings['export_format'] = export_format_var.get()
            
            config_window.grab_release()
            config_window.destroy()
            messagebox.showinfo("Configuración", "✅ Configuración guardada correctamente")
            
        def reset_config():
            if messagebox.askyesno("Restablecer", "¿Restablecer configuración por defecto?"):
                self.app_settings = {
                    'theme': 'dark',
                    'notifications': True,
                    'auto_save': False,
                    'selected_color': '#0078D4',
                    'export_format': 'json'
                }
                config_window.grab_release()
                config_window.destroy()
                messagebox.showinfo("Configuración", "🔄 Configuración restablecida")
                
        def cancel_config():
            config_window.grab_release()
            config_window.destroy()
        
        tk.Button(
            button_frame,
            text="💾 Guardar",
            font=("Arial", 11, "bold"),
            bg='#4CAF50',
            fg='white',
            command=save_config,
            padx=20,
            pady=8
        ).pack(side='left', padx=5)
        
        tk.Button(
            button_frame,
            text="🔄 Restablecer",
            font=("Arial", 11),
            bg='#FF9800',
            fg='white',
            command=reset_config,
            padx=20,
            pady=8
        ).pack(side='left', padx=5)
        
        tk.Button(
            button_frame,
            text="❌ Cancelar",
            font=("Arial", 11),
            bg='#F44336',
            fg='white',
            command=cancel_config,
            padx=20,
            pady=8
        ).pack(side='left', padx=5)
        
        self.open_windows.append(config_window)
        
    def change_app_color(self, color_display):
        """
        Cambia el color principal de la aplicación
        """
        color = colorchooser.askcolor(
            title="Seleccionar Color Principal",
            initialcolor=self.app_settings['selected_color']
        )
        if color[1]:
            self.app_settings['selected_color'] = color[1]
            color_display.config(fg=color[1])
            
    def export_data(self):
        """
        Exporta datos de estudiantes con selector de formato
        """
        if not self.students:
            messagebox.showwarning("Exportar", "No hay datos para exportar")
            return
            
        # Ventana de opciones de exportación
        export_window = tk.Toplevel(self.root)
        export_window.title("📤 Exportar Datos")
        export_window.geometry("400x300")
        export_window.configure(bg='#1E1E1E')
        export_window.resizable(False, False)
        
        # Hacer modal
        export_window.transient(self.root)
        export_window.grab_set()
        
        # Centrar ventana
        self.center_modal_window(export_window, 400, 300)
        
        # Header
        tk.Label(
            export_window,
            text="📤 Exportar Datos de Estudiantes",
            font=("Arial", 14, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        ).pack(pady=15)
        
        # Opciones de exportación
        options_frame = tk.LabelFrame(
            export_window,
            text="📁 Opciones de Exportación",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        options_frame.pack(fill='x', padx=20, pady=10)
        
        # Variables
        format_var = tk.StringVar(value=self.app_settings['export_format'])
        include_inactive = tk.BooleanVar(value=True)
        include_stats = tk.BooleanVar(value=True)
        
        # Formato
        tk.Label(
            options_frame,
            text="Formato:",
            font=("Arial", 11, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(anchor='w')
        
        formats_frame = tk.Frame(options_frame, bg='#2D2D30')
        formats_frame.pack(fill='x', pady=5)
        
        for fmt in ['json', 'csv', 'xml']:
            tk.Radiobutton(
                formats_frame,
                text=fmt.upper(),
                variable=format_var,
                value=fmt,
                font=("Arial", 10),
                bg='#2D2D30',
                fg='#FFFFFF',
                selectcolor='#0078D4'
            ).pack(side='left', padx=(0, 15))
            
        # Opciones adicionales
        tk.Checkbutton(
            options_frame,
            text="📊 Incluir estudiantes inactivos",
            variable=include_inactive,
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#FFFFFF',
            selectcolor='#4CAF50'
        ).pack(anchor='w', pady=(10, 2))
        
        tk.Checkbutton(
            options_frame,
            text="📈 Incluir estadísticas",
            variable=include_stats,
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#FFFFFF',
            selectcolor='#4CAF50'
        ).pack(anchor='w', pady=2)
        
        # Botones
        def perform_export():
            filename = filedialog.asksaveasfilename(
                title="Guardar exportación",
                defaultextension=f".{format_var.get()}",
                filetypes=[
                    (f"Archivos {format_var.get().upper()}", f"*.{format_var.get()}"),
                    ("Todos los archivos", "*.*")
                ]
            )
            
            if filename:
                try:
                    # Filtrar datos
                    export_data = self.students.copy()
                    if not include_inactive.get():
                        export_data = [s for s in export_data if s.get('status', '').lower() == 'activo']
                    
                    # Exportar según formato
                    if format_var.get() == 'json':
                        import json
                        export_dict = {
                            'students': export_data,
                            'total': len(export_data),
                            'exported_at': datetime.datetime.now().isoformat()
                        }
                        if include_stats.get():
                            export_dict['statistics'] = self.calculate_stats(export_data)
                        
                        with open(filename, 'w', encoding='utf-8') as f:
                            json.dump(export_dict, f, indent=2, ensure_ascii=False)
                            
                    elif format_var.get() == 'csv':
                        import csv
                        with open(filename, 'w', newline='', encoding='utf-8') as f:
                            if export_data:
                                writer = csv.DictWriter(f, fieldnames=export_data[0].keys())
                                writer.writeheader()
                                writer.writerows(export_data)
                                
                    elif format_var.get() == 'xml':
                        with open(filename, 'w', encoding='utf-8') as f:
                            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                            f.write('<students>\n')
                            for student in export_data:
                                f.write('  <student>\n')
                                for key, value in student.items():
                                    f.write(f'    <{key}>{value}</{key}>\n')
                                f.write('  </student>\n')
                            f.write('</students>\n')
                    
                    export_window.grab_release()
                    export_window.destroy()
                    messagebox.showinfo("Exportar", f"✅ Datos exportados exitosamente a:\n{filename}")
                    
                except Exception as e:
                    messagebox.showerror("Error", f"❌ Error al exportar: {str(e)}")
            
        button_frame = tk.Frame(export_window, bg='#1E1E1E')
        button_frame.pack(fill='x', padx=20, pady=15)
        
        tk.Button(
            button_frame,
            text="📤 Exportar",
            font=("Arial", 11, "bold"),
            bg='#4CAF50',
            fg='white',
            command=perform_export,
            padx=20,
            pady=8
        ).pack(side='left', padx=5)
        
        tk.Button(
            button_frame,
            text="❌ Cancelar",
            font=("Arial", 11),
            bg='#F44336',
            fg='white',
            command=lambda: (export_window.grab_release(), export_window.destroy()),
            padx=20,
            pady=8
        ).pack(side='left', padx=5)
        
        self.open_windows.append(export_window)
        
    def show_statistics(self):
        """
        Muestra ventana con estadísticas detalladas
        """
        if not self.students:
            messagebox.showinfo("Estadísticas", "No hay estudiantes registrados")
            return
            
        # Ventana de estadísticas
        stats_window = tk.Toplevel(self.root)
        stats_window.title("📊 Estadísticas Detalladas")
        stats_window.geometry("600x500")
        stats_window.configure(bg='#1E1E1E')
        
        # Centrar ventana
        self.center_modal_window(stats_window, 600, 500)
        
        # Header
        tk.Label(
            stats_window,
            text="📊 Dashboard de Estadísticas",
            font=("Arial", 16, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        ).pack(pady=15)
        
        # Frame principal con scroll
        from tkinter import ttk
        
        # Crear notebook para diferentes estadísticas
        notebook = ttk.Notebook(stats_window)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === TAB 1: RESUMEN GENERAL ===
        general_frame = tk.Frame(notebook, bg='#1E1E1E')
        notebook.add(general_frame, text="📈 General")
        
        stats = self.calculate_detailed_stats()
        
        # Mostrar estadísticas generales
        general_text = tk.Text(
            general_frame,
            font=("Courier", 10),
            bg='#2D2D30',
            fg='#FFFFFF',
            wrap=tk.WORD,
            height=20
        )
        general_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        general_content = f"""📊 RESUMEN GENERAL DE ESTUDIANTES
{'='*50}

📋 TOTALES:
   • Total de estudiantes: {stats['total']}
   • Estudiantes activos: {stats['active']}
   • Estudiantes inactivos: {stats['inactive']}
   • Estudiantes graduados: {stats['graduated']}

📊 DISTRIBUCIÓN POR ESTADO:
   • Activos: {stats['active_percent']:.1f}%
   • Inactivos: {stats['inactive_percent']:.1f}%
   • Graduados: {stats['graduated_percent']:.1f}%

👥 INFORMACIÓN DEMOGRÁFICA:
   • Edad promedio: {stats['avg_age']:.1f} años
   • Edad mínima: {stats['min_age']} años
   • Edad máxima: {stats['max_age']} años

📚 CURSOS POPULARES:
"""
        
        for course, count in stats['courses'].items():
            general_content += f"   • {course}: {count} estudiantes\n"
            
        general_content += f"""
👫 DISTRIBUCIÓN POR GÉNERO:
"""
        for gender, count in stats['genders'].items():
            general_content += f"   • {gender.title()}: {count} estudiantes\n"
            
        general_text.insert(tk.END, general_content)
        general_text.config(state='disabled')
        
        # === TAB 2: GRÁFICOS ===
        charts_frame = tk.Frame(notebook, bg='#1E1E1E')
        notebook.add(charts_frame, text="📊 Gráficos")
        
        # Crear gráfico simple con caracteres
        chart_text = tk.Text(
            charts_frame,
            font=("Courier", 9),
            bg='#2D2D30',
            fg='#FFFFFF',
            wrap=tk.NONE,
            height=25
        )
        chart_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Gráfico de barras ASCII
        chart_content = f"""📊 GRÁFICOS DE DISTRIBUCIÓN
{'='*60}

📈 ESTUDIANTES POR ESTADO:
"""
        
        max_val = max(stats['active'], stats['inactive'], stats['graduated']) if stats['total'] > 0 else 1
        scale = 30 / max_val if max_val > 0 else 1
        
        statuses = [
            ('Activos', stats['active'], '🟢'),
            ('Inactivos', stats['inactive'], '🔴'),
            ('Graduados', stats['graduated'], '🔵')
        ]
        
        for status, count, emoji in statuses:
            bar_length = int(count * scale)
            bar = '█' * bar_length
            chart_content += f"\n{status:12} {emoji} |{bar:<30}| {count:>3}"
            
        chart_content += f"""

📊 DISTRIBUCIÓN POR CURSOS:
"""
        
        if stats['courses']:
            max_course = max(stats['courses'].values())
            course_scale = 25 / max_course if max_course > 0 else 1
            
            for course, count in sorted(stats['courses'].items()):
                bar_length = int(count * course_scale)
                bar = '■' * bar_length
                chart_content += f"\n{course[:15]:15} |{bar:<25}| {count:>2}"
                
        chart_text.insert(tk.END, chart_content)
        chart_text.config(state='disabled')
        
        # Botón cerrar
        tk.Button(
            stats_window,
            text="❌ Cerrar",
            font=("Arial", 11),
            bg='#F44336',
            fg='white',
            command=stats_window.destroy,
            padx=30,
            pady=8
        ).pack(pady=10)
        
        self.open_windows.append(stats_window)
        
    def calculate_detailed_stats(self):
        """
        Calcula estadísticas detalladas de los estudiantes
        """
        if not self.students:
            return {}
            
        total = len(self.students)
        active = len([s for s in self.students if s.get('status', '').lower() == 'activo'])
        inactive = len([s for s in self.students if s.get('status', '').lower() == 'inactivo'])
        graduated = len([s for s in self.students if s.get('status', '').lower() == 'graduado'])
        
        # Edades
        ages = []
        for s in self.students:
            try:
                age = int(s.get('age', 0))
                if age > 0:
                    ages.append(age)
            except (ValueError, TypeError):
                pass
                
        # Cursos
        courses = {}
        for s in self.students:
            course = s.get('course', 'Sin especificar')
            courses[course] = courses.get(course, 0) + 1
            
        # Géneros
        genders = {}
        for s in self.students:
            gender = s.get('gender', 'no especificado')
            genders[gender] = genders.get(gender, 0) + 1
        
        return {
            'total': total,
            'active': active,
            'inactive': inactive,
            'graduated': graduated,
            'active_percent': (active / total * 100) if total > 0 else 0,
            'inactive_percent': (inactive / total * 100) if total > 0 else 0,
            'graduated_percent': (graduated / total * 100) if total > 0 else 0,
            'avg_age': sum(ages) / len(ages) if ages else 0,
            'min_age': min(ages) if ages else 0,
            'max_age': max(ages) if ages else 0,
            'courses': courses,
            'genders': genders
        }
        
    def calculate_stats(self, student_list):
        """
        Calcula estadísticas básicas para exportación
        """
        total = len(student_list)
        if total == 0:
            return {}
            
        active = len([s for s in student_list if s.get('status', '').lower() == 'activo'])
        
        ages = []
        for s in student_list:
            try:
                age = int(s.get('age', 0))
                if age > 0:
                    ages.append(age)
            except (ValueError, TypeError):
                pass
                
        return {
            'total_students': total,
            'active_students': active,
            'average_age': sum(ages) / len(ages) if ages else 0,
            'age_range': {'min': min(ages), 'max': max(ages)} if ages else None
        }
        
    def center_modal_window(self, window, width, height):
        """
        Centra una ventana modal en la pantalla
        """
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')
