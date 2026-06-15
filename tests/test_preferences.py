"""Pruebas unitarias para la persistencia simple de preferencias."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

from src.utils.preferences import (
    APP_DATA_DIRECTORY,
    PORTABLE_MARKER_FILENAME,
    AppPreferences,
    PreferencesManager,
)


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


@pytest.mark.parametrize(
    ("payload", "expected_language", "expected_theme"),
    [
        ('{"language_code": "fr", "theme_code": "neon"}', "es", "light"),
        ('{"language_code": 123, "theme_code": false}', "es", "light"),
        ("[]", "es", "light"),
    ],
)
def test_load_normalizes_invalid_preference_values(
    tmp_path: Path,
    payload: str,
    expected_language: str,
    expected_theme: str,
) -> None:
    file_path = tmp_path / "preferences.json"
    file_path.write_text(payload, encoding="utf-8")

    preferences = PreferencesManager(file_path).load()

    assert preferences.language_code == expected_language
    assert preferences.theme_code == expected_theme


def test_manager_uses_only_the_explicit_temporary_path(tmp_path: Path) -> None:
    file_path = tmp_path / "nested" / "preferences.json"
    manager = PreferencesManager(file_path)

    manager.save(AppPreferences(last_target_format="xml"))

    assert manager.file_path == file_path
    assert file_path.exists()


def test_default_path_uses_project_root_when_running_from_source(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """La ejecución con Python debe conservar la preferencia en el proyecto."""

    monkeypatch.delattr(sys, "frozen", raising=False)

    manager = PreferencesManager()

    expected_root = Path(__file__).resolve().parents[1]
    assert manager.file_path == expected_root / "preferences.json"


def test_default_path_uses_executable_directory_in_portable_mode(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """El marcador portable debe mantener las preferencias junto a la app."""

    executable_dir = tmp_path / "portable"
    executable_dir.mkdir()
    executable_path = executable_dir / "ConversorFormatos.exe"
    (executable_dir / PORTABLE_MARKER_FILENAME).write_text(
        "Portable distribution marker.\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(sys, "frozen", True, raising=False)
    monkeypatch.setattr(sys, "executable", str(executable_path))
    monkeypatch.setenv("APPDATA", str(tmp_path / "appdata"))

    manager = PreferencesManager()

    assert manager.file_path == executable_dir / "preferences.json"


def test_default_path_uses_appdata_in_installed_mode(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Un ejecutable sin marcador portable debe usar el perfil del usuario."""

    executable_dir = tmp_path / "installed"
    executable_dir.mkdir()
    executable_path = executable_dir / "ConversorFormatos.exe"
    app_data_dir = tmp_path / "appdata"
    monkeypatch.setattr(sys, "frozen", True, raising=False)
    monkeypatch.setattr(sys, "executable", str(executable_path))
    monkeypatch.setenv("APPDATA", str(app_data_dir))

    manager = PreferencesManager()

    assert manager.file_path == (
        app_data_dir / APP_DATA_DIRECTORY / "preferences.json"
    )
