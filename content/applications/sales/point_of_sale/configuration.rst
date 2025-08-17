Zobrazit obsah
:ukázat obsah:

=============
Konfigurace
=============

.. konfigurace/nastavení:

Přejděte do nastavení POS.
=======================

Pro přístup k obecným nastavením POS se přihlaste do:
Nastavení“. Pak otevřete rozbalovací nabídku v poli „Prodejní místo“ a vyberte prodejní místo.
konfigurovat.

.. obrázek: konfigurace/vyber-pozice-v-rozehrávce.png
:alt: Rozbalovací nabídka pro výběr POS v nastavení aplikace

.. poznámka::
Tyto nastavení jsou dostupná uživatelům s právy na přístup k :doc:`aplikacím a funkcím </applications/general/users>
:guilabel:`Administrace“ nastavit jako :guilabel:`Nastavení“.

Některé nastavení lze také upravit přímo z hlavního panelu kliknutím na tlačítko vertikální elipsy.
(:guilabel:'⋮') na platební kartě. Kliknutím se otevře okno s možnostmi:

- :doc:`Povolit více zaměstnancům přihlásit se. <employee_login>`
- :doc:`Připojte a nastavte systém Internetu věcí. <konfigurace/pos_iot>`
- :doc:`Připojte a nastavte tiskárnu pro EET. <konfigurace/epos_ssc>`

.. obrázek: konfigurace/vypnuto-zapnuto.png
:alt: okno pro rychlé nastavení v POS

.. poznámka::
Tyto nastavení jsou dostupná uživatelům s právy na přístup k :doc:`aplikacím a funkcím </applications/general/users>
:guilabel:`Prodejní místo“ nastavené jako „Administrátor“.

Zboží musí být dostupné
=======================

Prodávat produkty.

#Přejděte na: „Prodejní místo“ - „Produkty“ - „Produkty“.
#Vyberte produkt, abyste otevřeli formulář produktu.
#Zaškrtněte políčko „Prodejní místo“ na horním konci formuláře.

.. obrázek: konfigurace/dostupnost-pracovních-míst.png
:alt:Dostupnost produktu na vašem prodejním místě.

Kategorie produktů PoS
======================

Konfigurace
-------------

Kategorie produktů POS umožňují uživatelům třídit produkty a získat tak stručnější a čistší přehled.
POS terminál.

Pro správu kategorií PoS přejděte na: `menuselection:Pointe of Sale --> Konfigurace --> Produkty PoS
Kategorie. Chcete-li přidat novou kategorii, klikněte na tlačítko „Vytvořit“. Pak ji pojmenujte v
:guilabel:`Kategorie jméno pole`.

K přiřazení kategorie ke své nadkategorii vyplňte pole „Nadkategorie“.
Hlavní kategorie obsahuje jednu nebo více podkategorií.

Příklad:
.... obrázek: konfigurace/kategorie_rodiče.png
:alt:Produktové kategorie PoS seskupené podle rodičovských kategorií

Přiřaďte kategorie produktů PoS
-----------------------------

Přejděte na: „Prodejní místo“ - „Produkty“ - „Produkty“ a otevřete formulář produktu. Poté přejděte na
v záložce „Prodejní místo“ a do pole „Kategorie“ pod
sekci „Prodejní místo“ s jednou nebo více kategoriemi prodejních míst.

.. obrázek: konfigurace/form-pos-kategorie.png
:alt:Karta prodejního místa v produktové kartě, kde se přidává kategorie prodejního místa

Omezte kategorie
-------------------

Můžete omezit kategorie zobrazované na vašem POS rozhraní. Pro dosažení tohoto cíle přejděte do svého :ref:`POS
Nastavení (konfigurace/nastavení) a zvolte konkrétní kategorie, které chcete zobrazit v
V poli „Omezení kategorií“ v sekci „Produkt a POS“.

.. obrázek: konfigurace/omezení-kategorie.png
:alt:Nastavení, které nastavuje funkci omezeného kategorií

.. toctree::


konfigurace/pos_iot
konfigurace/epos_tiskárny
konfigurace/https
konfigurace/epos_ssc
