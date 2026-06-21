---
id: getting-started
title: 開発ガイド
sidebar_position: 2
---

# 開発ガイド

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

:::warning マージ方法
`Squash and merge` を使用してください。コミット履歴を整理するためです。
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
# バックエンド
pytest -v

# フロントエンド
npm test

# E2E（Playwright）
npm run test:e2e
```

---

## ディレクトリ構成

```
project-orbit/
├── backend/              # FastAPI バックエンド
│   ├── app/
│   │   ├── main.py       # エントリポイント
│   │   ├── api/          # ルーター（passes / telemetry / commands）
│   │   ├── models/       # SQLAlchemy モデル
│   │   ├── schemas/      # Pydantic スキーマ
│   │   └── services/     # ビジネスロジック
│   ├── alembic/          # DB マイグレーション
│   └── tests/
├── frontend/             # React 管制コンソール
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── api/          # API クライアント
│   └── tests/
└── docker-compose.yml
```

---

## 主要な環境変数

| 変数名 | 例 | 説明 |
|---|---|---|
| `DATABASE_URL` | `postgresql://orbit:***@localhost:5432/orbit` | PostgreSQL 接続文字列 |
| `GROUND_STATION_GW_URL` | `https://gw.internal.example` | 地上局ゲートウェイの URL |
| `JWT_SECRET` | `(32 文字以上のランダム文字列)` | API トークン署名鍵 |
| `LOG_LEVEL` | `INFO` | ログレベル（`DEBUG` / `INFO` / `WARNING`） |
| `TELEMETRY_POLL_SEC` | `5` | テレメトリ取得間隔（秒） |

:::danger 秘密情報の取り扱い
`.env` は **コミットしないでください**。変数を追加したら `.env.example` を更新してチームに共有します。
:::

---

## トラブルシューティング

<details>
<summary><code>alembic upgrade head</code> で DB 接続エラーになる</summary>

DB コンテナが起動しているか確認してください。

```bash
docker compose ps          # db が Up になっているか
docker compose up -d db    # 起動していなければ起動
```

それでも失敗する場合は `DATABASE_URL` のホスト・ポート・認証情報を確認します。

</details>

<details>
<summary><code>uvicorn</code> 起動時に <code>ModuleNotFoundError</code> が出る</summary>

仮想環境が有効化されていない可能性があります。

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

</details>

<details>
<summary>フロントエンドから API が CORS で弾かれる</summary>

バックエンドの CORS 許可オリジンにフロントエンドの URL（例: `http://localhost:5173`）が
含まれているか、`backend/app/main.py` の `CORSMiddleware` 設定を確認してください。

</details>
