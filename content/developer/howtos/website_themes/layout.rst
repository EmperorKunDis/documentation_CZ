======
Grafický návrh
======

V této kapitole se naučíte:

- Vytvořte vlastní hlavičku.
- Vytvořte vlastní záhlaví.
- Upravit standardní šablonu.
- Přidejte sekci o autorských právech.
- Zlepšete reakci vašeho webu.

... /webové-šablony/vzhled/výchozí/:

Výchozí
=======

Stránka Odoo kombinuje prvky přesahující stránku a jedinečné prvky. Prvky přesahující stránku jsou na každé stránce stejné,
stránka, zatímco jedinečné prvky jsou pouze pro konkrétní stránku. Výchozí hodnotou je dvě
křížové stránkové prvky, hlavičku a patičku a unikátní hlavní prvek obsahující konkrétní
obsahu této stránky.

... blok kódu::xml

<div id="wrapwrap">
<hlavička/>
<hlavní>
<div id="wrap" třída="oe_struktura">
<!-- Obsah stránky -->
</div>
</hlavní>
</footer>


Každý soubor XML Odoo začíná specifikací kódování. Poté musíte napsat svůj kód uvnitř
Tag <odoo>.

... blok kódu::xml



      ...


.. poznámka::
Používání přesných názvů šablon je důležité pro rychlé vyhledávání informací v celém modulu.
Názvy šablon by měly obsahovat pouze malá písmena, číslice a podtržítka.

Vždy přidejte prázdnou řádku na konec souboru. To lze provést automaticky nastavením
vašeho IDE.

.. /webové šablony/layout/XPath:

XPath
=====

XPath (jazyk pro cestování XML) je jazyk výrazů, který vám umožňuje navigovat mezi prvky.
a atributy v XML dokumentu snadno. XPath se používá k rozšíření standardních šablon Odoo.

Výhled je kódován následujícím způsobem.

... blok kódu::xml

<šablona id="..." dědí id="..." název="...">
<!--Obsah-->


.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * -Atribut
     - Popis
   * 
     - ID upraveného pohledu
   * - dědičný id
     - ID standardního pohledu (používající následující vzor: „modul.šablona“)
   * - jméno
     - Čitelný název upraveného pohledu

Pro každou cestu v XML upravujete dvě atributy: **výraz** a **pozice**.

Příklad:
... kódový blok :: XML


<šablona id="layout" dědí id="webová stránka.layout" názvem "Vítejte"
<xpath expr="//hlavička" pozice="před">
<!--Obsah-->
</xpath>
</vzorec>

Toto XPath přidává vítací zprávu před obsah stránky.

.. varování:
Pozor na nahrazování atributů výchozích prvků. Protože vaše téma nadstavbu výchozího obsahuje,
Váš upgrade bude přednostnější než jakýkoli budoucí update Odoo.

.. poznámka::
   - Pokud vytvoříte nový šablonu nebo záznam, měli byste aktualizovat svůj modul.
   - *XML ID* podřazených pohledů by měl používat stejné *ID* jako původní záznam. To pomáhá při vyhledávání
všechny dědění na jednom místě. Konečné *XML ID* jsou předponovány moduly, které je vytváří.
Nebylo by žádné překrývání.

... /webové šablony/layout/XPath/výrazy:

Výrazy
-----------

XPath používá výrazy pro vyjádření cesty k výběru uzlů v dokumentu XML. Selektory se používají uvnitř
vyjádření, které se zaměří na správný prvek. Nejvýznamnější jsou uvedeny níže.

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * - Výběr potomků
     - Popis
   * - /
     - Vybírá z kořenového uzlu.
   * - //
     - Vybírá uzly v dokumentu od aktuálního uzlu, který odpovídá výběru.
kde jsou.

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * - Atributové selektory
     - Popis
   * - \*
     - Vybírá jakýkoliv XML tag. Znak „*“ lze nahradit konkrétním tagem, pokud je potřeba
přesnější.
   * - *[@id="id"]
     - Vybírá konkrétní identifikátor.
   * - *[předmět.hasClass('třída')]
     - Vybírá konkrétní třídu.
   * - *[@name="name"]
     - Vybírá štítek s konkrétním názvem.
   * – *[@t-call="t-call"]
     - Vybírá konkrétní tónový signál.

.. /webové šablony/uspořádání/XPath/položka:

Pozice
--------

