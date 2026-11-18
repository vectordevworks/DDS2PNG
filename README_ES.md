# Convertidor de DDS a PNG

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="Ingl谷s"> Ingl谷s
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="Alem芍n"> Alem芍n
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="Espa?ol"> Espa?ol
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Franc谷s"> Franc谷s
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japon谷s"> Japon谷s
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Coreano"> Coreano
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Portugu谷s"> Portugu谷s
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

Una herramienta ligera de conversi車n de DDS a PNG, desarrollada en Python y equipada con una interfaz gr芍fica sencilla.

## Descripci車n general

DDS to PNG Converter es una aplicaci車n de escritorio dise?ada para convertir archivos de texturas en formato DDS (DirectDraw Surface) a im芍genes PNG mediante una interfaz gr芍fica intuitiva.

El objetivo del proyecto es permitir a los usuarios convertir archivos de texturas de forma sencilla y pr芍ctica, sin necesidad de utilizar comandos en la terminal.

## Caracter赤sticas

- Conversi車n de archivos DDS al formato PNG.
- Interfaz gr芍fica sencilla y f芍cil de usar.
- Aplicaci車n ligera desarrollada en Python.
- Selecci車n de archivos y proceso de conversi車n sencillos.

## Requisitos

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv): se utiliza para convertir archivos DDS al formato PNG. Se incluye con la aplicaci車n en la carpeta `assets`.

### Texconv (Descarga opcional)

Si la versi車n de Texconv incluida en el proyecto no funciona o desea descargarla manualmente, puede utilizar los siguientes m谷todos.

**PowerShell (Winget):**

```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Para comprobar la instalaci車n:

```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Descarga manual:**

[Versiones de Microsoft DirectXTex](https://github.com/microsoft/DirectXTex/releases)

## Instalaci車n

1. Clone el repositorio:

   ```bash
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```

2. Acceda al directorio del proyecto:

   ```bash
   cd "RUTA DEL PROYECTO"
   ```

3. Instale las dependencias necesarias:

   ```powershell
   pip install -r requirements.txt
   ```

### Entorno virtual (opcional)

Puede utilizar un entorno virtual para mantener las dependencias de Python separadas de las de otros proyectos.

1. (Solo si PowerShell muestra un error al ejecutar scripts) conceda permisos temporales para la sesi車n actual:

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

Ejecute la aplicaci車n:

```bash
python Converter.pyw
```

Seleccione su archivo DDS y siga las instrucciones que aparecen en pantalla para convertirlo al formato PNG.

## Compilaci車n (Creaci車n del archivo EXE)

Siga los pasos que se indican a continuaci車n para convertir la aplicaci車n Python en un 迆nico archivo EXE.

**Importante:** Ejecute PowerShell como usuario normal, no como administrador. No se necesitan permisos de administrador.

### 1. Abrir PowerShell

1. Abra el men迆 Inicio de Windows.
2. Escriba `PowerShell` o `Windows Terminal` en el cuadro de b迆squeda.
3. Abra Windows PowerShell o Windows Terminal normalmente.
4. No utilice la opci車n Ejecutar como administrador.

### 2. Acceder a la carpeta del proyecto

Introduzca el siguiente comando en PowerShell para acceder a la carpeta del proyecto:

```powershell
cd "D:\vectorrdevworks\Projeler\Yaz?l?m Projeleri\Python\DDS2PNG"
```

### 3. Incrustar el icono de la aplicaci車n

El siguiente comando ejecuta el script `embed_icon.ps1` para incrustar el icono de la aplicaci車n en el archivo Python.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Nota:** Se utiliza `-ExecutionPolicy Bypass` debido a la pol赤tica de ejecuci車n que puede impedir que Windows ejecute scripts de PowerShell. Esta configuraci車n solo se aplica al proceso de PowerShell iniciado. No se modifican los ajustes de seguridad del sistema.

### 4. Compilar con PyInstaller

Una vez completado el proceso de incrustaci車n del icono, ejecute el siguiente comando para crear el archivo EXE:

```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.png" --name "DDS2PNG" "Converter.pyw"
```

**Par芍metros del comando:**

| Par芍metro | Descripci車n |
|---|---|
| `--noconfirm` | Realiza la compilaci車n sin solicitar confirmaci車n. |
| `--clean` | Limpia la cach谷 de compilaciones anteriores. |
| `--onefile` | Crea un 迆nico archivo EXE. |
| `--windowed` | Oculta la ventana de la consola. |
| `--icon` | Establece el icono del archivo EXE. |
| `--name` | Define el nombre del archivo EXE que se generar芍. |

### 5. Resultado de la compilaci車n

Cuando la compilaci車n finalice correctamente, el archivo EXE se crear芍 en la siguiente carpeta:

```text
dist\Converter.exe
```

**Orden de los pasos al compilar una nueva versi車n:**

1. Abra PowerShell como usuario normal.
2. Acceda a la carpeta del proyecto.
3. Ejecute el comando para incrustar el icono.
4. Ejecute el comando de compilaci車n de PyInstaller.
5. Obtenga el archivo EXE generado desde la carpeta `dist`.

## Desarrollador

**vectordevworks**

## Licencia

Este proyecto est芍 bajo la licencia MIT. Para obtener m芍s informaci車n, consulte el archivo [LICENSE](LICENSE).