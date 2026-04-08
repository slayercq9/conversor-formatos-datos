from __future__ import annotations

from pathlib import Path

from src.core.converter import ConversionRequest, PreparedConversion, TabularConverter
from src.core.file_types import TabularFileType
from src.utils.errors import PendingConversionError
from src.utils.helpers import build_output_path


class FileService:
    """Expone operaciones de conversion para la capa de interfaz."""

    def __init__(self, converter: TabularConverter | None = None) -> None:
        self._converter = converter or TabularConverter()
        self._prepared_conversion: PreparedConversion | None = None

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

    def prepare_conversion(
        self,
        source_path: str | Path,
        target_format: str | TabularFileType,
    ) -> PreparedConversion:
        target_type = (
            target_format
            if isinstance(target_format, TabularFileType)
            else TabularFileType.from_extension(target_format)
        )
        self._prepared_conversion = self._converter.prepare_conversion(
            source_path=source_path,
            target_format=target_type,
        )
        return self._prepared_conversion

    def save_prepared_conversion(self, target_path: str | Path) -> Path:
        if self._prepared_conversion is None:
            raise PendingConversionError(
                "Primero convierte el archivo antes de intentar guardarlo."
            )
        return self._converter.save_prepared_conversion(
            self._prepared_conversion,
            target_path,
        )

    def clear_prepared_conversion(self) -> None:
        self._prepared_conversion = None

    def has_prepared_conversion(self) -> bool:
        return self._prepared_conversion is not None

    @property
    def prepared_conversion(self) -> PreparedConversion | None:
        return self._prepared_conversion

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
