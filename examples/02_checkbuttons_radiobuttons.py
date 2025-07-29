#!/usr/bin/env python3
"""
Demostración de Checkbuttons y Radiobuttons
==========================================

Este script demuestra el uso de:
- Checkbutton (Casillas de verificación) - Selección múltiple
- Radiobutton (Botones de opción) - Selección exclusiva
- Variables de control (BooleanVar, StringVar, IntVar)
- Diferentes estilos y configuraciones

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

import tkinter as tk
from tkinter import messagebox

class CheckRadioDemo:
    """
    Clase que demuestra el uso de Checkbuttons y Radiobuttons
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
        self.create_widgets()
        
    def setup_window(self):
        """
        Configura las propiedades de la ventana
        """
        self.root.title("Demostración: Checkbuttons y Radiobuttons")
        self.root.geometry("700x650")
        self.root.configure(bg='#2D2D30')
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
        Inicializa todas las variables de control
        """
        # Variables para Checkbuttons (BooleanVar)
        self.check_var1 = tk.BooleanVar(value=True)   # Marcado por defecto
        self.check_var2 = tk.BooleanVar(value=False)  # Desmarcado por defecto
        self.check_var3 = tk.BooleanVar(value=False)
        self.check_var4 = tk.BooleanVar(value=True)
        
        # Variables para preferencias (ejemplo práctico)
        self.notifications = tk.BooleanVar(value=True)
        self.auto_save = tk.BooleanVar(value=False)
        self.dark_mode = tk.BooleanVar(value=False)
        self.sound_effects = tk.BooleanVar(value=True)
        
        # Variables para Radiobuttons (StringVar)
        self.gender_var = tk.StringVar(value="no_especifica")
        self.difficulty_var = tk.StringVar(value="intermedio")
        self.language_var = tk.StringVar(value="spanish")
        
        # Variable para Radiobuttons con IntVar (números)
        self.priority_var = tk.IntVar(value=2)  # 1=Baja, 2=Media, 3=Alta
        
    def create_widgets(self):
        """
        Crea todos los widgets de la interfaz
        """
        # Frame principal
        main_frame = tk.Frame(
            self.root,
            bg='#1E1E1E',
            padx=20,
            pady=20
        )
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Crear secciones
        self.create_checkbuttons_section(main_frame)
        self.create_radiobuttons_section(main_frame)
        self.create_practical_examples(main_frame)
        self.create_control_buttons(main_frame)
        
    def create_checkbuttons_section(self, parent):
        """
        Crea la sección de demostración de Checkbuttons
        """
        # Frame para checkbuttons
        check_frame = tk.LabelFrame(
            parent,
            text="☑️ Demostración de Checkbuttons (Casillas de Verificación)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        check_frame.pack(fill='x', pady=(0, 15))
        
        # Título explicativo
        tk.Label(
            check_frame,
            text="Los Checkbuttons permiten selecciones múltiples independientes:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "italic")
        ).pack(anchor='w', pady=(0, 10))
        
        # Checkbutton básico
        check1 = tk.Checkbutton(
            check_frame,
            text="✅ Opción 1 - Checkbutton básico (marcado por defecto)",
            variable=self.check_var1,
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10),
            activebackground='#ECF0F1',
            command=lambda: self.on_check_change("Opción 1", self.check_var1)
        )
        check1.pack(anchor='w', pady=2)
        
        # Checkbutton con colores personalizados
        check2 = tk.Checkbutton(
            check_frame,
            text="🟢 Opción 2 - Con colores personalizados",
            variable=self.check_var2,
            bg='#2D2D30',
            fg='#27AE60',
            selectcolor='#2ECC71',  # Color cuando está marcado
            activebackground='#E8F8F5',
            font=("Arial", 10, "bold"),
            command=lambda: self.on_check_change("Opción 2", self.check_var2)
        )
        check2.pack(anchor='w', pady=2)
        
        # Checkbutton con indicador personalizado
        check3 = tk.Checkbutton(
            check_frame,
            text="🔵 Opción 3 - Con indicador azul",
            variable=self.check_var3,
            bg='#2D2D30',
            fg='#3498DB',
            selectcolor='#5DADE2',
            activebackground='#EBF5FB',
            font=("Arial", 10),
            indicatoron=True,  # Mostrar indicador (por defecto)
            command=lambda: self.on_check_change("Opción 3", self.check_var3)
        )
        check3.pack(anchor='w', pady=2)
        
        # Checkbutton estilo botón (sin indicador)
        check4 = tk.Checkbutton(
            check_frame,
            text="🔄 Opción 4 - Estilo botón (sin indicador)",
            variable=self.check_var4,
            bg='#8E44AD',
            fg='#2D2D30',
            selectcolor='#BB8FCE',
            activebackground='#A569BD',
            activeforeground='#2D2D30',
            font=("Arial", 10, "bold"),
            indicatoron=False,  # Sin indicador, estilo botón
            relief='raised',
            borderwidth=2,
            padx=10,
            pady=5,
            command=lambda: self.on_check_change("Opción 4", self.check_var4)
        )
        check4.pack(anchor='w', pady=5)
        
    def create_radiobuttons_section(self, parent):
        """
        Crea la sección de demostración de Radiobuttons
        """
        # Frame para radiobuttons
        radio_frame = tk.LabelFrame(
            parent,
            text="🔘 Demostración de Radiobuttons (Botones de Opción)",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        radio_frame.pack(fill='x', pady=(0, 15))
        
        # Título explicativo
        tk.Label(
            radio_frame,
            text="Los Radiobuttons permiten solo UNA selección por grupo:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "italic")
        ).pack(anchor='w', pady=(0, 10))
        
        # Configurar grid para organizar en columnas
        radio_frame.grid_columnconfigure(0, weight=1)
        radio_frame.grid_columnconfigure(1, weight=1)
        
        # GRUPO 1: Género (StringVar)
        gender_frame = tk.Frame(radio_frame, bg='#2D2D30')
        gender_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        tk.Label(
            gender_frame,
            text="👤 Selecciona tu género:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).pack(anchor='w', pady=(0, 5))
        
        # Radiobuttons para género
        genders = [
            ("♂️ Masculino", "masculino", "#3498DB"),
            ("♀️ Femenino", "femenino", "#E91E63"),
            ("⚧️ No binario", "no_binario", "#9B59B6"),
            ("❓ Prefiero no especificar", "no_especifica", "#95A5A6")
        ]
        
        for text, value, color in genders:
            radio = tk.Radiobutton(
                gender_frame,
                text=text,
                variable=self.gender_var,
                value=value,
                bg='#2D2D30',
                fg=color,
                selectcolor='#F8F9FA',
                activebackground='#F8F9FA',
                font=("Arial", 9),
                command=lambda v=value: self.on_radio_change("Género", v)
            )
            radio.pack(anchor='w', pady=1)
            
        # GRUPO 2: Dificultad (StringVar)
        difficulty_frame = tk.Frame(radio_frame, bg='#2D2D30')
        difficulty_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        tk.Label(
            difficulty_frame,
            text="🎯 Nivel de dificultad:",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).pack(anchor='w', pady=(0, 5))
        
        # Radiobuttons para dificultad
        difficulties = [
            ("🟢 Principiante", "principiante", "#27AE60"),
            ("🟡 Intermedio", "intermedio", "#F39C12"),
            ("🟠 Avanzado", "avanzado", "#E67E22"),
            ("🔴 Experto", "experto", "#E74C3C")
        ]
        
        for text, value, color in difficulties:
            radio = tk.Radiobutton(
                difficulty_frame,
                text=text,
                variable=self.difficulty_var,
                value=value,
                bg='#2D2D30',
                fg=color,
                selectcolor='#F8F9FA',
                activebackground='#F8F9FA',
                font=("Arial", 9, "bold"),
                command=lambda v=value: self.on_radio_change("Dificultad", v)
            )
            radio.pack(anchor='w', pady=1)
            
        # GRUPO 3: Prioridad con IntVar (números)
        priority_frame = tk.Frame(radio_frame, bg='#2D2D30')
        priority_frame.pack(fill='x', pady=(15, 0))
        
        tk.Label(
            priority_frame,
            text="⭐ Prioridad (usando IntVar con números):",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).pack(anchor='w', pady=(0, 5))
        
        priority_container = tk.Frame(priority_frame, bg='#2D2D30')
        priority_container.pack(anchor='w')
        
        priorities = [
            ("🟢 Baja (1)", 1, "#2ECC71"),
            ("🟡 Media (2)", 2, "#F1C40F"),
            ("🔴 Alta (3)", 3, "#E74C3C")
        ]
        
        for text, value, color in priorities:
            radio = tk.Radiobutton(
                priority_container,
                text=text,
                variable=self.priority_var,
                value=value,
                bg='#2D2D30',
                fg=color,
                selectcolor='#F8F9FA',
                activebackground='#F8F9FA',
                font=("Arial", 9, "bold"),
                command=lambda v=value: self.on_radio_change("Prioridad", f"Nivel {v}")
            )
            radio.pack(side='left', padx=(0, 20))
            
    def create_practical_examples(self, parent):
        """
        Crea ejemplos prácticos de uso
        """
        # Frame para ejemplos prácticos
        practical_frame = tk.LabelFrame(
            parent,
            text="⚙️ Ejemplo Práctico: Configuración de Aplicación",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        practical_frame.pack(fill='x', pady=(0, 15))
        
        # Configuraciones con checkboxes
        tk.Label(
            practical_frame,
            text="Configuraciones de la aplicación (selección múltiple):",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).pack(anchor='w', pady=(0, 5))
        
        configs = [
            ("🔔 Habilitar notificaciones", self.notifications, "#3498DB"),
            ("💾 Guardado automático", self.auto_save, "#27AE60"),
            ("🌙 Modo oscuro", self.dark_mode, "#34495E"),
            ("🔊 Efectos de sonido", self.sound_effects, "#E67E22")
        ]
        
        for text, var, color in configs:
            check = tk.Checkbutton(
                practical_frame,
                text=text,
                variable=var,
                bg='#2D2D30',
                fg=color,
                selectcolor='#F8F9FA',
                activebackground='#F8F9FA',
                font=("Arial", 10),
                command=lambda t=text, v=var: self.on_config_change(t, v)
            )
            check.pack(anchor='w', pady=2)
            
        # Idiomas con radiobuttons
        tk.Label(
            practical_frame,
            text="Idioma de la interfaz (selección única):",
            bg='#2D2D30',
            fg='#FFFFFF',
            font=("Arial", 10, "bold")
        ).pack(anchor='w', pady=(15, 5))
        
        language_container = tk.Frame(practical_frame, bg='#2D2D30')
        language_container.pack(anchor='w')
        
        languages = [
            ("🇪🇸 Español", "spanish"),
            ("🇺🇸 English", "english"),
            ("🇫🇷 Français", "french"),
            ("🇩🇪 Deutsch", "german")
        ]
        
        for text, value in languages:
            radio = tk.Radiobutton(
                language_container,
                text=text,
                variable=self.language_var,
                value=value,
                bg='#2D2D30',
                fg='#FFFFFF',
                selectcolor='#F8F9FA',
                activebackground='#F8F9FA',
                font=("Arial", 10),
                command=lambda v=value: self.on_language_change(v)
            )
            radio.pack(side='left', padx=(0, 15))
            
    def create_control_buttons(self, parent):
        """
        Crea botones de control para la demostración
        """
        # Frame para botones
        buttons_frame = tk.Frame(parent, bg='#2D2D30')
        buttons_frame.pack(fill='x', pady=(10, 0))
        
        # Centrar botones
        button_container = tk.Frame(buttons_frame, bg='#2D2D30')
        button_container.pack()
        
        # Botón para mostrar valores
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
            command=self.show_all_values
        )
        show_btn.pack(side='left', padx=5)
        
        # Botón para reiniciar
        reset_btn = tk.Button(
            button_container,
            text="🔄 Reiniciar Valores",
            font=("Arial", 11, "bold"),
            bg='#E67E22',
            fg='#2D2D30',
            activebackground='#D35400',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.reset_values
        )
        reset_btn.pack(side='left', padx=5)
        
        # Botón para marcar/desmarcar todos los checks
        toggle_btn = tk.Button(
            button_container,
            text="☑️ Toggle Todos los Checks",
            font=("Arial", 11, "bold"),
            bg='#27AE60',
            fg='#2D2D30',
            activebackground='#229954',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=8,
            command=self.toggle_all_checks
        )
        toggle_btn.pack(side='left', padx=5)
        
    # ====================================================================
    # MÉTODOS DE MANEJO DE EVENTOS
    # ====================================================================
    
    def on_check_change(self, option_name, var):
        """
        Maneja el cambio en un checkbutton
        
        Args:
            option_name (str): Nombre de la opción
            var (BooleanVar): Variable asociada
        """
        state = "marcado" if var.get() else "desmarcado"
        print(f"{option_name} ha sido {state}")
        
    def on_radio_change(self, group_name, value):
        """
        Maneja el cambio en un radiobutton
        
        Args:
            group_name (str): Nombre del grupo
            value (str): Valor seleccionado
        """
        print(f"{group_name} cambiado a: {value}")
        
    def on_config_change(self, config_name, var):
        """
        Maneja cambios en configuración
        
        Args:
            config_name (str): Nombre de la configuración
            var (BooleanVar): Variable asociada
        """
        state = "activado" if var.get() else "desactivado"
        print(f"Configuración '{config_name}' {state}")
        
    def on_language_change(self, language):
        """
        Maneja cambio de idioma
        
        Args:
            language (str): Idioma seleccionado
        """
        print(f"Idioma cambiado a: {language}")
        
    def show_all_values(self):
        """
        Muestra todos los valores seleccionados
        """
        # Recopilar valores de checkbuttons
        check_values = f"""Checkbuttons:
