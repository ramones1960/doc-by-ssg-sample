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

## 基本操作（SSG の作り方）

> 詳細は公式ドキュメント（[MkDocs](https://www.mkdocs.org/) / [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)）を参照。ここでは最低限必要な操作だけまとめます。

### 記事（ページ）を追加する

1. `docs/` 配下に Markdown ファイルを置く（例：`docs/guide/install.md`）
2. `mkdocs.yml` の `nav:` に追記してナビゲーションに表示する

```yaml
nav:
  - ホーム: index.md
  - 開発ガイド: getting-started.md
  - インストール: guide/install.md   # 追加
```

- ファイル先頭の `# 見出し` がページタイトルになる
- `nav:` を省略すると `docs/` 以下が自動でナビに並ぶ

### 内部リンクを作る

Markdown の相対リンクで `.md` ファイルを直接指定します（ビルド時に正しい URL に変換されます）。

```markdown
詳しくは [開発ガイド](getting-started.md) を参照。
見出しへのリンクは [環境構築](getting-started.md#環境構築) のように書く。
```

### 画像・静的ファイルを管理する

`docs/` 配下に画像を置き、Markdown から相対パスで参照します。

```
docs/
├── index.md
└── img/
    └── architecture.png
```

```markdown
![システム構成図](img/architecture.png)
```

### ビルドとプレビュー

```bash
mkdocs serve     # http://localhost:8000 でライブプレビュー
mkdocs build     # site/ に静的 HTML を出力
```

## 配布方法のメリット・デメリット

### A. Web サーバーなしで HTML を直接配布する（file:// やファイル共有）

`site/` をそのまま zip やファイル共有で配る使い方です。

| | |
|---|---|
| ✅ | 出力リンクが相対パスなので、ディレクトリごと配ればそのまま閲覧できる |
| ✅ | `use_directory_urls: false` を設定すると `*.html` 形式になり、ファイルをダブルクリックで開いてもページ遷移できる |
| ❌ | 全文検索は JavaScript がローカルインデックスを `fetch` するため、`file://` ではブラウザによって動かないことがある（`http://` 配信なら問題なし） |
| ❌ | ダークモード切替などは動くが、一部の動的機能はオフラインだと制限される |

```yaml
# file:// で配布するなら推奨
use_directory_urls: false
```

### B. GitLab Pages と連携する

```yaml
# .gitlab-ci.yml
pages:
  image: python:3.12
  script:
    - pip install mkdocs-material
    - mkdocs build -d public      # GitLab Pages は public/ を公開する
  artifacts:
    paths:
      - public
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
```

| | |
|---|---|
| ✅ | `mkdocs build -d public` だけで完結し、CI 設定が非常に短い |
| ✅ | サブパス（`/<repo>/`）配信でもリンクが相対パスなので崩れにくい |
| ✅ | Web サーバー配信なので検索・ナビが完全に動作する |
| ❌ | 絶対 URL を使う場合は `site_url` をサブパスに合わせて指定する必要がある |

## 長所 / 短所

| | |
|---|---|
| ✅ | セットアップが最も簡単（pip install だけ） |
| ✅ | Material テーマが充実（ダークモード・検索・コードコピー） |
| ✅ | Admonition で注釈ボックスが書きやすい |
| ❌ | JavaScript/React に慣れたチームには学習コストあり |
| ❌ | バージョン管理は mike プラグインが別途必要 |
