# Conversor de Formatos Tabulares

Aplicación de escritorio para convertir archivos de datos entre formatos
tabulares comunes sin depender de herramientas complejas. Permite cargar un
archivo, inspeccionar una vista previa y guardar el contenido en otro formato
mediante una interfaz gráfica sencilla para Windows.

- **Versión estable:** `1.0.0`
- **Última actualización:** `2026-06-10`
- **Autor:** Fernando Corrales Quirós
- **Licencia:** [MIT](LICENSE)

## Descargas

Los paquetes publicados están disponibles en:

**[GitHub Releases](https://github.com/slayercq9/conversor-formatos-datos/releases)**

- **Versión portable:** no requiere instalación; basta con descomprimirla y
  ejecutar `ConversorFormatos.exe`.
- **Instalador para Windows:** integra la aplicación mediante el asistente
  tradicional de instalación.

## Características principales

- Conversión de archivos mediante una estructura interna basada en pandas.
- Selección manual de archivos y carga mediante drag and drop.
- Vista previa tabular con columnas detectadas y filas de muestra.
- Información básica del archivo cargado.
- Interfaz disponible en español e inglés.
- Temas claro y oscuro.
- Persistencia local de idioma, tema, último formato y geometría de ventana.
- Validaciones para archivos vacíos, formatos no soportados y errores de
  lectura o escritura.
- Distribución portable e instalable para Windows.

## Formatos soportados

| Formato | Extensión | Lectura | Escritura |
| --- | --- | :---: | :---: |
| CSV | `.csv` | Sí | Sí |
| Excel | `.xlsx` | Sí | Sí |
| JSON | `.json` | Sí | Sí |
| Texto delimitado | `.txt` | Sí | Sí |
| TSV | `.tsv` | Sí | Sí |
| XML tabular | `.xml` | Sí | Sí |
| OpenDocument Spreadsheet | `.ods` | Sí | Sí |

JSON funciona mejor con listas de registros o estructuras claramente
tabulares. XML debe contener registros repetidos y campos consistentes para
representarse correctamente como tabla.

## Uso de la aplicación

1. Selecciona un archivo o arrástralo sobre la ventana principal.
2. Revisa la información del archivo y su vista previa.
3. Elige el formato de salida.
4. Presiona **Convertir**.
5. Presiona **Guardar convertido** y selecciona la ubicación de destino.

La aplicación crea un archivo nuevo y no modifica el archivo original.

## Tecnologías

- **Python**
- **Tkinter / ttk**
- **pandas**
- **openpyxl**
- **odfpy**
- **tkinterdnd2**
- **PyInstaller**
- **Inno Setup**
- **pytest**
- **Git y GitHub**

## Ejecución desde el código fuente

Requisitos:

- Python 3.11 o superior.
- Tkinter disponible en la instalación de Python.
- Git para clonar el repositorio.

```powershell
git clone https://github.com/slayercq9/conversor-formatos-datos.git
cd conversor-formatos-datos
python -m pip install -r requirements.txt
python app.py
```

Para aislar las dependencias se recomienda usar un entorno virtual antes de
instalar `requirements.txt`.

## Pruebas y validaciones

Desde la raíz del proyecto:

```powershell
python -m pytest
python -m compileall app.py src tests hook-tkinterdnd2.py
python -m pip check
```

La configuración de [pytest.ini](pytest.ini) limita la colección automática a
la carpeta `tests/`.

## Generación de distribuciones

Los comandos deben ejecutarse desde la raíz del proyecto y en el orden
indicado.

### Build de PyInstaller

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build.ps1
```

Salida: `dist/ConversorFormatos/`

### Paquete portable

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\package_portable.ps1
```

Salida: `portable/ConversorFormatos-1.0.0-portable.zip`

### Instalador de Windows

Requiere [Inno Setup 6](https://jrsoftware.org/isinfo.php).

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build_installer.ps1
```

Salida: `installer-output/ConversorFormatos-1.0.0-setup.exe`

Los artefactos generados están excluidos del control de versiones y deben
publicarse como archivos adjuntos de una versión.

## Estructura del proyecto

```text
.
|-- app.py                         # Punto de entrada
|-- assets/                        # Icono de la aplicación
|-- installer/
|   `-- ConversorFormatos.iss      # Definición del instalador
|-- scripts/
|   |-- build.ps1                  # Build con PyInstaller
|   |-- package_portable.ps1       # Paquete ZIP portable
|   `-- build_installer.ps1        # Instalador con Inno Setup
|-- src/
|   |-- core/                      # Conversión, lectura y escritura
|   |-- gui/                       # Ventanas y componentes Tkinter
|   |-- i18n/                      # Traducciones ES/EN
|   |-- services/                  # Coordinación de archivos y vista previa
|   `-- utils/                     # Constantes, errores y preferencias
|-- tests/                         # Suite automatizada
|-- ConversorFormatos.spec         # Configuración de PyInstaller
|-- hook-tkinterdnd2.py            # Recursos de drag and drop
`-- requirements.txt
```

## Documentación

- [Manual de usuario](MANUAL_USUARIO.md)
- [Historial de cambios](CHANGELOG.md)
- [Licencia MIT](LICENSE)
- [Resumen del proyecto](docs/project-summary.md)
- [Descripción técnica](docs/technical-overview.md)
- [Checklist de publicación](docs/release-checklist.md)

## Estado del proyecto

La versión `1.0.0` es la primera versión pública estable y utiliza versionado
semántico `MAJOR.MINOR.PATCH`. El estado actual incluye conversión para los
siete formatos documentados, vista previa, drag and drop, interfaz bilingüe,
temas, preferencias persistentes, paquete portable e instalador de Windows.

Mejoras futuras razonables:

- ampliar pruebas automatizadas de integración del ejecutable;
- continuar refinando accesibilidad y consistencia de la interfaz;
- mejorar la reutilización interna de componentes GUI sin aumentar la
  complejidad de la aplicación.
