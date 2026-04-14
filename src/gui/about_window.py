"""Ventana auxiliar con información general de la aplicación.

Su responsabilidad es mostrar datos estáticos como nombre, versión,
fecha de actualización, descripción y autoría sin depender de la lógica
de conversión.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from src.utils.constants import (
    APP_AUTHOR,
    APP_DESCRIPTION,
    APP_LAST_UPDATED_LABEL,
    APP_TITLE,
    APP_VERSION,
)


class AboutWindow(tk.Toplevel):
    """Muestra información resumida del proyecto en una ventana modal."""

    def __init__(self, master: tk.Misc) -> None:
        """Construye una ventana ligera enfocada en información fija."""
        super().__init__(master)
        self.title("Acerca de")
        self.resizable(False, False)
        self.transient(master)
        self.grab_set()

        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)

        header = ttk.Frame(frame)
        header.pack(fill="x")

        ttk.Label(header, text=APP_TITLE, font=("Segoe UI", 16, "bold")).pack(
            anchor="w"
        )
        ttk.Label(
            header,
            text=f"Versión actual: {APP_VERSION}",
            foreground="#555555",
        ).pack(anchor="w", pady=(6, 2))
        ttk.Label(
            header,
            text=f"Última actualización: {APP_LAST_UPDATED_LABEL}",
            foreground="#555555",
        ).pack(anchor="w")

        ttk.Separator(frame, orient="horizontal").pack(fill="x", pady=14)

        ttk.Label(frame, text=APP_DESCRIPTION, justify="left", wraplength=440).pack(
            anchor="w"
        )
        ttk.Label(
            frame,
            text=f"Creado por {APP_AUTHOR}",
            justify="left",
        ).pack(anchor="w", pady=(14, 0))

        footer = ttk.Frame(frame)
        footer.pack(fill="x", pady=(18, 0))
        ttk.Button(footer, text="Cerrar", command=self.destroy, width=14).pack(
            anchor="e"
        )

        self._center_on_parent(master)

    def _center_on_parent(self, master: tk.Misc) -> None:
        """Centra la ventana respecto a la principal para una apertura más natural."""
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
