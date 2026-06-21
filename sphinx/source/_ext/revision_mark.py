"""Sphinx extension: revision change-bar directive.

Usage (reStructuredText)::

    .. revision:: A

       この段落はA版で改訂されました。

Usage (MyST Markdown)::

    ```{revision} A
    この段落はA版で改訂されました。
    ```

Renders a vertical bar on the right edge of the block with the
revision label (e.g. "A") at the top of the bar.
"""

import re

from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class revision_mark(nodes.General, nodes.Element):
    pass


class RevisionDirective(SphinxDirective):
    required_arguments = 1  # revision label, e.g. "A" or "Rev.2"
    optional_arguments = 0
    has_content = True
    final_argument_whitespace = False

    _SAFE_LABEL = re.compile(r'^[\w.\-]+$')

    def run(self):
        label = self.arguments[0]
        if not self._SAFE_LABEL.match(label):
            raise self.error(
                f"revision label must be alphanumeric/dot/hyphen, got: {label!r}"
            )
        container = revision_mark()
        container['revision'] = label
        self.state.nested_parse(self.content, self.content_offset, container)
        return [container]


def visit_revision_html(self, node):
    label = self.attval(node['revision'])
    self.body.append(
        f'<div class="revision-mark" data-revision="{label}">'
    )


def depart_revision_html(self, node):
    self.body.append('</div>\n')


def visit_revision_latex(self, node):
    # LaTeX(PDF): 右側に改訂バーを描く revisionblock 環境（conf.py で定義）に
    # 改訂ラベルを引数として渡す。
    label = node['revision']
    self.body.append('\\begin{revisionblock}{%s}' % label)


def depart_revision_latex(self, node):
    self.body.append(r'\end{revisionblock}')


def visit_revision_text(self, node):
    pass


def depart_revision_text(self, node):
    pass


def setup(app):
    app.add_node(
        revision_mark,
        html=(visit_revision_html, depart_revision_html),
        latex=(visit_revision_latex, depart_revision_latex),
        text=(visit_revision_text, depart_revision_text),
    )
    app.add_directive('revision', RevisionDirective)
    app.add_css_file('revision-mark.css')
    return {'version': '0.1', 'parallel_read_safe': True}
