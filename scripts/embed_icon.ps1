$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot

$PythonFile = Join-Path $ProjectRoot "Converter.pyw"
$IconFile = Join-Path $ProjectRoot "assets\icon.png"

try {
    if (-not (Test-Path $PythonFile)) {
        throw "Converter.pyw bulunamadi!"
    }

    if (-not (Test-Path $IconFile)) {
        throw "assets\icon.png bulunamadi!"
    }

    $IconBytes = [System.IO.File]::ReadAllBytes($IconFile)

    # PNG imzasini kontrol et
    $PngSignature = [byte[]](137, 80, 78, 71, 13, 10, 26, 10)

    for ($i = 0; $i -lt 8; $i++) {
        if ($IconBytes[$i] -ne $PngSignature[$i]) {
            throw "icon.png gecerli bir PNG dosyasi degil!"
        }
    }

    $Base64 = [Convert]::ToBase64String($IconBytes)

    $Source = [System.IO.File]::ReadAllText($PythonFile)

    $IconCode = @"
    # EMBEDDED APPLICATION ICON
    import base64

    _EMBEDDED_ICON_DATA = "$Base64"

    _icon_image = tk.PhotoImage(
        data=_EMBEDDED_ICON_DATA
    )

    root.iconphoto(True, _icon_image)
    root._icon_reference = _icon_image
"@

    $BlockPattern = '(?ms)^[ \t]*# EMBEDDED APPLICATION ICON.*?^[ \t]*root\._icon_reference = _icon_image[ \t]*\r?\n?'

    $Source = [regex]::Replace($Source, $BlockPattern, "")

    $RootPattern = '(?m)^(\s*)root\s*=\s*tk\.Tk\(\)\s*$'

    if ($Source -notmatch $RootPattern) {
        throw "root = tk.Tk() satiri bulunamadi!"
    }

    $Source = [regex]::Replace(
        $Source,
        $RootPattern,
        {
            param($Match)
            return $Match.Value + "`r`n" + $IconCode.TrimEnd()
        },
        1
    )

    [System.IO.File]::WriteAllText(
        $PythonFile,
        $Source,
        [System.Text.UTF8Encoding]::new($false)
    )

    Write-Host ""
    Write-Host "PNG ikon basariyla gomuldu!" -ForegroundColor Green
    Write-Host "Kaynak: $IconFile"
    Write-Host "Hedef: $PythonFile"
}
catch {
    Write-Host ""
    Write-Host "HATA: $_" -ForegroundColor Red
    exit 1
}
