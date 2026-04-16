# Conversor de Formatos Tabulares

Aplicación de escritorio desarrollada con Python y Tkinter para convertir archivos tabulares entre formatos comunes de manera simple, portable y fácil de compartir.

Versión actual: 5.0.0

Fecha de última actualización: 2026-04-15

Autor: Fernando Corrales Quirós

Manual de usuario: [MANUAL_USUARIO.md](/C:/Users/Fernando/Documents/Conversor_formatos/MANUAL_USUARIO.md)

## Novedad principal de 5.0.0

La interfaz ahora puede mostrarse en español o inglés, con selección de idioma visible y una base centralizada de textos para facilitar mantenimiento futuro. La documentación del proyecto sigue en español en esta fase.

## Qué hace la aplicación

- Convierte archivos tabulares entre formatos comunes y extensibles.
- Muestra una vista previa clara de los datos antes de guardar.
- Permite cargar archivos tanto con selección manual como con drag and drop.
- Mantiene una arquitectura modular, ligera y preparada para seguir creciendo.
- Puede distribuirse como versión portable o como versión instalable para Windows.

## Idiomas de interfaz soportados

- Español
- Inglés

La preferencia de idioma se conserva entre sesiones usando el sistema de preferencias existente.

## Formatos soportados

- CSV
- TSV
- XLSX
- ODS
- JSON
- XML
- TXT

## Distribución

### Versión portable

- Se entrega como carpeta o ZIP listo para usar.
- No requiere instalación.

### Versión instalable

- Se prepara con Inno Setup 6 sobre la salida de PyInstaller.
- Ofrece una experiencia tradicional de instalación en Windows.

## Herramientas de empaquetado

- `PyInstaller` para la aplicación empaquetada.
- `Inno Setup 6` para el instalador de Windows.

## Estado del proyecto

La versión 5.0.0 incorpora interfaz bilingüe ligera sin modificar la lógica funcional central de conversión, guardado o empaquetado.
