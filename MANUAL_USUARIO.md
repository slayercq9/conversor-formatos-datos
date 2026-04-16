# Manual de Usuario

Documento vivo orientado al usuario final. Este manual describe cómo usar la aplicación en su estado actual, sin entrar en detalles técnicos innecesarios.

## Introducción

Conversor de Formatos Tabulares es una aplicación de escritorio para convertir archivos tabulares entre formatos comunes de manera simple y guiada.

## Versión actual

5.1.0

## Fecha de última actualización

2026-04-15

## Qué puede hacer la aplicación

- Cargar archivos compatibles desde el explorador.
- Cargar archivos mediante arrastrar y soltar.
- Mostrar una vista previa rápida del contenido.
- Convertir el archivo a otro formato tabular.
- Guardar el resultado como un archivo nuevo.
- Mostrar la interfaz en español o inglés.

## Idiomas disponibles

La interfaz puede mostrarse en:

- Español
- Inglés

El idioma se cambia desde la ventana principal y, cuando es posible, la aplicación recuerda esa preferencia al volver a abrirse.

## Formatos soportados actualmente

Formatos de entrada y salida:

- CSV (`.csv`)
- TSV (`.tsv`)
- XLSX (`.xlsx`)
- ODS (`.ods`)
- JSON (`.json`)
- XML (`.xml`)
- TXT (`.txt`)

## Cómo iniciar la aplicación

### Si usas la versión portable

1. Abre la carpeta de la aplicación.
2. Ejecuta `ConversorFormatos.exe` o inicia la app desde el proyecto con `python app.py`.

### Si usas la versión instalable

1. Instala la aplicación con el asistente de Windows.
2. Ábrela desde el acceso directo del menú Inicio o del escritorio.

## Flujo básico de uso

1. Presiona `Seleccionar archivo` o arrastra un archivo compatible.
2. Revisa la información visible del archivo cargado.
3. Consulta la vista previa para inspección rápida.
4. Selecciona el `Formato de salida`.
5. Presiona `Convertir`.
6. Presiona `Guardar convertido`.

## Vista previa

La vista previa está pensada para revisión rápida y no para edición.

Actualmente muestra:

- columnas detectadas
- filas visibles en la muestra
- aviso cuando la vista previa es parcial

La vista previa puede ser parcial para mantener la aplicación ligera y ágil.

## Ventanas informativas

La aplicación incluye:

- `Cómo usar`: explicación breve del flujo general
- `Acerca de`: nombre de la app, versión, fecha visible y autor

## Mensajes comunes

`Todavía no has cargado un archivo.`
Debes seleccionar o arrastrar un archivo antes de continuar.

`Debes elegir un formato de salida antes de convertir.`
Debes seleccionar un formato de destino para preparar la conversión.

`La vista previa es parcial.`
Solo se muestran las primeras filas para mantener la app rápida.

`No se pudo interpretar el archivo XML como una tabla.`
El archivo XML no tiene una estructura tabular compatible con esta versión.

## Modalidades de distribución

### Portable

- No requiere instalación.
- Puede copiarse y ejecutarse desde otra carpeta o unidad.

### Instalable

- Requiere un instalador de Windows.
- Integra mejor la app con el sistema mediante accesos directos y desinstalación.

## Historial de versiones del manual

### Versión 5.1.0

- Se alinea el manual con el estado actual real de la aplicación.
- Se documentan formatos soportados, vista previa mejorada, interfaz bilingüe y modalidades de distribución.

### Versión 5.0.0

- Se agrega soporte multidioma ligero para español e inglés en la interfaz.
- Se incorpora selección de idioma visible en la ventana principal.
- Se conserva la preferencia de idioma entre sesiones.
