"""Ventana auxiliar con informacion general de la aplicacion.

Su responsabilidad es mostrar datos estaticos como nombre, version,
descripcion y autoria sin depender de la logica de conversion.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from src.utils.constants import ABOUT_TEXT, APP_AUTHOR, APP_TITLE, APP_VERSION


class AboutWindow(tk.Toplevel):
    """Muestra informacion resumida del proyecto en una ventana modal."""

    def __init__(self, master: tk.Misc) -> None:
        """Construye una ventana ligera enfocada en informacion fija."""
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
            text=f"Creado por {APP_AUTHOR}",
            justify="left",
        ).pack(anchor="w")
        ttk.Button(frame, text="Cerrar", command=self.destroy).pack(
            anchor="e",
            pady=(16, 0),
        )
