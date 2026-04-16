# Changelog

Todos los cambios relevantes de este proyecto se documentan en este archivo.

## [5.2.0] - 2026-04-16

### Mejorado

- Revisión integral final del proyecto orientada a publicación futura.
- Comentarios y docstrings ajustados para reflejar mejor el estado actual de la aplicación.
- Scripts de empaquetado portable e instalador alineados con la versión visible vigente.
- Documentación actualizada para reflejar con precisión multidioma, tema oscuro, persistencia del tema y cadena de distribución.

## [5.1.2] - 2026-04-15

### Añadido

- Persistencia del tema visual entre sesiones usando el archivo ligero de preferencias.

### Mejorado

- Controles de idioma y tema rediseñados con una apariencia segmentada más compacta y coherente.
- Integración del selector de tema con restauración segura al iniciar la aplicación.

## [5.1.1] - 2026-04-15

### Añadido

- Soporte visual para tema claro y tema oscuro.
- Selector de tema en la ventana principal.

### Mejorado

- Estilos centralizados para facilitar el mantenimiento visual futuro.
- Ventanas `Acerca de`, `Cómo usar` y sección de vista previa alineadas con ambos temas.

## [5.1.0] - 2026-04-15

### Mejorado

- Documentación técnica y de usuario alineada con el estado real de la aplicación.
- README actualizado con scripts, distribución portable, instalador y estructura del proyecto.
- Manual de usuario ajustado al flujo actual, formatos soportados y experiencia bilingüe.
- Revisión técnica ligera de consistencia interna en GUI, scripts y metadatos de distribución.

## [5.0.0] - 2026-04-15

### Añadido

- Soporte multidioma ligero para español e inglés.
- Selector visible de idioma en la ventana principal.
- Persistencia del idioma entre sesiones.

### Mejorado

- Ventana principal, ayuda, acerca de, botones, etiquetas y mensajes visibles adaptados a ambos idiomas.

## [4.2.0] - 2026-04-15

### Añadido

- Preparación formal para generar instalador de Windows con Inno Setup 6.
- Script `scripts/build_installer.ps1` para compilar el instalador.
- Base del instalador en `installer/ConversorFormatos.iss`.

### Mejorado

- Documentación diferenciando versión portable e instalable.

## [4.1.0] - 2026-04-14

### Mejorado

- Vista previa más clara con resumen de columnas, filas visibles y aviso de parcialidad.
- Mejor uso del espacio y presentación más limpia de la tabla de inspección.

## [4.0.0] - 2026-04-14

### Añadido

- Soporte de lectura y escritura para TSV.
- Soporte de lectura y escritura para XML tabular.
- Soporte de lectura y escritura para ODS.

### Mejorado

- Compatibilidad reforzada para JSON, XML y ODS.
- Mensajes más claros cuando un archivo no puede representarse como tabla.

## [3.0.0] - 2026-04-14

### Añadido

- Preparación para distribución pública portable.
- `CHANGELOG.md`, `LICENSE` y documentación base para compartir la aplicación.
- Script auxiliar para empaquetar una versión portable en ZIP.

### Mejorado

- README y manual orientados a una distribución portable más profesional.

## [2.3.0] - 2026-04-14

### Mejorado

- Refinamiento de mensajes y estados visuales al limpiar la interfaz.
- Reinicio más claro de archivo, vista previa, conversión preparada y mensajes transitorios.
- Consistencia mejorada entre el estado visible de la GUI y la persistencia ligera entre sesiones.

## [2.2.0] - 2026-04-14

### Añadido

- Persistencia ligera de preferencias en JSON.
- Restauración del último formato de salida.
- Restauración simple del tamaño y posición de la ventana principal.

## [2.1.0] - 2026-04-13

### Mejorado

- Pulido visual fino de la interfaz principal.
- Ajustes de alineación, tamaños y proporciones de controles.
- Refinamiento de la ventana `Cómo usar` y de la tabla de vista previa.

## [2.0.0] - 2026-04-13

### Añadido

- Botón `Limpiar` para reiniciar la interfaz sin cerrar la aplicación.
- Resumen visible del archivo cargado con nombre, extensión, tamaño y filas cuando es posible.

### Mejorado

- Mensajes de éxito y estado más claros para el usuario.
- Ventana `Acerca de` con fecha visible en formato largo y legible.

## [1.2.0] - 2026-04-12

### Añadido

- Manual de usuario base y documentación inicial del proyecto.
- Integración de icono personalizado para la ventana y el ejecutable.
- Preparación y posterior integración real de drag and drop.

### Mejorado

- Metadatos visibles centralizados en constantes reutilizables.
- Compatibilidad de empaquetado ajustada para icono y drag and drop.

## [1.0.0] - 2026-04-12

### Añadido

- Estructura base modular del proyecto con `src/gui`, `src/core`, `src/services`, `src/utils` y `tests`.
- Punto de entrada `app.py`.
- Ventana principal con selección de archivo, selector de formato, conversión, guardado y vista previa.
- Ventanas informativas `Acerca de` y `Cómo usar`.
- Lectura, escritura y conversión para CSV, XLSX, JSON y TXT con `pandas`.
- Validaciones, errores personalizados y pruebas base del proyecto.
