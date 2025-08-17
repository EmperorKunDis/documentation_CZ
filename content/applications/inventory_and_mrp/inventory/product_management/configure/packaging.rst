=========
Obaly
=========

.. |upravit| nahradit:: :ikonka:`oi-settings-adjust` :guilabel:`(doplňkové možnosti)`

V Odoo *Sklad* je slovo „balení“ používáno pro jednorázové obaly, které obsahují více jednotek
Konkrétní produkt.

Příkladem mohou být různé balení plechovek limonády, např. šestikus, dvanáctikus nebo karton se 36 lahvemi.
musí být vyplněna na jednotlivých produktových formulářích, protože obaly jsou považovány za
Specifické, nikoli obecné.

.. tip::
Krabice lze použít v kombinaci s Odoo: doc: `Čárový kód <../../../barcode/setup/software>`.
Při přijímání produktů od dodavatelů se při skenování štítku automaticky přidává
počet jednotek v obalu k vnitřnímu počtu produktu.

Konfigurace
=============

Pro používání obalů přejděte na: „Inventář aplikace - Konfigurace - Nastavení“. Pak
V sekci „Produkty“ zapněte funkci „Obaly produktů“,
:guilabel:`Uložit“.

.. obrázek: balení/zapnout-balení.png
:align:center
:alt:Zapněte balení výrobku kliknutím na „Balíčky produktů“.

...Inventarizace, správa produktů, nastavení obalů:

Vytvořit obal
================

Balení lze vytvářet přímo na produktové kartě nebo z ní.
stránka.

Z produktové podoby
-----------------

Vytvořte obaly produktu pomocí tlačítka „Inventář aplikace“ - „Produkty“ -
Produkty“ a vyberte požadovaný produkt.

V záložce „Sklad“ v dolní části sekce „Balení“ klikněte na
Přidejte řádek. V tabulce vyplňte následující pole:

- :guilabel:`Obal“ (vyžadováno): název obalu, který se zobrazuje na objednávkách prodejů/nákupů.
možnost balení produktu.
- :guilabel:`Obsah balení“ (povinné): množství produktu v obalu.
- :guilabel:`Jednotka měření` (povinné): jednotka pro kvantifikaci produktu.
- :guilabel:`Prodejní objednávky“: zaškrtněte tuto možnost pro balení určená k použití na prodejních objednávkách.
- :guilabel:`Nákupní objednávka“: zaškrtněte tuto možnost pro balení určená k použití na nákupních objednávkách.

.. poznámka::
Přejděte dolů na tabulku „Balení“ a zobrazte další pole kliknutím na ikonu „upravit“.
doleva od názvů sloupců v části „Balení“ a vybrat
z nabídky, která se objeví.

- :guilabel:Čárový kód: identifikátor pro sledování balení při pohybu skladových zásob nebo vyskladňování, pomocí
:ref:`Čárový kód <barcode/operations/intro>`. Nechte prázdné, pokud není používán.
- :guilabel:`Společnost`: ukazuje, že balení je k dispozici pouze v vybrané společnosti.
aby byl obal k dispozici ve všech společnostech.

.. příklad::
Chcete-li vytvořit obalový typ pro šest jednotek produktu „Grape Soda“, začněte kliknutím
:guilabel:"Přidejte řádek". V řádku pojmenujte :guilabel:"Sestava" "šestičlennou sestavu" a nastavte
:guilabel:`Obsah“ na „6“. Opakujte tento proces pro další balení.

.. obrázek: balení/vytvořit-obal-produktu.png
:align:center
:alt: Vytvořit šestihrannou krabici pro produkt.

Z produktových obalů
----------------------------

Pro zobrazení všech vytvořených obalů přejděte na: „Inventář aplikace --> Konfigurace
--> Obaly výrobků. To odhalí stránku „Obaly výrobků“ s kompletním
seznam všech vytvořených obalů pro všechny produkty. Vytvořit nový obal kliknutím
:label:Nový.

.. příklad::
Dva produkty limonády „Grape Soda“ a „Diet Coke“ mají tři typy balení konfigurované.
stránce „Balení výrobků“, každý produkt může být prodáván jako balení „6-Pack“ s obsahem 6
produkty jako „12-pack“ s 12 produkty nebo jako „case“ se 32 produkty.

.. obrázek: balení/balení.png
:align:center
:alt: Seznam různých obalů výrobků.

