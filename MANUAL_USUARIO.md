# Manual de Usuario

Documento vivo orientado al usuario final. Este manual explica cómo usar la aplicación en su estado actual, de forma clara y sin detalles técnicos innecesarios.

## Introducción

Conversor de Formatos Tabulares es una aplicación de escritorio para convertir archivos tabulares entre formatos comunes de manera simple, guiada y ligera.

## Objetivo de la aplicación

Permitir que una persona cargue un archivo tabular, revise una vista previa rápida y lo convierta a otro formato compatible sin pasos complejos.

## Versión actual

`5.1.1`

## Fecha de última actualización

`2026-04-15`

## Requisitos de uso

- Un equipo con Windows y la aplicación ya preparada para ejecutarse.
- También puede ejecutarse desde Python con las dependencias instaladas.
- Si usas archivos ODS, la app requiere la dependencia `odfpy`, incluida en `requirements.txt`.

## Cómo iniciar la aplicación

### Si usas la versión portable

1. Abre la carpeta de la aplicación.
2. Ejecuta `ConversorFormatos.exe`.

### Si usas la versión instalable

1. Instala la aplicación con el asistente de Windows.
2. Ábrela desde el menú Inicio o desde el acceso directo creado.

### Si ejecutas desde el proyecto

```powershell
python app.py
```

## Cómo seleccionar un archivo

Puedes cargar un archivo de dos formas:

1. Presiona el botón `Seleccionar archivo`.
2. Arrastra y suelta un archivo compatible sobre la ventana principal.

Cuando el archivo se carga, la interfaz muestra:

- nombre del archivo
- extensión
- tamaño aproximado
- cantidad de registros o filas, cuando es posible calcularla

## Cómo elegir el formato de salida

1. Ubica la sección `Configuración`.
2. Abre el selector `Formato de salida`.
3. Elige el formato al que deseas convertir el archivo.

La aplicación recuerda el último formato usado entre sesiones, pero el botón `Limpiar` reinicia la selección visible dentro de la sesión actual.

## Tema visual

La interfaz ofrece dos temas:

- claro
- oscuro

Puedes cambiar el tema desde la ventana principal. En esta fase, el tema activo no se guarda entre sesiones.

## Cómo convertir y guardar

1. Carga un archivo compatible.
2. Revisa la información mostrada y, si lo deseas, la vista previa.
3. Elige el formato de salida.
4. Presiona `Convertir`.
5. Cuando la app indique que la conversión está lista, presiona `Guardar convertido`.
6. Elige la ubicación final y confirma.

## Formatos soportados actualmente

Formatos de entrada y salida:

- CSV (`.csv`)
- TSV (`.tsv`)
- XLSX (`.xlsx`)
- ODS (`.ods`)
- JSON (`.json`)
- XML (`.xml`)
- TXT (`.txt`)

Notas importantes:

- Algunos archivos XML no pueden convertirse en tabla si su estructura no es compatible.
- JSON funciona mejor con listas de registros o estructuras claramente tabulares.

## Vista previa

La vista previa está pensada para inspección rápida. No permite editar datos.

Puede mostrar:

- columnas detectadas
- filas visibles en la muestra
- aviso cuando la vista previa es parcial

La vista previa puede ser parcial para mantener la aplicación ligera y ágil.

## Mensajes o errores comunes y su significado

`Todavía no has cargado un archivo.`
Debes seleccionar o arrastrar un archivo antes de continuar.

`Todavía no has elegido un formato de salida.`
Debes seleccionar un formato de destino antes de convertir.

`La conversión está lista para guardarse.`
La app ya preparó el resultado y puedes usar `Guardar convertido`.

`No se pudo interpretar el archivo XML como una tabla.`
El XML no tiene una estructura tabular compatible con esta versión.

`La vista previa es parcial.`
Solo se muestran las primeras filas para mantener la app rápida.

## Preguntas frecuentes

### ¿La aplicación modifica mi archivo original?

No. La app prepara y guarda un archivo nuevo.

### ¿Puedo usar la aplicación sin instalarla?

Sí. La versión portable puede ejecutarse desde una carpeta local, un USB o una carpeta compartida.

### ¿Qué significa que la app sea portable?

Significa que puede ejecutarse sin proceso de instalación formal, siempre que el paquete portable esté completo.

### ¿La aplicación funciona en español e inglés?

Sí. La interfaz permite cambiar entre ambos idiomas desde la ventana principal.

### ¿También puedo cambiar el tema visual?

Sí. La ventana principal permite alternar entre tema claro y tema oscuro.

## Recomendaciones de uso

- Revisa la vista previa antes de convertir archivos grandes o de estructura poco clara.
- Si un XML o JSON falla, verifica que realmente tenga forma tabular.
- Guarda el archivo convertido en una ubicación distinta para conservar mejor el original.
- Usa `Limpiar` antes de iniciar una tarea nueva para evitar confusiones visuales.

## Mejoras futuras previstas

- ampliar cobertura automatizada de pruebas
- seguir refinando mensajes y consistencia interna
- mejorar reutilización de utilidades compartidas en la interfaz

## Historial de versiones del manual

### Versión 5.1.1

- Se agrega soporte para tema claro y tema oscuro.
- Se incorpora un selector de tema en la ventana principal.

### Versión 5.1.0

- Se alinea el manual con el estado real actual de la aplicación.
- Se documentan formatos soportados, vista previa mejorada, multidioma y modalidades de distribución.

### Versión 5.0.0

- Se incorpora la interfaz bilingüe en español e inglés.

### Versión 4.x

- Se añaden nuevos formatos, vista previa mejorada y preparación de instalador para Windows.
