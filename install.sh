#!/bin/bash

echo "🚀 INSTALACIÓN DEL SISTEMA DE GESTIÓN EDUCATIVA"
echo "================================================"

# Verificar Python
echo "📋 Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado. Por favor instala Python 3.7 o superior."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Python $PYTHON_VERSION encontrado"

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "📋 Creando entorno virtual..."
    python3 -m venv venv
    echo "✅ Entorno virtual creado"
else
    echo "ℹ️  Entorno virtual ya existe"
fi

# Activar entorno virtual e instalar dependencias
echo "📋 Instalando dependencias..."
source venv/bin/activate

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias principales
pip install reportlab>=4.0.4
pip install pandas>=2.0.3
pip install openpyxl>=3.1.2
pip install pillow>=10.0.0

echo "✅ Dependencias instaladas exitosamente"

# Probar instalación
echo "📋 Probando instalación..."
python3 test_database.py

echo ""
echo "🎉 ¡INSTALACIÓN COMPLETADA!"
echo "=========================="
echo ""
echo "🎯 Para usar el sistema:"
echo "  ./ejecutar_aplicacion.sh     - Aplicación principal"
echo "  ./ejemplo_crud_simple.sh     - Ejemplo CRUD básico"  
echo "  ./ejemplo_conceptos_bd.sh    - Demo completa de BD"
echo "  ./probar_sistema.sh          - Verificar funcionamiento"
echo ""
echo "📚 O manualmente:"
echo "  source venv/bin/activate"
echo "  python3 main.py"
echo ""
