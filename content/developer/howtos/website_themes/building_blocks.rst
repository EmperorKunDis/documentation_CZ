===============
Stavební bloky
===============

Bloky jsou také známé jako šablony a slouží k vytváření a uspořádávání stránek. Jsou důležité
XML prvky vašeho návrhu.

Stavební bloky jsou rozděleny do dvou typů:

#**Bloky struktury**: vizuálně používány jako „celé řádky“ a rozděleny do několika kategorií
(:gui-label:"Úvod", :gui-label:"Sloupce", :gui-label:"Obsah", :gui-label:"Obrázky",
:guilabel:`Lidé“, atd.)
#**Vnitřní obsahové bloky**: používají se uvnitř jiných bloků

Na konci této kapitoly budete umět vytvářet vlastní šablony.
<webové šablony/bloky/vlastní> a přidat je do vlastní kategorie.

..._webové_šablony/stavební_bloky/složka_souborů:

Struktura souborů
==============

Struktura souborů v tomto layoutu je následující.

::

názory
└── šablony
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
├─ s_snippet_name.xml

Struktura adresářů stylů je následující.

::

statické
└── src
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
├─────────────────────┴──────────────────────
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│           └── 000.scss
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

.. viz též:
„Šablony XML pro různé části
<https://github.com/odoo/odoo/blob/ccb78f7af2a4413836a969ff8009dc3df6c2df33/addons/website/views/snippets/snippets.xml>`_

.. varování: Demonstrační stránka

Pro přístup na tuto stránku je potřeba nainstalovat demo data:

   ::

      https://your-database.com/website/demo/snippets

... /webové-šablony/bloky/obsah:

Grafický návrh
======

Snippety lze upravit uživatelem pomocí Webového editoru. Některé třídy Bootstrapu jsou důležité jako
**spouští některé možnosti Webového editoru**.

... _webové šablony/stavební bloky/layout/obal:

Obal
-------

Standardní hlavní kontejner jakéhokoli kousku je „sekce“. Každý prvek sekce může být upraven jako
blok obsahu, který můžete přesunout nebo zkopírovat.

... blok kódu::xml

<část třídy s_snippet_name, která má název „…“ a obsahuje „…“>
<!--Obsah-->


Pro vnitřní obsah můžete použít jakýkoliv jiný značkovací jazyk HTML.

... blok kódu::xml

<div třída="s_snippet_name" data-name="..." data-snippet="...">
<!--Obsah-->


.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * -Atribut
     - Popis
   * – třída
     - Jedinečný název třídy pro tento kousek
   * 
     - Zobrazený v pravém panelu jako název snímku. Pokud není nalezen, bude se zobrazovat
*Blok*
   * 
     - Používá se systémem k identifikaci fragmentu

Systém automaticky přidává atributy „data-name“ a „data-snippet“ během přetahování.
na základě názvu šablony.

.. varování:
Tyto atributy by měly být přidány speciálně při vyhlášení snímku na stránce tématu.

.. varování:
Vyhněte se vkládání značky „section“ do jiné značky „section“, protože to vyvolá dvojnásobnou stránku.
Možnosti stavitele. Místo toho můžete použít vložené části obsahu.

..tip:
Pokud chcete psát obsah statické stránky pomocí standardních šablon, existují dvě možné cesty:

   - **Představte si vlastní statické stránky pomocí nástroje pro tvorbu webových stránek:** Přetáhněte a pusťte snímky, pak
kopírujte a vkládejte kód do souboru a udržujte jej čistý.

|  **NEBO**

   - **Všechno kódujte přímo:** Všimněte si však kompatibility s Webovým editorem.
Pro správnou funkci je zapotřebí určité třídy, názvy, ID, data atd. Doporučuje se vyhledat
vytáhnout kousky kódu, které vznikly ve standardním kódu v souborech zdrojového kódu Odoo.
Webový editor někdy přidává třídy do vložených kousků po jejich vložení na stránku.

... _webové šablony/stavební bloky/layout/prvek:

Elementy
--------

Na seznamu „vlastností“ je pak uvedeno, které z nich lze zapnout nebo vypnout pomocí konkrétních tříd CSS.

... _webové šablony/stavební bloky/layout/prvek velikosti:

Velikost
~~~~~~

Každá velká sloupcová sekce, která přímo vychází z prvku řádku (s ohledem na Bootstrap)
struktura) bude spuštěna webovým editorem, aby byly rezervovatelné.

... kódový blok:: CSS

.řádek > .kolonka s velikostí LG *

