"""Soporte opcional para arrastrar y soltar archivos en la interfaz.

Este modulo encapsula la integracion con `tkinterdnd2` para que la GUI
principal no dependa directamente de detalles de la libreria externa.
Si la dependencia no esta instalada, la aplicacion sigue funcionando
con el flujo manual de seleccion de archivos.
"""

from __future__ import annotations

import tkinter as tk
from pathlib import Path
from typing import Callable, Protocol

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
except ImportError:  # pragma: no cover - depende del entorno local.
    DND_FILES = "DND_Files"
    TkinterDnD = None


DropHandler = Callable[[Path], None]


def get_main_window_base() -> type[tk.Tk]:
    """Devuelve la clase base adecuada para la ventana principal."""
    if TkinterDnD is None:
        return tk.Tk
    return TkinterDnD.Tk


def split_drop_paths(raw_data: str, tk_root: tk.Misc | None = None) -> list[Path]:
    """Normaliza el payload de drag and drop a una lista de rutas."""
    if not raw_data.strip():
        return []

    if tk_root is not None:
        try:
            return [Path(item) for item in tk_root.tk.splitlist(raw_data) if item]
        except tk.TclError:
            pass

    normalized = raw_data.strip()
    if normalized.startswith("{") and normalized.endswith("}"):
        return [Path(normalized[1:-1])]
    return [Path(item) for item in normalized.split() if item]


class DragDropManager(Protocol):
    """Contrato para integrar drag and drop sin acoplar la GUI actual."""

    def attach(
        self,
        window: tk.Misc,
        drop_target: tk.Misc | None = None,
        on_drop_file: DropHandler | None = None,
    ) -> None:
        """Registra el soporte de drag and drop en la ventana dada."""


class NullDragDropManager:
    """Implementacion nula usada cuando drag and drop no esta disponible."""

    def attach(
        self,
        window: tk.Misc,
        drop_target: tk.Misc | None = None,
        on_drop_file: DropHandler | None = None,
    ) -> None:
        _ = window
        _ = drop_target
        _ = on_drop_file


class TkinterDnDManager:
    """Implementacion real de drag and drop basada en `tkinterdnd2`."""

    def attach(
        self,
        window: tk.Misc,
        drop_target: tk.Misc | None = None,
        on_drop_file: DropHandler | None = None,
    ) -> None:
        """Configura el area de destino y delega el archivo soltado a la GUI."""
        if TkinterDnD is None or drop_target is None or on_drop_file is None:
            return

        drop_target.drop_target_register(DND_FILES)

        def _handle_drop(event: object) -> None:
            data = getattr(event, "data", "")
            candidates = split_drop_paths(str(data), window)
            if not candidates:
                return
            on_drop_file(candidates[0])

        drop_target.dnd_bind("<<Drop>>", _handle_drop)


def create_drag_drop_manager() -> DragDropManager:
    """Crea el manager mas capaz disponible en el entorno actual."""
    if TkinterDnD is None:
        return NullDragDropManager()
    return TkinterDnDManager()
