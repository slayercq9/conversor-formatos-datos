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
    """Escribe DataFrames hacia distintos formatos tabulares."""

    def __init__(self) -> None:
        self._writers: dict[
            TabularFileType,
            Callable[[pd.DataFrame, Path], None],
        ] = {
            TabularFileType.CSV: self._write_csv,
            TabularFileType.XLSX: self._write_xlsx,
            TabularFileType.JSON: self._write_json,
            TabularFileType.TXT: self._write_txt,
        }

    def register_writer(
        self,
        file_type: TabularFileType,
        writer: Callable[[pd.DataFrame, Path], None],
    ) -> None:
        """Permite extender el escritor con nuevos formatos sin romper la API."""
        self._writers[file_type] = writer

    def supports(self, file_type: TabularFileType) -> bool:
        return file_type in self._writers

    def write(
        self,
        data_frame: pd.DataFrame,
        target_path: str | Path,
        target_type: TabularFileType | None = None,
    ) -> Path:
        path = validate_output_path(target_path)
        validate_dataframe_not_empty(data_frame)
        resolved_target_type = target_type or TabularFileType.from_path(path)
        writer = self._writers.get(resolved_target_type)
        if writer is None:
            raise WriteError(
                f"No hay escritor configurado para: {resolved_target_type.value}"
            )

        ensure_parent_directory(path)

        try:
            writer(data_frame, path)
        except Exception as exc:
            raise WriteError(
                f"No se pudo guardar el archivo '{path.name}'. Revisa permisos, ruta y si el archivo esta abierto."
            ) from exc

        return path

    def _write_csv(self, data_frame: pd.DataFrame, target_path: Path) -> None:
        data_frame.to_csv(target_path, index=False)

    def _write_xlsx(self, data_frame: pd.DataFrame, target_path: Path) -> None:
        data_frame.to_excel(target_path, index=False)

    def _write_json(self, data_frame: pd.DataFrame, target_path: Path) -> None:
        data_frame.to_json(
            target_path,
            orient="records",
            indent=2,
            force_ascii=False,
        )

    def _write_txt(self, data_frame: pd.DataFrame, target_path: Path) -> None:
        data_frame.to_csv(target_path, sep=DEFAULT_TEXT_DELIMITER, index=False)
