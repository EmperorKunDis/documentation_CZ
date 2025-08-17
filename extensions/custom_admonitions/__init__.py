"""Přidat nové vlastní příkazy pro upozornění."""

from docutils import nodes
from docutils.parsers.rst.directives import admonitions
from sphinx.locale import admonitionlabels
from sphinx.util.docutils import SphinxRole


class example(nodes.Admonition, nodes.Element):
    pass


class Example(admonitions.BaseAdmonition):
    node_class = example


class exercise(nodes.Admonition, nodes.Element):
    pass


class Exercise(admonitions.BaseAdmonition):
    node_class = exercise


class Dfn(SphinxRole):
    """Změňte roli „dfn“ na použití vlastního HTML."""

    def run(self):
        """ Process the content of the role.

Pro zobrazení „pásu“ používáme vlastní třídy uzlů namísto odpovídajících
klasifikátorů * sphinx.nodes, aby se zabránilo automatickému nastavení názvu uzlu jako třídy (např.
„obal“ na prvku.
        """
        outer_span = DfnSpan(classes=['dfn'])
        inner_span = DfnSpan()
        outer_span.append(inner_span)
        text = nodes.Text(self.text)
        inner_span.append(text)
        return [outer_span], []


class DfnSpan(nodes.General, nodes.Element):

    @staticmethod
    def visit(translator, node):
        translator.body.append(translator.starttag(node, 'span').rstrip())

    @staticmethod
    def depart(translator, node):
        translator.body.append('</span>')


def setup(app):
    app.add_directive('example', Example)
    app.add_node(example, html=(
        lambda self, node: self.visit_admonition(node, 'example'),
        lambda self, node: self.depart_admonition(node),
    ))
    app.add_directive('exercise', Exercise)
    app.add_node(exercise, html=(
        lambda self, node: self.visit_admonition(node, 'exercise'),
        lambda self, node: self.depart_admonition(node),
    ))
    app.add_role('dfn', Dfn(), override=True)
    app.add_node(DfnSpan, html=(DfnSpan.visit, DfnSpan.depart))

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }


admonitionlabels['example'] = 'Example'
admonitionlabels['exercise'] = 'Exercise'
