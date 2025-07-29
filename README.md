# Gestión de Estudiantes con Tkinter

Una aplicación de escritorio desarrollada en Python usando Tkinter para la gestión de estudiantes.

## Características

- ✅ Interfaz gráfica intuitiva con Tkinter
- ✅ Gestión completa de estudiantes (agregar, listar, eliminar)
- ✅ Validación de datos de entrada
- ✅ Arquitectura modular y escalable
- ✅ Código bien documentado

## Estructura del Proyecto

```
LP2/
├── main.py                    # Punto de entrada de la aplicación
├── src/
│   ├── __init__.py
│   ├── gui/
│   │   ├── __init__.py
│   │   └── main_window.py     # Ventana principal
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py         # Modelo de datos del estudiante
│   └── utils/
│       ├── __init__.py
│       └── validators.py      # Funciones de validación
├── assets/                    # Recursos (imágenes, iconos, etc.)
├── tests/                     # Pruebas unitarias
├── requirements.txt           # Dependencias del proyecto
└── README.md                  # Este archivo
```

## Requisitos

- Python 3.7 o superior
- Tkinter (incluido con Python)

## Instalación

1. Clona o descarga el proyecto
2. Navega al directorio del proyecto
3. Ejecuta la aplicación:

```bash
python main.py
```

## Uso

### Funcionalidades principales:

1. **Agregar estudiante**: Completa el formulario con nombre, email, edad y curso
2. **Validación automática**: Los datos se validan antes de ser guardados
3. **Lista de estudiantes**: Visualiza todos los estudiantes en una tabla
4. **Eliminar estudiante**: Selecciona un estudiante y elimínalo
5. **Limpiar campos**: Borra todos los campos del formulario

### Validaciones implementadas:

- **Nombre**: Solo letras y espacios
- **Email**: Formato válido de email
- **Edad**: Número entero entre 1 y 120
- **Curso**: Selección obligatoria

## Buenas Prácticas Implementadas

### 1. Arquitectura Modular
- Separación clara de responsabilidades
- Código organizado en paquetes y módulos
- Fácil mantenimiento y extensión

### 2. Documentación
- Docstrings en todas las funciones y clases
- Comentarios explicativos en el código
- README detallado

### 3. Validación de Datos
- Validaciones en el cliente
- Mensajes de error claros
- Prevención de datos inválidos

### 4. Manejo de Errores
- Try-catch apropiados
- Mensajes de error informativos
- Recuperación graceful de errores

### 5. Interfaz de Usuario
- Diseño intuitivo y limpio
- Navegación clara
- Feedback visual al usuario

## Extensiones Posibles

1. **Persistencia de datos**: Guardar en archivo JSON o base de datos
2. **Búsqueda y filtros**: Buscar estudiantes por nombre o curso
3. **Exportación**: Exportar lista a CSV o Excel
4. **Validaciones avanzadas**: Más reglas de negocio
5. **Temas**: Soporte para temas claro/oscuro

## Desarrollo

### Agregar nueva funcionalidad:

1. Crear la lógica en el modelo correspondiente
2. Agregar validaciones en `utils/validators.py`
3. Implementar la interfaz en `gui/main_window.py`
4. Documentar los cambios

### Estructura de archivos recomendada:

```python
# Para nuevos modelos
src/models/nuevo_modelo.py

# Para nuevas ventanas
src/gui/nueva_ventana.py

# Para nuevas utilidades
src/utils/nueva_utilidad.py
```

## Autor

Proyecto desarrollado para fines educativos en el curso de Programación II.

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
