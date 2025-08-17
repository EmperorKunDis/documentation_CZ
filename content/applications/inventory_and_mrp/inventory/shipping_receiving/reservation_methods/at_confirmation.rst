===========================
Na potvrzení rezervace
===========================

.. inventář/rezervační metody/potvrzení:

.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`

Metoda rezervace pomocí hvězdičky potvrzuje pouze rezervaci produktů, pokud je v objednávce prodej (SO).
potvrzeno a pokud je dostatečný počet produktů zahrnutých v SO k dispozici.

.. viz také:
:doc:`O rezervačních metodách <../reservation_methods>`

Konfigurace
=============

Chcete-li nastavit rezervační metodu na „Potvrzení“, přejděte do:
Konfigurace --> Typy operací. Pak vyberte požadovaný typ operace
konfigurovat nebo vytvořit nový kliknutím na „New“.

V sekci „Obecné“ na formuláři typu operace najděte „Způsob rezervace“.
pole a vyberte možnost „Při potvrzení“.

.. obrázek: at_confirmation/at-confirmation-operations-type.png
:align:center
:alt: pole rezervace na formuláři pro objednávku dodání.

Průběh práce
========

Chcete-li vidět metodu rezervace s potvrzením v akci, vytvořte novou rezervaci kliknutím na
:menu:Prodejní aplikace --> Nová.

V poli „Zákazník“ přidejte zákazníka. Pak v záložce „Částky objednávky“ klikněte
:guilabel:'Přidat produkt' a vyberte produkt, který chcete přidat do nabídky z roletky.
Nakonec v sloupci „Množství“ upravte požadované množství produktu k prodeji.

Jakmile bude objednávka připravena, klikněte na tlačítko „Potvrdit“.

Klikněte na ikonu „📈 (oblast graf)“ u produktové řady, abyste zjistili cenu produktu.
Nástroj „Dostupnost“, který odhaluje počet jednotek „Rezervovaných“ pro tuto
pořádku.

.. poznámka::
Pokud není dostatečné množství skladových zásob pro produkt zahrnutý v SO,
:guilabel:`📈 (oblastní graf)` ikona je červená místo zelené.

Výsledkem je místo zobrazení rezervovaného počtu jednotek pro objednávku zobrazení :guilabel:`Dostupnost`.
Nápověda zobrazuje text „K dispozici“ a ukazuje počet dostupných jednotek (např. 0 jednotek).

.. obrázek: at_confirmation/at-confirmation-availability-tooltip.png
:align:center
:alt: Potvrzená objednávka s vybraným nástrojem pro zobrazení dostupnosti produktu.

.. varování: Předpověď

Chcete-li zobrazit všechny faktory ovlivňující rezervaci produktu, klikněte na tlačítko „Zobrazit předpověď“.
klikněte na tento odkaz, abyste se dostali do panelu „Předpovědní zprávy“.

Řádek s názvem „Předpověď“ zobrazuje předpovědi o produktu (produktech), které jsou součástí
objednávka na prodej; tedy jakékoliv živé příjmy z produktu a všechny aktivní objednávky.
jsou uvedeny v sloupci „Použito“. Podívejte se, jak je každá objednávka vyřízena
:guilabel:`Dodávky“ sloupec.

Dále je na stránce vypočítána hodnota :guilabel:`Predikovaná`, která se počítá v horní části stránky
množství „Na ruce“ a „Příchozí“, a odečtete
:guilabel:`Výchozí“ množství, jak je uvedeno níže:

.. obrázek::at_confirmation/at-confirmation-forecasted-equation.png
:srovnání: do středu
:alt: Výpočet předpokládaného množství z stránky Předpovědní zprávy.

Pokud má být jedna objednávka přednostně vyřízena před jinou objednávkou, klikněte na tlačítko :guilabel:`Unreserve`.
odpovídající řádek v sloupci „Dodání“.

Pro dodání produktů klikněte na tlačítko „Dodání“ v horní části objednávky.
formulář. Pro potvrzení, že rezervace proběhla v pořádku, zkontrolujte, zda je ve :guilabel:`Produkt
V poli „Dostupnost“ je uvedeno „K dispozici“ (v zeleném písmu) a čísla v poli „Požadavky“
Sloupce „Množství“ odpovídají (v tomto případě by měly oba sloupce ukazovat hodnotu 100,00).

.. obrázek:at_confirmation/at-confirmation-delivery-order.png
:align:center
:alt:Dodací list pro produkt zahrnutý v objednávce s potvrzením rezervace.

Jakmile bude vše připraveno, klikněte na tlačítko „Zkontrolovat“.

.. viz také:
   - :doc:`Rezervace ručně <manually>`
   - :doc:`Před plánovaným termínem rezervace <before_scheduled_date>`
