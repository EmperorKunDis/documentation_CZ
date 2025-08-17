================================
Ocenění podle sériových čísel
================================

Účetní inventarizační hodnota podle :doc:`účetního předpisu <using_accounting_rules>
z „https://cs.wikipedia.org/w/index.php?title=Sledování_produktu&oldid=17839462“

#:ref:`Srovnejte a odlište náklady na nákup <Inventář/Produktový management/Zobrazení hodnoty>“
na základě čísla nebo sériového čísla.
#Sledovat skutečnou cenu výrobku na základě skutečné ceny každého sledovaného komponentu.
používány.
#Devalvujte konkrétní sériové číslo nebo počet, pokud zůstane příliš dlouho ve skladu.
<../sklady/reporting/stare-zbozi>.

.. důležité::
Prosím, přečtěte si tento článek:Úvod do oceňování zásob<inventory_valuation_config>.
zadávání hodnoty podle sériových čísel.

Konfigurace
=============

Aby bylo možné hodnotit podle sériových čísel nebo lotů, je třeba nejprve povolit :doc:`Sériová čísla a loty
vlastností <../product_tracking>. Poté přejděte na: menu výběru: Skladové zásoby --> Zboží
Produkty“, vyberte požadovaný produkt nebo vytvořte nový produkt kliknutím na „Nový“.

V poli „Kategorie“ na produktovém formuláři vyberte kategorii produktu. Zajistěte
Metoda nákladového účtování kategorie produktů je nastavena na
*První do první ven (FIFO)* nebo *Průměrná cena (AVCO)*.

.. tip::
Chcete-li zkontrolovat metodu cenového určení pro kategorii produktu, přejeďte kurzorem nad :guilabel:`Kategorie`.
pole a klikněte na ikonu „Obrázek 1“ (Vnitřní odkaz).

.. viz též:
:ref:`Metody výpočtu nákladů <sklady/metody-vypoctu-nakladu>`

Poté aktivujte produkt k sledování pomocí čísla šarže nebo sériového čísla zaškrtnutím políčka „Sledovat
Zaškrtněte políčko „Inventář“ a pak klikněte na pole vedle něj, které se objeví, a vyberte buď:
Vyberte položku „Lots“ nebo „By Unique Serial Number“ z nabídky, která se objeví.

Pokud tak učiníte, zobrazí se pod ním zaškrtávací políčko „Hodnota dle sériového čísla“. Zatrhněte
zaškrtávací políčko a konfigurace pro sledování hodnoty podle čísla nebo sériového čísla je kompletní.

.. obrázek: hodnotenie_podielmi/produkt-forma.png
:alt:Forma produktu, která zobrazuje funkci Ocenění podle čísla nebo sériového čísla.

Produktová forma, která zobrazuje funkci Hodnota dle sériového čísla nebo pořadového čísla

Vrstvy hodnotících parametrů
================

Chcete-li pochopit, jak funguje oceňování podle sériových čísel a lotů, zvažte následující scénáře:

#.:ref:`Nákup a prodej produktů <Inventář/Produktový management/Odhad ceny - příklad>`: náklady
vypočítané na základě metody nákladového účtování vztahující se k dané kategorii produktů.
#Vytvořte nové číslo sériového čísla (Inventář / Produktové řízení / Vyčíslení nákladů - Nový) pomocí
úprava zásob: hodnota nového čísla sériového čísla je přiřazena k nákladu na výrobek
formulář.
#Aktualizace zásob pro stávající číslo sériového čísla nebo položku.
</výrobek/správa výrobku/hodnota stávajících nákladů>: hodnota je přiřazena na základě nejvyšších
aktuální cena za tento lístek/sériové číslo.

Pro oba metody „Průměrná cena“ a „Nejprve vstupy, potom výstupy“ je pole „Cena“
Na výrobku se tato vzorce používají k výpočtu:

:math:`Průměrná cena = Celková hodnota / Celkové množství“

.. inventář/správa produktů/hodnota nákladů - příklad:

Nakupujte produkty
-----------------

Zvažte, jak nákup produktů ovlivňuje ocenění zásob v tabulce níže.

.. seznam tabulkový::
:hlavičkové řádky: 1
:prázdné sloupky: 1

   * -
     - Množství
     - Číslo losování
     - Matematika
     - Průměrná cena na produkt
   * - Prázdné sklady
     - 0.00
     -
     -
     - $0
   * - Den 1: Obdržíte jeden produkt za 10 dolarů/kus
     - 1.00
     - LOT 1
     - :\(\frac{10}{1}\)
     - $10
   * - Den 2: Obdržíte další produkt za 20 dolarů/kus
     - 1.00
     - LOT 2
     - :\(\frac{10+20}{2}\)
     - $15

.. obrázek: ocenění_po_lotu/rty.png
:alt:Zobrazit cenu na kartě produktu.

Výsledkem je, že produkt ve formě zobrazuje průměrnou cenu 15 USD v poli „Náklady“.

...Inventar/Produktverwaltung/Bewertungskosten Neuer:

Vytvořit nový sériový číslo
----------------------------

