# Módulo de Base de Datos - Sistema Educativo

Este módulo implementa un sistema completo de gestión de bases de datos para un sistema educativo, cubriendo todos los conceptos fundamentales de bases de datos relacionales.

## 📚 Conceptos Implementados

### 1. ¿Qué es una Base de Datos?
Una base de datos es un sistema organizado para almacenar, recuperar, actualizar y eliminar información de manera eficiente. En este proyecto utilizamos SQLite como motor de base de datos.

### 2. El "Control de Datos"
Implementamos control de datos mediante:
- **Transacciones**: Operaciones que se ejecutan completamente o no se ejecutan
- **Integridad**: Validación de datos y reglas de negocio
- **Concurrencia**: Manejo seguro de acceso simultáneo
- **Auditoría**: Registro de todas las operaciones

### 3. Integridad Referencial
Garantizamos la consistencia entre tablas relacionadas:
- **Claves primarias**: Identificadores únicos para cada registro
- **Claves foráneas**: Referencias entre tablas
- **Restricciones**: Reglas que los datos deben cumplir
- **Cascada**: Acciones automáticas en modificaciones

### 4. Navegación a Través de un Conjunto de Registros
Sistema de navegación que permite:
- Moverse por registros (Primero, Anterior, Siguiente, Último)
- Filtrar y ordenar datos
- Mantener estado de posición
- Búsquedas avanzadas

### 5. Objetos de Acceso a Datos (DAO)
Patrón de diseño que separa la lógica de datos:
- **StudentDAO**: Operaciones con estudiantes
- **CourseDAO**: Operaciones con cursos
- **EnrollmentDAO**: Operaciones con inscripciones

### 6. Generación de Reportes
Sistema completo de reportes en múltiples formatos:
- **PDF**: Reportes profesionales con ReportLab
- **Excel**: Hojas de cálculo con pandas
- **CSV**: Datos en formato de texto separado por comas
- **HTML**: Reportes web visuales

### 7. Manipulación de Datos (CRUD)
Operaciones básicas de base de datos:
- **CREATE**: Insertar nuevos registros
- **READ**: Consultar registros existentes
- **UPDATE**: Actualizar registros
- **DELETE**: Eliminar registros

## 🗂️ Estructura del Módulo

```
src/database/
├── __init__.py              # Inicialización del módulo
├── connection.py            # Conexión y configuración de BD
├── dao.py                   # Objetos de Acceso a Datos
├── crud_operations.py       # Operaciones CRUD unificadas
├── data_navigator.py        # Navegación de registros
└── report_generator.py      # Generación de reportes
```

## 🚀 Inicio Rápido

### Instalación de Dependencias

```bash
# Instalar dependencias necesarias
pip install -r requirements.txt

# Dependencias principales:
# - sqlite3 (incluido con Python)
# - reportlab (para reportes PDF)
# - pandas (para reportes Excel)
# - openpyxl (para archivos Excel)
```

### Uso Básico

```python
from src.database import DatabaseConnection, StudentDAO, CRUDOperations

# Conectar a la base de datos
db = DatabaseConnection()

# Usar DAO para operaciones específicas
student_dao = StudentDAO()
students = student_dao.get_all()

# Usar CRUD para operaciones unificadas
crud = CRUDOperations()
student_id = crud.add_student("Juan", "Pérez", "juan@email.com")
```

## 🎯 Ejemplos Prácticos

### Ejemplo 1: CRUD Completo
```bash
python examples/09_database_concepts.py
```
Demostración interactiva de todos los conceptos de base de datos.

### Ejemplo 2: CRUD Simple
```bash
python examples/10_crud_simple.py
```
Implementación simple y directa de operaciones CRUD.

## 📊 Esquema de Base de Datos

### Tabla: students
```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    birth_date DATE,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    status TEXT CHECK(status IN ('active', 'inactive', 'graduated')) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tabla: courses
```sql
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    code TEXT UNIQUE NOT NULL,
    description TEXT,
    credits INTEGER NOT NULL DEFAULT 3,
    semester TEXT,
    instructor TEXT,
    capacity INTEGER DEFAULT 30,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tabla: enrollments
```sql
CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    grade REAL CHECK(grade >= 0 AND grade <= 100),
    status TEXT CHECK(status IN ('enrolled', 'completed', 'dropped')) DEFAULT 'enrolled',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
    UNIQUE(student_id, course_id)
);
```

## 🔧 Operaciones CRUD Detalladas

### CREATE - Añadir Nuevos Registros
```python
# Agregar estudiante
student_id = crud.add_student(
    first_name="María",
    last_name="García", 
    email="maria@email.com",
    phone="123-456-7890"
)

# SQL ejecutado:
# INSERT INTO students (first_name, last_name, email, phone, status) 
# VALUES ('María', 'García', 'maria@email.com', '123-456-7890', 'active')
```

### READ - Localizar Registros
```python
# Buscar por ID
student = crud.find_student_by_id(1)

# Buscar por email
student = crud.find_student_by_email("maria@email.com")

# Búsqueda por nombre (parcial)
students = crud.find_students_by_name("María")

# SQL ejecutado:
# SELECT * FROM students WHERE id = 1
# SELECT * FROM students WHERE email = 'maria@email.com'
# SELECT * FROM students WHERE first_name LIKE '%María%' OR last_name LIKE '%María%'
```

