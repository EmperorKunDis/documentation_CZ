==========================
Odpad při výrobě
==========================

.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`

Během výrobního procesu může být nutné odstranit součástky nebo hotové produkty
zboží je poškozené, vadné nebo již nevyužitelné.

Sledování odpadu pomáhá výrobcům sledovat odpady, identifikovat problémy v procesech a vést účetnictví.
na výrobní náklady.

V Odoo jsou odstraněné položky vyřazeny z fyzické evidence zásob a přesunuty do virtuální lokality nazývané
*Fiktivní umístění/Vykopávky*. Toto místo není fyzickým prostorem, je to způsob záznamu a sledování ztrát.
bez ovlivnění skutečných zásob.

.. viz též:
:doc:`Typy skladů <../../inventory/warehouses_storage/inventory_management>`

..tip:
Zadání na vyřazení lze zobrazit kliknutím na „Sklad --> Provoz --> Vyřazení“.
Každá objednávka na odpadky zobrazuje datum a čas vytvoření objednávky spolu s produktem a
množství, které bylo vyřazeno.

Pro zobrazení celkového množství každé položky vyřazené z provozu přejděte na:
Konfigurace --> Lokality“, pak odstraňte filtr „Vnitřní“ z
:guilabel:`Hledat ...“ lištu a zobrazí se všechny virtuální umístění. Vyberte si z seznamu
:guilabel:`Virtuální lokace/Skládka“.

... výroba/řízení/odpadní okno:

Přejděte do okna s odpadem
============================

Smazání může být provedeno v aplikaci Manufacturing nebo ve modulu Shop Floor, podle toho,
úkol.

Aplikace **Výroba** umožňuje:

- Vyřazení hotových výrobků (pouze pokud je stav |MO| v položce *Dokončeno*).
- Zrušení součástí (při stavu Draft nebo Confirmed).

**Pracovní plocha** umožňuje:

- Vyřazení pouze některých součástí.

Aplikace pro výrobu
-----------------

Pro odstranění produktu z aplikace Manufacturing přejděte na:
Operace --> Výrobní objednávky a vyberte požadovanou |MO|.

Na stránce MO klikněte na ikonu „Akce“ (ikona „fa-cog“) a poté vyberte možnost „Vymazat“.
záložky.

.. obrázek: scrapyard-production/gear.png
:alt:MO s rozbaleným menu kola, aby se zobrazila možnost Skládka.

Prodejní plocha
----------

Ve **Shop Flooru** lze zlikvidovat pouze součástky. Otevřete požadovanou kartu |MO| a pak stiskněte
ikonu „fa-cog“ a v okně „Co chcete udělat?“.
okno, vyberte: guilabel: „Vyřazení“.

.. obrázek: scrapyard/shop-floor.png
:alt:Pop-up okno v aplikaci Shop Floor.

Pop-up okno s odpadky
===================

Po otevření okna „Odpad“ pomocí jedné z metod :ref:`podrobněji
nad výrobou / řízením / odpadním oknem“, vyberte součást nebo hotový produkt, který
odstraněny ze seznamu produktů z nabídky „Produkty“.

Do pole „Množství“ zadejte množství odstraněného materiálu.

Výchozí hodnotou pole „Zdroj“ je umístění předprodukce skladu.
Když je pole „Scrap Location“ nastaveno na „Virtuální umístění / Scrapy“,
umístění. Pokud má být zdroj nebo skládka změněna, vyberte jinou lokalitu z
jejich příslušných rozbalovacích nabídek.

Zaškrtněte políčko „Dodat množství vyřazené z výroby“
vyměnit součástku, která byla zrušena poté, co bude potvrzena objednávka na její likvidaci. Tato možnost by měla být
povoleno pro sklady s dvoufázovým výrobním procesem:
Třístupňové výrobní procesy povoleny, protože komponenty
nejsou vybírány jako součást výrobního procesu „jedním krokem“
proces.

.. obrázek: scrapyard/scrap-window.png
:alt:Pop-up okno s náhledem na odpadkový koš.

Po vyplnění okna „Sekundární suroviny“ klikněte na „Sekundární suroviny“.
tlačítko. Po vytvoření jednoho nebo více odpadových objednávek se zobrazí chytré tlačítko „Odpadky“.
v horní části obrazovky. Klikněte na něj, abyste zobrazili seznam všech objednávek na skládku pro |MO|.
