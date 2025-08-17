==============
Produktové kombinace
==============

Funkce **Produktové kombinace** umožňuje uživatelům definovat a spravovat možnosti kombinačních variant pro jednotlivé produkty.
produkt.

V kontextu restaurace umožňuje uživatelům vytvářet více možnostní menu.
Příkladem je to, že uživatel může definovat hlavní jídlo a specifikovat různé možnosti příloh, nápojů nebo dezertů.
K hlavnímu jídlu.

V maloobchodě tato funkce umožňuje vytvořit sadu produktů se více možnostmi výběru.
kombinovat.

Konfigurace
=============

Nejprve musíte vytvořit kombinované volby. Chcete-li tak učinit:

#Přejděte na: „Místo prodeje“ -> „Produkty“ -> „Kombinace produktů“ a klikněte na „Nový“.
#Název kombinace a produkty, které chcete, aby si zákazníci vybrali, přidejte kliknutím na tlačítko „Přidat“:
„cena za linii“. Můžete také zahrnout do ceny každé možnosti další cenu v poli „Doplňková cena“
sloupec.

.. poznámka::
Pro porovnání je uvedena cena výrobku v původní verzi.
Cenová kolonka.

.. obrázek: combos/combo-form.png
:skalka: 75 %

Dále je potřeba vytvořit konkrétní produkt pro shromáždění možností kombinací. K tomu:

#Přejděte do sekce „Prodejní místo“ – „Produkty“ – „Produkty“ a klikněte na „Nový“.
#Nastavte pole „Produktová kategorie“ na „Kombinace“ a vyplňte pole „Obecné informace“.
Informace" záložka.

....... poznámka::
Prodejní cena kombinovaného výrobku je pevná a není závislá na individuálních cenách.
zahrnutých položek nebo počtu položek v balíčku. Cena kombinovaného produktu se může lišit
zahrnuté v ceně, která je volitelně definována při vytváření kombinace nebo pokud se jedná o
Jedna věc má stanovenou zvláštní cenu.
#Přejděte na kartu „Volby kombinací“, klikněte na „Přidat řádek“ a vyberte
kombinaci přidat. Můžete také vytvořit novou kombinaci na této stránce kliknutím
:guilabel:`Nový“ v okně přehledu.

.. obrázek: combos/combo-product-form.png
:skalka: 75 %

Jakmile vytvoříte a přidáte do produktu kombinace možností, můžete prodávat kombinace ve svém obchodě.
obchod nebo restaurace.

Praktické využití
=====================

Otevřete sezení POS (<pos/session-start>) a vyberte kombinovaný produkt. Vyberte možnosti a
Klikněte na „Přidat do objednávky“. Příplatek se zobrazí pod souvisejícími volbami.

.. obrázek: combos/combo-select.png
:skalka: 75 %
