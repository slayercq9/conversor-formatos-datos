from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import ttk

from src.core.file_types import TabularFileType
from src.future.drag_drop import NullDragDropManager
from src.gui.about_window import AboutWindow
from src.gui.dialogs import ask_open_path, ask_save_path, show_error, show_info
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
        self.target_format_var = tk.StringVar(value=TabularFileType.CSV.value)
        self.status_var = tk.StringVar(value="Selecciona un archivo para comenzar.")

        self._configure_layout()
        self._build_menu()
        self._build_content()
        self.drag_drop_manager.attach(self)

    def _configure_layout(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _build_menu(self) -> None:
        menu = tk.Menu(self)

        help_menu = tk.Menu(menu, tearoff=False)
        help_menu.add_command(label="Ayuda", command=self.open_help)
        help_menu.add_command(label="Acerca de", command=self.open_about)

        menu.add_cascade(label="Informacion", menu=help_menu)
        self.config(menu=menu)

    def _build_content(self) -> None:
        container = ttk.Frame(self, padding=16)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_columnconfigure(1, weight=1)
        container.grid_rowconfigure(3, weight=1)

        ttk.Label(container, text="Archivo de entrada").grid(row=0, column=0, sticky="w")
        ttk.Entry(container, textvariable=self.source_path_var).grid(
            row=0,
            column=1,
            sticky="ew",
            padx=(8, 8),
        )
        ttk.Button(container, text="Examinar", command=self.select_source_file).grid(
            row=0,
            column=2,
            sticky="ew",
        )

        ttk.Label(container, text="Formato de salida").grid(row=1, column=0, sticky="w", pady=(12, 0))
        ttk.Combobox(
            container,
            textvariable=self.target_format_var,
            values=TabularFileType.values(),
            state="readonly",
        ).grid(row=1, column=1, sticky="w", padx=(8, 8), pady=(12, 0))

        actions = ttk.Frame(container)
        actions.grid(row=2, column=0, columnspan=3, sticky="w", pady=(16, 12))

        ttk.Button(actions, text="Previsualizar", command=self.preview_file).pack(side="left")
        ttk.Button(actions, text="Convertir", command=self.convert_file).pack(side="left", padx=(8, 0))

        self.preview_table = PreviewTable(container)
        self.preview_table.grid(row=3, column=0, columnspan=3, sticky="nsew")

        ttk.Label(
            container,
            textvariable=self.status_var,
            anchor="w",
        ).grid(row=4, column=0, columnspan=3, sticky="ew", pady=(12, 0))

    def select_source_file(self) -> None:
        path = ask_open_path(format_file_dialog_types())
        if path:
            self.source_path_var.set(path)
            self.status_var.set(f"Archivo seleccionado: {Path(path).name}")

    def preview_file(self) -> None:
        try:
            columns, rows = self.preview_service.load_preview(self.source_path_var.get())
        except AppError as exc:
            show_error("Vista previa", str(exc))
            self.status_var.set("No se pudo generar la vista previa.")
            return

        self.preview_table.update_data(columns, rows)
        self.status_var.set(f"Vista previa cargada con {len(rows)} filas.")

    def convert_file(self) -> None:
        source_path = self.source_path_var.get()
        target_format = self.target_format_var.get()

        try:
            default_path = self.file_service.build_default_output_path(source_path, target_format)
            target_path = ask_save_path(default_path, format_file_dialog_types())
            if not target_path:
                self.status_var.set("Conversion cancelada por el usuario.")
                return

            result_path = self.file_service.convert_file(source_path, target_path, target_format)
        except AppError as exc:
            show_error("Conversion", str(exc))
            self.status_var.set("La conversion fallo.")
            return

        message = f"Archivo convertido correctamente:\n{result_path}"
        show_info("Conversion completada", message)
        self.status_var.set(f"Conversion completada: {Path(result_path).name}")

    def open_about(self) -> None:
        AboutWindow(self)

    def open_help(self) -> None:
        HelpWindow(self)
