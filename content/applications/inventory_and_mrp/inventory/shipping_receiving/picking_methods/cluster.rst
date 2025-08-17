===============
Skupinové sběrání
===============

... inventární/nezařazené/skupinové vybírání:

.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`
.. |SOS| nahradit za :: :abbr:`SOs (Prodejní objednávky)`

Metoda cluster picking je pokročilá metoda skládání, která kombinuje efektivitu metody :ref:`batch pickingu
„Skladování/Dodávky/Balení“ s tříděním během samotného sběru. Je nejvhodnější
pro sklady s vysokým objemem objednávek, kde je organizace a rychlost klíčové.

Oproti skládkovému sběru je třeba při skládkovém sběru provést další krok třídění po vyzvednutí.
do určených košů nebo nádob pro každou objednávku. To zamezuje
potřeba konzolidačních operací po sklizni, což z něj dělá ideální řešení pro provozy zaměřené na rychlost a přesnost.

Tento způsob skládání je zvláště účinný v prostředí, kde je nezbytné okamžitě uspořádat věci.
a objednávky obsahují směsici položek, které vyžadují přesné třídění během, nikoli po sklizení.
procesu.

Clusterové vybírání však má i své nevýhody. Například není možné vybrat si zboží na poslední chvíli.
prioritizované a optimalizované balíčky musí být ručně vytvořeny předem. V důsledku toho je vyzvedávání
Proces může vést k zácpám.

... inventář/nezařazené/skupinové vybírání/příklad:

Příklad:
   #. |SO| 1 volá po jednom jablku a pomeranči
   #. |SO| 2 volá po jednom jablku a banánu
   #. |SO| 3 volá po jednom jablku, pomeranči a banánu

Jablka jsou uložena na police A, pomeranče na police B a banány na police C.

K vybrání produktů pro tři objednávky najednou je v košíku naskládáno tři prázdné balíčky.

Pracovník začíná na police A a do každého balení vkládá jablka. Poté pracovník pokračuje k
Police B a umísťuje pomeranče do balení označených pro SO 1 a SO 3. Nakonec sběrač
Přitlačí kočárek k polici C, naloží do něj balení pro SO2 a SO3 s banánem každé.

S balenými balíčky pro všechny tři |SOS| si vozík sáhne k výstupnímu místu.
Kde jsou balíčky uzavřeny a připraveny k odeslání.

....... obrázek:: cluster/cluster-example.png
:alt:Zobrazit příklad plnění objednávek číslo 2 a 3 současně.

Konfigurace
=============

Chcete-li umožnit skládání do skupin, začněte tím, že se přesunete na: „Aplikace inventáře --> Konfigurace
--> Nastavení“. V sekci „Operace“ aktivujte položku „Balíčky“
Možností „Přenosy v dávkách, vlnách a skupinách“.

.. obrázek: cluster/configs.png
:alt:Aktivujte funkce „Balíčky“ a „Hromadné převody“ v nastavení.

Odoo používá metodu skládkového sběru k optimalizaci operace „vybrat“ (Pick), protože:
Možnosti „Lokalita“ a „Vícekrokové trasy“, které jsou pod nadpisem „Sklad“, musí být
Lze také zkontrolovat na této stránce nastavení.

„Uložiště“ umožňují skladování konkrétních produktů na určitých místech, ze kterých je lze vyzvednout.
Díky vícekrokovým trasám je možné provádět samotnou operace sběru.

Po dokončení klikněte na tlačítko „Uložit“.

.. obrázek: cluster/lokalita-trasy-check.png
:alt:Zapněte volbu *Skladové lokality* a *Multistopové trasy* v inventáři > Konfigurace > Nastavení.

..._Inventář/Miscellaneous/Vytvořit balíček:

Instalace balíčků
--------------

Pro konfiguraci skladových boxů používaných při procesu vyskladňování přejděte na
:menuvolba:„Seznam skladových zásob“ --> „Produkty“ --> „Balíčky“. Klikněte na tlačítko „Nový“ pro vytvoření
nový balíček.

Na novém balíčku je předvyplněna referenční hodnota balíčku.
Číslo „balení“ v systému. V poli „Datum balení“ je automaticky nastaveno datum vytvoření
forma.

Zadejte pole „Použití balíčku“ hodnotu „Využitelný box“.

