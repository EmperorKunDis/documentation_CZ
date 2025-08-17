=======
Rozpočty
=======

:ref:`Analytické rozpočty <účetnictví/rozpočty/analytické rozpočty>` sledují konkrétní aktivity a projekty.
pomocí analytických účtů, které pomáhají firmám učinit informované rozhodnutí o konkrétních odděleních.
projekty nebo jiné skupiny transakcí. Na rozdíl od nich:ref:`rozpočet
<účetnictví/rozpočty/finance> jsou spojeny s účetními knihami, které se objevují na zisku
a ztrátu a soustředí se na celkovou ekonomickou pozici společnosti.

..účetnictví/rozpočty/analytické rozpočty:

Analytické rozpočty
================

Analytické rozpočty umožňují přidělovat a sledovat příjmy a výdaje podrobněji, rozdělením
náklady a příjmy konkrétních projektů, oddělení nebo skupin transakcí. Analytické rozpočty
je možné aplikovat na různé oddělení nebo projekty, aby se zjistila rentabilita a výkon.
Analytické rozpočty spravuje pomocí :doc:`analytického účetnictví <analytic_accounting>“.

Pro aktivování možnosti vytváření analytických rozpočtů přejděte na:
Konfigurace --> Nastavení“ a zapněte „Budget Management“ v části „Analytika“.
§

.. důležité::
Odoo strukturuje rozpočty pomocí :ref:`plánů <účetnictví/analytické účetnictví/analytické plány>`.
:ref:`účty <účetnictví/analytické účetnictví/analytické účty>“, které musí být nakonfigurovány
*před* vytvořením rozpočtu.

...účetnictví/rozpočty/analytické rozpočtové sady:

Vytvořte rozpočet na analýzu
----------------------

Pro vytvoření nového rozpočtu přejděte na: „Účetnictví - Účetnictví - Analytické rozpočty“.
Klikněte na tlačítko „Nový“. Ujistěte se, že jsou v následujících polích správně vyplněny tyto informace:
Jméno, období a typ rozpočtu.

Klikněte na „Přidat řádek“ v záložce „Řádky rozpočtu“ a strukturovat rozpočet pomocí
:ref:`analytické plány <účetnictví/analytická účetní závěrka/analytické plány>` a :ref:`účty
Analytické účty, které byly vytvořeny dříve.
Plány odpovídají názvům sloupců; vyberte
:ref:`analytické účty <účetnictví/analytická_účetnictví/analytické_účty>“ k definování rozpočtu
a nastavte částky pro každou v poli „Předpokládané“. Jakmile jsou všechny předpokládané výdaje
usadit, kliknout: guilabel:"Otevřít". Pokud je třeba provést změny po otevření rozpočtu
V poli „Otevřeno“ jsou dvě možnosti:

- :reset_to_draft:Přepsat data a znovu otevřít rozpočet.
- :guilabel:`Změnit rozpočet“: Vytvoří se nový rozpočet. Jakmile je „otevřen“, můžete provést :guilabel:`Rev
Reference je přidána k položce „Název rozpočtu“ a původní rozpočet je
:guilabel:`Změněno“.

...účetnictví/rozpočty/kontrola rozpočtu:

Zkontrolujte rozpočet na analýzu
------------------------

Jakmile je rozpočet otevřený, jsou k dispozici další dvě sloupce:
:guilabel:'Dosáhlo'. Částky v těchto sloupcích se počítají automaticky na základě související
:ref:`Analytická distribuce účtu <účetnictví/analytické účetnictví/analytická distribuce účtu>
položek. Když se jedná o analytickou distribuci, pak je tento účet veden podle :ref:`analytické distribuce <účetnictví/analytická-distribuce>`.
pokud dojde k aktualizaci položky v rozpočtu během období rozpočtu, pak se změní sloupce rozpočtu pro
Vybrané účty jsou automaticky aktualizovány. Výše dosaženého cíle je zobrazena v :guilabel:`Dosaženo`.
odráží aktuální výsledek podle položek potvrzených účetních záznamů pro spojené
:ref:`analytický účet <účtování/analytické_účty/>“. Na rozdíl od
:guilabel:`Přislíbená“ částka zobrazuje celkovou hodnotu „Dosažené“ částky včetně jakýchkoliv
potvrzené objednávky, které ještě nebyly fakturovány.

.. poznámka::
   - Pokud je v požadavku na nabídku nebo objednávce uvedena analytická distribuce,

pro další informace.
   - Pro „Otevřené rozpočty“ je-li vytvořena poptávka nebo objednávka pomocí
přidružené analytické distribuci a přesahuje alokovanou částku, pak odpovídající
položka objednávky je zvýrazněna červeně.

Pro zobrazení teoretické částky nebo procenta použijte ikonu „Nastavení“.
ikona „Nastavení“ v hlavičce „Rozpočtové řádky“.
:guilabel:„Teoretická“ částka představuje množství peněz, které by teoreticky mohlo být
byli nebo měly být přijaty v souladu s aktuálním datem ve vztahu k datům začátku a ukončení. Klikněte
:guilabel:`Podrobnosti“ otevřít filtrovaný pohled na „Zprávu o rozpočtu“.
související s konkrétní položkou rozpočtu.

