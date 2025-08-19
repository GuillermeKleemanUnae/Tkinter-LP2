#!/usr/bin/env python3
"""
Demostración de Geometry Managers en Tkinter
===========================================

Este script demuestra las diferencias entre los tres sistemas de geometría:
- pack: Empaquetado secuencial (top, bottom, left, right)
- grid: Sistema de cuadrícula (filas y columnas)
- place: Posicionamiento absoluto y relativo

IMPORTANTE: Nunca mezcles pack() y grid() en el mismo contenedor padre,
pero sí puedes usar place() con cualquiera de los otros dos.

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random

class GeometryManagerDemo:
    """
    Clase que demuestra los diferentes geometry managers
    """
    
    def __init__(self, root):
        """
        Inicializa la aplicación
        
        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.setup_window()
        self.create_main_interface()
        
    def setup_window(self):
        """
        Configura la ventana principal
        """
        self.root.title("📐 Demostración de Geometry Managers")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1E1E1E')
        self.root.resizable(True, True)
        
        # Centrar ventana
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_main_interface(self):
        """
        Crea la interfaz principal con pestañas para cada geometry manager
        """
        # Título principal
        title_label = tk.Label(
            self.root,
            text="📐 Geometry Managers: pack() vs grid() vs place()",
            font=("Arial", 16, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        )
        title_label.pack(pady=15)
        
        # Crear notebook para organizar ejemplos
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Crear pestañas para cada geometry manager
        self.create_pack_tab()
        self.create_grid_tab()
        self.create_place_tab()
        self.create_comparison_tab()
        self.create_mixed_tab()
        
    def create_pack_tab(self):
        """
        Crea la pestaña de demostración de pack()
        """
        pack_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(pack_frame, text="📦 PACK")
        
        # Header informativo
        info_frame = tk.Frame(pack_frame, bg='#2D2D30', relief='raised', borderwidth=2)
        info_frame.pack(fill='x', padx=10, pady=(10, 0))
        
        tk.Label(
            info_frame,
            text="📦 PACK - Empaquetado Secuencial",
            font=("Arial", 14, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(pady=10)
        
        tk.Label(
            info_frame,
            text="Pack organiza widgets secuencialmente: top → bottom → left → right\n"
                 "• Simple y rápido para layouts lineales\n"
                 "• Ideal para barras de herramientas, botones en fila\n"
                 "• Opciones: side, fill, expand, padx, pady, anchor",
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#CCCCCC',
            justify='left'
        ).pack(pady=(0, 10), padx=15)
        
        # Frame principal para ejemplos
        main_frame = tk.Frame(pack_frame, bg='#1E1E1E')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === EJEMPLO 1: PACK BÁSICO ===
        example1 = tk.LabelFrame(
            main_frame,
            text="🔹 Ejemplo 1: Pack Básico (side)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=10
        )
        example1.pack(fill='x', pady=(0, 10))
        
        # Controles
        control_frame1 = tk.Frame(example1, bg='#2D2D30')
        control_frame1.pack(fill='x', pady=(0, 10))
        
        tk.Button(
            control_frame1,
            text="🔄 Resetear",
            font=("Arial", 9),
            bg='#FF6B6B',
            fg='black',
            command=lambda: self.reset_pack_demo(demo_frame1),
            width=12
        ).pack(side='left', padx=(0, 5))
        
        tk.Button(
            control_frame1,
            text="📦 TOP",
            font=("Arial", 9),
            bg='#4ECDC4',
            fg='black',
            command=lambda: self.add_pack_widget(demo_frame1, 'top'),
            width=8
        ).pack(side='left', padx=(0, 5))
        
        tk.Button(
            control_frame1,
            text="📦 BOTTOM",
            font=("Arial", 9),
            bg='#45B7D1',
            fg='black',
            command=lambda: self.add_pack_widget(demo_frame1, 'bottom'),
            width=8
        ).pack(side='left', padx=(0, 5))
        
        tk.Button(
            control_frame1,
            text="📦 LEFT",
            font=("Arial", 9),
            bg='#F7DC6F',
            fg='black',
            command=lambda: self.add_pack_widget(demo_frame1, 'left'),
            width=8
        ).pack(side='left', padx=(0, 5))
        
        tk.Button(
            control_frame1,
            text="📦 RIGHT",
            font=("Arial", 9),
            bg='#BB8FCE',
            fg='black',
            command=lambda: self.add_pack_widget(demo_frame1, 'right'),
            width=8
        ).pack(side='left')
        
        # Área de demostración
        demo_frame1 = tk.Frame(example1, bg='#3C3C3C', relief='sunken', borderwidth=2, height=150)
        demo_frame1.pack(fill='both', expand=True)
        demo_frame1.pack_propagate(False)  # Mantener tamaño fijo
        
        # === EJEMPLO 2: PACK CON FILL Y EXPAND ===
        example2 = tk.LabelFrame(
            main_frame,
            text="🔹 Ejemplo 2: Pack con fill y expand",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=10
        )
        example2.pack(fill='both', expand=True)
        
        # Controles
        control_frame2 = tk.Frame(example2, bg='#2D2D30')
        control_frame2.pack(fill='x', pady=(0, 10))
        
        tk.Button(
            control_frame2,
            text="🔄 Limpiar",
            font=("Arial", 9),
            bg='#FF6B6B',
            fg='black',
            command=lambda: self.clear_frame(demo_frame2),
            width=10
        ).pack(side='left', padx=(0, 10))
        
        # Frame para layout típico
        demo_frame2 = tk.Frame(example2, bg='#3C3C3C', relief='sunken', borderwidth=2)
        demo_frame2.pack(fill='both', expand=True)
        
        # Crear layout típico de aplicación
        self.create_typical_pack_layout(demo_frame2)
        
    def create_grid_tab(self):
        """
        Crea la pestaña de demostración de grid()
        """
        grid_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(grid_frame, text="🔲 GRID")
        
        # Header informativo
        info_frame = tk.Frame(grid_frame, bg='#2D2D30', relief='raised', borderwidth=2)
        info_frame.pack(fill='x', padx=10, pady=(10, 0))
        
        tk.Label(
            info_frame,
            text="🔲 GRID - Sistema de Cuadrícula",
            font=("Arial", 14, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(pady=10)
        
        tk.Label(
            info_frame,
            text="Grid organiza widgets en filas y columnas como una tabla\n"
                 "• Perfecto para formularios y layouts complejos\n"
                 "• Control preciso de posición y tamaño\n"
                 "• Opciones: row, column, rowspan, columnspan, sticky, padx, pady",
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#CCCCCC',
            justify='left'
        ).pack(pady=(0, 10), padx=15)
        
        # Frame principal para ejemplos
        main_frame = tk.Frame(grid_frame, bg='#1E1E1E')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === EJEMPLO 1: GRID BÁSICO ===
        example1 = tk.LabelFrame(
            main_frame,
            text="🔹 Ejemplo 1: Grid Básico - Formulario",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=10
        )
        example1.pack(fill='x', pady=(0, 10))
        
        # Crear formulario con grid
        self.create_grid_form(example1)
        
        # === EJEMPLO 2: GRID AVANZADO ===
        example2 = tk.LabelFrame(
            main_frame,
            text="🔹 Ejemplo 2: Grid Avanzado - Calculadora",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=10
        )
        example2.pack(fill='both', expand=True)
        
        # Crear calculadora con grid
        self.create_grid_calculator(example2)
        
    def create_place_tab(self):
        """
        Crea la pestaña de demostración de place()
        """
        place_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(place_frame, text="📍 PLACE")
        
        # Header informativo
        info_frame = tk.Frame(place_frame, bg='#2D2D30', relief='raised', borderwidth=2)
        info_frame.pack(fill='x', padx=10, pady=(10, 0))
        
        tk.Label(
            info_frame,
            text="📍 PLACE - Posicionamiento Absoluto/Relativo",
            font=("Arial", 14, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF'
        ).pack(pady=10)
        
        tk.Label(
            info_frame,
            text="Place permite posicionamiento exacto con coordenadas\n"
                 "• Control total sobre posición y tamaño\n"
                 "• Puede superponerse con pack/grid en el mismo padre\n"
                 "• Opciones: x, y, relx, rely, width, height, relwidth, relheight, anchor",
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#CCCCCC',
            justify='left'
        ).pack(pady=(0, 10), padx=15)
        
        # Frame principal para ejemplos
        main_frame = tk.Frame(place_frame, bg='#1E1E1E')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === EJEMPLO 1: PLACE ABSOLUTO ===
        example1 = tk.LabelFrame(
            main_frame,
            text="🔹 Ejemplo 1: Posicionamiento Absoluto",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=10
        )
        example1.pack(fill='x', pady=(0, 10))
        
        # Controles para place absoluto
        control_frame1 = tk.Frame(example1, bg='#2D2D30')
        control_frame1.pack(fill='x', pady=(0, 10))
        
        tk.Button(
            control_frame1,
            text="📍 Colocar Widget",
            font=("Arial", 9),
            bg='#E74C3C',
            fg='black',
            command=lambda: self.place_random_widget(demo_place1),
            width=15
        ).pack(side='left', padx=(0, 10))
        
        tk.Button(
            control_frame1,
            text="🧹 Limpiar",
            font=("Arial", 9),
            bg='#34495E',
            fg='black',
            command=lambda: self.clear_frame(demo_place1),
            width=10
        ).pack(side='left')
        
        # Área de demostración absoluta
        demo_place1 = tk.Frame(example1, bg='#2C3E50', relief='sunken', borderwidth=2, height=200)
        demo_place1.pack(fill='x')
        demo_place1.pack_propagate(False)
        
        # === EJEMPLO 2: PLACE RELATIVO ===
        example2 = tk.LabelFrame(
            main_frame,
            text="🔹 Ejemplo 2: Posicionamiento Relativo - Dashboard",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=10
        )
        example2.pack(fill='both', expand=True)
        
        # Crear dashboard con place relativo
        self.create_place_dashboard(example2)
        
    def create_comparison_tab(self):
        """
        Crea la pestaña de comparación entre geometry managers
        """
        comp_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(comp_frame, text="⚖️ COMPARACIÓN")
        
        # Título
        tk.Label(
            comp_frame,
            text="⚖️ Comparación de Geometry Managers",
            font=("Arial", 16, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        ).pack(pady=15)
        
        # Frame para comparación lado a lado
        comparison_frame = tk.Frame(comp_frame, bg='#1E1E1E')
        comparison_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Configurar columnas
        comparison_frame.grid_columnconfigure(0, weight=1)
        comparison_frame.grid_columnconfigure(1, weight=1)
        comparison_frame.grid_columnconfigure(2, weight=1)
        
        # === PACK COMPARISON ===
        pack_comp = tk.LabelFrame(
            comparison_frame,
            text="📦 PACK",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#4ECDC4',
            padx=10,
            pady=10
        )
        pack_comp.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        
        pack_info = """
✅ VENTAJAS:
• Rápido y simple
• Ideal para layouts lineales
• Automáticamente responsive
• Menos código

❌ DESVENTAJAS:  
• Control limitado de posición
• Difícil para layouts complejos
• No mezclar con grid()

🎯 MEJOR PARA:
• Barras de herramientas
• Botones en fila/columna
• Layouts simples
• Prototipos rápidos
"""
        
        tk.Label(
            pack_comp,
            text=pack_info,
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#FFFFFF',
            justify='left',
            anchor='nw'
        ).pack(fill='both', expand=True)
        
        # === GRID COMPARISON ===
        grid_comp = tk.LabelFrame(
            comparison_frame,
            text="🔲 GRID",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#45B7D1',
            padx=10,
            pady=10
        )
        grid_comp.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        
        grid_info = """
✅ VENTAJAS:
• Control preciso de layout
• Perfecto para formularios
• Span de filas/columnas
• Fácil alineación

❌ DESVENTAJAS:
• Más complejo que pack
• Requiere planificación
• No mezclar con pack()

🎯 MEJOR PARA:
• Formularios
• Tablas de datos
• Layouts estructurados
• Interfaces complejas
"""
        
        tk.Label(
            grid_comp,
            text=grid_info,
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#FFFFFF',
            justify='left',
            anchor='nw'
        ).pack(fill='both', expand=True)
        
        # === PLACE COMPARISON ===
        place_comp = tk.LabelFrame(
            comparison_frame,
            text="📍 PLACE",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#E74C3C',
            padx=10,
            pady=10
        )
        place_comp.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
        
        place_info = """
✅ VENTAJAS:
• Control absoluto
• Superposición de widgets
• Posicionamiento exacto
• Combina con pack/grid

❌ DESVENTAJAS:
• No responsive automático
• Requiere cálculos manuales
• Puede ser complejo

🎯 MEJOR PARA:
• Overlays y tooltips
• Posicionamiento exacto
• Efectos visuales
• Gaming/multimedia
"""
        
        tk.Label(
            place_comp,
            text=place_info,
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#FFFFFF',
            justify='left',
            anchor='nw'
        ).pack(fill='both', expand=True)
        
        # Tabla de comparación rápida
        table_frame = tk.LabelFrame(
            comp_frame,
            text="📊 Tabla de Comparación Rápida",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        table_frame.pack(fill='x', padx=10, pady=10)
        
        # Crear tabla
        table_data = [
            ["Característica", "PACK", "GRID", "PLACE"],
            ["Facilidad de uso", "⭐⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐"],
            ["Control de layout", "⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
            ["Responsive", "⭐⭐⭐⭐⭐", "⭐⭐⭐⭐", "⭐"],
            ["Layouts complejos", "⭐", "⭐⭐⭐⭐⭐", "⭐⭐⭐"],
            ["Superposición", "❌", "❌", "✅"],
            ["Tiempo desarrollo", "⚡ Rápido", "⏳ Medio", "🐌 Lento"]
        ]
        
        for i, row in enumerate(table_data):
            row_frame = tk.Frame(table_frame, bg='#2D2D30')
            row_frame.pack(fill='x', pady=1)
            
            for j, cell in enumerate(row):
                bg_color = '#34495E' if i == 0 else '#2D2D30'
                font_weight = 'bold' if i == 0 else 'normal'
                
                tk.Label(
                    row_frame,
                    text=cell,
                    font=("Arial", 9, font_weight),
                    bg=bg_color,
                    fg='#FFFFFF',
                    width=20,
                    relief='ridge',
                    borderwidth=1
                ).pack(side='left', fill='x', expand=True)
    
    def create_mixed_tab(self):
        """
        Crea la pestaña que demuestra cómo combinar geometry managers
        """
        mixed_frame = tk.Frame(self.notebook, bg='#1E1E1E')
        self.notebook.add(mixed_frame, text="🔀 COMBINADOS")
        
        # Título
        tk.Label(
            mixed_frame,
            text="🔀 Combinando Geometry Managers",
            font=("Arial", 16, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        ).pack(pady=15)
        
        # Información importante
        warning_frame = tk.Frame(mixed_frame, bg='#E74C3C', relief='raised', borderwidth=3)
        warning_frame.pack(fill='x', padx=10, pady=(0, 10))
        
        tk.Label(
            warning_frame,
            text="⚠️ REGLA IMPORTANTE: ¡NUNCA mezcles pack() y grid() en el mismo Frame padre!",
            font=("Arial", 12, "bold"),
            bg='#E74C3C',
            fg='#FFFFFF'
        ).pack(pady=10)
        
        tk.Label(
            warning_frame,
            text="✅ SÍ puedes usar place() con pack() o grid() en el mismo Frame",
            font=("Arial", 11),
            bg='#E74C3C',
            fg='#FFFFFF'
        ).pack(pady=(0, 10))
        
        # Ejemplo de aplicación real combinando managers
        app_frame = tk.LabelFrame(
            mixed_frame,
            text="🏗️ Ejemplo: Aplicación Real (Pack + Grid + Place)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=10
        )
        app_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.create_real_app_example(app_frame)
        
    # ====================================================================
    # MÉTODOS AUXILIARES PARA PACK
    # ====================================================================
    
    def reset_pack_demo(self, parent):
        """Limpia el área de demostración de pack"""
        self.clear_frame(parent)
        
    def add_pack_widget(self, parent, side):
        """Añade un widget con pack usando el side especificado"""
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#F7DC6F', '#BB8FCE', '#82E0AA']
        color = random.choice(colors)
        
        widget_count = len(parent.winfo_children()) + 1
        
        label = tk.Label(
            parent,
            text=f"{side.upper()}\n#{widget_count}",
            font=("Arial", 10, "bold"),
            bg=color,
            fg='black' if color in ['#FF6B6B', '#45B7D1', '#BB8FCE'] else 'black',
            width=8,
            height=3,
            relief='raised',
            borderwidth=2
        )
        
        # Aplicar pack con el side correspondiente
        if side in ['top', 'bottom']:
            label.pack(side=side, fill='x', padx=5, pady=2)
        else:  # left, right
            label.pack(side=side, fill='y', padx=2, pady=5)
            
    def create_typical_pack_layout(self, parent):
        """Crea un layout típico de aplicación usando pack"""
        # Título (top)
        title = tk.Label(
            parent,
            text="📱 Layout Típico con Pack",
            font=("Arial", 12, "bold"),
            bg='#34495E',
            fg='#FFFFFF',
            pady=10
        )
        title.pack(side='top', fill='x')
        
        # Barra de herramientas (top)
        toolbar = tk.Frame(parent, bg='#3498DB', height=40)
        toolbar.pack(side='top', fill='x')
        toolbar.pack_propagate(False)
        
        for i, text in enumerate(['📁 Archivo', '✏️ Editar', '🔧 Herramientas', '❓ Ayuda']):
            tk.Button(
                toolbar,
                text=text,
                font=("Arial", 9),
                bg='#2980B9',
                fg='black',
                relief='flat',
                padx=15
            ).pack(side='left', padx=2, pady=5)
            
        # Barra de estado (bottom)
        status = tk.Label(
            parent,
            text="💡 Listo | Pack Layout | 12:34:56",
            font=("Arial", 9),
            bg='#95A5A6',
            fg='black',
            anchor='w',
            padx=10
        )
        status.pack(side='bottom', fill='x')
        
        # Sidebar (left)
        sidebar = tk.Frame(parent, bg='#E74C3C', width=150)
        sidebar.pack(side='left', fill='y')
        sidebar.pack_propagate(False)
        
        tk.Label(
            sidebar,
            text="📂 Navegación",
            font=("Arial", 10, "bold"),
            bg='#E74C3C',
            fg='black',
            pady=10
        ).pack(fill='x')
        
        for item in ['📄 Documentos', '🖼️ Imágenes', '🎵 Música', '📹 Videos']:
            tk.Button(
                sidebar,
                text=item,
                font=("Arial", 9),
                bg='#C0392B',
                fg='black',
                relief='flat',
                anchor='w',
                padx=10
            ).pack(fill='x', padx=5, pady=1)
        
        # Área principal (fill restante)
        main_area = tk.Frame(parent, bg='#FFFFFF')
        main_area.pack(fill='both', expand=True)
        
        tk.Label(
            main_area,
            text="📋 Área Principal de Contenido\n\n"
                 "Esta área se expande para llenar\n"
                 "todo el espacio restante gracias a:\n"
                 "pack(fill='both', expand=True)",
            font=("Arial", 11),
            bg='#FFFFFF',
            fg='#2C3E50',
            justify='center'
        ).pack(expand=True)
    
    # ====================================================================
    # MÉTODOS AUXILIARES PARA GRID
    # ====================================================================
    
    def create_grid_form(self, parent):
        """Crea un formulario usando grid"""
        form_frame = tk.Frame(parent, bg='#2D2D30')
        form_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Configurar pesos de columnas
        form_frame.grid_columnconfigure(1, weight=1)
        
        # Campos del formulario
        fields = [
            ("👤 Nombre:", "entry"),
            ("📧 Email:", "entry"),
            ("🎂 Edad:", "spinbox"),
            ("🏢 Empresa:", "entry"),
            ("📱 Teléfono:", "entry"),
            ("📍 Ciudad:", "combobox"),
            ("📝 Comentarios:", "text")
        ]
        
        self.form_widgets = {}
        
        for i, (label_text, widget_type) in enumerate(fields):
            # Etiqueta
            label = tk.Label(
                form_frame,
                text=label_text,
                font=("Arial", 10, "bold"),
                bg='#2D2D30',
                fg='#FFFFFF',
                anchor='w'
            )
            label.grid(row=i, column=0, sticky='w', padx=(0, 10), pady=5)
            
            # Widget correspondiente
            if widget_type == "entry":
                widget = tk.Entry(
                    form_frame,
                    font=("Arial", 10),
                    bg='#3C3C3C',
                    fg='#FFFFFF',
                    insertbackground='#FFFFFF'
                )
                widget.grid(row=i, column=1, sticky='ew', pady=5)
                
            elif widget_type == "spinbox":
                widget = tk.Spinbox(
                    form_frame,
                    from_=18,
                    to=100,
                    font=("Arial", 10),
                    bg='#3C3C3C',
                    fg='#FFFFFF'
                )
                widget.grid(row=i, column=1, sticky='w', pady=5)
                
            elif widget_type == "combobox":
                widget = ttk.Combobox(
                    form_frame,
                    values=["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao"],
                    font=("Arial", 10),
                    state="readonly"
                )
                widget.grid(row=i, column=1, sticky='ew', pady=5)
                
            elif widget_type == "text":
                widget = tk.Text(
                    form_frame,
                    font=("Arial", 10),
                    bg='#3C3C3C',
                    fg='#FFFFFF',
                    height=3,
                    wrap=tk.WORD
                )
                widget.grid(row=i, column=1, sticky='ew', pady=5)
                
            self.form_widgets[label_text] = widget
            
        # Botones (spanning multiple columns)
        button_frame = tk.Frame(form_frame, bg='#2D2D30')
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)
        
        tk.Button(
            button_frame,
            text="💾 Guardar",
            font=("Arial", 10, "bold"),
            bg='#27AE60',
            fg='black',
            command=self.submit_form,
            padx=20,
            pady=5
        ).pack(side='left', padx=(0, 10))
        
        tk.Button(
            button_frame,
            text="🧹 Limpiar",
            font=("Arial", 10),
            bg='#E67E22',
            fg='black',
            command=self.clear_form,
            padx=20,
            pady=5
        ).pack(side='left', padx=(0, 10))
        
        tk.Button(
            button_frame,
            text="❌ Cancelar",
            font=("Arial", 10),
            bg='#E74C3C',
            fg='black',
            padx=20,
            pady=5
        ).pack(side='left')
    
    def create_grid_calculator(self, parent):
        """Crea una calculadora usando grid"""
        calc_frame = tk.Frame(parent, bg='#2D2D30')
        calc_frame.pack(expand=True)
        
        # Display
        self.calc_var = tk.StringVar(value="0")
        display = tk.Entry(
            calc_frame,
            textvariable=self.calc_var,
            font=("Arial", 16, "bold"),
            bg='#1C1C1C',
            fg='#00FF00',
            justify='right',
            state='readonly',
            width=20
        )
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='ew')
        
        # Botones
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        colors = {
            'C': '#FF6B6B', '±': '#4ECDC4', '%': '#4ECDC4', '÷': '#F39C12',
            '×': '#F39C12', '-': '#F39C12', '+': '#F39C12', '=': '#27AE60',
            '.': '#95A5A6'
        }
        
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text == '0':
                    # El botón 0 ocupa 2 columnas
                    btn = tk.Button(
                        calc_frame,
                        text=btn_text,
                        font=("Arial", 12, "bold"),
                        bg=colors.get(btn_text, '#34495E'),
                        fg='black',
                        width=5,
                        height=2,
                        command=lambda t=btn_text: self.calc_button_click(t)
                    )
                    btn.grid(row=i+1, column=j, columnspan=2, padx=2, pady=2, sticky='ew')
                elif btn_text == '=':
                    btn = tk.Button(
                        calc_frame,
                        text=btn_text,
                        font=("Arial", 12, "bold"),
                        bg=colors.get(btn_text, '#34495E'),
                        fg='black',
                        width=5,
                        height=2,
                        command=lambda t=btn_text: self.calc_button_click(t)
                    )
                    btn.grid(row=i+1, column=j+1, padx=2, pady=2, sticky='ew')
                else:
                    btn = tk.Button(
                        calc_frame,
                        text=btn_text,
                        font=("Arial", 12, "bold"),
                        bg=colors.get(btn_text, '#34495E'),
                        fg='black',
                        width=5,
                        height=2,
                        command=lambda t=btn_text: self.calc_button_click(t)
                    )
                    btn.grid(row=i+1, column=j, padx=2, pady=2, sticky='ew')
    
    # ====================================================================
    # MÉTODOS AUXILIARES PARA PLACE
    # ====================================================================
    
    def place_random_widget(self, parent):
        """Coloca un widget en posición aleatoria usando place"""
        colors = ['#E74C3C', '#3498DB', '#2ECC71', '#F39C12', '#9B59B6', '#1ABC9C']
        color = random.choice(colors)
        
        # Posición aleatoria
        x = random.randint(10, 300)
        y = random.randint(10, 150)
        
        widget_count = len(parent.winfo_children()) + 1
        
        label = tk.Label(
            parent,
            text=f"📍\nWidget {widget_count}\n({x},{y})",
            font=("Arial", 8, "bold"),
            bg=color,
            fg='black',
            width=8,
            height=3,
            relief='raised',
            borderwidth=2
        )
        
        # Usar place con coordenadas absolutas
        label.place(x=x, y=y)
    
    def create_place_dashboard(self, parent):
        """Crea un dashboard usando place relativo"""
        # Frame para el dashboard
        dashboard = tk.Frame(parent, bg='#2C3E50')
        dashboard.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Header (usando place relativo)
        header = tk.Label(
            dashboard,
            text="📊 Dashboard con Place Relativo",
            font=("Arial", 14, "bold"),
            bg='#34495E',
            fg='#FFFFFF',
            relief='raised',
            borderwidth=2
        )
        header.place(relx=0.5, y=10, anchor='n', relwidth=0.9)
        
        # Panel superior izquierdo (25% width, 40% height)
        panel1 = tk.Frame(dashboard, bg='#E74C3C', relief='raised', borderwidth=2)
        panel1.place(relx=0.05, rely=0.15, relwidth=0.25, relheight=0.35)
        
        tk.Label(
            panel1,
            text="📈\nVentas\n$12,345",
            font=("Arial", 12, "bold"),
            bg='#E74C3C',
            fg='black'
        ).place(relx=0.5, rely=0.5, anchor='center')
        
        # Panel superior derecho (65% width, 40% height)
        panel2 = tk.Frame(dashboard, bg='#3498DB', relief='raised', borderwidth=2)
        panel2.place(relx=0.35, rely=0.15, relwidth=0.6, relheight=0.35)
        
        tk.Label(
            panel2,
            text="📊 Gráfico Principal\n(Área extendida para visualización)",
            font=("Arial", 11, "bold"),
            bg='#3498DB',
            fg='black',
            justify='center'
        ).place(relx=0.5, rely=0.5, anchor='center')
        
        # Panel inferior izquierdo (40% width, 35% height)
        panel3 = tk.Frame(dashboard, bg='#2ECC71', relief='raised', borderwidth=2)
        panel3.place(relx=0.05, rely=0.55, relwidth=0.4, relheight=0.35)
        
        tk.Label(
            panel3,
            text="👥\nUsuarios Activos\n1,234",
            font=("Arial", 11, "bold"),
            bg='#2ECC71',
            fg='black'
        ).place(relx=0.5, rely=0.5, anchor='center')
        
        # Panel inferior derecho (50% width, 35% height)
        panel4 = tk.Frame(dashboard, bg='#F39C12', relief='raised', borderwidth=2)
        panel4.place(relx=0.5, rely=0.55, relwidth=0.45, relheight=0.35)
        
        tk.Label(
            panel4,
            text="⚠️\nAlertas\n3 Pendientes",
            font=("Arial", 11, "bold"),
            bg='#F39C12',
            fg='black'
        ).place(relx=0.5, rely=0.5, anchor='center')
        
        # Botón flotante (usando place para superposición)
        floating_btn = tk.Button(
            dashboard,
            text="➕",
            font=("Arial", 16, "bold"),
            bg='#9B59B6',
            fg='black',
            width=3,
            height=1,
            relief='raised',
            borderwidth=3,
            command=lambda: messagebox.showinfo("Flotante", "¡Botón flotante con place!")
        )
        floating_btn.place(relx=0.9, rely=0.9, anchor='center')
    
    def create_real_app_example(self, parent):
        """Crea ejemplo de aplicación real combinando todos los managers"""
        # Frame principal que usará pack
        app_container = tk.Frame(parent, bg='#FFFFFF')
        app_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # ===== HEADER (PACK) =====
        header_frame = tk.Frame(app_container, bg='#2C3E50', height=50)
        header_frame.pack(side='top', fill='x')
        header_frame.pack_propagate(False)
        
        # Logo y título (pack dentro del header)
        tk.Label(
            header_frame,
            text="🏢 MiApp Pro",
            font=("Arial", 14, "bold"),
            bg='#2C3E50',
            fg='#FFFFFF'
        ).pack(side='left', padx=20, pady=10)
        
        # Botones del header (pack)
        header_buttons = tk.Frame(header_frame, bg='#2C3E50')
        header_buttons.pack(side='right', padx=20, pady=10)
        
        for text in ['👤 Perfil', '⚙️ Config', '🚪 Salir']:
            tk.Button(
                header_buttons,
                text=text,
                font=("Arial", 9),
                bg='#34495E',
                fg='#000',
                relief='flat',
                padx=10
            ).pack(side='left', padx=2)
        
        # ===== MAIN CONTAINER (PACK) =====
        main_container = tk.Frame(app_container, bg='#ECF0F1')
        main_container.pack(fill='both', expand=True)
        
        # ===== SIDEBAR (PACK) =====
        sidebar = tk.Frame(main_container, bg='#BDC3C7', width=200)
        sidebar.pack(side='left', fill='y')
        sidebar.pack_propagate(False)
        
        tk.Label(
            sidebar,
            text="📂 Navegación",
            font=("Arial", 11, "bold"),
            bg='#BDC3C7',
            fg='#2C3E50',
            pady=15
        ).pack(fill='x')
        
        nav_items = ['📊 Dashboard', '📈 Reportes', '👥 Usuarios', '🗂️ Archivos', '💼 Proyectos']
        for item in nav_items:
            btn = tk.Button(
                sidebar,
                text=item,
                font=("Arial", 10),
                bg='#95A5A6',
                fg='#2C3E50',
                relief='flat',
                anchor='w',
                padx=20,
                pady=5
            )
            btn.pack(fill='x', padx=10, pady=1)
        
        # ===== CONTENT AREA (GRID dentro de un Frame con pack) =====
        content_frame = tk.Frame(main_container, bg='#FFFFFF')
        content_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Título del contenido
        tk.Label(
            content_frame,
            text="📋 Formulario de Proyecto (Grid Layout)",
            font=("Arial", 12, "bold"),
            bg='#FFFFFF',
            fg='#2C3E50'
        ).grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='w')
        
        # Configurar grid
        content_frame.grid_columnconfigure(1, weight=1)
        
        # Campos del formulario usando grid
        form_fields = [
            "🏷️ Nombre del Proyecto:",
            "📝 Descripción:",
            "📅 Fecha de Inicio:",
            "👥 Responsable:",
            "💰 Presupuesto:"
        ]
        
        for i, field in enumerate(form_fields):
            # Etiqueta
            tk.Label(
                content_frame,
                text=field,
                font=("Arial", 10, "bold"),
                bg='#FFFFFF',
                fg='#2C3E50',
                anchor='w'
            ).grid(row=i+1, column=0, sticky='w', padx=(0, 15), pady=8)
            
            # Campo de entrada
            if "Descripción" in field:
                widget = tk.Text(
                    content_frame,
                    height=3,
                    font=("Arial", 10),
                    bg='#F8F9FA',
                    relief='solid',
                    borderwidth=1
                )
            else:
                widget = tk.Entry(
                    content_frame,
                    font=("Arial", 10),
                    bg='#F8F9FA',
                    relief='solid',
                    borderwidth=1,
                    width=30
                )
            widget.grid(row=i+1, column=1, sticky='ew', pady=8)
        
        # Botones del formulario (grid)
        button_row = len(form_fields) + 2
        
        tk.Button(
            content_frame,
            text="💾 Guardar Proyecto",
            font=("Arial", 10, "bold"),
            bg='#27AE60',
            fg='black',
            padx=20,
            pady=8
        ).grid(row=button_row, column=0, sticky='w', pady=20)
        
        tk.Button(
            content_frame,
            text="❌ Cancelar",
            font=("Arial", 10),
            bg='#E74C3C',
            fg='black',
            padx=20,
            pady=8
        ).grid(row=button_row, column=1, sticky='w', padx=(20, 0), pady=20)
        
        # ===== NOTIFICATION OVERLAY (PLACE) =====
        # Simular notificación flotante usando place
        notification = tk.Label(
            content_frame,
            text="🔔 Nueva notificación",
            font=("Arial", 9),
            bg='#3498DB',
            fg='black',
            padx=10,
            pady=5,
            relief='raised',
            borderwidth=2
        )
        # Colocar en esquina superior derecha de manera relativa
        notification.place(relx=1.0, rely=0.0, anchor='ne', x=-10, y=10)
        
        # ===== STATUS BAR (PACK) =====
        status_bar = tk.Frame(app_container, bg='#95A5A6', height=25)
        status_bar.pack(side='bottom', fill='x')
        status_bar.pack_propagate(False)
        
        tk.Label(
            status_bar,
            text="💡 Listo | Pack+Grid+Place | Aplicación ejemplo",
            font=("Arial", 9),
            bg='#95A5A6',
            fg='#2C3E50',
            anchor='w'
        ).pack(side='left', padx=10, fill='x', expand=True)
        
        tk.Label(
            status_bar,
            text="🕒 12:34:56",
            font=("Arial", 9),
            bg='#95A5A6',
            fg='#2C3E50'
        ).pack(side='right', padx=10)
    
    # ====================================================================
    # MÉTODOS AUXILIARES GENERALES
    # ====================================================================
    
    def clear_frame(self, frame):
        """Limpia todos los widgets de un frame"""
        for widget in frame.winfo_children():
            widget.destroy()
            
    def submit_form(self):
        """Maneja el envío del formulario"""
        data = {}
        for label, widget in self.form_widgets.items():
            if isinstance(widget, tk.Text):
                data[label] = widget.get(1.0, tk.END).strip()
            else:
                data[label] = widget.get()
                
        messagebox.showinfo(
            "Formulario Enviado",
            f"Datos capturados con Grid:\n\n" + 
            "\n".join([f"{k} {v}" for k, v in data.items()])
        )
        
    def clear_form(self):
        """Limpia todos los campos del formulario"""
        for widget in self.form_widgets.values():
            if isinstance(widget, tk.Text):
                widget.delete(1.0, tk.END)
            else:
                widget.delete(0, tk.END)
                
    def calc_button_click(self, value):
        """Maneja clicks de la calculadora"""
        current = self.calc_var.get()
        
        if value == 'C':
            self.calc_var.set('0')
        elif value == '=':
            try:
                # Reemplazar símbolos por operadores Python
                expression = current.replace('×', '*').replace('÷', '/')
                result = str(eval(expression))
                self.calc_var.set(result)
            except:
                self.calc_var.set('Error')
        else:
            if current == '0' and value not in ['±', '%', '.']:
                self.calc_var.set(value)
            else:
                self.calc_var.set(current + value)

def main():
    """
    Función principal para ejecutar la demostración
    """
    root = tk.Tk()
    app = GeometryManagerDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
