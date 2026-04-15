from src.core.file_types import (
    TabularFileType,
    get_file_dialog_filters,
    get_supported_extensions,
)


def test_from_extension_accepts_dot_prefix() -> None:
    assert TabularFileType.from_extension(".csv") == TabularFileType.CSV


def test_values_returns_supported_extensions() -> None:
    assert TabularFileType.values() == ["csv", "tsv", "xlsx", "ods", "json", "xml", "txt"]


def test_supported_extensions_are_centralized() -> None:
    assert get_supported_extensions() == ["csv", "tsv", "xlsx", "ods", "json", "xml", "txt"]


def test_file_dialog_filters_include_all_formats() -> None:
    filters = get_file_dialog_filters()
    assert ("CSV", "*.csv") in filters
    assert ("TSV", "*.tsv") in filters
    assert ("Excel (.xlsx)", "*.xlsx") in filters
    assert ("OpenDocument Spreadsheet (.ods)", "*.ods") in filters
    assert ("XML tabular (.xml)", "*.xml") in filters
