======
Tvar
======

Tvar je užitečný, pokud chcete přidat osobnost svému webu.

V této kapitole se dozvíte, jak přidat standardní a vlastní pozadí a obrazové tvary.

.. /webové-šablony/tvary/přední plán:

Pozadí tvarů
=================

Přídavné obrázky jsou soubory ve formátu SVG, které můžete použít jako dekorativní pozadí.
sekcí. Každý tvar má jednu nebo více nastavitelných barev a některé z nich jsou animované.

.. varování:
Výchozí tvary v Odoo používají jako referenci paletu barev Odoo. Tímto způsobem se barvy
Bude automaticky přizpůsobena nové palety pokaždé, když se změní:

... kódový blok: scss

výchozí paleta = {
'1': '#3AADAA',
'2': '#7C6576',
'3': '#FFFFFF',
'4': '#FFFFFF',
'5': '#383E45',
        }

... /webové-šablony/tvary/předloha:

Standard
--------

K dispozici je velký výběr přednastavených tvarů pozadí.

**Použití**

... blok kódu::xml

<část data-oe-tvarová-data={`{„tvar“: „web_editor/Zigy/06“}`}>
<div třída="o_we_shape" třída="o_web_editor_Zigs_06"/>
<div class="container">
<!--Obsah-->
</div>


„data-oe-shape-data“ je objekt JSON, který obsahuje informace o vašem tvaru, jako například umístění
souboru SVG, opakování a otočení apod.

Příkladem je možnost **zrcadlit tvar** vodorovně nebo svisle pomocí osy X nebo Y.
tohoto:

... blok kódu::xml

<část sekce s daty o tvaru webového editoru Zigs s hodnotami x a y>
<div class="o_we_shape o_we_flip_x o_we_flip_y o_web_editor_Zigs_06"/>
<div class="container">
<!--Obsah-->
</div>


..._webové šablony/tvary/předlohy/standardní barvy:

Mapování barev
~~~~~~~~~~~~~~

Můžete také změnit výchozí mapování barev vašeho tvaru buď přepnutím barev v
současnou mapu nebo vytvořit alternativní mapu bez modifikace původní.

.._webové šablony/tvar/přední plán/barvy/vypínač:

Přepínání barevného mapování
*********************

Nejprve můžeme použít tvar jako je tento:

.. obrázek: tvarů/tvarů-počáteční.png
:alt:Konečná podoba

... blok kódu::xml

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="none" width="100%" height="100%">
<definice>



<svg id="zigs06_dole" viewBox="0 0 30 30" preserveAspectRatio="xMinYMax meet" fill="#FFFFFF" width="100%">


</definice>
<svg>
<použít xlink:href="#zigs06_top"/>
<použití xlink:href="#zigs06_dno"/>



Zde používáme barvu číslo 383E45 a barvu číslo FFFFFF, což odpovídá páté a čtvrté barvě v Odoo.
výchozí paleta barev.

Tvar je v SCSS deklarován následovně:

... kódový blok: Sass
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

'Zigy/06': ('umístění': doleva, 'velikost': 30px 100%, 'barvy': (4, 5), 'opakování v x směru': pravda)

.. obrázek: tvar/tvar-priznaky.jpg
:alt:Barvy tvarů

Černá barva je použita na vrcholu („c5“), světlejší („c4“) na spodku a uprostřed.
Tvar je prostě průhledný.

Budeme přepsat mapu „barvy“ několika páry klíč-hodnota:

**S odkazem na barevný palec a vlastními barvami**

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-bg-shapes: změna barevného mapování pro tvar web_editoru ('Zigs/06', (4: 3, 5: rgb(187, 27, 152)))

**Anebo jen s odkazy**

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-bg-shapes: změnit barvy tvarů ('web_editor', 'Zigs/06', (4: 3, 5: 1));

Bílý pěšec „c4“ bude nahrazen pěšcem „c3“ a černý pěšec „c5“ bude nahrazen pěšcem „c1“.

**Výsledky**

.. obrázek: tvar/tvar-konec.png
:alt:Konečný tvar

.. obrázek: tvarů/tvarů-konečné možnosti.png
:alt:Konečné možnosti tvaru

..._webové šablony/tvary/přední plán/barevné schéma/extra:

Přidat další barvy mapování
************************

Přidání dalšího barevného mapování vám umožní přidat barvu do šablony tvaru,
Zachování původního.

... kódový blok::scss
:caption: „/webová_stránka_vzduchotěsná/statické/zdrojové soubory/bootstrap_převzatý.scss“

$o-bg-shapes: přidat další barvy pro mapování tvarů ('web_editor', 'Zigs/06', 'druhé', (4: 3, 5: 1));

... blok kódu::xml

<část data-oe-tvarová-data={`{„tvar“: „web_editor/Zigy/06“}`}>
<div třída="o_we_shape" třída="o_web_editor_Zigs_06" třída="o_second_extra_shape_mapping"/>
<div class="container">
<!--Obsah-->
</div>


..._webové šablony/tvary/přední plán/vlastní:

