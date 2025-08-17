=================
Používání čárového kódu GS1
=================

... _čárový kód/operační číslo/GS1 použití:

.. |AI| nahradit za: zkratka: `A.I. (Application Identifier)`
.. |EAN| nahradit za: zkratku: EAN (Global Trade Item Number)

GS1 kódy poskytují standardizovaný formát, který čtečky čárových kódů dokáží interpretovat.
informace v konkrétním strukturovaném formátu, který je uznáván po celém světě (<barcode/operations/gs1>)
snímače, které umožňují porozumět a zpracovávat datové toky dodavatelského řetězce konzistentně.

Odoo *Barcode* dekóduje a tiskne čárové kódy GS1, automatizuje identifikaci a sledování produktů
v procesech skladování jako je příjem, vybírání a odesílání.

Následující části obsahují příklady, jak Odoo používá čárové kódy GS1 poskytnuté firmou.
identifikovat běžné skladové položky a automatizovat určité skladové procesy.

.. důležité::
Odoo **nevytváří** GS1 čárové kódy. Firmy si musí zakoupit jedinečné celosvětové číslo obchodního předmětu
(GTIN) od společnosti GS1. Poté mohou kombinovat své stávající kódy GTIN s produkty a dodavatelským řetězcem
informace (poskytnuté i společností GS1), které umožňují vytvářet čárové kódy v Odoo.

.. viz též:
   - „Koupit GTIN <https://www.gs1.org/standards/get-barcodes>“
   - :ref:`Nomenklatura GS1 <barcode/operations/gs1>“

... _čárový kód/operaci/GS1 - loty:

Nastavte čárové kódy pro produkt, množství a šarže
==================================================

Vytvořit čárový kód GS1, který obsahuje informace o produktu, jeho množství a šarži
číslo následujících čárových kódů a identifikátorů aplikace (AI):

+------------+--------------------------+------+----------------------------------+------------------------------------------+
|Název|Pravidlo jména|A.I.|Čárový kód vzoru|Pole v Odoo|
+============+==========================+======+==================================+==========================================+
Produkt | Celosvětový číselný kód zboží | 01 | (01)(číslo 14)                      |:label: pole „Čárový kód“ na formuláři produktu
|            |(EAN)                    |      |                                  |                                          |
+------------+--------------------------+------+----------------------------------+------------------------------------------+
|Množství     |Počet položek v přepravě    |30   |(30)(0-8)                        |:guilabel:`Jednotky` pole na přepravním lístku
+------------+--------------------------+------+----------------------------------+------------------------------------------+
|Číslo šarže nebo losu | Číslo šarže nebo losu     | 10  | (10)([!"%-/0-9:-?A-Z_a-z]{0,20}) | :guilabel:`Šarže` na podrobné operace   |
|            |                          |      |                                  |pop-up                                   |
+------------+--------------------------+------+----------------------------------+------------------------------------------+

.. _čárový kód/operaci/sestavení lotu:

Konfigurace
-------------

Nejprve: zapněte sledování produktů pomocí šarží (<inventory/management/track_products_by_lots>).
Přejít na: menu-selection: „Seznam inventáře -> Konfigurace -> Nastavení“ a zaškrtnout políčko
pod nadpisem „Sledovatelnost“ v položce „Čísla a sériová čísla“.

Pak přejděte na požadovanou položku a zadejte kód produktu.
Vyberte aplikaci „Inventář“ -> „Produkty“ -> „Produkty“ a vyberte produkt. Na stránce s produktem
formulář, klikněte na „Upravit“. Pak v záložce „Obecné informace“ vyplňte
:guilabel: pole „Čárový kód“ s unikátním čtrnáctimístným číslem „Global Trade Item Number (GTIN)
<https://www.gs1.org/standards/get-barcodes>`, což je univerzálně uznávané identifikační číslo
Ta je poskytována společností GS1.

.. důležité::
V produktové formě vynechte znak |AI| „01“ pro vzor kódu produktu |GTIN|, protože se používá jenom
zahrnout do jediného čárového kódu více čárových kódů, které obsahují podrobné informace o
obsah balení.

.. příklad::

