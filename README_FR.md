# DDS2PNG

<<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="Anglais"> Anglais
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="Allemand"> Allemand
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="Espagnol"> Espagnol
</a>
|
<strong>
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français
</strong>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japonais"> Japonais
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Coréen"> Coréen
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Portugais"> Portugais
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Russe"> Russe
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Chinois simplifié"> Chinois simplifié
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Turc"> Turc
</a>

Le Convertisseur DDS vers PNG est une application de bureau légère basée sur Python, qui permet de convertir des fichiers de texture au format DDS (DirectDraw Surface) en images PNG. Son interface graphique simple permet de sélectionner facilement les fichiers et d'effectuer les conversions.

## Présentation générale

L'application convertit les fichiers de texture DDS au format PNG à l'aide de Microsoft DirectXTex (Texconv). La conversion s'effectue depuis une interface graphique ; il n'est donc pas nécessaire d'utiliser des commandes en ligne de commande.

L'outil Texconv est fourni avec l'application dans le dossier `assets`.

## Fonctionnalités

- **Conversion DDS vers PNG :** Convertit les fichiers DDS au format PNG.

- **Interface graphique :** Propose une interface simple qui facilite la sélection des fichiers et leur conversion.

- **Prise en charge de Texconv :** Utilise l'outil Microsoft DirectXTex pour convertir les fichiers DDS.

- **Facile à utiliser :** Permet d'effectuer les conversions sans utiliser la ligne de commande.


## Prérequis

- Windows

- Python 3.x

- Pillow

- Microsoft DirectXTex (Texconv)


Les modules `tkinter`, `ctypes`, `json`, `math`, `os` et `pathlib` font partie de la bibliothèque standard de Python.

Texconv sert à convertir les fichiers DDS au format PNG et est fourni avec l'application dans le dossier `assets`.

### Texconv (Téléchargement facultatif)

Si la version de Texconv fournie avec le projet ne fonctionne pas ou si vous souhaitez la télécharger manuellement, vous pouvez utiliser les méthodes ci-dessous.

**PowerShell (Winget):**

```
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Pour vérifier l'installation :

```
winget list --id Microsoft.DirectXTex.Texconv
```

**Téléchargement manuel:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Installation

1. Clonez le dépôt :

```
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Ouvrez le dossier du projet.

3. Lancez PowerShell dans ce dossier.

4. Installez les packages Python nécessaires :

```
py -m pip install -r requirements.txt
```

## Environnement virtuel (facultatif)

Vous pouvez utiliser un environnement virtuel pour séparer les dépendances Python des autres projets :

1. Créez un environnement virtuel :

```
py -m venv .venv
```

2. Activez l'environnement virtuel :

```
.\.venv\Scripts\Activate.ps1
```

3. Installez les packages Python nécessaires :

```
py -m pip install -r requirements.txt
```

4. Lorsque vous avez terminé, désactivez l'environnement virtuel :

```
deactivate
```

## Utilisation

1. Exécutez le fichier `DDSConverter.pyw` :

```
pyw .\DDSConverter.pyw
```

Autre possibilité :

```
pythonw .\DDSConverter.pyw
```

2. Sélectionnez le fichier DDS que vous souhaitez convertir.

3. Vous pouvez choisir le dossier `convert` existant comme dossier de sortie ou sélectionner le dossier de votre choix.

4. Effectuez la conversion au format PNG.

## Compilation (création d'un EXE)

PyInstaller permet de convertir l'application Python en un seul fichier EXE.

### 1. Accéder au dossier du projet

Ouvrez PowerShell dans le dossier du projet.

### 2. Intégrer l'icône et les images des langues

Exécutez le script `embed_icon.ps1` à l'aide de la commande ci-dessous. Ce script intègre dans le fichier Python l'icône de l'application ainsi que les images PNG utilisées pour la sélection de la langue.

```
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Remarque :** Le paramètre `-ExecutionPolicy Bypass` est utilisé lorsque la stratégie d'exécution de Windows risque d'empêcher le lancement des scripts PowerShell. Ce paramètre ne s'applique qu'au processus PowerShell lancé et ne modifie pas les paramètres de sécurité à l'échelle du système.

### 3. Résultat de la compilation

Une fois la compilation terminée avec succès, le fichier EXE est créé à l'emplacement suivant :

```
dist\DDS2PNG.exe
```

**Étapes pour compiler une nouvelle version :**

1. Ouvrez PowerShell.

2. Vérifiez que PyInstaller est installé.

3. Accédez au dossier du projet.

4. Exécutez le script de compilation.

5. Le fichier EXE généré se trouve dans le dossier `dist`.

## Développeur

**vectordevworks**

## Licence

Ce projet est distribué sous licence MIT. Consultez le fichier `LICENSE` du dépôt du projet pour plus de détails.
