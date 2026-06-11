"""Punto de entrada de la aplicación de escritorio.

Este archivo solo crea la ventana principal y arranca el loop de Tkinter.
Mantenerlo pequeño facilita localizar el inicio real de la app.
"""

from __future__ import annotations

from pathlib import Path
import sys

from src.gui.main_window import MainWindow


def resolve_asset_path(relative_path: str) -> Path:
    """Resuelve rutas de assets tanto en desarrollo como en ejecutable empaquetado."""
    bundle_path = getattr(sys, "_MEIPASS", None)
    base_path = Path(bundle_path) if bundle_path else Path(__file__).resolve().parent
    return base_path / relative_path


def main() -> None:
    """Crea la ventana principal y entrega el control a Tkinter."""
    icon_path = resolve_asset_path("assets/icon.ico")
    app = MainWindow(icon_path=icon_path)
    app.mainloop()


if __name__ == "__main__":
    main()
