# DDS to PNG コンバーター

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="英语"> 英语
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="德语"> 德语
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="西班牙语"> 西班牙语
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="法语"> 法语
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="俄语"> 俄语
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="韩语"> 韩语
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="葡萄牙语"> 葡萄牙语
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="日语"> 日语
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="简体中文"> 简体中文
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="土耳其语"> 土耳其语
</a>

シンプルなグラフィカルインターフェースを備えた、軽量なPythonベースのDDSからPNGへの変換ツールです。

## 概要

DDS to PNG Converterは、直感的なグラフィカルインターフェースを使用して、DDS（DirectDraw Surface）形式のテクスチャファイルをPNG画像に変換するために開発されたデスクトップアプリケーションです。

このプロジェクトの目的は、ユーザーがコマンドライン操作を行うことなく、テクスチャファイルを簡単かつ手軽に変換できるようにすることです。

## 機能

- DDSファイルをPNG形式に変換。
- シンプルで使いやすいグラフィカルインターフェース。
- Pythonベースの軽量アプリケーション。
- 簡単なファイル選択と変換プロセス。

## 必要環境

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)：DDSファイルをPNG形式に変換するために使用します。アプリケーションと一緒に`assets`フォルダーに同梱されています。

### Texconv（任意ダウンロード）

プロジェクトに同梱されているTexconvが動作しない場合、または手動でダウンロードしたい場合は、以下のいずれかの方法を使用できます。

**PowerShell (Winget)：**
```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

インストールの確認：
```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**手動ダウンロード：**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## インストール

1. リポジトリをクローンします：
   ```bash
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```
2. プロジェクトディレクトリに移動します：
   ```bash
   cd "プロジェクトフォルダーのパス"
   ```
3. 必要な依存関係をインストールします：
   ```powershell
   pip install -r requirements.txt
   ```

### 仮想環境（任意）

Pythonの依存関係を他のプロジェクトから分離して管理するために、仮想環境を使用できます。

1. (PowerShellでスクリプトの実行エラーが発生した場合のみ) 現在のセッションで一時的にスクリプトの実行を許可してください：
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
2. 仮想環境を作成します：
   ```powershell
   python -m venv .venv
   ```
3. 仮想環境を有効化します：
   ```powershell
   .venv\Scripts\activate
   ```
4. 必要な依存関係をインストールします：
   ```powershell
   python -m pip install -r requirements.txt
   ```
5. 作業が終わったら、仮想環境を終了してください：
   ```powershell
   deactivate
   ```
   
## 使用方法

アプリケーションを起動します：
```bash
python Converter.pyw
```

DDSファイルを選択し、画面の指示に従ってPNG形式に変換してください。

## ビルド（EXEの作成）

Pythonアプリケーションを単一のEXEファイルに変換するには、以下の手順に従ってください。

**重要：** PowerShellは管理者としてではなく、通常のユーザーとして起動してください。管理者権限は必要ありません。

### 1. PowerShellを開く

1. Windowsのスタートメニューを開きます。
2. 検索欄に`PowerShell`または`Windows Terminal`と入力します。
3. Windows PowerShellまたはWindows Terminalを通常どおり起動します。
4. 「管理者として実行」は使用しないでください。

### 2. プロジェクトフォルダーに移動する

PowerShellで以下のコマンドを実行して、プロジェクトフォルダーに移動します：
```powershell
cd "D:\vectorrdevworks\Projeler\Yazılım Projeleri\Python\DDS2PNG"
```

### 3. アプリケーションのアイコンを埋め込む

以下のコマンドは`embed_icon.ps1`スクリプトを実行し、アプリケーションのアイコンをPythonファイルに埋め込みます。
```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**注意：** Windowsの実行ポリシーによってPowerShellスクリプトの実行がブロックされる場合があるため、`-ExecutionPolicy Bypass`を使用します。この設定は起動されたPowerShellプロセスにのみ適用されます。システム全体のセキュリティ設定は変更されません。

### 4. PyInstallerでビルドする

アイコンの埋め込みが完了したら、以下のコマンドを実行してEXEファイルを作成します：
```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.png" --name "DDS2PNG" "Converter.pyw"
```

**コマンドパラメーター：**

| パラメーター | 説明 |
|---|---|
| `--noconfirm` | 確認を求めずにビルドを実行します。 |
| `--clean` | 前回のビルドキャッシュを削除します。 |
| `--onefile` | 単一のEXEファイルを作成します。 |
| `--windowed` | コンソールウィンドウを表示しません。 |
| `--icon` | EXEファイルのアイコンを指定します。 |
| `--name` | 作成するEXEファイルの名前を指定します。 |

### 5. ビルド結果

ビルドが正常に完了すると、EXEファイルは以下のフォルダーに作成されます：
```text
dist\DDSConverter.exe
```

**新しいバージョンをビルドする際の手順：**

1. PowerShellを通常のユーザーとして開きます。
2. プロジェクトフォルダーに移動します。
3. アイコンの埋め込みコマンドを実行します。
4. PyInstallerのビルドコマンドを実行します。
5. `dist`フォルダーから生成されたEXEファイルを取得します。

## 開発者

**vectordevworks**

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細についてはLICENSEファイルを参照してください。