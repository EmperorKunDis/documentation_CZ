=================================
Kapitola 3 – Základní nastavení
=================================

... /tutoriály/webový-vzhled/úpravy-část-1/vlastní-css/:

Přidejte vlastní SCSS
===============

Upravili jste proměnné Odoo a Bootstrapu a nastavili předvolby, přesto stále zaznamenáváte rozdíly
mezi vaším webem a návrhem klienta. Jediným řešením je začlenit vlastní SCSS.

V souboru `theme.scss` zopakujte následující prvky designu:

- Přidejte zelenou podtrženou linku na aktivní navigační položky.
- Upravte šipku pro skládací navigační položky.
- Upravte **přepínačové tlačítko** přidáním zeleného pozadí a změnou jeho vzhledu.

Různé „mediální“ zdroje najdete zde.
<{GITHUB_TUTO_PATH}/website_airproof/static/src/img/content/icons>.

.. viz též:
Podívejte se na odkazovanou dokumentaci, jak přidat své pravidla SCSS:

.. obrázek: 03_přizpůsobení_část1/menu.png
:scale: 50 %

.. obrázek: 03_přizpůsobení_část 1/slider.png

.. poznámka::
|Vždy je lepší zahrnout všechny vaše pravidla SCSS včetně ID #wrapwrap. Toto ID se aplikuje na
div, který seskupuje hlavičku, patičku a obsah hlavního panelu všech stránek.
Vaše stránky.
|Takže se můžete ujistit, že vaše pravidla budou mít vliv pouze na webové části.

..spoiler:: Řešení

Najděte řešení v našem příkladu Airproof v souboru header.scss

a souboru carousel.scss


... /návody/webové-téma/úprava/vlastní-javascript/:

Přidejte vlastní JavaScript
=============

Nyní přidáme myší sledovaný prvek na webovou stránku. Tento interaktivní prvek zvýší procházení
zkušenosti, čímž je interaktivnější a vizuálně atraktivnější.

.. obrázek: 03_přizpůsobení_část1/myš_sledovač.gif

Použijte své dovednosti v programování v JavaScriptu k realizaci této funkce.

.. viz též:
Podívejte se na dokumentaci, jak :ref:`přidat javascriptový kód <theming/assets/interactivity>`.

..spoiler:: Řešení

Najděte řešení v našem příkladu Airproof na souboru mouse_follower.js
<{GITHUB_TUTO_PATH}/website_airproof/static/src/js/mouse_follower.js> a <{GITHUB_TUTO_PATH}/website_airproof/static/src/sass/mouse_follower.scss
<{GITHUB_TUTO_PATH}/website_airproof/static/src/scss/components/mouse_follower.scss>.

.. _návody/vzhled webu/přizpůsobení část 1/přizpůsobit hlavičku:

Vytvořte vlastní hlavičku
======================

S proměnnými, přednastaveními a vlastním SCSS je čas upravit uspořádání a přidat klíčová slova.
křížové prvky, začínající hlavičkou.

Založte si vlastní hlavičku na základě návrhu Airproof s těmito prvky:

- Logo uprostřed. Ujistěte se, že deklarujete logo tak, aby se automaticky zobrazilo v hlavičce.
- Nastavitelný obrázek nákupního košíku.
- Tlačítko pro přihlášení/uživatele.
- Navigační text na 14 px.

Můžete najít logo
<{GITHUB_TUTO_PATH}/website_airproof/static/src/img/content/branding/airproof-logo.svg>
`<{GITHUB_TUTO_PATH}/website_airproof/static/src/img/content/icons/shopping.svg>`
Šablona ilustrace
<{GITHUB_TUTO_PATH}/website_airproof/static/src/img/wbuilder/template-header-opt.svg>.

