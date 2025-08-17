==========
Ceníky
==========

Pricelist je metoda dynamického cenotvorby, která aplikuje seznam cen (nebo pravidel pro stanovení ceny).
upravit prodejní ceny. Tato úprava se může vztahovat na konkrétního zákazníka, skupinu zákazníků, objednávku apod.
době, období apod., a je užitečná při vytváření cenových strategií a optimalizaci marží.

Modul prodeje v Odoo má užitečnou funkci ceníku, která lze přizpůsobit libovolným specifickým cenám.
strategie. Ceníky navrhují určitou cenu, ale vždy je možné ji na objednávce změnit.

Konfigurace
=============

Chcete-li zobrazit ceník v aplikaci Sales, nejprve přejděte na:
Konfigurace --> Nastavení“. V sekci „Ceník“ zaškrtněte políčko vedle
:guilabel:`Seznam cen“ a klikněte na :guilabel:`Uložit“.

.. obrázek: ceník/cena-sestava.png
:alt:Jak vypadá nastavení cenového seznamu v Odoo Sales.

Po aktivování a uložení funkce „Ceníky“ se na stránce „Nastavení“
opakování načítání stránky. Zde buď vyberte odkaz „Ceník“ (pod
(v sekci „Nastavení“ v části „Ceníky“), nebo přejděte na
:menu:Prodejní aplikace --> Produkty --> Ceníky.

Jedna z těchto možností otevře stránku „Ceníky“, na které lze vytvářet a upravovat ceníky.
a kdykoli změněna.

.. obrázek: ceny/18-cena-list-str.png
:alt:Jak vypadá stránka ceníků v Odoo Sales.

.. důležité:
Pokud není na prodejním dokladu konfigurovaná specifická cenová nabídka, použije se výchozí cenová nabídka.
se použije ceník.

.. poznámka::
Kolonka „Vybíratelné“ je pouze vhodná pro e-commerce Odoo. Tato možnost umožňuje
návštěvníci webu si mohou vybrat cenový list při nákupu na vašem e-shopu.

.. poznámka::
V Odoo 17 (a novějších verzích) není nutné zadávat cenovou nabídku v poli „Pricelist“.
pole na prodejním formuláři, aby jej potvrdil (tedy přeměnil na objednávku).

V sekci „Chat“ je možné přidávat poznámky a
komunikace na každé stránce ceníku.

Vytváření a úprava cenových nabídek
-------------------------------

Na stránce „Ceník“ buď vyberte cenový seznam k úpravě nebo klikněte na tlačítko „Nový“.
vytvořit novou ceníkovou nabídku, která odhaluje prázdný tvar ceníkové nabídky, který lze nakonfigurovat v počtu
různými způsoby.

.. obrázek: ceny/18-prodej-nový-ceník-formulář.png
:alt:Jak vypadá podrobný ceník v Odoo Sales.

Při vytváření nové cenové nabídky začněte přidáním názvu pro cenovou nabídku do pole na horní liště.
formulář. Poté vyberte, jakou měnou by se měla platba provádět.

Pokud pracujete v prostředí více společností, vyberte, pro kterou společnost se tato cenová nabídka má použít.
pole „Společnost“. Pokud je pole ponecháno prázdné, ceník se automaticky použije
všem společnostem v databázi.

Pokud pracujete v mezinárodní společnosti, vyberte země, pro které se tento ceník bude vztahovat.
sloupec „Země“.

.. prodej/produkty/cena:

Karta Ceny
---------------

V záložce „Pravidla cen“ se každá řádka vytvoří jako nový záznam, který bude implementovat individuální
cenu přiřadit k objednávce prodeje, kde je použitá ceníková položka. Chcete-li vytvořit novou pravidlo cen, klikněte na
„Přidat řádek“, která otevře nové okno s formulářem pro nastavení cenových pravidel.

Poté vyberte, zda chcete tento soubor pravidel použít pro produkt nebo kategorii.

Zde je několik možností konfigurace:

- Pokud je vybráno pole „Produkt“, použijte tento prvek k výběru jednoho
nebo více produktů, na které se bude tento ceník vztahovat.
- :guilabel:`Kategorie produktů“: Vyberte jednu nebo více kategorií produktů, na které se bude tato ceníková nabídka vztahovat.
- :guilabel:„Druh ceny“: Zvolte, zda se bude specializovaná cenotvorba
:guilabel:`Sleva“, „Formule“ nebo „Fixní cena“. Ceny se liší
je další konfigurace, která popisuje, jak aplikovat ceník.

  - :guilabel:`Sleva“: Zadejte procento, které chcete odečíst.
použít zápornou hodnotu v tomto poli.

...... důležité::
Pokud se na prodejní cenovou nabídku vztahuje ceník s tímto slevovým kódem, pak je zadána sleva
jako :guilabel:"Sleva", slevu uvidí zákazník.

... obrázek: ceny/ceník-prodejní-cena-pravidlo-slevy.png
:alt:Pravidlo cenové nabídky, které používá typ ceny Sleva k vytvoření slevy.

... obrázek: ceny/ceník-prodejní-cena-pravidlo-slevy-zákazník.png
:alt:Jak vypadá ceníková pravidla s použitím typu ceny Sleva na přehled pro zákazníka.

  - :guilabel:`Formule`: Vypočítat cenové pravidlo na základě následující konfigurace:

    - :guilabel:`Sleva“: Procentní sleva, která se má použít. Kladné i záporné hodnoty lze zadat.
zvýšit ceny.

...... důležité::
Pokud se na prodejní cenovou nabídku vztahuje ceník s tímto slevovým kódem, pak je zadána sleva
jako:guilabel:'Vzorec', slevu zákazníkovi neuvidí.

    - :guilabel:`Počítat na celé číslo“: Číselný údaj, který se má použít jako počáteční hodnota pro
slevu. Metoda zpracování se nastaví tak, aby cena byla násobkem hodnoty v tomto
pole.

.. poznámka::
Rozšíření se aplikuje po slevě a před příplatkem.

         - „Přirážka“: Pevná částka, která se přičte nebo odečte jednou „Sleva“.
a použito :guilabel:`Zobrazit jako`.
         - :guilabel:`Fixní cena“: Zadejte fixní cenu pro tento seznam cen. Když je aplikován, všechny produkty
Do cenových řádků v citacích se aktualizují na tuto cenu.

- :guilabel:`Min. množství“: Zadejte minimální počet vybraných produktů pro tento ceník
podat žádost.
- :validita_cena: Uveďte datum, od kterého a do kdy je tento ceník platný.
je aplikován na citace.

Příklad:
Vytvořit 100 % marže (nebo dvojnásobek ceny produktu) s minimální marží 5 $.
pole „Základní cena“ na pole „Prodejní cena“ a pole „Sleva“ na
"-100". Tento způsob je často vidět v obchodních situacích.

.... obrázek: ceny/vzorce-nákladů-a-marže-příklad.png
:alt:Jak v Odoo Sales zadat minimální marži ve výši 5 dolarů při stanovení ceny.

Příklad:
Pro aplikaci slevy ve výši 20 % a cen zaokrouhlených na 9,99 nastavte pole „Založeno na“ na
:guilabel:`Prodejní cena“, pole „Sleva“ na hodnotu 20, pole „Přirážka“ na hodnotu
na "-0,01" a pole „Metoda zpracování“ na „10“.

.. obrázek: ceník/slevová-formule-příklad.png
:alt:Příklad slevy o 20 % se zobrazenými cenami na 9,99 v Odoo Sales.

..tip:
Mít ceny, které končí na 9,99, nastavte metodu „Rounding“ na hodnotu 10.
:guilabel:`Příplatek“ na „-0,01“.

Karta Opakujících se cen
--------------------

Časová pravidla se používají zejména u předplatných produktů. Projděte si prosím Odoo
Pro více informací navštivte dokumentaci „Předplatné“ na adrese:

V záložce „Opakující se ceny“ jsou nastaveny cenové předpisy stejným způsobem jako v
kartě „Ceny“ s dalšími sloupci pro „Varianty produktů“.
:guilabel:`Opakující se plán“.

„Varianty produktů“ jsou konfigurovány pod produkty s jedním nebo více hodnotami, jako je
barva, velikost atd.). Jakmile je produkt vybrán pod záložkou „Produkty“, pokud
použitelné, vyberte požadované varianty produktů, které mají být zahrnuty do pravidla ceny.

