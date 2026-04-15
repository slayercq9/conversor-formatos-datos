from pathlib import Path

import pandas as pd
import pytest

from src.core.reader import TabularReader
from src.core.writer import TabularWriter
from src.utils.errors import ReadError, WriteError


def test_reader_loads_tsv_as_dataframe(tmp_path: Path) -> None:
    source = tmp_path / "datos.tsv"
    source.write_text("nombre\tedad\nAna\t30\nLuis\t28\n", encoding="utf-8")

    data_frame = TabularReader().read(source)

    assert list(data_frame.columns) == ["nombre", "edad"]
    assert data_frame.iloc[0]["nombre"] == "Ana"


def test_reader_uses_odf_engine_for_ods(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, object] = {}

    def fake_read_excel(path: Path, *args: object, **kwargs: object) -> pd.DataFrame:
        captured["path"] = path
        captured["kwargs"] = kwargs
        return pd.DataFrame({"nombre": ["Ana"]})

    monkeypatch.setattr(pd, "read_excel", fake_read_excel)

    source = Path("archivo.ods")
    data_frame = TabularReader()._read_ods(source)

    assert list(data_frame.columns) == ["nombre"]
    assert captured["path"] == source
    assert captured["kwargs"] == {"engine": "odf"}


def test_reader_reports_missing_odf_dependency_for_ods(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_read_excel(*args: object, **kwargs: object) -> pd.DataFrame:
        raise ImportError("missing odf")

    monkeypatch.setattr(pd, "read_excel", fake_read_excel)

    with pytest.raises(ReadError) as exc_info:
        TabularReader()._read_ods(Path("archivo.ods"))

    assert "odfpy" in str(exc_info.value)


def test_writer_uses_odf_engine_for_ods(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, object] = {}

    def fake_to_excel(
        self: pd.DataFrame,
        path: Path,
        *args: object,
        **kwargs: object,
    ) -> None:
        captured["path"] = path
        captured["kwargs"] = kwargs

    monkeypatch.setattr(pd.DataFrame, "to_excel", fake_to_excel)

    data_frame = pd.DataFrame({"nombre": ["Ana"]})
    target = Path("salida.ods")

    TabularWriter()._write_ods(data_frame, target)

    assert captured["path"] == target
    assert captured["kwargs"] == {"index": False, "engine": "odf"}


def test_writer_reports_missing_odf_dependency_for_ods(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_to_excel(
        self: pd.DataFrame,
        path: Path,
        *args: object,
        **kwargs: object,
    ) -> None:
        _ = self
        _ = path
        _ = args
        _ = kwargs
        raise ImportError("missing odf")

    monkeypatch.setattr(pd.DataFrame, "to_excel", fake_to_excel)

    with pytest.raises(WriteError) as exc_info:
        TabularWriter()._write_ods(pd.DataFrame({"nombre": ["Ana"]}), Path("salida.ods"))

    assert "odfpy" in str(exc_info.value)


def test_reader_reports_json_not_tabular(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_read_json(path: Path) -> pd.DataFrame:
        _ = path
        raise ValueError("invalid json")

    monkeypatch.setattr(pd, "read_json", fake_read_json)

    with pytest.raises(ReadError) as exc_info:
        TabularReader()._read_json(Path("datos.json"))

    assert "JSON" in str(exc_info.value)


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
