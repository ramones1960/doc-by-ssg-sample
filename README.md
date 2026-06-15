# SSG 比較サンプル — 社内文書への活用

静的サイトジェネレータ（SSG）を使って社内文書・プロジェクト情報を管理するためのサンプル集です。

## 比較対象

| SSG | 言語 | 特徴 | 向いている用途 |
|---|---|---|---|
| [MkDocs](./mkdocs/) | Python | シンプル・Material テーマが強力 | 技術文書・API リファレンス |
| [Hugo](./hugo/) | Go | 超高速ビルド・テーマが豊富 | 大量ページの社内 Wiki |
| [Docusaurus](./docusaurus/) | React / JS | バージョン管理・全文検索 | プロジェクト仕様書・変更履歴 |
| [Eleventy](./eleventy/) | JavaScript | 設計自由度が高い・軽量 | カスタマイズしたいチーム |

## 共通サンプル文書

各 SSG に同じ内容の文書を移植しています。

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
# MkDocs
cd mkdocs && pip install mkdocs-material && mkdocs serve

# Hugo
cd hugo && hugo server

# Docusaurus
cd docusaurus && npm install && npm run start

# Eleventy
cd eleventy && npm install && npm run serve
```

## 選定チェックリスト

- [ ] チームの主要言語は何か（Python → MkDocs、JS → Docusaurus/11ty、Go → Hugo）
- [ ] バージョン管理が必要か（Docusaurus が有利）
- [ ] デザインのカスタマイズ度は（11ty が最大自由度）
- [ ] ページ数・ビルド速度（大規模なら Hugo）
