# Sphinx 設定ファイル
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "社内プロジェクト文書"
copyright = "2025, 開発チーム（社内限定）"
author = "開発チーム"
release = "1.0"

# ─── 拡張 ───
extensions = [
    "myst_parser",          # Markdown(MyST) を解釈する
    "sphinx_copybutton",    # コードブロックのコピー ボタン
    "sphinx.ext.todo",      # TODO 管理
    "sphinx.ext.intersphinx",  # 他プロジェクトの文書を相互参照
]

# Markdown と reStructuredText の両方を受け付ける
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# MyST の追加機能（注釈ボックス・テーブルなど）
myst_enable_extensions = [
    "colon_fence",   # ::: で囲む記法
    "deflist",
    "tasklist",
]

language = "ja"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# ─── HTML 出力 ───
html_theme = "furo"
html_title = "社内プロジェクト文書"
# 全フレームワーク共通の日本語フォントを読み込む
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# intersphinx の例（Python 公式ドキュメントを相互参照）
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# todo を本文に表示する
todo_include_todos = True
