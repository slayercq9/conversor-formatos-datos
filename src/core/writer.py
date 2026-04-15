"""Escritura de DataFrames de pandas a formatos tabulares.

Este modulo abstrae la exportacion por extension y mantiene una API
estable para que la capa superior no dependa de detalles de pandas.
"""

from __future__ import annotations

from pathlib import Path
from typing import Callable

import pandas as pd

from src.core.file_types import TabularFileType
from src.core.validators import validate_dataframe_not_empty, validate_output_path
from src.utils.constants import DEFAULT_TEXT_DELIMITER
from src.utils.errors import WriteError
from src.utils.helpers import ensure_parent_directory


class TabularWriter:
    """Escribe DataFrames a disco segun el formato de salida requerido."""

    def __init__(self) -> None:
        """Registra los escritores por defecto disponibles en la aplicacion."""
        self._writers: dict[
            TabularFileType,
            Callable[[pd.DataFrame, Path], None],
        ] = {
            TabularFileType.CSV: self._write_csv,
            TabularFileType.TSV: self._write_tsv,
            TabularFileType.XLSX: self._write_xlsx,
            TabularFileType.ODS: self._write_ods,
            TabularFileType.JSON: self._write_json,
            TabularFileType.XML: self._write_xml,
            TabularFileType.TXT: self._write_txt,
        }

    def register_writer(
        self,
        file_type: TabularFileType,
        writer: Callable[[pd.DataFrame, Path], None],
    ) -> None:
        """Agrega o reemplaza el escritor asociado a un formato dado."""
        self._writers[file_type] = writer

    def supports(self, file_type: TabularFileType) -> bool:
        """Indica si existe un escritor registrado para el formato indicado."""
        return file_type in self._writers

    def write(
        self,
        data_frame: pd.DataFrame,
        target_path: str | Path,
        target_type: TabularFileType | None = None,
    ) -> Path:
        """Valida datos y ruta de salida antes de exportar el DataFrame."""
        path = validate_output_path(target_path)
        validate_dataframe_not_empty(data_frame)
        resolved_target_type = target_type or TabularFileType.from_path(path)
        writer = self._writers.get(resolved_target_type)
        if writer is None:
            raise WriteError(
                f"No hay escritor configurado para: {resolved_target_type.value}"
            )

        ensure_parent_directory(path)
        # Se crea el directorio de salida antes de escribir para evitar fallos
        # cuando el usuario elige una carpeta nueva.

        try:
            writer(data_frame, path)
        except WriteError:
            raise
        except Exception as exc:
            raise WriteError(
                f"No se pudo guardar el archivo '{path.name}'. Revisa permisos, ruta y si el archivo esta abierto."
            ) from exc

        return path

    def _write_csv(self, data_frame: pd.DataFrame, target_path: Path) -> None:
        """Exporta el DataFrame a CSV sin incluir el indice."""
        data_frame.to_csv(target_path, index=False)

    def _write_tsv(self, data_frame: pd.DataFrame, target_path: Path) -> None:
        """Exporta el DataFrame a TSV usando tabulacion fija."""
        data_frame.to_csv(target_path, sep="\t", index=False)

    def _write_xlsx(self, data_frame: pd.DataFrame, target_path: Path) -> None:
        """Exporta el DataFrame a un archivo Excel simple."""
        try:
            data_frame.to_excel(target_path, index=False)
        except ImportError as exc:
            raise WriteError(
                "No se pudo guardar el archivo XLSX porque falta una dependencia de Excel. "
                "Instala requirements.txt e intenta de nuevo."
            ) from exc

    def _write_ods(self, data_frame: pd.DataFrame, target_path: Path) -> None:
        """Exporta el DataFrame a ODS usando el motor odf de pandas."""
        try:
            data_frame.to_excel(target_path, index=False, engine="odf")
        except ImportError as exc:
            raise WriteError(
                "No se pudo guardar el archivo ODS porque falta la dependencia 'odfpy'. "
                "Instala requirements.txt e intenta de nuevo."
            ) from exc

    def _write_json(self, data_frame: pd.DataFrame, target_path: Path) -> None:
        """Exporta el DataFrame a JSON orientado a registros."""
        data_frame.to_json(
            target_path,
            orient="records",
            indent=2,
            force_ascii=False,
        )

    def _write_xml(self, data_frame: pd.DataFrame, target_path: Path) -> None:
        """Exporta el DataFrame a XML tabular con una estructura simple."""
        data_frame.to_xml(
            target_path,
            index=False,
            parser="etree",
            root_name="rows",
            row_name="row",
        )

    def _write_txt(self, data_frame: pd.DataFrame, target_path: Path) -> None:
        """Exporta el DataFrame a texto delimitado por tabulaciones."""
        data_frame.to_csv(target_path, sep=DEFAULT_TEXT_DELIMITER, index=False)
