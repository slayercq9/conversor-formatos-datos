"""Definiciones centralizadas de formatos tabulares soportados.

Este modulo funciona como fuente unica de verdad para extensiones,
etiquetas legibles y filtros de dialogo asociados a cada formato.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from src.utils.errors import UnsupportedFormatError


class TabularFileType(str, Enum):
    """Enum con las extensiones tabulares soportadas por la aplicacion."""

    CSV = "csv"
    TSV = "tsv"
    XLSX = "xlsx"
    ODS = "ods"
    JSON = "json"
    XML = "xml"
    TXT = "txt"

    @classmethod
    def from_extension(cls, extension: str) -> "TabularFileType":
        """Convierte una extension cruda en un valor del enum."""
        normalized = extension.strip().lower().removeprefix(".")
        for item in cls:
            if item.value == normalized:
                return item
        raise UnsupportedFormatError(f"Formato no soportado: {extension}")

    @classmethod
    def from_path(cls, file_path: str | Path) -> "TabularFileType":
        """Infiere el tipo de archivo a partir de la extension de una ruta."""
        return cls.from_extension(Path(file_path).suffix)

    @classmethod
    def values(cls) -> list[str]:
        """Devuelve las extensiones soportadas como lista simple."""
        return [item.value for item in cls]

    @property
    def label(self) -> str:
        """Devuelve la etiqueta legible usada en la interfaz."""
        return get_format_definition(self).label

    @property
    def file_pattern(self) -> str:
        """Devuelve el patron usado por los dialogos de archivos."""
        return get_format_definition(self).file_pattern


@dataclass(frozen=True, slots=True)
class TabularFormatDefinition:
    """Agrupa la metadata visible y tecnica de un formato soportado."""

    file_type: TabularFileType
    label: str
    file_pattern: str


FORMAT_DEFINITIONS: dict[TabularFileType, TabularFormatDefinition] = {
    TabularFileType.CSV: TabularFormatDefinition(
        file_type=TabularFileType.CSV,
        label="CSV",
        file_pattern="*.csv",
    ),
    TabularFileType.TSV: TabularFormatDefinition(
        file_type=TabularFileType.TSV,
        label="TSV",
        file_pattern="*.tsv",
    ),
    TabularFileType.XLSX: TabularFormatDefinition(
        file_type=TabularFileType.XLSX,
        label="Excel (.xlsx)",
        file_pattern="*.xlsx",
    ),
    TabularFileType.ODS: TabularFormatDefinition(
        file_type=TabularFileType.ODS,
        label="OpenDocument Spreadsheet (.ods)",
        file_pattern="*.ods",
    ),
    TabularFileType.JSON: TabularFormatDefinition(
        file_type=TabularFileType.JSON,
        label="JSON",
        file_pattern="*.json",
    ),
    TabularFileType.XML: TabularFormatDefinition(
        file_type=TabularFileType.XML,
        label="XML tabular (.xml)",
        file_pattern="*.xml",
    ),
    TabularFileType.TXT: TabularFormatDefinition(
        file_type=TabularFileType.TXT,
        label="Texto delimitado (.txt)",
        file_pattern="*.txt",
    ),
}


def get_format_definition(file_type: TabularFileType) -> TabularFormatDefinition:
    """Obtiene la definicion registrada de un formato concreto."""
    try:
        return FORMAT_DEFINITIONS[file_type]
    except KeyError as exc:
        raise UnsupportedFormatError(
            f"No existe una definicion registrada para: {file_type.value}"
        ) from exc


def get_supported_file_types() -> list[TabularFileType]:
    """Devuelve los formatos soportados en el orden de registro."""
    return list(FORMAT_DEFINITIONS.keys())


def get_supported_extensions() -> list[str]:
    """Devuelve solo las extensiones registradas."""
    return [file_type.value for file_type in get_supported_file_types()]


def get_supported_format_labels() -> dict[str, str]:
    """Devuelve un mapa simple extension -> etiqueta visible."""
    return {
        definition.file_type.value: definition.label
        for definition in FORMAT_DEFINITIONS.values()
    }


def get_file_dialog_filters() -> list[tuple[str, str]]:
    """Construye filtros reutilizables para dialogs de seleccion."""
    wildcard_group = " ".join(
        definition.file_pattern for definition in FORMAT_DEFINITIONS.values()
    )
    filters = [("Archivos tabulares", wildcard_group)]
    filters.extend(
        (definition.label, definition.file_pattern)
        for definition in FORMAT_DEFINITIONS.values()
    )
    filters.append(("Todos los archivos", "*.*"))
    return filters
