# Resumen del proyecto

## Descripción

Conversor de Formatos Tabulares es una aplicación de escritorio para Windows
que permite transformar archivos de datos entre formatos tabulares comunes.
La interfaz guía al usuario desde la selección del archivo hasta la revisión
de una muestra y el guardado del resultado.

## Objetivo

Facilitar conversiones tabulares frecuentes sin exigir conocimientos de
programación ni depender de una hoja de cálculo. La aplicación prioriza un
flujo directo, mensajes comprensibles y una distribución que pueda utilizarse
como paquete portable o mediante un instalador tradicional.

## Características principales

- Selección manual de archivos y carga mediante drag and drop.
- Conversión basada en DataFrames de pandas.
- Vista previa no editable con columnas, filas visibles y resumen de la muestra.
- Información básica del archivo cargado.
- Interfaz disponible en español e inglés.
- Temas claro y oscuro.
- Preferencias locales para idioma, tema, formato de salida y geometría.
- Validación de archivos vacíos, extensiones no soportadas y errores de E/S.
- Distribución portable e instalable para Windows.

## Formatos soportados

La versión actual permite lectura y escritura de:

| Formato | Extensión |
| --- | --- |
| CSV | `.csv` |
| Excel | `.xlsx` |
| JSON | `.json` |
| Texto delimitado | `.txt` |
| TSV | `.tsv` |
| XML tabular | `.xml` |
| OpenDocument Spreadsheet | `.ods` |

## Alcance

La aplicación está orientada a convertir conjuntos de datos que puedan
representarse como una tabla bidimensional. El archivo se carga en memoria,
se valida, se transforma a un DataFrame y se exporta al formato elegido.

La vista previa sirve para inspección rápida. No ofrece edición de celdas,
fórmulas, análisis estadístico ni operaciones propias de una hoja de cálculo.
Tampoco incluye bases de datos o conversión SQL.

## Estado actual

La versión `1.0.0` es la primera versión pública estable. Incluye:

- los siete formatos documentados;
- flujo completo de lectura, vista previa, conversión y guardado;
- interfaz ES/EN y temas claro/oscuro;
- persistencia local tolerante a errores;
- suite automatizada para el dominio no visual;
- build optimizado con PyInstaller;
- paquete portable e instalador creado con Inno Setup.

## Limitaciones conocidas

- JSON debe tener una estructura que pandas pueda interpretar como tabla.
- XML funciona mejor con registros repetidos y campos consistentes.
- XLSX y ODS se procesan como una tabla simple; no se preservan fórmulas,
  estilos, gráficos ni múltiples hojas.
- TXT se interpreta como texto delimitado y la detección del separador puede
  no cubrir estructuras ambiguas.
- La vista previa muestra una cantidad limitada de filas para mantener la
  aplicación ligera.
- Los archivos se cargan en memoria, por lo que conjuntos muy grandes dependen
  de los recursos disponibles en el equipo.
- La persistencia de preferencias requiere permiso de escritura en la carpeta
  donde se ejecuta la aplicación.

## Mejoras futuras realistas

- Ampliar pruebas automatizadas del ejecutable empaquetado.
- Mejorar accesibilidad mediante revisión de navegación y contraste.
- Reutilizar más componentes internos de las ventanas secundarias.
- Reforzar mensajes para estructuras JSON y XML especialmente complejas.

[Volver al README](../README.md)
