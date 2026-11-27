<div align="center">

# DDS2PNG

### Конвертер DDS в PNG

Легко преобразуйте текстуры из формата DDS (DirectDraw Surface) в PNG.

Лёгкое и простое в использовании настольное приложение на Python.

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

### 🌐 Выбор языка

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="English"> English</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Deutsch"> Deutsch</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Português"> Português</a> |
<strong><img src="https://flagcdn.com/ru.svg" width="20" alt="Русский"> Русский</strong> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="日本語"> 日本語</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe</a>

---

### 📑 Содержание

<a href="#genel-bakis">Обзор</a>
<a href="#ozellikler">Возможности</a>
<a href="#gereksinimler">Требования</a>
<a href="#kurulum">Установка</a>
<a href="#sanal-ortam">Виртуальное окружение (необязательно)</a>
<a href="#kullanim">Использование</a>
<a href="#derleme">Сборка (создание EXE)</a>
<a href="#gelistirici">Разработчик</a>
<a href="#lisans">Лицензия</a>

</div>

---

<a id="genel-bakis"></a>
## 🔍 Обзор

**DDS2PNG** — это лёгкое настольное приложение на Python, позволяющее преобразовывать текстуры из формата DDS (DirectDraw Surface) в PNG.

Простой графический интерфейс позволяет легко выбирать файлы и выполнять преобразование. Использовать команды командной строки не требуется.

Преобразование выполняется с помощью Microsoft DirectXTex (Texconv).

Инструмент Texconv поставляется вместе с приложением в папке `assets`.

<a id="ozellikler"></a>
## ✨ Возможности

- **Преобразование DDS в PNG:** Конвертирует файлы DDS в формат PNG.
- **Графический интерфейс:** Предоставляет простой интерфейс для выбора и преобразования файлов.
- **Поддержка Texconv:** Использует Microsoft DirectXTex для преобразования файлов DDS.
- **Простота использования:** Позволяет конвертировать файлы без командной строки.

<a id="gereksinimler"></a>
## 📋 Требования

- Windows
- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)

Модули `tkinter`, `ctypes`, `json`, `math`, `os` и `pathlib` входят в стандартную библиотеку Python.

Инструмент Texconv поставляется вместе с приложением в папке `assets`.

### Texconv (Необязательная загрузка)

Если версия Texconv, поставляемая с проектом, не работает или вы хотите загрузить её вручную, воспользуйтесь одним из способов ниже.

**PowerShell (Winget):**

```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Чтобы проверить установку:

```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Ручная загрузка:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

<a id="kurulum"></a>
## 📥 Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Откройте папку проекта.

3. Запустите PowerShell в папке проекта.

4. Установите необходимые пакеты Python:

```powershell
py -m pip install -r requirements.txt
```

<a id="sanal-ortam"></a>
## 🐍 Виртуальное окружение (необязательно)

Виртуальное окружение позволяет отделить зависимости Python от других проектов.

**1. Создать виртуальное окружение:**

```powershell
py -m venv .venv
```

**2. Активировать виртуальное окружение:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Установить необходимые зависимости:**

```powershell
py -m pip install -r requirements.txt
```

**4. После завершения деактивировать виртуальное окружение:**

```powershell
deactivate
```

**Активация через CMD (командную строку):**

Если вы используете CMD вместо PowerShell:

```cmd
.venv\Scripts\activate.bat
```

Чтобы выйти из виртуального окружения:

```cmd
deactivate
```

### Проблемы с активацией виртуального окружения

В некоторых случаях политика выполнения PowerShell может блокировать активацию виртуального окружения.

В этом случае выполните следующую команду:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Затем снова активируйте виртуальное окружение:

```powershell
.\.venv\Scripts\Activate.ps1
```

Эта настройка действует только для текущего сеанса PowerShell. При открытии нового сеанса будут восстановлены настройки по умолчанию.

### Использование виртуального окружения без активации

Активация виртуального окружения необязательна. Если активировать его не удаётся, продолжайте работу, вызывая исполняемые файлы Python и pip напрямую.

**Для установки зависимостей:**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Для запуска приложения:**

```powershell
.\.venv\Scripts\python.exe DDSConverter.pyw
```

