# プロジェクト構成の解剖

Sphinx プロジェクトは「**どのファイルが何の役割を持つか**」が分かると一気に理解できます。
このページでは、本サンプル（`sphinx/`）の実ファイルを題材に各要素を対応づけます。

## 全体像：source と build

Sphinx は **`source/`（入力）→ ビルド → `build/`（出力）** という一方向の流れです。

```{mermaid}
flowchart TD
    subgraph source["source/（あなたが編集する）"]
        conf["conf.py<br/>設定"]
        index["index.md<br/>トップ + toctree"]
        pages[".md / .rst<br/>各ページ"]
        static["_static/<br/>CSS・画像"]
        ext["_ext/<br/>自作拡張"]
    end
    conf --> build
    index --> build
    pages --> build
    static --> build
    ext --> build
    build{{"sphinx-build"}} --> out["build/html/<br/>build/latex/ など（出力・Git 管理外）"]
```

```{important}
`build/` は **生成物**なので Git で管理しません（`.gitignore` 済み）。
編集するのは常に `source/` 側です。「build を直接直す」のは禁物です。
```

## 各要素の役割

本サンプルのディレクトリ構成と、それぞれの責務は次の通りです。

```
sphinx/
├── requirements.txt        # Python 依存（このディレクトリ専用）
├── README.md               # サンプル全体の説明・操作手順
└── source/
    ├── conf.py             # ① 設定ファイル（プロジェクト名・拡張・出力設定）
    ├── index.md            # ② トップページ + toctree（目次ツリーの起点）
    ├── about-sphinx.md     #    各ページ（本文）
    ├── getting-started.md
    ├── api-reference.md
    ├── diagrams.md
    ├── revision-demo.md
    ├── meeting-notes/
    │   └── 2025-06.md      #    サブフォルダに置いてもよい
    ├── _ext/
    │   └── revision_mark.py # ③ 自作拡張（revision ディレクティブ）
    └── _static/            # ④ CSS・画像など静的ファイル
        ├── custom.css
        └── revision-mark.css
```

### ① conf.py — プロジェクトの設定

ビルドの挙動を決める **Python スクリプト**です。プロジェクト名・有効化する拡張・テーマ・PDF 設定などを書きます。
詳しくは {doc}`conf-py-guide` で逐条解説します。

### ② index.md と toctree — 目次ツリーの起点

`index.md` はトップページであると同時に、**`toctree` ディレクティブ**でサイト全体の目次構造を定義します。

````markdown
```{toctree}
:maxdepth: 2
:caption: 目次

getting-started      # ← 拡張子は書かない
api-reference
meeting-notes/2025-06 # ← サブフォルダはスラッシュ区切り
```
````

- ここに並べた順番が、サイドバー・目次・PDF の章順になる
- **`toctree` に載っていないページ**はビルドされるが「どこからもリンクされていない（orphan）」と警告される
- ネスト（あるページの toctree がさらに別の toctree を持つ）も可能で、大規模文書を階層化できる

```{tip}
新しいページを追加したら「① `source/` に置く」「② `toctree` に名前を足す」の 2 ステップが基本です。
どちらかを忘れるとビルド警告で気づけます。
```

### ③ _ext/ — 自作拡張

標準の拡張で足りない機能は、Python で**自作のディレクティブ**を書いて追加できます。
本サンプルの `_ext/revision_mark.py` は「改訂バー」を引く `revision` ディレクティブを定義しています
（表示例は {doc}`revision-demo` を参照）。
`conf.py` で `sys.path` に `_ext` を通し、`extensions` に名前を加えることで読み込まれます。

### ④ _static/ — 静的ファイル

CSS・画像・フォントなどを置きます。`conf.py` の `html_static_path` で指定し、
`html_css_files` で追加 CSS を読み込みます。本文からは相対パスで参照します。

```markdown
![システム構成図](_static/architecture.png)
```

## ビルドすると何が起きるか

`sphinx-build -b html source build/html` を実行すると、おおむね次の順で処理されます。

1. `conf.py` を読み込み、設定と拡張を初期化する
2. `source/` 内の `.md` / `.rst` を読み、**ドキュメントツリー（doctree）** という中間表現に変換する
3. `index.md` の `toctree` をたどってページ同士の関係・目次を解決する
4. 相互参照（`{doc}` `{ref}`）を解決し、**未解決の参照は警告**する
5. 選んだビルダ（`-b html` / `latex` / `epub`）で最終的な出力を `build/` に書き出す

```{note}
`-b`（builder）を変えるだけで出力形式が変わるのが Sphinx の強みです。
`html` / `latexpdf` / `epub` を同じソースから切り替えられます。
```

## 次に読む

- {doc}`conf-py-guide` — `conf.py` の各設定を読み解く
- {doc}`tutorial-from-scratch` — 実際に空から作って、この構成を自分の手で再現する
