
.. odkaz/aktiva:

======
Výnosy
======

Správa aktiv v Odoo není tak jednoduchá jako ve některých jiných aplikacích.
Jedním z důvodů je, že máme různé situace, kdy někdo, ale ne všichni
majetku jsou vyžadovány. Například potřeba klienta na webu, bod
Prodej přes aplikaci, web nebo dokonce mobilní aplikaci je jiný. A některé
mají být velké, ale často se nepotřebují: v takovém případě je můžeme chtít
být načítány pomalu (na požádání).

Typy aktiv
===========

Existují tři různé typy aktiv: kód (soubory „js“), styl („css“ nebo „scss“)
soubory a šablony (soubory s příponou xml)).

Kód
Odoo podporuje tři různé typy skriptů v JavaScriptu:
Všechny tyto soubory jsou pak zpracovány (nativní moduly v Javě se převádí na odoo).
pak zkomprimované (pokud není v režimu „vývoj“:ref:`<frontend/framework/assets_debug_mode>`).
a následně se spojí do jednoho souboru, který je uložen jako příloha.
Přílohy se obvykle načítají pomocí značky skriptu v části hlavičky.
stránku (jako statickou souborovou stránku).

Styl
Stylizaci lze provést buď pomocí „css“ nebo „scss <https://sass-lang.com/>“.
javascript soubory, tyto soubory se zpracovávají (soubory typu `scss` se převádějí na
pak zkomprimovány (opět pouze v případě, že nejsou ve režimu „vývoj“:ref:`<frontend/framework/assets_debug_mode>`).
a spojeny do jednoho souboru, který je pak uložen jako příloha e-mailu.
Poté se obvykle načte pomocí značky v části hlavičky stránky, která je určena pro
(statický soubor)

Šablona
Šablony (statické soubory XML) jsou zpracovávány jinak: jednoduše
čteny z disku, když jsou potřeba, a spojeny dohromady.

Každou dobu, když prohlížeč načítá odoo, volá kontroleru
načíst šablony:ref:`<reference/qweb>`.

Je užitečné vědět, že v naprosté většině případů prohlížeč provede pouze požadavek.
první načtení stránky. To je proto, že každý z těchto aktiv
spojené s kontrolním součtem, který je vložen do zdrojového kódu stránky.
Poté se přidá do URL adresy, což znamená, že je možné bezpečně nastavit cache.
hlavičky na dlouhou dobu.

.. odkaz na aktiva/balíček aktiv:

Sady
=======

Součásti Odoo jsou seskupeny do balíčků. Každý balíček obsahuje seznam cest k souborům (*složky s příponou .py*)
specifických typů: „xml“, „js“, „css“ nebo „sass“) je uveden v
:ref:`modul manifest <reference/module/manifest>`. Soubory lze deklarovat pomocí
Syntax globu, což znamená
Můžete deklarovat několik souborů aktiv pomocí jediné řádky.

Bundly jsou definovány v každém modulu v souboru __manifest__.py
s vlastním klíčem „aktiva“, který obsahuje slovník. Slovník mapuje
složky jmen (klíčů) k seznamu souborů, které obsahují (hodnotám). Vypadá
takto:

... kódový blok:: python

'aktiva': {
'web.assets_backend': [
'web/statické/src/xml/**/*'
        ],
'web.assets_common': [
'web/statické/lib/bootstrap/**/*'
"web/statické/zdroje/js/boot.js",
'web/statické/zdrojové/js/webklient.js',
'web/statické/zdrojové/xml/webclient.xml',
        ],
'web.qunit_suite_tests': [
'web/statické/zdrojové/js/testy_webklienta.js',
        ],
    },

Tady je seznam některých důležitých balíčků, které bude většina vývojářů potřebovat
Víte, že:

- „web.assets_common“: tento balíček obsahuje většinu společných aktiv,
webový klient, web i pokladna. To vše by mělo obsahovat
nižší úrovně stavebních bloků pro rámec Odoo. Poznámka: Obsahuje
:souboru `boot.js`, který definuje systém modulů Odoo.

