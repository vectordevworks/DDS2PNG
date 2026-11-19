# DDS2PNG

a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="英語"> 英語
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="ドイツ語"> ドイツ語
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="スペイン語"> スペイン語
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="フランス語"> フランス語
</a>
|
<strong>
  <img src="https://flagcdn.com/jp.svg" width="20" alt="日本語"> 日本語
</strong>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="韓国語"> 韓国語
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="ポルトガル語"> ポルトガル語
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="ロシア語"> ロシア語
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="簡体字中国語"> 簡体字中国語
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="トルコ語"> トルコ語
</a>

DDS から PNG への変換ツールは、DDS（DirectDraw Surface）形式のテクスチャファイルを PNG 画像に変換する、Python ベースの軽量なデスクトップアプリケーションです。シンプルなグラフィカルインターフェースで、ファイルの選択と変換を簡単に行えます。

## 概要

このアプリケーションは、Microsoft DirectXTex（Texconv）を使用して DDS テクスチャファイルを PNG 形式に変換します。変換はグラフィカルインターフェースから行うため、コマンドライン操作は必要ありません。

Texconv ツールはアプリケーションに同梱されており、`assets` フォルダーにあります。

## 機能

- **DDS から PNG への変換：** DDS ファイルを PNG 形式に変換します。

- **グラフィカルインターフェース：** ファイルの選択と変換を簡単に行えるシンプルな画面を提供します。

- **Texconv 対応：** DDS ファイルの変換に Microsoft DirectXTex ツールを使用します。

- **簡単な操作：** コマンドラインを使用せずに変換できます。


## 必要条件

- Windows

- Python 3.x

- Pillow

- Microsoft DirectXTex (Texconv)


`tkinter`、`ctypes`、`json`、`math`、`os`、`pathlib` モジュールは Python 標準ライブラリの一部です。

Texconv は DDS ファイルを PNG 形式に変換するために使用され、アプリケーションの `assets` フォルダーに同梱されています。

### Texconv (Texconv（任意のダウンロード）)

プロジェクトに同梱されている Texconv が動作しない場合、または手動でダウンロードしたい場合は、以下の方法を利用できます。

**PowerShell (Winget):**

```
winget install --id Microsoft.DirectXTex.Texconv --exact
```

インストールを確認するには：

```
winget list --id Microsoft.DirectXTex.Texconv
```

**手動ダウンロード:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## インストール

1. リポジトリをクローンします：

```
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. プロジェクトフォルダーを開きます。

3. このフォルダーで PowerShell を起動します。

4. 必要な Python パッケージをインストールします：

```
py -m pip install -r requirements.txt
```

## 仮想環境（任意）

Python の依存関係を他のプロジェクトから分離するために、仮想環境を使用できます：

1. 仮想環境を作成します：

```
py -m venv .venv
```

2. 仮想環境を有効にします：

```
.\.venv\Scripts\Activate.ps1
```

3. 必要な Python パッケージをインストールします：

```
py -m pip install -r requirements.txt
```

4. 作業が終わったら、仮想環境を無効にします：

```
deactivate
```

## 使い方

1. `DDSConverter.pyw` ファイルを実行します：

```
pyw .\DDSConverter.pyw
```

または、次のコマンドを使用します：

```
pythonw .\DDSConverter.pyw
```

2. 変換する DDS ファイルを選択します。

3. 出力先フォルダーには既存の `convert` フォルダー、または任意のフォルダーを指定できます。

4. PNG 形式への変換を実行します。

## ビルド（EXE の作成）

PyInstaller を使用して、Python アプリケーションを単一の EXE ファイルに変換します。

### 1. プロジェクトフォルダーへ移動

プロジェクトフォルダーで PowerShell を開きます。

### 2. アイコンと言語画像の埋め込み

以下のコマンドを実行して `embed_icon.ps1` スクリプトを起動します。このスクリプトは、アプリケーションのアイコンと言語選択に使用する PNG 画像を Python ファイルに埋め込みます。

```
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**注意：** `-ExecutionPolicy Bypass` パラメーターは、Windows の実行ポリシーによって PowerShell スクリプトの実行が妨げられる可能性がある場合に使用します。このパラメーターは起動する PowerShell プロセスにのみ適用され、システム全体のセキュリティ設定は変更しません。

### 3. ビルド結果

ビルドが正常に完了すると、EXE ファイルは次の場所に作成されます：

```
dist\DDS2PNG.exe
```

**新しいバージョンをビルドする手順：**

1. PowerShell を開きます。

2. PyInstaller がインストールされていることを確認します。

3. プロジェクトフォルダーに移動します。

4. ビルドスクリプトを実行します。

5. 生成された EXE ファイルは `dist` フォルダーにあります。

## 開発者

**vectordevworks**

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細については、プロジェクトリポジトリ内の `LICENSE` ファイルを参照してください。
