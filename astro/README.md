# Astro + Starlight サンプル

## スクリーンショット

| トップページ | 開発ガイド |
|---|---|
| ![トップページ](../docs/screenshots/astro/index.png) | ![開発ガイド](../docs/screenshots/astro/getting-started.png) |

## 特徴

- **Astro** は「Islands Architecture」で **超軽量な静的サイト**を生成（デフォルトで JS ゼロ出力）
- **Starlight** は Astro 公式のドキュメント用テーマ。これ単体で本格的な文書サイトが完成する
- **全文検索（Pagefind）が標準内蔵**。設定不要で日本語検索も動く
- **ダークモード・i18n（多言語）・サイドバー自動生成**が最初から備わっている
- React / Vue / Svelte など好きな UI フレームワークのコンポーネントを混在できる
- ページ表示が非常に高速（Lighthouse スコアが出やすい）

## 向いている用途

- パフォーマンス重視の社内ポータル
- 設定を最小限に、見栄えの良い文書サイトをすぐ立てたい場合
- 将来 React/Vue などのインタラクティブ要素も足したい場合

## セットアップ

```bash
cd astro

# このディレクトリ専用の依存をインストール
npm install

# 開発サーバー（http://localhost:4321）
npm run dev

# 本番ビルド（dist/ に出力。検索インデックスもここで生成）
npm run build

# ビルド結果のプレビュー
npm run preview
```

## ディレクトリ構成

```
astro/
├── package.json            # npm 依存（このディレクトリ専用）
├── astro.config.mjs        # Astro + Starlight 設定（サイドバー等）
└── src/
    └── content/
        ├── config.ts       # コンテンツコレクション定義
        └── docs/
            ├── index.md
            ├── getting-started.md
            ├── api-reference.md
            └── meeting-notes/
                └── 2025-06.md
```

## 長所 / 短所

| | |
|---|---|
| ✅ | 全文検索（Pagefind）が設定不要で内蔵 |
| ✅ | ダークモード・i18n・サイドバーが標準装備 |
| ✅ | 出力が軽量・高速（デフォルト JS ゼロ） |
| ✅ | React/Vue/Svelte コンポーネントを混在可能 |
| ❌ | エコシステムが新しめ（Docusaurus ほど枯れていない） |
| ❌ | バージョン管理機能は標準では弱い（Docusaurus が有利） |
| ❌ | Node.js 環境が前提 |
