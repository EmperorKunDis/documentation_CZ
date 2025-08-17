=================
Podlahy a stoly
=================

V **Pohledu na plán restaurace** můžete spravovat podlaží a uspořádání stolů a sledovat
stav stolu v reálném čase – včetně obsazenosti, rezervací a objednávek kuchyně.

.. obrázek:: podlahy_stoly/plán-pochopit.png
:alt: příklad pohledu na půdorys s vizuálními klíči pro jeho porozumění.
:skalka: 90 %

- Stůl číslo 101 je volný nyní, ale rezervován na 15:00.
- Stůl 102: Objednávka byla potvrzena a odeslána do kuchyně.
- Stůl číslo 103: Stůl byl rezervován na 12 hodin, ale zákazníci jsou pozdě.
- Tabulka 104: Dva předměty čekají na odeslání do kuchyně.
- Stůl číslo 105 je volný.

Konfigurace
=============

Z POS back-endu
--------------------

Pro vytvoření podlahy a stolů zadní části, přejděte na: „Systém prodeje - Konfigurace
→Plány podlaží“ a klikněte na „Nový“, abyste vytvořili plán podlaží. Volitelně aktivujte další
nastavení kliknutím na ikonu „OI Settings“ („Nastavení OI“) . Poté

#Zadejte název podlaží.
#Vyberte související položku „Prodejní místo“.
#. Přejděte myší nad místo pro obrázek a klikněte na ikonu „Penál“ (ikona „pencil“)
pozadí (např. uspořádání restaurace).
#Klikněte na tlačítko „Přidat řádek“ pro vytvoření tabulky a nastavení jejích parametrů:

   - Zadejte číslo stolu.
   - Vyplňte počet míst:guilabel:`Seats`.
   - Vyberte „Čtverec“ nebo „Kruh“.
   - Přidělte zdroj „Objednávka“ pomocí :guilabel:, aby se stůl dal rezervovat.
   - Upravte výšku, šířku a barvu.
#Klikněte na ikonu „smažení“ (ikona „odpadkový koš“).

.. obrázek: podlahy_stoly/přidat_podlahu_backend.png
:alt: okno pro vytvoření tabulky na pozadí

..tip:
Vytvořte podlahy na místě: přejděte do nastavení terminálu, zadejte své
jméno podlaží v poli „Podlahy“ sekce „Mapa podlah a stolů“,
Stiskněte klávesu Enter nebo klikněte na tlačítko „Vytvořit a upravit…“

... _podlažích, stolech a předních částech:

Z POS terminálu
----------------------

Pro vytvoření podlahy a stolu z předního konce: otevřete sezení POS:
ikonu „fa-bars“ (ikona „hamburger menu“) v pravém horním rohu a poté
:editplan:

#Přidejte podlaží kliknutím na ikonu „+“ (guilabel „plus“), pak zadejte název.
okno s možnostmi.
#Klikněte na ikonu „malířská štětka“ (zobrazí se ikona s nápisem „paintbrush“) a změňte barvu pozadí nebo
obrázek.
#Klikněte na ikonu „+“ vedle tabulky, abyste přidali novou tabulku.

Pro upravení konkrétní tabulky vyberte ji a klikněte na:

- Ikona „uživatel“ („user“) pro změnu počtu sedadel.
- :icon:`fa-square` (:guilabel:`square`) nebo :icon:`fa-circle` (:guilabel:`round`)
ikonu pro přepnutí tvaru z kruhu na čtverec a obráceně.
- Ikona „malířská štětec“ (ikona „paintbrush“) pro změnu barvy tabulky.
- Ikona „Penál s tužkou“ (rename) pro změnu čísla tabulky.
- Ikona „Kopírovat“ (zobrazená jako ikona „Duplikovat“) pro duplikaci tabulky.
- Ikona „koš“ (:guilabel:"koš") pro odstranění tabulky.

Po provedení všech potřebných úprav klikněte na tlačítko „Uložit“ nebo ikonu „fa-floppy-o“.
ikona pro ukládání ([:guilabel:`disketová mechanika`]).

.. obrázek: podlahy-stoly/upravit-plochu-v-předním-zobrazení.png
:alt: pohled na půdorys v režimu úprav.
:skalka: 85 %

.. varování:
Odstraňování stolu nebo podlahy nelze vrátit zpět.

.. _příjem/podlaží/stoly/převod:

Převod stolu
==============

Vyberte stůl, do kterého chcete zákazníky přesunout, pak klikněte na tlačítko „Akce“
:icon:`oi-arrow-right` :guilabel:`Převod/Sloučení“.

V pohledu plánu podlaží vyberte cílovou tabulku:

- Vyberte volný stůl, na který přenesete zákazníky a jejich objednávky.
- Vyberte obsazený stůl, ke kterému chcete připojit zákazníky a jejich objednávky.

.. viz též:
:doc:`/restaurace`
