from docutils import nodes
from sphinx.locale import admonitionlabels
from sphinx.writers.html5 import HTML5Translator


# Překladatelská řetězová reakce:
# Překladač docutils Base HTML: https://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/writers/_html_base.py
# └── Docutils Polyglot html5 překladač: https://sourceforge.net/p/docutils/code/HEAD/tree/trunk/docutils/docutils/writers/html5_polyglot/__init__.py
#     └─ Sphinx překladatel: https://github.com/sphinx-doc/sphinx/blob/master/sphinx/writers/html5.py
#         └──Odoo překladač

ADMONITION_MAPPING = {
    'note': 'alert-primary',

    'tip': 'alert-tip',

    'seealso': 'alert-secondary',

    'warning': 'alert-warning',
    'attention': 'alert-warning',
    'caution': 'alert-warning',
    'important': 'alert-warning',

    'danger': 'alert-danger',
    'error': 'alert-danger',

    'example': 'alert-success',
    'exercise': 'alert-dark',
}  # The alert classes have been replaced by default BS classes to reduce number of scss lines.


class BootstrapTranslator(HTML5Translator):
    # Specifikace docutils
    head_prefix = 'head_prefix'
    head = 'head'
    stylesheet = 'stylesheet'
    body_prefix = 'body_prefix'
    body_pre_docinfo = 'body_pre_docinfo'
    docinfo = 'docinfo'
    body_suffix = 'body_suffix'
    subtitle = 'subtitle'
    header = 'header'
    footer = 'footer'
    html_prolog = 'html_prolog'
    html_head = 'html_head'
    html_title = 'html_title'
    html_subtitle = 'html_subtitle'

    def __init__(self, builder, *args, **kwds):
        super().__init__(builder, *args, **kwds)

        # Meta
        self.meta = ['', '']  # HTMLWriter strips out the first two items from Translator.meta
        self.add_meta('<meta http-equiv="X-UA-Compatible" content="IE=edge">')
        self.add_meta('<meta name="viewport" content="width=device-width, initial-scale=1">')

        # Tělo
        self.body = []
        self.fragment = self.body
        self.html_body = self.body
        # název dokumentu
        self.title = []
        self.start_document_title = 0
        self.first_title = False

        self.context = []
        self.section_level = 0

        self.first_param = 1
        self.param_separator = ','

    def encode(self, text):
        return str(text).translate({
            ord('&'): '&amp;',
            ord('<'): '&lt;',
            ord('"'): '&quot;',
            ord('>'): '&gt;',
            0xa0: '&nbsp;'
        })

    def unknown_visit(self, node):
        print("unknown node", node.__class__.__name__)
        self.body.append(f'[UNKNOWN NODE {node.__class__.__name__}]')
        raise nodes.SkipNode

    # POZNÁMKA: když tento komentář odstraníme nebo přidáme, zobrazí se tituly pětkrát v globálním obsahu
    def visit_document(self, node):
        self.first_title = True
    def depart_document(self, node):
        pass

    # Připomínka účetnictví je v komentářích zrušena
    def visit_section(self, node):
        # blízký „rodič“ nebo předchozí část, pokud se nejedná o úvodní část.
        # první část
        if self.section_level:
            self.body.append('</section>')
        self.section_level += 1

        self.body.append(self.starttag(node, 'section'))
    def depart_section(self, node):
        self.section_level -= 1
        # uzavřít poslední část dokumentu
        if not self.section_level:
            self.body.append('</section>')

    # přepsané
    # Třídní mapování:
    # upozornění [název] -> upozornění - [název]
    # Zajistit, aby se uvedený titul zobrazoval jako třída v elementu
    def visit_admonition(self, node, name=''):
        # typ: (nodes.Node, unicode) -> None
        node_classes = ["alert"]
        if name:
            node_classes.append(ADMONITION_MAPPING[name])
        self.body.append(self.starttag(
            node, 'div', CLASS=" ".join(node_classes)))
        if name:
            node.insert(0, nodes.title(name, admonitionlabels[name]))

    # přepsané
    # Přidá třídu alert-title do tagu p, pokud je rodičem Admonition.
    def visit_title(self, node):
        # typ: (nodes.Node) -> None
        if isinstance(node.parent, nodes.Admonition):
            self.body.append(self.starttag(node, 'p', CLASS='alert-title'))
        else:
            super().visit_title(node)

    def depart_title(self, node):
        if isinstance(node.parent, nodes.Admonition):
            self.body.append("</p>")
        else:
            super().depart_title(node)

    def visit_literal(self, node):
        """Překrytí, které přidá třídu „o_code“ ke všem rolím „literal“, „code“ a „file“."""
        node['classes'].append('o_code')
        return super().visit_literal(node)

    def visit_literal_strong(self, node):
        """Překryjte třídu, která přidává třídu o_code pro všechny role command."""
        if 'command' in node['classes']:
            node['classes'].append('o_code')
        return super().visit_literal_strong(node)

    # přepsané
    # Zajistěte přítomnost třídy pro tabulky
    def visit_table(self, node):
        # typ: (nodes.Node) -> None
        self.generate_targets_for_table(node)

        # kopie z https://github.com/pydata/pydata-sphinx-theme/pull/509/files
        self._table_row_indices.append(0)

        classes = [cls.strip(' \t\n')
                   for cls in self.settings.table_style.split(',')]
        classes.insert(0, "docutils")  # compat
        classes.insert(0, "table")  # compat

        if 'align' in node:
            classes.append('align-%s' % node['align'])
        tag = self.starttag(node, 'table', CLASS=' '.join(classes))
        self.body.append(tag)
