#!/usr/bin/env python3
"""
Componente de Configuración
==========================

Este módulo contiene la clase ConfigurationPanel que maneja
las configuraciones de la aplicación.

Incluye:
- Checkboxes para preferencias
- Radiobuttons para opciones de tema
- Gestión de estado de configuración
- Persistencia de configuraciones

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

import tkinter as tk
from tkinter import messagebox


class ConfigurationPanel:
    """
    Clase que maneja el panel de configuración de la aplicación
    """
    
    def __init__(self, parent, on_config_changed=None):
        """
        Inicializa el panel de configuración
        
        Args:
            parent: Widget padre donde se colocará el panel
            on_config_changed: Callback que se ejecuta cuando cambia la configuración
        """
        self.parent = parent
        self.on_config_changed = on_config_changed
        self.init_variables()
        self.create_panel()
        
    def init_variables(self):
        """
        Inicializa las variables de configuración
        """
        # Variables para checkboxes
        self.notifications_var = tk.BooleanVar(value=True)
        self.newsletter_var = tk.BooleanVar(value=False)
        self.terms_var = tk.BooleanVar(value=False)
        self.backup_var = tk.BooleanVar(value=True)
        
        # Variables para radiobuttons
        self.theme_var = tk.StringVar(value="claro")
        
        # Vincular eventos de cambio
        for var in [self.notifications_var, self.newsletter_var, self.terms_var, self.backup_var]:
            var.trace_add('write', self.on_setting_changed)
        self.theme_var.trace_add('write', self.on_setting_changed)
        
    def create_panel(self):
        """
        Crea la interfaz del panel de configuración
        """
        # Frame principal
        self.config_frame = tk.LabelFrame(
            self.parent,
            text="⚙️ Configuraciones",
            font=("Arial", 12, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=15,
            pady=15,
            relief='groove',
            borderwidth=2
        )
        self.config_frame.pack(fill='x', pady=(10, 0))
        
        self.create_preferences()
        self.create_theme_selection()
        
    def create_preferences(self):
        """
        Crea la sección de preferencias con checkboxes
        """
        # Checkbutton para notificaciones
        self.notifications_check = tk.Checkbutton(
            self.config_frame,
            text="🔔 Recibir notificaciones por email",
            variable=self.notifications_var,
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#FFFFFF',
            activebackground='#404040',
            selectcolor='#0078D4',
            anchor='w'
        )
        self.notifications_check.pack(fill='x', pady=2)
        
        # Checkbutton para newsletter
        self.newsletter_check = tk.Checkbutton(
            self.config_frame,
            text="📧 Suscribirse al boletín informativo",
            variable=self.newsletter_var,
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#FFFFFF',
            activebackground='#404040',
            selectcolor='#0078D4',
            anchor='w'
        )
        self.newsletter_check.pack(fill='x', pady=2)
        
        # Checkbutton para términos
        self.terms_check = tk.Checkbutton(
            self.config_frame,
            text="📋 Acepto los términos y condiciones",
            variable=self.terms_var,
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#F44336',
            activebackground='#404040',
            selectcolor='#F44336',
            anchor='w'
        )
        self.terms_check.pack(fill='x', pady=2)
        
        # Checkbutton para respaldos
        self.backup_check = tk.Checkbutton(
            self.config_frame,
            text="💾 Crear respaldos automáticos",
            variable=self.backup_var,
            font=("Arial", 10),
            bg='#2D2D30',
            fg='#FFFFFF',
            activebackground='#404040',
            selectcolor='#4CAF50',
            anchor='w'
        )
        self.backup_check.pack(fill='x', pady=2)
        
    def create_theme_selection(self):
        """
        Crea la sección de selección de tema
        """
        # Frame para tema
        theme_frame = tk.LabelFrame(
            self.config_frame,
            text="🎨 Tema de la aplicación",
            font=("Arial", 10, "bold"),
            bg='#2D2D30',
            fg='#FFFFFF',
            padx=10,
            pady=5
        )
        theme_frame.pack(fill='x', pady=(10, 0))
        
        # Container para radiobuttons
        themes_container = tk.Frame(theme_frame, bg='#2D2D30')
        themes_container.pack(fill='x')
        
        # Radiobutton tema claro
        tk.Radiobutton(
            themes_container,
            text="☀️ Claro",
            variable=self.theme_var,
            value="claro",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#FFFFFF',
            activebackground='#404040',
            selectcolor='#FFA500'
        ).pack(side='left', padx=(0, 20))
        
        # Radiobutton tema oscuro
        tk.Radiobutton(
            themes_container,
            text="🌙 Oscuro",
            variable=self.theme_var,
            value="oscuro",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#FFFFFF',
            activebackground='#404040',
            selectcolor='#6C757D'
        ).pack(side='left', padx=(0, 20))
        
        # Radiobutton tema colorido
        tk.Radiobutton(
            themes_container,
            text="🌈 Colorido",
            variable=self.theme_var,
            value="colorido",
            font=("Arial", 9),
            bg='#2D2D30',
            fg='#FFFFFF',
            activebackground='#404040',
            selectcolor='#9C27B0'
        ).pack(side='left')
        
    def get_configuration(self):
        """
        Obtiene la configuración actual
        
        Returns:
            dict: Diccionario con la configuración actual
        """
        return {
            'notifications': self.notifications_var.get(),
            'newsletter': self.newsletter_var.get(),
            'terms_accepted': self.terms_var.get(),
            'auto_backup': self.backup_var.get(),
            'theme': self.theme_var.get()
        }
        
    def set_configuration(self, config):
        """
        Establece la configuración
        
        Args:
            config (dict): Diccionario con la configuración
        """
        self.notifications_var.set(config.get('notifications', True))
        self.newsletter_var.set(config.get('newsletter', False))
        self.terms_var.set(config.get('terms_accepted', False))
        self.backup_var.set(config.get('auto_backup', True))
        self.theme_var.set(config.get('theme', 'claro'))
        
    def on_setting_changed(self, *args):
        """
        Maneja el cambio en cualquier configuración
        """
        if self.on_config_changed:
            self.on_config_changed(self.get_configuration())
            
    def validate_configuration(self):
        """
        Valida que la configuración sea consistente
        
        Returns:
            bool: True si la configuración es válida
        """
        config = self.get_configuration()
        
        # Verificar que se hayan aceptado los términos si se requiere
        if config['notifications'] and not config['terms_accepted']:
            messagebox.showwarning(
                "Términos requeridos",
                "Debe aceptar los términos y condiciones para recibir notificaciones"
            )
            return False
            
        return True
        
    def reset_to_defaults(self):
        """
        Restaura la configuración a valores por defecto
        """
        self.notifications_var.set(True)
        self.newsletter_var.set(False)
        self.terms_var.set(False)
        self.backup_var.set(True)
        self.theme_var.set("claro")
        
    def apply_theme(self, theme_name):
        """
        Aplica un tema específico (placeholder)
        
        Args:
            theme_name (str): Nombre del tema a aplicar
        """
        # Aquí se implementaría la lógica para cambiar el tema
        print(f"Aplicando tema: {theme_name}")
        
    def export_config(self):
        """
        Exporta la configuración actual (placeholder)
        
        Returns:
            str: Configuración en formato texto
        """
        config = self.get_configuration()
        config_text = "Configuración actual:\n\n"
        
        for key, value in config.items():
            config_text += f"{key}: {value}\n"
            
        return config_text
        
    def import_config(self, config_dict):
        """
        Importa configuración desde un diccionario
        
        Args:
            config_dict (dict): Configuración a importar
        """
        try:
            self.set_configuration(config_dict)
            messagebox.showinfo("Éxito", "Configuración importada correctamente")
        except Exception as e:
            messagebox.showerror("Error", f"Error al importar configuración: {str(e)}")
            
    def is_terms_accepted(self):
        """
        Verifica si se han aceptado los términos
        
        Returns:
            bool: True si se han aceptado los términos
        """
        return self.terms_var.get()
