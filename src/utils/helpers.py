from __future__ import annotations

from pathlib import Path

from src.core.file_types import (
    TabularFileType,
    get_file_dialog_filters,
)


def normalize_extension(value: str) -> str:
    """Normaliza una extension eliminando punto y espacios."""
    return value.strip().lower().removeprefix(".")


def ensure_parent_directory(path: Path) -> None:
    """Crea el directorio padre si no existe."""
    path.parent.mkdir(parents=True, exist_ok=True)


def build_output_path(source_path: Path, target_format: TabularFileType) -> Path:
    """Construye una ruta de salida junto al archivo original."""
    return source_path.with_suffix(f".{target_format.value}")


def format_file_dialog_types() -> list[tuple[str, str]]:
    """Devuelve filtros compatibles con filedialog."""
    return get_file_dialog_filters()
