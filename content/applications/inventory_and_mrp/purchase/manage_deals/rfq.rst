======================
Žádosti o nabídku
======================

.. |PO| nahradit za: abbr: PO (objednávka)
.. |POs| nahradit za: zkratka: `POs (Purchase Orders)`
.. |RFQ| nahradit za: zkratka: RFQ (žádost o nabídku)
.. |RFQ| nahradí: :abbr:`RFQ (Žádosti o nabídku)“

Odoo poptávky na cenovou nabídku (RFQ) v aplikaci Přijetí standardizují objednávání produktů
od různých dodavatelů za různé ceny a s různými termíny dodání.

„Požadavky na nabídku“ jsou dokumenty, které společnosti zasílají dodavatelům s žádostí o cenovou nabídku. V Odoo se jedná o požadavek na nabídku, který je vytvořen a odeslán dodavateli.
schvaluje |RFQ| a potvrzuje objednávku (PO), aby se shodovaly s dodacími lhůtami a cenou.

Konfigurace
=============

Produkt
-------

Chcete-li automaticky doplnit informace o produktech a ceny na RFQ, přejděte na
:menuselection:`Koupit aplikaci --> Produkty --> Produkty“. Vyberte existující produkt nebo vytvořte nový.
Jedním z nich je výběr položky „New“. To otevře formulář produktu, kde jsou uvedeny prodejní a nákupní údaje
je možné přizpůsobit.

Pro nakupované produkty zaškrtněte políčko „Nákup“ pod názvem produktu.
Poté přejděte na záložku „Sklad“, zapněte možnost „Koupit“ a zadejte cenu.

.. důležité:
Tab „Inventář“ a trasy jsou viditelné pouze v případě, že používáte aplikaci „Inventář“.
<../soupis>.

.. viz též:
:doc:`Nastavte typy produktů a sledovat množství


.. obrázek:rfq/produkt-dodavatel-cenik.png
:alt:Nutná konfigurace pro nakupované produkty.


... nakupovat/spravovat smlouvy/cenové nabídky dodavatelů:

Seznam cen dodavatele
----------------

V záložce „Nákup“ v dialogovém okně pro zadání produktu klikněte na „Přidat řádek“, abyste mohli
dodavatele a jejich cenu, aby se tyto informace automaticky vyplňovaly v každé poptávce.
v seznamu.

.. viz též:
:doc:`../produkty/cenik.pdf`

Výchozí sloupce zahrnují: „Množství“, „Jednotková cena“ a „Čas dodání“.
Čas, ale další sloupce jako například „Kód dodavatele“ nebo „Sleva (%)“, mohou také
Musí být umožněn.

Chcete-li povolit nebo zakázat sloupce, klikněte na ikonu „Nastavení (další možnosti)“
ikonu vpravo od hlavičkové řady, aby se zobrazilo rozbalovací menu s dalšími sloupci.
bude přidán nebo odstraněn z záložky „Koupit“.

.. poznámka::
Alternativně lze ceny a dodací lhůty pro stávající produkty přidat kliknutím na
:menu:Koupit aplikaci --> Konfigurace --> Ceníky dodavatelů. Klikněte na
v pravém horním rohu. V sekci „Dodavatel“ formuláře cenové nabídky, která se zobrazí, přidejte
informace o produktu, které se týkají dodavatele.

Objednat produkty
==============

S produkty a cenami nakonfigurovanými proveďte tyto kroky pro vytvoření a odeslání požadavku na nabídku (RFQ)
pro společnost.

Dashboard RFQ
---------------

Chcete-li začít, přejděte na: „Nákupní aplikace --> Objednávky --> Požadavky na cenovou nabídku“.

Dashboard „Poptávky“ zobrazuje přehled o firmě a jejích |poptávkách|.
a jejich stav. V horní části obrazovky jsou zobrazeny všechny |RFQs| v dané společnosti a
individuální (kde uživatel je kupujícím) s přehledem jejich stavu.

V pravém horním rohu je také zpráva o nedávných nákupních transakcích společnosti podle celkové hodnoty.
času a počtu |poptávek| zaslaných.

Dalšími tlačítky jsou:

- :guilabel:`Odeslat“: objednávky v |RFQ| fázi, které nebyly odeslány dodavateli.
- :guilabel:`Čekající“: RFQ, které bylo odesláno e-mailem a čeká na potvrzení dodavatele.
- :guilabel:`Pozdní“: |RFQs| nebo |POs|, kde již uplynul termín „Deadline“.

.. obrázek: rfq/rfq-dashboard.png
:alt:Dashboard s objednávkami a stavy objednávek.

Kromě možností zobrazení nabízí rozhraní „Poptávky“ také
Možnosti filtru a seskupení dostupné prostřednictvím vyskakovacího menu nad lištou hledání.

.. viz též:
:doc:`../../../základy/vyhledávání`

... nakupovat, spravovat smlouvy a vytvářet nové poptávky.

Vytvořit novou |poptávku|
------------------

Pro vytvoření nového poptávkového formuláře klikněte na tlačítko „Nový“ v pravém horním rohu
příkazu „Požadavky na nabídku“ odhalit nový formulář PO.

Začněte přiřazením :guilabel:`Vendor`.

Záložka „Dodavatelské referenční číslo“ odkazuje na čísla objednávek a dodání, které byly zaslány
dodavatelem. Tento přístup se hodí v okamžiku, kdy jsou produkty obdrženy a potřebuje se zadat
dodací list.

