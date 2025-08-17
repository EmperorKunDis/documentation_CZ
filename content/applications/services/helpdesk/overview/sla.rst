==============================
Dohody o úrovni služeb (SLA)
==============================

.. |SLA| nahrazuje: zkratka: SLA (Service Level Agreement)
.. |SLA| nahradit: zkratka: `SLA (Service Level Agreements)`

„Smlouva o úrovni služeb“ (SLA) definuje úroveň podpory, kterou může od služby očekávat zákazník.
Poskytovatelé. Smlouvy o úrovni služeb poskytují časovou osu, která ukazuje zákazníkům, kdy mohou očekávat výsledky, a také
podpora týmu na cílové rovince.

.. poznámka::
Výchozí nastavení zahrnuje funkci „Politika SLA“ pro nově vytvořené týmy Helpdesku.

Chcete-li vypnout funkci nebo upravit pracovní dobu, přejděte na:
Konfigurace --> Pomocné týmy“. Klikněte na tým, abyste otevřeli stránku konfigurace daného týmu.

Odtud se přesuňte do části „Výkon“. Chcete-li vypnout funkci |SLAs| pro
tým, zaškrtněte políčko „SLA zásady“.


:alt: Pohled na stránku týmu v HelpDesku, která se zaměřuje na nastavení SLA Policy.

Vytvořte novou politiku SLA
=======================

Pro vytvoření nové politiky přejděte na: „Helpdesk app --> Konfigurace --> SLA Politika“
Klikněte na položku „Nový“.

Alternativně přejděte na: „Aplikace pro podporu --> Konfigurace --> Týmy pro podporu“ a klikněte
v týmu. Pak klikněte na chytrou ikonu „SLA Policy“ v horní části nastavení týmu
stránku a klikněte na „Nový“.

Na prázdném formuláři politiky SLA zadejte název a popis pro novou
politiku a postupujte podle kroků níže.

Definujte kritéria pro politiku SLA
-------------------------------------

Sekce „Kritéria“ se používá k identifikaci, na které lístky se tato politika vztahuje.

Vyplňte následující pole pro nastavení kritérií výběru:

.. poznámka::
Pokud není uvedeno jinak, lze pro každé pole provést více výběrů.

- :guilabel:`Tým Helpdesku`: Pravidlo lze použít jen na jeden tým.
- :guilabel:`Priorita“: Prioritní úroveň pro tiket je určena výběrem jedné, dvou nebo
tři ikony „hvězda“ (viz. ikonka „fa-star-o“) reprezentující prioritní úroveň na
Kanbanová karta nebo přímo na lístku. SLA se vztahuje pouze po splnění prioritního stupně.
bylo aktualizováno na lístek tak, aby odpovídal kritériím SLA. Pokud v tomto poli není žádný výběr,
Tato politika se vztahuje pouze na lístky označené jako „Nízká priorita“, což znamená, že
:icon:`fa-hvězda-o` :guilabel:`(hvězda)` ikony.
- :guilabel:`Štítky“: Štítky slouží k označení tématu daného lístku. Můžete použít více štítků
do jednotného lístku.
- :guilabel:`Zákazníci“: V tomto poli lze vybrat jednotlivé kontakty nebo společnosti.
- :guilabel:`Služby“: Toto pole je k dispozici pouze v případě, že tým má aktivní aplikaci „Časová kniha“.
Tento postup umožňuje vázat lístek přímo na konkrétní položku objednávky, což je nutné.
Uvedené na lístku v poli „Položky objednávky“ ve sloupci „Zboží“.

Příklad:
Podpora musí řešit naléhavé problémy pro VIP zákazníky do jednoho pracovního dne.

Nový postup s názvem „8 hodin k uzavření“ je přiřazen týmu „Podpora VIP“. **Jedině**
se vztahuje na lístky s třemi ikonami „hvězda o“ :guilabel:`(star)`
to je stejné jako priorita „Důležité“.

Současně lze k jednomu problému přiřadit více lístků, takže se na ně vztahuje politika.
s tagy „Oprava“, „Servis“ nebo „Náhradní díly“.

.. obrázek: sla/sla-vytvorit-novy.png
:alt: Pohled na nový záznam politiky SLA s veškerými potřebnými informacemi vloženými.

Určete cíl pro politiku SLA
------------------------------------

*Zaměřená osoba* je stupeň, který musí být dosažen, a čas, který je na dosažení takového stupně přidělen.
splnit politiku SLA. Každý stupeň, který je přiřazen týmu, může být vybrán pro :guilabel:`Dosah
Stageovo pole.

Čas strávený v etapách vybraných ve sloupci „Vyloučení etap“ **není** započítán do
počítání lhůty SLA.

Příklad:
SLA s názvem „8 Hours to Close“ sleduje pracovní dobu před
když je vyřešen, má „Vyřešeno“ jako :guilabel:`Dosažený stupeň`. Současně
|SLA| s názvem „2 dny do startu“ sleduje pracovní čas před
Pracuje se na lístku a stav by měl být „Ve vývoji“.

Splňte termíny SLA
==================

Jakmile je zjištěno, že lístek splňuje kritéria SLA, nastaví se
Výpočetní. Termín vychází z data vytvoření jízdenky i cílové stanice.
pracovní doba.

.. poznámka::
Hodnota uvedená vedle pole „Práce“ v politice |SLA| se používá k
určit lhůtu. Výchozí hodnota je určena na základě nastavené hodnoty v poli :guilabel:`Společnost
V poli „Práce“ v aplikaci „Nastavení“ --> „Zaměstnanci“ --> „Organizace práce“.

Termín je pak přidán do lístku spolu s štítkem označujícím jméno SLA.
použít.

