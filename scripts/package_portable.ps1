param(
    [string]$Version = "3.0.0"
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Path $PSScriptRoot -Parent
$sourceDist = Join-Path $projectRoot "dist\\ConversorFormatos"
$portableRoot = Join-Path $projectRoot "portable"
$packageName = "ConversorFormatos-$Version-portable"
$packageDir = Join-Path $portableRoot $packageName
$zipPath = Join-Path $portableRoot "$packageName.zip"

if (-not (Test-Path -LiteralPath $sourceDist)) {
    throw "No se encontró la salida de PyInstaller en '$sourceDist'. Ejecuta primero .\\scripts\\build.ps1 o pyinstaller ConversorFormatos.spec."
}

if (-not (Test-Path -LiteralPath $portableRoot)) {
    New-Item -ItemType Directory -Path $portableRoot | Out-Null
}

if (Test-Path -LiteralPath $packageDir) {
    Remove-Item -LiteralPath $packageDir -Recurse -Force
}

if (Test-Path -LiteralPath $zipPath) {
    Remove-Item -LiteralPath $zipPath -Force
}

Write-Host "Preparando carpeta portable en $packageDir"
New-Item -ItemType Directory -Path $packageDir | Out-Null

Copy-Item -Path (Join-Path $sourceDist "*") -Destination $packageDir -Recurse -Force

# Documentación mínima para compartir el paquete con contexto y licencia.
$docsToCopy = @(
    "README.md",
    "MANUAL_USUARIO.md",
    "LICENSE",
    "CHANGELOG.md"
)

foreach ($doc in $docsToCopy) {
    Copy-Item -Path (Join-Path $projectRoot $doc) -Destination $packageDir -Force
}

Compress-Archive -Path $packageDir -DestinationPath $zipPath -Force

Write-Host "Paquete portable listo."
Write-Host "Carpeta: $packageDir"
Write-Host "ZIP: $zipPath"