.. obrázek: rozpočet/rozpočet.png
:alt: otevřený rozpočet s částkami závaznými, dosaženými a teoretickými

.. poznámka::
Vymazání rozpočtu je povoleno pouze v etapách „Návrh“ a „Zrušený“.

Pro zobrazení rozpočtových položek jednoho nebo více rozpočtů přímo v seznamu „Rozpočty“
Vyberte rozpočet (rozpočty) a klikněte na položku „Rozpočtové řádky“.

...účetnictví/rozpočty/generovat rozpočtový analytický výkaz

Vytvářet periodické rozpočty
-------------------------

Vytvořit periodické rozpočty (měsíční, čtvrtletní a roční) pro vybrané :guilabel:`Analytic
Plány, klikněte na Generovat. Nový rozpočet je vytvořen pro každé období mezi
datum zahájení a ukončení:

- Pokud je vybrán pouze jeden analytický plán, každý rozpočet obsahuje řádek pro každou položku v tomto
analytický plán.
- Pokud je vybráno více analytických plánů, každý rozpočet obsahuje řádek pro každou položku/analytiku.
kombinace plánů.

Pro vytvoření periodického rozpočtu postupujte takto:

#V seznamu „Rozpočty“ klikněte na „Vytvořit“.
#V okně „Vytvořit rozpočet“ nastavte datum a vyberte období.
„Analytické plány“.

.. obrázek: budget/generate-budgets.png
:alt: všechny možnosti pro generování periodických rozpočtů

#Klikněte na tlačítko „Rozdělit“ a vytvořte periodické rozpočty.
#Klikněte na „Náklady“ v horním levém rohu, abyste se dostali zpět do pohledu „Náklady“.
#Každý z nich klikněte na různé periodické rozpočty s stavem „Návrh“
jim a nastavit částky v sloupci „Předpokládané“ pro každý analytický účet, který je s nimi spojen.
zvolené analytické plány.
#Klikněte na položku „Otevřít“ pro každý periodický rozpočet.

...účetnictví/rozpočty/analytické rozpočtové reporty:

Reportáž
---------

Pro provedení různých reportovacích akcí přejděte na: „Účetnictví --> Reporting -->
Zpráva o rozpočtu“, pak:

- Sledovat, analyzovat a porovnávat rozpočtová data.
- Filtrujte a skupujte data pomocí ikony „Plus“ („Plusová čtvercová“) nebo
:icon:`fa-minus-square` :guilabel:`(minus-square)`
- Pokud chcete zjistit více informací o skutečných částkách a transakcích, přejděte dolů do samotného hlášení.
- Exportujte data pro další analýzu nebo potřeby reportingu.

...účetnictví/rozpočty/finance:

Finanční rozpočty
=================

Finanční rozpočty jsou strukturovány kolem konkrétních účtů příjmů a výdajů a transakcí.
účetní a daňové účely.

.. poznámka::
Finanční rozpočty jsou k dispozici na stránce :ref:`Výsledovka.
<účetnictví/zpráva/výsledovka>

...účetnictví/rozpočty/finanční rozpočet:

Určete finanční rozpočet
----------------------

Chcete-li vytvořit nový finanční rozpočet, postupujte takto:

#Přejděte na: „Účetnictví“ -> „Zprávy“ -> „Výsledovka“.
:ref:`Zisk a ztráta <účetnictví/zprávy/zisk-a-ztráta>“.
#Klikněte na tlačítko „kalendář“ (zobrazí se ikona „fa-calendar“) pro použití kalendáře a zvolte datum.
období.
#Klikněte na tlačítko „Ikona:fa-bar-chart, Guilabel:Budget“ a pojmenujte rozpočet. Vytvoří se nová sloupec
budou vedle sloupce :guilabel:`Zůstatek“ zobrazeny s názvem rozpočtu.
#Přidělte částky každému účtu, který vyžaduje analýzu.
#. Nová sloupec „Budget“ se objeví vpravo od nového rozpočtu a bude ukazovat
aktuální stav.

Tyto kroky lze použít pro porovnání různých finančních rozpočtů.

.. poznámka::
Datumový výběr umožňuje rozdělení období a přechod mezi jednotlivými obdobími automaticky.
aktualizací částek v souladu s tímto.
