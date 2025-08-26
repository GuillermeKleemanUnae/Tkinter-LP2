# Sistema de Gestión Educativa - Instalación Rápida

¡Bienvenido al Sistema de Gestión Educativa! Este proyecto implementa todos los conceptos fundamentales de bases de datos de manera práctica y educativa.

## 🚀 Instalación Automática

Para instalar y configurar el sistema automáticamente, ejecuta:

```bash
python3 setup.py
```

Este script:
- ✅ Verifica tu versión de Python (requiere 3.7+)
- ✅ Crea un entorno virtual automáticamente
- ✅ Instala todas las dependencias necesarias
- ✅ Verifica que todo funcione correctamente
- ✅ Crea scripts de lanzamiento para facilitar el uso

## 📚 Conceptos de Base de Datos Implementados

El proyecto incluye implementaciones completas de:

### 1. ¿Qué es una Base de Datos?
- Implementación práctica con SQLite
- Demostración interactiva de conceptos fundamentales

### 2. El 'Control de Datos'
- Validación de datos automática
- Control de tipos y formatos
- Manejo de errores y excepciones

### 3. Integridad Referencial
- Claves foráneas con restricciones CASCADE
- Validación automática de relaciones
- Mantenimiento de consistencia de datos

### 4. Navegar a Través de un Conjunto de Registros
- Sistema de navegación completo (First, Previous, Next, Last)
- Filtrado y ordenamiento de registros
- Búsqueda avanzada

### 5. Objetos de Acceso a Datos (DAO)
- Patrón DAO completo implementado
- Separación clara entre lógica de negocio y acceso a datos
- DAOs para Student, Course, Enrollment

### 6. Generación de Reportes Usando 'Data Report'
- Reportes en múltiples formatos (PDF, Excel, CSV, HTML)
- Reportes estadísticos automáticos
- Exportación de transcripciones académicas

### 7. Manipulación de Datos (Operaciones CRUD con SQL)
- **Añadir Nuevos Registros (INSERT)**: Formularios intuitivos con validación
- **Editar un Registro (UPDATE)**: Edición en línea con confirmación
- **Borrar un Registro (DELETE)**: Eliminación segura con confirmación
- **Localizar un Registro (SELECT ... WHERE)**: Búsqueda avanzada y filtros

### 8. Uso de SQL (Structured Query Language)
- Ejemplos prácticos de todas las operaciones SQL
- Visualización en tiempo real de consultas ejecutadas
- SQL builder integrado para aprendizaje

## 🎯 Formas de Usar el Sistema

### Después de la instalación automática:

**En macOS/Linux:**
```bash
# Aplicación principal completa
./ejecutar_aplicacion.sh

# Ejemplo simple de CRUD
./ejemplo_crud_simple.sh

# Demostración interactiva de conceptos de BD
./ejemplo_conceptos_bd.sh

# Verificar que todo funcione
./probar_sistema.sh
```

**En Windows:**
```bash
# Aplicación principal completa
ejecutar_aplicacion.bat

# Ejemplo simple de CRUD
ejemplo_crud_simple.bat

# Demostración interactiva de conceptos de BD
ejemplo_conceptos_bd.bat

# Verificar que todo funcione
probar_sistema.bat
```

### Instalación manual (si prefieres):

```bash
# 1. Crear entorno virtual
python3 -m venv venv

# 2. Activar entorno virtual
source venv/bin/activate  # En macOS/Linux
# o
venv\Scripts\activate     # En Windows

# 3. Instalar dependencias
pip install reportlab pandas openpyxl pillow

# 4. Ejecutar aplicación
python main.py
```

## 📁 Estructura del Proyecto

```
LP2/
├── main.py                    # Aplicación principal
├── setup.py                   # Script de instalación automática
├── test_database.py           # Pruebas del sistema
├── src/
│   └── database/              # Módulo completo de base de datos
│       ├── connection.py      # Gestión de conexiones
│       ├── dao.py            # Objetos de acceso a datos
│       ├── crud_operations.py # Operaciones CRUD
│       ├── data_navigator.py  # Navegación de registros
│       ├── report_generator.py # Generador de reportes
│       └── README.md         # Documentación técnica detallada
├── examples/
│   ├── 09_database_concepts.py # Demo interactiva completa
│   └── 10_crud_simple.py      # Ejemplo CRUD básico
└── reports/                   # Reportes generados automáticamente
```

## 🛠️ Características Técnicas

- **Base de Datos**: SQLite con integridad referencial completa
- **Interfaz**: Tkinter con diseño moderno y responsivo
- **Reportes**: PDF (ReportLab), Excel (Pandas/OpenPyxl), CSV, HTML
- **Arquitectura**: Patrón MVC con DAOs, Singleton, Factory
- **Validación**: Sistema completo de validación de datos
- **Auditoría**: Log automático de todas las operaciones
- **Navegación**: Sistema completo de navegación de registros

## 🎓 Propósito Educativo

Este proyecto fue diseñado específicamente para enseñar conceptos de bases de datos de manera práctica. Cada concepto incluye:

- ✅ Implementación técnica completa
- ✅ Ejemplos interactivos
- ✅ Documentación detallada
- ✅ Demostraciones paso a paso
- ✅ Código comentado y explicado

## 📊 Datos de Ejemplo

El sistema incluye datos de ejemplo listos para usar:
- Estudiantes con información completa
- Cursos de diferentes materias
- Inscripciones con calificaciones
- Historial de auditoría

## 🆘 Soporte y Resolución de Problemas

1. **Ejecuta el script de pruebas**: `python3 test_database.py`
2. **Revisa la documentación técnica**: `src/database/README.md`
3. **Explora los ejemplos**: Carpeta `examples/`
4. **Verifica dependencias**: El script `setup.py` las instala automáticamente

## 🚀 ¡Comienza Ahora!

```bash
python3 setup.py
```

¡Y listo! En menos de 2 minutos tendrás un sistema completo de gestión educativa funcionando con todos los conceptos de bases de datos implementados.

---

*Desarrollado con 💙 para la educación en tecnología*
