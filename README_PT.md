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
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Russo"> Russo
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
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japonês"> Japonês
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

DDS to PNG Converter é uma aplicação de ambiente de trabalho concebida para converter ficheiros de textura no formato DDS (DirectDraw Surface) em imagens PNG através de uma interface gráfica intuitiva.

O objetivo do projeto é permitir que os utilizadores convertam ficheiros de textura de forma simples e prática, sem terem de utilizar comandos na linha de comandos.

## Funcionalidades

- Conversão de ficheiros DDS para o formato PNG.
- Interface gráfica simples e intuitiva.
- Aplicação leve baseada em Python.
- Seleção fácil de ficheiros e processo de conversão simples.

## Requisitos

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv): utilizado para converter ficheiros DDS para o formato PNG. É fornecido com a aplicação na pasta `assets`.

### Texconv (Transferência opcional)

Se a versão do Texconv incluída no projeto não funcionar ou se pretender transferi-la manualmente, pode utilizar um dos seguintes métodos.

**PowerShell (Winget):**
```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Para verificar a instalação:
```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Transferência manual:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```
2. Aceda ao diretório do projeto:
   ```bash
   cd "CAMINHO DA PASTA DO PROJETO"
   ```
3. Instale as dependências necessárias:
   ```powershell
   pip install -r requirements.txt
   ```

### Ambiente virtual (Opcional)

Pode utilizar um ambiente virtual para manter as dependências Python separadas das de outros projetos.

1. (Apenas se o PowerShell apresentar um erro ao executar o script) Permita temporariamente a execução de scripts na sessão atual:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
2. Crie um ambiente virtual:
   ```powershell
   python -m venv .venv
   ```
3. Ative o ambiente virtual:
   ```powershell
   .venv\Scripts\activate
   ```
4. Instale as dependências necessárias:
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. Quando terminar, saia do ambiente virtual:
   ```powershell
   deactivate
   ```
  
## Utilização

Execute a aplicação:
```bash
python DDSConverter.pyw
```

Selecione o ficheiro DDS e siga as instruções apresentadas no ecrã para o converter para o formato PNG.

## Compilação (Criar EXE)

Siga os passos abaixo para converter a aplicação Python num único ficheiro EXE.

**Importante:** Abra o PowerShell como utilizador normal, e não como administrador. Não são necessários privilégios de administrador.

### 1. Abrir o PowerShell

1. Abra o menu Iniciar do Windows.
2. Escreva `PowerShell` ou `Windows Terminal` na caixa de pesquisa.
3. Abra normalmente o Windows PowerShell ou o Windows Terminal.
4. Não utilize a opção «Executar como administrador».

### 2. Aceder à pasta do projeto

Introduza o seguinte comando no PowerShell para aceder à pasta do projeto:
```powershell
cd "CAMINHO DA PASTA DO PROJETO"
```

### 3. Incorporar o ícone da aplicação

O comando seguinte executa o script `embed_icon.ps1` para incorporar o ícone da aplicação no ficheiro Python.
```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Nota:** É utilizado `-ExecutionPolicy Bypass` porque a política de execução do Windows pode impedir a execução de scripts PowerShell. Esta configuração aplica-se apenas ao processo PowerShell iniciado. As definições de segurança de todo o sistema não são alteradas.

### 4. Compilar com PyInstaller

Após concluir a incorporação do ícone, execute o seguinte comando para criar o ficheiro EXE:
```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.png" --name "DDS2PNG" "DDSConverter.pyw"
```

**Parâmetros do comando:**

| Parâmetro | Descrição |
|---|---|
| `--noconfirm` | Executa a compilação sem pedir confirmação. |
| `--clean` | Limpa a cache das compilações anteriores. |
| `--onefile` | Cria um único ficheiro EXE. |
| `--windowed` | Não apresenta uma janela de consola. |
| `--icon` | Define o ícone do ficheiro EXE. |
| `--name` | Define o nome do ficheiro EXE a criar. |

### 5. Resultado da compilação

Quando a compilação for concluída com sucesso, o ficheiro EXE será criado na seguinte pasta:
```text
dist\DDSConverter.exe
```

**Ordem dos passos ao compilar uma nova versão:**

1. Abra o PowerShell como utilizador normal.
2. Aceda à pasta do projeto.
3. Execute o comando para incorporar o ícone.
4. Execute o comando de compilação do PyInstaller.
5. Obtenha o ficheiro EXE criado na pasta `dist`.

## Desenvolvedor

**vectordevworks**

## Licença

Este projeto está licenciado ao abrigo da Licença MIT. Consulte o ficheiro LICENSE para obter mais informações.