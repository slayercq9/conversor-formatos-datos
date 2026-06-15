"""Persistencia simple de preferencias locales de la aplicación.

El modo instalado usa la carpeta escribible del usuario, mientras que el
paquete portable conserva el JSON junto al ejecutable. Durante el desarrollo,
el archivo permanece en la raíz del proyecto. Si no existe o está dañado, se
usan valores por defecto sin interrumpir la ejecución.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path
import sys
from typing import Any


PREFERENCES_FILENAME = "preferences.json"
PORTABLE_MARKER_FILENAME = "portable.mode"
APP_DATA_DIRECTORY = "ConversorFormatos"


@dataclass(slots=True)
class AppPreferences:
    """Representa las preferencias livianas que la GUI puede recordar."""

    last_target_format: str = ""
    language_code: str = "es"
    theme_code: str = "light"
    window_width: int | None = None
    window_height: int | None = None
    window_x: int | None = None
    window_y: int | None = None


class PreferencesManager:
    """Carga y guarda preferencias en un archivo JSON local y escribible."""

    def __init__(self, file_path: Path | None = None) -> None:
        """Usa una ruta explícita o la ubicación apropiada para la ejecución."""
        self._file_path = file_path or self._resolve_default_path()

    @property
    def file_path(self) -> Path:
        """Expone la ruta efectiva del archivo de preferencias."""

        return self._file_path

    def load(self) -> AppPreferences:
        """Lee preferencias desde disco con tolerancia a errores."""

        if not self._file_path.exists():
            return AppPreferences()

        try:
            payload = json.loads(self._file_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return AppPreferences()

        if not isinstance(payload, dict):
            return AppPreferences()

        return AppPreferences(
            last_target_format=self._coerce_str(payload.get("last_target_format")),
            language_code=self._coerce_language(payload.get("language_code")),
            theme_code=self._coerce_theme(payload.get("theme_code")),
            window_width=self._coerce_int(payload.get("window_width")),
            window_height=self._coerce_int(payload.get("window_height")),
            window_x=self._coerce_int(payload.get("window_x")),
            window_y=self._coerce_int(payload.get("window_y")),
        )

    def save(self, preferences: AppPreferences) -> None:
        """Guarda preferencias en disco sin propagar fallos comunes."""

        try:
            self._file_path.parent.mkdir(parents=True, exist_ok=True)
            self._file_path.write_text(
                json.dumps(asdict(preferences), indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
        except OSError:
            return

    @staticmethod
    def _resolve_default_path() -> Path:
        """Selecciona una ruta segura para código fuente, portable o instalado."""

        if not getattr(sys, "frozen", False):
            project_root = Path(__file__).resolve().parents[2]
            return project_root / PREFERENCES_FILENAME

        executable_dir = Path(sys.executable).resolve().parent
        if (executable_dir / PORTABLE_MARKER_FILENAME).is_file():
            return executable_dir / PREFERENCES_FILENAME

        app_data_root = os.environ.get("APPDATA")
        if app_data_root:
            return (
                Path(app_data_root)
                / APP_DATA_DIRECTORY
                / PREFERENCES_FILENAME
            )

        roaming_fallback = Path.home() / "AppData" / "Roaming"
        return roaming_fallback / APP_DATA_DIRECTORY / PREFERENCES_FILENAME

    @staticmethod
    def _coerce_str(value: Any) -> str:
        """Normaliza cadenas opcionales provenientes del JSON."""

        return value if isinstance(value, str) else ""

    @staticmethod
    def _coerce_language(value: Any) -> str:
        """Normaliza el idioma guardado y cae a español por defecto."""

        if isinstance(value, str) and value in {"es", "en"}:
            return value
        return "es"

    @staticmethod
    def _coerce_theme(value: Any) -> str:
        """Normaliza el tema guardado y cae a claro por defecto."""

        if isinstance(value, str) and value in {"light", "dark"}:
            return value
        return "light"

    @staticmethod
    def _coerce_int(value: Any) -> int | None:
        """Normaliza enteros opcionales provenientes del JSON."""

        return value if isinstance(value, int) else None
