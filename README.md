# Conversor de Formatos Tabulares

Aplicación de escritorio creada con Python y Tkinter para convertir archivos tabulares entre formatos comunes. La app permite cargar un archivo, revisar una vista previa de los datos, elegir un formato de salida, preparar la conversión y guardar el archivo convertido.

Versión actual: 2.0.0

Autor: Fernando Corrales Quirós

Manual de usuario: [MANUAL_USUARIO.md](/C:/Users/Fernando/Documents/Conversor_formatos/MANUAL_USUARIO.md)

## Formatos soportados

Formatos de entrada:

- CSV (`.csv`)
- Excel (`.xlsx`)
- JSON (`.json`)
- Texto delimitado (`.txt`)

Formatos de salida:

- CSV (`.csv`)
- Excel (`.xlsx`)
- JSON (`.json`)
- Texto delimitado (`.txt`)

## Requisitos

- Python 3.11 o superior
- Windows, macOS o Linux con soporte para Tkinter

Tkinter normalmente viene incluido con Python. Si tu instalación no lo incluye, instala el paquete correspondiente para tu sistema operativo.

## Instalación

Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```powershell
pip install -r requirements.txt
```

## Ejecutar la app

Desde la raíz del proyecto:

```powershell
python app.py
```

Para una guía paso a paso orientada a usuarios no técnicos, consulta el manual de usuario en [MANUAL_USUARIO.md](/C:/Users/Fernando/Documents/Conversor_formatos/MANUAL_USUARIO.md).

## Cómo convertir archivos

1. Abrir la aplicación con `python app.py`.
2. Presionar el botón `Seleccionar archivo` o arrastrar y soltar un archivo compatible en la ventana principal.
3. Revisar la información visible del archivo cargado: nombre, extensión, tamaño aproximado y filas cuando aplique.
4. Elegir un archivo compatible: `.csv`, `.xlsx`, `.json` o `.txt`.
5. Usar `Vista previa` para revisar los datos cargados.
6. Seleccionar el formato de salida.
7. Presionar `Convertir` para preparar el archivo.
8. Presionar `Guardar convertido` para elegir la ubicación final.
9. Usar `Limpiar` si deseas reiniciar la interfaz sin cerrar la aplicación.

La app muestra mensajes claros si el archivo está vacío, si el formato no es compatible o si ocurre un error de lectura o escritura.

## Pruebas

Ejecutar la suite de pruebas:

```powershell
pytest
```

También puedes validar la sintaxis rápidamente con:

```powershell
python -m compileall app.py src tests
```

## Empaquetado con PyInstaller

Este proyecto incluye una base para generar un ejecutable con PyInstaller mediante el archivo `ConversorFormatos.spec`.

Opción directa:

```powershell
pyinstaller ConversorFormatos.spec
```

O usando el script incluido:

```powershell
.\scripts\build.ps1
```

El ejecutable quedará dentro de la carpeta `dist/`.

## Estructura del proyecto

```text
.
|-- app.py
|-- ConversorFormatos.spec
|-- MANUAL_USUARIO.md
|-- README.md
|-- hook-tkinterdnd2.py
|-- requirements.txt
|-- scripts/
|   `-- build.ps1
|-- src/
|   |-- core/
|   |   |-- converter.py
|   |   |-- file_types.py
|   |   |-- reader.py
|   |   |-- validators.py
|   |   `-- writer.py
|   |-- gui/
|   |   |-- about_window.py
|   |   |-- dialogs.py
|   |   |-- drag_drop.py
|   |   |-- help_window.py
|   |   |-- main_window.py
|   |   `-- preview_table.py
|   |-- services/
|   |   |-- file_service.py
|   |   `-- preview_service.py
|   `-- utils/
|       |-- constants.py
|       |-- errors.py
|       `-- helpers.py
`-- tests/
    |-- test_converter.py
    |-- test_drag_drop.py
    |-- test_file_service.py
    |-- test_file_types.py
    `-- test_validators.py
```

## Arquitectura

- `src/gui`: ventanas, diálogos y componentes visuales de Tkinter.
- `src/gui/drag_drop.py`: integración real de arrastre y suelta con `tkinterdnd2`.
- `src/core`: lógica central de lectura, escritura, conversión, tipos de archivo y validaciones.
- `src/services`: capa de coordinación entre la interfaz y la lógica de negocio.
- `src/utils`: constantes, helpers y excepciones personalizadas.
- `tests`: pruebas unitarias de la base del proyecto.

## Estado del proyecto

Esta es una base lista para continuar el desarrollo y publicarse en GitHub. La arquitectura ya separa interfaz, servicios, lógica de conversión, validaciones, utilidades y pruebas, e incluye soporte para selección manual y drag and drop de archivos compatibles.

Pendientes sugeridos:

- Agregar más pruebas de integración con archivos reales de ejemplo.
- Agregar un pipeline de CI para ejecutar pruebas automáticamente.
