Zobrazit obsah

==============
Zjištění čárového kódu
==============

„Barcode Lookup <https://www.barcodelookup.com/>“ umožňuje skenovat (nebo zadávat) čárové kódy produktů
(:zkratka:UPC (Univerzální kód výrobku), :zkratka:EAN (Číslo výrobku v Evropě) nebo :zkratka:ISBN
(mezinárodní standardní číslo knihy) automaticky vytvořit je ve vaší databázi Odoo.
s názvy produktů, popisy, obrázky a kategoriemi apod.

.._vyhledávání podle čárového kódu:

Konfigurace
-------------

Pokud je vaše databáze hostována na Odoo Online, můžete používat funkci čtení čárových kódů bez konfigurace.

Pokud je databáze hostována na Odoo.sh nebo v prostředí on-premise, postupujte takto:

#Navštivte webovou stránku „Vyhledávání čárového kódu“ <https://www.barcodelookup.com/api> a klikněte
:guilabel:`Přihlásit se k API“.
#Vyberte vhodný plán podle počtu čárových kódů, které chcete skenovat.
#Vyplňte požadované údaje a dokončete registrační proces.
#Zkopírujte klíč API.
#V Odoo otevřete aplikaci Nastavení, posuňte se dolů do části „Součásti“ a pod ní najděte
:guilabel:`Databáze čárových kódů“, vložte „Klíč API“ z :guilabel:`Vyhledávání čárového kódu“.

Použití
---

Chcete-li doplnit informace o produktu pomocí aplikace Barcode Lookup, vytvořte nový produkt a vyplňte
:guilabel:„Čárový kód“ pole. Detaily produktu jsou pak automaticky importovány z čárového kódu
Vyhledávání a aktualizace následujících polí: :guilabel:`Jméno`, :guilabel:`Cena`, :guilabel:`Popis`,
:guilabel:'Daň', :guilabel:'Obraz', :guilabel:'Hmotnost', :guilabel:'Atributy', :guilabel:'Produkt
kategorie“, „popis“ a „velikost“. Poté můžete upravit libovolný pole (pole).

.. viz též:
:ref:`Vytvářejte nové produkty při vnitropodnikových přesunech pomocí databáze čárového kódu
"<barcode/setup/barcodelookup>".