Pozice určuje, kde se kód v šabloně nachází. Povolené hodnoty jsou uvedeny
pod ní:

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * – Pohled
     - Popis
   * - nahradit
     - Nahradí cílový uzel obsahem XPath.
   * - uvnitř
     - Přidává obsah XPath do cílového uzlu.
   * – před
     - Přidává obsah XPath před cílovým uzlem.
   * – po
     - Přidává obsah XPath po cílovém uzlu.
   * - atributy
     - Přidává obsah XPath do atributu.

Příklad:
Toto XPath odstraní první prvek s třídou .breadcrumb.

... kódový blok :: XML

<xpath expr="//*[hasClass('breadcrumb')]" position="replace"/>

Toto XPath přidá další prvek typu <li> po posledním dítěti prvku <ul>.

... kódový blok :: XML

<xpath expr="//ul" position="inside">
<li>Poslední prvek seznamu</li>


Toto XPath přidává div před nav, který je přímo podřízený header.

... kódový blok :: XML

<xpath expr="//hlavička/navigace" position="předcházející">
<div>Nějaký obsah před nadpisem</div>


Tento XPath odstraňuje atribut „x_airproof_header“ z hlavičky třídy. V tomto případě je
nepotřebují používat atribut „oddělovač“.

... kódový blok :: XML

<xpath expr="//hlavička" pozice="atributy">



Tento XPath přidává atribut třídy „x_airproof_header“ do hlavičky. Musíte také definovat
a atribut „oddělovač“, který přidá mezi třídu, kterou přidáváte, mezera.

... kódový blok :: XML

<xpath expr="//hlavička" pozice="atributy">
<attribut name="class" přidat="x_airproof_header" oddělovač=" "/>


Toto XPath posouvá prvek s třídou .o_footer_scrolltop_wrapper před prvek se stejnou třídou.
atribut ID „footer“.

... kódový blok :: XML

<xpath expr="//div[@id='footer']" position="before">
<xpath expr="//div[@id='o_footer_scrolltop_wrapper']" position="move" />


..tip:
Používání příkazů „move“ uvnitř jiného XPath vám neumožňuje používat žádné jiné příkazy.

...... příklad::
|  **Příklad dobrý:**

... kódový blok::xml

<xpath expr="//*[hasclass('o_wsale_products_main_row')]" position="before">
<xpath expr="//t[@t-if='opt_wsale_categories_top']" position="move" />
</xpath>
<xpath expr="//*[hasclass('o_wsale_products_main_row')]" position="before">
<div><!-- Obsah --></div>
</xpath>

| **Špatný příklad:**

... kódový blok::xml

<xpath expr="//*[hasclass('o_wsale_products_main_row')]" position="before">
<xpath expr="//t[@t-if='opt_wsale_categories_top']" position="move" />
<div><!-- Obsah --></div>
</xpath>


.. viz též:
Více informací o XPathu najdete na této „šikovné kartičce“ https://devhints.io/xpath.

... webových šablon / layoutu / qweb:

QWeb
====

QWeb je primární šablonovací motor používaný v Odoo. Jedná se o XML šablonovací motor, který se hlavně používá k
generovat fragmenty a stránky v HTML.

