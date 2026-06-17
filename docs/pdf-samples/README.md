# PDF サンプル（Pandoc 経由）

各 SSG の既存 Markdown 資産を **Pandoc + LuaLaTeX** で直接 PDF 変換したサンプルです。

## ファイル一覧

| ファイル | 元 SSG | 変換元 MD |
|---------|--------|----------|
| `sphinx.pdf` | Sphinx | `sphinx/source/` |
| `mkdocs.pdf` | MkDocs | `mkdocs/docs/` |
| `hugo.pdf` | Hugo | `hugo/content/` |
| `docusaurus.pdf` | Docusaurus | `docusaurus/docs/` |
| `astro.pdf` | Astro | `astro/src/content/docs/` |
| `eleventy.pdf` | Eleventy | `eleventy/src/` |

## 再生成コマンド

各 SSG 共通のオプション（`sphinx` を例に）：

```bash
pandoc \
  sphinx/source/index.md \
  sphinx/source/getting-started.md \
  sphinx/source/api-reference.md \
  sphinx/source/meeting-notes/2025-06.md \
  -o docs/pdf-samples/sphinx.pdf \
  --pdf-engine=lualatex \
  -V documentclass=ltjsarticle \
  -V classoption=a4paper \
  -V geometry:top=25mm,bottom=25mm,left=25mm,right=25mm \
  -H docs/pdf-samples/_pandoc-header.tex \
  --toc --toc-depth=2
```

**必要なパッケージ（Ubuntu/Debian）**

```bash
apt-get install pandoc texlive-luatex texlive-lang-japanese fonts-noto-cjk
```

## ヘッダー・フッター設定

`_pandoc-header.tex` でフォントとヘッダー・フッターを定義しています。

- フォント: IPA ex 明朝 / IPA ex ゴシック（`luatexja-preset` の `ipaex` プリセット）
- ヘッダー左: 章タイトル / 右: 文書タイトル固定文字列
- フッター左: 機密区分 / 中: ページ番号（X / 総ページ数）/ 右: ビルド日付

## SSG 固有記法の変換結果

各 SSG の Markdown には SSG 固有の記法が含まれており、Pandoc 変換後は下記のように扱われます。

| SSG | 固有記法 | Pandoc での扱い |
|-----|---------|----------------|
| Sphinx | `::::{warning}` admonition | 本文として展開（スタイルなし） |
| MkDocs | `=== "タブ名"` タブ | 見出しとして展開 |
| Docusaurus | `:::warning` admonition | 本文として展開（スタイルなし） |
| Astro | `:::caution` admonition | 本文として展開（スタイルなし） |
| Hugo | なし（素の Markdown） | 完全互換 |
| Eleventy | なし（素の Markdown） | 完全互換 |
