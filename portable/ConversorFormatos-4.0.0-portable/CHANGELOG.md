# Changelog

Todos los cambios relevantes de este proyecto se documentarán en este archivo.

El formato está inspirado en Keep a Changelog y usa versionado visible alineado con el proyecto.

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
- Pruebas automáticas adicionales para compatibilidad práctica, vista previa y errores esperables en XML, JSON y ODS.

### Mejorado

- Registro central de formatos actualizado para exponer TSV, ODS y XML en filtros y opciones visibles.
- Manejo de errores más claro para JSON no tabular, XML no tabular y dependencias faltantes de XLSX u ODS.
- Ayuda y documentación alineadas con las limitaciones de compatibilidad más importantes.

### Notas

- XML se admite cuando su estructura puede representarse razonablemente como tabla.
- JSON funciona mejor con listas de registros o estructuras tabulares compatibles.
- Si el XML o el JSON no son tabularizables, la app informa el problema sin cerrarse.
- Parquet queda fuera de esta fase.
