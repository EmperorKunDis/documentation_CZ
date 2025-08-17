===================================
Čárové kódy pro číslo šarže a výrobní číslo
===================================

Aplikace Barcode ušetří čas a zabrání chybám při práci s :doc:`sériovým číslem.
<../../inventář/správa produktů/sledování produktů/sériové číslo
<../../inventar/Produktverwaltung/Produktverfolgung/Seriennummern>“. Statt lange
sekvence znaků, namísto toho tiskněte a skenujte čárové kódy.

Konfigurace
=============

Pro použití čísla šarže nebo sériového čísla:

#Musí být povoleny v databázi.
#Pro každý produkt musí být vybrána sledovací položka podle čísla nebo sériového čísla.

Podívejte se na dokumentaci sériových čísel.
<../../inventory/product_management/product_tracking/serial_numbers>` a :doc:`lots dokumentace
<../Inventura/Produktové řízení/Sledování skladových položek> se dozvíte, jak začít používat tento
feature.

QR kódy kompatibilní s GS1
-----------------------

Nomenklatura GS1 může být použita pro sériové číslo a šarži.

Pro umožnění čárových kódů pro šarže a sériové čísla přejděte na:
Konfigurace --> Nastavení a v části „Sledovatelnost“ pod položkou „Šarže a
Sériové číslo“, zaškrtněte políčko „Tisk štítku s GS1 kódem pro sériová a kontrolní čísla“.

.. obrázek: sériové číslo / loty / povolit GS1 čárový kód
:alt:Nastavení inventáře s zaškrtnutou položkou „Tisk GS1 čárových kódů pro šarže a sériové čísla“.

.. varování:
GS1 šarže a sériové číslo kódy vyžadují skener schopný skenovat 2D obrázky. Viz :doc:`hardware
konfigurace hardwaru, aby se ujistil, že funkce je kompatibilní s dostupným vybavením.

... inventář/čárový kód/povinné skenování:

Povinné a nepovinné skenování
-------------------------------

Operační typy, jako příjmy a dodací listy, lze konfigurovat individuálně.
Zobrazit „Nastavení typu operace“ v části „Inventář / Správa produktů / Operace“ a zjistit, zda vyžadují sériové číslo nebo
číslo slosovacího lístku k provedení operace. Kromě toho má každý typ operace v záložce
konfiguruje, zda je skenování čísla nebo sériového čísla povinné. V případě volby „Povinný sken“ se
Jediným způsobem, jak zadat požadovaný sériový nebo šaržový číslo, je pomocí skenování čárového kódu.
Možnost „volného skenování“ umožňuje uživatelům manuálně zadat čárový kód, pokud je třeba.

