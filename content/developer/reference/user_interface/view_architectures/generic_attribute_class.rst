.. atribut: třída
:noindex:

Řetězec HTML třídy, který se má nastavit na vytvořeném prvku.

Stylování používá rámec Bootstrap <https://getbootstrap.com> a ikony UI:
<odoo/reference/user_interface/ui_icons>. Klasické třídy Odoo zahrnují:

   - `oe_inline`: zabraňuje běžnému řádkování za poli a omezuje jejich rozsah.
   - „oe_left“, „oe_right“: „plovoucí <https://cs.wikipedia.org/wiki/CSS#FLOAT>“
prvek do odpovídajícího směru.
   - `oe_read_only`, `oe_edit_only`: zobrazuje pouze prvek v příslušném režimu formuláře.
   - `oe_avatar`: pro obrázkové pole zobrazuje obrázek jako „avatara“ (maximálně čtverec o rozměrech 90x90).
   - „oe_stat_button“: definuje konkrétní způsob zobrazení informací, které se dynamicky zobrazí
kliknutím na něj lze vyvolat akci.

...... příklad::
... kódový blok::xml

<položka jméno="fname" třída="oe_inline oe_left oe_avatar"/>

...... příklad::
... kódový blok::xml

<tlačítko typu "objekt" jméno="AKCE" třída="oe_stat_button" ikona="FONT_AWESOME" pomoc="POMOC">
<div třída="o_field_widget" třída="o_stat_info">
<span class="o_stat_value"><FIELD/></span>
<span class="o_stat_text">TEXT</span>
</div>
</tlačítko>

:volitelné
:typ: str
:default: „“
