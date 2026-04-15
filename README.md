# Conversor de Formatos Tabulares

Aplicación de escritorio desarrollada con Python y Tkinter para convertir archivos tabulares entre formatos comunes de manera simple, portable y fácil de compartir. La app permite cargar un archivo, revisar una vista previa, elegir un formato de salida, preparar la conversión y guardar el resultado como un archivo nuevo.

Versión actual: 4.2.0

Fecha de última actualización: 2026-04-15

Autor: Fernando Corrales Quirós

Manual de usuario: [MANUAL_USUARIO.md](/C:/Users/Fernando/Documents/Conversor_formatos/MANUAL_USUARIO.md)

## Qué hace la aplicación

- Convierte archivos tabulares entre formatos comunes y extensibles.
- Muestra una vista previa clara de los datos antes de guardar.
- Permite cargar archivos tanto con selección manual como con drag and drop.
- Mantiene una arquitectura modular, ligera y preparada para seguir creciendo.
- Puede distribuirse como versión portable o como versión instalable para Windows.

## Formatos soportados

Formatos de entrada:

- CSV (`.csv`)
- TSV (`.tsv`)
- Excel (`.xlsx`)
- OpenDocument Spreadsheet (`.ods`)
- JSON (`.json`)
- XML (`.xml`)
- Texto delimitado (`.txt`)

Formatos de salida:

- CSV (`.csv`)
- TSV (`.tsv`)
- Excel (`.xlsx`)
- OpenDocument Spreadsheet (`.ods`)
- JSON (`.json`)
- XML (`.xml`)
- Texto delimitado (`.txt`)

## Modalidades de distribución

### Versión portable

- Se entrega como carpeta o ZIP listo para usar.
- No requiere instalación.
- Puede ejecutarse desde una carpeta local, USB o unidad externa.
- Es ideal para pruebas, uso personal portátil o distribución directa.

### Versión instalable

- Se entrega como instalador tradicional para Windows.
- Copia la aplicación a `Archivos de programa`, crea accesos directos y permite desinstalación estándar.
- Es recomendable para usuarios que prefieren una experiencia más convencional de instalación.

Ambas opciones seguirán siendo oficiales. La vía portable no se elimina ni se reemplaza.

## Herramientas de empaquetado

El proyecto usa dos herramientas comunes y mantenibles:

- `PyInstaller` para generar la aplicación empaquetada en `dist/ConversorFormatos/`.
- `Inno Setup 6` para generar un instalador de Windows a partir de esa salida.

La base del instalador está en [installer/ConversorFormatos.iss](/C:/Users/Fernando/Documents/Conversor_formatos/installer/ConversorFormatos.iss).

## Requisitos

- Python 3.11 o superior
- Tkinter disponible en el sistema
- Dependencias instaladas desde `requirements.txt`

## Instalación de dependencias

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecutar la aplicación

```powershell
python app.py
```

## Cómo generar la aplicación empaquetada

```powershell
.\scripts\build.ps1
```

La salida base queda en:

```text
dist/ConversorFormatos/
```

## Cómo generar el paquete portable

```powershell
.\scripts\package_portable.ps1 -Version 4.2.0
```

Salida esperada:

```text
portable/
|-- ConversorFormatos-4.2.0-portable/
`-- ConversorFormatos-4.2.0-portable.zip
```

## Cómo generar el instalador de Windows

Primero construye la aplicación con PyInstaller:

```powershell
.\scripts\build.ps1
```

Después compila el instalador:

```powershell
.\scripts\build_installer.ps1 -Version 4.2.0
```

Requisito adicional para el instalador:

- Tener `Inno Setup 6` instalado en Windows.

Salida esperada:

```text
installer-output/
`-- ConversorFormatos-4.2.0-setup.exe
```

## Qué incluye cada distribución

### Portable

- Aplicación empaquetada por PyInstaller
- `README.md`
- `MANUAL_USUARIO.md`
- `LICENSE`
- `CHANGELOG.md`

### Instalable

- Aplicación empaquetada por PyInstaller
- Accesos directos de Windows
- Registro de desinstalación
- Documentación básica copiada junto a la app instalada

## Estructura relevante del proyecto

```text
.
|-- ConversorFormatos.spec
|-- installer/
|   `-- ConversorFormatos.iss
|-- installer-output/
|-- portable/
|-- scripts/
|   |-- build.ps1
|   |-- build_installer.ps1
|   `-- package_portable.ps1
`-- dist/
    `-- ConversorFormatos/
```

## Estado del proyecto

La versión 4.2.0 deja preparada una vía instalable seria para Windows sin perder la distribución portable ya existente. GitHub Releases y donaciones quedan fuera de esta fase.
