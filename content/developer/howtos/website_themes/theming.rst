=======
Tematizace
=======

Po dokončení vývojového prostředí můžete začít stavět kostru své
Tématický modul. V tomto kapitole se dozvíte, jak:

- Zapněte nebo vypněte standardní možnosti a šablony webového editoru.
- Určete barvy a písmo, které budou použity ve vašem návrhu.
- Využijte maximum ze proměnných Bootstrapu.
- Přidejte vlastní styly a JavaScript.

.. téma/modul:

Téma
============

Odoo je dodáván s výchozím tématem, které poskytuje minimální strukturu a uspořádání. Když vytvoříte nový
téma, které rozšiřuje výchozí téma.

Nezapomeňte přidat adresář, ve kterém je umístěn váš modul, do příkazového řádku s parametrem „addons-path“.
při běhu Odoa ve vývojovém prostředí.

... tématu, modulu a názvu:

Technické pojmenování
----------------

Prvním krokem je vytvoření nové složky.

... blok kódu::xml

webová stránka_vzduchotěsná

.. poznámka::
Před něj přidejte prefix „website_“ a použijte pouze malá písmena ASCII alfanumerické znaky a podtržítka.

V této dokumentaci budeme používat projekt Airproof (smyšlený příklad).

… téma, modul, struktura:

Struktura souborů
--------------

Témata jsou zabalena jako každý modul v Odoo. I když navrhujete základní webovou stránku, budete potřebovat
zpracovat své téma jako modul.

::

webová stránka proti vlhkosti
├── data
└── i18n
└── statické
│   ├── popis
│   └── fonts
│    ├── lib
│   │   └── shapes // Tvar pro pozadí
│   └── src
│        └── img
│       │   ├── content // Pro ty, které používáte na stránkách vašich webových stránek
│  │   │ └── wbuilder // Pro ty, které se používají v budovatelích
│       └── js
│         └── scss // Styl specifický pro téma
│        └──snippety // vlastní snippet
│ ├── views
├── __init__.py
└── __manifest__.py

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * -Složka
     - Popis
   * – data
     - Předvolby, menu, stránky, obrázky, tvary, ... (`.xml`)
   * 
     - Překlady („*.po“, „*.pot“)
   * –
     - Externí knihovny („*.js“)
   * - statický
     - Vlastní soubory („*.jpg“, „*.gif“, „*.png“, „*.svg“, „*.pdf“, „*.scss“, „*.js“)
   * – názory
     - Vlastní pohledy a šablony (`.xml`)

..._tematizaci/modul/základní inicializaci:

Inicializace
--------------

Odoo modul je také balíček v Pythonu s souborem __init__.py, který obsahuje import
návodů pro různé soubory v modulu. Tento soubor může zůstat prázdný.


... tématu/modulu/deklaraci:

Prohlášení
-----------

Modul v Odoo je deklarován pomocí souboru manifestu. Tento soubor deklaruje Pythonový balík jako modul Odoo
modul a specifikuje metadatový záznam modulu. Musí obsahovat alespoň pole „název“, které je
Je vždy požadována a obvykle obsahuje mnohem více informací.

... kódový blok:: python
:caption: „/webová_stránka_vzduchotěsná/__manifest__.py“

   {
„název“: „Airproof Theme“,
'popis': '...'
'kategorie': 'Webové stránky/Šablona',
„verze“: „{BRANCH}.0“,
'autor': '...'
'licence': '...',
'závisí na webu': ['webová stránka']
"data": [
         # ...
      ],
"aktiva": {
         # ...
      },
   }

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * – Hřiště
     - Popis
   * - jméno
     - Čitelný název modulu (nutné)
   * Popis
     - Doplněná popis modulu v reStrukturovaném textu
