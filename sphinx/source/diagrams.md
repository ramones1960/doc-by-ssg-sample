# 図の挿入（Mermaid）

Sphinx では **sphinxcontrib-mermaid** 拡張を使うことで、Markdown の中に
[Mermaid](https://mermaid.js.org/) の図を直接記述できます。
テキストとして管理でき、Git での差分追跡・レビューが容易です。

## セットアップ

```bash
# requirements.txt に追加済みの場合はこれだけ
pip install sphinxcontrib-mermaid
```

`conf.py` の `extensions` リストに追加します。

```python
extensions = [
    "myst_parser",
    "sphinxcontrib.mermaid",   # ← 追加
    # ...
]
```

---

## フローチャート

処理の流れやシステムの制御フローを表すのに使います。

````markdown
```{mermaid}
flowchart TD
    A[地上管制コンソール] -->|REST API| B[管制バックエンド API]
    B --> C[(PostgreSQL)]
    B --> D[地上局ゲートウェイ]
    D -->|コマンド送信| E((衛星))
    E -->|テレメトリ| D
```
````

```{mermaid}
flowchart TD
    A[地上管制コンソール] -->|REST API| B[管制バックエンド API]
    B --> C[(PostgreSQL)]
    B --> D[地上局ゲートウェイ]
    D -->|コマンド送信| E((衛星))
    E -->|テレメトリ| D
```

---

## シーケンス図

コンポーネント間のやり取り（API 呼び出しの順序など）を時系列で示します。

````markdown
```{mermaid}
sequenceDiagram
    actor Operator as オペレーター
    participant Console as 管制コンソール
    participant API as バックエンド API
    participant GW as 地上局 GW

    Operator->>Console: パス実行を指示
    Console->>API: POST /passes/{id}/execute
    API->>GW: コマンド送信リクエスト
    GW-->>API: 送信完了 (200 OK)
    API-->>Console: 実行結果 (200 OK)
    Console-->>Operator: 完了通知を表示
```
````

```{mermaid}
sequenceDiagram
    actor Operator as オペレーター
    participant Console as 管制コンソール
    participant API as バックエンド API
    participant GW as 地上局 GW

    Operator->>Console: パス実行を指示
    Console->>API: POST /passes/{id}/execute
    API->>GW: コマンド送信リクエスト
    GW-->>API: 送信完了 (200 OK)
    API-->>Console: 実行結果 (200 OK)
    Console-->>Operator: 完了通知を表示
```

---

## ER 図

データベースのテーブル構造とリレーションシップを表します。

````markdown
```{mermaid}
erDiagram
    PASS {
        uuid id PK
        string satellite_id
        datetime aos
        datetime los
        string status
    }
    TELEMETRY {
        uuid id PK
        uuid pass_id FK
        datetime recorded_at
        float battery_voltage
        float temperature
    }
    COMMAND {
        uuid id PK
        uuid pass_id FK
        string type
        string payload
        datetime sent_at
    }

    PASS ||--o{ TELEMETRY : "記録する"
    PASS ||--o{ COMMAND : "送信する"
```
````

```{mermaid}
erDiagram
    PASS {
        uuid id PK
        string satellite_id
        datetime aos
        datetime los
        string status
    }
    TELEMETRY {
        uuid id PK
        uuid pass_id FK
        datetime recorded_at
        float battery_voltage
        float temperature
    }
    COMMAND {
        uuid id PK
        uuid pass_id FK
        string type
        string payload
        datetime sent_at
    }

    PASS ||--o{ TELEMETRY : "記録する"
    PASS ||--o{ COMMAND : "送信する"
```

---

## ガントチャート

プロジェクトのスケジュールやフェーズ管理に使います。

````markdown
```{mermaid}
gantt
    title プロジェクト Orbit スケジュール
    dateFormat YYYY-MM
    axisFormat %Y/%m

    section 設計
    DB 設計書         :done,    des1, 2025-06, 2025-07
    API 仕様書         :done,    des2, 2025-06, 2025-07
    地上局 IF 仕様     :active,  des3, 2025-07, 2025-08

    section 開発
    バックエンド API   :         dev1, 2025-08, 2025-11
    フロントエンド     :         dev2, 2025-09, 2025-12

    section 検証
    結合テスト         :         qa1, 2026-01, 2026-02
    運用リハーサル     :         qa2, 2026-02, 2026-03

    section リリース
    本番運用開始       :milestone, rel1, 2026-03, 0d
```
````

```{mermaid}
gantt
    title プロジェクト Orbit スケジュール
    dateFormat YYYY-MM
    axisFormat %Y/%m

    section 設計
    DB 設計書         :done,    des1, 2025-06, 2025-07
    API 仕様書         :done,    des2, 2025-06, 2025-07
    地上局 IF 仕様     :active,  des3, 2025-07, 2025-08

    section 開発
    バックエンド API   :         dev1, 2025-08, 2025-11
    フロントエンド     :         dev2, 2025-09, 2025-12

    section 検証
    結合テスト         :         qa1, 2026-01, 2026-02
    運用リハーサル     :         qa2, 2026-02, 2026-03

    section リリース
    本番運用開始       :milestone, rel1, 2026-03, 0d
```

---

## キャプションを付ける

`caption` オプションでキャプションを追加できます。

````markdown
```{mermaid}
:caption: 図 1 — システム全体構成
flowchart LR
    A[コンソール] --> B[API] --> C[(DB)]
```
````

```{mermaid}
:caption: 図 1 — システム全体構成
flowchart LR
    A[コンソール] --> B[API] --> C[(DB)]
```

---

## 注意事項

- HTML 出力では Mermaid の JavaScript ライブラリがブラウザ側でレンダリングします。
- **PDF（LaTeX）出力**では `sphinxcontrib-mermaid` が Mermaid CLI (`mmdc`) を呼び出して
  PNG/SVG に変換します。PDF ビルド時は Node.js と Mermaid CLI のインストールが必要です。

  ```bash
  npm install -g @mermaid-js/mermaid-cli
  ```

  `conf.py` で出力形式を指定できます（デフォルトは `png`）。

  ```python
  mermaid_output_format = "png"  # or "svg"
  ```
