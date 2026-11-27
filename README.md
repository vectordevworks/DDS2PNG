# DDS2PNG

**Convert DDS textures into PNG images with ease.**

A lightweight Python desktop application for converting DDS (DirectDraw Surface) texture files into PNG images using Microsoft's DirectXTex.

<p align="center"> <a href="[https://github.com/vectordevworks/DDS2PNG](https://github.com/vectordevworks/DDS2PNG)"> <img src="[https://img.shields.io/badge/GitHub-DDS2PNG-181717?style=for-the-badge&logo=github](https://img.shields.io/badge/GitHub-DDS2PNG-181717?style=for-the-badge&logo=github)" alt="GitHub"> </a> <img src="[https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)" alt="Python"> <img src="[https://img.shields.io/badge/Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white](https://img.shields.io/badge/Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)" alt="Windows"> <img src="[https://img.shields.io/badge/License-MIT-6B34DB?style=for-the-badge](https://img.shields.io/badge/License-MIT-6B34DB?style=for-the-badge)" alt="MIT License"> </p>

<p align="center"> <a href="[https://github.com/vectordevworks/DDS2PNG/releases](https://github.com/vectordevworks/DDS2PNG/releases)">📦 Releases</a> &nbsp; · &nbsp; <a href="[https://github.com/vectordevworks/DDS2PNG/issues](https://github.com/vectordevworks/DDS2PNG/issues)">🐛 Issues</a> &nbsp; · &nbsp; <a href="#-installation">📥 Installation</a> &nbsp; · &nbsp; <a href="#-usage">🚀 Usage</a> &nbsp; · &nbsp; <a href="#️-building-the-exe">🛠️ Build EXE</a> </p>

---

## 🌐 Language

<p align="center"> <strong>🌍 Choose Your Language</strong> <br> <sub>Select your preferred language to explore DDS2PNG documentation.</sub> </p>

<table align="center"> <tr> <td align="center" width="20%"> <a href="README.md"> <img src="[https://flagcdn.com/w80/gb.png](https://flagcdn.com/w80/gb.png)" width="42" alt="English flag"> <br><strong>English</strong> <br><sub>🇬🇧 English</sub> </a> </td> <td align="center" width="20%"> <a href="README.de.md"> <img src="[https://flagcdn.com/w80/de.png](https://flagcdn.com/w80/de.png)" width="42" alt="German flag"> <br><strong>Deutsch</strong> <br><sub>🇩🇪 German</sub> </a> </td> <td align="center" width="20%"> <a href="README.es.md"> <img src="[https://flagcdn.com/w80/es.png](https://flagcdn.com/w80/es.png)" width="42" alt="Spanish flag"> <br><strong>Español</strong> <br><sub>🇪🇸 Spanish</sub> </a> </td> <td align="center" width="20%"> <a href="README.fr.md"> <img src="[https://flagcdn.com/w80/fr.png](https://flagcdn.com/w80/fr.png)" width="42" alt="French flag"> <br><strong>Français</strong> <br><sub>🇫🇷 French</sub> </a> </td> <td align="center" width="20%"> <a href="README.ja.md"> <img src="[https://flagcdn.com/w80/jp.png](https://flagcdn.com/w80/jp.png)" width="42" alt="Japanese flag"> <br><strong>日本語</strong> <br><sub>🇯🇵 Japanese</sub> </a> </td> </tr> <tr> <td align="center" width="20%"> <a href="README.ko.md"> <img src="[https://flagcdn.com/w80/kr.png](https://flagcdn.com/w80/kr.png)" width="42" alt="South Korean flag"> <br><strong>한국어</strong> <br><sub>🇰🇷 Korean</sub> </a> </td> <td align="center" width="20%"> <a href="README.pt.md"> <img src="[https://flagcdn.com/w80/pt.png](https://flagcdn.com/w80/pt.png)" width="42" alt="Portuguese flag"> <br><strong>Português</strong> <br><sub>🇵🇹 Portuguese</sub> </a> </td> <td align="center" width="20%"> <a href="README.ru.md"> <img src="[https://flagcdn.com/w80/ru.png](https://flagcdn.com/w80/ru.png)" width="42" alt="Russian flag"> <br><strong>Русский</strong> <br><sub>🇷🇺 Russian</sub> </a> </td> <td align="center" width="20%"> <a href="README.zh-CN.md"> <img src="[https://flagcdn.com/w80/cn.png](https://flagcdn.com/w80/cn.png)" width="42" alt="Chinese flag"> <br><strong>简体中文</strong> <br><sub>🇨🇳 Chinese</sub> </a> </td> <td align="center" width="20%"> <a href="README.tr.md"> <img src="[https://flagcdn.com/w80/tr.png](https://flagcdn.com/w80/tr.png)" width="42" alt="Turkish flag"> <br><strong>Türkçe</strong> <br><sub>🇹🇷 Turkish</sub> </a> </td> </tr> </table>

<p align="center"> <sub>✨ DDS2PNG documentation is available in 10 languages.</sub> </p>

---

## 📑 Contents

