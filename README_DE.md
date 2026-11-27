<div align="center">

# DDS2PNG

### DDS-zu-PNG-Konverter

Konvertieren Sie Texturdateien im DDS- (DirectDraw Surface-)Format ganz einfach in PNG.

Eine leichtgewichtige, einfach zu bedienende Desktop-Anwendung auf Python-Basis.

<p>
  <a href="https://github.com/vectordevworks/DDS2PNG">
    <img src="https://img.shields.io/badge/GitHub-Source%20Code-181717?style=for-the-badge&logo=github" alt="GitHub">
  </a>
  <a href="https://github.com/vectordevworks/DDS2PNG/issues">
    <img src="https://img.shields.io/badge/Report%20Issue-Issues-red?style=for-the-badge&logo=github" alt="Issues">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
  </a>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Platform-Windows-blue?style=flat-square&logo=windows&logoColor=white" alt="Windows">
  <img src="https://img.shields.io/badge/Format-DDS%20%E2%86%92%20PNG-orange?style=flat-square" alt="DDS to PNG">
</p>

---

### 🌐 Sprachauswahl

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="English"> English</a> |
<strong><img src="https://flagcdn.com/de.svg" width="20" alt="Deutsch"> Deutsch</strong> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Português"> Português</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Русский"> Русский</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="日本語"> 日本語</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe</a>

---

### 📑 Inhaltsverzeichnis

<a href="#genel-bakis">Überblick</a>
<a href="#ozellikler">Funktionen</a>
<a href="#gereksinimler">Voraussetzungen</a>
<a href="#kurulum">Installation</a>
<a href="#sanal-ortam">Virtuelle Umgebung (Optional)</a>
<a href="#kullanim">Verwendung</a>
<a href="#derleme">Erstellen (EXE erstellen)</a>
<a href="#gelistirici">Entwickler</a>
<a href="#lisans">Lizenz</a>

</div>

---

<a id="genel-bakis"></a>
## 🔍 Überblick

**DDS2PNG** ist eine leichtgewichtige Python-Desktop-Anwendung, mit der Sie Texturdateien im DDS- (DirectDraw Surface-)Format in PNG konvertieren können.

Über die einfache grafische Oberfläche können Sie Dateien auswählen und bequem konvertieren. Befehle in der Kommandozeile sind nicht erforderlich.

Die Konvertierung erfolgt mit Microsoft DirectXTex (Texconv).

Das Texconv-Tool wird zusammen mit der Anwendung im Ordner `assets` bereitgestellt.

<a id="ozellikler"></a>
## ✨ Funktionen

- **DDS-zu-PNG-Konvertierung:** Konvertiert DDS-Dateien in das PNG-Format.
- **Grafische Oberfläche:** Bietet eine einfache Oberfläche zum Auswählen und Konvertieren von Dateien.
- **Texconv-Unterstützung:** Verwendet Microsoft DirectXTex zur Konvertierung von DDS-Dateien.
- **Einfache Bedienung:** Ermöglicht die Konvertierung ohne Kommandozeile.

<a id="gereksinimler"></a>
## 📋 Voraussetzungen

- Windows
- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)

Die Module `tkinter`, `ctypes`, `json`, `math`, `os` und `pathlib` gehören zur Python-Standardbibliothek.

Das Texconv-Tool wird zusammen mit der Anwendung im Ordner `assets` bereitgestellt.

### Texconv (Optionaler Download)

Falls die mit dem Projekt bereitgestellte Texconv-Version nicht funktioniert oder Sie sie manuell herunterladen möchten, können Sie die folgenden Methoden verwenden.

**PowerShell (Winget):**

```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

So überprüfen Sie die Installation:

```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Manueller Download:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

<a id="kurulum"></a>
## 📥 Installation

1. Klonen Sie das Repository:

