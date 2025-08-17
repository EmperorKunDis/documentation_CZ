from docutils import nodes
from docutils.parsers.rst import roles
from sphinx import addnodes
from sphinx.environment.adapters import toctree

from . import pygments_override, translator


def setup(app):
    app.set_translator('html', translator.BootstrapTranslator)

    app.connect('html-page-context', set_missing_meta)

    app.add_js_file('js/utils.js')  # Keep in first position
    app.add_js_file('js/layout.js')
    app.add_js_file('js/menu.js')
    app.add_js_file('js/page_toc.js')
    app.add_js_file('js/switchers.js')

    roles.register_canonical_role('icon', icon_role)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }

def set_missing_meta(app, pagename, templatename, context, doctree):
    if context.get('meta') is None:  # Pages without title (used with `include::`) have no meta
        context['meta'] = {}

class Monkey:
    """Vyměnit metodu objektu za novou, která přijímá starou jako argument."""
    def __init__(self, obj):
        self.obj = obj
    def __call__(self, fn):
        name = fn.__name__
        old = getattr(self.obj, name)
        setattr(self.obj, name, lambda self_, *args, **kwargs: fn(old, self_, *args, **kwargs))

@Monkey(toctree.TocTree)
def resolve(old_resolve, tree, docname, *args, **kwargs):

    def _update_toctree_nodes(_node) -> None:
        """ Make necessary changes to Docutils' nodes of the toc.

Vnitřní struktura uzlů TOC:
<ul>
<li>

<ul>
                    ...

</li>

<ul/>
        """
        if isinstance(_node, nodes.reference):  # The node is a reference (<a/>)
            _node_docname = _get_docname(_node)
            _clear_reference_if_empty_page(_node, _node_docname)
            _set_docname_as_class(_node, _node_docname)
        elif isinstance(_node, (addnodes.compact_paragraph, nodes.bullet_list, nodes.list_item)):
            for _subnode in _node.children:
                _update_toctree_nodes(_subnode)

    def _get_docname(_node):
        """ Return the docname of the targeted document.

docname = nějaký běžný kořen / foo / bar / stránka, která se zobrazuje
_ref = /contributing/documentation
_path_parts = ['..', '..', 'přispívání', 'dokumentace']
res = ['nějaký společný kořen', 'přispívání', 'dokumentace']
_docname = nějaký_obecný_kořen/příspěvky/dokumentace

:návratová hodnota: Docname dokumentu, na který se vztahuje _node, tj. relativní cesta od kořenového adresáře
adresář zdrojů dokumentace (složka „content/“).
:rtype: str
        """
        _ref = _node['refuri'].replace('.html', '')
        _parent_directory_occurrences = _ref.count('..')
        if not _parent_directory_occurrences and '/' not in docname:
            # Aktuální dokument je v kořenové složce zdrojů dokumentace.
            # (např. docname == „index“ | „aplikace“ | ...). Tedy odkaz je již docname.
            _docname = _ref
        else:
            _path_parts = _ref.split('/')
            _res = docname.split('/')[:-(_parent_directory_occurrences+1)] \
                   + _path_parts[_parent_directory_occurrences:]
            _docname = '/'.join(_res)
        return _docname

    def _clear_reference_if_empty_page(_reference_node, _node_docname):
        """ Clear reference of 'empty' toctree pages.

Prozkoumejte sourozence rodičovského uzlu, abyste zjistili, zda uzel odkazuje na obsah a pokud ano,
odstranit svou referenční URL.
Pokud stránka obsahuje metadatový soubor „show-content“, nevymažte odkaz.
        """
        if _node_docname and any(
            isinstance(_subnode, nodes.bullet_list)
            for _subnode in _reference_node.parent.parent.children
        ):  # The node references a toc
            if 'show-content' not in tree.env.metadata[_node_docname]:
                _reference_node['refuri'] = '#'  # The page must not be accessible

    def _set_docname_as_class(_reference_node, _node_docname):
        _node_docname = _node_docname or docname  # refuri==None <-> href="#"
        _reference_node.parent.parent['classes'].append(f'o_menu_{_node_docname.replace("/", "_")}')

    resolved_toc = old_resolve(tree, docname, *args, **kwargs)
    if resolved_toc:  # `resolve` returns None if the depth of the TOC to resolve is too high
        _update_toctree_nodes(resolved_toc)
    return resolved_toc


def icon_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """Implementujte roli „ikona“ pro Odoo a Font Awesome ikony."""
    for icon_class in text.split():
        if not (icon_class.startswith('fa-') or icon_class.startswith('oi-') \
            or icon_class.startswith('os-')):
            report_error = inliner.reporter.error(
                f"'{icon_class}' is not a valid icon formatting class.", lineno=lineno
            )
            error_node = inliner.problematic(rawtext, rawtext, report_error)
            return [error_node], [report_error]
    if text.startswith('oi-'):
        icon_html = f'<i class="oi {text}"></i>'
    elif text.startswith('fa-'):
        icon_html = f'<i class="fa {text}"></i>'
    elif text.startswith('os-'):
        icon_html = (
            '<svg class="os-icon" aria-hidden="true" role="img">'
                f'<use href="#{text[3:]}" />' # [3:] strips 'os-' specifier from svg id
             '</svg>'                         # see ../static/img/odoo-spreadsheets-icons.svg
        )
    else:
        icon_html = f'<i class="{text}"></i>'
    return [nodes.raw('', icon_html, format='html')], []
