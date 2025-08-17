===========================
Přidělení čísla výrobní série
===========================

Změna nastavení sledování produktů na používání čárových kódů nebo sériových čísel po uložení produktu
Odoo bez nich může vést k nesourodým záznamům. Podívejte se na tuto dokumentaci a dozvíte se, jak používat
úprava zásob, při které se přidělují čísla sérií nebo losů pro výrobky, které původně neměly
předměty dražby.

.. obrázek: přidělování/varování.png
:align:center
:alt:Varování: produkty skladem nemají číslo šarže.

.. poznámka::
Tento dokument popisuje proces použití dvou inventurních oprav: jedné k odstranění chybného
záznamy bez čísla šarže a další k uložení množství s číslem šarže.

.. viz též:
   - :doc:`Nastavit a používat čísla šarží <lots>`
   - :doc:`Používejte sériová čísla <sériové_číslo>“

Změňte množství na skladě na nulu
===============================

Chcete-li změnit nastavení produktu na sledování podle čísla šarže nebo sériového čísla, začněte tím, že se přesunete do
:menu-vyber->Skladové zásoby -> Zboží -> Zboží“ a vyberte požadovaný produkt.

Dále klikněte na tlačítko „Na skladě“ produktu a otevřete „Aktualizovat množství“.
stránka. V sloupci „Množství na skladě“ změňte hodnotu na nulu.

.. poznámka::
Pokud je produkt uložen na více místech, zkontrolujte celkovou skladovou zásobu.
**všechny** lokality je nula.

.. obrázek: přidělování/odstraňování kvant.png
:align:center
:alt:Zobrazte model Zásoby a vyznačte pole „Množství skladem“.

Nastavte sledovatelnost
===========================

Návrat do produktového tvaru (:menuselection:`Skladová aplikace --> Zboží --> Zboží`) a přepnutí na
kartě „Zásobník“. V části „Sledovatelnost“ změňte
Možnost „Sledování“ z možnosti „Žádné sledování“ na možnost „Početně“ nebo „Podle lotů“.
Jedinečný sériový číslo.

.. viz též:
:doc:`datum vypršení platnosti“

.. obrázek: přidělování/sledování.png
:align:center
:alt:Zapnout sériové číslo a šarže.

Nastavte množství na skladě
========================

Po ručním nastavení skladových zásob na nulu a změně nastavení „Sledování“
čísla nebo sériové číslo, obnovte množství kliknutím na tlačítko „Na skladě“
z požadované podoby výrobku.

Na stránce „Aktualizace množství“ protože předchozí zásoba byla změněna na
Nula, objeví se na stránce varování „No Stock On Hand“. Zde klikněte na
:guilabel:`New“ tlačítko v pravém horním rohu. To odhalí novou, upravitelnou čáru na
stránce „Aktualizace množství“ a poté zadejte požadovaný sériový číslo na stránce „Série / Sériové číslo“.
Zadejte pole „Číslo“ a přizpůsobte pole „Skladová zásoba“ původní hodnotě.

.. viz též:
:doc:`../sklady-a-uskladnani/inventarni-systemy/poctu-produktu`

.. obrázek: přidělit/aktualizovat množství.png
:align:center
:alt:Vyplňte pole „Číslo šarže“ a „Množství skladem“.

.. tip::
najít původní množství a upravit odpovídajícím způsobem :guilabel:`Množství skladem`.
přiřazením nového čísla nebo sériového čísla klikněte na ikonu :icon:`fa-pencil` :guilabel:`(pencil)`
položku „Množství na skladě“ a poté klikněte na ikonu „Historie“.
tlačítko na nejvzdálenějším místě.

.... obrázek: přidělení/nastavení.png
:align:center
:alt:Zobrazte tlačítko „Historie“ na stránce Změny zásob.

Změna zásoby, která změnila skladovou zásobu na nulu, je zobrazena v
:guilabel:`Množství“ pole.

.. obrázek:: přidělení/historie.png
:srovnání: střed
:alt:Zobrazit záznam v historii.
