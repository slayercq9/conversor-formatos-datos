from __future__ import annotations

from pathlib import Path

from src.core.converter import ConversionRequest, TabularConverter
from src.core.file_types import TabularFileType
from src.utils.helpers import build_output_path


class FileService:
    """Expone operaciones de conversion para la capa de interfaz."""

    def __init__(self, converter: TabularConverter | None = None) -> None:
        self._converter = converter or TabularConverter()

    def build_default_output_path(
        self,
        source_path: str | Path,
        target_format: str | TabularFileType,
    ) -> Path:
        target_type = (
            target_format
            if isinstance(target_format, TabularFileType)
            else TabularFileType.from_extension(target_format)
        )
        return build_output_path(Path(source_path), target_type)

    def convert_file(
        self,
        source_path: str | Path,
        target_path: str | Path,
        target_format: str | TabularFileType,
    ) -> Path:
        target_type = (
            target_format
            if isinstance(target_format, TabularFileType)
            else TabularFileType.from_extension(target_format)
        )
        request = ConversionRequest(
            source_path=Path(source_path),
            target_path=Path(target_path),
            target_format=target_type,
        )
        return self._converter.convert(request)
