================
Metriky kampaně
================

*Metriky kampaně* jsou podrobné statistiky a analýzy v rámci marketingové kampaně, měřící její
úspěšnost a efektivita. Zapojené marketingové aktivity zaplňují relevantní bloky aktivit
v reálném čase v podrobnostech kampaně.

Analýza aktivit
==================

V sekci „Průběh“ kampaně v podrobnostech kampaně aplikace Marketing Automation
kde se nacházejí jednotlivé kampaně, užitečné informace najdete na
individuální blok aktivit, jako je počet komunikací: guilabel:Sent, procento zpráv
a mnoho dalšího.

.. obrázek: pochopení_metrik/aktivita_analytika_blok_vzorek.png
:align:center
:alt: Blok činnosti v sekci workflow s užitečnými analytickými daty v Odoo.

Vlevo od aktivitního bloku je konfigurovaný časový spouštěč :doc:`<workflow_activities>`.
zobrazen jako doba (buď „hodiny“, „dny“, „týdny“ nebo
:guilabel:`Měsíce“) pokud odpovídá období po zahájení procesu.

.. poznámka::
Pokud je spouštěcí čas závislý na jiné aktivitě nebo akci, např. :guilabel:`Pošta:
Odpověděl“, apod. V případě potřeby je zobrazen čas spolu s nutným krokem pro danou aktivitu.
aktivován (např. „Odpověděl po dvou hodinách“).

.... obrázek: pochopení metrik/odpověď po čase aktivitního spouštěče.png
:synchronizace: střed
:alt:Zobrazení časového spouštěče v závislosti na jiné aktivitě v marketingové automatizaci Odoo.

V bloku aktivit je každému typu aktivity přiřazeno ikonka. Ikona „✉️ (poštovní schránka)“
Toto znamená, že je aktivita e-mailová. Tři malé, propojené ikony „⚙️“ (kolečko) znamenají, že
Aktivita je vnitřní akcí. A malý základní ikonka „📱“ znamená aktivitu
je SMS.

..tip:
Název aktivity je také zobrazen pod názvem aktivity v menším písmu.

Nad aktivitou je ikona aktivity a nad ní název aktivity.
vpravo od názvu aktivity jsou tlačítka „Upravit“ a „Smazat“.

Klikněte na tlačítko „Upravit“ a otevřete okno pro vyplnění „Otevřeno: Akce“ pro konkrétní
akce, kterou lze upravit. Klikněte na tlačítko „Smazat“ pro úplné odstranění
odstranit konkrétní činnost z procesu.

.. viz též:
:doc:`workflow_activities“

Karta aktivit
------------------

V každém bloku aktivit je výchozím nastavením otevřená záložka „Graf (ikona písmena G)“, která zobrazuje
související metriky jako jednoduchá čára grafu. Úspěšné metriky jsou zobrazeny v „zelené“ barvě a
metriky, které byly odmítnuty, jsou zobrazeny v červené barvě.

Numerické reprezentace obou aktivit „úspěšné“ a „odmítnuté“ jsou zobrazeny
Vpravo od grafu.

..tip:
Při přejetí kurzorem nad jakýmkoliv bodem grafu aktivit bloku se zobrazí poznámkový výpis rozložení.
dat pro konkrétní den.

.... obrázek:: porozumění_metrikám/rozložení_dat.png
:synchronizace: střed
:alt:Přechodem nad kterýmkoliv bodem v grafu se zobrazí poznámky k rozdělení dat v Odoo.

Pod grafem v aktivitním bloku pro typy aktivit E-mail nebo SMS je přístupná
Data zahrnují přehled o kampaních včetně: :guilabel:`Sent`
(číselný), „Kliknutí“ (procento), „Odpověděl“ (procento) a
:guilabel:`Odpověď“ (procento).

..tip:
Kliknutím na kteroukoli z těchto statistik v řádku pod grafem DETAILS se objeví
stránku, která obsahuje každý konkrétní záznam pro dané datové body.

Karta filtru aktivit
-------------------

Vedle záložky „Graf“ v bloku aktivit je možnost otevřít
:guilabel:`Filtr“ záložka (zastupovaná ikonou :guilabel:`filtru/síta`).

.. obrázek: pochopení_metrik/aktivita_filtr_karta.png
:align:center
:alt:Jak vypadá filtr kampaně v marketingové automatizaci Odoo.

Kliknutím na záložku filtrů v bloku aktivit se zobrazí konkrétní filtry.
také konkrétní kampaň a kolik záznamů v databázi odpovídá této specifické
kriteria.

..tip:
Kliknutím na odkaz „záznamy“ pod zobrazeným filtrem se objeví samostatné okno.
Okno obsahující seznam všech záznamů, které odpovídají konkrétnímu pravidlu kampaně.

Sledovač odkazů
============

Odoo sleduje všechny URL adresy používané v marketingových kampaních. Chcete-li přistupovat a analyzovat tyto URL adresy, přejděte na
Vyberte aplikaci „Marketingová automatizace“ -> „Reporting“ -> „Link Tracker“. To vám ukáže
Stránka „Statistiky odkazů“, kde lze analyzovat všechny kampaně související URL adresy.

.. obrázek: pochopení_metrik/kampaňový_odkazový_sledovač.png
:align:center
:alt:Jak vypadá filtr kampaně v marketingové automatizaci Odoo.

Výchozí pohled na stránce „Statistiky odkazů“ je graf v podobě svislé osy, ale
V horním levém rohu jsou různé možnosti zobrazení. Lze si vybrat, že chceme vidět
statistiky jako :guilabel:`Line Chart“ nebo :guilabel:"Pie Chart“.

Kromě toho je také možné zobrazit statistiky jako „Skládané“ a datum
Může být řazen vzestupně nebo sestupně.

Vpravo dole je možnost „Měření“. Když na ni kliknete,
Možnost zobrazení počtu kliknutí nebo celkového počtu je dostupná.
Vpravo od nabídky „Měření“ je možnost přidat jakýkoliv datový bod.
vložení do tabulky kliknutím na tlačítko „Vložit do tabulky“.

Dále v pravém horním rohu stránky „Statistiky odkazů“ je na konci
vyhledávací liště jsou k dispozici další možnosti zobrazení: výchozí „Graf“
výhled Pivot a výhled List.

Stopy
======

Odoo sleduje všechny aktivity, které jsou používány v každé marketingové kampani. Data týkající se těchto aktivit
Můžete se k nim dostat a je možné je analyzovat na stránce „Sledování“, kterou najdete po kliknutí na
:menuvolba:„Automatizace marketingu“ --> „Zprávy“ --> „Sledování“.

.. obrázek:: pochopení_metrik/stopy-stránka-marketingová automatizace.png
:align:center
:alt:Stránka sledování v aplikaci Odoo Marketing Automation.

Výchozí pohled na stránce „Sledujte“ je graf v podobě barevného pruhu, ale existuje
V horním levém rohu jsou k dispozici různé možnosti zobrazení. Lze si vybrat,
statistiky jako :guilabel:`Line Chart“ nebo :guilabel:"Pie Chart“.

Na vrcholu grafu je barevný klíč, který uživateli sděluje, které aktivity byly
„Pracuje“, „Načítá“ a „Odmítnuto“. Dále existují i obrysy
indikátor, který informuje uživatele o součtu určitých aktivit.

Kromě různých možností zobrazení v horním levém rohu stránky :guilabel:`Sledování stavu` je zde
Dále je možnost zobrazit statistiky jako „Skládané“ a také možnost vložit data do
Sestupně nebo vzestupně.

Vpravo dole je možnost „Měření“. Když na ni kliknete,
Možnost zobrazení „ID dokumentu“ nebo celkového počtu „Počet“ je k dispozici. A také
Vpravo od položky „Měření“ je možné přidat jakékoliv měřené hodnoty.
vložení do tabulky kliknutím na tlačítko „Vložit do tabulky“.

Dále v pravém horním rohu stránky „Statistiky odkazů“ je na konci
vyhledávací liště jsou k dispozici další možnosti zobrazení: výchozí „Graf“
výhled Pivot a výhled List.

Účastníci
============

Odoo sleduje všechny účastníky spojené s každou marketingovou kampaní. Data týkající se těchto
Účastníci mohou být zobrazeni a analyzováni na stránce Participants, která je dostupná
Přejděte na: „Automatizace marketingu aplikace -> Zprávy -> Účastníci“.

.. obrázek: pochopení_metrik/účastníci-stránka-marketingová automatizace.png
:align:center
:alt:Stránka účastníků v aplikaci pro automatizaci marketingu Odoo.

Výchozí pohled na stránce „Účastníci“ je v grafu „Koláč“, ale
V horním levém rohu jsou k dispozici různé možnosti zobrazení, například
statistiky jako :guilabel:`Line Chart“ nebo :guilabel:`Bar Chart“.

Na vrcholu grafu je klíč barev, který popisuje typy účastníků nalezených v
graf.

Vpravo dole je možnost „Měření“. Když na ni kliknete,
Možnost zobrazení „ID záznamu“ nebo celkového počtu „Počet“ je k dispozici. A také
vpravo od položky „Měření“ je možné přidat do projektu jakékoliv měření.
vložení do tabulky kliknutím na tlačítko „Vložit do tabulky“.

Dále v pravém horním rohu stránky „Statistiky odkazů“ je na konci
vyhledávací liště jsou k dispozici další možnosti zobrazení: výchozí „Graf“
výhled Pivot a výhled List.