```bash
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Öffnen Sie den Projektordner.

3. Starten Sie PowerShell im Projektordner.

4. Installieren Sie die erforderlichen Python-Pakete:

```powershell
py -m pip install -r requirements.txt
```

<a id="sanal-ortam"></a>
## 🐍 Virtuelle Umgebung (Optional)

Mit einer virtuellen Umgebung können Sie Python-Abhängigkeiten von anderen Projekten getrennt halten.

**1. Virtuelle Umgebung erstellen:**

```powershell
py -m venv .venv
```

**2. Virtuelle Umgebung aktivieren:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Erforderliche Abhängigkeiten installieren:**

```powershell
py -m pip install -r requirements.txt
```

**4. Virtuelle Umgebung nach Abschluss deaktivieren:**

```powershell
deactivate
```

**Aktivierung über CMD (Eingabeaufforderung):**

Wenn Sie statt PowerShell CMD verwenden:

```cmd
.venv\Scripts\activate.bat
```

So verlassen Sie die virtuelle Umgebung:

```cmd
deactivate
```

### Probleme bei der Aktivierung der virtuellen Umgebung

In einigen Fällen verhindert die Ausführungsrichtlinie von PowerShell die Aktivierung der virtuellen Umgebung.

Führen Sie in diesem Fall folgenden Befehl aus:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Aktivieren Sie anschließend die virtuelle Umgebung erneut:

```powershell
.\.venv\Scripts\Activate.ps1
```

Diese Einstellung gilt nur für die aktuelle PowerShell-Sitzung. Beim Öffnen einer neuen Sitzung werden die Standardeinstellungen wiederhergestellt.

### Virtuelle Umgebung ohne Aktivierung verwenden

Die Aktivierung der virtuellen Umgebung ist nicht zwingend erforderlich. Falls sie fehlschlägt, können Sie die Umgebung weiterhin verwenden, indem Sie Python und pip direkt aufrufen.

**Abhängigkeiten installieren:**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Anwendung starten:**

```powershell
.\.venv\Scripts\python.exe DDSConverter.pyw
```

**Hinweis:** Zum Erstellen, Aktivieren, Installieren von Abhängigkeiten und Deaktivieren der virtuellen Umgebung sind keine Administratorrechte erforderlich. Python muss jedoch korrekt installiert sein und Sie benötigen Zugriff auf die erforderlichen Dateien.

<a id="kullanim"></a>
## 🚀 Verwendung

1. Führen Sie die Datei `DDSConverter.pyw` aus:

```powershell
pyw .\DDSConverter.pyw
```

Alternativ:

```powershell
pythonw .\DDSConverter.pyw
```

2. Wählen Sie die DDS-Datei aus, die Sie konvertieren möchten.

3. Sie können den vorhandenen Ordner `convert` als Ausgabeordner wählen oder einen beliebigen anderen Ordner festlegen.

4. Führen Sie die Konvertierung in das PNG-Format durch.

<a id="derleme"></a>
## 📦 Erstellen (EXE erstellen)

Mit PyInstaller wird die Python-Anwendung in eine einzelne EXE-Datei gepackt.

### 1. Zum Projektordner wechseln

Öffnen Sie zunächst den DDS2PNG-Projektordner. Mit einer der folgenden Methoden können Sie ein Terminal direkt in diesem Ordner starten.

**Methode 1: Terminal über den Datei-Explorer öffnen**

1. Öffnen Sie den DDS2PNG-Projektordner im Datei-Explorer.

2. Geben Sie `cmd` oder `powershell` in die Adressleiste ein.

3. Drücken Sie die Eingabetaste.

Das Terminal wird direkt im Projektordner geöffnet.

**Methode 2: Über das Terminal zum Projektordner wechseln**

Öffnen Sie CMD oder PowerShell und verwenden Sie den passenden Befehl unten.

**CMD:**

```cmd
cd /d "PROJE_KLASORUNUN_YOLU"
```

**PowerShell:**

```powershell
Set-Location -LiteralPath "PROJE_KLASORUNUN_YOLU"
```

Ersetzen Sie `PROJE_KLASORUNUN_YOLU` durch den vollständigen Pfad zum DDS2PNG-Projektordner auf Ihrem Computer.

**Hinweis:** Das Terminal muss nicht als Administrator ausgeführt werden. Normale Benutzerrechte reichen aus.

### 2. EXE erstellen

Das Skript `buid.ps1` im Ordner `scripts` des Projekts erstellt mit PyInstaller eine EXE-Datei.

Das Build-Skript führt automatisch folgende Aufgaben aus:

- Prüft die erforderlichen Projektdateien.
- Prüft die Installation von PyInstaller.
- Entfernt vorherige Build-Dateien.
- Verwendet `icon.ico` als EXE-Symbol.
- Fügt den Ordner `assets` in die EXE-Datei ein.
- Überprüft die Build-Ausgabe.

**Über CMD ausführen:**

```cmd
powershell -ExecutionPolicy Bypass -File "scripts\buid.ps1"
```

**Über PowerShell ausführen:**

```powershell
.\scripts\buid.ps1
```

### 3. Build-Ausgabe

Nach erfolgreichem Build wird die EXE-Datei an folgendem Speicherort erstellt:

```text
dist\DDS2PNG.exe
```

**Schritte zum Erstellen einer neuen Version:**

1. Öffnen Sie den DDS2PNG-Projektordner.

2. Starten Sie ein Terminal, indem Sie `cmd` oder `powershell` in die Adressleiste eingeben, oder wechseln Sie in einem bereits geöffneten Terminal zum Projektordner.

3. Führen Sie das Build-Skript aus.

4. Die erstellte EXE-Datei befindet sich im Ordner `dist`.

### 4. Anwendung starten

Nach erfolgreichem Build können Sie die Anwendung mit folgendem Befehl starten:

```powershell
dist\DDS2PNG.exe
```

Alternativ können Sie den Ordner `dist` öffnen und auf `DDS2PNG.exe` doppelklicken.

**Hinweis:** Zum Starten der Anwendung müssen CMD oder PowerShell nicht als Administrator ausgeführt werden.

<a id="gelistirici"></a>
## 👨‍💻 Entwickler

<div align="center">

**VectorDevWorks**

<a href="https://github.com/vectordevworks">
  <img src="https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github" alt="VectorDevWorks GitHub">
</a>

</div>

<a id="lisans"></a>
## 📄 Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei `LICENSE` im Projekt-Repository.

---

<div align="center">

**Entwickelt von VectorDevWorks.**

⭐ Wenn Ihnen das Projekt gefällt, geben Sie ihm einen Stern auf GitHub!

<a href="https://github.com/vectordevworks/DDS2PNG">
  <img src="https://img.shields.io/badge/Project%20Repository-DDS2PNG-blue?style=for-the-badge&logo=github" alt="DDS2PNG Repository">
</a>

</div>
