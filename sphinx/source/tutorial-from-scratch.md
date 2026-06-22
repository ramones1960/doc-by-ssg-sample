# ゼロから文書を作るチュートリアル

このページでは、**空のディレクトリ**から始めて、最初の HTML を表示し、
ページ追加・相互参照・テーマ適用、そして **PDF / ePub 出力**までを順に体験します。
本サンプルの `sphinx/` は、このチュートリアルの完成形だと考えてください。

```{note}
コマンドは macOS / Linux 前提です。Windows は仮想環境の有効化を
`.venv\Scripts\activate` に読み替えてください。
```

## STEP 0. 仮想環境を作る

Python 製ツールなので、システムの Python を汚さないよう **venv** を使います。

```bash
mkdir my-docs && cd my-docs
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install sphinx myst-parser furo
```

- `sphinx` … 本体
- `myst-parser` … Markdown を書けるようにする拡張
- `furo` … モダンな HTML テーマ

## STEP 1. sphinx-quickstart でひな型を作る

```bash
sphinx-quickstart
```

対話式に聞かれます。最初はおすすめの回答で進めてください。

| 質問 | おすすめの回答 | 意味 |
|---|---|---|
| Separate source and build directories | **y** | `source/` と `build/` を分ける（推奨） |
| Project name | （任意） | プロジェクト名 |
| Author name(s) | （任意） | 著者 |
| Project release | `1.0` | バージョン |
| Project language | `ja` | 日本語 |

完了すると次のような構成ができます。

```
my-docs/
├── build/            # 出力（まだ空）
├── source/
│   ├── conf.py       # 設定
│   ├── index.rst     # トップページ（最初は .rst）
│   ├── _static/
│   └── _templates/
├── make.bat
└── Makefile
```

## STEP 2. 最初の HTML をビルドする

まだ何も書いていませんが、もうビルドできます。

```bash
sphinx-build -b html source build/html
```

`build/html/index.html` をブラウザで開くと、空の文書が表示されます。
**「動く最小状態」をまず確認する**のが大事です。

```{tip}
毎回ビルドするのが面倒なら、ライブリロードが便利です。
`pip install sphinx-autobuild` の後に `sphinx-autobuild source build/html` を実行すると、
保存するたびにブラウザが自動更新されます。
```

## STEP 3. Markdown を書けるようにする

`conf.py` を開き、`extensions` と `html_theme` を編集します。

```python
extensions = [
    "myst_parser",   # Markdown(MyST) を有効化
]

html_theme = "furo"  # alabaster → furo に変更

# Markdown のうち、便利な追加記法を有効化
myst_enable_extensions = ["colon_fence", "deflist", "tasklist"]
```

これで `.md` ファイルが書けるようになります（`source_suffix` は `myst_parser` が自動で `.md` を追加します）。

## STEP 4. トップページを Markdown にする

`source/index.rst` を削除し、代わりに `source/index.md` を作ります。

````markdown
# My Document

ようこそ。これは Sphinx で作った最初の文書です。

```{toctree}
:maxdepth: 2
:caption: 目次

getting-started
```

:::{note}
これは MyST の注釈ボックスです。
:::
````

再ビルドして、トップページが置き換わったことを確認します。

```bash
sphinx-build -b html source build/html
```

## STEP 5. ページを追加して toctree につなぐ

`source/getting-started.md` を新規作成します。

```markdown
# はじめに

(setup-label)=
## セットアップ

ここにセットアップ手順を書きます。
```

`(setup-label)=` は、この見出しに **ラベル**を付ける MyST の記法です（次の STEP で参照します）。

すでに STEP 4 の `toctree` に `getting-started` を書いてあるので、
再ビルドすればサイドバーに新しいページが並びます。

```{important}
ページ追加は必ず「① `source/` にファイルを置く」＋「② `toctree` に名前を足す」の 2 ステップ。
`toctree` に載せ忘れると「document isn't included in any toctree」と警告されます。
```

## STEP 6. 相互参照でリンクする

`index.md` に、壊れにくい**相互参照**を足してみます。

```markdown
- ページ全体へ: {doc}`はじめに <getting-started>`
- 見出しへ:     {ref}`セットアップ手順 <setup-label>`
```

`{doc}` はページ、`{ref}` はラベル付き見出しへの参照です。
**存在しないページやラベルを指すとビルド時に警告**されるので、リンク切れに気づけます。

## STEP 7. PDF を出力する（LaTeX 経由）

ここまでで HTML は完成です。同じソースから **PDF** を作ります。
PDF は LaTeX を経由するため、TeX 環境が必要です。

```bash
# 日本語 PDF に必要な TeX（Debian/Ubuntu の例）
sudo apt-get install -y --no-install-recommends \
  texlive-latex-recommended texlive-latex-extra \
  texlive-fonts-recommended texlive-lang-japanese latexmk
```

`conf.py` に日本語向けエンジンを指定します。

```python
latex_engine = "uplatex"   # 日本語は uplatex + dvipdfmx が定番
```

ビルドします。

```bash
sphinx-build -M latexpdf source build
# → build/latex/<プロジェクト名>.pdf が生成される
```

```{tip}
`-M latexpdf` は `latexmk` を使って「LaTeX を複数回実行 → PDF 化」まで自動でやってくれます。
表紙・目次・ヘッダー/フッターを凝りたくなったら {doc}`conf-py-guide` の `latex_elements` を参照してください。
本サンプルの `conf.py` が実例です。
```

## STEP 8. ePub を出力する

電子書籍形式の ePub は、**追加設定なし**でビルドできます。

```bash
sphinx-build -b epub source build/epub
# → build/epub/<プロジェクト名>.epub
```

必要ならメタ情報を `conf.py` に足します。

```python
epub_title = "My Document"
epub_author = "Your Name"
epub_language = "ja"
```

```{note}
ここまでで分かるとおり、**ソースは 1 つのまま `-b` / `-M` を変えるだけ**で
HTML・PDF・ePub を作り分けられます。これが Sphinx の「Single Source, Multiple Output」です。
```

## STEP 9. 拡張で機能を足す（発展）

最後に、よく使う拡張を 2 つ紹介します。`conf.py` の `extensions` に足すだけです。

| 拡張 | できること |
|---|---|
| `sphinx.ext.autodoc` + `sphinx.ext.napoleon` | Python の docstring から API 文書を自動生成 |
| `sphinx_copybutton` | コードブロックにコピーボタンを付ける |
| `sphinxcontrib.mermaid` | Mermaid 図を埋め込む（{doc}`diagrams` 参照） |

自作のディレクティブを作りたくなったら、`_ext/` に Python を置く方法を
`_ext/revision_mark.py`（{doc}`revision-demo` のデモ）が示しています。

## まとめ

1. **venv → quickstart → ビルド**で「動く最小状態」を作る
2. `extensions` と `toctree` を足しながら育てる
3. 参照は `{doc}` / `{ref}` で壊れにくくする
4. 同じソースから `-b` / `-M` で **HTML / PDF / ePub** を出し分ける

ここから先は {doc}`conf-py-guide` で設定を深掘りし、本サンプルの各ページを実例として読んでみてください。
