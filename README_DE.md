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

Ein leichtgewichtiges, Python-basiertes DDS-zu-PNG-Konvertierungstool mit einer einfachen grafischen Benutzeroberfläche.

## Übersicht

DDS to PNG Converter ist eine Desktop-Anwendung, die entwickelt wurde, um Texturdateien im DDS-Format (DirectDraw Surface) über eine intuitive grafische Benutzeroberfläche in PNG-Bilder umzuwandeln.

Ziel dieses Projekts ist es, Benutzern eine einfache und praktische Konvertierung von Texturdateien zu ermöglichen, ohne dass sie mit Befehlen in der Kommandozeile arbeiten müssen.

## Funktionen

- Konvertierung von DDS-Dateien in das PNG-Format.
- Einfache und benutzerfreundliche grafische Oberfläche.
- Leichtgewichtige, Python-basierte Anwendung.
- Einfache Dateiauswahl und Konvertierung.

## Anforderungen

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv): Wird zum Konvertieren von DDS-Dateien in das PNG-Format verwendet. Ist zusammen mit der Anwendung im Ordner `assets` enthalten.

### Texconv (Optionaler Download)

Falls die mit dem Projekt bereitgestellte Texconv-Version nicht funktioniert oder Sie das Programm manuell herunterladen möchten, können Sie die folgenden Methoden verwenden.

**PowerShell (Winget):**
```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Um die Installation zu überprüfen:
```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Manueller Download:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Installation

1. Klonen Sie das Repository:
   ```
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
   ```
2. Wechseln Sie in das Projektverzeichnis:
   ```
   cd "PROJEKTVERZEICHNISPFAD"
   ```
3. Installieren Sie die erforderlichen Abhängigkeiten:
   ```
   pip install -r requirements.txt
   ```

### Virtuelle Umgebung (Optional)

Sie können eine virtuelle Umgebung verwenden, um Python-Abhängigkeiten von anderen Projekten getrennt zu halten.

1. Erstellen Sie eine virtuelle Umgebung:
   ```
   python -m venv .venv
   ```
2. Aktivieren Sie die virtuelle Umgebung:
   ```
   .venv\Scripts\activate
   ```
3. Installieren Sie die erforderlichen Abhängigkeiten:
   ```
   python -m pip install -r requirements.txt
   ```

**Hinweis:** Für Installations- und Abhängigkeitsverwaltungsaufgaben reicht es aus, PowerShell oder die Eingabeaufforderung (CMD) als normaler Benutzer auszuführen. Administratorrechte sind nicht erforderlich.

Wenn `pip` beim Schreiben in das systemweite Python-Verzeichnis einen Berechtigungsfehler verursacht, wird empfohlen, stattdessen eine virtuelle Umgebung (`venv`) zu verwenden, anstatt das Terminal als Administrator auszuführen.

## Installation

1. Repository klonen:

   ```bash
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
   ```

2. Zum Projektverzeichnis wechseln:

   ```bash
   cd "PROJEKTORDNERPFAD"
   ```

## Verwendung

Starten Sie die Anwendung:

```bash
python Converter.pyw
```

Wählen Sie Ihre DDS-Datei aus und folgen Sie den Anweisungen auf dem Bildschirm, um sie in das PNG-Format umzuwandeln.

## Erstellung (EXE-Datei erstellen)

Befolgen Sie die folgenden Schritte, um die Python-Anwendung in eine einzelne EXE-Datei umzuwandeln.

**Wichtig:** Führen Sie PowerShell als normaler Benutzer und nicht als Administrator aus. Administratorrechte sind nicht erforderlich.

### 1. PowerShell öffnen

1. Öffnen Sie das Windows-Startmenü.
2. Geben Sie `PowerShell` oder `Windows Terminal` in das Suchfeld ein.
3. Öffnen Sie Windows PowerShell oder Windows Terminal auf normale Weise.
4. Verwenden Sie nicht die Option Als Administrator ausführen.

### 2. Zum Projektverzeichnis wechseln

Geben Sie den folgenden Befehl in PowerShell ein, um zum Projektverzeichnis zu wechseln:

```powershell
cd "D:\vectorrdevworks\Projeler\Yazılım Projeleri\Python\DDS-to-PNG-Converter"
```

### 3. Anwendungssymbol einbetten

Der folgende Befehl führt das Skript `embed_icon.ps1` aus und bettet das Anwendungssymbol in die Python-Datei ein.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Hinweis:** Der Parameter `-ExecutionPolicy Bypass` wird verwendet, da Windows die Ausführung von PowerShell-Skripten durch die Ausführungsrichtlinie verhindern kann. Diese Einstellung gilt nur für den gestarteten PowerShell-Prozess. Die systemweiten Sicherheitseinstellungen werden nicht geändert.

### 4. Mit PyInstaller erstellen

Führen Sie nach dem Einbetten des Symbols den folgenden Befehl aus, um die EXE-Datei zu erstellen:

```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.ico" --name "DDS-to-PNG-Converter" "Converter.pyw"
```

**Befehlsparameter:**

| Parameter     | Beschreibung                                     |
| ------------- | ------------------------------------------------ |
| `--noconfirm` | Erstellt die Anwendung ohne Bestätigungsabfrage. |
| `--clean`     | Löscht den vorherigen Build-Cache.               |
| `--onefile`   | Erstellt eine einzelne EXE-Datei.                |
| `--windowed`  | Blendet das Konsolenfenster aus.                 |
| `--icon`      | Legt das Symbol der EXE-Datei fest.              |
| `--name`      | Legt den Namen der erstellten EXE-Datei fest.    |

### 5. Build-Ausgabe

Nach erfolgreichem Abschluss des Builds wird die EXE-Datei im folgenden Verzeichnis erstellt:

```text
dist\DDS-to-PNG-Converter.exe
```

**Reihenfolge beim Erstellen einer neuen Version:**

1. PowerShell als normaler Benutzer öffnen.
2. Zum Projektverzeichnis wechseln.
3. Den Befehl zum Einbetten des Symbols ausführen.
4. Den PyInstaller-Build-Befehl ausführen.
5. Die erstellte EXE-Datei aus dem Verzeichnis `dist` entnehmen.

## Entwickler

**vectordevworks**

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der Datei [LICENSE](LICENSE).
