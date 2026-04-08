from __future__ import annotations

import tkinter as tk
from tkinter import ttk


class PreviewTable(ttk.Frame):
    """Tabla reutilizable para mostrar una vista previa tabular."""

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)
        self.empty_message_var = tk.StringVar(
            value="La vista previa de los datos aparecera aqui."
        )

        self.tree = ttk.Treeview(self, show="headings")
        self.tree.grid(row=0, column=0, sticky="nsew")

        scrollbar_y = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar_y.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar_y.set)

        scrollbar_x = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        scrollbar_x.grid(row=1, column=0, sticky="ew")
        self.tree.configure(xscrollcommand=scrollbar_x.set)

        self.empty_label = ttk.Label(
            self,
            textvariable=self.empty_message_var,
            anchor="center",
            justify="center",
        )
        self.empty_label.grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.show_message("La vista previa de los datos aparecera aqui.")

    def update_data(self, columns: list[str], rows: list[tuple[str, ...]]) -> None:
        self.clear()
        if not columns:
            self.show_message("No se encontraron columnas para mostrar.")
            return

        self.tree["columns"] = columns
        self.empty_label.grid_remove()
        self.tree.grid()

        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=140, minwidth=100, anchor="w")

        for row in rows:
            self.tree.insert("", "end", values=row)

        if not rows:
            self.show_message("El archivo no contiene filas para previsualizar.")

    def clear(self) -> None:
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.tree["columns"] = ()

    def show_message(self, message: str) -> None:
        self.empty_message_var.set(message)
        self.tree.grid_remove()
        self.empty_label.grid()
