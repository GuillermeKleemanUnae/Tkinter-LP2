# Sistema de Gestión Educativa

Una aplicación completa de escritorio desarrollada en Python que implementa **todos los conceptos fundamentales de bases de datos** de manera práctica y educativa. Incluye interfaz gráfica moderna con Tkinter y un módulo completo de base de datos con SQLite.

## 🚀 Instalación Rápida

**¡Solo ejecuta un comando!**

```bash
./install.sh
```

**¿No funciona el script? Instalación manual:**

```bash
# 1. Crear entorno virtual
python3 -m venv venv

# 2. Activar entorno virtual
source venv/bin/activate

# 3. Instalar dependencias
pip install reportlab pandas openpyxl pillow

# 4. Probar instalación
python3 test_database.py
```

## 🎯 Cómo Usar el Sistema

**Después de la instalación, ejecuta:**

```bash
# Aplicación principal completa
./ejecutar_aplicacion.sh

# Ejemplo CRUD básico  
./ejemplo_crud_simple.sh

# Demo interactiva de conceptos de BD
./ejemplo_conceptos_bd.sh

# Verificar que todo funcione
./probar_sistema.sh
```

**O manualmente:**
```bash
source venv/bin/activate
python3 main.py
```

## 📂 Estructura del Proyecto

```
LP2/
├── main.py                         # Aplicación principal
├── install.sh                     # Script de instalación automática
├── test_database.py               # Pruebas del sistema
├── src/
│   ├── gui/                       # Interfaz gráfica
│   ├── models/                    # Modelos de datos
│   ├── utils/                     # Validaciones
│   └── database/                  # 🎯 Sistema completo de base de datos
│       ├── connection.py          # Conexión SQLite
│       ├── dao.py                 # Objetos de Acceso a Datos
│       ├── crud_operations.py     # Operaciones CRUD
│       ├── data_navigator.py      # Navegación de registros
│       ├── report_generator.py    # Generación de reportes
│       └── README.md              # Documentación técnica
├── examples/
│   ├── 09_database_concepts.py    # Demo completa de conceptos BD
│   └── 10_crud_simple.py          # CRUD básico
└── reports/                       # Reportes generados
```

## 🎓 Conceptos de Base de Datos Implementados

✅ **¿Qué es una Base de Datos?** - Sistema SQLite completo con tablas relacionadas  
✅ **El 'Control de Datos'** - Validaciones, transacciones y auditoría  
✅ **Integridad Referencial** - Claves foráneas y restricciones CASCADE  
✅ **Navegación de Registros** - Controles First/Previous/Next/Last  
✅ **Objetos de Acceso a Datos (DAO)** - Patrón DAO completo  
✅ **Generación de Reportes** - PDF, Excel, CSV, HTML automáticos  
✅ **Operaciones CRUD con SQL** - CREATE, READ, UPDATE, DELETE  
✅ **Uso de SQL** - Ejemplos prácticos con visualización en tiempo real

## 🛠️ Requisitos

- **Python 3.7+** (incluye SQLite y Tkinter)
- **Dependencias opcionales:** ReportLab, Pandas, OpenPyXL (se instalan automáticamente)

## 🧪 Verificar Funcionamiento

```bash
# Probar que todo funcione correctamente
python3 test_database.py

# Si hay problemas, reinstalar dependencias
./install.sh
```

## 📚 Documentación

- **Guía técnica completa:** `src/database/README.md`
- **Ejemplos interactivos:** Carpeta `examples/`
- **Instalación detallada:** `INSTALL.md`

## 📊 Esquema de Base de Datos

### Tablas Principales
- **students**: Información de estudiantes
- **courses**: Catálogo de cursos
- **enrollments**: Inscripciones (relación muchos a muchos)
- **audit_log**: Registro de auditoría

### Relaciones
```sql
students 1 ──── N enrollments N ──── 1 courses
```

### Integridad Referencial
- Las inscripciones se eliminan automáticamente al eliminar estudiantes (CASCADE)
- No se pueden crear inscripciones con estudiantes/cursos inexistentes
- Emails únicos, validación de calificaciones (0-100)

## 🎮 Funcionalidades de la Aplicación

### Ventana Principal
1. **Panel de Configuración**: Ajustes y configuraciones
2. **Formulario de Estudiantes**: Agregar/editar estudiantes  
3. **Lista de Estudiantes**: Visualización en tabla con navegación
4. **Panel de Estadísticas**: Métricas y análisis en tiempo real

### Operaciones CRUD Disponibles
- ➕ **CREATE**: Agregar nuevos estudiantes, cursos, inscripciones
- 🔍 **READ**: Buscar por ID, nombre, email, filtros avanzados
- ✏️ **UPDATE**: Editar información existente
- 🗑️ **DELETE**: Eliminar registros (con confirmación)

