from pathlib import Path

import pandas as pd
import pytest

from src.core.file_types import TabularFileType
from src.core.validators import (
    validate_dataframe_not_empty,
    validate_distinct_formats,
    validate_output_path,
    validate_source_path,
    validate_target_format,
)
from src.utils.helpers import build_output_path, normalize_extension
from src.utils.errors import EmptyFileError, MissingTargetFormatError, ValidationError


def test_validate_distinct_formats_raises_for_same_type() -> None:
    with pytest.raises(ValidationError):
        validate_distinct_formats(TabularFileType.CSV, TabularFileType.CSV)


def test_build_output_path_uses_target_extension() -> None:
    source = Path("datos/ventas.csv")
    target = build_output_path(source, TabularFileType.JSON)
    assert target == Path("datos/ventas.json")


def test_validate_output_path_returns_path_instance() -> None:
    result = validate_output_path("salidas/reporte.xlsx")
    assert result == Path("salidas/reporte.xlsx")


def test_normalize_extension_strips_point_and_spaces() -> None:
    assert normalize_extension(" .TXT ") == "txt"


def test_validate_target_format_requires_value() -> None:
    with pytest.raises(MissingTargetFormatError):
        validate_target_format("")


def test_validate_dataframe_not_empty_raises_for_empty_frame() -> None:
    with pytest.raises(EmptyFileError):
        validate_dataframe_not_empty(pd.DataFrame())


def test_validate_source_path_rejects_empty_file(tmp_path: Path) -> None:
    empty_file = tmp_path / "vacio.csv"
    empty_file.write_text("", encoding="utf-8")

    with pytest.raises(EmptyFileError):
        validate_source_path(empty_file)
