===================
Kapitola 1 – Tematizace
===================

Nyní, když máte nainstalovaný Odoo a váš server běží lokálně, je čas vytvořit svůj vlastní
motivový modul pro váš web.

.. _návody/webové téma/tématické nastavení:

Nastavení
=====

Prvním krokem je zajistit, aby Odoo fungovalo správně na místní úrovni. K tomu použijte skript v Shellu
aby mohl server běžet.
|V tomto skriptu definujte název databáze a nainstalujte pouze modul „webová stránka“.

.. viz též:
Podívejte se na odkazovanou dokumentaci, jak postupovat při spuštění Odoa.

... _návody/webový_vzhled/témata/moduly:

Postavte si svou strukturu modulu
===========================

Teď, když víme, že vše funguje správně, můžeme začít stavět náš modul.

Na základě následující struktury začněte vytvářet svůj modul, který bude sloužit jako téma.
kde budete přidávat své XML stránky, SCSS, JS, ...

.. viz též:
Podívejte se na odkazované dokumentace, jak strukturovat svůj :ref:`vzhled/modul`.

Začněte základy: souborů „/data“, „/img“, „/scss“ a „/js“.
|Nezapomeňte přidat soubory :file:`__init__.py` a :file:`__manifest__.py`.

V souboru __manifest__.py můžete svůj modul deklarovat následujícími informacemi:

- jméno (povinné)
- Popis
- kategorie
- verze
- autor
- licence
- závisí

... _tutorialy/webová_šablona/tematizace/odoo_proměnné:

Prohlásit proměnné Odoo
======================

V souboru `primary_variables.scss` můžete přehrát výchozí proměnné SCSS v Odoo.
přizpůsobit svůj návrh.

Založte si soubor „primary_variables.scss“ podle návrhu Airproof a definujte
následujících prvků:

- Písmo titulku: Space Grotesk
- Rodina písem: Lato
- Název barevné palety a 5 hlavních barev, které ji tvoří: `#000000`, `#BBE1FA`,
'#FFFFFF', '#0B8EE6'
- Hlavička a patička: V tuto chvíli použijte jeden z předdefinovaných šablon, později vytvoříme vlastní hlavičku.
Later.

.. viz též:
Podívejte se na odkazované dokumentace k použití proměnných primárních:ref:`<theming/module/variables>`.
stejně jako seznam všech „primárních proměnných
<{GITHUB_PATH}/addons/website/static/src/scss/primary_variables.scss> je k dispozici.

| Restartujte svůj skript, abyste ihned viděli aplikaci změn.
|Nezapomeňte přidat cestu k manifestu do skriptu a nastavit modul jako aplikaci
aby je bylo možné nainstalovat.

Aby byly vaše změny provedeny správně, přihlaste se do svého webu a zkontrolujte, že
barvová paleta zahrnuje vaše specifikované barvy.

..tip:
Budete muset přepsat více proměnných, abyste mohli napodobit návrh Airproofu. Pamatujte na jejich přidání
během celého procesu tvorby webových stránek.

.. poznámka::
Písmová rodina je z Google Fonts <https://fonts.google.com/>.

..spoiler:: Řešení

Abychom mohli tento úkol dokončit, musíme:

   #Vytvořte soubor `primary_variables.scss`. Všechny potřebné informace najdete
„primární proměnné.scss
<{GITHUB_TUTO_PATH}/website_airproof/static/src/sass/primary_variables.scss> souboru z našeho
příklad modulu.
   #Prohlášení souboru v souboru __manifest__.py, jak je uvedeno v dokumentaci.
   #Nainstalujte svůj modul pomocí vašeho skriptu. V našem příkladu vypadá takto:

... kódový blok :: XML

      ./odoo-bin --addons-path=../enterprise,addons,../myprojects --db-filter=theming -d theming
--bez-demonstrace všechny -i webová stránka_vzduchotěsná --pro vývojáře XML

... /tutoriály/webové-téma/vzhled/proměnné-bootstrapu/:

Prohlásit proměnné Bootstrap
===========================

Kromě výchozích proměnných Odoo můžete také předefinovat proměnné Bootstrapu. Bootstrap je
front-endový rámec, který je součástí Odoo.

Na základě návrhu Airproof definujte tyto prvky:

- Velikosti písma nadpisů:

  - h1: 3,125rem
  - h2: 2,5 rem
  - h3: 2rem
  - h4: 1.75rem
  - h5: 1,5rem
  - h6: 1.25rem

