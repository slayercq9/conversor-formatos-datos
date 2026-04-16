"""Utilidades ligeras de internacionalizacion para la interfaz.

La aplicacion usa un catalogo pequeno en memoria para mantener el
proyecto portable y facil de extender sin dependencias externas.
"""

from __future__ import annotations

import re
from typing import Any


SUPPORTED_LANGUAGES: dict[str, str] = {
    "es": "Español",
    "en": "English",
}


UI_TEXTS: dict[str, dict[str, Any]] = {
    "es": {
        "app": {
            "title": "Conversor de Formatos Tabulares",
            "subtitle": "Convierte archivos tabulares y revisa una vista previa antes de guardarlos.",
            "description": (
                "Aplicación de escritorio para convertir archivos tabulares entre "
                "CSV, TSV, XLSX, ODS, JSON, XML y TXT usando una interfaz clara y modular "
                "construida con Tkinter."
            ),
            "author_prefix": "Creado por {author}",
            "version_label": "Versión actual: {version}",
            "updated_label": "Última actualización: {date}",
            "language_label": "Idioma",
            "theme_label": "Tema",
        },
        "sections": {
            "load": "Carga de archivo",
            "config": "Configuración",
            "preview": "Vista previa",
        },
        "buttons": {
            "select_file": "Seleccionar archivo",
            "preview": "Vista previa",
            "convert": "Convertir",
            "clear": "Limpiar",
            "save": "Guardar convertido",
            "help": "Cómo usar",
            "about": "Acerca de",
            "close": "Cerrar",
        },
        "labels": {
            "output_format": "Formato de salida",
            "file_name": "Nombre",
            "file_extension": "Extensión",
            "file_size": "Tamaño aproximado",
            "file_rows": "Registros o filas",
        },
        "themes": {
            "light": "Claro",
            "dark": "Oscuro",
        },
        "messages": {
            "default_source_label": "Ningún archivo cargado todavía.",
            "default_file_info": "Cuando cargues un archivo, aquí verás un resumen útil para revisarlo rápidamente.",
            "default_status": "Selecciona un archivo para comenzar.",
            "default_ready": "Todavía no hay una conversión lista para guardar.",
            "load_hint": (
                "Selecciona un archivo desde el explorador o arrástralo a esta "
                "sección para cargarlo automáticamente."
            ),
            "config_hint": "Selecciona un formato antes de convertir.",
            "file_loaded": "Archivo cargado correctamente. Revisa la vista previa o elige Convertir para preparar el resultado.",
            "file_loaded_preview_hint": "Archivo cargado. Usa Vista previa para revisar su estructura y las primeras filas.",
            "status_file_selected": "Archivo seleccionado: {name}",
            "status_file_dropped": "Archivo cargado mediante arrastre: {name}",
            "status_selection_canceled": "Selección de archivo cancelada.",
            "status_drop_invalid": "El archivo soltado no es válido.",
            "status_preview_failed": "No se pudo generar la vista previa del archivo actual.",
            "status_conversion_failed": "La conversión falló.",
            "status_save_failed": "No se pudo guardar el archivo convertido.",
            "status_save_canceled": "Guardado cancelado por el usuario.",
            "status_waiting_file": "Esperando un archivo de entrada.",
            "status_waiting_format": "Esperando selección del formato de salida.",
            "status_preview_refresh_failed": "La interfaz sigue disponible, pero no fue posible refrescar la vista previa.",
            "status_format_updated": "Formato de salida actualizado.",
            "status_saved": "Archivo guardado: {name}",
            "status_save_prepare_first": "Primero convierte el archivo antes de intentar guardarlo.",
            "status_clean": "Interfaz limpia: se quitaron el archivo, la vista previa, la conversión preparada y la selección visible del formato.",
            "status_converted_ready": "Conversión lista a {format}.",
            "ready_format_updated": "Formato actualizado. Usa Convertir para preparar un nuevo archivo en ese formato.",
            "ready_conversion_failed": "No se pudo preparar la conversión. Revisa el archivo y vuelve a intentarlo.",
            "ready_conversion_ok": "Conversión preparada con éxito. Ya puedes guardar el archivo convertido.",
            "ready_conversion_saved": "Conversión completada y guardada. Puedes cargar otro archivo cuando quieras.",
            "save_completed_dialog": (
                "La conversión se completó correctamente.\n\n"
                "Archivo original: {source_name}\n"
                "Formato de salida: {target_format}\n"
                "Archivo guardado en:\n{result_path}"
            ),
            "clear_preview_message": "La interfaz se reinició. Selecciona o arrastra un archivo para comenzar de nuevo.",
            "drop_error_preview": "No se pudo cargar el archivo soltado. Intenta con otro archivo compatible.",
            "preview_build_failed": "No se pudo construir la vista previa. Revisa si el archivo puede representarse como tabla.",
            "preview_refresh_failed": "No se pudo actualizar la vista previa del archivo actual.",
            "preview_empty": "La vista previa de los datos aparecerá aquí.",
            "preview_idle_note": "La vista previa está pensada para inspección rápida y no permite editar datos.",
            "preview_no_columns": "No se encontraron columnas para mostrar.",
            "preview_no_rows": "Se detectaron columnas, pero no hay filas para previsualizar.",
            "preview_summary": "{columns} {column_label} detectadas | {rows} {row_label} en vista previa",
            "preview_summary_partial": "{summary} de {total} en total",
            "preview_note_partial": "La vista previa es parcial para mantener la aplicación ligera. Solo se muestran las primeras filas del archivo.",
            "preview_note_complete": "Vista previa completa cargada para inspección rápida.",
            "dialog_file_required": "Todavía no has cargado un archivo. Usa 'Seleccionar archivo' para continuar.",
            "dialog_format_required": "Todavía no has elegido un formato de salida. Selecciona uno para continuar.",
            "dialog_save_prepare_first": "Primero usa el botón Convertir para preparar el archivo.",
        },
        "titles": {
            "file": "Archivo",
            "preview": "Vista previa",
            "conversion": "Conversión",
            "save": "Guardar archivo",
            "save_completed": "Conversión completada",
            "file_required": "Archivo requerido",
            "format_required": "Formato requerido",
            "drag_drop": "Drag and drop",
            "about": "Acerca de",
            "help": "Cómo usar",
            "open_file": "Selecciona un archivo",
            "save_file": "Guardar archivo convertido",
        },
        "help": {
            "body": (
                "1. Selecciona un archivo con el botón 'Seleccionar archivo'.\n"
                "   También puedes arrastrar y soltar un archivo compatible en la ventana principal.\n"
                "2. La aplicación acepta archivos de entrada CSV, TSV, XLSX, ODS, JSON, XML y TXT.\n"
                "3. Revisa la información del archivo cargado para confirmar nombre, extensión y tamaño aproximado.\n"
                "4. Usa la vista previa para inspeccionar columnas, filas visibles y si la muestra es parcial.\n"
                "5. Elige el formato de salida en el selector correspondiente.\n"
                "6. Pulsa 'Convertir' para preparar el resultado.\n"
                "7. Pulsa 'Guardar convertido' para elegir la ubicación final y guardar.\n"
                "8. Si deseas comenzar otra tarea sin cerrar la app, usa el botón 'Limpiar'.\n\n"
                "Advertencias:\n"
                "- Si el archivo está vacío, la aplicación lo indicará con un mensaje claro.\n"
                "- Si el formato no es compatible o el archivo tiene errores, se mostrará un diálogo informativo.\n"
                "- Algunos XML no pueden convertirse a tabla; en ese caso la app mostrará un mensaje claro.\n"
                "- El soporte ODS usa la dependencia ligera 'odfpy', incluida en requirements.txt.\n"
                "- La app no se cierra por errores comunes; solo informa el problema.\n\n"
                "Nota: la aplicación puede distribuirse como versión portable o como instalador para Windows."
            )
        },
        "meta": {
            "language_names": SUPPORTED_LANGUAGES,
            "column_label_singular": "columna",
            "column_label_plural": "columnas",
            "row_label_singular": "fila",
            "row_label_plural": "filas",
            "without_extension": "sin extensión",
        },
    },
    "en": {
        "app": {
            "title": "Tabular Format Converter",
            "subtitle": "Convert tabular files and review a preview before saving them.",
            "description": (
                "Desktop application for converting tabular files between "
                "CSV, TSV, XLSX, ODS, JSON, XML and TXT using a clear, modular "
                "Tkinter interface."
            ),
            "author_prefix": "Created by {author}",
            "version_label": "Current version: {version}",
            "updated_label": "Last updated: {date}",
            "language_label": "Language",
            "theme_label": "Theme",
        },
        "sections": {
            "load": "Load File",
            "config": "Configuration",
            "preview": "Preview",
        },
        "buttons": {
            "select_file": "Select File",
            "preview": "Preview",
            "convert": "Convert",
            "clear": "Clear",
            "save": "Save Converted",
            "help": "How to Use",
            "about": "About",
            "close": "Close",
        },
        "labels": {
            "output_format": "Output format",
            "file_name": "Name",
            "file_extension": "Extension",
            "file_size": "Approx. size",
            "file_rows": "Rows",
        },
        "themes": {
            "light": "Light",
            "dark": "Dark",
        },
        "messages": {
            "default_source_label": "No file loaded yet.",
            "default_file_info": "When you load a file, you will see a quick summary here.",
            "default_status": "Select a file to get started.",
            "default_ready": "There is no conversion ready to save yet.",
            "load_hint": (
                "Select a file from the browser or drag it into this "
                "section to load it automatically."
            ),
            "config_hint": "Select an output format before converting.",
            "file_loaded": "File loaded successfully. Review the preview or click Convert to prepare the output.",
            "file_loaded_preview_hint": "File loaded. Use Preview to inspect its structure and first rows.",
            "status_file_selected": "Selected file: {name}",
            "status_file_dropped": "File loaded by drag and drop: {name}",
            "status_selection_canceled": "File selection canceled.",
            "status_drop_invalid": "The dropped file is not valid.",
            "status_preview_failed": "The current file preview could not be generated.",
            "status_conversion_failed": "Conversion failed.",
            "status_save_failed": "The converted file could not be saved.",
            "status_save_canceled": "Save operation canceled by the user.",
            "status_waiting_file": "Waiting for an input file.",
            "status_waiting_format": "Waiting for an output format selection.",
            "status_preview_refresh_failed": "The interface is still available, but the preview could not be refreshed.",
            "status_format_updated": "Output format updated.",
            "status_saved": "Saved file: {name}",
            "status_save_prepare_first": "Convert the file before trying to save it.",
            "status_clean": "Interface cleared: file, preview, prepared conversion and visible format selection were removed.",
            "status_converted_ready": "Conversion ready to {format}.",
            "ready_format_updated": "Format updated. Use Convert to prepare a new file in that format.",
            "ready_conversion_failed": "The conversion could not be prepared. Review the file and try again.",
            "ready_conversion_ok": "Conversion prepared successfully. You can now save the converted file.",
            "ready_conversion_saved": "Conversion completed and saved. You can load another file whenever you want.",
            "save_completed_dialog": (
                "The conversion completed successfully.\n\n"
                "Source file: {source_name}\n"
                "Output format: {target_format}\n"
                "Saved to:\n{result_path}"
            ),
            "clear_preview_message": "The interface was reset. Select or drop a file to start again.",
            "drop_error_preview": "The dropped file could not be loaded. Try another supported file.",
            "preview_build_failed": "The preview could not be built. Check whether the file can be represented as a table.",
            "preview_refresh_failed": "The current file preview could not be refreshed.",
            "preview_empty": "The data preview will appear here.",
            "preview_idle_note": "The preview is intended for quick inspection and does not allow editing.",
            "preview_no_columns": "No columns were found to display.",
            "preview_no_rows": "Columns were detected, but there are no rows to preview.",
            "preview_summary": "{columns} {column_label} detected | {rows} {row_label} in preview",
            "preview_summary_partial": "{summary} out of {total} total",
            "preview_note_partial": "The preview is partial to keep the application light. Only the first rows are shown.",
            "preview_note_complete": "Full preview loaded for quick inspection.",
            "dialog_file_required": "You have not loaded a file yet. Use 'Select File' to continue.",
            "dialog_format_required": "You have not chosen an output format yet. Select one to continue.",
            "dialog_save_prepare_first": "Use the Convert button first to prepare the file.",
        },
        "titles": {
            "file": "File",
            "preview": "Preview",
            "conversion": "Conversion",
            "save": "Save File",
            "save_completed": "Conversion Completed",
            "file_required": "File Required",
            "format_required": "Format Required",
            "drag_drop": "Drag and Drop",
            "about": "About",
            "help": "How to Use",
            "open_file": "Select a file",
            "save_file": "Save converted file",
        },
        "help": {
            "body": (
                "1. Select a file with the 'Select File' button.\n"
                "   You can also drag and drop a supported file onto the main window.\n"
                "2. The application accepts CSV, TSV, XLSX, ODS, JSON, XML and TXT input files.\n"
                "3. Review the loaded file information to confirm its name, extension and approximate size.\n"
                "4. Use the preview area to inspect columns, visible rows and whether the preview is partial.\n"
                "5. Choose the output format in the corresponding selector.\n"
                "6. Click 'Convert' to prepare the result.\n"
                "7. Click 'Save Converted' to choose the final location and save it.\n"
                "8. If you want to start another task without closing the app, use the 'Clear' button.\n\n"
                "Warnings:\n"
                "- If the file is empty, the application will show a clear message.\n"
                "- If the format is not supported or the file contains errors, an informational dialog will be shown.\n"
                "- Some XML files cannot be converted into a table; in that case the app will show a clear message.\n"
                "- ODS support uses the lightweight 'odfpy' dependency included in requirements.txt.\n"
                "- The app does not close on common errors; it only reports the issue.\n\n"
                "Note: the application can be distributed as a portable version or as a Windows installer."
            )
        },
        "meta": {
            "language_names": SUPPORTED_LANGUAGES,
            "column_label_singular": "column",
            "column_label_plural": "columns",
            "row_label_singular": "row",
            "row_label_plural": "rows",
            "without_extension": "no extension",
        },
    },
}


