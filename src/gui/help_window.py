from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from src.utils.constants import HELP_TEXT


class HelpWindow(tk.Toplevel):
    """Ventana de ayuda basica."""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.title("Como usar")
        self.geometry("620x420")
        self.minsize(560, 380)
        self.transient(master)
        self.grab_set()

        frame = ttk.Frame(self, padding=16)
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(0, weight=1)

        ttk.Label(frame, text="Como usar", font=("Segoe UI", 15, "bold")).grid(
            row=0,
            column=0,
            sticky="w",
        )

        content = ttk.LabelFrame(frame, text="Instrucciones", padding=14)
        content.grid(row=1, column=0, sticky="nsew", pady=(12, 0))
        content.columnconfigure(0, weight=1)

        ttk.Label(
            content,
            text=HELP_TEXT,
            justify="left",
            anchor="nw",
            wraplength=540,
        ).grid(row=0, column=0, sticky="nsew")

        ttk.Button(frame, text="Cerrar", command=self.destroy).grid(
            row=2,
            column=0,
            sticky="e",
            pady=(16, 0),
        )
