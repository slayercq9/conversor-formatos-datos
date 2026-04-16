"""Ventana auxiliar con información general de la aplicación."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from src.i18n.translations import Translator
from src.utils.constants import APP_AUTHOR, APP_LAST_UPDATED_LABEL, APP_VERSION


class AboutWindow(tk.Toplevel):
    """Muestra información resumida del proyecto en una ventana modal."""

    def __init__(self, master: tk.Misc, translator: Translator) -> None:
        super().__init__(master)
        self.translator = translator
        self.title(self.translator.t("titles.about"))
        self.resizable(False, False)
        self.transient(master)
        self.grab_set()

        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)

        header = ttk.Frame(frame)
        header.pack(fill="x")

        ttk.Label(
            header,
            text=self.translator.t("app.title"),
            font=("Segoe UI", 16, "bold"),
        ).pack(anchor="w")
        ttk.Label(
            header,
            text=self.translator.t("app.version_label", version=APP_VERSION),
            foreground="#555555",
        ).pack(anchor="w", pady=(6, 2))
        ttk.Label(
            header,
            text=self.translator.t("app.updated_label", date=APP_LAST_UPDATED_LABEL),
            foreground="#555555",
        ).pack(anchor="w")

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=14)

        ttk.Label(
            frame,
            text=self.translator.t("app.description"),
            justify="left",
            wraplength=440,
        ).pack(anchor="w")
        ttk.Label(
            frame,
            text=self.translator.t("app.author_prefix", author=APP_AUTHOR),
            justify="left",
        ).pack(anchor="w", pady=(14, 0))

        footer = ttk.Frame(frame)
        footer.pack(fill="x", pady=(18, 0))
        ttk.Button(
            footer,
            text=self.translator.t("buttons.close"),
            command=self.destroy,
            width=14,
        ).pack(anchor="e")

        self._center_on_parent(master)

    def _center_on_parent(self, master: tk.Misc) -> None:
        self.update_idletasks()
        parent_x = master.winfo_rootx()
        parent_y = master.winfo_rooty()
        parent_width = master.winfo_width()
        parent_height = master.winfo_height()
        width = self.winfo_width()
        height = self.winfo_height()
        pos_x = parent_x + max((parent_width - width) // 2, 0)
        pos_y = parent_y + max((parent_height - height) // 2, 0)
        self.geometry(f"+{pos_x}+{pos_y}")
