# Conversor de Formatos Tabulares

Aplicacion de escritorio en Python con Tkinter para convertir archivos `CSV`, `XLSX`, `JSON` y `TXT` entre formatos tabulares.

## Objetivo

La base del proyecto esta pensada para crecer de forma modular:

- `src/gui`: interfaz grafica y ventanas auxiliares.
- `src/core`: lectura, escritura, conversion y validaciones del dominio.
- `src/services`: coordinacion entre GUI y logica de negocio.
- `src/utils`: constantes, helpers y errores compartidos.
- `src/future`: puntos de extension planificados, como drag and drop.
- `tests`: pruebas unitarias y de humo.

## Estructura

```text
.
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- src/
|   |-- gui/
|   |-- core/
|   |-- services/
|   |-- utils/
|   `-- future/
`-- tests/
```

## Requisitos

- Python 3.11 o superior

## Instalacion

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecucion

```bash
python app.py
```

## Pruebas

```bash
pytest
```

## Notas de arquitectura

- La conversion tabular se centraliza en `TabularConverter`.
- `FileService` y `PreviewService` desacoplan la interfaz de la logica.
- `drag_drop.py` deja lista una interfaz de integracion futura sin implementacion real.
- No se incluye SQL ni dependencias relacionadas.
