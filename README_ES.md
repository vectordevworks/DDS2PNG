<div align="center">

# DDS2PNG

### Convertidor de DDS a PNG

Convierte fácilmente archivos de texturas en formato DDS (DirectDraw Surface) a PNG.

Una aplicación de escritorio ligera y fácil de usar, desarrollada con Python.

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

### 🌐 Selección de idioma

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="English"> English</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Deutsch"> Deutsch</a> |
<strong><img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español</strong> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Português"> Português</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Русский"> Русский</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="日本語"> 日本語</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe</a>

---

### 📑 Tabla de contenidos

<a href="#genel-bakis">Descripción general</a>
<a href="#ozellikler">Características</a>
<a href="#gereksinimler">Requisitos</a>
<a href="#kurulum">Instalación</a>
<a href="#sanal-ortam">Entorno virtual (opcional)</a>
<a href="#kullanim">Uso</a>
<a href="#derleme">Compilación (crear EXE)</a>
<a href="#gelistirici">Desarrollador</a>
<a href="#lisans">Licencia</a>

</div>

---

<a id="genel-bakis"></a>
## 🔍 Descripción general

**DDS2PNG** es una aplicación de escritorio ligera basada en Python que permite convertir archivos de texturas en formato DDS (DirectDraw Surface) a PNG.

Su sencilla interfaz gráfica permite seleccionar archivos y convertirlos fácilmente. No es necesario utilizar comandos de la línea de comandos.

Las conversiones se realizan mediante Microsoft DirectXTex (Texconv).

La herramienta Texconv se incluye con la aplicación en la carpeta `assets`.

<a id="ozellikler"></a>
## ✨ Características

- **Conversión de DDS a PNG:** Convierte archivos DDS al formato PNG.
- **Interfaz gráfica:** Ofrece una interfaz sencilla para seleccionar y convertir archivos.
- **Compatibilidad con Texconv:** Utiliza Microsoft DirectXTex para convertir archivos DDS.
- **Fácil de usar:** Permite convertir archivos sin utilizar la línea de comandos.

<a id="gereksinimler"></a>
## 📋 Requisitos

- Windows
- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)

Los módulos `tkinter`, `ctypes`, `json`, `math`, `os` y `pathlib` forman parte de la biblioteca estándar de Python.

La herramienta Texconv se incluye con la aplicación en la carpeta `assets`.

### Texconv (Descarga opcional)

Si la versión de Texconv incluida en el proyecto no funciona o desea descargarla manualmente, puede utilizar los métodos siguientes.

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

<a id="kurulum"></a>
## 📥 Instalación

1. Clone el repositorio:

