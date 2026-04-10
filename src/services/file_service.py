"""Servicios de archivo para la capa de interfaz.

Este modulo ofrece una API mas cercana a la GUI para preparar, guardar
y reutilizar conversiones sin exponer detalles de la capa core.
"""

from __future__ import annotations

from pathlib import Path

from src.core.converter import ConversionRequest, PreparedConversion, TabularConverter
from src.core.file_types import TabularFileType
from src.core.validators import validate_target_format
from src.utils.errors import PendingConversionError
from src.utils.helpers import build_output_path


class FileService:
    """Adapta el conversor central al flujo interactivo de la interfaz."""

    def __init__(self, converter: TabularConverter | None = None) -> None:
        """Inicializa el servicio y el estado de conversion pendiente."""
        self._converter = converter or TabularConverter()
        self._prepared_conversion: PreparedConversion | None = None

    def build_default_output_path(
        self,
        source_path: str | Path,
        target_format: str | TabularFileType,
    ) -> Path:
        """Construye una ruta sugerida segun el formato de salida elegido."""
        target_type = (
            target_format
            if isinstance(target_format, TabularFileType)
            else validate_target_format(target_format)
        )
        return build_output_path(Path(source_path), target_type)

    def prepare_conversion(
        self,
        source_path: str | Path,
        target_format: str | TabularFileType,
    ) -> PreparedConversion:
        """Prepara la conversion y conserva el resultado en memoria."""
        target_type = (
            target_format
            if isinstance(target_format, TabularFileType)
            else validate_target_format(target_format)
        )
        self._prepared_conversion = self._converter.prepare_conversion(
            source_path=source_path,
            target_format=target_type,
        )
        return self._prepared_conversion

    def save_prepared_conversion(self, target_path: str | Path) -> Path:
        """Guarda la conversion pendiente previamente preparada por la GUI."""
        if self._prepared_conversion is None:
            raise PendingConversionError(
                "Primero convierte el archivo antes de intentar guardarlo."
            )
        return self._converter.save_prepared_conversion(
            self._prepared_conversion,
            target_path,
        )

    def clear_prepared_conversion(self) -> None:
        """Descarta cualquier conversion pendiente almacenada en memoria."""
        self._prepared_conversion = None

    def has_prepared_conversion(self) -> bool:
        """Indica si ya existe una conversion lista para guardarse."""
        return self._prepared_conversion is not None

    @property
    def prepared_conversion(self) -> PreparedConversion | None:
        """Expone el estado actual solo para lectura."""
        return self._prepared_conversion

    def convert_file(
        self,
        source_path: str | Path,
        target_path: str | Path,
        target_format: str | TabularFileType,
    ) -> Path:
        """Ejecuta el flujo completo en un solo llamado cuando se necesita."""
        target_type = (
            target_format
            if isinstance(target_format, TabularFileType)
            else validate_target_format(target_format)
        )
        request = ConversionRequest(
            source_path=Path(source_path),
            target_path=Path(target_path),
            target_format=target_type,
        )
        return self._converter.convert(request)