Přidejte do sloupců a sekcí přepážky.

... blok kódu::xml

class="pb80 pt80"

.. poznámka::

‚pb*‘ a ‚pt*‘ jsou třídy používané v Odoo k ovládání handlerů.
zvýšené na **mnohonásobek 8** až do maxima **256** (0, 8, 16, 24, 32, 40, 48, ...).

Zapněte výběr sloupců.

... blok kódu::xml

<div class="container s_allow_columns">

Zakázat možnost nastavení počtu sloupců.

... blok kódu::xml

<div třída="row" třída="s_nb_column_fixed">

Vypněte možnost velikosti pro všechny podřadé sloupce.

... blok kódu::xml

<div class="row s_col_no_resize">

Vypněte velikost pro jednu konkrétní sloupec.

... blok kódu::xml

<div class="col-lg-* s_col_no_resize">

... _webové šablony/stavební bloky/layout/prvek/barvy:

Barvy
~~~~~~

Přidejte pozadí založené na barevném schématu pro sloupce a tag <section>.

... blok kódu::xml

class="o_cc o_cc*"

Vypněte možnost pozadí pro všechny sloupce.

... blok kódu::xml

<div class="row s_col_no_bgcolor">

Vypněte možnost nastavení pozadí jedné konkrétní sloupce.

... blok kódu::xml

<div class="col-lg-* s_col_no_bgcolor">

Přidejte černý barevný filtr s průhledností 50 %.

... blok kódu::xml

<část>
<div class="o_we_bg_filter bg-black-50"/>
<div class="container">
<!--Obsah-->
</div>


Přidejte bílý filtr s průhledností 85 %.

... blok kódu::xml

<část>
<div třída="o_we_bg_filter" styl="zadní pozadí: bílá 85%"/>
<div class="container">
<!--Obsah-->
</div>


Přidejte vlastní barevný filtr.

... blok kódu::xml

<část>
<div třída="o_we_bg_filter" styl="zadní barva: RGB (39, 110, 114, 0.54) !důležité;"/>
<div class="container">
<!--Obsah-->
</div>


Přidejte vlastní filtr s gradientem.

... blok kódu::xml

<část>

<div class="container">
<!--Obsah-->
</div>


... /webové-šablony/bloky-stavebních-kostek/layout/prveků/vlastnosti:

Poznámky pod čarou
~~~~~~~~

... /webové-šablony/bloky/přednastavené-oblasti:

Nepravidelné oblasti
******************

Změňte prvek na neupravitelný.

... blok kódu::xml

<div class="o_not_editable">

Změňte neodstranitelný prvek.

... blok kódu::xml

<div class="oe_unremovable">

..._webové_šablony/stavební_bloky/předlohy/výplň:

Pozadí
***********

Přidejte pozadí a nastavte jej do středu.

... blok kódu::xml

<div třída="oe_img_bg" třída="o_bg_img_center" styl="zadní obrázek: url('...')">

Přidejte efekt paralaxy.

... blok kódu::xml


<span třída="s_parallax_bg oe_img_bg o_bg_img_center" styl="zadní pozadí: url('...'); zadní pozice: 50 %; 75 % "/>
<div class="container">
<!--Obsah-->
</div>


... update reference níže po vytvoření sekce médií (jak na to/webové šablony/média/video).

.. poznámka::

Příslušenství můžete nastavit na sekci. Podívejte se do kapitoly „:doc:`media`“ této dokumentace.

... _webové šablony/stavební bloky/layout/výrazné texty:

Text je zvýrazněn
***************

Textové zvýraznění je soubor SVG, který lze přidat na konkrétní slova nebo fráze a vyzdvihnout je. Textové zvýraznění nabízí možnosti nastavení barev a tloušťky.

.. obrázek: stavební_bloky/text-highlight.jpg
:alt: Příklad zvýrazněného textu
:šířka: 500

... blok kódu::xml


Titulek


zvýrazněný text
<svg fill="none" třída="o_text_highlight_svg o_content_no_merge pozice-absolutní přetékání nahoru dole 0 zahájení 0 šířka 100 výška 100 pe-none">
<!-- SVG cesta -->





.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 35 65

   * - vlastnost CSS
     - Popis
   * --text-highlight-width
     - Tloušťka hran SVG
   * --barva-vyznačení-textu
     - Barva objektu SVG

... _webové šablony/stavební bloky/layout/mřížka:

Síťový layout
-----------

Systém Grid Layout je silný a flexibilní systém pro uspořádání v CSS, který umožňuje uživatelům navrhovat složité
skládačky z kostek snadno.

