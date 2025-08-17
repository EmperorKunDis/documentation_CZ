.. atribut: default_order
:noindex:

Seznam polí, která převezmou pořadí definované na modelu.
atribut ~odoo.models.BaseModel._order.

Pro obrácený pořadí řazení pole přidejte k jeho názvu znak „desc“, oddělený mezerou.

...... příklad::
... kódový blok::xml

<list default_order="seřadit podle sekvence a jména sestupně">
             ...
</seznam>

:volitelné
:typ: str
:default: „“