<https://cs.wikipedia.org/wiki/ReStructuredText>
   * kategorie
     - Kategorie třídění v Odoo
   * – verze
     - Verze Odoo, na kterou se tento modul vztahuje
   * Autor
     - Jméno autora modulu
   * Licence
     - Výchozí licencí je LGPL 3. Více informací v souboru :ref:`manifest
stránce „Odkaz / modul / manifest“.
   * – záleží
     - Moduly Odoo musí být načteny před tímto modulem, buď proto, že tento modul využívá funkce
nebo proto, že mění zdroje, které definují.
   * – data
     - Seznam souborů XML
   * aktiva
     - Seznam souborů SCSS a JS

.. poznámka::
    - Struktura složek výše je pouze návrhem. Můžeme přidat takové množství dalších složek, jaké potřebujeme.
projektu, například do složky /controllers pro kontroly nebo /views/backend pro zadní část.
názory, atd.
    - Pro vytvoření šablony webu stačí nainstalovat aplikaci Webové stránky. Pokud potřebujete další aplikace
(blogy, události, elektronický obchod atd.) můžete je také přidat.
    - Verze a hlavní číslo jsou povinné. Patchové číslo je však volitelné. Pokud chcete
abyste specifikovali požadovanou verzi Odoo pro běh vašeho modulu, použijte pět argumentů
struktura, použijte první dva argumenty k označení vaší aktuální verze Odoo („* = {BRANCH}“).

.. obrázek:: theming/versioning.png
:alt: Verze modulu
:šířka: 300

Příklad:
{BRANCH}.1.0.0
`odoo_major.odoo_minor.modul_major.modul_minor.modul_patch`

.. varování:
Automatické zahrnutí souborů pomocí divokých karetových zápisů (např. /myfolder/*.scss) nefunguje
Odoo databáze jako služba (SaaS). V tomto případě musíte každý soubor ručně přidat do manifestu.

...Téma/volby:

Výchozí možnosti
===============

Nejprve se pokuste vytvořit svůj motiv pomocí výchozích možností Odoo. To zajistí dvě věci:

#Nevynalézáte něco, co už existuje. Například Odoo nabízí možnost
Pokud chcete přidat hranu na záhlaví, neměli byste si ji upravovat sami. Místo toho zapněte výchozí možnost
Nejprve zkontrolujte, zda je vše v pořádku, a pokud ne, pak se snažte problém vyřešit.
#Uživatel může stále používat všechny funkce Odoo s vaším tématem. Například pokud převedete
Pokud chcete vypnout výchozí možnost nebo ji udělat nefunkční, můžete na hlavičce stránky umístit pruh.
zkušenosti. Kromě toho vaše přehrávání nemusí fungovat tak dobře jako výchozí možnost, protože jiné verze Odoo
Tyto funkce mohou na něm záviset.

..tip:
   - Pro každý úroveň odsazení používejte čtyři mezeru.
   - Nepoužívejte tabulátory.
   - Nikdy nesmíte míchat mezery a tabulátory.

.. viz též:
:doc:`Pravidla pro kódování Odoo <../../../contributing/development/coding_guidelines>`

... tématu/modulu/proměnných:

Proměnné Odoo
--------------

Odoo deklaruje mnoho CSS pravidel, většina z nich je plně přizpůsobitelná pomocí převedení příslušných proměnných SCSS.
Pro to vytvořte soubor `primary_variables.scss` a přidejte ho do souboru _assets_primary_variables
balíček.

**Prohlášení**

... kódový blok:: python
:caption: „/webová_stránka_vzduchotěsná/__manifest__.py“

"aktiva": {
'web._assets_primary_variables': [
'webová stránka_neprůzvučnost/statické soubory/sass/primární proměnné.sass'.
      ],
   },

Pokud se podíváte na zdrojový kód, jsou proměnné související s možnostmi snadno viditelné.

... blok kódu::xml

<tlačítko s titulkem="...
data-name="..."
data-customize-website-views="..."
data-customize-website-variable="'Navigace'"
data-img="..."/>

Tyto proměnné lze přehrát například pomocí mapy $o-website-value-palettes.

... tématu/modulu/proměnných/globálních:

Global
~~~~~~

**Prohlášení**

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-webové-hodnoty-barevného-spektra:
      (
         // Templates
         // Colors
         // Fonts
         // Buttons
         // ...
      ),
   );

..tip:
Tento soubor může obsahovat pouze definice a přehrávání proměnných a mixinů v SCSS.

.. viz též:
„Primární proměnné SCSS
<https://github.com/odoo/odoo/blob/c272c49657e8b7865bb93e5f1dcc183cc7d44f17/addons/website/static/src/scss/primary_variables.scss#L2089>`_

… tématu, modulu, proměnných a fontů:

Písmo
~~~~~

Můžete vložit jakýkoli font na svou webovou stránku. Webový editor je automaticky přidá do
fonty.

