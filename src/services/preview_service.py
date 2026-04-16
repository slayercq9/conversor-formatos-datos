"""Servicios para construir vistas previas ligeras para la GUI.

La idea es transformar un `DataFrame` en una estructura serializable y
directa de pintar en Tkinter, manteniendo separadas la lectura de
archivos y la presentación visual.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from src.core.reader import TabularReader
from src.core.validators import validate_source_path
from src.utils.constants import PREVIEW_ROW_LIMIT
from src.utils.errors import AppError, PreviewError


@dataclass(slots=True)
class PreviewData:
    """Representa una vista previa ligera y lista para la interfaz."""

    columns: list[str]
    rows: list[tuple[str, ...]]
    total_columns: int
    previewed_rows: int
    total_rows: int
    is_partial: bool


class PreviewService:
    """Adapta datos tabulares a una forma facil de pintar en la interfaz."""

    def __init__(self, reader: TabularReader | None = None) -> None:
        """Permite inyectar un lector alternativo, util en pruebas."""
        self._reader = reader or TabularReader()

    def load_preview(
        self,
        source_path: str | Path,
        max_rows: int = PREVIEW_ROW_LIMIT,
    ) -> PreviewData:
        """Devuelve una vista previa ligera con filas, columnas y resumen."""
        path = validate_source_path(source_path)

        try:
            data_frame = self._reader.read(path).fillna("")
        except AppError as exc:
            raise PreviewError(str(exc)) from exc
        except Exception as exc:
            raise PreviewError("No se pudo cargar la vista previa.") from exc

        preview_frame = data_frame.head(max_rows)
        columns = [str(column) for column in preview_frame.columns]
        rows = [
            tuple(str(value) for value in record)
            for record in preview_frame.itertuples(index=False, name=None)
        ]
        total_rows = len(data_frame.index)

        return PreviewData(
            columns=columns,
            rows=rows,
            total_columns=len(columns),
            previewed_rows=len(rows),
            total_rows=total_rows,
            is_partial=total_rows > len(rows),
        )
