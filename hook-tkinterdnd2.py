"""Hook de PyInstaller para incluir los binarios de tkdnd.

`tkinterdnd2` necesita empaquetar su carpeta interna con librerias Tcl/Tk.
Mantener este hook en la raiz hace mas estable la generacion del ejecutable.
"""

from PyInstaller.utils.hooks import collect_data_files


datas = collect_data_files("tkinterdnd2")