S aktivovanou funkcí „Nákupní smlouvy“ (<blanket_orders>) je možné používat :guilabel:„Plošnou objednávku“.
V poli „Objednávka“ se objeví odkaz na dlouhodobou kupní smlouvu o opakujících se objednávkách s předem stanoveným
cenotvorba. Pro zobrazení a konfiguraci objednávek přejděte na: „Nákupní aplikace --> Objednávky -->
Kupní smlouvy.

.. důležité:
Zobrazení „Smluv o koupi“ se zobrazí pouze v případě, že je nastaveno „Dodavatelská objednávka“.
je aktivován. Chcete-li tak učinit, přejděte na: „Koupit aplikaci - Konfigurace - Nastavení“ a poté
Zatrhněte políčko „Plošné objednávky“.

Dále nastavte datum „Termín objednávky“, což je datum do kdy musí dodavatel potvrdit
jejich souhlas s dodávkami produktů.

.. poznámka::
Po překročení termínu objednávky je RFQ označen jako pozdní, ale produkty
Stále je možné objednat.

„Očekávaný příjezd“ je automaticky vypočítán na základě „Termínu dodání“.
doba dodání. Zaškrtněte políčko „Potvrzení od dodavatele“ a požádejte dodavatele o potvrzení
datum expedice e-mailem.

S funkcí „Uložiště“
pokud je aktivován parametr <../../inventory/warehouses_storage/inventory_management/use_locations>.
V poli „Doručit do“ se objeví pole s názvem „Doručit do“, které určuje, který skladový úkon (nastavený v
Aplikace „Inventura“ slouží k přijetí zásilky.

Vyberte adresu skladu pro odeslání zde nebo vyberte možnost „Dropship“ a uveďte tak, že tato
Zboží je určeno přímo pro konečného zákazníka. Pokud je vybrána možnost „Dropship“,
V poli „Adresa pro přepravu“ je povoleno zadávání kontaktních jmen.
Aplikace **Kontakty**.

.. důležité:
Pouze možnosti „Dropship“ se zobrazí, pokud je zapnutá volba „Dropshipping“.
v aplikaci Inventář. Chcete-li tak učinit, přejděte na:
--> Nastavení, pak zaškrtněte políčko „Dropshipping“.

..tip:
Pro vytvoření |RFQ| s různými měnami je třeba každou měnu povolit v
**Nastavení fakturace**. Podrobnosti naleznete v kapitole :doc:`../../../sales/sales/products_prices/prices/currencies`.
Zjistit více.

Karta produktů
~~~~~~~~~~~~

V záložce „Produkty“ přidejte produkty, které chcete objednat. Klikněte na „Přidat produkt“.
a zadejte název produktu nebo vyberte položku ze seznamu.

Pro vytvoření nového produktu a jeho přidání zadejte název nového produktu do sloupce :guilabel:`Produkt`,
Vyberte možnost „Vytvořit [název produktu]“ z výsledného seznamu a ručně přidejte jednotku
cena. Nebo vyberte možnost „Vytvořit a upravit ...“ a přejděte do formuláře produktu pro tento
nový produkt.

Kromě kategorie „Katalog“ lze vybrat také možnost „Výrobce“, díky které se dostanete na nabídku produktů od daného výrobce.
Zde lze přidávat produkty do košíku.

.. poznámka::
Pro úpravy produktů a cen přejděte do formuláře produktu kliknutím na
:icon:`oi-arrow-right` :guilabel:`(pravý šipka)` ikona, která se objeví při přejetí myší
název produktu.

Zaslat RFQ
--------------

Kliknutím na tlačítko „Odeslat e-mailem“ se zobrazí okno „Sestavit e-mail“, ve kterém je
Šablona „Nákup: Požadavek na nabídku“ byla načtena a připravena k odeslání e-mailem dodavateli.
adresa (nastavená v aplikaci Kontakty).

Po vytvoření požadovaného zprávy klikněte na „Odeslat“. Jakmile je odesláno, RFQ se přesune do
:guilabel:`Odeslání RFQ“ fáze.

Kliknutím na tlačítko „Tisk RFQ“ se stáhne PDF s |RFQ|.

.. viz též:
:doc:`../../../základy/kontakty`

Potvrzení objednávky
-------------

Kliknutím na tlačítko „Potvrdit objednávku“ se převádí RFQ přímo na PO.

..tip:
Odoo sleduje komunikaci na každé objednávce prostřednictvím chatu v formuláři PO.
e-maily zaslané mezi uživatelem a kontaktem, stejně jako vnitřní poznámky a aktivity.
Příspěvky, poznámky a aktivity lze také zaznamenat na chatu.

Jakmile je poptávka potvrzena, vytvoří se objednávka.

Na novém PO se pole „Termín objednávky“ mění na „Datum potvrzení“.
Ukazuje datum a čas, kdy uživatel potvrdil objednávku.

V závislosti na zvolené konfiguraci v nastavení aplikace Přijatá faktura je
Vytváří se poté, co byly objednány nebo obdrženy. Pro více informací navštivte
dokumentace na téma:

.. poznámka::
Po zadání objednávky kliknutím na tlačítko „Přijmout produkty“ se zaznamená převzetí nových produktů.
produktů do databáze.

.. poznámka::
S aplikací Inventář nainstalovanou potvrdíte PO automaticky vytvořeným dokladem o přijetí.
s automaticky vyplněnými informacemi o produktu a očekávanými daty dodání.

.. viz též:
:doc:`spravovat“
