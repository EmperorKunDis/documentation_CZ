=============
Pravidla pro ukládání
=============

Putaway je proces směrování produktů do vhodných skladových míst při příjezdu lodí.

Odoo dokáže tento proces provést bezchybně pomocí pravidel pro ukládání, které určují, jak produkty putují skrze
specifických skladových lokalit.

Po příjezdu zboží jsou vygenerovány operace na základě pravidel skladování pro efektivní pohyb produktů
na určená místa a zajistit snadnou přepravu pro budoucí objednávky.

V skladech zpracovávajících konkrétní druhy produktů mohou pravidla pro ukládání také zabránit vzniku výbušných směsí.
látky z blízkosti skladování a směřují je do jiných lokalit určených.
skladníkem.

.. viz též:
`Návody k Odoo: Pravidla pro skladování <https://www.youtube.com/watch?v=nCQMf6sj_w8>`_

Konfigurace
=============

Pro použití pravidel skladování přejděte na: „Aplikace Sklad --> Konfigurace --> Nastavení“
aktivujte funkci „Dlouhé trasy“ v sekci „Sklad“.
Takže se automaticky aktivuje funkce „Skladovací místa“.

Nakonec klikněte na tlačítko „Uložit“.

.. obrázek: putaway/activate-multi-step-routes.png
:align:center
:alt:Aktivujte vícekrokové trasy v nastavení skladu.

... inventář/cesty/pravidlo pro ukládání:

Definujte pravidlo pro ukládání
-------------------

Pro správu skladování konkrétních produktů přejděte na: `Inventory app
--> Konfigurace --> Pravidla pro ukládání. Pomocí tlačítka „Vytvořit“ konfigurujte nové pravidlo
pravidlo pro produkt nebo kategorii produktu, které pravidlo ovlivňuje.

.. důležité::
Pravidla pro uložení lze definovat buď na úrovni produktu/kategorie produktů a/nebo typu balení.
V nastavení „Soubory“ musí být zapnuté v:
(v nastavení pro tento účet).

Ve stejné linii je položka „Když produkt dorazí“ umístěna v místě, kde se používá pravidlo pro skladování.
spustit operaci, která přesune produkt na místo „Sklad“.

Pro toto fungování musí být umístění „Store to“ podumístěním prvního (např.
„WH/Stock/Ovoce“ je specifická lokalita uvnitř „WH/Stock“, kde jsou skladovány produkty.
snadněji najít).

.. příklad::
V skladovém místě **WH/Stock** jsou následující podmístnosti:

   - WH/Stock/Ovoce
   - WH/Stock/Zelenina

Zajistěte, aby všechny jablka byla uložena v oddíle ovoce, vyplněním pole „Uložit do“
lokalitu „WH/Stock/Fruits“ v okamžiku, kdy se produkt „Apple“ dostane do skladu „WH/Stock“.

Tento postup opakujte pro všechny produkty a poté stiskněte tlačítko „Uložit“.

...... obrázek:: putaway/create-putaway-rules.png
:align:center
:alt:Vytvořte pravidla pro ukládání jablek a mrkve.

Priorita pravidla o vzdálenosti
---------------------

Odoo vybírá pravidlo pro ukládání podle následujícího seznamu priorit (od nejvyšší k nejnižší):
Hledaný zápas byl nalezen.

#. Druh balení a produkt
#. Druh balení a kategorie produktu
#Balík typu
#Produkt
#Kategorie produktu

.. příklad::
Pro výrobek „Limonáda“ jsou následovně nakonfigurovány pravidla pro umístění:

   #Při přijetí „palety“ (:guilabel:„Druh balení“) s plechovkami limonády je přesměrováno na
„WH/Sklad/Palety/PAL1“.
   #„Limonáda může“: „Kategorie produktu“ je „Vše/Nápoje“, když obdržíte „Balíček“.
jakýkoliv produkt v této kategorii, zboží je přesměrováno na „WH/Sklad/Položka 1“.
   #Každý produkt na paletě je přesměrován do složky „SKLAD/Palety“.
   #Produkt „Limonáda“ je přesměrován na „WH/Sklad/Police 2“.
   #Zboží v kategorii „Vše/Nápoje“ je přesměrováno na „SKLAD/ZÁSOBY/Malý ledniček“.


:synchronizace: střed
:alt:Příklady pravidel pro uložení.

