# Conversor de Formatos Tabulares

Aplicación de escritorio desarrollada con Python y Tkinter para convertir archivos tabulares entre formatos comunes de manera simple, portable y fácil de compartir. La app permite cargar un archivo, revisar una vista previa, elegir un formato de salida, preparar la conversión y guardar el resultado como un archivo nuevo.

Versión actual: 4.1.0

Fecha de última actualización: 2026-04-14

Autor: Fernando Corrales Quirós

Manual de usuario: [MANUAL_USUARIO.md](/C:/Users/Fernando/Documents/Conversor_formatos/MANUAL_USUARIO.md)

## Qué hace la aplicación

- Convierte archivos tabulares entre formatos comunes y extensibles.
- Muestra una vista previa más clara de los datos antes de guardar.
- Permite cargar archivos tanto con selección manual como con drag and drop.
- Mantiene una arquitectura modular, ligera y preparada para seguir creciendo.
- Conserva preferencias simples entre sesiones sin dejar de ser portable.

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

Notas importantes de compatibilidad:

- XML se soporta cuando puede representarse razonablemente como tabla.
- Si el archivo XML no tiene una estructura tabular compatible, la app mostrará un mensaje claro sin cerrarse.
- JSON funciona mejor con listas de registros o estructuras tabulares compatibles.
- ODS usa la dependencia ligera `odfpy`, declarada en [requirements.txt](/C:/Users/Fernando/Documents/Conversor_formatos/requirements.txt).
- Si falta una dependencia necesaria para XLSX u ODS, la app lo indicará con un mensaje claro.
- Parquet no forma parte de esta fase y no está implementado en la app.

## Vista previa avanzada ligera

La versión 4.1.0 mejora la inspección rápida del archivo cargado sin convertir la vista previa en un editor:

- muestra cuántas columnas fueron detectadas
- indica cuántas filas se están previsualizando
- avisa cuando la vista previa es parcial
- presenta mejor los encabezados y aprovecha mejor el espacio disponible

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

## Pruebas y validación

Ejecutar la suite de pruebas:

```powershell
pytest
```

Validar sintaxis rápidamente:

```powershell
python -m compileall app.py src tests
```

## Estado del proyecto

La versión 4.1.0 mejora la experiencia de vista previa con una inspección más clara y útil, manteniendo la app ligera, portable y coherente con su enfoque de conversión rápida.
