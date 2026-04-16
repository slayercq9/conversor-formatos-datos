# Changelog

Todos los cambios relevantes de este proyecto se documentarán en este archivo.

## [5.0.0] - 2026-04-15

### Añadido

- Soporte multidioma ligero para español e inglés en la interfaz.
- Selector visible de idioma en la ventana principal.
- Persistencia de la preferencia de idioma entre sesiones.
- Capa centralizada de textos para facilitar mantenimiento futuro.

### Mejorado

- Ventana principal, ayuda, acerca de, botones, etiquetas y mensajes visibles ahora pueden mostrarse en ambos idiomas.
- La vista previa y los mensajes del dominio se traducen en la capa de interfaz sin tocar la lógica central.

## [4.2.0] - 2026-04-15

### Añadido

- Preparación formal para generar un instalador de Windows con Inno Setup 6.
- Script [scripts/build_installer.ps1](/C:/Users/Fernando/Documents/Conversor_formatos/scripts/build_installer.ps1) para compilar el instalador de forma repetible.
- Base de configuración del instalador en [installer/ConversorFormatos.iss](/C:/Users/Fernando/Documents/Conversor_formatos/installer/ConversorFormatos.iss).

### Mejorado

- Documentación actualizada para distinguir claramente entre versión portable e instalable.
- Flujo de build principal actualizado para mencionar ambas salidas oficiales.
