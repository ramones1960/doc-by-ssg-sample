---
title: 開発ガイド
description: 開発環境の構築手順とブランチ運用ルール
---

## 環境構築

### 必要なツール

- Python 3.11 以上
- Node.js 20 以上（フロントエンド）
- Docker / Docker Compose
- Git

### バックエンドのセットアップ

```bash
# リポジトリのクローン
git clone https://github.com/your-org/project-orbit.git
cd project-orbit/backend

# 仮想環境の作成・有効化
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 依存パッケージのインストール
pip install -r requirements.txt

# 環境変数の設定
cp .env.example .env

# DB の起動・マイグレーション
docker compose up -d db
alembic upgrade head

# 開発サーバー起動
uvicorn app.main:app --reload
```

### フロントエンドのセットアップ

```bash
cd project-orbit/frontend
npm install
cp .env.example .env.local
npm run dev
```

---

## ブランチ運用

```
main          ← 本番リリース済みコード（直接 push 禁止）
  └─ develop  ← 開発統合ブランチ
       ├─ feature/xxx    機能追加
       ├─ fix/xxx        バグ修正
       └─ docs/xxx       文書更新
```

### Pull Request のルール

1. `develop` ブランチへの PR を作成
2. レビュアーを 1 名以上アサイン
3. CI（テスト・Lint）が全てグリーンであること

:::caution
マージは `Squash and merge` を使用してください。コミット履歴を整理するためです。
:::

---

## コーディング規約

### バックエンド（Python）

```python
# 良い例: 型ヒントを必ず付ける
async def get_pass(pass_id: str) -> PassResponse:
    ...
```

- フォーマッタ: `ruff format`
- リンタ: `ruff check`
- 型チェック: `mypy`

---

## テスト

```bash
pytest -v          # バックエンド
npm test           # フロントエンド
npm run test:e2e   # E2E（Playwright）
```
