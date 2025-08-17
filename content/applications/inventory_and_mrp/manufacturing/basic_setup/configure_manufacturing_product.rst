===================================
Konfigurace výrobku
===================================

... výrobu/řízení/konfigurovat výrobní produkt:
.. |BOM| nahradit za: zkratka: `BoM (Bill of Materials)`

Chcete-li vytvořit výrobek v Odoo Manufacturing, musí být správně nakonfigurován.
Provedení spočívá v zapnutí výrobního postupu a konfiguraci nákladového listu
pro výrobek. Jakmile jsou tyto kroky dokončeny, je výrobek vybratelný při vytváření nového
výrobní objednávka.

Aktivujte výrobní trasu
==============================

Součástí každé produktové stránky je aktivní tlačítko „Výroba“.
Navigujte na:menu-selection:'Výroba -> Produkty -> Produkty'. Pak vyberte existující
produkt nebo vytvořit nový kliknutím na „New“.

Na stránce produktu vyberte záložku „Sklad“, pak zapněte „Výroba“.
zaškrtávací políčko v sekci „Dopravní trasy“. Toto oznámení říká Odoo, že produkt lze vyrobit.

.. obrázek: configure_manufacturing_product/manufacturing-route.png
:align:center
:alt:Výrobní trasa na záložce Inventář produktu.

.. výroba/základní nastavení/sledování sériových čísel:

Sledování čísla/sériového čísla
--------------------------

Přidělování sériových čísel nebo číselných lotů nově vyrobeným výrobkům je nepovinné.
:doc:`přidělit čísla nebo sériová čísla <../../inventar/produktverwaltung/produktový monitoring>`
na nově vyrobené výrobky, přejděte do sekce „Sledovatelnost“ na
Karta „Sledování“. V poli „Sledování“ vyberte možnost „Podle jedinečného sériového čísla“.
Číslo nebo:Guilabel: By Lots.

Tímto způsobem lze vytvořit pole „Číslo šarže“ nebo „Registrační číslo“ na výrobním příkazu.
Výrobní pokyny na pracovním příkazu v aplikaci Shop Floor.

.. obrázek: configure_manufacturing_product/lot-number-field.png
:align:center
:alt:"Číslo sériového čísla" pole na MO.

pole „Číslo šarže“ na MO.

.. obrázek:: configure_manufacturing_product/register-production.png
:align:center
:alt: možnost „Výroba“ pro generování čísla výrobního šarže na kartě pracovní objednávky.

volba „Výroba registru“ pro generování čísla výrobního šarže na kartě pracovního příkazu.

Nastavte seznam materiálů (BOM)
===================================

Dále je potřeba pro výrobek nakonfigurovat |BOM|, aby systém věděl, jak se vyrábí. |BOM| je
seznam komponentů a operací potřebných k výrobě produktu.

Pro vytvoření BOM pro konkrétní produkt přejděte na: „Výroba > Produkty“.
Produkty“, pak vyberte produkt. Na stránce s produktem klikněte na „Seznam komponent“.
Chytrý tlačítko v horní části stránky, pak vyberte: guilabel: New a založte novou |BOM|.

.. obrázek: configure_manufacturing_product/bom-smart-button.png
:align:center
:alt:Tlačítko chytré složky na stránce produktu.

Na BOM se automaticky vyplní pole „Produkt“ s produktem.
V poli „Kvalita“ zadejte počet jednotek, které BOZP vyrábí.

Přidejte součástku do |BOM| kliknutím na záložku „Součástky“ a poté na tlačítko „Přidat“.
linie. Vyberte komponentu z rozevírací nabídky „Komponenta“ a pak zadejte množství
v poli „Množství“. Přidejte komponenty na nové řádky, dokud nebudou všechny komponenty
byla přidána.

.. obrázek: configure_manufacturing_product/components-tab.png
:align:center
:alt:Karta součástek v návrhu výrobku.

Dále vyberte záložku „Operace“ a klikněte na „Přidat řádek“ a „Vytvořit“.
Zobrazí se okno pro přidání operace. V poli „Operace“ zadejte název
přidávané operace (například Sestavit, Řezat atd.) a vyberte pracovní centrum, kde se operace bude provádět.
Provedené z nabídky „Drobečková navigace“ v seznamu „Zdroj“. Nakonec klikněte na „Uložit a zavřít“.
dokončit přidávání operací nebo stisknout tlačítko „Uložit a nový“.

.. důležité::
Tab „Operace“ se zobrazí pouze v případě, že je zapnuté nastavení „Dodávky“.
Vyberte si takovou možnost, která vám vyhovuje. Pokud chcete používat aplikaci, přejděte na „Nastavení“ a zapněte ji.
:guilabel:`Pracovní objednávky“ zaškrtávací políčko.

.. obrázek: configure_manufacturing_product/operations-tab.png
:align:center
:alt:Karta operace v záložce materiálové skladby.

.. varování: Více se dozvíte zde

Sekce výše obsahuje pokyny pro vytvoření základního |BOM|, které umožňují produktu být
Výroba v Odoo. To ale rozhodně není vyčerpávající výčet všech možností
dostupné při konfiguraci BOM. Pro více informací o fakturách materiálu se podívejte na
dokumentace o tom, jak vytvořit seznam součástek (<bill_configuration>).