class Translator:
    """Resuelve textos visibles y traduce mensajes del dominio en tiempo real."""

    def __init__(self, language_code: str) -> None:
        self.language_code = language_code if language_code in UI_TEXTS else "es"

    def t(self, key: str, **kwargs: Any) -> str:
        value: Any = UI_TEXTS[self.language_code]
        for part in key.split("."):
            value = value[part]
        assert isinstance(value, str)
        return value.format(**kwargs)

    def language_display_name(self, code: str) -> str:
        return SUPPORTED_LANGUAGES.get(code, SUPPORTED_LANGUAGES["es"])

    def resolve_language_code(self, display_name: str) -> str:
        for code, label in SUPPORTED_LANGUAGES.items():
            if label == display_name:
                return code
        return "es"

    def translate_runtime_message(self, message: str) -> str:
        if self.language_code == "es":
            return message

        exact_map = {
            "Todavia no has cargado un archivo.": "You have not loaded a file yet.",
            "El archivo seleccionado no existe.": "The selected file does not exist.",
            "La ruta de entrada no es un archivo valido.": "The input path is not a valid file.",
            "El archivo seleccionado esta vacio.": "The selected file is empty.",
            "El formato del archivo cargado no es soportado.": "The selected file format is not supported.",
            "Debes elegir un formato de salida antes de convertir.": "You must choose an output format before converting.",
            "El formato de salida seleccionado no es soportado.": "The selected output format is not supported.",
            "El formato de salida debe ser distinto al de entrada.": "The output format must be different from the input format.",
            "Debes indicar un nombre de archivo de salida.": "You must provide an output file name.",
            "El archivo seleccionado no contiene datos para procesar.": "The selected file does not contain data to process.",
            "No se pudo interpretar el archivo XML como una tabla. Usa un XML con registros repetidos y campos consistentes.": "The XML file could not be interpreted as a table. Use XML with repeated records and consistent fields.",
            "El archivo XML no contiene una estructura tabular compatible.": "The XML file does not contain a compatible tabular structure.",
            "No se pudo interpretar el archivo JSON como una tabla. Usa una lista de registros o una estructura tabular compatible.": "The JSON file could not be interpreted as a table. Use a list of records or another compatible tabular structure.",
            "No se pudo leer el archivo ODS porque falta la dependencia 'odfpy'. Instala requirements.txt e intenta de nuevo.": "The ODS file could not be read because the 'odfpy' dependency is missing. Install requirements.txt and try again.",
            "No se pudo guardar el archivo ODS porque falta la dependencia 'odfpy'. Instala requirements.txt e intenta de nuevo.": "The ODS file could not be saved because the 'odfpy' dependency is missing. Install requirements.txt and try again.",
            "No se pudo leer el archivo XLSX porque falta una dependencia de Excel. Instala requirements.txt e intenta de nuevo.": "The XLSX file could not be read because an Excel dependency is missing. Install requirements.txt and try again.",
            "No se pudo guardar el archivo XLSX porque falta una dependencia de Excel. Instala requirements.txt e intenta de nuevo.": "The XLSX file could not be saved because an Excel dependency is missing. Install requirements.txt and try again.",
            "Primero convierte el archivo antes de intentar guardarlo.": "Convert the file before trying to save it.",
        }
        if message in exact_map:
            return exact_map[message]

        patterns: list[tuple[re.Pattern[str], str]] = [
            (
                re.compile(r"No se pudo leer el archivo '(.+)'\. Verifica que no este danado o en uso\."),
                "The file '{name}' could not be read. Check that it is not damaged or in use.",
            ),
            (
                re.compile(r"No se pudo guardar el archivo '(.+)'\. Revisa permisos, ruta y si el archivo esta abierto\."),
                "The file '{name}' could not be saved. Check permissions, the target path and whether the file is open.",
            ),
        ]
        for pattern, template in patterns:
            match = pattern.fullmatch(message)
            if match:
                return template.format(name=match.group(1))
        return message


def build_translator(language_code: str) -> Translator:
    return Translator(language_code)
