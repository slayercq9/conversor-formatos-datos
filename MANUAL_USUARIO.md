# Manual de Usuario

Documento vivo del proyecto. Este manual está pensado para actualizarse en cada nueva versión de la aplicación y servir como referencia clara para usuarios no técnicos.

## Introducción

Conversor de Formatos Tabulares es una aplicación de escritorio que permite transformar archivos tabulares entre distintos formatos comunes. Su interfaz está pensada para que el proceso de conversión sea claro, guiado y seguro.

## Objetivo de la aplicación

El objetivo principal de la aplicación es facilitar la conversión de archivos tabulares sin requerir conocimientos técnicos avanzados. La herramienta permite abrir un archivo, revisar una vista previa, elegir un formato de salida y guardar el resultado convertido.

## Versión actual

4.0.0

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

Notas importantes:

- XML se soporta cuando sus registros pueden representarse como tabla.
- Si el archivo XML no tiene una estructura tabular compatible, la aplicación lo informará claramente.
- ODS requiere la dependencia `odfpy`, incluida en `requirements.txt`.
- Parquet no forma parte de esta fase.

## Mensajes o errores comunes y su significado

`Todavía no has cargado un archivo.`
Significa que debes seleccionar un archivo antes de usar la vista previa o iniciar la conversión.

`Debes elegir un formato de salida antes de convertir.`
Significa que la lista de formato de salida aún no tiene una opción elegida.

`El archivo seleccionado está vacío.`
Indica que el archivo no contiene datos útiles para procesar.

`El formato del archivo cargado no es soportado.`
Indica que la extensión del archivo no pertenece a los formatos actualmente compatibles.

`No se pudo interpretar el archivo XML como una tabla.`
Indica que el XML no tiene una estructura tabular compatible para esta versión de la app.

`No se pudo leer el archivo ...`
Suele significar que el archivo está dañado, en uso por otro programa o no tiene un contenido válido para su formato.

`No se pudo guardar el archivo ...`
Suele indicar problemas de permisos, rutas inválidas o que el archivo de destino está abierto en otro programa.

`Interfaz reiniciada.`
Indica que se limpió el estado visual de la app sin cerrar la ventana. También se reinicia la selección visible del formato de salida para comenzar una tarea nueva con claridad.

`La aplicación recuerda preferencias de la sesión anterior.`
Indica que el último formato elegido y, cuando sea posible, la geometría de la ventana principal pueden restaurarse automáticamente al volver a abrir la app, aunque durante la sesión actual uses `Limpiar`.

## Preguntas frecuentes

### ¿La aplicación modifica mi archivo original?

No. La aplicación prepara un archivo nuevo y lo guarda en la ubicación que el usuario elige.

### ¿Puedo guardar con otro nombre?

Sí. Al usar `Guardar convertido`, puedes cambiar el nombre y la carpeta de destino.

### ¿Qué pasa si cierro la ventana antes de guardar?

La conversión preparada en memoria se perderá y deberás repetir el proceso.

### ¿Puedo convertir al mismo formato?

No. La aplicación evita conversiones redundantes al mismo formato de origen.

### ¿Qué significa que la app sea portable?

Significa que puede compartirse como una carpeta o un archivo ZIP listo para usar, sin instalador. El usuario solo necesita descomprimir el paquete y ejecutar el archivo principal de la aplicación.

### ¿Qué necesito para usar archivos ODS?

Solo necesitas tener instaladas las dependencias del proyecto. El soporte ODS usa `odfpy`, que ya está declarado en `requirements.txt`.

## Recomendaciones de uso

- Revisa la vista previa antes de guardar el archivo convertido.
- Usa nombres de archivo claros para distinguir originales y convertidos.
- Evita abrir el archivo de destino en otro programa mientras intentas guardarlo.
- Si trabajas con archivos importantes, conserva una copia del original.
- Si compartes la app con otros usuarios, incluye también el manual, la licencia y el changelog junto al ejecutable portable.

## Mejoras futuras previstas

- Más pruebas con archivos reales de ejemplo.
- Publicación del paquete en GitHub Releases.
- Evaluación de un posible canal de donaciones o apoyo al proyecto.
- Posible ampliación de formatos soportados en futuras versiones.

## Historial de versiones del manual

### Versión 4.0.0

- Se agregan los formatos TSV, XML y ODS como opciones de lectura y escritura.
- Se documentan las limitaciones de XML cuando no puede representarse como tabla.
- Se documenta la dependencia `odfpy` para soporte ODS.
- Se alinean la versión y la fecha visibles con la nueva fase funcional.

### Versión 3.0.0

- Se documenta la preparación del proyecto para distribución pública portable.
- Se agrega una explicación breve sobre qué significa que la app sea portable.
- Se alinean la versión y la fecha visibles con la documentación de distribución.
- Se deja constancia de que GitHub Releases y donaciones quedan para fases futuras.

### Versión 2.2.0

- Se agrega persistencia simple de preferencias en un archivo JSON portable.
- La aplicación recuerda el último formato de salida entre sesiones.
- La aplicación puede restaurar el tamaño y la posición de la ventana principal cuando la información es válida.

### Versión 2.1.0

- Se realiza un pulido visual menor para mejorar espaciados, alineación y consistencia de la interfaz.
- Se ajustan ventanas informativas y vista previa para una presentación más uniforme.
- Se actualizan la versión y la fecha visibles del proyecto.

### Versión 2.0.0

- Se actualiza la experiencia de usuario con el botón `Limpiar`.
- Se mantiene el último formato de salida durante la sesión actual.
- Se agrega información resumida del archivo cargado en la interfaz.
- Se actualizan la versión y la fecha visibles del proyecto.

### Versión 1.2.0

- Se crea el manual de usuario inicial.
- Se documenta el flujo completo de uso de la aplicación.
- Se alinean la versión y la fecha visibles con la documentación del proyecto.
- Se confirma la integración del icono definitivo `assets/icon.ico`.
- Se agrega soporte de drag and drop para cargar archivos compatibles.
