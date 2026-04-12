"""Ventana auxiliar con informacion general de la aplicacion.

Su responsabilidad es mostrar datos estaticos como nombre, version,
fecha de actualizacion, descripcion y autoria sin depender de la logica
de conversion.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from src.utils.constants import (
    APP_AUTHOR,
    APP_DESCRIPTION,
    APP_LAST_UPDATED,
    APP_TITLE,
    APP_VERSION,
)


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
        ttk.Label(
            frame,
            text=f"Versión actual: {APP_VERSION}",
            foreground="#555555",
        ).pack(anchor="w", pady=(4, 2))
        ttk.Label(
            frame,
            text=f"Última actualización: {APP_LAST_UPDATED}",
            foreground="#555555",
        ).pack(anchor="w", pady=(0, 12))
        ttk.Label(frame, text=APP_DESCRIPTION, justify="left", wraplength=420).pack(
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
        self._center_on_parent(master)

    def _center_on_parent(self, master: tk.Misc) -> None:
        """Centra la ventana respecto a la principal para una apertura mas natural."""
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