**Prohlášení**

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-theme-font-configs: (
font-name: (
"rodina": <seznam písem rodiny>
'url' (volitelné): <odkaz na část Google Fonts>
'vlastnosti' (volitelné):
font-alias: (
<webová hodnota klíče>: <hodnota>,
               ...,
            ),
         ...,
      )
   )

**Použití**

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-webové-hodnoty-barevného-spektra:
      (
'písmo':                              '<jméno písma>'
'nadpisy-písmo':                     '<jméno-fontu>'
'nav_bar_font':                       '<font-name>'
"tlačítka-písmo":                    "<název-písma>"
      ),
   );

.._tematizaci/moduly/proměnné/písmo/Google:

Google Fonty
************

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-theme-font-configs: (
„Mary Poppins“:
'rodina':                            ('Poppins', bez písma)
'url':                                'Poppins:400,500'
"vlastnosti" : (
'base': (
„písmo velikosti základní“: 1 rem
            ),
         ),
      ),
   );

.._tematické/moduly/proměnné/písmo/vlastní:

Vlastní písmo
************

Nejprve vytvořte speciální soubor SCSS, ve kterém deklarujete svůj vlastní font.

... kódový blok:: python
:caption: „/webová_stránka_vzduchotěsná/__manifest__.py“

"aktiva": {
'web.assets_frontend': [
'webové stránky_vzduchotěsné/statické/scss/font.scss'
      ],
   },

Pak použijte pravidlo @font-face k tomu, abyste umožnili na webu načítání vašich vlastních písem.

... kódový blok::scss
:caption: „/webová_stránka_neprůzvučnost/statické soubory/scss/font.scss“

@font-face {
font-family: "Můj vlastní font", Helvetica, Helvetica Neue, Arial, sans-serif;
font-weight: 400;
font-style: normal;
src: url('/písmo/můj vlastní font.woff') formátu ('woff'),
url('/písmo/můj-vlastní-font.woff2') formátu ('woff2');
   }

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-theme-font-configs: (
„Proxima Nova“:
'rodina':                            ('Proxima Nova', bezpísemný)
"vlastnosti" : (
'base': (
„písmo velikosti základní“: 1 rem
            ),
         ),
      ),
   );

..tip:
Doporučuje se používat formát „.woff“ a/nebo „.woff2“.

...Téma, modul, proměnné, barvy:

Barvy
~~~~~~

Webový tvůrce webových stránek využívá paletky složené z pěti barev s názvy. Tyto definujte ve svém šabloně
zajišťuje, aby zůstala konzistentní.

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * -Barva
     - Popis
   * o-color-1
     - Primární
   * o-color-2
     - Střední
   * o-color-3
     - Extra (Lehké)
   * o-color-4
     - Bílý
   * o-color-5
     - Černější

.. obrázek: theming/theme-colors.png
:alt: Barvy motivu
:šířka: 300

**Prohlášení**

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-color-palety: map-merge($o-color-palety,
      (
„voděodolný“:
„o-color-1“:                   #bedb39,
'o-color-2':                        #2c3e50,
'o-color-3':                    #f2f2f2,
'o-color-4':                      #ffffff,
„o-color-5“:                          #000000,
         ),
      )
   );

Přidejte vytvořenou paletu do seznamu nabízených palet Webového tvůrce.

... kódový blok::scss

$o-selected-color-palettes-names: přidat($o-selected-color-palettes-names, 'airproof');

**Použití**

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-webové-hodnoty-barevného-spektra:
      (
'nazev-barevného-schématu':           'voděodolný',
      ),
   );

.. obrázek: theming/theme-colors-airproof.png
:alt:Barvy téma Airproof
:šířka: 800

**Kombinace barev**

Webový editor automaticky vytváří webové stránky na základě pěti předem definovaných barevných schémat.
pět barevných kombinací, každá z nich definuje barvu pro pozadí, text, nadpisy, odkazy a primární
tlačítka a sekundární tlačítka. Tyto barvy lze později upravit uživatelem.

.. obrázek: theming/theme-colors-big.png
:alt: Barvy motivu
:šířka: 300

