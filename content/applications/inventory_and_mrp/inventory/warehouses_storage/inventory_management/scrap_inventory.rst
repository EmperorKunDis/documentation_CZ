===============
Skládka odpadu
===============

.. |SP| nahradit za: zkratka: SP (Skladovací objednávka)
.. |SPs| nahradí: zkratka: `SPs (Scrap Orders)`

Někdy se může stát, že zboží v skladu společnosti bude poškozené nebo nefunkční.
smyslu opravitelnosti. Pokud není možné zboží opravit nebo vrátit zpět
prodejce, může být zlikvidován.

Odoo *Sklad* umožňuje uživatelům zlikvidovat zásoby a označit zboží nebo materiál, který již není potřeba.
použitelné nebo prodejné k likvidaci (nebo recyklaci).

Odstranění zásob z databáze pomáhá udržet skladové zásoby přesné, protože odstraňuje produkty, které byly vyřazeny
fyzického skladu a umístění ji do virtuální skládky (*Virtuální lokality/Skartování*).

.. poznámka::
*Virtuální lokality* v Odoo nejsou skutečnými fyzickými prostory ve skladu. Spíše jde o
určená místa v databázi, která poskytují sledování položek, které se nemají započítat do
fyzická inventura.

Pro více informací o virtuálních lokalitách se podívejte na dokumentaci k různým typům
:ref:`druhy skladů <inventar/lagerorte/lagerort-typ>“.

Zbytky z výroby
================

Pro vytvoření nového odpadového příkazu (SP) pro zboží skladem přejděte na:
-->Operace --> Skládka“ a klikněte na „Nový“. To otevře nové okno.

Klikněte na rozbalovací nabídku v poli „Produkt“ a vyberte produkt, který má být
vyřazen z evidence. V poli „Množství“ změňte hodnotu na množství skladového zásobníku
produkt, který má být zrušen (výchozí hodnota je 1,00).

.. obrázek: scrapyard/scrapyard-new-scrap-order.png
:align:center
:alt:Vyplnil nový formulář pro objednávku odpadu s podrobnostmi o produktu.

Výchozí hodnota položky „Zdroj“ je umístění, kde se produkt v současné době nachází.
Výchozí hodnota položky „Odpadová lokalita“ je určená odpadová lokalita („virtuální
Místo/Šrot“. Můžete změnit místo nebo šrot vybráním jiného místa.
jejich příslušné nabídky.

Pokud se odpisy váží k určitému konkrétnímu úkonu, uveďte tento úkon v
:guilabel:`Zdrojový dokument“ pole.

V poli „Společnost“ se zobrazuje společnost, ke které patří tento produkt. Pokud
Pravidlo doplňování je nastaveno pro produkt, který se vyřazuje a pokud by měl být
doplněny, zaškrtněte políčko pro „Doplnit množství“.

Jakmile je připraveno, klikněte na tlačítko „Zkontrolovat“ pro dokončení nového |SP|.
Na horní části formuláře se objeví tlačítko „Produkt pohybuje“. Klikněte na tlačítko,
zobrazit podrobnosti o odstranění skládky.

.. obrázek: scrape_inventory/scrape-inventory-product-moves-button.png
:align:center
:alt:Tlačítko Smart Move se objeví na nové objednávce odpadu.

..tip:
Pro zobrazení celkového množství odstraněných položek přejděte na:
app --> Konfigurace --> Lokality. Klikněte na tlačítko „x (smazat)“ v
:guilabel:`Vnitřní filtr“ v nabídce „Hledat…“, abyste zobrazili virtuální polohy.

Vyberte virtuální umístění „Scrap“.
formulář, klikněte na tlačítko „Aktuální zásoba“ ve formuláři nahoře.

Seznam všech zrušených produktů a jejich množství je zobrazen.

...... obrázek: scrapyard/inventory/scrap-inventory-current-stock.png
:srovnání: do středu
:alt:Aktuální seznam všech zlikvidovaných produktů v virtuálním skladišti.

Odpad z již existujícího provozu
================================

Skladové objednávky (SP) lze vytvářet také z již existujících operací, jako jsou například faktury nebo dodání.
objednávky a vnitřní převody předtím, než jsou zaregistrovány nebo odebrány ze skladu.
operace.

Zrušit produkt během operace, přejděte do aplikace „Sklad“.
Klikněte na tlačítko „Přidat do seznamu“ v přehledu zásob.
kartu úkolu (tj. kartu s názvem „Pokladní doklady“).

.. obrázek: scrapyard/scrapyard-invoices-task-card.png
:align:center
:alt: Tlačítko „Zpracovat“ na kartě úkolu „Přijaté faktury“ v přehledu zásob.

Poté vyberte operaci zpracování z výsledného seznamu stávajících objednávek. To vám umožní otevřít
formě operace.

Klikněte na ikonu „fa-cog“ (kolečko) a vyberte možnost „Vymazat“.
příkazovém řádku. To otevře okno s názvem „Zbytky výroby“.

.. obrázek: scrapyard/scrapyard-popup-window.png
:align:center
:alt:Pop-up okno pro výrobní formu Scrap Products.

V tomto okně zvolte ze seznamu v poli „Produkt“ možnost
výrobky z operace, které by měly být odstraněny. Upravte hodnotu v poli:guilabel:`Množství`.
pokud je třeba.

Pokud je vybraný produkt sledován pomocí čísla šarže nebo lístku,
V poli „Lot/Sériové číslo“ se zobrazí pole pro zadání sledovacího čísla.

Zdrojová a odpadní místa lze změnit, pokud je potřeba. Pokud
Pravidlo doplňování je nastaveno pro produkt, který se vyřazuje a pokud by měl být
doplněny, zaškrtněte políčko pro „Doplnit množství“.

Jakmile je hotovo, klikněte na „Odpadní produkty“. V horní části se objeví tlačítko „Suroviny“
z operace. Klikněte na tento chytrý tlačítko, abyste zobrazili podrobnosti všech odřezů vytvořených z
Tato konkrétní operace.

.. obrázek: scrapyard/scrapyard-scraps-smart-button.png
:align:center
:alt: Chytrý tlačítko s náhledem všech odpadových objednávek z provozu.