|Section|Description|
|---|---|
|📖 [Overview](#-overview)|Introduction to DDS2PNG|
|✨ [Features](#-features)|Application features|
|⚙️ [Requirements](#️-requirements)|Required software and tools|
|📥 [Installation](#-installation)|Download and install|
|🐍 [Virtual Environment](#-virtual-environment-optional)|Optional Python environment|
|🚀 [Usage](#-usage)|How to use the application|
|🛠️ [Building the EXE](#️-building-the-exe)|Create a standalone executable|
|👨‍💻 [Developer](#-developer)|Project developer|
|📄 [License](#-license)|License information|

---

## 📖 Overview

**DDS2PNG** is a lightweight Python desktop application designed to convert DDS (DirectDraw Surface) texture files into PNG images.

With its simple graphical interface, you can select DDS files, choose an output directory, and perform conversions without manually entering terminal commands.

The conversion process is powered by **Texconv**, a command-line texture conversion tool included in Microsoft's DirectXTex project.

## ✨ Features

- Convert DDS texture files into PNG images.
    
- Simple and accessible graphical user interface.
    
- Select an output directory for converted images.
    
- Use Microsoft DirectXTex Texconv for conversion.
    
- Run directly from Python source code.
    
- Build a standalone Windows executable.
    

## ⚙️ Requirements

To run the Python source code, you need:

- Windows 10 or Windows 11.
    
- Python 3.x.
    
- Pillow.
    
- Microsoft DirectXTex (Texconv).
    

> **Note:** Python is not required when using a standalone executable. However, Texconv must still be accessible to the application.

### Microsoft DirectXTex (Texconv)

Texconv is the tool used by DDS2PNG to convert DDS texture files.

**Install using Winget:**

```
winget install --id Microsoft.DirectXTex.Texconv --exact
```

**Verify the installation:**

```
winget list --id Microsoft.DirectXTex.Texconv
```

**Manual installation:**

1. Visit the [Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases) page.
    
2. Download the appropriate release.
    
3. Make sure the Texconv executable is accessible to DDS2PNG.
    

## 📥 Installation

**1. Clone the repository:**

```
git clone https://github.com/vectordevworks/DDS2PNG.git
```

**2. Navigate to the project directory:**

```
cd DDS2PNG
```

**3. Install the required dependencies:**

```
py -m pip install -r requirements.txt
```

## 🐍 Virtual Environment (Optional)

You can create a virtual environment to keep the project's Python dependencies isolated from other projects.

### 1. Create a Virtual Environment

```
py -m venv .venv
```

### 2. Activate the Virtual Environment

**PowerShell:**

```
.\.venv\Scripts\Activate.ps1
```

**CMD:**

```
.venv\Scripts\activate.bat
```

### 3. Install Dependencies

```
py -m pip install -r requirements.txt
```

### 4. Deactivate the Virtual Environment

When you are finished, run:

```
deactivate
```

### Troubleshooting Virtual Environment Activation

PowerShell may prevent activation because of its execution policy.

To allow activation for the current PowerShell session only, run:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the virtual environment again:

```
.\.venv\Scripts\Activate.ps1
```

### Alternative: Run Without Activating

You do not need to activate the virtual environment to use it.

**Install dependencies directly:**

```
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Run the application:**

```
.\.venv\Scripts\python.exe DDSConverter.pyw
```

## 🚀 Usage

1. Open the DDS2PNG project directory.
    
2. Run the application using one of the following commands.
    

**Using pyw:**

```
pyw .\DDSConverter.pyw
```

**Alternatively, using pythonw:**

```
pythonw .\DDSConverter.pyw
```

3. Select the DDS files you want to convert.
    
4. Choose the output directory.
    
5. Start the conversion process.
    

The converted PNG files will be saved in the selected output directory.

## 🛠️ Building the EXE

You can package DDS2PNG into a standalone Windows executable using the PowerShell build script included in the project.

### 1. Open the Project Directory

**Method 1 — File Explorer**

1. Open the DDS2PNG project folder in File Explorer.
    
2. Click the address bar.
    
3. Type `powershell` or `cmd`.
    
4. Press Enter.
    

The terminal will open directly in the project directory.

**Method 2 — Open a Terminal Manually**

Open CMD or PowerShell and navigate to your project directory.

**CMD:**

```
cd /d "YOUR_PROJECT_DIRECTORY"
```

**PowerShell:**

```
Set-Location -LiteralPath "YOUR_PROJECT_DIRECTORY"
```

Replace `YOUR_PROJECT_DIRECTORY` with the actual path to your DDS2PNG folder.

### 2. Run the Build Script

**PowerShell:**

```
.\scripts\buid.ps1
```

**CMD:**

```
powershell -ExecutionPolicy Bypass -File "scripts\buid.ps1"
```

The build script performs the following operations:

- Checks the required project files.
    
- Checks the PyInstaller installation.
    
- Cleans previous build files.
    
- Builds the application into an executable.
    
- Includes the required files from the `assets` directory.
    
- Checks the generated executable.
    

### 3. Find the Executable

After a successful build, the executable will be available at:

```
dist\DDS2PNG.exe
```

You can run `DDS2PNG.exe` directly from the `dist` directory.

> **Note:** When using the executable on another computer, make sure Texconv is accessible to the application.

## 👨‍💻 Developer

**VectorDevWorks**

<p align="center"> <a href="[https://github.com/vectordevworks](https://github.com/vectordevworks)"> <img src="[https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github](https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github)" alt="VectorDevWorks GitHub"> </a> </p>

## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.

---

<p align="center"> <strong>Developed with ❤️ by VectorDevWorks</strong> <br> <sub>© VectorDevWorks — DDS2PNG</sub> </p>