- `web.assets_backend“: tento balíček obsahuje kód specifický pro webového klienta
(zejména webový klient, správce akcí, pohledy a statické šablony XML).

- „web.assets_frontend“: tento balíček se zabývá vším, co je specifické pro veřejnost
web:e-shop, portál, fórum, blog, ...

- `web.qunit_suite_tests`: všechny testovací kódy v JavaScriptu (testy, pomocníci a náhražky)

- `web.qunit_mobile_suite_tests`: mobilní specifické testovací kód


Operace
----------

Obvykle je správa aktiv jednoduchá: stačí přidat několik nových souborů.
do často používaného balíčku „assets_common“ nebo „assets_backend“. Existují další operace
k pokrytí některých konkrétnějších případů použití.

Poznámka: všechny direktivy, které se zaměřují na určitý soubor aktiva (například „before“, „after“),
„nahradit“ a „odstranit“) potřebují k prohlášení souboru předem.
v vyšších manifeštích nebo v záznamu „ir.asset“ s nižším
sled.

„připojit“
~~~~~~~~

Tato operace přidává jeden nebo více souborů. Je to nejčastější
operace lze provést pouhým uvedením názvu souboru:

... kódový blok:: python

"web.assets_common": [
'my_addon/statické/zdrojové soubory/js/**/*',
  ],

Pokud se do balíčku přidá jednoduchý řetězec, bude k němu automaticky připojen soubor s názvem odpovídající tomuto řetězci.
globální vzor na konci balíčku. Samozřejmě může být i přímo
jediný cestu k souboru.

„připojit“
~~~~~~~~~

Přidejte jeden nebo více souborů na začátek balíčku.

Užitečné, pokud potřebujete umístit určitý soubor před ostatními v balíku (například
příklad s CSS soubory). Operace prepend je vyvolána následujícím
Syntaxe: '('. Předchozí cesta.')'.

... kódový blok:: python

"web.assets_common": [
('připojit', 'můj_doplněk/statické/zdroje/css/bootstrap_overridden.scss')
  ],

„před“
~~~~~~~~

Přidejte jeden nebo více souborů před konkrétní soubor.

Přidání souboru na začátek balíčku nemusí být přesné.
Příkaz „before“ lze použít k přidání zadaných souborů přímo před cílem.
souboru, který je deklarován nahrazením normální cesty tříčlenným seznamem
„(před, <cílový bod>, <cesta>).“

... kódový blok:: python

"web.assets_common": [
(před, web/statické soubory CSS/bootsrap_overridden.scss, my_addon/statické soubory CSS/bootsrap_overridden.scss)
  ],

„po“
~~~~~~~

Přidejte jeden nebo více souborů po konkrétním souboru.

Stejně jako u příkazu „předtím“, s odpovídajícími soubory připojenými hned za cílový soubor.
Je deklarována nahrazením běžné cesty tříčlenným tuplíkem
„(Po, cíl, cesta)“.

... kódový blok:: python

"web.assets_common": [
(po, "web/statické/zdrojové soubory CSS/list_view.scss", "můj doplněk/statické zdroje CSS/list_view.scss")
  ],

„zahrnout“
~~~~~~~~~

Používejte balíčky vložené do sebe.

Directive „include“ je způsob, jak použít balíček v jiných balících, aby se minimalizovala
velikost vašeho manifestu. V Odoo používáme podbalíčky (předpona s lomítkem)
zvykem) k souborům s více balíčky, které pak můžete
specifikovat podbalíček jako dvojici „(include, <bundle>)“ takto:

... kódový blok:: python

"web.assets_common": [
(‚zahrnout‘, ‚web._primární proměnné‘),
  ],

„odstranit“
~~~~~~~~

Odebrat jeden nebo více souborů.

V některých případech můžete chtít odstranit jeden nebo více souborů z balíčku.
Lze provést pomocí příkazu remove, který specifikuje dvojici
„(Odebrat, <cíl>):

... kódový blok:: python

"web.assets_common": [
('odstranit', 'web/statické/src/js/boot.js')
  ],

„vyměnit“
~~~~~~~~~

Nahraďte soubor aktivu jedním nebo více soubory.

Řekněme, že aktivum nejen odstraníte, ale také do něj chcete vložit
novou verzí tohoto aktiva na stejném místě. To lze provést pomocí
direktivu replace s trojmístným tuplem ('replace', <cílová stránka>, <cesta k souboru>)

... kódový blok:: python

"web.assets_common": [
('replace', 'web/static/src/js/boot.js', 'my_addon/static/src/js/boot.js')),
  ],


Pořadí načítání
-------------

Pořadí načítání aktiv je někdy kritické a musí být deterministické.
především pro priority stylů a nastavení skriptů. Assety v Odoo jsou zpracovávány
takto:

#Když je volána sada aktiv (např. t-call-assets="web.assets_common""), vytvoří se prázdný
vytvoří se seznam aktiv

#Všechny záznamy typu ir.asset, které odpovídají balíčku, jsou získány a seřazeny.
podle čísla pořadí. Pak jsou všechny záznamy s číslem menším než 16
zpracovány a aplikovány na aktuální seznam aktiv.

#Všechny moduly, které v manifestu deklarují aktiva pro tento balíček, se na něj
do seznamu aktivních operací. Toto je provedeno podle pořadí závislostí modulů
(např. webové aktivity jsou zpracovány před webem). Pokud se některá z těchto
pokud je soubor již v seznamu, nic se s ním nedělá.
v seznamu je uchovávána pouze první verze souboru.

#Ostatní záznamy „ir.asset“ (s pořadovým číslem větším nebo rovným
Tyto hodnoty (v rozmezí od 0 do 15) jsou pak zpracovány a aplikovány stejně jako ostatní.

Výrobky uvedené v prohlášení mohou být naloženy ve specifickém pořadí.
Příklad: soubor `jquery.js` musí být načten před všemi ostatními skripty jQuery při načítání
složku lib. Jednou z možností by bylo vytvoření :ref:`ir.asset <frontend/assets/ir_asset>
s nižším sekvenčním číslem nebo příkazem „předcházet“, ale existuje i jednodušší
jak na to.

