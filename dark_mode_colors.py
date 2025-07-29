#!/usr/bin/env python3
"""
Configuración de Colores para Modo Oscuro macOS
==============================================

Este archivo define los colores optimizados para el modo oscuro de macOS
siguiendo las guías de diseño de Apple y las mejores prácticas de UI/UX.

Paleta de colores inspirada en:
- macOS Big Sur Dark Mode
- Visual Studio Code Dark Theme
- Material Design Dark Theme

Autor: Sistema de Gestión Estudiantil
Fecha: 2025
"""

# COLORES PRINCIPALES MODO OSCURO
# ===============================

# Colores de fondo
DARK_BG_PRIMARY = '#1E1E1E'      # Fondo principal muy oscuro
DARK_BG_SECONDARY = '#2D2D30'    # Fondo secundario (paneles)
DARK_BG_TERTIARY = '#3C3C3C'     # Fondo terciario (inputs)
DARK_BG_ACCENT = '#404040'       # Fondo accent (hover states)

# Colores de texto
DARK_TEXT_PRIMARY = '#FFFFFF'    # Texto principal blanco
DARK_TEXT_SECONDARY = '#B3B3B3'  # Texto secundario gris claro
DARK_TEXT_DISABLED = '#6C757D'   # Texto deshabilitado

# Colores de acento
DARK_ACCENT_BLUE = '#0078D4'     # Azul Microsoft (primary)
DARK_ACCENT_GREEN = '#4CAF50'    # Verde Material (success)
DARK_ACCENT_RED = '#F44336'      # Rojo Material (danger)
DARK_ACCENT_PURPLE = '#9C27B0'   # Morado Material (info)
DARK_ACCENT_ORANGE = '#FFA500'   # Naranja (warning)
DARK_ACCENT_GRAY = '#6C757D'     # Gris (neutral)

# Estados interactivos
DARK_HOVER_BLUE = '#106EBE'      # Azul hover
DARK_HOVER_GREEN = '#45A049'     # Verde hover
DARK_HOVER_RED = '#DA190B'       # Rojo hover
DARK_HOVER_PURPLE = '#7B1FA2'    # Morado hover
DARK_HOVER_GRAY = '#5A6268'      # Gris hover

# Colores de estado
DARK_STATUS_ACTIVE = '#4CAF50'   # Estado activo
DARK_STATUS_INACTIVE = '#F44336' # Estado inactivo
DARK_STATUS_GRADUATED = '#9C27B0' # Estado graduado

def get_dark_color_scheme():
    """
    Retorna el esquema de colores completo para modo oscuro
    
    Returns:
        dict: Diccionario con todos los colores organizados por categoría
    """
    return {
        'backgrounds': {
            'primary': DARK_BG_PRIMARY,
            'secondary': DARK_BG_SECONDARY,
            'tertiary': DARK_BG_TERTIARY,
            'accent': DARK_BG_ACCENT
        },
        'text': {
            'primary': DARK_TEXT_PRIMARY,
            'secondary': DARK_TEXT_SECONDARY,
            'disabled': DARK_TEXT_DISABLED
        },
        'accents': {
            'blue': DARK_ACCENT_BLUE,
            'green': DARK_ACCENT_GREEN,
            'red': DARK_ACCENT_RED,
            'purple': DARK_ACCENT_PURPLE,
            'orange': DARK_ACCENT_ORANGE,
            'gray': DARK_ACCENT_GRAY
        },
        'hovers': {
            'blue': DARK_HOVER_BLUE,
            'green': DARK_HOVER_GREEN,
            'red': DARK_HOVER_RED,
            'purple': DARK_HOVER_PURPLE,
            'gray': DARK_HOVER_GRAY
        },
        'status': {
            'active': DARK_STATUS_ACTIVE,
            'inactive': DARK_STATUS_INACTIVE,
            'graduated': DARK_STATUS_GRADUATED
        }
    }

def print_color_palette():
    """
    Imprime la paleta de colores con ejemplos visuales
    """
    print("🎨 PALETA DE COLORES MODO OSCURO macOS")
    print("=" * 50)
    
    colors = get_dark_color_scheme()
    
    print("\n📱 FONDOS:")
    for name, color in colors['backgrounds'].items():
        print(f"   {name.capitalize():12}: {color}")
    
    print("\n📝 TEXTOS:")
    for name, color in colors['text'].items():
        print(f"   {name.capitalize():12}: {color}")
    
    print("\n🎯 ACENTOS:")
    for name, color in colors['accents'].items():
        print(f"   {name.capitalize():12}: {color}")
    
    print("\n⚡ INTERACCIONES:")
    for name, color in colors['hovers'].items():
        print(f"   {name.capitalize():12}: {color}")
    
    print("\n📊 ESTADOS:")
    for name, color in colors['status'].items():
        print(f"   {name.capitalize():12}: {color}")
    
    print("\n✅ BENEFICIOS DEL ESQUEMA:")
    print("   • 🌙 Optimizado para modo oscuro macOS")
    print("   • 👁️  Reduce fatiga visual en ambientes oscuros")
    print("   • 🎨 Mantiene excelente contraste y legibilidad")
    print("   • 🔋 Ahorra batería en pantallas OLED")
    print("   • 📱 Sigue las guías de diseño de Apple")
    print("   • ♿ Cumple estándares de accesibilidad WCAG")
    
    print("\n🎯 APLICACIÓN EN COMPONENTES:")
    print("   • MainWindow: Fondo principal #1E1E1E")
    print("   • LabelFrames: Fondo secundario #2D2D30") 
    print("   • Entry widgets: Fondo terciario #3C3C3C")
    print("   • Botones: Colores de acento según función")
    print("   • Texto: Blanco principal #FFFFFF")
    print("   • Selecciones: Azul Microsoft #0078D4")

if __name__ == "__main__":
    print_color_palette()