.. viz také:
:doc:`Balíčky <../../product_management/configure/package>`

Příklad:
Balíček určený pro shlukovou manipulaci je pojmenován jako „CLUSTER-PACK-3“ pro snadnou identifikaci.
v tomto procesu jsou produkty baleny přímo do svých obalů určených k přepravě.
:guilabel:`Použití balíčku“ je nastaveno na „Využitelný box“.

.. obrázek:: cluster/cluster-package.png
:alt: Vytvořit nový balíček.

Vytvořit soubor sestav
====================

Pro vytvoření karty navigujte do aplikace Inventář a vyberte typ operace.
„Dodací příkaz“ nebo „Vyzvednout“ (podle toho, která operace je první v dodání
proud).

.. poznámka::
Příslušné balíčky mohou být vytvořeny pro odchozí zásilky ve třech krocích.

.. viz také:
   - :doc:`Dodání v jednom kroku <../denní operace/přijetí a dodání v jednom kroku>`
   - :doc:`Dodání ve dvou krocích <../denní operace/přijetí a dodání ve dvou krocích>`
   - :doc:`Dodání ve třech krocích <../denní operace/dodání ve třech krocích>`

Zaškrtněte políčko vedle příslušného výstupního operace a přidejte je do balíčku.
Po výběru požadovaných položek klikněte na tlačítko „Akce“ a vyberte
Možnost „Přidat do balíčku“ z rozevíracého seznamu, který vznikne po kliknutí na tlačítko „Vybrat“.

Příklad:
Pro vytvoření balíčku s více úlohami podle příkladu výše viz
<inventář/nezařazené/skupinové vybírání/příklad>, v skladu s dvoufázovým výdejem
následujících operací vyzvednutí:

   - „WH/PICK/00007“: spojené s číslem |SO| 88 pro jedno jablko a pomeranč.
   - „WH/PICK/00008“: spojené s číslem „SO“ 89 pro jeden jablko a banán.
   - „WH/PICK/00009“: spojené s „SO“ 90 pro jedno jablko, pomeranč a banán.

.. obrázek:: cluster/select-picks.png
:alt:Použijte tlačítko „Přidat do balíčku“, které je v seznamu tlačítek „Akce“.

Tím se otevře okno „Přidat do balíčku“, kde může zaměstnanec
Může být přiřazen odpovědný za vyskladnění.

Vyberte si z dvou možností v poli „Přidat do“ jednu z následujících možností: přidat do
přenos dat, nebo vytvořit: guilabel:" nový přenos dat".

Pak přidejte popis pro tuto sadu.

..tip:
V poli :guilabel:`Popis` lze přidat další informace, které pomohou pracovníkům
identifikovat zdroj balení, kde umístit balení, jaké obaly použít atd.

Pro vytvoření návrhu na výběr zboží k potvrzení později vyberte :guilabel:`Návrh`.
zaškrtávací políčko.

Proces ukončete kliknutím na tlačítko „Potvrdit“.

.. obrázek: cluster/add-to-batch-window.png
:alt:Zobrazte okno „Přidat do balíčku“ pro vytvoření přenosu balíčkem.

Procesní cykly
===============

Pro zpracování sériových čísel přejděte na: „Skladové aplikace - operace - převody sériových čísel“.
Klikněte na sérii, abyste ji vybrali.

V záložce „Podrobné operace“ jsou produkty, které mají být vybrány, seskupeny podle místa.

Nastavte značku „Zákaznický balíček“ na balík, který je určen pro konkrétní objednávku.

Příklad:
Procesujte balíček pro tři objednávky jablek, pomerančů a banánů:ref:`příklad
<Inventář/Miscellaneous/Skladování v regálech/Příklad> přiřadit každé skladování k jednomu balíčku.

V skladovém místě pro jablka „WH/Sklad/Police A“ přiřaďte všechna jablka ve třech sklizních.
do jednoho ze tří opakovaně použitelných balení „CLUSTER-PACK-1“, „CLUSTER-PACK-2“ nebo „CLUSTER-PACK-3“.

Zaznamenejte tento údaj v Odoo pomocí pole :guilabel:`Destination Package` ve formuláři :guilabel:`Detailed
Karta „Operace“.

.... obrázek:: cluster/cluster-batch-example.png
:alt: Příklad zpracování sklizně v inventáři.
