# Hugo サンプル

## スクリーンショット

| トップページ | 開発ガイド |
|---|---|
| ![トップページ](../docs/screenshots/hugo/index.png) | ![開発ガイド](../docs/screenshots/hugo/getting-started.png) |

## 特徴

- **Go** 製のバイナリ 1 つで動作。インストールが超簡単
- **ビルド速度が圧倒的に速い**（数千ページでも数秒）
- テーマが豊富（Docsy・Hugo Book・PaperMod など）
- Front Matter（TOML / YAML）で柔軟なメタデータ管理
- Git で管理しやすいシンプルな構成

## 向いている用途

- ページ数が多い大規模社内 Wiki
- ビルドを CI/CD に組み込んで自動デプロイしたい場合
- Go チームの社内文書

## セットアップ

```bash
# Hugo のインストール（macOS）
brew install hugo

# Linux / Windows → https://gohugo.io/installation/

cd hugo
hugo server         # http://localhost:1313 でプレビュー
hugo                # public/ にビルド成果物が出力される
```

> **注**: このサンプルはテーマなしの最小構成です。実際の利用では `themes/` に Docsy などを追加してください。

## ディレクトリ構成

```
hugo/
├── hugo.toml           # 設定ファイル
└── content/
    ├── _index.md       # トップページ
    └── docs/
        ├── getting-started.md
        ├── api-reference.md
        └── meeting-notes/
            └── 2025-06.md
```

## 長所 / 短所

| | |
|---|---|
| ✅ | ビルドが最速（大規模サイトに強い） |
| ✅ | バイナリ 1 つで動く（npm / pip 不要） |
| ✅ | テーマエコシステムが充実 |
| ❌ | Go テンプレート構文の学習コストがある |
| ❌ | テーマのカスタマイズは複雑になりがち |