.. viz též:
:doc:`Dokumentace šablon QWeb <../../reference/frontend/qweb>.

.._webové šablony/layout/vlastní pole:

Vlastní pole
=============

Podle vašich potřeb můžete vytvořit pole pro ukládání dat do databáze.

.._webové šablony/vzhled/přizpůsobené pole/vyhláška:

Prohlášení
-----------

Nejprve vytvořte záznam k vyhlášení pole. To musí být propojeno s existujícím modelem.

... blok kódu::xml
:caption: „/webové stránky/vzduchotěsnost/data/pole.xml“

<záznam id="x_post_category" typu="ir.model.fields">
<pole název="název">x_post_category</pole>
<polozka name="název položky">...</polozka>
<položka name="ttype">html</položka>
<pole název="stát">manuální</pole>
<vlastnost jméno="index">0</vlastnost>
<field name="model_id" ref="webové stránky - blog.model_blog_příspěvek"/>
</záznam>

.. poznámka: Vytváření polí je také možné (a doporučováno) pomocí „modelu v Pythonu“ <developer/tutorials/backend>.

.. _webové šablony/layout/vlastní pole/back-end:

Back-end
--------

Přidejte pole do příslušného pohledu pomocí XPath. Proto uživatel může vidět pole v
připojit a naplnit později.

... blok kódu::xml
:podpis: „/webové stránky/zabezpečení proti vlhkosti/názory na webové stránce/blogy“

<zaznamenání id="zobrazit formulář pro kategorii blogu" typ="ir.ui.view">
<pole název="název">zobrazit formulář pro kategorii blogu</pole>
<field name="model">blog.post</field>
<položka název="dědit id" odkaz="webová stránka blog.zobrazit formulář pro příspěvek blogu"/>
<položka jméno="arch" typ="xml">
<xpath expr="//field[@name='blog_id']" position="before">
<políčko jméno="x_post_category" text="" placeholder="..."/>
</xpath>
</p>
</záznam>

.. /webové-šablony/vzhled/přizpůsobené pole/přední strana:

Front-end
---------

Hodnota pole může být zobrazena někde na stránce voláním modelu a pole, například takto:

... blok kódu::xml
:caption: „/webové stránky_vzduchotěsné/vyhledávání/webové stránky_blog_šablony.xml“

<h1 t-field="blog_post.x_post_category"/>

.. /webové šablony/vzhled/přední plán:

Pozadí
==========

Můžete definovat barvu nebo obrázek jako pozadí svého webu.

.._webové šablony/vzhled/předloha/barvy:

Barvy
------

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-color-palety: map-merge($o-color-palety,
      (
„voděodolný“:
„o-cc1-bg“: „o-barva-5“,
'o-cc5-bg':                   'o-barva-1',
         ),
       )
   );

... /webové šablony/vzhled/zadní obrázek:

Obrázek/vzor
-------------

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-webové-hodnoty-barevného-spektra:
      (
'tělesné vnímání': '/webové stránky/vzduchotěsnost/statické obrázky/zdroj/obrázek pozadí čar.svg',
„tělesný obraz“: „obrázek“ nebo „vzor“
      )
   );

... /webové-šablony/vzhled/hlavička:

Hlavička
======

Výchozí hlavička obsahuje dva odlišné šablony (pro desktop a pro mobilní zařízení), které zobrazují hlavní část stránky.
navigace, loga společnosti a další volitelné prvky (akce, jazykový výběr atd.).
Podle situace buď povolte nebo zakážete existující prvky pomocí standardního
šablonu nebo vytvořit zcela nový šablonový vzor.

... /webové-šablony/vzhled-hlavní stránky/standard:

Standard
--------

Odoo Web Builder rozlišuje mezi šablonami pro desktop a mobilní verzi, aby
usnadnit přizpůsobení uživatelského zážitku podle zařízení.

.._webové šablony/základní šablona pro desktop

Šablona pro stolní počítač
~~~~~~~~~~~~~~~~

Zapněte jeden z přednastavených šablon hlavičky.

.. důležité:
Nezapomeňte, že musíte nejprve vypnout aktivní šablonu hlavičky.

...... příklad::

... kódový blok::xml
:caption: „/webové stránky_aiproof/data/předvolby.xml“

<záznam id="webové stránky - šablona hlavičky výchozí" typu="ir.ui.view">
<pole název="aktivní" hodnota="false"/>
</záznam>

Ve souboru `primary_variables.scss` výslovně nastavte požadovaný šablonový soubor.

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-webové-hodnoty-barevného-spektra:
      (
„hlavička“: „Kontakt“,
      ),
   );

... blok kódu::xml
:předmět: „/webová_stránka_vzduchotěsná/data/prezentace.xml“

<záznam id="web.template_header_contact" typu="ir.ui.view">
<pole název="aktivní" hodnota="true"/>
</záznam>

... /webové-šablony/základní-vzhled/hlavička/standardní pro mobilní zařízení:

Mobilní šablona
~~~~~~~~~~~~~~~

Každý šablona hlavičky obsahuje šablonu „template_header_mobile“, která zajišťuje plynulé používání.
zkušenosti na všech zařízeních.

.. viz též:
`Mobilní šablona hlavičky v repozitáři Git Odoo <https://github.com/odoo/odoo/blob/43b20e6e52526c415e28c21810cd7023f6feef1e/addons/website/views/website_templates.xml#L354>`_.


... _webové šablony/základní stránka/hlavička/vlastní:

Obchodní zvyklost
------

Vytvořte si vlastní šablonu a přidejte ji do seznamu.

.. důležité:
Nezapomeňte, že nejprve musíte vypnout aktivní šablonu hlavičky.
vlastní.

**Volitelné**

Použijte následující kód pro přidání nové vlastní hlavičky na Webového stavitele.

