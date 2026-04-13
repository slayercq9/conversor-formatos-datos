"""Integracion real de drag and drop para la interfaz principal.

Este modulo encapsula la integracion con ``tkinterdnd2`` y mantiene
aislada la GUI principal de los detalles de la libreria.
"""

from __future__ import annotations

from pathlib import Path
import tkinter as tk
from typing import Callable, Protocol

try:
    from tkinterdnd2 import COPY, DND_FILES, TkinterDnD
except ImportError:  # pragma: no cover - depende del entorno local.
    COPY = "copy"
    DND_FILES = "DND_Files"
    TkinterDnD = None


DropHandler = Callable[[Path], None]


def get_main_window_base() -> type[tk.Tk]:
    """Devuelve la clase base correcta para la ventana principal."""

    if TkinterDnD is None:
        return tk.Tk
    return TkinterDnD.Tk


def split_drop_paths(raw_data: str, tk_root: tk.Misc | None = None) -> list[Path]:
    """Normaliza el payload de tkdnd a una lista de rutas."""

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
    """Contrato para registrar drag and drop sin acoplar la GUI."""

    def attach(
        self,
        window: tk.Misc,
        drop_target: tk.Misc | None = None,
        on_drop_file: DropHandler | None = None,
    ) -> None:
        """Activa el soporte de drop sobre la ventana y su area visible."""


class NullDragDropManager:
    """Implementacion segura cuando ``tkinterdnd2`` no esta disponible."""

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
    """Adaptador de ``tkinterdnd2`` para archivos soltados en la interfaz."""

    def attach(
        self,
        window: tk.Misc,
        drop_target: tk.Misc | None = None,
        on_drop_file: DropHandler | None = None,
    ) -> None:
        """Registra la ventana principal y el arbol del area de carga."""

        if TkinterDnD is None or on_drop_file is None:
            return

        widgets_to_register: list[tk.Misc] = [window]
        if drop_target is not None:
            widgets_to_register.extend(self._collect_drop_widgets(drop_target))

        seen_widgets: set[str] = set()
        for widget in widgets_to_register:
            widget_id = str(widget)
            if widget_id in seen_widgets:
                continue
            seen_widgets.add(widget_id)
            self._register_drop_widget(window, widget, on_drop_file)

    def _collect_drop_widgets(self, root_widget: tk.Misc) -> list[tk.Misc]:
        """Incluye hijos para que ningun control intermedio bloquee el drop."""

        widgets = [root_widget]
        for child in root_widget.winfo_children():
            widgets.extend(self._collect_drop_widgets(child))
        return widgets

    def _register_drop_widget(
        self,
        window: tk.Misc,
        widget: tk.Misc,
        on_drop_file: DropHandler,
    ) -> None:
        """Registra un widget individual como destino de archivos."""

        try:
            widget.drop_target_register(DND_FILES)
            widget.dnd_bind("<<DropEnter>>", self._accept_drop)
            widget.dnd_bind("<<DropPosition>>", self._accept_drop)
            widget.dnd_bind("<<DropLeave>>", self._leave_drop)
            widget.dnd_bind(
                "<<Drop>>",
                lambda event, owner=window: self._handle_drop(
                    owner,
                    str(getattr(event, "data", "")),
                    on_drop_file,
                ),
            )
        except (AttributeError, tk.TclError):
            return

    def _accept_drop(self, event: object) -> str:
        """Confirma a tkdnd que el widget acepta el archivo arrastrado."""

        return getattr(event, "action", COPY)

    def _leave_drop(self, event: object) -> str:
        """Responde limpiamente cuando el puntero sale del area registrada."""

        return getattr(event, "action", COPY)

    def _handle_drop(
        self,
        window: tk.Misc,
        raw_data: str,
        on_drop_file: DropHandler,
    ) -> str:
        """Entrega a la GUI el primer archivo valido recibido por tkdnd."""

        candidates = split_drop_paths(raw_data, tk_root=window)
        if candidates:
            on_drop_file(candidates[0])
        return COPY


def create_drag_drop_manager() -> DragDropManager:
    """Crea el backend de drag and drop disponible en el entorno actual."""

    if TkinterDnD is None:
        return NullDragDropManager()
    return TkinterDnDManager()
