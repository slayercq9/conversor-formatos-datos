from __future__ import annotations

from pathlib import Path

from src.core.reader import TabularReader
from src.core.validators import validate_source_path
from src.utils.constants import PREVIEW_ROW_LIMIT
from src.utils.errors import PreviewError


class PreviewService:
    """Genera una vista previa ligera para mostrar en la GUI."""

    def __init__(self, reader: TabularReader | None = None) -> None:
        self._reader = reader or TabularReader()

    def load_preview(
        self,
        source_path: str | Path,
        max_rows: int = PREVIEW_ROW_LIMIT,
    ) -> tuple[list[str], list[tuple[str, ...]]]:
        path = validate_source_path(source_path)

        try:
            data_frame = self._reader.read(path).head(max_rows).fillna("")
        except Exception as exc:
            raise PreviewError("No se pudo cargar la vista previa.") from exc

        columns = [str(column) for column in data_frame.columns]
        rows = [
            tuple(str(value) for value in record)
            for record in data_frame.itertuples(index=False, name=None)
        ]
        return columns, rows
