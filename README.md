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
├── .npmrc              ← npm プロキシ設定（環境変数を参照）
├── proxy.env.example   ← プロキシ環境変数テンプレート
├── pip.conf.example    ← pip プロキシ設定テンプレート
├── docs/               ← リポジトリ用の資料（各 SSG の README で使うスクリーンショット）
│   └── screenshots/<ssg>/{index,getting-started}.png
├── mkdocs/        … requirements.txt（Python）
├── sphinx/        … requirements.txt（Python）
├── hugo/          … Go バイナリのみ（パッケージ管理なし）
├── docusaurus/    … package.json（npm）
├── astro/         … package.json（npm）
└── eleventy/      … package.json（npm）
```

各 SSG ディレクトリには、その SSG を動かすのに必要なファイルだけが入っています。
README で使うスクリーンショットなどリポジトリ全体の資料は、各 SSG の公開コンテンツに
混ざらないよう最上位の `docs/` にまとめています。

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

## プロキシ環境での利用

社内プロキシ経由でパッケージをインストールする場合は、**環境変数を設定するだけ**で
すべてのパッケージ管理ツール（pip / npm / go）に自動的に適用されます。

```bash
# 1. テンプレートをコピーして編集（proxy.env はコミットされません）
cp proxy.env.example proxy.env
# proxy.env の HTTP_PROXY / HTTPS_PROXY / NO_PROXY を実際の値に書き換える

# 2. 環境変数を読み込む
source proxy.env

# 3. あとは通常どおり各 SSG をセットアップするだけ
```

| ツール | プロキシの仕組み |
|---|---|
| **pip** | `HTTP_PROXY` / `HTTPS_PROXY` 環境変数を自動読み取り |
| **npm** | ルートの `.npmrc` が `${HTTP_PROXY}` / `${HTTPS_PROXY}` を参照 |
| **go install**（Hugo） | `HTTP_PROXY` / `HTTPS_PROXY` 環境変数を自動読み取り |

> **社内 CA 証明書が必要な場合** — `pip.conf.example` を参照して pip に証明書を登録してください。

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

> ビルド後のサイトはすべて `localhost` でアクセスします（`hugo server` → `:1313`、`mkdocs serve` → `:8000` 等）。

## 選定チェックリスト

- [ ] チームの主要言語は何か（Python → MkDocs / Sphinx、JS → Docusaurus / Astro / 11ty、Go → Hugo）
- [ ] Python ソースから API 文書を自動生成したいか（Sphinx の autodoc が有利）
- [ ] バージョン管理が必要か（Docusaurus が有利）
- [ ] 全文検索を手軽に使いたいか（Astro / Starlight は標準内蔵）
- [ ] デザインのカスタマイズ度は（11ty が最大自由度）
- [ ] ページ数・ビルド速度（大規模なら Hugo）
- [ ] PDF / ePub での配布が必要か（Sphinx が有利）
