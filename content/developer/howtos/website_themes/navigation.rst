==========
Navigace
==========

Webový editor vám umožní snadno upravit navigaci tak, aby vyhovovala vašim potřebám.

V tomto kapitole se dozvíte, jak:

- Smazat a vytvořit položky nabídky.
- Vytvořte rozbalovací nabídku.
- Vytvořte megamenu.

... /webové šablony/navigace/výchozí:

Výchozí
=======

Odoo automaticky vytváří některé základní položky nabídky podle aplikací, které jste nainstalovali. Například
Webová aplikace přidává dvě položky do hlavního menu. Tyto položky jsou spojeny s stránkami, které jsou také
Vytvořen automaticky.

Smazat výchozí položky nabídky.

.. kódový blok::xml
:caption:"/web/airproof/data/menu.xml"


<smazat model="webová stránka.menu" vyhledávání = "[('url', 'v', ['/', '/kontaktujte nás'])]


<!-- Obchod -->
<delete model="website.menu" search="[('url','in', ['/', '/shop']),


... _webové šablony/navigace/nabídka:

Položka menu
=========

**Prohlášení**

.. kódový blok::xml
:caption:"/web/airproof/data/menu.xml"

<záznam id="menu_o_nas" model="web.menu">
<polozka name="name">O nás</polozka>
<field name="url">/o-nas</field>
<field name="parent_id" search="[
('url', '==', '/default-main-menu')
["web_id" => "1"]]
<vlastnost jméno="webová stránka">1</vlastnost>
<položka jméno="pořadí" typ="int">10</položka>
</záznam>

... seznam tabulky:
:hlavičkové řádky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * – Hřiště
     - Popis
   * - jméno
     - Titulek
   * URL
     - Hodnota atributu href
   * -parent_id
     - Název menu, do kterého chcete položku přidat.
   * - webová stránka
     - Webová stránka, na které bude položka přidána.
   * - pořadí
     - Určuje pozici odkazu v horním menu.

.._webové šablony/navigace/nabídka/nové okno:

Nový okno
----------

Otevřete odkazovou adresu v novém okně.

.. kódový blok::xml


<field name="new_window" eval="True"/>
</záznam>

... /webové-šablony/navigace/nabídka/externí odkazy/:

Externí odkazy
--------------

Přidejte odkaz na externí webové stránky.

.. kódový blok::xml


<položka jméno="url">https://www.odoo.com</položka>
</záznam>

... _webové šablony/navigace/nabídka/dock:

Záložní bod
------

Odkaz na konkrétní část stránky.

.. kódový blok::xml


<políčko name="url">/o-nas/#naše-tým/</políčko>
</záznam>

... /webové-šablony/navigace/vybírání/:

Drobný menu
=============

**Prohlášení**

.. kódový blok::xml
:caption:"/web/airproof/data/menu.xml"

<záznam id="menu_služeb" model="web.menu">
<pole název="name">Služby</pole>
<vlastnost jméno="webová stránka">1</vlastnost>
<field name="parent_id" search="[
('url', '==', '/default-main-menu')
["web_id" => "1"]]
<položka jméno="pořadí" typ="int">...</položka>
</záznam>

Přidejte položku do nabídky.

.. kódový blok::xml

<záznam id="menu_služby_item_1" model="web.menu">
<položka name="název">Položka 1</položka>
<pole name="url">/dropdown/item-1</pole>
<vlastnost jméno="webová stránka">1</vlastnost>
<položka jméno="parent_id" odkaz="website_airproof.menu_services"/>
<položka jméno="pořadí" typ="int">...</položka>
</záznam>

... seznam tabulky:
:hlavičkové řádky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * – Hřiště
     - Popis
   * -parent_id
     - Vyberte položku, do které chcete přidat prvek.

.._webové šablony/navigace/megamenu:

Mega menu
=========

Megamenu je rozbalovací nabídka s dalšími možnostmi, nikoliv jen seznam odkazů.
megamenu lze použít jakýkoliv obsah (text, obrázky, ikony, ...).

V Odoo si můžete vybrat šablonu megamenu v seznamu. Pokud nemáte potřebu vlastního rozložení,
lze znovu použít strukturu šablony v poli obsahu menu, jako u jakéhokoli statického obsahu.

**Prohlášení**

.. kódový blok::xml
:caption:"/web/airproof/data/menu.xml"

<zaznamenání id="menu_megamenu" model="web.menu">
<polozka name="název">Mega Menu</polozka>
<field name="parent_id" search="[
('url', '==', '/default-main-menu')
(“webová stránka”, “=”, 1)]"/>
<field name="web_id">1</field>
<položka jméno="pořadí" typ="int">...</položka>
<field name="is_mega_menu" eval="true"/>
<položka název="mega_menu_class">...</položka>
<položka jméno="mega_menu_content" typ="html">
<section třída="s_mega_menu_multi_menus" style="padding: 4px; background-color: #ffffff; color: #000000; z-index: 9999;" o_colored_level="1" o_cc="1" o_cc1="1">
<div class="container">


<h4 class="o_default_snippet_text">První menu</h4>



<a href="#" class="nav-link o_default_snippet_text" data-name="Menu Item">Menu Item 3</a>



<h4 class="o_default_snippet_text">Druhé menu</h4>



<a href="#" class="nav-link o_default_snippet_text" data-name="Menu Item">Menu Item 3</a>







<a href="#" class="nav-link o_default_snippet_text" data-name="Menu Item">Menu Item 3</a>



<h4 class="o_default_snippet_text">Poslední menu</h4>



<a href="#" class="nav-link o_default_snippet_text" data-name="Menu Item">Menu Item 3</a>


</div>


</field>
</záznam>

... seznam tabulky:
:hlavičkové řádky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * – Hřiště
     - Popis
   * - je_mega_menu
     - Zapněte funkci Mega Menu.
   * mega_menu_classes
     - Přidat vlastní třídy do hlavního prvku
   * mega_menu_content
     - Výchozí obsah megamenu

Kromě toho můžete potřebovat něco víc vizuálně pokročilého s vlastním šablonou.
Můžete si zkontrolovat, jak vypadá šablona „<{GITHUB_PATH}/addons/website/views/snippets/s_mega_menu_odoo_menu.xml>“
jsou implementovány přímo do zdrojových kódů Odoo.

.. _webové šablony/navigace/megamenu/vlastní:

Vlastní šablona
---------------

Vytvořte si vlastní šablonu a přidejte ji do seznamu.

**Grafické zpracování**

.. kódový blok::xml


<šablona id="s_mega_menu_airproof" jméno="Airproof" skupiny="základní.skupina_uživatel">
<section class="s_mega_menu_airproof o_cc o_cc1 pt40">
<!--Obsah-->
</odd>


**Volitelné**

Použijte následující kód, abyste přidali možnost pro váš nový vlastní megamenu na webovém editoru.

.. kódový blok::xml
:caption: „/webová_stránka_vzduchotěsná/pohledy/součásti/možnosti.xml“

<šablona id="snippet_options" dědí id="website.snippet_options" název="Airproof - Mega Menu Options">
<xpath expr="//*[@data-name='mega_menu_template_opt']/*" position="before">
<t t-set="_label">Airproof</t>
<tlačítko-we-button t-att-data-select-label="_label"
data-select-template="webová stránka_vzduchotěsné.s_mega_menu_vzduchotěsné"
data-img="/webová stránka airproof/statické zdroje/obrázky/stavitel/hlavička opt.svg"
t-out="_label"/>
</xpath>

