"""Ventana principal de la interfaz de usuario.

Este modulo compone los widgets principales y delega la logica real de
conversion y vista previa a servicios especializados.
"""

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
    """Coordina el flujo principal de uso desde la interfaz grafica."""

    def __init__(self) -> None:
        """Inicializa estado visual, servicios y puntos de extension futuros."""
        super().__init__()
        self.title(APP_TITLE)
        self.minsize(*APP_MIN_SIZE)

        self.file_service = FileService()
        self.preview_service = PreviewService()
        self.drag_drop_manager = NullDragDropManager()

        self.source_path_var = tk.StringVar()
        self.source_label_var = tk.StringVar(value="Ningun archivo cargado todavia.")
        self.target_format_var = tk.StringVar(value="")
        self.status_var = tk.StringVar(value="Selecciona un archivo para comenzar.")
        self.ready_to_save_var = tk.StringVar(
            value="Todavia no hay una conversion lista para guardar."
        )
        self.save_button: ttk.Button | None = None
        self.drop_area: ttk.LabelFrame | None = None

        self._configure_styles()
        self._configure_layout()
        self._build_content()
        # TODO: Reemplazar NullDragDropManager por una implementacion real.
        self.drag_drop_manager.attach(self, self.drop_area)

    def _configure_styles(self) -> None:
        """Define una paleta visual sobria y estilos reutilizables."""
        palette = {
            "bg": "#dfe8f6",
            "surface": "#f8fbff",
            "surface_alt": "#edf3fb",
            "border": "#93a7c0",
            "border_soft": "#c0cede",
            "text": "#1f2d3d",
            "muted": "#5e6d7d",
            "accent": "#3f78b5",
            "accent_hover": "#2f6297",
            "accent_light": "#eaf2fc",
        }
        self._palette = palette

        self.configure(background=palette["bg"])
        style = ttk.Style(self)
        if "clam" in style.theme_names():
            style.theme_use("clam")

        style.configure("TFrame", background=palette["bg"])
        style.configure("Surface.TFrame", background=palette["surface"])
        style.configure(
            "Hero.TFrame",
            background=palette["surface"],
            relief="raised",
            borderwidth=1,
            lightcolor="#ffffff",
            darkcolor=palette["border"],
        )
        style.configure(
            "Card.TLabelframe",
            background=palette["surface"],
            bordercolor=palette["border"],
            relief="raised",
            borderwidth=1,
            padding=14,
        )
        style.configure(
            "Card.TLabelframe.Label",
            background=palette["surface"],
            foreground=palette["text"],
            font=("Segoe UI", 10, "bold"),
        )
        style.configure("TLabel", background=palette["bg"], foreground=palette["text"])
        style.configure(
            "Surface.TLabel",
            background=palette["surface"],
            foreground=palette["text"],
        )
        style.configure(
            "HeroTitle.TLabel",
            background=palette["surface"],
            foreground=palette["text"],
            font=("Segoe UI", 18, "bold"),
        )
        style.configure(
            "HeroSubtitle.TLabel",
            background=palette["surface"],
            foreground=palette["muted"],
            font=("Segoe UI", 10),
        )
        style.configure(
            "SectionHint.TLabel",
            background=palette["surface"],
            foreground=palette["muted"],
            font=("Segoe UI", 9),
        )
        style.configure(
            "InfoValue.TLabel",
            background=palette["surface_alt"],
            foreground=palette["text"],
            font=("Segoe UI", 9),
            padding=(10, 8),
            relief="sunken",
            borderwidth=1,
        )
        style.configure(
            "Status.TLabel",
            background=palette["surface_alt"],
            foreground=palette["muted"],
            font=("Segoe UI", 9),
            padding=(12, 9),
            relief="sunken",
            borderwidth=1,
        )
        style.configure(
            "Toolbar.TFrame",
            background=palette["surface"],
        )
        style.configure(
            "TButton",
            padding=(12, 7),
            font=("Segoe UI", 9),
            relief="raised",
            borderwidth=1,
            focusthickness=1,
            focuscolor=palette["border_soft"],
        )
        style.configure(
            "Accent.TButton",
            background=palette["accent"],
            foreground="#ffffff",
            borderwidth=1,
            lightcolor="#7ea7d5",
            darkcolor="#2a5077",
        )
        style.map(
            "Accent.TButton",
            background=[("active", palette["accent_hover"]), ("disabled", "#9fb3c1")],
            foreground=[("disabled", "#f4f7fa")],
        )
        style.configure(
            "Secondary.TButton",
            background=palette["accent_light"],
            foreground=palette["text"],
            bordercolor=palette["border"],
            lightcolor="#ffffff",
            darkcolor=palette["border"],
        )
        style.map(
            "Secondary.TButton",
            background=[("active", "#dce9f8")],
        )
        style.configure(
            "Preview.Treeview",
            background=palette["surface"],
            fieldbackground=palette["surface"],
            foreground=palette["text"],
            bordercolor=palette["border"],
            rowheight=28,
        )
        style.configure(
            "Preview.Treeview.Heading",
            background=palette["surface_alt"],
            foreground=palette["text"],
            font=("Segoe UI", 9, "bold"),
            relief="raised",
            padding=(8, 6),
        )
        style.map(
            "Preview.Treeview.Heading",
            background=[("active", "#e4ebf1")],
        )

    def _configure_layout(self) -> None:
        """Configura el contenedor raiz para permitir redimensionamiento."""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _build_content(self) -> None:
        """Construye los bloques visuales principales de la ventana."""
        container = ttk.Frame(self, padding=22)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(2, weight=1)

        header = ttk.Frame(container, style="Hero.TFrame", padding=18)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        title_block = ttk.Frame(header, style="Hero.TFrame")
        title_block.grid(row=0, column=0, sticky="w")
        ttk.Label(title_block, text=APP_TITLE, style="HeroTitle.TLabel").pack(
            anchor="w"
        )
        ttk.Label(
            title_block,
            text="Convierte archivos tabulares y revisa una vista previa antes de guardarlos.",
            style="HeroSubtitle.TLabel",
        ).pack(anchor="w", pady=(4, 0))

        quick_access = ttk.Frame(header, style="Toolbar.TFrame", padding=(0, 2, 0, 2))
        quick_access.grid(row=0, column=1, sticky="e")
        ttk.Button(
            quick_access,
            text="Como usar",
            command=self.open_help,
            style="Secondary.TButton",
        ).grid(row=0, column=0, padx=(0, 10))
        ttk.Button(
            quick_access,
            text="Acerca de",
            command=self.open_about,
            style="Secondary.TButton",
        ).grid(row=0, column=1)

        top_sections = ttk.Frame(container)
        top_sections.grid(row=1, column=0, sticky="ew", pady=(18, 14))
        top_sections.grid_columnconfigure(0, weight=3)
        top_sections.grid_columnconfigure(1, weight=2)

        self.drop_area = ttk.LabelFrame(
            top_sections,
            text="Carga de archivo",
            style="Card.TLabelframe",
        )
        self.drop_area.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        self.drop_area.grid_columnconfigure(0, weight=1)
        self.drop_area.grid_columnconfigure(1, weight=0)

        ttk.Label(
            self.drop_area,
            text="Selecciona un archivo desde el explorador. El soporte drag and drop quedo listo para integrarse aqui mas adelante.",
            wraplength=760,
            justify="left",
            style="SectionHint.TLabel",
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 14))

        ttk.Button(
            self.drop_area,
            text="Seleccionar archivo",
            command=self.select_source_file,
            style="Accent.TButton",
        ).grid(row=1, column=0, sticky="w")

        ttk.Label(
            self.drop_area,
            textvariable=self.source_label_var,
            wraplength=760,
            justify="left",
            style="InfoValue.TLabel",
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(14, 0))

        config_frame = ttk.LabelFrame(
            top_sections,
            text="Configuracion",
            style="Card.TLabelframe",
        )
        config_frame.grid(row=0, column=1, sticky="nsew")
        config_frame.grid_columnconfigure(1, weight=1)

        ttk.Label(config_frame, text="Formato de salida", style="Surface.TLabel").grid(
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

        ttk.Label(
            config_frame,
            text="Selecciona un formato antes de convertir.",
            style="SectionHint.TLabel",
        ).grid(row=0, column=2, sticky="w", padx=(12, 0))

        actions = ttk.Frame(config_frame, style="Surface.TFrame")
        actions.grid(row=1, column=0, columnspan=3, sticky="w", pady=(18, 0))

        ttk.Button(
            actions,
            text="Vista previa",
            command=self.preview_file,
            style="Secondary.TButton",
        ).pack(
            side="left"
        )
        ttk.Button(
            actions,
            text="Convertir",
            command=self.convert_file,
            style="Accent.TButton",
        ).pack(
            side="left",
            padx=(8, 0),
        )
        self.save_button = ttk.Button(
            actions,
            text="Guardar convertido",
            command=self.save_converted_file,
            state="disabled",
            style="Secondary.TButton",
        )
        self.save_button.pack(side="left", padx=(8, 0))

        ttk.Label(
            config_frame,
            textvariable=self.ready_to_save_var,
            wraplength=760,
            justify="left",
            style="InfoValue.TLabel",
        ).grid(row=2, column=0, columnspan=3, sticky="ew", pady=(16, 0))

        preview_frame = ttk.LabelFrame(
            container,
            text="Vista previa",
            style="Card.TLabelframe",
        )
        preview_frame.grid(row=2, column=0, sticky="nsew")
        preview_frame.grid_rowconfigure(0, weight=1)
        preview_frame.grid_columnconfigure(0, weight=1)

        self.preview_table = PreviewTable(preview_frame)
        self.preview_table.grid(row=0, column=0, sticky="nsew")

        ttk.Label(
            container,
            textvariable=self.status_var,
            anchor="w",
            style="Status.TLabel",
        ).grid(row=3, column=0, sticky="ew", pady=(14, 0))

    def _on_target_format_changed(self, _: tk.Event[tk.Misc] | None = None) -> None:
        """Limpia el estado pendiente al cambiar el formato de salida."""
        self.file_service.clear_prepared_conversion()
        self._set_save_enabled(False)
        self.ready_to_save_var.set(
            "Selecciona Convertir para preparar el archivo en el formato elegido."
        )
        self.status_var.set("Formato de salida actualizado.")

    def select_source_file(self) -> None:
        """Abre el selector de archivos y actualiza el estado visual."""
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
        else:
            self.status_var.set("No se selecciono ningun archivo.")

    def preview_file(self) -> None:
        """Carga una vista previa de las primeras filas del archivo."""
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
        """Prepara la conversion en memoria sin escribir todavia a disco."""
        if not self._ensure_source_selected():
            return
        if not self._ensure_target_format_selected():
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
        """Solicita una ruta y guarda el archivo convertido preparado."""
        if not self.file_service.has_prepared_conversion():
            show_info(
                "Guardar archivo",
                "Primero usa el boton Convertir para preparar el archivo.",
            )
            self.status_var.set("Aun no hay una conversion lista para guardar.")
            return
        if not self._ensure_target_format_selected():
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
        """Abre la ventana informativa 'Acerca de'."""
        AboutWindow(self)

    def open_help(self) -> None:
        """Abre la ventana informativa 'Como usar'."""
        HelpWindow(self)

    def _ensure_source_selected(self) -> bool:
        """Valida desde la GUI que exista un archivo elegido por el usuario."""
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

    def _ensure_target_format_selected(self) -> bool:
        """Valida desde la GUI que haya un formato de salida seleccionado."""
        if self.target_format_var.get().strip():
            return True

        show_warning(
            "Formato requerido",
            "Todavia no has elegido un formato de salida. Selecciona uno para continuar.",
        )
        self.status_var.set("Esperando seleccion del formato de salida.")
        return False

    def _refresh_preview_after_conversion(self) -> None:
        """Refresca la vista previa luego de preparar la conversion."""
        try:
            columns, rows = self.preview_service.load_preview(self.source_path_var.get())
        except AppError:
            self.preview_table.show_message(
                "La conversion quedo preparada, pero la vista previa no se pudo actualizar."
            )
            return

        self.preview_table.update_data(columns, rows)

    def _set_save_enabled(self, enabled: bool) -> None:
        """Activa o desactiva el boton de guardado segun el estado actual."""
        if self.save_button is None:
            return
        self.save_button.config(state="normal" if enabled else "disabled")
