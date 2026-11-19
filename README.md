# DDS2PNG

<strong>
  <img src="https://flagcdn.com/gb.svg" width="20" alt="English"> English
</strong>
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
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japanese"> Japanese
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
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Russian"> Russian
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Simplified Chinese"> Simplified Chinese
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Turkish"> Turkish
</a>

DDS to PNG Converter is a lightweight Python-based desktop application that converts texture files in DDS (DirectDraw Surface) format into PNG images. Its simple graphical interface lets you easily select files and perform conversions.

## Overview

The application converts DDS texture files to PNG format using Microsoft DirectXTex (Texconv). Conversion is performed through a graphical interface, so you do not need to work with command-line commands.

The Texconv tool is included with the application in the `assets` folder.

## Features

- **DDS to PNG conversion:** Converts DDS files to PNG format.

- **Graphical interface:** Provides a simple interface that makes file selection and conversion easy.

- **Texconv support:** Uses the Microsoft DirectXTex tool to convert DDS files.

- **Easy to use:** Lets you convert files without using the command line.


## Requirements

- Windows

- Python 3.x

- Pillow

- Microsoft DirectXTex (Texconv)


The `tkinter`, `ctypes`, `json`, `math`, `os`, and `pathlib` modules are part of the Python standard library.

Texconv is used to convert DDS files to PNG format and is included with the application in the `assets` folder.

### Texconv (Optional Download)

If the Texconv version included with the project does not work, or if you want to download it manually, you can use the methods below.

**PowerShell (Winget):**

```
winget install --id Microsoft.DirectXTex.Texconv --exact
```

To verify the installation:

```
winget list --id Microsoft.DirectXTex.Texconv
```

**Manual Download:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Installation

1. Clone the repository:

```
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Open the project folder.

3. Open PowerShell in this folder.

4. Install the required Python packages:

```
py -m pip install -r requirements.txt
```

## Virtual Environment (Optional)

You can use a virtual environment to keep Python dependencies separate from other projects:

1. Create a virtual environment:

```
py -m venv .venv
```

2. Activate the virtual environment:

```
.\.venv\Scripts\Activate.ps1
```

3. Install the required Python packages:

```
py -m pip install -r requirements.txt
```

4. When you are finished, deactivate the virtual environment:

```
deactivate
```

## Usage

1. Run the `DDSConverter.pyw` file:

```
pyw .\DDSConverter.pyw
```

Alternatively:

```
pythonw .\DDSConverter.pyw
```

2. Select the DDS file you want to convert.

3. You can select the existing `convert` folder as the output folder or choose any folder you like.

4. Convert the file to PNG format.

## Build (Create EXE)

PyInstaller is used to package the Python application into a single EXE file.

1. Open the Project Folder

Open PowerShell in the project folder.

2. Embed the Icon and Language Images

Run the `embed_icon.ps1` script using the command below. This script embeds the application icon and the PNG images used for language selection into the Python file.

```
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Note:** The `-ExecutionPolicy Bypass` parameter is used in cases where Windows execution policy may prevent PowerShell scripts from running. This parameter applies only to the PowerShell process being launched and does not change system-wide security settings.

3. Build Output

After the build completes successfully, the EXE file is created at the following location:

```
dist\DDS2PNG.exe
```

**Steps for building a new version:**

1. Open PowerShell.

2. Make sure PyInstaller is installed.

3. Navigate to the project folder.

4. Run the build script.

5. You can find the generated EXE file in the `dist` folder.

## Developer

**vectordevworks**

## License

This project is licensed under the MIT License. See the `LICENSE` file in the project repository for details.