### Sistema de Navegación
- Controles de navegación tipo reproductor de música
- Indicadores de posición ("Registro 1 de 25")
- Filtros por estado (activo/inactivo/graduado)
- Ordenamiento por múltiples campos

### Generación de Reportes
- 📄 **Reporte de Estudiantes**: Lista completa con estadísticas
- 📚 **Reporte de Cursos**: Información de cursos y inscripciones  
- 🎓 **Historial Académico**: Transcripción individual por estudiante
- 📊 **Reporte Estadístico**: Métricas generales del sistema

## 🧪 Testing

### Ejecutar Pruebas
```bash
# Pruebas unitarias individuales
python -m pytest tests/test_student.py -v
python -m pytest tests/test_validators.py -v

# Todas las pruebas
python -m pytest tests/ -v

# Con cobertura
pip install pytest-cov
python -m pytest tests/ --cov=src --cov-report=html
```

### Pruebas de Integridad
Los ejemplos incluyen pruebas automáticas de integridad referencial:
- Violaciones de clave foránea
- Restricciones UNIQUE
- Validaciones CHECK
- Operaciones en cascada

## 🏗️ Arquitectura y Patrones

### Patrón MVC Implementado
- **Model**: `src/models/` y `src/database/dao.py`
- **View**: `src/gui/` y componentes
- **Controller**: `src/database/crud_operations.py`

### Patrones de Diseño Utilizados
- **DAO (Data Access Object)**: Abstracción de acceso a datos
- **Singleton**: Conexión única a la base de datos
- **Factory**: Creación de objetos de base de datos
- **Observer**: Navegación y actualización de UI

### Principios SOLID
- **S**ingle Responsibility: Cada clase tiene una responsabilidad específica
- **O**pen/Closed: Extensible sin modificar código existente
- **L**iskov Substitution: Interfaces consistentes
- **I**nterface Segregation: Interfaces específicas (DAOs)
- **D**ependency Inversion: Depende de abstracciones, no implementaciones

## 📚 Documentación Adicional

### Para Usuarios
- [Guía de Usuario](src/database/README.md) - Documentación completa del módulo de BD
- [Ejemplos Prácticos](examples/) - Código de ejemplo paso a paso
- [Manual de Reportes](reports/) - Cómo generar y usar reportes

### Para Desarrolladores
- [Arquitectura del Sistema](docs/architecture.md) - Diseño y patrones
- [API Reference](docs/api.md) - Documentación de APIs
- [Guía de Contribución](CONTRIBUTING.md) - Cómo contribuir al proyecto

## 🔄 Roadmap y Extensiones Futuras

### Próximas Funcionalidades
- [ ] **Autenticación**: Sistema de usuarios y permisos
- [ ] **Backup Automático**: Respaldos programados de BD
- [ ] **Importación/Exportación**: Intercambio de datos masivos
- [ ] **Dashboard Avanzado**: Métricas en tiempo real con gráficos
- [ ] **API REST**: Exposición de servicios web
- [ ] **Mobile App**: Aplicación complementaria móvil

### Mejoras Técnicas
- [ ] **ORM Integration**: Integración con SQLAlchemy
- [ ] **Async Operations**: Operaciones asíncronas para mejor rendimiento  
- [ ] **Caching System**: Sistema de caché para consultas frecuentes
- [ ] **Multi-tenancy**: Soporte para múltiples organizaciones
- [ ] **Cloud Storage**: Integración con servicios en la nube

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork el repositorio
2. Crea una rama de feature (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios siguiendo las convenciones del proyecto
4. Agrega tests para nueva funcionalidad
5. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
6. Push a la rama (`git push origin feature/nueva-funcionalidad`)
7. Crea un Pull Request

### Áreas donde Puedes Ayudar
- 🐛 **Reporte de bugs** y correcciones
- 📝 **Documentación** y ejemplos
- 🚀 **Nuevas funcionalidades** 
- 🧪 **Tests** y cobertura
- 🎨 **UI/UX** mejoradas
- 🌐 **Internacionalización**

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

**Proyecto Educativo - LP2**  
Desarrollado para demostrar conceptos avanzados de:
- Programación orientada a objetos
- Interfaces gráficas con Tkinter  
- Bases de datos relacionales
- Patrones de diseño
- Arquitectura de software

---

## 🆘 Soporte y Contacto

**¿Tienes preguntas o problemas?**

1. **Documentación**: Revisa [src/database/README.md](src/database/README.md)
2. **Ejemplos**: Ejecuta los archivos en [examples/](examples/)
3. **Issues**: Abre un issue en GitHub
4. **Discusiones**: Participa en GitHub Discussions

**¿Necesitas ayuda específica con conceptos de BD?**
- Ejecuta `python examples/09_database_concepts.py` para una demostración interactiva
- Consulta los comentarios detallados en el código fuente
- Revisa los tests para ver casos de uso prácticos

¡Gracias por usar este sistema educativo! 🎓✨
