<div align="center">

# DDS2PNG

### DDS 转 PNG 转换器

轻松将 DDS（DirectDraw Surface）格式的纹理文件转换为 PNG。

一款基于 Python、轻量且易于使用的桌面应用程序。

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

### 🌐 语言选择

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="English"> English</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Deutsch"> Deutsch</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Português"> Português</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Русский"> Русский</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="日本語"> 日本語</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어</a> |
<strong><img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文</strong> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe</a>

---

### 📑 目录

<a href="#genel-bakis">概述</a>
<a href="#ozellikler">功能</a>
<a href="#gereksinimler">系统要求</a>
<a href="#kurulum">安装</a>
<a href="#sanal-ortam">虚拟环境（可选）</a>
<a href="#kullanim">使用方法</a>
<a href="#derleme">构建（生成 EXE）</a>
<a href="#gelistirici">开发者</a>
<a href="#lisans">许可证</a>

</div>

---

<a id="genel-bakis"></a>
## 🔍 概述

**DDS2PNG** 是一款轻量级 Python 桌面应用程序，可将 DDS（DirectDraw Surface）格式的纹理文件转换为 PNG。

通过简单的图形界面即可轻松选择文件并完成转换，无需使用命令行命令。

转换通过 Microsoft DirectXTex（Texconv）完成。

Texconv 工具随应用程序一起放在 `assets` 文件夹中。

<a id="ozellikler"></a>
## ✨ 功能

- **DDS 转 PNG：** 将 DDS 文件转换为 PNG 格式。
- **图形界面：** 提供简单的文件选择和转换界面。
- **支持 Texconv：** 使用 Microsoft DirectXTex 转换 DDS 文件。
- **易于使用：** 无需使用命令行即可转换文件。

<a id="gereksinimler"></a>
## 📋 系统要求

- Windows
- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)

`tkinter`、`ctypes`、`json`、`math`、`os` 和 `pathlib` 模块属于 Python 标准库。

Texconv 工具随应用程序一起放在 `assets` 文件夹中。

### Texconv (Texconv（可选下载）)

如果项目附带的 Texconv 无法运行，或者您希望手动下载，可以使用以下方法。

**PowerShell (Winget):**

```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

检查安装情况：

```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**手动下载：**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

<a id="kurulum"></a>
## 📥 安装

1. 克隆仓库：

