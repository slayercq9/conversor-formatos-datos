# Checklist de publicación

Esta lista describe las verificaciones recomendadas antes de publicar una nueva
versión. Debe ejecutarse desde la raíz del repositorio y adaptarse al número de
versión correspondiente.

## 1. Metadatos y documentación

- [ ] Confirmar la versión SemVer en `src/utils/constants.py`.
- [ ] Confirmar la fecha visible de última actualización.
- [ ] Revisar `README.md`, `MANUAL_USUARIO.md` y `CHANGELOG.md`.
- [ ] Verificar que scripts e instalador usan la misma versión.
- [ ] Confirmar que las notas de compatibilidad siguen siendo correctas.
- [ ] Buscar referencias a versiones anteriores que aparezcan como actuales.

## 2. Pruebas previas

```powershell
python -m pytest
python -m compileall app.py src tests hook-tkinterdnd2.py
python -m pip check
```

- [ ] Todas las pruebas pasan.
- [ ] `compileall` termina sin errores.
- [ ] No existen dependencias instaladas con conflictos.
- [ ] La aplicación abre correctamente desde `python app.py`.

## 3. Limpieza de artefactos

Antes de construir, eliminar únicamente salidas generadas de ejecuciones
anteriores:

```powershell
Remove-Item .\build, .\dist, .\portable, .\installer-output `
  -Recurse -Force -ErrorAction SilentlyContinue
```

- [ ] No quedan ejecutables o ZIP antiguos mezclados con la nueva versión.
- [ ] No se eliminan `src/`, `tests/`, `assets/`, `scripts/` ni `installer/`.
- [ ] `.gitignore` continúa excluyendo artefactos y preferencias locales.

## 4. Build de la aplicación

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build.ps1
```

- [ ] El script termina con código de salida correcto.
- [ ] Existe `dist/ConversorFormatos/ConversorFormatos.exe`.
- [ ] El ejecutable muestra el icono y abre sin errores.
- [ ] Drag and drop funciona en el ejecutable.
- [ ] Se prueban lectura, conversión y guardado de los formatos soportados.

## 5. Paquete portable

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\package_portable.ps1
```

- [ ] Existe `portable/ConversorFormatos-<versión>-portable.zip`.
- [ ] El ZIP incluye el ejecutable, `_internal/`, `docs/` y la documentación principal.
- [ ] El ZIP incluye `portable.mode` junto al ejecutable.
- [ ] El paquete se descomprime en una carpeta nueva sin errores.
- [ ] La aplicación funciona desde la carpeta descomprimida.
- [ ] Las preferencias se crean junto al ejecutable cuando la carpeta tiene permisos de escritura.

## 6. Instalador de Windows

Requiere Inno Setup 6:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\build_installer.ps1
```

- [ ] Existe `installer-output/ConversorFormatos-<versión>-setup.exe`.
- [ ] Nombre, versión, autor e icono son correctos.
- [ ] La instalación funciona en una ubicación limpia.
- [ ] Los accesos directos opcionales apuntan al ejecutable correcto.
- [ ] La aplicación inicia después de instalarse.
- [ ] La instalación incluye `docs/` y sus enlaces desde el README funcionan.
- [ ] Las preferencias se guardan en `%APPDATA%\ConversorFormatos\preferences.json`.
- [ ] La desinstalación elimina los archivos instalados.

## 7. Validación de Git

```powershell
git status --short
git diff --check
git ls-files
```

- [ ] El árbol de trabajo contiene únicamente cambios intencionales.
- [ ] No hay errores de espacios o formato detectados por `git diff --check`.
- [ ] No están rastreados `build/`, `dist/`, `portable/` o `installer-output/`.
- [ ] No están rastreados archivos `.exe`, `.zip` ni `preferences.json`.
- [ ] El commit de publicación contiene documentación y metadatos coherentes.

## 8. GitHub Release

- [ ] El tag coincide exactamente con la versión publicada.
- [ ] El tag apunta al commit validado.
- [ ] El título y las notas resumen los cambios de `CHANGELOG.md`.
- [ ] Se adjuntan el ZIP portable y el instalador correctos.
- [ ] Los nombres de los assets contienen la versión esperada.
- [ ] No se adjuntan builds intermedios, cachés o preferencias locales.

## 9. Verificación de descargas

- [ ] Descargar ambos assets desde la página pública del release.
- [ ] Comparar nombres y tamaños con los archivos locales publicados.
- [ ] Descomprimir y ejecutar nuevamente la versión portable descargada.
- [ ] Ejecutar el instalador descargado en un entorno limpio o máquina virtual.
- [ ] Confirmar que Windows muestra la versión correcta en las propiedades.
- [ ] Verificar al menos una conversión con cada formato soportado.
- [ ] Registrar opcionalmente hashes SHA-256 para futuras comprobaciones.

## 10. Cierre

- [ ] Confirmar que los enlaces del README y la documentación funcionan.
- [ ] Eliminar artefactos locales que ya no sean necesarios.
- [ ] Conservar una copia verificable de los assets publicados.
- [ ] Registrar cualquier limitación descubierta para la siguiente versión.

[Volver al README](../README.md)