.._webové šablony/stavební bloky/layout/řádkové použití:

Užívání
~~~

Zapněte rozložení sítě přidáním třídy CSS o_grid_mode na řádek. Počet řádků v
Váš řádek je definován atributem data-row-count. Vždy obsahuje 12 sloupců.
Vzdálenost mezi řádky, která je uvedena v atributu style, určuje mezery (nebo průlezy).
sloupy.

... blok kódu::xml


<!--Obsah-->


... /webové-šablony/bloky-stavebních-kostek/uspořádání/políčko:

Položky v mřížce
~~~~~~~~~~~~~~~

Přidejte položky do sítě pomocí třídy o_grid_item. Pokud obsahuje obrázek, použijte
třída „o_grid_item_image“.

... blok kódu::xml
:zvýrazněte-řádky: 2,3,4,5,6

<div class="row o_grid_mode" data-row-count="13">
<div třídy "o_grid_item" s vlastnostmi "g-height-*" a "g-col-lg-*" stylu "grid-area: 2 / 1 / 7 / 8; z-index: 3;">
<!--Obsah-->
</div>

<img src="..." alt="..." >
</div>


Rozměry a poloha prvku v mřížce jsou definovány oblastí mřížky, která lze přímo nastavit
v atributu style spolu s hodnotou z-index.

Třídy „g-height-*“ a „g-col-lg-*“ vytvářejí webový editor pro účely editaci.

... _webové šablony/stavební bloky/dispozice/odstupy mezi prvky v mřížce:

Vzdálenost mezi prvky sítě
~~~~~~~~~~~~~~~~~

... blok kódu::xml
:zvýrazněte-řádky: 2


<div class="o_grid_item g-height-* g-col-lg-*" style="--grid-item-padding-y: 20px; --grid-item-padding-x: 15px; grid-area: 2 / 1 / 7 / 8; z-index: 3;">
<!--Obsah-->
</div>


.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 35 65

   * - vlastnost CSS
     - Popis
   * -- `grid-item-padding-y`
     - Svislé vkládání (osová osa Y)
   * -- `grid-item-padding-x`
     - Horizontální vodítka (osová osu X)

... _webové šablony/stavební bloky/kompatibilita:

Systém kompatibility
====================

Pokud má kousek kódu atributy „data-vcss“, „data-vjs“ nebo „data-vxml“, znamená to, že je aktualizovaný.
verze, nikoliv originál.

... blok kódu::xml

<část třídy „s_snippet_name“ s atributem „data-vcss“ hodnotou „001“ a atributem „data-vxml“ hodnotou „001“ a atributem „data-js“ hodnotou „001“>
<!--Obsah-->


Tyto atributy dat ukazují systému, který verzi souboru má načíst pro daný
ukázka (např. soubor:file:`001.js`, soubor:file:`002.scss`).

..._webové šablony/stavební bloky/vlastní:

Vlastní kousek
==============

Některé specifické potřeby vyžadují vytvoření vlastních šablon. Tady je návod, jak vytvořit
vlastní kousek kódu

... webové šablony / stavební bloky / vlastní šablona:

Šablona
--------

Nejprve vytvořte šablonu snímku. Poté přidejte do seznamu a umožněte jejich zobrazení na webových stránkách.
Stavitel.

1. Prohlášení
~~~~~~~~~~~~~~

Nejprve vytvořte šablonu vlastního kousku:

... blok kódu::xml





<template id="s_airproof_snippet" name="...">

<!-- Obsah -->

</vzorce>



.. varování:
Atributy „data-name“ a „data-snippet“ musí být definovány při deklaraci snímku.
stránka s tématem. Jinak se vám webová stránka nebude správně zobrazovat a mohou nastat problémy.
se objeví při každém upgradu databáze. Dále si pamatujte, že atribut jméno
Je zobrazen jako název vašeho vlastního kusu skriptu v sekci „Bloky“ v nastavení.

..tip:
   - Používejte co nejvíce Bootstrapových vlastních tříd.
   - Přidejte před všechny vaše vlastní třídy příponu.
   - Používejte podtržené nízké písmeno k pojmenování tříd, např. .x_nav, .x_nav_item.
   - Vyhněte se používání atributu id uvnitř vašeho tagu section, protože může být zobrazeno více příkladů
na celé stránce (ID atribut musí být unikátní na stránce).

Přidejte vlastní kód do seznamu standardních kódů, takže uživatel může přetáhnout a vložit ho na
stránku přímo z editačního panelu.

