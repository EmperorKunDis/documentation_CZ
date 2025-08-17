==============================
Kapitola 2 – Vytvořte svůj web
==============================

... /tutoriály/webový-vzhled/postavit-webovou-stránku/stránka:

Vytvořte stránku
=============

Nyní, když je téma nastaveno, pojďme se podívat na vytváření obsahu.

Nejprve si vytvořte první téma stránky: domovskou stránku. Prozatím jen uveďte „Ahoj“.
jako obsah stránky.

..tip:
Musíte vypnout výchozí domovskou stránku.

.. viz též:
Podívejte se na odkazované dokumentace, jak deaktivovat výchozí stránku
<webové šablony/stránky/výchozí> a jak začít novou stránku
<webové šablony/stránky/šablona stránek>.

..spoiler:: Řešení

... kódový blok:: python
:popisek: „/website_airproof/__manifest__.py“

"data": [
            # Stránky
‚data/stránky/domov.xml‘,
         ]

... kódový blok :: XML
:caption: „/webová_stěna_vzduchotěsná/data/stránky/domov.xml“


<odoo noupdate="1">
<!--Deaktivace výchozí domovské stránky-->
<záznam id="webová stránka.domovská stránka" typu="ir.ui.view">
<pole název="aktivní" hodnota="false"/>
</záznam>

<záznam id="stránka_domovská" typu="web.stránka">
<polozka name="název">Domov</polozka>
<vlastnost jméno="je publikována" hodnota="Pravda"/>
<položka jméno="klíč">web_vzduchotěsný.stránka_domovská</položka>
<pole název="url">/</pole>
<položka typu="qweb" />
<položka jméno="arch" typ="xml">
<t t-name="web_vzduchotěsné.stránka_domovská">


<t t-set="additional_title">Kousek za obzorem | Airproof</t>
<!--Obsah-->



</t>
</t>
</položka>
</záznam>
</odoo>

... /tutoriály/webové-téma/vytvoření-webu/multimédia:

Přidejte médium
===========

Pokud chcete, aby si klient mohl vybrat určité fotografie, které do svého profilu přidáte
webové stránky musí být přidány do knihovny obrázků.

Pro vykonání testu je nutné prohlásit dronovou fotografii a přidat ji do knihovny. Najdete ji pod názvem „Dronová fotografie
tady <{GITHUB_TUTO_PATH}/website_airproof/static/src/img/content/drone-robin.png>.

.. viz též:
Podívejte se na odkazovanou dokumentaci, jak přidat média :ref:`<website_themes/media/images>`.

Přejděte na Webového stavitele, dvojklikem na logo se dostanete k
dronovou fotografii v knihovně.

..spoiler:: Řešení

Abychom mohli tento úkol dokončit, musíme:

   #Uložte svůj PNG do správné složky obrázků.
   #Vytvořte soubor `images.xml`. Všechny potřebné informace najdete
v souboru images.xml
<{GITHUB_TUTO_PATH}/website_airproof/data/images.xml>
soubor z našeho příkladového modulu.
   #Prohlášení souboru v souboru: __manifest__.py.

... _návody/webové šablony/vytvoření webu/stavební bloky:

Přidejte stavební bloky.
===================

Teď se pustíme do skutečné práce. Začneme přidávat obsah na stránky.

Na webu Odoo vytváříme obsah stránky pomocí bloků. Ty lze přirovnat k
úryvky, které může uživatel upravit v editoru webových stránek. Standardní hlavní kontejner pro jakýkoli úryvek
Je to „oddíl“.

Na hlavní stránku přidejte následující prvky podle návrhu Airproof:

- Vytvořte sekci s třemi boxy pomocí bloku „Velké boxy“.

  - Pro tuto část nechcete, aby uživatel mohl upravovat obsah pomocí Webového editoru.
  - Nastavte na pozadí obrázku tří boxů filtr průhlednosti.

- Vytvořte další sekci s názvem a ikonami.

Můžete používat tyto „obrázky“ a „ikonky“
<{GITHUB_TUTO_PATH}/website_airproof/static/src/img/content/icons>.

.. viz též:
Podívejte se na odkazovanou dokumentaci, jak napsat standardní vzorek
<webové šablony/bloky/vzhled>.

.. obrázek: 02_vytvorit_web/bloky.png
:alt:Stavební bloky vzduchotěsné.
:skalka: 75 %

..tip:
Pro určení kódu potřebného k vytvoření vašich základních stavebních kamenů:

   - Vytvořte testovací stránku pomocí webového editoru.
|Přetáhněte a pusťte na místo, které vás zajímá, a aplikujte správný návrh.
|Vložte kód vygenerovaný v Editoru HTML/SCSS v nabídce.
   - Můžete také najít původní blokový kód v Odoo:
:soubor: `odoo/addons/website/views/snippets/*.xml`.

..spoiler:: Řešení

Najděte řešení v našem příkladu Airproof v souboru home.xml


... _návody/webový_vzhled/postavit_web/navigace:

Navigace
==========

Zatím je klient spokojen s výchozími hlavičkami, ale požádal o několik úprav navigace.

Klient požaduje následující změny:

- Odstraňte odkaz na domovskou stránku a obchod.
- Přidejte odkaz na budoucí stránku „O nás“.
- Nahraďte výchozí položku blogu tlačítkem s rozbalovacím seznamem, ve kterém budou zobrazovány různé blogy: „Naše nejnovější zprávy“
a „Návody“.
- Přidejte megamenu „Vodotěsné drony“ pro zobrazení různých produktů.

.. viz též:
   - Originální šablony menu najdete v Odoo:
`odoo/addons/website/views/snippets/s_mega_menu_**.xml
<{GITHUB_PATH}/addons/website/views/snippets>
   - Podívejte se na odkazovanou dokumentaci, jak změnit
:doc:`/rozvoj/jak-na-to/webové-tematické-navigace/navigace.

.. obrázek: 02_postavit_webovou_stránku/mega-menu.png
:alt: Mega menu od Aiproofu.

..tip:
   - Ujistěte se, že je aplikace Blog nainstalovaná a vytvořte dvě různé blogy na zadní straně.
   - Vytvořte různé produkty v administraci. Můžete použít tyto „obrázky produktů“.
<{GITHUB_TUTO_PATH}/website_airproof/static/src/img/content>`.

..spoiler:: Řešení

Najděte řešení v našem příkladu Airproof ve souboru menu.xml
<{GITHUB_TUTO_PATH}/website_airproof/data/menu.xml>.
