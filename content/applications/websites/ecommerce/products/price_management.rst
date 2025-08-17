================
Řízení cen
================

Odoo nabízí několik možností výběru cen zobrazovaných na webu, stejně jako
cena podle stanovených kritérií, která se odvíjí od konkrétního stavu.

Daně
=====

Daňový konfigurátor
-----------------

Pokud chcete danit produkt, můžete buď nastavit daň v poli „Daň odběratele“ ve
**vzor produktu** nebo použijte :doc:`daňové pozice
</aplikace/finance/účetnictví/daně/daňová pozice>“.

.. viz též:
   - :/applications/finance/accounting/tax
   - :doc:`/aplikace/finance/účetnictví/daně/avatax`
   - :doc:`/aplikace/finance/účetnictví/daně/daňové pozice`

.._ecommerce-price-management-tax-display:

Daňová tabulka
-----------

Zvolená cena včetně daně závisí na legislativě země nebo typu zákazníků.
**(B2B vs. B2C)**. Pro výběr typu ceny zvolte v nabídce:
Konfigurace --> Nastavení“, v sekci „Obchod – Zboží“ přejděte dolů a vyberte
:guilabel:„Daň zahrnuta“ nebo :guilabel:„Daň nezahrnuta“.

- :guilabel:'Daň zahrnuta do ceny': Cena na webu je uvedena bez DPH.
vypočítáno v kroku přezkoumání košíku.
- :guilabel:`S DPH“: cena zobrazená na webu je **s DPH**.

.. poznámka::
Toto nastavení je webu specifické, protože se dá pro každý web upravit.
databáze.

Zobrazit typ cenové politiky vedle ceny produktu přejděte na:
Stránka --> Domovská stránka --> Obchod“, vyberte produkt, pak klikněte na „Upravit“ a v
Kartě „Nastavení“, zapněte „Daňové označení“.

.. obrázek: price_management/price-tax-display-type.png
:alt:Zobrazený daňový typ na stránce produktu.

.. viz též:
:doc:`/aplikace/finance/účetnictví/daně/b2b_b2c`

Cena za jednotku
==============

Možné je zobrazit cenu za jednotku
„Nastavení jednotek měření“ na stránce produktu.
Přejděte na „Webové stránky > Konfigurace > Nastavení“ a zapněte „Produkt“.
Referenční cena“ v sekci „Obchod – Zboží“. Pokud je aktivní, zadejte částku
je nastaven v poli „Počet základních jednotek“ šablony produktu a v poli „Prodejní cena“ šablony produktu.
Hráčův pozemek.

.. obrázek: price_management/price-cost-per-unit.png
:alt: Cena za jednotku na šabloně produktu.

Cenu za jednotku množství najdete nad tlačítkem „Přidat do košíku“ u produktu.
stránka.

.. obrázek:: price_management/price-cost-per-unit-page.png
:alt: Cena za jednotku na stránce produktu.

.. poznámka::
Pozor, že v některých zemích může být cena za jednotku povinná.

.. viz též:
:doc:`../../../inventar-und-mrp/Inventar/Produktverwaltung/Konfigurieren/Einheit`

.. _ecommerce/cena:

Ceníky
==========

Ceníky jsou primárním nástrojem pro správu cen na webových stránkách elektronického obchodování.
definovat webové ceny, které jsou odlišné od cen na šabloně produktu, podle
země skupina, měna, minimální množství, období nebo varianta.

.. viz též:
:doc:`/aplikace/prodej/produkty a ceny/ceny/cenotvorba`

Porozumění výchozím cenovým hladinám
--------------------------------

Koncept výchozího ceníku v Odoo závisí na aplikaci, kterou používáte. V **Prodejích**
aplikace, zákazníkům je přiřazen výchozí ceník podle kontaktního profilu. Pokud je
přiřazený kontaktu se stává jeho výchozím nastavením. Pokud není žádný ceník přiřazen,
Výchozí je první ceník.

V aplikaci e-commerce je výchozí ceník přiřazen na úrovni webu.
Ovlivněné uživatelským přihlášením a nastaveními země/regionu.

Jak se ceníky používají v e-commerce
---------------------------------------

Pokud je uživateli portálu přiřazen konkrétní ceník v kontaktním profilu, použije se
při jejich nákupu. Pokud však tento ceník není přiřazen webu, na kterém jsou zboží nabízena,
Při návštěvě webu uživatel vidí výchozí ceník.

.. poznámka::
Výchozí ceník je první dostupný ceník přiřazený webu bez ohledu na
nastavení skupiny země.

Veřejnost vidí ceník zobrazený na webu.

Pokud se v ceníku nachází zeměpisná skupina, Odoo zkontroluje adresu IP návštěvníka a aplikuje
odpovídající ceník. Pokud má návštěvník přiřazený ceník v kontaktním profilu,
Seznam cen má přednost před zeměpisnou verzí, pokud je přiřazena
jiná země.

