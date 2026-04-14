"""Persistencia simple de preferencias locales de la aplicación.

Este módulo guarda un JSON pequeño junto a la app para mantener la
portabilidad. Si el archivo no existe o está dañado, se usan valores
por defecto sin interrumpir la ejecución.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
import sys
from typing import Any


@dataclass(slots=True)
class AppPreferences:
    """Representa las preferencias livianas que la GUI puede recordar."""

    last_target_format: str = ""
    window_width: int | None = None
    window_height: int | None = None
    window_x: int | None = None
    window_y: int | None = None


class PreferencesManager:
    """Carga y guarda preferencias en un archivo JSON portable."""

    def __init__(self, file_path: Path | None = None) -> None:
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

    def _resolve_default_path(self) -> Path:
        """Ubica el archivo junto a la app para mantener el modo portable."""

        if getattr(sys, "frozen", False):
            base_dir = Path(sys.executable).resolve().parent
        else:
            base_dir = Path(__file__).resolve().parents[2]
        return base_dir / "preferences.json"

    def _coerce_str(self, value: Any) -> str:
        """Normaliza cadenas opcionales provenientes del JSON."""

        return value if isinstance(value, str) else ""

    def _coerce_int(self, value: Any) -> int | None:
        """Normaliza enteros opcionales provenientes del JSON."""

        return value if isinstance(value, int) else None
