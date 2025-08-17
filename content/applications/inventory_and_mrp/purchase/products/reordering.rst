==========================
Nastavte pravidla pro přeskupování
==========================

U některých produktů je nutné zajistit, aby byl vždy k dispozici minimální počet.
v daném okamžiku. Udržování minimálního skladového stavu zajišťuje, že podniky mohou uspokojit poptávku zákazníků.
požadovat bez prodlení a udržet provoz v chodu. Pomáhá také tlumit dodavatelské
Poruchy řetězce a neočekávané nárůsty poptávky. Nespolehlivost může vzniknout kvůli nepřesné poptávce
předpovědi, zpoždění dodavatelského řetězce a špatné řízení skladu, které všechny mohou vést k
náklady na provoz a zbytečné zdroje.

Udržujte vysokou poptávku po produktech stále na skladě pomocí pravidel pro automatické nákupy, které spustí poptávkový formulář.
(požadavek na nabídku) každýkrát, když se předpokládané množství zásob dostane pod minimální hodnotu.
:abbr.: RFQs (požadavky na nabídku) vygenerované z pravidel pro opakování mají dodavatele, cenu
počet kusů potřebných pro další objednávku, což zrychluje a usnadňuje celý proces.

.. důležité:
Aplikace **Inventář** musí být nainstalována, aby se mohly používat pravidla pro přeskupování zásob, protože aplikace sleduje skladové zásoby.
množství.

Nastavte produkty pro opětovné objednání
=================================

Produkt musí být konfigurován určitým způsobem, než bude možné k němu přidat pravidlo pro opětovné objednávání.

Začíná se v záložce „Sklad“, „Výroba“
Klikněte na „Nákup“ nebo „Prodej“, přejděte do sekce „Produkty“.
Poté klikněte na „Vytvořit nový produkt“ nebo najděte produkt, který
je v databázi a klikněte na jeho produktovou podobu.

Dále na kartě produktu zaškrtněte políčko „Nákup“
pod políčkem s názvem produktu a pak pod záložkou „Obecné informace“.
Zadejte hodnotu „Produkt“ do pole „Typ produktu“. Nakonec zaškrtněte políčko s názvem
„Sledování zásob“, a vyberte možnost „Dokumentace“.
Vyberte možnost „Sledování produktu“ z nabídky.

.. obrázek: přehledně/produkt-pro-opakované-objednávky.png
:alt:Nastavte produkt pro opětovné objednání v Odoo.

Přidejte pravidlo pro přeskupení produktů
==================================

Po správném nastavení produktu lze k němu přidat pravidlo opakované objednávky klepnutím na tlačítko
viditelný tlačítko „Obnovit“ s ikonou „fa-refresh“ a štítkem „Pravidla pro přeskupení“ v horní části produktu.
formulář, pak klikněte na tlačítko „Vytvořit“ v panelu „Pravidla přesouvání“.

..tip:
Pokud tlačítko „Smart Button Reordering Rules“ s ikonou :icon:`fa-refresh` není vidět, klikněte
:guilabel:`Další“.

Jednou vytvořená pravidla pro přeskupení lze nakonfigurovat tak, aby automaticky generovala objednávky.
definují následující pole:

- :guilabel:`Lokalita“ určuje, kde by měly být uloženy objednané množství po přijetí.
obdržené a zanesené do zásob.
- :guilabel:`Minimální množství“ stanoví dolní hranici pro pravidlo znovuobjednání, zatímco „Maximum
„Množství“ nastavuje horní hranici. Pokud je skladová zásoba pod minimální množstvím, bude vytvořena nová
Poté je vytvořena objednávka na doplnění zásob do maximální množství.

...... příklad::
Pokud je nastaveno „Min Quantity“ na 5 a „Max Quantity“ na 25,
Pokud je skladová zásoba čtyři, vytvoří se objednávka na nákup 21 kusů produktu.

- :guilabel:`Množství více než jedna položka“ lze nakonfigurovat tak, aby se produkty objednávaly pouze ve skupinách
určité množství. V závislosti na zadaném počtu se tak může stát, že vznikne nákup
příkaz, který by umístil zůstatek na skladě nad hodnotu uvedenou v poli „Max
pole „Množství“.

...... příklad::
Pokud je nastavená hodnota :guilabel:`Max Quantity` na 100, ale :guilabel:`Multiple Quantity` je nastaveno na objednávku
výrobek v sériích po „200“, poté je vytvořen nákupní příkaz na 200 kusů tohoto výrobku.
produktu.

- :guilabel:`Jednotka` určuje jednotku měření, podle které se množství má uspořádat.
pokud se jedná o diskrétní produkty, měla by být tato hodnota nastavena na „jednotky“.
měření typu „Objem“ nebo „Hmotnost“ pro nekonečné produkty, jako je voda nebo cihly.

.. obrázek: přehazování/přesun-souboru-konfigurace-pravidla.png
:alt: Konfigurace pravidla přeskupování v Odoo.

.. viz též:
:doc:`../skladovani/dodavky/pravidla-pro-naskladneni/reordering-rules`

Zapněte ruční aktivaci pravidel pro přesunutí pomocí plánovače
=====================================================

Pravidla přeřazování jsou automaticky spouštěna plánovačem, který běží každý den v týdnu.
spustit ručně pravidla pro přeskupování položek, zapnout vývojářský mód a navigovat na:menuselection:Inventory app
-->Provoz --> Nákupní procesy: Spustit scheduler“. V okně potvrďte ruční akci
klikněte na tlačítko „Spustit plánovač“.

.. poznámka::
Manuální spouštění pravidel pro přeskupování také spustí jakékoliv další naplánované akce.

Spravovat pravidla pro přeskupování
=======================

Pro správu pravidel pro přeskupení produktů jednotlivě přejděte na stránku s formulářem daného produktu a vyberte
tlačítko „Přeskupit pravidla“ v horní části formuláře.

Pro správu všech pravidel pro přeobjednání produktů pro každý produkt přejděte na:
--> Dodávky“. Z této karty lze provádět běžné akce v Odoo, jako jsou
exportování dat nebo archivace pravidel, které již nejsou potřeba. Dále také :guilabel:`Filtry`.
:guilabel:„Skupina“ nebo „Zaškrtávací políčko“ v nabídce na formuláři jsou k dispozici pro vyhledání a/nebo uspořádání.
přepočítávání podle požadavku.