... blok kódu::xml
:předmět: „/webové stránky_vzduchotěsné/views/webové šablony.xml“

<šablona id="šablona_hlavičky_opt" dědí_id="webová stránka. možnosti vložení" jméno="Šablona hlavičky - možnost">
<xpath expr="//we-select[@data-variable='header-template']" position="inside">
<tlačítko titulem="vzduchotěsnost"
data-customize-website-views="website_airproof.header"
data-customize-website-variable="'vzduchotěsné'"  data-img="/website_airproof/static/src/img/wbuilder/template_header_opt.svg"/>



.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * -Atribut
     - Popis
   * 
     - Šablona pro povolení
   * 
     - Jméno, které bylo přiděleno proměnné
   * 
     - Náhled vlastního šablony zobrazený při výběru šablon na Webové stránce

Nyní musíte explicitně definovat, že chcete používat svůj vlastní šablonový soubor ve verzi Odoo SASS.
proměnné.

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-webové-hodnoty-barevného-spektra:
      (
'hlavička šablony': 'vzduchotěsná',
      ),
   );

**Šablona**

... blok kódu::xml
:předmět: „/webové stránky_vzduchotěsné/views/webové šablony.xml“

<šablona id="hlavička" dědí id="webového layoutu" název="Airproof - Hlavička" aktivní="Pravda">
<xpath expr="//hlavička//navigace" pozice="vyměnit">
<!--Statické obsahy-->
<!-- Komponenty -->
<!--Editovatelné oblasti-->



Nezapomeňte upravit šablonu „template_header_mobile“ tak, aby byla konzistentní s desktop verzí.
a mobilní:

... blok kódu::xml
:caption: „webové stránky/vzory webových stránek.xml“


<!--XPathy-->


.. /webové šablony/základní stránka/hlavička/komponenty:

Součásti
----------

Ve vašem vlastním hlavičkovém šabloně můžete zavolat několik podšablon pomocí příkazu t-call z knihovny QWeb:

... /webové-šablony/základní-položka/hlavička/komponenty/logo/:

Logo
~~~~

... blok kódu::xml

<t t-call="website.placeholder_header_brand">
<t t-set="_link_class" t-valuef="..."/>


.. důležité:

Nezapomeňte vytvořit záznam o webové značce:ref:`<website_themes/media/images/use/logo>`.
logo v databázi.

.._webové šablony/layout/hlavičky/komponenty menu:

Menu
~~~~

... blok kódu::xml

<t t-foreach="web.menu_id.dite" t-as="podmenu">
<t t-call="website.submenu">
<t t-set="item_class" t-valuef="nav-item"/>
<t t-set="link_class" t-valuef="nav-link"/>
</t>


... /webové-šablony/základní-stavební-kamenná-vrstva/komponenty/přihlášení:

Přihlášení
~~~~~~~

... blok kódu::xml

<t t-call="portal.placeholder_user_sign_in">
<t t-set="_item_class" t-valuef="nav-item"/>
<t t-set="_link_class" t-valuef="nav-link"/>


.. /webové-šablony/layout/hlavička/komponenty/vyskakovací lišta uživatele:

Drodown menu uživatele
~~~~~~~~~~~~~

... blok kódu::xml


<t t-set="_user_name" t-value="true"/>
<t t-set="_icon" t-value="false"/>
<t t-set="_avatar" t-value="false"/>
<t t-set="_item_class" t-valuef="nav-item dropdown"/>
<t t-set="_link_class" t-valuef="nav-link"/>
<t t-set="_dropdown_menu_class" t-valuef="..."/>


... /webové-šablony/vzhled/hlavička/komponenty/vybírač jazyka:

Jazyková nabídka
~~~~~~~~~~~~~~~~~

... blok kódu::xml

<t t-call="website.placeholder_header_language_selector">
<t t-set="_div_classes" t-valuef="..."/>


... /webové-šablony/vzhled/hlavička/komponenty/cta:

Vyzývání k akci
~~~~~~~~~~~~~~

... blok kódu::xml


<t t-set="_div_classes" t-valuef="..."/>


.._webové šablony/základní stránka/hlavička/komponenty pro zobrazení nabídky:

Navigační lišta
~~~~~~~~~~~~~~

... blok kódu::xml

<t t-call="website.navbar_toggler">
<t t-set="_toggler_class" t-valuef="..."/>


