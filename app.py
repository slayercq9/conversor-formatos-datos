"""Punto de entrada de la aplicacion de escritorio.

Este archivo solo crea la ventana principal y arranca el loop de Tkinter.
Mantenerlo pequeno facilita localizar el inicio real de la app.
"""

from __future__ import annotations

from pathlib import Path
import sys

from src.gui.main_window import MainWindow


def resolve_asset_path(relative_path: str) -> Path:
    """Resuelve rutas de assets tanto en desarrollo como en ejecutable empaquetado."""
    if hasattr(sys, "_MEIPASS"):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent
    return base_path / relative_path


def main() -> None:
    """Crea la ventana principal y entrega el control a Tkinter."""
    # La app usa `assets/icon.ico` como icono principal si el archivo esta disponible.
    icon_path = resolve_asset_path("assets/icon.ico")
    app = MainWindow(icon_path=icon_path)
    app.mainloop()


if __name__ == "__main__":
    main()
