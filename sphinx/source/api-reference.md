# API リファレンス

ベース URL: `https://api.internal.example/v1`

認証: Bearer トークン（`Authorization: Bearer <token>`）

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
| `from` | string (date) | - | AOS（可視開始）日時の開始 |
| `to` | string (date) | - | AOS 日時の終了 |
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
      "los_at": "2025-06-15T09:42:00+09:00",
      "max_elevation_deg": 54.8,
      "tasks": [
        {
          "task_id": "TASK-0032",
          "task_name": "光学センサー画像ダウンリンク",
          "priority": 2,
          "duration_sec": 420
        }
      ]
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
    {
      "task_id": "TASK-0032",
      "priority": 2
    }
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

## エラーコード一覧

| コード | HTTP | 説明 |
|---|---|---|
| `not_found` | 404 | リソースが存在しない |
| `validation_error` | 422 | リクエストパラメータが不正 |
| `pass_conflict` | 409 | 指定時間帯に地上局が予約済み（パス競合） |
| `unauthorized` | 401 | 認証トークンが無効 |
| `forbidden` | 403 | 操作権限がない |