2. Vytváření skupin
~~~~~~~~~~~~~~~~~

Přidejte skupinu na začátek seznamu (můžete ji umístit tam, kde potřebujete v tomto seznamu).

... blok kódu::xml
:komentář: „/webové stránky/zabrání-průvanu/výhledy/součásti/možnosti.xml“

<šablona id="snippety" dědí id="webová stránka.snippety" název="Airproof - Snippety">
<!-- Vytvoření skupiny -->
<xpath expr="//snippet[@id='snippet_groups']/*[1]" position="before">




.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * -Atribut
     - Popis
   * snippet-group
     - ID skupiny
   * – t-článek
     - Dědičný identifikátor šablony
   * - řetěz
     - Zobrazovaný název skupiny uživatelům
   * - miniatura
     - Cesta ke snímku skupiny

3. Přidání fragmentu
~~~~~~~~~~~~~~~~~~~

Poté přidejte vlastní šablonu do značky
všechny existující na stejné úrovni. Webový editor je automaticky rozdělí do
kategorie podle čtení atributu „group“ v tagu

... blok kódu::xml
:komentář: „/webové stránky/zabrání-průvanu/výhledy/součásti/možnosti.xml“
:zvýraznit-řádky: 7-12

<šablona id="snippety" dědí id="webová stránka.snippety" název="Airproof - Snippety">
<!-- Vytvoření skupiny -->
<xpath expr="//snippet[@id='snippet_groups']/*[1]" position="before">



<!--Přidejte vlastní šablonu do skupiny-->
<xpath expr="//snippet[@id='snippet_structure']/*[1]" position="before">
<t t-snippet="webová_vzduchotěsnost.s_vzduchotěsnost_snippet" string="Vlastní název" skupina="vzduchotěsnost">
<klíčová slova>Snippet</klíčová slova>
</t>



.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * -Atribut
     - Popis
   * – t-článek
     - Šablona pro vložení
   * - skupina
     - Skupina, do které se vložíte.
   * —
     - Klíčová slova, která uživatel zadá do vyhledávacího pole v panelu Snippet

Výňatek z obsahu
~~~~~~~~~~~~~~~~~~~~~

Chcete-li vytvořit vlastní kus textu, který se zobrazuje v seznamu „Vnitřní obsah“, přidejte jej do pole „snippet_content“
namísto:

... blok kódu::xml
:komentář: „/webové stránky/zabrání-průvanu/výhledy/součásti/možnosti.xml“

<šablona id="snippety" dědí id="webová stránka.snippety" název="Airproof - Snippety">
<!--Přidejte vlastní šablonu do skupiny-->
<xpath expr="//snippet[@id='snippet_content']/*[1]" position="before">
<t t-snippet="website_airproof.s_airproof_snippet" string="Vlastní sada" t-thumbnail="/website_airproof/static/src/img/wbuilder/s_airproof_snippet.svg" />



.. důležité:
   - Nezapomeňte přidat atribut t-thumbnail a odstranit atribut group, protože takové budovy
bloky je k dispozici přímo v pravém panelu nastavení webového editoru.
   - Nezapomeňte přidat šablonu do seznamu všech dostupných „Vnitřního obsahu“ šablon.
<webové_šablony/bloky/vlastní/možnosti/vnitřní obsah>.

..._webové_šablony/stavební_bloky/vlastní/možnosti:

Možnosti
-------

Možnosti umožňují uživatelům upravit vzhled a chování kousku pomocí Webové stránky. Můžete vytvořit
Možnosti vložení fragmentů jsou snadno dostupné a automaticky přidávají do editoru webových stránek.

.. viz též:
`Standardní možnosti vložených kusů textu <https://github.com/odoo/odoo/blob/247f28fdec788c7eb7c4288db29b931c73a23757/addons/website/views/snippets/snippets.xml>`_

..._webové šablony/stavební bloky/vlastní/možnosti/šablona:

Šablona
~~~~~~~~

Existuje spousta příkazů, které umožňují nastavit možnosti vlastního kódu.
do souboru: `/webové stránky_vzduchotěsné/shluky/s_vzduchotěsnost_snippet.xml`.

... blok kódu::xml



<xpath expr=".">
<!-- Možnosti -->



Poté vložte různé dostupné možnosti:

... blok kódu::xml

:zvýrazněte-řádky: 3-16


