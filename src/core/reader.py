"""Lectura de archivos tabulares hacia DataFrames de pandas.

La clase principal encapsula la seleccion del lector segun extension y
actua como punto de extension para agregar formatos adicionales.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Callable

import pandas as pd

from src.core.file_types import TabularFileType
from src.core.validators import validate_dataframe_not_empty, validate_source_path
from src.utils.constants import DEFAULT_TEXT_DELIMITER
from src.utils.errors import ReadError


class TabularReader:
    """Lee archivos soportados y los entrega como DataFrames de pandas."""

    def __init__(self) -> None:
        """Registra los lectores por defecto disponibles en la aplicacion."""
        self._readers: dict[TabularFileType, Callable[[Path], pd.DataFrame]] = {
            TabularFileType.CSV: self._read_csv,
            TabularFileType.TSV: self._read_tsv,
            TabularFileType.XLSX: self._read_xlsx,
            TabularFileType.ODS: self._read_ods,
            TabularFileType.JSON: self._read_json,
            TabularFileType.XML: self._read_xml,
            TabularFileType.TXT: self._read_txt,
        }

    def register_reader(
        self,
        file_type: TabularFileType,
        reader: Callable[[Path], pd.DataFrame],
    ) -> None:
        """Agrega o reemplaza el lector asociado a un formato dado."""
        self._readers[file_type] = reader

    def supports(self, file_type: TabularFileType) -> bool:
        """Indica si existe un lector registrado para el formato indicado."""
        return file_type in self._readers

    def read(self, source_path: str | Path) -> pd.DataFrame:
        """Valida la ruta, selecciona el lector y devuelve un DataFrame listo."""
        path = validate_source_path(source_path)
        file_type = TabularFileType.from_path(path)
        reader = self._readers.get(file_type)
        if reader is None:
            raise ReadError(f"No hay lector configurado para: {file_type.value}")

        try:
            data_frame = reader(path)
        except ReadError:
            raise
        except Exception as exc:
            raise ReadError(
                f"No se pudo leer el archivo '{path.name}'. Verifica que no este danado o en uso."
            ) from exc

        return validate_dataframe_not_empty(data_frame)

    def _read_csv(self, source_path: Path) -> pd.DataFrame:
        """Lee un archivo CSV usando la configuracion por defecto de pandas."""
        return pd.read_csv(source_path)

    def _read_tsv(self, source_path: Path) -> pd.DataFrame:
        """Lee un archivo TSV usando tabulacion como separador fijo."""
        return pd.read_csv(source_path, sep="\t")

    def _read_xlsx(self, source_path: Path) -> pd.DataFrame:
        """Lee la primera hoja de un archivo Excel soportado."""
        try:
            return pd.read_excel(source_path)
        except ImportError as exc:
            raise ReadError(
                "No se pudo leer el archivo XLSX porque falta una dependencia de Excel. "
                "Instala requirements.txt e intenta de nuevo."
            ) from exc

    def _read_ods(self, source_path: Path) -> pd.DataFrame:
        """Lee un archivo ODS usando el motor odf de pandas."""
        try:
            return pd.read_excel(source_path, engine="odf")
        except ImportError as exc:
            raise ReadError(
                "No se pudo leer el archivo ODS porque falta la dependencia 'odfpy'. "
                "Instala requirements.txt e intenta de nuevo."
            ) from exc

    def _read_json(self, source_path: Path) -> pd.DataFrame:
        """Lee un archivo JSON tabularizable mediante pandas."""
        try:
            return pd.read_json(source_path)
        except ValueError as exc:
            raise ReadError(
                "No se pudo interpretar el archivo JSON como una tabla. "
                "Usa una lista de registros o una estructura tabular compatible."
            ) from exc

    def _read_xml(self, source_path: Path) -> pd.DataFrame:
        """Lee XML cuando puede interpretarse como una tabla de registros."""
        try:
            data_frame = pd.read_xml(source_path, parser="etree")
        except Exception as exc:
            raise ReadError(
                "No se pudo interpretar el archivo XML como una tabla. "
                "Usa un XML con registros repetidos y campos consistentes."
            ) from exc

        if data_frame is None or (data_frame.empty and len(data_frame.columns) == 0):
            raise ReadError(
                "El archivo XML no contiene una estructura tabular compatible."
            )

        return data_frame

    def _read_txt(self, source_path: Path) -> pd.DataFrame:
        """Lee texto delimitado detectando el separador cuando es posible."""
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
