from __future__ import annotations

import tkinter as tk
from typing import Protocol


class DragDropManager(Protocol):
    """Contrato para integrar drag and drop sin acoplar la GUI actual."""

    def attach(self, window: tk.Misc) -> None:
        """Registra el soporte de drag and drop en la ventana dada."""


class NullDragDropManager:
    """Implementacion nula para dejar lista la extension futura."""

    def attach(self, window: tk.Misc) -> None:
        _ = window
        # Punto de extension reservado para una futura integracion real.
