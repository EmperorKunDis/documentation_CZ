=========
Reportáž
=========

Ve většině aplikací, které umožňují analýzu, najdete několik zpráv pod položkou „Zprávy“ v nabídce.
a vizualizovat data z vašich záznamů.

..._zprávy/názory:

Výběr pohledu
================

Podle zprávy může Odoo zobrazit data různými způsoby. Někdy je jedinečný pohled
Zcela přizpůsobená zprávě je k dispozici, zatímco pro některé jsou k dispozici různé pohledy.
dva obecné pohledy jsou určeny pro reportování: graf a svislá osa.

..._zprávy/výhledy/graf:

Grafický pohled
----------

Pomocí grafického zobrazení :ref:`dat <reporting/using-graph>` můžete vizualizovat svá data.
identifikovat vzorce a trendy. Výhled je často nalezen pod položkou „Zprávy“ v aplikacích
Můžete je však najít jinde. Klikněte na tlačítko „Zobrazení grafu“ umístěné v pravém horním rohu, abyste se dostali k
it.

.. obrázek:reporting/graf-tlačítko.png
:alt:Vybrat graf

.._reporting/views/pivot:

Pohled na střed
----------

Pomocí nástroje :ref:`pivotního pohledu <reporting/using-pivot>` lze agregovat vaše záznamy a zobrazit je
pro analýzu. Pohled je často nalezen pod nabídkou „Zprávy“ v aplikacích, ale může být
je k dispozici jinde. Klikněte na tlačítko „Pohled na přepočet“ umístěné v pravém horním rohu, abyste se do něj dostali.

.. obrázek:reporting/pivot-button.png
:alt:Výběr pohledu na sestavu

... _zprávy/volba opatření:

Volba opatření
=================

Po výběru pohledu byste měli zajistit, aby byly zobrazeny pouze relevantní záznamy: „filtrované“ pomocí vyhledávání.
Dalším krokem je výběr měřené veličiny. Výchozí měřená veličina je vždy vybrána. Pokud chcete
upravit ji, kliknout na „Měřítka“ a vybrat jedno nebo, pouze pro osy, více měřítek.

.. poznámka::
Když si vyberete měřítko, Odoo agreguje hodnoty zaznamenané v tomto poli pro filtrovaný
záznamy. Pouze pole s čísly (:ref:`integrováno <studio/fields/simple-fields-integer>`,
:ref:`desetinná <studio/poli/jednoduché-pole-desetinné>`, :ref:`peněžní
<studia/pole/jednoduché-pole-měna>“) lze měřit. Dále je k dispozici pole :guilabel:`Počet`,
Tato možnost se používá k celkovému počtu filtrovaných záznamů.

Po výběru toho, co chcete měřit, můžete definovat, jaká data by měla být :ref:`skupována
podle rozměru, který chcete analyzovat. Výchozí hodnotou je často
skupinované podle *Datum > Měsíc*, což se používá k analýze vývoje měření v průběhu měsíců.

.. tip::
Při filtrování jednoho časového období se zobrazí možnost porovnat ho s jiným.

.... obrázek::reporting/srovnani.png
:alt:Použití možnosti porovnání

.. příklad::

... záložky ::

.. tab:: Vybrané měřítka

Mezi dalšími opatřeními můžete přidat měřítko „Margin“ a „Count“.
do zprávy Analýza prodeje. Výchozí měřítko „Nezdaněná částka“ je
vybráno.

.. obrázek::reporting/measures.png
:alt:Vybrat různé měřítka na výstupu z Analýzy prodeje

.. tab:: Skupinové měření

Můžete seskupit měření podle:guilabel:`Kategorie produktu` na úrovni řádků v tabulce.
příklad předchozího reportu o prodejních analýzách.

.. obrázek::reporting/single-group.png
:alt:Přidání skupiny na zprávu Analýza prodeje

..._zprávy/použití pivotů:

Použitím zobrazení s kloubem
====================

Skupování dat je naprosto zásadní pro pohled na převrácení tabulky. Umožňuje vám procházet hlubšími vrstvami dat
poznatků. Použitím možnosti „Skupina“ můžete rychle přidat skupinu na úrovni
řádky, jak je vidět na příkladu výše, můžete také kliknout na tlačítko „plus“ (:guilabel:`➕`) vedle
:guilabel:Hlavička „Celkem“ na úrovni řádků i sloupců a poté vyberte jeden z
**přednastavené skupiny**. Chcete-li ji odebrat, klikněte na tlačítko mínusu (:guilabel:`➖`).

Jakmile přidáte skupinu, můžete přidat další na opačné ose nebo nově vytvořené.
podskupiny.

.. příklad::
Další možností je dále rozdělit ukazatele z předchozího příkladu analýzy prodeje.
:guilabel:`Prodejci“ na úrovni sloupců a podle „Datum objednávky > Měsíc“
skupina v kategorii „Vše / Prodávané / Kancelářský nábytek“.

.... obrázek::reporting/multiple-groups.png
:alt:Přidání více skupin na výstupní report Analýza prodeje

.. tip::
   - Přepněte řádky a sloupce mezi skupinami kliknutím na tlačítko „Otočit osy“ (:guilabel:„⇄“).
   - Klikněte na štítek měřítka, abyste seřadili hodnoty vzestupně (⏶) nebo sestupně (⏷).
   - Stáhněte si verzi sestavy v formátu .xlsx kliknutím na tlačítko ke stažení (:guilabel:⭳).

..._zpravodajství/využití grafů:

Použitím grafického zobrazení
====================

K dispozici jsou tři grafy: sloupcový, čárový a koláčový.

Používají se k zobrazení rozložení nebo srovnání několika kategorií.
Je zvláště užitečné, že dokáží pracovat s většími datovými sadami.

**Plošné grafy** jsou užitečné pro zobrazení sezónních časových řad a trendů v čase.

Diagramy slouží k zobrazení distribuce nebo porovnání malého počtu kategorií.
Když vytváří smysluplné celky.

.. záložky::

.. tabulka:: Graf

.. obrázek:: reporting/bar.png
:alt: Zobrazení zprávy o prodejních analýzách jako sloupcového grafu

.. tabulka:: Graf

.. obrázek: reporting/line.png
:alt: Zobrazení analýzy prodeje jako čárového grafu

... tabulka:: Sloupcový graf

.. obrázek::reporting/pie.png
:alt: Zobrazení zprávy o prodejní analýze jako grafu sloužícího k porovnání

.. tip::
Pro grafy sloupců a čar můžete použít možnost „stohování“, pokud máte alespoň dva
skupinami, které se pak objevují na sobě navrch místo vedle sebe.

... záložky ::

.. tabulka:: Seskupená sloupcová graf

.. obrázek:: reporting/stacked-bar.png
:alt:Příklad sloupcového grafu

... tab: Běžná sloupcová graf

.. obrázek::reporting/non-stacked-bar.png
:alt:Příklad nezaplňované sloupcové grafy

... tab:: Sloupcový graf

.. obrázek: stacked-line.png
:alt:Příklad sloupcového grafu

.. tab:: Obvyklá čára

.. obrázek::reporting/non-stacked-line.png
:alt: Příklad nezaplňované svislé osy

Pro grafy svislých čar lze použít možnost součtu hodnot, což je zejména užitečné.
aby ukázal změnu růstu v čase.

... záložky ::

.. tabulka:: Součet čárového grafu

.. obrázek:reporting/cumulative.png
:alt: Příklad kumulativní čárové graf

.. tab:: Obvyklá čára

.. obrázek::reporting/necumulativní.png
:alt: Příklad obyčejné čárové grafy
