===========================
Zpráva o nákladech na pořízení
===========================

.. |RFQ| nahradit za: zkratku: „RfQ (žádost o nabídku)“
.. |RFQ| nahrazuje: :abbr:`RfQ (požadavky na nabídku)“
.. |POs| nahradit za: zkratka: `POs (Purchase Orders)`
.. |PO| nahradit za: abbr: PO (objednávka)
.. |caret| nahradit:: :icon:`fa-caret-down` :guilabel:`(dolů)`
.. |per| nahradit za: nákupní výkaz

S aplikací „Nákup“ mohou uživatelé sledovat výdaje za nákupy v čase. Tento report jim pomáhá
Společnosti sledují a analyzují výdaje, identifikují příležitosti ke snížení nákladů a zajišťují efektivitu.
rozpočtový management.

Vytvořte výkaz nákladů na pořízení
==================================

Nejprve přejděte na „Nákupní aplikace -> Zprávy -> Nákup“.
otevřete panel „Analýza nákupu“.

Výchozí nastavení zobrazuje přehled liniového grafu Untaxed Total.
„Nákupní objednávky“ („PO“) s „Datem potvrzení“ pro aktuální měsíc nebo
Nabídky s výzvou k podání nabídek (RFQ) se stavem „Připravované“, „Odeslané“ nebo „Zrušené“.

Přidejte filtry a skupiny
----------------------

V pravém horním rohu klikněte na ikonu „Pohled na sloupce“ (pivot) a přepněte se do pohledu na sloupce.

..tip:
Zatímco |per| lze také považovat za :ref:`výsledky nákupu <purchase/view-results> ve formě grafu
:guilabel:`(svislá osa)` nebo :icon:`fa-line-chart` :guilabel:`(svislá osa)`
:guilabel:`(položka v grafu)“ poskytuje nejpodrobnější pohled na data a je to
doporučený startovní bod.

Odeberte všechny výchozí filtry z lišty „Hledat…“. Pak klikněte na |caret| a otevřete
padající nabídka, která obsahuje filtry, skupiny a
Sloupce „Oblíbené“.

.. poznámka::
Výchozí nastavení zobrazuje data ze všech RFQ a PO.
změnit výběrem buď „Nabídky“ nebo „Objednávek“.
pod sloupcem Filtry.

V sloupci Filtry vyberte časové období pro porovnání. Zpráva může být
filtrované buď podle „Datum objednání“ nebo „Datum potvrzení“. Vyberte si jeden z
listu a klikněte na |caret| pro určení rozsahu dat, buď měsíce, čtvrtletí nebo roku.

Dále pod sloupcem „Skupina“ vyberte „Dodavatel“. Pak vyberte
„Kategorie produktu“, která je také umístěna v sloupci „Skupina“.

.. poznámka::
Výběry pod nadpisem „Skupina“ lze měnit v závislosti na potřebách uživatele.
individuální společnost. Například výběrem :guilabel:`Produkt` místo :guilabel:`Produkt
Kategorie „Výkonnost“, poskytuje podrobnější pohled na výkon konkrétních položek místo
celé kategorii.

Dále vyberte možnost pod nadpisem „Srovnání“, který se objeví. Tyto možnosti jsou
jsou k dispozici po výběru rozsahu dat pod sloupcem Filtry a liší se v závislosti na
Tento rozsah. „Předchozí období“ přidává srovnání předchozího období, například posledních
měsíci nebo čtvrtletí. Výchozím bodem je stejný měsíc nebo čtvrtletí předchozího roku.

.. poznámka::
Ve filtru můžete přidávat více časových filtrů najednou, ale k porovnání lze vybrat pouze jeden.
čas.

.. obrázek:: nákupní_náklady_výkazu/filtry-skupiny.png
:align:center
:alt: Rozbalovací nabídka filtrů, skupin a možností srovnání nákladů na pořízení
zpráva.

Filtr pro Q2, porovnání **Předchozí období** a seskupení podle **Dodavatele** a **Produktu**.
Byly vybrány kategorie**.

Přidat opatření
------------

Po výběru nastavení filtrů, skupinování a porovnání
klikněte na položku v rozbalovacím seznamu.

Výchozí nastavení zobrazuje následující měřítka: :guilabel:`Objednávky
:guilabel:`Celkem“, :guilabel:`Nezdaněné celkové“ a :guilabel:"Počet“. Klikněte na
nahoře vlevo pro otevření seznamu dostupných měřítek.

Klikněte na následující konkrétní opatření, abyste mohli přidat další sloupce pro výdaje spojené s nákupem.
reportáž:

- :guilabel:'Celkem' a :guilabel:'Bez daně celkem': mohou zahrnovat jeden nebo oba ukazatele.
zahrnuty do celkového rozboru výdajů.
- :guilabel:`Průměrná cena“: zahrnuta do hodnocení efektivity nákladů.
- :guilabel:'Dny k potvrzení' a :guilabel:'Dny k přijetí': používané k posouzení výkonnosti dodavatelů.
- :guilabel:`Počet objednaných kusů“ a „Počet obdržených kusů“: slouží k pochopení efektivity objednávky.
- :guilabel:„Počet fakturovaných položek“ a :guilabel:„Počet položek, které ještě nebyly fakturovány“: slouží k sledování přesnosti objednávky.

..tip:
Pokud si přejete, můžete do zprávy přidat další kroky, které vám poskytnou další poznatky.
Příkladem mohou být například „Hmotnost včetně nákladu“ a „Objem“.
logistické a manažerské analýzy.

Po výběru všech potřebných opatření klikněte mimo rozbalovací nabídku.

... nákup/zobrazení výsledků:

Zobrazit výsledky
============

Po výběru všech filtrů a měření se zobrazí vybraný pohled.

.. obrázek: nákupní výdaje/výkaz za zprávu/vzorek pro každou zprávu.png
:align:center
:alt: Vzorový výkaz o nákladech na získání zakázky.

Klikněte na tlačítko „Vložit do tabulky“ a přidejte rozbalovací pohled do formátu editovatelné tabulky.
v aplikaci Dokumenty*.

.. důležité:
Volba „Vložit do tabulky“ je k dispozici pouze v případě, že se nacházíte ve formátu *Dokumenty Tabulka*.
modul je nainstalován.

.. poznámka::
Přepočet je také k dispozici v grafickém zobrazení. Klikněte na ikonu „fa-area-chart“ (graf
grafu). Klikněte na příslušný ikonu v horní části zprávy, abyste přepnuli do grafického pohledu.
přepnout na graf :icon:`fa-bar-chart` :guilabel:`(bar chart)` nebo :icon:`fa-line-chart` :guilabel:`(line
„graf“, nebo „:icon:“ fa-pie-chart “: guilabel: „(kruhová grafika)“.

.. viz též:
Chcete-li si tento výstup uložit jako oblíbený, podívejte se na :ref:`vyhledávání/oblíbené`.
