===========
Přídatné produkty
===========

.. |MO| nahradit za: zkratka: `MO (manufacturing order)`
.. |BoM| nahradit::: zkratka: BoM (seznam materiálů)
.. |BoMs| nahrazuje:: :abbr:`BoMs (seznamy materiálů)`

Výroba některých produktů zanechává po sobě i odpadní materiál navíc.
hotový výrobek. Tyto materiály jsou známé jako vedlejší produkty. Specifikací vedlejších produktů
vzniklé při výrobě na seznamu materiálů (BOM) produktu, množství vedlejších produktů
Skladové zásoby jsou sledovány pomocí Odoo.

Příklad:
Výroba křesílka vyžaduje deset kusů dřeva. Během výroby se spotřebují pět kusů
Kromě křesílka vznikají také další věci z odpadního dřeva. Odpadní dřevo se označuje za
odpad na houpací síti |BoM|, Odoo sleduje skladovou zásobu odřezků dřeva a také
počet vyrobených houpaček.

Konfigurace
=============

Chcete-li uvést vedlejší produkty na seznamu výrobku (BoM), musí být nastavení vedlejších produktů povoleno.
takže přejděte na: „Výroba -> Konfigurace -> Nastavení“ a zaškrtněte
zaškrtávací políčko „Přídavky“ pod nadpisem „Operace“. Pak klikněte
:guilabel:`Uložit“ pro aplikaci změn.

.. obrázek: vedlejší produkty/vedlejší produkty-nastavení.png
:align:center
:alt:Nastavení vedlejších produktů v nastavení aplikace Manufacturing.

Pokud je zapnuto nastavení „Nepotravinářské produkty“, objeví se v kartě „Nepotravinářské produkty“
BOM).

Přidejte vedlejší produkt do BoM
====================

Přidat vedlejší produkty do BoM, přejděte na: „Výroba“ -> „Produkty“ -> „Faktury“.
Výrobků“, vyberte „|BoM|“.

Na BoM vyberte záložku „Přídavky“. Klikněte na „Přidat řádek“ a vyberte
V poli „Příloha“ vyberte možnost „Příloha“. Do pole „Množství“ zadejte
množství vedlejšího produktu vzniklého při výrobě.

Pokud se vedlejší produkt vyrábí při provádění konkrétní operace výrobního příkazu (MO), vyberte
operace v poli „Výrobek“ v operaci. Například pokud je vedlejším produktem dřevní štěpka
Vyrobené během operace *Assemble*, vyberte tuto operaci v poli :guilabel:`Vyrobeno
Operační pole.

.. obrázek: vedlejší produkty/vedlejší produkty-tab.png
:align:center
:alt:Karta vedlejších produktů v BOM s „odpadem dřeva“ jako vedlejším produktem.

Výrobní odpad
======================

Když je |MO| dokončeno a označeno jako *Dokončeno*, Odoo zaznamenává množství vedlejších produktů vytvořených
během výrobního procesu. Chcete-li vytvořit nový |MO|, přejděte na:
app --> Operace --> Výrobní objednávky“ a klikněte na „Nový“.

V poli „Seznam materiálů“ vyberte BoM, na němž jsou uvedeny vedlejší produkty.
Po provedení takového kroku se pole „Produkt“ automaticky vyplní odpovídajícím produktem. Klikněte
:guilabel:`Potvrdit` pro potvrzení |MO|.

Když je výroba dokončena, klikněte na tlačítko „Vyrobit vše“ nahoře nad |MO|.
Po provedení takového kroku se zásoby aktualizují a odráží množství vedlejšího produktu (produktů), který byl vyroben.
Jde o množství produktu.

Klikněte na tlačítko „Produkt se pohybuje“ v horní části stránky, abyste viděli pohyby produktu
součástek a produktů. Každý vedlejší výrobek je uveden v seznamu :guilabel:`Inventářních pohybů`.
stránka s sloupcem :guilabel:`Od“ zobrazujícím virtuální místo produkce a
:guilabel:„Tam“ slouží pro zobrazení místa, kde se vedlejší produkt skladuje.

.. obrázek: vedlejší produkty/pohyb výrobku.png
:align:center
:alt:Stránka s pohybem produktů pro MO s vedlejšími produkty.