Barvy použité v barevné kombinaci jsou přístupné a lze je přehrát.
Používá se specifický předponový znak („o-cc“ pro „kombinace barev“).

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-color-palety: map-merge($o-color-palety,
      (
„voděodolný“:

„o-cc*-bg“: „o-color-*“,
'o-oc*-text':                     'o-barva-*'
'o-cc*-heading':                'o-color-*'
'o-cc*-h2':                      'o-barva-*'
'o-cc*-h3':                      'o-color-*',
'o-cc*-h4':                   'o-color-*',
'o-cc*-h5':                       'o-barva-*',
'o-oc*-h6':                   'o-barva-*'
„o-cc*-link“: „o-color-*“,
'o-cc*-btn-primary':           'o-color-*',
'o-cc*-btn-primary-border':      'o-barva-*',
'o-cc*-btn-secondary':         'o-barva-*',
'o-cc*-btn-secondary-border':  'o-barva-*',

         ),
      )
   );

.. poznámka::
Pro každé o-cc* nahraďte * číslem (1 - 5), které odpovídá požadované barvě
kombinace.

Výchozí barva písma je „o-color-5“. Pokud je pozadí příliš tmavé, automaticky se ztmaví.
změnit barvu na „o-color-4“.

.. viz též:
'Kombinace barev v SCSS
<https://github.com/odoo/odoo/blob/c272c49657e8b7865bb93e5f1dcc183cc7d44f17/addons/web_editor/static/src/scss/web_editor.common.scss#L16>

.. varování: Demonstrační stránka

Webový editor automaticky vytvoří stránku, na které můžete vidět barevné kombinace tématu.
paleta barev: http://localhost:8069/webová stránka/demo/kombinace barev

….motivy, moduly, proměnné a gradienty:

Gradienty
~~~~~~~~~

Můžete také definovat gradienty pro nabídku, hlavičku, patičku a pruh s autorským právem přímo ve vašem
souboru `primary_variables.scss`.

**Prohlášení**

... kódový blok::scss
:caption: „/webové stránky/statické soubory CSS/primární proměnné.scss“

$o-webové-hodnoty-barevného-spektra:
      (
„menu-gradient“: lineární gradient (135°, RGB(203, 94, 238) 0%, RGB(75, 225, 236) 100%)
'hlavička-boxová-plynulá': [vaše-plynulá]
"footer-gradient": [vaše-barevná-křivka]
'copyright-gradient': [vaše-přechodová čára]
      ),
   );

... _tematizaci/modul/bootstrapping:

Proměnné pro bootstrapping
-------------------

Odoo obsahuje Bootstrap výchozím nastavením. Můžete používat všechny proměnné a mixiny rámce.

Pokud v Odoo nenajdete proměnnou, kterou hledáte, může existovat proměnná Bootstrap.
umožňuje to. Ve skutečnosti všechny Odoo šablony respektují strukturu Bootstrap a používají komponenty Bootstrap nebo
jejich rozšíření. Pokud upravíte proměnnou Bootstrapu, přidáte univerzální styl pro celého uživatele
webové stránky.

Použijte soubor v příslušném balíčku, který je přidán do :file:`_assets_frontend_helpers`, k překrytí Bootstrap
hodnoty a ne souboru:file:`primary_variables.scss`.

**Prohlášení**

... kódový blok:: python
:caption: „/webová_stránka_vzduchotěsná/__manifest__.py“

"aktiva": {
'web._assets_frontend_helpers': [
('připojit', 'webová_vzduchotěsná/statické/scss/bootstrap_overridden.scss')
      ],
   },

**Použití**

... kódový blok::scss
:komentář: „/webová_stránka_voděodolná/statické/sass/bootstrap_převzatý.scss“

   // Typography
font-size:                        4rem !default;

   // Navbar
@media (min-width: 768px) { navbar-nav-link-padding-x: 1rem !important; }

   // Buttons + Forms
$vstupní-umístění-barva:       o-barva('o-barva-1') !výchozí;

   // Cards
$kartičkový-okraj-šířka:           0 !výchozí hodnota;

..tip:
Tento soubor může obsahovat pouze definice a přehrávání proměnných a mixinů v SCSS.

.. varování:
Nepřekrývejte proměnné Bootstrapu, které závisí na proměnných Odoo. Jinak byste je mohli poškodit.
možnost pro uživatele upravit je pomocí Webového editoru.

Pokud je možnost definována proměnnou v souboru `primary_variables.scss` a proměnnou Bootstrapu,
Vždy se snažte používat přesměrování skrze primární proměnné. To provádějte pomocí
Pouze pokud v hlavních proměnných nic není, použijeme soubor „bootstrap_overridden.scss“.