.. viz též:
Můžete přidat :ref:`nadpisovou vrstvu <website_themes/pages/theme_pages/header_overlay>`, která umístí nadpis na obsah.
Vaší stránce. Musí se provést na každé stránce zvlášť.

... /webové-šablony/vzhled/patička/:

Patička
======

Výchozí obsah patičky je sekce s nějakým statickým obsahem. Můžete snadno přidat nové prvky
nebo vytvořte si svůj vlastní šablonu.

... /webové-šablony/základní-vzhled-patičky/:

Standard
--------

Povolte jeden z přednastavených šablon patičky. Nezapomeňte, že můžete muset vypnout aktivní
šablona patičky je první.

.. důležité:
Nezapomeňte, že je možná nutné nejprve vypnout aktivní šablonu pro patičku.

...... příklad::

... kódový blok::xml
:caption: „/webové stránky_aiproof/data/předvolby.xml“


<pole název="aktivní" hodnota="false"/>
</záznam>

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-webové-hodnoty-barevného-spektra:
      (
"šablona patičky": "Odkazy",
      ),
   );

... blok kódu::xml
:předmět: „/webová_stránka_vzduchotěsná/data/prezentace.xml“


<pole název="aktivní" hodnota="true"/>
</záznam>

... /webové-šablony/základní-složka/patička/vlastní:

Obchodní zvyklost
------

Vytvořte si vlastní šablonu a přidejte ji do seznamu. Nezapomeňte, že můžete muset deaktivovat
aktivní šablona patičky jako první.

**Volitelné**

... blok kódu::xml
:předmět: „/webové stránky_vzduchotěsné/views/webové šablony.xml“

<šablona id="šablona_patička_opt" dědí_id="webové stránky.soubor_možností" název="Šablona patičky - možnosti">
<xpath expr="//*[@data-variable='footer-template']" position="inside">
<tlačítko titulem="vzduchotěsnost"
data-customize-website-views="webová stránka_vzduchotěsná.patička"
data-customize-website-variable="'vzduchotěsnost'"
data-img="/webové stránky/AirProof/statické zdroje/obrázky/wbuilder/šablona patičky - opt.svg"/>



**Prohlášení**

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-webové-hodnoty-barevného-spektra:
      (
'footer-template': 'vzduchotěsný',
      ),
   );

**Šablona**

... blok kódu::xml
:podpis: „/webové_prostředí_neprůzvučné/výhledy/šablony webových stránek.xml“

<šablona id="patička" dědí id="webová šablona" název="Airproof - Patička" aktivní="Pravda">
<xpath expr="//div[@id='footer']" position="replace">
<div id="footer" třída="oe_struktura oe_struktura_solo" ignorujte="pravda" a pokud ne "nepřítomnost nohy">
<!--Obsah-->


</záznam>

... /webové-šablony/vzhled/autorská práva/:

Autorské právo
=========

V současné době je k dispozici pouze jeden šablonový vzor pro ochrannou známku.

Chcete-li nahradit obsah nebo změnit jeho strukturu, můžete přidat vlastní kód do následujícího XPath.

... blok kódu::xml
:podpis: „/webové_prostředí_neprůzvučné/výhledy/šablony webových stránek.xml“

<šablona id="copyright" dědí id="webové stránky.layout">
<xpath expr="//div[contains-class('o_footer_copyright')]" position="replace">
<div třída="o_footer_copyright" data-jméno="Copyright">
<!--Obsah-->

</xpath>


.. _webové šablony/layout/dropzone:

Pádová zóna
=========

Místo toho, abyste definovali celkový vzhled stránky, můžete vytvářet bloky (snippety).
Uživatelé si mohou vybrat, kam je přetáhnout a kde je umístit, což jim umožní vytvořit vlastní uspořádání stránky.
tento modulární design.

Můžete definovat prázdnou oblast, kterou uživatel může zaplnit kousky textu.

... blok kódu::xml

<div id="oe_structure_layout_01" class="oe_structure">

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * – třída
     - Popis
   * – oe_structure
     - Definujte oblast pro přetažení a pustění.
   * – oe_structure_solo
     - Do této oblasti lze vložit pouze jeden úryvek.
   * – oe_struktura_nejbližší
     - Pokud je blok vypuštěn mimo zónu s touto třídou, bude
Přesunuli se do nejbližšího drop zóny.

Můžete také naplnit stávající plochu s obsahem.

... blok kódu::xml

