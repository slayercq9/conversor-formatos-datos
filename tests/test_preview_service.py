from pathlib import Path

import pandas as pd
import pytest

from src.services.preview_service import PreviewService
from src.utils.errors import PreviewError, ReadError


class FakePreviewReader:
    def __init__(
        self,
        data_frame: pd.DataFrame | None = None,
        error: Exception | None = None,
    ) -> None:
        self._data_frame = data_frame
        self._error = error

    def read(self, source_path: str | Path) -> pd.DataFrame:
        _ = source_path
        if self._error is not None:
            raise self._error
        assert self._data_frame is not None
        return self._data_frame


def test_preview_service_limits_rows_and_builds_summary(tmp_path: Path) -> None:
    source = tmp_path / "datos.csv"
    source.write_text("ok", encoding="utf-8")
    service = PreviewService(
        reader=FakePreviewReader(
            pd.DataFrame({"nombre": ["Ana", "Luis"], "edad": [30, 28]})
        )
    )

    preview = service.load_preview(source, max_rows=1)

    assert preview.columns == ["nombre", "edad"]
    assert preview.rows == [("Ana", "30")]
    assert preview.total_columns == 2
    assert preview.previewed_rows == 1
    assert preview.total_rows == 2
    assert preview.is_partial is True
    assert "2 columnas detectadas" in preview.summary_text


def test_preview_service_marks_complete_preview_when_all_rows_fit(tmp_path: Path) -> None:
    source = tmp_path / "datos.csv"
    source.write_text("ok", encoding="utf-8")
    service = PreviewService(
        reader=FakePreviewReader(pd.DataFrame({"nombre": ["Ana"], "edad": [30]}))
    )

    preview = service.load_preview(source, max_rows=5)

    assert preview.is_partial is False
    assert preview.note_text == "Vista previa completa cargada para inspección rápida."


def test_preview_service_preserves_clear_domain_message(tmp_path: Path) -> None:
    source = tmp_path / "datos.xml"
    source.write_text("<rows></rows>", encoding="utf-8")
    service = PreviewService(
        reader=FakePreviewReader(
            error=ReadError(
                "El archivo XML no contiene una estructura tabular compatible."
            )
        )
    )

    with pytest.raises(PreviewError) as exc_info:
        service.load_preview(source)

    assert "estructura tabular compatible" in str(exc_info.value)
