# DDS-zu-PNG-Konverter

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="Englisch"> Englisch
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="Deutsch"> Deutsch
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="Spanisch"> Spanisch
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Französisch"> Französisch
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japanisch"> Japanisch
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Koreanisch"> Koreanisch
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Portugiesisch"> Portugiesisch
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Russisch"> Russisch
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Vereinfachtes Chinesisch"> Vereinfachtes Chinesisch
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Türkisch"> Türkisch
</a>

Der DDS-zu-PNG-Konverter ist eine leichtgewichtige Desktop-Anwendung auf Python-Basis, mit der sich Texturdateien im DDS-Format (DirectDraw Surface) in PNG-Bilder umwandeln lassen. Über die einfache grafische Benutzeroberfläche können Sie Dateien bequem auswählen und konvertieren.

## Übersicht

Die Anwendung konvertiert DDS-Texturdateien mithilfe von Microsoft DirectXTex (Texconv) in das PNG-Format. Die Konvertierung erfolgt über eine grafische Benutzeroberfläche; Befehle in der Kommandozeile sind nicht erforderlich.

Das Texconv-Tool wird zusammen mit der Anwendung im Ordner `assets` bereitgestellt.

## Funktionen

- **DDS-zu-PNG-Konvertierung:** Wandelt DDS-Dateien in das PNG-Format um.

- **Grafische Benutzeroberfläche:** Bietet eine einfache Oberfläche zur Dateiauswahl und Konvertierung.

- **Texconv-Unterstützung:** Verwendet Microsoft DirectXTex zur Konvertierung von DDS-Dateien.

- **Einfache Bedienung:** Ermöglicht die Konvertierung ohne Verwendung der Kommandozeile.


## Systemanforderungen

- Windows

- Python 3.x

- Pillow

- Microsoft DirectXTex (Texconv)


Die Module `tkinter`, `ctypes`, `json`, `math`, `os` und `pathlib` gehören zur Python-Standardbibliothek.

Texconv wird zur Konvertierung von DDS-Dateien in das PNG-Format verwendet und befindet sich zusammen mit der Anwendung im Ordner `assets`.

### Texconv (Optionaler Download)

Falls die mit dem Projekt bereitgestellte Texconv-Version nicht funktioniert oder Sie Texconv manuell herunterladen möchten, können Sie eine der folgenden Methoden verwenden.

**PowerShell (Winget):**

```
winget install --id Microsoft.DirectXTex.Texconv --exact
```

So überprüfen Sie die Installation:

```
winget list --id Microsoft.DirectXTex.Texconv
```

**Manueller Download:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Installation

1. Repository klonen:

```
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Öffnen Sie den Projektordner.

3. Starten Sie PowerShell in diesem Ordner.

4. Installieren Sie die erforderlichen Python-Pakete:

```
py -m pip install -r requirements.txt
```

## Virtuelle Umgebung (optional)

Sie können eine virtuelle Umgebung verwenden, um Python-Abhängigkeiten von anderen Projekten getrennt zu halten:

1. Virtuelle Umgebung erstellen:

```
py -m venv .venv
```

2. Virtuelle Umgebung aktivieren:

```
.\.venv\Scripts\Activate.ps1
```

3. Installieren Sie die erforderlichen Python-Pakete:

```
py -m pip install -r requirements.txt
```

4. Deaktivieren Sie die virtuelle Umgebung, wenn Sie fertig sind:

```
deactivate
```

## Verwendung

1. Führen Sie die Datei `DDSConverter.pyw` aus:

```
pyw .\DDSConverter.pyw
```

Alternativ:

```
pythonw .\DDSConverter.pyw
```

2. Wählen Sie die DDS-Datei aus, die Sie konvertieren möchten.

3. Als Ausgabeordner können Sie den vorhandenen Ordner `convert` oder einen beliebigen anderen Ordner auswählen.

4. Führen Sie die Konvertierung in das PNG-Format durch.

## Erstellen (EXE erstellen)

Mit PyInstaller wird die Python-Anwendung in eine einzelne EXE-Datei umgewandelt.

### 1. Zum Projektordner wechseln

Öffnen Sie PowerShell im Projektordner.

### 2. Symbol- und Sprachbilder einbetten

Führen Sie mit dem folgenden Befehl das Skript `embed_icon.ps1` aus. Dieses Skript bettet das Anwendungssymbol und die für die Sprachauswahl verwendeten PNG-Bilder in die Python-Datei ein.

```
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Hinweis:** Der Parameter `-ExecutionPolicy Bypass` wird verwendet, wenn die Windows-Ausführungsrichtlinie das Ausführen von PowerShell-Skripten verhindern könnte. Dieser Parameter gilt nur für den gestarteten PowerShell-Prozess und ändert nicht die systemweiten Sicherheitseinstellungen.

### 3. Build-Ausgabe

Nach erfolgreichem Abschluss des Builds wird die EXE-Datei an folgendem Speicherort erstellt:

```
dist\DDS2PNG.exe
```

**So erstellen Sie eine neue Version:**

1. Öffnen Sie PowerShell.

2. Stellen Sie sicher, dass PyInstaller installiert ist.

3. Wechseln Sie zum Projektordner.

4. Führen Sie das Build-Skript aus.

5. Die erstellte EXE-Datei finden Sie im Ordner `dist`.

## Entwickler

**vectordevworks**

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei `LICENSE` im Projekt-Repository.
