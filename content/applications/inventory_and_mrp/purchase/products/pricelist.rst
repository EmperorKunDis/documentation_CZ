=======================
Import ceníku dodavatele
=======================

Nastavte ceny prodejců, aby automaticky vyplňovaly požadavky na nabídku (RFQ) nebo objednávky (PO).
jednotková cena, která se zobrazí po přidání produktu, a tím se sníží chybovost a ušetří čas.

V Odoo lze dodavatelské ceníky přidávat jednotlivě podle návodu:
formě produktu nebo jako „dodávaný v celku“ (viz nákup/produkty/import cenového seznamu) ve formátu XLSX nebo CSV.
soubor.

.. důležité:
Prosím, přečtěte si tento návod k importu dat:
ceníky dodavatelů.

.. nákup/produkty/ceník:

Na tvaru výrobku
===============

Chcete-li ručně přidat cenu dodavatele do formuláře produktu, přejděte na:
Produkty --> Produkty“, a klikněte na požadovaný produkt.

.. poznámka::
Produktové formuláře jsou dostupné z více aplikací, například ze Sales, Inventory a
**Výroba**.

V záložce „Nákup“ v dialogovém okně pro zadání produktu vyplňte dodavatele a jejich cenu, abyste měli
Informace se automaticky vyplní při každém požadavku na cenovou nabídku, kdy je produkt uveden.

.. viz též:
:ref:`Ceník dodavatele na formuláři produktu <nákup/spravovat smlouvy/dodavatelský ceník>`

.. obrázek: cenik/produkt-formulář-ceník.png
:alt: Ceník dodavatele na produktovém formuláři.

.. _nákup/zboží/ceník importu:

Import ceníku dodavatele
=======================

Pro import ceníků dodavatelů je nutné zajistit, aby byl soubor XLSX nebo CSV správně vyplněn. Nejlepší způsob, jak
získat správně formátovaný vzor s názvy produktů, referencemi a podrobnostmi o dodavatelích je
Nejprve exportovat cenový seznam z databáze podle návodu v části Přidání cenového seznamu do aplikace.

Upravte exportovaný soubor podle potřeby a pak jej opět do databáze Odoo.

.. kupní cena/výrobky/exportní cena:

Export cenové nabídky
----------------

Pro vývoz cenového seznamu přejděte na: „Nákupní aplikace --> Konfigurace --> Ceníky dodavatelů“.

Na stránce zaškrtněte příslušné políčko u požadovaných ceníků dodavatelů.

Pak klikněte na tlačítko „Akce“ s ikonou „fa-cog“, které se objeví, a vyberte „fa-upload“.
Vyberte položku „Export“ z nabídky.

.. obrázek: cenik-export.png
:alt:Zobrazit vybrané exportované pole s tlačítkem pro exportování viditelným.

V okně, které se otevře, jsou položky uvedené pod záložkou „Pole k exportu“.
Přidat další pole najdete požadované pole v
sekci „Dostupné pole“ a klikněte na ikonu „+“
vlevo od hřiště.

.. poznámka::
Chcete aktualizovat existující záznamy? Zaškrtněte „Chci aktualizovat data (import-kompatibilní)“
exportu a odkaz na část o :ref:`externím identifikátoru
pole „Nákupní ID“.

Pro podrobnosti o běžně používaných polích pro import cenových seznamů dodavatelů si přečtěte :ref:`Běžné pole
v sekci „Nákup/Produkty/Obecné informace“.

Vyberte požadovaný formát exportu: :guilabel:`XLSX“ nebo :guilabel:`CSV“.

Pro uložení vybraných polí jako šablony klikněte na pole „Šablona“ a zvolte
Vyberte z roletky „Nové šablony“ a zadejte název nové šablony.
Ikona „Floppy disk“ (Uložit) ikona. Po tomto kroku se šablona stává volitelnou možností
kliknutím na pole :guilabel:`Šablona`.

Konečně klikněte na tlačítko :guilabel:`Exportovat“.

.. poznámka::
S zapnutým režimem vývojáře (:ref:`developer mode <developer-mode>`) se názvy sloupců ve vyexportovaném souboru
zobrazit jméno pole (*pole*) v závorkách za technickým názvem (*název*).

Příklad:
.. obrázek: cenik_exportu.png
:alt:Exportní ceník dodavatele.

Exportní cenový seznam v formátu XLSX obsahuje: guilabel:„Šablona produktu“ a další
pole v sekci „Pole k exportu“.

...koupit produkt s externím identifikátorem:

Externí identifikátor
~~~~~~~~~~~

*Externí identifikátor* je jedinečným identifikátorem používaným k aktualizaci stávajících cenových seznamů dodavatelů. Bez něj nelze importovat
Záznamy vytvářejí nové záznamy namísto aktualizace stávajících. Tento prvek by měl být součástí XLSX nebo
CSV uvádí, že tato řádek nahrazuje stávající ceník dodavatele v databázi Odoo.

Příklad:
.... obrázek: cenik/dupl_hodnoty.png
:alt: Záznam „Připravený koberec“ se objeví dvakrát.

„Připravená matrace“ se objevuje dvakrát, protože při aktualizaci ceny byl vynechán externí identifikátor.
z $790 na $780.

Pro vyhledání cenového seznamu dodavatele zadejte do pole „Vnější identifikátor“ hodnotu „Výchozí“.
zaškrtávací políčko „Data (přenositelná do importu)“ v horní části okna „Export dat“.

.. poznámka::
Vybrat pole „Externí identifikátor“ z sekce „Dostupná pole“ s
:guilabel:`Chci aktualizovat data (importovatelný vývoz)“ zaškrtnutím vede k exportu
soubor s dvěma sloupci, obsahující externí identifikační číslo.

