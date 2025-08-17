====================
Předplatitelské zprávy
====================

.. |MRR| nahradit: zkratka: MRR (měsíční opakující se příjem)
.. |ARR| nahradit za: :abbr:`ARR (Roční opakující příjem)`

Aplikace Odoo **Subscription** poskytuje sérii stránek pro zprávy, které pomohou společnostem analyzovat, jak
Předplatné se prodávají.

Na stránce s výstupem pro analýzu předplatitelů mohou uživatelé zobrazit konkrétní údaje týkající se opakujících se plateb.
předplatné, počet předplatných, předplatná v průběhu nebo pozastavená a další.

Stránka s výstupem „Analýza udržení“ poskytuje uspořádanou tabulku o účasti na předplatném.
procenta za jakýkoliv časový úsek.

Stránka s výkazem „*MRR Breakdown*“ jasně rozděluje metriky MRR a ARR pro předplatné.
různé grafy, seznamy a tabulky.

A stránka s výstupy analýzy MRR nabízí časově orientovanou sbírku analytických dat, která ukazují
Subscription MRR a ARR se mění v průběhu času.

Zprávy o stránce
=======================

Všechny stránky s předplatným jsou dostupné přes hlavní nabídku „Reporting“ v
aplikace **Předplatné**.

Následující části popisují prvky, které jsou na každé stránce zprávy.

Filtry a Skupiny
--------------------

