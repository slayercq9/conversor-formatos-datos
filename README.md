# Conversor de Formatos Tabulares

Aplicación de escritorio desarrollada con Python y Tkinter para convertir archivos tabulares entre formatos comunes. El proyecto está orientado a una experiencia ligera, portable y fácil de mantener, con interfaz bilingüe, vista previa rápida y dos vías de distribución para Windows.

Versión actual: 5.1.0

Fecha de última actualización: 2026-04-15

Autor: Fernando Corrales Quirós

Manual de usuario: [MANUAL_USUARIO.md](/C:/Users/Fernando/Documents/Conversor_formatos/MANUAL_USUARIO.md)

## Qué hace la app actualmente

- Convierte archivos tabulares entre formatos comunes.
- Permite cargar archivos con selección manual o drag and drop.
- Muestra una vista previa ligera antes de convertir.
- Permite elegir idioma visible de la interfaz en español o inglés.
- Conserva preferencias simples entre sesiones.
- Puede distribuirse como versión portable o como instalador de Windows.

## Formatos soportados

Formatos de entrada y salida actualmente soportados:

- CSV (`.csv`)
- TSV (`.tsv`)
- XLSX (`.xlsx`)
- ODS (`.ods`)
- JSON (`.json`)
- XML (`.xml`)
- TXT (`.txt`)

Notas de compatibilidad:

- `XML` se soporta cuando puede representarse razonablemente como tabla.
- `JSON` funciona mejor con listas de registros o estructuras tabulares compatibles.
- `ODS` usa la dependencia ligera `odfpy`.

## Interfaz y experiencia actual

- Interfaz bilingüe: español e inglés.
- Selector visible de idioma en la ventana principal.
- Preferencia de idioma persistente entre sesiones.
- Vista previa mejorada con resumen de columnas, filas visibles y aviso de parcialidad.
- Ventanas informativas de `Cómo usar` y `Acerca de`.

## Requisitos

- Python 3.11 o superior
- Tkinter disponible en el sistema
- Dependencias instaladas desde [requirements.txt](/C:/Users/Fernando/Documents/Conversor_formatos/requirements.txt)

Instalación de dependencias:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Cómo ejecutar la app

Desde la raíz del proyecto:

```powershell
python app.py
```

## Scripts disponibles

En [scripts](/C:/Users/Fernando/Documents/Conversor_formatos/scripts) hay tres scripts principales:

- [build.ps1](/C:/Users/Fernando/Documents/Conversor_formatos/scripts/build.ps1): genera la aplicación empaquetada con `python -m PyInstaller`.
- [package_portable.ps1](/C:/Users/Fernando/Documents/Conversor_formatos/scripts/package_portable.ps1): prepara la distribución portable y genera un ZIP.
- [build_installer.ps1](/C:/Users/Fernando/Documents/Conversor_formatos/scripts/build_installer.ps1): compila el instalador de Windows a partir de la salida de PyInstaller.

## Build portable

1. Genera la aplicación empaquetada:

```powershell
.\scripts\build.ps1
```

2. Prepara el paquete portable:

```powershell
.\scripts\package_portable.ps1 -Version 5.1.0
```

Salida esperada:

```text
portable/
|-- ConversorFormatos-5.1.0-portable/
`-- ConversorFormatos-5.1.0-portable.zip
```

## Build instalador de Windows

Herramienta elegida:

- `Inno Setup 6`

Base de configuración:

- [installer/ConversorFormatos.iss](/C:/Users/Fernando/Documents/Conversor_formatos/installer/ConversorFormatos.iss)

Pasos:

1. Genera la aplicación empaquetada:

```powershell
.\scripts\build.ps1
```

2. Compila el instalador:

```powershell
.\scripts\build_installer.ps1 -Version 5.1.0
```

Salida esperada:

```text
installer-output/
`-- ConversorFormatos-5.1.0-setup.exe
```

## Distribución

### Versión portable

- No requiere instalación.
- Puede ejecutarse desde carpeta local, USB o ZIP descomprimido.
- Es útil para distribución directa o uso portátil.

### Versión instalable

- Ofrece una instalación tradicional en Windows.
- Puede crear accesos directos y desinstalación estándar.
- Usa Inno Setup sobre la salida de PyInstaller.

Ambas vías siguen siendo oficiales y compatibles con el estado actual del proyecto.

## Estructura general del proyecto

```text
.
|-- app.py
|-- CHANGELOG.md
|-- ConversorFormatos.spec
|-- LICENSE
|-- MANUAL_USUARIO.md
|-- README.md
|-- installer/
|   `-- ConversorFormatos.iss
|-- scripts/
|   |-- build.ps1
|   |-- build_installer.ps1
|   `-- package_portable.ps1
|-- src/
|   |-- core/
|   |-- gui/
|   |-- i18n/
|   |-- services/
|   `-- utils/
`-- tests/
```

## Estado del proyecto

La versión 5.1.0 deja la documentación alineada con el estado real de la aplicación: formatos soportados, interfaz bilingüe, vista previa mejorada, persistencia ligera y dos modalidades de distribución para Windows.
