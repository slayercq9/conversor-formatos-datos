# Verificación de integridad con SHA-256

## ¿Qué es un hash SHA-256?

SHA-256 es una función que calcula una huella digital de longitud fija para un
archivo. Si el contenido cambia, aunque sea mínimamente, el valor calculado
también cambia.

El hash no cifra el archivo ni demuestra por sí solo quién lo publicó. Su
utilidad es permitir comparar una descarga con el valor oficial proporcionado
por el proyecto.

## ¿Para qué sirve?

Antes de ejecutar el instalador o utilizar el paquete portable, la verificación
permite comprobar que:

- la descarga terminó correctamente;
- el archivo no se dañó durante la transferencia;
- el ZIP o EXE coincide con el asset publicado.

Los hashes oficiales de cada release se publicarán en sus notas o en un archivo
adjunto llamado `SHA256SUMS.txt`. Este documento no contiene hashes reales.

## Verificación con PowerShell

Abre PowerShell en la carpeta donde descargaste los archivos y ejecuta:

```powershell
Get-FileHash .\ConversorFormatos-1.0.0-portable.zip -Algorithm SHA256
Get-FileHash .\ConversorFormatos-1.0.0-setup.exe -Algorithm SHA256
```

PowerShell mostrará una tabla con el algoritmo, el hash calculado y la ruta del
archivo. Compara cada valor, carácter por carácter, con el hash oficial
publicado para el mismo nombre de archivo.

La verificación es correcta únicamente cuando ambos valores son idénticos. Si
no coinciden:

1. No ejecutes ni distribuyas el archivo.
2. Elimina la descarga.
3. Descarga nuevamente el asset desde el release oficial.
4. Repite la comprobación.

## Comprobación de un archivo individual

También puedes guardar el resultado en una variable para facilitar la lectura:

```powershell
$result = Get-FileHash .\ConversorFormatos-1.0.0-setup.exe -Algorithm SHA256
$result.Hash
```

La comparación debe realizarse siempre contra las notas del release
correspondiente o contra su `SHA256SUMS.txt`, nunca contra un valor obtenido de
una fuente distinta.

[Volver al README](../README.md)
