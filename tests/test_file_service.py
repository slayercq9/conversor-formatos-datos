from pathlib import Path

import pytest

from src.core.file_types import TabularFileType
from src.services.file_service import FileService
from src.utils.errors import MissingTargetFormatError, PendingConversionError


class FakeConverter:
    def __init__(self) -> None:
        self.prepared_conversion = object()
        self.prepare_calls: list[tuple[Path, TabularFileType]] = []
        self.saved_target_path: Path | None = None
        self.convert_request: object | None = None

    def prepare_conversion(
        self,
        source_path: str | Path,
        target_format: TabularFileType,
    ) -> object:
        self.prepare_calls.append((Path(source_path), target_format))
        return self.prepared_conversion

    def save_prepared_conversion(
        self,
        prepared_conversion: object,
        target_path: str | Path,
    ) -> Path:
        assert prepared_conversion is self.prepared_conversion
        self.saved_target_path = Path(target_path)
        return self.saved_target_path

    def convert(self, request: object) -> Path:
        self.convert_request = request
        return Path("salidas/ventas.json")


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
    assert converter.prepare_calls == [
        (Path("datos/ventas.xlsx"), TabularFileType.CSV)
    ]


def test_prepare_conversion_requires_target_format() -> None:
    service = FileService(converter=FakeConverter())

    with pytest.raises(MissingTargetFormatError):
        service.prepare_conversion("datos/ventas.xlsx", "")


def test_build_default_output_path_accepts_typed_format() -> None:
    service = FileService(converter=FakeConverter())

    result = service.build_default_output_path(
        "datos/ventas.csv",
        TabularFileType.JSON,
    )

    assert result == Path("datos/ventas.json")


def test_clear_prepared_conversion_resets_pending_state() -> None:
    service = FileService(converter=FakeConverter())
    service.prepare_conversion("datos/ventas.xlsx", "csv")

    service.clear_prepared_conversion()

    assert service.has_prepared_conversion() is False
    assert service.prepared_conversion is None


def test_convert_file_builds_typed_conversion_request() -> None:
    converter = FakeConverter()
    service = FileService(converter=converter)

    result = service.convert_file(
        "datos/ventas.csv",
        "salidas/ventas.json",
        "json",
    )

    assert result == Path("salidas/ventas.json")
    assert converter.convert_request is not None
    assert converter.convert_request.source_path == Path("datos/ventas.csv")
    assert converter.convert_request.target_path == Path("salidas/ventas.json")
    assert converter.convert_request.target_format == TabularFileType.JSON
