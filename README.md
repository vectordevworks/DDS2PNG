# DDS to PNG Converter

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="English"> English
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="German"> German
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="Spanish"> Spanish
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="French"> French
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Russian"> Russian
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Korean"> Korean
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Portuguese"> Portuguese
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japanese"> Japanese
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Simplified Chinese"> Simplified Chinese
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Turkish"> Turkish
</a>

A lightweight Python-based DDS to PNG conversion tool with a simple graphical interface.

## Overview

DDS to PNG Converter is a desktop application designed to convert texture files in DDS (DirectDraw Surface) format into PNG images through an intuitive graphical interface.

The purpose of this project is to make texture file conversion easy and convenient without requiring users to deal with command-line commands.

## Features

- Convert DDS files to PNG format.
- Simple and user-friendly graphical interface.
- Lightweight Python-based application.
- Easy file selection and conversion process.

## Requirements

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv): Used to convert DDS files to PNG format. It is included with the application in the `assets` folder.

### Texconv (Optional Download)

If the Texconv version included with the project does not work or you prefer to download it manually, you can use the following methods.

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

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```
2. Navigate to the project directory:
   ```bash
   cd "PROJECT FILE PATH"
   ```
3. Install the required dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

### Virtual Environment (Optional)

You can use a virtual environment to keep Python dependencies separate from other projects.

1. (Only if PowerShell reports a script execution error) Temporarily allow script execution for the current session:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
2. Create a virtual environment:
   ```powershell
   python -m venv .venv
   ```
3. Activate the virtual environment:
   ```powershell
   .venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. When you are finished, deactivate the virtual environment:
   ```powershell
   deactivate
   ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd "PROJECT FILE PATH"
   ```

## Usage

Run the application:
```bash
python Converter.pyw
```

Select your DDS file and follow the on-screen instructions to convert it to PNG format.

## Building (Creating an EXE)

Follow the steps below to convert the Python application into a single EXE file.

**Important:** Run PowerShell as a standard user, not as an administrator. Administrator privileges are not required.

### 1. Opening PowerShell

1. Open the Windows Start menu.
2. Type `PowerShell` or `Windows Terminal` in the search bar.
3. Open Windows PowerShell or Windows Terminal normally.
4. Do not use the Run as administrator option.

### 2. Navigating to the Project Folder

Enter the following command in PowerShell to navigate to the project folder:
```powershell
cd "D:\vectorrdevworks\Projeler\Yazılım Projeleri\Python\DDS-to-PNG-Converter"
```

### 3. Embedding the Application Icon

The following command runs the `embed_icon.ps1` script to embed the application icon into the Python file.
```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Note:** The `-ExecutionPolicy Bypass` parameter is used because Windows may prevent PowerShell scripts from running due to the execution policy. This setting applies only to the launched PowerShell process. System-wide security settings are not changed.

### 4. Building with PyInstaller

After the icon embedding process is complete, run the following command to create the EXE file:
```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.ico" --name "DDS-to-PNG-Converter" "Converter.pyw"
```

**Command parameters:**

| Parameter | Description |
|---|---|
| `--noconfirm` | Builds without prompting for confirmation. |
| `--clean` | Clears the previous build cache. |
| `--onefile` | Creates a single EXE file. |
| `--windowed` | Hides the console window. |
| `--icon` | Specifies the EXE file's icon. |
| `--name` | Specifies the name of the EXE file to be created. |

### 5. Build Output

After the build completes successfully, the EXE file will be created in the following folder:
```text
dist\DDS-to-PNG-Converter.exe
```

**Build order when creating a new version:**

1. Open PowerShell as a standard user.
2. Navigate to the project folder.
3. Run the icon embedding command.
4. Run the PyInstaller build command.
5. Retrieve the generated EXE file from the `dist` folder.

## Developer

**vectordevworks**

## License

This project is licensed under the MIT License. See the LICENSE file for details.

