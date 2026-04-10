"""Coordinacion del flujo de conversion entre lectura y escritura.

La responsabilidad de este modulo es orquestar validaciones, lectura
del origen, preparacion del resultado en memoria y guardado final.
"""

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
    validate_target_format,
)
from src.core.writer import TabularWriter


@dataclass(slots=True)
class ConversionRequest:
    """Representa una solicitud completa de conversion con destino final."""

    source_path: Path
    target_path: Path
    target_format: TabularFileType


@dataclass(slots=True)
class PreparedConversion:
    """Representa una conversion validada y cargada en memoria."""

    source_path: Path
    source_format: TabularFileType
    target_format: TabularFileType
    data_frame: pd.DataFrame


class TabularConverter:
    """Orquesta la conversion tabular sin depender de la interfaz grafica."""

    def __init__(
        self,
        reader: TabularReader | None = None,
        writer: TabularWriter | None = None,
    ) -> None:
        """Permite inyectar lector y escritor para pruebas o extensiones."""
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
        """Escribe un DataFrame al formato indicado o inferido por extension."""
        validated_target_path = validate_output_path(target_path)
        return self._writer.write(data_frame, validated_target_path, target_format)

    def prepare_conversion(
        self,
        source_path: str | Path,
        target_format: str | TabularFileType,
    ) -> PreparedConversion:
        """Valida el origen y prepara una conversion aun no guardada."""
        validated_source_path = validate_source_path(source_path)
        source_type = TabularFileType.from_path(validated_source_path)
        resolved_target_format = (
            target_format
            if isinstance(target_format, TabularFileType)
            else validate_target_format(target_format)
        )
        validate_distinct_formats(source_type, resolved_target_format)

        data_frame = self.read_as_dataframe(validated_source_path)
        return PreparedConversion(
            source_path=validated_source_path,
            source_format=source_type,
            target_format=resolved_target_format,
            data_frame=data_frame,
        )

    def save_prepared_conversion(
        self,
        prepared_conversion: PreparedConversion,
        target_path: str | Path,
    ) -> Path:
        """Guarda en disco una conversion preparada previamente."""
        return self.write_dataframe(
            prepared_conversion.data_frame,
            target_path,
            prepared_conversion.target_format,
        )

    def convert(self, request: ConversionRequest) -> Path:
        """Ejecuta el flujo completo de preparar y guardar en un solo paso."""
        prepared_conversion = self.prepare_conversion(
            request.source_path,
            request.target_format,
        )
        return self.save_prepared_conversion(prepared_conversion, request.target_path)
