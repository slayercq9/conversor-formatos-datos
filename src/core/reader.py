from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd

from src.core.file_types import TabularFileType
from src.utils.constants import DEFAULT_TEXT_DELIMITER
from src.utils.errors import ConversionError


class TabularReader:
    """Lee archivos tabulares y los normaliza como DataFrame."""

    def read(self, source_path: str | Path) -> pd.DataFrame:
        path = Path(source_path)
        file_type = TabularFileType.from_path(path)

        try:
            if file_type == TabularFileType.CSV:
                return pd.read_csv(path)
            if file_type == TabularFileType.XLSX:
                return pd.read_excel(path)
            if file_type == TabularFileType.JSON:
                return pd.read_json(path)
            if file_type == TabularFileType.TXT:
                delimiter = self._detect_text_delimiter(path)
                return pd.read_csv(path, sep=delimiter)
        except Exception as exc:
            raise ConversionError(f"No se pudo leer el archivo: {path.name}") from exc

        raise ConversionError(f"No hay lector configurado para: {file_type.value}")

    def _detect_text_delimiter(self, source_path: Path) -> str:
        """Intenta detectar el delimitador del archivo TXT."""
        try:
            with source_path.open("r", encoding="utf-8", newline="") as handle:
                sample = handle.read(2048)
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
            return dialect.delimiter
        except Exception:
            return DEFAULT_TEXT_DELIMITER
