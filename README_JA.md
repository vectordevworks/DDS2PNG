# DDS to PNG コンバーター



シンプルなグラフィカルユーザーインターフェースを備えた、Python ベースの軽量な DDS から PNG への変換ツールです。

## 概要

DDS to PNG Converter は、直感的なグラフィカルユーザーインターフェースを通じて、DDS（DirectDraw Surface）形式のテクスチャファイルを PNG 画像に変換するために開発されたデスクトップアプリケーションです。

このプロジェクトの目的は、ユーザーがコマンドライン操作を行うことなく、テクスチャファイルを簡単かつ手軽に変換できるようにすることです。

## 機能

- DDS ファイルを PNG 形式に変換。
- シンプルで使いやすいグラフィカルインターフェース。
- Python ベースの軽量アプリケーション。
- 簡単なファイル選択と変換操作。

## 必要条件

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)：DDSファイルをPNG形式に変換するために使用します。アプリケーションと一緒に `assets` フォルダーに含まれています。

### Texconv（任意ダウンロード）

プロジェクトに同梱されているTexconvが正常に動作しない場合、または手動でダウンロードしたい場合は、以下の方法を利用できます。

**PowerShell (Winget)：**
```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

インストールを確認するには：
```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**手動ダウンロード：**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## インストール

1. リポジトリをクローンします：
   ```
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
   ```
2. プロジェクトディレクトリに移動します：
   ```
   cd "プロジェクトディレクトリのパス"
   ```
3. 必要な依存関係をインストールします：
   ```
   pip install -r requirements.txt
   ```

### 仮想環境（任意）

Pythonの依存関係を他のプロジェクトから分離して管理するために、仮想環境を使用できます。

1. 仮想環境を作成します：
   ```
   python -m venv .venv
   ```
2. 仮想環境を有効化します：
   ```
   .venv\Scripts\activate
   ```
3. 必要な依存関係をインストールします：
   ```
   python -m pip install -r requirements.txt
   ```

**注意：** インストールおよび依存関係の管理には、PowerShellまたはコマンドプロンプト（CMD）を通常のユーザー権限で実行すれば十分です。管理者権限は必要ありません。

`pip`がシステム全体のPythonディレクトリに書き込もうとしてアクセス許可エラーが発生した場合は、ターミナルを管理者として実行するのではなく、仮想環境（`venv`）を使用することをおすすめします。

## インストール

1. リポジトリをクローンします。

   ```bash
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
   ```

2. プロジェクトディレクトリに移動します。

   ```bash
   cd "プロジェクトフォルダーのパス"
   ```

## 使用方法

アプリケーションを起動します。

```bash
python Converter.pyw
```

DDS ファイルを選択し、画面の指示に従って PNG 形式に変換してください。

## ビルド（EXE の作成）

以下の手順に従って、Python アプリケーションを単一の EXE ファイルに変換します。

**重要：** PowerShell は管理者としてではなく、通常のユーザーとして実行してください。管理者権限は必要ありません。

### 1. PowerShell を開く

1. Windows のスタートメニューを開きます。
2. 検索欄に `PowerShell` または `Windows Terminal` と入力します。
3. Windows PowerShell または Windows Terminal を通常どおり開きます。
4. 「管理者として実行」は選択しないでください。

### 2. プロジェクトディレクトリに移動する

PowerShell に次のコマンドを入力して、プロジェクトディレクトリに移動します。

```powershell
cd "D:\vectorrdevworks\Projeler\Yazılım Projeleri\Python\DDS-to-PNG-Converter"
```

### 3. アプリケーションアイコンを埋め込む

次のコマンドは `embed_icon.ps1` スクリプトを実行し、アプリケーションのアイコンを Python ファイルに埋め込みます。

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**注意：** Windows の実行ポリシーによって PowerShell スクリプトの実行が制限される場合があるため、`-ExecutionPolicy Bypass` を使用します。この設定は起動した PowerShell プロセスにのみ適用されます。システム全体のセキュリティ設定は変更されません。

### 4. PyInstaller でビルドする

アイコンの埋め込みが完了したら、次のコマンドを実行して EXE ファイルを作成します。

```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.ico" --name "DDS-to-PNG-Converter" "Converter.pyw"
```

**コマンドのパラメーター：**

| パラメーター | 説明 |
|---|---|
| `--noconfirm` | 確認を求めずにビルドします。 |
| `--clean` | 以前のビルドキャッシュを削除します。 |
| `--onefile` | 単一の EXE ファイルを作成します。 |
| `--windowed` | コンソールウィンドウを表示しません。 |
| `--icon` | EXE ファイルのアイコンを指定します。 |
| `--name` | 生成される EXE ファイルの名前を指定します。 |

### 5. ビルド出力

ビルドが正常に完了すると、EXE ファイルは次のディレクトリに作成されます。

```text
dist\DDS-to-PNG-Converter.exe
```

**新しいバージョンをビルドする際の手順：**

1. 通常のユーザーとして PowerShell を開きます。
2. プロジェクトディレクトリに移動します。
3. アイコン埋め込みコマンドを実行します。
4. PyInstaller のビルドコマンドを実行します。
5. `dist` ディレクトリから生成された EXE ファイルを取得します。

## 開発者

**vectordevworks**

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細については [LICENSE](LICENSE) ファイルを参照してください。