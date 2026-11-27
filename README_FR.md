<div align="center">

# DDS2PNG

### Convertisseur DDS vers PNG

Convertissez facilement des fichiers de texture au format DDS (DirectDraw Surface) en PNG.

Une application de bureau légère et facile à utiliser, développée en Python.

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

### 🌐 Sélection de la langue

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="English"> English</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Deutsch"> Deutsch</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español</a> |
<strong><img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français</strong> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Português"> Português</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Русский"> Русский</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="日本語"> 日本語</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe</a>

---

### 📑 Table des matières

<a href="#genel-bakis">Présentation</a>
<a href="#ozellikler">Fonctionnalités</a>
<a href="#gereksinimler">Prérequis</a>
<a href="#kurulum">Installation</a>
<a href="#sanal-ortam">Environnement virtuel (facultatif)</a>
<a href="#kullanim">Utilisation</a>
<a href="#derleme">Compilation (création de l’EXE)</a>
<a href="#gelistirici">Développeur</a>
<a href="#lisans">Licence</a>

</div>

---

<a id="genel-bakis"></a>
## 🔍 Présentation

**DDS2PNG** est une application de bureau légère basée sur Python qui permet de convertir des fichiers de texture au format DDS (DirectDraw Surface) en PNG.

Son interface graphique simple vous permet de sélectionner et de convertir facilement des fichiers. Aucune commande en ligne de commande n’est nécessaire.

Les conversions sont effectuées à l’aide de Microsoft DirectXTex (Texconv).

L’outil Texconv est fourni avec l’application dans le dossier `assets`.

<a id="ozellikler"></a>
## ✨ Fonctionnalités

- **Conversion DDS vers PNG :** Convertit les fichiers DDS au format PNG.
- **Interface graphique :** Offre une interface simple pour sélectionner et convertir des fichiers.
- **Prise en charge de Texconv :** Utilise Microsoft DirectXTex pour convertir les fichiers DDS.
- **Facile à utiliser :** Permet de convertir des fichiers sans utiliser la ligne de commande.

<a id="gereksinimler"></a>
## 📋 Prérequis

- Windows
- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)

Les modules `tkinter`, `ctypes`, `json`, `math`, `os` et `pathlib` font partie de la bibliothèque standard de Python.

L’outil Texconv est fourni avec l’application dans le dossier `assets`.

### Texconv (Téléchargement facultatif)

Si la version de Texconv fournie avec le projet ne fonctionne pas ou si vous souhaitez la télécharger manuellement, utilisez l’une des méthodes ci-dessous.

**PowerShell (Winget):**

```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Pour vérifier l’installation :

```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Téléchargement manuel :**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

<a id="kurulum"></a>
## 📥 Installation

1. Clonez le dépôt :

