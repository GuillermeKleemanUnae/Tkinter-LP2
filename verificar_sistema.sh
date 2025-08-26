#!/bin/bash

echo "🔧 VERIFICACIÓN COMPLETA DEL SISTEMA"
echo "==================================="

echo ""
echo "📋 1. Verificando Python y entorno virtual..."
if [ ! -d "venv" ]; then
    echo "❌ Entorno virtual no encontrado. Ejecuta: ./install.sh"
    exit 1
fi

source venv/bin/activate

echo "✅ Entorno virtual activado"

echo ""
echo "📋 2. Verificando importaciones..."
python3 -c "
try:
    from src.database import DatabaseConnection, NavigationDirection, SortOrder
    from src.database import StudentDAO, CRUDOperations, ReportGenerator
    print('✅ Todas las importaciones funcionan correctamente')
except ImportError as e:
    print(f'❌ Error de importación: {e}')
    exit(1)
"

echo ""
echo "📋 3. Ejecutando pruebas completas..."
python3 test_database.py

echo ""
echo "📋 4. Verificando scripts de ejecución..."
if [ -x "./ejecutar_aplicacion.sh" ]; then
    echo "✅ Script ejecutar_aplicacion.sh está listo"
else
    echo "❌ Script ejecutar_aplicacion.sh no es ejecutable"
fi

if [ -x "./ejemplo_conceptos_bd.sh" ]; then
    echo "✅ Script ejemplo_conceptos_bd.sh está listo"
else
    echo "❌ Script ejemplo_conceptos_bd.sh no es ejecutable"
fi

if [ -x "./ejemplo_crud_simple.sh" ]; then
    echo "✅ Script ejemplo_crud_simple.sh está listo"
else
    echo "❌ Script ejemplo_crud_simple.sh no es ejecutable"
fi

echo ""
echo "📋 5. Verificando archivos importantes..."
archivos_importantes=("main.py" "src/database/connection.py" "src/database/dao.py" "examples/09_database_concepts.py" "school_database.db")

for archivo in "${archivos_importantes[@]}"; do
    if [ -f "$archivo" ]; then
        echo "✅ $archivo existe"
    else
        echo "❌ $archivo NO encontrado"
    fi
done

echo ""
echo "🎉 VERIFICACIÓN COMPLETADA"
echo "========================"
echo ""
echo "🚀 Para usar el sistema:"
echo "   ./ejecutar_aplicacion.sh     - Aplicación principal"
echo "   ./ejemplo_conceptos_bd.sh    - Demo completa de BD"
echo "   ./ejemplo_crud_simple.sh     - CRUD básico"
echo ""
echo "📚 Documentación:"
echo "   QUICKSTART.md                - Guía rápida"
echo "   README.md                    - Documentación completa"
echo "   src/database/README.md       - Documentación técnica"
echo ""
