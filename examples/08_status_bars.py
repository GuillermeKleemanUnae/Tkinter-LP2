#!/usr/bin/env python3
"""
Barras de Estado y Elementos de Información en Tkinter
=====================================================

Este script demuestra:
1. Creación de barras de estado simples y complejas
2. Información dinámica y actualización en tiempo real
3. Múltiples paneles de estado
4. Indicadores visuales (progreso, estado, notificaciones)
5. Integración con eventos de la aplicación
6. Barras de progreso y medidores
7. Tooltips y ayuda contextual

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import threading
import time
import random

class StatusBarDemo:
    """
    Clase que demuestra barras de estado en Tkinter
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
        self.create_main_interface()
        self.start_background_processes()
        
    def setup_window(self):
        """
        Configura la ventana principal
        """
        self.root.title("📊 Barras de Estado en Tkinter")
        self.root.geometry("1000x800")
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
        Inicializa variables de la aplicación
        """
        # Variables para información de estado
        self.current_time = tk.StringVar()
        self.app_status = tk.StringVar(value="🟢 Listo")
        self.cpu_usage = tk.DoubleVar(value=0.0)
        self.memory_usage = tk.DoubleVar(value=0.0)
        self.network_status = tk.StringVar(value="🌐 Conectado")
        
        # Variables de progreso
        self.task_progress = tk.DoubleVar(value=0.0)
        self.download_progress = tk.DoubleVar(value=0.0)
        
        # Contadores de actividad
        self.documents_count = tk.IntVar(value=3)
        self.unsaved_changes = tk.BooleanVar(value=False)
        self.notifications_count = tk.IntVar(value=0)
        
        # Variables de configuración
        self.show_time = tk.BooleanVar(value=True)
        self.show_system_info = tk.BooleanVar(value=True)
        self.show_progress = tk.BooleanVar(value=True)
        
        # Estados de simulación
        self.is_processing = False
        self.is_downloading = False
        self.current_file = "documento.txt"
        self.zoom_level = 100
        
    def create_main_interface(self):
        """
        Crea la interfaz principal con múltiples barras de estado
        """
        # Título principal
        title_label = tk.Label(
            self.root,
            text="📊 Barras de Estado - Demostración Completa",
            font=("Arial", 16, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        )
        title_label.pack(pady=15)
        
        # Frame principal para contenido
        main_content_frame = tk.Frame(self.root, bg='#1E1E1E')
        main_content_frame.pack(fill='both', expand=True, padx=10, pady=(0, 10))
        
        # Crear notebook para diferentes ejemplos
        self.notebook = ttk.Notebook(main_content_frame)
        self.notebook.pack(fill='both', expand=True)
        
        # Crear pestañas de ejemplos
        self.create_simple_status_tab()
        self.create_advanced_status_tab()
        self.create_realtime_status_tab()
        self.create_progress_status_tab()
        
        # === BARRA DE ESTADO PRINCIPAL (SIEMPRE VISIBLE) ===
        self.create_main_status_bar()
        
        # === BARRA DE ESTADO SECUNDARIA ===
        self.create_secondary_status_bar()
        
        # === BARRA DE PROGRESO FLOTANTE ===
        self.create_floating_progress_bar()
        
    def create_simple_status_tab(self):
        """
        Pestaña con ejemplos de barras de estado simples
        """
        simple_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(simple_frame, text="📋 Básicas")
        
        # Información sobre barras de estado
        info_frame = tk.Frame(simple_frame, bg='#2D2D30', relief='raised', borderwidth=2)
        info_frame.pack(fill='x', padx=10, pady=(10, 0))
        
        tk.Label(
            info_frame,
            text="📋 Barras de Estado Básicas",
            font=("Arial", 14, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(pady=10)
        
        tk.Label(
            info_frame,
            text="Las barras de estado proporcionan información contextual sobre el estado\n"
                 "de la aplicación, progreso de tareas, y datos relevantes para el usuario.",
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#CCCCCC',
            justify='center'
        ).pack(pady=(0, 10), padx=15)
        
        # Frame para ejemplos
        examples_frame = tk.Frame(simple_frame, bg='#1E1E1E')
        examples_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === EJEMPLO 1: STATUS BAR CON UN SOLO LABEL ===
        example1_frame = tk.LabelFrame(
            examples_frame,
            text="🔹 Ejemplo 1: Barra de Estado Simple",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        example1_frame.pack(fill='x', pady=(0, 15))
        
        # Área de trabajo simulada
        work_area1 = tk.Text(
            example1_frame,
            height=5,
            font=("Arial", 10),
            bg='#FFFFFF',
            fg='#2C3E50'
        )
        work_area1.pack(fill='x', pady=(0, 10))
        work_area1.insert(tk.END, "📝 Área de trabajo - Escribe algo para ver cambios en la barra de estado...")
        
        # Barra de estado simple
        status_simple = tk.Frame(example1_frame, bg='#BDC3C7', relief='sunken', borderwidth=2)
        status_simple.pack(fill='x')
        
        self.simple_status_label = tk.Label(
            status_simple,
            text="💡 Listo - 0 caracteres",
            font=("Arial", 9),
            bg='#BDC3C7',
            fg='#2C3E50',
            anchor='w',
            padx=10
        )
        self.simple_status_label.pack(fill='x', pady=3)
        
        # Vincular evento de texto
        work_area1.bind('<KeyRelease>', lambda e: self.update_simple_status(work_area1))
        
        # === EJEMPLO 2: STATUS BAR CON MÚLTIPLES SECCIONES ===
        example2_frame = tk.LabelFrame(
            examples_frame,
            text="🔹 Ejemplo 2: Barra de Estado Multi-Sección",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        example2_frame.pack(fill='x', pady=(0, 15))
        
        # Controles para cambiar estado
        controls_frame = tk.Frame(example2_frame, bg='#2D2D30')
        controls_frame.pack(fill='x', pady=(0, 10))
        
        tk.Button(
            controls_frame,
            text="💾 Guardar",
            font=("Arial", 10),
            bg='#27AE60',
            fg='white',
            command=self.simulate_save_action,
            padx=15
        ).pack(side='left', padx=(0, 5))
        
        tk.Button(
            controls_frame,
            text="📂 Abrir",
            font=("Arial", 10),
            bg='#3498DB',
            fg='white',
            command=self.simulate_open_action,
            padx=15
        ).pack(side='left', padx=(0, 5))
        
        tk.Button(
            controls_frame,
            text="⚠️ Error",
            font=("Arial", 10),
            bg='#E74C3C',
            fg='white',
            command=self.simulate_error_action,
            padx=15
        ).pack(side='left', padx=(0, 5))
        
        tk.Button(
            controls_frame,
            text="🔄 Reset",
            font=("Arial", 10),
            bg='#95A5A6',
            fg='white',
            command=self.reset_multi_status,
            padx=15
        ).pack(side='left')
        
        # Barra de estado multi-sección
        multi_status = tk.Frame(example2_frame, bg='#34495E', relief='sunken', borderwidth=2)
        multi_status.pack(fill='x')
        
        # Sección izquierda (mensaje principal)
        self.multi_status_left = tk.Label(
            multi_status,
            text="🟢 Aplicación lista",
            font=("Arial", 9),
            bg='#34495E',
            fg='#FFFFFF',
            anchor='w',
            padx=10
        )
        self.multi_status_left.pack(side='left', fill='x', expand=True, pady=3)
        
        # Sección derecha (información adicional)
        self.multi_status_right = tk.Label(
            multi_status,
            text="📄 Sin archivo | 🕒 " + datetime.datetime.now().strftime("%H:%M:%S"),
            font=("Arial", 9),
            bg='#34495E',
            fg='#ECF0F1',
            padx=10
        )
        self.multi_status_right.pack(side='right', pady=3)
        
        # === EJEMPLO 3: STATUS BAR CON ICONOS DE ESTADO ===
        example3_frame = tk.LabelFrame(
            examples_frame,
            text="🔹 Ejemplo 3: Barra con Iconos de Estado",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        example3_frame.pack(fill='both', expand=True)
        
        # Controles para cambiar iconos
        icon_controls = tk.Frame(example3_frame, bg='#2D2D30')
        icon_controls.pack(fill='x', pady=(0, 10))
        
        states = [
            ("🟢 Conectado", "#27AE60"),
            ("🟡 Advertencia", "#F39C12"),
            ("🔴 Error", "#E74C3C"),
            ("⚪ Desconectado", "#95A5A6")
        ]
        
        for state_text, color in states:
            tk.Button(
                icon_controls,
                text=state_text,
                font=("Arial", 9),
                bg=color,
                fg='white',
                command=lambda s=state_text, c=color: self.change_icon_status(s, c),
                width=12
            ).pack(side='left', padx=(0, 5))
        
        # Barra de estado con iconos
        icon_status = tk.Frame(example3_frame, bg='#2C3E50', relief='sunken', borderwidth=2)
        icon_status.pack(fill='x')
        
        # Grid para organizar los iconos
        icon_status.grid_columnconfigure(0, weight=1)
        
        # Estado de conexión
        self.connection_icon = tk.Label(
            icon_status,
            text="🟢 Conectado",
            font=("Arial", 9, "bold"),
            bg='#2C3E50',
            fg='#27AE60'
        )
        self.connection_icon.grid(row=0, column=0, sticky='w', padx=10, pady=3)
        
        # Información de red
        network_info = tk.Label(
            icon_status,
            text="📡 192.168.1.100",
            font=("Arial", 9),
            bg='#2C3E50',
            fg='#ECF0F1'
        )
        network_info.grid(row=0, column=1, padx=10, pady=3)
        
        # Estado de seguridad
        security_icon = tk.Label(
            icon_status,
            text="🔒 Seguro",
            font=("Arial", 9),
            bg='#2C3E50',
            fg='#2ECC71'
        )
        security_icon.grid(row=0, column=2, padx=10, pady=3)
        
        # Nivel de batería (simulado)
        battery_icon = tk.Label(
            icon_status,
            text="🔋 85%",
            font=("Arial", 9),
            bg='#2C3E50',
            fg='#F39C12'
        )
        battery_icon.grid(row=0, column=3, sticky='e', padx=10, pady=3)
        
    def create_advanced_status_tab(self):
        """
        Pestaña con barras de estado avanzadas
        """
        advanced_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(advanced_frame, text="⚙️ Avanzadas")
        
        # Título
        tk.Label(
            advanced_frame,
            text="⚙️ Barras de Estado Avanzadas",
            font=("Arial", 16, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        ).pack(pady=15)
        
        # Frame principal
        advanced_content = tk.Frame(advanced_frame, bg='#1E1E1E')
        advanced_content.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === BARRA DE ESTADO CON PROGRESO INTEGRADO ===
        progress_frame = tk.LabelFrame(
            advanced_content,
            text="📊 Barra con Progreso Integrado",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        progress_frame.pack(fill='x', pady=(0, 15))
        
        # Controles de progreso
        progress_controls = tk.Frame(progress_frame, bg='#2D2D30')
        progress_controls.pack(fill='x', pady=(0, 10))
        
        tk.Button(
            progress_controls,
            text="▶️ Iniciar Tarea",
            font=("Arial", 10),
            bg='#27AE60',
            fg='white',
            command=self.start_progress_task,
            padx=15
        ).pack(side='left', padx=(0, 5))
        
        tk.Button(
            progress_controls,
            text="⏸️ Pausar",
            font=("Arial", 10),
            bg='#F39C12',
            fg='white',
            command=self.pause_progress_task,
            padx=15
        ).pack(side='left', padx=(0, 5))
        
        tk.Button(
            progress_controls,
            text="⏹️ Detener",
            font=("Arial", 10),
            bg='#E74C3C',
            fg='white',
            command=self.stop_progress_task,
            padx=15
        ).pack(side='left')
        
        # Barra de estado con progreso
        self.progress_status_frame = tk.Frame(progress_frame, bg='#34495E', relief='sunken', borderwidth=2)
        self.progress_status_frame.pack(fill='x')
        
        # Información de la tarea
        self.task_info = tk.Label(
            self.progress_status_frame,
            text="⏳ Listo para comenzar",
            font=("Arial", 9),
            bg='#34495E',
            fg='#FFFFFF',
            anchor='w',
            padx=10
        )
        self.task_info.pack(side='left', fill='x', expand=True, pady=3)
        
        # Barra de progreso pequeña
        self.mini_progress = ttk.Progressbar(
            self.progress_status_frame,
            length=100,
            mode='determinate',
            variable=self.task_progress
        )
        self.mini_progress.pack(side='right', padx=10, pady=5)
        
        # Porcentaje
        self.progress_percent = tk.Label(
            self.progress_status_frame,
            text="0%",
            font=("Arial", 9),
            bg='#34495E',
            fg='#ECF0F1',
            width=4
        )
        self.progress_percent.pack(side='right', padx=(0, 5), pady=3)
        
        # === BARRA DE ESTADO CONTEXTUAL ===
        context_frame = tk.LabelFrame(
            advanced_content,
            text="🎯 Barra Contextual",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        context_frame.pack(fill='x', pady=(0, 15))
        
        # Área de trabajo con diferentes contextos
        context_work = tk.Frame(context_frame, bg='#2D2D30')
        context_work.pack(fill='x', pady=(0, 10))
        
        # Pestañas simuladas para cambiar contexto
        context_tabs = tk.Frame(context_work, bg='#2D2D30')
        context_tabs.pack(fill='x')
        
        contexts = [
            ("📄 Editor", "text"),
            ("🖼️ Imagen", "image"), 
            ("📊 Datos", "data"),
            ("🔧 Config", "config")
        ]
        
        for tab_text, context_type in contexts:
            tk.Button(
                context_tabs,
                text=tab_text,
                font=("Arial", 9),
                bg='#3498DB',
                fg='white',
                command=lambda ctx=context_type: self.change_context(ctx),
                width=12
            ).pack(side='left', padx=(0, 5))
        
        # Barra de estado contextual
        self.context_status_frame = tk.Frame(context_frame, bg='#2C3E50', relief='sunken', borderwidth=2)
        self.context_status_frame.pack(fill='x')
        
        self.context_status = tk.Label(
            self.context_status_frame,
            text="📄 Editor de texto - Línea 1, Columna 1 | Sin selección",
            font=("Arial", 9),
            bg='#2C3E50',
            fg='#FFFFFF',
            anchor='w',
            padx=10
        )
        self.context_status.pack(fill='x', pady=3)
        
        # === BARRA DE NOTIFICACIONES ===
        notifications_frame = tk.LabelFrame(
            advanced_content,
            text="🔔 Barra de Notificaciones",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        notifications_frame.pack(fill='both', expand=True)
        
        # Controles de notificación
        notif_controls = tk.Frame(notifications_frame, bg='#2D2D30')
        notif_controls.pack(fill='x', pady=(0, 10))
        
        notification_types = [
            ("ℹ️ Info", "#3498DB"),
            ("✅ Éxito", "#27AE60"),
            ("⚠️ Advertencia", "#F39C12"),
            ("❌ Error", "#E74C3C")
        ]
        
        for notif_text, color in notification_types:
            tk.Button(
                notif_controls,
                text=notif_text,
                font=("Arial", 9),
                bg=color,
                fg='white',
                command=lambda t=notif_text, c=color: self.show_notification(t, c),
                width=12
            ).pack(side='left', padx=(0, 5))
            
        tk.Button(
            notif_controls,
            text="🧹 Limpiar",
            font=("Arial", 9),
            bg='#95A5A6',
            fg='white',
            command=self.clear_notifications,
            width=12
        ).pack(side='left', padx=(5, 0))
        
        # Frame contenedor para área de notificaciones con scrollbar
        notifications_container = tk.Frame(notifications_frame, bg='#34495E')
        notifications_container.pack(fill='both', expand=True)
        
        # Canvas y scrollbar para notificaciones
        notifications_canvas = tk.Canvas(notifications_container, bg='#34495E', highlightthickness=0)
        notifications_scrollbar = tk.Scrollbar(notifications_container, orient="vertical", command=notifications_canvas.yview)
        self.notifications_area = tk.Frame(notifications_canvas, bg='#34495E')
        
        self.notifications_area.bind(
            "<Configure>",
            lambda e: notifications_canvas.configure(scrollregion=notifications_canvas.bbox("all"))
        )
        
        notifications_canvas.create_window((0, 0), window=self.notifications_area, anchor="nw")
        notifications_canvas.configure(yscrollcommand=notifications_scrollbar.set)
        
        notifications_canvas.pack(side="left", fill="both", expand=True)
        notifications_scrollbar.pack(side="right", fill="y")
        
        # Habilitar scroll con rueda del ratón para notificaciones
        self.bind_mousewheel(notifications_canvas)
        
        # Mensaje inicial
        initial_notif = tk.Label(
            self.notifications_area,
            text="💡 Área de notificaciones - Haz clic en los botones de arriba",
            font=("Arial", 10),
            bg='#34495E',
            fg='#BDC3C7',
            pady=20
        )
        initial_notif.pack(fill='both', expand=True)
        
    def create_realtime_status_tab(self):
        """
        Pestaña con información en tiempo real
        """
        realtime_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(realtime_frame, text="⏱️ Tiempo Real")
        
        # Título
        tk.Label(
            realtime_frame,
            text="⏱️ Información en Tiempo Real",
            font=("Arial", 16, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        ).pack(pady=15)
        
        # Frame principal
        realtime_content = tk.Frame(realtime_frame, bg='#1E1E1E')
        realtime_content.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === DASHBOARD DE SISTEMA ===
        dashboard_frame = tk.LabelFrame(
            realtime_content,
            text="📊 Dashboard del Sistema",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        dashboard_frame.pack(fill='x', pady=(0, 15))
        
        # Grid para métricas
        dashboard_frame.grid_columnconfigure(0, weight=1)
        dashboard_frame.grid_columnconfigure(1, weight=1)
        dashboard_frame.grid_columnconfigure(2, weight=1)
        
        # CPU Usage
        cpu_frame = tk.Frame(dashboard_frame, bg='#34495E', relief='raised', borderwidth=2)
        cpu_frame.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
        
        tk.Label(
            cpu_frame,
            text="🖥️ CPU",
            font=("Arial", 10, "bold"),
            bg='#34495E',
            fg='#FFFFFF'
        ).pack(pady=5)
        
        self.cpu_progress = ttk.Progressbar(
            cpu_frame,
            length=150,
            mode='determinate',
            variable=self.cpu_usage
        )
        self.cpu_progress.pack(pady=5)
        
        self.cpu_label = tk.Label(
            cpu_frame,
            text="0%",
            font=("Arial", 12, "bold"),
            bg='#34495E',
            fg='#E74C3C'
        )
        self.cpu_label.pack(pady=5)
        
        # Memory Usage
        memory_frame = tk.Frame(dashboard_frame, bg='#34495E', relief='raised', borderwidth=2)
        memory_frame.grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        
        tk.Label(
            memory_frame,
            text="🧠 Memoria",
            font=("Arial", 10, "bold"),
            bg='#34495E',
            fg='#FFFFFF'
        ).pack(pady=5)
        
        self.memory_progress = ttk.Progressbar(
            memory_frame,
            length=150,
            mode='determinate',
            variable=self.memory_usage
        )
        self.memory_progress.pack(pady=5)
        
        self.memory_label = tk.Label(
            memory_frame,
            text="0%",
            font=("Arial", 12, "bold"),
            bg='#34495E',
            fg='#F39C12'
        )
        self.memory_label.pack(pady=5)
        
        # Network Status
        network_frame = tk.Frame(dashboard_frame, bg='#34495E', relief='raised', borderwidth=2)
        network_frame.grid(row=0, column=2, padx=5, pady=5, sticky='ew')
        
        tk.Label(
            network_frame,
            text="🌐 Red",
            font=("Arial", 10, "bold"),
            bg='#34495E',
            fg='#FFFFFF'
        ).pack(pady=5)
        
        self.network_icon = tk.Label(
            network_frame,
            text="📶",
            font=("Arial", 20),
            bg='#34495E',
            fg='#27AE60'
        )
        self.network_icon.pack(pady=5)
        
        self.network_label = tk.Label(
            network_frame,
            textvariable=self.network_status,
            font=("Arial", 9),
            bg='#34495E',
            fg='#FFFFFF'
        )
        self.network_label.pack(pady=5)
        
        # === ACTIVIDAD EN TIEMPO REAL ===
        activity_frame = tk.LabelFrame(
            realtime_content,
            text="📈 Actividad en Tiempo Real",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        activity_frame.pack(fill='both', expand=True)
        
        # Frame contenedor para log de actividad con scrollbar
        log_container = tk.Frame(activity_frame, bg='#2D2D30')
        log_container.pack(fill='both', expand=True)
        
        # Log de actividad
        self.activity_log = tk.Text(
            log_container,
            height=15,
            font=("Courier", 9),
            bg='#1C1C1C',
            fg='#00FF00',
            wrap=tk.WORD
        )
        self.activity_log.pack(side='left', fill='both', expand=True)
        
        # Scrollbar para el log
        activity_scroll = tk.Scrollbar(log_container, command=self.activity_log.yview)
        activity_scroll.pack(side='right', fill='y')
        self.activity_log.configure(yscrollcommand=activity_scroll.set)
        
        # Barra de estado para el log
        activity_status = tk.Frame(activity_frame, bg='#2C3E50', relief='sunken', borderwidth=1)
        activity_status.pack(fill='x', pady=(5, 0))
        
        self.activity_count = tk.Label(
            activity_status,
            text="📊 0 eventos registrados",
            font=("Arial", 9),
            bg='#2C3E50',
            fg='#FFFFFF',
            anchor='w',
            padx=10
        )
        self.activity_count.pack(side='left', fill='x', expand=True, pady=3)
        
        self.activity_time = tk.Label(
            activity_status,
            textvariable=self.current_time,
            font=("Arial", 9),
            bg='#2C3E50',
            fg='#ECF0F1',
            padx=10
        )
        self.activity_time.pack(side='right', pady=3)
        
    def create_progress_status_tab(self):
        """
        Pestaña enfocada en barras de progreso
        """
        progress_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(progress_frame, text="📊 Progreso")
        
        # Título
        tk.Label(
            progress_frame,
            text="📊 Barras de Progreso Especializadas",
            font=("Arial", 16, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        ).pack(pady=15)
        
        # Frame principal
        progress_content = tk.Frame(progress_frame, bg='#1E1E1E')
        progress_content.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === PROGRESO DE DESCARGA ===
        download_frame = tk.LabelFrame(
            progress_content,
            text="📥 Simulador de Descarga",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        download_frame.pack(fill='x', pady=(0, 15))
        
        # Controles de descarga
        download_controls = tk.Frame(download_frame, bg='#2D2D30')
        download_controls.pack(fill='x', pady=(0, 10))
        
        tk.Button(
            download_controls,
            text="📥 Descargar",
            font=("Arial", 10),
            bg='#3498DB',
            fg='white',
            command=self.start_download,
            padx=20
        ).pack(side='left', padx=(0, 10))
        
        tk.Button(
            download_controls,
            text="⏸️ Pausar",
            font=("Arial", 10),
            bg='#F39C12',
            fg='white',
            command=self.pause_download,
            padx=20
        ).pack(side='left', padx=(0, 10))
        
        tk.Button(
            download_controls,
            text="❌ Cancelar",
            font=("Arial", 10),
            bg='#E74C3C',
            fg='white',
            command=self.cancel_download,
            padx=20
        ).pack(side='left')
        
        # Información del archivo
        file_info = tk.Frame(download_frame, bg='#34495E', relief='sunken', borderwidth=2)
        file_info.pack(fill='x', pady=(0, 10))
        
        self.download_file_name = tk.Label(
            file_info,
            text="📄 archivo_ejemplo.zip",
            font=("Arial", 10, "bold"),
            bg='#34495E',
            fg='#FFFFFF',
            anchor='w',
            padx=10
        )
        self.download_file_name.pack(fill='x', pady=3)
        
        # Barra de progreso de descarga
        self.download_progress_bar = ttk.Progressbar(
            download_frame,
            length=400,
            mode='determinate',
            variable=self.download_progress
        )
        self.download_progress_bar.pack(fill='x', pady=(0, 10))
        
        # Información detallada de descarga
        download_info = tk.Frame(download_frame, bg='#2C3E50', relief='sunken', borderwidth=1)
        download_info.pack(fill='x')
        
        self.download_status = tk.Label(
            download_info,
            text="⏳ Listo para descargar",
            font=("Arial", 9),
            bg='#2C3E50',
            fg='#FFFFFF',
            anchor='w',
            padx=10
        )
        self.download_status.pack(side='left', fill='x', expand=True, pady=3)
        
        self.download_speed = tk.Label(
            download_info,
            text="🚀 0 KB/s",
            font=("Arial", 9),
            bg='#2C3E50',
            fg='#ECF0F1',
            padx=10
        )
        self.download_speed.pack(side='right', pady=3)
        
        self.download_eta = tk.Label(
            download_info,
            text="⏰ --:--",
            font=("Arial", 9),
            bg='#2C3E50',
            fg='#ECF0F1',
            padx=10
        )
        self.download_eta.pack(side='right', pady=3)
        
        # === MÚLTIPLES TAREAS EN PROGRESO ===
        tasks_frame = tk.LabelFrame(
            progress_content,
            text="📋 Múltiples Tareas",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        tasks_frame.pack(fill='both', expand=True)
        
        # Frame contenedor para lista de tareas con scrollbar
        tasks_container = tk.Frame(tasks_frame, bg='#2D2D30')
        tasks_container.pack(fill='both', expand=True, pady=(0, 10))
        
        # Canvas y scrollbar para tareas
        tasks_canvas = tk.Canvas(tasks_container, bg='#2D2D30', highlightthickness=0)
        tasks_scrollbar = tk.Scrollbar(tasks_container, orient="vertical", command=tasks_canvas.yview)
        self.tasks_list_frame = tk.Frame(tasks_canvas, bg='#2D2D30')
        
        self.tasks_list_frame.bind(
            "<Configure>",
            lambda e: tasks_canvas.configure(scrollregion=tasks_canvas.bbox("all"))
        )
        
        tasks_canvas.create_window((0, 0), window=self.tasks_list_frame, anchor="nw")
        tasks_canvas.configure(yscrollcommand=tasks_scrollbar.set)
        
        tasks_canvas.pack(side="left", fill="both", expand=True)
        tasks_scrollbar.pack(side="right", fill="y")
        
        # Habilitar scroll con rueda del ratón para tareas
        self.bind_mousewheel(tasks_canvas)
        
        # Crear algunas tareas de ejemplo
        self.create_sample_tasks()
        
        # Controles para las tareas
        tasks_controls = tk.Frame(tasks_frame, bg='#2D2D30')
        tasks_controls.pack(fill='x', pady=(10, 0))
        
        tk.Button(
            tasks_controls,
            text="➕ Nueva Tarea",
            font=("Arial", 10),
            bg='#27AE60',
            fg='white',
            command=self.add_new_task,
            padx=20
        ).pack(side='left', padx=(0, 10))
        
        tk.Button(
            tasks_controls,
            text="▶️ Iniciar Todas",
            font=("Arial", 10),
            bg='#3498DB',
            fg='white',
            command=self.start_all_tasks,
            padx=20
        ).pack(side='left', padx=(0, 10))
        
        tk.Button(
            tasks_controls,
            text="⏹️ Detener Todas",
            font=("Arial", 10),
            bg='#E74C3C',
            fg='white',
            command=self.stop_all_tasks,
            padx=20
        ).pack(side='left')
        
    def create_main_status_bar(self):
        """
        Crea la barra de estado principal (siempre visible)
        """
        self.main_status = tk.Frame(self.root, bg='#95A5A6', relief='sunken', borderwidth=2)
        self.main_status.pack(side='bottom', fill='x')
        
        # Estado general de la aplicación
        self.main_status_label = tk.Label(
            self.main_status,
            textvariable=self.app_status,
            font=("Arial", 9, "bold"),
            bg='#95A5A6',
            fg='#2C3E50',
            anchor='w',
            padx=10
        )
        self.main_status_label.pack(side='left', fill='x', expand=True, pady=3)
        
        # Información de documentos
        self.docs_info = tk.Label(
            self.main_status,
            text="📄 3 documentos",
            font=("Arial", 9),
            bg='#95A5A6',
            fg='#2C3E50',
            padx=10
        )
        self.docs_info.pack(side='right', pady=3)
        
        # Notificaciones
        self.notif_indicator = tk.Label(
            self.main_status,
            text="🔔 0",
            font=("Arial", 9),
            bg='#95A5A6',
            fg='#2C3E50',
            padx=10
        )
        self.notif_indicator.pack(side='right', pady=3)
        
        # Zoom level
        self.zoom_info = tk.Label(
            self.main_status,
            text="🔍 100%",
            font=("Arial", 9),
            bg='#95A5A6',
            fg='#2C3E50',
            padx=10
        )
        self.zoom_info.pack(side='right', pady=3)
        
        # Hora actual
        self.time_info = tk.Label(
            self.main_status,
            textvariable=self.current_time,
            font=("Arial", 9),
            bg='#95A5A6',
            fg='#2C3E50',
            padx=10
        )
        self.time_info.pack(side='right', pady=3)
        
    def create_secondary_status_bar(self):
        """
        Crea una barra de estado secundaria
        """
        self.secondary_status = tk.Frame(self.root, bg='#34495E', relief='flat', borderwidth=1)
        self.secondary_status.pack(side='bottom', fill='x', before=self.main_status)
        
        # Información del archivo actual
        self.file_info = tk.Label(
            self.secondary_status,
            text=f"📄 {self.current_file}",
            font=("Arial", 8),
            bg='#34495E',
            fg='#FFFFFF',
            anchor='w',
            padx=10
        )
        self.file_info.pack(side='left', fill='x', expand=True, pady=2)
        
        # Estado de guardado
        self.save_status = tk.Label(
            self.secondary_status,
            text="💾 Guardado",
            font=("Arial", 8),
            bg='#34495E',
            fg='#27AE60',
            padx=10
        )
        self.save_status.pack(side='right', pady=2)
        
    def create_floating_progress_bar(self):
        """
        Crea una barra de progreso flotante (se muestra cuando es necesaria)
        """
        self.floating_progress_frame = tk.Frame(self.root, bg='#3498DB', relief='raised', borderwidth=2)
        # No la empaquetamos todavía - aparecerá cuando sea necesaria
        
        # Información de la tarea
        self.floating_task_label = tk.Label(
            self.floating_progress_frame,
            text="⏳ Procesando...",
            font=("Arial", 10),
            bg='#3498DB',
            fg='#FFFFFF',
            padx=10
        )
        self.floating_task_label.pack(side='left', pady=5)
        
        # Barra de progreso
        self.floating_progress = ttk.Progressbar(
            self.floating_progress_frame,
            length=200,
            mode='indeterminate'
        )
        self.floating_progress.pack(side='left', padx=10, pady=5)
        
        # Botón cancelar
        self.cancel_btn = tk.Button(
            self.floating_progress_frame,
            text="❌",
            font=("Arial", 8),
            bg='#E74C3C',
            fg='white',
            width=3,
            command=self.hide_floating_progress
        )
        self.cancel_btn.pack(side='right', padx=5, pady=5)
    
    # ====================================================================
    # MÉTODOS DE ACTUALIZACIÓN DE ESTADO
    # ====================================================================
    
    def update_simple_status(self, text_widget):
        """Actualiza la barra de estado simple"""
        content = text_widget.get(1.0, tk.END)
        char_count = len(content) - 1  # -1 para el \n final
        word_count = len(content.split())
        
        self.simple_status_label.config(
            text=f"📝 {char_count} caracteres, {word_count} palabras"
        )
        
    def simulate_save_action(self):
        """Simula acción de guardado"""
        self.multi_status_left.config(text="💾 Guardando archivo...", fg='#F39C12')
        self.root.after(2000, lambda: self.multi_status_left.config(
            text="✅ Archivo guardado correctamente", fg='#27AE60'))
        self.root.after(4000, lambda: self.multi_status_left.config(
            text="🟢 Aplicación lista", fg='#FFFFFF'))
            
    def simulate_open_action(self):
        """Simula acción de apertura"""
        self.multi_status_left.config(text="📂 Abriendo archivo...", fg='#3498DB')
        self.root.after(1500, lambda: self.multi_status_left.config(
            text="✅ Archivo abierto correctamente", fg='#27AE60'))
        self.root.after(3500, lambda: self.multi_status_left.config(
            text="🟢 Aplicación lista", fg='#FFFFFF'))
            
    def simulate_error_action(self):
        """Simula error"""
        self.multi_status_left.config(text="❌ Error: No se pudo realizar la operación", fg='#E74C3C')
        self.root.after(3000, lambda: self.multi_status_left.config(
            text="🟢 Aplicación lista", fg='#FFFFFF'))
            
    def reset_multi_status(self):
        """Resetea el estado múltiple"""
        self.multi_status_left.config(text="🟢 Aplicación lista", fg='#FFFFFF')
        
    def change_icon_status(self, status_text, color):
        """Cambia el estado de los iconos"""
        self.connection_icon.config(text=status_text, fg=color)
        
    # ====================================================================
    # MÉTODOS DE PROGRESO
    # ====================================================================
    
    def start_progress_task(self):
        """Inicia una tarea con progreso"""
        if not self.is_processing:
            self.is_processing = True
            self.task_progress.set(0)
            self.task_info.config(text="⏳ Procesando datos...")
            self.update_progress_task()
            
    def update_progress_task(self):
        """Actualiza el progreso de la tarea"""
        if self.is_processing:
            current = self.task_progress.get()
            if current < 100:
                new_progress = min(current + random.uniform(1, 5), 100)
                self.task_progress.set(new_progress)
                self.progress_percent.config(text=f"{int(new_progress)}%")
                
                if new_progress >= 100:
                    self.task_info.config(text="✅ Tarea completada")
                    self.is_processing = False
                else:
                    self.root.after(200, self.update_progress_task)
                    
    def pause_progress_task(self):
        """Pausa la tarea en progreso"""
        self.is_processing = False
        self.task_info.config(text="⏸️ Tarea pausada")
        
    def stop_progress_task(self):
        """Detiene la tarea en progreso"""
        self.is_processing = False
        self.task_progress.set(0)
        self.progress_percent.config(text="0%")
        self.task_info.config(text="⏹️ Tarea detenida")
        
    def change_context(self, context_type):
        """Cambia el contexto de la aplicación"""
        context_messages = {
            "text": "📄 Editor de texto - Línea 1, Columna 1 | Sin selección",
            "image": "🖼️ Editor de imagen - 1920x1080 | Herramienta: Pincel",
            "data": "📊 Vista de datos - 1,234 registros | Filtros activos: 2",
            "config": "🔧 Configuración - 15 opciones modificadas | Sin guardar"
        }
        
        self.context_status.config(text=context_messages.get(context_type, "❓ Contexto desconocido"))
        
    def show_notification(self, notif_type, color):
        """Muestra una notificación"""
        # Limpiar notificaciones anteriores si hay muchas
        children = self.notifications_area.winfo_children()
        if len(children) > 5:
            children[0].destroy()
            
        # Crear nueva notificación
        notif_frame = tk.Frame(self.notifications_area, bg=color, relief='raised', borderwidth=1)
        notif_frame.pack(fill='x', padx=2, pady=1)
        
        # Timestamp
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        tk.Label(
            notif_frame,
            text=f"[{timestamp}] {notif_type} - Mensaje de ejemplo",
            font=("Arial", 9),
            bg=color,
            fg='white',
            anchor='w',
            padx=10
        ).pack(side='left', fill='x', expand=True, pady=3)
        
        # Botón cerrar
        tk.Button(
            notif_frame,
            text="×",
            font=("Arial", 8),
            bg=color,
            fg='white',
            relief='flat',
            width=2,
            command=notif_frame.destroy
        ).pack(side='right', pady=3, padx=5)
        
        # Auto-eliminar después de 5 segundos
        self.root.after(5000, lambda: notif_frame.destroy() if notif_frame.winfo_exists() else None)
        
    def clear_notifications(self):
        """Limpia todas las notificaciones"""
        for child in self.notifications_area.winfo_children():
            child.destroy()
            
        # Mensaje inicial
        initial_notif = tk.Label(
            self.notifications_area,
            text="💡 Notificaciones limpiadas",
            font=("Arial", 10),
            bg='#34495E',
            fg='#BDC3C7',
            pady=20
        )
        initial_notif.pack(fill='both', expand=True)
        
    # ====================================================================
    # MÉTODOS DE DESCARGA
    # ====================================================================
    
    def start_download(self):
        """Inicia simulación de descarga"""
        if not self.is_downloading:
            self.is_downloading = True
            self.download_progress.set(0)
            self.download_status.config(text="📥 Descargando...")
            self.update_download()
            
    def update_download(self):
        """Actualiza el progreso de descarga"""
        if self.is_downloading:
            current = self.download_progress.get()
            if current < 100:
                new_progress = min(current + random.uniform(0.5, 3), 100)
                self.download_progress.set(new_progress)
                
                # Simular velocidad y ETA
                speed = random.randint(50, 500)
                remaining = (100 - new_progress) / 2  # Segundos restantes aproximados
                eta_min = int(remaining // 60)
                eta_sec = int(remaining % 60)
                
                self.download_speed.config(text=f"🚀 {speed} KB/s")
                self.download_eta.config(text=f"⏰ {eta_min}:{eta_sec:02d}")
                
                if new_progress >= 100:
                    self.download_status.config(text="✅ Descarga completada")
                    self.download_speed.config(text="🚀 0 KB/s")
                    self.download_eta.config(text="⏰ 00:00")
                    self.is_downloading = False
                else:
                    self.root.after(300, self.update_download)
                    
    def pause_download(self):
        """Pausa la descarga"""
        self.is_downloading = False
        self.download_status.config(text="⏸️ Descarga pausada")
        self.download_speed.config(text="🚀 0 KB/s")
        
    def cancel_download(self):
        """Cancela la descarga"""
        self.is_downloading = False
        self.download_progress.set(0)
        self.download_status.config(text="❌ Descarga cancelada")
        self.download_speed.config(text="🚀 0 KB/s")
        self.download_eta.config(text="⏰ --:--")
        
    # ====================================================================
    # MÉTODOS DE TAREAS MÚLTIPLES
    # ====================================================================
    
    def create_sample_tasks(self):
        """Crea tareas de ejemplo"""
        sample_tasks = [
            "📄 Procesando documento.pdf",
            "🖼️ Redimensionando imagen.jpg",
            "📊 Analizando datos.csv",
            "🔄 Sincronizando archivos"
        ]
        
        for i, task_name in enumerate(sample_tasks):
            self.create_task_widget(task_name, i * 25)  # Progreso inicial diferente
            
    def create_task_widget(self, task_name, initial_progress=0):
        """Crea un widget de tarea individual"""
        task_frame = tk.Frame(self.tasks_list_frame, bg='#34495E', relief='raised', borderwidth=1)
        task_frame.pack(fill='x', padx=2, pady=2)
        
        # Información de la tarea
        info_frame = tk.Frame(task_frame, bg='#34495E')
        info_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(
            info_frame,
            text=task_name,
            font=("Arial", 9),
            bg='#34495E',
            fg='#FFFFFF',
            anchor='w'
        ).pack(side='left', fill='x', expand=True)
        
        status_label = tk.Label(
            info_frame,
            text="⏳ Pendiente",
            font=("Arial", 8),
            bg='#34495E',
            fg='#F39C12'
        )
        status_label.pack(side='right')
        
        # Barra de progreso
        progress_var = tk.DoubleVar(value=initial_progress)
        progress_bar = ttk.Progressbar(
            task_frame,
            length=300,
            mode='determinate',
            variable=progress_var
        )
        progress_bar.pack(fill='x', padx=10, pady=(0, 5))
        
        # Guardar referencias para control posterior
        task_frame.progress_var = progress_var
        task_frame.status_label = status_label
        task_frame.task_name = task_name
        task_frame.is_running = False
        
    def add_new_task(self):
        """Añade una nueva tarea"""
        task_names = [
            "🔄 Backup de datos",
            "📦 Comprimiendo archivos",
            "🔍 Escaneando virus",
            "🌐 Actualizando software",
            "📧 Enviando emails",
            "🎥 Codificando video"
        ]
        
        task_name = random.choice(task_names)
        self.create_task_widget(task_name)
        
    def start_all_tasks(self):
        """Inicia todas las tareas"""
        for task_widget in self.tasks_list_frame.winfo_children():
            if hasattr(task_widget, 'is_running') and not task_widget.is_running:
                task_widget.is_running = True
                task_widget.status_label.config(text="▶️ En progreso", fg='#3498DB')
                self.animate_task_progress(task_widget)
                
    def stop_all_tasks(self):
        """Detiene todas las tareas"""
        for task_widget in self.tasks_list_frame.winfo_children():
            if hasattr(task_widget, 'is_running'):
                task_widget.is_running = False
                task_widget.status_label.config(text="⏹️ Detenida", fg='#E74C3C')
                
    def animate_task_progress(self, task_widget):
        """Anima el progreso de una tarea específica"""
        if task_widget.is_running and task_widget.winfo_exists():
            current = task_widget.progress_var.get()
            if current < 100:
                new_progress = min(current + random.uniform(0.5, 2), 100)
                task_widget.progress_var.set(new_progress)
                
                if new_progress >= 100:
                    task_widget.status_label.config(text="✅ Completada", fg='#27AE60')
                    task_widget.is_running = False
                else:
                    self.root.after(500, lambda: self.animate_task_progress(task_widget))
    
    # ====================================================================
    # MÉTODOS DE PROGRESO FLOTANTE
    # ====================================================================
    
    def show_floating_progress(self, message="Procesando..."):
        """Muestra la barra de progreso flotante"""
        self.floating_task_label.config(text=f"⏳ {message}")
        self.floating_progress_frame.pack(side='bottom', fill='x', before=self.secondary_status)
        self.floating_progress.start(10)
        
    def hide_floating_progress(self):
        """Oculta la barra de progreso flotante"""
        self.floating_progress.stop()
        self.floating_progress_frame.pack_forget()
        
    # ====================================================================
    # PROCESOS EN SEGUNDO PLANO
    # ====================================================================
    
    def start_background_processes(self):
        """Inicia procesos en segundo plano para actualización en tiempo real"""
        self.update_time()
        self.update_system_metrics()
        self.log_random_activity()
        
    def update_time(self):
        """Actualiza la hora actual"""
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.current_time.set(f"🕒 {current_time}")
        self.root.after(1000, self.update_time)  # Actualizar cada segundo
        
    def update_system_metrics(self):
        """Actualiza métricas del sistema (simuladas)"""
        # Simular cambios en CPU
        cpu_change = random.uniform(-5, 5)
        new_cpu = max(0, min(100, self.cpu_usage.get() + cpu_change))
        self.cpu_usage.set(new_cpu)
        self.cpu_label.config(text=f"{int(new_cpu)}%")
        
        # Simular cambios en memoria
        memory_change = random.uniform(-3, 3)
        new_memory = max(0, min(100, self.memory_usage.get() + memory_change))
        self.memory_usage.set(new_memory)
        self.memory_label.config(text=f"{int(new_memory)}%")
        
        # Cambiar estado de red ocasionalmente
        if random.random() < 0.1:  # 10% probabilidad
            statuses = ["🌐 Conectado", "📶 Señal débil", "❌ Sin conexión"]
            colors = ["#27AE60", "#F39C12", "#E74C3C"]
            status, color = random.choice(list(zip(statuses, colors)))
            self.network_status.set(status)
            self.network_label.config(fg=color)
            
        # Actualizar cada 2 segundos
        self.root.after(2000, self.update_system_metrics)
        
    def log_random_activity(self):
        """Registra actividad aleatoria en el log"""
        activities = [
            "📄 Archivo guardado automáticamente",
            "🔍 Escaneo de seguridad completado",
            "📧 Nuevo mensaje recibido",
            "🔄 Sincronización con servidor",
            "💾 Backup automático realizado",
            "🌐 Conectado a red Wi-Fi",
            "🖱️ Usuario inactivo detectado",
            "📊 Generando estadísticas",
            "🔒 Sesión bloqueada por inactividad",
            "⚡ Sistema optimizado"
        ]
        
        # Registrar actividad aleatoriamente
        if random.random() < 0.3:  # 30% probabilidad
            activity = random.choice(activities)
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            
            self.activity_log.insert(tk.END, f"[{timestamp}] {activity}\n")
            self.activity_log.see(tk.END)
            
            # Actualizar contador
            line_count = int(self.activity_log.index('end').split('.')[0]) - 1
            self.activity_count.config(text=f"📊 {line_count} eventos registrados")
            
        # Actualizar cada 5 segundos
        self.root.after(5000, self.log_random_activity)
    
    # ====================================================================
    # FUNCIONES DE SOPORTE DE SCROLL
    # ====================================================================
    
    def bind_mousewheel(self, canvas):
        """Vincula el scroll de la rueda del ratón al canvas"""
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        def _bind_to_mousewheel(event):
            canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        def _unbind_from_mousewheel(event):
            canvas.unbind_all("<MouseWheel>")
        
        canvas.bind('<Enter>', _bind_to_mousewheel)
        canvas.bind('<Leave>', _unbind_from_mousewheel)

def main():
    """
    Función principal para ejecutar la demostración
    """
    root = tk.Tk()
    app = StatusBarDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
