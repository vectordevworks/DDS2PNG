# DDS to PNG 변환기

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
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="러시아어"> 러시아어
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="포르투갈어"> 포르투갈어
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="일본어"> 일본어
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="중국어(간체)"> 중국어(간체)
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="터키어"> 터키어
</a>

간단한 그래픽 인터페이스를 갖춘 가볍고 Python 기반의 DDS to PNG 변환 도구입니다.

## 개요

DDS to PNG Converter는 직관적인 그래픽 인터페이스를 통해 DDS(DirectDraw Surface) 형식의 텍스처 파일을 PNG 이미지로 변환하도록 설계된 데스크톱 애플리케이션입니다.

이 프로젝트의 목적은 사용자가 명령줄 명령어를 직접 사용할 필요 없이 텍스처 파일을 쉽고 편리하게 변환할 수 있도록 하는 것입니다.

## 주요 기능

- DDS 파일을 PNG 형식으로 변환합니다.
- 간단하고 사용하기 쉬운 그래픽 인터페이스를 제공합니다.
- Python 기반의 가벼운 애플리케이션입니다.
- 간편한 파일 선택 및 변환 과정을 제공합니다.

## 요구 사항

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv): DDS 파일을 PNG 형식으로 변환하는 데 사용됩니다. 애플리케이션과 함께 `assets` 폴더에 제공됩니다.

### Texconv (선택적 다운로드)

프로젝트에 포함된 Texconv가 작동하지 않거나 수동으로 다운로드하려는 경우 다음 방법 중 하나를 사용할 수 있습니다.

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

## 설치

1. 저장소를 복제합니다:
   ```bash
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```
2. 프로젝트 디렉터리로 이동합니다:
   ```bash
   cd "프로젝트 폴더 경로"
   ```
3. 필요한 종속성을 설치합니다:
   ```powershell
   pip install -r requirements.txt
   ```

### 가상 환경 (선택 사항)

Python 종속성을 다른 프로젝트와 분리하여 관리하려면 가상 환경을 사용할 수 있습니다.

1. (PowerShell에서 스크립트 실행 오류가 발생한 경우에만) 현재 세션에서만 스크립트 실행을 임시로 허용합니다:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
2. 가상 환경을 생성합니다:
   ```powershell
   python -m venv .venv
   ```
3. 가상 환경을 활성화합니다:
   ```powershell
   .venv\Scripts\activate
   ```
4. 필요한 종속성을 설치합니다:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. 작업이 끝나면 가상 환경을 종료합니다:
   ```powershell
   deactivate
   ```

## 사용 방법

애플리케이션을 실행합니다:
```bash
python Converter.pyw
```

DDS 파일을 선택하고 화면의 안내에 따라 PNG 형식으로 변환합니다.

## 빌드 (EXE 파일 생성)

Python 애플리케이션을 하나의 EXE 파일로 변환하려면 다음 단계를 따르세요.

**중요:** PowerShell은 관리자 권한이 아닌 일반 사용자 권한으로 실행하세요. 관리자 권한은 필요하지 않습니다.

### 1. PowerShell 열기

1. Windows 시작 메뉴를 엽니다.
2. 검색창에 `PowerShell` 또는 `Windows Terminal`을 입력합니다.
3. Windows PowerShell 또는 Windows Terminal을 일반적으로 실행합니다.
4. '관리자 권한으로 실행' 옵션을 사용하지 마세요.

### 2. 프로젝트 폴더로 이동

PowerShell에 다음 명령어를 입력하여 프로젝트 폴더로 이동합니다:
```powershell
cd "D:\vectorrdevworks\Projeler\Yazılım Projeleri\Python\DDS2PNG"
```

### 3. 애플리케이션 아이콘 삽입

다음 명령어는 `embed_icon.ps1` 스크립트를 실행하여 애플리케이션 아이콘을 Python 파일에 삽입합니다.
```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**참고:** Windows의 실행 정책으로 인해 PowerShell 스크립트 실행이 차단될 수 있으므로 `-ExecutionPolicy Bypass`를 사용합니다. 이 설정은 실행된 PowerShell 프로세스에만 적용됩니다. 시스템 전체의 보안 설정은 변경되지 않습니다.

### 4. PyInstaller로 빌드

아이콘 삽입이 완료되면 다음 명령어를 실행하여 EXE 파일을 생성합니다:
```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.png" --name "DDS2PNG" "Converter.pyw"
```

**명령어 매개변수:**

| 매개변수 | 설명 |
|---|---|
| `--noconfirm` | 확인 메시지 없이 빌드를 수행합니다. |
| `--clean` | 이전 빌드 캐시를 삭제합니다. |
| `--onefile` | 하나의 EXE 파일을 생성합니다. |
| `--windowed` | 콘솔 창을 표시하지 않습니다. |
| `--icon` | EXE 파일의 아이콘을 지정합니다. |
| `--name` | 생성할 EXE 파일의 이름을 지정합니다. |

### 5. 빌드 결과

빌드가 성공적으로 완료되면 EXE 파일이 다음 폴더에 생성됩니다:
```text
dist\Converter.exe
```

**새 버전을 빌드할 때의 순서:**

1. PowerShell을 일반 사용자 권한으로 엽니다.
2. 프로젝트 폴더로 이동합니다.
3. 아이콘 삽입 명령어를 실행합니다.
4. PyInstaller 빌드 명령어를 실행합니다.
5. `dist` 폴더에서 생성된 EXE 파일을 가져옵니다.

## 개발자

**vectordevworks**

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 배포됩니다. 자세한 내용은 LICENSE 파일을 참조하세요.