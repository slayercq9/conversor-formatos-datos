# Descripción técnica

## Ficha técnica

| Campo | Valor |
| --- | --- |
| Aplicación | Conversor de Formatos Tabulares |
| Versión estable | `1.0.0` |
| Plataforma de distribución | Windows |
| Lenguaje | Python |
| Interfaz | Tkinter y ttk |
| Modelo de datos interno | `pandas.DataFrame` |
| Punto de entrada | `app.py` |
| Licencia | MIT |
| Persistencia local | JSON |

## Tecnologías utilizadas

- **Python:** implementación de la aplicación y scripts auxiliares.
- **Tkinter / ttk:** ventanas, controles, tabla de vista previa y estilos.
- **pandas:** lectura, representación y escritura de datos tabulares.
- **openpyxl:** soporte de lectura y escritura para XLSX.
- **odfpy:** soporte de lectura y escritura para ODS.
- **tkinterdnd2:** integración de drag and drop con la ventana raíz.
- **PyInstaller:** generación del ejecutable y distribución portable.
- **Inno Setup:** generación del instalador de Windows.
- **pytest:** pruebas automatizadas.
- **Git y GitHub:** control de versiones, documentación y distribución.

## Arquitectura del proyecto

La aplicación sigue una separación por responsabilidades:

```text
app.py
  |
  v
src/gui/  --->  src/services/  --->  src/core/
   |                |                  |
   +----------> src/utils/ <-----------+
   |
   +----------> src/i18n/
```

La GUI captura acciones del usuario, pero no implementa la conversión. Los
servicios adaptan esas acciones a operaciones del núcleo y mantienen estados
de sesión como la conversión preparada. El núcleo valida, lee y escribe los
datos mediante handlers registrados por formato.

## Responsabilidades por carpeta

### `src/core/`

- `file_types.py`: fuente central de formatos, extensiones, etiquetas y filtros.
- `validators.py`: validaciones de rutas, formatos y DataFrames.
- `reader.py`: lectores que transforman cada formato en un DataFrame.
- `writer.py`: escritores que exportan un DataFrame al formato solicitado.
- `converter.py`: coordinación del flujo de preparación y guardado.

### `src/services/`

- `file_service.py`: adapta el conversor al flujo interactivo de la GUI y
  conserva temporalmente la conversión preparada.
- `preview_service.py`: construye una muestra serializable con filas, columnas
  y métricas para la tabla de vista previa.

### `src/gui/`

- `main_window.py`: composición de la ventana principal y coordinación de eventos.
- `preview_table.py`: representación visual de la muestra tabular.
- `dialogs.py`: diálogos de selección, guardado y mensajes.
- `drag_drop.py`: integración real y fallback seguro de tkinterdnd2.
- `theme.py`: paletas y estilos reutilizables para temas claro y oscuro.
- `about_window.py` y `help_window.py`: ventanas informativas.

### `src/i18n/`

`translations.py` contiene los catálogos ES/EN y el traductor ligero utilizado
por las ventanas y mensajes visibles.

### `src/utils/`

Contiene metadatos, constantes, excepciones de dominio, helpers y persistencia
de preferencias. `preferences.py` guarda un JSON pequeño y utiliza valores
seguros cuando el archivo no existe o no puede interpretarse. En la instalación
tradicional utiliza `%APPDATA%\ConversorFormatos\preferences.json`; el paquete
portable conserva el archivo junto al ejecutable mediante un marcador propio.

### `tests/`

Agrupa pruebas unitarias y de integración ligera para formatos, validaciones,
servicios, preferencias, temas, traducciones y drag and drop no visual.

### `scripts/` e `installer/`

Los scripts PowerShell generan el build, el paquete portable y el instalador.
`installer/ConversorFormatos.iss` define los metadatos, archivos y accesos
directos utilizados por Inno Setup.

## Flujo general de conversión

1. La GUI recibe una ruta mediante selección manual o drag and drop.
2. Los validadores comprueban existencia, tamaño y extensión.
3. `TabularReader` selecciona el handler y obtiene un DataFrame.
4. `PreviewService` limita la muestra y prepara los datos para la tabla.
5. El usuario selecciona un formato de salida diferente al formato de origen.
6. `FileService` solicita a `TabularConverter` una `PreparedConversion`.
7. El resultado permanece en memoria hasta que el usuario elige una ruta.
8. `TabularWriter` selecciona el handler de salida y escribe el archivo.
9. Las excepciones de dominio se convierten en mensajes amigables en la GUI.

## Estrategia de pruebas

La suite evita automatización GUI frágil y se concentra en comportamiento
determinista:

- roundtrip para CSV, XLSX, JSON, TXT, TSV, XML y ODS;
- errores por archivo inexistente, vacío o no soportado;
- coordinación de `TabularConverter` y `FileService`;
- límites y métricas de `PreviewService`;
- preferencias con rutas temporales y fallbacks seguros;
- consistencia de temas claro/oscuro;
- paridad de claves y fallback de traducciones ES/EN;
- normalización de rutas recibidas mediante drag and drop;
- metadatos públicos de versión.

`pytest.ini` restringe la colección a `tests/`. La validación previa a una
publicación combina pytest, `compileall` y `pip check`.

## Empaquetado y distribución

`ConversorFormatos.spec` configura un build `onedir` optimizado. Incluye el
icono, los motores necesarios para XLSX y ODS, y los recursos Tcl/Tk requeridos
por tkinterdnd2. También excluye bibliotecas opcionales de pandas que la
aplicación no utiliza.

El proceso de distribución tiene tres etapas:

1. `scripts/build.ps1` ejecuta PyInstaller y valida su código de salida.
2. `scripts/package_portable.ps1` reúne el build y la documentación en un ZIP.
3. `scripts/build_installer.ps1` invoca Inno Setup y valida el resultado.

Las salidas se crean en `dist/`, `portable/` e `installer-output/`. Estas
carpetas están excluidas de Git y los archivos finales se publican como assets
de GitHub Releases.

## Capacidades técnicas cubiertas

- Arquitectura modular por capas.
- Registro extensible de lectores y escritores.
- Manejo de excepciones de dominio.
- Persistencia JSON con validación y fallback.
- Internacionalización ligera sin dependencias adicionales.
- Temas ttk centralizados.
- Integración opcional con una biblioteca nativa de drag and drop.
- Pruebas parametrizadas y uso de rutas temporales.
- Empaquetado automatizado y dos modalidades de distribución.

[Volver al README](../README.md)
