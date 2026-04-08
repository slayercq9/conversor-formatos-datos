from pathlib import Path

import pytest

from src.core.file_types import TabularFileType
from src.core.validators import validate_distinct_formats, validate_output_path
from src.utils.helpers import build_output_path, normalize_extension
from src.utils.errors import ValidationError


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
