from pathlib import Path

import pandas as pd
import pytest

from src.core.converter import PreparedConversion, TabularConverter
from src.core.file_types import TabularFileType
from src.utils.errors import ValidationError


class FakeReader:
    def __init__(self, data_frame: pd.DataFrame) -> None:
        self.data_frame = data_frame
        self.read_calls: list[Path] = []

    def read(self, source_path: str | Path) -> pd.DataFrame:
        path = Path(source_path)
        self.read_calls.append(path)
        return self.data_frame


class FakeWriter:
    def __init__(self) -> None:
        self.write_calls: list[tuple[pd.DataFrame, Path, TabularFileType | None]] = []

    def write(
        self,
        data_frame: pd.DataFrame,
        target_path: str | Path,
        target_type: TabularFileType | None = None,
    ) -> Path:
        path = Path(target_path)
        self.write_calls.append((data_frame, path, target_type))
        return path


def test_write_dataframe_delegates_to_writer() -> None:
    reader = FakeReader(pd.DataFrame({"a": [1]}))
    writer = FakeWriter()
    converter = TabularConverter(reader=reader, writer=writer)

    result = converter.write_dataframe(
        pd.DataFrame({"total": [5]}),
        "salidas/reporte.csv",
        TabularFileType.CSV,
    )

    assert result == Path("salidas/reporte.csv")
    assert writer.write_calls[0][1] == Path("salidas/reporte.csv")
    assert writer.write_calls[0][2] == TabularFileType.CSV


def test_save_prepared_conversion_uses_prepared_dataframe() -> None:
    data_frame = pd.DataFrame({"nombre": ["Ana"]})
    reader = FakeReader(data_frame)
    writer = FakeWriter()
    converter = TabularConverter(reader=reader, writer=writer)
    prepared = PreparedConversion(
        source_path=Path("datos/clientes.csv"),
        source_format=TabularFileType.CSV,
        target_format=TabularFileType.JSON,
        data_frame=data_frame,
    )

    result = converter.save_prepared_conversion(prepared, "salidas/clientes.json")

    assert result == Path("salidas/clientes.json")
    assert writer.write_calls[0][0].equals(data_frame)
    assert writer.write_calls[0][2] == TabularFileType.JSON


def test_prepare_conversion_reads_source_and_records_formats(tmp_path: Path) -> None:
    source = tmp_path / "clientes.csv"
    source.write_text("nombre\nAna\n", encoding="utf-8")
    data_frame = pd.DataFrame({"nombre": ["Ana"]})
    reader = FakeReader(data_frame)
    converter = TabularConverter(reader=reader, writer=FakeWriter())

    prepared = converter.prepare_conversion(source, TabularFileType.JSON)

    assert prepared.source_path == source
    assert prepared.source_format == TabularFileType.CSV
    assert prepared.target_format == TabularFileType.JSON
    assert prepared.data_frame is data_frame
    assert reader.read_calls == [source]


def test_prepare_conversion_rejects_same_source_and_target_format(
    tmp_path: Path,
) -> None:
    source = tmp_path / "clientes.csv"
    source.write_text("nombre\nAna\n", encoding="utf-8")
    reader = FakeReader(pd.DataFrame({"nombre": ["Ana"]}))
    converter = TabularConverter(reader=reader, writer=FakeWriter())

    with pytest.raises(ValidationError, match="distinto"):
        converter.prepare_conversion(source, TabularFileType.CSV)

    assert reader.read_calls == []