<xpath expr=".">
<div data-selector="s_airproof_snippet">
<vyber-layout>
<we-button data-select-class="">Výchozí</we-button>
<we-button data-select-class="s_airproof_snippet_portrait">Portrét</we-button>
<we-button data-select-class="s_airproof_snippet_square">Čtverec</we-button>
<we-button data-select-class="s_airproof_snippet_landscape">Pohled do krajiny</we-button>

<we-title>Kosmos</we-title>
<tlačítko-skupina-string="Před tím"
<we-button data-select-class="mt-0">1</we-button>
<we-button data-select-class="mt-3">2</we-button>
<we-button data-select-class="mt-5">3</we-button>
</tlačítko-skupina>




... _webové šablony/bloky/vlastní/možnosti/vnitřní obsah:

**Obsah článku**

Vytvořte vlastní šablonu „vnitřní obsah“ (přetaženou do jiného bloku), který se dá upravovat.
Proměnná so_content_addition_selector, která obsahuje všechny CSS selektory odkazující na existující
vnitřní stavební bloky obsahu:

... blok kódu::xml
:caption: `/web/airproof/views/snippets/options.xml`

<šablona id="snippet_options" dědí id="website.snippet_options" jméno="Airproof - Snippets Options">
<xpath expr="//t[@t-set='so_content_addition_selector']" position="after">
<t t-set="so_content_addition_selector"
t-value="so_content_addition_selector + ', .s_airproof_snippet'" />



.. viz též:

`Standardní deklarace vnitřního obsahu na GitHubu společnosti Odoo <https://github.com/odoo/odoo/blob/cc05d9d50ac668eaa26363e1127f914897a4b125/addons/website/views/snippets/snippets.xml#L988>`_

... _webové šablony / stavební bloky / vlastní / možnosti / vázání:

Vázání
~~~~~~~

Tyto možnosti používají CSS selektory (třída, XML značka, ID atd.).

..._webové šablony/stavební bloky/vlastní/možnosti/zpracování dat/datový výběr:

data-selector
*************

Možnosti jsou zabaleny do skupin. Skupiny mohou obsahovat vlastnosti, které definují, jakým způsobem zahrnuté možnosti
interagovat s uživatelským rozhraním.

Atribut data-selector spojuje všechny možnosti zahrnuté v skupině s konkrétním prvkem, který odpovídá
hodnota selektoru (třída CSS, ID atd.). Vybraná možnost se zobrazí při výběru shodného selektoru.

... blok kódu::xml

<div data-selector="section, h1, .custom_class, #custom_id">

Může být použito v kombinaci s dalšími atributy, jako například „data-target“, „data-exclude“ nebo
„Data-apply-to“.

... /webové-šablony/bloky/vlastní/možnosti/připojení/cílová data:

data-target
***********

„data-target“ umožňuje použití možnosti na dítěti prvku „data-selector“.

... blok kódu::xml

<div
data-selector="s_airproof_snippet"
data-target="row">

..._webové šablony/bloky/vlastní/možnosti/připojení/vynechání dat:

data-vyloučit
************

„data-exclude=“ umožňuje vyloučit některé konkrétní selektory z pravidla.

... blok kódu::xml
:předpis:Možnost se zobrazí, pokud je vybrána značka ul (bez třídy .navbar-nav).

<div
data-selector="ul"
data-exclude=" .navbar-nav">

... /webové-šablony/bloky/vlastní/možnosti/připojení/datový-výsek/:

data-drop-in
************

`data-drop-in` definuje seznam prvků, kam lze vložit kousek kódu.

... blok kódu::xml

<div data-selector=".s_airproof_snippet" data-drop-in=".x_custom_location">

... /webové-šablony/bloky/vlastní/možnosti/vazby/datový-pád-blízko:

data-drop-near
**************

`data-drop-near` definuje seznam prvků, kde lze snímek vložit vedle.

... blok kódu::xml

<div data-selector=".s_airproof_snippet_card" data-drop-near=".card">

... /webové-šablony/bloky/vlastní/možnosti/zpracování dat/javascript:

data-js
*******

„data-js“ vázává nadefinované metody JavaScriptu.

... blok kódu::xml



... /webové-šablony/bloky/vlastní/možnosti/položky layoutu:

Struktura a pole
~~~~~~~~~~~~~~~

.._webové šablony/stavební bloky/vlastní/možnosti/položky layoutu/název webu:

<název>
************

Přidejte titulky mezi možnosti, abyste je mohli kategorizovat.

... blok kódu::xml

<we-title>Příslušenství titulek 1</we-title>

.. obrázek: building_blocks/we-title.jpg
:alt:Přidejte titulek mezi možnosti
:šířka: 300

