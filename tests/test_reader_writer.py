from pathlib import Path

import pandas as pd
import pytest

from src.core.reader import TabularReader
from src.core.writer import TabularWriter
from src.utils.errors import ReadError


def test_reader_loads_tsv_as_dataframe(tmp_path: Path) -> None:
    source = tmp_path / "datos.tsv"
    source.write_text("nombre\tedad\nAna\t30\nLuis\t28\n", encoding="utf-8")

    data_frame = TabularReader().read(source)

    assert list(data_frame.columns) == ["nombre", "edad"]
    assert data_frame.iloc[0]["nombre"] == "Ana"


def test_writer_exports_xml_and_reader_loads_it_back(tmp_path: Path) -> None:
    data_frame = pd.DataFrame(
        {
            "nombre": ["Ana", "Luis"],
            "edad": [30, 28],
        }
    )
    target = tmp_path / "salida.xml"

    writer = TabularWriter()
    writer.write(data_frame, target)
    loaded = TabularReader().read(target)

    assert list(loaded.columns) == ["nombre", "edad"]
    assert loaded.iloc[1]["nombre"] == "Luis"


def test_reader_raises_clear_error_for_invalid_xml(tmp_path: Path) -> None:
    source = tmp_path / "invalido.xml"
    source.write_text("<root><row><name>Ana</name></row>", encoding="utf-8")

    with pytest.raises(ReadError) as exc_info:
        TabularReader().read(source)

    assert "XML" in str(exc_info.value)
