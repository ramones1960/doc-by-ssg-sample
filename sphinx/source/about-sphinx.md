# Sphinx とは / 設計思想

このページは「Sphinx をはじめて触る人」向けに、**Sphinx がどういう考えで作られているか**を解説します。
個別の操作手順より先に、ここで全体像をつかんでおくと後がスムーズです。

## ひとことで言うと

Sphinx は **「1 つのソースから、HTML・PDF・ePub など複数の形式の文書を生成する」** ためのドキュメントビルダーです。
もともと **Python 公式ドキュメント**のために作られ、今では多くの OSS・社内文書で使われています。

```{mermaid}
flowchart LR
    subgraph ソース[ソース（あなたが書くもの）]
        A[".rst / .md ファイル"]
        B["conf.py（設定）"]
    end
    A --> S{{Sphinx ビルド}}
    B --> S
    S --> H["HTML（Web サイト）"]
    S --> P["PDF（LaTeX 経由）"]
    S --> E["ePub（電子書籍）"]
```

ポイントは、**書くのはプレーンテキスト 1 種類だけ**で、出力形式はビルド時に選べるということです。
「Web 用」「印刷・納品用 PDF」を別々に作る必要がありません（**Single Source, Multiple Output**）。

## なぜそう作られているのか — 4 つの設計思想

### 1. ドキュメントを「ソースコード」として扱う（Docs as Code）

文書を `.rst` / `.md` というテキストで書くため、**Git で差分管理・レビュー・履歴追跡**ができます。
Word のバイナリファイルと違い、「誰が・いつ・どこを変えたか」が `git diff` で分かります。
本サンプルが Mermaid 図（テキストで図を書く）を採用しているのも同じ理由です。

### 2. 「壊れない参照」を仕組みで保証する

Sphinx 最大の特徴が **相互参照（cross-reference）** です。
ページや見出しを **ID（ラベル）** で参照するため、リンク先を移動・改名しても壊れにくく、
**存在しない参照はビルド時に警告**として検出されます。

```markdown
ページ参照: {doc}`開発ガイド <getting-started>`
見出し参照: {ref}`環境構築 <setup-label>`
```

大規模な仕様書ほど「リンク切れの放置」が起きがちですが、Sphinx はそれをビルドで機械的に防ぎます。

### 3. 1 ソースから複数フォーマットへ出力する

同じソースから **HTML / PDF（LaTeX）/ ePub / man ページ** を生成できます。
「Web で公開しつつ、PDF で納品する」といった要件に、ソースを二重管理せず対応できます。
（PDF・ePub の具体的な作り方は {doc}`tutorial-from-scratch` を参照）

### 4. 拡張（extension）で機能を足せる

Sphinx 本体は最小限で、機能は **拡張**として `conf.py` の `extensions` に足していきます。

| 拡張 | 役割 |
|---|---|
| `myst_parser` | Markdown(MyST) を書けるようにする |
| `sphinx.ext.autodoc` | Python の docstring から API 文書を自動生成 |
| `sphinx.ext.intersphinx` | 他プロジェクトの文書（Python 公式など）を相互参照 |
| `sphinxcontrib.mermaid` | Mermaid 図を埋め込む |

本サンプルの `_ext/revision_mark.py` のように、**自作の拡張**でディレクティブを追加することもできます。
（どの拡張を有効化しているかは {doc}`conf-py-guide` を参照）

## reStructuredText と MyST(Markdown) の関係

Sphinx の **本来のフォーマットは reStructuredText（`.rst`）** です。
しかし `.rst` は記法の学習コストが高いため、**MyST という拡張で Markdown（`.md`）も書ける**ようになっています。

| | reStructuredText (`.rst`) | MyST Markdown (`.md`) |
|---|---|---|
| 位置づけ | Sphinx 標準・最も機能が豊富 | Markdown で reST 相当の機能を使う |
| 学習コスト | 高め（独自記法） | 低め（Markdown ベース） |
| ディレクティブ | `.. note::` | ```` ```{note} ```` または `:::{note}` |
| 本サンプル | 混在可 | **こちらを採用** |

どちらも **同じ「ディレクティブ」「ロール」という仕組み**の上に乗っているのがポイントです。

- **ディレクティブ**: ブロック要素を作る命令（注釈ボックス・図・目次ツリーなど）
- **ロール**: 文中のインライン要素（相互参照 `{doc}` `{ref}` など）

```{note}
本サンプルは Markdown(MyST) + Furo テーマで統一しています。
`.rst` と `.md` は 1 つのプロジェクト内で混在できるので、
チームの好みや既存資産に合わせて選べます。
```

## 次に読む

- {doc}`structure` — プロジェクトの構成（`source/` `build/` `conf.py` の関係）を解剖する
- {doc}`conf-py-guide` — 設定ファイル `conf.py` を逐条で読む
- {doc}`tutorial-from-scratch` — 空のディレクトリから最初の文書をビルドする
