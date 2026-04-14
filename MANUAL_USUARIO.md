# Manual de Usuario

Documento vivo del proyecto. Este manual está pensado para actualizarse en cada nueva versión de la aplicación y servir como referencia clara para usuarios no técnicos.

## Introducción

Conversor de Formatos Tabulares es una aplicación de escritorio que permite transformar archivos tabulares entre distintos formatos comunes. Su interfaz está pensada para que el proceso de conversión sea claro, guiado y seguro.

## Objetivo de la aplicación

El objetivo principal de la aplicación es facilitar la conversión de archivos tabulares sin requerir conocimientos técnicos avanzados. La herramienta permite abrir un archivo, revisar una vista previa, elegir un formato de salida y guardar el resultado convertido.

## Versión actual

2.0.0

## Fecha de última actualización

2026-04-13

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

Si ocurre un problema durante la lectura o escritura, la aplicación mostrará un diálogo explicando el motivo.

## Formatos soportados actualmente

Formatos de entrada:

- CSV (`.csv`)
- XLSX (`.xlsx`)
- JSON (`.json`)
- TXT (`.txt`)

Formatos de salida:

- CSV (`.csv`)
- XLSX (`.xlsx`)
- JSON (`.json`)
- TXT (`.txt`)

## Mensajes o errores comunes y su significado

`Todavía no has cargado un archivo.`
Significa que debes seleccionar un archivo antes de usar la vista previa o iniciar la conversión.

`Debes elegir un formato de salida antes de convertir.`
Significa que la lista de formato de salida aún no tiene una opción elegida.

`El archivo seleccionado está vacío.`
Indica que el archivo no contiene datos útiles para procesar.

`El formato del archivo cargado no es soportado.`
Indica que la extensión del archivo no pertenece a los formatos actualmente compatibles.

`No se pudo leer el archivo ...`
Suele significar que el archivo está dañado, en uso por otro programa o no tiene un contenido válido para su formato.

`No se pudo guardar el archivo ...`
Suele indicar problemas de permisos, rutas inválidas o que el archivo de destino está abierto en otro programa.

`Interfaz reiniciada.`
Indica que se limpió el estado visual de la app sin cerrar la ventana. El formato de salida puede mantenerse durante la sesión para agilizar nuevas conversiones.

## Preguntas frecuentes

### ¿La aplicación modifica mi archivo original?

No. La aplicación prepara un archivo nuevo y lo guarda en la ubicación que el usuario elige.

### ¿Puedo guardar con otro nombre?

Sí. Al usar `Guardar convertido`, puedes cambiar el nombre y la carpeta de destino.

### ¿Qué pasa si cierro la ventana antes de guardar?

La conversión preparada en memoria se perderá y deberás repetir el proceso.

### ¿Puedo convertir al mismo formato?

No. La aplicación evita conversiones redundantes al mismo formato de origen.

## Recomendaciones de uso

- Revisa la vista previa antes de guardar el archivo convertido.
- Usa nombres de archivo claros para distinguir originales y convertidos.
- Evita abrir el archivo de destino en otro programa mientras intentas guardarlo.
- Si trabajas con archivos importantes, conserva una copia del original.

## Mejoras futuras previstas

- Más pruebas con archivos reales de ejemplo.
- Mejora visual del empaquetado y la distribución.
- Posible ampliación de formatos soportados en futuras versiones.

## Historial de versiones del manual

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
