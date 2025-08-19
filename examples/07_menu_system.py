#!/usr/bin/env python3
"""
Menús y Sistemas de Navegación en Tkinter
========================================

Este script demuestra:
1. Creación de Menús (MenuBar)
2. Agregar Campos (Comandos) al Menú
3. Agregar Código (Funciones command) a los Campos
4. Menús Pop-Up (Menús Contextuales)
5. Menús jerárquicos y submenu
6. Separadores y atajos de teclado
7. Estados de menú (habilitado/deshabilitado)

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import webbrowser

class MenuSystemDemo:
    """
    Clase que demuestra sistemas de menús en Tkinter
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
        self.create_menu_bar()
        self.create_main_interface()
        self.create_context_menus()
        
    def setup_window(self):
        """
        Configura la ventana principal
        """
        self.root.title("🍽️ Sistema de Menús en Tkinter")
        self.root.geometry("900x700")
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
        # Variables para el estado de la aplicación
        self.current_file = None
        self.is_modified = False
        self.clipboard_content = ""
        
        # Variables para configuraciones
        self.show_toolbar = tk.BooleanVar(value=True)
        self.show_status_bar = tk.BooleanVar(value=True)
        self.word_wrap = tk.BooleanVar(value=False)
        self.auto_save = tk.BooleanVar(value=False)
        
        # Variable para tema
        self.current_theme = tk.StringVar(value="Oscuro")
        
        # Contador de acciones para demostración
        self.action_counter = 0
        
    def create_menu_bar(self):
        """
        Crea la barra de menús principal
        """
        # Crear barra de menús
        menubar = tk.Menu(self.root, bg='#2D2D30', fg='#FFFFFF', tearoff=0)
        
        # === MENÚ ARCHIVO ===
        file_menu = tk.Menu(menubar, tearoff=0, bg='#2D2D30', fg='#FFFFFF')
        
        file_menu.add_command(
            label="📄 Nuevo",
            command=self.file_new,
            accelerator="Ctrl+N"
        )
        
        file_menu.add_command(
            label="📂 Abrir...",
            command=self.file_open,
            accelerator="Ctrl+O"
        )
        
        # Submenú "Abrir Reciente"
        recent_menu = tk.Menu(file_menu, tearoff=0, bg='#2D2D30', fg='#FFFFFF')
        recent_files = ["documento1.txt", "proyecto.py", "notas.md"]
        for filename in recent_files:
            recent_menu.add_command(
                label=f"📄 {filename}",
                command=lambda f=filename: self.open_recent_file(f)
            )
        recent_menu.add_separator()
        recent_menu.add_command(
            label="🧹 Limpiar historial",
            command=self.clear_recent_files
        )
        
        file_menu.add_cascade(label="🕒 Abrir Reciente", menu=recent_menu)
        
        file_menu.add_separator()
        
        file_menu.add_command(
            label="💾 Guardar",
            command=self.file_save,
            accelerator="Ctrl+S"
        )
        
        file_menu.add_command(
            label="💾 Guardar Como...",
            command=self.file_save_as,
            accelerator="Ctrl+Shift+S"
        )
        
        file_menu.add_separator()
        
        # Submenú de Exportar
        export_menu = tk.Menu(file_menu, tearoff=0, bg='#2D2D30', fg='#FFFFFF')
        export_menu.add_command(label="📄 Como PDF", command=lambda: self.export_file("pdf"))
        export_menu.add_command(label="📊 Como CSV", command=lambda: self.export_file("csv"))
        export_menu.add_command(label="🌐 Como HTML", command=lambda: self.export_file("html"))
        
        file_menu.add_cascade(label="📤 Exportar", menu=export_menu)
        
        file_menu.add_separator()
        
        file_menu.add_command(
            label="🖨️ Imprimir",
            command=self.file_print,
            accelerator="Ctrl+P"
        )
        
        file_menu.add_separator()
        
        file_menu.add_command(
            label="🚪 Salir",
            command=self.file_exit,
            accelerator="Alt+F4"
        )
        
        menubar.add_cascade(label="📁 Archivo", menu=file_menu)
        
        # === MENÚ EDITAR ===
        edit_menu = tk.Menu(menubar, tearoff=0, bg='#2D2D30', fg='#FFFFFF')
        
        edit_menu.add_command(
            label="↶ Deshacer",
            command=self.edit_undo,
            accelerator="Ctrl+Z"
        )
        
        edit_menu.add_command(
            label="↷ Rehacer",
            command=self.edit_redo,
            accelerator="Ctrl+Y"
        )
        
        edit_menu.add_separator()
        
        edit_menu.add_command(
            label="✂️ Cortar",
            command=self.edit_cut,
            accelerator="Ctrl+X"
        )
        
        edit_menu.add_command(
            label="📋 Copiar",
            command=self.edit_copy,
            accelerator="Ctrl+C"
        )
        
        edit_menu.add_command(
            label="📌 Pegar",
            command=self.edit_paste,
            accelerator="Ctrl+V"
        )
        
        edit_menu.add_separator()
        
        edit_menu.add_command(
            label="🔍 Buscar...",
            command=self.edit_find,
            accelerator="Ctrl+F"
        )
        
        edit_menu.add_command(
            label="🔄 Buscar y Reemplazar...",
            command=self.edit_replace,
            accelerator="Ctrl+H"
        )
        
        edit_menu.add_separator()
        
        edit_menu.add_command(
            label="📝 Seleccionar Todo",
            command=self.edit_select_all,
            accelerator="Ctrl+A"
        )
        
        menubar.add_cascade(label="✏️ Editar", menu=edit_menu)
        
        # === MENÚ VER ===
        view_menu = tk.Menu(menubar, tearoff=0, bg='#2D2D30', fg='#FFFFFF')
        
        # Opciones con checkbutton
        view_menu.add_checkbutton(
            label="🔧 Mostrar Barra de Herramientas",
            variable=self.show_toolbar,
            command=self.toggle_toolbar
        )
        
        view_menu.add_checkbutton(
            label="📊 Mostrar Barra de Estado",
            variable=self.show_status_bar,
            command=self.toggle_status_bar
        )
        
        view_menu.add_separator()
        
        view_menu.add_checkbutton(
            label="📄 Ajuste de Línea",
            variable=self.word_wrap,
            command=self.toggle_word_wrap
        )
        
        view_menu.add_separator()
        
        # Submenú de Zoom
        zoom_menu = tk.Menu(view_menu, tearoff=0, bg='#2D2D30', fg='#FFFFFF')
        zoom_levels = [50, 75, 100, 125, 150, 200]
        for level in zoom_levels:
            zoom_menu.add_command(
                label=f"{level}%",
                command=lambda z=level: self.set_zoom(z)
            )
        zoom_menu.add_separator()
        zoom_menu.add_command(label="🔍➕ Acercar", command=self.zoom_in, accelerator="Ctrl++")
        zoom_menu.add_command(label="🔍➖ Alejar", command=self.zoom_out, accelerator="Ctrl+-")
        
        view_menu.add_cascade(label="🔍 Zoom", menu=zoom_menu)
        
        # Submenú de Tema
        theme_menu = tk.Menu(view_menu, tearoff=0, bg='#2D2D30', fg='#FFFFFF')
        themes = ["Claro", "Oscuro", "Azul", "Verde"]
        for theme in themes:
            theme_menu.add_radiobutton(
                label=f"🎨 {theme}",
                variable=self.current_theme,
                value=theme,
                command=lambda t=theme: self.change_theme(t)
            )
            
        view_menu.add_cascade(label="🎨 Tema", menu=theme_menu)
        
        menubar.add_cascade(label="👁️ Ver", menu=view_menu)
        
        # === MENÚ HERRAMIENTAS ===
        tools_menu = tk.Menu(menubar, tearoff=0, bg='#2D2D30', fg='#FFFFFF')
        
        tools_menu.add_command(
            label="🔤 Contador de Palabras",
            command=self.tools_word_count
        )
        
        tools_menu.add_command(
            label="📊 Estadísticas del Documento",
            command=self.tools_document_stats
        )
        
        tools_menu.add_separator()
        
        tools_menu.add_command(
            label="🔍 Validador de Sintaxis",
            command=self.tools_syntax_checker
        )
        
        tools_menu.add_command(
            label="🎨 Formateador de Código",
            command=self.tools_code_formatter
        )
        
        tools_menu.add_separator()
        
        tools_menu.add_checkbutton(
            label="💾 Guardado Automático",
            variable=self.auto_save,
            command=self.toggle_auto_save
        )
        
        tools_menu.add_command(
            label="⚙️ Preferencias...",
            command=self.tools_preferences
        )
        
        menubar.add_cascade(label="🔧 Herramientas", menu=tools_menu)
        
        # === MENÚ VENTANA ===
        window_menu = tk.Menu(menubar, tearoff=0, bg='#2D2D30', fg='#FFFFFF')
        
        window_menu.add_command(
            label="➕ Nueva Ventana",
            command=self.window_new,
            accelerator="Ctrl+Shift+N"
        )
        
        window_menu.add_separator()
        
        window_menu.add_command(
            label="📐 Organizar Verticalmente",
            command=lambda: self.arrange_windows("vertical")
        )
        
        window_menu.add_command(
            label="📐 Organizar Horizontalmente", 
            command=lambda: self.arrange_windows("horizontal")
        )
        
        window_menu.add_separator()
        
        # Lista de ventanas abiertas (simulada)
        open_windows = ["Documento1.txt", "main.py", "config.json"]
        for i, window_name in enumerate(open_windows):
            window_menu.add_command(
                label=f"{i+1}. {window_name}",
                command=lambda w=window_name: self.switch_to_window(w)
            )
            
        menubar.add_cascade(label="🪟 Ventana", menu=window_menu)
        
        # === MENÚ AYUDA ===
        help_menu = tk.Menu(menubar, tearoff=0, bg='#2D2D30', fg='#FFFFFF')
        
        help_menu.add_command(
            label="📖 Manual de Usuario",
            command=self.help_manual
        )
        
        help_menu.add_command(
            label="💡 Consejos y Trucos",
            command=self.help_tips
        )
        
        help_menu.add_separator()
        
        help_menu.add_command(
            label="🌐 Sitio Web",
            command=self.help_website
        )
        
        help_menu.add_command(
            label="📧 Soporte Técnico",
            command=self.help_support
        )
        
        help_menu.add_separator()
        
        help_menu.add_command(
            label="🔄 Buscar Actualizaciones",
            command=self.help_updates
        )
        
        help_menu.add_command(
            label="ℹ️ Acerca de...",
            command=self.help_about
        )
        
        menubar.add_cascade(label="❓ Ayuda", menu=help_menu)
        
        # Asignar la barra de menús a la ventana
        self.root.config(menu=menubar)
        
        # Guardar referencia para poder modificar después
        self.menubar = menubar
        self.edit_menu = edit_menu
        
        # Vincular atajos de teclado
        self.setup_keyboard_shortcuts()
        
    def create_main_interface(self):
        """
        Crea la interfaz principal de la aplicación
        """
        # Título principal
        title_label = tk.Label(
            self.root,
            text="🍽️ Sistema de Menús Completo en Tkinter",
            font=("Arial", 16, "bold"),
            bg='#1E1E1E',
            fg='#FFFFFF'
        )
        title_label.pack(pady=15)
        
        # Información sobre el menú
        info_frame = tk.Frame(self.root, bg='#2D2D30', relief='raised', borderwidth=2)
        info_frame.pack(fill='x', padx=10, pady=(0, 10))
        
        tk.Label(
            info_frame,
            text="💡 Explora todos los menús de la barra superior. Muchas opciones están completamente funcionales.",
            font=("Arial", 11),
            bg='#2D2D30',
            fg='#CCCCCC'
        ).pack(pady=10, padx=15)
        
        # Área de trabajo principal
        main_frame = tk.Frame(self.root, bg='#1E1E1E')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # === BARRA DE HERRAMIENTAS (opcional) ===
        self.toolbar_frame = tk.Frame(main_frame, bg='#34495E', height=40)
        if self.show_toolbar.get():
            self.toolbar_frame.pack(fill='x', pady=(0, 5))
            
        self.create_toolbar()
        
        # === ÁREA DE CONTENIDO ===
        content_frame = tk.Frame(main_frame, bg='#2D2D30')
        content_frame.pack(fill='both', expand=True)
        
        # Frame izquierdo: Texto de trabajo
        left_frame = tk.LabelFrame(
            content_frame,
            text="📝 Área de Trabajo (Clic derecho para menú contextual)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15
        )
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 5))
        
        # Área de texto principal
        self.main_text = tk.Text(
            left_frame,
            font=("Arial", 11),
            bg='#FFFFFF',
            fg='#2C3E50',
            wrap=tk.WORD if self.word_wrap.get() else tk.NONE,
            undo=True
        )
        self.main_text.pack(fill='both', expand=True)
        
        # Scrollbars para el texto
        text_scroll_y = tk.Scrollbar(left_frame, command=self.main_text.yview)
        text_scroll_x = tk.Scrollbar(left_frame, command=self.main_text.xview, orient='horizontal')
        self.main_text.configure(yscrollcommand=text_scroll_y.set, xscrollcommand=text_scroll_x.set)
        
        # Contenido inicial del texto
        initial_content = """🍽️ SISTEMA DE MENÚS EN TKINTER
=====================================

¡Bienvenido al sistema de demostración de menús!

📋 CARACTERÍSTICAS IMPLEMENTADAS:

✅ Barra de menús completa con 6 menús principales
✅ Submenús y menús anidados (jerárquicos)  
✅ Separadores visuales entre opciones
✅ Atajos de teclado (accelerators)
✅ Checkbuttons y Radiobuttons en menús
✅ Estados habilitado/deshabilitado dinámicos
✅ Menús contextuales (clic derecho)
✅ Iconos emoji para mejor UX
✅ Funcionalidades reales implementadas

🔧 PRUEBA ESTAS FUNCIONES:

• Archivo → Nuevo, Abrir, Guardar
• Editar → Cortar, Copiar, Pegar, Buscar
• Ver → Cambiar tema, zoom, mostrar/ocultar elementos
• Herramientas → Contador de palabras, estadísticas
• Ventana → Gestión de múltiples documentos
• Ayuda → Manual, soporte, acerca de

🖱️ MENÚ CONTEXTUAL:
Haz clic derecho en esta área para ver el menú contextual con opciones específicas del texto.

⌨️ ATAJOS DE TECLADO:
Muchos comandos tienen atajos de teclado que aparecen junto al nombre del menú.

📊 ESTADO DINÁMICO:
Los menús cambian según el contexto - algunas opciones se habilitan/deshabilitan automáticamente.

¡Explora todos los menús para ver la funcionalidad completa!"""

        self.main_text.insert(tk.END, initial_content)
        
        # Frame derecho: Log de acciones
        right_frame = tk.LabelFrame(
            content_frame,
            text="📊 Log de Acciones del Menú",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            width=300
        )
        right_frame.pack(side='right', fill='y', padx=(5, 0))
        right_frame.pack_propagate(False)
        
        # Área de log
        self.log_text = tk.Text(
            right_frame,
            font=("Courier", 9),
            bg='#3C3C3C',
            fg='#00FF00',
            wrap=tk.WORD,
            height=20
        )
        self.log_text.pack(fill='both', expand=True)
        
        # Scrollbar para el log
        log_scroll = tk.Scrollbar(right_frame, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=log_scroll.set)
        
        # === BARRA DE ESTADO (opcional) ===
        self.status_bar = tk.Frame(self.root, bg='#95A5A6', height=25)
        if self.show_status_bar.get():
            self.status_bar.pack(side='bottom', fill='x')
            
        self.create_status_bar()
        
        # Mensaje inicial del log
        self.log_action("🚀 Sistema de menús inicializado")
        self.log_action("💡 Explora los menús para ver todas las funciones")
        
    def create_toolbar(self):
        """
        Crea la barra de herramientas
        """
        # Limpiar toolbar existente
        for widget in self.toolbar_frame.winfo_children():
            widget.destroy()
            
        if not self.show_toolbar.get():
            return
            
        # Botones de la toolbar
        toolbar_buttons = [
            ("📄", "Nuevo", self.file_new),
            ("📂", "Abrir", self.file_open), 
            ("💾", "Guardar", self.file_save),
            ("|", "", None),  # Separador
            ("✂️", "Cortar", self.edit_cut),
            ("📋", "Copiar", self.edit_copy),
            ("📌", "Pegar", self.edit_paste),
            ("|", "", None),  # Separador
            ("🔍", "Buscar", self.edit_find),
            ("🔄", "Reemplazar", self.edit_replace),
        ]
        
        for icon, tooltip, command in toolbar_buttons:
            if icon == "|":  # Separador
                separator = tk.Frame(self.toolbar_frame, bg='#2C3E50', width=2, height=30)
                separator.pack(side='left', padx=5, pady=5)
            else:
                btn = tk.Button(
                    self.toolbar_frame,
                    text=icon,
                    font=("Arial", 12),
                    bg='#3498DB',
                    fg='white',
                    width=3,
                    height=1,
                    relief='raised',
                    borderwidth=1,
                    command=command
                )
                btn.pack(side='left', padx=1, pady=5)
                
                # Tooltip simple
                if tooltip:
                    self.create_simple_tooltip(btn, tooltip)
                    
    def create_status_bar(self):
        """
        Crea la barra de estado
        """
        # Limpiar barra de estado existente
        for widget in self.status_bar.winfo_children():
            widget.destroy()
            
        if not self.show_status_bar.get():
            return
            
        # Información de estado
        self.status_left = tk.Label(
            self.status_bar,
            text="📄 Documento sin título",
            font=("Arial", 9),
            bg='#95A5A6',
            fg='#2C3E50',
            anchor='w'
        )
        self.status_left.pack(side='left', padx=10, fill='x', expand=True)
        
        # Estado del zoom
        self.status_zoom = tk.Label(
            self.status_bar,
            text="🔍 100%",
            font=("Arial", 9),
            bg='#95A5A6',
            fg='#2C3E50'
        )
        self.status_zoom.pack(side='right', padx=5)
        
        # Tema actual
        self.status_theme = tk.Label(
            self.status_bar,
            text=f"🎨 {self.current_theme.get()}",
            font=("Arial", 9),
            bg='#95A5A6',
            fg='#2C3E50'
        )
        self.status_theme.pack(side='right', padx=5)
        
        # Hora
        import datetime
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.status_time = tk.Label(
            self.status_bar,
            text=f"🕒 {current_time}",
            font=("Arial", 9),
            bg='#95A5A6',
            fg='#2C3E50'
        )
        self.status_time.pack(side='right', padx=5)
        
    def create_context_menus(self):
        """
        Crea menús contextuales (clic derecho)
        """
        # Menú contextual para el área de texto
        self.text_context_menu = tk.Menu(self.root, tearoff=0, bg='#2D2D30', fg='#FFFFFF')
        
        self.text_context_menu.add_command(
            label="✂️ Cortar",
            command=self.edit_cut
        )
        
        self.text_context_menu.add_command(
            label="📋 Copiar", 
            command=self.edit_copy
        )
        
        self.text_context_menu.add_command(
            label="📌 Pegar",
            command=self.edit_paste
        )
        
        self.text_context_menu.add_separator()
        
        self.text_context_menu.add_command(
            label="📝 Seleccionar Todo",
            command=self.edit_select_all
        )
        
        self.text_context_menu.add_separator()
        
        # Submenú de formato
        format_menu = tk.Menu(self.text_context_menu, tearoff=0, bg='#2D2D30', fg='#FFFFFF')
        format_menu.add_command(label="🔤 MAYÚSCULAS", command=self.format_uppercase)
        format_menu.add_command(label="🔡 minúsculas", command=self.format_lowercase)
        format_menu.add_command(label="🎨 Capitalizar", command=self.format_capitalize)
        
        self.text_context_menu.add_cascade(label="📝 Formato", menu=format_menu)
        
        self.text_context_menu.add_separator()
        
        self.text_context_menu.add_command(
            label="🔍 Buscar en Google",
            command=self.search_in_google
        )
        
        # Vincular menú contextual al área de texto
        self.main_text.bind("<Button-3>", self.show_context_menu)  # Clic derecho en macOS
        self.main_text.bind("<Button-2>", self.show_context_menu)  # Clic medio alternativo
        
    def setup_keyboard_shortcuts(self):
        """
        Configura atajos de teclado
        """
        shortcuts = {
            '<Control-n>': self.file_new,
            '<Control-o>': self.file_open,
            '<Control-s>': self.file_save,
            '<Control-Shift-S>': self.file_save_as,
            '<Control-p>': self.file_print,
            '<Control-z>': self.edit_undo,
            '<Control-y>': self.edit_redo,
            '<Control-x>': self.edit_cut,
            '<Control-c>': self.edit_copy,
            '<Control-v>': self.edit_paste,
            '<Control-a>': self.edit_select_all,
            '<Control-f>': self.edit_find,
            '<Control-h>': self.edit_replace,
            '<Control-Shift-N>': self.window_new,
            '<Control-plus>': self.zoom_in,
            '<Control-minus>': self.zoom_out
        }
        
        for shortcut, command in shortcuts.items():
            self.root.bind(shortcut, lambda e, cmd=command: cmd())
            
    # ====================================================================
    # MÉTODOS DEL MENÚ ARCHIVO
    # ====================================================================
    
    def file_new(self):
        """Crear nuevo documento"""
        if self.is_modified:
            if messagebox.askyesno("Documento no guardado", 
                                 "¿Deseas guardar los cambios antes de crear un nuevo documento?"):
                self.file_save()
                
        self.main_text.delete(1.0, tk.END)
        self.main_text.insert(tk.END, "📄 Nuevo documento creado\n\n")
        self.current_file = None
        self.is_modified = False
        self.update_status("📄 Nuevo documento")
        self.log_action("📄 Nuevo documento creado")
        
    def file_open(self):
        """Abrir archivo existente"""
        filename = filedialog.askopenfilename(
            title="Abrir archivo",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Archivos Python", "*.py"),
                ("Archivos Markdown", "*.md"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.main_text.delete(1.0, tk.END)
                    self.main_text.insert(tk.END, content)
                    
                self.current_file = filename
                self.is_modified = False
                self.update_status(f"📂 {filename}")
                self.log_action(f"📂 Archivo abierto: {filename}")
                
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo abrir el archivo:\n{str(e)}")
                self.log_action(f"❌ Error abriendo archivo: {str(e)}")
                
    def file_save(self):
        """Guardar documento actual"""
        if self.current_file:
            try:
                content = self.main_text.get(1.0, tk.END)
                with open(self.current_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
                self.is_modified = False
                self.log_action(f"💾 Archivo guardado: {self.current_file}")
                messagebox.showinfo("Guardado", "Archivo guardado correctamente")
                
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")
                self.log_action(f"❌ Error guardando archivo: {str(e)}")
        else:
            self.file_save_as()
            
    def file_save_as(self):
        """Guardar documento como"""
        filename = filedialog.asksaveasfilename(
            title="Guardar como",
            defaultextension=".txt",
            filetypes=[
                ("Archivos de texto", "*.txt"),
                ("Archivos Python", "*.py"),
                ("Archivos Markdown", "*.md"),
                ("Todos los archivos", "*.*")
            ]
        )
        
        if filename:
            try:
                content = self.main_text.get(1.0, tk.END)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                    
                self.current_file = filename
                self.is_modified = False
                self.update_status(f"💾 {filename}")
                self.log_action(f"💾 Archivo guardado como: {filename}")
                messagebox.showinfo("Guardado", "Archivo guardado correctamente")
                
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")
                
    def file_print(self):
        """Imprimir documento"""
        self.log_action("🖨️ Enviando documento a la impresora...")
        messagebox.showinfo("Imprimir", "🖨️ Documento enviado a la impresora\n(Simulación)")
        
    def file_exit(self):
        """Salir de la aplicación"""
        if self.is_modified:
            if messagebox.askyesno("Documento no guardado", 
                                 "¿Deseas guardar los cambios antes de salir?"):
                self.file_save()
                
        if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir?"):
            self.root.quit()
            
    def open_recent_file(self, filename):
        """Abrir archivo reciente"""
        self.log_action(f"🕒 Abriendo archivo reciente: {filename}")
        messagebox.showinfo("Archivo Reciente", f"Abriendo: {filename}\n(Simulación)")
        
    def clear_recent_files(self):
        """Limpiar historial de archivos recientes"""
        self.log_action("🧹 Historial de archivos recientes limpiado")
        messagebox.showinfo("Historial", "Historial de archivos recientes limpiado")
        
    def export_file(self, format_type):
        """Exportar archivo en formato específico"""
        self.log_action(f"📤 Exportando archivo como {format_type.upper()}")
        messagebox.showinfo("Exportar", f"Archivo exportado como {format_type.upper()}\n(Simulación)")
    
    # ====================================================================
    # MÉTODOS DEL MENÚ EDITAR
    # ====================================================================
    
    def edit_undo(self):
        """Deshacer última acción"""
        try:
            self.main_text.edit_undo()
            self.log_action("↶ Deshacer acción")
        except:
            self.log_action("↶ No hay acciones para deshacer")
            
    def edit_redo(self):
        """Rehacer acción"""
        try:
            self.main_text.edit_redo()
            self.log_action("↷ Rehacer acción")
        except:
            self.log_action("↷ No hay acciones para rehacer")
            
    def edit_cut(self):
        """Cortar texto seleccionado"""
        try:
            self.main_text.event_generate("<<Cut>>")
            self.log_action("✂️ Texto cortado al portapapeles")
        except:
            self.log_action("✂️ No hay texto seleccionado para cortar")
            
    def edit_copy(self):
        """Copiar texto seleccionado"""
        try:
            self.main_text.event_generate("<<Copy>>")
            self.log_action("📋 Texto copiado al portapapeles")
        except:
            self.log_action("📋 No hay texto seleccionado para copiar")
            
    def edit_paste(self):
        """Pegar texto del portapapeles"""
        try:
            self.main_text.event_generate("<<Paste>>")
            self.log_action("📌 Texto pegado desde portapapeles")
        except:
            self.log_action("📌 No hay contenido en el portapapeles")
            
    def edit_select_all(self):
        """Seleccionar todo el texto"""
        self.main_text.tag_add(tk.SEL, "1.0", tk.END)
        self.main_text.mark_set(tk.INSERT, "1.0")
        self.main_text.see(tk.INSERT)
        self.log_action("📝 Todo el texto seleccionado")
        
    def edit_find(self):
        """Buscar texto"""
        search_term = simpledialog.askstring("Buscar", "Ingresa el texto a buscar:")
        if search_term:
            # Búsqueda simple
            content = self.main_text.get(1.0, tk.END)
            if search_term in content:
                self.log_action(f"🔍 Texto encontrado: '{search_term}'")
                messagebox.showinfo("Buscar", f"Texto '{search_term}' encontrado")
            else:
                self.log_action(f"🔍 Texto no encontrado: '{search_term}'")
                messagebox.showinfo("Buscar", f"Texto '{search_term}' no encontrado")
                
    def edit_replace(self):
        """Buscar y reemplazar texto"""
        find_text = simpledialog.askstring("Buscar y Reemplazar", "Texto a buscar:")
        if find_text:
            replace_text = simpledialog.askstring("Buscar y Reemplazar", "Texto de reemplazo:")
            if replace_text is not None:  # Puede ser string vacío
                content = self.main_text.get(1.0, tk.END)
                new_content = content.replace(find_text, replace_text)
                
                if content != new_content:
                    self.main_text.delete(1.0, tk.END)
                    self.main_text.insert(1.0, new_content)
                    self.log_action(f"🔄 Texto reemplazado: '{find_text}' → '{replace_text}'")
                    messagebox.showinfo("Reemplazar", "Texto reemplazado correctamente")
                else:
                    self.log_action(f"🔄 No se encontró texto para reemplazar: '{find_text}'")
                    messagebox.showinfo("Reemplazar", "No se encontró texto para reemplazar")
    
    # ====================================================================
    # MÉTODOS DEL MENÚ VER
    # ====================================================================
    
    def toggle_toolbar(self):
        """Mostrar/ocultar barra de herramientas"""
        if self.show_toolbar.get():
            self.toolbar_frame.pack(fill='x', pady=(0, 5), before=self.toolbar_frame.master.winfo_children()[1])
            self.create_toolbar()
            self.log_action("🔧 Barra de herramientas mostrada")
        else:
            self.toolbar_frame.pack_forget()
            self.log_action("🔧 Barra de herramientas ocultada")
            
    def toggle_status_bar(self):
        """Mostrar/ocultar barra de estado"""
        if self.show_status_bar.get():
            self.status_bar.pack(side='bottom', fill='x')
            self.create_status_bar()
            self.log_action("📊 Barra de estado mostrada")
        else:
            self.status_bar.pack_forget()
            self.log_action("📊 Barra de estado ocultada")
            
    def toggle_word_wrap(self):
        """Activar/desactivar ajuste de línea"""
        wrap_mode = tk.WORD if self.word_wrap.get() else tk.NONE
        self.main_text.config(wrap=wrap_mode)
        status = "activado" if self.word_wrap.get() else "desactivado"
        self.log_action(f"📄 Ajuste de línea {status}")
        
    def set_zoom(self, level):
        """Establecer nivel de zoom"""
        self.log_action(f"🔍 Zoom establecido a {level}%")
        if hasattr(self, 'status_zoom'):
            self.status_zoom.config(text=f"🔍 {level}%")
        messagebox.showinfo("Zoom", f"Zoom establecido a {level}%\n(Simulación)")
        
    def zoom_in(self):
        """Acercar zoom"""
        self.log_action("🔍➕ Zoom acercado")
        messagebox.showinfo("Zoom", "Zoom acercado\n(Simulación)")
        
    def zoom_out(self):
        """Alejar zoom"""
        self.log_action("🔍➖ Zoom alejado")
        messagebox.showinfo("Zoom", "Zoom alejado\n(Simulación)")
        
    def change_theme(self, theme):
        """Cambiar tema de la aplicación"""
        self.current_theme.set(theme)
        self.log_action(f"🎨 Tema cambiado a: {theme}")
        if hasattr(self, 'status_theme'):
            self.status_theme.config(text=f"🎨 {theme}")
        messagebox.showinfo("Tema", f"Tema cambiado a: {theme}\n(Simulación)")
    
    # ====================================================================
    # MÉTODOS DEL MENÚ HERRAMIENTAS
    # ====================================================================
    
    def tools_word_count(self):
        """Contador de palabras"""
        content = self.main_text.get(1.0, tk.END)
        words = len(content.split())
        chars = len(content)
        lines = content.count('\n')
        
        stats = f"""📊 ESTADÍSTICAS DEL DOCUMENTO

📄 Líneas: {lines}
🔤 Palabras: {words}  
📝 Caracteres: {chars}
📝 Caracteres (sin espacios): {len(content.replace(' ', ''))}"""

        messagebox.showinfo("Contador de Palabras", stats)
        self.log_action(f"🔤 Contador: {words} palabras, {chars} caracteres")
        
    def tools_document_stats(self):
        """Estadísticas completas del documento"""
        content = self.main_text.get(1.0, tk.END)
        
        # Análisis más detallado
        paragraphs = content.split('\n\n')
        sentences = content.split('.')
        avg_words_per_line = len(content.split()) / max(content.count('\n'), 1)
        
        stats = f"""📊 ESTADÍSTICAS COMPLETAS

📄 Párrafos: {len(paragraphs)}
📝 Oraciones: {len(sentences)}
📊 Promedio palabras/línea: {avg_words_per_line:.1f}
📋 Archivo actual: {self.current_file or 'Sin guardar'}
💾 Estado: {'Modificado' if self.is_modified else 'Guardado'}"""

        messagebox.showinfo("Estadísticas del Documento", stats)
        self.log_action("📊 Estadísticas completas generadas")
        
    def tools_syntax_checker(self):
        """Validador de sintaxis"""
        self.log_action("🔍 Validando sintaxis del documento...")
        messagebox.showinfo("Validador", "🔍 Sintaxis validada correctamente\n(Simulación)")
        
    def tools_code_formatter(self):
        """Formateador de código"""
        self.log_action("🎨 Formateando código...")
        messagebox.showinfo("Formateador", "🎨 Código formateado correctamente\n(Simulación)")
        
    def toggle_auto_save(self):
        """Activar/desactivar guardado automático"""
        status = "activado" if self.auto_save.get() else "desactivado"
        self.log_action(f"💾 Guardado automático {status}")
        
    def tools_preferences(self):
        """Abrir ventana de preferencias"""
        self.log_action("⚙️ Abriendo ventana de preferencias...")
        messagebox.showinfo("Preferencias", "⚙️ Ventana de preferencias\n(Simulación)")
    
    # ====================================================================
    # MÉTODOS DEL MENÚ VENTANA
    # ====================================================================
    
    def window_new(self):
        """Crear nueva ventana"""
        self.log_action("➕ Creando nueva ventana...")
        messagebox.showinfo("Nueva Ventana", "➕ Nueva ventana creada\n(Simulación)")
        
    def arrange_windows(self, arrangement):
        """Organizar ventanas"""
        self.log_action(f"📐 Organizando ventanas: {arrangement}")
        messagebox.showinfo("Organizar", f"📐 Ventanas organizadas {arrangement}mente\n(Simulación)")
        
    def switch_to_window(self, window_name):
        """Cambiar a ventana específica"""
        self.log_action(f"🪟 Cambiando a ventana: {window_name}")
        messagebox.showinfo("Cambiar Ventana", f"🪟 Cambiado a: {window_name}\n(Simulación)")
    
    # ====================================================================
    # MÉTODOS DEL MENÚ AYUDA
    # ====================================================================
    
    def help_manual(self):
        """Mostrar manual de usuario"""
        manual_text = """📖 MANUAL DE USUARIO - SISTEMA DE MENÚS

🍽️ NAVEGACIÓN POR MENÚS:
• Usa la barra de menús superior para acceder a todas las funciones
• Los atajos de teclado aparecen junto a cada comando
• Algunas opciones tienen submenús con más opciones

📁 ARCHIVO:
• Crear, abrir, guardar documentos
• Exportar en diferentes formatos
• Historial de archivos recientes

✏️ EDITAR:
• Deshacer/rehacer cambios
• Cortar, copiar, pegar texto
• Buscar y reemplazar

👁️ VER:
• Cambiar tema y zoom
• Mostrar/ocultar barras
• Ajustar configuración visual

🔧 HERRAMIENTAS:
• Contador de palabras
• Estadísticas de documento
• Validadores y formateadores

🖱️ MENÚ CONTEXTUAL:
• Clic derecho en el texto para opciones rápidas
• Funciones específicas del contexto actual"""

        messagebox.showinfo("Manual de Usuario", manual_text)
        self.log_action("📖 Manual de usuario consultado")
        
    def help_tips(self):
        """Mostrar consejos y trucos"""
        tips = """💡 CONSEJOS Y TRUCOS

⌨️ ATAJOS ÚTILES:
• Ctrl+N: Nuevo documento
• Ctrl+O: Abrir archivo
• Ctrl+S: Guardar
• Ctrl+F: Buscar
• Ctrl+Z: Deshacer

🖱️ NAVEGACIÓN:
• Clic derecho para menú contextual
• Los separadores organizan opciones relacionadas
• Las opciones deshabilitadas aparecen grises

🎨 PERSONALIZACIÓN:
• Cambia el tema desde Ver → Tema
• Ajusta el zoom para mejor lectura
• Oculta barras para más espacio

💾 PRODUCTIVIDAD:
• Usa guardado automático
• Aprovecha el historial de archivos recientes
• Las estadísticas ayudan a revisar tu trabajo"""

        messagebox.showinfo("Consejos y Trucos", tips)
        self.log_action("💡 Consejos y trucos consultados")
        
    def help_website(self):
        """Abrir sitio web"""
        self.log_action("🌐 Abriendo sitio web oficial...")
        messagebox.showinfo("Sitio Web", "🌐 Abriendo sitio web oficial\n(Simulación)")
        
    def help_support(self):
        """Contactar soporte técnico"""
        self.log_action("📧 Contactando soporte técnico...")
        messagebox.showinfo("Soporte", "📧 Contactando soporte técnico\n(Simulación)")
        
    def help_updates(self):
        """Buscar actualizaciones"""
        self.log_action("🔄 Buscando actualizaciones...")
        messagebox.showinfo("Actualizaciones", "🔄 No hay actualizaciones disponibles\n(Simulación)")
        
    def help_about(self):
        """Mostrar información de la aplicación"""
        about_text = """🍽️ SISTEMA DE MENÚS EN TKINTER

📋 Versión: 1.0.0
📅 Fecha: 2025
👨‍💻 Desarrollado con Python + Tkinter

🎯 CARACTERÍSTICAS:
✅ Barra de menús completa
✅ Submenús jerárquicos  
✅ Atajos de teclado
✅ Menús contextuales
✅ Estados dinámicos
✅ Iconos y separadores
✅ Funcionalidades reales

📧 Contacto: soporte@ejemplo.com
🌐 Web: www.ejemplo.com

© 2025 - Sistema de Gestión Estudiantil"""

        messagebox.showinfo("Acerca de", about_text)
        self.log_action("ℹ️ Información de la aplicación consultada")
    
    # ====================================================================
    # MÉTODOS DE MENÚ CONTEXTUAL
    # ====================================================================
    
    def show_context_menu(self, event):
        """Mostrar menú contextual"""
        try:
            # Verificar si hay texto seleccionado para habilitar/deshabilitar opciones
            selection = self.main_text.selection_get()
            has_selection = True
        except:
            has_selection = False
            
        # Actualizar estado de opciones según contexto
        cut_state = "normal" if has_selection else "disabled"
        copy_state = "normal" if has_selection else "disabled"
        
        self.text_context_menu.entryconfig(0, state=cut_state)   # Cortar
        self.text_context_menu.entryconfig(1, state=copy_state)  # Copiar
        
        # Mostrar menú en posición del cursor
        self.text_context_menu.post(event.x_root, event.y_root)
        self.log_action("🖱️ Menú contextual mostrado")
        
    def format_uppercase(self):
        """Convertir selección a mayúsculas"""
        try:
            selected_text = self.main_text.selection_get()
            self.main_text.delete(tk.SEL_FIRST, tk.SEL_LAST)
            self.main_text.insert(tk.INSERT, selected_text.upper())
            self.log_action("🔤 Texto convertido a MAYÚSCULAS")
        except:
            self.log_action("🔤 No hay texto seleccionado para formatear")
            
    def format_lowercase(self):
        """Convertir selección a minúsculas"""
        try:
            selected_text = self.main_text.selection_get()
            self.main_text.delete(tk.SEL_FIRST, tk.SEL_LAST)
            self.main_text.insert(tk.INSERT, selected_text.lower())
            self.log_action("🔡 Texto convertido a minúsculas")
        except:
            self.log_action("🔡 No hay texto seleccionado para formatear")
            
    def format_capitalize(self):
        """Capitalizar selección"""
        try:
            selected_text = self.main_text.selection_get()
            self.main_text.delete(tk.SEL_FIRST, tk.SEL_LAST)
            self.main_text.insert(tk.INSERT, selected_text.title())
            self.log_action("🎨 Texto capitalizado")
        except:
            self.log_action("🎨 No hay texto seleccionado para formatear")
            
    def search_in_google(self):
        """Buscar texto seleccionado en Google"""
        try:
            selected_text = self.main_text.selection_get()
            self.log_action(f"🔍 Buscando en Google: '{selected_text[:20]}...'")
            messagebox.showinfo("Buscar", f"🔍 Buscando en Google: '{selected_text[:50]}...'\n(Simulación)")
        except:
            self.log_action("🔍 No hay texto seleccionado para buscar")
    
    # ====================================================================
    # MÉTODOS AUXILIARES
    # ====================================================================
    
    def log_action(self, message):
        """Registrar acción en el log"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)  # Scroll automático
        
        self.action_counter += 1
        
    def update_status(self, message):
        """Actualizar barra de estado"""
        if hasattr(self, 'status_left'):
            self.status_left.config(text=message)
            
    def create_simple_tooltip(self, widget, text):
        """Crear tooltip simple"""
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

def main():
    """
    Función principal para ejecutar la demostración
    """
    root = tk.Tk()
    app = MenuSystemDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
