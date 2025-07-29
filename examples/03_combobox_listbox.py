#!/usr/bin/env python3
"""
Demostración de ttk.Combobox y tkinter.Listbox
=============================================

Este script demuestra el uso de:
- ttk.Combobox (Caja combo moderna con estilos TTK)
- tkinter.Listbox (Lista de selección con múltiples opciones)
- Diferentes modos de selección en Listbox
- Eventos y manejo de selecciones
- Integración entre widgets

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox

class ComboListboxDemo:
    """
    Clase que demuestra el uso de Combobox y Listbox
    """
    
    def __init__(self, root):
        """
        Inicializa la ventana de demostración
        
        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.setup_window()
        self.init_variables()
        self.init_data()
        self.create_widgets()
        
    def setup_window(self):
        """
        Configura las propiedades de la ventana
        """
        self.root.title("Demostración: ttk.Combobox y tkinter.Listbox")
        self.root.geometry("800x700")
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
        Inicializa variables de control
        """
        # Variables para Combobox
        self.country_var = tk.StringVar()
        self.city_var = tk.StringVar()
        self.course_var = tk.StringVar()
        self.editable_var = tk.StringVar()
        
        # Listas para almacenar selecciones de Listbox
        self.selected_skills = []
        self.selected_languages = []
        self.cart_items = []
        
    def init_data(self):
        """
        Inicializa los datos para los widgets
        """
        # Datos para Combobox
        self.countries_cities = {
            "Argentina": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata"],
            "Chile": ["Santiago", "Valparaíso", "Concepción", "Antofagasta", "Temuco"],
            "Colombia": ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"],
            "México": ["Ciudad de México", "Guadalajara", "Monterrey", "Puebla", "Tijuana"],
            "España": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza"],
            "Perú": ["Lima", "Arequipa", "Trujillo", "Chiclayo", "Huancayo"]
        }
        
        self.courses = [
            "Programación I - Fundamentos",
            "Programación II - Estructuras de Datos",
            "Base de Datos - Diseño y Consultas",
            "Desarrollo Web - Frontend",
            "Desarrollo Web - Backend",
            "Algoritmos y Complejidad",
            "Ingeniería de Software",
            "Sistemas Operativos",
            "Redes de Computadoras",
            "Inteligencia Artificial",
            "Machine Learning",
            "Ciberseguridad",
            "Desarrollo Móvil",
            "DevOps y Cloud Computing"
        ]
        
        # Datos para Listbox
        self.programming_skills = [
            "Python - Programación General",
            "JavaScript - Frontend/Backend",
            "Java - Desarrollo Empresarial",
            "C++ - Programación de Sistemas",
            "C# - Desarrollo .NET",
            "HTML/CSS - Maquetación Web",
            "React - Framework Frontend",
            "Angular - Framework Frontend",
            "Vue.js - Framework Frontend",
            "Node.js - Backend JavaScript",
            "Django - Framework Python",
            "Flask - Microframework Python",
            "Spring Boot - Framework Java",
            "Laravel - Framework PHP",
            "Ruby on Rails - Framework Ruby",
            "SQL - Base de Datos",
            "MongoDB - Base de Datos NoSQL",
            "Git - Control de Versiones",
            "Docker - Contenedores",
            "Kubernetes - Orquestación"
        ]
        
        self.languages = [
            "🇪🇸 Español (Nativo)",
            "🇺🇸 Inglés (English)",
            "🇫🇷 Francés (Français)",
            "🇩🇪 Alemán (Deutsch)",
            "🇮🇹 Italiano (Italiano)",
            "🇵🇹 Portugués (Português)",
            "🇯🇵 Japonés (日本語)",
            "🇰🇷 Coreano (한국어)",
            "🇨🇳 Chino (中文)",
            "🇷🇺 Ruso (Русский)"
        ]
        
        self.products = [
            {"name": "💻 Laptop Gaming", "price": 1200},
            {"name": "🖱️ Mouse Inalámbrico", "price": 25},
            {"name": "⌨️ Teclado Mecánico", "price": 80},
            {"name": "🖥️ Monitor 4K", "price": 300},
            {"name": "🎧 Auriculares Premium", "price": 150},
            {"name": "📱 Smartphone", "price": 600},
            {"name": "⌚ Smartwatch", "price": 200},
            {"name": "📷 Cámara Digital", "price": 450},
            {"name": "🔊 Altavoces Bluetooth", "price": 75},
            {"name": "💾 Disco Duro Externo", "price": 90}
        ]
        
    def create_widgets(self):
        """
        Crea todos los widgets de la interfaz
        """
        # Frame principal con scroll
        main_frame = tk.Frame(
            self.root,
            bg='#1E1E1E',
            padx=20,
            pady=20
        )
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Crear secciones
        self.create_combobox_section(main_frame)
        self.create_listbox_section(main_frame)
        self.create_integration_section(main_frame)
        self.create_control_buttons(main_frame)
        
    def create_combobox_section(self, parent):
        """
        Crea la sección de demostración de ttk.Combobox
        """
        # Frame para combobox
        combo_frame = tk.LabelFrame(
            parent,
            text="🔽 Demostración de ttk.Combobox (Cajas Desplegables)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        combo_frame.pack(fill='x', pady=(0, 15))
        
        # Configurar grid
        combo_frame.grid_columnconfigure(1, weight=1)
        
        # Título explicativo
        tk.Label(
            combo_frame,
            text="Los Combobox combinan un campo de texto con una lista desplegable:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "italic")
        ).grid(row=0, column=0, columnspan=2, sticky='w', pady=(0, 15))
        
        # Combobox 1: País (readonly)
        tk.Label(
            combo_frame,
            text="🌍 País:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).grid(row=1, column=0, sticky='w', pady=5, padx=(0, 10))
        
        self.country_combo = ttk.Combobox(
            combo_frame,
            textvariable=self.country_var,
            values=list(self.countries_cities.keys()),
            state="readonly",  # Solo lectura - fuerza selección de lista
            width=25,
            font=("Arial", 11)
        )
        self.country_combo.grid(row=1, column=1, sticky='ew', pady=5)
        self.country_combo.bind('<<ComboboxSelected>>', self.on_country_selected)
        
        # Combobox 2: Ciudad (dependiente del país)
        tk.Label(
            combo_frame,
            text="🏙️ Ciudad:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).grid(row=2, column=0, sticky='w', pady=5, padx=(0, 10))
        
        self.city_combo = ttk.Combobox(
            combo_frame,
            textvariable=self.city_var,
            state="readonly",
            width=25,
            font=("Arial", 11)
        )
        self.city_combo.grid(row=2, column=1, sticky='ew', pady=5)
        self.city_combo.bind('<<ComboboxSelected>>', self.on_city_selected)
        
        # Combobox 3: Curso con búsqueda
        tk.Label(
            combo_frame,
            text="📚 Curso:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).grid(row=3, column=0, sticky='w', pady=5, padx=(0, 10))
        
        self.course_combo = ttk.Combobox(
            combo_frame,
            textvariable=self.course_var,
            values=self.courses,
            state="readonly",
            width=25,
            font=("Arial", 11)
        )
        self.course_combo.grid(row=3, column=1, sticky='ew', pady=5)
        self.course_combo.bind('<<ComboboxSelected>>', self.on_course_selected)
        
        # Combobox 4: Editable (permite escribir)
        tk.Label(
            combo_frame,
            text="✏️ Editable:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).grid(row=4, column=0, sticky='w', pady=5, padx=(0, 10))
        
        self.editable_combo = ttk.Combobox(
            combo_frame,
            textvariable=self.editable_var,
            values=["Opción 1", "Opción 2", "Opción 3", "Valor personalizado"],
            state="normal",  # Editable - permite escribir valores personalizados
            width=25,
            font=("Arial", 11)
        )
        self.editable_combo.grid(row=4, column=1, sticky='ew', pady=5)
        self.editable_combo.bind('<KeyRelease>', self.on_editable_change)
        
        # Información sobre estados
        info_text = """💡 Tipos de Combobox:
• readonly: Solo permite selección de la lista
• normal: Permite escribir y seleccionar
• disabled: No permite interacción"""
        
        tk.Label(
            combo_frame,
            text=info_text,
            bg='#F8F9FA',
            fg='#000',
            font=("Arial", 9),
            justify='left',
            relief='sunken',
            borderwidth=1,
            padx=10,
            pady=5
        ).grid(row=5, column=0, columnspan=2, sticky='ew', pady=(15, 0))
        
    def create_listbox_section(self, parent):
        """
        Crea la sección de demostración de tkinter.Listbox
        """
        # Frame para listbox
        list_frame = tk.LabelFrame(
            parent,
            text="📋 Demostración de tkinter.Listbox (Listas de Selección)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        list_frame.pack(fill='x', pady=(0, 15))
        
        # Título explicativo
        tk.Label(
            list_frame,
            text="Los Listbox muestran múltiples elementos y permiten diferentes tipos de selección:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "italic")
        ).pack(anchor='w', pady=(0, 10))
        
        # Container horizontal para múltiples listbox
        listbox_container = tk.Frame(list_frame, bg='#2D2D30')
        listbox_container.pack(fill='both', expand=True)
        
        # Listbox 1: Selección única
        self.create_single_selection_listbox(listbox_container)
        
        # Listbox 2: Selección múltiple
        self.create_multiple_selection_listbox(listbox_container)
        
        # Listbox 3: Selección extendida (con Ctrl/Shift)
        self.create_extended_selection_listbox(listbox_container)
        
    def create_single_selection_listbox(self, parent):
        """
        Crea un Listbox con selección única
        """
        # Frame para single selection
        single_frame = tk.Frame(parent, bg='#2D2D30')
        single_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        tk.Label(
            single_frame,
            text="🔘 Selección Única (SINGLE)",
            bg='#2D2D30',
            fg='#E74C3C',
            font=("Arial", 10, "bold")
        ).pack(anchor='w', pady=(0, 5))
        
        # Frame para listbox con scrollbar
        list_frame = tk.Frame(single_frame, bg='#2D2D30')
        list_frame.pack(fill='both', expand=True)
        
        self.single_listbox = tk.Listbox(
            list_frame,
            selectmode=tk.SINGLE,  # Solo una selección
            height=8,
            font=("Arial", 9),
            bg='#3C3C3C',
            fg='#FFFFFF',
            selectbackground='#0078D4',
            selectforeground='#FFFFFF',
            borderwidth=2,
            relief='sunken'
        )
        
        # Agregar elementos
        for lang in self.languages:
            self.single_listbox.insert(tk.END, lang)
            
        # Scrollbar
        single_scrollbar = tk.Scrollbar(
            list_frame,
            orient=tk.VERTICAL,
            command=self.single_listbox.yview
        )
        self.single_listbox.configure(yscrollcommand=single_scrollbar.set)
        
        # Posicionar
        self.single_listbox.pack(side='left', fill='both', expand=True)
        single_scrollbar.pack(side='right', fill='y')
        
        # Bind event
        self.single_listbox.bind('<<ListboxSelect>>', self.on_single_select)
        
    def create_multiple_selection_listbox(self, parent):
        """
        Crea un Listbox con selección múltiple
        """
        # Frame para multiple selection
        multiple_frame = tk.Frame(parent, bg='#2D2D30')
        multiple_frame.pack(side='left', fill='both', expand=True, padx=5)
        
        tk.Label(
            multiple_frame,
            text="☑️ Selección Múltiple (MULTIPLE)",
            bg='#2D2D30',
            fg='#27AE60',
            font=("Arial", 10, "bold")
        ).pack(anchor='w', pady=(0, 5))
        
        # Frame para listbox con scrollbar
        list_frame = tk.Frame(multiple_frame, bg='#2D2D30')
        list_frame.pack(fill='both', expand=True)
        
        self.multiple_listbox = tk.Listbox(
            list_frame,
            selectmode=tk.MULTIPLE,  # Selección múltiple independiente
            height=8,
            font=("Arial", 9),
            bg='#3C3C3C',
            fg='#FFFFFF',
            selectbackground='#4CAF50',
            selectforeground='#FFFFFF',
            borderwidth=2,
            relief='sunken'
        )
        
        # Agregar elementos
        for skill in self.programming_skills:
            self.multiple_listbox.insert(tk.END, skill)
            
        # Scrollbar
        multiple_scrollbar = tk.Scrollbar(
            list_frame,
            orient=tk.VERTICAL,
            command=self.multiple_listbox.yview
        )
        self.multiple_listbox.configure(yscrollcommand=multiple_scrollbar.set)
        
        # Posicionar
        self.multiple_listbox.pack(side='left', fill='both', expand=True)
        multiple_scrollbar.pack(side='right', fill='y')
        
        # Bind event
        self.multiple_listbox.bind('<<ListboxSelect>>', self.on_multiple_select)
        
    def create_extended_selection_listbox(self, parent):
        """
        Crea un Listbox con selección extendida
        """
        # Frame para extended selection
        extended_frame = tk.Frame(parent, bg='#2D2D30')
        extended_frame.pack(side='left', fill='both', expand=True, padx=(10, 0))
        
        tk.Label(
            extended_frame,
            text="🔗 Selección Extendida (EXTENDED)",
            bg='#2D2D30',
            fg='#3498DB',
            font=("Arial", 10, "bold")
        ).pack(anchor='w', pady=(0, 5))
        
        tk.Label(
            extended_frame,
            text="Ctrl+Click | Shift+Click",
            bg='#2D2D30',
            fg='#7F8C8D',
            font=("Arial", 8, "italic")
        ).pack(anchor='w')
        
        # Frame para listbox con scrollbar
        list_frame = tk.Frame(extended_frame, bg='#2D2D30')
        list_frame.pack(fill='both', expand=True)
        
        self.extended_listbox = tk.Listbox(
            list_frame,
            selectmode=tk.EXTENDED,  # Selección con Ctrl y Shift
            height=8,
            font=("Arial", 9),
            bg='#3C3C3C',
            fg='#FFFFFF',
            selectbackground='#0078D4',
            selectforeground='#FFFFFF',
            borderwidth=2,
            relief='sunken'
        )
        
        # Agregar elementos (productos para carrito)
        for product in self.products:
            display_text = f"{product['name']} - ${product['price']}"
            self.extended_listbox.insert(tk.END, display_text)
            
        # Scrollbar
        extended_scrollbar = tk.Scrollbar(
            list_frame,
            orient=tk.VERTICAL,
            command=self.extended_listbox.yview
        )
        self.extended_listbox.configure(yscrollcommand=extended_scrollbar.set)
        
        # Posicionar
        self.extended_listbox.pack(side='left', fill='both', expand=True)
        extended_scrollbar.pack(side='right', fill='y')
        
        # Bind event
        self.extended_listbox.bind('<<ListboxSelect>>', self.on_extended_select)
        
    def create_integration_section(self, parent):
        """
        Crea sección que demuestra integración entre widgets
        """
        # Frame para integración
        integration_frame = tk.LabelFrame(
            parent,
            text="🔗 Integración: Combobox filtra Listbox",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        integration_frame.pack(fill='x', pady=(0, 15))
        
        # Container horizontal
        integration_container = tk.Frame(integration_frame, bg='#2D2D30')
        integration_container.pack(fill='x')
        
        # Combobox para filtrar
        filter_frame = tk.Frame(integration_container, bg='#2D2D30')
        filter_frame.pack(side='left', fill='both', expand=True, padx=(0, 20))
        
        tk.Label(
            filter_frame,
            text="🔍 Filtrar por categoría:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).pack(anchor='w', pady=(0, 5))
        
        categories = ["Todos", "Programación", "Frameworks", "Bases de Datos", "DevOps", "Frontend"]
        self.filter_var = tk.StringVar(value="Todos")
        
        self.filter_combo = ttk.Combobox(
            filter_frame,
            textvariable=self.filter_var,
            values=categories,
            state="readonly",
            width=20,
            font=("Arial", 11)
        )
        self.filter_combo.pack(fill='x')
        self.filter_combo.bind('<<ComboboxSelected>>', self.filter_skills)
        
        # Listbox filtrado
        filtered_frame = tk.Frame(integration_container, bg='#2D2D30')
        filtered_frame.pack(side='right', fill='both', expand=True)
        
        tk.Label(
            filtered_frame,
            text="📋 Lista filtrada:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).pack(anchor='w', pady=(0, 5))
        
        list_container = tk.Frame(filtered_frame, bg='#2D2D30')
        list_container.pack(fill='both', expand=True)
        
        self.filtered_listbox = tk.Listbox(
            list_container,
            selectmode=tk.MULTIPLE,
            height=6,
            font=("Arial", 9),
            bg='#3C3C3C',
            fg='#FFFFFF',
            selectbackground='#9C27B0',
            selectforeground='#FFFFFF',
            borderwidth=2,
            relief='sunken'
        )
        
        # Scrollbar para listbox filtrado
        filtered_scrollbar = tk.Scrollbar(
            list_container,
            orient=tk.VERTICAL,
            command=self.filtered_listbox.yview
        )
        self.filtered_listbox.configure(yscrollcommand=filtered_scrollbar.set)
        
        # Posicionar
        self.filtered_listbox.pack(side='left', fill='both', expand=True)
        filtered_scrollbar.pack(side='right', fill='y')
        
        # Inicializar con todos los elementos
        self.update_filtered_list("Todos")
        
    def create_control_buttons(self, parent):
        """
        Crea botones de control
        """
        # Frame para botones
        buttons_frame = tk.Frame(parent, bg='#F8F9FA')
        buttons_frame.pack(fill='x', pady=(10, 0))
        
        # Centrar botones
        button_container = tk.Frame(buttons_frame, bg='#F8F9FA')
        button_container.pack()
        
        # Botón para mostrar selecciones
        show_btn = tk.Button(
            button_container,
            text="📋 Mostrar Todas las Selecciones",
            font=("Arial", 11, "bold"),
            bg='#3498DB',
            fg='#2D2D30',
            activebackground='#2980B9',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.show_all_selections
        )
        show_btn.pack(side='left', padx=5)
        
        # Botón para limpiar selecciones
        clear_btn = tk.Button(
            button_container,
            text="🧹 Limpiar Selecciones",
            font=("Arial", 11, "bold"),
            bg='#E74C3C',
            fg='#2D2D30',
            activebackground='#C0392B',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.clear_all_selections
        )
        clear_btn.pack(side='left', padx=5)
        
        # Botón para seleccionar aleatorio
        random_btn = tk.Button(
            button_container,
            text="🎲 Selección Aleatoria",
            font=("Arial", 11, "bold"),
            bg='#27AE60',
            fg='#2D2D30',
            activebackground='#229954',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.random_selection
        )
        random_btn.pack(side='left', padx=5)
        
    # ====================================================================
    # MÉTODOS DE MANEJO DE EVENTOS
    # ====================================================================
    
    def on_country_selected(self, event):
        """
        Maneja la selección de país y actualiza ciudades
        """
        country = self.country_var.get()
        if country:
            cities = self.countries_cities.get(country, [])
            self.city_combo['values'] = cities
            self.city_var.set("")  # Limpiar selección anterior
            print(f"País seleccionado: {country}")
            
    def on_city_selected(self, event):
        """
        Maneja la selección de ciudad
        """
        city = self.city_var.get()
        country = self.country_var.get()
        if city and country:
            print(f"Ubicación completa: {city}, {country}")
            
    def on_course_selected(self, event):
        """
        Maneja la selección de curso
        """
        course = self.course_var.get()
        if course:
            print(f"Curso seleccionado: {course}")
            
    def on_editable_change(self, event):
        """
        Maneja cambios en el combobox editable
        """
        value = self.editable_var.get()
        print(f"Valor editable: {value}")
        
    def on_single_select(self, event):
        """
        Maneja selección única en listbox
        """
        selection = self.single_listbox.curselection()
        if selection:
            item = self.single_listbox.get(selection[0])
            print(f"Idioma seleccionado: {item}")
            
    def on_multiple_select(self, event):
        """
        Maneja selección múltiple en listbox
        """
        selections = self.multiple_listbox.curselection()
        self.selected_skills = []
        for i in selections:
            skill = self.multiple_listbox.get(i)
            self.selected_skills.append(skill)
        print(f"Habilidades seleccionadas: {len(self.selected_skills)}")
        
    def on_extended_select(self, event):
        """
        Maneja selección extendida en listbox
        """
        selections = self.extended_listbox.curselection()
        total_price = 0
        items = []
        
        for i in selections:
            item_text = self.extended_listbox.get(i)
            items.append(item_text)
            # Extraer precio del texto
            price_str = item_text.split('$')[1]
            total_price += int(price_str)
            
        print(f"Carrito: {len(items)} items, Total: ${total_price}")
        
    def filter_skills(self, event):
        """
        Filtra la lista de habilidades según la categoría
        """
        category = self.filter_var.get()
        self.update_filtered_list(category)
        
    def update_filtered_list(self, category):
        """
        Actualiza la lista filtrada según la categoría
        """
        # Limpiar lista
        self.filtered_listbox.delete(0, tk.END)
        
        # Filtros por categoría
        if category == "Todos":
            items = self.programming_skills
        elif category == "Programación":
            items = [s for s in self.programming_skills if any(lang in s for lang in ["Python", "JavaScript", "Java", "C++", "C#"])]
        elif category == "Frameworks":
            items = [s for s in self.programming_skills if any(fw in s for fw in ["React", "Angular", "Vue", "Django", "Flask", "Spring", "Laravel"])]
        elif category == "Bases de Datos":
            items = [s for s in self.programming_skills if any(db in s for db in ["SQL", "MongoDB"])]
        elif category == "DevOps":
            items = [s for s in self.programming_skills if any(dev in s for dev in ["Git", "Docker", "Kubernetes"])]
        elif category == "Frontend":
            items = [s for s in self.programming_skills if any(fe in s for fe in ["HTML", "CSS", "React", "Angular", "Vue"])]
        else:
            items = []
            
        # Agregar items filtrados
        for item in items:
            self.filtered_listbox.insert(tk.END, item)
            
    def show_all_selections(self):
        """
        Muestra todas las selecciones actuales
        """
        # Combobox values
        combo_info = f"""Combobox Selections:
