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

O Conversor de DDS para PNG é uma aplicação de desktop leve, baseada em Python, que permite converter ficheiros de textura no formato DDS (DirectDraw Surface) em imagens PNG. A sua interface gráfica simples permite selecionar ficheiros e realizar conversões facilmente.

## Visão geral

A aplicação converte ficheiros de textura DDS para o formato PNG através do Microsoft DirectXTex (Texconv). A conversão é efetuada através de uma interface gráfica, sem necessidade de utilizar comandos na linha de comandos.

A ferramenta Texconv é fornecida juntamente com a aplicação na pasta `assets`.

## Funcionalidades

- **Conversão de DDS para PNG:** Converte ficheiros DDS para o formato PNG.

- **Interface gráfica:** Disponibiliza uma interface simples que facilita a seleção de ficheiros e a conversão.

- **Suporte para Texconv:** Utiliza a ferramenta Microsoft DirectXTex para converter ficheiros DDS.

- **Fácil de utilizar:** Permite converter ficheiros sem recorrer à linha de comandos.


## Requisitos

- Windows

- Python 3.x

- Pillow

- Microsoft DirectXTex (Texconv)


Os módulos `tkinter`, `ctypes`, `json`, `math`, `os` e `pathlib` fazem parte da biblioteca padrão do Python.

O Texconv é utilizado para converter ficheiros DDS para o formato PNG e é fornecido com a aplicação na pasta `assets`.

### Texconv (Transferência opcional)

Se a versão do Texconv incluída no projeto não funcionar ou se pretender transferi-la manualmente, pode utilizar os métodos abaixo.

**PowerShell (Winget):**

```
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Para verificar a instalação:

```
winget list --id Microsoft.DirectXTex.Texconv
```

**Transferência manual:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Instalação

1. Clone o repositório:

```
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Abra a pasta do projeto.

3. Inicie o PowerShell nesta pasta.

4. Instale os pacotes Python necessários:

```
py -m pip install -r requirements.txt
```

## Ambiente virtual (opcional)

Pode utilizar um ambiente virtual para manter as dependências Python separadas de outros projetos:

1. Crie um ambiente virtual:

```
py -m venv .venv
```

2. Ative o ambiente virtual:

```
.\.venv\Scripts\Activate.ps1
```

3. Instale os pacotes Python necessários:

```
py -m pip install -r requirements.txt
```

4. Quando terminar, desative o ambiente virtual:

```
deactivate
```

## Utilização

1. Execute o ficheiro `DDSConverter.pyw`:

```
pyw .\DDSConverter.pyw
```

Em alternativa:

```
pythonw .\DDSConverter.pyw
```

2. Selecione o ficheiro DDS que pretende converter.

3. Pode selecionar a pasta `convert` existente como pasta de saída ou escolher qualquer outra pasta.

4. Efetue a conversão para o formato PNG.

## Compilação (criar EXE)

O PyInstaller é utilizado para converter a aplicação Python num único ficheiro EXE.

### 1. Aceder à pasta do projeto

Abra o PowerShell na pasta do projeto.

### 2. Incorporar o ícone e as imagens dos idiomas

Execute o script `embed_icon.ps1` através do comando abaixo. Este script incorpora no ficheiro Python o ícone da aplicação e as imagens PNG utilizadas na seleção do idioma.

```
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Nota:** O parâmetro `-ExecutionPolicy Bypass` é utilizado quando a política de execução do Windows pode impedir a execução de scripts do PowerShell. Este parâmetro aplica-se apenas ao processo do PowerShell iniciado e não altera as definições de segurança de todo o sistema.

### 3. Resultado da compilação

Quando a compilação for concluída com sucesso, o ficheiro EXE será criado na seguinte localização:

```
dist\DDS2PNG.exe
```

**Passos para compilar uma nova versão:**

1. Abra o PowerShell.

2. Certifique-se de que o PyInstaller está instalado.

3. Aceda à pasta do projeto.

4. Execute o script de compilação.

5. Pode encontrar o ficheiro EXE gerado na pasta `dist`.

## Programador

**vectordevworks**

## Licença

Este projeto está licenciado ao abrigo da Licença MIT. Consulte o ficheiro `LICENSE` no repositório do projeto para obter mais informações.
