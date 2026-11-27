<div align="center">

# DDS2PNG

### DDS to PNG Converter

Easily convert texture files in DDS (DirectDraw Surface) format to PNG.

A lightweight, easy-to-use desktop application built with Python.

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

### 🌐 Language Selection

<strong><img src="https://flagcdn.com/gb.svg" width="20" alt="English"> English</strong> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Deutsch"> Deutsch</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Português"> Português</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Русский"> Русский</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="日本語"> 日本語</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe</a>

---

### 📑 Table of Contents

<a href="#genel-bakis">Overview</a>
<a href="#ozellikler">Features</a>
<a href="#gereksinimler">Requirements</a>
<a href="#kurulum">Installation</a>
<a href="#sanal-ortam">Virtual Environment (Optional)</a>
<a href="#kullanim">Usage</a>
<a href="#derleme">Build (Create EXE)</a>
<a href="#gelistirici">Developer</a>
<a href="#lisans">License</a>

</div>

---

<a id="genel-bakis"></a>
## 🔍 Overview

**DDS2PNG** is a lightweight Python-based desktop application that lets you convert texture files in DDS (DirectDraw Surface) format to PNG.

Its simple graphical interface lets you select files and convert them easily. No command-line commands are required.

Conversions are performed using Microsoft DirectXTex (Texconv).

The Texconv tool is included with the application in the `assets` folder.

<a id="ozellikler"></a>
## ✨ Features

- **DDS to PNG conversion:** Converts DDS files to PNG format.
- **Graphical interface:** Provides a simple interface for selecting and converting files.
- **Texconv support:** Uses Microsoft DirectXTex to convert DDS files.
- **Easy to use:** Lets you convert files without using the command line.

<a id="gereksinimler"></a>
## 📋 Requirements

- Windows
- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)

The `tkinter`, `ctypes`, `json`, `math`, `os` and `pathlib` modules are part of the Python standard library.

The Texconv tool is included with the application in the `assets` folder.

### Texconv (Optional Download)

If the Texconv version included with the project does not work, or if you want to download it manually, you can use the methods below.

**PowerShell (Winget):**

```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

To verify the installation:

```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Manual Download:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

<a id="kurulum"></a>
## 📥 Installation

1. Clone the repository:

```bash
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Open the project folder.

3. Start PowerShell in the project folder.

4. Install the required Python packages:

```powershell
py -m pip install -r requirements.txt
```

<a id="sanal-ortam"></a>
## 🐍 Virtual Environment (Optional)

You can use a virtual environment to keep Python dependencies separate from other projects.

**1. Create a virtual environment:**

```powershell
py -m venv .venv
```

**2. Activate the virtual environment:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Install the required dependencies:**

```powershell
py -m pip install -r requirements.txt
```

**4. Deactivate the virtual environment when you are finished:**

```powershell
deactivate
```

**Activation via CMD (Command Prompt):**

If you use CMD instead of PowerShell:

```cmd
.venv\Scripts\activate.bat
```

To exit the virtual environment:

```cmd
deactivate
```

### Virtual Environment Activation Issues

In some cases, PowerShell may block virtual environment activation because of its execution policy.

In this case, run the following command:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the virtual environment again:

```powershell
.\.venv\Scripts\Activate.ps1
```

This setting applies only to the current PowerShell session. The default settings are restored when you open a new PowerShell session.

### Using the Virtual Environment Without Activating It

Activating the virtual environment is not mandatory. If activation fails, you can continue using the environment by calling the Python and pip executables directly.

**To install dependencies:**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**To run the application:**

```powershell
.\.venv\Scripts\python.exe DDSConverter.pyw
```

**Note:** Administrator privileges are not required to create, activate, install dependencies in, or deactivate the virtual environment. However, Python must be installed correctly and you must have permission to access the required files.

<a id="kullanim"></a>
## 🚀 Usage

1. Run the `DDSConverter.pyw` file:

```powershell
pyw .\DDSConverter.pyw
```

Alternatively:

```powershell
pythonw .\DDSConverter.pyw
```

2. Select the DDS file you want to convert.

3. You can choose the existing `convert` folder as the output folder or specify any folder you prefer.

4. Perform the conversion to PNG format.

<a id="derleme"></a>
## 📦 Build (Create EXE)

PyInstaller is used to package the Python application into a single EXE file.

### 1. Navigate to the Project Folder

First, open the DDS2PNG project folder. You can use one of the following methods to start a terminal in the project folder.

**Method 1: Open a terminal through File Explorer**

1. Open the DDS2PNG project folder in File Explorer.

2. Type `cmd` or `powershell` in the address bar.

3. Press Enter.

The terminal will open directly in the project folder.

**Method 2: Navigate to the project folder through the terminal**

Open CMD or PowerShell and use the appropriate command below.

**CMD:**

```cmd
cd /d "PROJE_KLASORUNUN_YOLU"
```

**PowerShell:**

```powershell
Set-Location -LiteralPath "PROJE_KLASORUNUN_YOLU"
```

Replace `PROJE_KLASORUNUN_YOLU` with the full path to the DDS2PNG project folder on your computer.

**Note:** You do not need to run the terminal as an administrator. Normal user permissions are sufficient.

### 2. Build the EXE

The `buid.ps1` script in the project's `scripts` folder builds the application in EXE format using PyInstaller.

The build script automatically performs the following tasks:

- Checks the required project files.
- Checks whether PyInstaller is installed.
- Cleans up previous build files.
- Uses `icon.ico` as the EXE icon.
- Includes the `assets` folder in the EXE file.
- Checks the build output.

**Run via CMD:**

```cmd
powershell -ExecutionPolicy Bypass -File "scripts\buid.ps1"
```

**Run via PowerShell:**

```powershell
.\scripts\buid.ps1
```

### 3. Build Output

After a successful build, the EXE file is created at the following location:

```text
dist\DDS2PNG.exe
```

**Steps to build a new version:**

1. Open the DDS2PNG project folder.

2. Start a terminal by typing `cmd` or `powershell` in the address bar, or navigate to the project folder from an existing terminal.

3. Run the build script.

4. You can find the generated EXE file in the `dist` folder.

### 4. Run the Application

After the build completes successfully, use the following command to run the application:

```powershell
dist\DDS2PNG.exe
```

Alternatively, open the `dist` folder and double-click `DDS2PNG.exe`.

**Note:** You do not need to run CMD or PowerShell as an administrator to launch the application.

<a id="gelistirici"></a>
## 👨‍💻 Developer

<div align="center">

**VectorDevWorks**

<a href="https://github.com/vectordevworks">
  <img src="https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github" alt="VectorDevWorks GitHub">
</a>

</div>

<a id="lisans"></a>
## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file in the project repository for details.

---

<div align="center">

**Developed by VectorDevWorks.**

⭐ If you like the project, don't forget to star it on GitHub!

<a href="https://github.com/vectordevworks/DDS2PNG">
  <img src="https://img.shields.io/badge/Project%20Repository-DDS2PNG-blue?style=for-the-badge&logo=github" alt="DDS2PNG Repository">
</a>

</div>
