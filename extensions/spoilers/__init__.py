from docutils import nodes
from sphinx.locale import get_translation
from sphinx.util.docutils import SphinxDirective


class Spoiler(SphinxDirective):
    """Implementujte příkaz „spoiler“ s komponentou rozbalovacího seznamu v Bootstrapu."""
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    def run(self):
        """ Process the content of the directive.

Používáme vlastní třídy uzlů, které reprezentují HTML prvky (např. div).
odpovídající třídu sphinx.nodes.* (např. sphinx.nodes.container), aby se zabránilo automatickému
nastavení názvu uzlu jako třídy (např. „obal“) na prvku.
        """
        _ = get_translation('spoilers')
        self.assert_has_content()
        spoiler_id = self.env.new_serialno("spoiler")
        heading_id = f'o_spoiler_header_{spoiler_id}'
        content_id = f'o_spoiler_content_{spoiler_id}'

        # Vytvořte hlavní kontejner s akordy.
        accordion_container = Container(
            classes=['accordion', 'accordion-flush', 'o_spoiler', 'alert']
        )  # Reuse the SCSS rules already defined for `alert`. Same thing for `alert-title`.

        # Vytvořte kontejner pro položky akordeonu.
        accordion_item_container = Container(classes=['accordion-item'])
        accordion_container.append(accordion_item_container)

        # Vytvořte hlavičku.
        header = Header(ids=[heading_id], classes=['accordion-header'])
        accordion_item_container.append(header)

        # Vytvořte tlačítko přepínače.
        button = Button(
            classes=[
                'accordion-button', 'collapsed', 'flex-row-reverse', 'justify-content-end',
                'fw-bold', 'p-0', 'border-bottom-0'
            ],
            **{
                'type': 'button',
                'data-bs-toggle': 'collapse',
                'data-bs-target': f'#{content_id}',
                'aria-expanded': 'false',
                'aria-controls': content_id,
            }
        )
        header.append(button)

        # Vytvořte název tlačítka.
        label = self.arguments[0] if self.arguments else _("Spoiler")
        button_label = nodes.Text(label)
        button.append(button_label)

        # Vytvořte kontejner pro skládání harmoniky.
        accordion_collapse_container = Container(
            ids=[content_id],
            classes=['accordion-collapse', 'collapse', 'border-bottom-0'],
            **{'aria-labelledby': heading_id},
        )
        accordion_item_container.append(accordion_collapse_container)

        # Vytvořte kontejner s rozbalovacími panely.
        accordion_body_container = Container(classes=['accordion-body'])
        self.state.nested_parse(self.content, self.content_offset, accordion_body_container)
        accordion_collapse_container.append(accordion_body_container)

        return [accordion_container]


class Container(nodes.General, nodes.Element):
    custom_tag_name = 'div'


class Header(nodes.General, nodes.Element):
    custom_tag_name = 'span'


class Button(nodes.General, nodes.Element):
    custom_tag_name = 'button'


def visit_node(translator, node):
    custom_attr = {k: v for k, v in node.attributes.items() if k not in node.known_attributes}
    translator.body.append(translator.starttag(node, node.custom_tag_name, **custom_attr).rstrip())


def depart_node(translator, node):
    translator.body.append(f'</{node.custom_tag_name}>')


def setup(app):
    app.add_directive('spoiler', Spoiler)
    app.add_node(Container, html=(visit_node, depart_node))
    app.add_node(Header, html=(visit_node, depart_node))
    app.add_node(Button, html=(visit_node, depart_node))
    return {
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
