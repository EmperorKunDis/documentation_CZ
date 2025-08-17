.. atribut: skupiny
:noindex:

Seznam uživatelských skupin, pro které je prvek zobrazen. Uživatelé, kteří nepatří do žádné
k alespoň jednomu z těchto skupin není vidět prvek. Skupiny lze předřadit s předponou
negativní operátor „!“, který je vylučuje.

...... příklad::

... kódový blok::xml

<pole název="POLE_NÁZEV" skupiny="základní.skupina_bez_účetních,!základní.skupina_s_více_společnostmi"/>

:volitelné
:typ: str
:default: „“
