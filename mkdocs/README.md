# MkDocs サンプル

## スクリーンショット

| トップページ | 開発ガイド |
|---|---|
| ![トップページ](./docs/screenshots/index.png) | ![開発ガイド](./docs/screenshots/getting-started.png) |

## 特徴

- **Python** で動作。`pip` だけで導入できる
- **Material テーマ** が強力でそのままでも十分きれい
- タブ・Admonition（注釈ボックス）・コードコピーなど社内文書向け機能が充実
- `mkdocs.yml` 1 ファイルで設定が完結
- 日本語全文検索が標準で使える

## 向いている用途

- 技術文書・API リファレンス
- Python チームの社内 Wiki
- 小〜中規模のドキュメントサイト

## セットアップ

```bash
pip install mkdocs-material
cd mkdocs
mkdocs serve        # http://localhost:8000 でプレビュー
mkdocs build        # site/ にビルド成果物が出力される
```

## ディレクトリ構成

```
mkdocs/
├── mkdocs.yml          # 設定ファイル（ナビ・テーマ・プラグイン）
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
| ✅ | セットアップが最も簡単（pip install だけ） |
| ✅ | Material テーマが充実（ダークモード・検索・コードコピー） |
| ✅ | Admonition で注釈ボックスが書きやすい |
| ❌ | JavaScript/React に慣れたチームには学習コストあり |
| ❌ | バージョン管理は mike プラグインが別途必要 |
