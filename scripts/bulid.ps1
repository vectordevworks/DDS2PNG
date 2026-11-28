$ErrorActionPreference = "Stop"

# ============================================================
# DDS2PNG - PATH CONFIGURATION
# ============================================================

# Build script is located inside the scripts folder.
$ProjectDir = Split-Path -Parent $PSScriptRoot

$MainFile = Join-Path $ProjectDir "DDSConverter.pyw"

$AssetsDir = Join-Path $ProjectDir "assets"
$IconFile = Join-Path $ProjectDir "icon.ico"
$LanguageIconFile = Join-Path $AssetsDir "language.png"
$TexConvFile = Join-Path $AssetsDir "texconv.exe"

$DistDir = Join-Path $ProjectDir "dist"
$BuildDir = Join-Path $ProjectDir "build"

Write-Host ""
Write-Host "========================================"
Write-Host " DDS2PNG - BUILD"
Write-Host " VECTORDEVWORKS"
Write-Host "========================================"
Write-Host ""

# ============================================================
# FILE CHECKS
# ============================================================

Write-Host "[1/5] Dosyalar kontrol ediliyor..."

if (!(Test-Path $MainFile -PathType Leaf)) {
    throw "Ana Python dosyasi bulunamadi: $MainFile"
}

if (!(Test-Path $AssetsDir -PathType Container)) {
    throw "Assets klasoru bulunamadi: $AssetsDir"
}

if (!(Test-Path $IconFile -PathType Leaf)) {
    throw "ICO simgesi bulunamadi: $IconFile"
}

if (!(Test-Path $LanguageIconFile -PathType Leaf)) {
    throw "Dil simgesi bulunamadi: $LanguageIconFile"
}

if (!(Test-Path $TexConvFile -PathType Leaf)) {
    throw "TexConv bulunamadi: $TexConvFile"
}

# ============================================================
# PYINSTALLER CHECK
# ============================================================

Write-Host "[2/5] PyInstaller kontrol ediliyor..."

python -m PyInstaller --version

if ($LASTEXITCODE -ne 0) {
    throw "PyInstaller yuklu degil veya calistirilamadi."
}

# ============================================================
# CLEAN OLD BUILD FILES
# ============================================================

Write-Host "[3/5] Eski derleme dosyalari temizleniyor..."

Remove-Item $DistDir -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item $BuildDir -Recurse -Force -ErrorAction SilentlyContinue

New-Item -ItemType Directory -Path $BuildDir -Force | Out-Null

# ============================================================
# BUILD EXE
# ============================================================

Write-Host "ICO simgesi kullaniliyor..."
Write-Host "TexConv assets klasorunden EXE icine dahil ediliyor..."
Write-Host "[4/5] EXE derleniyor..."

python -m PyInstaller `
    --noconfirm `
    --clean `
    --onefile `
    --windowed `
    --name "DDS2PNG" `
    --icon $IconFile `
    --add-data "$IconFile;." `
    --add-data "$AssetsDir;assets" `
    --distpath $DistDir `
    --workpath $BuildDir `
    --specpath $BuildDir `
    $MainFile

if ($LASTEXITCODE -ne 0) {
    throw "Derleme basarisiz!"
}

# ============================================================
# OUTPUT CHECK
# ============================================================

Write-Host "[5/5] EXE kontrol ediliyor..."

$ExeFile = Join-Path $DistDir "DDS2PNG.exe"

if (!(Test-Path $ExeFile -PathType Leaf)) {
    throw "EXE dosyasi olusturulamadi: $ExeFile"
}

# ============================================================
# SUCCESS
# ============================================================

Write-Host ""
Write-Host "========================================"
Write-Host " BUILD SUCCESSFUL"
Write-Host "========================================"
Write-Host ""
Write-Host "EXE: $ExeFile"
Write-Host "Assets: $AssetsDir"
Write-Host "Icon: $IconFile"
Write-Host "Language Icon: $LanguageIconFile"
Write-Host "TexConv: $TexConvFile"
Write-Host ""
