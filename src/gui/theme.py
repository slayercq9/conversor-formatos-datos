"""Configuracion visual centralizada para los temas de la interfaz.

Este modulo mantiene una capa ligera de temas para evitar repetir
paletas y estilos en cada ventana. El objetivo es conservar una base
portable y facil de mantener usando solo Tkinter/ttk.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


DEFAULT_THEME = "light"
SUPPORTED_THEMES = ("light", "dark")


THEME_PALETTES: dict[str, dict[str, str]] = {
    "light": {
        "bg": "#dfe8f6",
        "surface": "#f8fbff",
        "surface_alt": "#edf3fb",
        "surface_soft": "#f3f7fd",
        "border": "#93a7c0",
        "border_soft": "#c0cede",
        "text": "#1f2d3d",
        "muted": "#5e6d7d",
        "accent": "#3f78b5",
        "accent_hover": "#2f6297",
        "accent_light": "#eaf2fc",
        "accent_text": "#ffffff",
        "selection": "#7fa7d6",
    },
    "dark": {
        "bg": "#17202b",
        "surface": "#1f2b39",
        "surface_alt": "#273647",
        "surface_soft": "#223141",
        "border": "#425466",
        "border_soft": "#52657a",
        "text": "#edf3fb",
        "muted": "#b2c0cf",
        "accent": "#5e9ae0",
        "accent_hover": "#7bafea",
        "accent_light": "#32465d",
        "accent_text": "#08111c",
        "selection": "#4c7db3",
    },
}


def get_palette(theme_code: str) -> dict[str, str]:
    """Devuelve la paleta del tema solicitado con fallback seguro."""

    return THEME_PALETTES.get(theme_code, THEME_PALETTES[DEFAULT_THEME]).copy()


def apply_theme(root: tk.Misc, theme_code: str) -> dict[str, str]:
    """Aplica una paleta y estilos ttk reutilizables a toda la aplicacion."""

    palette = get_palette(theme_code)
    style = ttk.Style(root)
    if "clam" in style.theme_names():
        style.theme_use("clam")

    root.configure(background=palette["bg"])

    style.configure("TFrame", background=palette["bg"])
    style.configure("Surface.TFrame", background=palette["surface"])
    style.configure("Toolbar.TFrame", background=palette["surface"])
    style.configure(
        "Hero.TFrame",
        background=palette["surface"],
        relief="groove",
        borderwidth=1,
        lightcolor=palette["surface_soft"],
        darkcolor=palette["border"],
    )
    style.configure(
        "Modal.TFrame",
        background=palette["surface"],
    )
    style.configure(
        "Section.TLabelframe",
        background=palette["surface"],
        bordercolor=palette["border_soft"],
        relief="flat",
        borderwidth=1,
        padding=12,
        lightcolor=palette["surface_soft"],
        darkcolor=palette["border_soft"],
    )
    style.configure(
        "Section.TLabelframe.Label",
        background=palette["bg"],
        foreground=palette["accent"],
        font=("Segoe UI", 10, "bold"),
        padding=(6, 0),
    )

    style.configure("TLabel", background=palette["bg"], foreground=palette["text"])
    style.configure("Surface.TLabel", background=palette["surface"], foreground=palette["text"])
    style.configure(
        "HeroTitle.TLabel",
        background=palette["surface"],
        foreground=palette["text"],
        font=("Segoe UI", 18, "bold"),
    )
    style.configure(
        "HeroSubtitle.TLabel",
        background=palette["surface"],
        foreground=palette["muted"],
        font=("Segoe UI", 10),
    )
    style.configure(
        "ModalTitle.TLabel",
        background=palette["surface"],
        foreground=palette["text"],
        font=("Segoe UI", 16, "bold"),
    )
    style.configure(
        "ModalBody.TLabel",
        background=palette["surface"],
        foreground=palette["text"],
        font=("Segoe UI", 9),
    )
    style.configure(
        "SectionHint.TLabel",
        background=palette["surface"],
        foreground=palette["muted"],
        font=("Segoe UI", 9),
    )
    style.configure(
        "InfoValue.TLabel",
        background=palette["surface_alt"],
        foreground=palette["text"],
        font=("Segoe UI", 9),
        padding=(11, 9),
        relief="groove",
        borderwidth=1,
    )
    style.configure(
        "Status.TLabel",
        background=palette["surface_alt"],
        foreground=palette["muted"],
        font=("Segoe UI", 9),
        padding=(11, 9),
        relief="groove",
        borderwidth=1,
    )

    style.configure(
        "TButton",
        padding=(12, 7),
        font=("Segoe UI", 9),
        relief="raised",
        borderwidth=1,
        focusthickness=1,
        focuscolor=palette["border_soft"],
    )
    style.map(
        "TButton",
        foreground=[("disabled", palette["muted"])],
    )
    style.configure(
        "Accent.TButton",
        background=palette["accent"],
        foreground=palette["accent_text"],
        borderwidth=1,
        lightcolor=palette["accent_hover"],
        darkcolor=palette["border"],
    )
    style.map(
        "Accent.TButton",
        background=[("active", palette["accent_hover"]), ("disabled", palette["border_soft"])],
        foreground=[("disabled", palette["surface_soft"])],
    )
    style.configure(
        "Secondary.TButton",
        background=palette["accent_light"],
        foreground=palette["text"],
        bordercolor=palette["border"],
        lightcolor=palette["surface_soft"],
        darkcolor=palette["border"],
    )
    style.map(
        "Secondary.TButton",
        background=[("active", palette["surface_alt"]), ("disabled", palette["surface_alt"])],
    )

    style.configure(
        "TCombobox",
        fieldbackground=palette["surface_alt"],
        background=palette["surface"],
        foreground=palette["text"],
        bordercolor=palette["border"],
        lightcolor=palette["surface_soft"],
        darkcolor=palette["border"],
        arrowsize=14,
        padding=(6, 4),
    )
    style.map(
        "TCombobox",
        fieldbackground=[("readonly", palette["surface_alt"])],
        foreground=[("readonly", palette["text"])],
        selectbackground=[("readonly", palette["selection"])],
        selectforeground=[("readonly", palette["text"])],
    )

    style.configure(
        "Preview.Treeview",
        background=palette["surface"],
        fieldbackground=palette["surface"],
        foreground=palette["text"],
        bordercolor=palette["border"],
        rowheight=28,
    )
    style.map(
        "Preview.Treeview",
        background=[("selected", palette["selection"])],
        foreground=[("selected", palette["text"])],
    )
    style.configure(
        "Preview.Treeview.Heading",
        background=palette["surface_alt"],
        foreground=palette["text"],
        font=("Segoe UI", 9, "bold"),
        relief="raised",
        padding=(8, 7),
    )
    style.map(
        "Preview.Treeview.Heading",
        background=[("active", palette["surface_soft"])],
    )
    style.configure(
        "PreviewSummary.TLabel",
        background=palette["surface"],
        foreground=palette["text"],
        font=("Segoe UI", 10, "bold"),
    )

    return palette


def apply_toplevel_theme(window: tk.Toplevel, theme_code: str) -> dict[str, str]:
    """Aplica el color de fondo base a una ventana secundaria."""

    palette = get_palette(theme_code)
    window.configure(background=palette["bg"])
    return palette
