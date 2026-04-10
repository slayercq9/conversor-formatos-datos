# Conversor de Formatos Tabulares

Aplicacion de escritorio creada con Python y Tkinter para convertir archivos tabulares entre formatos comunes. La app permite cargar un archivo, revisar una vista previa de los datos, elegir un formato de salida, preparar la conversion y guardar el archivo convertido.

Version actual: 1.2.0

Autor: Fernando Corrales Quiros

Manual de usuario: [MANUAL_USUARIO.md](/C:/Users/Fernando/Documents/Conversor_formatos/MANUAL_USUARIO.md)

## Formatos Soportados

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

Tkinter normalmente viene incluido con Python. Si tu instalacion no lo incluye, instala el paquete correspondiente para tu sistema operativo.

## Instalacion

Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```powershell
pip install -r requirements.txt
```

## Ejecutar la App

Desde la raiz del proyecto:

```powershell
python app.py
```

Para una guia paso a paso orientada a usuarios no tecnicos, consulta el manual de usuario en [MANUAL_USUARIO.md](/C:/Users/Fernando/Documents/Conversor_formatos/MANUAL_USUARIO.md).

## Como Convertir Archivos

1. Abrir la aplicacion con `python app.py`.
2. Presionar el boton `Seleccionar archivo`.
3. Elegir un archivo compatible: `.csv`, `.xlsx`, `.json` o `.txt`.
4. Usar `Vista previa` para revisar los datos cargados.
5. Seleccionar el formato de salida.
6. Presionar `Convertir` para preparar el archivo.
7. Presionar `Guardar convertido` para elegir la ubicacion final.

La app muestra mensajes claros si el archivo esta vacio, si el formato no es soportado o si ocurre un error de lectura o escritura.

## Pruebas

Ejecutar la suite de pruebas:

```powershell
pytest
```

Tambien puedes validar sintaxis rapidamente con:

```powershell
python -m compileall app.py src tests
```

## Empaquetado con PyInstaller

Este proyecto incluye una base para generar un ejecutable con PyInstaller mediante el archivo `ConversorFormatos.spec`.

Opcion directa:

```powershell
pyinstaller ConversorFormatos.spec
```

O usando el script incluido:

```powershell
.\scripts\build.ps1
```

El ejecutable quedara dentro de la carpeta `dist/`.

## Estructura del Proyecto

```text
.
|-- app.py
|-- ConversorFormatos.spec
|-- MANUAL_USUARIO.md
|-- README.md
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
|   |-- future/
|   |   `-- drag_drop.py
|   |-- gui/
|   |   |-- about_window.py
|   |   |-- dialogs.py
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
    |-- test_file_service.py
    |-- test_file_types.py
    `-- test_validators.py
```

## Arquitectura

- `src/gui`: ventanas, dialogos y componentes visuales de Tkinter.
- `src/core`: logica central de lectura, escritura, conversion, tipos de archivo y validaciones.
- `src/services`: capa de coordinacion entre la interfaz y la logica de negocio.
- `src/utils`: constantes, helpers y excepciones personalizadas.
- `src/future`: puntos preparados para extensiones futuras, como drag and drop.
- `tests`: pruebas unitarias de la base del proyecto.

## Estado del Proyecto

Esta es una base lista para continuar desarrollo y publicarse en GitHub. La arquitectura ya separa interfaz, servicios, logica de conversion, validaciones, utilidades y pruebas.

Pendientes sugeridos:

- Integrar drag and drop para cargar archivos desde la interfaz.
- Agregar mas pruebas de integracion con archivos reales de ejemplo.
- Incorporar icono de aplicacion para el empaquetado.
- Agregar pipeline de CI para ejecutar pruebas automaticamente.
