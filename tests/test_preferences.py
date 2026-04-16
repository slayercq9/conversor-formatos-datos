"""Pruebas unitarias para la persistencia simple de preferencias."""

from __future__ import annotations

from pathlib import Path

from src.utils.preferences import AppPreferences, PreferencesManager


def test_load_returns_defaults_when_file_is_missing(tmp_path: Path) -> None:
    """Debe devolver valores por defecto si el archivo no existe."""

    manager = PreferencesManager(tmp_path / "preferences.json")

    preferences = manager.load()

    assert preferences == AppPreferences()


def test_load_returns_defaults_when_file_is_invalid(tmp_path: Path) -> None:
    """Debe ignorar archivos dañados sin interrumpir la app."""

    file_path = tmp_path / "preferences.json"
    file_path.write_text("{not-valid-json", encoding="utf-8")
    manager = PreferencesManager(file_path)

    preferences = manager.load()

    assert preferences == AppPreferences()


def test_load_uses_safe_default_theme_when_value_is_invalid(tmp_path: Path) -> None:
    """Debe caer a un tema seguro si el JSON trae un valor no soportado."""

    file_path = tmp_path / "preferences.json"
    file_path.write_text('{"theme_code": "neon"}', encoding="utf-8")
    manager = PreferencesManager(file_path)

    preferences = manager.load()

    assert preferences.theme_code == "light"


def test_save_and_load_roundtrip_preferences(tmp_path: Path) -> None:
    """Debe conservar preferencias simples entre guardado y lectura."""

    file_path = tmp_path / "preferences.json"
    manager = PreferencesManager(file_path)
    expected = AppPreferences(
        last_target_format="json",
        language_code="en",
        theme_code="dark",
        window_width=1200,
        window_height=800,
        window_x=25,
        window_y=40,
    )

    manager.save(expected)

    assert manager.load() == expected
