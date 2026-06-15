---
title: API リファレンス
description: 受発注システム REST API のエンドポイント一覧
---

ベース URL: `https://api.internal.example/v1`

認証: Bearer トークン（`Authorization: Bearer <token>`）

---

## 受注管理

### 受注一覧取得

```
GET /orders
```

**クエリパラメータ**

| パラメータ | 型 | 必須 | 説明 |
|---|---|---|---|
| `status` | string | - | `pending` / `confirmed` / `shipped` / `cancelled` |
| `from` | string (date) | - | 受注日の開始 |
| `to` | string (date) | - | 受注日の終了 |
| `limit` | integer | - | 取得件数（デフォルト: 20、最大: 100） |
| `offset` | integer | - | オフセット（デフォルト: 0） |

**レスポンス例**

```json
{
  "total": 142,
  "items": [
    {
      "id": "ORD-2025-00142",
      "status": "confirmed",
      "customer_id": "CUST-001",
      "ordered_at": "2025-06-15T09:30:00+09:00",
      "total_amount": 54800
    }
  ]
}
```

---

### 受注作成

```
POST /orders
```

**リクエストボディ**

```json
{
  "customer_id": "CUST-001",
  "lines": [
    { "product_id": "PROD-0032", "quantity": 2 }
  ],
  "note": "午前中指定"
}
```

**レスポンス** `201 Created`

```json
{
  "id": "ORD-2025-00143",
  "status": "pending",
  "ordered_at": "2025-06-15T10:00:00+09:00"
}
```

---

## 在庫管理

### 在庫照会

```
GET /inventory/{product_id}
```

**レスポンス例**

```json
{
  "product_id": "PROD-0032",
  "product_name": "ノートPC 15インチ",
  "available": 24,
  "reserved": 8,
  "warehouse": "東京倉庫"
}
```

---

## エラーコード一覧

| コード | HTTP | 説明 |
|---|---|---|
| `not_found` | 404 | リソースが存在しない |
| `validation_error` | 422 | リクエストパラメータが不正 |
| `insufficient_stock` | 409 | 在庫不足 |
| `unauthorized` | 401 | 認証トークンが無効 |
| `forbidden` | 403 | 操作権限がない |
