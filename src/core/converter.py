from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from src.core.file_types import TabularFileType
from src.core.reader import TabularReader
from src.core.validators import (
    validate_distinct_formats,
    validate_output_path,
    validate_source_path,
)
from src.core.writer import TabularWriter


@dataclass(slots=True)
class ConversionRequest:
    source_path: Path
    target_path: Path
    target_format: TabularFileType


@dataclass(slots=True)
class PreparedConversion:
    source_path: Path
    source_format: TabularFileType
    target_format: TabularFileType
    data_frame: pd.DataFrame


class TabularConverter:
    """Coordina el flujo completo de lectura y escritura."""

    def __init__(
        self,
        reader: TabularReader | None = None,
        writer: TabularWriter | None = None,
    ) -> None:
        self._reader = reader or TabularReader()
        self._writer = writer or TabularWriter()

    def read_as_dataframe(self, source_path: str | Path) -> pd.DataFrame:
        """Lee cualquier archivo soportado y devuelve un DataFrame."""
        validated_source_path = validate_source_path(source_path)
        return self._reader.read(validated_source_path)

    def write_dataframe(
        self,
        data_frame: pd.DataFrame,
        target_path: str | Path,
        target_format: TabularFileType | None = None,
    ) -> Path:
        """Escribe un DataFrame al formato deseado o al inferido por la extension."""
        validated_target_path = validate_output_path(target_path)
        return self._writer.write(data_frame, validated_target_path, target_format)

    def prepare_conversion(
        self,
        source_path: str | Path,
        target_format: TabularFileType,
    ) -> PreparedConversion:
        validated_source_path = validate_source_path(source_path)
        source_type = TabularFileType.from_path(validated_source_path)
        validate_distinct_formats(source_type, target_format)

        data_frame = self.read_as_dataframe(validated_source_path)
        return PreparedConversion(
            source_path=validated_source_path,
            source_format=source_type,
            target_format=target_format,
            data_frame=data_frame,
        )

    def save_prepared_conversion(
        self,
        prepared_conversion: PreparedConversion,
        target_path: str | Path,
    ) -> Path:
        return self.write_dataframe(
            prepared_conversion.data_frame,
            target_path,
            prepared_conversion.target_format,
        )

    def convert(self, request: ConversionRequest) -> Path:
        prepared_conversion = self.prepare_conversion(
            request.source_path,
            request.target_format,
        )
        return self.save_prepared_conversion(prepared_conversion, request.target_path)