```bash
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. 打开项目文件夹。

3. 在项目文件夹中启动 PowerShell。

4. 安装所需的 Python 软件包：

```powershell
py -m pip install -r requirements.txt
```

<a id="sanal-ortam"></a>
## 🐍 虚拟环境（可选）

您可以使用虚拟环境，将 Python 依赖项与其他项目隔离。

**1. 创建虚拟环境：**

```powershell
py -m venv .venv
```

**2. 激活虚拟环境：**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. 安装所需依赖项：**

```powershell
py -m pip install -r requirements.txt
```

**4. 完成后停用虚拟环境：**

```powershell
deactivate
```

**通过 CMD（命令提示符）激活：**

如果使用 CMD 而不是 PowerShell：

```cmd
.venv\Scripts\activate.bat
```

退出虚拟环境：

```cmd
deactivate
```

### 虚拟环境激活问题

在某些情况下，PowerShell 的执行策略可能会阻止虚拟环境激活。

此时请运行以下命令：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

然后再次激活虚拟环境：

```powershell
.\.venv\Scripts\Activate.ps1
```

此设置仅对当前 PowerShell 会话有效。打开新的 PowerShell 会话时，将恢复默认设置。

### 不激活虚拟环境直接使用

激活虚拟环境并非必需。如果激活失败，您可以直接调用 Python 和 pip 可执行文件继续使用该环境。

**安装依赖项：**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**运行应用程序：**

```powershell
.\.venv\Scripts\python.exe DDSConverter.pyw
```

**注意：** 创建、激活、安装依赖项以及停用虚拟环境均不需要管理员权限。但必须正确安装 Python，并且您需要拥有访问所需文件的权限。

<a id="kullanim"></a>
## 🚀 使用方法

1. 运行 `DDSConverter.pyw` 文件：

```powershell
pyw .\DDSConverter.pyw
```

或者：

```powershell
pythonw .\DDSConverter.pyw
```

2. 选择要转换的 DDS 文件。

3. 可以选择现有的 `convert` 文件夹作为输出文件夹，也可以指定其他文件夹。

4. 执行 PNG 格式转换。

<a id="derleme"></a>
## 📦 构建（生成 EXE）

使用 PyInstaller 将 Python 应用程序打包为单个 EXE 文件。

### 1. 进入项目文件夹

首先打开 DDS2PNG 项目文件夹。您可以使用以下任一方法在项目文件夹中启动终端。

**方法 1：通过文件资源管理器打开终端**

1. 在文件资源管理器中打开 DDS2PNG 项目文件夹。

2. 在地址栏中输入 `cmd` 或 `powershell`。

3. 按 Enter 键。

终端将直接在项目文件夹中打开。

**方法 2：通过终端进入项目文件夹**

打开 CMD 或 PowerShell，并使用下面相应的命令。

**CMD:**

```cmd
cd /d "PROJE_KLASORUNUN_YOLU"
```

**PowerShell:**

```powershell
Set-Location -LiteralPath "PROJE_KLASORUNUN_YOLU"
```

将 `PROJE_KLASORUNUN_YOLU` 替换为计算机上 DDS2PNG 项目文件夹的完整路径。

**注意：** 无需以管理员身份运行终端。普通用户权限即可。

### 2. 构建 EXE

项目 `scripts` 文件夹中的 `buid.ps1` 脚本使用 PyInstaller 将应用程序构建为 EXE 格式。

构建脚本会自动执行以下操作：

- 检查所需的项目文件。
- 检查 PyInstaller 是否已安装。
- 清理以前的构建文件。
- 使用 `icon.ico` 作为 EXE 图标。
- 将 `assets` 文件夹包含在 EXE 文件中。
- 检查构建输出。

**通过 CMD 运行：**

```cmd
powershell -ExecutionPolicy Bypass -File "scripts\buid.ps1"
```

**通过 PowerShell 运行：**

```powershell
.\scripts\buid.ps1
```

### 3. 构建输出

构建成功完成后，EXE 文件将在以下位置生成：

```text
dist\DDS2PNG.exe
```

**构建新版本的步骤：**

1. 打开 DDS2PNG 项目文件夹。

2. 在地址栏中输入 `cmd` 或 `powershell` 启动终端，或者在现有终端中切换到项目文件夹。

3. 运行构建脚本。

4. 可以在 `dist` 文件夹中找到生成的 EXE 文件。

### 4. 运行应用程序

构建成功完成后，使用以下命令运行应用程序：

```powershell
dist\DDS2PNG.exe
```

也可以打开 `dist` 文件夹，双击 `DDS2PNG.exe`。

**注意：** 运行应用程序时，无需以管理员身份打开 CMD 或 PowerShell。

<a id="gelistirici"></a>
## 👨‍💻 开发者

<div align="center">

**VectorDevWorks**

<a href="https://github.com/vectordevworks">
  <img src="https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github" alt="VectorDevWorks GitHub">
</a>

</div>

<a id="lisans"></a>
## 📄 许可证

本项目采用 MIT 许可证。详情请参阅项目仓库中的 `LICENSE` 文件。

---

<div align="center">

**由 VectorDevWorks 开发。**

⭐ 如果您喜欢这个项目，别忘了在 GitHub 上点亮 Star！

<a href="https://github.com/vectordevworks/DDS2PNG">
  <img src="https://img.shields.io/badge/Project%20Repository-DDS2PNG-blue?style=for-the-badge&logo=github" alt="DDS2PNG Repository">
</a>

</div>
