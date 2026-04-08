from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from src.utils.constants import ABOUT_TEXT


class AboutWindow(tk.Toplevel):
    """Ventana simple de informacion de la aplicacion."""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.title("Acerca de")
        self.resizable(False, False)

        frame = ttk.Frame(self, padding=16)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text=ABOUT_TEXT, justify="left").pack(anchor="w")
        ttk.Button(frame, text="Cerrar", command=self.destroy).pack(anchor="e", pady=(12, 0))
