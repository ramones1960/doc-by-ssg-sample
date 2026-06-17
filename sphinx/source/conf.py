# Sphinx 設定ファイル
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# カスタム拡張のパスを通す
sys.path.insert(0, os.path.abspath("_ext"))

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
    "revision_mark",        # 改訂マーク（縦線 + 版番号）
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
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# intersphinx の例（Python 公式ドキュメントを相互参照）
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# todo を本文に表示する
todo_include_todos = True

# ─── PDF (LaTeX) 出力 ───
# lualatex を使うと Unicode・日本語フォントの扱いが楽
latex_engine = "lualatex"

latex_documents = [
    # (startdocname, targetname, title, author, theme, toctree_only)
    ("index", "shakai-project-docs.tex", "社内プロジェクト文書", "開発チーム", "manual"),
]

latex_elements = {
    # ── 用紙サイズ・余白（Word 標準に近い設定）──
    "papersize": "a4paper",
    "pointsize": "11pt",
    # ── LaTeX プリアンブル ──
    "preamble": r"""
% ページ総数を参照するために必要
\usepackage{lastpage}

% ヘッダー・フッターのカスタマイズ
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}

% ── ヘッダー ──
% 左：現在の章タイトル（\leftmark）
% 右：文書タイトル固定文字列
\fancyhead[L]{\small\nouppercase{\leftmark}}
\fancyhead[R]{\small 社内プロジェクト文書}
\renewcommand{\headrulewidth}{0.4pt}   % ヘッダー下の罫線

% ── フッター ──
% 左：機密区分ラベル
% 中：ページ番号 (X / 総ページ数)
% 右：ビルド日付
\fancyfoot[L]{\small 社内限定}
\fancyfoot[C]{\small \thepage\ /\ \pageref{LastPage}}
\fancyfoot[R]{\small \today}
\renewcommand{\footrulewidth}{0.4pt}   % フッター上の罫線

% 章の先頭ページ（plain スタイル）も同じフッターにする
\fancypagestyle{plain}{
  \fancyhf{}
  \fancyhead[R]{\small 社内プロジェクト文書}
  \fancyfoot[L]{\small 社内限定}
  \fancyfoot[C]{\small \thepage\ /\ \pageref{LastPage}}
  \fancyfoot[R]{\small \today}
  \renewcommand{\headrulewidth}{0.0pt}
  \renewcommand{\footrulewidth}{0.4pt}
}
""",
}