.. viz též:
Podívejte se na odkazovanou dokumentaci, jak postupovat:

   - vytvořit vlastní hlavičku:ref:`<webové téma/layout/hlavička/vlastní>
   - do sekce „webové šablony / uspořádání / XPath“.
   - deklarovat :ref:`webové šablony/mediální obrázky/použití/logo`.

.. obrázek: 03_přizpůsobení_část 1/hlavička.png

..tip:
   - Postavte se na kód existujících šablon hlaviček, které najdete v
'odoo/addons/webové stránky/zobrazení/vzorce webových stránek.xml
<{GITHUB_PATH}/addons/website/views/website_templates.xml>.
   - Dobrou praxí je vytvářet různé soubory, abyste mohli spravovat své vlastní pohledy a šablony.
Například vše co se týká obecného uspořádání (hlavička, patička...).
:souboru website_templates.xml, vše související s blogem v souboru website_blog_templates.xml,
události v souboru :file:`website_event_templates.xml`, atd.
   - |Pro úpravu ikony košíku můžete použít XPath.
|Odkazujte na e-commerce, umístěte jej do nového souboru s názvem
:file:`webové-prodejní-šablony.xml“.
   - Nezapomeňte pokračovat v tom, co jste začali, a udělat co nejvíce změn.
proměnných a :file:`primárních proměnných` (písmo, barvy, velikost ...). Můžete je používat k tomu, abyste se při psaní
s touto cvičení.

..spoiler:: Řešení

Najděte řešení v našem příkladu Airproof pro:

   - struktura XML a přidat šablonu do seznamu možností.
`webovou šablonu.xml <{GITHUB_TUTO_PATH}/website_airproof/views/website_templates.xml>`.
   - vypnout výchozí hlavičku:

... kódový blok:: xml
:caption: „/webová_stránka_vzduchotěsná/data/prezentace.xml“


<záznam id="webová stránka - šablona hlavičky výchozí" typu="ir.ui.view">
<pole název="aktivní" hodnota="false"/>


   - zaznamenat logo:

... kódový blok:: xml
:popisek: „/webové stránky/vzduchotěsnost/data/obrázky.xml“

<!--Nastavte jako logo webu-->
<záznam id="web.výchozí web" typu="web">
<pole jméno="logo" typ="base64" soubor="webová stránka/airproof/statické/zdrojové obrázky/obsah/branding/airproof-logo.svg"/>


   - deklarujte soubor `website_templates.xml` společně s novými v celém vašem
:soubor: manifest.
   - Vypněte možnosti, které nechcete mít ve svém záhlaví pomocí příkazu
<{GITHUB_TUTO_PATH}/website_airproof/data/presets.xml>.
   - používání „primárních voleb
<{GITHUB_TUTO_PATH}/website_airproof/static/src/scss/primary_variables.scss>
„šablona hlavičky“, „písmo pro navigační lištu“, „velikost písma hlavičky“…
   - použít bootstrapping_override
<{GITHUB_TUTO_PATH}/website_airproof/static/src/sass/bootstrap_overridden.scss>
`$navbar-light-color`, `$navbar-light-hover-color`, `$navbar-padding-y`...
   - přidejte nějaký „sass <{GITHUB_TUTO_PATH}/website_airproof/static/src/sass/layout/header.sass>“
pravidla.

... _návody/webová_šablona/úprava/vlastní_základna:

Vytvořte vlastní zápatí
======================

Klient je nadšený z nového loga, protože dokonale ladí s předloženým návrhem.
Chce vlastní šablonu pro záhlaví.

Na základě návrhu Airproof vytvořte vlastní patičku s následujícími prvky:

- Oddíl pro odběr newsletteru.
- Sekce pro autorská práva a sociální média.

Ikony najdete zde <{GITHUB_TUTO_PATH}/website_airproof/static/src/img/content/icons>

.. viz též:
Podívejte se na dokumentaci k vytvoření vlastního zápatí
a přizpůsobit kopírování webu podle tématu „webové šablony/layout/kopírování“.

.. obrázek: 03_přizpůsobení_část 1/zápatí.png

..tip:
   - Můžete zapnout nebo vypnout část o autorských právech pomocí předvoleb.
   - Pro funkci zpravodaje je nutné nainstalovat aplikaci „Webová masová pošta“.