<šablona id="oe_struktura_layout_01" dědí id="..." název="...">
<xpath expr="//*[@id='oe_structure_layout_01']" position="replace">
<div id="oe_structure_layout_01" třída="oe_structure" třída="oe_structure_solo">
<!--Obsah-->

</xpath>


.. /webové šablony/vzhled/odpovídající:

Responzivní
==========

Odoo obecně staví na frameworku Bootstrap, který usnadňuje přizpůsobení webové stránky pro různé zařízení.
desktop a mobilních zařízení. Na verzi Odoo 16 se můžete hlavně zaměřit na tři aspekty:

#Automatické nastavení velikosti písma podle zařízení
#. Velikost sloupců na stolním počítači (sloupce jsou automaticky uspořádány na mobilních zařízeních).
#Zobrazit na desktopu/mobilu

.. viz též:
   - Dokumentace k Bootstrapu o vlastnosti zobrazení
<https://getbootstrap.com/docs/5.3/utilities/display/>

..._webové šablony/layout/responsivní/velikosti písma:

Velikosti písma
----------

Ve verzi Bootstrap 5 jsou písma automaticky nastavena na reaktivní velikost, takže se text může lépe přizpůsobit
při různých velikostech zařízení a rozlišeních (s ohledem na proměnnou `$enable-rfs`).

.. viz též:
   - Dokumentace Bootstrapu o odpovídajících velikostech písma
<https://getbootstrap.com/docs/5.3/getting-started/rfs/>

..._webové šablony/layout/responsivní/sloupce:

Velikosti sloupců
------------

Bootstrap používá strukturu řádků a sloupců k uspořádání stránky. Díky této struktuře lze vytvořit
může mít různé rozměry na mobilu a na stolním počítači. V této verzi umožňuje Website Builder nastavit
mobilních velikostí („col-12“ například) a stolních velikostí („col-lg-4“ například), ale ne
střední mezery („col-md-4“ například).

.. varování:
Střední velikosti lze nastavit, ale uživatel není schopen je upravovat v editoru Webové stránky.

.. viz též:
   - „Dokumentace Bootstrapu o reakčních bodech <https://getbootstrap.com/docs/5.3/layout/breakpoints/>“
   - „Dokumentace Bootstrapu o rozložení <https://getbootstrap.com/docs/5.3/layout/grid/>“

... _webové šablony/vzhled/responsivní/podmínky zobrazení:

Podmínky viditelnosti
---------------------

Ve webovém editoru Odoo lze skrýt celé sekce nebo konkrétní sloupce na mobilních i stolních počítačích.
Tato funkce využívá Bootstrap společně s třídami specifickými pro Odoo:

- „o_snippet_mobilní_neviditelný“
- „o_snippet_desktop_invisible“

Skrytí sekce na ploše počítače:

... blok kódu::xml

<section class="s_text_block o_cc o_cc1 o_colored_level pt16 pb16 d-lg-none o_snippet_desktop_invisible" data-snippet="s_text_block" name="Text">
<!--Obsah-->


Skrytí sloupce na mobilu:

... blok kódu::xml

<část třídy „s_text_block“ s atributy „o_cc“, „o_cc1“ a „o_colored_level“ s hodnotou „pt16“ a „pb16“ jménem „Text“>
<div class="container s_allow_columns">
<div class="row">
<div class="col-12 col-lg-6 d-none d-lg-block o_snippet_mobile_invisible">
Sloupec 1
</div>
<div class="col-12 col-lg-6">
Sloupec 2
</div>

</div>


.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * – třída
     - Popis
   * – o_snippet_mobile_invisible
     - Udává Webovému editoru, že prvek je skrytý a používá podmínky viditelnosti.
volba.
   * – o_snippet_desktop_invisible
     - Udává Webovému editoru, že prvek je skrytý **na desktopu a** používá viditelnost
podmínky.
   * –
     - Skryjte prvek v každé situaci.
   * – d-lg-block
     - Zobrazte prvek z „velkého“ rozhraní (na desktopu).

.. důležité:
„o_snippet_mobile_invisible“ a „o_snippet_desktop_invisible“ musí být uvedeny, aby se zabránilo
Zobrazovací podmínky jsou funkční. I když je prvek na desktopu skrytý,
Webový editor zobrazuje seznam těchto prvků, takže uživatel může vlastními silami zobrazit
prvek a upravit jej bez přepínání mezi mobilním a desktopovým režimem.

.... obrázek::layout/screenshot-visibility.png
:alt:Zobrazit skrytý prvek na aktuálním zařízení.
