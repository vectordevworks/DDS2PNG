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
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Russisch"> Russisch
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
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japanisch"> Japanisch
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Vereinfachtes Chinesisch"> Vereinfachtes Chinesisch
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Türkisch"> Türkisch
</a>

Ein leichtgewichtiges, Python-basiertes DDS-zu-PNG-Konvertierungstool mit einer einfachen grafischen Benutzeroberfläche.

## Überblick

DDS to PNG Converter ist eine Desktop-Anwendung, mit der Texturdateien im DDS-Format (DirectDraw Surface) über eine intuitive grafische Benutzeroberfläche in PNG-Bilder umgewandelt werden können.

Ziel des Projekts ist es, Benutzern eine einfache und praktische Konvertierung von Texturdateien zu ermöglichen, ohne dass sie sich mit Befehlen in der Kommandozeile beschäftigen müssen.

## Funktionen

- Konvertierung von DDS-Dateien in das PNG-Format.
- Einfache und benutzerfreundliche grafische Oberfläche.
- Leichtgewichtige, Python-basierte Anwendung.
- Einfache Dateiauswahl und Konvertierung.

## Voraussetzungen

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv): Wird zur Konvertierung von DDS-Dateien in das PNG-Format verwendet. Wird zusammen mit der Anwendung im Ordner `assets` bereitgestellt.

### Texconv (Optionaler Download)

Falls die mit dem Projekt bereitgestellte Texconv-Version nicht funktioniert oder Sie sie manuell herunterladen möchten, können Sie eine der folgenden Methoden verwenden.

**PowerShell (Winget):**
```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Überprüfen der Installation:
```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Manueller Download:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Installation

1. Repository klonen:
   ```bash
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```
2. In das Projektverzeichnis wechseln:
   ```bash
   cd "PROJEKTDATEIPFAD"
   ```
3. Die erforderlichen Abhängigkeiten installieren:
   ```powershell
   pip install -r requirements.txt
   ```

### Virtuelle Umgebung (Optional)

Sie können eine virtuelle Umgebung verwenden, um Python-Abhängigkeiten von anderen Projekten getrennt zu halten.

1. (Nur wenn PowerShell einen Skriptausführungsfehler meldet) Erlauben Sie die Skriptausführung vorübergehend für die aktuelle Sitzung:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
2. Virtuelle Umgebung erstellen:
   ```powershell
   python -m venv .venv
   ```
3. Virtuelle Umgebung aktivieren:
   ```powershell
   .venv\Scripts\activate
   ```
4. Erforderliche Abhängigkeiten installieren:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. Nach Abschluss die virtuelle Umgebung verlassen:
   ```powershell
   deactivate
   ```
   
## Verwendung

Anwendung starten:
```bash
python DDSConverter.pyw
```

Wählen Sie Ihre DDS-Datei aus und folgen Sie den Anweisungen auf dem Bildschirm, um sie in das PNG-Format zu konvertieren.

## Kompilierung (EXE erstellen)

Führen Sie die folgenden Schritte aus, um die Python-Anwendung in eine einzelne EXE-Datei umzuwandeln.

**Wichtig:** Starten Sie PowerShell als normaler Benutzer und nicht als Administrator. Administratorrechte sind nicht erforderlich.

### 1. PowerShell öffnen

1. Öffnen Sie das Windows-Startmenü.
2. Geben Sie im Suchfeld `PowerShell` oder `Windows Terminal` ein.
3. Öffnen Sie Windows PowerShell oder Windows Terminal wie gewohnt.
4. Verwenden Sie nicht die Option „Als Administrator ausführen“.

### 2. Zum Projektordner wechseln

Geben Sie den folgenden Befehl in PowerShell ein, um zum Projektordner zu wechseln:
```powershell
cd "PROJEKTDATEIPFAD"
```

### 3. Anwendungssymbol einbetten

Mit dem folgenden Befehl wird das Skript `embed_icon.ps1` ausgeführt, um das Anwendungssymbol in die Python-Datei einzubetten.
```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Hinweis:** `-ExecutionPolicy Bypass` wird verwendet, weil die Ausführungsrichtlinie von Windows die Ausführung von PowerShell-Skripten verhindern kann. Diese Einstellung gilt nur für den gestarteten PowerShell-Prozess. Die systemweiten Sicherheitseinstellungen werden nicht geändert.

### 4. Mit PyInstaller kompilieren

Führen Sie nach dem Einbetten des Symbols den folgenden Befehl aus, um die EXE-Datei zu erstellen:
```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.png" --name "DDS2PNG" "DDSConverter.pyw"
```

**Befehlsparameter:**

| Parameter | Beschreibung |
|---|---|
| `--noconfirm` | Führt die Kompilierung ohne Rückfrage aus. |
| `--clean` | Löscht den Cache vorheriger Kompilierungen. |
| `--onefile` | Erstellt eine einzelne EXE-Datei. |
| `--windowed` | Zeigt kein Konsolenfenster an. |
| `--icon` | Legt das Symbol der EXE-Datei fest. |
| `--name` | Legt den Namen der zu erstellenden EXE-Datei fest. |

### 5. Kompilierungsergebnis

Nach erfolgreicher Kompilierung wird die EXE-Datei im folgenden Ordner erstellt:
```text
dist\DDSConverter.exe
```

**Reihenfolge beim Erstellen einer neuen Version:**

1. PowerShell als normaler Benutzer öffnen.
2. Zum Projektordner wechseln.
3. Den Befehl zum Einbetten des Symbols ausführen.
4. Den PyInstaller-Kompilierungsbefehl ausführen.
5. Die erstellte EXE-Datei aus dem Ordner `dist` entnehmen.

## Entwickler

**vectordevworks**

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der Datei LICENSE.