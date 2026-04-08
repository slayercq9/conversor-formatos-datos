from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.core.file_types import TabularFileType
from src.utils.constants import DEFAULT_TEXT_DELIMITER
from src.utils.errors import ConversionError
from src.utils.helpers import ensure_parent_directory


class TabularWriter:
    """Escribe DataFrames hacia distintos formatos tabulares."""

    def write(
        self,
        data_frame: pd.DataFrame,
        target_path: str | Path,
        target_type: TabularFileType,
    ) -> Path:
        path = Path(target_path)
        ensure_parent_directory(path)

        try:
            if target_type == TabularFileType.CSV:
                data_frame.to_csv(path, index=False)
            elif target_type == TabularFileType.XLSX:
                data_frame.to_excel(path, index=False)
            elif target_type == TabularFileType.JSON:
                data_frame.to_json(path, orient="records", indent=2, force_ascii=False)
            elif target_type == TabularFileType.TXT:
                data_frame.to_csv(path, sep=DEFAULT_TEXT_DELIMITER, index=False)
            else:
                raise ConversionError(
                    f"No hay escritor configurado para: {target_type.value}"
                )
        except Exception as exc:
            raise ConversionError(f"No se pudo escribir el archivo: {path.name}") from exc

        return path
