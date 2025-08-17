"""
ReST příkaz pro vložení videí z YouTube a Vimea.
Dva nové příkazy byly přidány: „youtube“ a „vimeo“. Jediný
argumentem je identifikátor videa, které chceme zahrnout.
Oba příkazy mají tři volitelné parametry: „výška“, „šířka“
a „srovnat“. Výchozí výška je 281 a šířka 500.
Příklad:
.. youtube:: anwy2MPT5RE
:výška: 315
:šířka: 560
:srovnání: vlevo
:copyright: (c) 2012 Danilo Bargen
:licence: BSD 3-členská
"""
from docutils import nodes
from docutils.parsers.rst import Directive, directives


def align(argument):
    """Funkce převodu pro možnost „srovnat“."""
    return directives.choice(argument, ('left', 'center', 'right'))


class IframeVideo(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'height': directives.nonnegative_int,
        'width': directives.nonnegative_int,
        'align': align,
    }
    default_width = 500
    default_height = 281

    def run(self):
        self.options['video_id'] = directives.uri(self.arguments[0])
        if not self.options.get('width'):
            self.options['width'] = self.default_width
        if not self.options.get('height'):
            self.options['height'] = self.default_height
        if not self.options.get('align'):
            self.options['align'] = 'left'
        return [nodes.raw('', self.html % self.options, format='html')]


class Youtube(IframeVideo):
    html = '<iframe src="https://www.youtube.com/embed/%(video_id)s" \
    width="%(width)u" height="%(height)u" frameborder="0" \
    webkitAllowFullScreen mozallowfullscreen allowfullscreen \
    class="align-%(align)s"></iframe>'


class Vimeo(IframeVideo):
    html = '<iframe src="https://player.vimeo.com/video/%(video_id)s" \
    width="%(width)u" height="%(height)u" frameborder="0" \
    webkitAllowFullScreen mozallowfullscreen allowFullScreen \
    class="align-%(align)s"></iframe>'


def setup(app):
    directives.register_directive('youtube', Youtube)
    directives.register_directive('vimeo', Vimeo)

    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }
