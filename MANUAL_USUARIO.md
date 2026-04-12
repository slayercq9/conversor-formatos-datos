# Manual de Usuario

Documento vivo del proyecto. Este manual esta pensado para actualizarse en cada nueva version de la aplicacion y servir como referencia clara para usuarios no tecnicos.

## Introduccion

Conversor de Formatos Tabulares es una aplicacion de escritorio que permite transformar archivos tabulares entre distintos formatos comunes. Su interfaz esta pensada para que el proceso de conversion sea claro, guiado y seguro.

## Objetivo de la aplicacion

El objetivo principal de la aplicacion es facilitar la conversion de archivos tabulares sin requerir conocimientos tecnicos avanzados. La herramienta permite abrir un archivo, revisar una vista previa, elegir un formato de salida y guardar el resultado convertido.

## Version actual

1.2.0

## Fecha de ultima actualizacion

2026-04-12

## Requisitos de uso

- Tener Python 3.11 o superior instalado.
- Tener las dependencias del proyecto instaladas desde `requirements.txt`.
- Contar con un archivo de entrada en uno de los formatos soportados.

## Como iniciar la aplicacion

1. Abrir una terminal en la carpeta raiz del proyecto.
2. Activar el entorno virtual si el proyecto utiliza uno.
3. Ejecutar el siguiente comando:

```powershell
python app.py
```

Al iniciar, se abrira la ventana principal de la aplicacion.

## Como seleccionar un archivo

1. Presiona el boton `Seleccionar archivo`.
2. Busca el archivo que deseas convertir.
3. Seleccionalo y confirma la apertura.
4. La aplicacion mostrara la ruta o nombre del archivo cargado.

Si no seleccionas ningun archivo, la aplicacion seguira abierta y mostrara un mensaje de orientacion.

## Como elegir el formato de salida

1. Ubica el campo `Formato de salida`.
2. Haz clic en la lista desplegable.
3. Selecciona el formato al que deseas convertir el archivo.

Debes elegir un formato antes de convertir. Si no lo haces, la aplicacion mostrara un mensaje informativo.

## Como convertir y guardar

1. Una vez cargado el archivo y elegido el formato de salida, presiona `Convertir`.
2. La aplicacion preparara la conversion internamente.
3. Cuando la conversion este lista, presiona `Guardar convertido`.
4. Elige la carpeta de destino y el nombre del archivo.
5. Confirma el guardado.

Si ocurre un problema durante la lectura o escritura, la aplicacion mostrara un dialogo explicando el motivo.

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

`Todavia no has cargado un archivo.`
Significa que debes seleccionar un archivo antes de usar la vista previa o iniciar la conversion.

`Debes elegir un formato de salida antes de convertir.`
Significa que la lista de formato de salida aun no tiene una opcion elegida.

`El archivo seleccionado esta vacio.`
Indica que el archivo no contiene datos utiles para procesar.

`El formato del archivo cargado no es soportado.`
Indica que la extension del archivo no pertenece a los formatos actualmente compatibles.

`No se pudo leer el archivo ...`
Suele significar que el archivo esta danado, en uso por otro programa o no tiene un contenido valido para su formato.

`No se pudo guardar el archivo ...`
Suele indicar problemas de permisos, rutas invalidas o que el archivo de destino esta abierto en otro programa.

## Preguntas frecuentes

### La aplicacion modifica mi archivo original?

No. La aplicacion prepara un archivo nuevo y lo guarda en la ubicacion que el usuario elige.

### Puedo guardar con otro nombre?

Si. Al usar `Guardar convertido`, puedes cambiar el nombre y la carpeta de destino.

### Que pasa si cierro la ventana antes de guardar?

La conversion preparada en memoria se perdera y deberas repetir el proceso.

### Puedo convertir al mismo formato?

No. La aplicacion evita conversiones redundantes al mismo formato de origen.

## Recomendaciones de uso

- Revisa la vista previa antes de guardar el archivo convertido.
- Usa nombres de archivo claros para distinguir originales y convertidos.
- Evita abrir el archivo de destino en otro programa mientras intentas guardarlo.
- Si trabajas con archivos importantes, conserva una copia del original.

## Mejoras futuras previstas

- Soporte para arrastrar y soltar archivos en la ventana principal.
- Mas pruebas con archivos reales de ejemplo.
- Mejora visual del empaquetado y distribucion.
- Posible ampliacion de formatos soportados en futuras versiones.

## Historial de versiones del manual

### Version 1.2.0

- Se crea el manual de usuario inicial.
- Se documenta el flujo completo de uso de la aplicacion.
- Se alinean version y fecha visibles con la documentacion del proyecto.
- Se confirma la integracion del icono definitivo `assets/icon.ico`.
