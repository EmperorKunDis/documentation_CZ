.. atribut:: sloupec_neviditelný
:noindex:

Zda je sloupec viditelný („false“) nebo skrytý („true“), jako v Pythonu vyhodnocovaná výrazová
na logickou hodnotu.

Výraz „neviditelný“ se vztahuje na celou sloupcovou hodnotu a nebere v úvahu podřetězec.

...... příklad::
... kódový blok::xml

<vlastnost produkt_je_pozde vložení skrytého rodiče, pokud je nesprávný parametr has_late_products==False
<tlačítko typu "objekt" jméno="akce_potvrdit" sloupec_neviditelný="kontext.get('skrýt_potvrzení')"/>

:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:výchozí hodnota: „Pravda“
