# conf.py 設定ガイド

`conf.py` は Sphinx プロジェクトの**設定ファイル**です。ただの設定ではなく **Python スクリプト**なので、
変数を代入するだけでなく、パスを通したり条件分岐を書いたりもできます。

このページでは「**最小構成**」から始め、本サンプルの `conf.py` を**逐条で**読み解きます。

## まずは最小構成

`sphinx-quickstart` が生成する最小限の `conf.py` は、実質これだけです。

```python
project = "My Document"        # プロジェクト名
author = "Your Name"           # 著者
release = "1.0"                # バージョン

extensions = []                # 有効化する拡張（最初は空でよい）
templates_path = ["_templates"]
exclude_patterns = []

html_theme = "alabaster"       # HTML テーマ
```

これだけで HTML はビルドできます。ここに**必要な分だけ設定を足していく**のが基本方針です。

## 本サンプルの conf.py を逐条で読む

以下、本サンプルの設定を区分ごとに解説します。

### 自作拡張のパスを通す

```python
import os
import sys
sys.path.insert(0, os.path.abspath("_ext"))
```

`conf.py` は Python なので、`_ext/` を **import 検索パスに追加**しています。
これにより後述の `extensions` で自作の `revision_mark` を名前で読み込めます。

### メタ情報

```python
project = "社内プロジェクト文書"
copyright = "2025, 開発チーム（社内限定）"
author = "開発チーム"
release = "1.0"
```

タイトル・著作権表示・版番号など。HTML のフッターや PDF の表紙に反映されます。

### extensions — 有効化する拡張

```python
extensions = [
    "myst_parser",            # Markdown(MyST) を解釈する
    "sphinx_copybutton",      # コードブロックにコピーボタン
    "sphinx.ext.todo",        # TODO 管理
    "sphinx.ext.intersphinx", # 他プロジェクト文書を相互参照
    "revision_mark",          # 改訂マーク（自作拡張）
    "sphinxcontrib.mermaid",  # Mermaid 図
]
```

**Sphinx の機能はここで足す**のが基本です。`sphinx.ext.*` は標準同梱、
`myst_parser` / `sphinx_copybutton` / `sphinxcontrib.mermaid` は `requirements.txt` で導入する外部拡張、
`revision_mark` は `_ext/` の自作拡張です。

```{tip}
よく使う標準拡張に `sphinx.ext.autodoc`（docstring から API 文書を自動生成）、
`sphinx.ext.napoleon`（Google/NumPy 形式の docstring 対応）があります。
Python ライブラリの文書化ではほぼ必須です。
```

### source_suffix — 受け付ける拡張子

```python
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
```

`.rst` と `.md` の**両方を受け付ける**設定です。`myst_parser` を入れた上でこう書くと、
1 プロジェクト内で reST と Markdown を混在できます。

### myst_enable_extensions — MyST の追加機能

```python
myst_enable_extensions = [
    "colon_fence",  # ::: で囲む記法（admonition を書きやすく）
    "deflist",      # 定義リスト
    "tasklist",     # - [ ] チェックリスト
]
```

MyST は既定では「素の Markdown + α」です。`colon_fence` を有効にすると
`:::{note} ... :::` のように**バッククォートなしで注釈ボックス**が書けます
（本サンプルの `warning` / `danger` ボックスはこれ）。

### 言語・テンプレート・除外

```python
language = "ja"
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
```

`language = "ja"` は UI 文言・全文検索の分かち書き・PDF の章見出し（「第 1 章」など）に効きます。
`exclude_patterns` はビルド対象から外すパターンです。

### HTML 出力

```python
html_theme = "furo"
html_title = "社内プロジェクト文書"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
```

`furo` はモダンな人気テーマ（`requirements.txt` で導入）。
`html_static_path` で静的ファイルの場所を指定し、`html_css_files` で追加 CSS を読み込みます。

### intersphinx — 他プロジェクトとの相互参照

```python
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
```

Python 公式ドキュメントなど**外部プロジェクトの見出し**を `{ref}` で参照できるようになります。

### todo

```python
todo_include_todos = True
```

`sphinx.ext.todo` の TODO を**本文に表示**する設定（`False` なら非表示で管理だけ）。

## PDF（LaTeX）出力の設定

ここからは出力形式を **PDF（LaTeX 経由）**に広げる設定です。
Sphinx は HTML だけでなく**表紙・目次・ヘッダー/フッター付きの納品 PDF**を生成できます。

### エンジンと文書定義

```python
latex_engine = "uplatex"   # 日本語は uplatex + dvipdfmx が定番
latex_documents = [
    ("index", "shakai-project-docs.tex", "社内プロジェクト文書", "開発チーム", "manual"),
]
latex_toplevel_sectioning = "chapter"  # トップ見出しを「章」扱い
```

日本語 PDF は **uplatex（jsbook クラス）+ dvipdfmx** の組み合わせが最も実績があります。
`latex_documents` は `(起点ファイル, 出力 .tex 名, タイトル, 著者, テーマ)` のタプルです。

### latex_elements — 表紙・目次・ヘッダー/フッター

`latex_elements` 辞書で LaTeX の各部分を差し替えます。本サンプルでは次を設定済みです。

| キー | 役割 |
|---|---|
| `preamble` | パッケージ読み込み・`revisionblock` 環境（改訂バー）・fancyhdr 定義 |
| `maketitle` | 表紙（機密区分・タイトル・版・発行日） |
| `tableofcontents` | 前付けはローマ数字、本文はアラビア数字でページ番号を振る |
| `papersize` / `pointsize` | A4・11pt |

```{note}
`preamble` 内の `revisionblock` 環境は、自作拡張 `revision_mark` が
**PDF 出力時に**呼び出します。HTML では CSS、PDF では LaTeX 環境、と
**出力ごとに描き分ける**のが Sphinx 拡張の典型パターンです。
```

LaTeX をカスタマイズしなくても、`latex_elements` を空のままにすれば
Sphinx 既定の体裁で PDF は出力されます。凝った体裁が必要なときだけ触れば十分です。

## ePub 出力の設定

ePub（電子書籍）は **追加設定なしでもビルド可能**です。必要なら次のようなメタ情報を足します。

```python
epub_title = "社内プロジェクト文書"
epub_author = "開発チーム"
epub_language = "ja"
epub_show_urls = "footnote"  # リンク URL を脚注に出す
```

ビルドは `sphinx-build -b epub source build/epub` です（{doc}`tutorial-from-scratch` 参照）。

## 設定変更が効かないときは

`conf.py` を変えても反映されないときは、**`build/` を消して再ビルド**してください。
Sphinx は変更のないページをキャッシュするため、設定変更が一部に反映されないことがあります。

```bash
rm -rf build && sphinx-build -b html source build/html
# または: sphinx-build -E ...（環境を作り直す）
```

:::{warning}
上記のように `build/` を消すか `-E` オプションを付けて**環境を作り直す**と、
キャッシュ起因の「設定が反映されない」問題はたいてい解消します。
:::

## 次に読む

- {doc}`tutorial-from-scratch` — この設定を自分で書きながら、HTML・PDF・ePub をビルドする
- {doc}`structure` — `conf.py` が他のファイルとどう連携するか
