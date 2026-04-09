from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.core.file_types import TabularFileType
from src.utils.errors import (
    EmptyFileError,
    MissingFileError,
    MissingTargetFormatError,
    UnsupportedFormatError,
    ValidationError,
)


def validate_required_file_path(file_path: str | Path) -> Path:
    """Valida que el usuario haya indicado una ruta de archivo."""
    raw_path = str(file_path).strip()
    if not raw_path:
        raise MissingFileError("Todavia no has cargado un archivo.")
    return Path(raw_path)


def validate_source_path(file_path: str | Path) -> Path:
    """Valida que el archivo de entrada exista y sea soportado."""
    path = validate_required_file_path(file_path)
    if not path.exists():
        raise MissingFileError("El archivo seleccionado no existe.")
    if not path.is_file():
        raise ValidationError("La ruta de entrada no es un archivo valido.")
    if path.stat().st_size == 0:
        raise EmptyFileError("El archivo seleccionado esta vacio.")
    try:
        TabularFileType.from_path(path)
    except UnsupportedFormatError as exc:
        raise UnsupportedFormatError(
            "El formato del archivo cargado no es soportado."
        ) from exc
    return path


def validate_target_format(value: str) -> TabularFileType:
    """Valida el formato de salida solicitado."""
    if not str(value).strip():
        raise MissingTargetFormatError(
            "Debes elegir un formato de salida antes de convertir."
        )
    try:
        return TabularFileType.from_extension(value)
    except UnsupportedFormatError as exc:
        raise UnsupportedFormatError(
            "El formato de salida seleccionado no es soportado."
        ) from exc


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


def validate_dataframe_not_empty(data_frame: pd.DataFrame) -> pd.DataFrame:
    """Valida que el DataFrame contenga datos o al menos columnas utilizables."""
    if data_frame.empty and len(data_frame.columns) == 0:
        raise EmptyFileError("El archivo seleccionado no contiene datos para procesar.")
    return data_frame