```bash
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Abra la carpeta del proyecto.

3. Inicie PowerShell en la carpeta del proyecto.

4. Instale los paquetes de Python necesarios:

```powershell
py -m pip install -r requirements.txt
```

<a id="sanal-ortam"></a>
## 🐍 Entorno virtual (opcional)

Puede utilizar un entorno virtual para mantener las dependencias de Python separadas de otros proyectos.

**1. Crear un entorno virtual:**

```powershell
py -m venv .venv
```

**2. Activar el entorno virtual:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Instalar las dependencias necesarias:**

```powershell
py -m pip install -r requirements.txt
```

**4. Desactivar el entorno virtual cuando termine:**

```powershell
deactivate
```

**Activación mediante CMD (símbolo del sistema):**

Si utiliza CMD en lugar de PowerShell:

```cmd
.venv\Scripts\activate.bat
```

Para salir del entorno virtual:

```cmd
deactivate
```

### Problemas al activar el entorno virtual

En algunos casos, PowerShell puede impedir la activación del entorno virtual debido a la directiva de ejecución.

En ese caso, ejecute el siguiente comando:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

A continuación, vuelva a activar el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Esta configuración solo se aplica a la sesión actual de PowerShell. Al abrir una nueva sesión, se restaurarán los valores predeterminados.

### Usar el entorno virtual sin activarlo

No es obligatorio activar el entorno virtual. Si la activación falla, puede seguir utilizándolo llamando directamente a los ejecutables de Python y pip.

**Para instalar las dependencias:**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Para ejecutar la aplicación:**

```powershell
.\.venv\Scripts\python.exe DDSConverter.pyw
```

**Nota:** No se necesitan permisos de administrador para crear, activar, instalar dependencias o desactivar el entorno virtual. Sin embargo, Python debe estar instalado correctamente y debe tener permiso para acceder a los archivos necesarios.

<a id="kullanim"></a>
## 🚀 Uso

1. Ejecute el archivo `DDSConverter.pyw`:

```powershell
pyw .\DDSConverter.pyw
```

Como alternativa:

```powershell
pythonw .\DDSConverter.pyw
```

2. Seleccione el archivo DDS que desea convertir.

3. Puede elegir la carpeta `convert` existente como carpeta de salida o seleccionar cualquier otra carpeta.

4. Realice la conversión al formato PNG.

<a id="derleme"></a>
## 📦 Compilación (crear EXE)

Se utiliza PyInstaller para empaquetar la aplicación Python en un único archivo EXE.

### 1. Acceder a la carpeta del proyecto

Primero, abra la carpeta del proyecto DDS2PNG. Puede utilizar uno de los siguientes métodos para abrir un terminal en dicha carpeta.

**Método 1: Abrir un terminal desde el Explorador de archivos**

1. Abra la carpeta del proyecto DDS2PNG en el Explorador de archivos.

2. Escriba `cmd` o `powershell` en la barra de direcciones.

3. Pulse Intro.

El terminal se abrirá directamente en la carpeta del proyecto.

**Método 2: Acceder a la carpeta del proyecto desde el terminal**

Abra CMD o PowerShell y utilice el comando correspondiente de los siguientes.

**CMD:**

```cmd
cd /d "PROJE_KLASORUNUN_YOLU"
```

**PowerShell:**

```powershell
Set-Location -LiteralPath "PROJE_KLASORUNUN_YOLU"
```

Sustituya `PROJE_KLASORUNUN_YOLU` por la ruta completa de la carpeta del proyecto DDS2PNG en su equipo.

**Nota:** No es necesario ejecutar el terminal como administrador. Los permisos de usuario normales son suficientes.

### 2. Compilar el EXE

El script `buid.ps1`, ubicado en la carpeta `scripts` del proyecto, compila la aplicación en formato EXE mediante PyInstaller.

El script de compilación realiza automáticamente las siguientes tareas:

- Comprueba los archivos necesarios del proyecto.
- Comprueba la instalación de PyInstaller.
- Limpia los archivos de compilaciones anteriores.
- Utiliza `icon.ico` como icono del EXE.
- Incluye la carpeta `assets` en el archivo EXE.
- Comprueba el resultado de la compilación.

**Ejecutar mediante CMD:**

```cmd
powershell -ExecutionPolicy Bypass -File "scripts\buid.ps1"
```

**Ejecutar mediante PowerShell:**

```powershell
.\scripts\buid.ps1
```

### 3. Resultado de la compilación

Cuando la compilación finalice correctamente, el archivo EXE se creará en la siguiente ubicación:

```text
dist\DDS2PNG.exe
```

**Pasos para compilar una nueva versión:**

1. Abra la carpeta del proyecto DDS2PNG.

2. Abra un terminal escribiendo `cmd` o `powershell` en la barra de direcciones, o acceda a la carpeta del proyecto desde un terminal existente.

3. Ejecute el script de compilación.

4. Encontrará el archivo EXE generado en la carpeta `dist`.

### 4. Ejecutar la aplicación

Una vez finalizada correctamente la compilación, utilice el siguiente comando para ejecutar la aplicación:

```powershell
dist\DDS2PNG.exe
```

También puede abrir la carpeta `dist` y hacer doble clic en `DDS2PNG.exe`.

**Nota:** No es necesario abrir CMD ni PowerShell como administrador para ejecutar la aplicación.

<a id="gelistirici"></a>
## 👨‍💻 Desarrollador

<div align="center">

**VectorDevWorks**

<a href="https://github.com/vectordevworks">
  <img src="https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github" alt="VectorDevWorks GitHub">
</a>

</div>

<a id="lisans"></a>
## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulte el archivo `LICENSE` del repositorio para obtener más información.

---

<div align="center">

**Desarrollado por VectorDevWorks.**

⭐ Si le gusta el proyecto, ¡no olvide darle una estrella en GitHub!

<a href="https://github.com/vectordevworks/DDS2PNG">
  <img src="https://img.shields.io/badge/Project%20Repository-DDS2PNG-blue?style=for-the-badge&logo=github" alt="DDS2PNG Repository">
</a>

</div>
