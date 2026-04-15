# Conversor de Formatos Tabulares

Aplicación de escritorio desarrollada con Python y Tkinter para convertir archivos tabulares entre formatos comunes de manera simple, portable y fácil de compartir. La app permite cargar un archivo, revisar una vista previa, elegir un formato de salida, preparar la conversión y guardar el resultado como un archivo nuevo.

Versión actual: 3.0.0

Fecha de última actualización: 2026-04-14

Autor: Fernando Corrales Quirós

Manual de usuario: [MANUAL_USUARIO.md](/C:/Users/Fernando/Documents/Conversor_formatos/MANUAL_USUARIO.md)

## Qué hace la aplicación

- Convierte archivos tabulares entre formatos comunes.
- Muestra una vista previa de los datos antes de guardar.
- Permite cargar archivos tanto con selección manual como con drag and drop.
- Mantiene una arquitectura modular, ligera y preparada para seguir creciendo.
- Conserva preferencias simples entre sesiones sin dejar de ser portable.

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
- Tkinter disponible en el sistema
- Dependencias instaladas desde `requirements.txt`

Tkinter normalmente viene incluido con Python. Si tu instalación no lo incluye, instala el paquete correspondiente para tu sistema operativo.

## Instalación de dependencias

Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar dependencias:

```powershell
pip install -r requirements.txt
```

## Ejecutar la aplicación

Desde la raíz del proyecto:

```powershell
python app.py
```

Para una guía orientada a usuarios no técnicos, consulta [MANUAL_USUARIO.md](/C:/Users/Fernando/Documents/Conversor_formatos/MANUAL_USUARIO.md).

## Uso básico

1. Inicia la app con `python app.py`.
2. Selecciona un archivo o arrástralo a la ventana principal.
3. Revisa la información visible del archivo y su vista previa.
4. Elige el formato de salida.
5. Presiona `Convertir`.
6. Presiona `Guardar convertido`.
7. Usa `Limpiar` para reiniciar la interfaz sin cerrar la app.

La aplicación muestra mensajes claros si el archivo está vacío, si el formato no es compatible o si ocurre un error de lectura o escritura.

## Distribución portable

La aplicación está preparada para compartirse como un paquete portable. Esto significa que puede distribuirse como una carpeta o archivo ZIP con todo lo necesario para ejecutarse, sin instalador y sin modificar el sistema del usuario.

Características del enfoque portable:

- No requiere instalador.
- Puede ejecutarse desde una carpeta local, USB o unidad externa.
- Mantiene su configuración simple en archivos livianos dentro del entorno de la app.
- Facilita compartir una misma versión con otros usuarios de forma directa.

## Cómo generar el ejecutable

Opción directa con PyInstaller:

```powershell
pyinstaller ConversorFormatos.spec
```

O usando el script incluido:

```powershell
.\scripts\build.ps1
```

La salida principal del ejecutable queda en:

```text
dist/ConversorFormatos/
```

## Cómo preparar un paquete portable

El proyecto incluye un script auxiliar para reunir el contenido de distribución y generar un ZIP portable:

```powershell
.\scripts\package_portable.ps1
```

Ese script:

- verifica que exista la salida en `dist/ConversorFormatos/`
- crea una carpeta de distribución en `portable/`
- copia el ejecutable y los archivos de documentación esenciales
- genera un ZIP listo para compartir

La salida esperada queda en una estructura como esta:

```text
portable/
|-- ConversorFormatos-3.0.0-portable/
|   |-- ConversorFormatos.exe
|   |-- LICENSE
|   |-- README.md
|   |-- MANUAL_USUARIO.md
|   `-- CHANGELOG.md
`-- ConversorFormatos-3.0.0-portable.zip
```

## Qué debe incluir un paquete portable

Para compartir la aplicación con otros usuarios, el paquete portable debe incluir al menos:

- el contenido generado por PyInstaller en `dist/ConversorFormatos/`
- [README.md](/C:/Users/Fernando/Documents/Conversor_formatos/README.md)
- [MANUAL_USUARIO.md](/C:/Users/Fernando/Documents/Conversor_formatos/MANUAL_USUARIO.md)
- [LICENSE](/C:/Users/Fernando/Documents/Conversor_formatos/LICENSE)
- [CHANGELOG.md](/C:/Users/Fernando/Documents/Conversor_formatos/CHANGELOG.md)

## Cómo compartir la app con otros usuarios

1. Genera el ejecutable con PyInstaller.
2. Prepara el paquete portable con `.\scripts\package_portable.ps1`.
3. Comparte la carpeta portable o el ZIP generado.
4. Indica al usuario que solo necesita descomprimir el paquete y ejecutar `ConversorFormatos.exe`.

No se crea instalador en esta fase porque la distribución sigue siendo completamente portable.

## Pruebas y validación

Ejecutar la suite de pruebas:

```powershell
pytest
```

Validar sintaxis rápidamente:

```powershell
python -m compileall app.py src tests
```

## Estructura del proyecto

```text
.
|-- app.py
|-- CHANGELOG.md
|-- ConversorFormatos.spec
|-- LICENSE
|-- MANUAL_USUARIO.md
|-- README.md
|-- hook-tkinterdnd2.py
|-- requirements.txt
|-- scripts/
|   |-- build.ps1
|   `-- package_portable.ps1
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
|       |-- helpers.py
|       `-- preferences.py
|-- tests/
|   |-- test_converter.py
|   |-- test_drag_drop.py
|   |-- test_file_service.py
|   |-- test_file_types.py
|   |-- test_preferences.py
|   `-- test_validators.py
|-- dist/
|   `-- ConversorFormatos/
`-- portable/
```

Referencias importantes:

- `dist/ConversorFormatos/`: salida generada por PyInstaller.
- `portable/`: carpeta sugerida para armar paquetes listos para compartir.
- `src/gui`: ventanas y componentes visuales.
- `src/core`: lectura, escritura, conversión y validaciones.
- `src/services`: coordinación entre interfaz y lógica.
- `src/utils`: constantes, errores, preferencias y utilidades.

## Estado del proyecto

La versión 3.0.0 deja la base lista para distribución pública portable, con documentación clara, licencia permisiva, registro de cambios y una rutina simple para preparar paquetes de entrega.

Elementos reservados para versiones futuras:

- publicación automatizada en GitHub Releases
- canal de donaciones o apoyo al proyecto
- mayor automatización del proceso de publicación

