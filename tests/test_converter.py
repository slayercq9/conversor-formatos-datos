from pathlib import Path

import pandas as pd

from src.core.converter import PreparedConversion, TabularConverter
from src.core.file_types import TabularFileType


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
