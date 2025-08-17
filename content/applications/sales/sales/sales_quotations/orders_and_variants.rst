===============================================
Varianty produktů v cenových nabídkách a objednávkách
===============================================

Předtím, než se podíváme na to, jak používat varianty produktů v cenových nabídkách a objednávkách, je
doporučuje se seznámit se s :doc:`../products_prices/products/variants` v Odoo.

Jakmile se seznámíte s základy kolem variant produktů, následující obsahuje informace o tom, jak
Varianty lze přidávat do objednávek a faktur pomocí konfigurátoru produktů nebo rozbalovacího seznamu.
entry*

.. poznámka::
Je nutné poznamenat, že nastavení je označeno jako „Vstup do sítě Variant Grid“ v aplikaci Nastavení.
Stránku a nazvali ji „Vstup do sítě“. Takže si dejte pozor na to.

Nastavení
========

Při práci s variantami produktů používá Odoo výchozí konfigurátor produktu.
možnost vstupu do sítě, která je **nutná** pro aplikaci Odoo Sales.
Varianta vstupu do sítě nabízí okno na citaci/objednávku, aby se zjednodušila
výběr variant.

Chcete-li tuto možnost zapnout, přejděte na: „Prodejní aplikace --> Konfigurace --> Nastavení“ a posuňte
do sekce „Katalog produktů“. Poté zaškrtněte políčko vedle „Svislý seznam variant“
Možnost „Přidat“ a klikněte na „Uložit“.

.. obrázek: objednávky_a_varianty/soubor-výpisu-objednávky.png
:align:center
:alt:Nastavení sítě v aplikaci Odoo Sales.

.. poznámka::
Samozřejmě musí být aktivována i funkce Varianty.
varianty na citace a objednávky.

Konfigurace produktu
=====================

Jakmile je zapnuté nastavení „Variantní vstup do sítě“, oba možnosti (konfigurátor produktů a
*Přístup do sítě obchodů*) se stane dostupným na každém produktu.

Pro konfiguraci produktu použijte buď produktový konfigurátor nebo rozbalovací seznam variant.
Navigace na:menu-selection:'Sales app --> Products --> Products' pro zobrazení všech produktů v
databáze.

Pak vyberte požadovaný produkt pro konfiguraci nebo klikněte na „Nový“, abyste vytvořili nový produkt.
od začátku. Jakmile je produkt ve formě, klikněte do záložky „Attributy a varianty“, kde
Varianty produktů lze zobrazit, upravovat a přidávat.

Na spodní části záložky „Vlastnosti & varianty“ je záložka „Prodejní varianta“.
Sekce „Výběr“ s dvěma možnostmi: „Konfigurátor produktů“ a „Řádkový výpis objednávek“.
Vstup“.

.. poznámka::
Je třeba poznamenat, že tyto možnosti se zobrazí pouze v případě, že alespoň dvě hodnoty atributu
Byla přidána do záznamu.

.. obrázek: objednávky_a_varianty/atributy-varianty-karta-vybrané-možnosti.png
:align:center
:alt: Výběr prodejních variant na záložce atributy a varianty v kartě produktu.

Tyto možnosti určují, jaký způsob se používá při přidávání variant produktu do nabídek nebo prodeje.
objednávek.

:guilabel:Produktový konfigurátor poskytuje okno s přehledným zobrazením všech dostupných
varianty produktu pro daný produkt při přidání do nabídky.
Varianta může být vybrána/přidána v libovolném okamžiku.

Tlačítko „Přidat do košíku“ poskytuje stejné informace jako tlačítko „Dodací lhůta“.
Konfigurátor v tabulkovém uspořádání, který umožňuje uživateli vybrat větší počet jedinečných produktů.
varianty a přidat je do cenové nabídky nebo objednávky v jednom pohledu.

Konfigurátor produktů
====================

Funkce konfigurátoru produktu se zobrazuje jako okno „Nastavit“ po stisknutí tlačítka
Produkt s variantami se přidá do nabídky nebo objednávky, ale pouze v případě, že
Vyberte možnost „Konfigurátor produktů“ na formuláři produktu.

.. obrázek: objednavky_a_varianty/produkt-konfigurátor-okno.png
:align:center
:alt:Pop-up okno konfigurátoru produktu, které se zobrazí při citaci nebo objednávce.

.. poznámka::
Toto okno „Nastavení“ se také zobrazí, pokud je nastavení „Vstup do sestavy objednávek“
je **neaktivní**, protože je výchozí volbou používanou systémem Odoo při práci s variantami produktů.
citace a/nebo objednávky na prodej.

Možnost „Konfigurátor produktů“ umožňuje obchodníkům vybrat přesně tu variantu produktu,
přidat do citační nebo objednávky formou, podobnou internetovému nákupu.

Vstup do sítě
================

Funkce „Vložení řádku objednávky“ se zobrazí jako okno s názvem „Zvolte varianty produktu“, jakmile
Jako produkt s alespoň dvěma variantami se přidává do cenové nabídky nebo objednávky na prodej, ale pouze v případě, že
Výrobní formulář produktu obsahuje možnost „Přidání do seznamu objednávek“.

.. obrázek: objednani_a_varianty/vyberte_produktove_varianty_popup.png
:align:center
:alt:Okno s výběrem variant produktu, které se zobrazí při vytváření nabídky v Odoo.

Pop-up okno „Vybrat varianty produktu“ zobrazuje všechny varianty pro tento
určitého produktu. Z této okna obchodník může určit počet kusů každé varianty
Chtěli by přidat k citaci nebo objednávce hned.

Po výběru všech požadovaných množství a variant stačí obchodník jednoduše kliknout
:guilabel:'Potvrdit' a tyto objednávky jsou okamžitě přidány do cenové nabídky/objednávky.
:guilabel:„Řádky objednávek“ kartě.

.. obrázek: objednávky a varianty/soupis_v_detailu_objednávky.png
:align:center
:alt:Vyplněná záložka s řádky objednávky po výběru řádku v seznamu objednávek slouží k výběru produktů.

.. viz též:
:doc:`../produkty-cena/produkty/varianty`
