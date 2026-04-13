"""Pruebas unitarias para el soporte opcional de drag and drop."""

from __future__ import annotations

from pathlib import Path

from src.future.drag_drop import split_drop_paths


def test_split_drop_paths_supports_braced_windows_paths() -> None:
    """Debe conservar rutas con espacios cuando Tk las envia entre llaves."""

    raw_data = r"{C:\Archivos de prueba\datos base.csv}"

    paths = split_drop_paths(raw_data)

    assert paths == [Path(r"C:\Archivos de prueba\datos base.csv")]


def test_split_drop_paths_supports_single_plain_path() -> None:
    """Debe aceptar una ruta simple cuando solo se suelta un archivo."""

    raw_data = r"C:\datos\entrada.xlsx"

    paths = split_drop_paths(raw_data)

    assert paths == [Path(r"C:\datos\entrada.xlsx")]
