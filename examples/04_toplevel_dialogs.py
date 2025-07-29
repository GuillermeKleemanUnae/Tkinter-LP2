#!/usr/bin/env python3
"""
Demostración de Ventanas Secundarias y Diálogos
==============================================

Este script demuestra el uso de:
- tk.Toplevel (Ventanas secundarias/diálogos personalizados)
- messagebox (Diálogos estándar de mensaje)
- simpledialog (Diálogos de entrada de datos)
- filedialog (Diálogos de archivos)
- Modalidad y transient windows
- Comunicación entre ventanas

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, colorchooser
import os

class ToplevelsDialogDemo:
    """
    Clase que demuestra ventanas secundarias y diálogos
    """
    
    def __init__(self, root):
        """
        Inicializa la aplicación
        
        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.setup_window()
        self.init_variables()
        self.create_widgets()
        
        # Lista para mantener referencia a ventanas abiertas
        self.open_windows = []
        
    def setup_window(self):
        """
        Configura la ventana principal
        """
        self.root.title("Demostración: Ventanas Secundarias y Diálogos")
        self.root.geometry("600x700")
        self.root.configure(bg='#1E1E1E')
        self.root.resizable(True, True)
        
        # Centrar ventana
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def init_variables(self):
        """
        Inicializa variables para comunicación entre ventanas
        """
        self.shared_data = {
            'counter': 0,
            'user_name': 'Usuario',
            'selected_color': '#3498DB',
            'preferences': {
                'notifications': True,
                'auto_save': False,
                'theme': 'light'
            }
        }
        
    def create_widgets(self):
        """
        Crea la interfaz principal
        """
        # Frame principal
        main_frame = tk.Frame(
            self.root,
            bg='#1E1E1E',
            padx=20,
            pady=20
        )
        main_frame.pack(fill=tk.BOTH, expand=True)        # Título principal
        title_label = tk.Label(
            main_frame,
            text="🪟 Demostración de Ventanas y Diálogos",
            font=("Arial", 16, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        )
        title_label.pack(pady=(0, 20))
        
        # Crear secciones
        self.create_toplevel_section(main_frame)
        self.create_messagebox_section(main_frame)
        self.create_input_dialogs_section(main_frame)
        self.create_file_dialogs_section(main_frame)
        self.create_advanced_dialogs_section(main_frame)
        self.create_status_section(main_frame)
        
    def create_toplevel_section(self, parent):
        """
        Crea la sección de ventanas Toplevel
        """
        toplevel_frame = tk.LabelFrame(
            parent,
            text="🪟 Ventanas Secundarias (tk.Toplevel)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        toplevel_frame.pack(fill='x', pady=(0, 15))
        
        # Información
        tk.Label(
            toplevel_frame,
            text="Las ventanas Toplevel crean ventanas independientes con funcionalidad completa:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "italic")
        ).pack(anchor='w', pady=(0, 10))
        
        # Botones para diferentes tipos de ventanas
        buttons_frame = tk.Frame(toplevel_frame, bg='#2D2D30')
        buttons_frame.pack(fill='x')
        
        # Ventana básica
        basic_btn = tk.Button(
            buttons_frame,
            text="🪟 Ventana Básica",
            font=("Arial", 10),
            bg='#3498DB',
            fg='#2D2D30',
            activebackground='#2980B9',
            relief='raised',
            borderwidth=2,
            padx=15,
            pady=5,
            command=self.open_basic_window
        )
        basic_btn.pack(side='left', padx=(0, 10), pady=5)
        
        # Ventana modal
        modal_btn = tk.Button(
            buttons_frame,
            text="🔒 Ventana Modal",
            font=("Arial", 10),
            bg='#E74C3C',
            fg='#2D2D30',
            activebackground='#C0392B',
            relief='raised',
            borderwidth=2,
            padx=15,
            pady=5,
            command=self.open_modal_window
        )
        modal_btn.pack(side='left', padx=(0, 10), pady=5)
        
        # Ventana de configuración
        config_btn = tk.Button(
            buttons_frame,
            text="⚙️ Configuración",
            font=("Arial", 10),
            bg='#27AE60',
            fg='#2D2D30',
            activebackground='#229954',
            relief='raised',
            borderwidth=2,
            padx=15,
            pady=5,
            command=self.open_config_window
        )
        config_btn.pack(side='left', padx=(0, 10), pady=5)
        
        # Ventana con comunicación
        comm_btn = tk.Button(
            buttons_frame,
            text="🔄 Comunicación",
            font=("Arial", 10),
            bg='#8E44AD',
            fg='#2D2D30',
            activebackground='#7D3C98',
            relief='raised',
            borderwidth=2,
            padx=15,
            pady=5,
            command=self.open_communication_window
        )
        comm_btn.pack(side='left', pady=5)
        
    def create_messagebox_section(self, parent):
        """
        Crea la sección de MessageBox
        """
        msgbox_frame = tk.LabelFrame(
            parent,
            text="💬 Diálogos de Mensaje (messagebox)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        msgbox_frame.pack(fill='x', pady=(0, 15))
        
        # Grid para organizar botones
        msgbox_frame.grid_columnconfigure(0, weight=1)
        msgbox_frame.grid_columnconfigure(1, weight=1)
        msgbox_frame.grid_columnconfigure(2, weight=1)
        
        # Fila 1: Mensajes informativos
        tk.Button(
            msgbox_frame,
            text="ℹ️ Información",
            font=("Arial", 9),
            bg='#5DADE2',
            fg='#2D2D30',
            command=lambda: messagebox.showinfo("Información", "Este es un mensaje informativo"),
            width=15
        ).grid(row=0, column=0, padx=5, pady=3)
        
        tk.Button(
            msgbox_frame,
            text="⚠️ Advertencia",
            font=("Arial", 9),
            bg='#F7DC6F',
            fg='#FFFFFF',
            command=lambda: messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia"),
            width=15
        ).grid(row=0, column=1, padx=5, pady=3)
        
        tk.Button(
            msgbox_frame,
            text="❌ Error",
            font=("Arial", 9),
            bg='#EC7063',
            fg='#2D2D30',
            command=lambda: messagebox.showerror("Error", "Este es un mensaje de error"),
            width=15
        ).grid(row=0, column=2, padx=5, pady=3)
        
        # Fila 2: Preguntas
        tk.Button(
            msgbox_frame,
            text="❓ Sí/No",
            font=("Arial", 9),
            bg='#85C1E9',
            fg='#2D2D30',
            command=self.ask_yes_no,
            width=15
        ).grid(row=1, column=0, padx=5, pady=3)
        
        tk.Button(
            msgbox_frame,
            text="❔ OK/Cancel",
            font=("Arial", 9),
            bg='#82E0AA',
            fg='#2D2D30',
            command=self.ask_ok_cancel,
            width=15
        ).grid(row=1, column=1, padx=5, pady=3)
        
        tk.Button(
            msgbox_frame,
            text="🔄 Retry/Cancel",
            font=("Arial", 9),
            bg='#D7BDE2',
            fg='#2D2D30',
            command=self.ask_retry_cancel,
            width=15
        ).grid(row=1, column=2, padx=5, pady=3)
        
    def create_input_dialogs_section(self, parent):
        """
        Crea la sección de diálogos de entrada
        """
        input_frame = tk.LabelFrame(
            parent,
            text="⌨️ Diálogos de Entrada (simpledialog)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        input_frame.pack(fill='x', pady=(0, 15))
        
        # Botones para diferentes tipos de entrada
        input_buttons_frame = tk.Frame(input_frame, bg='#2D2D30')
        input_buttons_frame.pack(fill='x')
        
        tk.Button(
            input_buttons_frame,
            text="📝 Texto",
            font=("Arial", 10),
            bg='#58D68D',
            fg='#2D2D30',
            command=self.ask_string,
            width=12
        ).pack(side='left', padx=5, pady=5)
        
        tk.Button(
            input_buttons_frame,
            text="🔢 Entero",
            font=("Arial", 10),
            bg='#5DADE2',
            fg='#2D2D30',
            command=self.ask_integer,
            width=12
        ).pack(side='left', padx=5, pady=5)
        
        tk.Button(
            input_buttons_frame,
            text="🔢 Decimal",
            font=("Arial", 10),
            bg='#AF7AC5',
            fg='#2D2D30',
            command=self.ask_float,
            width=12
        ).pack(side='left', padx=5, pady=5)
        
        tk.Button(
            input_buttons_frame,
            text="🔐 Contraseña",
            font=("Arial", 10),
            bg='#EC7063',
            fg='#2D2D30',
            command=self.ask_password,
            width=12
        ).pack(side='left', padx=5, pady=5)
        
    def create_file_dialogs_section(self, parent):
        """
        Crea la sección de diálogos de archivos
        """
        file_frame = tk.LabelFrame(
            parent,
            text="📁 Diálogos de Archivos (filedialog)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        file_frame.pack(fill='x', pady=(0, 15))
        
        # Botones para operaciones de archivo
        file_buttons_frame = tk.Frame(file_frame, bg='#2D2D30')
        file_buttons_frame.pack(fill='x')
        
        tk.Button(
            file_buttons_frame,
            text="📂 Abrir Archivo",
            font=("Arial", 10),
            bg='#F39C12',
            fg='#2D2D30',
            command=self.open_file_dialog,
            width=15
        ).pack(side='left', padx=5, pady=5)
        
        tk.Button(
            file_buttons_frame,
            text="💾 Guardar Como",
            font=("Arial", 10),
            bg='#27AE60',
            fg='#2D2D30',
            command=self.save_file_dialog,
            width=15
        ).pack(side='left', padx=5, pady=5)
        
        tk.Button(
            file_buttons_frame,
            text="📁 Carpeta",
            font=("Arial", 10),
            bg='#3498DB',
            fg='#2D2D30',
            command=self.select_directory_dialog,
            width=15
        ).pack(side='left', padx=5, pady=5)
        
    def create_advanced_dialogs_section(self, parent):
        """
        Crea la sección de diálogos avanzados
        """
        advanced_frame = tk.LabelFrame(
            parent,
            text="🎨 Diálogos Avanzados",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        advanced_frame.pack(fill='x', pady=(0, 15))
        
        advanced_buttons_frame = tk.Frame(advanced_frame, bg='#2D2D30')
        advanced_buttons_frame.pack(fill='x')
        
        tk.Button(
            advanced_buttons_frame,
            text="🎨 Selector de Color",
            font=("Arial", 10),
            bg='#E91E63',
            fg='#2D2D30',
            command=self.choose_color,
            width=18
        ).pack(side='left', padx=5, pady=5)
        
        tk.Button(
            advanced_buttons_frame,
            text="📋 Diálogo Personalizado",
            font=("Arial", 10),
            bg='#9C27B0',
            fg='#2D2D30',
            command=self.custom_dialog,
            width=18
        ).pack(side='left', padx=5, pady=5)
        
    def create_status_section(self, parent):
        """
        Crea la sección de estado para mostrar resultados
        """
        status_frame = tk.LabelFrame(
            parent,
            text="📊 Estado y Resultados",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        status_frame.pack(fill='both', expand=True)
        
        # Área de texto para mostrar resultados
        self.status_text = tk.Text(
            status_frame,
            height=8,
            font=("Courier", 9),
            bg='#3C3C3C',
            fg='#FFFFFF',
            wrap=tk.WORD,
            borderwidth=2,
            relief='sunken'
        )
        self.status_text.pack(fill='both', expand=True, pady=(0, 10))
        
        # Scrollbar para el texto
        status_scrollbar = tk.Scrollbar(status_frame, command=self.status_text.yview)
        self.status_text.configure(yscrollcommand=status_scrollbar.set)
        
        # Botón para limpiar log
        tk.Button(
            status_frame,
            text="🧹 Limpiar Log",
            font=("Arial", 10),
            bg='#95A5A6',
            fg='#2D2D30',
            command=self.clear_log,
            width=15
        ).pack()
        
        # Mensaje inicial
        self.log_message("🚀 Aplicación iniciada. Prueba los diferentes tipos de diálogos y ventanas.")
        
    # ====================================================================
    # MÉTODOS PARA VENTANAS TOPLEVEL
    # ====================================================================
    
    def open_basic_window(self):
        """
        Abre una ventana básica no modal
        """
        window = tk.Toplevel(self.root)
        window.title("Ventana Básica")
        window.geometry("400x300")
        window.configure(bg='#2D2D30')
        
        # Centrar ventana
        self.center_window(window, 400, 300)
        
        # Contenido
        tk.Label(
            window,
            text="🪟 Ventana Básica No Modal",
            font=("Arial", 14, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(pady=20)
        
        tk.Label(
            window,
            text="Esta ventana es independiente.\nPuedes usar ambas ventanas al mismo tiempo.",
            font=("Arial", 11),
            bg='#2D2D30',
            fg='#FFFFFF',
            justify='center'
        ).pack(pady=10)
        
        # Counter para demostrar independencia
        counter_var = tk.IntVar(value=0)
        counter_label = tk.Label(
            window,
            textvariable=counter_var,
            font=("Arial", 16, "bold"),
            bg='#2D2D30',
            fg='#E74C3C'
        )
        counter_label.pack(pady=10)
        
        def increment():
            counter_var.set(counter_var.get() + 1)
            
        tk.Button(
            window,
            text="➕ Incrementar",
            font=("Arial", 11),
            bg='#3498DB',
            fg='#2D2D30',
            command=increment,
            padx=20,
            pady=5
        ).pack(pady=10)
        
        tk.Button(
            window,
            text="❌ Cerrar",
            font=("Arial", 11),
            bg='#E74C3C',
            fg='#2D2D30',
            command=window.destroy,
            padx=20,
            pady=5
        ).pack(pady=5)
        
        self.open_windows.append(window)
        self.log_message("✅ Ventana básica abierta")
        
    def open_modal_window(self):
        """
        Abre una ventana modal que bloquea la ventana principal
        """
        window = tk.Toplevel(self.root)
        window.title("Ventana Modal")
        window.geometry("350x250")
        window.configure(bg='#FADBD8')
        
        # Hacer modal
        window.transient(self.root)  # Ventana hija
        window.grab_set()  # Capturar todos los eventos
        window.focus_set()  # Enfocar
        
        # Centrar ventana
        self.center_window(window, 350, 250)
        
        # Contenido
        tk.Label(
            window,
            text="🔒 Ventana Modal",
            font=("Arial", 14, "bold"),
            bg='#FADBD8',
            fg='#FFFFFF'
        ).pack(pady=20)
        
        tk.Label(
            window,
            text="Esta ventana es MODAL.\nNo puedes usar la ventana principal\nhasta que cierres esta.",
            font=("Arial", 11),
            bg='#FADBD8',
            fg='#E74C3C',
            justify='center'
        ).pack(pady=15)
        
        def close_modal():
            window.grab_release()  # Liberar captura
            window.destroy()
            self.log_message("❌ Ventana modal cerrada")
            
        tk.Button(
            window,
            text="✅ Entendido",
            font=("Arial", 11, "bold"),
            bg='#27AE60',
            fg='#2D2D30',
            command=close_modal,
            padx=30,
            pady=8
        ).pack(pady=20)
        
        # Protocolo de cierre
        window.protocol("WM_DELETE_WINDOW", close_modal)
        
        self.log_message("🔒 Ventana modal abierta (bloquea ventana principal)")
        
    def open_config_window(self):
        """
        Abre una ventana de configuración con widgets funcionales
        """
        window = tk.Toplevel(self.root)
        window.title("Configuración")
        window.geometry("450x400")
        window.configure(bg='#E8F8F5')
        
        # Centrar ventana
        self.center_window(window, 450, 400)
        
        # Variables locales para la configuración
        notify_var = tk.BooleanVar(value=self.shared_data['preferences']['notifications'])
        autosave_var = tk.BooleanVar(value=self.shared_data['preferences']['auto_save'])
        theme_var = tk.StringVar(value=self.shared_data['preferences']['theme'])
        
        # Contenido
        tk.Label(
            window,
            text="⚙️ Configuración de la Aplicación",
            font=("Arial", 14, "bold"),
            bg='#E8F8F5',
            fg='#FFFFFF'
        ).pack(pady=15)
        
        # Frame para configuraciones
        config_frame = tk.Frame(window, bg='#E8F8F5')
        config_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Notificaciones
        tk.Checkbutton(
            config_frame,
            text="🔔 Habilitar notificaciones",
            variable=notify_var,
            font=("Arial", 11),
            bg='#E8F8F5',
            fg='#FFFFFF'
        ).pack(anchor='w', pady=5)
        
        # Auto guardado
        tk.Checkbutton(
            config_frame,
            text="💾 Guardado automático",
            variable=autosave_var,
            font=("Arial", 11),
            bg='#E8F8F5',
            fg='#FFFFFF'
        ).pack(anchor='w', pady=5)
        
        # Tema
        tk.Label(
            config_frame,
            text="🎨 Tema:",
            font=("Arial", 11, "bold"),
            bg='#E8F8F5',
            fg='#FFFFFF'
        ).pack(anchor='w', pady=(15, 5))
        
        theme_frame = tk.Frame(config_frame, bg='#E8F8F5')
        theme_frame.pack(anchor='w')
        
        for theme in ['light', 'dark', 'auto']:
            tk.Radiobutton(
                theme_frame,
                text=theme.capitalize(),
                variable=theme_var,
                value=theme,
                font=("Arial", 10),
                bg='#E8F8F5',
                fg='#FFFFFF'
            ).pack(side='left', padx=(0, 15))
            
        # Botones
        buttons_frame = tk.Frame(window, bg='#E8F8F5')
        buttons_frame.pack(fill='x', padx=20, pady=15)
        
        def save_config():
            self.shared_data['preferences']['notifications'] = notify_var.get()
            self.shared_data['preferences']['auto_save'] = autosave_var.get()
            self.shared_data['preferences']['theme'] = theme_var.get()
            self.log_message(f"💾 Configuración guardada: {self.shared_data['preferences']}")
            window.destroy()
            
        def cancel_config():
            self.log_message("❌ Configuración cancelada")
            window.destroy()
            
        tk.Button(
            buttons_frame,
            text="💾 Guardar",
            font=("Arial", 11, "bold"),
            bg='#27AE60',
            fg='#2D2D30',
            command=save_config,
            padx=20,
            pady=5
        ).pack(side='left', padx=(0, 10))
        
        tk.Button(
            buttons_frame,
            text="❌ Cancelar",
            font=("Arial", 11),
            bg='#E74C3C',
            fg='#2D2D30',
            command=cancel_config,
            padx=20,
            pady=5
        ).pack(side='left')
        
        self.log_message("⚙️ Ventana de configuración abierta")
        
    def open_communication_window(self):
        """
        Abre una ventana que demuestra comunicación entre ventanas
        """
        window = tk.Toplevel(self.root)
        window.title("Comunicación entre Ventanas")
        window.geometry("400x350")
        window.configure(bg='#F4ECF7')
        
        # Centrar ventana
        self.center_window(window, 400, 350)
        
        # Contenido
        tk.Label(
            window,
            text="🔄 Comunicación entre Ventanas",
            font=("Arial", 14, "bold"),
            bg='#F4ECF7',
            fg='#FFFFFF'
        ).pack(pady=15)
        
        # Mostrar datos compartidos
        data_frame = tk.Frame(window, bg='#2D2D30', relief='sunken', borderwidth=2)
        data_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(
            data_frame,
            text="📊 Datos Compartidos:",
            font=("Arial", 11, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(pady=5)
        
        # Variables para mostrar datos
        counter_label = tk.Label(data_frame, bg='#2D2D30', fg='#FFFFFF')
        user_label = tk.Label(data_frame, bg='#2D2D30', fg='#FFFFFF')
        color_label = tk.Label(data_frame, bg='#2D2D30', fg='#FFFFFF')
        
        def update_display():
            counter_label.config(text=f"Contador: {self.shared_data['counter']}")
            user_label.config(text=f"Usuario: {self.shared_data['user_name']}")
            color_label.config(text=f"Color: {self.shared_data['selected_color']}")
            
        update_display()
        counter_label.pack()
        user_label.pack()
        color_label.pack(pady=(0, 5))
        
        # Controles para modificar datos
        controls_frame = tk.Frame(window, bg='#F4ECF7')
        controls_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Button(
            controls_frame,
            text="➕ Incrementar Contador",
            font=("Arial", 10),
            bg='#3498DB',
            fg='#2D2D30',
            command=lambda: self.modify_shared_data('counter', 1, update_display),
            width=20
        ).pack(pady=3)
        
        tk.Button(
            controls_frame,
            text="👤 Cambiar Usuario",
            font=("Arial", 10),
            bg='#E67E22',
            fg='#2D2D30',
            command=lambda: self.change_user_name(update_display),
            width=20
        ).pack(pady=3)
        
        tk.Button(
            controls_frame,
            text="🎨 Cambiar Color",
            font=("Arial", 10),
            bg='#9B59B6',
            fg='#2D2D30',
            command=lambda: self.change_color(update_display),
            width=20
        ).pack(pady=3)
        
        tk.Button(
            controls_frame,
            text="🔄 Actualizar",
            font=("Arial", 10),
            bg='#27AE60',
            fg='#2D2D30',
            command=update_display,
            width=20
        ).pack(pady=10)
        
        self.log_message("🔄 Ventana de comunicación abierta")
        
    # ====================================================================
    # MÉTODOS PARA MESSAGEBOX
    # ====================================================================
    
    def ask_yes_no(self):
        """Demuestra messagebox.askyesno"""
        result = messagebox.askyesno(
            "Pregunta",
            "¿Te gusta esta demostración de diálogos?\n\n¡Tu respuesta se registrará en el log!"
        )
        response = "¡Excelente! 😊" if result else "Trabajaremos para mejorar 😔"
        self.log_message(f"❓ Pregunta Sí/No: {'Sí' if result else 'No'} - {response}")
        
    def ask_ok_cancel(self):
        """Demuestra messagebox.askokcancel"""
        result = messagebox.askokcancel(
            "Confirmación",
            "¿Deseas continuar con la operación?\n\nEsta acción se registrará en el log."
        )
        status = "confirmada" if result else "cancelada"
        self.log_message(f"❔ Operación {status}")
        
    def ask_retry_cancel(self):
        """Demuestra messagebox.askretrycancel"""
        result = messagebox.askretrycancel(
            "Error Simulado",
            "Error al conectar con el servidor.\n\n¿Deseas reintentar la conexión?"
        )
        action = "Reintentando conexión..." if result else "Conexión cancelada"
        self.log_message(f"🔄 {action}")
        
    # ====================================================================
    # MÉTODOS PARA SIMPLEDIALOG
    # ====================================================================
    
    def ask_string(self):
        """Solicita entrada de texto"""
        result = simpledialog.askstring(
            "Entrada de Texto",
            "¿Cuál es tu nombre completo?",
            initialvalue=self.shared_data['user_name']
        )
        if result:
            self.shared_data['user_name'] = result
            self.log_message(f"📝 Nombre ingresado: '{result}'")
        else:
            self.log_message("📝 Entrada de texto cancelada")
            
    def ask_integer(self):
        """Solicita entrada de número entero"""
        result = simpledialog.askinteger(
            "Entrada Numérica",
            "Ingresa tu edad:",
            minvalue=1,
            maxvalue=120,
            initialvalue=25
        )
        if result is not None:
            self.log_message(f"🔢 Edad ingresada: {result} años")
        else:
            self.log_message("🔢 Entrada numérica cancelada")
            
    def ask_float(self):
        """Solicita entrada de número decimal"""
        result = simpledialog.askfloat(
            "Entrada Decimal",
            "Ingresa tu altura en metros:",
            minvalue=0.5,
            maxvalue=3.0,
            initialvalue=1.75
        )
        if result is not None:
            self.log_message(f"🔢 Altura ingresada: {result:.2f} metros")
        else:
            self.log_message("🔢 Entrada decimal cancelada")
            
    def ask_password(self):
        """Simula entrada de contraseña"""
        result = simpledialog.askstring(
            "Contraseña",
            "Ingresa una contraseña:",
            show='*'
        )
        if result:
            self.log_message(f"🔐 Contraseña ingresada (longitud: {len(result)} caracteres)")
        else:
            self.log_message("🔐 Entrada de contraseña cancelada")
            
    # ====================================================================
    # MÉTODOS PARA FILEDIALOG
    # ====================================================================
    
    def open_file_dialog(self):
        """Abre diálogo para seleccionar archivo"""
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Archivos Python", "*.py"),
                ("Archivos de imagen", "*.png *.jpg *.jpeg *.gif"),
                ("Todos los archivos", "*.*")
            ],
            initialdir=os.path.expanduser("~")
        )
        if filename:
            file_size = os.path.getsize(filename) if os.path.exists(filename) else 0
            self.log_message(f"📂 Archivo seleccionado: {os.path.basename(filename)} ({file_size} bytes)")
        else:
            self.log_message("📂 Selección de archivo cancelada")
            
    def save_file_dialog(self):
        """Abre diálogo para guardar archivo"""
        filename = filedialog.asksaveasfilename(
            title="Guardar archivo como",
            defaultextension=".txt",
            filetypes=[
                ("Archivo de texto", "*.txt"),
                ("Archivo Python", "*.py"),
                ("Todos los archivos", "*.*")
            ],
            initialdir=os.path.expanduser("~")
        )
        if filename:
            self.log_message(f"💾 Archivo para guardar: {os.path.basename(filename)}")
            # Simular guardado
            try:
                with open(filename, 'w') as f:
                    f.write("Archivo de demostración creado por tkinter\n")
                    f.write(f"Fecha: {tk.datetime.datetime.now()}\n")
                self.log_message(f"✅ Archivo guardado exitosamente")
            except Exception as e:
                self.log_message(f"❌ Error al guardar: {str(e)}")
        else:
            self.log_message("💾 Guardado de archivo cancelado")
            
    def select_directory_dialog(self):
        """Abre diálogo para seleccionar carpeta"""
        directory = filedialog.askdirectory(
            title="Seleccionar carpeta",
            initialdir=os.path.expanduser("~")
        )
        if directory:
            try:
                file_count = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
                self.log_message(f"📁 Carpeta seleccionada: {os.path.basename(directory)} ({file_count} archivos)")
            except:
                self.log_message(f"📁 Carpeta seleccionada: {os.path.basename(directory)}")
        else:
            self.log_message("📁 Selección de carpeta cancelada")
            
    # ====================================================================
    # MÉTODOS PARA DIÁLOGOS AVANZADOS
    # ====================================================================
    
    def choose_color(self):
        """Abre selector de color"""
        color = colorchooser.askcolor(
            title="Seleccionar Color",
            initialcolor=self.shared_data['selected_color']
        )
        if color[1]:  # color[1] es el valor hexadecimal
            self.shared_data['selected_color'] = color[1]
            rgb = color[0]
            self.log_message(f"🎨 Color seleccionado: {color[1]} (RGB: {rgb})")
        else:
            self.log_message("🎨 Selección de color cancelada")
            
    def custom_dialog(self):
        """Crea un diálogo personalizado complejo"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Diálogo Personalizado")
        dialog.geometry("400x300")
        dialog.configure(bg='#FFF3E0')
        dialog.resizable(False, False)
        
        # Hacer modal
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Centrar
        self.center_window(dialog, 400, 300)
        
        # Variables
        name_var = tk.StringVar()
        age_var = tk.IntVar(value=25)
        gender_var = tk.StringVar(value="otro")
        
        # Contenido
        tk.Label(
            dialog,
            text="📋 Formulario Personalizado",
            font=("Arial", 14, "bold"),
            bg='#FFF3E0',
            fg='#FFFFFF'
        ).pack(pady=15)
        
        # Frame para formulario
        form_frame = tk.Frame(dialog, bg='#FFF3E0')
        form_frame.pack(fill='both', expand=True, padx=30)
        
        # Nombre
        tk.Label(form_frame, text="Nombre:", bg='#FFF3E0', font=("Arial", 10, "bold")).pack(anchor='w')
        tk.Entry(form_frame, textvariable=name_var, font=("Arial", 11), width=30).pack(fill='x', pady=(0, 10))
        
        # Edad
        tk.Label(form_frame, text="Edad:", bg='#FFF3E0', font=("Arial", 10, "bold")).pack(anchor='w')
        age_frame = tk.Frame(form_frame, bg='#FFF3E0')
        age_frame.pack(fill='x', pady=(0, 10))
        tk.Scale(
            age_frame,
            from_=1,
            to=100,
            orient='horizontal',
            variable=age_var,
            bg='#FFF3E0'
        ).pack(fill='x')
        
        # Género
        tk.Label(form_frame, text="Género:", bg='#FFF3E0', font=("Arial", 10, "bold")).pack(anchor='w')
        gender_frame = tk.Frame(form_frame, bg='#FFF3E0')
        gender_frame.pack(anchor='w', pady=(0, 15))
        
        for value, text in [("masculino", "Masculino"), ("femenino", "Femenino"), ("otro", "Otro")]:
            tk.Radiobutton(
                gender_frame,
                text=text,
                variable=gender_var,
                value=value,
                bg='#FFF3E0'
            ).pack(side='left', padx=(0, 15))
            
        # Botones
        def submit():
            data = {
                'nombre': name_var.get(),
                'edad': age_var.get(),
                'genero': gender_var.get()
            }
            self.log_message(f"📋 Formulario enviado: {data}")
            dialog.grab_release()
            dialog.destroy()
            
        def cancel():
            self.log_message("📋 Formulario cancelado")
            dialog.grab_release()
            dialog.destroy()
            
        button_frame = tk.Frame(dialog, bg='#FFF3E0')
        button_frame.pack(fill='x', padx=30, pady=15)
        
        tk.Button(
            button_frame,
            text="✅ Enviar",
            command=submit,
            bg='#4CAF50',
            fg='#2D2D30',
            font=("Arial", 11, "bold"),
            padx=20
        ).pack(side='left', padx=(0, 10))
        
        tk.Button(
            button_frame,
            text="❌ Cancelar",
            command=cancel,
            bg='#F44336',
            fg='#2D2D30',
            font=("Arial", 11),
            padx=20
        ).pack(side='left')
        
        self.log_message("📋 Diálogo personalizado abierto")
        
    # ====================================================================
    # MÉTODOS AUXILIARES
    # ====================================================================
    
    def center_window(self, window, width, height):
        """Centra una ventana en la pantalla"""
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')
        
    def modify_shared_data(self, key, increment, callback):
        """Modifica datos compartidos"""
        self.shared_data[key] += increment
        callback()
        self.log_message(f"🔄 {key} modificado: {self.shared_data[key]}")
        
    def change_user_name(self, callback):
        """Cambia el nombre de usuario"""
        new_name = simpledialog.askstring(
            "Cambiar Usuario",
            "Nuevo nombre de usuario:",
            initialvalue=self.shared_data['user_name']
        )
        if new_name:
            self.shared_data['user_name'] = new_name
            callback()
            self.log_message(f"👤 Usuario cambiado a: {new_name}")
            
    def change_color(self, callback):
        """Cambia el color seleccionado"""
        color = colorchooser.askcolor(
            title="Seleccionar Nuevo Color",
            initialcolor=self.shared_data['selected_color']
        )
        if color[1]:
            self.shared_data['selected_color'] = color[1]
            callback()
            self.log_message(f"🎨 Color cambiado a: {color[1]}")
            
    def log_message(self, message):
        """Registra un mensaje en el log"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.status_text.insert(tk.END, log_entry)
        self.status_text.see(tk.END)  # Scroll automático
        
    def clear_log(self):
        """Limpia el log de mensajes"""
        self.status_text.delete(1.0, tk.END)
        self.log_message("🧹 Log limpiado")

def main():
    """
    Función principal para ejecutar la demostración
    """
    root = tk.Tk()
    app = ToplevelsDialogDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
