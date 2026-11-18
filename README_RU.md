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

Легкий инструмент для преобразования DDS в PNG на Python с простым графическим интерфейсом.

## Обзор

DDS to PNG Converter — это настольное приложение, предназначенное для преобразования текстурных файлов в формате DDS (DirectDraw Surface) в изображения PNG с помощью интуитивно понятного графического интерфейса.

Цель проекта — предоставить пользователям простой и удобный способ преобразования текстурных файлов без необходимости использования командной строки.

## Возможности

- Преобразование файлов DDS в формат PNG.
- Простой и удобный графический интерфейс.
- Легкое приложение на основе Python.
- Удобный выбор файлов и процесс преобразования.

## Требования

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv): Используется для преобразования файлов DDS в формат PNG. Входит в состав приложения и находится в папке `assets`.

### Texconv (Необязательная загрузка)

Если версия Texconv, поставляемая вместе с проектом, не работает или вы предпочитаете скачать её вручную, воспользуйтесь следующими способами.

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

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
   ```
2. Перейдите в каталог проекта:
   ```
   cd "ПУТЬ К КАТАЛОГУ ПРОЕКТА"
   ```
3. Установите необходимые зависимости:
   ```
   pip install -r requirements.txt
   ```

### Виртуальное окружение (Необязательно)

Вы можете использовать виртуальное окружение, чтобы отделить зависимости Python от других проектов.

1. Создайте виртуальное окружение:
   ```
   python -m venv .venv
   ```
2. Активируйте виртуальное окружение:
   ```
   .venv\Scripts\activate
   ```
3. Установите необходимые зависимости:
   ```
   python -m pip install -r requirements.txt
   ```

**Примечание:** Для установки и управления зависимостями достаточно запускать PowerShell или командную строку (CMD) от имени обычного пользователя. Права администратора не требуются.

Если `pip` выдаёт ошибку доступа при попытке записи в системный каталог Python, рекомендуется использовать виртуальное окружение (`venv`), а не запускать терминал от имени администратора.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
   ```

2. Перейдите в каталог проекта:

   ```bash
   cd "ПУТЬ К ПАПКЕ ПРОЕКТА"
   ```

## Использование

Запустите приложение:

```bash
python Converter.pyw
```

Выберите файл DDS и следуйте инструкциям на экране, чтобы преобразовать его в формат PNG.

## Сборка (Создание EXE)

Выполните следующие шаги, чтобы преобразовать приложение Python в один EXE-файл.

**Важно:** Запускайте PowerShell от имени обычного пользователя, а не администратора. Права администратора не требуются.

### 1. Открытие PowerShell

1. Откройте меню «Пуск» Windows.
2. Введите `PowerShell` или `Windows Terminal` в поле поиска.
3. Откройте Windows PowerShell или Windows Terminal обычным способом.
4. Не выбирайте параметр «Запуск от имени администратора».

### 2. Переход в каталог проекта

Введите следующую команду в PowerShell, чтобы перейти в каталог проекта:

```powershell
cd "D:\vectorrdevworks\Projeler\Yazılım Projeleri\Python\DDS-to-PNG-Converter"
```

### 3. Встраивание значка приложения

Следующая команда запускает скрипт `embed_icon.ps1` и встраивает значок приложения в файл Python.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Примечание:** Параметр `-ExecutionPolicy Bypass` используется, поскольку политика выполнения Windows может блокировать запуск сценариев PowerShell. Эта настройка применяется только к запущенному процессу PowerShell. Системные параметры безопасности не изменяются.

### 4. Сборка с помощью PyInstaller

После встраивания значка выполните следующую команду, чтобы создать EXE-файл:

```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.ico" --name "DDS-to-PNG-Converter" "Converter.pyw"
```

**Параметры команды:**

| Параметр      | Описание                                    |
| ------------- | ------------------------------------------- |
| `--noconfirm` | Выполняет сборку без запроса подтверждения. |
| `--clean`     | Очищает кэш предыдущей сборки.              |
| `--onefile`   | Создает один EXE-файл.                      |
| `--windowed`  | Скрывает окно консоли.                      |
| `--icon`      | Задает значок EXE-файла.                    |
| `--name`      | Задает имя создаваемого EXE-файла.          |

### 5. Результат сборки

После успешного завершения сборки EXE-файл будет создан в следующем каталоге:

```text
dist\DDS-to-PNG-Converter.exe
```

**Порядок действий при сборке новой версии:**

1. Откройте PowerShell от имени обычного пользователя.
2. Перейдите в каталог проекта.
3. Выполните команду встраивания значка.
4. Выполните команду сборки PyInstaller.
5. Найдите созданный EXE-файл в каталоге `dist`.

## Разработчик

**vectordevworks**

## Лицензия

Этот проект распространяется по лицензии MIT. Подробности приведены в файле [LICENSE](LICENSE).
