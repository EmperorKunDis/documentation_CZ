===============
Předpověď
===============

.. |caret| nahradit:: :icon:`fa-caret-down` :guilabel:`(dolů)`
.. |pivot| nahradit:: :ikonka:`oi-view-pivot` :guilabel:`(pivot)`
.. |seznam| nahradit za: :icon:`oi-view-list` :guilabel:`(seznam)`

V aplikaci CRM je k dispozici zpráva Forecast, která umožňuje uživatelům prohlížet seznam nadcházejících příležitostí a vytvářet
předpověď potenciálních prodejů. Možnosti jsou seskupeny podle měsíce očekávaného uzavření
A můžete je přetáhnout a pustit, abyste upravili termín.

Chcete-li zobrazit výhledový report, přejděte na: „Aplikace CRM -> Hlášení -> Výhled“.

Přejděte na předpověď
============================

Výchozí zpráva „Předpověď“ včetně příležitostí přidělených uživateli aktuálního
trubky a uzavření je očekáváno do čtyř měsíců. Ukazuje také příležitosti bez
předpokládaný termín uzavření příležitosti. Možnosti jsou seskupeny podle měsíce v :icon:`oi-view-kanban`
Zobrazení „(Kanban)“.

.. obrázek: předpověď/vzorek zprávy.png
:align:center
:alt: Vzorová verze výstupu předpovědi v aplikaci CRM.

Očekávaný termín uzavření
---------------------

Možnosti jsou seskupeny podle data, které bylo přiřazeno v poli „Očekávané uzavření“
formulář. Chcete-li tuto datum změnit přímo z karty kanbanu na stránce „Výhled“, vyberte
Poté klikněte a přetáhněte kartu do požadované sloupce.

.. poznámka::
Výchozí časový rámec pro předpověď je měsíc. Tento můžete změnit kliknutím na
vedle pole „Hledat…“ v horní části zprávy. Pod položkou „Skupit podle“
vzniklém rozbalovacím seznamu klikněte na položku „Očekávané uzavření“ pro zobrazení dalšího
dostupné možnosti a vyberte požadovanou dobu z nabídky.

Po přidání příležitosti do nového měsíce se pole „Očekávané uzavření“ na formuláři příležitosti
je aktualizována na poslední den nového měsíce.

..tip:
Pole „Očekávané uzavření“ můžete také ručně aktualizovat na kartě příležitosti.
Klikněte na kartu Kanban pro příležitost na stránce Forecast, aby se otevřela
podrobné informace o příležitosti. Klikněte na pole „Očekávané uzavření“ a použijte kalendář
pop-up okno pro výběr nového data uzávěrky.

Přepočtená tržba
----------------

Na stránce s výkazem Forecast je v horní části sloupce pro každý měsíc, vedle
Progresová lišta je součtem procentuálního příjmu za dané období.

Částečný příjem se vypočítává podle vzorce níže:

.. matematika::

\text{Očekávaný příjem} \krát \text{Věrohodnost} = \text{Způsobilost pro úhradu}

Když se příležitosti přesouvají z jedné sloupce do druhé, automaticky se aktualizuje příjmy této sloupce.
aby odrážela změnu.

Příklad:
V předpovědi pro červen je dvě příležitosti:

První příležitost, „Global Solutions“, má očekávaný příjem 3800 $, a pravděpodobnost
„90 %“. To vede k tomu, že celkový příjem je 3 420 $.

Druhá příležitost „Citace pro 600 židlí“ má očekávaný příjem $22,500.
20%. To znamená, že se vypočítá odpovídající daň z příjmu ve výši 4 500 $.

Kombinovaný procentuální příjem z příležitostí je 7 920 $, což je uvedeno na vrcholu
sloupec pro měsíc.

...... obrázek: předpověď/výdělek.png
:synchronizace: střed
:alt: Příklad procentuálního příjmu za jeden měsíc z předpovědní zprávy.

.. viz též:
Pro více informací o tom, jak je pravděpodobnost přiřazována příležitostem, se podívejte na
:doc:`../track_leads/lead_scoring`

Zobrazit výsledky
============

Klikněte na ikonu „fa-area-chart“ („oblastní graf“) a přepněte se do grafického zobrazení. Pak klikněte
přepnout na graf v podobě sloupce (bar)
diagram`, :ikona: `fa-line-chart` :guilabel: (line diagram), nebo :ikona: `fa-pie-chart` :guilabel:
Graf).

.. obrázek: predpoved_zpravy/graf.png
:align:center
:alt: Zobrazení grafu v předpovědním výkazu.

Klikněte na |pivot| pro přepnutí do zobrazení sloupce nebo na |list| pro přepnutí do seznamového zobrazení.

..tip:
Pohled na data lze získat pomocí :ref:`pivotového pohledu <reporting/using-pivot>`, který umožňuje
v hlubších souvislostech. Můžete vybrat více opatření a zobrazit údaje podle měsíců a podle
stádium příležitosti.

.. obrázek:: předpověď/pivot-view.png
:synchronizace: střed
:alt: Vzorek předpovědi v přepínačovém pohledu.

.. viz též:
Chcete-li si tento výstup uložit jako oblíbený, podívejte se na :ref:`vyhledávání/oblíbené`.
