"""Constantes compartidas por la interfaz y servicios auxiliares.

Centralizar estos valores evita cadenas dispersas y facilita mantener
textos visibles o configuraciones base desde un solo lugar.
"""

from __future__ import annotations

APP_TITLE = "Conversor de Formatos Tabulares"
APP_VERSION = "1.2.0"
APP_LAST_UPDATED = "2026-04-12"
APP_AUTHOR = "Fernando Corrales Quiros"
APP_MIN_SIZE = (960, 640)
DEFAULT_TEXT_DELIMITER = "\t"
PREVIEW_ROW_LIMIT = 50

APP_DESCRIPTION = (
    "Aplicacion de escritorio para convertir archivos tabulares entre "
    "CSV, XLSX, JSON y TXT usando una interfaz clara y modular construida "
    "con Tkinter."
)

HELP_TEXT = (
    "1. Selecciona un archivo con el boton 'Seleccionar archivo'.\n"
    "   Tambien puedes arrastrar y soltar un archivo compatible en la ventana principal.\n"
    "2. La aplicacion acepta archivos de entrada CSV, XLSX, JSON y TXT.\n"
    "3. Elige el formato de salida en el selector correspondiente.\n"
    "4. Usa 'Vista previa' para revisar los datos antes de convertir.\n"
    "5. Pulsa 'Convertir' para preparar el resultado.\n"
    "6. Pulsa 'Guardar convertido' para elegir la ubicacion final y guardar.\n\n"
    "Advertencias:\n"
    "- Si el archivo esta vacio, la aplicacion lo indicara con un mensaje claro.\n"
    "- Si el formato no es compatible o el archivo tiene errores, se mostrara un dialogo informativo.\n"
    "- La app no se cierra por errores comunes; solo informa el problema.\n\n"
    "Nota: la aplicacion ya permite arrastrar y soltar archivos compatibles en la ventana principal."
)
