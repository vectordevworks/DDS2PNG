<div align="center">

# DDS2PNG

### DDS를 PNG로 변환하는 도구

DDS(DirectDraw Surface) 형식의 텍스처 파일을 PNG로 간편하게 변환합니다.

Python 기반의 가볍고 사용하기 쉬운 데스크톱 애플리케이션입니다.

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

### 🌐 언어 선택

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="English"> English</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Deutsch"> Deutsch</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Português"> Português</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Русский"> Русский</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="日本語"> 日本語</a> |
<strong><img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어</strong> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe</a>

---

### 📑 목차

<a href="#genel-bakis">개요</a>
<a href="#ozellikler">기능</a>
<a href="#gereksinimler">요구 사항</a>
<a href="#kurulum">설치</a>
<a href="#sanal-ortam">가상 환경(선택 사항)</a>
<a href="#kullanim">사용 방법</a>
<a href="#derleme">빌드(EXE 만들기)</a>
<a href="#gelistirici">개발자</a>
<a href="#lisans">라이선스</a>

</div>

---

<a id="genel-bakis"></a>
## 🔍 개요

**DDS2PNG**는 DDS(DirectDraw Surface) 형식의 텍스처 파일을 PNG로 변환할 수 있는 가벼운 Python 기반 데스크톱 애플리케이션입니다.

간단한 그래픽 인터페이스에서 파일을 선택하고 쉽게 변환할 수 있습니다. 명령줄 명령을 사용할 필요가 없습니다.

변환 작업은 Microsoft DirectXTex(Texconv)를 통해 수행됩니다.

Texconv 도구는 애플리케이션과 함께 `assets` 폴더에 포함되어 있습니다.

<a id="ozellikler"></a>
## ✨ 기능

- **DDS에서 PNG로 변환:** DDS 파일을 PNG 형식으로 변환합니다.
- **그래픽 인터페이스:** 파일 선택과 변환을 위한 간단한 인터페이스를 제공합니다.
- **Texconv 지원:** Microsoft DirectXTex를 사용하여 DDS 파일을 변환합니다.
- **간편한 사용:** 명령줄을 사용하지 않고 파일을 변환할 수 있습니다.

<a id="gereksinimler"></a>
## 📋 요구 사항

- Windows
- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)

`tkinter`, `ctypes`, `json`, `math`, `os`, `pathlib` 모듈은 Python 표준 라이브러리에 포함되어 있습니다.

Texconv 도구는 애플리케이션과 함께 `assets` 폴더에 포함되어 있습니다.

### Texconv (Texconv(선택적 다운로드))

프로젝트에 포함된 Texconv가 작동하지 않거나 수동으로 다운로드하려는 경우 아래 방법을 사용할 수 있습니다.

**PowerShell (Winget):**

```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

설치 확인:

```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**수동 다운로드:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

<a id="kurulum"></a>
## 📥 설치

1. 저장소를 복제합니다:

```bash
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. 프로젝트 폴더를 엽니다.

3. 프로젝트 폴더에서 PowerShell을 시작합니다.

4. 필요한 Python 패키지를 설치합니다:

```powershell
py -m pip install -r requirements.txt
```

<a id="sanal-ortam"></a>
## 🐍 가상 환경(선택 사항)

가상 환경을 사용하면 Python 종속성을 다른 프로젝트와 분리할 수 있습니다.

**1. 가상 환경 만들기:**

```powershell
py -m venv .venv
```

**2. 가상 환경 활성화:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. 필요한 종속성 설치:**

```powershell
py -m pip install -r requirements.txt
```

**4. 작업이 끝나면 가상 환경 비활성화:**

```powershell
deactivate
```

**CMD(명령 프롬프트)를 통한 활성화:**

PowerShell 대신 CMD를 사용하는 경우:

```cmd
.venv\Scripts\activate.bat
```

가상 환경 종료:

```cmd
deactivate
```

### 가상 환경 활성화 문제

경우에 따라 PowerShell 실행 정책으로 인해 가상 환경 활성화가 차단될 수 있습니다.

이 경우 다음 명령을 실행하세요:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

그런 다음 가상 환경을 다시 활성화하세요:

```powershell
.\.venv\Scripts\Activate.ps1
```

이 설정은 현재 PowerShell 세션에만 적용됩니다. 새 PowerShell 세션을 열면 기본 설정이 다시 적용됩니다.

### 가상 환경을 활성화하지 않고 사용하기

가상 환경 활성화는 필수가 아닙니다. 활성화에 실패하면 Python 및 pip 실행 파일을 직접 호출하여 계속 사용할 수 있습니다.

**종속성 설치:**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**애플리케이션 실행:**

```powershell
.\.venv\Scripts\python.exe DDSConverter.pyw
```

**참고:** 가상 환경 생성, 활성화, 종속성 설치 및 비활성화에는 관리자 권한이 필요하지 않습니다. 단, Python이 올바르게 설치되어 있고 필요한 파일에 접근할 권한이 있어야 합니다.

<a id="kullanim"></a>
## 🚀 사용 방법

1. `DDSConverter.pyw` 파일을 실행합니다:

```powershell
pyw .\DDSConverter.pyw
```

또는 다음 명령을 사용합니다:

```powershell
pythonw .\DDSConverter.pyw
```

2. 변환할 DDS 파일을 선택합니다.

3. 출력 폴더로 기존 `convert` 폴더를 선택하거나 원하는 폴더를 지정할 수 있습니다.

4. PNG 형식으로 변환합니다.

<a id="derleme"></a>
## 📦 빌드(EXE 만들기)

PyInstaller를 사용하여 Python 애플리케이션을 하나의 EXE 파일로 패키징합니다.

### 1. 프로젝트 폴더로 이동

먼저 DDS2PNG 프로젝트 폴더를 엽니다. 다음 방법 중 하나를 사용하여 해당 폴더에서 터미널을 시작할 수 있습니다.

**방법 1: 파일 탐색기에서 터미널 열기**

1. 파일 탐색기에서 DDS2PNG 프로젝트 폴더를 엽니다.

2. 주소 표시줄에 `cmd` 또는 `powershell`을 입력합니다.

3. Enter 키를 누릅니다.

터미널이 프로젝트 폴더에서 바로 열립니다.

**방법 2: 터미널에서 프로젝트 폴더로 이동**

CMD 또는 PowerShell을 열고 아래에서 적절한 명령을 사용합니다.

**CMD:**

```cmd
cd /d "PROJE_KLASORUNUN_YOLU"
```

**PowerShell:**

```powershell
Set-Location -LiteralPath "PROJE_KLASORUNUN_YOLU"
```

`PROJE_KLASORUNUN_YOLU`를 컴퓨터에 있는 DDS2PNG 프로젝트 폴더의 전체 경로로 바꾸세요.

**참고:** 터미널을 관리자 권한으로 실행할 필요가 없습니다. 일반 사용자 권한이면 충분합니다.

### 2. EXE 빌드

프로젝트의 `scripts` 폴더에 있는 `buid.ps1` 스크립트는 PyInstaller를 사용하여 애플리케이션을 EXE 형식으로 빌드합니다.

빌드 스크립트는 다음 작업을 자동으로 수행합니다:

- 필요한 프로젝트 파일을 확인합니다.
- PyInstaller 설치 여부를 확인합니다.
- 이전 빌드 파일을 정리합니다.
- `icon.ico`를 EXE 아이콘으로 사용합니다.
- `assets` 폴더를 EXE 파일에 포함합니다.
- 빌드 결과를 확인합니다.

**CMD에서 실행:**

```cmd
powershell -ExecutionPolicy Bypass -File "scripts\buid.ps1"
```

**PowerShell에서 실행:**

```powershell
.\scripts\buid.ps1
```

### 3. 빌드 결과

빌드가 성공적으로 완료되면 EXE 파일이 다음 위치에 생성됩니다:

```text
dist\DDS2PNG.exe
```

**새 버전을 빌드하는 단계:**

1. DDS2PNG 프로젝트 폴더를 엽니다.

2. 주소 표시줄에 `cmd` 또는 `powershell`을 입력하여 터미널을 시작하거나, 이미 열린 터미널에서 프로젝트 폴더로 이동합니다.

3. 빌드 스크립트를 실행합니다.

4. 생성된 EXE 파일은 `dist` 폴더에서 찾을 수 있습니다.

### 4. 애플리케이션 실행

빌드가 성공적으로 완료된 후 다음 명령으로 애플리케이션을 실행합니다:

```powershell
dist\DDS2PNG.exe
```

또는 `dist` 폴더를 열고 `DDS2PNG.exe`를 두 번 클릭합니다.

**참고:** 애플리케이션을 실행할 때 CMD 또는 PowerShell을 관리자 권한으로 열 필요가 없습니다.

<a id="gelistirici"></a>
## 👨‍💻 개발자

<div align="center">

**VectorDevWorks**

<a href="https://github.com/vectordevworks">
  <img src="https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github" alt="VectorDevWorks GitHub">
</a>

</div>

<a id="lisans"></a>
## 📄 라이선스

이 프로젝트는 MIT 라이선스에 따라 제공됩니다. 자세한 내용은 저장소의 `LICENSE` 파일을 참조하세요.

---

<div align="center">

**VectorDevWorks에서 개발했습니다.**

⭐ 프로젝트가 마음에 들면 GitHub에서 별표를 눌러 주세요!

<a href="https://github.com/vectordevworks/DDS2PNG">
  <img src="https://img.shields.io/badge/Project%20Repository-DDS2PNG-blue?style=for-the-badge&logo=github" alt="DDS2PNG Repository">
</a>

</div>