.. obrázek:: sla/sla-open-deadline.png
:alt:Výhled na formulář lístku, který upozorňuje na otevřené termíny v systému Odoo Helpdesk.

Když je splněna SLA politika, zelená se značka SLA a termín zmizí.
Z pohledu na lístek.

.. obrázek: sla/sla-deadline.png
:alt:Pohled na formulář vstupenky, který zdůrazňuje spokojenost s úrovní služeb ve verzi Odoo Helpdesk.

.. důležité:
Pokud je lístek splňuje více kritérií pro SLA, použije se ten nejdříve nastavený.
Vypsané termíny jsou zobrazeny na lístku. Po uplynutí této lhůty se zobrazí další termín.

Pokud uplyne lhůta SLA a jízdenka se nedostane do fáze :guilabel:`Reach Stage`, bude
tag se změní na červenou barvu. Po neúspěšném pokusu o SLA zůstane na lístku i po jeho vyřízení
přesunul se na krok :guilabel:`Reach Stage`.

.. obrázek: sla/sla-passing-failing.png
:alt:Pohled na formulář lístku s neúspěšným a úspěšným SLA v Odoo Helpdesku.

... helpdesk/analyzujte výkon SLA:

Analýza výkonnosti SLA
=======================

Zpráva „Analýza stavu SLA“ sleduje rychlost plnění smlouvy o úrovni služeb (SLA) a také
výkon jednotlivých členů týmu. Otevřete zprávu a odpovídající tabulku s přehledem
Přejít na: `Helpdesk app --> Reporting --> SLA Status Analysis`.

Pohled na střed
----------

Výchozí zobrazení reportu je ve formátu „Sloupcový“ (Pivot). V databázi jsou uloženy všechny |SLA| politiky
Tištěné jízdenky, které nebyly splněny politikou, jsou v procesu nebo byly splněny politikou, jsou uvedeny.
Výchozí nastavení je seskupení podle týmů a počtu lístků.

.. obrázek:: sla/sla-status-analysis.png
:alt: Zobrazení zprávy o analýze stavu SLA v Odoo Helpdesku.

Pohled na střed je agregací dat, která lze upravit přidáním měření a filtrů.

Pro změnu zobrazení nebo přidání dalších měření klikněte na tlačítko „Měření“.
zobrazí se rozbalovací nabídka s kritérii hlášení a vyberte si z dostupných možností.

Každý vybraný měřený údaj je označen ikonou „:fa-check:“
položky rozbalovací nabídky, aby bylo zřejmé, že měření je započítáno, a odpovídající nová sloupec se objeví.
do tabulky sestav, kde se zobrazí potřebné výpočty.

.. obrázek:: sla/sla-pivot-measures.png
:alt: Přehled dostupných opatření v zprávě o analýze stavu SLA.

K přidání skupiny do řádku nebo sloupce klikněte na ikonu :icon:`fa-plus-square` :guilabel:`(plus)` vedle
Vyberte politiku a poté jednu ze skupin. Chcete-li ji odebrat, klikněte na
:ikona: `fa-minus-square-o` ikona vedle názvu politiky.

.. obrázek:: sla/sla-pivot-groups.png
:alt: Zobrazení dostupných skupin podle možností v analýze stavu SLA.

Grafický pohled
----------

Přepněte se do grafického zobrazení kliknutím na ikonu :icon:`fa-area-chart` :guilabel:`(grafické zobrazení)“
nahoře na obrazovce. Chcete-li přepínat mezi různými grafy, vyberte ikonu *souvisejících dat* v horní části
v grafickém zobrazení.

.. záložky::

...... tabulka:: Graf

.. obrázek:: sla/sla-report-bar.png
:alt: Zobrazení hodnoty analýzy stavu SLA v grafické podobě.

Barový graf může pracovat s většími daty a porovnávat data mezi několika kategoriemi.

... tabulka:: Graf

.. obrázek:: sla/sla-report-line.png
:alt: Zobrazení zprávy o analýze stavu SLA v liniovém zobrazení.

Přímá čára může zobrazovat trendy nebo změny v čase.

....... tabulka:: Sloupcový graf

.. obrázek:: sla/sla-report-pie.png
:alt: Zobrazení analýzy stavu SLA v grafu sloupcovém.

Pie diagram porovnává data mezi malým počtem kategorií.

..tip:
Obě grafy, barový i čárový, lze zobrazit v režimu „skládané“ (stacked). To znamená, že se na nich
nebo více skupin dat na sebe navrch, namísto vedle sebe, což usnadňuje
porovnat data. Při zobrazení buďto sloupcového grafu nebo čárového grafu klikněte na ikonku :icon:`fa-database`.
:guilabel:`(skládaný)` ikonu pro zapnutí nebo vypnutí skládaného zobrazení.

.... obrázek:: sla/sla-report-stacked.png
:alt: Pohled na zprávu o analýze stavu SLA v podobě grafu sestupně.

Pohled na kohortu
-----------

Pohled na kohortu se používá ke sledování změn v datech v čase.
Ve zprávě „Analýza stavu SLA“ v kohortním pohledu klikněte na ikonu „oi-view-cohort“.
:guilabel:`(soubor lidí)` ikona vedle ostatních možností zobrazení.

.. obrázek:: sla/sla-report-cohort.png
:alt: Zobrazení výstupu analýzy stavu SLA ve skupinovém pohledu.

Výhled kohorty zkoumá životní cyklus dat v čase.

.. viz též:
   - :ref:`Přístupy k zobrazování <reporting/views>`
   - :doc:`Umožnit zákazníkům uzavřít své požadavky

