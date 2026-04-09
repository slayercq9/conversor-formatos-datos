from __future__ import annotations

APP_TITLE = "Conversor de Formatos Tabulares"
APP_VERSION = "1.0.0"
APP_AUTHOR = "Fernando Corrales Quirós"
APP_MIN_SIZE = (960, 640)
DEFAULT_TEXT_DELIMITER = "\t"
PREVIEW_ROW_LIMIT = 50

ABOUT_TEXT = (
    "Aplicacion de escritorio para convertir archivos tabulares entre "
    "CSV, XLSX, JSON y TXT usando una interfaz clara y modular construida "
    "con Tkinter."
)

HELP_TEXT = (
    "1. Selecciona un archivo con el boton 'Seleccionar archivo'.\n"
    "2. La aplicacion acepta archivos de entrada CSV, XLSX, JSON y TXT.\n"
    "3. Elige el formato de salida en el selector correspondiente.\n"
    "4. Usa 'Vista previa' para revisar los datos antes de convertir.\n"
    "5. Pulsa 'Convertir' para preparar el resultado.\n"
    "6. Pulsa 'Guardar convertido' para elegir la ubicacion final y guardar.\n\n"
    "Advertencias:\n"
    "- Si el archivo esta vacio, la aplicacion lo indicara con un mensaje claro.\n"
    "- Si el formato no es compatible o el archivo tiene errores, se mostrara un dialogo informativo.\n"
    "- La app no se cierra por errores comunes; solo informa el problema.\n\n"
    "Nota: en el futuro se planea agregar soporte para arrastrar y soltar archivos."
)
