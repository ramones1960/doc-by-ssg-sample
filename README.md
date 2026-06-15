# SSG 比較サンプル — 社内文書への活用

静的サイトジェネレータ（SSG）を使って社内文書・プロジェクト情報を管理するためのサンプル集です。

## 比較対象

| SSG | 言語 | 特徴 | 向いている用途 |
|---|---|---|---|
| [MkDocs](./mkdocs/) | Python | シンプル・Material テーマが強力 | 技術文書・API リファレンス |
| [Sphinx](./sphinx/) | Python | 相互参照・autodoc・PDF 出力 | ライブラリ API 文書・厳密な仕様書 |
| [Hugo](./hugo/) | Go | 超高速ビルド・テーマが豊富 | 大量ページの社内 Wiki |
| [Docusaurus](./docusaurus/) | React / JS | バージョン管理・全文検索 | プロジェクト仕様書・変更履歴 |
| [Astro](./astro/) | JS (Starlight) | 軽量・検索内蔵・モダン | パフォーマンス重視のポータル |
| [Eleventy](./eleventy/) | JavaScript | 設計自由度が高い・軽量 | カスタマイズしたいチーム |

## リポジトリ構成（モノレポ）

各 SSG はディレクトリで分離され、依存（npm / pip）も**それぞれのディレクトリに閉じています**。
他の SSG をインストールせずに、試したいものだけをセットアップできます。

```
doc-by-ssg-sample/
├── README.md
├── mkdocs/        … requirements.txt（Python）
├── sphinx/        … requirements.txt（Python）
├── hugo/          … Go バイナリのみ（パッケージ管理なし）
├── docusaurus/    … package.json（npm）
├── astro/         … package.json（npm）
└── eleventy/      … package.json（npm）
```

各ディレクトリの `README.md` に、その SSG の特色・長所/短所・セットアップ手順を記載しています。

## 共通サンプル文書

各 SSG に同じ内容の文書を移植しています。記法の違い（注釈ボックス・サイドバー定義など）を見比べてください。

- **プロジェクト概要** — 背景・目的・体制
- **開発ガイド** — 環境構築・ブランチ運用
- **API リファレンス** — エンドポイント一覧
- **議事録** — 定例会議のサンプル

## 前提：社内利用を想定した設計方針

- 一般公開しない（ビルド成果物は社内ネットワーク or GitHub Pages の private 環境）
- 認証は別途 nginx / Cloudflare Access 等で行う
- Markdown で執筆し Git で変更管理

## 各 SSG を試す

```bash
# MkDocs（Python）
cd mkdocs && pip install -r requirements.txt && mkdocs serve

# Sphinx（Python）
cd sphinx && pip install -r requirements.txt && sphinx-build -b html source build/html

# Hugo（Go バイナリ）
cd hugo && hugo server

# Docusaurus（npm）
cd docusaurus && npm install && npm run start

# Astro / Starlight（npm）
cd astro && npm install && npm run dev

# Eleventy（npm）
cd eleventy && npm install && npm run serve
```

## 選定チェックリスト

- [ ] チームの主要言語は何か（Python → MkDocs / Sphinx、JS → Docusaurus / Astro / 11ty、Go → Hugo）
- [ ] Python ソースから API 文書を自動生成したいか（Sphinx の autodoc が有利）
- [ ] バージョン管理が必要か（Docusaurus が有利）
- [ ] 全文検索を手軽に使いたいか（Astro / Starlight は標準内蔵）
- [ ] デザインのカスタマイズ度は（11ty が最大自由度）
- [ ] ページ数・ビルド速度（大規模なら Hugo）
- [ ] PDF / ePub での配布が必要か（Sphinx が有利）
