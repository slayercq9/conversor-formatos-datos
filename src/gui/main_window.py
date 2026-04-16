"""Ventana principal de la interfaz de usuario."""

from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import ttk

from src.core.file_types import TabularFileType
from src.core.reader import TabularReader
from src.core.validators import validate_source_path
from src.gui.about_window import AboutWindow
from src.gui.drag_drop import create_drag_drop_manager, get_main_window_base
from src.gui.dialogs import (
    ask_open_path,
    ask_save_path,
    show_error,
    show_info,
    show_warning,
)
from src.gui.help_window import HelpWindow
from src.gui.preview_table import PreviewTable
from src.gui.theme import DEFAULT_THEME, SUPPORTED_THEMES, apply_theme, apply_toplevel_theme
from src.i18n.translations import SUPPORTED_LANGUAGES, Translator, build_translator
from src.services.file_service import FileService
from src.services.preview_service import PreviewData, PreviewService
from src.utils.constants import APP_MIN_SIZE
from src.utils.errors import AppError
from src.utils.helpers import format_file_dialog_types
from src.utils.preferences import AppPreferences, PreferencesManager


class MainWindow(get_main_window_base()):
    """Coordina el flujo principal de uso desde la interfaz gráfica."""

    def __init__(self, icon_path: Path | None = None) -> None:
        super().__init__()
        self.minsize(*APP_MIN_SIZE)

        self.file_service = FileService()
        self.preview_service = PreviewService()
        self.reader = TabularReader()
        self.drag_drop_manager = create_drag_drop_manager()
        self.preferences_manager = PreferencesManager()
        self.preferences = self.preferences_manager.load()
        self.translator = build_translator(self.preferences.language_code)
        self.theme_code = (
            self.preferences.theme_code
            if self.preferences.theme_code in SUPPORTED_THEMES
            else DEFAULT_THEME
        )

        self.source_path_var = tk.StringVar()
        self.source_label_var = tk.StringVar()
        self.file_info_var = tk.StringVar()
        self.target_format_var = tk.StringVar(
            value=self.preferences.last_target_format.strip()
        )
        self.status_var = tk.StringVar()
        self.ready_to_save_var = tk.StringVar()
        self.language_var = tk.StringVar(
            value=self.translator.language_code
        )
        self.theme_var = tk.StringVar(value=self.theme_code)

        self.last_target_format = self.target_format_var.get().strip()
        self.save_button: ttk.Button | None = None
        self.drop_area: ttk.LabelFrame | None = None
        self.config_frame: ttk.LabelFrame | None = None
        self.preview_frame: ttk.LabelFrame | None = None
        self.help_button: ttk.Button | None = None
        self.about_button: ttk.Button | None = None
        self.select_button: ttk.Button | None = None
        self.preview_button: ttk.Button | None = None
        self.convert_button: ttk.Button | None = None
        self.clear_button: ttk.Button | None = None
        self.output_format_label: ttk.Label | None = None
        self.load_hint_label: ttk.Label | None = None
        self.config_hint_label: ttk.Label | None = None
        self.hero_title_label: ttk.Label | None = None
        self.hero_subtitle_label: ttk.Label | None = None
        self.language_label: ttk.Label | None = None
        self.language_pill_frame: ttk.Frame | None = None
        self.language_es_button: ttk.Radiobutton | None = None
        self.language_en_button: ttk.Radiobutton | None = None
        self.theme_label: ttk.Label | None = None
        self.theme_pill_frame: ttk.Frame | None = None
        self.theme_light_button: ttk.Radiobutton | None = None
        self.theme_dark_button: ttk.Radiobutton | None = None
        self.output_format_selector: ttk.Combobox | None = None

        self._configure_styles()
        self._configure_layout()
        self._build_content()
        self._apply_translations()
        self._apply_window_icon(icon_path)
        self._restore_window_preferences()
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _configure_styles(self) -> None:
        self._palette = apply_theme(self, self.theme_code)

    def _configure_layout(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def _build_content(self) -> None:
        container = ttk.Frame(self, padding=22)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(2, weight=1)

        header = ttk.Frame(container, style="Hero.TFrame", padding=20)
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        title_block = ttk.Frame(header, style="Hero.TFrame")
        title_block.grid(row=0, column=0, sticky="w")
        self.hero_title_label = ttk.Label(title_block, style="HeroTitle.TLabel")
        self.hero_title_label.pack(anchor="w")
        self.hero_subtitle_label = ttk.Label(title_block, style="HeroSubtitle.TLabel")
        self.hero_subtitle_label.pack(anchor="w", pady=(6, 0))

        quick_access = ttk.Frame(header, style="Toolbar.TFrame")
        quick_access.grid(row=0, column=1, sticky="e", padx=(18, 0))
        language_card = ttk.Frame(quick_access, style="SelectorCard.TFrame")
        language_card.grid(row=0, column=0, padx=(0, 12))
        self.language_label = ttk.Label(language_card, style="PillTitle.TLabel")
        self.language_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.language_pill_frame = ttk.Frame(language_card, style="PillGroup.TFrame", padding=3)
        self.language_pill_frame.grid(row=1, column=0, sticky="w")
        self.language_es_button = ttk.Radiobutton(
            self.language_pill_frame,
            variable=self.language_var,
            value="es",
            style="Pill.TRadiobutton",
            command=self._on_language_changed,
        )
        self.language_es_button.grid(row=0, column=0, sticky="ew", padx=(0, 4))
        self.language_en_button = ttk.Radiobutton(
            self.language_pill_frame,
            variable=self.language_var,
            value="en",
            style="Pill.TRadiobutton",
            command=self._on_language_changed,
        )
        self.language_en_button.grid(row=0, column=1, sticky="ew")

        theme_card = ttk.Frame(quick_access, style="SelectorCard.TFrame")
        theme_card.grid(row=0, column=1, padx=(0, 12))
        self.theme_label = ttk.Label(theme_card, style="PillTitle.TLabel")
        self.theme_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.theme_pill_frame = ttk.Frame(theme_card, style="PillGroup.TFrame", padding=3)
        self.theme_pill_frame.grid(row=1, column=0, sticky="w")
        self.theme_light_button = ttk.Radiobutton(
            self.theme_pill_frame,
            variable=self.theme_var,
            value="light",
            style="Pill.TRadiobutton",
            command=self._on_theme_changed,
        )
        self.theme_light_button.grid(row=0, column=0, sticky="ew", padx=(0, 4))
        self.theme_dark_button = ttk.Radiobutton(
            self.theme_pill_frame,
            variable=self.theme_var,
            value="dark",
            style="Pill.TRadiobutton",
            command=self._on_theme_changed,
        )
        self.theme_dark_button.grid(row=0, column=1, sticky="ew")

        self.help_button = ttk.Button(quick_access, style="Secondary.TButton", width=12, command=self.open_help)
        self.help_button.grid(row=0, column=2, padx=(0, 10))
        self.about_button = ttk.Button(quick_access, style="Secondary.TButton", width=12, command=self.open_about)
        self.about_button.grid(row=0, column=3)

        top_sections = ttk.Frame(container)
        top_sections.grid(row=1, column=0, sticky="ew", pady=(18, 14))
        top_sections.grid_columnconfigure(0, weight=3)
        top_sections.grid_columnconfigure(1, weight=2)

        self.drop_area = ttk.LabelFrame(top_sections, style="Section.TLabelframe")
        self.drop_area.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        self.drop_area.grid_columnconfigure(0, weight=1)

        self.load_hint_label = ttk.Label(
            self.drop_area,
            wraplength=700,
            justify="left",
            style="SectionHint.TLabel",
        )
        self.load_hint_label.grid(row=0, column=0, sticky="w", pady=(0, 14))

        self.select_button = ttk.Button(
            self.drop_area,
            command=self.select_source_file,
            style="Accent.TButton",
            width=18,
        )
        self.select_button.grid(row=1, column=0, sticky="w")

        ttk.Label(
            self.drop_area,
            textvariable=self.source_label_var,
            wraplength=700,
            justify="left",
            style="InfoValue.TLabel",
        ).grid(row=2, column=0, sticky="ew", pady=(14, 0))

        ttk.Label(
            self.drop_area,
            textvariable=self.file_info_var,
            wraplength=700,
            justify="left",
            style="SectionHint.TLabel",
        ).grid(row=3, column=0, sticky="ew", pady=(10, 0))

        self.config_frame = ttk.LabelFrame(top_sections, style="Section.TLabelframe")
        self.config_frame.grid(row=0, column=1, sticky="nsew")
        self.config_frame.grid_columnconfigure(0, weight=1)

        selector_row = ttk.Frame(self.config_frame, style="Surface.TFrame")
        selector_row.grid(row=0, column=0, sticky="w")

        self.output_format_label = ttk.Label(selector_row, style="Surface.TLabel")
        self.output_format_label.grid(row=0, column=0, sticky="w")
        self.output_format_selector = ttk.Combobox(
            selector_row,
            textvariable=self.target_format_var,
            values=TabularFileType.values(),
            state="readonly",
            width=10,
        )
        self.output_format_selector.grid(row=0, column=1, sticky="w", padx=(10, 0))
        self.output_format_selector.bind("<<ComboboxSelected>>", self._on_target_format_changed)

        self.config_hint_label = ttk.Label(
            self.config_frame,
            style="SectionHint.TLabel",
        )
        self.config_hint_label.grid(row=1, column=0, sticky="w", pady=(8, 0))

        actions = ttk.Frame(self.config_frame, style="Surface.TFrame")
        actions.grid(row=2, column=0, sticky="w", pady=(18, 0))

        self.preview_button = ttk.Button(actions, style="Secondary.TButton", width=14, command=self.preview_file)
        self.preview_button.pack(side="left")
        self.convert_button = ttk.Button(actions, style="Accent.TButton", width=15, command=self.convert_file)
        self.convert_button.pack(side="left", padx=(10, 0))
        self.clear_button = ttk.Button(actions, style="Secondary.TButton", width=12, command=self.clear_interface)
        self.clear_button.pack(side="left", padx=(10, 0))
        self.save_button = ttk.Button(actions, state="disabled", style="Secondary.TButton", width=18, command=self.save_converted_file)
        self.save_button.pack(side="left", padx=(10, 0))

        ttk.Label(
            self.config_frame,
            textvariable=self.ready_to_save_var,
            wraplength=460,
            justify="left",
            style="InfoValue.TLabel",
        ).grid(row=3, column=0, sticky="ew", pady=(16, 0))

        self.preview_frame = ttk.LabelFrame(container, style="Section.TLabelframe")
        self.preview_frame.grid(row=2, column=0, sticky="nsew")
        self.preview_frame.grid_rowconfigure(0, weight=1)
        self.preview_frame.grid_columnconfigure(0, weight=1)

        self.preview_table = PreviewTable(self.preview_frame)
        self.preview_table.grid(row=0, column=0, sticky="nsew")

        ttk.Label(
            container,
            textvariable=self.status_var,
            anchor="w",
            style="Status.TLabel",
        ).grid(row=3, column=0, sticky="ew", pady=(16, 0))

        self.drag_drop_manager.attach(self, self.drop_area, self.load_dropped_file)

    def _apply_window_icon(self, icon_path: Path | None) -> None:
        if icon_path is None or not icon_path.exists():
            return
        try:
            self.iconbitmap(default=str(icon_path))
        except tk.TclError:
            pass

    def _apply_translations(self) -> None:
        self.title(self.translator.t("app.title"))
        assert self.hero_title_label and self.hero_subtitle_label
        assert self.drop_area and self.config_frame and self.preview_frame
        assert self.help_button and self.about_button and self.select_button
        assert self.preview_button and self.convert_button and self.clear_button and self.save_button
        assert self.output_format_label and self.load_hint_label and self.config_hint_label
        assert self.language_label and self.theme_label
        assert self.language_es_button and self.language_en_button
        assert self.theme_light_button and self.theme_dark_button

        self.hero_title_label.config(text=self.translator.t("app.title"))
        self.hero_subtitle_label.config(text=self.translator.t("app.subtitle"))
        self.language_label.config(text=self.translator.t("app.language_label"))
        self.theme_label.config(text=self.translator.t("app.theme_label"))
        self.help_button.config(text=self.translator.t("buttons.help"))
        self.about_button.config(text=self.translator.t("buttons.about"))
        self.language_es_button.config(text=self._language_button_label("es"))
        self.language_en_button.config(text=self._language_button_label("en"))
        self.theme_light_button.config(text=self.translator.t("themes.light"))
        self.theme_dark_button.config(text=self.translator.t("themes.dark"))
        self.language_var.set(self.translator.language_code)
        self.theme_var.set(self.theme_code)
        self.drop_area.configure(text=self.translator.t("sections.load"))
        self.config_frame.configure(text=self.translator.t("sections.config"))
        self.preview_frame.configure(text=self.translator.t("sections.preview"))
        self.load_hint_label.config(text=self.translator.t("messages.load_hint"))
        self.select_button.config(text=self.translator.t("buttons.select_file"))
        self.output_format_label.config(text=self.translator.t("labels.output_format"))
        self.config_hint_label.config(text=self.translator.t("messages.config_hint"))
        self.preview_button.config(text=self.translator.t("buttons.preview"))
        self.convert_button.config(text=self.translator.t("buttons.convert"))
        self.clear_button.config(text=self.translator.t("buttons.clear"))
        self.save_button.config(text=self.translator.t("buttons.save"))

        if not self.source_path_var.get().strip():
            self._apply_empty_state_texts()
        else:
            self._refresh_loaded_file_texts()
            if self.file_service.has_prepared_conversion():
                self.ready_to_save_var.set(self.translator.t("messages.ready_conversion_ok"))
                self.status_var.set(
                    self.translator.t(
                        "messages.status_converted_ready",
                        format=self.target_format_var.get().upper(),
                    )
                )
            else:
                self.ready_to_save_var.set(self.translator.t("messages.file_loaded"))
                self.status_var.set(
                    self.translator.t(
                        "messages.status_file_selected",
                        name=Path(self.source_path_var.get()).name,
                    )
                )
    def _language_button_label(self, language_code: str) -> str:
        """Devuelve una etiqueta compacta para el selector segmentado de idioma."""
        return "ES" if language_code == "es" else "EN"

    def _apply_empty_state_texts(self) -> None:
        """Restablece textos visibles cuando no hay archivo cargado."""
        self.source_label_var.set(self.translator.t("messages.default_source_label"))
        self.file_info_var.set(self.translator.t("messages.default_file_info"))
        self.ready_to_save_var.set(self.translator.t("messages.default_ready"))
        self.status_var.set(self.translator.t("messages.default_status"))
        self.preview_table.show_message(
            self.translator.t("messages.preview_empty"),
            note_text=self.translator.t("messages.preview_idle_note"),
        )

    def _refresh_loaded_file_texts(self) -> None:
        """Actualiza el resumen visible del archivo cargado en el idioma actual."""
        self.file_info_var.set(self._build_file_summary(Path(self.source_path_var.get())))

    def _restore_window_preferences(self) -> None:
        width = self.preferences.window_width
        height = self.preferences.window_height
        pos_x = self.preferences.window_x
        pos_y = self.preferences.window_y

        if width and height and width >= APP_MIN_SIZE[0] and height >= APP_MIN_SIZE[1]:
            geometry = f"{width}x{height}"
            if pos_x is not None and pos_y is not None:
                geometry += f"+{pos_x}+{pos_y}"
            self.geometry(geometry)

    def _on_language_changed(self, _: tk.Event[tk.Misc] | None = None) -> None:
        language_code = self.language_var.get().strip()
        if language_code not in SUPPORTED_LANGUAGES:
            language_code = "es"
        self.translator = build_translator(language_code)
        self._apply_translations()
        if self.source_path_var.get().strip():
            self._refresh_preview_from_source()

    def _on_theme_changed(self, _: tk.Event[tk.Misc] | None = None) -> None:
        selected_theme = self.theme_var.get().strip()
        self._apply_selected_theme(selected_theme)

    def _apply_selected_theme(self, theme_code: str) -> None:
        """Actualiza la paleta activa sin alterar la logica funcional."""
        self.theme_code = theme_code if theme_code in SUPPORTED_THEMES else DEFAULT_THEME
        self._palette = apply_theme(self, self.theme_code)
        self.theme_var.set(self.theme_code)
        self._apply_theme_to_open_windows()

    def _apply_theme_to_open_windows(self) -> None:
        """Propaga el color base a ventanas secundarias ya abiertas."""
        for child in self.winfo_children():
            if isinstance(child, tk.Toplevel):
                apply_toplevel_theme(child, self.theme_code)

    def _on_target_format_changed(self, _: tk.Event[tk.Misc] | None = None) -> None:
        self.last_target_format = self.target_format_var.get().strip()
        self.file_service.clear_prepared_conversion()
        self._set_save_enabled(False)
        self.ready_to_save_var.set(self.translator.t("messages.ready_format_updated"))
        self.status_var.set(self.translator.t("messages.status_format_updated"))

    def select_source_file(self) -> None:
        path = ask_open_path(
            format_file_dialog_types(self.translator.language_code),
            title=self.translator.t("titles.open_file"),
        )
        if path:
            try:
                self._load_source_file(path, refresh_preview=False)
            except AppError as exc:
                show_error(self.translator.t("titles.file"), self._localize_error(exc))
                self.status_var.set(self.translator.t("messages.status_preview_failed"))
        else:
            self.status_var.set(self.translator.t("messages.status_selection_canceled"))

    def load_dropped_file(self, source_path: Path) -> None:
        try:
            self._load_source_file(source_path, refresh_preview=True)
            self.status_var.set(
                self.translator.t("messages.status_file_dropped", name=source_path.name)
            )
        except AppError as exc:
            show_error(self.translator.t("titles.drag_drop"), self._localize_error(exc))
            self.preview_table.show_message(
                self.translator.t("messages.drop_error_preview"),
                note_text=self.translator.t("messages.preview_idle_note"),
            )
            self.status_var.set(self.translator.t("messages.status_drop_invalid"))

    def _load_source_file(self, source_path: str | Path, refresh_preview: bool) -> None:
        validated_path = validate_source_path(source_path)
        path_text = str(validated_path)

        self.source_path_var.set(path_text)
        self.source_label_var.set(path_text)
        self.file_info_var.set(self._build_file_summary(validated_path))
        self.file_service.clear_prepared_conversion()
        self._set_save_enabled(False)
        self.ready_to_save_var.set(self.translator.t("messages.file_loaded"))
        self.status_var.set(
            self.translator.t("messages.status_file_selected", name=validated_path.name)
        )

        if refresh_preview:
            self._refresh_preview_from_source()
        else:
            self.preview_table.show_message(
                self.translator.t("messages.file_loaded_preview_hint"),
                note_text=self.translator.t("messages.preview_idle_note"),
            )

    def preview_file(self) -> None:
        if not self._ensure_source_selected():
            return

        try:
            preview = self.preview_service.load_preview(self.source_path_var.get())
        except AppError as exc:
            show_error(self.translator.t("titles.preview"), self._localize_error(exc))
            self.preview_table.show_message(
                self.translator.t("messages.preview_build_failed"),
                note_text=self.translator.t("messages.preview_idle_note"),
            )
            self.status_var.set(self.translator.t("messages.status_preview_failed"))
            return

        self._render_preview(preview)
        self.status_var.set(self._build_preview_summary(preview))

    def convert_file(self) -> None:
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
            show_error(self.translator.t("titles.conversion"), self._localize_error(exc))
            self.status_var.set(self.translator.t("messages.status_conversion_failed"))
            self.file_service.clear_prepared_conversion()
            self._set_save_enabled(False)
            self.ready_to_save_var.set(self.translator.t("messages.ready_conversion_failed"))
            return

        self._set_save_enabled(True)
        self.ready_to_save_var.set(self.translator.t("messages.ready_conversion_ok"))
        self.status_var.set(
            self.translator.t(
                "messages.status_converted_ready",
                format=prepared_conversion.target_format.value.upper(),
            )
        )
        self._refresh_preview_after_conversion()

    def save_converted_file(self) -> None:
        if not self.file_service.has_prepared_conversion():
            show_info(
                self.translator.t("titles.save"),
                self.translator.t("messages.dialog_save_prepare_first"),
            )
            self.status_var.set(self.translator.t("messages.status_save_prepare_first"))
            return
        if not self._ensure_target_format_selected():
            return

        default_path = self.file_service.build_default_output_path(
            self.source_path_var.get(),
            self.target_format_var.get(),
        )
        target_path = ask_save_path(
            default_path,
            format_file_dialog_types(self.translator.language_code),
            title=self.translator.t("titles.save_file"),
        )
        if not target_path:
            self.status_var.set(self.translator.t("messages.status_save_canceled"))
            return

        try:
            result_path = self.file_service.save_prepared_conversion(target_path)
        except AppError as exc:
            show_error(self.translator.t("titles.save"), self._localize_error(exc))
            self.status_var.set(self.translator.t("messages.status_save_failed"))
            return

        show_info(
            self.translator.t("titles.save_completed"),
            self.translator.t(
                "messages.save_completed_dialog",
                source_name=Path(self.source_path_var.get()).name,
                target_format=self.target_format_var.get().upper(),
                result_path=result_path,
            ),
        )
        self.status_var.set(
            self.translator.t("messages.status_saved", name=Path(result_path).name)
        )
        self.ready_to_save_var.set(self.translator.t("messages.ready_conversion_saved"))

    def open_about(self) -> None:
        AboutWindow(self, self.translator, self.theme_code)

    def open_help(self) -> None:
        HelpWindow(self, self.translator, self.theme_code)

    def _ensure_source_selected(self) -> bool:
        if self.source_path_var.get().strip():
            return True

        self.preview_table.show_message(
            self.translator.t("messages.dialog_file_required"),
            note_text=self.translator.t("messages.preview_idle_note"),
        )
        show_warning(
            self.translator.t("titles.file_required"),
            self.translator.t("messages.dialog_file_required"),
        )
        self.status_var.set(self.translator.t("messages.status_waiting_file"))
        return False

    def _ensure_target_format_selected(self) -> bool:
        if self.target_format_var.get().strip():
            return True

        show_warning(
            self.translator.t("titles.format_required"),
            self.translator.t("messages.dialog_format_required"),
        )
        self.status_var.set(self.translator.t("messages.status_waiting_format"))
        return False

    def _refresh_preview_after_conversion(self) -> None:
        self._refresh_preview_from_source()

    def _refresh_preview_from_source(self) -> None:
        try:
            preview = self.preview_service.load_preview(self.source_path_var.get())
        except AppError:
            self.preview_table.show_message(
                self.translator.t("messages.preview_refresh_failed"),
                note_text=self.translator.t("messages.preview_idle_note"),
            )
            self.status_var.set(self.translator.t("messages.status_preview_refresh_failed"))
            return

        self._render_preview(preview)

    def _render_preview(self, preview: PreviewData) -> None:
        self.preview_table.update_data(
            preview,
            summary_text=self._build_preview_summary(preview),
            note_text=self._build_preview_note(preview),
            empty_message=self.translator.t("messages.preview_no_rows")
            if preview.columns
            else self.translator.t("messages.preview_no_columns"),
        )

    def _build_preview_summary(self, preview: PreviewData) -> str:
        column_label = self._pluralize(
            preview.total_columns,
            "meta.column_label_singular",
            "meta.column_label_plural",
        )
        row_label = self._pluralize(
            preview.previewed_rows,
            "meta.row_label_singular",
            "meta.row_label_plural",
        )
        summary = self.translator.t(
            "messages.preview_summary",
            columns=preview.total_columns,
            column_label=column_label,
            rows=preview.previewed_rows,
            row_label=row_label,
        )
        if preview.is_partial:
            return self.translator.t(
                "messages.preview_summary_partial",
                summary=summary,
                total=preview.total_rows,
            )
        return summary

    def _build_preview_note(self, preview: PreviewData) -> str:
        if preview.is_partial:
            return self.translator.t("messages.preview_note_partial")
        return self.translator.t("messages.preview_note_complete")

    def _pluralize(self, value: int, singular_key: str, plural_key: str) -> str:
        if value == 1:
            return self.translator.t(singular_key)
        return self.translator.t(plural_key)

    def _localize_error(self, error: AppError) -> str:
        return self.translator.translate_runtime_message(str(error))

    def _set_save_enabled(self, enabled: bool) -> None:
        if self.save_button is None:
            return
        self.save_button.config(state="normal" if enabled else "disabled")

    def clear_interface(self) -> None:
        self.source_path_var.set("")
        self.target_format_var.set("")
        self.file_service.clear_prepared_conversion()
        self._set_save_enabled(False)
        self.source_label_var.set(self.translator.t("messages.default_source_label"))
        self.file_info_var.set(self.translator.t("messages.default_file_info"))
        self.ready_to_save_var.set(self.translator.t("messages.default_ready"))
        self.preview_table.show_message(
            self.translator.t("messages.clear_preview_message"),
            note_text=self.translator.t("messages.preview_idle_note"),
        )
        self.status_var.set(self.translator.t("messages.status_clean"))

    def _build_file_summary(self, source_path: Path) -> str:
        extension = source_path.suffix.lower() or self.translator.t("meta.without_extension")
        details = [
            f"{self.translator.t('labels.file_name')}: {source_path.name}",
            f"{self.translator.t('labels.file_extension')}: {extension}",
            f"{self.translator.t('labels.file_size')}: {self._format_file_size(source_path.stat().st_size)}",
        ]
        row_count = self._try_get_row_count(source_path)
        if row_count is not None:
            details.append(f"{self.translator.t('labels.file_rows')}: {row_count}")
        return " | ".join(details)

    def _try_get_row_count(self, source_path: Path) -> int | None:
        try:
            data_frame = self.reader.read(source_path)
        except AppError:
            return None
        return len(data_frame.index)

    def _format_file_size(self, size_in_bytes: int) -> str:
        size = float(size_in_bytes)
        units = ("B", "KB", "MB", "GB")
        for unit in units:
            if size < 1024 or unit == units[-1]:
                if unit == "B":
                    return f"{int(size)} {unit}"
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size_in_bytes} B"

    def _capture_preferences(self) -> AppPreferences:
        self.update_idletasks()
        return AppPreferences(
            last_target_format=self.last_target_format,
            language_code=self.translator.language_code,
            theme_code=self.theme_code,
            window_width=self.winfo_width(),
            window_height=self.winfo_height(),
            window_x=self.winfo_x(),
            window_y=self.winfo_y(),
        )

    def _on_close(self) -> None:
        self.preferences_manager.save(self._capture_preferences())
        self.destroy()
