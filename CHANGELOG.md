# Changelog

Todos los cambios relevantes de este proyecto se documentarán en este archivo.

El formato está inspirado en Keep a Changelog y usa versionado visible alineado con el proyecto.

## [4.2.0] - 2026-04-14

### Añadido

- Preparación formal para generar un instalador de Windows con Inno Setup 6.
- Script [scripts/build_installer.ps1](/C:/Users/Fernando/Documents/Conversor_formatos/scripts/build_installer.ps1) para compilar el instalador de forma repetible.
- Base de configuración del instalador en [installer/ConversorFormatos.iss](/C:/Users/Fernando/Documents/Conversor_formatos/installer/ConversorFormatos.iss).

### Mejorado

- Documentación actualizada para distinguir claramente entre versión portable e instalable.
- Flujo de build principal actualizado para mencionar ambas salidas oficiales.

### Notas

- La distribución portable se mantiene como vía oficial.
- GitHub Releases y donaciones siguen fuera de esta fase.

## [4.1.0] - 2026-04-14

### Mejorado

- La vista previa ahora muestra un resumen más claro de columnas detectadas y filas visibles.
- Se agrega una nota visible cuando la vista previa es parcial.
- Se mejora el uso del espacio y la presentación de encabezados en la tabla de inspección.
- La interfaz conserva el enfoque de inspección rápida sin edición.
