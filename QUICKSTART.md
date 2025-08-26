# 🚀 GUÍA RÁPIDA - Sistema de Gestión Educativa

## ⚡ Instalación en 30 segundos

```bash
# 1. Descargar/clonar el proyecto
# 2. Abrir terminal en la carpeta del proyecto
# 3. Ejecutar:
./install.sh
```

## 🎯 Usar el Sistema

**Después de la instalación:**

```bash
# Aplicación principal
./ejecutar_aplicacion.sh

# Demo de conceptos de BD  
./ejemplo_conceptos_bd.sh

# CRUD simple
./ejemplo_crud_simple.sh

# Verificar funcionamiento
./probar_sistema.sh
```

## ❓ Si algo no funciona

```bash
# Reinstalar dependencias
./install.sh

# O probar manualmente:
source venv/bin/activate
python3 test_database.py     # Debería pasar todos los tests
python3 main.py             # Aplicación principal

# Si hay errores de importación:
cd /path/to/LP2
source venv/bin/activate
python3 -c "from src.database import *; print('✅ Importaciones OK')"
```

## 📚 Lo que incluye este sistema

✅ **Aplicación completa** con interfaz gráfica  
✅ **Base de datos SQLite** con datos de ejemplo  
✅ **Todos los conceptos de BD** implementados:
- Qué es una Base de Datos
- Control de Datos  
- Integridad Referencial
- Navegación de Registros
- Objetos de Acceso a Datos (DAO)
- Generación de Reportes
- Operaciones CRUD con SQL
- Uso de SQL completo

✅ **Reportes automáticos** en PDF, Excel, CSV, HTML  
✅ **Ejemplos interactivos** paso a paso  
✅ **Documentación completa** en `src/database/README.md`

## 🆘 Soporte

- **Documentación técnica**: `src/database/README.md`
- **Código de ejemplo**: Carpeta `examples/`
- **Verificar instalación**: `python3 test_database.py`

---

**¡Listo para usar!** 🎉
