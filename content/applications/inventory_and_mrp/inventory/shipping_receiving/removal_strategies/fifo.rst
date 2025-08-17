============
Odstranění FIF
============

Strategie „První vstup, první výstup“ (FIFO) vybírá produkty s nejranějšími daty příjezdu.
Tento způsob je užitečný pro společnosti prodávající produkty, které mají krátké cykly poptávky, jako jsou například oblečení.
například. Pomocí zkratky FIFO (First In, First Out) mohou společnosti zabránit tomu, aby se zásoby
zachování specifických stylů.

.. viz také:
:doc:`O odstraňovacích strategiích <../removal_strategies>`

Příklad:
V různém množství produktu „Tričko“ sledovaného podle čísla šarže dorazí 1. srpna a
25. srpna. U objednávky z 1. září platí :abbr:`FIFO (First In, First Out)` výdej
Strategie se zaměřuje na položky, které jsou skladem nejdéle. Proto produkty přijaté v srpnu
První se sklízí jako první.

.... obrázek:: fifo/fifo-example.png
:srovnání: do středu
:alt:Ilustrace vybírání nejstarších produktů skladem.

.. viz také:
:ref:`Nastavení čísla a sériového čísla <skladové zásoby/úložiště/nastavení čísla a sériového čísla>“

.. skladové zásoby/sklady/datum příjezdu:

Datum příjezdu
============

Chcete-li zobrazit první položku nebo sériové číslo produktu, který byl přijat do skladu, přejděte na
:menuvolba:„Aplikace pro inventář --> Zboží --> Šarže“.

Pak vyberte ikonu „▶️ (směřující vpravo)“ na levé straně produktového řádku.
zveřejnit seznam skladových položek nebo sériových čísel produktu, které jsou v zásobě.
Na hrací ploše je uvedeno číslo/sériové číslo a datum vytvoření, což je ve skutečnosti datum příjezdu.

Příklad:
Sériové číslo produktu „Skříň s dvířky“ bylo doručeno 29. prosince v podobě „00000000500“.
zobrazené v poli :guilabel:`Vytvořeno`.

.... obrázek:: fifo/vytvoreno.png
:srovnání: do středu
:alt:Zobrazení data příjezdu položky.

Průběh práce
========

Chcete-li pochopit, jak funguje :abbr:`FIFO (First In, First Out)“, zvažte následující
například na třech bílých košilích.

Trička jsou z kategorie „Oblečení“, kde je nastaveno FIFO („První do skladu, první ven“).
:guilabel:`Strategie silového odstranění“.

Bílé tričko je sledováno pod štítkem „By lots“ v záložce „Sklad“.
forma.

.. viz také:
   - :ref:`Nastavte strategii odstraňování skladů <inventory/warehouses_storage/removal-config>“
   - :ref:`Nastavit sledování skladových položek <sklad/skladové zásoby a skladování/nastavení skladových položek>`

Následující tabulka představuje dostupné zásoby a číslo položky bílých triček.

.. seznam-tabulka::
:hlavičkové řádky: 1
:sloupek: 1

   * -
     - LOT 1
     - LOT2
     - LOT3
   * -Na skladě
     - 5
     - 3
     - 2
   * - :ref:`Vytvořeno dne <inventory/warehouses_storage/arrival_date>`
     - 1. března
     - 1. dubna
     - 1. května

Chcete-li vidět strategii odstranění v akci, vytvořte objednávku na dodání zboží.
Pro šest bílých triček přejděte do aplikace „Prodej“ a vytvořte novou nabídku.

Po kliknutí na tlačítko „Potvrdit“ v objednávce se zobrazí dodací list s nejstaršími čísly
Trička jsou rezervována a využívají se podle strategie „první do skladu, první ven“.

Pro zobrazení podrobného výpisu klikněte na ikonu „⦙≣ (seznam bodů)“, která se nachází v
pravicového extremismu v produktové řadě bílých triček v záložce „Operace“ objednávky dodání.
Tím se otevře okno „Přesun do skladu“.

V okně „Přesun otevřeného skladu“ se v poli „Odebrat z“ zobrazí
množství, které je nutné dodat, se vybírá z. Od objednávky požadované šesti
Vybírá se pět triček z „LOT1“ a jedno z „LOT2“.

.. obrázek: fifo/bílá-košile-přebírající.png
:align:center
:alt:Dva pozemky vyhrazené pro prodejní objednávku s FIFO strategií.
