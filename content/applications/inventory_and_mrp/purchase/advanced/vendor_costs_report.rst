===================
Zpráva o nákladech dodavatele
===================

.. |RFQ| nahradit za: zkratku: „RfQ (žádost o nabídku)“
.. |RFQ| nahrazuje: :abbr:`RfQ (požadavky na nabídku)“
.. |POs| nahradit za: zkratka: `POs (Purchase Orders)`
.. |caret| nahradit:: :icon:`fa-caret-down` :guilabel:`(dolů)`

S aplikací Purchase mohou uživatelé sledovat kolísání nákladů na dodavatele v čase.
Uživatelům umožňuje identifikovat nejdražší dodavatele a sledovat sezónní změny.

Vytvořit nákladové reporty pro dodavatele
===========================

Pro vytvoření nákupního reportu se nejprve přesunete na: „Nákupní aplikace --> Zprávy“.
Klikněte na tlačítko „Nákup“ pro otevření panelu „Analýza nákupu“. Výchozí nastavení zobrazuje
Grafické shrnutí tabulky „Nepodané celkem“ POs (nákupních objednávek) s
„Datum potvrzení“ pro aktuální měsíc nebo požadavků na nabídky (RFQ – Request for Quotation).
Stav „Návrh“, „Odesláno“ nebo „Zrušeno“.

.._nákupní/prodejní cenový report filtrů:

Přidejte filtry a skupiny
----------------------

V pravém horním rohu klikněte na ikonu „Pohled na sloupce“ (pivot) a přepněte se do pohledu na sloupce.

Odeberte všechny výchozí filtry z lišty „Hledat…“. Pak klikněte na |caret| a otevřete
padající nabídka, která obsahuje filtry, skupiny a
Sloupce „Oblíbené“.

.. poznámka::
Výchozí nastavení zobrazuje data ze všech RFQ a PO.
změnit výběrem buď „Nabídky“ nebo „Objednávek“.
pod sloupcem Filtry.

V sloupci Filtry vyberte datový rozsah pro porovnání. Zpráva může být
filtrované buď podle „Datum objednání“ nebo „Datum potvrzení“. Vyberte si jeden z
listu a klikněte na |caret| pro určení rozsahu dat, buď měsíce, čtvrtletí nebo roku.

Dále pod sloupcem „Skupina“ vyberte „Dodavatel“. Pak vyberte
„Produkt“, který je také umístěn v sloupci „Skupina“.

.. poznámka::
Vybrat položku „Produkt“ není pro tento výkaz nutné, ale je doporučeno, protože
Provádí další analýzu výkonnosti jednotlivých dodavatelů a nabízí další možnosti výběru.
Může být také vytvořen pod záložkou „Skupina“ a zahrnout i „Produkt“.
Kategorie, stav a zástupce pro nákup.

Aby byl report vytvořen správně, ujistěte se, že je nastaveno pole „Dodavatel“ jako první.
výběr provedený podle sloupce :guilabel:`Group By`.

Dále vyberte možnost pod nadpisem „Srovnání“. Tyto možnosti jsou k dispozici
Po výběru rozsahu dat pod sloupcem Filtry se mohou měnit v závislosti na tomto rozsahu.
:guilabel:`Předchozí období“ přidává srovnání předchozího období, například posledního měsíce nebo
čtvrtletí. Výchozím obdobím je stejné čtvrtletí předchozího roku.

.. poznámka::
Ve filtru můžete přidávat více časových filtrů najednou, ale k porovnání lze vybrat pouze jeden.
čas.

.. obrázek:vendor_costs_report/filters-groups.png
:align:center
:alt: Rozbalovací nabídka filtrů, skupin a možností srovnání pro výkaz nákladů dodavatelů.

Přidat opatření
------------

Po výběru nastavení filtrů, skupinování a porovnání
klikněte na položku v rozbalovacím seznamu.

Výchozí zobrazení reportu obsahuje následující měřítka: :guilabel:`Objednávky“, :guilabel:`Celkem“.
:guilabel:`Celkem nezdaněných“, a :guilabel:"Počet". Klikněte na „Měřítka“ v horním levém rohu, abyste otevřeli
seznam dostupných měřítek. Klikněte na položku „Průměrná cena“ a přidejte ji do zprávy.
Vyberte další kroky, které chcete přidat do zprávy, nebo klikněte na některý z již vybraných.
opatření k odstranění těchto prvků, pokud je to požadováno.

..tip:
Je doporučeno spustit zprávu s alespoň jednou z následujících hodnot: „Průměrná cena“, „Celkem“ nebo
:guilabel:`Celkem nezdaněných“ vybraný z seznamu :guilabel:`Měření“. Kromě toho lze použít další měření, například
:guilabel:`Dny k doručení“ mohou být přidány, aby poskytly další informace.

Zobrazit výsledky
============

Po výběru všech filtrů a měření
„Příjemce/dodavatel – náklady na zboží“, což je výchozí nastavení, a report se vytvoří ve formátu přehledu. Klikněte
:guilabel:`Vložit do tabulky“ pro vložení pohledu na sestavování do formátu editovatelné tabulky
aplikace Dokumenty*.

.. důležité:
Volba „Vložit do tabulky“ je dostupná pouze v případě, že se aplikace *Dokumenty Tabulka*
modul je nainstalován.

.. obrázek: vendor_costs_report/sample-vendor-report.png
:align:center
:alt: Vzorek výkazu nákladů prodejce s měřítky celkových a průměrných nákladů.

.. poznámka::
Výkaz o nákladech na dodavatele je také k dispozici v grafickém zobrazení. Klikněte na ikonu :icon:`fa-area-chart`.
:guilabel:`(oblastový graf)` ikonu pro přepnutí na grafický pohled. Klikněte na příslušnou ikonu v horní části
výstup přepnout na :icon:`fa-bar-chart` :guilabel:`(bar chart)` nebo :icon:`fa-line-chart`
:guilabel:`(svislá osa)“, nebo :icon:`fa-pie-chart“ :guilabel:`(kruhová grafika)“.

.. viz též:
Chcete-li si tento výstup uložit jako oblíbený, podívejte se na :ref:`vyhledávání/oblíbené`.