..spoiler:: Řešení

Abychom mohli tento úkol dokončit, musíme:

   - Přidejte závislost „masová pošta“:

... kódový blok: Python
:popisek: „/website_airproof/__manifest__.py“

„závisí“: ['webová stránka prodeje', 'webová stránka prodeje seznam přání', 'webová stránka blogu',
['webová stránka masového rozesílání e-mailů']

   - naleznete strukturu XML a přidáte šablonu do seznamu možností
`webovou šablonu.xml <{GITHUB_TUTO_PATH}/website_airproof/views/website_templates.xml>`.
   - Vypněte výchozí patičku a zapněte autorská práva:

... kódový blok:: xml
:caption: „/webová_stránka_vzduchotěsná/data/prezentace.xml“



<pole název="aktivní" hodnota="false"/>


<záznam id="webová stránka.základní informace bez autorských práv" typu="ir.ui.view">
<pole název="aktivní" hodnota="false"/>


   - používání „primárních voleb
<{GITHUB_TUTO_PATH}/website_airproof/static/src/scss/primary_variables.scss>
„šablona patičky“, „patička“, „odkaz na CC 4.0“...
   - Přidejte si malý CSS pravidlo pro newsletter.
v sekci „<{GITHUB_TUTO_PATH}/website_airproof/static/src/scss/snippets/newsletter.scss>“.

... /návody/webové-téma/úprava/vlastní-bloky:

Vytvořte si vlastní stavební bloky
==================================

Aby váš klient mohl svůj web dále upravit, vytvořte šablony, které jsou přizpůsobené jeho potřebám.
Můžete je libovolně přetahovat a vkládat na různé stránky.

Na základě návrhu Airproof vytvořte vlastní šablonu pro ukazování dronů. Pak ji přidejte jako
záložku na hlavní stránce.

#Vytvořte šablonu snímku a přidejte ji do seznamu stavebních bloků dostupných na webu.
stavitel. Zde najdete obrázky

„ilustrace vtipu“
<{GITHUB_TUTO_PATH}/website_airproof/static/src/img/wbuilder/s-airproof-snippet.svg>.

......viz také::
Podívejte se na odkazovanou dokumentaci, jak vytvořit vlastní bloky.
<webové_šablony/bloky/vlastní>.

... obrázek: 03_zákaznická úprava část 1/vlastní stavební blok.png

#Přidejte možnost v Editoru webových stránek, která umožní uživatelům vybrat mezi modrou nebo zelenou bublinou.
stín.

......viz také::
Podívejte se na odkazované dokumentace, jak přidat možnosti :ref:`snippetu
<webové šablony/bloky/vlastní/možnosti>.

.... obrázek: 03_customizace_část1/vlastní stavební blok - možnost.png
:skalka: 75 %

#Přidejte kousek na svou domovskou stránku.

..tip:
Nezapomeňte vždy správně deklarovat nové soubory ve svém souboru ``.py`` __manifest__.py a dodržet
dobré: struktura složek, kterou jsme viděli dříve.

..spoiler:: Řešení

Abychom mohli tento úkol dokončit, musíme:

   #Vytvořte si vlastní šablonu.

      - Všechny potřebné informace najdete v souboru s_airproof_carousel.xml
souboru „<{GITHUB_TUTO_PATH}/website_airproof/views/snippets/s_airproof_carousel.xml>“
`s_airproof_carousel/000.scss

soubor z našeho příkladového modulu.
      - Uložte své obrázky do souboru „images.xml“ v adresáři „{GITHUB_TUTO_PATH}/website_airproof/data/images.xml>“.
      - Prohlášte své soubory v souboru __manifest__.py
<{GITHUB_TUTO_PATH}/website_airproof/__manifest__.py>`.
      - Přidejte ho do seznamu stavebních bloků. V našem případě takto:

... kódový blok::xml
:podpis: „/webová_stěna_vzduchotěsná/vyhledávání/součásti.xml“

<!-- Přidejte vlastní šablony do konstruktéra -->
<šablona id="vzorky" dědí id="webová stránka. vzorky" název="Airproof - Vlastní vzorky">
<xpath expr="//*[@id='default_snippets']" position="before">


<div class="o_panel_header">Airproof</div>



t-thumbnail="/web/airproof/static/src/img/wbuilder/s-airproof-snippet.svg">





</xpath>


   #Přidejte možnost do Webového editoru. V našem příkladu takto:

... kódový blok::xml
:podpis: „/webové stránky_vzduchotěsné/views/snippety/s_vzduchotěsnost_kolo.xml“

<!--Přidat možnosti pro vložené kousky textu-->
<šablona id="snippet_options" dědí id="website.snippet_options" jméno="Airproof -
Možnosti Snippetů">
<xpath expr=".">
<!-- *** Snippet kolotoče : modrá nebo zelená bublina *** -->
<div data-selector=".x_bubble_item">
<tlačítko-skupina string="Stín bubliny">
<we-button data-select-class="x_bubble1">Modrá</we-button>

</we-button-group>
</div>
</xpath>


Další soubor SCSS se týká bublin v souboru s_airproof_carousel/000.scss
souboru v adresáři _<{GITHUB_TUTO_PATH}/website_airproof/static/src/snippets/s_airproof_carousel/000.scss>_.

   #Přidejte svůj kousek do domovské stránky. Všechny potřebné informace najdete v souboru home.xml
souboru _<{GITHUB_TUTO_PATH}/website_airproof/data/pages/home.xml}>_ z našeho příkladového modulu.

... _tutorials/website_theme/customization_part1/custom_dynamic_template:

Vytvořte nový šablonu dynamických odkazů
======================================

Dynamické fragmenty jsou užitečné stavební bloky. Tyto umožňují získat informace ze serveru
a zobrazit je na webu podle určitých filtrů.
|Na výběr máte již několik šablon pro zobrazení dynamických kousků.
Existující šablony plně vyhovují potřebám vašeho klienta.

Na základě návrhu společnosti Airproof vytvořte vlastní šablonu, kterou aplikujete na produktový dynamický obrázek.
ukázka na domovské stránce.

#Nejprve vytvořte vlastní šablonu, která bude přidána do seznamu dynamických šablon produktů.
musí obsahovat následující prvky:

   - Přidejte odkaz „Zjistěte více“.
   - Přidejte efekt přejetí myší na karty.
   - Přesuňte navigační šipky.

Ikony najdete zde <{GITHUB_TUTO_PATH}/website_airproof/static/src/img/content/icons>_.

......viz také::
Podívejte se na dokumentaci k tématu, jak vytvořit šablonu pro dynamické fragmenty
<webové_šablony/bloky/vlastní/dynamické>.

.. obrázek: 03_zákaznický_design_část_1/vlastní šablona.png

......tip:
Můžete si ověřit v Editoru webových stránek, že váš šablona je uvedena mezi dostupnými.
šablony pro dynamický produktový proužek.

#Poté přidejte produktový dynamický štítek s vytvořeným šablonou na domovskou stránku.

......viz také::
Podívejte se na odkazované dokumentace, jak :ref:`volat šablonu
<webové_šablony/bloky/vlastní/dynamické/volání>.

..spoiler:: Řešení

Abychom mohli tento úkol dokončit, musíme:

   #Vytvořte si vlastní šablonu sestavy. Vše potřebné najdete na
`soubor options.xml (cesta {GITHUB_TUTO_PATH}/website_airproof/views/snippets/options.xml)`
souboru a souboru „carousel.scss
souboru <{GITHUB_TUTO_PATH}/website_airproof/static/src/scss/snippets/caroussel.scss>.
příklad modulu.

   #Použijte šablonu na dynamický prvek produktu v záhlaví. Můžete najít všechny
potřebné informace v souboru home.xml
souboru _<{GITHUB_TUTO_PATH}/website_airproof/data/pages/home.xml}>_ z našeho příkladového modulu.
