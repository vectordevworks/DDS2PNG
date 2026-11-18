# DDS 转 PNG 转换器

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="英语"> 英语
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="德语"> 德语
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="西班牙语"> 西班牙语
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="法语"> 法语
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="日语"> 日语
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="韩语"> 韩语
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="葡萄牙语"> 葡萄牙语
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="俄语"> 俄语
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="土耳其语"> 土耳其语
</a>

一款基于 Python 的轻量级 DDS 转 PNG 工具，配备简洁的图形用户界面。

## 概述

DDS to PNG Converter 是一款桌面应用程序，旨在通过直观的图形用户界面，将 DDS（DirectDraw Surface）格式的纹理文件转换为 PNG 图像。

本项目旨在让用户无需使用命令行命令，即可轻松便捷地转换纹理文件。

## 功能

- 将 DDS 文件转换为 PNG 格式。
- 简洁且易于使用的图形界面。
- 基于 Python 开发的轻量级应用程序。
- 简单的文件选择和转换流程。

## 系统要求

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)：用于将 DDS 文件转换为 PNG 格式。随应用程序一起包含在 `assets` 文件夹中。

### Texconv（可选下载）

如果项目附带的 Texconv 无法正常工作，或者您希望手动下载，可以使用以下方法。

**PowerShell (Winget)：**
```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

检查安装情况：
```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**手动下载：**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## 安装

1. 克隆仓库：
   ```
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```
2. 进入项目目录：
   ```
   cd "项目目录路径"
   ```
3. 安装所需的依赖项：
   ```
   pip install -r requirements.txt
   ```

### 虚拟环境（可选）

您可以使用虚拟环境，将 Python 依赖项与其他项目隔离开来。

1. 创建虚拟环境：
   ```
   python -m venv .venv
   ```
2. 激活虚拟环境：
   ```
   .venv\Scripts\activate
   ```
3. 安装所需的依赖项：
   ```
   python -m pip install -r requirements.txt
   ```

**注意：** 安装和依赖项管理操作只需以普通用户身份运行 PowerShell 或命令提示符（CMD）即可，无需管理员权限。

如果 `pip` 在尝试写入系统级 Python 目录时遇到权限错误，建议使用虚拟环境（`venv`），而不是以管理员身份运行终端。

## 安装

1. 克隆代码仓库：

   ```bash
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
   ```

2. 进入项目目录：

   ```bash
   cd "ПУТЬ К ПАПКЕ ПРОЕКТА"
   ```

## 使用方法

运行应用程序：

```bash
python Converter.pyw
```

选择 DDS 文件，并按照屏幕上的说明将其转换为 PNG 格式。

## 构建（创建 EXE 文件）

按照以下步骤将 Python 应用程序打包为单个 EXE 文件。

**重要提示：** 请以普通用户身份运行 PowerShell，而不是以管理员身份运行。此操作不需要管理员权限。

### 1. 打开 PowerShell

1. 打开 Windows 开始菜单。
2. 在搜索框中输入 `PowerShell` 或 `Windows Terminal`。
3. 正常打开 Windows PowerShell 或 Windows Terminal。
4. 不要选择“以管理员身份运行”。

### 2. 进入项目目录

在 PowerShell 中输入以下命令，进入项目目录：

```powershell
cd "D:\vectorrdevworks\Projeler\Yazılım Projeleri\Python\DDS-to-PNG-Converter"
```

### 3. 嵌入应用程序图标

以下命令会运行 `embed_icon.ps1` 脚本，并将应用程序图标嵌入 Python 文件中。

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**注意：** 由于 Windows 执行策略可能会阻止 PowerShell 脚本运行，因此需要使用 `-ExecutionPolicy Bypass` 参数。此设置仅对启动的 PowerShell 进程有效，不会更改系统范围内的安全设置。

### 4. 使用 PyInstaller 进行构建

图标嵌入完成后，运行以下命令以创建 EXE 文件：

```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.ico" --name "DDS-to-PNG-Converter" "Converter.pyw"
```

**命令参数：**

| 参数            | 说明              |
| ------------- | --------------- |
| `--noconfirm` | 无需确认即可执行构建。     |
| `--clean`     | 清除之前的构建缓存。      |
| `--onefile`   | 创建单个 EXE 文件。    |
| `--windowed`  | 隐藏控制台窗口。        |
| `--icon`      | 设置 EXE 文件的图标。   |
| `--name`      | 设置生成的 EXE 文件名称。 |

### 5. 构建输出

构建成功完成后，EXE 文件将生成在以下目录中：

```text
dist\DDS-to-PNG-Converter.exe
```

**构建新版本时的步骤顺序：**

1. 以普通用户身份打开 PowerShell。
2. 进入项目目录。
3. 运行图标嵌入命令。
4. 运行 PyInstaller 构建命令。
5. 从 `dist` 目录中获取生成的 EXE 文件。

## 开发者

**vectordevworks**

## 许可证

本项目采用 MIT 许可证授权。详情请参阅 [LICENSE](LICENSE) 文件。
