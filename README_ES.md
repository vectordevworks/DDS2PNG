# DDS2PNG

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="Inglés"> Inglés
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="Alemán"> Alemán
</a>
|
<strong>
  <img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español
</strong>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Francés"> Francés
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japonés"> Japonés
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
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Ruso"> Ruso
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Chino simplificado"> Chino simplificado
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Turco"> Turco
</a>

Convertidor de DDS a PNG es una aplicación de escritorio ligera, basada en Python, que permite convertir archivos de textura en formato DDS (DirectDraw Surface) a imágenes PNG. Su sencilla interfaz gráfica permite seleccionar archivos y realizar conversiones fácilmente.

## Descripción general

La aplicación convierte archivos de textura DDS al formato PNG mediante Microsoft DirectXTex (Texconv). La conversión se realiza desde una interfaz gráfica, por lo que no es necesario utilizar comandos de la línea de comandos.

La herramienta Texconv se incluye con la aplicación en la carpeta `assets`.

## Características

- **Conversión de DDS a PNG:** Convierte archivos DDS al formato PNG.

- **Interfaz gráfica:** Ofrece una interfaz sencilla que facilita la selección de archivos y la conversión.

- **Compatibilidad con Texconv:** Utiliza la herramienta Microsoft DirectXTex para convertir archivos DDS.

- **Fácil de usar:** Permite realizar conversiones sin utilizar la línea de comandos.


## Requisitos

- Windows

- Python 3.x

- Pillow

- Microsoft DirectXTex (Texconv)


Los módulos `tkinter`, `ctypes`, `json`, `math`, `os` y `pathlib` forman parte de la biblioteca estándar de Python.

Texconv se utiliza para convertir archivos DDS al formato PNG y se incluye con la aplicación en la carpeta `assets`.

### Texconv (Descarga opcional)

Si la versión de Texconv incluida con el proyecto no funciona o desea descargarla manualmente, puede utilizar los métodos siguientes.

**PowerShell (Winget):**

```
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Para comprobar la instalación:

```
winget list --id Microsoft.DirectXTex.Texconv
```

**Descarga manual:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Instalación

1. Clona el repositorio:

```
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Abre la carpeta del proyecto.

3. Inicia PowerShell en esta carpeta.

4. Instala los paquetes de Python necesarios:

```
py -m pip install -r requirements.txt
```

## Entorno virtual (opcional)

Puedes utilizar un entorno virtual para mantener las dependencias de Python separadas de otros proyectos:

1. Crea un entorno virtual:

```
py -m venv .venv
```

2. Activa el entorno virtual:

```
.\.venv\Scripts\Activate.ps1
```

3. Instala los paquetes de Python necesarios:

```
py -m pip install -r requirements.txt
```

4. Cuando termines, desactiva el entorno virtual:

```
deactivate
```

## Uso

1. Ejecuta el archivo `DDSConverter.pyw`:

```
pyw .\DDSConverter.pyw
```

Como alternativa:

```
pythonw .\DDSConverter.pyw
```

2. Selecciona el archivo DDS que deseas convertir.

3. Puedes seleccionar la carpeta `convert` existente como carpeta de salida o elegir cualquier otra carpeta.

4. Realiza la conversión al formato PNG.

## Compilación (crear EXE)

Se utiliza PyInstaller para convertir la aplicación Python en un único archivo EXE.

### 1. Acceder a la carpeta del proyecto

Abre PowerShell en la carpeta del proyecto.

### 2. Incrustar el icono y las imágenes de idioma

Ejecuta el script `embed_icon.ps1` mediante el siguiente comando. Este script incrusta en el archivo Python el icono de la aplicación y las imágenes PNG utilizadas para seleccionar el idioma.

```
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Nota:** El parámetro `-ExecutionPolicy Bypass` se utiliza cuando la política de ejecución de Windows puede impedir que se ejecuten scripts de PowerShell. Este parámetro solo se aplica al proceso de PowerShell que se inicia y no modifica la configuración de seguridad de todo el sistema.

### 3. Resultado de la compilación

Cuando la compilación finalice correctamente, el archivo EXE se creará en la siguiente ubicación:

```
dist\DDS2PNG.exe
```

**Pasos para compilar una nueva versión:**

1. Abre PowerShell.

2. Asegúrate de que PyInstaller esté instalado.

3. Accede a la carpeta del proyecto.

4. Ejecuta el script de compilación.

5. Puedes encontrar el archivo EXE generado en la carpeta `dist`.

## Desarrollador

**vectordevworks**

## Licencia

Este proyecto está distribuido bajo la Licencia MIT. Consulta el archivo `LICENSE` del repositorio del proyecto para obtener más información.
