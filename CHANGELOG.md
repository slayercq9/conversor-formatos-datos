# Changelog

Todos los cambios relevantes de este proyecto se documentarán en este archivo.

El formato está inspirado en Keep a Changelog y usa versionado visible alineado con el proyecto.

## [4.0.0] - 2026-04-14

### Añadido

- Soporte de lectura y escritura para archivos TSV.
- Soporte de lectura y escritura para archivos XML tabulares.
- Pruebas automáticas para lectura de TSV, escritura y lectura de XML y errores claros en XML inválido.

### Mejorado

- Registro central de formatos actualizado para exponer TSV y XML en filtros y opciones visibles.
- Ayuda y documentación alineadas con los nuevos formatos soportados.

### Notas

- XML se admite cuando su estructura puede representarse razonablemente como tabla.
- Si el XML no es tabularizable, la app informa el problema sin cerrarse.

## [3.0.0] - 2026-04-14

### Añadido

- Archivo `CHANGELOG.md` para registrar cambios por versión.
- Archivo `LICENSE` con licencia MIT.
- Script `scripts/package_portable.ps1` para preparar un paquete portable y generar un ZIP compartible.
- Documentación ampliada para distribución pública portable.

### Mejorado

- README reforzado con instrucciones para generar el ejecutable, preparar un paquete portable y compartir la app con otros usuarios.
- Manual de usuario actualizado con una explicación breve de qué significa que la app sea portable.
- Estructura documental del proyecto más clara para una futura distribución pública.

### Notas

- La distribución sigue siendo portable y no incluye instalador.
- GitHub Releases y posibles donaciones quedan documentados como trabajo futuro, sin implementación en esta versión.

## [2.2.0] - 2026-04-14

### Añadido

- Persistencia simple de preferencias en un archivo JSON portable.
- Restauración del último formato de salida entre sesiones.
- Restauración opcional del tamaño y la posición de la ventana principal.

### Mejorado

- El botón `Limpiar` reinicia de forma más consistente el estado visual de la interfaz.
- Mensajes de estado, éxito y advertencia más claros para el usuario.

## [2.1.0] - 2026-04-13

### Mejorado

- Pulido visual de la interfaz principal, la vista previa y las ventanas informativas.
- Ajustes finos de proporciones, espaciados, alineación y jerarquía visual.

## [2.0.0] - 2026-04-13

### Añadido

- Botón `Limpiar` para reiniciar la interfaz sin cerrar la aplicación.
- Información visible del archivo cargado: nombre, extensión, tamaño aproximado y filas cuando aplica.

### Mejorado

- Retroalimentación más clara al completar una conversión.
- Conservación del último formato de salida durante la sesión actual.

## [1.2.0] - 2026-04-12

### Añadido

- Manual de usuario inicial.
- Ventana "Acerca de" conectada a metadatos centralizados.
- Integración del icono definitivo `assets/icon.ico`.
- Soporte de drag and drop para archivos compatibles.

### Mejorado

- Consistencia de versión y fecha en la documentación visible del proyecto.
