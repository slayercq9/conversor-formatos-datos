from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

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


class TabularConverter:
    """Coordina el flujo completo de lectura y escritura."""

    def __init__(
        self,
        reader: TabularReader | None = None,
        writer: TabularWriter | None = None,
    ) -> None:
        self._reader = reader or TabularReader()
        self._writer = writer or TabularWriter()

    def convert(self, request: ConversionRequest) -> Path:
        source_path = validate_source_path(request.source_path)
        target_path = validate_output_path(request.target_path)
        source_type = TabularFileType.from_path(source_path)
        validate_distinct_formats(source_type, request.target_format)

        data_frame = self._reader.read(source_path)
        return self._writer.write(data_frame, target_path, request.target_format)
