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
# 日本語は uplatex（jsbook クラス）+ dvipdfmx が最も実績がある組み合わせ。
# ビルド: sphinx-build -M latexpdf source build   （latexmk が uplatex→dvipdfmx を自動実行）
latex_engine = "uplatex"

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
% 注意: Sphinx は独自に fancyhdr の "normal"/"plain" ページスタイルを定義するため、
% \pagestyle{fancy} ではなく、これらのスタイル自体を再定義して上書きする必要がある。
\usepackage{fancyhdr}

% ── 本文ページ（normal スタイル）──
% ヘッダー左：現在の章タイトル（\leftmark）／右：文書タイトル
% フッター左：機密区分／中：ページ番号 (X / 総ページ数)／右：ビルド日付
\fancypagestyle{normal}{%
  \fancyhf{}%
  \fancyhead[L]{\small\nouppercase{\leftmark}}%
  \fancyhead[R]{\small 社内プロジェクト文書}%
  \fancyfoot[L]{\small 社内限定}%
  \fancyfoot[C]{\small \thepage\ /\ \pageref{LastPage}}%
  \fancyfoot[R]{\small \today}%
  \renewcommand{\headrulewidth}{0.4pt}%
  \renewcommand{\footrulewidth}{0.4pt}%
}

% ── 章の先頭ページ（plain スタイル）──
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyhead[R]{\small 社内プロジェクト文書}%
  \fancyfoot[L]{\small 社内限定}%
  \fancyfoot[C]{\small \thepage\ /\ \pageref{LastPage}}%
  \fancyfoot[R]{\small \today}%
  \renewcommand{\headrulewidth}{0.0pt}%
  \renewcommand{\footrulewidth}{0.4pt}%
}

\pagestyle{normal}

% 目次に出す見出しの深さ（章・節まで）
\setcounter{tocdepth}{2}

% 改訂マーク（revision ディレクティブ）の PDF 用環境。
% ブロックの右側に赤い改訂バーを引き、先頭に [改訂 X] ラベルを表示する。
\usepackage{mdframed}
\newenvironment{revisionblock}[1]{%
  \par\smallskip
  \begin{mdframed}[topline=false,bottomline=false,leftline=false,rightline=true,%
    linewidth=2pt,linecolor=red,innerleftmargin=8pt,innerrightmargin=8pt,%
    innertopmargin=4pt,innerbottommargin=4pt,skipabove=2pt,skipbelow=2pt]%
  \nobreak\hfill{\small\bfseries\color{red}[\,改訂 #1\,]}\par\nobreak
}{%
  \end{mdframed}\par\smallskip
}
""",
    # ── 表紙（タイトルページ）──
    # Sphinx 既定のタイトルを差し替え、機密区分・版・発行日を載せた表紙にする
    "maketitle": r"""
\begin{titlepage}
  \centering
  \vspace*{1.5cm}
  {\large 社内限定 / CONFIDENTIAL\par}
  \vspace{1.0cm}
  \rule{\linewidth}{0.4pt}\par
  \vspace{1.2cm}
  {\Huge\bfseries 社内プロジェクト文書\par}
  \vspace{0.8cm}
  {\LARGE プロジェクト Orbit\par}
  \vspace{0.4cm}
  {\large 小型衛星 地上管制システム — 技術文書・運用ガイド\par}
  \vspace{1.2cm}
  \rule{\linewidth}{0.4pt}\par
  \vfill
  \begin{tabular}{rl}
    \textbf{バージョン} & 1.0 \\[4pt]
    \textbf{作成} & 開発チーム \\[4pt]
    \textbf{発行日} & \today \\
  \end{tabular}
  \vspace{1.5cm}
\end{titlepage}
""",
    # ── 目次 ──
    # 前付け（表紙・目次）はローマ数字、本文はアラビア数字でページ番号を振る
    "tableofcontents": r"""
\clearpage
\pagenumbering{roman}
\sphinxtableofcontents
\clearpage
\pagenumbering{arabic}
""",
}

# PDF の章立て：トップレベルの見出しを「章」として扱う
latex_toplevel_sectioning = "chapter"
