from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class PreviewTable(ttk.Frame):
    """Tabla reutilizable para mostrar una vista previa tabular."""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.tree = ttk.Treeview(self, show="headings")
        self.tree.grid(row=0, column=0, sticky="nsew")

        scrollbar_y = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar_y.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar_y.set)

        scrollbar_x = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        scrollbar_x.grid(row=1, column=0, sticky="ew")
        self.tree.configure(xscrollcommand=scrollbar_x.set)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def update_data(self, columns: list[str], rows: list[tuple[str, ...]]) -> None:
        self.clear()
        self.tree["columns"] = columns

        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=140, minwidth=100, anchor="w")

        for row in rows:
            self.tree.insert("", "end", values=row)

    def clear(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.tree["columns"] = ()