Zvolte prázdné pole v sloupci „Opakovaný plán“ a zobrazí se vyskakovací nabídka.
předem stanovené periody opakování (např. „Měsíčně“, „Čtvrtletně“, „Týdně“ apod.)

.. obrázek: ceník/ceník-opakujících-cena.png
:alt:Opakující se cenová tabulka v konfiguračním formuláři ceníku.

Nové periodické intervaly lze vytvořit i z této sloupce. Pro nový interval je potřeba vyplnit jeho název
Vyberte možnost „Opakovaný plán“ a poté z rozevírací nabídky vyberte možnost „Vytvořit“.
Vytvořte časový úsek, který lze později upravit. Nebo vyberte možnost „Vytvořit a
edit...“Otevřít formulář „Vytvořit opakující se plán“. Z tohoto formuláře lze vytvořit
Interval opakování lze nastavit s konkrétními podrobnostmi:
a možností „Cenotvorba“. Po dokončení konfigurace klikněte na „Uložit a
Tlačítko „Zavřít“.

.. obrázek: ceny/doba-platnosti-popup.png
:align:center
:alt: Vlastní okno pro výběr časového období v Odoo Sales.

Nakonec přidejte požadovanou cenu pro tuto pravidlo opakujících se cen v poli :guilabel:`Recurring Price`.
sloupce.

