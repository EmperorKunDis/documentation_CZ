=====
Média
=====

V tomto kapitole se podíváme na to, jak do aplikace Odoo zahrnout média, jako jsou například obrázky, videa nebo ikony.

.. /webové-šablony/mediální obrázky:

Obrázky
======

Zaznamenávejte obrázky do databáze a používejte je později ve svém návrhu/kódu.
dostupné pro konečného uživatele prostřednictvím *dialogu médií*.

.. obrázek: media/media-okno.png
:alt: Okno médií

Webový editor podporuje následující formáty obrázků: JPG, GIF, PNG a SVG.

.. varování:
Některé možnosti nabízené Webovým stavitelem jsou pouze vhodné pro média registrovaná do
rekord. Možná neuvidíte některé možnosti, pokud přidáte obrázek přímo s relativním cestou.
do složky vašeho modulu.

... /webové-šablony/mediální obrázky/prohlášení:

Prohlášení
-----------

Používat vaše obrázky ve svém kódu a mít je zahrnuty do galerie stavitele (takže zákazník
jejich znovupoužití), deklarujte je takto:

... blok kódu::xml
:caption: „/webová_stránka_vzduchotěsná/data/obrázky.xml“

<záznam id="img_about_01" typu="ir.attachment">
<políčko jméno="Obraz 01">O obrázku 01</políčko>
<pole jméno="datos" typ="base64" soubor="webové stránky/vzduchotěsnost/statické/zdroj/img/obsah/img_o_nás_01.jpg"/>
<položka jméno="res_model">ir.ui.view</položka>
<pole název="veřejné" hodnota="True"/>
</záznam>

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * – Hřiště
     - Popis
   * 
     - Název obrázku, který chcete použít ve svém kódu
   * - jméno
     - Popisný název pro vaši fotografii
   * Datas
     - Umístění vaší fotografie

.. /webové-šablony/mediální obrázky/použití:

Užívání
---

.. /webové-šablony/multimédia/obrázky/použití/standardní:

Běžné obrázky
~~~~~~~~~~~~~~

Ve vašich šablonách XML zavolejte své obrázky takto:

... blok kódu::xml

<img src="/web/obrazky/weby_vzduchotěsnost.img_o_nas_01" alt=""/>

Jako ID obrázku, který jste mu dali.

.. /webové-šablony/multimédia/obrázky/použití/výchozí pozadí:

Přídavné obrázky
~~~~~~~~~~~~~~~~~

... blok kódu::xml

<část stylu="zadní obrázek: url('http://www.airproof.cz/images/website_airproof.img_about_01.jpg')">

... /webové-šablony/multimédia/obrázky/použití/logo:

Logo společnosti
~~~~~~~~~~~~

Pro použití loga společnosti je používání trochu jiné. Nejprve ho deklarujte v souboru `website.xml`.
a pak je volat pomocí správné šablony. Například pro volání uvnitř hlavičky budeme
použijte značku „<t t-call="website.placeholder_header_brand">“.

... blok kódu::xml


<záznam id="webové stránky.výchozí webová stránka" typu="webové stránky">

</záznam>

.. poznámka::
:ref:`Více informací o nastavení loga společnosti najdete zde <theming/module/website>
a předvolby globálních webových stránek.

..tip:
Abyste se ujistili, že vaše obrázky nezpomalí váš web a nepřidají příliš mnoho hmotnosti, zkuste
Věnujte prosím pozornost těmto pár bodům:

   - **Váha**: < 200 KB.
   - **Velikost**: ne více než 1500 px pokud není potřeba.
   - **Doplnění**: použijte SVG nebo JPG, PNG nebo GIF.
   - *Jméno*: žádné mezery, akcenty ani speciální znaky a slova oddělujte pomlčkami.
používat relevantní slova, pokud je to možné.
   - Obrázky větší než 1920px budou na webu komprimovány. Pokud je menší než 1920px,
Zůstane zachován.

.. /webové-šablony/mediální soubory:

Videa
======

Přidejte do pozadí videa.

... blok kódu::xml

<část třídy „o_zadní_videopodklad“ s datovým zdrojem „…“>
<!--Obsah-->


.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * -Atribut
     - Popis
   * 
     - URL videa.

Přidejte videa jako obsah.

... blok kódu::xml

<div class="media_iframe_video" data-oe-expression="...">
<div třída="css_editable_mode_display" />
<div třída="media_iframe_video_size" contenteditable="false" />
<iframe src="...
rámeček="0"
editovatelný obsah="ne"
allowfullscreen="allowfullscreen"/>


.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * -Atribut
     - Popis
   * 
     - URL videa.
   * - zdroj
     - URL videa.

... /webové-šablony/multimédia/ikonky:

Ikony
=====

Ve výchozím nastavení je knihovna ikon Font Awesome součástí Webové stránky. Můžete do ní vložit ikony
kdekoliv používáte CSS Předponu „fa“ a název ikony. Font Awesome je navržen tak, aby byl používán s
inline prvky. Můžete použít značku <i> pro úsporu místa, ale použití značky <span> je více sémantické
správně.

... blok kódu::xml



.. viz též:
„Ikony Font Awesome verze 4 <https://fontawesome.com/v4/icons/>“

Povolte možnosti stylu webové stránky.

... blok kódu::xml

<span class="fa fa-2x fa-picture-o rounded-circle"/>

Zvětšit velikost ikony (fa-2x, fa-3x, fa-4x nebo fa-5x třídy).

... blok kódu::xml

<span class="fa fa-2x fa-picture-o"/>

.. obrázek: media/icon-options.png
:alt:Možnosti ikon