```bash
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Ouvrez le dossier du projet.

3. Lancez PowerShell dans le dossier du projet.

4. Installez les paquets Python requis :

```powershell
py -m pip install -r requirements.txt
```

<a id="sanal-ortam"></a>
## 🐍 Environnement virtuel (facultatif)

Vous pouvez utiliser un environnement virtuel afin de séparer les dépendances Python des autres projets.

**1. Créer un environnement virtuel :**

```powershell
py -m venv .venv
```

**2. Activer l’environnement virtuel :**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Installer les dépendances requises :**

```powershell
py -m pip install -r requirements.txt
```

**4. Désactiver l’environnement virtuel une fois terminé :**

```powershell
deactivate
```

**Activation via CMD (invite de commandes) :**

Si vous utilisez CMD au lieu de PowerShell :

```cmd
.venv\Scripts\activate.bat
```

Pour quitter l’environnement virtuel :

```cmd
deactivate
```

### Problèmes d’activation de l’environnement virtuel

Dans certains cas, la stratégie d’exécution de PowerShell peut empêcher l’activation de l’environnement virtuel.

Dans ce cas, exécutez la commande suivante :

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Activez ensuite à nouveau l’environnement virtuel :

```powershell
.\.venv\Scripts\Activate.ps1
```

Ce paramètre s’applique uniquement à la session PowerShell en cours. Les paramètres par défaut sont rétablis à l’ouverture d’une nouvelle session PowerShell.

### Utiliser l’environnement virtuel sans l’activer

L’activation de l’environnement virtuel n’est pas obligatoire. En cas d’échec, vous pouvez continuer à l’utiliser en appelant directement les exécutables Python et pip.

**Pour installer les dépendances :**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Pour lancer l’application :**

```powershell
.\.venv\Scripts\python.exe DDSConverter.pyw
```

**Remarque :** Les droits d’administrateur ne sont pas nécessaires pour créer, activer, installer les dépendances ou désactiver l’environnement virtuel. Python doit toutefois être correctement installé et vous devez disposer des droits d’accès aux fichiers requis.

<a id="kullanim"></a>
## 🚀 Utilisation

1. Exécutez le fichier `DDSConverter.pyw` :

```powershell
pyw .\DDSConverter.pyw
```

Autre possibilité :

```powershell
pythonw .\DDSConverter.pyw
```

2. Sélectionnez le fichier DDS que vous souhaitez convertir.

3. Vous pouvez choisir le dossier `convert` existant comme dossier de sortie ou sélectionner le dossier de votre choix.

4. Effectuez la conversion au format PNG.

<a id="derleme"></a>
## 📦 Compilation (création de l’EXE)

PyInstaller permet de regrouper l’application Python dans un seul fichier EXE.

### 1. Accéder au dossier du projet

Commencez par ouvrir le dossier du projet DDS2PNG. Vous pouvez utiliser l’une des méthodes suivantes pour ouvrir un terminal dans ce dossier.

**Méthode 1 : Ouvrir un terminal depuis l’Explorateur de fichiers**

1. Ouvrez le dossier du projet DDS2PNG dans l’Explorateur de fichiers.

2. Saisissez `cmd` ou `powershell` dans la barre d’adresse.

3. Appuyez sur Entrée.

Le terminal s’ouvrira directement dans le dossier du projet.

**Méthode 2 : Accéder au dossier du projet depuis le terminal**

Ouvrez CMD ou PowerShell et utilisez la commande appropriée ci-dessous.

**CMD:**

```cmd
cd /d "PROJE_KLASORUNUN_YOLU"
```

**PowerShell:**

```powershell
Set-Location -LiteralPath "PROJE_KLASORUNUN_YOLU"
```

Remplacez `PROJE_KLASORUNUN_YOLU` par le chemin complet du dossier du projet DDS2PNG sur votre ordinateur.

**Remarque :** Il n’est pas nécessaire d’exécuter le terminal en tant qu’administrateur. Les droits d’un utilisateur standard suffisent.

### 2. Compiler l’EXE

Le script `buid.ps1`, situé dans le dossier `scripts` du projet, compile l’application au format EXE à l’aide de PyInstaller.

Le script de compilation effectue automatiquement les opérations suivantes :

- Vérifie les fichiers requis du projet.
- Vérifie l’installation de PyInstaller.
- Nettoie les fichiers de compilation précédents.
- Utilise `icon.ico` comme icône de l’EXE.
- Inclut le dossier `assets` dans le fichier EXE.
- Vérifie le résultat de la compilation.

**Exécution via CMD :**

```cmd
powershell -ExecutionPolicy Bypass -File "scripts\buid.ps1"
```

**Exécution via PowerShell :**

```powershell
.\scripts\buid.ps1
```

### 3. Résultat de la compilation

Une fois la compilation terminée, le fichier EXE est créé à l’emplacement suivant :

```text
dist\DDS2PNG.exe
```

**Étapes pour compiler une nouvelle version :**

1. Ouvrez le dossier du projet DDS2PNG.

2. Ouvrez un terminal en saisissant `cmd` ou `powershell` dans la barre d’adresse, ou accédez au dossier du projet depuis un terminal déjà ouvert.

3. Exécutez le script de compilation.

4. Vous trouverez le fichier EXE généré dans le dossier `dist`.

### 4. Lancer l’application

Une fois la compilation terminée, utilisez la commande suivante pour lancer l’application :

```powershell
dist\DDS2PNG.exe
```

Vous pouvez également ouvrir le dossier `dist` et double-cliquer sur `DDS2PNG.exe`.

**Remarque :** Il n’est pas nécessaire d’ouvrir CMD ou PowerShell en tant qu’administrateur pour lancer l’application.

<a id="gelistirici"></a>
## 👨‍💻 Développeur

<div align="center">

**VectorDevWorks**

<a href="https://github.com/vectordevworks">
  <img src="https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github" alt="VectorDevWorks GitHub">
</a>

</div>

<a id="lisans"></a>
## 📄 Licence

Ce projet est distribué sous licence MIT. Consultez le fichier `LICENSE` du dépôt pour plus de détails.

---

<div align="center">

**Développé par VectorDevWorks.**

⭐ Si le projet vous plaît, n’oubliez pas de lui attribuer une étoile sur GitHub !

<a href="https://github.com/vectordevworks/DDS2PNG">
  <img src="https://img.shields.io/badge/Project%20Repository-DDS2PNG-blue?style=for-the-badge&logo=github" alt="DDS2PNG Repository">
</a>

</div>
