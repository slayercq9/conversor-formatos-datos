from __future__ import annotations

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
