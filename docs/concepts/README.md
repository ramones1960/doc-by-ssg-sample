# DaC を学ぶ — 概念解説コンテンツ

このディレクトリは、**Documentation as Code（DaC）** の考え方そのものを学ぶための
解説コンテンツをまとめた場所です。

各 SSG ディレクトリ（`mkdocs/`, `sphinx/` …）が「**ツールの使い方・記法の比較**」を扱うのに対し、
ここでは「**そもそも DaC とは何か / どう運用するのか**」という概念とワークフローを扱います。

## 読む順番（学習の地図）

| # | ドキュメント | 内容 |
|---|---|---|
| 1 | [DaC ワークフロー解説](./dac-workflow.md) | 執筆 → レビュー → ビルド → 公開 のライフサイクルと、DaC を支える 4 本柱 |
| 2 | [Developer Portal / IDP 解説](./developer-portal.md) | DaC で書いたドキュメントを全社で束ねる Backstage / TechDocs などのポータル基盤 |

```
個々のドキュメントを SSG（DaC）で書く        ← 1. dac-workflow.md
            ↓
全社のドキュメント・サービスを束ねる         ← 2. developer-portal.md
（Developer Portal / IDP）
```

## このリポジトリ全体との関係

- **概念を学ぶ** → このディレクトリ（`docs/concepts/`）
- **ツールを選ぶ・試す** → ルート [`README.md`](../../README.md) と各 SSG ディレクトリ