Vytvoření nového čísla sériového čísla prostřednictvím :doc:`účetního ošetření
V poli <../../warehouses_storage/inventory_management/count_products> je přiřazen stejný výpočet jako u nákladů
na výrobku.

Pro provedení inventarizační operace a přiřazení čísla skladového místa přejděte na:
Operace --> Fyzický inventář“. Pak klikněte na „Nový“.

V nové řádce úpravy zásob zadejte:guilabel:Produkt a vytvořte
Vyberte „Číslo šarže“ a „Počet“, klikněte na ikonu „Floppy“.
:guilabel:`Použít“.

Pro zobrazení vrstvy ocenění přejděte na: „Inventářová aplikace --> Zprávy --> Oceňování“.
Hodnota celkem na jednotku odpovídá ceně v produktovém formuláři.

.. příklad::
Pokračujme v příkladu uvedeném v tabulce výše. Pokud je cena produktu 15 $, hodnota pro ocenění
nově vytvořená LOT3 bude také $15.

.... obrázek:: hodnotit_podle_aukcí/vytvořit-nový.png
:alt:Zobrazit hodnotu úpravy zásob.

.. inventarizaci, správu produktů a ocenění stávajících aktiv:

Stávající číslo/sériové číslo
--------------------------

Při upravování množství stávajícího čísla sériového čísla se hodnota odvíjí od nejnovější
hodnotící vrstva pro konkrétní číslo sériového čísla.

.. příklad::
Pokračujme v příkladu uvedeném ve výše uvedené tabulce. Hodnota pro „LOT 1“ je $10.

Takže když je množství aktualizováno na hodnotu 1,00 dolaru na 2,00 dolarů, navýšená částka se také změní na
10 dolarů, což odráží nejnovější cenovou vrstvu pro „LOT 1“.

.. obrázek:: valuation_by_lots/existing.png
:alt:Zobrazí aktualizovanou cenu položky číslo 1.

Inventarizační rozdíl (horní hranice) je oceněn stejně jako LOT 1 (spodní hranice).

...Inventar/Produktverwaltung/Anzeige der Bewertung:

Zobrazit hodnotu
==============

Pro zjištění průměrné ceny konkrétního kusu/sériového čísla přejděte do aplikace „Sklad“ v menu:
Produkty --> Sériové číslo / Šarže“, vyberte požadovaný záznam.

Oba pole „Náklady“ a „Průměrné náklady“ ukazují průměrnou cenu jednotky.
:guilabel:`Celková hodnota“ odráží celkovou hodnotu v daném čísle sériového čísla.

.. důležité::
Zajistěte, aby metoda výpočtu nákladů byla nastavena na *První vstup, první výstup* nebo *Průměrná cena (AVCO)*
Zobrazit cenu na této stránce.

.. obrázek: ocenění_podle_lokací/lokace.png
:alt:Zobrazit cenu za jednotku/sériové číslo.

Formulář s poli „Cena“ a tlačítkem „Ocenění“, které je v pravém horním rohu.

Výsledky hodnocení lze zobrazit v hodnoticím protokolu.
<Inventář/Správa produktů/Ocenění> nebo kliknutím na číslo položky / sériové číslo
:guilabel:„Ocenění“ chytrý tlačítko. Tyto podrobné záznamy linií po linii mohou pomoci určit, jak každá
Přesun zásob z konkrétního skladu nebo sériového čísla ovlivňuje jeho ocenění.

...Inventarizace, řízení zásob a ocenění:

Ocenění
----------------

Zobrazení hodnoty položek a sériových čísel v databázi proveďte tak, že přejdete na
:menuvolba:„Skladové zásoby -> Hlášení - > Ocenění“.

Na výsledném zprávě o hodnotě akcií klikněte na vyhledávací lištu a v
Vyberte možnost „Skupina“ v sekci „Použít“, která je součástí výsledného rozbalovacího menu.
:guilabel:`Číslo šarže“.

.. tip::
Klikněte na ikonu „Plus“ vedle zmenšené čáry prodejního pořadí, abyste
:ref:`ručně upravit cenu <inventory/product_management/update-unit-price>.

Toto je užitečné pro nastavení individuálních cen jednotlivých položek v případě nákupního
více položek/sériových čísel, protože ceny při přijetí jsou stejné.

.. obrázek: ocenění_aukcí/hodnota_akcií.png
:alt:Zobrazit hodnotící zprávu podle jednotlivých položek.

Tlačítko pro hodnocení
----------------------

Přejděte do části zprávy o hodnotě akcií specifické pro konkrétní položku nebo sériové číslo.
:menuvolba:„Aplikace skladu“ -> „Zboží“ -> „Sériová čísla“, a vyberte požadovaný výrobek.

Na stránce „Číslo šarže / číslo výrobku“ klikněte na tlačítko „Ocenění“.

.. obrázek:: oceňování_podle_souborů/oceňování-podle-skladových-zásob.png
:alt:Všechny pohyby skladových zásob související s „LOTem 1“.

Všechny pohyby zásob, které ovlivňují ocenění „LOT 1“.
