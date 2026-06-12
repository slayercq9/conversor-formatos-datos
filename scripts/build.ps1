$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Path $PSScriptRoot -Parent
$specPath = Join-Path $projectRoot "ConversorFormatos.spec"

Write-Host "Building ConversorFormatos with PyInstaller..."
Push-Location $projectRoot
try {
    python -m PyInstaller --clean --noconfirm $specPath
    if ($LASTEXITCODE -ne 0) {
        throw "PyInstaller finalizó con el código de error $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}

Write-Host "Build finished. Check the dist/ConversorFormatos folder."
Write-Host "To prepare a portable package, run .\\scripts\\package_portable.ps1"
Write-Host "To build a Windows installer, run .\\scripts\\build_installer.ps1"
