#!/usr/bin/env python3
"""
Controles Avanzados y Elementos de Interfaz en Tkinter
====================================================

Este script demuestra:
1. ImageList (Concepto y Alternativas en Tkinter)
2. Toolbar (Concepto y Creación con Frame y Button)
3. Mask (Entrada Enmascarada - show en Entry o Widgets Personalizados)
4. Controles personalizados y avanzados

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import re
import os

# Intentar importar PIL, si no está disponible usar fallback
try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

class AdvancedControlsDemo:
    """
    Clase que demuestra controles avanzados en Tkinter
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
        self.create_image_list()
        self.create_main_interface()
        
    def setup_window(self):
        """
        Configura la ventana principal
        """
        self.root.title("🎛️ Controles Avanzados en Tkinter")
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
        Inicializa variables y datos de la aplicación
        """
        # Variables para formularios con máscara
        self.phone_var = tk.StringVar()
        self.dni_var = tk.StringVar()
        self.date_var = tk.StringVar()
        self.credit_card_var = tk.StringVar()
        
        # Lista de herramientas para toolbar
        self.toolbar_actions = []
        
    def create_image_list(self):
        """
        Crea una lista de imágenes (ImageList alternativa)
        En Tkinter no hay ImageList nativo, pero podemos simular uno
        """
        self.image_list = {}
        
        try:
            # Crear iconos simples usando caracteres Unicode como alternativa
            self.icons = {
                'new': '📄',
                'open': '📂',
                'save': '💾',
                'cut': '✂️',
                'copy': '📋',
                'paste': '📌',
                'undo': '↶',
                'redo': '↷',
                'find': '🔍',
                'replace': '🔄',
                'print': '🖨️',
                'settings': '⚙️',
                'help': '❓',
                'exit': '🚪'
            }
            
            # Si tenemos PIL, podemos crear iconos más sofisticados
            self.create_simple_icons()
            
        except Exception as e:
            print(f"Error creando ImageList: {e}")
            # Fallback a iconos de texto simple
            self.icons = {key: f"[{key.upper()}]" for key in self.icons.keys()}
    
    def create_simple_icons(self):
        """
        Crea iconos simples usando PIL (si está disponible)
        """
        if PIL_AVAILABLE:
            try:
                # Crear algunos iconos básicos de colores
                icon_size = (16, 16)
                colors = {
                    'new': '#4CAF50',
                    'open': '#2196F3', 
                    'save': '#FF9800',
                    'cut': '#F44336',
                    'copy': '#9C27B0',
                    'paste': '#607D8B'
                }
                
                for name, color in colors.items():
                    # Crear imagen simple de color sólido
                    img = Image.new('RGBA', icon_size, color)
                    self.image_list[name] = ImageTk.PhotoImage(img)
                    
            except Exception as e:
                # Si hay algún error, usar fallback
                print(f"Error creando iconos con PIL: {e}")
        # Si PIL no está disponible, los iconos de texto se usan automáticamente
    
    def create_main_interface(self):
        """
        Crea la interfaz principal con pestañas
        """
        # Título principal
        title_label = tk.Label(
            self.root,
            text="🎛️ Controles Avanzados en Tkinter",
            font=("Arial", 16, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        )
        title_label.pack(pady=15)
        
        # Crear notebook para organizar ejemplos
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Crear pestañas
        self.create_imagelist_tab()
        self.create_toolbar_tab() 
        self.create_mask_tab()
        self.create_custom_controls_tab()
        
    def create_imagelist_tab(self):
        """
        Crea la pestaña de demostración de ImageList
        """
        imagelist_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(imagelist_frame, text="🖼️ ImageList")
        
        # Header informativo
        info_frame = tk.Frame(imagelist_frame, bg='#2D2D30', relief='raised', borderwidth=2)
        info_frame.pack(fill='x', padx=10, pady=(10, 0))
        
        tk.Label(
            info_frame,
            text="🖼️ ImageList - Gestión de Iconos y Imágenes",
            font=("Arial", 14, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(pady=10)
        
        tk.Label(
            info_frame,
            text="Tkinter no tiene ImageList nativo como otros frameworks,\n"
                 "pero podemos crear alternativas usando diccionarios y PhotoImage.\n"
                 "Útil para iconos de toolbar, botones, listview, etc.",
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#CCCCCC',
            justify='left'
        ).pack(pady=(0, 10), padx=15)
        
        # Frame principal
        main_frame = tk.Frame(imagelist_frame, bg='#1E1E1E')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === DEMOSTRACIÓN DE IMAGELIST ===
        demo_frame = tk.LabelFrame(
            main_frame,
            text="🔹 ImageList Simulado",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        demo_frame.pack(fill='both', expand=True)
        
        # Lista de iconos disponibles
        icons_list_frame = tk.Frame(demo_frame, bg='#2D2D30')
        icons_list_frame.pack(fill='x', pady=(0, 15))
        
        tk.Label(
            icons_list_frame,
            text="📋 Iconos Disponibles en nuestro ImageList:",
            font=("Arial", 11, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(anchor='w', pady=(0, 10))
        
        # Mostrar iconos en grid
        icons_grid = tk.Frame(icons_list_frame, bg='#3C3C3C', relief='sunken', borderwidth=2)
        icons_grid.pack(fill='x', padx=10)
        
        row, col = 0, 0
        for i, (name, icon) in enumerate(self.icons.items()):
            # Frame para cada icono
            icon_frame = tk.Frame(icons_grid, bg='#3C3C3C')
            icon_frame.grid(row=row, column=col, padx=5, pady=5)
            
            # Botón con icono
            if name in self.image_list:
                btn = tk.Button(
                    icon_frame,
                    image=self.image_list[name],
                    compound='top',
                    text=name,
                    font=("Arial", 8),
                    bg='#4CAF50',
                    fg='black',
                    width=60,
                    command=lambda n=name: self.icon_clicked(n)
                )
            else:
                btn = tk.Button(
                    icon_frame,
                    text=f"{icon}\n{name}",
                    font=("Arial", 8),
                    bg='#4CAF50',
                    fg='black',
                    width=8,
                    height=3,
                    command=lambda n=name: self.icon_clicked(n)
                )
            btn.pack()
            
            col += 1
            if col > 6:  # 7 iconos por fila
                col = 0
                row += 1
                
        # Área de resultados
        results_frame = tk.LabelFrame(
            demo_frame,
            text="📊 Resultado de Interacción",
            font=("Arial", 11, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=10
        )
        results_frame.pack(fill='both', expand=True, pady=(15, 0))
        
        self.imagelist_result = tk.Text(
            results_frame,
            height=8,
            font=("Courier", 9),
            bg='#3C3C3C',
            fg='#FFFFFF',
            wrap=tk.WORD
        )
        self.imagelist_result.pack(fill='both', expand=True)
        
        # Scrollbar para el texto
        scrollbar_img = tk.Scrollbar(results_frame, command=self.imagelist_result.yview)
        self.imagelist_result.configure(yscrollcommand=scrollbar_img.set)
        
        # Mensaje inicial
        self.imagelist_result.insert(tk.END, 
            "🖼️ ImageList Simulado Inicializado\n"
            f"📋 Total de iconos cargados: {len(self.icons)}\n"
            "💡 Haz clic en cualquier icono para ver la interacción\n"
            "=" * 50 + "\n\n"
        )
        
    def create_toolbar_tab(self):
        """
        Crea la pestaña de demostración de Toolbar
        """
        toolbar_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(toolbar_frame, text="🔧 Toolbar")
        
        # Header informativo
        info_frame = tk.Frame(toolbar_frame, bg='#2D2D30', relief='raised', borderwidth=2)
        info_frame.pack(fill='x', padx=10, pady=(10, 0))
        
        tk.Label(
            info_frame,
            text="🔧 Toolbar - Barra de Herramientas",
            font=("Arial", 14, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(pady=10)
        
        tk.Label(
            info_frame,
            text="Creación de toolbars usando Frame y Button.\n"
                 "Incluye separadores, iconos, tooltips y diferentes estilos.",
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#CCCCCC',
            justify='left'
        ).pack(pady=(0, 10), padx=15)
        
        # Frame principal
        main_frame = tk.Frame(toolbar_frame, bg='#1E1E1E')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === TOOLBAR HORIZONTAL ===
        self.create_horizontal_toolbar(main_frame)
        
        # === TOOLBAR VERTICAL ===  
        self.create_vertical_toolbar(main_frame)
        
        # === ÁREA DE TRABAJO ===
        work_area_frame = tk.LabelFrame(
            main_frame,
            text="📝 Área de Trabajo",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        work_area_frame.pack(fill='both', expand=True, pady=(10, 0))
        
        # Text area que responde a las acciones del toolbar
        self.work_text = tk.Text(
            work_area_frame,
            font=("Arial", 11),
            bg='#FFFFFF',
            fg='#2C3E50',
            wrap=tk.WORD,
            undo=True
        )
        self.work_text.pack(fill='both', expand=True)
        
        # Insertar texto inicial
        self.work_text.insert(tk.END,
            "📝 Área de trabajo interactiva\n\n"
            "Usa los botones del toolbar para:\n"
            "• Crear nuevo documento\n" 
            "• Abrir archivo existente\n"
            "• Guardar contenido\n"
            "• Cortar, copiar, pegar texto\n"
            "• Deshacer y rehacer cambios\n"
            "• Buscar y reemplazar texto\n\n"
            "¡Prueba todas las funcionalidades!"
        )
        
    def create_horizontal_toolbar(self, parent):
        """
        Crea toolbar horizontal
        """
        toolbar_frame = tk.LabelFrame(
            parent,
            text="🔹 Toolbar Horizontal",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=10
        )
        toolbar_frame.pack(fill='x', pady=(0, 10))
        
        # Toolbar container
        toolbar = tk.Frame(toolbar_frame, bg='#34495E', relief='raised', borderwidth=2)
        toolbar.pack(fill='x', padx=5, pady=5)
        
        # Grupo 1: Archivo
        self.create_toolbar_group(toolbar, [
            ('new', 'Nuevo', self.toolbar_new),
            ('open', 'Abrir', self.toolbar_open),
            ('save', 'Guardar', self.toolbar_save)
        ])
        
        self.create_toolbar_separator(toolbar)
        
        # Grupo 2: Edición
        self.create_toolbar_group(toolbar, [
            ('cut', 'Cortar', self.toolbar_cut),
            ('copy', 'Copiar', self.toolbar_copy),
            ('paste', 'Pegar', self.toolbar_paste)
        ])
        
        self.create_toolbar_separator(toolbar)
        
        # Grupo 3: Navegación
        self.create_toolbar_group(toolbar, [
            ('undo', 'Deshacer', self.toolbar_undo),
            ('redo', 'Rehacer', self.toolbar_redo)
        ])
        
        self.create_toolbar_separator(toolbar)
        
        # Grupo 4: Búsqueda
        self.create_toolbar_group(toolbar, [
            ('find', 'Buscar', self.toolbar_find),
            ('replace', 'Reemplazar', self.toolbar_replace)
        ])
        
    def create_vertical_toolbar(self, parent):
        """
        Crea un área con toolbar vertical (sidebar)
        """
        container = tk.Frame(parent, bg='#1E1E1E')
        container.pack(fill='x', pady=(0, 10))
        
        # Toolbar vertical
        vtoolbar_frame = tk.LabelFrame(
            container,
            text="🔹 Toolbar Vertical",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=10
        )
        vtoolbar_frame.pack(side='left', fill='y')
        
        # Toolbar vertical container
        vtoolbar = tk.Frame(vtoolbar_frame, bg='#2C3E50', relief='raised', borderwidth=2)
        vtoolbar.pack(fill='y', padx=5, pady=5)
        
        # Botones verticales
        vertical_tools = [
            ('settings', 'Configuración', self.toolbar_settings),
            ('print', 'Imprimir', self.toolbar_print),
            ('help', 'Ayuda', self.toolbar_help),
            ('exit', 'Salir', self.toolbar_exit)
        ]
        
        for name, tooltip, command in vertical_tools:
            icon = self.icons.get(name, f"[{name}]")
            btn = tk.Button(
                vtoolbar,
                text=icon,
                font=("Arial", 12),
                bg='#3498DB',
                fg='white',
                width=4,
                height=2,
                relief='raised',
                borderwidth=1,
                command=command
            )
            btn.pack(pady=2, padx=2)
            
            # Tooltip simple
            self.create_tooltip(btn, tooltip)
            
        # Información del toolbar vertical  
        info_vtoolbar = tk.LabelFrame(
            container,
            text="ℹ️ Información",
            font=("Arial", 11, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=10
        )
        info_vtoolbar.pack(side='left', fill='both', expand=True, padx=(10, 0))
        
        tk.Label(
            info_vtoolbar,
            text="🔧 Características del Toolbar:\n\n"
                 "✅ Iconos personalizables\n"
                 "✅ Tooltips informativos\n" 
                 "✅ Separadores visuales\n"
                 "✅ Grupos lógicos de acciones\n"
                 "✅ Orientación horizontal/vertical\n"
                 "✅ Estilos personalizables\n"
                 "✅ Acciones vinculadas a funciones\n\n"
                 "💡 Pasa el mouse sobre los botones\n"
                 "    para ver los tooltips",
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#CCCCCC',
            justify='left',
            anchor='nw'
        ).pack(fill='both', expand=True)
        
    def create_mask_tab(self):
        """
        Crea la pestaña de demostración de entrada enmascarada
        """
        mask_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(mask_frame, text="🎭 Máscaras")
        
        # Header informativo
        info_frame = tk.Frame(mask_frame, bg='#2D2D30', relief='raised', borderwidth=2)
        info_frame.pack(fill='x', padx=10, pady=(10, 0))
        
        tk.Label(
            info_frame,
            text="🎭 Entrada Enmascarada (Masked Input)",
            font=("Arial", 14, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(pady=10)
        
        tk.Label(
            info_frame,
            text="Implementación de máscaras de entrada para formatear automáticamente\n"
                 "datos como teléfonos, DNI, fechas, tarjetas de crédito, etc.\n"
                 "Usando validación con funciones de callback y expresiones regulares.",
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#CCCCCC',
            justify='left'
        ).pack(pady=(0, 10), padx=15)
        
        # Frame principal
        main_frame = tk.Frame(mask_frame, bg='#1E1E1E')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === FORMULARIO CON MÁSCARAS ===
        form_frame = tk.LabelFrame(
            main_frame,
            text="📋 Formulario con Campos Enmascarados",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=20,
            pady=20
        )
        form_frame.pack(fill='x', pady=(0, 15))
        
        # Configurar grid
        form_frame.grid_columnconfigure(1, weight=1)
        
        # Campo: Teléfono
        tk.Label(
            form_frame,
            text="📱 Teléfono:",
            font=("Arial", 11, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).grid(row=0, column=0, sticky='w', pady=10)
        
        self.phone_entry = tk.Entry(
            form_frame,
            textvariable=self.phone_var,
            font=("Arial", 11),
            bg='#3C3C3C',
            fg='#FFFFFF',
            insertbackground='#FFFFFF',
            width=20
        )
        self.phone_entry.grid(row=0, column=1, sticky='w', padx=(10, 0), pady=10)
        self.phone_entry.bind('<KeyRelease>', lambda e: self.format_phone(e))
        
        tk.Label(
            form_frame,
            text="Formato: (123) 456-7890",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#95A5A6'
        ).grid(row=0, column=2, sticky='w', padx=(10, 0), pady=10)
        
        # Campo: DNI/ID
        tk.Label(
            form_frame,
            text="🆔 DNI:",
            font=("Arial", 11, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).grid(row=1, column=0, sticky='w', pady=10)
        
        self.dni_entry = tk.Entry(
            form_frame,
            textvariable=self.dni_var,
            font=("Arial", 11),
            bg='#3C3C3C',
            fg='#FFFFFF',
            insertbackground='#FFFFFF',
            width=20
        )
        self.dni_entry.grid(row=1, column=1, sticky='w', padx=(10, 0), pady=10)
        self.dni_entry.bind('<KeyRelease>', lambda e: self.format_dni(e))
        
        tk.Label(
            form_frame,
            text="Formato: 12.345.678-9",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#95A5A6'
        ).grid(row=1, column=2, sticky='w', padx=(10, 0), pady=10)
        
        # Campo: Fecha
        tk.Label(
            form_frame,
            text="📅 Fecha:",
            font=("Arial", 11, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).grid(row=2, column=0, sticky='w', pady=10)
        
        self.date_entry = tk.Entry(
            form_frame,
            textvariable=self.date_var,
            font=("Arial", 11),
            bg='#3C3C3C',
            fg='#FFFFFF',
            insertbackground='#FFFFFF',
            width=20
        )
        self.date_entry.grid(row=2, column=1, sticky='w', padx=(10, 0), pady=10)
        self.date_entry.bind('<KeyRelease>', lambda e: self.format_date(e))
        
        tk.Label(
            form_frame,
            text="Formato: DD/MM/AAAA",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#95A5A6'
        ).grid(row=2, column=2, sticky='w', padx=(10, 0), pady=10)
        
        # Campo: Tarjeta de Crédito
        tk.Label(
            form_frame,
            text="💳 Tarjeta:",
            font=("Arial", 11, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).grid(row=3, column=0, sticky='w', pady=10)
        
        self.credit_entry = tk.Entry(
            form_frame,
            textvariable=self.credit_card_var,
            font=("Arial", 11),
            bg='#3C3C3C',
            fg='#FFFFFF',
            insertbackground='#FFFFFF',
            width=25,
            show='*'  # Ocultar números por seguridad
        )
        self.credit_entry.grid(row=3, column=1, sticky='w', padx=(10, 0), pady=10)
        self.credit_entry.bind('<KeyRelease>', lambda e: self.format_credit_card(e))
        
        tk.Label(
            form_frame,
            text="Formato: 1234 5678 9012 3456",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#95A5A6'
        ).grid(row=3, column=2, sticky='w', padx=(10, 0), pady=10)
        
        # Botones de acción
        button_frame = tk.Frame(form_frame, bg='#2D2D30')
        button_frame.grid(row=4, column=0, columnspan=3, pady=20)
        
        tk.Button(
            button_frame,
            text="✅ Validar Campos",
            font=("Arial", 10, "bold"),
            bg='#27AE60',
            fg='white',
            command=self.validate_masked_fields,
            padx=20,
            pady=8
        ).pack(side='left', padx=(0, 10))
        
        tk.Button(
            button_frame,
            text="🧹 Limpiar",
            font=("Arial", 10),
            bg='#E67E22',
            fg='white',
            command=self.clear_masked_fields,
            padx=20,
            pady=8
        ).pack(side='left', padx=(0, 10))
        
        tk.Button(
            button_frame,
            text="👁️ Mostrar/Ocultar Tarjeta",
            font=("Arial", 10),
            bg='#9B59B6',
            fg='white',
            command=self.toggle_credit_card_visibility,
            padx=20,
            pady=8
        ).pack(side='left')
        
        # === ÁREA DE INFORMACIÓN ===
        info_mask_frame = tk.LabelFrame(
            main_frame,
            text="ℹ️ Información sobre Máscaras",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        info_mask_frame.pack(fill='both', expand=True)
        
        info_text = tk.Text(
            info_mask_frame,
            font=("Courier", 10),
            bg='#3C3C3C',
            fg='#FFFFFF',
            wrap=tk.WORD,
            height=12
        )
        info_text.pack(fill='both', expand=True)
        
        mask_info = """🎭 IMPLEMENTACIÓN DE MÁSCARAS EN TKINTER