🌍 País: {self.country_var.get() or 'No seleccionado'}
🏙️ Ciudad: {self.city_var.get() or 'No seleccionado'}
📚 Curso: {self.course_var.get() or 'No seleccionado'}
✏️ Editable: {self.editable_var.get() or 'Vacío'}"""

        # Listbox selections
        single_sel = self.single_listbox.curselection()
        single_item = self.single_listbox.get(single_sel[0]) if single_sel else "Ninguno"
        
        multiple_sel = self.multiple_listbox.curselection()
        multiple_items = [self.multiple_listbox.get(i) for i in multiple_sel]
        
        extended_sel = self.extended_listbox.curselection()
        extended_items = [self.extended_listbox.get(i) for i in extended_sel]
        total_price = sum(int(item.split('$')[1]) for item in extended_items)
        
        filtered_sel = self.filtered_listbox.curselection()
        filtered_items = [self.filtered_listbox.get(i) for i in filtered_sel]
        
        listbox_info = f"""Listbox Selections:
🔘 Idioma (single): {single_item}
☑️ Habilidades ({len(multiple_items)}): {', '.join(multiple_items[:3])}{'...' if len(multiple_items) > 3 else ''}
🛒 Carrito ({len(extended_items)} items): ${total_price}
🔍 Filtradas ({len(filtered_items)}): {', '.join(filtered_items[:2])}{'...' if len(filtered_items) > 2 else ''}"""

        full_message = f"{combo_info}\n\n{listbox_info}"
        messagebox.showinfo("Todas las Selecciones", full_message)
        
    def clear_all_selections(self):
        """
        Limpia todas las selecciones
        """
        # Limpiar combobox
        self.country_var.set("")
        self.city_var.set("")
        self.course_var.set("")
        self.editable_var.set("")
        self.filter_var.set("Todos")
        
        # Limpiar listbox selections
        self.single_listbox.selection_clear(0, tk.END)
        self.multiple_listbox.selection_clear(0, tk.END)
        self.extended_listbox.selection_clear(0, tk.END)
        self.filtered_listbox.selection_clear(0, tk.END)
        
        # Restaurar ciudad combo
        self.city_combo['values'] = []
        
        # Restaurar lista filtrada
        self.update_filtered_list("Todos")
        
        messagebox.showinfo("Limpiado", "Todas las selecciones han sido limpiadas")
        
    def random_selection(self):
        """
        Hace selecciones aleatorias en todos los widgets
        """
        import random
        
        # Selección aleatoria en combobox
        countries = list(self.countries_cities.keys())
        random_country = random.choice(countries)
        self.country_var.set(random_country)
        
        # Actualizar ciudades y seleccionar una aleatoria
        cities = self.countries_cities[random_country]
        self.city_combo['values'] = cities
        self.city_var.set(random.choice(cities))
        
        # Curso aleatorio
        self.course_var.set(random.choice(self.courses))
        
        # Selecciones aleatorias en listbox
        # Single selection
        self.single_listbox.selection_clear(0, tk.END)
        random_lang = random.randint(0, len(self.languages) - 1)
        self.single_listbox.selection_set(random_lang)
        
        # Multiple selection (2-4 items)
        self.multiple_listbox.selection_clear(0, tk.END)
        num_skills = random.randint(2, 4)
        random_skills = random.sample(range(len(self.programming_skills)), num_skills)
        for idx in random_skills:
            self.multiple_listbox.selection_set(idx)
            
        # Extended selection (1-3 items)
        self.extended_listbox.selection_clear(0, tk.END)
        num_products = random.randint(1, 3)
        random_products = random.sample(range(len(self.products)), num_products)
        for idx in random_products:
            self.extended_listbox.selection_set(idx)
            
        messagebox.showinfo("Selección Aleatoria", "Se han realizado selecciones aleatorias en todos los widgets")

def main():
    """
    Función principal para ejecutar la demostración
    """
    root = tk.Tk()
    app = ComboListboxDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
