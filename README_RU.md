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
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Русский"> Русский
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
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Японский"> Японский
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Упрощённый китайский"> Упрощённый китайский
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Турецкий"> Турецкий
</a>

Лёгкий инструмент для преобразования DDS в PNG, разработанный на Python и оснащённый простым графическим интерфейсом.

## Обзор

DDS to PNG Converter — это настольное приложение, предназначенное для преобразования файлов текстур в формате DDS (DirectDraw Surface) в изображения PNG с помощью интуитивно понятного графического интерфейса.

Цель проекта — предоставить пользователям простой и удобный способ преобразования файлов текстур без необходимости использовать команды командной строки.

## Возможности

- Преобразование файлов DDS в формат PNG.
- Простой и удобный графический интерфейс.
- Лёгкое приложение на основе Python.
- Удобный выбор файлов и простой процесс преобразования.

## Требования

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv): используется для преобразования файлов DDS в формат PNG. Поставляется вместе с приложением в папке `assets`.

### Texconv (Необязательная загрузка)

Если поставляемая вместе с проектом версия Texconv не работает или вы хотите загрузить её вручную, воспользуйтесь одним из следующих способов.

**PowerShell (Winget):**
```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Проверка установки:
```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Ручная загрузка:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```
2. Перейдите в каталог проекта:
   ```bash
   cd "ПУТЬ К ПАПКЕ ПРОЕКТА"
   ```
3. Установите необходимые зависимости:
   ```powershell
   pip install -r requirements.txt
   ```

### Виртуальное окружение (Необязательно)

Вы можете использовать виртуальное окружение, чтобы изолировать зависимости Python от других проектов.

1. (Только если PowerShell сообщает об ошибке выполнения скрипта) Временно разрешите выполнение скриптов для текущего сеанса:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
2. Создайте виртуальное окружение:
   ```powershell
   python -m venv .venv
   ```
3. Активируйте виртуальное окружение:
   ```powershell
   .venv\Scripts\activate
   ```
4. Установите необходимые зависимости:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. После завершения работы выйдите из виртуального окружения:
   ```powershell
   deactivate
   ```

## Использование

Запустите приложение:
```bash
python DDSConverter.pyw
```

Выберите DDS-файл и следуйте инструкциям на экране, чтобы преобразовать его в формат PNG.

## Сборка (Создание EXE)

Выполните следующие шаги, чтобы преобразовать Python-приложение в один EXE-файл.

**Важно:** Запускайте PowerShell от имени обычного пользователя, а не администратора. Права администратора не требуются.

### 1. Открытие PowerShell

1. Откройте меню «Пуск» Windows.
2. Введите `PowerShell` или `Windows Terminal` в строке поиска.
3. Обычным способом откройте Windows PowerShell или Windows Terminal.
4. Не используйте параметр «Запуск от имени администратора».

### 2. Переход в папку проекта

Введите следующую команду в PowerShell, чтобы перейти в папку проекта:
```powershell
   cd "ПУТЬ К ПАПКЕ ПРОЕКТА"
```

### 3. Встраивание значка приложения

Следующая команда запускает скрипт `embed_icon.ps1`, который встраивает значок приложения в файл Python.
```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Примечание:** Параметр `-ExecutionPolicy Bypass` используется, поскольку политика выполнения Windows может блокировать запуск скриптов PowerShell. Эта настройка действует только для запущенного процесса PowerShell. Системные параметры безопасности не изменяются.

### 4. Сборка с помощью PyInstaller

После завершения встраивания значка выполните следующую команду, чтобы создать EXE-файл:
```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.png" --name "DDS2PNG" "DDSConverter.pyw"
```

**Параметры команды:**

| Параметр | Описание |
|---|---|
| `--noconfirm` | Выполняет сборку без запроса подтверждения. |
| `--clean` | Очищает кэш предыдущих сборок. |
| `--onefile` | Создаёт один EXE-файл. |
| `--windowed` | Не отображает окно консоли. |
| `--icon` | Задаёт значок EXE-файла. |
| `--name` | Задаёт имя создаваемого EXE-файла. |

### 5. Результат сборки

После успешного завершения сборки EXE-файл будет создан в следующей папке:
```text
dist\DDSConverter.exe
```

**Порядок действий при сборке новой версии:**

1. Откройте PowerShell от имени обычного пользователя.
2. Перейдите в папку проекта.
3. Выполните команду встраивания значка.
4. Выполните команду сборки PyInstaller.
5. Возьмите созданный EXE-файл из папки `dist`.

## Разработчик

**vectordevworks**

## Лицензия

Проект распространяется по лицензии MIT. Подробности см. в файле LICENSE.