📋 TÉCNICAS UTILIZADAS:
══════════════════════════════════════════════════════════

1️⃣ VALIDACIÓN CON EVENTOS:
   • <KeyRelease>: Se ejecuta después de cada tecla
   • Permite formatear el texto en tiempo real
   • No bloquea la entrada del usuario

2️⃣ EXPRESIONES REGULARES:
   • re.sub(): Reemplaza caracteres no deseados
   • Patrones específicos para cada tipo de dato
   • Validación de formato completo

3️⃣ VARIABLES TKINTER:
   • StringVar(): Vincula datos con widgets
   • Permite rastrear cambios automáticamente
   • Facilita la validación cruzada

🔧 PERSONALIZACIÓN:
══════════════════════════════════════════════════════════

📱 Teléfono: Permite solo dígitos, formatea automáticamente
🆔 DNI: Añade puntos y guión en posiciones correctas
📅 Fecha: Valida día/mes/año con barras automáticas
💳 Tarjeta: Agrupa en bloques de 4 dígitos

💡 CONSEJOS:
══════════════════════════════════════════════════════════

✅ Siempre validar en el servidor también
✅ Proporcionar feedback visual inmediato
✅ Permitir pegado y mantener formato
✅ Considerar internacionalización
✅ Usar show='*' para datos sensibles"""

        info_text.insert(tk.END, mask_info)
        info_text.config(state='disabled')  # Solo lectura
        
    def create_custom_controls_tab(self):
        """
        Crea la pestaña de controles personalizados
        """
        custom_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(custom_frame, text="🎨 Personalizados")
        
        # Título
        tk.Label(
            custom_frame,
            text="🎨 Controles Personalizados",
            font=("Arial", 16, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        ).pack(pady=15)
        
        # Frame principal
        main_frame = tk.Frame(custom_frame, bg='#1E1E1E')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === CONTROL PERSONALIZADO 1: RATING ===
        rating_frame = tk.LabelFrame(
            main_frame,
            text="⭐ Control de Calificación (Rating)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        rating_frame.pack(fill='x', pady=(0, 15))
        
        tk.Label(
            rating_frame,
            text="Califica este producto:",
            font=("Arial", 11),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(anchor='w', pady=(0, 10))
        
        # Rating widget personalizado
        self.create_rating_widget(rating_frame)
        
        # === CONTROL PERSONALIZADO 2: COLOR PICKER ===
        color_frame = tk.LabelFrame(
            main_frame,
            text="🎨 Selector de Color Personalizado",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        color_frame.pack(fill='x', pady=(0, 15))
        
        self.create_color_picker_widget(color_frame)
        
        # === CONTROL PERSONALIZADO 3: SLIDER PERSONALIZADO ===
        slider_frame = tk.LabelFrame(
            main_frame,
            text="🎚️ Slider Personalizado con Indicadores",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        slider_frame.pack(fill='both', expand=True)
        
        self.create_custom_slider_widget(slider_frame)

    # ====================================================================
    # MÉTODOS DE IMAGELIST
    # ====================================================================
    
    def icon_clicked(self, icon_name):
        """Maneja clicks en iconos del ImageList"""
        timestamp = tk.datetime.datetime.now().strftime("%H:%M:%S")
        message = f"[{timestamp}] 🖱️ Icono clickeado: '{icon_name}' ({self.icons[icon_name]})\n"
        
        self.imagelist_result.insert(tk.END, message)
        self.imagelist_result.see(tk.END)
        
    # ====================================================================
    # MÉTODOS DE TOOLBAR
    # ====================================================================
    
    def create_toolbar_group(self, toolbar, buttons):
        """Crea un grupo de botones en el toolbar"""
        for name, tooltip, command in buttons:
            icon = self.icons.get(name, f"[{name}]")
            
            btn = tk.Button(
                toolbar,
                text=icon,
                font=("Arial", 10),
                bg='#3498DB',
                fg='white',
                width=6,
                height=2,
                relief='raised',
                borderwidth=1,
                command=command
            )
            btn.pack(side='left', padx=1, pady=2)
            
            # Agregar tooltip
            self.create_tooltip(btn, tooltip)
            
    def create_toolbar_separator(self, toolbar):
        """Crea un separador visual en el toolbar"""
        separator = tk.Frame(
            toolbar,
            bg='#2C3E50',
            width=2,
            height=30,
            relief='sunken',
            borderwidth=1
        )
        separator.pack(side='left', padx=5, pady=5)
        
    def create_tooltip(self, widget, text):
        """Crea un tooltip simple para un widget"""
        def on_enter(event):
            tooltip = tk.Toplevel()
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root+10}+{event.y_root+10}")
            
            label = tk.Label(
                tooltip,
                text=text,
                background='#FFFFE0',
                foreground='black',
                relief='solid',
                borderwidth=1,
                font=("Arial", 9)
            )
            label.pack()
            
            widget.tooltip = tooltip
            
        def on_leave(event):
            if hasattr(widget, 'tooltip'):
                widget.tooltip.destroy()
                del widget.tooltip
                
        widget.bind('<Enter>', on_enter)
        widget.bind('<Leave>', on_leave)
    
    # Métodos de acción del toolbar
    def toolbar_new(self):
        if hasattr(self, 'work_text'):
            self.work_text.delete(1.0, tk.END)
            self.work_text.insert(tk.END, "📄 Nuevo documento creado\n\n")
            
    def toolbar_open(self):
        if hasattr(self, 'work_text'):
            filename = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
            if filename:
                try:
                    with open(filename, 'r') as f:
                        content = f.read()
                        self.work_text.delete(1.0, tk.END)
                        self.work_text.insert(tk.END, content)
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo abrir el archivo: {str(e)}")
                    
    def toolbar_save(self):
        if hasattr(self, 'work_text'):
            filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
            if filename:
                try:
                    with open(filename, 'w') as f:
                        content = self.work_text.get(1.0, tk.END)
                        f.write(content)
                    messagebox.showinfo("Guardado", "Archivo guardado correctamente")
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo guardar el archivo: {str(e)}")
                    
    def toolbar_cut(self):
        if hasattr(self, 'work_text'):
            try:
                self.work_text.event_generate("<<Cut>>")
            except:
                pass
                
    def toolbar_copy(self):
        if hasattr(self, 'work_text'):
            try:
                self.work_text.event_generate("<<Copy>>")
            except:
                pass
                
    def toolbar_paste(self):
        if hasattr(self, 'work_text'):
            try:
                self.work_text.event_generate("<<Paste>>")
            except:
                pass
                
    def toolbar_undo(self):
        if hasattr(self, 'work_text'):
            try:
                self.work_text.edit_undo()
            except:
                pass
                
    def toolbar_redo(self):
        if hasattr(self, 'work_text'):
            try:
                self.work_text.edit_redo()
            except:
                pass
                
    def toolbar_find(self):
        messagebox.showinfo("Buscar", "🔍 Función de búsqueda activada")
        
    def toolbar_replace(self):
        messagebox.showinfo("Reemplazar", "🔄 Función de reemplazar activada")
        
    def toolbar_settings(self):
        messagebox.showinfo("Configuración", "⚙️ Panel de configuración")
        
    def toolbar_print(self):
        messagebox.showinfo("Imprimir", "🖨️ Enviando a impresora...")
        
    def toolbar_help(self):
        messagebox.showinfo("Ayuda", "❓ Sistema de ayuda\n\nDocumentación disponible en línea")
        
    def toolbar_exit(self):
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
            self.root.quit()
    
    # ====================================================================
    # MÉTODOS DE MÁSCARAS
    # ====================================================================
    
    def format_phone(self, event):
        """Formatea el número de teléfono automáticamente"""
        value = re.sub(r'\D', '', self.phone_var.get())  # Solo dígitos
        
        if len(value) >= 10:
            value = value[:10]  # Máximo 10 dígitos
            formatted = f"({value[:3]}) {value[3:6]}-{value[6:]}"
            self.phone_var.set(formatted)
        elif len(value) >= 6:
            formatted = f"({value[:3]}) {value[3:]}"
            self.phone_var.set(formatted)
        elif len(value) >= 3:
            formatted = f"({value})"
            self.phone_var.set(formatted)
        else:
            self.phone_var.set(value)
            
    def format_dni(self, event):
        """Formatea el DNI automáticamente"""
        value = re.sub(r'\D', '', self.dni_var.get())  # Solo dígitos
        
        if len(value) >= 9:
            value = value[:9]  # Máximo 9 dígitos
            formatted = f"{value[:2]}.{value[2:5]}.{value[5:8]}-{value[8]}"
            self.dni_var.set(formatted)
        elif len(value) >= 8:
            formatted = f"{value[:2]}.{value[2:5]}.{value[5:]}"
            self.dni_var.set(formatted)
        elif len(value) >= 5:
            formatted = f"{value[:2]}.{value[2:]}"
            self.dni_var.set(formatted)
        else:
            self.dni_var.set(value)
            
    def format_date(self, event):
        """Formatea la fecha automáticamente"""
        value = re.sub(r'\D', '', self.date_var.get())  # Solo dígitos
        
        if len(value) >= 8:
            value = value[:8]  # Máximo 8 dígitos
            formatted = f"{value[:2]}/{value[2:4]}/{value[4:]}"
            self.date_var.set(formatted)
        elif len(value) >= 4:
            formatted = f"{value[:2]}/{value[2:]}"
            self.date_var.set(formatted)
        else:
            self.date_var.set(value)
            
    def format_credit_card(self, event):
        """Formatea la tarjeta de crédito automáticamente"""
        value = re.sub(r'\D', '', self.credit_card_var.get())  # Solo dígitos
        
        if len(value) > 16:
            value = value[:16]  # Máximo 16 dígitos
            
        # Agregar espacios cada 4 dígitos
        formatted = ' '.join([value[i:i+4] for i in range(0, len(value), 4)])
        self.credit_card_var.set(formatted)
        
    def validate_masked_fields(self):
        """Valida todos los campos con máscara"""
        results = []
        
        # Validar teléfono
        phone = self.phone_var.get()
        phone_digits = re.sub(r'\D', '', phone)
        if len(phone_digits) == 10:
            results.append("✅ Teléfono: Válido")
        else:
            results.append("❌ Teléfono: Incompleto")
            
        # Validar DNI
        dni = self.dni_var.get()
        dni_digits = re.sub(r'\D', '', dni)
        if len(dni_digits) == 9:
            results.append("✅ DNI: Válido")
        else:
            results.append("❌ DNI: Incompleto")
            
        # Validar fecha
        date = self.date_var.get()
        date_digits = re.sub(r'\D', '', date)
        if len(date_digits) == 8:
            # Validación básica de fecha
            try:
                day, month, year = int(date_digits[:2]), int(date_digits[2:4]), int(date_digits[4:])
                if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100:
                    results.append("✅ Fecha: Válida")
                else:
                    results.append("❌ Fecha: Fuera de rango")
            except:
                results.append("❌ Fecha: Formato inválido")
        else:
            results.append("❌ Fecha: Incompleta")
            
        # Validar tarjeta
        card = self.credit_card_var.get()
        card_digits = re.sub(r'\D', '', card)
        if len(card_digits) == 16:
            results.append("✅ Tarjeta: Válida")
        else:
            results.append("❌ Tarjeta: Incompleta")
            
        messagebox.showinfo("Validación de Campos", "\n".join(results))
        
    def clear_masked_fields(self):
        """Limpia todos los campos con máscara"""
        self.phone_var.set("")
        self.dni_var.set("")
        self.date_var.set("")
        self.credit_card_var.set("")
        
    def toggle_credit_card_visibility(self):
        """Alterna la visibilidad de la tarjeta de crédito"""
        current_show = self.credit_entry.cget('show')
        if current_show == '*':
            self.credit_entry.config(show='')
        else:
            self.credit_entry.config(show='*')
    
    # ====================================================================
    # CONTROLES PERSONALIZADOS
    # ====================================================================
    
    def create_rating_widget(self, parent):
        """Crea un widget de calificación con estrellas"""
        self.rating_value = tk.IntVar(value=3)
        
        rating_container = tk.Frame(parent, bg='#2D2D30')
        rating_container.pack(anchor='w', pady=10)
        
        self.star_buttons = []
        
        for i in range(5):
            star_btn = tk.Button(
                rating_container,
                text="⭐",
                font=("Arial", 20),
                bg='#2D2D30',
                fg='#FFD700' if i < self.rating_value.get() else '#666666',
                relief='flat',
                borderwidth=0,
                command=lambda x=i+1: self.set_rating(x)
            )
            star_btn.pack(side='left')
            self.star_buttons.append(star_btn)
            
        # Label del rating actual
        self.rating_label = tk.Label(
            rating_container,
            text=f"({self.rating_value.get()}/5)",
            font=("Arial", 11),
            bg='#2D2D30',
            fg='#FFFFFF'
        )
        self.rating_label.pack(side='left', padx=(10, 0))
        
    def set_rating(self, value):
        """Establece el valor del rating"""
        self.rating_value.set(value)
        
        # Actualizar colores de las estrellas
        for i, btn in enumerate(self.star_buttons):
            if i < value:
                btn.config(fg='#FFD700')
            else:
                btn.config(fg='#666666')
                
        # Actualizar label
        self.rating_label.config(text=f"({value}/5)")
        
    def create_color_picker_widget(self, parent):
        """Crea un selector de color personalizado"""
        colors = [
            '#FF6B6B', '#4ECDC4', '#45B7D1', '#F7DC6F', 
            '#BB8FCE', '#82E0AA', '#F39C12', '#E74C3C'
        ]
        
        self.selected_color = tk.StringVar(value=colors[0])
        
        color_container = tk.Frame(parent, bg='#2D2D30')
        color_container.pack(fill='x', pady=10)
        
        tk.Label(
            color_container,
            text="Selecciona un color:",
            font=("Arial", 11),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(anchor='w', pady=(0, 10))
        
        # Grid de colores
        color_grid = tk.Frame(color_container, bg='#2D2D30')
        color_grid.pack(anchor='w')
        
        for i, color in enumerate(colors):
            row, col = i // 4, i % 4
            
            color_btn = tk.Button(
                color_grid,
                bg=color,
                width=4,
                height=2,
                relief='raised',
                borderwidth=2,
                command=lambda c=color: self.select_color(c)
            )
            color_btn.grid(row=row, column=col, padx=2, pady=2)
            
        # Mostrar color seleccionado
        self.color_display = tk.Label(
            color_container,
            text="Color seleccionado:",
            font=("Arial", 11),
            bg=self.selected_color.get(),
            fg='white',
            width=20,
            height=2,
            relief='sunken',
            borderwidth=2
        )
        self.color_display.pack(pady=(15, 0))
        
    def select_color(self, color):
        """Selecciona un color"""
        self.selected_color.set(color)
        self.color_display.config(bg=color)
        self.color_display.config(text=f"Color: {color}")
        
    def create_custom_slider_widget(self, parent):
        """Crea un slider personalizado con indicadores"""
        slider_container = tk.Frame(parent, bg='#2D2D30')
        slider_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(
            slider_container,
            text="Volumen del Sistema:",
            font=("Arial", 11, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(anchor='w', pady=(0, 10))
        
        # Slider principal
        self.volume_var = tk.DoubleVar(value=50)
        
        volume_slider = tk.Scale(
            slider_container,
            from_=0,
            to=100,
            orient='horizontal',
            variable=self.volume_var,
            bg='#3498DB',
            fg='#FFFFFF',
            font=("Arial", 10),
            length=300,
            command=self.on_volume_change
        )
        volume_slider.pack(pady=10)
        
        # Indicadores visuales
        indicators_frame = tk.Frame(slider_container, bg='#2D2D30')
        indicators_frame.pack(pady=(10, 0))
        
        # Barra de volumen visual
        self.volume_bar_frame = tk.Frame(indicators_frame, bg='#34495E', height=20, width=300)
        self.volume_bar_frame.pack()
        self.volume_bar_frame.pack_propagate(False)
        
        self.volume_bar = tk.Frame(self.volume_bar_frame, bg='#2ECC71', height=18)
        self.volume_bar.place(x=1, y=1, width=148, height=18)  # 50% inicial
        
        # Etiquetas de estado
        status_frame = tk.Frame(slider_container, bg='#2D2D30')
        status_frame.pack(fill='x', pady=(15, 0))
        
        self.volume_label = tk.Label(
            status_frame,
            text="🔊 Volumen: 50%",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        )
        self.volume_label.pack()
        
        self.volume_status = tk.Label(
            status_frame,
            text="Medio",
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#F39C12'
        )
        self.volume_status.pack()
        
    def on_volume_change(self, value):
        """Maneja cambios en el slider de volumen"""
        vol = float(value)
        
        # Actualizar barra visual
        bar_width = int((vol / 100) * 298)  # 298 = 300 - 2 (borders)
        
        # Cambiar color según nivel
        if vol < 30:
            color = '#E74C3C'  # Rojo para bajo
            icon = '🔈'
            status = 'Bajo'
        elif vol < 70:
            color = '#F39C12'  # Naranja para medio
            icon = '🔉'
            status = 'Medio'
        else:
            color = '#2ECC71'  # Verde para alto
            icon = '🔊'
            status = 'Alto'
            
        self.volume_bar.config(bg=color)
        self.volume_bar.place(width=bar_width)
        
        # Actualizar etiquetas
        self.volume_label.config(text=f"{icon} Volumen: {int(vol)}%")
        self.volume_status.config(text=status, fg=color)

def main():
    """
    Función principal para ejecutar la demostración
    """
    root = tk.Tk()
    app = AdvancedControlsDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