Příklad:
Američan navštíví webovou stránku, nemá portálový účet.
:guilabel:`Spojené státy“ se použije ceník.

Jiný návštěvník, také z USA, má slevu :guilabel:`Sleva pro věrného zákazníka`.
cenovou nabídku přiřazenou v jejich kontaktním záznamu. Tato přiřazení mají přednost před zeměpisnou polohou
skupinové přiřazení, takže se aplikuje slevový kód „Věrný zákazník“.

.... obrázek::price_management/cenniky-priklad.png
:alt: Příklad různých ceníků přiřazených k webu.

Konfigurace ceníku
-----------------------

Aby byly ceníky aktivní, přejděte na „Webová stránka -> Konfigurace -> Nastavení“ a posuňte se dolů.
do sekce „Obchod – Zboží“, zapněte funkci „Ceník“ a
Klikněte na „Uložit“. Jakmile budou ceníky aktivní, přejděte do sekce „Webové stránky“ ->
e-commerce --> Nastavení cenových listů.

Zamezení prodeje při ceně nula
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Funkce „Zamezit prodeji zboží za nulovou cenu“ zabraňuje zákazníkům nakupovat produkty za nulu.
produktu, pokud je uvedena prodejní cena jako ‚0‘. Když je tato funkce zapnutá, místo toho vidíte
Když se pokusí zakoupit produkt, vidí „Zeptejte se nás“.
Tato funkce je užitečná pro společnosti, které chtějí skrýt ceny svých produktů.

Chcete-li využít tuto funkci, nejprve přejděte na :menuselection:`Website --> Konfigurace --> Nastavení`.
Zatrhněte zaškrtávací políčko „Předcházet prodeji zboží za nulovou cenu“ a klikněte na „Uložit“.

Poté vytvořte ceník, který nastaví všechny ceny produktů na hodnotu 0. Ujistěte se, že je tento ceník přiřazen
správná webová stránka a je uvedena jako první v cenovém seznamu.

Volitelné ceníky
~~~~~~~~~~~~~~~~~~~~~

Vybrané ceníky se zobrazují v rozevíracím seznamu cenových hladin na stránce obchodu.
Jako „výběr možností“ označené, umožňuje zákazníkům vybrat si mezi dostupnými ceníky.

.. důležité:
Pokud je ceník označen jako :guilabel:`Vybíratelný`, ale není přiřazen k žádnému konkrétnímu
webové stránky, pak se ceník zobrazí na všech webových stránkách.

Pokud je ceník označen jako :guilabel:`Vybíratelný“, objeví se v roletce vedle
vyhledávací liště. Pokud však seznam cen nebude v nabídce, může to být z několika důvodů
Další důvody:

- Pokud je možné vybrat pouze jednu cenovou nabídku, a kontakt je přiřazen k cenové nabídce, pak se
Nemusí se objevit.
- Pokud existují více zvolitelných ceníků, které odpovídají skupině návštěvníků země, jsou použity pouze tyto ceníky.
Jsou zobrazeny v rozevíracím seznamu.

Měna cizí
----------------

Pokud prodáváte v několika měnách a máte ceníky v zahraničních měnách, zákazníci
mohou vybrat svůj odpovídající ceník na stránce Shop z roletky
menu vedle vyhledávacího pole.

.. obrázek: price_management/price-pricelists.png
:alt: Výběr ceníků.

.. viz též:
   - :doc:`/aplikace/prodej/prodej/produkty-ceny/ceny/ceník`
   - :doc:`/aplikace/prodej/prodej/produkty a ceny/ceny/měny`

Trvalá sleva
==================

Pokud trvale snižujete cenu produktu, oblíbeným prostředkem k přilákání zákazníků je
*strike-through* strategie. Strategie spočívá v zobrazení předchozí ceny přeškrtnuté
*sleva* vedle něj.

.. obrázek: price_management/price-strikethrough.png
:alt: Cena přeškrtnutá.

Pro zobrazení „zrušené“ ceny zapněte možnost „Srovnávací cena“ v
V nabídce „Webová stránka“ -> „Konfigurace“ -> „Nastavení“ -> „Obchod – Kategorie produktů“. Poté přejděte na
šablonu produktu (:menuselection:`Webová stránka --> E-commerce --> Produkty`) a v
Do pole „Srovnat s cenou“ zadejte novou cenu.

.. poznámka::
Pokud ceník obsahuje typ ceny :ref:`Sleva <sales/products/price-rules>`, bude mít přeškrtnutou.
cena je viditelná pro příslušné zákazníky. To platí i v případě, že je cenou porovnání :guilabel:`Srovnávací cena`.
tato funkce nebyla zapnuta.
