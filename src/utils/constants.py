from __future__ import annotations

APP_TITLE = "Conversor de Formatos Tabulares"
APP_MIN_SIZE = (960, 640)
DEFAULT_TEXT_DELIMITER = "\t"
PREVIEW_ROW_LIMIT = 50

SUPPORTED_FORMAT_LABELS = {
    "csv": "CSV",
    "xlsx": "Excel (.xlsx)",
    "json": "JSON",
    "txt": "Texto delimitado (.txt)",
}

ABOUT_TEXT = (
    "Conversor de Formatos Tabulares\n\n"
    "Base modular para convertir archivos CSV, XLSX, JSON y TXT "
    "desde una interfaz de escritorio construida con Tkinter."
)

HELP_TEXT = (
    "Uso basico:\n"
    "1. Selecciona un archivo de entrada.\n"
    "2. Elige el formato de salida.\n"
    "3. Previsualiza los datos si lo deseas.\n"
    "4. Indica la ruta del archivo de salida.\n"
    "5. Ejecuta la conversion.\n\n"
    "La integracion con drag and drop quedo preparada para una fase futura."
)
