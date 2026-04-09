from __future__ import annotations

import tkinter as tk
from typing import Protocol


class DragDropManager(Protocol):
    """Contrato para integrar drag and drop sin acoplar la GUI actual."""

    def attach(self, window: tk.Misc, drop_target: tk.Misc | None = None) -> None:
        """Registra el soporte de drag and drop en la ventana dada."""


class NullDragDropManager:
    """Implementacion nula para dejar lista la extension futura."""

    def attach(self, window: tk.Misc, drop_target: tk.Misc | None = None) -> None:
        _ = window
        _ = drop_target
        # TODO: Integrar una libreria de drag and drop compatible con Tkinter.
        # TODO: Conectar el archivo soltado con el flujo de seleccion actual.
