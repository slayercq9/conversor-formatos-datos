from __future__ import annotations

from src.gui.main_window import MainWindow


def main() -> None:
    """Punto de entrada de la aplicacion."""
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()
