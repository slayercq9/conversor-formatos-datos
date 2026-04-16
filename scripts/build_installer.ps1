param(
    [string]$Version = "5.2.0"
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Path $PSScriptRoot -Parent
$issPath = Join-Path $projectRoot "installer\\ConversorFormatos.iss"
$distPath = Join-Path $projectRoot "dist\\ConversorFormatos"
$installerOutput = Join-Path $projectRoot "installer-output"

if (-not (Test-Path -LiteralPath $distPath)) {
    throw "No se encontró la salida de PyInstaller en '$distPath'. Ejecuta primero .\\scripts\\build.ps1."
}

if (-not (Test-Path -LiteralPath $issPath)) {
    throw "No se encontró el script de Inno Setup en '$issPath'."
}

$compilerCandidates = @(
    "${env:ProgramFiles(x86)}\\Inno Setup 6\\ISCC.exe",
    "${env:ProgramFiles}\\Inno Setup 6\\ISCC.exe"
)

$iscc = $compilerCandidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1

if (-not $iscc) {
    throw (
        "No se encontró ISCC.exe. Instala Inno Setup 6 para compilar el instalador de Windows. " +
        "La preparación del proyecto ya está lista en installer\\ConversorFormatos.iss."
    )
}

if (-not (Test-Path -LiteralPath $installerOutput)) {
    New-Item -ItemType Directory -Path $installerOutput | Out-Null
}

Write-Host "Compilando instalador con Inno Setup..."
& $iscc "/DMyAppVersion=$Version" $issPath

Write-Host "Instalador listo. Revisa la carpeta installer-output."
