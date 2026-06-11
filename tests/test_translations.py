"""Pruebas unitarias para la resolución ligera de traducciones."""

from __future__ import annotations

import pytest

from src.i18n.translations import (
    SUPPORTED_LANGUAGES,
    UI_TEXTS,
    Translator,
    build_translator,
)

MINIMUM_TEXT_KEYS = (
    "app.title",
    "buttons.select_file",
    "buttons.convert",
    "buttons.save",
    "sections.preview",
    "messages.default_status",
    "titles.help",
)


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


@pytest.mark.parametrize("language_code", ["es", "en"])
def test_supported_languages_expose_minimum_interface_texts(
    language_code: str,
) -> None:
    translator = Translator(language_code)

    assert language_code in SUPPORTED_LANGUAGES
    for key in MINIMUM_TEXT_KEYS:
        assert translator.t(key).strip()


def test_language_catalogs_share_the_same_top_level_sections() -> None:
    assert UI_TEXTS["es"].keys() == UI_TEXTS["en"].keys()


def test_runtime_domain_message_is_translated_to_english() -> None:
    translator = Translator("en")

    result = translator.translate_runtime_message(
        "El archivo seleccionado no existe."
    )

    assert result == "The selected file does not exist."


def test_unknown_runtime_message_is_preserved() -> None:
    message = "Mensaje externo no catalogado."

    assert Translator("en").translate_runtime_message(message) == message
