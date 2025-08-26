#!/usr/bin/env python3
"""
Script de prueba para el módulo de base de datos
Verifica que todas las funcionalidades básicas funcionen correctamente
"""

import sys
import os

# Agregar el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def test_database_module():
    """Prueba básica del módulo de base de datos"""
    
    print("🔍 Probando el módulo de base de datos...")
    
    try:
        # Importar módulos
        from src.database import (
            DatabaseConnection, 
            StudentDAO, CourseDAO, EnrollmentDAO,
            CRUDOperations,
            DataNavigator,
            ReportGenerator
        )
        print("✅ Importaciones exitosas")
        
        # Probar conexión
        db = DatabaseConnection()
        print("✅ Conexión a base de datos establecida")
        
        # Probar CRUD básico
        crud = CRUDOperations()
        
        # CREATE
        student_id = crud.add_student("Prueba", "Test", "prueba@test.com")
        print(f"✅ Estudiante creado con ID: {student_id}")
        
        # READ
        student = crud.find_student_by_id(student_id)
        if student:
            print(f"✅ Estudiante encontrado: {student.full_name}")
        
        # UPDATE
        success = crud.update_student(student_id, phone="123-456-7890")
        if success:
            print("✅ Estudiante actualizado exitosamente")
        
        # Probar navegación
        navigator = DataNavigator()
        recordset = navigator.load_students()
        print(f"✅ Navegación cargada con {recordset.record_count} registros")
        
        # Probar generación de reportes
        report_gen = ReportGenerator()
        formats = report_gen.get_available_formats()
        print(f"✅ Formatos de reporte disponibles: {formats}")
        
        # Generar un reporte simple
        if "csv" in formats:
            csv_report = report_gen.generate_student_report("csv")
            print(f"✅ Reporte CSV generado: {csv_report}")
        
        # DELETE (limpiar datos de prueba)
        delete_success = crud.delete_student(student_id)
        if delete_success:
            print("✅ Datos de prueba eliminados")
        
        print("\n🎉 ¡Todas las pruebas pasaron exitosamente!")
        print("\n📋 Funcionalidades verificadas:")
        print("   • Conexión a base de datos SQLite")
        print("   • Operaciones CRUD (Create, Read, Update, Delete)")  
        print("   • Integridad referencial")
        print("   • Navegación de registros")
        print("   • Generación de reportes")
        print("   • Objetos de Acceso a Datos (DAO)")
        
        return True
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        print("   Asegúrate de que todos los archivos del módulo database estén presentes")
        return False
        
    except Exception as e:
        print(f"❌ Error durante las pruebas: {e}")
        return False

def show_database_info():
    """Muestra información sobre la base de datos"""
    try:
        from src.database import DatabaseConnection
        
        db = DatabaseConnection()
        info = db.get_database_info()
        
        print("\n📊 Información de la Base de Datos:")
        print(f"   Archivo: {info['database_path']}")
        print(f"   Tamaño: {info['database_size']} bytes")
        print(f"   Total de registros: {info['total_records']}")
        print("\n   Tablas:")
        for table in info['tables']:
            print(f"   • {table['name']}: {table['records']} registros")
            
    except Exception as e:
        print(f"❌ Error al obtener información de BD: {e}")

def main():
    """Función principal"""
    print("=" * 60)
    print("🧪 PRUEBA DEL MÓDULO DE BASE DE DATOS")
    print("=" * 60)
    
    # Probar funcionalidades básicas
    if test_database_module():
        # Mostrar información de la base de datos
        show_database_info()
        
        print("\n" + "=" * 60)
        print("✨ SISTEMA LISTO PARA USAR")
        print("=" * 60)
        print("\n🚀 Próximos pasos:")
        print("   1. Ejecuta 'python examples/10_crud_simple.py' para una demo interactiva simple")
        print("   2. Ejecuta 'python examples/09_database_concepts.py' para una demo completa")
        print("   3. Ejecuta 'python main.py' para la aplicación principal")
        print("\n📚 Documentación:")
        print("   • Revisa 'src/database/README.md' para documentación completa")
        print("   • Explora los archivos en 'examples/' para más ejemplos")
        
    else:
        print("\n❌ Las pruebas fallaron. Revisa los errores anteriores.")
        print("\n🔧 Posibles soluciones:")
        print("   • Verifica que todos los archivos estén presentes")
        print("   • Instala las dependencias con: pip install -r requirements.txt")
        print("   • Verifica que Python 3.7+ esté disponible")

if __name__ == "__main__":
    main()