Částečná rezervace
-------------------

Po dokončení nastavení balení (viz inventory/product_management/packaging-setup)
balení lze rezervovat v plném nebo částečném množství pro odesílání zásilek. Částečné balení
Flexibilita zrychluje plnění objednávek tím, že umožňuje okamžitou dodávku dostupných položek.
Čeká na zbytek.

Pro konfiguraci rezervace balení přejděte do: „Inventář aplikace --> Konfigurace
Pak klikněte na „Nový“ nebo vyberte požadovanou kategorii produktů.

V sekci Logistika v kategorii produktu je možné zadat rezervní obaly.
Může být nastaven na „Rezervace pouze celých balení“ nebo „Rezervace částečných balení“.

.. důležité::
Zobrazit pole „Rezervní balení“ lze pomocí funkce „Balení výrobku“.
Tato funkce **musí být zapnutá**. Chcete-li tuto funkci zapnout, přejděte na :menuselection:`Inventář aplikací -->
Konfigurace --> Nastavení“, posuňte se do části „Produkty“ a zaškrtněte
zaškrtněte políčko „Obaly výrobku“ a klikněte na „Uložit“.

.. obrázek:balení/rezervní_obal.png
:align:center
:alt:Zobrazit pole Rezervní obal na stránce kategorie produktu.

.. příklad::
Aby bylo možné lépe posoudit různé varianty podle obchodních potřeb, je vhodné se podívat na následující příklad:

   - Na balení je dvanáct kusů.
   - Dodání dvou balení.
   - Je jich k dispozici pouze dvacet dva.

Když je vybrána možnost „Rezervace pouze plných balení“, jsou rezervována pouze dvanáct kusů.
pořádku.

Naopak při výběru položky „Částečné balení v rezervě“ je vybráno dvacet dva jednotek.
vyhrazené pro objednávku.

Aplikovat obaly
================

Při vytváření objednávky prodeje v aplikaci „Prodej“ zadejte balení, která mají být
použité pro výrobek. Vybraná obalová forma se zobrazuje na :abbr:`SO (objednávka na prodej)` pod
:guilabel:„Obal“ pole.

.. příklad::
Do tří šestipacků se vejde celkem 18 plechovek s nápojem „Grape Soda“.

.... obrázek: balení/objednávka_balení.png
:align:center
:alt:Přiřaďte balení na lince prodejního objednávkového dokladu.

.. inventář / řízení produktů / balení:

Dopravní trasy pro balení
====================

Při přijímání balení se vždy automaticky řídí nastavenou cestou přijetí skladu.
<../../shipping_receiving/daily_operations>“. Volitelně lze nastavit trasu pro balení.
Přejděte na: menu: „Skladová aplikace“ - „Nastavení“ - „Trasy“.

.. důležité::
Funkce „Produktové balení“, „Uložiště“ a „Multistopové trasy“ (naleznete v nabídce)
musí být aktivována položka „Nastavení“ (v menu „Aplikace inventáře --> Konfigurace --> Nastavení“).
zachráněny.

.. viz též:
:doc:`../pravidelné operace/denní provoz/využívat trasy“

Vytvořit trasu
------------

Na stránce „Trasy“ klikněte na „Nový“, nebo vyberte trasu, která není určena pro
skladu. Následně v sekci „Použitelné na“ zaškrtněte políčko „Obaly“.

.. obrázek: balení/trasa.png
:align:center
:alt: Vytvořit trasu pro balení.

Trasu s vybranými „Balíčky“, bez „Produktů“ a „Skladů“.

... inventář/správa produktů/balení s trasou:

Aplikace trasy na obalu
------------------------

Poté přejděte do sekce „Nástroje“ a klikněte na „Vybrat cestu“.
produkt, který používá obal.

V produktové podobě přepněte na záložku „Sklad“ a v sekci „Balení“
obsahující konfigurované balení, klikněte na
Změňte ikonu na „Upravit“. Zaškrtněte políčko „Trasy“ a zobrazí se sloupec v
:guilabel:Tabulka balení.

V poli „Trasy“ vyberte balení specifickou trasu. Opakujte tyto kroky pro všechny
obal, který má sloužit k používání této trasy.

.. obrázek: balení/použití trasy.png
:align:center
:alt:Nastavit trasu na obalu.

