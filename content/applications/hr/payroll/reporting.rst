=========
Reportáž
=========

Součástí aplikace „Mzdy“ je sekce „Hlášení“, která nabízí širokou škálu různých reportů.
podle lokality.

Výchozími jsou zprávy *Zaměstnanecké výplatní listiny*, *Analýza vstupu do práce* a *Příloha k mzdovému výměru*.
v aplikaci *Mzdy*, a jsou k dispozici pro všechny společnosti bez ohledu na jejich umístění.

Pod třemi výchozími zprávami jsou všechny zprávy založené na lokalizaci, uspořádané podle země.
abecedním pořadí. Tyto zprávy obsahují všechny různé informace o nabízených výhodách a
lokální daňové zákony.

Pro zobrazení všech dostupných zpráv o databázi včetně těch specifických pro lokalizaci
Přejděte na: „Mzdy -> Zprávy“ k zobrazení dostupných zpráv v seznamu.
Najděte si konkrétní zprávu, na kterou chcete kliknout.

.. obrázek:reporting/reporty.png
:align:center
:alt: Zobrazení panelu s přehledem o zprávách, které ukazují další zprávy pro databáze v Belgii.

Pokud je uživateli nek dispozici zpráva, objeví se okno s chybovou hláškou „Nesprávná operace“.
s tím, že: guilabel:„Pro použití této funkce musíte být přihlášeni do společnosti v zemi“.
„(země)“ je konkrétní země, pro kterou je společnost nakonfigurována.

Výchozí zprávy
===============

Mzdy
-------

Klikněte na položku „Mzdy“ -> „Zprávy“ -> „Mzdy“. Zobrazí se pole „Mzdy“.
Analýza zprávy. Tato zpráva ukazuje všechny výplatní pásky vytvořené za posledních 365 dnů, protože
Výchozí filtr: ref: <payroll/filters>: „Poslední platba za posledních 365 dnů“.

.. obrázek: hlášení/mzdy.png
:align:center
:alt: Zpráva o přehledu mzdy za posledních 365 dní.

Výstup zprávy může obsahovat metriky pro různé parametry. Klikněte na pole „Metriky“
zobrazit seznam různých možností zobrazení metrik. Výchozí možnosti
zahrnuje:

- :guilabel:`#Pracovní smlouva“
- :guilabel:`Základní mzda“
- :guilabel:`Základní mzda za dovolenou“
- :guilabel:`Dny placeného volna“
- :guilabel:`Dny nečekané absenci“
- :guilabel:Dny neplaceného volna
- :guilabel:`Mzda hrubá“
- :guilabel:`Mzda“
- :guilabel:`Počet dní“
- :guilabel:`Počet hodin“
- :guilabel:`Dny práce“
- :guilabel:`Práce“
- :guilabel:`Počet“

:guilabel:`Mzda“ je výchozí metrika pro zprávu „Personal“.

.. obrázek:reporting/měření.png
:align:center
:alt:Různé možnosti zobrazení pro výkaz o mzdách.

Svislá osa
~~~~~~~~~~

Pohled řádkového grafu je výchozím pohledem pro zprávu o mzdách. Pokud chcete použít jiný pohled, klikněte
tlačítko „Line Chart“ (zastoupené ikonou „📈 (vývoj nahoru)“) v
položku nabídky, která změní pohled zpět na čárový graf.

Pro čárový graf jsou k dispozici několik možností, které lze aktivovat stisknutím příslušného tlačítka.
výběr a změna způsobu prezentace dat. Tyto ikony se objevují na konci grafu
možnosti. Mezi různé možnosti patří:

.. _mzdová/skládaná:

- :guilabel:`Stapled“: datum je prezentováno s každým metrikou ve vlastní řádce, „stapled“ na vrcholu
jiná. To pomáhá vizualizovat distribuci a rozptyl mezi různými kategoriemi.

.. _mzdy/součet:

- :guilabel:`Součet“: Data jsou zobrazena na jednotlivých řádcích s celkovým počtem.
částka vypočítaná kombinací všech řádků, což poskytuje celkový pohled na součet
data.

.._sestupně:

- :guilabel:`Sestupně“: Data jsou zobrazena s největšími hodnotami vlevo na grafu.
přibližně se snižující k nejmenším hodnotám na pravé straně osy x.
Tento uspořádání pomáhá zdůraznit trendy nebo výjimky na krajích.

... _platové tabulky:

- :guilabel:`Vzestupně“: Data jsou zobrazena s nejmenšími hodnotami v levém dolním rohu grafu.
vzestupně k největším hodnotám na pravé straně osy x.
použitelné pro zvýraznění pokrokového růstu nebo trendů.

.. poznámka::
Tyto možnosti lze kombinovat, aby vzniklo mnoho různých pohledů.

.. obrázek: reporting/line-chart.png
:align:center
:alt:Tlačítka menu s názvy grafů a dalších možností.

Sloupcový graf
~~~~~~~~~

Pro zobrazení dat v sloupcovém grafu klikněte na tlačítko „Sloupcový graf“ (zastupované symbolem
:guilabel:`📊 (graf v podobě barevného pruhu)` ikona v nabídce.

Klikněte na ikonu „Vícevrstvá <payroll/stacked>“ pro zobrazení grafu v vícevrstvém formátu (kde
V každé sloupci se vyskytuje více hodnot (viz např. grafy s kumulativními výplatami). Grafy s kumulativními výplatami jsou užitečné
pro vizualizaci postupu v čase nebo jiných kategorií.

Možnost zobrazení sloupců v :ref:`Sestupném pořadí <pracovní listy/sestupně> nebo :ref:`Vzestupném pořadí
Výsledky seřazené podle platů se objevují na konci možností.

.. obrázek::reporting/bar-chart.png
:align:center
:alt:Tlačítka menu s výsečovým grafem a ostatní možnosti tlačítek.

.. tip::
Kliknutím na možnost ji zapnete. Když chcete možnost vypnout, klikněte na ni znovu.
ikonka je světlejší s modrým obrysem. Když je neaktivní, je šedá bez obrysu.
zásadní otázky.

Kruhová graf
~~~~~~~~~

Pro zobrazení dat v grafu sloupcovém klikněte na tlačítko „Sloupcový graf“ (jehož symbol je
„Pie Chart“ (ikona „Kruhová grafika“) v nabídce.
pohled.

.. obrázek:reporting/pie-chart.png
:align:center
:alt:Tlačítka menu s výkresem grafu.

Pivotová tabulka
~~~~~~~~~~~

Pro zobrazení dat v tabulce sestav, klikněte na tlačítko „Sestava“ (jehož obrázek je
Ikona „Pivota“ (viz obrázek níže), která se nachází v pravém horním rohu nabídky.

Výchozí informace zahrnuje počet výplatních pásek (:guilabel:"Počet výplatních pásek"),
„Mzda čistá“, „Mzda hrubá“, počet „Dnů placené dovolené“
a počet dnů neplaceného volna. Informace jsou seřazeny podle oddělení.

Pro zobrazení dalších informací o zprávě klikněte na tlačítko „Měření“ a zobrazí se
položky nabídky. Pak klikněte na jakoukoli jinou metriku a zobrazte ji v tabulce převrácené.

.. obrázek:reporting/pivot.png
:align:center
:alt: Zobrazení tabulky s různými metrikami.

Pro seřazení položek podle konkrétní sloupce, například „Čistá mzda“, klikněte na název sloupce.
dvakrát. První kliknutí vybere sloupec a druhé řadí informace vzestupně
pořádku.

Pro export dat ve formátu XLSX klikněte na tlačítko „Stáhnout xlsx“, které je reprezentováno
:guilabel:`⬇️ (spodní šipka nad horizontální čárou)` ikona v pravém dolním rohu dostupných
ikonami. Informace se pak stáhne do tabulky.

.. obrázek::reporting/xlsx.png
:align:center
:alt:Možnosti nabídky s vyznačeným tlačítkem ke stažení.

Každý report lze vložit do tabulky kliknutím na tlačítko „Vložit do tabulky“.
tlačítko. V okně „Vyberte list s tabulkou pro vložení (druhu zprávy)“ se objeví
a ptát se, do které tabulky s informacemi je vložit. Vyberte existující tabulku nebo panel.
nebo vyberte nový:guilabel:`Prázdná tabulka“. Klikněte na tlačítko „Potvrdit“ pro přechod do
výpis v tabulkovém formátu s přidáným hlášením.

.. obrázek:reporting/excel.png
:align:center
:alt:Pohled na přenesená data do tabulky.

... _mzdový systém / úložiště dokumentů:

.. poznámka::
Pokud aplikace „Dokumenty“ není nainstalována, pak v nabídce „Vložit do tabulky“
přidá nově vytvořenou tabulku do aplikace Dashboards.

Pokud je aplikace **Dokumenty** nainstalovaná, tabulka má možnost uložit se
nebo aplikaci Dashboards nebo aplikaci Documents.

..._mzdy/filtry:

Filtry
=======

Na začátku každého hlášení jsou zobrazeny výchozí filtry uvnitř pole „Hledat…“.

Klikněte na ikonu „⬇️ (spodní šipka)“ v vyhledávacím poli, abyste zobrazili dostupné
:guilabel:`Filtry“. Filtry zobrazují informace, které odpovídají konkrétním filtrům.

.. příklad::
Zpráva „Analýza pracovních vstupů“ má dvě výchozí filtrační kritéria, „Současný měsíc: (Měsíc)
(Rok) filtru a filtru „Ověřený“.

.. obrázek:: reporting/custom-filter.png
:align:center
:alt:Filtry povoleny pro zprávu Analýza pracovních záznamů.

Výkazu mzdy je nastaven pouze jeden výchozí filtr, a to „Poslední platba za posledních 365 dní“.

Výkazu o připojených mzdách existuje pouze jeden výchozí filtr, a to „Datum ukončení platby:
(Rok).

Všechny zprávy mohou obsahovat vlastní filtry nebo skupinová data podle různých metrik (zaměstnanec,
oddělení, společnost atd.

Některé zprávy mají možnost porovnat současnou zprávu s předchozím obdobím nebo rokem (a
Možnost „Srovnání“ (viz obrázek výše).

Klikněte na parametr, abyste jej vybrali a aktivovali. Hned se vám zobrazí aktualizovaný
parametry.

Aktualizovaný výstup lze nastavit jako oblíbený výstup, což znamená, že parametry jsou uloženy pro rychlé
přístup v budoucnu. Chcete-li tak učinit, klikněte na tlačítko „Uložit aktuální vyhledávání“ pod
:guilabel:'Oblíbené' sekce, která je v rozbalovacím menu filtrů nad vyhledávací lištou.
Tím se zobrazí dvě možnosti a tlačítko „Uložit“.

Chcete-li nastavit aktuální zprávu jako výchozí konfiguraci při přístupu k zprávě, zaškrtněte políčko
vedle pole „Výchozí filtr“. Pokud má být aktuální zpráva dostupná všem v
databáze, zaškrtněte políčko vedle :guilabel:`Sdílet`.

Konečně klikněte na tlačítko „Uložit“, které uloží aktuálně konfigurovaný report. Poté se zobrazí
pod tlačítkem Favorites v rozbalovacím menu filtrů ve vyhledávací liště.
