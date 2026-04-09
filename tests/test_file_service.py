from pathlib import Path

import pytest

from src.services.file_service import FileService
from src.utils.errors import MissingTargetFormatError, PendingConversionError


class FakeConverter:
    def __init__(self) -> None:
        self.prepared_conversion = object()
        self.saved_target_path: Path | None = None

    def prepare_conversion(self, source_path: str | Path, target_format: str) -> object:
        _ = source_path
        _ = target_format
        return self.prepared_conversion

    def save_prepared_conversion(
        self,
        prepared_conversion: object,
        target_path: str | Path,
    ) -> Path:
        assert prepared_conversion is self.prepared_conversion
        self.saved_target_path = Path(target_path)
        return self.saved_target_path


def test_save_prepared_conversion_requires_pending_result() -> None:
    service = FileService(converter=FakeConverter())

    with pytest.raises(PendingConversionError):
        service.save_prepared_conversion("salidas/reporte.csv")


def test_prepare_conversion_enables_later_save() -> None:
    converter = FakeConverter()
    service = FileService(converter=converter)

    service.prepare_conversion("datos/ventas.xlsx", "csv")
    result = service.save_prepared_conversion("salidas/ventas.csv")

    assert result == Path("salidas/ventas.csv")
    assert converter.saved_target_path == Path("salidas/ventas.csv")


def test_prepare_conversion_requires_target_format() -> None:
    service = FileService(converter=FakeConverter())

    with pytest.raises(MissingTargetFormatError):
        service.prepare_conversion("datos/ventas.xlsx", "")
