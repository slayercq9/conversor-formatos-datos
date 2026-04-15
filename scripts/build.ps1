$ErrorActionPreference = "Stop"

Write-Host "Building ConversorFormatos with PyInstaller..."
pyinstaller ConversorFormatos.spec
Write-Host "Build finished. Check the dist/ConversorFormatos folder."
Write-Host "To prepare a portable package, run .\\scripts\\package_portable.ps1"
Write-Host "To build a Windows installer, run .\\scripts\\build_installer.ps1"