Obchodní zvyklost
------

Někdy může být nutné vytvořit jeden nebo více vlastních tvarů.

Nejprve musíte vytvořit soubor SVG pro tvar.

... blok kódu::xml


<svg verze="1.1"  xmlns="http://www.w3.org/2000/svg" šířka="86" výška="100">
<polygon points="0 25, 43 0, 86 25, 86 75, 43 100, 0 75" style="fill:#24AB96;"/>


Ujistěte se, že používáte barvy ze standardní palety Odoo pro svůj tvar (viz výše:ref:).

... kódový blok::scss

defaultní paleta = {
'1': '#3AADAA',
'2': '#7C6576',
'3': '#FFFFFF',
'4': '#FFFFFF',
'5': '#383E45',
   }
... webové šablony tvarů pozadí vlastní přílohy:

Příloha
~~~~~~~~~~

Označte svůj soubor s daty o tvaru.

... blok kódu::xml
:caption: „/webová_stránka_vzduchotěsná/data/tvar.xml“

<záznam id="tvar-šestihran-01" typu="ir.attachment">
<polozka name="name">01.svg</polozka>
<položka jméno="daty" typ="base64" soubor="webové stránky/vzduchotěsnost/statické obrázky/šestiúhelníky/01.svg"/>
<políčko name="url">/web_editor/tvar/ilustrace/šestiúhelníky/01.svg</políčko>
<pole název="veřejné" hodnota="True"/>
</záznam>

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * – Hřiště
     - Popis
   * - jméno
     - Jméno tvaru
   * Datas
     - Cesta k tvaru
   * - url
     - Umístění vašeho tvaru v webovém editoru. Soubor se automaticky zkopíruje do
/web_editor/tvar/ilustrace, vytvořené Webovým editorem.
   * – veřejnost
     - Tvar je k dispozici pro pozdější úpravy.

... /webové-šablony/tvary/zadní-plán/vlastní/scss:

SCSS
~~~~

Určete styl vašeho tvaru.

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-bg-shapes: map-merge($o-bg-shapes,
       (
'ilustrace': map-merge(
map_get($o-bg-shapes, 'ilustrace') nebo (),
               (
'šestiúhelníky/01': ('položka': střed středu, 'velikost': automaticky 100%, 'barvy': (1), 'opakování x': pravda, 'opakování y': pravda),
               ),
           ),
       )
   );

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * – Klíč
     - Popis
   * - umístění souboru
     - „hexagons/01“ odpovídá umístění vašeho souboru v adresáři „shapes“.
   * – pozice
     - Určuje polohu vašeho tvaru.
   * - velikost
     - Určuje velikost vašeho tvaru.
   * - barvy
     - Určuje barvu, kterou chcete, aby měla (toto přebije barvu, kterou jste uvedli v
SVG).
   * Repeat-X
     - Určuje, zda je tvar opakován vodorovně. Tento klíč je volitelný a pouze pokud je vyplněný,
Pokud je nastaveno na hodnotu true, definuje se.
   * opakující se
     - Určuje, zda je tvar opakovaný ve svislé ose. Tento klíč je volitelný a pouze v případě jeho nastavení
Pokud je nastaveno na hodnotu true, definuje se.

.._webové šablony/tvary/předvolby:

Přidejte možnost
~~~~~~~~~~~~~~

Nakonec přidejte svůj tvar do seznamu dostupných tvarů na Webové stránce.

... blok kódu::xml
:komentář: „/webové stránky/zabrání-průvanu/výhledy/součásti/možnosti.xml“

<šablona id="snippet_options_background_options" dědí id="website.snippet_options_background_options" název="Airproof - Shapes">
<xpath expr="//*[hasclass('o_we_bg_shape_menu')]/header[hasclass('o_pager_nav')]//*[hasclass('o_pager_nav_btn')][last()]" position="after">
<button type="button" class="o_pager_nav_btn p-0 text-uppercase" data-scroll-to="x_wd_scroll_bgshapes_aiproof">
Airproof
</tlačítko>

<xpath expr="//*[@class='o_we_bg_shape_menu']/div[@class='o_pager_container']" position="inside">

<we-title>Airproof</we-title>
<vyber-stránku string="Airproof">
<tlačítko data-tvar="ilustrace/vzduchotěsné/01" data-vybraný-text="Vzduchotěsné 01"/>
</vyber-stranku>




... /webové-šablony/tvary/předdefinované/použít:

Použijte ho do svých stránek
~~~~~~~~~~~~~~~~~~~~~~

Ve vašich XML stránkách můžete používat své tvarování stejně jako ostatní.

... blok kódu::xml

<section class="..." data-oe-shape-data="{'shape': 'illustration/airproof/01', 'colors': 'c4': '#8595A2', 'c5': 'rgba(0, 255, 0)'}">
<div třída="o_we_shape" třída="o_illustration_airproof_01"/>
<div class="container">
<!--Obsah-->
</div>


Můžete také definovat barvy pomocí atributu data-oe-shape-data, ale je to volitelné.

