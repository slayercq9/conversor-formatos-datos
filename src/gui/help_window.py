from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from src.utils.constants import HELP_TEXT


class HelpWindow(tk.Toplevel):
    """Ventana de ayuda basica."""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.title("Como usar")
        self.geometry("480x300")

        frame = ttk.Frame(self, padding=16)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text=HELP_TEXT, justify="left", wraplength=430).pack(
            fill="both",
            expand=True,
            anchor="nw",
        )
        ttk.Button(frame, text="Cerrar", command=self.destroy).pack(anchor="e", pady=(12, 0))
