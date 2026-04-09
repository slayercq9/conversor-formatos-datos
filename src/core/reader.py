from __future__ import annotations

import csv
from pathlib import Path
from typing import Callable

import pandas as pd

from src.core.file_types import TabularFileType
from src.utils.constants import DEFAULT_TEXT_DELIMITER
from src.utils.errors import ConversionError


class TabularReader:
    """Lee archivos tabulares y los normaliza como DataFrame."""

    def __init__(self) -> None:
        self._readers: dict[TabularFileType, Callable[[Path], pd.DataFrame]] = {
            TabularFileType.CSV: self._read_csv,
            TabularFileType.XLSX: self._read_xlsx,
            TabularFileType.JSON: self._read_json,
            TabularFileType.TXT: self._read_txt,
        }

    def register_reader(
        self,
        file_type: TabularFileType,
        reader: Callable[[Path], pd.DataFrame],
    ) -> None:
        """Permite extender el lector con nuevos formatos sin cambiar su interfaz."""
        self._readers[file_type] = reader

    def supports(self, file_type: TabularFileType) -> bool:
        return file_type in self._readers

    def read(self, source_path: str | Path) -> pd.DataFrame:
        path = Path(source_path)
        file_type = TabularFileType.from_path(path)
        reader = self._readers.get(file_type)
        if reader is None:
            raise ConversionError(f"No hay lector configurado para: {file_type.value}")

        try:
            return reader(path)
        except Exception as exc:
            raise ConversionError(f"No se pudo leer el archivo: {path.name}") from exc

    def _read_csv(self, source_path: Path) -> pd.DataFrame:
        return pd.read_csv(source_path)

    def _read_xlsx(self, source_path: Path) -> pd.DataFrame:
        return pd.read_excel(source_path)

    def _read_json(self, source_path: Path) -> pd.DataFrame:
        return pd.read_json(source_path)

    def _read_txt(self, source_path: Path) -> pd.DataFrame:
        delimiter = self._detect_text_delimiter(source_path)
        return pd.read_csv(source_path, sep=delimiter)

    def _detect_text_delimiter(self, source_path: Path) -> str:
        """Intenta detectar el delimitador del archivo TXT."""
        try:
            with source_path.open("r", encoding="utf-8", newline="") as handle:
                sample = handle.read(2048)
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
            return dialect.delimiter
        except Exception:
            return DEFAULT_TEXT_DELIMITER