.. viz též:
:doc:`/subscriptions`

Pravidla pronájmu
----------------

Ceny mohou být nastaveny pro pronájem produktů podle:
:guilabel:„Pravidla pronájmu“, používají stejnou metodiku jako „Pravidla cen“ a
:guilabel:`Opakující se ceny“ karty.

Chcete-li přidat pravidlo pronájmu, klikněte na tlačítko „Přidat řádek“ a vyberte požadovaný produkt v
Vyberte sloupec „Produkty“ a poté vyberte konkrétní variantu, pokud je třeba.

Poté vyberte dobu pronájmu (např. „Denně“, „Hodinově“ atd.) v poli „Časový úsek“.

Nakonec nastavte cenu pronájmu v příslušné sloupci podle pravidla pronájmu.

.. obrázek: ceník/prodejní-cena-půjčovna.png
:alt:Pronájem v konfiguračním formuláři cenovky.

E-commerce tab
-------------

Pod záložkou „E-commerce“ lze nastavit cenové pravidla pro produkty prodávané přes
:doc:`E-shop <../../../../websites/ecommerce/products>“.

Pro zobrazení ceníku vyberte cílovou webovou stránku v poli „Webová stránka“.

Pokud chcete, aby zákazník mohl vybrat tento ceník, aktivujte pole „Vybíratelný“.

Nakonec lze kódy na slevu a věrnost přidat do pole „E-commerce Promotional Code“
pole.

Zatrhněte políčko „Vybrané“ pro zobrazení ceníku jako volby pro zákazníky.
vybrat si při nákupu. Pokud je zaškrtávací políčko „Vybrané“ nezaškrtnuté, zákazníci nemohou
si vybrat tento ceník.