Odůvodnění je jednoduché. Každá cesta k souboru v seznamu aktiv má svou jedinečnou cestu, takže
zmínit konkrétní soubor před globem, který jej zahrnuje. Soubor se tak objeví
v seznamu před všemi ostatními, kteří jsou součástí globu.

... kódový blok:: python

'web.assets_common': [
'my_addon/static/lib/jquery/jquery.js',
'my_addon/statické/knihovny/jQuery/**/*'
    ],

.. poznámka::

Modul b, který odstraňuje nebo nahrazuje aktiva vyhlášená v modulu a,
se na ně spoléhat. Používání aktiv, které dosud nebyly vyhlášeny,
Výsledkem je chyba.

... frontend/assety/lazy_loading:

Nebuďte líný
============

Někdy je užitečné načítat soubory a/nebo aktivační balíčky dynamicky.
příklad načítání knihovny pouze v případě potřeby. K tomu slouží rámec
poskytuje několik funkcí, které jsou umístěny v souboru: @web/core/assets.

... kódový blok: JavaScript

očekávej načtení aktiv {
jsLibs: ["/web/statické/lib/stacktracejs/stacktrace.js"]
  });


..js:function::loadAssets(assety)

:param Object assets: popis různých aktiv, které by měly být načteny
:vrací:Promise<void>

Načtěte aktiva popsaná parametrem `assets`. Jedná se o objekt, který
Může obsahovat následující klíče:

...... seznamová tabulka::
:šířky: 20 20 60
:hlavičkové řádky: 1

      * – Klíč
        - Typ
        - Popis
      * – „jsLibs“
        - „řetězec“
        - seznam URL souborů JavaScriptu
      * - `cssLibs`
        - „řetězec“
        - seznam adres URL CSS souborů


..js:function::useAssets(aktiva)

:param Object assets: popis různých aktiv, které by měly být načteny

Tento háček je užitečný, pokud komponenty potřebují načíst nějaké aktiva.
metoda onWillStart, která interně volá funkci loadAssets.

.. _frontend/assets/ir_asset:

Model aktiv („ir.asset“)
============================

Většinou budou postačovat majetkové podmínky vyjádřené v prohlášení.
více pružnosti také podporuje dynamické aktiva vyhlášená v
databáze.

Toho se dosáhne vytvářením záznamů „ir.asset“. Ty budou zpracovávány jako kdyby byly
byly nalezeny v modulu manifestu a mají stejnou výrazovou sílu jako jejich
manifestní protivníci.

... autoklasifikace: odoo.addons.base.models.ir_asset.IrAsset

.. první třídy: o definice

Jméno
Název záznamu o aktivu (pro účely identifikace).

„balíček“
Soubor, do kterého bude aktivum aplikováno.

„směrnice“ (výchozí hodnota „připojit“)
Toto pole určuje, jak bude interpretována cesta (a cíl, pokud je potřeba).
Níže je uveden seznam dostupných příkazů spolu s jejich povinnými argumenty:

    - **připojit**: `cesta`
    - **připojit předchozí cestu**: `cesta`
    - *před*: „cíl“, „cesta“
    - *po*: „cíl“, „cesta“
    - **zahrnout**: `cesta` (vyhodnocená jako **název balíčku**)
    - **odstranit**: `cesta` (vykládáno jako cílový aktivum, které má být odstraněno).
    - **vyměnit**: `cíl`, `cesta`

„cesta“
Řetězec definující jednu z následujících možností:

    - relativní cesta k souboru aktiv v systému souborů doplňků.
    - globální vzor pro sadu souborů aktiv v systému souborů doplňků;
    - URL odkazující na přílohu nebo externí soubor.
    - jméno balíku, pokud používáte příkaz include.

„cíl“
cílový soubor, který určuje pozici v balíku. Lze použít pouze s
příkazů „vyměnit“, „před“ a „po“.

„aktivní“ (výchozí hodnota „Pravda“)
Zda je rekord aktivní

„soubor“ (výchozí hodnota = „16“)
Pořadí záznamů o aktivu (vzestupně). Sekvence nižší než 16 znamená
že aktivum bude zpracováno před aktivy uvedenými v prohlášení o přepravě.
