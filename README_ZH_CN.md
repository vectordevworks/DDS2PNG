# DDS2PNG

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
<strong>
  <img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文
</strong>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="土耳其语"> 土耳其语
</a>

DDS 转 PNG 转换器是一款轻量级的 Python 桌面应用程序，可将 DDS（DirectDraw Surface）格式的纹理文件转换为 PNG 图像。通过简洁的图形界面，您可以轻松选择文件并完成转换。

## 概述

该应用程序使用 Microsoft DirectXTex（Texconv）将 DDS 纹理文件转换为 PNG 格式。转换操作通过图形界面完成，无需使用命令行命令。

Texconv 工具随应用程序一起提供，位于 `assets` 文件夹中。

## 功能

- **DDS 转 PNG：** 将 DDS 文件转换为 PNG 格式。

- **图形界面：** 提供简洁的界面，方便选择文件并执行转换。

- **Texconv 支持：** 使用 Microsoft DirectXTex 工具转换 DDS 文件。

- **易于使用：** 无需使用命令行即可完成文件转换。


## 运行要求

- Windows

- Python 3.x

- Pillow

- Microsoft DirectXTex (Texconv)


`tkinter`、`ctypes`、`json`、`math`、`os` 和 `pathlib` 模块均属于 Python 标准库。

Texconv 用于将 DDS 文件转换为 PNG 格式，并随应用程序一起放在 `assets` 文件夹中。

### Texconv (Texconv（可选下载）)

如果项目附带的 Texconv 无法正常工作，或者您希望手动下载，可以使用以下方法。

**PowerShell (Winget):**

```
winget install --id Microsoft.DirectXTex.Texconv --exact
```

检查安装情况：

```
winget list --id Microsoft.DirectXTex.Texconv
```

**手动下载:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## 安装

1. 克隆仓库：

```
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. 打开项目文件夹。

3. 在此文件夹中启动 PowerShell。

4. 安装所需的 Python 软件包：

```
py -m pip install -r requirements.txt
```

## 虚拟环境（可选）

您可以使用虚拟环境，将 Python 依赖项与其他项目隔离：

1. 创建虚拟环境：

```
py -m venv .venv
```

2. 激活虚拟环境：

```
.\.venv\Scripts\Activate.ps1
```

3. 安装所需的 Python 软件包：

```
py -m pip install -r requirements.txt
```

4. 完成后，停用虚拟环境：

```
deactivate
```

## 使用方法

1. 运行 `DDSConverter.pyw` 文件：

```
pyw .\DDSConverter.pyw
```

或者：

```
pythonw .\DDSConverter.pyw
```

2. 选择要转换的 DDS 文件。

3. 您可以选择现有的 `convert` 文件夹作为输出文件夹，也可以指定任意文件夹。

4. 执行 PNG 格式转换。

## 构建（生成 EXE）

使用 PyInstaller 可以将 Python 应用程序打包为单个 EXE 文件。

### 1. 进入项目文件夹

在项目文件夹中打开 PowerShell。

### 2. 嵌入图标和语言图片

运行以下命令以启动 `embed_icon.ps1` 脚本。该脚本会将应用程序图标以及用于语言选择的 PNG 图片嵌入 Python 文件中。

```
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**注意：** 当 Windows 执行策略可能阻止 PowerShell 脚本运行时，可以使用 `-ExecutionPolicy Bypass` 参数。该参数仅对启动的 PowerShell 进程有效，不会更改系统范围的安全设置。

### 3. 构建输出

构建成功完成后，EXE 文件将在以下位置生成：

```
dist\DDS2PNG.exe
```

**构建新版本的步骤：**

1. 打开 PowerShell。

2. 确保已安装 PyInstaller。

3. 进入项目文件夹。

4. 运行构建脚本。

5. 生成的 EXE 文件可以在 `dist` 文件夹中找到。

## 开发者

**vectordevworks**

## 许可证

本项目采用 MIT 许可证授权。详情请参阅项目仓库中的 `LICENSE` 文件。
