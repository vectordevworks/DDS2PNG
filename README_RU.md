# Конвертер DDS в PNG

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="Английский"> Английский
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="Немецкий"> Немецкий
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="Испанский"> Испанский
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Французский"> Французский
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Японский"> Японский
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Корейский"> Корейский
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Португальский"> Португальский
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Русский"> Русский
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Упрощённый китайский"> Упрощённый китайский
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Турецкий"> Турецкий
</a>

Конвертер DDS в PNG — это лёгкое настольное приложение на Python, предназначенное для преобразования текстурных файлов формата DDS (DirectDraw Surface) в изображения PNG. Простой графический интерфейс позволяет легко выбирать файлы и выполнять преобразование.

## Обзор

Приложение преобразует текстурные файлы DDS в формат PNG с помощью Microsoft DirectXTex (Texconv). Преобразование выполняется через графический интерфейс, поэтому использовать команды командной строки не требуется.

Инструмент Texconv поставляется вместе с приложением в папке `assets`.

## Возможности

- **Преобразование DDS в PNG:** Преобразует файлы DDS в формат PNG.

- **Графический интерфейс:** Предоставляет простой интерфейс для выбора файлов и выполнения преобразования.

- **Поддержка Texconv:** Использует инструмент Microsoft DirectXTex для преобразования файлов DDS.

- **Простота использования:** Позволяет выполнять преобразование без командной строки.


## Требования

- Windows

- Python 3.x

- Pillow

- Microsoft DirectXTex (Texconv)


Модули `tkinter`, `ctypes`, `json`, `math`, `os` и `pathlib` входят в стандартную библиотеку Python.

Texconv используется для преобразования файлов DDS в формат PNG и поставляется вместе с приложением в папке `assets`.

### Texconv (Texconv (необязательная загрузка))

Если версия Texconv, включённая в проект, не работает или вы хотите загрузить её вручную, воспользуйтесь одним из способов ниже.

**PowerShell (Winget):**

```
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Чтобы проверить установку:

```
winget list --id Microsoft.DirectXTex.Texconv
```

**Ручная загрузка:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Откройте папку проекта.

3. Запустите PowerShell в этой папке.

4. Установите необходимые пакеты Python:

```
py -m pip install -r requirements.txt
```

## Виртуальное окружение (необязательно)

Вы можете использовать виртуальное окружение, чтобы отделить зависимости Python от других проектов:

1. Создайте виртуальное окружение:

```
py -m venv .venv
```

2. Активируйте виртуальное окружение:

```
.\.venv\Scripts\Activate.ps1
```

3. Установите необходимые пакеты Python:

```
py -m pip install -r requirements.txt
```

4. После завершения работы деактивируйте виртуальное окружение:

```
deactivate
```

## Использование

1. Запустите файл `DDSConverter.pyw`:

```
pyw .\DDSConverter.pyw
```

Также можно использовать:

```
pythonw .\DDSConverter.pyw
```

2. Выберите DDS-файл, который хотите преобразовать.

3. В качестве выходной папки можно выбрать существующую папку `convert` или указать любую другую папку.

4. Выполните преобразование в формат PNG.

## Сборка (создание EXE)

Для преобразования Python-приложения в один EXE-файл используется PyInstaller.

### 1. Переход в папку проекта

Откройте PowerShell в папке проекта.

### 2. Встраивание значка и изображений языков

Запустите скрипт `embed_icon.ps1` с помощью следующей команды. Скрипт встраивает значок приложения и PNG-изображения, используемые для выбора языка, в файл Python.

```
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Примечание:** Параметр `-ExecutionPolicy Bypass` используется в случаях, когда политика выполнения Windows может препятствовать запуску сценариев PowerShell. Этот параметр действует только для запускаемого процесса PowerShell и не изменяет общесистемные параметры безопасности.

### 3. Результат сборки

После успешного завершения сборки EXE-файл будет создан по следующему пути:

```
dist\DDS2PNG.exe
```

**Порядок сборки новой версии:**

1. Откройте PowerShell.

2. Убедитесь, что PyInstaller установлен.

3. Перейдите в папку проекта.

4. Запустите сценарий сборки.

5. Созданный EXE-файл можно найти в папке `dist`.

## Разработчик

**vectordevworks**

## Лицензия

Проект распространяется по лицензии MIT. Подробности см. в файле `LICENSE` в репозитории проекта.
