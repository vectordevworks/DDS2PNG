# Convertisseur DDS vers PNG

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
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Chino simplificado"> Chino simplificado
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Turco"> Turco
</a>

Un outil léger de conversion DDS vers PNG, développé en Python et doté d'une interface graphique simple.

## Présentation générale

DDS to PNG Converter est une application de bureau conçue pour convertir des fichiers de textures au format DDS (DirectDraw Surface) en images PNG à l'aide d'une interface graphique intuitive.

L'objectif du projet est de permettre aux utilisateurs de convertir facilement et rapidement leurs fichiers de textures, sans avoir à utiliser des commandes en ligne de commande.

## Fonctionnalités

- Conversion de fichiers DDS au format PNG.
- Interface graphique simple et conviviale.
- Application légère basée sur Python.
- Sélection facile des fichiers et processus de conversion simple.

## Prérequis

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv) : utilisé pour convertir les fichiers DDS au format PNG. Il est fourni avec l'application dans le dossier `assets`.

### Texconv (Téléchargement facultatif)

Si la version de Texconv fournie avec le projet ne fonctionne pas ou si vous souhaitez la télécharger manuellement, vous pouvez utiliser l'une des méthodes suivantes.

**PowerShell (Winget) :**
```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Pour vérifier l'installation :
```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Téléchargement manuel :**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd "CHEMIN DU DOSSIER DU PROJET"
   ```
3. Installez les dépendances nécessaires :
   ```powershell
   pip install -r requirements.txt
   ```

### Environnement virtuel (Facultatif)

Vous pouvez utiliser un environnement virtuel afin de garder les dépendances Python séparées de celles des autres projets.

1. (Uniquement si PowerShell affiche une erreur lors de l'exécution du script) Autorisez temporairement l'exécution des scripts pour la session actuelle :
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
2. Créez un environnement virtuel :
   ```powershell
   python -m venv .venv
   ```
3. Activez l'environnement virtuel :
   ```powershell
   .venv\Scripts\activate
   ```
4. Installez les dépendances nécessaires :
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. Lorsque vous avez terminé, quittez l'environnement virtuel :
   ```powershell
   deactivate
   ```

## Utilisation

Lancez l'application :
```bash
python DDSConverter.pyw
```

Sélectionnez votre fichier DDS et suivez les instructions à l'écran pour le convertir au format PNG.

## Compilation (Créer un EXE)

Suivez les étapes ci-dessous pour convertir l'application Python en un seul fichier EXE.

**Important :** Ouvrez PowerShell en tant qu'utilisateur normal et non en tant qu'administrateur. Les droits d'administrateur ne sont pas nécessaires.

### 1. Ouvrir PowerShell

1. Ouvrez le menu Démarrer de Windows.
2. Saisissez `PowerShell` ou `Windows Terminal` dans la barre de recherche.
3. Ouvrez normalement Windows PowerShell ou Windows Terminal.
4. N'utilisez pas l'option « Exécuter en tant qu'administrateur ».

### 2. Accéder au dossier du projet

Saisissez la commande suivante dans PowerShell pour accéder au dossier du projet :
```powershell
   cd "CHEMIN DU DOSSIER DU PROJET"
```

### 3. Intégrer l'icône de l'application

La commande suivante exécute le script `embed_icon.ps1` afin d'intégrer l'icône de l'application dans le fichier Python.
```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Remarque :** `-ExecutionPolicy Bypass` est utilisé parce que la stratégie d'exécution de Windows peut empêcher l'exécution des scripts PowerShell. Ce paramètre s'applique uniquement au processus PowerShell lancé. Les paramètres de sécurité du système ne sont pas modifiés.

### 4. Compiler avec PyInstaller

Une fois l'intégration de l'icône terminée, exécutez la commande suivante pour créer le fichier EXE :
```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.png" --name "DDS2PNG" "DDSConverter.pyw"
```

**Paramètres de la commande :**

| Paramètre | Description |
|---|---|
| `--noconfirm` | Effectue la compilation sans demander de confirmation. |
| `--clean` | Efface le cache des compilations précédentes. |
| `--onefile` | Crée un seul fichier EXE. |
| `--windowed` | N'affiche pas de fenêtre de console. |
| `--icon` | Définit l'icône du fichier EXE. |
| `--name` | Définit le nom du fichier EXE à créer. |

### 5. Résultat de la compilation

Une fois la compilation terminée avec succès, le fichier EXE sera créé dans le dossier suivant :
```text
dist\DDSConverter.exe
```

**Ordre des étapes lors de la compilation d'une nouvelle version :**

1. Ouvrez PowerShell en tant qu'utilisateur normal.
2. Accédez au dossier du projet.
3. Exécutez la commande d'intégration de l'icône.
4. Exécutez la commande de compilation PyInstaller.
5. Récupérez le fichier EXE généré dans le dossier `dist`.

## Développeur

**vectordevworks**

## Licence

Ce projet est distribué sous licence MIT. Consultez le fichier LICENSE pour plus de détails.