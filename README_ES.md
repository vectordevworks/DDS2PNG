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

Una herramienta ligera de conversión de DDS a PNG basada en Python y equipada con una interfaz gráfica sencilla.

## Descripción general

DDS to PNG Converter es una aplicación de escritorio diseñada para convertir archivos de texturas en formato DDS (DirectDraw Surface) a imágenes PNG mediante una interfaz gráfica intuitiva.

El objetivo de este proyecto es permitir a los usuarios convertir archivos de texturas de forma sencilla y práctica, sin necesidad de utilizar comandos de línea de comandos.

## Características

- Conversión de archivos DDS al formato PNG.
- Interfaz gráfica sencilla y fácil de usar.
- Aplicación ligera basada en Python.
- Selección de archivos y proceso de conversión sencillos.

## Requisitos

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv): Se utiliza para convertir archivos DDS al formato PNG. Se incluye en la carpeta `assets` junto con la aplicación.

### Texconv (Descarga opcional)

Si la versión de Texconv incluida con el proyecto no funciona o prefieres descargarla manualmente, puedes utilizar los siguientes métodos.

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

1. Clona el repositorio:
   ```
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
   ```
2. Accede al directorio del proyecto:
   ```
   cd "RUTA DEL DIRECTORIO DEL PROYECTO"
   ```
3. Instala las dependencias necesarias:
   ```
   pip install -r requirements.txt
   ```

### Entorno virtual (Opcional)

Puedes utilizar un entorno virtual para mantener las dependencias de Python separadas de las de otros proyectos.

1. Crea un entorno virtual:
   ```
   python -m venv .venv
   ```
2. Activa el entorno virtual:
   ```
   .venv\Scripts\activate
   ```
3. Instala las dependencias necesarias:
   ```
   python -m pip install -r requirements.txt
   ```

**Nota:** Puedes realizar las tareas de instalación y gestión de dependencias utilizando PowerShell o el Símbolo del sistema (CMD) como usuario normal. No se requieren permisos de administrador.

Si `pip` encuentra un error de permisos al intentar escribir en el directorio de Python de todo el sistema, se recomienda utilizar un entorno virtual (`venv`) en lugar de ejecutar la terminal como administrador.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```

2. Accede al directorio del proyecto:

   ```bash
   cd "RUTA DE LA CARPETA DEL PROYECTO"
   ```

## Uso

Ejecuta la aplicación:

```bash
python Converter.pyw
```

Selecciona tu archivo DDS y sigue las instrucciones en pantalla para convertirlo al formato PNG.

## Compilación (Creación de un EXE)

Sigue los pasos indicados a continuación para convertir la aplicación Python en un único archivo EXE.

**Importante:** Ejecuta PowerShell como usuario normal, no como administrador. No se requieren permisos de administrador.

### 1. Abrir PowerShell

1. Abre el menú Inicio de Windows.
2. Escribe `PowerShell` o `Windows Terminal` en el cuadro de búsqueda.
3. Abre Windows PowerShell o Windows Terminal normalmente.
4. No selecciones la opción Ejecutar como administrador.

### 2. Acceder al directorio del proyecto

Introduce el siguiente comando en PowerShell para acceder al directorio del proyecto:

```powershell
cd "D:\vectorrdevworks\Projeler\Yazılım Projeleri\Python\DDS-to-PNG-Converter"
```

### 3. Incrustar el icono de la aplicación

El siguiente comando ejecuta el script `embed_icon.ps1` e incrusta el icono de la aplicación en el archivo Python.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Nota:** El parámetro `-ExecutionPolicy Bypass` se utiliza porque la directiva de ejecución de Windows puede impedir que se ejecuten scripts de PowerShell. Esta configuración solo se aplica al proceso de PowerShell iniciado. No se modifican los ajustes de seguridad del sistema.

### 4. Compilar con PyInstaller

Después de incrustar el icono, ejecuta el siguiente comando para crear el archivo EXE:

```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.ico" --name "DDS-to-PNG-Converter" "Converter.pyw"
```

**Parámetros del comando:**

| Parámetro     | Descripción                                   |
| ------------- | --------------------------------------------- |
| `--noconfirm` | Compila sin solicitar confirmación.           |
| `--clean`     | Limpia la caché de compilaciones anteriores.  |
| `--onefile`   | Crea un único archivo EXE.                    |
| `--windowed`  | Oculta la ventana de la consola.              |
| `--icon`      | Establece el icono del archivo EXE.           |
| `--name`      | Establece el nombre del archivo EXE generado. |

### 5. Resultado de la compilación

Una vez finalizada correctamente la compilación, el archivo EXE se crea en el siguiente directorio:

```text
dist\DDS-to-PNG-Converter.exe
```

**Orden de pasos para compilar una nueva versión:**

1. Abre PowerShell como usuario normal.
2. Accede al directorio del proyecto.
3. Ejecuta el comando para incrustar el icono.
4. Ejecuta el comando de compilación de PyInstaller.
5. Obtén el archivo EXE generado en el directorio `dist`.

## Desarrollador

**vectordevworks**

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más información.