... /webové-šablony/bloky/vlastní/možnosti/uspořádání/we-řádek:

<we-row>
**********

Vytvořte řádek, ve kterém jsou prvky vedle sebe.

... blok kódu::xml

<řádek>
<vybereme>...</vybereme>
<tlačítková skupina>...</tlačítková skupina>


Tento příklad je ideální pro tuto situaci: řádek Animation.

.. obrázek: building_blocks/we-row.png
:alt:Sdílejte různé možnosti polí do jedné řádky.

..._webové šablony/stavební bloky/vlastní/možnosti/položky layoutu/tlačítko my:

<tlačítko>
*************

Tento značky se používají uvnitř značek <we-select> a <we-button-group>.

... blok kódu::xml
:zvýraznit-řádky: 2-4

<we-button-group string="Předtím">
<we-button data-select-class="mt-0">1</we-button>
<we-button data-select-class="mt-3">2</we-button>
<we-button data-select-class="mt-5">3</we-button>


Přidejte „data-select-class=““, abyste určili, která třída bude přidána na cílový prvek při tomto
volba je vybrána. Stejně jako u jakéhokoliv XML uzlu umožňuje přidání dalších atributů vylepšit styl a/nebo
uživatelský zážitek.

... blok kódu::xml

<tlačítko>
class="fa fa-fw fa-angle-double-right"
title="Přesun na konec"
data-position="last" />

.. obrázek: building_blocks/we-button.jpg
:alt:Přidejte možnosti a ozdobte je několika ikonami
:šířka: 300

.._webové šablony/stavební bloky/vlastní/možnosti/položky layoutu/vybereme:

<vyber>
*************

Formátuje možnost jako seznam. Přidejte „string =“ k označení pole.

... blok kódu::xml

<vyber-layout>...</vyber-layout>

.. obrázek: building_blocks/we-select.jpg
:alt:Přidejte pole seznamu
:šířka: 300

..._webové šablony/bloky/vlastní/možnosti/položky layoutu/tlačítka skupiny:

<tlačítko skupiny>
*******************

Formátuje možnosti jako tlačítka vedle sebe.

... blok kódu::xml

<we-button-group string="Před tím, než ...">...</we-button-group>

.. obrázek:: building_blocks/we-button-group.jpg
:alt:Přidejte pole seznamu
:šířka: 300

... _webové šablony/stavební bloky/vlastní/možnosti/položky layoutu/my_check_box:

<we-checkbox>
***************

Formátuje možnost jako přepínač.

... blok kódu::xml

<we-checkbox
string="Nápověda"
data-select-class="s_airproof_snippet_tooltip" />

.. obrázek: building_blocks/we-checkbox.jpg
:alt:Přidejte přepínač.
:šířka: 300

.._webové šablony/bloky/vlastní/možnosti/položky layoutu/rozsah:

<rozsah>
************

Formátuje možnost jako posuvník.

... blok kódu::xml

<položka-rozsahu
string="Vzdálenost obrázků"
data-select-class="o_spc-none|o_spc-small|o_spc-medium|o_spc-big" />

Každý krok rozsahu je oddělen znakem „|“. Zde každý název třídy odpovídá kroku.

.. obrázek:: building_blocks/we-range.jpg
:alt:Přidejte přepínač.
:šířka: 300

.._webové šablony/stavební bloky/vlastní/možnosti/položky vzhledu/my vkládáme:

<we-input>
************

Formátuje možnost jako textové pole.

... blok kódu::xml
:vyzdvihnout-řádky: 3–5
:podpis:  „data-unit“, „data-save-unit“ a „data-step“ jsou nepovinné

<we-input
string="Rychlost"
jednotka dat="s"
data-save-unit="ms"
data-step="0.1"/>

.. obrázek: building_blocks/we-input.jpg
:alt:Přidejte pole pro text.
:šířka: 300

Tag <we-input> má několik volitelných atributů, které jsou užitečné v konkrétních případech:

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 30 70

   * -Atribut
     - Popis
   * – „data-unit“
     - Zobrazuje očekávanou jednotku měření.
   * – „data-save-unit“
     - Zadejte jednotku měření, do které se převede hodnota zadaná uživatelem a která bude uložena.
   * – data-step
     - Určete číselnou hodnotu, kterou lze pole zvýšit.

... _webové šablony/bloky/vlastní/možnosti/položky layoutu/barvy:

<we-colorpicker>
******************

Formátuje možnost jako barvu/gradient, ze kterého je možné vybrat.

... blok kódu::xml

