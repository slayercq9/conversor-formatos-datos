# Changelog

Todos los cambios relevantes de este proyecto se documentan en este archivo.

## [5.1.0] - 2026-04-15

### Mejorado

- Documentación general alineada con el estado actual del proyecto.
- README actualizado con formatos soportados, scripts disponibles, build portable, build instalable y estructura del proyecto.
- MANUAL_USUARIO actualizado con el flujo real de uso, vista previa, multidioma y modalidades de distribución.
- CHANGELOG reorganizado para reflejar versiones cerradas de forma más clara y consistente.

## [5.0.0] - 2026-04-15

### Añadido

- Soporte multidioma ligero para español e inglés en la interfaz.
- Selector visible de idioma en la ventana principal.
- Persistencia de la preferencia de idioma entre sesiones.
- Capa centralizada de textos para facilitar mantenimiento futuro.

### Mejorado

- Ventana principal, ayuda, acerca de, botones, etiquetas y mensajes visibles ahora pueden mostrarse en ambos idiomas.
- La vista previa y los mensajes del dominio se traducen en la capa de interfaz sin tocar la lógica central.

## [4.2.0] - 2026-04-15

### Añadido

- Preparación formal para generar un instalador de Windows con Inno Setup 6.
- Script [scripts/build_installer.ps1](/C:/Users/Fernando/Documents/Conversor_formatos/scripts/build_installer.ps1) para compilar el instalador de forma repetible.
- Base de configuración del instalador en [installer/ConversorFormatos.iss](/C:/Users/Fernando/Documents/Conversor_formatos/installer/ConversorFormatos.iss).

### Mejorado

- Documentación actualizada para distinguir claramente entre versión portable e instalable.
- Flujo de build principal actualizado para mencionar ambas salidas oficiales.

## [4.1.0] - 2026-04-14

### Mejorado

- La vista previa ahora muestra un resumen más claro de columnas detectadas y filas visibles.
- Se agrega una nota visible cuando la vista previa es parcial.
- Se mejora el uso del espacio y la presentación de encabezados en la tabla de inspección.
- La interfaz conserva el enfoque de inspección rápida sin edición.

## [4.0.0] - 2026-04-14

### Añadido

- Soporte de lectura y escritura para archivos TSV.
- Soporte de lectura y escritura para archivos XML tabulares.
- Soporte de lectura y escritura para archivos ODS.

### Mejorado

- Manejo de errores más claro para JSON no tabular, XML no tabular y dependencias faltantes de XLSX u ODS.
- Documentación alineada con limitaciones de compatibilidad importantes.