Pro zaznamenání kódu GS1 pro produkt „Fuji Apple“ vložte 14místný
V poli „Čárový kód“ na formuláři produktu zadat hodnotu „20611628936004“.

.... obrázek:: gs1_usage/barcode-field.png
:align:center
:alt: Do pole Barcode na kartě produktu zadejte čtrnáctimístný GTIN.

.. tip::
Chcete-li zobrazit seznam všech produktů a jejich odpovídajících čárových kódů v databázi Odoo, přejděte
do: „Nastavení aplikace Inventar --> Konfigurace --> Nastavení“. Pod položkou „Čárový kód“
hlavičce, klikněte na tlačítko „Nastavit čárové kódy produktů“ pod „Čárový kód produktu“.
části skenování. Zadejte 14místný kód GTIN do sloupce Barcode a pak stiskněte
:guilabel:`Uložit“.

.... obrázek: gs1_usage/produktové čárové kódy - stránka.png
:align:center
:alt:Zobrazit stránku s čárovými kódy produktů z nastavení skladu.

.. _čárový kód/operaci/nastavení lotu na produkt:

Po aktivaci sledování dle šarží a sériových čísel z nastavení je třeba specifikovat
funkce se aplikuje na každý produkt po přechodu do záložky „Sklad“.
formě produktu. V poli „Sledování“ vyberte možnost „Podle balení“.

.. obrázek:: gs1_usage/track-by-lots.png
:align:center
:alt:V položce „Sklad“ v kartě produktu povolte sledování skladových pohybů podle šarží.

Naskenujte čárový kód na účtence
-----------------------

Aby bylo možné přesně interpretovat odběr zboží v Odoo na základě čárových kódů, které byly skenovány při příjmu.
operaci, přejděte do aplikace „Čárový kód“ a spravujte proces vyzvedávání účtenek.
<čárový kód/operaci/snímají přijaté produkty>.

Ve widgetu „Skenování čárových kódů“ klikněte na tlačítko „Provoz“, poté
Tlačítko „Přijaté faktury“ pro zobrazení seznamu přijatých faktur, které je třeba zpracovat. Faktury vytvořené
Seznam POs (nákupních objednávek) je uveden, ale nové příjemové operace lze vytvářet také přímo.
pomocí aplikace „Čárový kód“ přes tlačítko „Vytvořit“.

V seznamu dokladů klikněte na skladovou operaci („WH/IN“) a naskenujte čárové kódy produktů.
čísla losů s čtečkou čárového kódu. Po naskenování se pak produkt objeví na seznamu. Použijte
Tlačítko „:guilabel:`✏️ (tužka)“ pro otevření okna, ve kterém lze ručně zadat množství konkrétní položky.
čísla.

.. příklad::
Po vytvoření objednávky na 50 jablek přejděte do příslušného dokladu.
v aplikaci Barcode.

Zkontrolujte čárový kód obsahující |GTIN|, množství a číslo šarže. Pro testování s čárovým kódem
snímač, níže je příklad čárového kódu pro padesát jablek Fujis v balení číslo dvě.

...... seznamová tabulka::
:šířky: 50 50
:hlavičkové řádky: 1
:sloupky: 1

      * – 50 jablek Fujis v lotu 0002
        -
      * - 2D Matrix
        - .. obrázek: gs1_usage/fuji-apples-barcode.png
:alt: 2D matice čárového kódu GS1 pro 50 jablek Fuji s přiřazeným šaržovým číslem.
      * - |AI| (produkt)
        - 01
      * - GS1 Barcode (produkt)
        - 20611628936004
      * - |AI| (množství)
        - 30
      * - GS1 čárový kód (množství)
        - 00000050
      * - |AI| (los)
        - 10
      * - GS1 Barcode (série číslo)
        - LOT0002
      * - Celý čárový kód GS1
        - 0120611628936004 3000000050 10LOT0002

