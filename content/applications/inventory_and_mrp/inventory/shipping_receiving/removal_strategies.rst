
:ukrýt stránku obsahující obsah:

==================
Strategie odstranění
==================

Pro společnosti s sklady jsou důležité strategie **odstraňování**, které produkty se z nich
skladu a **kdy**. Například u potravinových produktů se dá přednostně vybírat zboží
s nejkratším datem spotřeby pomáhá minimalizovat znehodnocení potravin.

Následující sloupce v tabulce níže uvádějí odstraňovací strategie dostupné v Odoo a podrobně popisují
jak se určuje výběr a jaká je pořadí odstranění. Využijte tyto metody pro
Odoo automaticky vybírá, jaké produkty se budou používat pro objednávky:

.. seznam-tabulka::
:hlavičkové řádky: 1
:sloupek: 1

   * -
     - :doc:`FIFO <odstraňovací strategie/fifo>`
     - :doc:`LIFO <vyřazovací strategie/lifo>“
     - :doc:`FEFO <odstraňovací strategie/fefo>`
     - :doc:`Nejbližší místo <odstranění strategií/nejbližší místo>`
     - :doc:`Nejmenší balíčky <removal_strategies/least_packages>`
   * – Na základě
     - :ref:`Datum příjmu <skladové zásoby/sklady a skladování/datum příjmu>“
     - :ref:`Datum příjmu <skladové zásoby/sklady a skladování/datum příjmu>“
     - :ref:`Datum vyřazení <skladové zásoby/datum-vyřazeni>`
     - :ref:`Sekvenční umístění <inventář/sklady a skladování/pořadí>“
     - :ref:`Množství balení <skladování/sklady/mnozstvi-baleni>`
   * - pořadí výběru
     - První v pořadí
     - Poslední
     - :ref:`První zaniká <skladové zásoby/sklady a skladování/datum vypršení platnosti>“
     - Alfanumerické jméno místa
     - Nejbližší množství k naplnění poptávky

Pro komplexní příklady použití každé odstranění strategie se podívejte na jednotlivé
dokumentační stránka.

... inventář/skladovací prostory/ukládání konfigurace:

Konfigurace
=============

Strategie odstraňování jsou nastaveny buď na produktovou kategorii nebo skladovací místo.

.. obrázek: odstranění strategií/navigace kategorie umístění.png
:align:center
:alt:Změnit strategii odstranění síly pro buď kategorie produktů nebo lokality.

Konfigurace odstranění položek na místě proveďte přes:
a vyberte požadované umístění. Na formuláři pro umístění zvolte strategii odstranění
z nabídky možností z položky „Strategie odstranění“.

.. důležité::
Aby bylo možné nastavit odstranění na určitém místě, je potřeba vybrat v nabídce „Skladovací místa“
:guilabel:`Nastavení vícekrokových tras“ musí být zapnuto v menu „Sklad –>
Konfigurace --> Nastavení.

Tyto vlastnosti jsou **pouze** nutné při nastavení odstranění na místě.

Konfigurujte strategie odstranění produktů v kategoriích pomocí volby:
Konfigurace --> Kategorie produktů a vyberte požadovanou kategorii produktu. Následně zvolte
strategie odstranění z nabídky „Vymazat strategii“.

