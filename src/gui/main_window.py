from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import ttk

from src.core.file_types import TabularFileType
from src.future.drag_drop import NullDragDropManager
from src.gui.about_window import AboutWindow
from src.gui.dialogs import (
    ask_open_path,
    ask_save_path,
    show_error,
    show_info,
    show_warning,
)
from src.gui.help_window import HelpWindow
from src.gui.preview_table import PreviewTable
from src.services.file_service import FileService
from src.services.preview_service import PreviewService
from src.utils.constants import APP_MIN_SIZE, APP_TITLE
from src.utils.errors import AppError
from src.utils.helpers import format_file_dialog_types


class MainWindow(tk.Tk):
    """Ventana principal del conversor."""

    def __init__(self) -> None:
        super().__init__()
        self.title(APP_TITLE)
        self.minsize(*APP_MIN_SIZE)

        self.file_service = FileService()
        self.preview_service = PreviewService()
        self.drag_drop_manager = NullDragDropManager()

        self.source_path_var = tk.StringVar()
        self.source_label_var = tk.StringVar(value="Ningun archivo cargado todavia.")
        self.target_format_var = tk.StringVar(value=TabularFileType.CSV.value)
        self.status_var = tk.StringVar(value="Selecciona un archivo para comenzar.")
        self.ready_to_save_var = tk.StringVar(
            value="Todavia no hay una conversion lista para guardar."
        )
        self.save_button: ttk.Button | None = None
        self.drop_area: ttk.LabelFrame | None = None

        self._configure_layout()
        self._build_menu()
        self._build_content()
        self.drag_drop_manager.attach(self, self.drop_area)

    def _configure_layout(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _build_menu(self) -> None:
        menu = tk.Menu(self)

        help_menu = tk.Menu(menu, tearoff=False)
        help_menu.add_command(label="Como usar", command=self.open_help)
        help_menu.add_command(label="Acerca de", command=self.open_about)

        menu.add_cascade(label="Informacion", menu=help_menu)
        self.config(menu=menu)

    def _build_content(self) -> None:
        container = ttk.Frame(self, padding=16)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(3, weight=1)

        header = ttk.Frame(container)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        title_block = ttk.Frame(header)
        title_block.grid(row=0, column=0, sticky="w")
        ttk.Label(title_block, text=APP_TITLE, font=("Segoe UI", 16, "bold")).pack(
            anchor="w"
        )
        ttk.Label(
            title_block,
            text="Convierte archivos tabulares y revisa una vista previa antes de guardarlos.",
        ).pack(anchor="w", pady=(4, 0))

        quick_access = ttk.Frame(header)
        quick_access.grid(row=0, column=1, sticky="e")
        ttk.Button(quick_access, text="Como usar", command=self.open_help).pack(
            side="left"
        )
        ttk.Button(quick_access, text="Acerca de", command=self.open_about).pack(
            side="left",
            padx=(8, 0),
        )

        self.drop_area = ttk.LabelFrame(container, text="Carga de archivo")
        self.drop_area.grid(row=1, column=0, sticky="ew", pady=(16, 12))
        self.drop_area.grid_columnconfigure(0, weight=1)
        self.drop_area.grid_columnconfigure(1, weight=0)

        ttk.Label(
            self.drop_area,
            text="Selecciona un archivo desde el explorador. El soporte drag and drop quedo listo para integrarse aqui mas adelante.",
            wraplength=760,
            justify="left",
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 12))

        ttk.Button(
            self.drop_area,
            text="Seleccionar archivo",
            command=self.select_source_file,
        ).grid(row=1, column=0, sticky="w")

        ttk.Label(
            self.drop_area,
            textvariable=self.source_label_var,
            foreground="#444444",
            wraplength=760,
            justify="left",
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(10, 0))

        config_frame = ttk.LabelFrame(container, text="Configuracion")
        config_frame.grid(row=2, column=0, sticky="ew", pady=(0, 12))
        config_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(config_frame, text="Formato de salida").grid(
            row=0,
            column=0,
            sticky="w",
        )
        format_selector = ttk.Combobox(
            config_frame,
            textvariable=self.target_format_var,
            values=TabularFileType.values(),
            state="readonly",
            width=18,
        )
        format_selector.grid(row=0, column=1, sticky="w", padx=(8, 0))
        format_selector.bind("<<ComboboxSelected>>", self._on_target_format_changed)

        actions = ttk.Frame(config_frame)
        actions.grid(row=1, column=0, columnspan=2, sticky="w", pady=(16, 0))

        ttk.Button(actions, text="Vista previa", command=self.preview_file).pack(
            side="left"
        )
        ttk.Button(actions, text="Convertir", command=self.convert_file).pack(
            side="left",
            padx=(8, 0),
        )
        self.save_button = ttk.Button(
            actions,
            text="Guardar convertido",
            command=self.save_converted_file,
            state="disabled",
        )
        self.save_button.pack(side="left", padx=(8, 0))

        ttk.Label(
            config_frame,
            textvariable=self.ready_to_save_var,
            foreground="#444444",
            wraplength=760,
            justify="left",
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(12, 0))

        preview_frame = ttk.LabelFrame(container, text="Vista previa")
        preview_frame.grid(row=3, column=0, sticky="nsew")
        preview_frame.grid_rowconfigure(0, weight=1)
        preview_frame.grid_columnconfigure(0, weight=1)

        self.preview_table = PreviewTable(preview_frame)
        self.preview_table.grid(row=0, column=0, sticky="nsew")

        ttk.Label(
            container,
            textvariable=self.status_var,
            anchor="w",
        ).grid(row=4, column=0, sticky="ew", pady=(12, 0))

    def _on_target_format_changed(self, _: tk.Event[tk.Misc] | None = None) -> None:
        self.file_service.clear_prepared_conversion()
        self._set_save_enabled(False)
        self.ready_to_save_var.set(
            "Selecciona Convertir para preparar el archivo en el formato elegido."
        )

    def select_source_file(self) -> None:
        path = ask_open_path(format_file_dialog_types())
        if path:
            self.source_path_var.set(path)
            self.source_label_var.set(path)
            self.file_service.clear_prepared_conversion()
            self._set_save_enabled(False)
            self.ready_to_save_var.set(
                "Archivo cargado. Puedes revisar la vista previa o preparar la conversion."
            )
            self.preview_table.show_message(
                "Archivo cargado. Usa Vista previa para revisar los datos."
            )
            self.status_var.set(f"Archivo seleccionado: {Path(path).name}")

    def preview_file(self) -> None:
        if not self._ensure_source_selected():
            return

        try:
            columns, rows = self.preview_service.load_preview(self.source_path_var.get())
        except AppError as exc:
            show_error("Vista previa", str(exc))
            self.status_var.set("No se pudo generar la vista previa.")
            return

        self.preview_table.update_data(columns, rows)
        self.status_var.set(f"Vista previa cargada con {len(rows)} filas.")

    def convert_file(self) -> None:
        if not self._ensure_source_selected():
            return

        try:
            prepared_conversion = self.file_service.prepare_conversion(
                self.source_path_var.get(),
                self.target_format_var.get(),
            )
        except AppError as exc:
            show_error("Conversion", str(exc))
            self.status_var.set("La conversion fallo.")
            self.file_service.clear_prepared_conversion()
            self._set_save_enabled(False)
            self.ready_to_save_var.set(
                "No se pudo preparar la conversion. Revisa el archivo y vuelve a intentar."
            )
            return

        self._set_save_enabled(True)
        self.ready_to_save_var.set(
            "Conversion preparada. Ya puedes guardar el archivo convertido."
        )
        self.status_var.set(
            f"Conversion lista a {prepared_conversion.target_format.value.upper()}."
        )
        self._refresh_preview_after_conversion()

    def save_converted_file(self) -> None:
        if not self.file_service.has_prepared_conversion():
            show_info(
                "Guardar archivo",
                "Primero usa el boton Convertir para preparar el archivo.",
            )
            self.status_var.set("Aun no hay una conversion lista para guardar.")
            return

        default_path = self.file_service.build_default_output_path(
            self.source_path_var.get(),
            self.target_format_var.get(),
        )
        target_path = ask_save_path(default_path, format_file_dialog_types())
        if not target_path:
            self.status_var.set("Guardado cancelado por el usuario.")
            return

        try:
            result_path = self.file_service.save_prepared_conversion(target_path)
        except AppError as exc:
            show_error("Guardar archivo", str(exc))
            self.status_var.set("No se pudo guardar el archivo convertido.")
            return

        show_info(
            "Archivo guardado",
            f"El archivo convertido se guardo correctamente en:\n{result_path}",
        )
        self.status_var.set(f"Archivo guardado: {Path(result_path).name}")
        self.ready_to_save_var.set(
            "Archivo guardado. Puedes cambiar el formato o convertir otro archivo."
        )

    def open_about(self) -> None:
        AboutWindow(self)

    def open_help(self) -> None:
        HelpWindow(self)

    def _ensure_source_selected(self) -> bool:
        if self.source_path_var.get().strip():
            return True

        self.preview_table.show_message(
            "Todavia no hay un archivo cargado. Selecciona uno para continuar."
        )
        show_warning(
            "Archivo requerido",
            "Todavia no has cargado un archivo. Usa 'Seleccionar archivo' para continuar.",
        )
        self.status_var.set("Esperando un archivo de entrada.")
        return False

    def _refresh_preview_after_conversion(self) -> None:
        try:
            columns, rows = self.preview_service.load_preview(self.source_path_var.get())
        except AppError:
            self.preview_table.show_message(
                "La conversion quedo preparada, pero la vista previa no se pudo actualizar."
            )
            return

        self.preview_table.update_data(columns, rows)

    def _set_save_enabled(self, enabled: bool) -> None:
        if self.save_button is None:
            return
        self.save_button.config(state="normal" if enabled else "disabled")
