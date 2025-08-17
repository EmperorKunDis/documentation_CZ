..zvýrazněno::xml

.._reference/qweb:

==============
Šablony QWeb
==============

QWeb je primární šablonovací_ motor používaný v Odoo.
je XML šablonovacím jazykem a používá se především k generování HTML.
fragments a stránky.

Šablonové příkazy jsou specifikovány jako atributy XML s předponou „t-“.
například „t-if“ pro :ref:`reference/qweb/podmínky`, s prvky
a další vlastnosti jsou vykreslovány přímo.

Pro vyhnutí se zobrazení prvku je k dispozici také místo „<t>“.
která provádí příkaz, ale nevytváří žádný výstup.
sám o sobě:

<t t-if="podmínka">
<p>Test</p>


Výsledkem bude:



Pokud je „podmínka“ pravdivá, ale:

<div t-if="podmínka">
<p>Test</p>


Výsledkem bude:


<p>Test</p>


... odkaz/qweb/výstup:

Výstup dat
===========

Výstupní příkaz „out“ z QWeb automaticky HTML-escapuje jeho vstup.
omezit rizika při zobrazování uživatelsky poskytnutého obsahu.

„out“ přijímá výraz, vyhodnocuje ho a vloží výsledek do dokumentu:

<p><t t-out="value"/></p>

s hodnotou „value“ nastavenou na „42“ vypadá takto:

<p>42</p>

Podrobnější informace najdete v části „Pokročilé výstupy“ (např.
např. vkládání neupraveného HTML atd.).

.._odkaz/qweb/podmínky:

Podmínky
============

QWeb má podmíněný příkaz „if“, který vyhodnocuje výraz, který je uveden.
jako hodnota atributu:


<t t-if="podmínka">

</t>


Výraz se vyhodnocuje pouze v případě, že je podmínka pravdivá:


<p>OK</p>


Pokud je podmínka nepravdivá, je z výsledku odstraněna.




Podmíněné zobrazení se vztahuje na nositele směrnice, který
nemusí být „<t>“:


<p t-if="podmínka">OK</p>


dá stejné výsledky jako předchozí příklad.

Další podmíněné větve s příkazy „t-elif“ a „t-else“ jsou také
Dostupné:


<p t-if="user.narozeniny == dnes()">Gratulujeme k narozeninám!</p>
<p t-elif="uživatel.login == 'root'">Vítej, pane!</p>
<p t-else="">Vítejte!</p>



.._odkaz/qweb/smyčky:

Smyčky
=====

QWeb má iterativní příkaz foreach, který přijímá výraz vracící
soubor k iterování a druhý parametr „t-as“ poskytující
název pro „aktuální položku“ v průchodu.

<t t-for="[1, 2, 3]" t-as="i">
<p><t t-out="i"/></p>


bude přeloženo jako:

<p>1</p>
<p>2</p>
<p>3</p>

Stejně jako podmínky, „foreach“ se vztahuje na prvek nesoucí příkaz.
atribut.

::

<p t-for="[1, 2, 3]" t-as="i">
<t t-out="i" />


je stejné jako v předchozím příkladu.

