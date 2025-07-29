#!/usr/bin/env python3
"""
Demostración de Widgets Básicos de Tkinter
==========================================

Este script demuestra el uso de los componentes básicos de Tkinter:
- Label (Etiquetas)
- Entry (Campos de texto)
- Button (Botones)
- Frame (Marcos/contenedores)

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

import tkinter as tk
from tkinter import messagebox

class WidgetsBasicosDemo:
    """
    Clase que demuestra el uso de widgets básicos de Tkinter
    """
    
    def __init__(self, root: tk.Tk):
        """
        Inicializa la ventana de demostración
        
        Args:
            root: Ventana principal de Tkinter
        """
        self.root = root
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """
        Configura las propiedades básicas de la ventana
        """
        self.root.title("Demostración: Widgets Básicos de Tkinter")
        self.root.geometry("600x500")
        self.root.configure(bg='#1E1E1E')  # Color modo oscuro macOS
        self.root.resizable(True, True)
        
        # Centrar la ventana
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_widgets(self):
        """
        Crea todos los widgets de demostración
        """
        # ====================================================================
        # FRAME PRINCIPAL - Contenedor para organizar todos los widgets
        # ====================================================================
        main_frame = tk.Frame(
            self.root, 
            bg='#1E1E1E',
            padx=20,
            pady=20
        )
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # ====================================================================
        # SECCIÓN 1: ETIQUETAS (LABELS) - Demostración de diferentes estilos
        # ====================================================================
        self.create_labels_section(main_frame)
        
        # ====================================================================
        # SECCIÓN 2: CAMPOS DE TEXTO (ENTRIES) - Diferentes configuraciones
        # ====================================================================
        self.create_entries_section(main_frame)
        
        # ====================================================================
        # SECCIÓN 3: BOTONES (BUTTONS) - Estilos y funcionalidades variadas
        # ====================================================================
        self.create_buttons_section(main_frame)
        
        # ====================================================================
        # SECCIÓN 4: FRAME CON BORDES - Demostración de contenedores
        # ====================================================================
        self.create_frames_section(main_frame)
        
    def create_labels_section(self, parent):
        """
        Crea la sección de demostración de Labels
        """
        # Frame contenedor para las etiquetas
        labels_frame = tk.LabelFrame(
            parent,
            text="📝 Demostración de Labels (Etiquetas)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        labels_frame.pack(fill='x', pady=(0, 15))
        
        # LABEL básico con texto simple
        basic_label = tk.Label(
            labels_frame,
            text="Etiqueta básica con texto simple",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10)
        )
        basic_label.pack(anchor='w', pady=2)
        
        # LABEL con formato de fuente avanzado
        formatted_label = tk.Label(
            labels_frame,
            text="Etiqueta con formato: Negrita, Cursiva y Color",
            bg='#2D2D30',
            fg='#E74C3C',  # Color rojo
            font=("Times", 12, "bold italic"),
            relief='raised',  # Efecto de relieve
            borderwidth=2
        )
        formatted_label.pack(anchor='w', pady=2)
        
        # LABEL con múltiples líneas y justificación
        multiline_label = tk.Label(
            labels_frame,
            text="Esta es una etiqueta\ncon múltiples líneas\nque demuestra la justificación\ny el ancho fijo",
            bg='#ECF0F1',
            fg='#000',
            font=("Courier", 9),
            justify='center',  # Justificación centrada
            width=40,          # Ancho fijo en caracteres
            height=4,          # Alto fijo en líneas
            relief='sunken',   # Efecto hundido
            borderwidth=2
        )
        multiline_label.pack(pady=5)
        
        # LABEL con emojis y caracteres especiales
        emoji_label = tk.Label(
            labels_frame,
            text="🎯 Etiqueta con emojis y símbolos especiales ⭐ ✨ 🚀",
            bg='#2D2D30',
            fg='#FFA500',
            font=("Arial", 11, "bold"),
            relief='ridge',
            borderwidth=3
        )
        emoji_label.pack(pady=2)
        
    def create_entries_section(self, parent):
        """
        Crea la sección de demostración de Entries
        """
        # Variables para los campos de texto
        self.text_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.number_var = tk.StringVar()
        self.readonly_var = tk.StringVar(value="Campo de solo lectura")
        
        # Frame contenedor para los campos de texto
        entries_frame = tk.LabelFrame(
            parent,
            text="⌨️ Demostración de Entries (Campos de Texto)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        entries_frame.pack(fill='x', pady=(0, 15))
        
        # Configurar grid para organización
        entries_frame.grid_columnconfigure(1, weight=1)
        
        # ENTRY básico para texto normal
        tk.Label(
            entries_frame,
            text="Texto normal:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).grid(row=0, column=0, sticky='w', pady=5, padx=(0, 10))
        
        normal_entry = tk.Entry(
            entries_frame,
            textvariable=self.text_var,
            font=("Arial", 11),
            bg='#F8F9FA',
            fg='#FFFFFF',
            relief='sunken',
            borderwidth=2,
            insertbackground='#3498DB'  # Color del cursor
        )
        normal_entry.grid(row=0, column=1, sticky='ew', pady=5)
        
        # ENTRY para contraseña (caracteres ocultos)
        tk.Label(
            entries_frame,
            text="Contraseña:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).grid(row=1, column=0, sticky='w', pady=5, padx=(0, 10))
        
        password_entry = tk.Entry(
            entries_frame,
            textvariable=self.password_var,
            font=("Arial", 11),
            bg='#F8F9FA',
            fg='#FFFFFF',
            show='*',  # Ocultar caracteres con asteriscos
            relief='sunken',
            borderwidth=2
        )
        password_entry.grid(row=1, column=1, sticky='ew', pady=5)
        
        # ENTRY para números con validación
        tk.Label(
            entries_frame,
            text="Solo números:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).grid(row=2, column=0, sticky='w', pady=5, padx=(0, 10))
        
        number_entry = tk.Entry(
            entries_frame,
            textvariable=self.number_var,
            font=("Arial", 11),
            bg='#E8F6F3',
            fg='#FFFFFF',
            relief='sunken',
            borderwidth=2,
            validate='key',  # Validación en tiempo real
            validatecommand=(self.root.register(self.validate_number), '%P')
        )
        number_entry.grid(row=2, column=1, sticky='ew', pady=5)
        
        # ENTRY de solo lectura
        tk.Label(
            entries_frame,
            text="Solo lectura:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).grid(row=3, column=0, sticky='w', pady=5, padx=(0, 10))
        
        readonly_entry = tk.Entry(
            entries_frame,
            textvariable=self.readonly_var,
            font=("Arial", 11),
            bg='#F4F4F4',
            fg='#7F8C8D',
            relief='flat',
            borderwidth=2,
            state='readonly'  # No editable
        )
        readonly_entry.grid(row=3, column=1, sticky='ew', pady=5)
        
        # Botón para mostrar valores
        show_values_btn = tk.Button(
            entries_frame,
            text="📋 Mostrar Valores de los Campos",
            font=("Arial", 10, "bold"),
            bg='#3498DB',
            fg='#2D2D30',
            relief='raised',
            borderwidth=2,
            command=self.show_entry_values
        )
        show_values_btn.grid(row=4, column=0, columnspan=2, pady=(15, 5))
        
    def create_buttons_section(self, parent):
        """
        Crea la sección de demostración de Buttons
        """
        # Frame contenedor para los botones
        buttons_frame = tk.LabelFrame(
            parent,
            text="🔘 Demostración de Buttons (Botones)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        buttons_frame.pack(fill='x', pady=(0, 15))
        
        # Fila 1: Botones básicos con diferentes estilos
        row1_frame = tk.Frame(buttons_frame, bg='#2D2D30')
        row1_frame.pack(fill='x', pady=5)
        
        # Botón básico
        basic_btn = tk.Button(
            row1_frame,
            text="Botón Básico",
            font=("Arial", 10),
            command=lambda: self.show_message("Botón Básico", "Has clickeado el botón básico")
        )
        basic_btn.pack(side='left', padx=5)
        
        # Botón con colores personalizados
        colored_btn = tk.Button(
            row1_frame,
            text="Botón Colorido",
            font=("Arial", 10, "bold"),
            bg='#E74C3C',
            fg='#2D2D30',
            activebackground='#C0392B',
            activeforeground='#2D2D30',
            command=lambda: self.show_message("Botón Colorido", "¡Me gusta este color!")
        )
        colored_btn.pack(side='left', padx=5)
        
        # Botón con relieve especial
        relief_btn = tk.Button(
            row1_frame,
            text="Botón con Relieve",
            font=("Arial", 10),
            bg='#27AE60',
            fg='#2D2D30',
            relief='ridge',
            borderwidth=4,
            command=lambda: self.show_message("Relieve", "Botón con efecto ridge")
        )
        relief_btn.pack(side='left', padx=5)
        
        # Fila 2: Botones con funcionalidades especiales
        row2_frame = tk.Frame(buttons_frame, bg='#2D2D30')
        row2_frame.pack(fill='x', pady=5)
        
        # Botón deshabilitado
        disabled_btn = tk.Button(
            row2_frame,
            text="Botón Deshabilitado",
            font=("Arial", 10),
            bg='#BDC3C7',
            fg='#7F8C8D',
            state='disabled'  # Botón no clickeable
        )
        disabled_btn.pack(side='left', padx=5)
        
        # Botón con cursor personalizado
        cursor_btn = tk.Button(
            row2_frame,
            text="Cursor Especial",
            font=("Arial", 10),
            bg='#8E44AD',
            fg='#2D2D30',
            cursor='hand2',  # Cursor de mano
            command=lambda: self.show_message("Cursor", "¡Cursor de mano!")
        )
        cursor_btn.pack(side='left', padx=5)
        
        # Botón que cambia su propio texto
        self.toggle_text = "Clickea para cambiar"
        self.change_btn = tk.Button(
            row2_frame,
            text=self.toggle_text,
            font=("Arial", 10),
            bg='#F39C12',
            fg='#2D2D30',
            command=self.toggle_button_text
        )
        self.change_btn.pack(side='left', padx=5)
        
    def create_frames_section(self, parent):
        """
        Crea la sección de demostración de Frames
        """
        # Frame contenedor principal
        frames_demo = tk.LabelFrame(
            parent,
            text="🖼️ Demostración de Frames (Marcos/Contenedores)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        frames_demo.pack(fill='both', expand=True)
        
        # Frame con borde raised
        raised_frame = tk.Frame(
            frames_demo,
            bg='#E8F8F5',
            relief='raised',
            borderwidth=3,
            padx=10,
            pady=10
        )
        raised_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        tk.Label(
            raised_frame,
            text="Frame con relieve 'raised'",
            bg='#E8F8F5',
            fg='#4CAF50',
            font=("Arial", 10, "bold")
        ).pack()
        
        tk.Label(
            raised_frame,
            text="Este marco tiene un efecto\nelevado que lo hace\nsobresalir del fondo",
            bg='#E8F8F5',
            fg='#000',
            justify='center'
        ).pack(pady=5)
        
        # Frame con borde sunken
        sunken_frame = tk.Frame(
            frames_demo,
            bg='#FDF2E9',
            relief='sunken',
            borderwidth=3,
            padx=10,
            pady=10
        )
        sunken_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        tk.Label(
            sunken_frame,
            text="Frame con relieve 'sunken'",
            bg='#FDF2E9',
            fg='#E67E22',
            font=("Arial", 10, "bold")
        ).pack()
        
        tk.Label(
            sunken_frame,
            text="Este marco tiene un efecto\nhundido que lo hace\nverse empotrado",
            bg='#FDF2E9',
            fg='#000',
            justify='center'
        ).pack(pady=5)
        
        # Frame con borde ridge
        ridge_frame = tk.Frame(
            frames_demo,
            bg='#F4ECF7',
            relief='ridge',
            borderwidth=4,
            padx=10,
            pady=10
        )
        ridge_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        tk.Label(
            ridge_frame,
            text="Frame con relieve 'ridge'",
            bg='#F4ECF7',
            fg='#8E44AD',
            font=("Arial", 10, "bold")
        ).pack()
        
        tk.Label(
            ridge_frame,
            text="Este marco tiene un efecto\nde cresta que crea\nun borde en 3D",
            bg='#F4ECF7',
            fg='#000',
            justify='center'
        ).pack(pady=5)
        
    # ====================================================================
    # MÉTODOS DE FUNCIONALIDAD
    # ====================================================================
    
    def validate_number(self, value):
        """
        Valida que el input sea solo números
        
        Args:
            value (str): Valor a validar
            
        Returns:
            bool: True si es válido, False si no
        """
        if value == "":
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False
            
    def show_entry_values(self):
        """
        Muestra los valores de todos los campos de texto
        """
        values = f"""Valores de los campos:

Texto normal: '{self.text_var.get()}'
Contraseña: '{self.password_var.get()}'
Número: '{self.number_var.get()}'
Solo lectura: '{self.readonly_var.get()}'"""
        
        messagebox.showinfo("Valores de los Campos", values)
        
    def show_message(self, title, message):
        """
        Muestra un mensaje de información
        
        Args:
            title (str): Título del mensaje
            message (str): Contenido del mensaje
        """
        messagebox.showinfo(title, message)
        
    def toggle_button_text(self):
        """
        Cambia el texto del botón cada vez que se clickea
        """
        if self.toggle_text == "Clickea para cambiar":
            self.toggle_text = "¡Texto cambiado!"
            self.change_btn.configure(bg='#2ECC71')
        else:
            self.toggle_text = "Clickea para cambiar"
            self.change_btn.configure(bg='#F39C12')
            
        self.change_btn.configure(text=self.toggle_text)

def main():
    """
    Función principal para ejecutar la demostración
    """
    root = tk.Tk()
    app = WidgetsBasicosDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
