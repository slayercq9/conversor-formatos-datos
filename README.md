# Conversor de Formatos Tabulares

Aplicación de escritorio desarrollada con Python y Tkinter para convertir archivos tabulares entre formatos comunes. El proyecto prioriza una experiencia ligera, portable y mantenible, con vista previa rápida, soporte multidioma básico y dos vías de distribución para Windows.

Versión actual: `5.1.1`

Fecha de última actualización: `2026-04-15`

Autor: `Fernando Corrales Quirós`

Manual de usuario: [MANUAL_USUARIO.md](/C:/Users/Fernando/Documents/Conversor_formatos/MANUAL_USUARIO.md)

## Qué hace la aplicación

- Carga archivos mediante selección manual o drag and drop.
- Muestra una vista previa ligera para inspección rápida.
- Convierte entre formatos tabulares soportados.
- Guarda el resultado como un archivo nuevo.
- Permite cambiar el idioma visible entre español e inglés.
- Permite alternar entre tema claro y tema oscuro.
- Conserva preferencias simples entre sesiones.
- Puede distribuirse como versión portable o como instalador de Windows.

## Formatos soportados

Formatos de entrada y salida:

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
- `ODS` requiere la dependencia ligera `odfpy`.

## Requisitos

- Python 3.11 o superior
- Tkinter disponible en el sistema
- Dependencias instaladas desde [requirements.txt](/C:/Users/Fernando/Documents/Conversor_formatos/requirements.txt)

Instalación recomendada:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecución en desarrollo

```powershell
python app.py
```

El punto de entrada principal es [app.py](/C:/Users/Fernando/Documents/Conversor_formatos/app.py).

## Scripts disponibles

Los scripts principales están en [scripts](/C:/Users/Fernando/Documents/Conversor_formatos/scripts):

- [build.ps1](/C:/Users/Fernando/Documents/Conversor_formatos/scripts/build.ps1): genera la app empaquetada con `python -m PyInstaller`.
- [package_portable.ps1](/C:/Users/Fernando/Documents/Conversor_formatos/scripts/package_portable.ps1): arma la carpeta portable y genera un ZIP compartible.
- [build_installer.ps1](/C:/Users/Fernando/Documents/Conversor_formatos/scripts/build_installer.ps1): compila el instalador de Windows con Inno Setup.

## Distribución portable

1. Genera la salida empaquetada:

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

Un paquete portable debe incluir al menos:

- el contenido de `dist/ConversorFormatos/`
- `README.md`
- `MANUAL_USUARIO.md`
- `LICENSE`
- `CHANGELOG.md`

## Instalador de Windows

Herramienta elegida:

- `Inno Setup 6`

Archivo base:

- [installer/ConversorFormatos.iss](/C:/Users/Fernando/Documents/Conversor_formatos/installer/ConversorFormatos.iss)

Pasos:

```powershell
.\scripts\build.ps1
.\scripts\build_installer.ps1 -Version 5.1.0
```

Salida esperada:

```text
installer-output/
`-- ConversorFormatos-5.1.0-setup.exe
```

## Cómo compartir la aplicación

### Versión portable

- Comparte el ZIP generado en `portable/`.
- El usuario solo debe descomprimir la carpeta y ejecutar `ConversorFormatos.exe`.

### Versión instalable

- Comparte el ejecutable generado en `installer-output/`.
- El usuario instala la app con el asistente tradicional de Windows.

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

## Estado técnico actual

La versión `5.1.1` deja la base lista para seguir creciendo con una arquitectura modular, soporte multiformato, interfaz bilingüe, tema claro/oscuro, vista previa ligera y preparación seria para distribución en Windows.

Recomendaciones técnicas futuras no implementadas en esta fase:

- centralizar aún más los mensajes del dominio para reducir texto literal repetido
- introducir una pequeña capa de utilidades compartidas para ventanas secundarias
- ampliar la cobertura automatizada de GUI sin comprometer ligereza ni portabilidad