.. nákup produktů/obecné pole:

Společná pole
~~~~~~~~~~~~~

Níže je uveden seznam běžně používaných polí při importu ceníků dodavatelů:

.. seznam-tabulka: Definice polí
:hlavičky: 1

   * - pole jméno
     - Použití
     - Pole v databázi Odoo
     - Technické označení pole
   * - Prodávající
     - Toto pole je povinné pro vytváření záznamu cenového seznamu dodavatele. Toto pole určuje
dodavatel spojený s produktem.
     - Pole „Dodavatel“ v cenovém listu produktu ve formuláři
„<nákupní seznam/produkty/cena>“.
     - partner_id
   * - Šablona produktu
     - Odoo produkt, ke kterému se vztahuje ceník dodavatele.
     - „Produkt“ v seznamu cen dodavatele.
     - „produkt_tmpl_id“
   * - Množství
     - Nejmenší množství, které je potřeba k převzetí produktu za stanovenou cenu.
     - V poli „Množství“ v cenovém seznamu dodavatele. (Pokud není viditelné, zobrazí se po kliknutí na
ikonu „Nastavení“ (adjust) a zaškrtněte pole „Množství“.
zaškrtávací políčko
     - min_qty
   * - Jednotková cena
     - Nákupní cena produktu od dodavatele.
     - :guilabel:`Cena“ pole v ceníku dodavatele.
     - „cena“
   * -Doba dodání
     - :ref:`Počet dní <sklad/úložiště/nákup-LT> před přijetím produktu
po potvrzení objednávky.
     - :guilabel:`Čas dodání“ pole na cenovce dodavatele.
     - „odklad“
   * - Sekvence
     - Určuje pořadí dodavatelů v ceníku, pokud je k dispozici více dodavatelů.
Příkladem je např. uvedení Azure Interior jako prvního a Wood Corner jako druhého, jejich sekvence by byly
„1“ a „2“.
     - N/A
     - „sekvence“
   * Společnost
     - Název společnosti, která produkt vyrábí.
     - V poli „Firma“ v cenovém seznamu dodavatele.
     - „id_spolecnosti“
   * – :ref:`Externí identifikátor <nákup/produkty/externi-identifikator>`
     - Jedinečný identifikátor záznamu používaný k aktualizaci stávajících cenových seznamů dodavatelů.
     - N/A
     - „id“

Dodací listy
--------------

S vyplněným šablonou vložte do souboru XLSX nebo CSV požadované informace.
Vložte vše a nahrajte soubor zpět do databáze Odoo, kliknutím na
:menuselection:`Koupit aplikaci --> Konfigurace --> Ceníky dodavatelů“.

Na stránce klikněte na ikonu „fa-cog“ v levém horním rohu.
vyskakovací nabídce klikněte na položku „Importovat záznamy“.

Pak klikněte na tlačítko „Nahrát soubor“ v pravém horním rohu a po výběru souboru XLSX nebo CSV
souboru, potvrďte správná pole a klikněte na „Import“.

.. viz též:
   - :doc:`../../../základy/export-a-import-dat`
   - :ref:`Obecné pole <nákup/produkty/obecne-pole>`

.. obrázek: cenikdodavatele/cena-dodavatele-priklad.png
:alt:Obrázek obrazovky pro nahrání souboru.

Formátování souboru s daty
~~~~~~~~~~~~~~~~~~~~~~

Chcete-li pochopit, jak formátovat soubory pro dovoz z cenových seznamů dodavatelů, podívejte se na následující příklad.

- „Úložný box“ (:guilabel:"Referenční objekt": "E-COM08") je prodáván firmou „Wood Corner“ za 10 $.
- „Velký stůl“ (:guilabel:"Referenční číslo": "E-COM09") nemá v ceníku dodavatele žádné záznamy.

Importní soubor vytvoříme pro následující účely:

- Aktualizujte cenu „Dřevěný roh“ z $10 na $13.
- Přidejte ceník pro „Skladovací krabici“: dodavatel Ready Mat chce prodávat produkt za 14 $.
- Přidejte ceník pro „Velký stůl“: dodavatel je „Dřevo roh“, cena je 1299 $.
- Přidejte ceník pro „Velký stůl“: dodavatel je „Interiér Azure“, cena je 1399 $.

.. seznam-tabulka: Ceník dodavatele
:hlavičky: 1

   * 
     - id_spolecnosti
     - odklad
     - cena
     - product_tmpl_id
     - série
     - partner_id
   * - produkt.produktovyrobce
     - Moje společnost (San Francisco)
     - 3
     - 13.00
     - [E-COM08] Úložná krabice
     - 4
     - Dřevo Corner
   * -
     - Moje společnost (San Francisco)
     - 3
     - 14.00
     - [E-COM08] Úložná krabice
     - 5
     - Ready Mat
   * -
     - Moje společnost (San Francisco)
     - 2
     - 1299.00
     - [E-KOM09] Velká pracovní deska
     - 6
     - Dřevo Corner
   * -
     - Moje společnost (San Francisco)
     - 4
     - 1399.00
     - [E-KOM09] Velká pracovní deska
     - 7
     - Interiér v modrém

.. poznámka::
Tento informační dokument byl vytvořen na základě technického pole názvu.

.. poznámka::
Stáhněte si vzorky souborů pro odkaz:

   - :download:`Příklad souboru pro import XLSX <pricelist/pricelist-example.xlsx>`
   - :download:`Příklad souboru pro import CSV <pricelist/pricelist-example.csv>`

