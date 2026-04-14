"""Ventana auxiliar con instrucciones de uso para el usuario final.

Este módulo encapsula la ayuda visual para que la ventana principal
solo tenga que abrirla cuando sea necesario.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from src.utils.constants import HELP_TEXT


class HelpWindow(tk.Toplevel):
    """Muestra instrucciones de uso en una ventana separada y legible."""

    def __init__(self, master: tk.Misc) -> None:
        """Construye una ventana modal con recomendaciones de uso."""
        super().__init__(master)
        self.title("Cómo usar")
        self.geometry("620x430")
        self.minsize(560, 390)
        self.transient(master)
        self.grab_set()

        frame = ttk.Frame(self, padding=20)
        frame.pack(fill="both", expand=True)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)

        ttk.Label(frame, text="Cómo usar", font=("Segoe UI", 16, "bold")).grid(
            row=0,
            column=0,
            sticky="w",
        )

        content = ttk.Frame(frame, padding=0)
        content.grid(row=1, column=0, sticky="nsew", pady=(14, 0))
        content.columnconfigure(0, weight=1)

        ttk.Separator(content, orient="horizontal").grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, 12),
        )
        ttk.Label(
            content,
            text=HELP_TEXT,
            justify="left",
            anchor="nw",
            wraplength=540,
            padding=(6, 4),
        ).grid(row=1, column=0, sticky="nsew")

        footer = ttk.Frame(frame)
        footer.grid(row=2, column=0, sticky="ew", pady=(18, 0))
        ttk.Button(footer, text="Cerrar", command=self.destroy, width=14).pack(
            anchor="e"
        )

        self._center_on_parent(master)

    def _center_on_parent(self, master: tk.Misc) -> None:
        """Centra la ventana respecto a la principal para evitar aperturas bruscas."""
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
