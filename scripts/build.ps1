$ErrorActionPreference = "Stop"

Write-Host "Building ConversorFormatos with PyInstaller..."
pyinstaller ConversorFormatos.spec
Write-Host "Build finished. Check the dist/ConversorFormatos folder."