.. viz též:
„Překrytá CSS Bootstrap


.. varování: Demonstrační stránka

   http://localhost:8069/website/demo/bootstrap

.._tematizace/modul/bootstap/písmo:

Velikosti písma
~~~~~~~~~~

Odoo má třídy písma pro oddělení stylu (velikosti písma) a semantiku (tagy a styly).
generální). Oba logické systémy lze kombinovat, aby byly flexibilnější.

.. viz též:
„Dokumentace Bootstrapu k hlavičkám zobrazení


.._theming/module/bootstrap/fonts/text:

Styl textu
**********

Webový editor Odoo umožňuje vybrat si styl pro váš text. Některé jsou jen související s tagem, jako například
Hlavička bez dalšího třídění CSS. Jinak se kombinuje značka a styl přímo na nich, jako je
„Hlavička 1 Zobrazit“.

.. obrázek: theming/header.png
:alt: Styl hlavičky
:šířka: 300

... blok kódu::xml



<h1 třída="zobrazit-2">Hlavička s velikostí hlavičky zobrazení 2</h1>
<h1 třída="zobrazit-3">Hlavička 1 s velikostí hlavičky zobrazit-3</h1>
<h1 class="display-4">Hlavička 1 s velikostí hlavičky 4</h1>





<p class="o_small">Tělo textu s menším písmem.</p>

... téma/modul/bootstarp/písmo/velikost:

Třídy velikosti
**************

Velikostní třídy se přidávají do nově vytvořeného tagu span uvnitř cílového prvku (viz
příkladů níže).

.. obrázek: theming/sizing.png
:alt:Třídy velikosti
:šířka: 300

... tématu/modulu/základní rozhraní/písma/velikost písma/nadpisy a tělo:

Hlavička a tělo textu
^^^^^^^^^^^^^^^^^^^^^

Pokud by se tyto třídy daly použít na jakýkoliv textový prvek, vezměme si jako příklad níže uvedené h2:

... blok kódu::xml


<h2><span class="h1-fs">Hlavička</span></h2>

<!-- nadpis 2. úrovně, který je velikosti ostatních nadpisů -->
<h2><span class="h2-fs">Hlavní nadpis</span></h2>
<h2><span class="h3-fs">Hlava</span></h2>
<h2><span class="h4-fs">Hlava</span></h2>
<h2><span class="h5-fs">Hlava</span></h2>
<h2><span class="h6-fs">Hlava</span></h2>


<h2><span class="base-fs">Hlavní nadpis</span></h2>


<h2><span class="o_small-fs">Hlava</span></h2>

... tématu, modulu, bootstrapu, písma, velikosti a zobrazení:

Hlavičky obrazovky
^^^^^^^^^^^^^^^^

Pokud jsou potřeba větší nadpisy, používá Odoo třídy založené na Bootstrapu od „display-1“ do „6“.

... blok kódu::xml

<h2><span class="display-1-fs">Hlava</span></h2>
<h2><span class="display-2-fs">Hlava</span></h2>
<h2><span class="display-3-fs">Hlavní nadpis</span></h2>
<h2><span class="display-4-fs">Hlava</span></h2>

.. poznámka::
Webový editor umožňuje uživateli nastavit pouze velikosti od „Zobrazení 1“ do „Zobrazení 4“.
můžete nastavit ostatní velikosti (5 a 6) pro použití v kódu, ale uživatel nebude moci
upravit je přímo v rozhraní Webového editoru.

.. téma/modul/webové stránky:

Nastavení webu
----------------

Globální možnosti pro webové stránky lze nastavit pomocí záznamu o webových stránkách následovně
struktura níže.

**Prohlášení**

... blok kódu::xml
:caption: „/webová_stránka_voděodolná/data/webová stránka.xml“


<odoo noupdate="1">
<záznam id="web.defaultní web" typu "web">
<pole název="název">Airproof</pole>

<položka jméno="favicon" typ="base64" soubor="webové stránky/statické obrázky/popis/favicon.png" />
<field name="shop_ppg">18</field>
<field name="shop_ppr">3</field>
<field name="cookies_bar" eval="true" />
<field name="kontaktujte-nás-tlačítko-url">/kontakt/</field>
<field name="social_facebook">https://www.facebook.com/Airproof</field>
<field name="social_instagram">https://www.instagram.com/airproof</field>
<field name="social_linkedin">https://www.linkedin.com/company/airproof</field>
<field name="social_youtube">https://www.youtube.com/c/AirProof</field>
</záznam>


