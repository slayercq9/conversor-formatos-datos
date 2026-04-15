"""Componente visual reutilizable para la vista previa tabular."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from src.services.preview_service import PreviewData


class PreviewTable(ttk.Frame):
    """Tabla reutilizable para mostrar una vista previa tabular."""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master, padding=4)
        self.empty_message_var = tk.StringVar(
            value="La vista previa de los datos aparecerá aquí."
        )
        self.summary_var = tk.StringVar(value="Sin vista previa cargada.")
        self.note_var = tk.StringVar(
            value="Cuando cargues un archivo, aquí verás una inspección rápida de su estructura."
        )

        header = ttk.Frame(self, style="Surface.TFrame", padding=(6, 2, 6, 10))
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        ttk.Label(
            header,
            textvariable=self.summary_var,
            style="PreviewSummary.TLabel",
        ).grid(row=0, column=0, sticky="w")
        ttk.Label(
            header,
            textvariable=self.note_var,
            style="SectionHint.TLabel",
            wraplength=760,
            justify="left",
        ).grid(row=1, column=0, sticky="w", pady=(4, 0))

        table_area = ttk.Frame(self, style="Surface.TFrame", padding=4)
        table_area.grid(row=1, column=0, sticky="nsew")
        table_area.grid_rowconfigure(0, weight=1)
        table_area.grid_columnconfigure(0, weight=1)

        self.tree = ttk.Treeview(table_area, show="headings", style="Preview.Treeview")
        self.tree.grid(row=0, column=0, sticky="nsew")

        scrollbar_y = ttk.Scrollbar(table_area, orient="vertical", command=self.tree.yview)
        scrollbar_y.grid(row=0, column=1, sticky="ns", padx=(6, 0))
        self.tree.configure(yscrollcommand=scrollbar_y.set)

        scrollbar_x = ttk.Scrollbar(table_area, orient="horizontal", command=self.tree.xview)
        scrollbar_x.grid(row=1, column=0, sticky="ew", pady=(6, 0))
        self.tree.configure(xscrollcommand=scrollbar_x.set)

        self.empty_label = ttk.Label(
            table_area,
            textvariable=self.empty_message_var,
            anchor="center",
            justify="center",
            style="SectionHint.TLabel",
            padding=(24, 24),
        )
        self.empty_label.grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.show_message("La vista previa de los datos aparecerá aquí.")

    def update_data(self, preview: PreviewData) -> None:
        """Pinta una nueva grilla con resumen, columnas y filas serializadas."""
        self.clear()
        self.summary_var.set(preview.summary_text)
        self.note_var.set(preview.note_text)

        if not preview.columns:
            self.show_message("No se encontraron columnas para mostrar.")
            return

        self.tree["columns"] = preview.columns
        self.empty_label.grid_remove()
        self.tree.grid()

        for column in preview.columns:
            width = min(max(len(column) * 12, 130), 240)
            self.tree.heading(column, text=column)
            self.tree.column(column, width=width, minwidth=110, anchor="w", stretch=True)

        for row in preview.rows:
            self.tree.insert("", "end", values=row)

        if not preview.rows:
            self.show_message("Se detectaron columnas, pero no hay filas para previsualizar.")

    def clear(self) -> None:
        """Limpia filas y columnas previas antes de mostrar nuevos datos."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.tree["columns"] = ()

    def show_message(self, message: str) -> None:
        """Oculta la tabla y muestra un mensaje centrado en su lugar."""
        self.empty_message_var.set(message)
        self.summary_var.set("Sin vista previa cargada.")
        self.note_var.set(
            "La vista previa está pensada para inspección rápida y no permite editar datos."
        )
        self.tree.grid_remove()
        self.empty_label.grid()
