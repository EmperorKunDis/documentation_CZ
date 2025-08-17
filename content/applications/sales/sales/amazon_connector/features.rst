=========================
Funkce Amazon Connector
=========================

Synchronizátor Amazonu (*Amazon Connector*) synchronizuje objednávky mezi Amazonem a Odoo, což výrazně snižuje
Čas, který je potřeba strávit ručním zadáváním objednávek na Amazonu (z účtu prodejce Amazonu) do Odoo.
umožňuje uživatelům přesně sledovat prodeje na Amazonu v Odoo.

Podporované funkce
==================

Amazon Connector umí:

- Synchronizujte všechny potvrzené objednávky (FBA i FBM) a jejich položky.
zahrnuje:

  - název produktu, popis a množství
  - poštovné za zboží
  - náklady na zabalení dárku

- Vytvořte chybějícího partnera souvisejícího s objednávkou v Odoo (podporované typy kontaktů: kontakt a
doručovací adresa)

- Oznámit Amazonu potvrzení dodávky v Odoo (FBM), abyste dostali zaplaceno.

- Synchronizujte všechny dostupné množství produktů (FBM).

- Podpora více prodejců.

- Podpora prodeje na více tržištích v rámci jednoho účtu prodávajícího.

Následující tabulka uvádí funkce poskytované systémem Odoo při použití Amazon Connectoru:

+---------------------------+----------------------------+-------------------------------------+
|                              |Amazon plní objednávku (FBA)|Prodáno přes Amazon (FBM)        |
+===========================+============================+=====================================+
|Objednávky                   |Odeslané a expedované objednávky |Neodeslané a zrušené objednávky |
|                               |Zrušené objednávky.         |Objednávky.                            |
+---------------------------+----------------------------+-------------------------------------+
|Poštovné a balné|Počítá se poštovné a balné|Počítá se poštovné a balné Amazonem.
|                                   |Amazonem a zahrnuty do  |synchronizované verze.
|                              |synchronizovaný pořadí.  |objednávky.                            |
|                           +----------------------------+-------------------------------------+
|                               |Doprava zajišťuje Amazon.  |A automaticky vám bude zaslána faktura.
|                              |                             | vytvořené v Odoo pro každý nový objednávkový formulář.
|                               |                             |Po zpracování v Odoo|
|                               |                             | pak se stav synchronizuje v  |
|                               |                             |Amazon.                              |
+---------------------------+----------------------------+-------------------------------------+
|Dárkové balení||Zpracovává Amazon.||Cena je vypočítána společností Amazon a
|                              |                             |zařazeny do synchronizovaného pořadí. |
|                              |                             |Dárkové sdělení se přidává na řádku|
|                               |                             | na dodací list a na objednávku.|
|                               |                             | Pak je na uživateli.         |
+---------------------------+----------------------------+-------------------------------------+
|Správa zásob|Spravované společností Amazon a||Správné v aplikaci Odoo Inventární systém a||
|                               | virtuální stroj|synchronizovaný s Amazonem.
|                                |místo, kde se mu bude dařit  |                                      |
|                               |Odoo.                       |                                    |
+---------------------------+----------------------------+-------------------------------------+
|Oznámení o dodání|Zpracováno společností Amazon.|Odeslání zásilky na základě dodání|
|                              |                             |Stav synchronizován z Odoo.       |
+---------------------------+----------------------------+-------------------------------------+

.. poznámka::
Amazon Connector je navržen tak, aby synchronizoval data objednávek. Jiná činnost, jako například
- stahování měsíčních poplatků, řešení sporů nebo vystavování náhrad, **musí být řízeny z
*Amazon Seller Central*, jak je zvykem.

.. varování:
Od 19. února 2024 v severoamerických tržištích:abbr:FBA (Fulfilled by Amazon) objednávky
Vytvořené pomocí Amazon Connectoru, nejsou jména zákazníků předávána na
objednávky v Odoo. Důvodem je skutečnost, že Amazon nyní vypočítává a odvádí
daň z přidané hodnoty za prodejce. To znamená, že osobní údaje o zákazníkovi jsou
již nejsou dále předávány prodejci po objednávce „Fulfilled by Amazon“

..._amazon/podporované trhy:

Podporované tržiště
======================

Pokud se na tržišti neobjeví v nabídce vašich tržišť Amazonu, je možné:ref:`přidat nový
tržiště „amazon/add-new-marketplace“.

+-------------------------------+
|Severoamerická oblast||
+===============+===============+
|Kanada         |Amazon.ca      |
+---------------+---------------+
|Mexiko         |Amazon.com.mx |
+---------------+---------------+
|USA             |Amazon.com     |
+---------------+---------------+

+-------------------------------+
|Evropský region|
+===============+===============+
|Německo        |Amazon.de      |
+---------------+---------------+
|Španělsko      |Amazon.es     |
+---------------+---------------+
|Francie         |Amazon.fr      |
+---------------+---------------+
|UK             |Amazon.co.uk  |
+---------------+---------------+
|Itálie         |Amazon.it      |
+---------------+---------------+
|Nizozemí      |Amazon.nl    |
+---------------+---------------+

.. viz též:
   - :doc:`setup`
   - :doc:`spravovat`
