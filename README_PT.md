<div align="center">

# DDS2PNG

### Conversor de DDS para PNG

Converta facilmente arquivos de textura no formato DDS (DirectDraw Surface) para PNG.

Um aplicativo de desktop leve e fácil de usar, desenvolvido em Python.

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

### 🌐 Seleção de idioma

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="English"> English</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Deutsch"> Deutsch</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français</a> |
<strong><img src="https://flagcdn.com/pt.svg" width="20" alt="Português"> Português</strong> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Русский"> Русский</a> |
<a href="README_JA.md"><img src="https://flagcdn.com/jp.svg" width="20" alt="日本語"> 日本語</a> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe</a>

---

### 📑 Sumário

<a href="#genel-bakis">Visão geral</a>
<a href="#ozellikler">Recursos</a>
<a href="#gereksinimler">Requisitos</a>
<a href="#kurulum">Instalação</a>
<a href="#sanal-ortam">Ambiente virtual (opcional)</a>
<a href="#kullanim">Uso</a>
<a href="#derleme">Compilação (criar EXE)</a>
<a href="#gelistirici">Desenvolvedor</a>
<a href="#lisans">Licença</a>

</div>

---

<a id="genel-bakis"></a>
## 🔍 Visão geral

**DDS2PNG** é um aplicativo de desktop leve, baseado em Python, que permite converter arquivos de textura no formato DDS (DirectDraw Surface) para PNG.

Sua interface gráfica simples permite selecionar arquivos e convertê-los facilmente. Não é necessário usar comandos de linha de comando.

As conversões são realizadas usando o Microsoft DirectXTex (Texconv).

A ferramenta Texconv é fornecida com o aplicativo na pasta `assets`.

<a id="ozellikler"></a>
## ✨ Recursos

- **Conversão de DDS para PNG:** Converte arquivos DDS para o formato PNG.
- **Interface gráfica:** Oferece uma interface simples para selecionar e converter arquivos.
- **Suporte ao Texconv:** Usa o Microsoft DirectXTex para converter arquivos DDS.
- **Fácil de usar:** Permite converter arquivos sem usar a linha de comando.

<a id="gereksinimler"></a>
## 📋 Requisitos

- Windows
- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)

Os módulos `tkinter`, `ctypes`, `json`, `math`, `os` e `pathlib` fazem parte da biblioteca padrão do Python.

A ferramenta Texconv é fornecida com o aplicativo na pasta `assets`.

### Texconv (Download opcional)

Se a versão do Texconv incluída no projeto não funcionar ou se você quiser baixá-la manualmente, use um dos métodos abaixo.

**PowerShell (Winget):**

```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Para verificar a instalação:

```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Download manual:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

<a id="kurulum"></a>
## 📥 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Abra a pasta do projeto.

3. Inicie o PowerShell na pasta do projeto.

4. Instale os pacotes Python necessários:

```powershell
py -m pip install -r requirements.txt
```

<a id="sanal-ortam"></a>
## 🐍 Ambiente virtual (opcional)

Você pode usar um ambiente virtual para manter as dependências do Python separadas de outros projetos.

**1. Criar um ambiente virtual:**

```powershell
py -m venv .venv
```

**2. Ativar o ambiente virtual:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. Instalar as dependências necessárias:**

```powershell
py -m pip install -r requirements.txt
```

**4. Desativar o ambiente virtual quando terminar:**

```powershell
deactivate
```

**Ativação pelo CMD (Prompt de Comando):**

Se você usa o CMD em vez do PowerShell:

```cmd
.venv\Scripts\activate.bat
```

Para sair do ambiente virtual:

```cmd
deactivate
```

### Problemas ao ativar o ambiente virtual

Em alguns casos, o PowerShell pode impedir a ativação do ambiente virtual devido à política de execução.

Nesse caso, execute o seguinte comando:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Em seguida, ative o ambiente virtual novamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Essa configuração se aplica somente à sessão atual do PowerShell. As configurações padrão serão restauradas quando uma nova sessão for aberta.

### Usar o ambiente virtual sem ativá-lo

A ativação do ambiente virtual não é obrigatória. Se a ativação falhar, você poderá continuar usando o ambiente chamando diretamente os executáveis do Python e do pip.

**Para instalar as dependências:**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Para executar o aplicativo:**

```powershell
.\.venv\Scripts\python.exe DDSConverter.pyw
```

