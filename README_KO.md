# DDS2PNG

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="영어"> 영어
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="독일어"> 독일어
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="스페인어"> 스페인어
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="프랑스어"> 프랑스어
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="일본어"> 일본어
</a>
|
<strong>
  <img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어
</strong>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="포르투갈어"> 포르투갈어
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="러시아어"> 러시아어
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="중국어 간체"> 중국어 간체
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="터키어"> 터키어
</a>

DDS-PNG 변환기는 DDS(DirectDraw Surface) 형식의 텍스처 파일을 PNG 이미지로 변환하는 Python 기반의 가벼운 데스크톱 애플리케이션입니다. 간단한 그래픽 인터페이스를 통해 파일을 쉽게 선택하고 변환할 수 있습니다.

## 개요

이 애플리케이션은 Microsoft DirectXTex(Texconv)를 사용하여 DDS 텍스처 파일을 PNG 형식으로 변환합니다. 그래픽 인터페이스에서 변환을 수행하므로 명령줄 명령을 사용할 필요가 없습니다.

Texconv 도구는 애플리케이션의 `assets` 폴더에 함께 포함되어 있습니다.

## 기능

- **DDS에서 PNG로 변환:** DDS 파일을 PNG 형식으로 변환합니다.

- **그래픽 인터페이스:** 파일 선택과 변환을 쉽게 할 수 있는 간단한 인터페이스를 제공합니다.

- **Texconv 지원:** DDS 파일을 변환하기 위해 Microsoft DirectXTex 도구를 사용합니다.

- **간편한 사용:** 명령줄을 사용하지 않고 파일을 변환할 수 있습니다.


## 요구 사항

- Windows

- Python 3.x

- Pillow

- Microsoft DirectXTex (Texconv)


`tkinter`, `ctypes`, `json`, `math`, `os`, `pathlib` 모듈은 Python 표준 라이브러리에 포함되어 있습니다.

Texconv는 DDS 파일을 PNG 형식으로 변환하는 데 사용되며 애플리케이션의 `assets` 폴더에 함께 제공됩니다.

### Texconv (Texconv 선택적 다운로드)

프로젝트에 포함된 Texconv가 작동하지 않거나 수동으로 다운로드하려는 경우 아래 방법을 사용할 수 있습니다.

**PowerShell (Winget):**

```
winget install --id Microsoft.DirectXTex.Texconv --exact
```

설치 여부를 확인하려면:

```
winget list --id Microsoft.DirectXTex.Texconv
```

**수동 다운로드:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## 설치

1. 저장소를 복제합니다:

```
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. 프로젝트 폴더를 엽니다.

3. 이 폴더에서 PowerShell을 실행합니다.

4. 필요한 Python 패키지를 설치합니다:

```
py -m pip install -r requirements.txt
```

## 가상 환경(선택 사항)

Python 종속성을 다른 프로젝트와 분리하려면 가상 환경을 사용할 수 있습니다:

1. 가상 환경을 만듭니다:

```
py -m venv .venv
```

2. 가상 환경을 활성화합니다:

```
.\.venv\Scripts\Activate.ps1
```

3. 필요한 Python 패키지를 설치합니다:

```
py -m pip install -r requirements.txt
```

4. 작업을 마치면 가상 환경을 비활성화합니다:

```
deactivate
```

## 사용 방법

1. `DDSConverter.pyw` 파일을 실행합니다:

```
pyw .\DDSConverter.pyw
```

또는 다음 명령을 사용할 수 있습니다:

```
pythonw .\DDSConverter.pyw
```

2. 변환할 DDS 파일을 선택합니다.

3. 출력 폴더로 기존 `convert` 폴더를 선택하거나 원하는 폴더를 지정할 수 있습니다.

4. PNG 형식으로 변환을 실행합니다.

## 빌드(EXE 만들기)

PyInstaller를 사용하면 Python 애플리케이션을 하나의 EXE 파일로 만들 수 있습니다.

### 1. 프로젝트 폴더로 이동

프로젝트 폴더에서 PowerShell을 엽니다.

### 2. 아이콘 및 언어 이미지 포함

아래 명령을 실행하여 `embed_icon.ps1` 스크립트를 시작합니다. 이 스크립트는 애플리케이션 아이콘과 언어 선택에 사용되는 PNG 이미지를 Python 파일에 포함합니다.

```
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**참고:** `-ExecutionPolicy Bypass` 매개변수는 Windows 실행 정책으로 인해 PowerShell 스크립트 실행이 차단될 수 있는 경우에 사용합니다. 이 매개변수는 실행되는 PowerShell 프로세스에만 적용되며 시스템 전체의 보안 설정을 변경하지 않습니다.

### 3. 빌드 결과

빌드가 성공적으로 완료되면 EXE 파일이 다음 위치에 생성됩니다:

```
dist\DDS2PNG.exe
```

**새 버전을 빌드하는 단계:**

1. PowerShell을 엽니다.

2. PyInstaller가 설치되어 있는지 확인합니다.

3. 프로젝트 폴더로 이동합니다.

4. 빌드 스크립트를 실행합니다.

5. 생성된 EXE 파일은 `dist` 폴더에서 찾을 수 있습니다.

## 개발자

**vectordevworks**

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 배포됩니다. 자세한 내용은 프로젝트 저장소의 `LICENSE` 파일을 참조하세요.
