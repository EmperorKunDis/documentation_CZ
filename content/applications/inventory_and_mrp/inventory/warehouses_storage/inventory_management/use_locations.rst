=========
Lokalita
=========

„Lokalita“ je konkrétní prostor v skladu. To může být například police, místnost, chodba atd.

Konfigurace
=============

Pro vytvoření konkrétních skladových míst povolte funkci „Skladové lokality“ přes
:menuvolba:„Skladové aplikace“ --> „Konfigurace“ --> „Nastavení“. V části
V části „Uložení“ zaškrtněte políčko „Uložení“. Pak klikněte na tlačítko „Uložit“.

.. poznámka::
Typicky se používá funkce „Uložiště“ (Guilabel: Storage Locations) s funkcí „Multistopové trasy“ (Doc: Multi-Step Routes).
<../../shipping_receiving/daily_operations/use_routes>, která řídí pohyb produktů mezi
lokality.

.. obrázek: enable-location.png
:align:center
:alt:Zobrazit funkci Zobrazení skladových míst.

Vytvořit novou polohu
===================

Po zapnutí položky „Uložiště“ přejděte na:
Lokality.

.. obrázek: use_locations/locations.png
:align:center
:alt: Seznam vnitřních lokalit.

Na této stránce klikněte na tlačítko „Nový“. Poté můžete novou polohu konfigurovat takto:

- :guilabel:`Název místa“: poznatelný název místa.
- :guilabel:`Parent Location“: místo, ve kterém se nová lokalita nachází. Po zadání lokality
je vytvořen, je uveden na stránce :guilabel:`Lokace`, která používá hierarchii *lokací*.
popisují, jak konkrétní místo zapadá do větších oblastí skladu.

...... příklad::
V poli „WH/Stock/Zone A/Refrigerator 1“ je „Refrigerator 1“ názvem lokace a „Zone A“ je zónou.
místo a vše před ním je cesta ukazující, kde se tento bod nachází ve městě.
skladu.

Dodatečné informace
------------------------------

Kromě povinných polí výše je třeba také nakonfigurovat následující položky umístění, aby bylo zajištěno
lokalita plní svůj účel v databázi:

- :guilabel:`Typ umístění“: z rozevírací nabídky vyberte „Prodejce“.
:guilabel:`Zobrazení“, :guilabel:`Vnitřní umístění“, :guilabel:`Umístění zákazníka“
:guilabel:`Ztráta zásob“, :guilabel:`Výroba“ nebo :guilabel:"Přepravní místo" kategorizovat
lokalitu. Pro podrobnosti o každém typu lokality se podívejte na část :ref:`Lokalita

- :guilabel:`Kategorie úložiště“: k dispozici pouze s :doc:`Kategoriemi úložišť
<../../shipping_receiving/daily_operations/storage_category> funkce,
:menu:"Inventář aplikace --> Konfigurace --> Nastavení".
- :guilabel:`Společnost“: společnost, ke které patří dané místo.
- Zatrhněte tuto políčko, pokud chcete umožnit odpisy.
Zde jsou uloženy.
- Zatrhněte tuto políčko, pokud chcete umožnit vrácení produktů na tento sklad.
lokalita.
- :guilabel:`Čárový kód“: používá se s aplikací *Čárový kód*, zadejte čárový kód pro identifikaci akcí
„<čárový kód/nastavení/umístění>“ v tomto místě při skenování.
- „Dodat místo“: používá se k :doc:`konfiguraci tras

místo pro přijímání produktů od *Kup teď*, *Vyráběj* nebo jiných cest nákupu
zajištění dodržování správného procesu dodání zboží do skladu.

.. obrázek: use_locations/new-location.png
:align:center
:alt:Dodatečné informace v nově vytvářeném formuláři pro umístění.

Zbývající pole v sekci „Další informace“ nastavte následovně:

- :guilabel:`Společnost“: společnost, jejíž sklad je v tomto místě umístěn. Nechte toto pole prázdné
pokud se tato lokalita dělí mezi společnosti.
- Zatrhněte tuto políčko, pokud chcete umožnit odpisy.
Zde jsou uloženy.
- Zatrhněte tuto políčko, pokud chcete umožnit vrácení produktů na tento sklad.
lokalita.
- :guilabel:`Čárový kód`: čárový kód přidělený místu.
- Zaškrtněte políčko „Doplnit zásoby na tomto místě“ a zvolte všechny množství, které chcete doplnit.
lokalita.

V části „Kruhový počet“ změňte hodnotu v poli „Četnost inventury“.
(Dny) pole na hodnotu 0, pokud je to nutné.

.. obrázek: use_locations/use-locations-cyclic-counting.png
:align:center
:alt:Součást nové položky vytváření umístění s cyklickým počítáním.

Pokud je jiná než 0, datum skladování pro produkty uložené v této lokalitě jsou
automaticky nastavena na definované frekvence.

V sekci „Doprava“ v poli „Strategie odvozu“ klikněte na vyhledávací pole.
menu a vyberte strategii odstranění (viz dokumentační stránku „Strategie pro odstraňování zboží“).
Tyto předměty by měly být odstraněny z této oblasti.

... inventář/hierarchie umístění:

Oddíl cyklického počítání
-----------------------

Každý měsíc se zde provádějí inventury.
Zadejte požadovaný interval do pole „Dny“. Výchozí hodnota je 0 (bez plánovaných sčítání).

Příklad: Pokud tento prvek nastavíte na hodnotu 30, pak se počítá každých 30 dní.
pro instalaci a používání této funkce se podívejte na dokumentaci „Počítání cyklů“ (viz cycle_counts).

V poli „Poslední platná inventura“ je zobrazen datum posledního sečtení zásob na tomto místě.
místo se nekonalo. Když jsou zapnuté plánované inventarizační kontroly, zobrazí se :guilabel:`Další očekávaný
Kolonka „Inventura“ zobrazuje datum příští inventury.

Příklad:
S inventarizačními kontrolami každých 30 dní a datem „Poslední účinnosti“ v poli „Label“
V případě inventury z 16. července je příští očekávaná inventura 15. srpna.

.... obrázek: use_locations/scheduled-count.png
:srovnání: do středu
:alt:Zobrazit sekci cyklického počítání v záložce lokalita.

Logistická sekce
-----------------

V sekci „Doprava“ v záložce „Lokace“ lze volitelně vybrat možnost „Odvoz“.
Strategie určuje pořadí a prioritu vybírání produktů ze skladu.
Jedná se o: :guilabel:`první vstup, první výstup (FIFO)“, :guilabel:`poslední vstup, první výstup (LIFO)“ a
Lokalita, a :guilabel:'První vypršení první ven' (FEFO)“.

.. viz také:
:doc:`../prijmu-vydeje/strategie-odvozu`

Aktuální zásoba na místě
=========================

Pro zobrazení aktuálního stavu zásob na jednom místě přejděte do aplikace Inventář -->
Konfigurace --> Umístění“ a vyberte požadované umístění.

Poté klikněte na tlačítko „Aktuální zásoby“ chytrého panelu, abyste získali seznam všech produktů.
Lokalita.

Příklad:
Seznam skladových zásob na „Polici 1“ obsahuje „266“ skříní a „39“ stolů.

.... obrázek: use_locations/current-stock.png
:srovnání: do středu
:alt:Zobrazit zásoby na polici číslo 1.
