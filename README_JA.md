<div align="center">

# DDS2PNG

### DDS から PNG への変換ツール

DDS（DirectDraw Surface）形式のテクスチャファイルを簡単に PNG に変換します。

Python 製の軽量で使いやすいデスクトップアプリケーションです。

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

### 🌐 言語の選択

<a href="README.md"><img src="https://flagcdn.com/gb.svg" width="20" alt="English"> English</a> |
<a href="README_DE.md"><img src="https://flagcdn.com/de.svg" width="20" alt="Deutsch"> Deutsch</a> |
<a href="README_ES.md"><img src="https://flagcdn.com/es.svg" width="20" alt="Español"> Español</a> |
<a href="README_FR.md"><img src="https://flagcdn.com/fr.svg" width="20" alt="Français"> Français</a> |
<a href="README_PT.md"><img src="https://flagcdn.com/pt.svg" width="20" alt="Português"> Português</a> |
<a href="README_RU.md"><img src="https://flagcdn.com/ru.svg" width="20" alt="Русский"> Русский</a> |
<strong><img src="https://flagcdn.com/jp.svg" width="20" alt="日本語"> 日本語</strong> |
<a href="README_KO.md"><img src="https://flagcdn.com/kr.svg" width="20" alt="한국어"> 한국어</a> |
<a href="README_ZH_CN.md"><img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文</a> |
<a href="README_TR.md"><img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe</a>

---

### 📑 目次

<a href="#genel-bakis">概要</a>
<a href="#ozellikler">機能</a>
<a href="#gereksinimler">必要条件</a>
<a href="#kurulum">インストール</a>
<a href="#sanal-ortam">仮想環境（任意）</a>
<a href="#kullanim">使い方</a>
<a href="#derleme">ビルド（EXE の作成）</a>
<a href="#gelistirici">開発者</a>
<a href="#lisans">ライセンス</a>

</div>

---

<a id="genel-bakis"></a>
## 🔍 概要

**DDS2PNG** は、DDS（DirectDraw Surface）形式のテクスチャファイルを PNG に変換できる、軽量な Python 製デスクトップアプリケーションです。

シンプルな GUI からファイルを選択して簡単に変換できます。コマンドライン操作は必要ありません。

変換には Microsoft DirectXTex（Texconv）を使用します。

Texconv ツールはアプリケーションとともに `assets` フォルダーに同梱されています。

<a id="ozellikler"></a>
## ✨ 機能

- **DDS から PNG への変換：** DDS ファイルを PNG 形式に変換します。
- **グラフィカルインターフェース：** ファイルの選択と変換を簡単に行えるシンプルな画面を提供します。
- **Texconv 対応：** Microsoft DirectXTex を使用して DDS ファイルを変換します。
- **簡単操作：** コマンドラインを使わずにファイルを変換できます。

<a id="gereksinimler"></a>
## 📋 必要条件

- Windows
- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)

`tkinter`、`ctypes`、`json`、`math`、`os`、`pathlib` は Python 標準ライブラリの一部です。

Texconv ツールはアプリケーションとともに `assets` フォルダーに同梱されています。

### Texconv (Texconv（任意ダウンロード）)

プロジェクトに同梱されている Texconv が動作しない場合、または手動でダウンロードしたい場合は、以下の方法を利用できます。

**PowerShell (Winget):**

```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

インストールを確認するには：

```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**手動ダウンロード：**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

<a id="kurulum"></a>
## 📥 インストール

1. リポジトリをクローンします：

