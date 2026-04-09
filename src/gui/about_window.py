from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from src.utils.constants import ABOUT_TEXT, APP_TITLE, APP_VERSION


class AboutWindow(tk.Toplevel):
    """Ventana simple de informacion de la aplicacion."""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.title("Acerca de")
        self.resizable(False, False)
        self.transient(master)
        self.grab_set()

        frame = ttk.Frame(self, padding=16)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text=APP_TITLE, font=("Segoe UI", 15, "bold")).pack(anchor="w")
        ttk.Label(frame, text=f"Version {APP_VERSION}", foreground="#555555").pack(
            anchor="w",
            pady=(4, 12),
        )
        ttk.Label(frame, text=ABOUT_TEXT, justify="left", wraplength=420).pack(
            anchor="w"
        )
        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=14)
        ttk.Label(
            frame,
            text="Creado por Fernando Corrales Quiros",
            justify="left",
        ).pack(anchor="w")
        ttk.Button(frame, text="Cerrar", command=self.destroy).pack(
            anchor="e",
            pady=(16, 0),
        )
