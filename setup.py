#!/usr/bin/env python3
"""
Script de configuración e instalación del Sistema de Gestión Educativa
Automatiza la instalación de dependencias y verificación del sistema
"""

import os
import sys
import subprocess
import platform

def print_header(title):
    """Imprime un encabezado con formato"""
    print("\n" + "=" * 60)
    print(f"🚀 {title}")
    print("=" * 60)

def print_step(step_number, description):
    """Imprime un paso numerado"""
    print(f"\n📋 Paso {step_number}: {description}")

def run_command(command, description):
    """Ejecuta un comando y maneja errores"""
    print(f"   Ejecutando: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"   ✅ {description} - Exitoso")
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ {description} - Error: {e}")
        if e.stdout:
            print(f"   Stdout: {e.stdout}")
        if e.stderr:
            print(f"   Stderr: {e.stderr}")
        return False

def check_python_version():
    """Verifica la versión de Python"""
    print_step(1, "Verificando versión de Python")
    
    version = sys.version_info
    print(f"   Python detectado: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("   ❌ Python 3.7 o superior es requerido")
        return False
    
    print("   ✅ Versión de Python compatible")
    return True

def setup_virtual_environment():
    """Configura el entorno virtual"""
    print_step(2, "Configurando entorno virtual")
    
    venv_path = "venv"
    
    if os.path.exists(venv_path):
        print("   ⚠️  Entorno virtual ya existe, omitiendo creación...")
        return True
    
    # Crear entorno virtual
    if not run_command(f"{sys.executable} -m venv {venv_path}", "Creando entorno virtual"):
        return False
    
    return True

def install_dependencies():
    """Instala las dependencias necesarias"""
    print_step(3, "Instalando dependencias")
    
    # Determinar comando de activación según el OS
    if platform.system() == "Windows":
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    # Lista de dependencias principales
    dependencies = [
        "reportlab>=4.0.4",
        "pandas>=2.0.3", 
        "openpyxl>=3.1.2",
        "pillow>=10.0.0"
    ]
    
    # Instalar cada dependencia
    for dep in dependencies:
        if not run_command(f"{pip_cmd} install {dep}", f"Instalando {dep}"):
            print(f"   ⚠️  No se pudo instalar {dep}, continuando...")
    
    print("   ✅ Instalación de dependencias completada")
    return True

def verify_installation():
    """Verifica que la instalación sea correcta"""
    print_step(4, "Verificando instalación")
    
    # Determinar comando Python en el entorno virtual
    if platform.system() == "Windows":
        python_cmd = "venv\\Scripts\\python"
    else:
        python_cmd = "venv/bin/python"
    
    # Ejecutar script de prueba
    if not run_command(f"{python_cmd} test_database.py", "Ejecutando pruebas del sistema"):
        return False
    
    return True

def create_launcher_scripts():
    """Crea scripts de lanzamiento para facilitar el uso"""
    print_step(5, "Creando scripts de lanzamiento")
    
    # Determinar extensión y comando según el OS
    if platform.system() == "Windows":
        python_cmd = "venv\\Scripts\\python"
        ext = ".bat"
        shebang = "@echo off\n"
    else:
        python_cmd = "venv/bin/python"
        ext = ".sh"
        shebang = "#!/bin/bash\n"
    
    scripts = {
        f"ejecutar_aplicacion{ext}": f"""{shebang}echo "🚀 Iniciando Sistema de Gestión Educativa..."
{python_cmd} main.py
""",
        f"ejemplo_crud_simple{ext}": f"""{shebang}echo "🧪 Iniciando ejemplo de CRUD simple..."
{python_cmd} examples/10_crud_simple.py
""",
        f"ejemplo_conceptos_bd{ext}": f"""{shebang}echo "📚 Iniciando demostración de conceptos de BD..."
{python_cmd} examples/09_database_concepts.py
""",
        f"probar_sistema{ext}": f"""{shebang}echo "🧪 Ejecutando pruebas del sistema..."
{python_cmd} test_database.py
"""
    }
    
    for filename, content in scripts.items():
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Hacer ejecutable en sistemas Unix
            if not platform.system() == "Windows":
                os.chmod(filename, 0o755)
            
            print(f"   ✅ Creado: {filename}")
        except Exception as e:
            print(f"   ❌ Error creando {filename}: {e}")
    
    return True

def show_usage_instructions():
    """Muestra las instrucciones de uso"""
    print_header("INSTALACIÓN COMPLETADA")
    
    print("✨ ¡El Sistema de Gestión Educativa está listo para usar!")
    
    print("\n🎯 FORMAS DE EJECUTAR LA APLICACIÓN:")
    
    if platform.system() == "Windows":
        print("   • Aplicación principal:      ejecutar_aplicacion.bat")
        print("   • CRUD Simple:               ejemplo_crud_simple.bat")
        print("   • Demo de conceptos BD:      ejemplo_conceptos_bd.bat")
        print("   • Probar sistema:            probar_sistema.bat")
        print("\n   O manualmente:")
        print("   • venv\\Scripts\\python main.py")
    else:
        print("   • Aplicación principal:      ./ejecutar_aplicacion.sh")
        print("   • CRUD Simple:               ./ejemplo_crud_simple.sh")
        print("   • Demo de conceptos BD:      ./ejemplo_conceptos_bd.sh")
        print("   • Probar sistema:            ./probar_sistema.sh")
        print("\n   O manualmente:")
        print("   • source venv/bin/activate && python main.py")
    
    print("\n📚 CONCEPTOS DE BASE DE DATOS INCLUIDOS:")
    print("   ✅ ¿Qué es una Base de Datos?")
    print("   ✅ El 'Control de Datos'")
    print("   ✅ Integridad Referencial")
    print("   ✅ Navegar a Través de un Conjunto de Registros")
    print("   ✅ Objetos de Acceso a Datos (DAO)")
    print("   ✅ Generación de Reportes Usando 'Data Report'")
    print("   ✅ Manipulación de Datos (Operaciones CRUD con SQL)")
    print("      • Añadir Nuevos Registros (INSERT)")
    print("      • Editar un Registro (UPDATE)")
    print("      • Borrar un Registro (DELETE)")  
    print("      • Localizar un Registro (SELECT ... WHERE)")
    print("   ✅ Uso de SQL (Structured Query Language)")
    
    print("\n📂 ARCHIVOS IMPORTANTES:")
    print("   • src/database/README.md - Documentación completa del módulo de BD")
    print("   • examples/ - Ejemplos prácticos paso a paso")
    print("   • reports/ - Reportes generados automáticamente")
    print("   • school_database.db - Base de datos SQLite principal")
    
    print("\n🆘 SOPORTE:")
    print("   • Ejecuta './probar_sistema.sh' para verificar el funcionamiento")
    print("   • Revisa la documentación en src/database/README.md")
    print("   • Explora los ejemplos en la carpeta examples/")

def main():
    """Función principal de configuración"""
    print_header("CONFIGURACIÓN DEL SISTEMA DE GESTIÓN EDUCATIVA")
    
    print("🎓 Este script configurará automáticamente:")
    print("   • Entorno virtual de Python")
    print("   • Dependencias necesarias (ReportLab, Pandas, etc.)")
    print("   • Base de datos SQLite con datos de ejemplo")
    print("   • Scripts de lanzamiento")
    print("   • Verificación del sistema")
    
    # Verificar Python
    if not check_python_version():
        print("\n❌ Instalación abortada - Versión de Python incompatible")
        return False
    
    # Configurar entorno virtual
    if not setup_virtual_environment():
        print("\n❌ Instalación abortada - Error configurando entorno virtual")
        return False
    
    # Instalar dependencias
    if not install_dependencies():
        print("\n❌ Instalación abortada - Error instalando dependencias")
        return False
    
    # Verificar instalación
    if not verify_installation():
        print("\n❌ Instalación abortada - Falló la verificación del sistema")
        return False
    
    # Crear scripts de lanzamiento
    create_launcher_scripts()
    
    # Mostrar instrucciones
    show_usage_instructions()
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        if not success:
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Instalación interrumpida por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado durante la instalación: {e}")
        sys.exit(1)
