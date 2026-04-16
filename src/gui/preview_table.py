"""Componente visual reutilizable para la vista previa tabular."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from src.services.preview_service import PreviewData


class PreviewTable(ttk.Frame):
    """Tabla reutilizable para mostrar una vista previa tabular."""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master, padding=4)
        self.empty_message_var = tk.StringVar()
        self.summary_var = tk.StringVar()
        self.note_var = tk.StringVar()

        header = ttk.Frame(self, style="Surface.TFrame", padding=(6, 2, 6, 10))
        header.grid(row=0, column=0, sticky="ew")
        header.grid_columnconfigure(0, weight=1)

        self.summary_label = ttk.Label(
            header,
            textvariable=self.summary_var,
            style="PreviewSummary.TLabel",
        )
        self.summary_label.grid(row=0, column=0, sticky="w")
        self.note_label = ttk.Label(
            header,
            textvariable=self.note_var,
            style="SectionHint.TLabel",
            wraplength=760,
            justify="left",
        )
        self.note_label.grid(row=1, column=0, sticky="w", pady=(4, 0))

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

    def update_data(
        self,
        preview: PreviewData,
        *,
        summary_text: str,
        note_text: str,
        empty_message: str,
    ) -> None:
        """Pinta una nueva grilla con resumen, columnas y filas serializadas."""
        self.clear()
        self.summary_var.set(summary_text)
        self.note_var.set(note_text)

        if not preview.columns:
            self.show_message(empty_message, note_text=note_text)
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
            self.show_message(empty_message, note_text=note_text)

    def clear(self) -> None:
        """Limpia filas y columnas previas antes de mostrar nuevos datos."""
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.tree["columns"] = ()

    def show_message(self, message: str, *, note_text: str) -> None:
        """Oculta la tabla y muestra un mensaje centrado en su lugar."""
        self.empty_message_var.set(message)
        self.summary_var.set("")
        self.note_var.set(note_text)
        self.tree.grid_remove()
        self.empty_label.grid()
