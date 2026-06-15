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

## 採用基準の比較表（観点別）

採用を検討する際の観点を 1 つの表にまとめました。評価は ◎=得意 / ○=対応 / △=工夫が必要 / ✕=非対応（または標準外）の目安です。

| 観点 | MkDocs | Sphinx | Hugo | Docusaurus | Astro | Eleventy |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| 言語 / ランタイム | Python | Python | Go バイナリ | Node.js / React | Node.js | Node.js |
| 執筆フォーマット | Markdown | Markdown(MyST)/reST | Markdown | MDX(Markdown+JSX) | Markdown(MDX) | Markdown など自由 |
| セットアップの容易さ | ◎ | △ | ◎ | △ | ○ | ○ |
| ビルド速度 | ○ | ○ | ◎ | △ | ○ | ◎ |
| テーマ・デザインの完成度 | ◎ | ○ | ○ | ◎ | ◎ | △（自作前提） |
| 全文検索（標準） | ◎ | △ | ✕ | ◎ | ◎ | ✕ |
| バージョン管理（複数版併存） | △（mike） | △ | △ | ◎ | △ | △ |
| API 自動生成（docstring） | ✕ | ◎ | ✕ | ✕ | ✕ | ✕ |
| 多形式出力（PDF / ePub） | △ | ◎ | ✕ | △ | ✕ | △ |
| 図表（Mermaid） | ◎（テーマ内蔵） | ○（拡張） | ○（render hook） | ◎（公式テーマ） | ○（連携） | △（自前スクリプト） |
| カスタマイズ自由度 | ○ | ○ | ○ | ○ | ○ | ◎ |
| 主な用途 | 技術文書・API リファレンス | ライブラリ API・厳密な仕様書 | 大規模 Wiki | バージョン付き仕様書 | 高速ポータル | 独自設計サイト |

> **観点ごとの最有力**
> セットアップの容易さ → **MkDocs / Hugo**、ビルド速度 → **Hugo / Eleventy**、検索内蔵 → **MkDocs / Docusaurus / Astro**、
> バージョン管理 → **Docusaurus**、API 自動生成・PDF 出力 → **Sphinx**、デザイン自由度 → **Eleventy**。

## ホスティング・配布方法（全 SSG 共通）

ここが分かれて見えがちですが、**6 つの SSG はすべて「静的 HTML」を出力する**ため、配布先は共通です。
特定の SSG だけ GitLab Pages や静的 HTML 配布に縛られる、ということはありません。

| 配布先 | 仕組み | 全 SSG 対応 |
|---|---|:--:|
| GitHub Pages | ビルド成果物を Pages（または private リポジトリの Pages）へ公開 | ✅ |
| GitLab Pages | `.gitlab-ci.yml` でビルドし `public/` を artifacts として公開 | ✅ |
| 静的 HTML 配布 | ビルド成果物（下表のディレクトリ）を社内 Web サーバー / 共有・zip 配布 | ✅ |

各 SSG のビルド成果物ディレクトリ（このフォルダを上記いずれの方法でも配布できます）:

| SSG | ビルド出力先 |
|---|---|
| MkDocs | `site/` |
| Sphinx | `build/html/` |
| Hugo | `public/` |
| Docusaurus | `build/` |
| Astro | `dist/` |
| Eleventy | `_site/` |

> いずれも認証は別途 nginx / Cloudflare Access 等で行う前提です（[設計方針](#前提社内利用を想定した設計方針)を参照）。

## リポジトリ構成（モノレポ）

各 SSG はディレクトリで分離され、依存（npm / pip）も**それぞれのディレクトリに閉じています**。
他の SSG をインストールせずに、試したいものだけをセットアップできます。

```
doc-by-ssg-sample/
├── README.md
├── .npmrc              ← npm プロキシ設定（環境変数を参照）
├── proxy.env.example   ← プロキシ環境変数テンプレート
├── pip.conf.example    ← pip プロキシ設定テンプレート
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

- **プロジェクト概要** — 背景・目的・体制（**画像（SVG）と Mermaid 図の挿入例**を含む）
- **開発ガイド** — 環境構築・ブランチ運用
- **API リファレンス** — エンドポイント一覧
- **議事録** — 定例会議のサンプル

各サンプルのトップページに「**図・画像の挿入例**」セクションを設け、画像（`architecture.svg`）と
Mermaid 図（フローチャート・シーケンス図）を同じ内容で掲載しています。SSG ごとの Mermaid 有効化方法は
上の[採用基準の比較表](#採用基準の比較表観点別)の「図表（Mermaid）」行を参照してください。

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
- [ ] Mermaid 図を多用するか（MkDocs / Docusaurus は設定が最も手軽）
- [ ] 配布先は？（GitHub Pages / GitLab Pages / 社内サーバーへの静的 HTML 配布 — **どの SSG でも対応可**）
