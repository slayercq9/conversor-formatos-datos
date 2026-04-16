from __future__ import annotations

from pathlib import Path
from tkinter import filedialog, messagebox


def ask_open_path(file_types: list[tuple[str, str]], title: str) -> str:
    return filedialog.askopenfilename(title=title, filetypes=file_types)


def ask_save_path(
    default_path: str | Path,
    file_types: list[tuple[str, str]],
    title: str,
) -> str:
    path = Path(default_path)
    return filedialog.asksaveasfilename(
        title=title,
        initialfile=path.name,
        initialdir=str(path.parent),
        defaultextension=path.suffix,
        filetypes=file_types,
    )


def show_info(title: str, message: str) -> None:
    messagebox.showinfo(title, message)


def show_error(title: str, message: str) -> None:
    messagebox.showerror(title, message)


def show_warning(title: str, message: str) -> None:
    messagebox.showwarning(title, message)