<barva-vyber
string="Barvový filtr"
data-select-style="true"
data-css-property="barva pozadí"
data-color-prefix="bg-"
data-apply-to=".s_map_color_filter" />

.. obrázek: building_blocks/we-colorpicker.jpg
:alt:Přidat barevný výběr.
:šířka: 300

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 30 70

   * -Atribut
     - Popis
   * – „data-select-style“
     - Odkazuje na metodu „selectStyle“ v JavaScriptu. Vybírá hodnotu atributu „style“.
aplikované na cíl, aby se zvolil správný výběr možností.
   * – „data-css-vlastnost“
     - Definujte vlastnost CSS, na kterou se tlačítko pro výběr barvy zaměřuje.
   * – „data-barva-předpona“
     - Definujte předponu použitou pro návrat třídy CSS.
   * „Použijte na“
     - Nastavte prvek, na který se barva aplikuje.

... /webové-šablony/bloky/vlastní/možnosti/metody:

Metody
~~~~~~~

Kromě možností vázání umožňujících vybrat, cílit nebo vyloučit prvek.
několik užitečných atributů dat odkazujících na standardní metody JavaScriptu.

Příkladem je například data-select-class, které odkazuje na metodu selectClass v JavaScriptu.

... _webové šablony/stavba bloků/vlastní/možnosti/metody/přirozené:

Vlastní metody
****************

..._webové šablony/stavební bloky/vlastní/možnosti/metody/přirozené/vybrání:

Výběr
^^^^^^^^^

Existuje několik vnitřních metod, které lze volat pomocí příslušného atributu dat
přímo do šablony XML.

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 35 65

   * – Atributy dat
     - Popis
   * „data-select-class“
     - Umožňuje vybrat pouze jednu třídu v možnostech Classes
nastavit a nastavit na příslušný kousek kódu.
   * – „data-select-data-attribute“ + „data-attribute-name“
     - Umožňuje vybrat hodnotu a nastavit ji jako atribut na příslušném kousku textu.
je určena atributem data-attribute-name.
   * – „data-select-property“ + „data-property-name“
     - Umožňuje vybrat hodnotu a nastavit ji jako vlastnost na příslušném kousku kódu.
je udělována atributem data-property-name.
   * – „data-select-style“ + „data-css-property“
     - Umožňuje vybrat hodnotu a nastavit ji jako styl CSS v příslušném kousku kódu.
je udělována pomocí atributu data-css-property.
   * – „barva-kombinace“
     - Zvolte paletu barev.
**Pouze pro** `we-colorpicker`

... /webové-šablony/bloky/vlastní/možnosti/metody/přirozené/události:

Akce
^^^^^^

Webový editor obsahuje také vestavěné metody přímo propojené s událostmi, na které Webový editor reaguje:

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * - Jméno
     - Popis
   * - začátek
     - Při prvním výběru snímku v editačním sezení.
když je kousek textu přetáhnut na stránku.
   * - zničit
     - Probíhá po uložení stránky vydavatelem.
   * - naFokus
     - Při každém výběru uživatelem nebo při přetažení
na stránce.
   * - naZaostření
     - Při ztrátě soustředění na část stránky.
   * -onClone
     - Přichází ihned po kopírování fragmentu.
   * 
     - Přichází krátce před odstraněním fragmentu.
   * onBuilt
     - Přiřazuje se k tomuto události, když je fragment přetahován na místo vložení.
Pokud je tlačítko aktivní, obsah už je vložen na stránku.
   * - čistý pro uložení
     - Probíhá před uložením stránky.

.. viz též:
   - „Editor webu – metody v JavaScriptu související s možnostmi přetáčení na GitHub
<https://github.com/odoo/odoo/blob/cc05d9d50ac668eaa26363e1127f914897a4b125/addons/web_editor/static/src/js/editor/snippets.options.js#L3512>`_
   - „Šablony XML různých standardních vložek
<https://github.com/odoo/odoo/blob/cc05d9d50ac668eaa26363e1127f914897a4b125/addons/website/views/snippets/snippets.xml>

... _webové šablony/bloky/vlastní/možnosti/metody/vlastní:

Metody přizpůsobené
**************

Pro vytvoření vlastních metod JavaScriptu je potřeba vytvořit spojení mezi možností skupiny a vlastními metodami.
musí být vytvořen. K tomu je potřeba vytvořit třídu JavaScriptu a volat ji v šabloně XML
„data-js“.

Přidejte atribut data-js do vaší skupiny možností:

... blok kódu::xml
:vyzdvihnout-řádky: 3


