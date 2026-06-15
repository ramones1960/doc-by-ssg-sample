# Eleventy（11ty）サンプル

## スクリーンショット

| トップページ | 開発ガイド |
|---|---|
| ![トップページ](../docs/screenshots/eleventy/index.png) | ![開発ガイド](../docs/screenshots/eleventy/getting-started.png) |

## 特徴

- **JavaScript** 製で設定の自由度が最大
- テンプレートエンジンを自由に選択（Nunjucks・Liquid・EJS・Pug など）
- 依存ライブラリが最小限で動作が軽量
- ページのデータカスケード（`_data/` ）が柔軟
- 意見（opinionated な構成）が少ない

## 向いている用途

- 独自デザインの社内ポータル
- フロントエンドエンジニアがゼロから設計したい場合
- 特殊なデータソース（社内 API・JSON）から文書を生成したい場合

## セットアップ

```bash
cd eleventy
npm install
npm run serve       # http://localhost:8080 でプレビュー
npm run build       # _site/ にビルド成果物が出力される
```

## ディレクトリ構成

```
eleventy/
├── .eleventy.js            # 設定ファイル（JavaScript）
├── package.json
└── src/
    ├── _layouts/
    │   └── base.njk        # ベースレイアウト（Nunjucks）
    ├── css/
    │   └── style.css       # スタイルシート
    ├── index.md            # トップページ
    └── docs/
        ├── getting-started.md
        ├── api-reference.md
        └── meeting-notes/
            └── 2025-06.md
```

## 長所 / 短所

| | |
|---|---|
| ✅ | 設計の自由度が最大（テンプレート・データソースなど） |
| ✅ | 依存が少なく軽量 |
| ✅ | 既存の HTML / CSS をそのまま使える |
| ❌ | 「標準の正解」がないので設計力が問われる |
| ❌ | プラグインエコシステムは MkDocs / Docusaurus より小さい |
| ❌ | 検索などは自前実装または外部サービスが必要 |