Filtrační prvky se používají k omezení metrik na zobrazení konkrétních analýz, zatímco seskupení (pomocí
Možnost „Skupit podle“ (angl. Group by) se používá k seskupení dat z konkrétních částí do skupin pro
organizované analýzy.

Tato část se týká jak filtrů, tak skupin, protože kombinace obou dvou může být uložena v
Soubor „Oblíbené“.

Pro změnu výsledků zobrazovaných na jakékoliv stránce s reportem klikněte na ikonu
:guilabel:`(svislá šipka doleva)` ikona vedle vyhledávací lišty. Když na ni kliknete, objeví se vám
podrobná filtrování a skupinování.

Pokud si přejete, můžete filtr nebo skupinu (nebo kombinaci filtru a skupiny) uložit v
:guilabel:`Oblíbené“ části rozbalovací nabídky. Chcete-li tak učinit, klikněte na :icon:`fa-caret-down`.
Ikona vedle tlačítka „Uložit aktuální vyhledávání“, které se nachází pod
:guilabel:`Oblíbené“ sekci.

To odhaluje pole pro přiřazení titulku filtru „oblíbené“. Pod ním se nachází dvě další možnosti
Titulek pole: „Výchozí filtr“ a „Sdílené“.

Zatrhnutím políčka vedle :guilabel:`Výchozí filtr` se nově oblíbený filtr stane výchozím.
možnost pro tuto stránku s výsledky.

Zaškrtnutím políčka vedle :guilabel:`Shared` se nově oblíbený filtr stane dostupným ostatním uživatelům.
uživatelů v databázi.

.. poznámka::
Výchozí filtr a volba „Sdílený“ nejsou povinné.
*jedna* z těchto možností může být vybrána najednou.

Pro uložení filtru klikněte na tlačítko „Uložit“ v sekci „Oblíbené“ v rozbalovacím menu.
filtrovací menu.

Když na něj kliknete, zobrazí se pod sloupcem „Oblíbené“ v rozevíracím seznamu.
filtru, objeví se vedle filtru s oblíbenými položkami ikona „hvězda“
Do vyhledávacího pole.

Názory
-----

Na stránce „Analýza předplatného“, „Porovnání MRR“ a „Analýza MRR“.
V pravém horním rohu jsou tři možnosti zobrazení stránky.

.. poznámka::
Na stránce s výstupem analýzy zadržování není žádné jiné nastavení možné.

K dispozici je několik možností zobrazení, od leva doprava:

- :guilabel:`Graf“
- :guilabel:`Seznam“
- :guilabel:`Pivota“

.. obrázek:reporty/zákaznický účet - stránka s nastavením zobrazení.png
:align:center
:alt:Různé možnosti zobrazení na stránce Analýza předplatitelů.

Každý pohled má svou vlastní sérii souvisejících vizuálních možností pro daný pohled.

Grafický pohled
~~~~~~~~~~

S výběrem grafického zobrazení se mezi vyhledávacím polem a vizuálním zobrazením objeví následující možnosti
zobrazení dat. Tyto graf specifické možnosti jsou umístěny napravo od
tlačítka „Změřit“ a „Vložit do tabulky“.

.. obrázek:reporty/předplatné_specifické_možnosti.png
:align:center
:alt:Možnosti grafického zobrazení v aplikaci Odoo Subscriptions.

První tři možnosti zleva doprava představují různé grafové pohledy.
Možnosti představují různé způsoby, jak uspořádat a vizualizovat konkrétní datová související s grafem.

Specifické možnosti zobrazení grafu jsou následující:

- :icon:`fa-bar-chart` :guilabel:`Bar Chart“: zobrazuje data v grafu sloupcovém.
- :icon:`fa-line-chart` :guilabel:`Line Chart“: zobrazuje data v grafu svislé čáry.
- :icon:`fa-pie-chart` :guilabel:`Pie Chart“: zobrazuje data v grafu sestávajícím ze sektorů.

Každá možnost zobrazení grafu má vlastní sérii specifických vizuálních možností, které jsou reprezentovány
tlačítka, která se zobrazují vpravo od vybrané možnosti grafického pohledu.

Když je vybrána grafická vizualizace „Bar Chart“ (ikona „fa-bar-chart“), zobrazí se následující vizuální
je možné využít následujících možností:

- :icon:`fa-database` :guilabel:`Skládaný“: zobrazuje data v grafickém formátu „skládání“.
- :icon:`fa-sort-amount-desc` :guilabel:`Sestupně“: zobrazuje data v sestupném pořadí.
- :icon:`fa-sort-amount-asc` :guilabel:`Vzestupně“: zobrazuje data vzestupným pořadím.

Při výběru grafu „Vývojová křivka“ jsou následující vizuální možnosti dostupné:

- :icon:`fa-database` :guilabel:`Skládaný“: zobrazuje data v grafickém formátu „skládání“.
- :icon:`fa-signal` :guilabel:`Součet“ zobrazuje data v kumulativním, rostoucím formátu.
- :icon:`fa-sort-amount-desc` :guilabel:`Sestupně“: zobrazuje data v sestupném pořadí.
- :icon:`fa-sort-amount-asc` :guilabel:`Vzestupně“: zobrazuje data vzestupným pořadím.

Když je vybrána grafická zobrazení „Pie Chart“, nejsou k dispozici žádné další vizuální možnosti.

Zobrazení seznamu
~~~~~~~~~

Při zobrazení seznamu jsou vyhodnocovány metriky předplatného v jednoduchém seznamu.
Které lze plně přizpůsobit pomocí jakýchkoliv dostupných filtrů nebo skupin v rolovacím seznamu.
filtrovací nabídka (přístupná přes ikonu „fa-caret-down“ vlevo od
vyhledávací liště).

.. poznámka::
Vybraná zobrazení v podobě seznamu umožňují použití nabídky „Měřítka“ a „Vložit do“.
Tlačítko „Tabulka“ je nedostupné.

Pohled na střed
~~~~~~~~~~

Při zvoleném pohledu na otočný stůl jsou uvedeny metriky předplatného v tabulce dat, která lze
plně přizpůsobitelné.

Pohyblivá tabulka může být upravena pomocí možností dostupných v :guilabel:`Měřítkách
a nebo filtrační skupiny dostupné v rozbalovacím seznamu filtrů
(přístupný pomocí ikony „svislá šipka“ vedle vyhledávacího pole)
baru.

Tři možnosti specifické pro otočné body jsou k dispozici vpravo od tlačítka „Měření“.
nabídku a tlačítko „Vložit do tabulky“.

.. obrázek::reports/subscriptions-pivot-view-options.png
:align:center
:alt:Možnosti nastavení pohledu na předplatné v aplikaci Odoo Subscriptions.

Zleva doprava jsou tyto možnosti zobrazení pro konkrétní pohledy:

- :ikonka:fa-exchange: :guilabel:Otočit osy: Otočí osy x a y v tabulce s daty otočenými na půl.
- :icon:`fa-arrows` :guilabel:`Rozbalit vše“: všechny dostupné sloupce a řádky datových sad
stůl se plně rozloží.
- :icon:`fa-download` :guilabel:`Stáhnout .xlsx“: seznam datových sad je ke stažení ve formátu
:soubor:`.xlsx` soubor.

Opatření
--------

Stránky grafů a rozcestníků mají vlastní seznam měřítek, který je k dispozici pomocí tlačítka „Měření“
nabídku datových možností v horním levém rohu nad vizuálem.
zobrazení metrik.

.. obrázek:reporty/předplatné-opatření-kliknutím-na-tlačítko-sestupně.png
:align:center
:alt: Výchozí měřítko v nabídce rozbalovacího seznamu aplikace Odoo Subscriptions.

Když je kliknut na tlačítko „Měření“, zobrazí se sada měřitelných hodnot.
v rozbalovacím seznamu. Když je zvolena jedna ze volby v seznamu :guilabel:`Měření`,
menu se na stránce s reportem objeví vybrané metriky související s tímto konkrétním ukazatelem.

.. poznámka::
Více informací o různých opatřeních, která lze na každé stránce s hlášením použít, najdete v
k konkrétním stránkám s přehledem vydaných zpráv, které naleznete níže na této stránce.
tuto dokumentaci.

Vložení do tabulky
---------------------

Vedle rozbalovací nabídky „Měřítka“ je i „Vložit do tabulky“.
tlačítko.

Když je kliknutá, umožňuje přidat konfigurovaná data zobrazovaná na stránce s reporty
do nové nebo již existující tabulky nebo panelu se zobrazí okno s nabídkou.

.. obrázek:reports/subscriptions-analysis-spreadsheet-popup.png
:align:center
:alt:Pop-up okno tabulky na stránce Analýza předplatitelů.

Vyberte požadovanou možnost z tohoto okna a poté klikněte na tlačítko „Potvrdit“.

..._předplatné/zprávy/výkaznictví:

Stránky s výkazem
===============

V aplikaci Odoo **Předplatné** jsou k dispozici čtyři různé stránky pro sledování.

Pro přístup k různým zprávám týkajícím se předplatného, přejděte na
:menu „Předplatné“, a klikněte na položku „Zprávy“ v
hlavičku, která odhalí následující stránky s reportážemi:

- :guilabel:`Předplatné“
- :guilabel:`Udržení“
- :guilabel:`Zlomení MRR“
- :guilabel:`Časová osa MRR“

Kliknutím na kteroukoli z těchto možností se objeví samostatná stránka s plně přizpůsobitelným reportem zaměřeným na to
konkrétní aspekt předplatného.

Následující je stručný přehled těchto čtyř konkrétních stránek s hlášením.

Analýza předplatitelů
----------------------

Chcete-li zobrazit stránku s analýzou předplatného, přejděte na
:menu-vyber->„Aplikace pro předplatné“ --> „Zprávy“ --> „Předplatné“.

Výchozí volbou je v grafovém zobrazení možnost „Svislý sloupec“.
:guilabel:`Analýza předplatného“ stránka zpráv.

Vyhledávací lišta obsahuje také tyto filtry: :guilabel:`Ve vývoji nebo pozastaveno“.
:label_recurrentní:

.. obrázek:reporty/prihlasky-analyzace-stranky-default.png
:align:center
:alt: Výchozí pohled stránky Analýza předplatného v Odoo Subscriptions.

Když je na stránce „Analýza předplatitelů“ tlačítko „Měření“,
klikněte, zobrazí se vám jako rozbalovací nabídka s možnostmi souvisejícími s měřením.

.. obrázek: reports/subscriptions-analysis-measures.png
:align:center
:alt: Výběr možností v rozevíracím seznamu na stránce Analýza předplatitelů.

Metrické možnosti v nabídce „Měřítka“ na kartě
Stránka „Analýza předplatného“ obsahuje následující informace:

- :guilabel:`Měsíční opakující se platby“
- :guilabel:`Množství“
- :guilabel:`Opakující se příjem“
- :guilabel:`Celková daň“
- :guilabel:`Roky opakující se“
- :guilabel:`Počet“

.. poznámka::
Výchozí je měsíční opakování.

Když je kliknutá kterákoliv z dostupných měřítek, Odoo zobrazí vybraná data v reportu.
stránka pro další analýzu.

Analýza udržení
------------------

Chcete-li zobrazit stránku s výstupem analýzy udržení, přejděte na
:menu:„Aplikace pro předplatné --> Zprávy --> Udržení“.

Stránka s výstupem analýzy udržení se liší od ostatních stránek aplikace **Předplatné**.
stránky ohlášení, protože neposkytuje žádné další možnosti zobrazení dat.
je pouze v přizpůsobitelném grafu dat.

.. obrázek:reporty/zpracování-údajů-o-zákaznících-stránka-výchozí.png
:align:center
:alt: Výchozí pohled stránky s výsledky analýzy udržení v Odoo Subscriptions.

Když se na stránce „Analýza udržení“ zobrazí položka „Měření“,
klikněte na něj, otevře se vám řada možností souvisejících s měřením.

.. obrázek:reporty/zadržení-předplatitelů-analýza-opatření.png
:align:center
:alt: Rozbalovací nabídka měření na stránce Analýza udržení.

V nabídce „Měření“ v rozevíracím seznamu „Způsob měření“ na kartě „Uchovávání“
Analýza se zabývá následujícími stránkami:

- :label_guid:"Fakturační částka"
- :guilabel:`Poznámka“
- :guilabel:`Marže (%)“
- :guilabel:`Procento předplacených služeb“
- :guilabel:`Hmotnost balíku“
- :guilabel:`Nedoplatek“
- :guilabel:`Počet“

.. poznámka::
Výchozí je volba měření počtu kusů („Count“).

Vpravo od nabídky „Měření“ na stránce „Analýza zadržování“.
Je to další rozbalovací nabídka obsahující různé časové období. Výchozím je
:guilabel:`Měsíc“.

Když na něj kliknete, objeví se vám nabídka různých možností časových úseků.

.. obrázek: reports/subscriptions-retention-analysis-time-periods.png
:align:center
:alt: Rozbalovací nabídka časového období na stránce Analýza udržení.

Možnosti časového rozsahu jsou:

- :guilabel:`Den´
- :guilabel:`Týden“
- :guilabel:`Měsíc“
- :guilabel:`Rok“

Když je vybrána možnost z této nabídky, otevře se dialogové okno :guilabel:`Analýza datových souborů`.
Stránka s výsledky zobrazuje data pro vybrané měřítko a filtry v daném časovém období.

Vpravo od rozbalovací nabídky s časovým obdobím je tlačítko pro stažení, které umožňuje uživateli
stáhnout data zobrazená na stránce „Analýza retence“ ve formátu Excel.

Zpětný odběr
-------------

Pro přístup na stránku s výkazem „Výdaje za služby“ přejděte do části „Předplatné“.
app --> Hlášení --> Rozdělení MRR“.

Výchozí zobrazení dat na stránce s reportem „Porovnání MRR“ je grafické.
s volbou „Graf s osami“ a „Skládaný“.

Vyhledávací lišta také obsahuje výchozí filtr pro :guilabel:`Datum události: měsíc > Typ události`.

.. obrázek:reporty/předplatné-mrr-rozložení-výchozí.png
:align:center
:alt: Výchozí vzhled stránky s přehledem účtů za služby v Odoo Subscriptions.

Když se v nabídce „Měření“ na stránce „Základní rozložení MRR“ objeví
klikněte na něj, otevře se vám řada možností souvisejících s měřením.

.. obrázek:reporty/předplatné-mrr-rozložení-opatření.png
:align:center
:alt: Výchozí vzhled stránky s přehledem účtů za služby v Odoo Subscriptions.

Metrické možnosti v rozevíracím seznamu „Měření“ na kartě „MRR“
Stránky s přehledem nefunkčních vozidel jsou:

- :guilabel:`Aktivní předplatné změnilo“
- :guilabel:`Změna ARR“
- :guilabel:`Změna MRR“
- :guilabel:`Počet“

.. poznámka::
Výchozí je volba měření „MRR Change“.

..tip:
Pro změnu výchozího měřítka je třeba nejprve vybrat požadované měřítko z nabídky.
:guilabel:`Měření“ v rozevíracím seznamu. Pak klikněte na ikonku „fa-caret-down“ :guilabel:
přepínačem v hledání, který otevře megamenu filtrů a skupin.

V sloupci „Oblíbené“ klikněte na ikonu „svislá čára dolů“ (svislou čárou dolů).
ikonu vedle :guilabel:`Uložit aktuální vyhledávání“ pro zobrazení pole, kde se může vložit název.
spolu s dvěma zaškrtávacími políčky: „Výchozí filtr“ a „Sdílené“.

Zatrhněte políčko u možnosti „Výchozí filtr“ a klikněte na tlačítko „Uložit“.

Nově zvolená měřítka je nyní výchozím nastavením, které se objevuje při otevření této stránky.
Je přístupná.

Analýza MRR
------------

Pro přístup k stránce s analýzou MRR přejděte na „Předplatná“.
app --> Hlášení --> Časová osa MRR“.

Výchozí zobrazení dat na stránce s výsledky analýzy MRR je v grafickém zobrazení.
volba „Svislá osa“, „Vrstvená“ a „Kumulativní“.
vybrané.

Vyhledávací liště také obsahuje výchozí filtr pro :guilabel:`Datum události: Měsíc`.

.. obrázek:reporty/předplatné-mrr-analýza-výchozí.png
:align:center
:alt:Výchozí vzhled stránky s výsledky analýzy MRR v Odoo Subscription.

Když se na stránce „Analýza MRR“ v poli „Měření“ objeví
klikněte na něj, otevře se vám řada možností souvisejících s měřením.

.. obrázek: zprávy/předplatné-MRR-analýza-opatření.png
:align:center
:alt:Výchozí vzhled stránky s výsledky analýzy MRR v Odoo Subscription.

Metrické možnosti v rozevíracím seznamu „Měření“ na kartě „MRR“
Analýza se zabývá následujícími stránkami:

- :guilabel:`Aktivní předplatné změnilo“
- :guilabel:`Změna ARR“
- :guilabel:`Změna MRR“
- :guilabel:`Počet“

.. poznámka::
Výchozí je volba měření „MRR Change“.

.. viz též:
   - :doc:`../předplatné`