.. důležité::
Když se používá různá odstraňovací strategie na místě i v kategorii produktu
produktu, hodnota nastavená v poli „Základní strategie odstranění“ na
:guilabel:`Kategorie produktu“ je aplikována jako priorita.

Požadované funkce
=================

Některé odstranění strategií jsou k dispozici výchozím nastavením, některé funkce však musí být povoleny.
V nabídce „Nastavení“ -> „Správa“ pro možnost odstranění.
zobrazit se v rolovacím menu „Strategie odstranění“ nebo „Odstranění“.
Strategické pole.

Pro shrnutí požadovaných funkcí se podívejte na následující tabulku. Jinak se obraťte na
sekce pro odstranění strategie s podrobnějšími požadavky a použitím.

.. seznam-tabulka::
:hlavičkové řádky: 1
:sloupek: 1

   * -
     - FIFO
     - LIFO
     - FEFO
     - Nejbližší místo
     - Nejmenší balíčky
   * -Povinné funkce
     - Čísla a sériová čísla
     - Čísla a sériová čísla
     - Číslo šarže a sériové číslo, datum expirace
     - Skladové lokality, vícekrokové trasy
     - Balíčky

... skladovací prostory, skladové zásoby, skladování:

Čísla a sériová čísla
-----------------------

Čísla a sériové číslo odlišují stejné produkty a sledují informace, jako je například příjezd nebo
datum vypršení platnosti. Chcete-li tuto funkci aktivovat, přejděte na: „Sklad --> Konfigurace
V nastavení zvolte položku „Sledovatelnost“ a u položky „Šarže a sériové číslo“ zaškrtněte pole vedle „Šarže“.
Sériové číslo, abyste tuto funkci aktivovali.

.. obrázek:: odstraneni-zadosti/vypnuti-lootu.png
:align:center
:alt:Povolit sériová čísla a šarže.

Dále zkontrolujte, že je produkt sledován podle číselných lotů nebo sériových čísel, přesunutím se na stránku produktu.
formou: „Skladové zásoby“ - „Zboží“ - „Zboží“, a vyberte požadované.
produktu. V položce produkt přepněte na záložku Inventář a pod
V poli „Sledování“ vyberte buď „Podle jedinečného sériového čísla“, nebo „Podle
Možností je spousta.

Po zapnutí funkcí přiřaďte produktům čísla položek nebo sériové číslo pomocí :doc:`skladového
Adaptace na skladové zásoby nebo během :ref:`produktu
příjem <výpočetní technika/správa produktů/přiřazení položek>.

Lokalita a trasa
--------------------

Paměťové umístění a vícekrokové trasy jsou nezbytné funkce pro nastavení všech typů
strategie odstranění na místě. Tyto vlastnosti jsou však specificky požadovány pro nejbližší
strategie odstranění umístění, protože je aplikována pouze na úrovni umístění.

Aby byly tyto funkce aktivovány, přejděte na: „Inventář“ → „Konfigurace“ → „Nastavení“.
V sekci Sklad zapněte položku Skladová lokalita.
:guilabel:`Multistepové trasy“

.. obrázek: odstranění strategií/zapnout umístění.png
:align:center
:alt:Zapněte funkce umístění a trasy.

... skladovací prostory, sklady a výrobní zařízení:

Datum vypršení platnosti
---------------

Aktivujte funkci „datum vypršení platnosti“, abyste mohli sledovat datum vypršení platnosti, doporučené datum spotřeby, odstranění.
a upozornění na datum nebo sériové číslo pomocí navigace do sekce „Sklad“ ->
Konfigurace --> Nastavení.

Pod nadpisem „Sledovatelnost“ zajistěte funkci „Čísla šarží a sériové číslo“.
vyberte si a pak zaškrtněte políčko pro:guilabel:`Datum vypršení platnosti` a zapněte tuto funkci.

.. obrázek:: odstraneni_strategii/vypršení.png
:align:center
:alt:Zapnout funkci datumu spotřeby pro FEFO.

.. skladovací prostory, sklady a balení:

Balíčky
--------

Funkce balíčků je používána k seskupení produktů a je pro nejmenší balíčky povinná.
strategie odstranění.

Přejděte do sekce „Nastavení“ a zaškrtněte políčko u
:guilabel:`Soubory“.

.. obrázek: odstraneni-baliku/povolit-balik.png
:align:center
:alt:Zapněte funkci balíčku.

.. viz také:
   - :doc:`Balíčky <../product_management/configure/packages>`
   - :doc:`Dodání ve dvou krocích <denní operace/přijetí zásilek ve dvou krocích>`
   - :doc:`Dodání ve třech krocích <denní operace/dodání ve třech krocích>`

.. toctree::
:tituly:

strategie odstranění fifo
strategie odstranění/LIFO
odstranění strategií/fefo
strategie odstranění/nejblíže umístěné
odstranění strategií/nejmenších balíků
