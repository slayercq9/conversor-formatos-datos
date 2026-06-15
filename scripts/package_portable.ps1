param(
    [string]$Version = "1.0.0"
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Path $PSScriptRoot -Parent
$sourceDist = Join-Path $projectRoot "dist\\ConversorFormatos"
$portableRoot = Join-Path $projectRoot "portable"
$packageName = "ConversorFormatos-$Version-portable"
$packageDir = Join-Path $portableRoot $packageName
$zipPath = Join-Path $portableRoot "$packageName.zip"

if (-not (Test-Path -LiteralPath $sourceDist)) {
    throw "No se encontró la salida de PyInstaller en '$sourceDist'. Ejecuta primero .\\scripts\\build.ps1."
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

# Este marcador permite que la app conserve sus preferencias dentro del paquete.
Set-Content `
    -LiteralPath (Join-Path $packageDir "portable.mode") `
    -Value "Portable distribution marker. Keep this file next to the executable." `
    -Encoding ASCII

# Documentación para compartir el paquete con contexto, ayuda y licencia.
$docsToCopy = @(
    "README.md",
    "MANUAL_USUARIO.md",
    "LICENSE",
    "CHANGELOG.md"
)

foreach ($doc in $docsToCopy) {
    Copy-Item -Path (Join-Path $projectRoot $doc) -Destination $packageDir -Force
}

$docsDirectory = Join-Path $projectRoot "docs"
if (-not (Test-Path -LiteralPath $docsDirectory)) {
    throw "No se encontró la carpeta de documentación en '$docsDirectory'."
}
Copy-Item -LiteralPath $docsDirectory -Destination $packageDir -Recurse -Force

$maxZipAttempts = 4
$zipCreated = $false

for ($attempt = 1; $attempt -le $maxZipAttempts; $attempt++) {
    try {
        Compress-Archive -Path $packageDir -DestinationPath $zipPath -Force
        $zipCreated = $true
        break
    }
    catch {
        if ($attempt -eq $maxZipAttempts) {
            throw "No se pudo crear el ZIP después de $maxZipAttempts intentos. Error: $($_.Exception.Message)"
        }

        $delaySeconds = 2 * $attempt
        Write-Warning (
            "No se pudo crear el ZIP en el intento $attempt. " +
            "Se reintentará en $delaySeconds segundos."
        )
        Remove-Item -LiteralPath $zipPath -Force -ErrorAction SilentlyContinue
        Start-Sleep -Seconds $delaySeconds
    }
}

if (-not $zipCreated -or -not (Test-Path -LiteralPath $zipPath)) {
    throw "El proceso de compresión terminó sin generar el ZIP portable."
}

Write-Host "Paquete portable listo."
Write-Host "Carpeta: $packageDir"
Write-Host "ZIP: $zipPath"