**Примечание:** Для создания, активации, установки зависимостей и деактивации виртуального окружения права администратора не требуются. Однако Python должен быть установлен правильно, а у вас должен быть доступ к необходимым файлам.

<a id="kullanim"></a>
## 🚀 Использование

1. Запустите файл `DDSConverter.pyw`:

```powershell
pyw .\DDSConverter.pyw
```

Или выполните:

```powershell
pythonw .\DDSConverter.pyw
```

2. Выберите файл DDS, который требуется преобразовать.

3. В качестве папки вывода можно выбрать существующую папку `convert` или указать любую другую папку.

4. Выполните преобразование в формат PNG.

<a id="derleme"></a>
## 📦 Сборка (создание EXE)

Для упаковки приложения Python в один EXE-файл используется PyInstaller.

### 1. Перейдите в папку проекта

Сначала откройте папку проекта DDS2PNG. Чтобы запустить терминал в этой папке, воспользуйтесь одним из следующих способов.

**Способ 1: Открытие терминала через Проводник**

1. Откройте папку проекта DDS2PNG в Проводнике.

2. Введите `cmd` или `powershell` в адресную строку.

3. Нажмите Enter.

Терминал откроется непосредственно в папке проекта.

**Способ 2: Переход в папку проекта из терминала**

Откройте CMD или PowerShell и выполните подходящую команду ниже.

**CMD:**

```cmd
cd /d "PROJE_KLASORUNUN_YOLU"
```

**PowerShell:**

```powershell
Set-Location -LiteralPath "PROJE_KLASORUNUN_YOLU"
```

Замените `PROJE_KLASORUNUN_YOLU` полным путём к папке проекта DDS2PNG на вашем компьютере.

**Примечание:** Запускать терминал от имени администратора не требуется. Достаточно обычных прав пользователя.

### 2. Сборка EXE

Скрипт `buid.ps1` в папке `scripts` проекта собирает приложение в формате EXE с помощью PyInstaller.

Скрипт сборки автоматически выполняет следующие действия:

- Проверяет необходимые файлы проекта.
- Проверяет наличие установленного PyInstaller.
- Удаляет файлы предыдущих сборок.
- Использует `icon.ico` в качестве значка EXE.
- Добавляет папку `assets` в EXE-файл.
- Проверяет результат сборки.

**Запуск через CMD:**

```cmd
powershell -ExecutionPolicy Bypass -File "scripts\buid.ps1"
```

**Запуск через PowerShell:**

```powershell
.\scripts\buid.ps1
```

### 3. Результат сборки

После успешного завершения сборки EXE-файл будет создан по следующему пути:

```text
dist\DDS2PNG.exe
```

**Шаги для сборки новой версии:**

1. Откройте папку проекта DDS2PNG.

2. Запустите терминал, введя `cmd` или `powershell` в адресной строке, либо перейдите в папку проекта из уже открытого терминала.

3. Запустите скрипт сборки.

4. Созданный EXE-файл будет находиться в папке `dist`.

### 4. Запуск приложения

После успешной сборки используйте следующую команду для запуска приложения:

```powershell
dist\DDS2PNG.exe
```

Также можно открыть папку `dist` и дважды щёлкнуть `DDS2PNG.exe`.

**Примечание:** Для запуска приложения не требуется открывать CMD или PowerShell от имени администратора.

<a id="gelistirici"></a>
## 👨‍💻 Разработчик

<div align="center">

**VectorDevWorks**

<a href="https://github.com/vectordevworks">
  <img src="https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github" alt="VectorDevWorks GitHub">
</a>

</div>

<a id="lisans"></a>
## 📄 Лицензия

Проект распространяется по лицензии MIT. Подробности см. в файле `LICENSE` в репозитории проекта.

---

<div align="center">

**Разработано VectorDevWorks.**

⭐ Если проект вам понравился, не забудьте поставить ему звезду на GitHub!

<a href="https://github.com/vectordevworks/DDS2PNG">
  <img src="https://img.shields.io/badge/Project%20Repository-DDS2PNG-blue?style=for-the-badge&logo=github" alt="DDS2PNG Repository">
</a>

</div>