### UPDATE - Editar Registros
```python
# Actualizar email de un estudiante
success = crud.update_student(1, email="nuevo_email@email.com")

# Actualizar múltiples campos
success = crud.update_student(1, 
    phone="999-888-7777",
    status="inactive"
)

# SQL ejecutado:
# UPDATE students SET email = 'nuevo_email@email.com', updated_at = CURRENT_TIMESTAMP WHERE id = 1
```

### DELETE - Borrar Registros
```python
# Eliminar estudiante (y sus inscripciones automáticamente)
success = crud.delete_student(1)

# SQL ejecutado:
# DELETE FROM students WHERE id = 1
# (Las inscripciones se eliminan automáticamente por CASCADE)
```

## 🧭 Navegación de Datos

```python
from src.database import DataNavigator, NavigationDirection

navigator = DataNavigator()

# Cargar datos
navigator.load_students()

# Navegar
navigator.navigate_students(NavigationDirection.FIRST)
navigator.navigate_students(NavigationDirection.NEXT)
navigator.navigate_students(NavigationDirection.PREVIOUS)
navigator.navigate_students(NavigationDirection.LAST)

# Filtrar y ordenar
navigator.load_students("active")  # Solo estudiantes activos
navigator.sort_students("name", SortOrder.ASC)
```

## 📈 Generación de Reportes

```python
from src.database import ReportGenerator

report_gen = ReportGenerator()

# Reporte de estudiantes en PDF
pdf_path = report_gen.generate_student_report("pdf", "active")

# Reporte de cursos en Excel  
excel_path = report_gen.generate_course_report("excel")

# Historial académico individual
transcript_path = report_gen.generate_student_transcript(1, "pdf")

# Reporte estadístico
stats_path = report_gen.generate_statistics_report("pdf")
```

## 🔒 Integridad Referencial

### Ejemplos de Restricciones

```python
# ❌ Error: Estudiante inexistente
try:
    crud.enroll_student(9999, 1)  # student_id no existe
except ValueError as e:
    print("Error: Estudiante o curso no válido")

# ❌ Error: Email duplicado
try:
    crud.add_student("Juan", "Nuevo", "juan@email.com")  # email ya existe
except ValueError as e:
    print("Error: El email ya existe en el sistema")

# ✅ Cascada: Eliminar estudiante elimina sus inscripciones
success = crud.delete_student(1)  # Elimina estudiante e inscripciones
```

## 📊 Consultas SQL Avanzadas

### Historial Académico Completo
```sql
SELECT 
    s.first_name,
    s.last_name,
    c.name as course_name,
    c.code as course_code,
    c.credits,
    e.grade,
    e.status,
    e.enrollment_date
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON e.course_id = c.id
WHERE s.id = ?
ORDER BY e.enrollment_date
```

### Estadísticas por Curso
```sql
SELECT 
    c.name,
    c.code,
    COUNT(e.id) as total_enrollments,
    AVG(e.grade) as average_grade,
    COUNT(CASE WHEN e.status = 'completed' THEN 1 END) as completed_count
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
GROUP BY c.id, c.name, c.code
ORDER BY total_enrollments DESC
```

## 🛠️ Configuración Avanzada

### Variables de Entorno
```bash
# Configurar ruta de base de datos
export DB_PATH="/ruta/personalizada/database.db"

# Directorio de reportes
export REPORTS_DIR="/ruta/reportes"
```

### Configuración de Conexión
```python
# Configurar timeout de conexión
db = DatabaseConnection()
db.connect().execute("PRAGMA busy_timeout = 30000")

# Habilitar WAL mode para mejor concurrencia
db.connect().execute("PRAGMA journal_mode = WAL")
```

## 🧪 Testing

```bash
# Ejecutar pruebas unitarias
python -m pytest tests/test_student.py
python -m pytest tests/test_validators.py

# Ejecutar todas las pruebas
python -m pytest tests/
```

## 📝 Logs y Auditoría

Todas las operaciones se registran automáticamente en la tabla `audit_log`:

```sql
SELECT 
    table_name,
    operation,
    record_id,
    user_id,
    timestamp
FROM audit_log 
ORDER BY timestamp DESC
LIMIT 10;
```

## 🚨 Manejo de Errores

```python
try:
    student_id = crud.add_student("Juan", "Pérez", "juan@email.com")
except ValueError as e:
    # Error de validación (email duplicado, datos inválidos, etc.)
    print(f"Error de validación: {e}")
except sqlite3.Error as e:
    # Error de base de datos
    print(f"Error de base de datos: {e}")
except Exception as e:
    # Error inesperado
    print(f"Error inesperado: {e}")
```

## 📚 Recursos Adicionales

- [Documentación SQLite](https://sqlite.org/docs.html)
- [Guía de SQL](https://www.w3schools.com/sql/)
- [Patrones DAO](https://www.oracle.com/java/technologies/dataaccessobject.html)
- [ReportLab Documentation](https://docs.reportlab.com/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

## 🤝 Contribuciones

Para contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

---

**¿Tienes preguntas?** Abre un issue en el repositorio o consulta los ejemplos en la carpeta `examples/`.
