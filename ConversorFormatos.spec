# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

from PyInstaller.utils.hooks import collect_data_files


# pandas descubre los motores de Excel de forma dinámica. Declarar únicamente
# esos módulos evita empaquetar sus suites de pruebas y dependencias opcionales.
hiddenimports = [
    "openpyxl",
    "odf.config",
    "odf.element",
    "odf.namespaces",
    "odf.office",
    "odf.opendocument",
    "odf.style",
    "odf.table",
    "odf.text",
    "pandas.io.excel._odfreader",
    "pandas.io.excel._odswriter",
    "pandas.io.excel._openpyxl",
    "tkinterdnd2",
]
excludes = [
    "IPython",
    "PySide6",
    "ipykernel",
    "jupyter_client",
    "jupyter_core",
    "matplotlib",
    "numba",
    "pytest",
    "scipy",
    "sklearn",
    "zmq",
]
icon_file = Path("assets/icon.ico")
datas = collect_data_files("tkinterdnd2")

# `assets/icon.ico` es el icono principal del ejecutable.
# Si en el futuro cambia la ubicacion o el nombre, ajusta esta referencia.
if icon_file.exists():
    datas.append((str(icon_file), "assets"))


a = Analysis(
    ["app.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=["."],
    hooksconfig={},
    runtime_hooks=[],
    excludes=excludes,
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="ConversorFormatos",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=str(icon_file) if icon_file.exists() else None,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="ConversorFormatos",
)
