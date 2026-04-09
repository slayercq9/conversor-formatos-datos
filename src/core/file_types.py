from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

from src.utils.errors import UnsupportedFormatError


class TabularFileType(str, Enum):
    CSV = "csv"
    XLSX = "xlsx"
    JSON = "json"
    TXT = "txt"

    @classmethod
    def from_extension(cls, extension: str) -> "TabularFileType":
        normalized = extension.strip().lower().removeprefix(".")
        for item in cls:
            if item.value == normalized:
                return item
        raise UnsupportedFormatError(f"Formato no soportado: {extension}")

    @classmethod
    def from_path(cls, file_path: str | Path) -> "TabularFileType":
        return cls.from_extension(Path(file_path).suffix)

    @classmethod
    def values(cls) -> list[str]:
        return [item.value for item in cls]

    @property
    def label(self) -> str:
        return get_format_definition(self).label

    @property
    def file_pattern(self) -> str:
        return get_format_definition(self).file_pattern


@dataclass(frozen=True, slots=True)
class TabularFormatDefinition:
    file_type: TabularFileType
    label: str
    file_pattern: str


FORMAT_DEFINITIONS: dict[TabularFileType, TabularFormatDefinition] = {
    TabularFileType.CSV: TabularFormatDefinition(
        file_type=TabularFileType.CSV,
        label="CSV",
        file_pattern="*.csv",
    ),
    TabularFileType.XLSX: TabularFormatDefinition(
        file_type=TabularFileType.XLSX,
        label="Excel (.xlsx)",
        file_pattern="*.xlsx",
    ),
    TabularFileType.JSON: TabularFormatDefinition(
        file_type=TabularFileType.JSON,
        label="JSON",
        file_pattern="*.json",
    ),
    TabularFileType.TXT: TabularFormatDefinition(
        file_type=TabularFileType.TXT,
        label="Texto delimitado (.txt)",
        file_pattern="*.txt",
    ),
}


def get_format_definition(file_type: TabularFileType) -> TabularFormatDefinition:
    try:
        return FORMAT_DEFINITIONS[file_type]
    except KeyError as exc:
        raise UnsupportedFormatError(
            f"No existe una definicion registrada para: {file_type.value}"
        ) from exc


def get_supported_file_types() -> list[TabularFileType]:
    return list(FORMAT_DEFINITIONS.keys())


def get_supported_extensions() -> list[str]:
    return [file_type.value for file_type in get_supported_file_types()]


def get_supported_format_labels() -> dict[str, str]:
    return {
        definition.file_type.value: definition.label
        for definition in FORMAT_DEFINITIONS.values()
    }


def get_file_dialog_filters() -> list[tuple[str, str]]:
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
