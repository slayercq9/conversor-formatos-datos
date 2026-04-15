"""Constantes compartidas por la interfaz y servicios auxiliares.

Centralizar estos valores evita cadenas dispersas y facilita mantener
textos visibles o configuraciones base desde un solo lugar.
"""

from __future__ import annotations

APP_TITLE = "Conversor de Formatos Tabulares"
APP_VERSION = "4.0.0"
APP_LAST_UPDATED = "2026-04-14"
APP_LAST_UPDATED_LABEL = "Martes, 14 de abril de 2026"
APP_AUTHOR = "Fernando Corrales Quirós"
APP_MIN_SIZE = (960, 640)
DEFAULT_TEXT_DELIMITER = "\t"
PREVIEW_ROW_LIMIT = 50

APP_DESCRIPTION = (
    "Aplicación de escritorio para convertir archivos tabulares entre "
    "CSV, TSV, XLSX, ODS, JSON, XML y TXT usando una interfaz clara y modular "
    "construida con Tkinter."
)

HELP_TEXT = (
    "1. Selecciona un archivo con el botón 'Seleccionar archivo'.\n"
    "   También puedes arrastrar y soltar un archivo compatible en la ventana principal.\n"
    "2. La aplicación acepta archivos de entrada CSV, TSV, XLSX, ODS, JSON, XML y TXT.\n"
    "3. Revisa la información del archivo cargado para confirmar nombre, extensión y tamaño aproximado.\n"
    "4. Elige el formato de salida en el selector correspondiente.\n"
    "5. Usa 'Vista previa' para revisar los datos antes de convertir.\n"
    "6. Pulsa 'Convertir' para preparar el resultado.\n"
    "7. Pulsa 'Guardar convertido' para elegir la ubicación final y guardar.\n"
    "8. Si deseas comenzar otra tarea sin cerrar la app, usa el botón 'Limpiar'.\n\n"
    "Advertencias:\n"
    "- Si el archivo está vacío, la aplicación lo indicará con un mensaje claro.\n"
    "- Si el formato no es compatible o el archivo tiene errores, se mostrará un diálogo informativo.\n"
    "- Algunos XML no pueden convertirse a tabla; en ese caso la app mostrará un mensaje claro.\n"
    "- El soporte ODS usa la dependencia ligera 'odfpy', incluida en requirements.txt.\n"
    "- La app no se cierra por errores comunes; solo informa el problema.\n\n"
    "Nota: la aplicación recuerda el último formato de salida y puede restaurar el tamaño y la posición de la ventana."
)
