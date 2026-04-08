from src.core.file_types import TabularFileType


def test_from_extension_accepts_dot_prefix() -> None:
    assert TabularFileType.from_extension(".csv") == TabularFileType.CSV


def test_values_returns_supported_extensions() -> None:
    assert TabularFileType.values() == ["csv", "xlsx", "json", "txt"]