Pro učinění skenování čárových kódů sériových čísel a šarží povinným, přejděte na:
app --> Konfigurace --> Druhy operací a vyberte operaci, kde mají být kódy
požadované pro sériové číslo. Potom klikněte na záložku „Aplikace čárového kódu“ a v
:guilabel:`POVINNÉ SKENOVÁNÍ“ v sekci „LOT/SERIÁL“ nastavte na „Povinné skenování“.

.. obrázek: sériové číslo/volitelný skener.png
:alt: Vybrat „Volitelný sken“ v operaci typu Příjemky.

Čárové kódy na výrobky a šarže
==============================

Pro tisk čárového kódu pro jeden nebo více výrobních šarží a sériových čísel přejděte na
Vyberte v nabídce aplikace „Skladové zásoby“ položku „Zboží“ a poté klikněte na
za každý produkt tlačítko pro tisk, klikněte na tlačítko „Tisk“ se ikonou „fa-print“ a
Vyberte buď PDF nebo ZPL podle nastavení tiskárny.

.. obrázek: sériové číslo / vybrat produkty k tisku.png
:alt:Tři vybrané produkty a tlačítko s názvem „Výtisk“ se zvýrazněným „Číslo šarže (PDF)“.

Operace
==========

Pro každý produkt sledovaný číslem šarže nebo sériovým číslem je možné provádět operace pomocí čárového kódu.
z hlavní stránky Barcode klepnutím na „Operace“ a klepnutím na požadovanou operaci
v rozhraní nebo skenováním čárového kódu pro konkrétní objednávku. Jakmile je objednávka skenována,
Vyberte produkt klepnutím nebo skenováním čárového kódu a skenujte číslo šarže nebo sériové číslo pro každý
množství.

.. tip::
Protože čárový kód výrobce a sériové číslo mohou být poškozeny během přepravy a dorazí v nefunkčním stavu
Pokud nelze skenovat, je dobrou praxí nastavit sériové číslo nebo kontrolu šarže na
volitelné <inventární číslo / čárový kód / povinné skenování>. Jinak by neplatný čárový kód zablokoval ověření.
o přijetí.

Pro výrobky bez sériového čísla existují tři možnosti řízení:
ručním zadáváním čísla, generováním je předem nebo vypnutím sériových čísel pro tento
operace.

Manuálně zadávejte sériové a šaržové číslo
-------------------------------------

Pro případy, kdy je málo produktů nebo vzácné dodávky, může být nejjednodušší zadat lot nebo
sériové číslo při převzetí zboží. Po otevření stávajícího dokladu nebo vytvoření nového
a naskenujte kód výrobku, pak stiskněte ikonu :icon:`fa-pencil` :guilabel:`(pencil)` ikona.
V poli „Sériové číslo“ zadejte sériové číslo a stiskněte „Potvrdit“.

.. obrázek: sériové číslo/ruční vstup sn
:alt: Zadávání sériového čísla.

Vytvořit sériové číslo před potvrzením
----------------------------------------

Číslo a sériové číslo lze vygenerovat z plánované přijaté faktury předtím, než se produkty dostanou na místo určení.
Má výhodu, že umožňuje tisk všech sériových čísel seřazených podle pořadí
faktura.

Pro generování čísla a sériového čísla v aplikaci Sklad klikněte na záložku „Přijaté faktury“ a vyberte
faktura vyžadující generované číslo sériového nebo losovacího lístku. V záložce „Provádění“ najdete
linie produktu a klikněte na ikonu „fa-list“ s názvem „(seznam)“.
Vyberte možnost „Otevřít: Přesun zásob“ v kontextovém menu a klikněte na „Vytvořit sériová čísla / šarže“.

.. obrázek: sériové číslo/sériové číslo vygenerovat.png
:alt: Vytvořit sériové číslo pro příchozí zásilku.

.. viz též:
:ref:`Přidělit sériové číslo <inventar/produktverwaltung/assign-sn>`

Vypněte číslo šarže a sériové číslo pro příjem
--------------------------------------------

S vyřazenými čísly a sériovými čísly pro operace jsou produkty, které lze sledovat pomocí těchto metod
Lze přijmout bez dodání sériového čísla nebo šarže. Stále je možné naskenovat
sériové číslo na stavu přijetí, ale chybějící čísla budou muset být vytvořena pomocí
Inventarizační aplikace <inventarizace/produktové řízení/skladem>.

Pro vypnutí používání sériových čísel pro konkrétní typ operace přejděte na
:menuvolba:„Správa zásob --> Konfigurace --> Typy operací“ a vyberte typ operaci.
V sekci „Číslo sériového čísla“ odškrtněte políčka „Vytvořit nové“ a „Použít“.
Ty stávající.“

.. poznámka::
Volba „Vytvořit nový“ vyžaduje od uživatele zadání sériového čísla nebo šarže.
snímání nebo typ (pokud je zapnuté skenování podle :ref:`volitelného skeneru <inventory/barcode/mandatory-scan>`,
nebude automaticky generovat sériové číslo
a způsobem, jakým je schopna aplikace Inventář.
