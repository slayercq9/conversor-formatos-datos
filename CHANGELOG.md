# Changelog

Todos los cambios relevantes del proyecto se documentan en este archivo.

El proyecto usa versionado semántico `MAJOR.MINOR.PATCH` a partir de la primera versión pública estable. El trabajo previo se resume mediante rangos numéricos internos desde `0.1.0` hasta `0.5.8`.

## [1.0.0] - 2026-06-10

Primera versión pública estable de Conversor de Formatos Tabulares.

### Incluido

- Conversión tabular entre CSV, XLSX, JSON, TXT, TSV, XML y ODS.
- Interfaz gráfica de escritorio construida con Tkinter y ttk.
- Selección manual de archivos y carga mediante drag and drop.
- Vista previa ligera con columnas detectadas, filas visibles y aviso de muestra parcial.
- Interfaz disponible en español e inglés.
- Temas claro y oscuro con controles segmentados.
- Persistencia local de idioma, tema, último formato de salida y geometría de ventana.
- Validaciones y mensajes claros para archivos vacíos, formatos no soportados y errores de lectura o escritura.
- Distribución portable para Windows mediante PyInstaller.
- Preparación de instalador tradicional para Windows mediante Inno Setup 6.

## Historial interno anterior a 1.0.0

Estas etapas corresponden al desarrollo previo a la primera publicación estable y no representan releases públicas.

### 0.5.0 a 0.5.8

- Vista previa mejorada, interfaz multidioma ES/EN y temas claro/oscuro.
- Persistencia del tema y refinamiento de los controles de idioma y apariencia.
- Preparación del instalador de Windows y revisión final técnica y documental.

### 0.4.0 a 0.4.4

- Soporte para TSV, XML y ODS.
- Robustez adicional para estructuras tabulares sensibles y dependencias opcionales.
- Pruebas y mensajes de compatibilidad reforzados.

### 0.3.0 a 0.3.4

- Documentación profesional, manual de usuario, licencia MIT y changelog.
- Preparación de distribución portable y generación de paquetes ZIP.

### 0.2.0 a 0.2.5

- Mejoras de experiencia de usuario, drag and drop y preferencias persistentes.
- Información del archivo cargado, mensajes de estado y pulido visual.

### 0.1.0 a 0.1.4

- Estructura modular inicial y ventana principal.
- Conversión base para CSV, XLSX, JSON y TXT.
- Validaciones, manejo de errores, pruebas iniciales y ejecutable preliminar.
