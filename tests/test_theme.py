import pytest

from src.gui.theme import DEFAULT_THEME, SUPPORTED_THEMES, get_palette

REQUIRED_PALETTE_KEYS = {
    "bg",
    "surface",
    "surface_alt",
    "surface_soft",
    "border",
    "border_soft",
    "text",
    "muted",
    "accent",
    "accent_hover",
    "accent_light",
    "accent_text",
    "selection",
}


def test_default_theme_is_supported() -> None:
    assert DEFAULT_THEME in SUPPORTED_THEMES


@pytest.mark.parametrize("theme_code", ["light", "dark"])
def test_supported_theme_palettes_expose_required_colors(theme_code: str) -> None:
    palette = get_palette(theme_code)

    assert REQUIRED_PALETTE_KEYS <= palette.keys()
    assert all(palette[key].startswith("#") for key in REQUIRED_PALETTE_KEYS)


def test_unknown_theme_uses_safe_default_palette() -> None:
    assert get_palette("unknown") == get_palette(DEFAULT_THEME)


def test_get_palette_returns_an_independent_copy() -> None:
    palette = get_palette("light")
    palette["bg"] = "#000000"

    assert get_palette("light")["bg"] != "#000000"
