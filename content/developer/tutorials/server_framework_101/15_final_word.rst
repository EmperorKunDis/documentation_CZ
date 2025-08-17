==========================
Kapitola 15: Konečné slovo
==========================

Pravidla pro psaní kódu
=================

Začneme refaktorovat kód, aby odpovídal pravidlům pro psaní kódu v Odoo.
aby se zlepšila kvalita kódu aplikací Odoo.

**Poznámka**: najdete v ní kódování Odoo.
:doc:`/přispívání/vývoj/kódování_pravidla`.

..cvičení: Vylepšujte svůj kód.

Refaktorujte svůj kód, aby respektoval kodérské zásady. Nezapomeňte spustit svého lintera a
respektovat modulovou strukturu, názvy proměnných a konvence jmen metod, stejně jako model.
přidat atributy pořadí a XML identifikátory.

Test na běhací robot
==================

Odoo má vlastní CI server s názvem „runbot“ (<https://runbot.odoo.com/>).
zavádí se, větve a PR budou testovány, aby se předešlo regresím nebo porušení stabilních verzí.
Všechny testované běhy jsou nasazeny na vlastním serveru s demodatami.

...cvičení: Hra s robotem na běhání.

Navštivte webovou stránku runbot a otevřete poslední stabilní verzi Odoo, abyste zkontrolovali všechny dostupné
aplikace a funkce.
