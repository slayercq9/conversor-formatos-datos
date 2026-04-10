"""Servicios para construir vistas previas de datos en la GUI.

La idea es transformar un DataFrame en una estructura ligera y amigable
para widgets de tabla sin mezclar esa logica con la lectura de archivos.
"""

from __future__ import annotations

from pathlib import Path

from src.core.reader import TabularReader
from src.core.validators import validate_source_path
from src.utils.constants import PREVIEW_ROW_LIMIT
from src.utils.errors import AppError, PreviewError


class PreviewService:
    """Adapta datos tabulares a una forma facil de pintar en la interfaz."""

    def __init__(self, reader: TabularReader | None = None) -> None:
        """Permite inyectar un lector alternativo, util en pruebas."""
        self._reader = reader or TabularReader()

    def load_preview(
        self,
        source_path: str | Path,
        max_rows: int = PREVIEW_ROW_LIMIT,
    ) -> tuple[list[str], list[tuple[str, ...]]]:
        """Devuelve columnas y filas serializadas para la tabla de preview."""
        path = validate_source_path(source_path)

        try:
            data_frame = self._reader.read(path).head(max_rows).fillna("")
        except AppError as exc:
            raise PreviewError(str(exc)) from exc
        except Exception as exc:
            raise PreviewError("No se pudo cargar la vista previa.") from exc

        columns = [str(column) for column in data_frame.columns]
        # La GUI trabaja mejor con valores ya convertidos a texto simple.
        rows = [
            tuple(str(value) for value in record)
            for record in data_frame.itertuples(index=False, name=None)
        ]
        return columns, rows
