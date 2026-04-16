from src.gui.theme import DEFAULT_THEME, SUPPORTED_THEMES, get_palette


def test_default_theme_is_supported() -> None:
    assert DEFAULT_THEME in SUPPORTED_THEMES


def test_dark_theme_palette_exposes_required_colors() -> None:
    palette = get_palette("dark")
    for key in (
        "bg",
        "surface",
        "surface_alt",
        "border",
        "text",
        "muted",
        "accent",
        "accent_hover",
        "selection",
    ):
        assert key in palette


def test_unknown_theme_uses_safe_default_palette() -> None:
    assert get_palette("unknown") == get_palette(DEFAULT_THEME)
