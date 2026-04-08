from __future__ import annotations

from pathlib import Path

from src.core.file_types import TabularFileType
from src.utils.errors import ValidationError


def validate_source_path(file_path: str | Path) -> Path:
    """Valida que el archivo de entrada exista y sea soportado."""
    path = Path(file_path)
    if not path.exists():
        raise ValidationError("El archivo de entrada no existe.")
    if not path.is_file():
        raise ValidationError("La ruta de entrada no es un archivo valido.")
    TabularFileType.from_path(path)
    return path


def validate_target_format(value: str) -> TabularFileType:
    """Valida el formato de salida solicitado."""
    return TabularFileType.from_extension(value)


def validate_distinct_formats(
    source_type: TabularFileType,
    target_type: TabularFileType,
) -> None:
    """Evita conversiones redundantes al mismo formato."""
    if source_type == target_type:
        raise ValidationError("El formato de salida debe ser distinto al de entrada.")


def validate_output_path(file_path: str | Path) -> Path:
    """Valida una ruta de salida basica."""
    path = Path(file_path)
    if not path.name:
        raise ValidationError("Debes indicar un nombre de archivo de salida.")
    return path
