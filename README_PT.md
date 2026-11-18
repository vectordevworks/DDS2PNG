# Conversor de DDS para PNG

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="Inglês"> Inglês
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="Alemão"> Alemão
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="Espanhol"> Espanhol
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Francês"> Francês
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japonês"> Japonês
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Coreano"> Coreano
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Português"> Português
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Russo"> Russo
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Chinês simplificado"> Chinês simplificado
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Turco"> Turco
</a>

Uma ferramenta leve de conversão de DDS para PNG, desenvolvida em Python e com uma interface gráfica simples.

## Visão geral

DDS to PNG Converter é uma aplicação de desktop desenvolvida para converter arquivos de textura no formato DDS (DirectDraw Surface) em imagens PNG por meio de uma interface gráfica intuitiva.

O objetivo deste projeto é permitir que os usuários convertam arquivos de textura de maneira fácil e prática, sem precisar utilizar comandos de linha de comando.

## Funcionalidades

- Conversão de arquivos DDS para o formato PNG.
- Interface gráfica simples e fácil de usar.
- Aplicação leve desenvolvida em Python.
- Seleção de arquivos e processo de conversão simples.

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
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
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

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd "CAMINHO DA PASTA DO PROJETO"
   ```

## Utilização

Execute a aplicação:

```bash
python Converter.pyw
```

Selecione seu arquivo DDS e siga as instruções na tela para convertê-lo para o formato PNG.

## Compilação (Criação de um EXE)

Siga as etapas abaixo para converter a aplicação Python em um único arquivo EXE.

**Importante:** Execute o PowerShell como usuário normal, não como administrador. Não são necessários privilégios de administrador.

### 1. Abrir o PowerShell

1. Abra o menu Iniciar do Windows.
2. Digite `PowerShell` ou `Windows Terminal` na caixa de pesquisa.
3. Abra o Windows PowerShell ou o Windows Terminal normalmente.
4. Não selecione a opção Executar como administrador.

### 2. Acessar o diretório do projeto

Digite o seguinte comando no PowerShell para acessar o diretório do projeto:

```powershell
cd "D:\vectorrdevworks\Projeler\Yazılım Projeleri\Python\DDS-to-PNG-Converter"
```

### 3. Incorporar o ícone da aplicação

O comando abaixo executa o script `embed_icon.ps1` e incorpora o ícone da aplicação ao arquivo Python.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Nota:** O parâmetro `-ExecutionPolicy Bypass` é utilizado porque a política de execução do Windows pode impedir a execução de scripts do PowerShell. Essa configuração aplica-se apenas ao processo do PowerShell iniciado. As configurações de segurança de todo o sistema não são alteradas.

### 4. Compilar com PyInstaller

Após incorporar o ícone, execute o seguinte comando para criar o arquivo EXE:

```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.ico" --name "DDS-to-PNG-Converter" "Converter.pyw"
```

**Parâmetros do comando:**

| Parâmetro     | Descrição                             |
| ------------- | ------------------------------------- |
| `--noconfirm` | Compila sem solicitar confirmação.    |
| `--clean`     | Limpa o cache da compilação anterior. |
| `--onefile`   | Cria um único arquivo EXE.            |
| `--windowed`  | Oculta a janela do console.           |
| `--icon`      | Define o ícone do arquivo EXE.        |
| `--name`      | Define o nome do arquivo EXE gerado.  |

### 5. Resultado da compilação

Após a conclusão bem-sucedida da compilação, o arquivo EXE será criado no seguinte diretório:

```text
dist\DDS-to-PNG-Converter.exe
```

**Ordem das etapas para compilar uma nova versão:**

1. Abra o PowerShell como usuário normal.
2. Acesse o diretório do projeto.
3. Execute o comando para incorporar o ícone.
4. Execute o comando de compilação do PyInstaller.
5. Obtenha o arquivo EXE gerado no diretório `dist`.

## Desenvolvedor

**vectordevworks**

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
