"""Pruebas unitarias para la resolución ligera de traducciones."""

from __future__ import annotations

import pytest

from src.i18n.translations import Translator, build_translator


def test_build_translator_falls_back_to_spanish() -> None:
    translator = build_translator("unsupported")

    assert translator.language_code == "es"


def test_translator_formats_text_values() -> None:
    translator = Translator("en")

    result = translator.t("messages.status_saved", name="report.csv")

    assert result == "Saved file: report.csv"


def test_translator_rejects_non_text_catalog_nodes() -> None:
    translator = Translator("es")

    with pytest.raises(TypeError):
        translator.t("messages")
