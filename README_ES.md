# Convertidor de DDS a PNG

[🇬🇧 English](README.md) | [🇩🇪 Deutsch](README_DE.md) | [🇪🇸 Español](README_ES.md) | [🇫🇷 Français](README_FR.md) | [🇯🇵 日本語](README_JA.md) | [🇰🇷 한국어](README_KO.md) | [🇵🇹 Português](README_PT.md) | [🇷🇺 Русский](README_RU.md) | [🇨🇳 简体中文](README_ZH-CN.md) | [🇹🇷 Türkçe](README_TR.md)

Una herramienta ligera de conversión de DDS a PNG basada en Python y equipada con una interfaz gráfica sencilla.

## Descripción general

DDS to PNG Converter es una aplicación de escritorio diseñada para convertir archivos de texturas en formato DDS (DirectDraw Surface) a imágenes PNG mediante una interfaz gráfica intuitiva.

El objetivo del proyecto es permitir a los usuarios convertir archivos de texturas de forma fácil y práctica, sin tener que utilizar comandos de línea de comandos.

## Características

- Conversión de archivos DDS al formato PNG.
- Interfaz gráfica sencilla y fácil de usar.
- Aplicación ligera basada en Python.
- Selección de archivos y proceso de conversión sencillos.

## Requisitos

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv): se utiliza para convertir archivos DDS al formato PNG. Se incluye con la aplicación en la carpeta `assets`.

### Texconv (Descarga opcional)

Si la versión de Texconv incluida con el proyecto no funciona o desea descargarla manualmente, puede utilizar uno de los siguientes métodos.

**PowerShell (Winget):**
```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Para comprobar la instalación:
```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Descarga manual:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Instalación

1. Clone el repositorio:
   ```bash
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```
2. Acceda al directorio del proyecto:
   ```bash
   cd "RUTA DE LA CARPETA DEL PROYECTO"
   ```
3. Instale las dependencias necesarias:
   ```powershell
   pip install -r requirements.txt
   ```

### Entorno virtual (Opcional)

Puede utilizar un entorno virtual para mantener las dependencias de Python separadas de las de otros proyectos.

1. (Solo si PowerShell muestra un error al ejecutar el script) Permita temporalmente la ejecución de scripts en la sesión actual:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
2. Cree un entorno virtual:
   ```powershell
   python -m venv .venv
   ```
3. Active el entorno virtual:
   ```powershell
   .venv\Scripts\activate
   ```
4. Instale las dependencias necesarias:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. Cuando termine, salga del entorno virtual:
   ```powershell
   deactivate
   ```

## Instalación

1. Clone el repositorio:
   ```bash
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
   ```
2. Acceda al directorio del proyecto:
   ```bash
   cd "RUTA DE LA CARPETA DEL PROYECTO"
   ```

## Uso

Ejecute la aplicación:
```bash
python Converter.pyw
```

Seleccione su archivo DDS y siga las instrucciones en pantalla para convertirlo al formato PNG.

## Compilación (Crear un EXE)

Siga los pasos que se indican a continuación para convertir la aplicación Python en un único archivo EXE.

**Importante:** Abra PowerShell como usuario normal, no como administrador. No se necesitan permisos de administrador.

### 1. Abrir PowerShell

1. Abra el menú Inicio de Windows.
2. Escriba `PowerShell` o `Windows Terminal` en el cuadro de búsqueda.
3. Abra Windows PowerShell o Windows Terminal normalmente.
4. No utilice la opción «Ejecutar como administrador».

### 2. Acceder a la carpeta del proyecto

Introduzca el siguiente comando en PowerShell para acceder a la carpeta del proyecto:
```powershell
cd "D:\vectorrdevworks\Projeler\Yazılım Projeleri\Python\DDS-to-PNG-Converter"
```

### 3. Incrustar el icono de la aplicación

El siguiente comando ejecuta el script `embed_icon.ps1` para incrustar el icono de la aplicación en el archivo Python.
```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Nota:** Se utiliza `-ExecutionPolicy Bypass` porque la política de ejecución de Windows puede impedir la ejecución de scripts de PowerShell. Esta configuración solo se aplica al proceso de PowerShell iniciado. No se modifican los ajustes de seguridad de todo el sistema.

### 4. Compilar con PyInstaller

Una vez incrustado el icono, ejecute el siguiente comando para crear el archivo EXE:
```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.ico" --name "DDS-to-PNG-Converter" "Converter.pyw"
```

**Parámetros del comando:**

| Parámetro | Descripción |
|---|---|
| `--noconfirm` | Realiza la compilación sin solicitar confirmación. |
| `--clean` | Limpia la caché de compilaciones anteriores. |
| `--onefile` | Crea un único archivo EXE. |
| `--windowed` | No muestra una ventana de consola. |
| `--icon` | Establece el icono del archivo EXE. |
| `--name` | Establece el nombre del archivo EXE que se creará. |

### 5. Resultado de la compilación

Cuando la compilación finalice correctamente, el archivo EXE se creará en la siguiente carpeta:
```text
dist\DDS-to-PNG-Converter.exe
```

**Orden de los pasos al compilar una nueva versión:**

1. Abra PowerShell como usuario normal.
2. Acceda a la carpeta del proyecto.
3. Ejecute el comando para incrustar el icono.
4. Ejecute el comando de compilación de PyInstaller.
5. Obtenga el archivo EXE generado de la carpeta `dist`.

## Desarrollador

**vectordevworks**

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulte el archivo LICENSE para obtener más información.