.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * – Hřiště
     - Popis
   * - jméno
     - Název webu (zobrazený v prohlížeči)
   * - logo
     - Cesta k logu (dříve vytvořená na gramofonové desce)
   * - ikona
     - Cesta ke znaku webové stránky (dříve vytvořenému do záznamu)
   * – shop_ppg
     - Počet produktů na stránce v elektronickém obchodě
   * shop_ppr
     - Počet produktů na řádku (na stránce) v elektronickém obchodě
   * - cookies_bar
     - Povolit/zakázat lištu s cookies
   * - kontakt_nás
     - URL stránky „Kontaktujte nás“ (například používáno v šablonách hlaviček).
   * -social_facebook
     - URL profilu na Facebooku
   * -social_instagram
     - URL profilu na Instagramu
   * -social_linkedin
     - URL firemního profilu na LinkedIn
   * -social_youtube
     - URL kanálu na YouTube

.. poznámka::

„webová stránka.výchozí webová stránka“ je výchozím odkazem, pokud pracujete pouze s jednou webovou stránkou.
V databázi je několik webových stránek, tento záznam se bude vztahovat na výchozí web (tj.
první z nich.

... šablony/moduly/výhledy:

Názory
-----

Pro některé možnosti je potřeba kromě proměnné Webové stránky aktivovat také konkrétní
pohled.

Pokud člověk prohlíží zdrojový kód, šablony související s možnostmi jsou snadno nalezitelné.

... blok kódu::xml

<tlačítko s titulkem="...
data-name="..."
data-customize-website-views="webové stránky.výchozí šablona hlavičky"
data-customize-website-variable="..."
data-img="..."/>

... blok kódu::xml


<šablona id="..." dědí id="..." název="..." aktivní="False"/>

... šablony / moduly / pohledy / přednastavení:

Předvolby
~~~~~~~

Chcete-li aktivovat a deaktivovat pohledy jako přednastavení, měly by být zahrnuty do
souboru presets.xml.

**Použití**

... blok kódu::xml
:předmět: „/webová_stránka_vzduchotěsná/data/prezentace.xml“

<zaznamenání id="modul.vid" model="ir.ui.view">
<pole název="aktivní" hodnota="false"/>
</záznam>

Příklad:
**Změna horizontální orientace položek nabídky**

... kódový blok :: XML
:popisek: „/webové_stránky_vzduchotěsné/data/prezentace.xml“

<záznam id="webová stránka.vzorec hlavičky výchozího zarovnání do středu" typu="ir.ui.view">
<pole název="aktivní" hodnota="True"/>
</záznam>

Také pro ostatní aplikace Odoo lze použít stejnou logiku.

**E-commerce – Zobrazení kategorií produktů**

... kódový blok :: XML
:popisek: „/webové_stránky_vzduchotěsné/data/prezentace.xml“

<záznam id="webové prodeje.produkty kategorie" typu="ir.ui.view">
<pole název="aktivní" hodnota="false"/>
</záznam>

**Portál - Vypněte jazykový filtr**

... kódový blok :: XML
:popisek: „/webové_stránky_vzduchotěsné/data/prezentace.xml“

<zaznamenání id="portal.footer_language_selector" typu="ir.ui.view">
<pole název="aktivní" hodnota="false"/>
</záznam>

... téma / aktiva:

Výnosy
======

Pro tuto část se budeme odvolávat na balíček „assets_frontend“ v modulu webu. Tento balíček
Specifikuje seznam aktiv načtených webovým editorem a cílem je přidat vaše SCSS a JS.
soubory do balíčku.

Toto je neúplný seznam často používaných balíčků pro webové stránky:

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * - Sada
     - Popis
   * - web._assets_primary_variables
     - Hlavně pro soubor „primary_variables.scss“.
   * - web._assets_secondary_variables
     - Hlavně pro soubor „secondary_variables.scss“.
   * - web._assets_frontend_helpers
     - Hlavně pro soubor „bootstrap_overridden.scss“
   * - web.assets_frontend
     - Můžete přidat všechny své vlastní soubory SCSS, JS nebo QWeb JS.
   * - webové stránky.assets_wysiwyg
     - Přidejte své soubory JavaScriptu týkající se chování možností Webové stránky (například vlastní
metoda pro vaši vlastní stavební blok).
   * - webové stránky.assets_wysiwyg
     - Pokud potřebujete rozšířit Bootstrap prostřednictvím API Bootstrap Utilities, například

...stylů a témat:

Styl
------

Webový editor společně s Bootstrapem jsou skvělým nástrojem pro definování základních stylů vašich webových stránek.
Ale abyste vytvořili něco jedinečného, musíte jít ještě dál. To lze snadno provést přidáním libovolných Sass
soubor do vašeho tématu.

**Prohlášení**

... kódový blok:: python
:caption: „/webová_stránka_vzduchotěsná/__manifest__.py“

"aktiva": {
'web.assets_frontend': [
'webové stránky/základní/zdrojový kód/styl.css'
      ],
   },

Můžete bez obav používat proměnné z vašeho souboru Bootstrap a ty, které používá Odoo.
souboru `theme.scss`.

Příklad:
... kódový blok::javascript
:caption: „/webová stránka_vzduchotěsná/statické/zdrojový kód/styl.css“

blockquote {
border-radius: $zvýrazněná-pilulka;
barva: o-barva('o-barva-3');
font-family: 'o-webové hodnoty' ('hlavičkový font');
       }

... tématu, aktivit a interaktivních prvků:

Interaktivita
-------------

Odoo podporuje tři různé typy souborů JavaScriptu:

- :ref:`pouze prosté soubory JavaScriptu <frontend/modules/plain_js> (bez modulového systému)
- :ref:`nativní modul JavaScriptu <frontend/modules/native_js>“.
- :ref:`Moduly Odoo <frontend/modules/odoo_module>“ (pomocí vlastního modulového systému).

Většina nových kódů v jazyce JavaScript by měla používat nativní systém modulů v JavaScriptu. Je jednodušší a
přináší výhody lepšího vývojářského zážitku s lepším propojením s integrovaným vývojovým prostředím.

**Prohlášení**

... kódový blok:: python
:caption: „/webová_stránka_vzduchotěsná/__manifest__.py“

"aktiva": {
'web.assets_frontend': [
"webové stránky/airproof/statické/js/theme.js",
      ],
   },

.. poznámka::
Pokud chcete zahrnout soubory ze vzdálené knihovny, můžete je přidat do složky :file:`/lib`.
soubor vašeho modulu.

..tip:
   - Použijte linter (JSHint, ...)
   - Nikdy nepřidávejte minifikované knihovny JavaScriptu.
   - Přidejte na začátek každého starého modulu řádku „use strict;“ (to je automatické u nových stylů).
moduly.
   - Používejte CSS třídy s předponou „js_“ na prvky, které cílíte pomocí JavaScriptu.
   - Proměnné a funkce by měly být psány s velkým počátečním písmenem („myVariable“) místo malého počátečního písmene
(„má varianta“).
   - Neznačte proměnnou jako „event“, použijte místo ní „ev“. To je proto, aby se zabránilo chybám na ne-Chromu
prohlížeče, jako je Chrome, který kouzlem přiřazuje globální proměnnou „event“ (takže pokud používáte
Pokud nevyhlásíte proměnnou „event“, bude fungovat v prohlížeči Chrome, ale ve všech ostatních prohlížečích se zhroutí.
prohlížeč.
   - Používejte přísné porovnání (například „===“ místo „==“).
   - Používejte dvojité uvozovky pro všechny textové řetězce („Hello“) a jednoduché uvozovky pro ostatní.
řetězce, například CSS selektoru .x_nav_item.
   - Pokud používáte nativní funkce JavaScriptu (např. start(), willStart(), cleanForSave()
aplikace metody _super() na sebe a argumenty.
standardní kód).

.. viz též:
   - „Pravidla pro kódování v Odoo JavaScriptu <https://github.com/odoo/odoo/wiki/Javascript-coding-guidelines>“
   - Přehled o JavaScriptovém rámci Odoo
<../../reference/frontend/javascript_reference>
   - „Odoo Experience Talk: 10 Tipů, jak vylepšit design webových stránek! <https://www.youtube.com/watch?v=vAgE_fPVXUQ&ab_channel=Odoo>“