**Observação:** Não são necessárias permissões de administrador para criar, ativar, instalar dependências ou desativar o ambiente virtual. No entanto, o Python deve estar instalado corretamente e você precisa ter permissão para acessar os arquivos necessários.

<a id="kullanim"></a>
## 🚀 Uso

1. Execute o arquivo `DDSConverter.pyw`:

```powershell
pyw .\DDSConverter.pyw
```

Como alternativa:

```powershell
pythonw .\DDSConverter.pyw
```

2. Selecione o arquivo DDS que deseja converter.

3. Você pode escolher a pasta `convert` existente como pasta de saída ou selecionar qualquer outra pasta desejada.

4. Realize a conversão para o formato PNG.

<a id="derleme"></a>
## 📦 Compilação (criar EXE)

O PyInstaller é usado para empacotar o aplicativo Python em um único arquivo EXE.

### 1. Acessar a pasta do projeto

Primeiro, abra a pasta do projeto DDS2PNG. Você pode usar um dos métodos abaixo para abrir um terminal nessa pasta.

**Método 1: Abrir um terminal pelo Explorador de Arquivos**

1. Abra a pasta do projeto DDS2PNG no Explorador de Arquivos.

2. Digite `cmd` ou `powershell` na barra de endereço.

3. Pressione Enter.

O terminal será aberto diretamente na pasta do projeto.

**Método 2: Acessar a pasta do projeto pelo terminal**

Abra o CMD ou o PowerShell e use o comando apropriado abaixo.

**CMD:**

```cmd
cd /d "PROJE_KLASORUNUN_YOLU"
```

**PowerShell:**

```powershell
Set-Location -LiteralPath "PROJE_KLASORUNUN_YOLU"
```

Substitua `PROJE_KLASORUNUN_YOLU` pelo caminho completo da pasta do projeto DDS2PNG no seu computador.

**Observação:** Não é necessário executar o terminal como administrador. As permissões normais de usuário são suficientes.

### 2. Compilar o EXE

O script `buid.ps1`, localizado na pasta `scripts` do projeto, compila o aplicativo no formato EXE usando o PyInstaller.

O script de compilação executa automaticamente as seguintes tarefas:

- Verifica os arquivos necessários do projeto.
- Verifica a instalação do PyInstaller.
- Limpa os arquivos de compilações anteriores.
- Usa `icon.ico` como ícone do EXE.
- Inclui a pasta `assets` no arquivo EXE.
- Verifica o resultado da compilação.

**Executar pelo CMD:**

```cmd
powershell -ExecutionPolicy Bypass -File "scripts\buid.ps1"
```

**Executar pelo PowerShell:**

```powershell
.\scripts\buid.ps1
```

### 3. Resultado da compilação

Após a conclusão bem-sucedida da compilação, o arquivo EXE será criado no seguinte local:

```text
dist\DDS2PNG.exe
```

**Etapas para compilar uma nova versão:**

1. Abra a pasta do projeto DDS2PNG.

2. Abra um terminal digitando `cmd` ou `powershell` na barra de endereço, ou navegue até a pasta do projeto em um terminal já aberto.

3. Execute o script de compilação.

4. Você encontrará o arquivo EXE gerado na pasta `dist`.

### 4. Executar o aplicativo

Após a compilação ser concluída com sucesso, use o comando abaixo para executar o aplicativo:

```powershell
dist\DDS2PNG.exe
```

Como alternativa, abra a pasta `dist` e clique duas vezes em `DDS2PNG.exe`.

**Observação:** Não é necessário abrir o CMD ou o PowerShell como administrador para executar o aplicativo.

<a id="gelistirici"></a>
## 👨‍💻 Desenvolvedor

<div align="center">

**VectorDevWorks**

<a href="https://github.com/vectordevworks">
  <img src="https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github" alt="VectorDevWorks GitHub">
</a>

</div>

<a id="lisans"></a>
## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` no repositório para obter detalhes.

---

<div align="center">

**Desenvolvido por VectorDevWorks.**

⭐ Se você gostou do projeto, não se esqueça de deixar uma estrela no GitHub!

<a href="https://github.com/vectordevworks/DDS2PNG">
  <img src="https://img.shields.io/badge/Project%20Repository-DDS2PNG-blue?style=for-the-badge&logo=github" alt="DDS2PNG Repository">
</a>

</div>