• Opción 1: {'✅' if self.check_var1.get() else '❌'}
• Opción 2: {'✅' if self.check_var2.get() else '❌'}
• Opción 3: {'✅' if self.check_var3.get() else '❌'}
• Opción 4: {'✅' if self.check_var4.get() else '❌'}"""
        
        # Recopilar valores de radiobuttons
        radio_values = f"""Radiobuttons:
• Género: {self.gender_var.get()}
• Dificultad: {self.difficulty_var.get()}
• Prioridad: {self.priority_var.get()}
• Idioma: {self.language_var.get()}"""
        
        # Recopilar configuraciones
        config_values = f"""Configuraciones:
• Notificaciones: {'✅' if self.notifications.get() else '❌'}
• Guardado automático: {'✅' if self.auto_save.get() else '❌'}
• Modo oscuro: {'✅' if self.dark_mode.get() else '❌'}
• Efectos de sonido: {'✅' if self.sound_effects.get() else '❌'}"""
        
        full_message = f"{check_values}\n\n{radio_values}\n\n{config_values}"
        
        messagebox.showinfo("Valores Actuales", full_message)
        
    def reset_values(self):
        """
        Reinicia todos los valores a sus valores por defecto
        """
        # Reiniciar checkbuttons
        self.check_var1.set(True)
        self.check_var2.set(False)
        self.check_var3.set(False)
        self.check_var4.set(True)
        
        # Reiniciar radiobuttons
        self.gender_var.set("no_especifica")
        self.difficulty_var.set("intermedio")
        self.priority_var.set(2)
        self.language_var.set("spanish")
        
        # Reiniciar configuraciones
        self.notifications.set(True)
        self.auto_save.set(False)
        self.dark_mode.set(False)
        self.sound_effects.set(True)
        
        messagebox.showinfo("Reiniciado", "Todos los valores han sido restaurados a sus valores por defecto")
        
    def toggle_all_checks(self):
        """
        Alterna el estado de todos los checkbuttons
        """
        # Obtener estado actual del primer check
        current_state = self.check_var1.get()
        new_state = not current_state
        
        # Aplicar nuevo estado a todos
        self.check_var1.set(new_state)
        self.check_var2.set(new_state)
        self.check_var3.set(new_state)
        self.check_var4.set(new_state)
        
        # También configuraciones
        self.notifications.set(new_state)
        self.auto_save.set(new_state)
        self.dark_mode.set(new_state)
        self.sound_effects.set(new_state)
        
        action = "marcados" if new_state else "desmarcados"
        messagebox.showinfo("Toggle Completado", f"Todos los checkbuttons han sido {action}")

def main():
    """
    Función principal para ejecutar la demostración
    """
    root = tk.Tk()
    app = CheckRadioDemo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