```bash
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. プロジェクトフォルダーを開きます。

3. プロジェクトフォルダーで PowerShell を起動します。

4. 必要な Python パッケージをインストールします：

```powershell
py -m pip install -r requirements.txt
```

<a id="sanal-ortam"></a>
## 🐍 仮想環境（任意）

仮想環境を使用すると、Python の依存関係を他のプロジェクトから分離できます。

**1. 仮想環境を作成：**

```powershell
py -m venv .venv
```

**2. 仮想環境を有効化：**

```powershell
.\.venv\Scripts\Activate.ps1
```

**3. 必要な依存関係をインストール：**

```powershell
py -m pip install -r requirements.txt
```

**4. 作業が終わったら仮想環境を無効化：**

```powershell
deactivate
```

**CMD（コマンドプロンプト）での有効化：**

PowerShell の代わりに CMD を使用する場合：

```cmd
.venv\Scripts\activate.bat
```

仮想環境を終了するには：

```cmd
deactivate
```

### 仮想環境の有効化に関する問題

PowerShell の実行ポリシーにより、仮想環境の有効化がブロックされる場合があります。

その場合は、次のコマンドを実行してください：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

その後、仮想環境を再度有効化します：

```powershell
.\.venv\Scripts\Activate.ps1
```

この設定は現在の PowerShell セッションにのみ適用されます。新しいセッションを開くと既定の設定に戻ります。

### 有効化せずに仮想環境を使用する

仮想環境の有効化は必須ではありません。有効化に失敗した場合は、Python と pip の実行ファイルを直接呼び出して引き続き使用できます。

**依存関係をインストールするには：**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**アプリケーションを実行するには：**

```powershell
.\.venv\Scripts\python.exe DDSConverter.pyw
```

**注意：** 仮想環境の作成、有効化、依存関係のインストール、無効化に管理者権限は必要ありません。ただし、Python が正しくインストールされ、必要なファイルへのアクセス権があることを確認してください。

<a id="kullanim"></a>
## 🚀 使い方

1. `DDSConverter.pyw` ファイルを実行します：

```powershell
pyw .\DDSConverter.pyw
```

または：

```powershell
pythonw .\DDSConverter.pyw
```

2. 変換する DDS ファイルを選択します。

3. 出力先には既存の `convert` フォルダー、または任意のフォルダーを指定できます。

4. PNG 形式への変換を実行します。

<a id="derleme"></a>
## 📦 ビルド（EXE の作成）

Python アプリケーションを単一の EXE ファイルにパッケージ化するには PyInstaller を使用します。

### 1. プロジェクトフォルダーへ移動

まず DDS2PNG プロジェクトフォルダーを開きます。次のいずれかの方法で、そのフォルダー内にターミナルを起動できます。

**方法 1：エクスプローラーからターミナルを開く**

1. エクスプローラーで DDS2PNG プロジェクトフォルダーを開きます。

2. アドレスバーに `cmd` または `powershell` と入力します。

3. Enter キーを押します。

ターミナルがプロジェクトフォルダー内で直接開きます。

**方法 2：ターミナルからプロジェクトフォルダーへ移動**

CMD または PowerShell を開き、以下の該当するコマンドを使用します。

**CMD:**

```cmd
cd /d "PROJE_KLASORUNUN_YOLU"
```

**PowerShell:**

```powershell
Set-Location -LiteralPath "PROJE_KLASORUNUN_YOLU"
```

`PROJE_KLASORUNUN_YOLU` を、お使いのコンピューター上にある DDS2PNG プロジェクトフォルダーの完全なパスに置き換えてください。

**注意：** 管理者として実行する必要はありません。通常のユーザー権限で十分です。

### 2. EXE のビルド

プロジェクトの `scripts` フォルダーにある `buid.ps1` スクリプトは、PyInstaller を使用してアプリケーションを EXE 形式にビルドします。

ビルドスクリプトは次の処理を自動的に実行します：

- 必要なプロジェクトファイルを確認します。
- PyInstaller のインストール状況を確認します。
- 以前のビルドファイルを削除します。
- `icon.ico` を EXE のアイコンとして使用します。
- `assets` フォルダーを EXE ファイルに含めます。
- ビルド結果を確認します。

**CMD から実行：**

```cmd
powershell -ExecutionPolicy Bypass -File "scripts\buid.ps1"
```

**PowerShell から実行：**

```powershell
.\scripts\buid.ps1
```

### 3. ビルド結果

ビルドが正常に完了すると、EXE ファイルは次の場所に作成されます：

```text
dist\DDS2PNG.exe
```

**新しいバージョンをビルドする手順：**

1. DDS2PNG プロジェクトフォルダーを開きます。

2. アドレスバーに `cmd` または `powershell` と入力してターミナルを起動するか、既存のターミナルでプロジェクトフォルダーへ移動します。

3. ビルドスクリプトを実行します。

4. 生成された EXE ファイルは `dist` フォルダーにあります。

### 4. アプリケーションの起動

ビルドが正常に完了したら、次のコマンドでアプリケーションを起動します：

```powershell
dist\DDS2PNG.exe
```

または、`dist` フォルダーを開き、`DDS2PNG.exe` をダブルクリックします。

**注意：** アプリケーションの起動に CMD や PowerShell の管理者権限は必要ありません。

<a id="gelistirici"></a>
## 👨‍💻 開発者

<div align="center">

**VectorDevWorks**

<a href="https://github.com/vectordevworks">
  <img src="https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github" alt="VectorDevWorks GitHub">
</a>

</div>

<a id="lisans"></a>
## 📄 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細はリポジトリ内の `LICENSE` ファイルを参照してください。

---

<div align="center">

**VectorDevWorks によって開発されました。**

⭐ プロジェクトを気に入ったら、GitHub でスターを付けてください！

<a href="https://github.com/vectordevworks/DDS2PNG">
  <img src="https://img.shields.io/badge/Project%20Repository-DDS2PNG-blue?style=for-the-badge&logo=github" alt="DDS2PNG Repository">
</a>

</div>