Ve funkci foreach bude aktuálním prvkem aktuální prvek pole.
hodnota) nebo mapování (současný prvek bude klíčem aktuálního objektu). Při
celé číslo (ekvivalentní k opakování na pole mezi hodnotou 0 včetně a
(celé číslo vyloučeně) je stále podporováno, ale zastaralé.

Kromě jména předaného přes „t-as“ poskytuje „foreach“ ještě několik dalších
proměnné pro různá data:

Upozornění: Výraz „$as“ bude nahrazen jménem, které bylo předáno funkci t-as.

.. první třídy: o definice

:samp:`{$as}_all` (zastaralé)
objekt, který je v průběhu iterace

...... poznámka: Tato proměnná je k dispozici pouze v JavaScriptu QWeb, nikoli v Pythonu.

:samp:`{$as} value`
současná hodnota iterace, která je stejná jako „$as“ u seznamů a celých čísel.
ale pro mapování poskytuje hodnotu (kde „$as“ poskytuje klíč).
:samp:`{$as}_index“
aktuální iterace (první položka v iteracích má index 0)
samp:`{$as} velikost`
velikost sbírky, pokud je k dispozici
:samp:`{$as}`
zda aktuální položka je první položkou právě probíhajícího cyklu.
:samp:`{$as}_index == 0`)
:samp:`{$as}`
zda je aktuální položka poslední v iteracích (což odpovídá
:samp:`(${as} index + 1) == (${as} size)`), vyžaduje, aby velikost iterátoru byla
dostupné
:samp:`{$as}` (zastaralá)
buď „součet“ nebo „díl“, parita aktuální smyčky
:samp:`{$as}` (zastaralá funkce)
pravdivá hodnota, která ukazuje na to, že aktuální kolo je sudé.
index
:samp:`{$as}` (zastaralé)
pravdivá hodnota, která ukazuje na to, že aktuální kolo je v lichém kole.
index

Tyto nové proměnné vytvořené a všechny nové proměnné poskytnuté
„foreach“ je k dispozici pouze v rámci „foreach“. Pokud
Proměnná existuje mimo kontext cyklu „for each“, hodnota je zkopírována
v kontextu globálního prostředí na konci cyklu foreach.

::


<!-- existující proměnná je nyní False -->

<p t-for="[1, 2, 3]" t-as="i">





<!-- existující proměnná vždycky pravdivá -->
<!-- nová proměnná je neznámá -->

.. odkaz/qweb/atributy:

atributy
==========

QWeb může počítat atributy na lince a nastavit výsledek výpočtu.
na výstupním uzlu. To se provádí pomocí příkazu „t-att“ (atribut), který
existuje ve třech různých formách:

.. první třídy: o definice

:samp:`t-att-{$name}`
vytvoří se atribut s názvem „$name“, hodnota atributu je vyhodnocena
a výsledek je nastaven jako hodnota atributu

<div t-att-a="42"/>

Bude zobrazeno jako:

<div a="42" />
:samp:`t-attf-{$name}`
stejný jako předchozí, ale parametr je :term:`formátovací řetězec
místo pouhé fráze, která je často užitečná k smíchání literálních a neliterárních
řetězec (např. třídy):

<t t-foreach="[1, 2, 3]" t-as="item">
<li t-attf-class="row {{ (item_index % 2 === 0) ? 'souvislý' : 'nepravidelný' }}">
<t t-out="item"/>
</li>
</t>

Bude zobrazeno jako:

<li class="row even">1</li>
<li class="row odd">2</li>
<li class="row even">3</li>

.......tip::
Pro formátovací řetězce existují dvě ekvivalentní syntaxe: „přirozený text {{kód}}“ (také
a „""plain_text #{kód}"“ (alias ruby-style).

:samp:`t-att=mapping“
pokud je parametrem mapa, každý pár klíč-hodnota vytvoří nový
atribut a jeho hodnota:

<div t-att="{'a': 1, 'b': 2}"/>

Bude zobrazeno jako:

<div a="1" b="2"></div>
samp:t-att=pár
pokud je parametrem dvojice (tj. tupl nebo pole se dvěma prvky), první
prvním položkou páru je název atributu a druhou položkou je
hodnota::

<div t-att="['a', 'b']"/>

Bude zobrazeno jako:

<div a="b"></div>

.. odkaz/qweb/set:

nastavování proměnných
=================

QWeb umožňuje vytvářet proměnné přímo v šabloně, pamatovat si výpočty (používat je
opakovaně), dát datu jasnější název, ...

Toho je dosaženo pomocí příkazu „set“, který přijímá název proměnné
vytvořit. Hodnota, kterou chcete nastavit, může být poskytnuta dvěma způsoby:

* atribut „t-hodnota“ obsahující výraz a výsledek jeho
hodnotit budeme::

<t t-set="foo" t-value="2 + 1"/>
<t t-out="foo"/>

Výstupem bude hodnota „3“.
* pokud není atribut „t-value“, tělo uzlu se zobrazí a nastaví
jako hodnota proměnné::

<t t-set="foo">
<li>OK</li>

<t t-out="foo"/>

.. odkaz/qweb/volání:

.. odkaz na šablonu/odkaz na podšablony:

volání podšablon
=====================

Šablony QWeb lze použít pro renderování na úrovni vrcholu, ale také
z jiného šablony (aby se předešlo duplicitě nebo aby byly pojmenovány části
šablon) pomocí příkazu „t-call“:

<t t-call="jiný šablonový výraz"/>

Toto volá vybraný šablonový soubor s výkonnostním kontextem rodičovského souboru, pokud
„other_template“ je definováno jako::

<p><t t-value="var"/></p>

následující volání se zobrazí jako „<p/>“ (bez obsahu):

<t t-set="var" t-value="1"/>
<t t-call="jiný šablonový výraz"/>

bude zobrazeno jako „<p>1</p>“.

Tento způsob však má problém s viditelností zvenčí.
Alternativně obsah nastavený v těle příkazu „call“ bude
hodnocené před voláním podšablony a mohou měnit místní kontext:

<t t-call="jiný šablonový soubor">
<t t-set="var" t-value="1"/>

<!-- zde neexistuje "var" -->

Tělo příkazu „volání“ může být libovolně složité (nejen
„set“ (řídicí příkazy) a jeho zobrazená forma bude k dispozici v volané
Šablona jako „magická“ proměnná 0:


Tento šablonu se volala s obsahem:
<t t-out="0"/>


takto nazývána

<t t-call="jiný šablonový soubor">
<em>obsah</em>


Výsledkem bude:


Tento šablonu se volala s obsahem:
<em>obsah</em>


... odkaz/qweb/pokročilý výstup:

Pokročilý výstup
===============

Výchozí nastavení „out“ by mělo HTML-escapovat obsah, který je potřeba zabezpečit.
chránit systém před XSS.

Obsah, který nemusí být zneškodněn, bude vložen tak, jak je.
dokumentu a může se stát součástí skutečného formátování dokumentu.

Jediným bezpečným obsahem, který je k dispozici na všech platformách, je výstup.
:ref:`t-volání <reference/qweb/call>“ nebo „:ref:`t-vytvoření <reference/qweb/set>“.
používá se s „tělem“ (proti „t-hodnotě“ nebo „t-hodnotě f“).

Python
------

Obvykle se nemusíte příliš starat: API, které dávají smysl
měla vytvářet „bezpečný“ obsah automaticky a věci by měly fungovat
průhledně.

Pro případy, kdy je potřeba věci uvést na pravou míru, následují následující API.
bezpečný obsah, který bude automaticky ne(re)escapován při vložení
šablony:

* :třída:odoo.fields.Html.
* :funkce odoo.tools.misc.html_escape a markupsafe.escape (jsou
a nemáte riziko dvojitého uvozovkování.
* :func:`~odoo.tools.mail.html_sanitize`.
* :klasifikační třída: `markupsafe.Markup`.

... varování: Klasifikace `markupsafe.Markup` je nebezpečná, jedná se o * tvrzení*.
že chcete, aby obsah byl bezpečný pro značkování, ale nemusí být
Neboť pokud se neověří, měl by být používán s opatrností.
* Funkce:~odoo.tools.pycompat.to_text neoznačuje obsah jako bezpečný
nebude odstraňovat tuto informaci z bezpečného obsahu.

nutnost dvojitého uvozového znaménka
-----------------------

Pokud je obsah označen jako bezpečný, ale přesto se musí v některých případech zabezpečit
(např. tisknutí značek HTML pole) je možné ji jen převést zpět
k normálnímu řetězci „odstranit“ bezpečnostní vlajku např. pomocí funkce str() v Pythonu
„String(obsah)“ v Javě.

.. poznámka::

Protože třída Markup je mnohem bohatší typ než
:js:třída Markup, některé operace odstraní bezpečnostní informace
třída Markup, ale ne třída Markupsafe.Markup např. řetězec
v Pythonu se získá koncatenace ('' + obsah)
:třída Markupsafe.Markup s druhým operandem, který byl správně
získáme :js:class:`String`.
druhý operand nebyl před koncatenací „uniknut“.

Deprecované výstupní příkazy
----------------------------

.. první třídy: o definice

„Esc“
Alias pro „out“ by původně HTML-escapoval jeho vstup. To ještě
formálně degradován jako jediný rozdíl mezi „out“ a „esc“.
že druhá je trochu nejasná/nepřesná.
„neupravené“
Verze „out“, která nikdy neuniká svému obsahu. Obsah je vypouštěn
tak jak je, bez ohledu na jejich bezpečnost.

... zastaralé: 15.0

Ve výchozím nastavení se používá „out“ s hodnotou objektu třídy Markup.

„t-raw“ byl zastaralý, protože kód produkující obsah
Pokud se tento kód vyvíjí, může být obtížné sledovat, že bude použit pro značkování.
To povede k složitějším recenzím a nebezpečnějším chybám.

Python
======

Exkluzivní příkazy
--------------------

Soubory aktiv
~~~~~~~~~~~~~

... vše: Nechám si napsat tyto informace, protože o tom nemám ani tušení.

Formátování polí „inteligentních záznamů“
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

„T-pole“ lze použít jen při přístupu k poli
(„a.b“) na „chytré“ záznamy (výsledky metody „procházet“). Je schopná
automaticky formátovat podle typu pole a je integrována v
bohaté možnosti úpravy textu na webových stránkách.

„t-options“ lze použít k přizpůsobení políček. Nejběžnější možnost
„gadget“; další možnosti jsou „pole“ nebo „gadget“.

Ladění
---------

.. první třídy: o definice

„t-debug“
s prázdným parametrem vyvolává funkci breakpoint.
Funkce, která obvykle spouští debugger (:mod:`pdb`).
výchozí hodnoty).

Chování lze nastavit pomocí proměnné prostředí :envvar:`PYTHONBREAKPOINT`.
:func:`sys.breakpointhook`.

Výstup renderovacího cache:
----------------

„t-cache=“key_cache““ značkuje část šablony, která se má vykreslit při renderování.
Každá podřízená direktivy bude volána pouze při prvním vykreslení. To znamená
Výsledky dotazů SQL provedených při vykreslování těchto podřízených příkazů
Jsou také prováděny pouze jednou.

„t-nocache=“ dokumentace „tags část šablony, která se má zobrazit pokaždé.
Obsah může používat jen kořenové hodnoty.

Proč a kdy používat „t-cache“?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tento příkaz se používá k zrychlení renderování tím, že části finálního výstupu ukládá do mezipaměti.
dokument, který může ušetřit dotazy na databázi. Je však třeba jej používat
šetřivě, protože „t-cache“ nevyhnutelně komplikuje šablony (a jejich
pochopení „t-setu“ například.

Abychom skutečně ušetřili databázové dotazy, může být nutné
vložit šablonu s hodnotami, které se vyhodnocují pouze tehdy, když je potřebujeme.
hodnoty jsou použity v části uložené v paměti, nebudou vyhodnoceny, pokud je část
k dispozici v mezipaměti.

„t-cache“ je užitečná pro části šablony, které používají hodnoty závislé na
na omezeném množství dat. Doporučujeme analyzovat renderování
šablona s profilerem (pomocí aktivace „**Přidat kontext pro příkaz qweb**“
volba). Předávání líných hodnot do renderování v kontrolérech umožňuje
zobrazit příkazy s těmito hodnotami a spustit dotazy.

Obavou při používání takového mezipaměti je, že ji mohou využívat různí uživatelé.
(různí uživatelé by měli zobrazovat vykachlíkovanou část stejně).
Potenciální problém je zrušit své záznamy v případě potřeby.
Klíčové výrazy by měly být zvoleny s rozmyslem. Výraz „write_date“
recordset může zneplatnit klíč k vyrovnávací paměti bez nutnosti jej smazat.
Třeba přímo z mezipaměti.

Je třeba také věnovat pozornost tomu, že hodnoty v části „t-cache“
jsou rozsahovány. To znamená, že pokud je v této části souboru t-set příkazů,
šablona a zpracování toho, co přijde po ní, může být jiná než kdyby
nebyl žádný „t-cache“ příkaz.

Co když je uvnitř „t-cache“ další „t-cache“?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Části jsou uloženy v mezipaměti. Každá obsahuje pouze řetězec odpovídající její
rendering. Tím pádem se pravděpodobně bude „t-cache“ uvnitř číst méně často, jeho
klíč ke cache nebude nutně použit. Pokud tomu tak musí být, pak můžete
musíte přidat „t-nocache“ (na stejném uzlu nebo rodičovském uzlu).

Co je t-nocache používáno k?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud chcete část šablony uložit pomocí „t-cache“, ale malý kousek musí být
zůstat dynamický a vyhodnocovat se v časech mezipaměti. Nicméně část
„t-nocache“ nemá přístup k hodnotě „t-set“ šablony.
Hodnoty poskytnuté kontrolovanou osobou jsou tam dostupné.
Například se menu ukládá do cache, protože je stejné vždy a načítání trvá
doba na vykreslení (pomocí vývojových nástrojů pro výkon s kontextem QWeb vám umožní
Zkoumat) však chceme mít vždy zapnutý nákupní košík.
do dnešního dne. Proto je zde „t-nocache“, aby se tato část dynamicky měnila.

Základ t-cache
~~~~~~~~~~~~~~~~~~~~~~~

„T-cache“ umožňuje ukládat vygenerovaný výsledek šablony.
Klíčové výrazy (**např. 42: "t-cache="42"")** budou vyhodnoceny jako Python
vyjádření, které bude použito k generování klíče pro **mezipaměť**. To znamená, že může být
různé hodnoty cache (ukládaná část renderu) pro stejný šablonový prvek. Pokud
**klíčové vyjádření** je tupl nebo seznam, bude hledat při generování
klíč k vyhledávání. Pokud se vrací jeden nebo více záznamů, je klíč
výraz**, pak se použije model, id a datum psaní.
použité k generování klíče ke cache. Speciální případ: Pokud je **klíčová výrazová konstrukce**
vrací hodnotu False, pak se obsah nebude ukládat do cache.

Příklad:

<div t-cache="record,pravda(podmínka)">
<span t-if="condition" t-field="record.partner_id.name">
<span t-else="" t-field="record.partner_id" t-options-widget="kontakt">


V tomto případě mohou být v mezipaměti hodnoty (řetězec), které odpovídají každému
Záznam již byl vrácen s pravdivou podmínkou i pro nepravdivou
podmínka. A pokud modul upraví záznam, pak se změní i datum poslední úpravy.
hodnota z cache se vymaže.

„t-cache“ a proměnné s rozsahem („t-set“, „t-foreach“…)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Hodnoty v „t-cache“ jsou omezené, což znamená změnu chování mezi
mít nebo nemít „t-cache“ na jednom z rodičovských uzlů. Nezapomeňte
zohlednit, že Odoo používá mnoho šablon, „t-call“ a „view“.
dědictví. Přidáním „t-cache“ tedy může dojít ke změně zpracování
šablona, kterou při editaci neuvidíte.
(„t-foreach“ je jako „t-set“ pro každou iterace)

Příklad:

<div>
<t t-set="a" t-value="1"/>

<t t-set="a" t-value="2"/>

</vnitřní>
<vnější t-out="a"/>

<t t-set="b" t-value="1"/>
<t-cache="True">
<t t-set="b" t-value="2"/>
<t t-out="b"/>
</vnitřní>
<vnější t-out="b"/>
</div>

Výsledkem bude:

<div>
<vnitřní>2</vnitřní>
<venku>2</vnitř>

<vnitřní>2</vnitřní>
<venku>1</vnitř>
</div>


Základ t-nocache
~~~~~~~~~~~~~~~~~~~~~~~~~

Část šablony obsažená v uzlu s atributem „t-nocache“ není
do mezipaměti. Tento obsah je tedy dynamický a zobrazuje se systémově.
Ale dostupné hodnoty jsou ty, které poskytl provozovatel (v případě
voláním metody „_render“).

Příklad:

<část>
<článek t-cache="zaznamenání">
<title><t t-out="record.name"/> (zobrazení: <t t-out="counter"/>)</title>
<content t-out="record.description"/>
</článek>


Zobrazí (počet zobrazení = 1):

<část>
<článek>
<title>Název rekordu (zobrazení: 1)</title>
<p>Popis záznamu</p>
</článek>


Zde se vždy zobrazí „„<i>““ značka, která obsahuje kontejner.
zbytek je v jednom řetězu v mezipaměti.

„t-nocache“ a proměnné kořenového uzlu („t-set“, „t-foreach“…)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Obsah značky „t-nocache“ může být použit pro dokumentaci a
vysvětlit, proč je příkaz přidán.
Hodnoty jsou vnořeny do „t-nocache“, tyto hodnoty jsou pouze kořenové
(hodnoty poskytnuté kontrolerem a/nebo při volání metody "_render"
„ir.qweb“). „T-set“ lze provést v šabloně, ale nebude
je k dispozici jinde.

Příklad:

<část>
<t t-set="counter" t-value="counter * 10"/>
<hlavička t-nocache="">
<t t-set="counter" t-value="counter + 5"/>
(zobrazení: <t t-out="counter"/>)

<článek t-cache="zaznamenání">
<title><t t-out="record.name"/> (zobrazení: <t t-out="counter"/>)</title>
<content t-out="record.description"/>
</článek>
<footer>(zobrazení: <t t-out="counter"/>)</footer>


Zobrazí (počet zobrazení = 1):

<část>

(zobrazení: 6)

<článek>
<title>Název rekordu (zobrazení: 1)</title>
<p>Popis záznamu</p>
</článek>
<footer>(zobrazení: 10)</footer>


Zde se vždy zobrazí „„<i>““ značka, která obsahuje kontejner.
zbytek je v jednom řetězci v mezipaměti.
„t-set“ z „t-nocache“.

„t-nocache-*“ přidá nějaké primitivní hodnoty do mezipaměti
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Aby bylo možné používat hodnoty vygenerované v šabloně, je nutné
ukládat je do mezipaměti. Direktiva se používá jako „t-nocache-*=„expresní výraz““.
název zvolené hodnoty a „expr“ pro výraz v Pythonu, aby byl výsledek
být uloženo do mezipaměti. Hodnota uložená v mezipaměti musí být primitivní typ.

Příklad:

<část t-cache="záznamy">
<článek t-pro každý záznam t-jako záznam>
<hlavička>
<title t-field="record.get_method_title()"/>


t-nocache-cached_value="record.get_base_counter()">
<span t-out="counter + cache_value"/>
</stop>
</článek>


Hodnota „cached_value“ je uložena s předem vygenerovanou částí šablony.
„t-cache=“záznamy“ a přidávat hodnoty do kořenového rozsahu každou chvíli.

Pomocníci
-------

Na žádost
~~~~~~~~~~~~~

Většina použití QWeb na straně Pythonu je v kontrolorech (a během HTTP požadavků).
V takovém případě se používají šablony uložené v databázi (jako
(viz. reference/view_architectures/qweb) lze snadno zobrazit voláním
:meth:`odoo.http.HttpRequest.render`:

... kódový blok:: python

response = http.požadavek.výstup(„můj šablonový soubor“, {
'context_value': 42
    })

Tímto se automaticky vytvoří objekt odoo.http.Response, který lze
bude vrácena zpět do kontroleru (nebo dále upravena tak, aby vyhovovala).

Založené na pohledu
~~~~~~~~~~

Hlouběji než u předchozího pomocníka je metoda „_render“
„ir.qweb“ (použijte datovou tabulku) a veřejnou metodu „render“
Nezapomeňte, že se jedná o databázi.

.. metoda: render(id, [hodnoty])

Zobrazuje QWebové pohledy nebo šablony podle ID v databázi nebo :term:`externího ID`.
Šablony se automaticky načítají z záznamů „ir.qweb“.

„_připravit_prostředí“ metoda nastavuje několik výchozích hodnot.
kontextu renderování. Přídavné moduly „http_routing“ a „webová stránka“
i výchozí hodnoty, které potřebují.
Můžete použít možnost „minimal_qcontext=False“ k tomu, aby se tento výchozí
hodnota jako u veřejné metody render():

... první třídy :: o definici seznamu

„Žádost“
:objednávka:objekt aktuální požadavku (pokud existuje)
„debug“
zda je aktuální požadavek v režimu „debug“
:func:`quote_plus <werkzeug.urls.url_quote_plus>`
funkce pro kódování URL
:mod:`json`
odpovídající knihovna standardních funkcí
:mod:`čas`
odpovídající knihovna standardních funkcí
:mod:`datetime`
odpovídající knihovna standardních funkcí
`relativní rozdíl <https://labix.org/python-dateutil#head-ba5ffd4df8111d1b83fc194b97ebecf837add454>`_
vidět modul
„keep_query“
funkce „keep_query“

:param values: kontextové hodnoty, které se předávají do QWeb pro zobrazení
:param str engine: název použitého modelu Odoo pro zobrazení, může být
používá k rozšíření nebo přizpůsobení QWebu (vytvořením
nový „qweb“ postavený na „ir.qweb“ s úpravami

... metoda: render(šablona, hodnoty, načíst, volby)

:func:`load(ref)`
vrací objekt etree, ref

.. odkaz/qweb/javascript:

...:: členové níže již nejsou platní, část přepsat

.. API
.. ---

...Je také možné používat přímo „ir.qweb“ model (a rozšířit ho) a
.. dědí po něm).

.. .automoduly: odoo.addons.base.ir.ir_qweb
..:členové:QWeb, QWebContext, FieldConverter, QwebWidget

Javascript
==========

Exkluzivní příkazy
--------------------

Definování šablon
~~~~~~~~~~~~~~~~~~

„t-název“ příkaz může být umístěn pouze na úrovni šablony
soubor (směřuje přímo k kořenovému adresáři):

<šablony>
<t t-name="template-name">
<!-- kód šablony -->
</t>
</šablony>

Nebere žádný další parametr, ale může být použit s „<t>“ nebo jakýmkoliv jiným
jiný. Pro „<t>“ by mělo být pouze jedno dítě.

Název šablony je libovolný řetězec, i když při použití více šablon
jsou související (např. jsou podšablonami), je zvykem používat oddělené tečkou
název pro označení hierarchických vztahů.

.. _reference/qweb/dědičnost šablon:

Dědičnost šablon
~~~~~~~~~~~~~~~~~~~~

Šablonové dědičství se používá k buď:
 - Upravit existující šablony na místě, například přidat informace do šablon
Vytvořené jinými moduly.
 - Vytvořit nový šablonu na základě zadaného rodičovského šablonu

Dědičnost šablon je prováděna pomocí dvou příkazů:
 - „t-dědit“, což je název šablony, ze které se dědí.
 - „t-inherit-mode“, který určuje chování dědičnosti: buď
nastavit na „primární“, aby se vytvořil nový šablonový soubor z rodičovského.
to „rozšíření“, které upraví vzorovou šablonu přímo na místě.

Můžete také zadat volitelný „t-name“ příkaz, který bude jméno
nově vytvořený šablonový soubor se použije v režimu primárního výběru, jinak bude přidán jako
komentář k transformovanému vzoru, který pomáhá při sledování dědictví.

Sám dědění se provádí pomocí příkazů xpaths.
Podívejte se na dokumentaci k XPATH_, kde najdete kompletní sadu dostupných příkazů.

Primární dědění (podkladový vzor):

<t t-name="dítě.šablona" t-dědictví="základní šablona" t-dědictvím-režimu="primární">
<xpath expr="//ul" pozice="uvnitř">
<li>nový prvek</li>
</xpath>


Dědičnost rozšíření (transformace v místě):

<t t-inherit="base.template" t-inherit-mode="extension">
<xpath expr="//tr[1]" position="po ní">
<tr><td>nová buňka</td></tr>
</xpath>


Starý mechanismus dědění (zastaralý)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provádění šablonového dědění se provádí pomocí příkazu „t-extend“, který přijímá
jméno šablony, kterou chceme upravit jako parametr.

Příkaz „t-extend“ bude fungovat jako primární dědění, pokud je použitý společně s
„t-name“ a jako přípona, pokud je použita sama o sobě.

V obou případech se pak provádí změna s libovolným počtem „t-jquery“.
podřízené příkazy:

<t t-extend="base.template">
<t t-jquery="ul" t-operation="append">
<li>nový prvek</li>
</t>


Direktivy „t-jquery“ přijímají „selektor CSS“. Tento selektor se používá
na rozšířený vzor, kde vyberete kontextové uzly, ke kterým je uvedeno
Použije se „t-operace“:

.. první třídy: o definice

„připojit“
tělo uzlu se přidává na konec kontextového uzlu (po kontextovém uzlu).
posledním dítětem uzlu kontextu
„připojit“
tělo uzlu je připojeno k kontextovému uzlu (vloženo před kontextový uzel).
prvním dítětem uzlu kontextu
„předtím“
tělo uzlu se vkládá před kontextovým uzlem
„po“
tělo uzlu se vkládá hned za kontextový uzel
„vnitřní“
tělo uzlu nahrazuje děti kontextového uzlu
„nahradit“
tělo uzlu se používá k nahrazení kontextového uzlu samotného
„atributy“
tělo uzlu by mělo být libovolný počet „atributů“
Každý z nich má atribut „name“ a nějaký obsah.
atribut kontextového uzlu bude nastaven na zadanou hodnotu
(pokud již existovala, tak nahrazena nebo přidána).
Žádná operace
pokud není specifikována „t-operaci“, tělo šablony je interpretováno jako
javascriptový kód a proveden s kontextovým uzlem jako „this“

.... varování: i když je tento režim mnohem silnější než ostatní operace,
Je také mnohem obtížnější ladit a udržovat, proto se doporučuje
se mu vyhnout

ladění
---------

Implementace QWeb v jazyce JavaScript poskytuje několik možností pro ladění chyb:

.. první třídy: o definice

„t-log“
bere jako parametr výraz a vyhodnocuje jej při zobrazení
a zaznamenává výsledek pomocí „console.log“::

<t t-set="foo" t-value="42"/>
<t t-log="foo"/>

bude na konzoli tisknout „42“.
„t-debug“
způsobuje zastavení ladiče při zpracování šablony::

<t t-if="a_test">

</t>

zastaví provádění pokud je aktivní ladění (přesná podmínka se liší v závislosti na
(prohlížeč a jeho vývojové nástroje)
„t-js“
tělo uzlu je JavaScriptový kód, který se spouští při zpracování šablony.
Tento parametr „kontext“ je jméno pod kterým se zobrazuje.
kontext bude dostupný v těle objektu „t-js“::

<t t-set="foo" t-value="42"/>
<t t-js="ctx">
console.log("Foo je", ctx.foo);
</t>

Pomocníci
-------

..js:attr::core.qweb

(jádro je modul „web.core“) Instance objektu :js:třída:`QWeb2.Engine`, který obsahuje všechny šablony definované v modulech
nahrána a odkazuje na standardní pomocné objekty „_“.
(_underscore_, „_t“ (funkce pro překlad) a JSON_.

:js:funkce `core.qweb.render <QWeb2.Engine.render>` se používá k
snadno vytvářet základní šablony modulů

.. odkaz/qweb/api:

API
---

...:class:QWeb2.Engine

QWeb „renderer“, který zpracovává většinu logiky QWebu (načítání,
parsování, kompilace a vykreslování šablon.

Odoo Web vytváří pro uživatele jeden v základním modulu.
exportuje do „core.qweb“. Dále načítá všechny šablony.
různých modulů do tohoto QWebu.

A:js:class:`QWeb2.Engine` také slouží jako „jmenný prostor šablon“.

...js: funkce: QWeb2.Engine.render(šablona, kontext)

Předem načtený šablonu zobrazí jako řetězec.
„kontext“ (pokud je k dispozici), aby bylo možné najít proměnné, které byly přístupné
při zpracování šablony (např. zobrazitelné řetězce).

:param String šablona: název šablony, kterou chcete zobrazit
:param objekt kontextu: základní prostředí pro šablonu
zobrazování
:vrací: řetězec

Motor nabízí jinou metodu, která může být užitečná v některých případech.
případě (např. pokud potřebujete samostatný šablonový prostor s)
Odoo Web a Kanban získaly vlastní třídu:
příkladu, aby jejich šablony nekolidovaly s obecnějšími.
„šablony“ (tj. „vzory“) modulů):

... funkce:QWeb2.Engine.add_template(šablony)

Načítá šablonu (soubor s šablonami).
Příklad: šablony lze specifikovat jako:

XML řetězec
QWeb se pokusí z něj vytvořit dokument XML a následně jej načíst.
Využijte tento čas, abyste se na něj připravili.

URL
QWeb se pokusí stáhnout obsah URL adresy a poté načíst
výsledný řetězec XML.

„Dokument“ nebo „Uzel“
QWeb projde první úrovní dokumentu (úroveň).
dětské uzly kořenového uzlu a načíst všechny názvy
šablona nebo šablonové přetížení.

:typ šablony: řetězec | dokument | uzl

Kromě toho je k dispozici také několik atributů, které jsou vlastní pro
přizpůsobení chování:

..js:atribut:: QWeb2.Engine.prefix

Předpona používaná k rozpoznání příkazů během analýzy.
Výchozí hodnota je „t“.

...:attr:QWeb2.Engine.debug

Pravdivá vlajková hodnota umístí motor do režimu „debug“.
QWeb zachycuje všechny chyby, které vzniknou při zpracování šablony.
režimu ladění, nechává všechny výjimky bez povšimnutí.
je zadržovat.

......js:atribut::QWeb2.Engine.jQuery

Příklad jQuery, který se používá při zpracování dědičnosti šablony.
Výchozí hodnota je „window.jQuery“.

......js:atribut::QWeb2.Motor.předprocesovat_uzel

Funkce. Pokud je přítomna, volá se před kompilací každého DOMu
vytvořit šablonu kódu. V Odoo Web se používá pro
Automaticky překládá obsah textu a některé atributy.
šablony. Výchozí hodnota je „null“.

... je podobná jako Genshi_, i když nepoužívá (a
nepodporuje (tak jako XML jazyky) „jmenné prostory“

... i když používá několik dalších, buď z důvodu historického
důvody nebo proto, že zůstávají lepšími doplňky
použití případu. Odoo 9.0 stále vyžaduje Jinja_ a Mako_.

... šablonování:
    https://en.wikipedia.org/wiki/Template_processor

... Jinja: http://jinja.pocoo.org
..._Mako: https://www.makotemplates.org
.. _Genshi: https://genshi.edgewall.org
... _jmenné prostory XML: https://cs.wikipedia.org/wiki/XML_namespace
.. _HTML: https://cs.wikipedia.org/wiki/HTML
.. _XSS: https://cs.wikipedia.org/wiki/Křížové_skriptování
.. _JSON: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON
..._Vybraný CSS výraz: https://api.jquery.com/category/selectors/
.._XPATH: https://developer.mozilla.org/en-US/docs/Web/XPath
