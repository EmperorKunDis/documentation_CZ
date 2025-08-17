from docutils.parsers.rst import Directive, directives


class PlaceHolder(Directive):
    """Třída, která slouží jako místo pro příkazy, které musí být přeskočeny."""

    has_content = True

    def run(self):
        return []  # Return an empty list of nodes


def setup(app):
    directives.register_directive('automodule', PlaceHolder)
    directives.register_directive('autoclass', PlaceHolder)
    directives.register_directive('autoexception', PlaceHolder)
    directives.register_directive('autofunction', PlaceHolder)
    directives.register_directive('autodecorator', PlaceHolder)
    directives.register_directive('autodata', PlaceHolder)
    directives.register_directive('automethod', PlaceHolder)
    directives.register_directive('autoattribute', PlaceHolder)
    directives.register_directive('autofield', PlaceHolder)
    directives.register_directive('automodel', PlaceHolder)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
