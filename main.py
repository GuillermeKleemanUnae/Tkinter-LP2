#!/usr/bin/env python3
"""
Aplicación principal con Tkinter
Archivo de entrada del programa
"""

import tkinter as tk
from src.gui.main_window import MainWindow

def main():
    """
    Función principal que inicializa la aplicación
    """
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