- Rozměr okraje vstupu: 10 px
- Barva okrajů vstupu: černá
- Šířka hrany vstupu: 1 pixel
- Velké tlačítko s poloměrem rohů 0 px, 10 px, 10 px a 10 px

.. viz též:
   - Podívejte se na odkazované dokumentace, jak používat :ref:`theming/module/bootstrap`.
   - Seznam všech proměnných Bootstrap
používané v Odoo.
   - A „Rámec Bootstrapu <https://getbootstrap.com/docs/4.6/getting-started/introduction/>“
oficiální dokumentace.

..tip:
   - Budete muset přehrát více proměnných, abyste mohli napodobit návrh Airproof. Pamatujte na ně
po celou dobu tvorby vašich webových stránek.
   - Zvykněte si pravidelně kontrolovat, zda byly vaše změny úspěšně aplikovány
a nezpůsobily žádné chyby.

..spoiler:: Řešení

Abychom mohli tento úkol dokončit, musíme:

   #Vytvořte soubor:file:`bootstrap_overridden.scss`. Všechny potřebné informace najdete
v souboru `bootstrap_overridden.scss
souboru <{GITHUB_TUTO_PATH}/website_airproof/static/src/scss/bootstrap_overridden.scss>
náš příkladový modul.
   #Prohlášení souboru v souboru __manifest__.py, jak je uvedeno v dokumentaci.

... _návody/webový_vzhled/témata/předvolby:

Definujte předvolby
==============

Kromě proměnných, které jsme právě probrali, můžete také aktivovat konkrétní pohledy a upravit
design.

Přidejte soubor presets.xml a podle návrhu Airproofu zapněte příslušné pohledy
abyste vyhověli následujícím požadavkům klientů:

- Vypněte Call-to-action v hlavičce.
- Vypněte funkci seznamu přání v obchodě, ale aktivujte ji na stránce produktu.
- Na stránce s obchodem aktivujte filtrování pouze v levém sloupci.

.. viz též:
|Podívejte se, jak můžete definovat své :ref:`předvolby <theming/module/views/presets>`.
|Chcete-li začít psát svůj soubor, postupujte podle pokynů pro jakoukoli stránku XML v Odoo popsaných v
:doc:`/rozvoj/jak-na-to/webové-šablony/layout`.

..tip:
   - K dokončení cvičení je potřeba nainstalovat e-commerce (webová prodejna) a
**seznam přání** (webové stránky prodeje seznamu přání) aplikace. **Budete muset být opatrní!** Odkazování na
pokud se v kódu objeví aplikace, která nebyla nainstalována, dojde k chybě.
   - | Chcete-li najít šablony pro aktivaci nebo deaktivaci, přejděte do zdrojového kódu:
„odoo/addons/website/views/*“.
| Například všechny šablony pro hlavičku najdete v
`webové šablony.xml <{GITHUB_PATH}/addons/website/views/webové šablony.xml>`.
   - Pro zobrazení účinku vašich předvoleb přidejte nějaké produkty (Airproof Mini, Airproof Robin).
*Záruka*, *Nabíjecí kabel*) a vytvořit **kategorie e-commerce** (*Záruky*, *Příslušenství*,
a v databázi najdete i „Drony“ s podkategoriemi „Kamery na drony“ a „Voděodolné drony“.
„Obrázky produktů zde <{GITHUB_TUTO_PATH}/website_airproof/static/src/img/content>“.
   - Pokud chcete dosáhnout stejného vzhledu jako u Airproof, budete potřebovat více zobrazení. Pamatujte na přidání
po celou dobu tvorby vašich webových stránek.

..spoiler:: Řešení

Chcete-li vypnout tlačítko „Přijmout“:

   #Výhled, který musíte najít, je v souboru: `odoo/addons/website/views/website_templates.xml l:2113`.
   #Vytvořte soubor s názvem „presets.xml“ se správnými záznamy

... kódový blok::xml
:popisek: „/webové stránky/airproof/data/presety.xml“


<odoo>
<!-- Deaktivujte volání k akci v hlavičce.
<záznam id="webová hlavička - výzva k akci" typu="ir.ui.view">
<pole název="aktivní" hodnota="false"/>


   #V manifestu přidejte oba aplikace a deklarujte svůj soubor.

... kódový blok: Python
:popisek: „/website_airproof/__manifest__.py“

'závisí na': ['prodej webu', 'seznam přání webu']
"data": [
            # Možnosti
"data/předvolby.xml",
         ]
