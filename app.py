"""Punto de entrada de la aplicacion de escritorio.

Este archivo solo crea la ventana principal y arranca el loop de Tkinter.
Mantenerlo pequeno facilita localizar el inicio real de la app.
"""

from __future__ import annotations

from src.gui.main_window import MainWindow


def main() -> None:
    """Crea la ventana principal y entrega el control a Tkinter."""
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
