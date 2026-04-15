# Manual de Usuario

Documento vivo del proyecto. Este manual está pensado para actualizarse en cada nueva versión de la aplicación y servir como referencia clara para usuarios no técnicos.

## Introducción

Conversor de Formatos Tabulares es una aplicación de escritorio que permite transformar archivos tabulares entre distintos formatos comunes. Su interfaz está pensada para que el proceso de conversión sea claro, guiado y seguro.

## Objetivo de la aplicación

El objetivo principal de la aplicación es facilitar la conversión de archivos tabulares sin requerir conocimientos técnicos avanzados. La herramienta permite abrir un archivo, revisar una vista previa, elegir un formato de salida y guardar el resultado convertido.

## Versión actual

4.1.0

## Fecha de última actualización

2026-04-14

## Requisitos de uso

- Tener Python 3.11 o superior instalado.
- Tener las dependencias del proyecto instaladas desde `requirements.txt`.
- Contar con un archivo de entrada en uno de los formatos soportados.

## Cómo iniciar la aplicación

1. Abrir una terminal en la carpeta raíz del proyecto.
2. Activar el entorno virtual si el proyecto utiliza uno.
3. Ejecutar el siguiente comando:

```powershell
python app.py
```

Al iniciar, se abrirá la ventana principal de la aplicación.

## Cómo seleccionar un archivo

1. Presiona el botón `Seleccionar archivo`.
2. Busca el archivo que deseas convertir.
3. Selecciónalo y confirma la apertura.
4. La aplicación mostrará la ruta o el nombre del archivo cargado.
5. Cuando sea posible, también mostrará información útil como extensión, tamaño aproximado y cantidad de filas.

Si no seleccionas ningún archivo, la aplicación seguirá abierta y mostrará un mensaje de orientación.

También puedes arrastrar y soltar un archivo compatible directamente sobre la zona de carga de la ventana principal. Si el archivo es válido, la aplicación lo cargará automáticamente y actualizará la vista previa.

## Cómo usar la vista previa

La vista previa está pensada para inspección rápida. Ahora muestra mejor la estructura tabular del archivo cargado:

- columnas detectadas
- cantidad de filas visibles en pantalla
- aviso cuando la vista previa es parcial
- mejor distribución de encabezados y espacio disponible

La vista previa no es editable y no reemplaza el archivo original.

## Cómo elegir el formato de salida

1. Ubica el campo `Formato de salida`.
2. Haz clic en la lista desplegable.
3. Selecciona el formato al que deseas convertir el archivo.

Debes elegir un formato antes de convertir. Si no lo haces, la aplicación mostrará un mensaje informativo.

## Cómo convertir y guardar

1. Una vez cargado el archivo y elegido el formato de salida, presiona `Convertir`.
2. La aplicación preparará la conversión internamente.
3. Cuando la conversión esté lista, presiona `Guardar convertido`.
4. Elige la carpeta de destino y el nombre del archivo.
5. Confirma el guardado.
6. Si deseas comenzar una nueva tarea sin cerrar la aplicación, usa el botón `Limpiar`.
7. Al limpiar, la app reinicia el archivo cargado, la vista previa, la conversión preparada, los mensajes transitorios y la selección visible del formato de salida.

Si ocurre un problema durante la lectura o escritura, la aplicación mostrará un diálogo explicando el motivo.

## Formatos soportados actualmente

Formatos de entrada:

- CSV (`.csv`)
- TSV (`.tsv`)
- XLSX (`.xlsx`)
- ODS (`.ods`)
- JSON (`.json`)
- XML (`.xml`)
- TXT (`.txt`)

Formatos de salida:

- CSV (`.csv`)
- TSV (`.tsv`)
- XLSX (`.xlsx`)
- ODS (`.ods`)
- JSON (`.json`)
- XML (`.xml`)
- TXT (`.txt`)

## Mensajes o errores comunes y su significado

`No se pudo construir la vista previa.`
Indica que el archivo no pudo representarse correctamente para inspección rápida, aunque la aplicación sigue disponible.

`La vista previa es parcial.`
Indica que solo se muestran las primeras filas para mantener la app ligera y rápida.

`Todavía no has cargado un archivo.`
Significa que debes seleccionar un archivo antes de usar la vista previa o iniciar la conversión.

`Debes elegir un formato de salida antes de convertir.`
Significa que la lista de formato de salida aún no tiene una opción elegida.

`El archivo seleccionado está vacío.`
Indica que el archivo no contiene datos útiles para procesar.

## Preguntas frecuentes

### ¿La vista previa modifica mis datos?

No. La vista previa solo muestra una parte del contenido para revisión rápida.

### ¿Por qué no siempre veo todas las filas?

Porque la app limita la cantidad de filas mostradas para seguir siendo ligera y responder rápido.

### ¿Qué significa que la app sea portable?

Significa que puede compartirse como una carpeta o un archivo ZIP listo para usar, sin instalador. El usuario solo necesita descomprimir el paquete y ejecutar el archivo principal de la aplicación.

## Historial de versiones del manual

### Versión 4.1.0

- Se mejora la vista previa con un resumen más útil de columnas y filas.
- Se agrega aviso claro cuando la vista previa es parcial.
- Se refuerza la inspección rápida sin convertir la tabla en editor.

### Versión 4.0.0

- Se consolida la compatibilidad práctica de TSV, XML y ODS.
- Se documentan las limitaciones de XML y JSON cuando no pueden representarse como tabla.
- Se documenta la dependencia `odfpy` para soporte ODS y sus mensajes de error esperables.
- Se alinean la versión y la fecha visibles con la fase de robustez.
