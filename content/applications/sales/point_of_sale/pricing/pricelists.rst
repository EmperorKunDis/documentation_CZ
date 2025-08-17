==========
Ceníky
==========

Ceníky umožňují automaticky upravovat ceny produktů podle různých kritérií.
Příkladem je možnost nastavit ceny pro konkrétní obchody, vytvářet dočasné slevové období nebo odměňovat určité zákazníky.
zákazníky nebo nabídnout slevy při objednání stanoveného množství.

... cenové nabídky / konfigurace:

Konfigurace
=============

Přejděte na obecné nastavení aplikace POS a zkontrolujte
V sekci „Ceníky“ je zapnuto „Průhledné cenové nabídky“.

:ref:`Mnoho cen za produkt <pricelists/simple>` je výchozím nastavením pro pricelist.
jednoduché pevné ceny za produkt. Vyberte:ref:`Pokročilá pravidla pro cenu (slevy, vzorce)
<ceník/pokročilé> a aplikovat pravidla cen na více produktů najednou a vypočítat ceny.
dynamicky pomocí procentních slev nebo složitějších vzorců navíc k stanoveným cenám.

.. obrázek: ceniky/nastaveni.png
:alt:Povolení cenových nabídek v obecných nastaveních P0S

.. poznámka::
Vybraný typ ceníku se vztahuje na celou databázi, včetně :doc:`Prodeje.
<../../prodej/produkty-a-ceny/cena/ceniky>` a :ref:`e-commerce <ecommerce/ceniky>
aplikace.

.. _ceníky/vytvořit:

Vytvořte ceníky
-----------------

Přejděte do sekce „Prodejní místo“ -> „Produkty“ -> „Ceníky“ a klikněte na „Nový“.
Vyberte existující ceník. Nastavení ceníku se liší podle vybraného ceníku.
volba „<ceník/konfigurace>“.

.. _ceníky/jednoduché:

Několik cen za produkt
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Když jsou ceníky nakonfigurovány tak, aby využívaly možnost „Nastavení více cen za produkt“, je
je možné používat více pevných cen pro různé produkty nebo jejich varianty podle
povinná, s jedním nebo více podmínek. Přidat novou cenovou pravidlo do ceníku:

#Klikněte na tlačítko „Přidat řádek“ a vyberte produkt a jeho variantu, pokud je potřeba.
#Přidejte podmínku (podmínky):

   - počet produktů, který lze dosáhnout pomocí sloupce Min. Quantity.
   - určité období, během kterého se používá cenový seznam s pomocí pole Start Date.
a sloupce s názvem „Datum ukončení“ a „Konec“.

#Přidejte :guilabel:`Cena`, která se má použít, když jsou splněny podmínky (pokud nějaké existují).

.. obrázek: ceniky/cena-podle-mnozstvi.png
:alt: Formát nastavení více cen

.. _ceníky/pokročilé:

Pokročilé pravidla cen
~~~~~~~~~~~~~~~~~~~~

Při konfiguraci ceníku na použití pokročilých pravidel ocenění („slevy, formule“)
můžete používat procentuální slevy a marže a vzorečky navíc k pevným
ceny. Chcete-li přidat novou cenovou pravidlo do ceníku, klikněte na tlačítko „Přidat řádek“. V okně se zobrazí:

#Vyberte metodu pro výpočet:

   - „Fixní cena“ pro nastavení nové fixní ceny (podobně jako „Několik cen“).
(za každý produkt).
   - :guilabel:"Sleva" pro výpočet procentní slevy (např. "10,00 %") nebo přirážky (např.
     `-10.00` %).
   - :guilabel:`Vzorec“ k výpočtu ceny podle vzorce. Je nutné definovat, co
výpočet je založený na (:guilabel:`Prodejní ceně“, „Nákladech“ nebo „Jiném“)
Ceník. Poté můžete:

     - Použijte procento nebo přirážku.
     - Přidejte příplatek („například 5,00 $“) nebo odečtěte pevnou částku („například -5,00 $“).
     - Definujte metodu zpracování cen podle pokynů v dokumentu „Metoda zpracování cen <cash_rounding>“
:guilabel:`Sleva“ musí být násobkem hodnoty, kterou uživatel zadá. „Přirážka“ se aplikuje
později.

...... příklad::
Pro konečnou cenu, která končí na „.99“, nastavte metodu zaokrouhlování na „1.00“.
přidat příplatek „Extra Fee“ na -0,01.

     - Uveďte minimální zisk (např. 20,00 USD) a maximální zisk (např. 50,00 USD).
:guilabel:`Okraje“ pro výpočty založené na :guilabel:`Nákladech“.

#Vyberte, na které produkty se má pravidlo cen aplikovat:

   - :guilabel:`Všechny produkty“
   - :guilabel:`Produktová kategorie“
   - :guilabel:`Produkt“
   - :guilabel:`Produktová varianta“

#Přidejte podmínky, například konkrétní množství, které je třeba dosáhnout pro změnu ceny pomocí
:guilabel:`Minimální množství“ nebo konkrétní období, v němž by měla být cenová nabídka
aplikován pomocí pole validity.

.. obrázek: ceniky/cena-pravidla.png
:alt:Nastavení formuláře pro konfiguraci pokročilé cenové nabídky

Vyberte ceník
-----------------

Přejděte do konkrétních nastavení POS a přidejte všechny dostupné
ceníků v poli „Dostupné“. Pak nastavte jeho výchozí ceník
:guilabel:`Výchozí hodnota“ pole.

Když spustíte obchodní sezení pomocí příkazu :ref:`<pos/session-start>`, klikněte na tlačítko „ceníky“ a vyberte
Chcete-li zobrazit požadovaný ceník, vyberte ho ze seznamu.

.. obrázek: ceny/tlačítko_ceník.png
:alt:Tlačítko pro výběr ceníku na pokladním zařízení

.. poznámka::
   - Tlačítko „cena“ se nezobrazí, pokud není vybrána více cenových nabídek.
   - Pokud je v objednávce na prodejně vybrána cenová nabídka, jejíž podmínky nejsou splněny, bude
Nebude-li tento návrh schválen, nebude možné jej upravovat.

..tip:
Můžete také nastavit ceník, který se bude automaticky vybírat při určitém :ref:`zákazníkovi.
<pos/customer>. Chcete-li tak učinit, přejděte na formulář zákazníka a v předvoleném ceníku.
:guilabel:`Ceník“ pole v záložce „Prodej a nákup“.

.. viz též:
   - :doc:`../../prodej/produkty-a-ceny/cena/cenik`
   - :ref:`Jak používat ceníky v elektronickém obchodě <ecommerce/pricelists>`
