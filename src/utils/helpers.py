from __future__ import annotations

from pathlib import Path

from src.core.file_types import TabularFileType
from src.utils.constants import SUPPORTED_FORMAT_LABELS


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
    filters = [
        ("Archivos tabulares", "*.csv *.xlsx *.json *.txt"),
    ]
    filters.extend(
        (label, f"*.{extension}")
        for extension, label in SUPPORTED_FORMAT_LABELS.items()
    )
    filters.append(("Todos los archivos", "*.*"))
    return filters