<xpath expr=".">
<div data-selector=".s_airproof_snippet" data-js="airproofSnippet">
            // Options




Poté může být třída vytvořena v souboru JavaScriptu:

... kódový blok: JavaScript


   /** @odoo-module */

importovat možnosti z webového editoru „web_editor.snippets.options“;

const AirproofSnippet = (options) => {
      // Built-in method example
funkce start():
         //...
      }
      // Custom method example
customMethodName: function () {
         //...
      }
   });

options.registry.AirproofSnippet = AirproofSnippet;

export default AirproofSnippet;

Konečně můžete volat metodu vaší vlastní třídy pomocí šablony XML:

... blok kódu::xml
:vyzdvihnout-řádky: 3


<xpath expr=".">
<div data-selector=".s_airproof_snippet" data-js="airproofSnippet">
<we-checkbox data-custom-method-name="">




... _webové šablony/bloky/vlastní/dynamické:

Šablony dynamického obsahu
-------------------------

Výchozí nastavení obsahuje výběr šablon v editoru webových stránek.
Přizpůsobené šablony lze také automaticky přidat do seznamu pomocí stejného názvu
Atribut id šablony.

... _webové šablony/bloky/vlastní/dynamické/volání:

Vyvolat šablonu
~~~~~~~~~~~~~~~~~

Vybraný dynamický kousek nahradí vložené místo
správný šablonový soubor na základě klíče datové šablony a vlastního CSS třídění:

... blok kódu::xml
:vyzdvihnout-řádky: 3,4

<část
data-snippet="s_blog_posts"
name="Blogové příspěvky"
class="s_blog_post_airproof s_dynamic_snippet_blog_posts s_blog_posts_effect_marley s_dynamic pb32 o_cc o_cc2 o_dynamic_empty"
data-template-key="webová stránka_airproof.dynamický filtr šablony blogového příspěvku airproof"
data-filter-by-blog-id="-1"
data-počet-záznamů="3"
data-počet-prvků="3"
   >
<div class="container o_not_editable">

<div class="alert alert-info rounded-0 fade show d-none d-print-none">
Váš dynamický náhled bude zobrazen zde... Toto sdělení se zobrazí, protože jste neposkytli oba filtr a šablonu k použití.
</div>

<div třída="dynamický šablonový prvek"/>
</div>


... _webové šablony/bloky/dynamické/příklady:

Příklady
~~~~~~~~

.. záložky::

... tab:: Příspěvky na blogu

... kódový blok::xml
:popisek: „/web/airproof/views/snippets/options.xml“

<šablona id="dynamický filtr blogu - vzduchotěsnost" jméno="...">
<div t-foreach="records" t-as="data" class="s_blog_posts_post">
<t t-set="record" t-value="data._record"/>
<!-- Obsah -->
</div>


... seznamová tabulka::
:hlavičkové řádky: 1
:sloupky: 1
:šířky: 20 80

         * -Atribut
           - Popis
         * 
           - ID šablony. Musí začínat „dynamic_filter_template_blog_post_“.
         * - jméno
           - Čitelný název šablony



... kódový blok::xml
:popisek: „/web/airproof/views/snippets/options.xml“


<t t-foreach="records" t-as="data" data-number-of-elements="4" data-number-of-elements-sm="1" data-number-of-elements-fetch="8">
<t t-set="record" t-value="data._record"/>
<!-- Obsah -->



... seznamová tabulka::
:hlavičkové řádky: 1
:sloupky: 1
:šířky: 40 60

         * -Atribut
           - Popis
         * 
           - ID šablony. Musí začínat „dynamic_filter_template_product_product_“.
         * - jméno
           - Čitelný název šablony
         * 
           - Počet produktů na snímku na ploše počítače
         * 
           - Počet produktů na jedné stránce v mobilu
         * – počet položek na stránce
           - Celkový objem vytažených produktů

...... tab:: Akce

... kódový blok::xml
:popisek: „/web/airproof/views/snippets/options.xml“

<šablona id="dynamický filtr - událost - vzduchotěsnost" jméno="...">
<div t-foreach="records" t-as="data" class="s_events_event">
<t t-set="record" t-value="data['_record']._set_tz_context()"/>
<!-- Obsah -->
</div>


... seznamová tabulka::
:hlavičkové řádky: 1
:sloupky: 1
:šířky: 20 80

         * -Atribut
           - Popis
         * 
           - ID šablony. Musí začínat „dynamic_filter_template_event_event_“.
         * - jméno
           - Čitelný název šablony
