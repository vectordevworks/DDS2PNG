# Convertidor de DDS a PNG

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="Inglés"> Inglés
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="Alemán"> Alemán
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Francés"> Francés
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Ruso"> Ruso
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Coreano"> Coreano
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Portugués"> Portugués
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japonés"> Japonés
</a>
|
<a href="README_ZH-CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Chino simplificado"> Chino simplificado
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Turco"> Turco
</a>

Una herramienta ligera de conversión de DDS a PNG, desarrollada en Python y equipada con una interfaz gráfica sencilla.

## Descripción general

DDS to PNG Converter es una aplicación de escritorio diseñada para convertir archivos de texturas en formato DDS (DirectDraw Surface) a imágenes PNG mediante una interfaz gráfica intuitiva.

El objetivo del proyecto es facilitar la conversión de archivos de texturas sin que los usuarios tengan que utilizar comandos de línea de comandos.

## Características

- Convierte archivos DDS al formato PNG.
- Interfaz gráfica sencilla y fácil de usar.
- Aplicación ligera desarrollada en Python.
- Selección de archivos y proceso de conversión sencillos.

## Requisitos

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv): se utiliza para convertir archivos DDS al formato PNG. Se incluye con la aplicación en la carpeta `assets`.

### Texconv (descarga opcional)

Si la versión de Texconv incluida en el proyecto no funciona o prefiere descargarla manualmente, puede utilizar cualquiera de los siguientes métodos.

**PowerShell (Winget):**
```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Para comprobar la instalación:
```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Descarga manual:**

[Versiones de Microsoft DirectXTex](https://github.com/microsoft/DirectXTex/releases)

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

### Entorno virtual (opcional)

Puede utilizar un entorno virtual para mantener las dependencias de Python separadas de las de otros proyectos.

1. (Solo si PowerShell muestra un error al ejecutar scripts) Permita temporalmente la ejecución de scripts durante la sesión actual:
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

## Uso

Ejecute la aplicación:
```bash
python DDSConverter.pyw
```

Seleccione su archivo DDS y siga las instrucciones que aparecen en pantalla para convertirlo al formato PNG.

## Compilación (creación del archivo EXE)

Siga los pasos que se indican a continuación para empaquetar la aplicación Python en un único archivo EXE.

**Importante:** Ejecute PowerShell como usuario normal, no como administrador. No se necesitan permisos de administrador.

### 1. Abrir PowerShell

1. Abra el menú Inicio de Windows.
2. Escriba `PowerShell` o `Windows Terminal` en el cuadro de búsqueda.
3. Abra Windows PowerShell o Windows Terminal normalmente.
4. No utilice la opción «Ejecutar como administrador».

### 2. Acceder a la carpeta del proyecto

Introduzca el siguiente comando en PowerShell para acceder a la carpeta del proyecto:
```powershell
cd "RUTA DE LA CARPETA DEL PROYECTO"
```

### 3. Incrustar el icono de la aplicación

El siguiente comando ejecuta el script `embed_icon.ps1` para incrustar el icono de la aplicación en el archivo Python.
```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Nota:** Se utiliza el parámetro `-ExecutionPolicy Bypass` porque la directiva de ejecución de Windows puede impedir que se ejecuten scripts de PowerShell. Esta configuración solo se aplica al proceso de PowerShell iniciado y no modifica la configuración de seguridad de todo el sistema.

### 4. Compilar con PyInstaller

Una vez incrustado el icono, ejecute el siguiente comando para crear el archivo EXE:
```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.png" --name "DDS2PNG" "DDSConverter.pyw"
```

**Parámetros del comando:**

| Parámetro | Descripción |
|---|---|
| `--noconfirm` | Realiza la compilación sin solicitar confirmación. |
| `--clean` | Limpia la caché de compilaciones anteriores. |
| `--onefile` | Crea un único archivo EXE. |
| `--windowed` | Oculta la ventana de la consola. |
| `--icon` | Establece el icono del archivo EXE. |
| `--name` | Define el nombre del archivo EXE que se va a crear. |

### 5. Resultado de la compilación

Cuando la compilación finalice correctamente, el archivo EXE se creará en la siguiente carpeta:
```text
dist\DDSConverter.exe
```

**Orden de los pasos para compilar una nueva versión:**

1. Abra PowerShell como usuario normal.
2. Acceda a la carpeta del proyecto.
3. Ejecute el comando para incrustar el icono.
4. Ejecute el comando de compilación de PyInstaller.
5. Obtenga el archivo EXE generado en la carpeta `dist`.

## Desarrollador

**vectordevworks**

## Licencia

Este proyecto está publicado bajo la licencia MIT. Para obtener más información, consulte el archivo [LICENSE](LICENSE).
