---
title: API リファレンス
description: 地上管制システム REST API のエンドポイント一覧
---

ベース URL: `https://api.internal.example/v1`

認証: Bearer トークン（`Authorization: Bearer <token>`）

---

## 共通仕様

- **日時フォーマット**: ISO 8601・JST（例: `2025-06-15T09:30:00+09:00`）
- **ページネーション**: `limit`（デフォルト 20・最大 100）と `offset` を共通サポート。レスポンスに総件数 `total` を含む
- **レート制限**: 1 トークンあたり 600 リクエスト/分。超過時は `429 rate_limited` を返却し、`Retry-After` ヘッダで再試行可能秒数を通知
- **冪等性**: `POST /passes` は `Idempotency-Key` ヘッダで重複作成を防止できる

---

## 運用計画（パス）管理

### 可視パス一覧取得

```
GET /passes
```

**クエリパラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `status` | string | - | `scheduled` / `confirmed` / `executed` / `cancelled` |
| `satellite_id` | string | - | 衛星 ID で絞り込み（例: `SAT-001`） |
| `from` | string (date-time) | - | AOS（可視開始）日時の開始 |
| `to` | string (date-time) | - | AOS 日時の終了 |
| `limit` | integer | - | 取得件数（デフォルト: 20、最大: 100） |
| `offset` | integer | - | オフセット（デフォルト: 0） |

**レスポンス例**

```json
{
  "total": 142,
  "items": [
    {
      "id": "PASS-2025-00142",
      "status": "confirmed",
      "satellite_id": "SAT-001",
      "ground_station": "GS-AKITA",
      "aos_at": "2025-06-15T09:30:00+09:00",
      "max_elevation_deg": 54.8
    }
  ]
}
```

---

### パス予約作成

```
POST /passes
```

**リクエストボディ**

```json
{
  "satellite_id": "SAT-001",
  "ground_station": "GS-AKITA",
  "aos_at": "2025-06-15T09:30:00+09:00",
  "tasks": [
    { "task_id": "TASK-0032", "priority": 2 }
  ],
  "note": "夜間パス・低仰角注意"
}
```

**レスポンス** `201 Created`

```json
{
  "id": "PASS-2025-00143",
  "status": "scheduled",
  "created_at": "2025-06-15T10:00:00+09:00"
}
```

---

## 衛星リソース管理

### テレメトリ照会

```
GET /telemetry/{satellite_id}
```

**レスポンス例**

```json
{
  "satellite_id": "SAT-001",
  "satellite_name": "ひかり 1 号",
  "battery_pct": 87,
  "storage_free_mb": 1240,
  "mode": "nominal",
  "ground_station": "GS-AKITA"
}
```

---

### テレメトリ履歴取得

```
GET /telemetry/{satellite_id}/history
```

**クエリパラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `from` | string (date-time) | ○ | 取得開始日時 |
| `to` | string (date-time) | ○ | 取得終了日時 |
| `interval` | string | - | 集計間隔（`1m` / `5m` / `1h`、デフォルト `5m`） |

**レスポンス例**

```json
{
  "satellite_id": "SAT-001",
  "interval": "5m",
  "items": [
    { "at": "2025-06-15T09:30:00+09:00", "battery_pct": 87, "temp_c": 12.4 },
    { "at": "2025-06-15T09:35:00+09:00", "battery_pct": 86, "temp_c": 12.1 }
  ]
}
```

---

## コマンド管理

### コマンド送信

```
POST /commands
```

衛星へのコマンドは、可視パス（`pass_id`）に紐づけてキューイングされ、AOS 後に順次実行されます。

**リクエストボディ**

```json
{
  "satellite_id": "SAT-001",
  "pass_id": "PASS-2025-00142",
  "command": "CAPTURE_IMAGE",
  "params": { "sensor": "optical", "exposure_ms": 12 }
}
```

**レスポンス** `202 Accepted`

```json
{
  "command_id": "CMD-2025-04821",
  "status": "queued"
}
```

---

## 地上局

### 地上局一覧取得

```
GET /ground-stations
```

**レスポンス例**

```json
{
  "items": [
    { "id": "GS-AKITA", "name": "秋田局", "location": "秋田県", "status": "online" },
    { "id": "GS-OKINAWA", "name": "沖縄局", "location": "沖縄県", "status": "maintenance" }
  ]
}
```

---

## エラーコード一覧

| コード | HTTP | 説明 |
|---|---|---|
| `not_found` | 404 | リソースが存在しない |
| `validation_error` | 422 | リクエストパラメータが不正 |
| `pass_conflict` | 409 | 指定時間帯に地上局が予約済み（パス競合） |
| `unauthorized` | 401 | 認証トークンが無効 |
| `forbidden` | 403 | 操作権限がない |
| `rate_limited` | 429 | レート制限を超過（`Retry-After` を参照） |