Poslední možností je přidání „Slevového kódu pro e-commerce“ pomocí klávesové zkratky :guilabel:`E-commerce Promotional Code`. Chcete-li kód přidat, zadejte
v požadovaném slevovém kódu, který při zadání v procesu objednávky aplikuje na
zákazníkovi, i když zákazník nespadá do předem stanovených kritérií.

Aplikace ceníku pro zákazníky
==============================

Základní ceník, který se vztahuje na všechny zákazníky, je „Veřejný ceník“ (:guilabel:`Public Pricelist`).
poskytuje příležitost aplikovat jiný ceník na zákazníka prostřednictvím kontaktního formuláře.

Pro to otevřete požadovaný kontaktní formulář buď kliknutím na „Prodej“
app --> Objednávky --> Zákazníci a vyberte si zákazníka z hlavního panelu „Zákazníci“.
nebo kliknutím na jméno zákazníka v objednávce prodeje.

.. obrázek: ceník/objednávka.png
:align:center
:alt: Vzorový formulář pro zákaznický záznam v Odoo Sales.

Na požadovaném kontaktním formuláři pod záložkou „Prodej a nákup“ v
:guilabel:„Prodej“ sekce, určete, jaká cenová nabídka by měla být aplikována na konkrétního zákazníka z
rozbalovací nabídka v poli „Ceník“.

.. obrázek: cenotvorba_zakaznik.png
:align:center
:alt: Cenový seznam v podrobnostech zákazníka v Odoo Sales.

.. poznámka::
Když je zákazník přidán do databáze, automaticky se na něj aplikuje výchozí ceník.
Není žádný způsob, jak mít prázdné pole cenového seznamu na kontaktním formuláři. I když je toto pole
Pokud je pole nevyplněné, v případě znovuotevření kontaktního formuláře se zobrazí výchozí cenový seznam.

Avšak když je tento kontakt přidán do nabídky a pole „Ceník“ se automaticky vyplní
(podle informací z jejich kontaktního formuláře) lze odstranit předem stanovenou cenu.
z políčka „Ceník“ a cenová nabídka ještě může být potvrzena a následně převedena
do prodejního příkazu.

Podmínky
----------

Na spodní části okna „Vytvořit pravidla pro cenové nabídky“ je položka „Podmínky“.
část.

Zde začněte výběrem jedné z možností v poli „Aplikovat na“:

- :guilabel:`Všechny produkty“: pokročilá pravidla cen se aplikují na všechny produkty.
- :guilabel:`Kategorie produktu“: pokročilá pravidla cen se budou vztahovat na konkrétní kategorii
produktů.
- :guilabel:`Produkt“: pokročilá pravidla cen se aplikují na konkrétní produkty.
- :guilabel:`Varianta produktu“: pokročilá pravidla cen se budou vztahovat na konkrétní produkty
variantu.

Pokud je vybrána některá z možností kromě „Všechny produkty“, bude vytvořen nový volba-specifický
Vyskytne se pole, ve kterém je specifický :guilabel:„Kategorie produktu“, „Produkt“ nebo
:guilabel:`Produktová varianta“ musí být vybrána.

Poté vyberte minimální množství, které se má aplikovat na pokročilý pravidlo cen v poli Min.
V poli Množství vyberte požadované množství. Nakonec zvolte rozsah dat pro ověření cenového předpisu v
:guilabel:`Platnost“ pole.

Jakmile jsou všechny konfigurace dokončeny, klikněte na tlačítko „Uložit a zavřít“ pro uložení pokročilých
pravidlo ceníku nebo klikněte na tlačítko „Uložit a vytvořit nový“ a okamžitě vytvořte další pokročilý ceník.
vytvořit novou podobu pravidel.

.. poznámka::
Pokud je pro konkrétní produkt nastavena cenová pravidla a pro kategorii produktu další, pak Odoo
Využívá pravidla produktu samotného.

.. viz též:
   - :doc:`/aplikace/prodej/prodej/produkty a ceny/ceny/měny`
   - :doc:`/aplikace/weby/e-commerce/produkty/cena_správa`