:ref:`Pokud je konfigurace správná <barcode/operations/troubleshooting>`, „50/50“
:guilabel:`Jednotky“ se zobrazí a tlačítko „Přijmout“ změní barvu na zelenou.
Klikněte na tlačítko „Potvrdit“ pro dokončení přijetí.

.... obrázek: gs1_usage/receive-50-apples.png
:align:center
:alt:Naskenujte čárový kód produktu na stránce s vyzvednutím zboží v aplikaci Barcode.

..._čárový kód/operaci/množství-ex:

Nastavte čárový kód pro produkt a množství, které není jednotkou.
===================================================

Vytvořit čárový kód GS1, který obsahuje produkty měřené v nejednotkové hmotnosti, jako jsou například kilogramy.
Příkladem jsou následující kódy čárových kódů:

+-------------+--------------------------+----------+--------------------+----------------------------+
|Jméno|Název pravidla|A.I.|Šablona čárového kódu|Pole v Odoo|
+=============+==========================+==========+====================+============================+
|Produkt     |Číslo celosvětové obchodní položky |01       |(01)\d{14}        |:guilabel:`Čárový kód` pole |
|             |(EAN)                     |          |                    | na výrobku ve formě      |
+-------------+--------------------------+----------+--------------------+----------------------------+
| Množství v | Počet položek | 310[0-5] | (310[0-5])(\\d{6}) | :guilabel:`Jednotky` pole na
|kilogramy      |                            |          |                     |přenosná forma           |
+-------------+--------------------------+----------+--------------------+----------------------------+

Naskenujte čárový kód na účtence
-----------------------

Pro potvrzení správného výkladu množství v Odoo je nutné zadat objednávku v aplikaci Purchase
použít vhodný jednotkový měrný systém (zde :guilabel:`UoM`) pro množství produktů, které mají být
koupené.

.. viz též:
:ref:`Zjednodušte konverzi jednotek dodavatelů s UoM
<Inventář/Dodávka zboží/Převod jednotek>

Po zadání objednávky přejděte do aplikace „Čárový kód“ a získejte informace o dodavateli.
doručení zboží s kódem „<barcode/operations/scan-received-products>“.

.. příklad::
Na účtence v aplikaci Barcode obdržíte objednávku na 52,1 kilogramů broskví po skenování
čárový kód obsahující GTIN a množství broskví v kilogramech.

...... seznamová tabulka::
:šířky: 50 50
:hlavičkové řádky: 1
:sloupky: 1

      * – 52,1 kg broskví
        -
      * - 2D Matrix
        - .. obrázek: gs1_usage/broskve-kod.png
:alt: Matrix 2D kódu GS1 o 52,1 kg broskví.
      * - |AI| (produkt)
        - 01
      * - GS1 Barcode (produkt)
        - 00614141000012
      * - |AI| (kg, 1 desetinné místo)
        - 3101
      * - GS1 čárový kód (množství)
        - 000521
      * - Celý čárový kód GS1
        - 0100614141000012 3101000521

Pokud je konfigurace správná, pak se zobrazí kód „52.1 / 52.1“.
:guilabel:'kg' se zobrazí a tlačítko :guilabel:'Validovat' změní barvu na zelenou. Nakonec stiskněte
:guilabel:`Zkontrolovat“ k dokončení kontroly.

.... obrázek:: gs1_usage/scan-barcode-peaches.png
:align:center
:alt: Skenujte čárový kód na obrazovce pro příjem operaci v aplikaci Barcode.

Zkontrolujte pohyb produktů
====================

Kromě toho se do účetních záznamů zaznamenává také množství přijatých produktů.
výkazu „Pohyb produktů“, který je dostupný po přechodu na „Skladové aplikace -
Zprávy --> Pohyb produktů.

Výrobky na zprávě „Pohyb produktů“ jsou standardně seskupeny podle výrobku.
přijaté množství, klikněte na produktovou řadu, abyste otevřeli skládací nabídku s výběrem.
seznam pohybů zásob pro daný produkt. Nejnovější pohyb zásob odpovídá příjmu skladu
číslo referenční (např. „WH/IN/00013“) a množství zpracované v skenu čárového kódu, což dokazuje, že
Záznamy zpracované v aplikaci Barcode byly správně uloženy do Inventáře.

.. obrázek: gs1_usage/stock-moves-peach.png
:align:center
:alt:Přijatá zásoba se pohybuje kolem 52,1 kilogramu broskví.
