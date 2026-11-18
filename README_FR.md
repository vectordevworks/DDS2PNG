# Convertisseur DDS vers PNG

<a href="README.md">
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
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français
</a>
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

Un outil léger de conversion DDS vers PNG basé sur Python et doté d'une interface graphique simple.

## Présentation

DDS to PNG Converter est une application de bureau conçue pour convertir des fichiers de textures au format DDS (DirectDraw Surface) en images PNG à l'aide d'une interface graphique intuitive.

L'objectif de ce projet est de permettre aux utilisateurs de convertir facilement et rapidement des fichiers de textures sans avoir à utiliser des commandes en ligne de commande.

## Fonctionnalités

- Conversion de fichiers DDS au format PNG.
- Interface graphique simple et conviviale.
- Application légère basée sur Python.
- Sélection de fichiers et processus de conversion faciles.

## Prérequis

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv) : Utilisé pour convertir les fichiers DDS au format PNG. Fourni avec l'application dans le dossier `assets`.

### Texconv (Téléchargement facultatif)

Si la version de Texconv fournie avec le projet ne fonctionne pas ou si vous préférez la télécharger manuellement, vous pouvez utiliser les méthodes suivantes.

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
   ```
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```
2. Accédez au répertoire du projet :
   ```
   cd "CHEMIN DU DOSSIER DU PROJET"
   ```
3. Installez les dépendances nécessaires :
   ```
   pip install -r requirements.txt
   ```

### Environnement virtuel (Facultatif)

Vous pouvez utiliser un environnement virtuel pour isoler les dépendances Python des autres projets.

1. Créez un environnement virtuel :
   ```
   python -m venv .venv
   ```
2. Activez l'environnement virtuel :
   ```
   .venv\Scripts\activate
   ```
3. Installez les dépendances nécessaires :
   ```
   python -m pip install -r requirements.txt
   ```

**Remarque :** Vous pouvez effectuer les opérations d'installation et de gestion des dépendances avec PowerShell ou l'invite de commandes (CMD) en tant qu'utilisateur standard. Les privilèges administrateur ne sont pas nécessaires.

Si `pip` rencontre une erreur d'autorisation lorsqu'il tente d'écrire dans le répertoire Python installé pour l'ensemble du système, il est recommandé d'utiliser un environnement virtuel (`venv`) plutôt que d'exécuter le terminal en tant qu'administrateur.

## Installation

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
   ```

2. Accéder au répertoire du projet :

   ```bash
   cd "CHEMIN DU DOSSIER DU PROJET"
   ```

## Utilisation

Lancez l'application :

```bash
python Converter.pyw
```

Sélectionnez votre fichier DDS et suivez les instructions à l'écran pour le convertir au format PNG.

## Compilation (Création d'un EXE)

Suivez les étapes ci-dessous pour convertir l'application Python en un seul fichier EXE.

**Important :** Exécutez PowerShell en tant qu'utilisateur standard, et non en tant qu'administrateur. Les privilèges d'administrateur ne sont pas nécessaires.

### 1. Ouvrir PowerShell

1. Ouvrez le menu Démarrer de Windows.
2. Saisissez `PowerShell` ou `Windows Terminal` dans la barre de recherche.
3. Ouvrez Windows PowerShell ou Windows Terminal normalement.
4. Ne sélectionnez pas l'option Exécuter en tant qu'administrateur.

### 2. Accéder au répertoire du projet

Saisissez la commande suivante dans PowerShell pour accéder au répertoire du projet :

```powershell
cd "D:\vectorrdevworks\Projeler\Yazılım Projeleri\Python\DDS-to-PNG-Converter"
```

### 3. Intégrer l'icône de l'application

La commande suivante exécute le script `embed_icon.ps1` et intègre l'icône de l'application dans le fichier Python.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Remarque :** Le paramètre `-ExecutionPolicy Bypass` est utilisé car la stratégie d'exécution de Windows peut empêcher l'exécution des scripts PowerShell. Ce paramètre s'applique uniquement au processus PowerShell lancé. Les paramètres de sécurité globaux du système ne sont pas modifiés.

### 4. Compiler avec PyInstaller

Une fois l'icône intégrée, exécutez la commande suivante pour créer le fichier EXE :

```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.ico" --name "DDS-to-PNG-Converter" "Converter.pyw"
```

**Paramètres de la commande :**

| Paramètre     | Description                                            |
| ------------- | ------------------------------------------------------ |
| `--noconfirm` | Effectue la compilation sans demander de confirmation. |
| `--clean`     | Efface le cache de compilation précédent.              |
| `--onefile`   | Crée un seul fichier EXE.                              |
| `--windowed`  | Masque la fenêtre de la console.                       |
| `--icon`      | Définit l'icône du fichier EXE.                        |
| `--name`      | Définit le nom du fichier EXE généré.                  |

### 5. Résultat de la compilation

Une fois la compilation terminée avec succès, le fichier EXE est créé dans le répertoire suivant :

```text
dist\DDS-to-PNG-Converter.exe
```

**Ordre des étapes pour compiler une nouvelle version :**

1. Ouvrez PowerShell en tant qu'utilisateur standard.
2. Accédez au répertoire du projet.
3. Exécutez la commande d'intégration de l'icône.
4. Exécutez la commande de compilation PyInstaller.
5. Récupérez le fichier EXE généré dans le répertoire `dist`.

## Développeur

**vectordevworks**

## Licence

Ce projet est distribué sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
