========================
Nejbližší odstranění umístění
========================

Pro strategii Nejbližší lokalita jsou produkty vybírány podle abecedního pořadí
název skladovacího místa.

Tímto způsobem chce společnost ušetřit svým zaměstnancům dlouhé cesty do vzdálenějších skladů.
polici, pokud je produkt k dispozici i v blízkém místě.

.. viz také:
:doc:`O odstraňovacích strategiích <../removal_strategies>`

… skladovací prostory, inventář/sklady/sekvence:

Chcete-li pochopit sekvenci umístění v nejbližším odstranění, zvažte následující příklad:

Příklad:
Produkt je uložen na těchto místech: „Police A/Paleta“, „Police A/Regál 1“ a „Police A/Regál 2“.
A/Skříňka 2“.

.. obrázek:: closest_location/locations.png
:srovnání: do středu
:alt:Zobrazit ukázku skutečného uskladnění v skladu.

Sublokalita „Paleta“ je v přízemí a zboží zde uložené je snáze dostupné.
v porovnání s tím, že je nutné použít vysokozdvižný vozík k dosažení skladových míst „Rack 1“ a „Rack 2“. Skladová místa byla
Strategicky pojmenované podle abecedy a snadnosti přístupu.

.. důležité::
Pro použití této strategie odstranění je nutné využít :guilabel:`Skladovací místa“ a :guilabel:`Dvoufázové trasy“.
Nastavení **musí být zapnuté** v:menu:„Skladová aplikace – Konfigurace – Nastavení“.

.. viz také:
:ref:`Nastavení strategie odstranění <inventory/warehouses_storage/removal-config>“

...Inventář, sklady, skladování, místo:

Názvy lokalit
==============

Pro konfiguraci názvů lokalit začněte tím, že se přesunete na:
Vyberte existující lokalitu nebo klikněte na „Nový“ a vytvořte novou.
Pak zadejte požadované jméno do pole „Název lokality“ (Guilabel).

Jakmile jsou názvy míst uvedeny v abecedním pořadí podle jejich blízkosti výstupu nebo
umístění balení, nastavte strategii odstranění na :ref:`rodičské umístění
<soupis/hierarchie umístění>.

Pro to v seznamu :guilabel:`Lokace` vyberte rodičovskou lokaci alfabeticky.
Uvedení skladových míst.

Tím se otevře formulář pro rodičovskou lokaci. V poli „Strategie odstranění“ vyberte
:guilabel:`Nejbližší místo“.

Příklad:
V skladu je nejblíže balicímu prostoru skladové místo „WH/Sklad/Regál 1“.
kde jsou baleny produkty vytažené z regálů pro odeslání. Nejoblíbenějším výrobkem je iPhone
„nabíječka“ je uložena ve třech lokalitách „WH/Sklad/Police 1“, „WH/Sklad/Police 2“ a
„WH/Sklad/Police 3“.

Pro použití nejbližšího umístění nastavte strategii odstranění na rodičovské umístění „WH/Sklad“.

Průběh práce
========

Abychom viděli, jak funguje strategie odstranění nejbližšího umístění, podívejme se na následující příklad s
oblíbený produkt „nabíječka iPhone“, který je uložen na „Položky skladu/Police 1“, „Položky skladu/Police 2“
a „WH/Sklad/Regál 3“.

Na každém místě je k dispozici patnáct, pět a třicet jednotek.

..tip:
Chcete-li zkontrolovat skladové zásoby na každém místě uložení produktu, přejděte do formuláře produktu a klikněte na
:guilabel:`Tlačítko On Hand“.

.... obrázek: nejbližší místo/zboží na skladě.png
:srovnání: do středu
:alt:Zobrazit skladové zásoby na všech pobočkách.

Vytvořte objednávku na dodání zboží (viz. :ref:`objednávka na dodání <sklad/dodání/jednostupňová>`) v počtu 18 kusů telefonu
Nabíječku lze objednat přes aplikaci „Prodej“ v sekci „Výběr menu“.

Po přidání produktů kliknutím na tlačítko „Potvrdit“ vytvoříte objednávku dodání, která rezervuje položky.
ukládané na nejbližším místě s použitím strategie odstraňování.

Pro více informací o tom, kde byly jednotky vybrány, zvolte :guilabel:`⦙≣ (seznam bodů)
ikona umístěná na pravé straně. Kliknutím se otevře okno „Přesun do skladu“
ukazuje, jak byly vybrané položky odstraněny podle strategie odstraňování.

V okně „Přesun otevřeného skladu“ se v poli „Odebrat z“ zobrazí
Na vyplnění požadavku jsou vybrány množství skladovaných v jednotlivých skladech.
Nejbližší položka „WH/Stock/Shelf 1“ je vybrána jako první. Zbývající tři jednotky jsou pak vybrány
z druhé nejbližší polohy „WH/Sklad/Police 2“.

.. obrázek: nejblíže/přesun-skladu-okno.png
:align:center
:alt:Zobrazit množství objednaných nabíječek pro iPhone.
