from docutils import nodes
from docutils.parsers.rst import Directive, directives


class PlaceHolder(Directive):
    """Třída, která slouží jako místo pro příkazy, které musí být přeskočeny."""

    has_content = True

    def run(self):
        node = nodes.literal_block('graphviz', '')
        node += nodes.Text(
            f'{self.content[0]}\n'
            '> Graph not rendered because `dot` is not installed'
        )
        return [node]


def setup(app):
    directives.register_directive('graphviz', PlaceHolder)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
