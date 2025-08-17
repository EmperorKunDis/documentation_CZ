:sirotčinec:

==========================
Přizpůsobení webového klienta
==========================

.. nebezpečí::
Tento návod je zastaralý.

.. výrazně::javascript

.. výchozí doména: js

Tento průvodce je o vytváření modulů pro webového klienta Odoo.

Pro vytváření webových stránek pomocí Odoo se podívejte na :doc:`webové šablony`; pro přidání obchodních schopností
nebo rozšířit stávající podnikové systémy Odoo, viz: `backend`.

.. varování:

Tento průvodce předpokládá znalosti o:

    * Základy JavaScriptu a dobré postupy
    * jQuery
    * „Underscore.js“

Pro využití této funkce je také nutné mít nainstalované Odoo na místním serveru a Git.

Jednoduchý modul
===============

Začněme jednoduchým modulem v Odoo, který obsahuje základní webové komponenty
konfiguraci a nechat nás otestovat webový rámec.

Příkladový modul je dostupný on-line a může být stáhnut pomocí
a následně příkazem:

.. kódový blok: konzole

$ git clone http://github.com/odoo/petstore

Tímto vytvoří složku „PetStore“ na místě, kde jste příkaz spustili.
Poté musíte přidat tuto složku do Odoo.
:option:`addons path <odoo-bin --addons-path>`, vytvořte novou databázi a
nainstalovat modul „oepetstore“.

Pokud procházíte složkou „petstore“, měli byste vidět následující obsah:

... blok kódu:: text

oepetstore
|-- obrázky
|  |-- aligátor.jpg
|   |--balon.jpg
|  |--crazy_circle.jpg
|  |-- ryby.jpg
|  |--myši.jpg
|-- __init__.py
|-- oepetstore.zpráva_dne.csv
|-- __manifest__.py
|-- petstore_data.xml
|-- petstore.py
|-- petstore.xml
-- statické
--src
|-- css
|     |--petstore.css
|-- js
|     |-- petstore.js
--xml
-- petstore.xml

Modul již obsahuje různé úpravy serveru, na které se vrátíme.
Ty pozdější, prozatím se zaměřme na obsah spojený s webem, v „statickém“
složka.

Soubory používané v „webu“ části modulu Odoo musí být umístěny do složky „static“.
složky, aby byly dostupné pro webový prohlížeč, soubory mimo tuto složku
nebyly získány prohlížečem. „Src/css“, „src/js“ a „src/xml“
Podsložky jsou konvenční a nejsou nutné.

„oepetstore/static/css/petstore.css“
:V současné době prázdná, bude obsahovat CSS pro obchody se zvířaty
„oepetstore/static/xml/petstore.xml“
Většinou prázdná, obsahuje šablony :ref:`reference/qweb`.
„oepetstore/static/js/petstore.js“
Nejdůležitější a zároveň nejzajímavější část obsahuje logiku celého
aplikace (nebo alespoň její webový prohlížeč) jako JavaScript. Měla by
V současné době vypadají následovně:

odoo.oepetstore = funkce (instance, místní) {
var _t = instance.web._t
_lt = instance.web._lt;
var QWeb = instance.web.qweb;

místní.DomovskáStránka = instance.Výstup.rozšířit (
start: function () {
console.log("domovská stránka obchodu s domácími mazlíčky byla načtena");
                },
            });

instance.web.klientské akce.add(
'domovská stránka obchodu se zvířaty', 'objekt instance.OePetStore.HomePage');
        }

A která jen v prohlížeči zobrazí malý textový příspěvek.

Soubory v adresáři „static“ musí být definovány v modulu, aby se
správně načteny. Všechno v adresáři „src/xml“ je definováno v souboru „__manifest__.py“, zatímco obsah
„src/css“ a „src/js“ jsou definovány v souboru „petstore.xml“, nebo podobném souboru.

.. varování:

Všechny soubory JavaScriptu jsou sloučeny a :term:`minifikovány`, aby se zlepšila
doba načítání aplikace.

Jedním z nevýhod je, že ladění se stává obtížnější.
jednotlivé soubory zmizí a kód se výrazně zmenší.
Je možné tento proces vypnout zapnutím
„rozvojový režim“: přihlásit se do vaší instanci Odoo (uživatelské jméno *admin* heslo
*admin* výchozí hodnotou) otevře nabídku uživatele (v pravém horním rohu).
Odoo obrazovce a vyberte „O doo“ a poté „Aktivovat“.
vývojářský režim“

.. obrázek:: web/about_odoo.png
:align: střed


:align: střed

Tím se znovu načte webový klient s optimalizacemi vypnutými, což
Vývoj a ladění je výrazně pohodlnější.

... vše: soubory qweb jsou připojeny pomocí __manifest__.py, ale JS a CSS používají balíčky

Odoo modul pro JavaScript
======================

V jazyce JavaScript nejsou zabudované moduly. Výsledkem je, že proměnné definované v
Různé soubory jsou všechny smíchány dohromady a mohou se navzájem potýkat. To vzniklo
různým vzorcům modulů používaných k budování čistých jmen prostor a omezení rizik
jmenovací konflikty.

Odoo framework používá jeden takový vzor k definování modulů uvnitř webových doplňků.
aby bylo možné jmenovat kód a správně jej načítat.

„oepetstore/static/js/petstore.js“ obsahuje deklaraci modulu::

odoo.oepetstore = funkce (instanci, místní)
místní.xxx = ...;
    }

V Odoo webu jsou moduly definovány jako funkce nastavené na globální proměnné „odoo“.
proměnná. Název funkce musí být stejný jako název doplňku (v tomto případě
„oepetstore“ a rámec tak najde tento soubor a automaticky jej inicializuje.

Když se webový klient načte, zavolá funkci kořenového modulu.
a poskytnout dvě parametry:

* První parametr je aktuální instanci webového klienta Odoo, která dává
přístup k různým funkcím definovaných v Odoo (překlady,
i objekty definované jádrem nebo jinými službami.
moduly.
* druhý parametr je vaše vlastní místní jméno, které automaticky vytvoří
webového klienta. Objekty a proměnné, které by měly být přístupné z
vně vašeho modulu (ať už proto, že webový klient Odoo potřebuje tyto funkce
nebo proto, že je někdo může chtít upravit).
jméno prostoru.

Třídy
=======

Mnoho modulů a v rozporu s většinou objektově orientovaných jazyků
nebuduje v třídách, i když poskytuje přibližně
srovnatelné (i když nižší úrovně a více slovné) mechanismy.

Pro jednoduchost a přívětivost pro vývojáře poskytuje Odoo web třídu
systém založený na John Resigově Simple JavaScript Inheritance.

Nové třídy jsou definovány voláním metody :func:`~odoo.web.Class.extend`
Metoda třídy:

MyClass = instance.web.Class.extend({
funkce say_hello() {
console.log("Ahoj");
        },
    });

Metoda :func:`~odoo.web.Class.extend` přijímá seznam, který popisuje
obsah nové třídy (metody a statické atributy). V tomto případě bude
má pouze metodu „say_hello“, která nemá žádné parametry.

Třídy se vytvářejí pomocí operátoru „new“:

var my_object = nový objekt třídy MyClass();
my_object.vykriknout_azdravim();
    // print "hello" in the console

A přístup k atributům instancí lze provést pomocí „this“:

MyClass = instance.web.Class.extend({
funkce say_hello() {
console.log("Ahoj, jmenuji se " + this.name);
        },
    });

var my_object = nový objekt třídy MyClass();
my_object.jméno = "Bob";
my_object.vykriknout_azdravim();
    // print "hello Bob" in the console

Třídy mohou poskytnout inicializátor, který provede prvotní nastavení.
například definováním metody „init()“. Inicializátor přijímá
parametry, které se předávají při použití operátoru „new“:

MyClass = instance.web.Class.extend({
funkce init(jméno):
tento.jméno = jméno;
        },
funkce say_hello() {
console.log("Ahoj, jmenuji se " + this.name);
        },
    });

var my_object = nový objekt třídy MyClass ("Bob");
my_object.vykriknout_azdravim();
    // print "hello Bob" in the console

Je také možné vytvářet podtřídy z již existujících (použitě definovaných) tříd.
voláním metody:func:`~odoo.web.Class.extend` na základní třídu, jak je učiněno
podtřída:třída:

var MySpanishClass = MyClass.extend({
funkce say_hello() {
console.log("hola", this.name);
        },
    });

var my_objekt = nový MySpanishClass("Bob");
my_object.vykriknout_azdravim();
    // print "hola Bob" in the console

Při přebírání metody dědičností můžete použít „this._super()“
volat původní metodu:

var MySpanishClass = MyClass.extend({
funkce say_hello() {
tento._super();
console.log("překlad do španělštiny: hola", this.name);
        },
    });

var my_objekt = nový MySpanishClass("Bob");
my_object.vykriknout_azdravim();
    // print "hello Bob \n translation in Spanish: hola Bob" in the console

.. varování:

„_super“ není standardní metoda, je jí přiřazena na letu.
metoda v aktuální dědičné hierarchii, pokud existuje. Je definována
během synchronní části volání metody pro použití v asynchronním
handlery (po síťových voláních nebo v callbacku funkce „setTimeout“).
by mělo být zachováno jeho hodnota, neměla by se k němu přistupovat pomocí „tohoto“:

        // broken, will generate an error
funkce say_hello() {
setTimeout(function () {
tento._super();
}.bind(this), 0);
        }

        // correct
funkce say_hello() {
            // don't forget .bind()
_super = this._super.bind(this);
setTimeout(function () {
_super();
}.bind(this), 0);
        }

Základy widgetů
==============

Webový klient Odoo obsahuje jQuery, což usnadňuje práci s DOM. Je užitečný
a poskytuje lepší API než standardní „DOM W3C“_[#dombugs], ale
na složité aplikace, které jsou obtížné
údržba.

Má mnoho podobností s objektově orientovanými nástrojovými balíčky pro desktopové uživatelské rozhraní (např. Qt, Cocoa nebo GTK).
Odoo Web dělí stránku na části, které jsou zodpovědné za konkrétní komponenty.
Odoo web je základem pro takové komponenty a jeho základním typem je třída :class:`~odoo.Widget`.
třída, která je specializovaná na zpracování části stránky a zobrazení
informace pro uživatele.

Váš první widget
-----------------

Základní modul demonstrace už dnes nabízí základní widget:

lokální.Domovská stránka = instance.Widget.extend({
funkce start():
console.log("domovská stránka obchodu s domácími zvířaty byla načtena");
        },
    });

Rozšiřuje třídu widgetu a přebírá standardní metodu
:funkce ~odoo.Widget.start, která je velmi podobná funkci „MyClass“
— v tuto chvíli nic neřeší.

Tato řádka na konci souboru:

instance.web.client_actions.add(
'domovská stránka obchodu se zvířaty', 'objekt instance.oepetstore.HomePage');

zaregistruje základní widget jako akci klienta. Klientské akce budou
později vysvětlil, prozatím je to jenom to, co nám umožňuje naše widgety
je možné zobrazit a volat, když vybereme
:menuselection:`Obchod se zvířaty --> Obchod se zvířaty --> Úvodní stránka“ menu.

.. varování:

protože widget bude volán zvenčí naší modulové knihovny, musíme ho připravit pro použití v webovém klientovi.
Potřebuje své „plně kvalifikované“ jméno, nikoliv místní verzi.

Zobrazit obsah
---------------

Widgety mají řadu metod a funkcí, ale základy jsou jednoduché:

* nainstalovat widget
* formátovat data widgetu
* zobrazit widget

„Domovská stránka“ už má funkci „start“:
metoda, která je součástí normálního životního cyklu widgetu a automaticky
Volá se jednou, když je widget vložen do stránky. Můžeme ho použít k zobrazení nějaké
obsah.

Každý widget má atribut $el, který reprezentuje
sekci stránky, kterou spravují (jako objekt jQuery). Obsah widgetu
se do něj vloží. Výchozí hodnota atributu ~odoo.Widget.$el je
prázdný „„div““.

„<div>“ je obvykle neviditelný pro uživatele, pokud nemá žádný obsah (nebo
bez konkrétního stylu, který by mu dával velikost), protože se nic nezobrazuje.
na stránce, která se zobrazí při spuštění aplikace „HomePage“.

Přidejme nějaký obsah do kořenového prvku widgetu pomocí jQuery:

lokální.Domovská stránka = instance.Widget.extend({
funkce start():
tento.$el.append('<div>Ahoj, milý uživatelé Odoo!</div>');
        },
    });

Toto upozornění se nyní objeví při otevření menu Pet Store.
--> Zverimex --> Hlavní stránka

.. poznámka::

pokud chcete aktualizovat JavaScript kód načtený v Odoo Webu, budete muset stránku znovu načíst
stránku. Není nutné znovu spouštět server Odoo.

„Domovská stránka“ je widget, který používá Odoo Web a spravuje se automaticky.
Abychom se naučili používat widget „od nuly“, vytvořme si nový:

místní.Pozdravovací widget = instance.Widget.extenzí {
funkce start():
tento.$el.append('<div>Jsme rádi, že vás opět uvidíme na tomto menu!</div>');
        },
    });

Nyní můžeme přidat naší „GreetingsWidget“ do „HomePage“ pomocí
Metoda „widgetu“ „GreetingsWidget“::

lokální.Domovská stránka = instance.Widget.extend({
funkce start():
tento.$el.append('<div>Ahoj, milý uživatelé Odoo!</div>');
var pozdrav = nový widget místních pozdravů (tento).
návratová hodnota je vrácena do tohoto objektu.
        },
    });

* První, co „HomePage“ přidá do svého kořenového elementu DOM, je vlastní obsah.
* Poté „HomePage“ vytvoří instanci „GreetingsWidget“.
* Nakonec se „WidgetPozdravu“ zeptá, kde má vložit svůj kód, přičemž část
jeho atributu :attr:`~odoo.Widget.$el` na widget „Pozdravy“.

Když je metoda :func:`~odoo.Widget.appendTo` volána, požádá o
widget, který se vloží na určené místo a zobrazí svůj obsah.
Metoda:func:`~odoo.Widget.start` bude volána při každém volání
:funkci ~odoo.Widget.appendTo.

Abychom viděli, co se děje pod zobrazenou obrazovkou, použijeme prohlížeč.
DOM Explorer. Nejprve však upravíme naše widgety tak, abychom mohli snadněji
zjistit, kde se nacházejí, pomocí atributu „přidání třídy do jejich kořenových prvků
„<odoo.Widget.className>“::

lokální.Domovská stránka = instance.Widget.extend({
classname: 'oe_petstore_homepage',
        ...
    });
místní.Pozdravovací widget = instance.Widget.extenzí {
classname: 'oe_petstore_greetings',
        ...
    });

Pokud najdete příslušnou část DOMu (kliknutím pravým tlačítkem na text),
Pak by mělo vypadat takto:

.. kódový blok:: html


<p>Ahoj, milý uživateli Odoo!</p>

<div>Jsme tak rádi, že vás opět uvidíme v tomto menu!</div>
</div>


Jasně ukazuje dva automaticky vytvořené elementy „<div>“.
:třída:~odoo.Widget, protože jsme na ně přidali nějaké třídy.

Můžeme vidět i dva divy, které jsme sami přidali

Za zmínku stojí také prvek „<div class="oe_petstore_greetings">“
reprezentuje instanci „GreetingsWidget“ je uvnitř
„<div class="oe_petstore_homepage">“, což představuje „HomePage“.
například, protože jsme připojili

Widget rodičů a dětí
---------------------------

V předchozí části jsme vytvořili widget pomocí následujícího syntaxe:

nový místní widget pozdravů (toto).

První argument je „to“, co v tom případě bylo „Domovská stránka“.
příkladu, který říká widgetu, který je vytvářen, jaký další widget je jeho
*rodiče*.

Jak jsme viděli, widgety se obvykle vkládají do DOM jiným widgetem.
Vnitřek jiného widgetu, tedy že většina widgetů je „částí“
jiného widgetu a existují na jeho účet. My jsme tento kontejner nazvali
*rodiče* a vložený widget je *dítě*.

Z důvodu mnoha technických a koncepčních důvodů je nutné widget
znát, kdo je jeho rodič a kdo jsou jeho děti.

:func:`~odoo.Widget.getParent`
Může být použita k získání rodiče widgetu:

místní.Pozdravovací widget = instance.Widget.extend({
start: function () {
console.log(this.getParent().$el);
                // will print "div.oe_petstore_homepage" in the console
            },
        });

:func:`~odoo.Widget.getChildren`
může být použito k získání seznamu jeho dětí:

local.HomePage = instance.Widget.extend({
start: function () {
var greeting = nový widget s pozdravem z lokálního souboru (tento).
pozdrav připojí k tomuto objektu.
console.log(this.getChildren()[0].$el);
                // will print "div.oe_petstore_greetings" in the console
            },
        });

Při přepsání metody init() widgetu je
je nezbytné předat rodiče do volání „this._super()“.
jinak se vztah nezaloží správně:

místní.Pozdravovací widget = instance.Widget.extenzí {
funkce init (parent, jméno):
tento._super(rodiče);
tento.jméno = jméno;
        },
    });

V neposlední řadě pokud widget nemá rodiče (např. protože je kořenem),
widget aplikace), „null“ může být poskytnuto jako rodič::

nový místní widget Přivítání (s hodnotou null).

Zničení widgetů
------------------

Pokud můžete obsah zobrazit uživatelům, měli byste být schopni jej také smazat.
Je provedeno metodou :meth:`~odoo.Widget.destroy`::

pozdrav.Destroy();

Když se widget zničí, tak nejprve volá
Všechny své děti vymaže metodou ~odoo.Widget.destroy a poté se sama vymaže.
z DOMu. Pokud jste si vytvořili trvalé struktury
:funkce ~odoo.Widget.init nebo funkce ~odoo.Widget.start,
musí být explicitně uklizeno (protože sběr odpadu nebude s tímto úkolem zacházet).
jí, můžete přepsat metodu :meth:`~odoo.Widget.destroy`.

.. nebezpečí::
při přebírání metody :func:`~odoo.Widget.destroy`, funkce „_super()“
*musí být vždy voláno*, jinak nebudou widget a jeho děti dostupné.
správně uklidit, nezanechává možné paměťové úniky a „fantomové události“.
i když se žádný chybový hlášení nezobrazí

QWeb Template Engine
========================

V předchozím odstavci jsme přidali obsah do našich widgetů přímo
manipulace s jejich DOMem:

tento.$el.append(„<div>Ahoj, milý uživatelé Odoo!“);

Tento způsob umožňuje vytvářet a zobrazovat jakýkoliv obsah, ale je nepraktický
při vytváření velkého množství DOM (mnoho duplikací a citací)
(výzvy, ...).

Jako mnoho jiných prostředí používá i Odoo řešení pomocí „vložky šablony“ _.
Šablonový motor v Odoo se nazývá :ref:`reference/qweb`.

QWeb je jazyk šablonovacího systému založený na XML, podobný Genshi.
<http://cs.wikipedia.org/wiki/Genshi_(šablonovací_jazyk)>`,
<http://cs.wikipedia.org/wiki/Thymeleaf> nebo <http://cs.wikipedia.org/wiki/Facelets
<http://cs.wikipedia.org/wiki/Facelet>“. Má následující
vlastnosti:

* Je naprogramován v JavaScriptu a zobrazen v prohlížeči.
* Každý šablonový soubor (.xml soubory) obsahuje více šablon.
* Má speciální podporu v widgetech Odoo Web:class:`~odoo.Widget`, i když
Může být použit mimo webový klient Odoo (a je možné jej používat)
:třída:~odoo.Widget bez použití QWeb

.. poznámka::
Důvodem používání QWeb namísto stávajícího javascriptového šablony
výhodou motorů je rozšiřitelnost stávajících (třetích stran) šablon, což
jako Odoo: `výhledy <../reference/user_interface/view_records>`.

Většina javascriptových šablonových motorů je textová, což znemožňuje snadné použití.
strukturální rozšiřitelnost, kde může být použita XML-založená šablona.
genericky upraveno pomocí např. XPath nebo CSS a stromového jazyka pro úpravy
(i když jen v XML). Tato flexibilita a rozšiřitelnost je základem
Je to charakteristické pro Odoo a ztráta byla nepřijatelná.

Použití QWeb
----------

Nejprve definujme jednoduchý šablonový soubor QWeb v téměř prázdném
Soubor „oepetstore/static/src/xml/petstore.xml“:

... blok kódu::xml


<šablony xml:space="preserve">

<div style="barva pozadí: červená;">To je nějaký jednoduchý HTML kód.</div>
</t>
</šablony>

Nyní můžeme používat tento šablonu uvnitř widgetu „Domovská stránka“. Pomocí
Proměnná „QWeb“ definovaná na začátku stránky nám umožňuje volat
šablona definovaná v souboru XML:

lokální.Domovská stránka = instance.Widget.extend({
funkce start():
tento.$el.append(QWeb.render("Stránka domů šablona"));
        },
    });

Funkce QWeb.render() hledá zadaný šablonu, převádí ji na řetězec
a vrací výsledek.

Ale protože třída Widget má speciální integraci pro QWeb
šablonu lze nastavit přímo na widgetu pomocí jeho
Atribut:~odoo.Widget.template~

lokální.Domovská stránka = instance.Widget.extend({
šablona: „Šablona domovské stránky“,
funkce start():
            ...
        },
    });

I když výsledek vypadá podobně, existují dvě rozdíly mezi těmito
Použití:

* S druhou verzí se šablona zobrazí až před tím.
:funkce:~odoo.Widget.start je volána
* V první verzi se do kořenového elementu widgetu přidá obsah šablony.
prvku, zatímco v druhé verzi je kořenovým prvkem šablony
jsou přímo nastaveny jako kořenové prvky widgetu. Proto se v „pozdravu“
Podpůvodní widget také získá červený podklad.

.. varování:
šablony by měly mít pouze jediný kořenový prvek, který není „t“, zejména pokud
jsou nastaveny jako atribut widgetu ~odoo.Widget.template. Pokud existují
více „kořenových prvků“, výsledky jsou neurčité (obvykle pouze první)
bude použit kořenový prvek a ostatní budou ignorovány).

QWeb Kontext
~~~~~~~~~~~~

Šablony QWeb mohou obsahovat základní logiku zobrazení a lze do nich přidávat data.

Pro explicitní volání funkce :func:`QWeb.render` se předává jako parametry
druhý parametr::

QWeb.render("Stránka domovské stránky", {jméno: "Klaus"});

s šablonou upravenou takto:

... blok kódu::xml

<t t-name="Stránka domů">
<div>Ahoj, <t t-esc="name"/></div>


bude mít následek:

.. kódový blok:: html

Ahoj, Klause

Při použití integrace třídy :class:`~odoo.Widget` není možné
poskytnout další informace do šablony. Šablona bude obsahovat pouze
kontextová proměnná „widget“, která odkazuje na widget, který je právě zobrazován.
před voláním funkce ~odoo.Widget.start (stav widgetu bude
v podstatě se jedná o to, co je zavedeno funkcí :func:`~odoo.Widget.init`:

... blok kódu::xml

<t t-name="Stránka domů">
<div>Ahoj <t t-esc="widget.name"/></div>


::

lokální.Domovská stránka = instance.Widget.extend({
šablona: „Šablona domovské stránky“,
funkce init(rodič):
tento._super(rodiče);
tento.jméno = "Mordecai";
        },
funkce start():
        },
    });

Výsledek:

.. kódový blok:: html

<div>Ahoj, Mordechai!</div>

Šablona prohlášení
~~~~~~~~~~~~~~~~~~~~

Podíváme se na způsob *zobrazení* šablon QWeb. Teď si ukážeme syntaxi
sami šablony.

Šablona QWeb je složena z běžného XML smíchaného s příkazy QWeb *.
Řádek s příkazem QWeb je deklarován pomocí atributů XML začínajících znakem „t-“.

Nejzákladnější příkaz je „t-name“, který se používá k deklaraci nových šablon.
šablonový soubor:

... blok kódu::xml

<šablony>

<div>To je nějaký jednoduchý HTML kód.</div>
</t>
</šablony>

Výraz „t-name“ bere název šablony, kterou definujeme, a vyjadřuje, že
Je možné ji zavolat pomocí funkce QWeb::render(). Může být používána jen na
nahoře v šabloně.

Útěk
~~~~~~~~

„T-esc“ lze použít k vypuštění textu:

... blok kódu::xml

<div>Ahoj, <t t-esc="name"/></div>

Výraz je vyhodnocen a výsledek se použije jako
Takto vyjádření je pak z HTML uvedeno a vloženo do dokumentu.
Výraz lze poskytnout pouze jméno proměnné jako výše nebo více
komplexní výraz jako početní operace:

... blok kódu::xml

<div><t t-esc="3+5"/></div>

nebo metodové volání:

... blok kódu::xml

<div><t t-esc="name.toUpperCase()" /></div>

Výstup do HTML
~~~~~~~~~~~~~~~

Pro vložení HTML do stránky, která se zobrazuje, použijte „t-raw“. Stejně jako u „t-esc“
Ve svém parametru bere libovolný javascriptový výraz, ale
provede krok HTML-escapování.

... blok kódu::xml

<div><t t-raw="jméno.odkaz(uživatelský účet)"/></div>

.. nebezpečí::

„t-raw“ *nemůže být použito na žádných datech, které mohou obsahovat neunesené
obsah poskytnutý uživatelem, což vede k „křížovému skriptování“
zranitelnosti

Podmínky
~~~~~~~~~~~~

QWeb může obsahovat podmíněné bloky pomocí „t-if“. Direktiva přijímá
arbitrární výraz, pokud je výraz falesný („false“, „null“, „0“).
nebo prázdný řetězec celý blok je potlačen, jinak se zobrazí.

... blok kódu::xml


<t t-if="pravda == pravda">
Pravda je pravdou.
</t>

Pravda není pravdou.
</t>


.. poznámka::

QWeb nemá strukturu „jinak“, použijte druhý t-if s
původní stav obrácený. Možná budete chtít uložit stav do
lokální proměnná, pokud je složitá nebo nákladná.

Smyčka
~~~~~~~~~

Pro iterování nad seznamem použijte „t-foreach“ a „t-as“. „t-foreach“ přijímá
Výraz, který se vrací seznam, aby jej bylo možné procházet pomocí „t-as“, přijímá jméno proměnné.
připojit k položce během iterace.

... blok kódu::xml


<t t-foreach="jména" t-as="jméno">

Ahoj, <t t-esc="name"/>
</div>
</t>


.. poznámka: „t-foreach“ lze použít i s čísly a objekty
(slovníky)

Definující vlastnosti
~~~~~~~~~~~~~~~~~~~

QWeb poskytuje dva příbuzné direktivy pro definování počítaných atributů:
:samp:`t-att-{name}` a :samp:`t-attf-{name}“. V obou případech je *name*
název atributu, který chcete vytvořit (například „t-att-id“ definuje atribut
„ID“ po vykreslení.

„t-att-“ přijímá JavaScriptovou výraz, jehož výsledek je nastaven jako
hodnota atributu, je nejvýhodnější, pokud má všechny hodnoty atributu.
počítáno:

... blok kódu::xml


Zadejte své jméno:
<input type="text" t-att-value="defaultName"/>


„t-attf-“ přijímá „formátovací řetězec“. Formátovací řetězec je prostý text s
Ve vnitřních interpolačních blocích je interpolační blok jazykem JavaScript.
výraz mezi „{{“ a „}}“, který bude nahrazen výsledkem
pro výrazy, které jsou částečně závislé na
literální a částečně vypočítané, jako například třída:

... blok kódu::xml

<div t-attf-class="container {{ left ? 'text-left' : '' }} {{ extra_class }}">
vložte obsah zde


Volání ostatních šablon
~~~~~~~~~~~~~~~~~~~~~~~

Šablony lze rozdělit na podšablony (pro jednoduchost, udržovatelnost).
opakovatelnosti nebo se vyhnout nadměrnému vnořování značek.

Toho se dosahuje pomocí příkazu t-call, který přijímá název
šablona pro zobrazení:

... blok kódu::xml

<t t-name="A">

<t t-call="B"/>
</div>

<t t-name="B">
<div class="i-am-b"/>


výstup z „A“ šablony bude následující:

... blok kódu::xml

<div class="jsem-to-je">
<div class="i-am-b"/>


Podskupinové šablony dědí renderovací kontext svého volajícího.

Chcete se dozvědět více o QWeb?
~~~~~~~~~~~~~~~~~~~~~~~~

Pro odkaz na QWeb viz :ref:`reference/qweb`.

Cvičení
~~~~~~~~

... cvičení:Použití QWeb v widgetech

Vytvořte widget, jehož konstruktor přijímá dva parametry kromě
„rodič“: „názvy produktů“ a „barva“.

    * „product_names“ by mělo být pole řetězců, které obsahuje každý název produktu.
produkt
    * „barva“ je řetězec obsahující barvu v formátu CSS (tj.
„#000000“ pro černou barvu.

Widget by měl zobrazovat názvy produktů jeden pod druhým.
každý v samostatném boxu s pozadím barvy s hodnotou
„barva“ a „okraj“. Měli byste použít QWeb k zobrazení HTML.
potřebný CSS by měl být v „oepetstore/static/src/css/petstore.css“.

Ve widgetu v „Domovské stránce“ zobrazte šest produktů.



        ::

odoo.oepetstore = funkce (instance, místní) {
var _t = instance.web._t
_lt = instance.web._lt;
var QWeb = instance.web.qweb;

místní.DomovskáStránka = instance.Výstup.rozšířit (
start: function () {
var produkty = nový widget s produkty
tento, ["procesor", "myš", "klávesnice", "grafická karta", "obrazovka"], "#00FF00");
produkty.přidatK(toto.$el);
                    },
                });

místní.ProduktyWidget = instance.Widget.extend({
šablona: „Produkty“,
funkce init(rodič, produkty, barva):
tento._super(rodiče);
tento.produkty = produkty;
tento.barva = barva;
                    },
                });

Příklad:
'domovská stránka obchodu se zvířaty', 'objekt instance.oepetstore.HomePage');
            }

... kódový blok::xml


<šablony xml:space="preserve">
<t t-name="Produkty widget">







</t>

</t>


... kódový blok:: CSS

.oe_products_item {
displej: inline-block;
hrana: 3 px;
margin: 5px;
hranice: 1 pixelová černá linka.
border-radius: 3px;
            }

.. obrázek: web/qweb.png
:align:center
:šířka: 70 %

Widget Helpers
==============

„Widget“ jQuery výběr
----------------------------

Výběr prvků DOM uvnitř widgetu lze provést voláním
Metoda „find()“ na kořenovém elementu widgetu:

tento.$el.find("input.my_input")...

Ale protože se jedná o běžnou operaci, třída Widget poskytuje
equivalentní zkratka přes metodu :func:`~odoo.Widget.$`:

místní.MyWidget = instance.Widget.extend({
funkce start():
tento.$("input.my_input")...
        },
    });

.. varování:

Globální funkce „$()“ by se měla používat jen výjimečně, pokud není
zcela nezbytné: výběr na kořenovém widgetu je omezený pouze
widget a lokální k němu, ale výběry s „$()“ jsou globální pro celý
stránce nebo aplikaci a může odpovídat částem jiných widgetů a zobrazení.
na nebezpečné nebo nepředvídatelné vedlejší účinky. Většinou by měl widget fungovat
na vlastní části DOMu (která je vlastně i jeho jedinou součástí) není důvod pro celosvětové vybírání.

Snadnější vazby událostí DOM
-------------------------

Dříve jsme přiřazovali události DOM pomocí běžných jQuery handlerů (např.
„Kliknutí“ nebo „změna“ na prvky widgetu::

místní.MyWidget = instance.Widget.extend({
funkce start():
var self = this;
tento.$(".my_button").klikni(funkce () {
self.tlačítko_kliknutí();
            });
        },
button_clicked: function () {
            ..
        },
    });

I když to funguje, má pár problémů:

1. Je poněkud rozvláčný.
2. nepodporuje nahrazování kořenového prvku widgetu během provozu.
připoutání se provádí pouze při spuštění metody „start()“ (během zobrazování widgetu).
inicializace
3. vyžaduje řešení „tohoto“ vázání

Widgety tedy poskytují zkratku k vazbě událostí DOMu
:attr:`~odoo.widget.events`::

místní.MyWidget = instance.Widget.extend({
události: {
„kliknutí na tlačítko .my_button“: „tlačítko bylo stisknuto“,
        },
button_clicked: function () {
            ..
        }
    });

Odkaz na události je objektem (mapováním) události k
funkci nebo metodu, kterou je třeba zavolat při spuštění události:

* Klíč je název události, možná doplněný o selektor CSS, ve kterém
pouze v případě, že se událost stane na vybraném podčásti, bude funkce
nebo metoda spuštění: „click“ bude zpracovávat všechny kliknutí uvnitř widgetu.
„click .my_button“ bude zacházet pouze s kliknutími na prvky, které nesou
„my_button“ třída
* hodnota je akce, která se vykoná při spuštění události

Může být buď funkcí::

události: {
'click': function (e) { /* kód zde */ }
      }

nebo název metody na objektu (viz příklad výše).

V každém případě je „to“ widget a funkce dostává widget jako argument.
jediný parametr, objekt události jQuery pro danou událost.

Widgety událostí a vlastnosti
============================

Akce
------

Widgety poskytují vlastní systém událostí (oddělený od systému událostí DOM/jQuery).
popisované výše): widget může spouštět události na samotném sobě nebo na jiných widgetech (nebo
sám o sobě může vázat a poslouchat tyto události:

místní.Potvrzovací widget je rozšířením widgetu a má následující konstruktor:
události: {
"kliknout na tlačítko OK":
tento.spustit("uživatel zvolil", true);
            },
'kliknout na tlačítko.cancel_button': function () {
tento spustí událost user_chose s hodnotou false.
            }
        },
funkce start():
tento.$el.append(„Chcete si být jisti, že chcete provést tuto akci?“ +
"<button type='button' class='ok_button'>OK</button>"
"<tlačítko třídy 'zrušit_tlačítko' >Zrušit</tlačítko>");
        },
    });

Tento widget slouží jako fasáda, převádí uživatelské vstupy (pomocí událostí DOM)
do dokumentovatelného vnitřního události, ke které mohou být rodičovské widgety přiřazeny
sama.

Funkce ~odoo.Widget.trigger() přijímá jméno události, kterou chceme spustit
jeho první (povinný) argument, další jsou považovány za událost
a předána přímo posluchačům.

Poté můžeme vytvořit rodičovskou událost, která bude obsahovat náš obecný widget.
poslouchat událost „user_chose“ pomocí funkce :func:`~odoo.Widget.on`::

lokální.Domovská stránka = instance.Widget.extend({
funkce start():
var widget = nový widget potvrzení (toto).
widget.on("user_chose", tento, tento.user_chose);
widget přidat do tohoto objektu.
        },
user_chose: function (potvrdil) {
Pokud je potvrzení, tak
console.log("Uživatel souhlasil s pokračováním");
}
console.log("Uživatel odmítl pokračovat");
            }
        },
    });

Funkce: ~odoo.Widget.on() připojuje funkci, která se má volat při
identifikované událostí „event_name“ je. Argument „func“ představuje
funkci, kterou chcete volat a „objekt“ je objekt, na který se tato funkce vztahuje.
pokud je metoda, pak se volá funkce s
další argumenty funkce :func:`~odoo.Widget.trigger`, pokud je
jakákoli. Příklad:

funkce start():
widget = ...
widget.přidat(„my_event“, tento, tento.my_event_triggered);
Widget spustí událost my_event s parametry 1, 2 a 3.
    },
my_event_triggered: function (a, b, c) {
console.log(a, b, c);
        // will print "1 2 3"
    }

.. poznámka::

Způsobení události na jiném widgetu je obecně špatnou myšlenkou. Hlavní
Výjimkou je „odoo.web.bus“, který existuje zcela specificky
vysílat pořady, ve kterých by se mohl každý widget zúčastnit.
webová aplikace Odoo.

Vlastnosti
----------

Vlastnosti jsou velmi podobné běžným atributům objektů v tom, že umožňují
ukládání dat na instanci widgetu, ale mají navíc možnost
Aktivují události, když jsou nastaveny:

funkce start():
tento widget je ...
tento widget přidá na události "změna jména" (change:name) a přiřadí mu funkci name_changed.
tento widget nastaví na „Nicolas“.
    },
funkce name_changed:
console.log("Nový význam vlastnosti 'name' je", this.widget.get("name"));
    }

* Funkce ~odoo.Widget.set nastaví hodnotu vlastnosti a spustí
:samp:`změnit: {propname}` (kde *propname* je jméno vlastnosti, které bylo
prvním parametrem metody: funkce set() a „změna“
* Funkce ~odoo.Widget.get() získá hodnotu vlastnosti.

Cvičení
--------

... cvičení: Vlastnosti widgetu a události

Vytvořte widget „ColorInputWidget“, který bude zobrazovat 3 „<input
typu „text“: „“. Každý z těchto „<input>“ je určen k vložení
šestnáctkové číslo od 00 do FF. Když se jedno z těchto „<input>“ změní,
widgety, které uživatel upravil, musí požádat o obsah tří
„<input>“, přičemž hodnoty jejich proměnných sečtou, aby vznikl kompletní kód barev CSS
(„#00FF00“), a výsledek vložte do vlastnosti „color“. Prosím
pozorně si přečtěte událost „change()“ v jQuery, kterou lze přiřadit na jakýkoliv HTML
„<input>“ prvek a metoda „val()“, která může vyhledat aktuální hodnotu.
Hodnota tohoto „<input>“ může být užitečná pro tuto cvičení.

Pak upravte widget „Domovská stránka“ tak, aby vytvářel widget „Vstupní pole pro barvy“.
a zobrazit ji. Widget „Domovská stránka“ by měl také zobrazovat prázdnou
čtverec. Tento čtverec musí mít v každém okamžiku stejnou velikost.
pozadí jako barvu vlastnosti „barva“
Instance třídy „ColorInputWidget“.

Využijte QWeb k generování všech HTML stránek.



        ::

odoo.oepetstore = funkce (instance, místní) {
var _t = instance.web._t
_lt = instance.web._lt;
var QWeb = instance.web.qweb;

místní.BarvaVstupníhoZařízení = instance.Widget.extend({
šablona: „Barva vstupního pole“,
events: {
'změna vstupu': 'vstup_změněn'
                    },
start: function () {
tento.input_změnil( );
návrat tohoto._super();
                    },
onInputChanged: function () {
var barva = [
                            "#",
tento.$(".oe_color_red").val()
tento.find("[class='oe_color_green']").val()
this.$(".oe_color_blue").val()
]).join('');
tento.nastavit("barva", barvu);
                    },
                });

místní.DomovskáStránka = instance.Výstup.rozšířit (
šablona: „Domovská stránka“,
start: function () {
tento.barvaVstupu = nový widget barvy z místní knihovny;
tento.inputColor.on("změna:barva", tento, tento.color_changed);
vrátí tento objekt zpět do pole vstupu barvy a připojí se k tomuto objektu.
                    },
color_changed: function() {
tento.$(".oe_color_div").css("background-color", this.colorInput.get("color"));
                    },
                });

příkladu.web.klientské akce.Přidat ('domovská stránka obchodu s domácími mazlíčky', 'obchod s domácími mazlíčky.Domovská stránka');
            }

... kódový blok::xml


<šablony xml:space="preserve">


Červená: <input type="text" class="oe_color_red" value="00"></input><br />



</t>
<t t-name="Domovská stránka">



</t>


... kódový blok:: CSS

.oe_color_div {
šířka: 100 px;
výška: 100 px;
margin-right: 10px;
            }

Upravit stávající widgety a třídy
===================================

Třídílný systém webového rámce Odoo umožňuje přímo upravovat
existující třídy, které používají metodu include()::

var TestClass = instance.web.Class.extend({
testovací metoda:
vrací „Ahoj“.
        },
    });

TestClass.include({
testovací metoda:
návratová hodnota je tedy toto plus „world“
        },
    });

console.log(new TestClass().testMetoda());
    // will print "hello world"

Tento systém je podobný dědickému mechanismu, s tím rozdílem, že bude měnit
místo vytváření nové třídy použít stávající třídu.

V tomto případě bude „this._super()“ volat původní implementaci
Metoda nahrazena/přepsána. Pokud třída již měla podtřídy, všechny
volání metody „_super()“ v podtřídách volá nové implementace
definované v volání funkce: ~odoo.web.Class.include. To také funguje
pokud byly vytvořeny některé instancí třídy (nebo kterékoli z jejích podtříd).
před voláním metody :meth:`~odoo.Widget.include`.

Překlady
============

Proces převodu textu do kódu v Pythonu a JavaScriptu je velmi
podobné. Mohl jste si všimnout těchto řádků na začátku článku.
soubor „petstore.js“:

_t = instance.web._t
_lt = instance.web._lt;

Tyto řádky jsou pouze pro dočasné načtení překladových funkcí v aktuálním
JavaScriptový modul. Jeho použití je následující:

tento.$el.text(_t("Ahoj uživateli!"));

V Odoo se překladové soubory automaticky generují skenováním zdrojových
kód. Všechny kusy kódu, které volají určitou funkci, jsou detekovány a
Do překladového souboru se přidá obsah, který pak bude odeslán
překladatelé. V jazyce Python je funkce „_()“. V jazyce JavaScript je funkce
:funkce ~odoo.web._t (a také funkce ~odoo.web._lt).

Funkce „_t()“ vrátí překlad definovaný pro zadaný text. Pokud není
je definována pro tento text, vrátí originální text tak, jak je.

.. poznámka::

Pro vložení uživatelsky definovaných hodnot do přeložitelných řetězců se doporučuje
použít funkci _.str.sprintf
<http://gabceb.github.io/underscore.string.site/#sprintf> s názvem
argumenty po překladu::

tento.$el.text(_.str.sprintf(
_("Ahoj %(uživatel)s!")
uživatel: „Ed“
        }));

To dělá přeložitelné řetězce čitelnější pro překladatele a poskytuje
jim dává větší pružnost při přeskupování nebo ignorování parametrů.

Funkce ~odoo.web._lt („překlad pomocí lazy“) je podobná, ale o něco složitější.
komplexní: místo okamžitého překladu svého parametru se vrací
objekt, který při převodu na řetězec provede překlad.

Je používán k definování překladitelných termínů před tím, než bude systém
inicializovány, například pro atributy třídy (protože moduly se načítají před
je nastaven jazyk uživatele a stahují se překlady.

Komunikace s serverem Odoo
==================================

Kontaktování modelů
-----------------

Většina operací s Odoo zahrnuje komunikaci s modelem, který implementuje
podnikatelskou společností, pak by se tyto modely mohly (případně) setkat s nějakými
databázový motor (obvykle PostgreSQL_).

Ačkoli jQuery poskytuje funkci $.ajax pro interakce sítě,
Komunikace s Odoo vyžaduje další metadatové informace, které je nutné nastavit před každým
volání by bylo nepřehledné a chybové. Proto Odoo web nabízí
vyšší úrovně komunikačních primitivů.

Chcete-li to ukázat, soubor „petstore.py“ již obsahuje malý model
s vzorkovým postupem:

... kódový blok:: python

klasa zprávy_dne(model.Model):
_name = "oepetstore.zpráva_dne"

@ApiModel
def my_metoda(self):
return {"hello": "world"}

zpráva = text(fields),
barva = fields.Char(velikost=20)

Toto deklaruje model s dvěma poli a metodou „my_method()“, která
vrací slovník obsahující přesný výraz.

Tady je vzorek widgetu, který volá „my_method()“ a zobrazuje výsledek:

lokální.Domovská stránka = instance.Widget.extend({
funkce start():
var self = this;
var model = nový instanci webu.Model ("oepetstore.zpráva dne");
model.call("můj_metod", {kontext: nový instanci.web.Složený kontext() }). Poté (funkce(výsledek)):
self.$el.append(„<div>Ahoj „ + výsledek["ahoj"] + „</div>“);
                // will show "Hello world" to the user
            });
        },
    });

Třída, která se používá pro model Odoo, je třída:class:`odoo.Model`.
instancovaný s názvem modelu Odoo jako prvním parametrem
(„Opeřený obchodník zpráva dne“ zde).

Funkce ~odoo.web.Model.call() může volat jakýkoliv (veřejný) metoda modelu.
Odoo model, který přijímá následující pozice argumentů:

„jméno“
Název metody, kterou chceme volat, „my_method“ zde
„args“
seznam „argumentů v pořadí“_ poskytnout metodě. Protože metoda
Příklad nemá žádný pozice argument k poskytnutí, takže „args“ parametr není
Vybavení je k dispozici.

Tady je další příklad s pozicí argumentů:

... kódový blok:: python

@ApiModel
def my_metoda2(self, a, b, c): ...

...... kódový blok:: javascript

model.call("my_method", [1, 2, 3], ...
      // with this a=1, b=2 and c=3

„Kwargs“
a mapování „klíčových argumentů“ k předání. Příklad poskytuje pouze jeden
argument „kontext“.

... kódový blok:: python

@ApiModel
def my_metoda2(self, a, b, c): ...

...... kódový blok:: javascript

model.call("my_method", [], {a: 1, b: 2, c: 3, ...
      // with this a=1, b=2 and c=3

Funkce ~odoo.Widget.call vrací odložený výraz, který je vyřešen hodnotou
vracený metodou modelu jako první argument.

Složený kontext
---------------

Předchozí část používala argument „kontext“, který nebyl vysvětlen.
metoda volání::

model.call("my_method", {context: nový instanci.web.Složený kontext()})

Kontext je jako „magický“ argument, který klient webu vždy dá.
server při volání metody. Kontext je slovník obsahující
více klíčů. Jedním z nejdůležitějších je jazyk uživatele, který se používá
serveru, aby překládal všechny zprávy aplikace. Další je
časové pásmo uživatele používané k výpočtu správných dat a časů v případě Odoo
je používána lidmi z různých zemí.

„Argument“ je nutný ve všech metodách, jinak by se mohly stát špatné věci.
může nastat (například pokud aplikace nebude správně přeložena). Proto
Když voláte metodu modelu, měli byste vždy poskytnout tento argument.
řešením je použít třídu :class:`odoo.web.CompoundContext`.

Třída CompoundContext je používána k předání uživatelského jména
kontextu (jazyk, časové pásmo atd.) k serveru a přidání nových
klíče do kontextu (některé modely používají libovolné klíče přidávané do
kontextu). Vytváří se dáním jeho konstruktorovi libovolnému počtu
slovníky nebo jiné instancí třídy CompoundContext.
sloučit všechny kontexty před odesláním na server.

... kódový blok: JavaScript

model.call('my_method', {'context': new instance.web.CompoundContext({'new_key': 'key_value'})})

... kódový blok:: python

@ApiModel
def my_metoda(self):
print(self.kontext)
        // will print: {'lang': 'en_US', 'new_key': 'key_value', 'tz': 'Europe/Brussels', 'uid': 1}

V argumentu „kontext“ je vidět, že slovník obsahuje některé klíče.
se týkají konfigurace uživatele v Odoo.
„nový klíč“, který byl přidán při instanciování
:třída:~odoo.web.CompoundContext

Dotazy
-------

Pokud chcete interagovat s Odoo, postačí vám funkce
modely, Odoo Web poskytuje pomocníka pro jednodušší a srozumitelnější dotazování modelů

:funkce ~odoo.Model.query, která slouží jako zkratka pro běžné dotazy
kombinace metody ~odoo.models.Model.search
::py:meth:`~odoo.models.Model.read`. Poskytuje jasnější syntaxi pro vyhledávání
a číst modely::

model.query(['jméno', 'login', 'uživatelské e-mailové adresy', 'podpisy'])
.filter(["active", "=", true], ["company_id", "=", hlavní společnost])
.limit(15)
.all() .then(function (uživatelé) {
        // do work with users records
    });

proti:

model.call('search', [[["active", "=", true], ["company_id", "=", hlavní společnost]]], {limit: 15})
.poté, co se vám zobrazí výsledky vyhledávání,
return model.call('read', [ids, ['jméno', 'login', 'e-mail', 'podpis']]);
        })
.poté, co se vám zobrazí uživatelé,
            // do work with users records
        });

* Funkce ~odoo.web.Model.query přijímá seznam polí jako
parametr (pokud není zadána pole, jsou vyzvednuty všechny pole modelu).
Vrací objekt :class:`odoo.web.Query`, který lze dále upravit před
byl popraven
* Třída Query reprezentuje dotaz, který je vytvářen.
nezměnitelné, metody pro přizpůsobení dotazu vrací skutečně upravenou kopii.
Proto je možné používat původní a novou verzi vedle sebe.
:třída:~odoo.web.Query pro možnosti přizpůsobení.

Když je dotaz nastaven tak, jak chcete, jednoduše zavolejte
Funkci odoo.web.Query.all, která ji spustí a vrátí
odkázal na výsledek, který je stejný jako
:py:metoda:'~odoo.models.Model.read' s, která je seznamem slovníků, kde každý
Slovník je požadovaný záznam, který má pro každé požadované pole klíč slovníku.

Cvičení
=========

.. cvičení: Zpráva dne

Vytvořte widget „Zpráva dne“, který zobrazuje poslední záznam.
„oepetstore.message_of_the_day“ vzorec. Widget by měl získat svůj obsah
nahrát hned, jak se zobrazí.

Zobrazte widget na domovské stránce obchodu s mazlíčky.



... kódový blok: JavaScript

odoo.oepetstore = funkce (instance, místní) {
var _t = instance.web._t
_lt = instance.web._lt;
var QWeb = instance.web.qweb;

místní.DomovskáStránka = instance.Výstup.rozšířit (
šablona: „Domovská stránka“,
start: function () {
vrací nový objekt MessageOfTheDay a přidá jej na konci do této proměnné.
                    },
                });

příkladu.web.klientské akce.Přidat ('domovská stránka obchodu s domácími mazlíčky', 'obchod s domácími mazlíčky.Domovská stránka');

místní.ZprávaDne = instance.Vývěska.rozšíření
šablona: „ZprávaDne“,
start: function () {
var self = this;
vrací nový instanci webu Model ("oepetstore.zpráva-dne").
.query("message")
.order_by('-create_date', '-id')
.first()
.poté(funkce(výsledek){
self.$(".oe_mywidget_message_of_the_day").text(result.message);
                            });
                    },
                });

            }

... kódový blok::xml


<šablony xml:space="preserve">
<t t-name="Domovská stránka">


</t>




</t>


... kódový blok:: CSS

.oe_petstore_motd {
margin: 5px;
padding: 5px;
border-radius: 3px;
pozadí: #F0EEEE;
            }

.. cvičení: Seznam hraček pro domácí zvířata

Vytvořte widget „Seznam hraček pro zvířata“ s pěti hračkami (pomocí jejich názvu
jejich obrazy).

Pelíšky pro domácí mazlíčky nejsou uloženy v nové verzi, ale jsou uloženy
„produkt.produkt“ pomocí speciální kategorie „Hračky pro domácí zvířata“. Můžete si je prohlédnout zde:
předem vygenerované hračky a přidat nové tím, že se vydáte
:menu_selection:`Obchod s domácími zvířaty --> Obchod s domácími zvířaty --> Hračky pro domácí zvířata.
Musíme prozkoumat „produkt.produkt“ a vytvořit správnou doménu,
vybírejte jen hračky pro domácí zvířata.

V Odoo se obvykle ukládají obrázky do běžných polí s kódováním
base64_, HTML podporuje zobrazení obrázků přímo ze souboru base64
:samp:`<img src="data:{mime_type};base64,{base64_image_data}"/>

Widget „PetToysList“ by se měl zobrazovat na domovské stránce.
právo na widget „Zprávy dne“. Budete potřebovat nějaké rozvržení
pomocí CSS k tomu, aby se to podařilo.



... kódový blok: JavaScript

odoo.oepetstore = funkce (instance, místní) {
var _t = instance.web._t
_lt = instance.web._lt;
var QWeb = instance.web.qweb;

místní.DomovskáStránka = instance.Výstup.rozšířit (
šablona: „Domovská stránka“,
start: function () {
vrací seznam všech proměnných, které byly zadány do funkce
nový místní PetToysList(toto).připojit k tomuto ($ ('. oe_petstore_homepage_left'))
nový místní MessageOfTheDay(tohoto).Připojit k tomuto $ ('.oe_petstore_homepage_right')
                        ]);
                    }
                });
příkladu.web.klientské akce.Přidat ('domovská stránka obchodu s domácími mazlíčky', 'obchod s domácími mazlíčky.Domovská stránka');

místní.ZprávaDne = instance.Vývěska.rozšíření
šablona: 'ZprávaDne',
start: function () {
var self = this;
vrací nový instanci webu Model ('oepetstore.message_of_the_day').
.query("message")
.order_by('-create_date', '-id')
.first()
.poté(funkce (výsledek) {
self.$(".oe_mywidget_message_of_the_day").text(result.message);
                            });
                    }
                });

místní.PetToysList = instance.Widget.extend({
šablona: 'Seznam hraček pro zvířata',
start: function () {
var self = this;
vrací nový instanci webu Model('produkt.produkt')
.query(["jméno", "obrázek"])
.filter(["categ_id.name", "===", "Pet Toys"])
.limit(5)
.all()
.poté, co byly získány výsledky
_(výsledky). Každou položku (item)
self.$el.append(QWeb.render('PetToy', {item: item}));
                                });
                            });
                    }
                });
            }

... kódový blok::xml



<šablony xml:space="preserve">
<t t-name="Domovská stránka">




</t>




</t>
<t t-name="Seznam hraček pro zvířata">
<div class="oe_petstore_pettoyslist">

</t>


<p><t t-esc="item.name"/></p>
<p><img src='data:image/jpg;base64,'+item.image+'/>

</t>


... kódový blok:: CSS

.oe_petstore_homepage {
zobrazit: tabulka;
            }

.oe_petstore_homepage_left {
zobrazení: buňka tabulky;
šířka: 300 px;
            }

.oe_petstore_homepage_right {
zobrazení: buňka tabulky;
šířka: 300 px;
            }

.oe_petstore_motd {
margin: 5px;
padding: 5px;
border-radius: 3px;
pozadí: #F0EEEE;
            }

.oe_petstore_pettoyslist {
padding: 5px;
            }

.oe_petstore_pettoy {
margin: 5px;
padding: 5px;
border-radius: 3px;
pozadí: #F0EEEE;
            }


Existující webové komponenty
=======================

Manažer akcí
------------------

V Odoo se mnoho operací spouští z akce:
otevření položky menu (na zobrazení), tisk výstupu, ...

Akce jsou kusy dat popisující, jak by se měl klient zachovat na základě
aktivace obsahu. Akce mohou být uloženy (a čteny prostřednictvím
modelu) nebo mohou být generovány na místě (pro klienta lokálně).
skriptovacím jazykem JavaScript nebo vzdáleně pomocí metody modelu.

V Odoo Webu je komponenta zodpovědná za zpracování a reakci na tyto
akcí je *Manager akcí*.

Použitím Správce akcí
~~~~~~~~~~~~~~~~~~~~~~~~

Akční manažer lze vyvolat přímo z JavaScriptového kódu tím, že vytvoříte
slovník popisující: „akci <../reference/backend/actions>“
a voláním instanci akčního manažera s ní.

Funkce :func:`~odoo.Widget.do_action` je zkratkou třídy :class:`~odoo.Widget`.
Vyhledání „současného“ manažera akcí a spuštění akce:

instance.web.TestWidget = instance.Widget.extend({
funkce pro přesměrování na novou akci:
tento.vykonat(parametry)
typ: 'ir.actions.act_window',
model: "produkt.produkt"
res_id: 1
pohledy: [false, 'form']
cíl: 'aktuální'
kontext: {}
            });
        },
    });

Nejběžnějším typem akce je „ir.actions.act_window“, který poskytuje
zobrazení modelu, jehož nejčastější formou je
atributy jsou:

„res_model“
Model pro zobrazení v pohledech
„res_id“ (volitelné)
Pro formulářové pohledy je v „res_model“ předvybraný záznam.
„pohledy“
Seznamuje s pohledy, které jsou k dispozici v akci.
„[ID záznamu, typ záznamu]“, ID záznamu může buď být identifikátor databáze
zobrazení typu správného nebo „false“ pro použití výchozího zobrazení
určeného typu. Zobrazení typů se nemohou vyskytovat vícekrát. Akce
Otevře se první pohled na seznamu.
„cíl“
Buď „aktuální“ (výchozí), který nahradí část „obsahu“,
webovým klientem nebo „nový“ pro otevření akce v dialogovém okně.
„kontext“
Další kontextová data, která lze použít v akci.

.. cvičení: Skok na produkt

Změňte komponentu „PetToysList“ tak, že kliknutím na hračku nahradíte
domovskou stránku podle tvaru hračky.



... kódový blok: JavaScript

místní.PetToysList = instance.Widget.extend({
šablona: PetToysList,
události: {
'.oe_petstore_pettoy .click': 'vybrané položky',
                },
funkce start() {
var self = this;
vrací nový instanci web.Modelu ('produkt.produkt')
.query(["jméno", "obrázek"])
.filter(['categ_id.name', '==', "Hračky pro zvířata"])
.limit(5)
.all()
.poté, co byly získány výsledky,
_(výsledky). Každou položku (item)
self.$el.append(QWeb.render('PetToy', {item: item}))
                            });
                        });
                },
funkce pro výběr položky (event):
do_action(
typ: 'ir.actions.act_window',
model: 'product.product',
res_id: $(event.currentTarget).data('id'),
pohledy: [ [false, "form"] ]
                    });
                },
            });

... kódový blok::xml

<t t-name="PetToy">

<p><t t-esc="item.name"/></p>




...jaktovys/webu/klientské akce:

Akce klienta
--------------

V průběhu celého návodu jsme používali jednoduchý „widget HomePage“, který je k dispozici na
Klient automaticky spustíme, když vybereme správný položku v nabídce. Ale jak
Odoo web ví, že tento widget začíná? Protože widget je registrován jako
*akce klienta*.

Akce klienta je (jak již název napovídá) typ akce definovaný téměř
celé v klientovi, ve skriptovacím jazyce pro webové aplikace Odoo. Server prostě jen odesílá
akční značku (arbitrární název) a možná několik parametrů.
Všechno ostatní je řešeno vlastním klientským kódem.

Naše widget je registrováno jako zpracovatel akce klienta prostřednictvím tohoto:

instance.web.client_actions.add('petstore.homepage', 'instance.oepetstore.HomePage');


„instance.web.client_actions“ je :třída:`~odoo.web.Registry`, ve které
manažer akcí vyhledává klientské akční zpracovatele, když je potřeba akci provést.
Jeden. První parametr metody Registry.add() je název
(tag) akce klienta a druhý parametr je cesta ke widgetu
od kořenového adresáře webového klienta Odoo.

Když musí být spuštěna akce klienta, hledá její značku
v registru chodí po zadané cestě a zobrazí widget, který nalezne
Konec.

.. poznámka: klientský akční zpracovatel může být také běžnou funkcí, v takovém případě
bude volán a jeho výsledek (pokud existuje) bude interpretován jako
:Další akci, kterou je třeba provést.

Na straně serveru jsme jednoduše definovali akci „ir.actions.client“:

... blok kódu::xml

<záznam id="domovská stránka" typu "ir.actions.client">
<políčko jméno="tag">petstore.homepage</políčko>
</záznam>

a menu, které otevírá akci:

... blok kódu::xml


name="Domovská stránka" action="action_home_page"/>

Architektura pohledů
-------------------------

Velká část užitečnosti a komplexity Odoo webu spočívá v pohledech. Každý pohled
typ je způsob zobrazení modelu v klientovi.

View Manager
~~~~~~~~~~~~~~~~

Když instanci ActionManageru přijde akce typu
„ir.actions.act_window“ a přenáší odpovědnost za synchronizaci a správu
sám se pak o ně postará view manager, který je buď zobrazí nebo
více pohledů podle požadavků původního úkonu:

.. obrázek: web/viewarchitecture.png
:align:center
:šířka: 40 %

Názory
~~~~~~~~~

Výhledy Odoo jsou implementovány prostřednictvím podtřídy
třídy: `odoo.web.View`, která poskytuje nějaký obecný základní strukturu
pro zpracování událostí a zobrazování informací o modelech.

Výhled hledání je považován za typ výhledu v rámci hlavního rámce Odoo, ale
je zpracovávána samostatně klientem webu (protože je trvalou součástí a
Mohou se vzájemně ovlivňovat s ostatními pohledy (což běžné pohledy nedokáží).

Viditelnost je zodpovědná za načítání svého vlastního popisu XML (pomocí
:py:class:`~odoo.models.Model.fields_view_get`) a jakýkoli jiný zdroj dat
Pro tento účel jsou pohledy vybaveny volitelným pohledem
identifikátor nastavený jako atribut :attr:`~odoo.web.View.view_id`.

Výhledy jsou také poskytovány s instancí třídy `~odoo.web.DataSet`,
obsahuje nejdůležitější informace o modelech (název modelu a případně další).
id záznamů).

Názory mohou také chtít vyhledávací dotazy řešit přesměrováním
:funkce dohledávání v aplikaci Odoo, a aktualizace jejich
:třída ~odoo.web.DataSet, pokud je potřeba.

Formulářové pole Zobrazení
--------------------

Obecný požadavek je rozšíření webového formuláře o nové způsoby
Zobrazení polí.

Všechny vložené pole mají výchozí zobrazení implementace, nová
formulářový prvek může být nutný k správné interakci s novým typem pole.
(např. pole GIS nebo vytvářet nové reprezentace a způsoby).
interagovat s existujícími typy polí (např. ověřit
:py:class:`~odoo.fields.Char` pole, která by měla obsahovat e-mailové adresy
a zobrazovat je jako e-mailové odkazy.

Pro explicitní specifikaci, jaký formulářový prvek by měl být použit k zobrazení pole.
Použijte v popisu pohledu atribut „widget“:

... blok kódu::xml



.. poznámka::

    * stejný widget se používá v režimu „zobrazení“ i „upravování“.
v případě zobrazení formuláře není možné používat widget v jednom a jiném
widget v druhém
    * a dané pole (jméno) nesmí být v jedné formě použito vícekrát.
    * Widget může ignorovat aktuální režim zobrazení formuláře a zůstat
stejné v obou režimech prohlížení a editaci

... vše: většina toho by měla být pravděpodobně přesunuta do pokročilého formuláře

Pole jsou instancována po zobrazení formuláře, který přečetl svou popisku v XML
a vytvořil odpovídající HTML, který popisuje tuto situaci. Po
Takže vzorec pro výhled pole bude komunikovat s objekty pole pomocí nějakého
metodami, které jsou definovány v „FieldInterface“.
rozhraní. Většina polí dědí „AbstractField“ abstraktní třídu.
třída, která definuje některé výchozí mechanismy, které je třeba implementovat
Ve většině oborů.

Níže jsou uvedeny některé povinnosti polní třídy:

* Třída pole musí zobrazit a umožnit uživateli upravovat hodnotu pole.
* Musí správně implementovat tři atributy pole dostupné ve všech polích
Odoo. Třída „AbstractField“ již implementuje algoritmus, který
dynamicky vypočítává hodnotu těchto atributů (mohou se měnit v průběhu času).
významný okamžik, protože jejich hodnota se mění v závislosti na hodnotě jiných
pole). Hodnoty jsou uloženy v poli *Vlastnosti widgetu* (widget
Vlastnosti byly vysvětleny dříve v tomto průvodci. Jejich zodpovědnost
každého pole třídy, aby tyto vlastnosti widgetu zkontrolovala a dynamicky se k nim přizpůsobila.
podle jejich hodnoty. Níže je popsáno, jaký je rozdíl mezi nimi.
atributy:

  * „Povinné“: pole musí mít hodnotu před uložením. Pokud „povinné“,
Pokud je „true“ a pole nemá hodnotu, metoda
„is_valid()“ pole musí vrátit „false“.
  * „neviditelný“: Pokud je „pravda“, pole musí být neviditelné.
„Třída AbstractField“ již obsahuje základní implementaci této metody.
chování, které se hodí do většiny oborů.
  * „jen pro čtení“: Pokud je „pravda“, pole nesmí být upravitelné.
uživatel. Většina polí v Odoo má zcela odlišné chování podle toho, kdo je používá.
na hodnotu „const“. Například pole „FieldChar“ zobrazuje
HTML „<input>“ v případě, že je editovatelný a jednoduše zobrazuje text.
To znamená, že má mnohem více kódu, než by potřebovala.
pouze jednu chování, ale je to nutné k zajištění dobrého uživatelského zážitku.
zkušenosti.

* Metody pole mají dvě metody „set_value()“ a „get_value()“, které
zavolána formulářovým pohledem, aby mu poskytla hodnotu k zobrazení a naopak vrátila novou
hodnota zadaná uživatelem. Tyto metody musí být schopny zpracovat hodnotu jako
vydané Odoo serverem při provádění operace „čtení“ na modelu a
zpět platnou hodnotu pro funkci „write()“. Pamatujte, že v JavaScriptu/Pythonu
datových typů používaných k reprezentování hodnot, které jsou vráceny funkcí „read()“ a předávány do
„Write()“ není v Odoo nutně stejná jako u jiných programů. Například při čtení
je vždycky dvojice s prvním hodnotovým údajem, který je identifikátorem
První je záznam a druhý je jméno get (tj. „(15, Agrolait)``).
při psaní mnoho2jednačky musí být jediným číslem, nikoli součtem
už ne. „Abstraktní pole“ má výchozí implementaci těchto metod
to funguje dobře pro jednoduché datové typy a nastaví vlastnost widgetu s názvem
„hodnota“.

Pro lepší pochopení, jak implementovat pole, je třeba
byli silně vyzváni, aby se podívali na definici „FieldInterface“
rozhraní a třídu „AbstractField“ přímo v kódu webu Odoo
klient.

Vytvoření nového typu pole
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V této části vysvětlíme, jak vytvořit nový typ pole. Příklad
bude třeba znovu implementovat třídu „FieldChar“ a postupně vysvětlovat
Každá část.

Jednoduchý pole čtení
**********************

Tady je první implementace, která bude zobrazovat pouze text.
uživatel nebude moci upravovat obsah pole.

... kódový blok: JavaScript

local.FieldChar2 = instance.web.form.AbstractField.extend({
funkce init():
tento._super.apply(toto, argumenty);
tento.nastavit("hodnota","");
        },
render_value: function () {
tento.$el.text(toto.get("value"));
        },
    });

instance.web.form.widgets.add('char2', 'instance.oepetstore.FieldChar2');

V tomto příkladu deklarujeme třídu s názvem „FieldChar2“, která dědí od
„Abstraktní pole“. Třídu také zaregistrujeme v registru
„instance.web.form.widgets“ pod klíčem „char2“. To nám umožní
Použijte tento nový prvek v jakémkoliv formuláři zadáním „widget=char2“ do
„<field/>“ tag v deklaraci XML prohlížeče.

V tomto příkladu definujeme jedinou metodu: „render_value()“. Jediné, co dělá, je
zobrazit vlastnost „hodnota“ widgetu. Jsou to dva nástroje definované
Třída „AbstractField“. Formulář zobrazí volání třídy
metoda „set_value()“ pole pro nastavení hodnoty zobrazené hodnoty. Tato metoda
má již implementaci v „AbstractField“, která jednoduše nastaví
Vlastnost „hodnota“ widgetu. „Abstraktní pole“ také sleduje
„změna:hodnota“ událost na samotné sebe a volá „zobrazit hodnotu“ v případě, že
se vyskytuje. Proto je metoda render_value() pohodlnou metodou pro implementaci v dětech
třídy, které provádějí nějakou operaci každýkrát, když se změní hodnota pole.

V metodě „init()“ také definujeme výchozí hodnotu pole.
Žádný není specifikován v pohledu na formulář (předpokládáme výchozí hodnotu)
„char“ pole by mělo být prázdné.

Čtení/Zápis
****************

Čtené pole, které obsahují pouze text a neumožňují vkládání.
Uživatel může upravit, ale většina polí v Odoo také umožňuje úpravy.
Tím se pole stávají složitějšími, hlavně kvůli tomu, že pole jsou
aby zvládal oba režimy, tedy režim editační i needitační.
často úplně jiná (pro účely designu a použitelnosti), a oblasti
musí být schopna přepínat mezi režimy kdykoliv.

K získání informací o tom, v jakém režimu by měl být aktuální obor, je třeba použít třídu „AbstractField“.
Nastaví vlastnost widgetu s názvem „effective_readonly“. Hodnota pole by měla být
pro změnu vlastnosti widgetu a zobrazení správného režimu
Podle toho. Příklad:

local.FieldChar2 = instance.web.form.AbstractField.extend({
funkce init():
tento._super.apply(toto, argumenty);
tento.nastavit("hodnota","");
        },
funkce start():
tento.při "změně:účinné-jen-pro-čtení" tento, funkce () {
tento.zobrazit_pole();
tento.zobrazit_hodnotu();
            });
tento.zobrazit_pole();
návrat tohoto._super();
        },
funkce display_field():
var self = this;
tento.$el.html(QWeb.render("PoleChar2", {widget: tento}));
Pokud není tato vlastnost „pouze pro čtení“,
tento.$("input").on("change", function() {
self.internal_set_value(self.$("input").val());
                });
            }
        },
render_value: function () {
Pokud je tato proměnná nastavena na hodnotu true,
tento.$el.text(toto.get("value"));
}
tento.$("input").val(toto.get("value"));
            }
        },
    });

instance.web.form.widgets.add('char2', 'instance.oepetstore.FieldChar2');

... blok kódu::xml

<t t-name="PoleChar2">
<div class="oe_field_char2">
<t t-if="! widget.get('effective_readonly')">
<input type="text"></input>

</div>


Metoda „start()“ (která se volá hned po zobrazení widgetu)
(připojené k DOMu), na události „změna:účinná-jen-pro-čtení“ vázané.
nám umožňuje znovu zobrazit pole každýkrát, když změníme vlastnost widgetu
„Efektivní čtení“ změny. Tento událostní zpracovatel zavolá
„zobrazit pole“ (v angličtině „display_field()“), která je také přímo volána v „začít“.
„display_field()“ bylo vytvořeno speciálně pro tento prvek, není metoda
definované v „AbstractField“ nebo jiné třídě. Můžeme použít tento metodu
zobrazit obsah pole v závislosti na aktuálním režimu.

Od té doby je koncepce tohoto pole typická, s výjimkou
spoustu ověření, abychom věděli stav vlastnosti „effective_readonly“:

* V šabloně QWeb používané k zobrazení obsahu widgetu se zobrazí
pokud jsme v režimu čtení/zápis, tak „<input type="text" />“
v režimu čtení pouze.
* V metodě „zobrazit_pole()“ je nutné vázat na událost „změna“.
z „<input type="text" />“ a víte, když uživatel změní hodnotu.
hodnotu. Když k tomu dojde, voláme metodu „internal_set_value()“ s touto hodnotou.
novou hodnotu pole. Tato metoda je k dispozici jako pohodlná funkce
„Abstraktní pole“ třída. Tato metoda nastaví novou hodnotu v proměnné „hodnota“.
mají vlastnost, ale nevyvolají volání metody „render_value()“ (která není
je nezbytné, protože „<input type="text" />“ již obsahuje správný
hodnota.
* V metodě render_value() používáme úplně jiný kód pro zobrazení
hodnotu pole podle toho, zda se nacházíme v režimu čtení nebo zápisu.

... cvičení: Vytvořit pole barev

Vytvořte třídu „FieldColor“. Hodnota pole by měla být řetězec
obsahující barvu, jako je ta používaná v CSS (příklad: „#FF0000“ pro
červené barvy. V režimu pouze pro čtení by měl být v tomto poli zobrazen malý blok
její barva odpovídá hodnotě pole. V režimu čtení/zápis má
mělo zobrazit „<input typu="barva" />“. Tento typ „<input />“
je komponentou HTML5, která v některých prohlížečích nefunguje, ale ve většině ano.
Google Chrome, takže je v pořádku ho používat jako cvičení.

Tento widget můžete používat v formuláři zobrazení „zprávy dne“.
vzorem pro pole s názvem „barva“. Kromě toho můžete změnit
„Widget zprávy dne“ vytvořený v předchozí části této příručky
zobrazit zprávu dne s pozadím barvy uvedené v
„barva“ pole.



... kódový blok: JavaScript

local.FieldColor = instance.web.form.AbstractField.extend({
události: {
'změna vstupu': funkce (e) {
pokud (!tohoto.get('effective_readonly')) {
tento.interní_nastavit_hodnotu($(e.currentTarget).val());
                        }
                    }
                },
funkce init():
toto._super.apply(to, argumenty);
tento.nastavit("hodnota","");
                },
start: function () {
this.on("change:effective_readonly", this, function() {
tento.zobrazit_pole();
tento.zobrazit_hodnotu();
                    });
tento.zobrazit_pole();
návratová hodnota je tedy vrácena metodou _super().
                },
funkce_zobrazení_pole: function() {
tento.$el.html(QWeb.render("Barva pole", {widget: tento}));
                },
render_value: function () {
pokud je tato vlastnost nastavena na „pouze pro čtení“,
tento.$(".oe_field_color_content").css("barva pozadí", tento.get("hodnota") nebo "#FFFFFF");
} jinak {
tento.$("input").val(toto.get("value") nebo "#FFFFFF");
                    }
                },
            });
instance.web.form.widgets.add('barva', 'instance.oepetstore.FieldColor');

... kódový blok::xml

<t t-name="Barva pole">

<t t-if="widget.get('effective_readonly')">

</t>

<input type="color"></input>
</t>



... kódový blok:: CSS

.oe_field_color_content {
výška: 20 px;
šířka: 50 px;
hranice: 1 pixelová černá linka.
            }

Vlastní widgety pro formulář
----------------------------

Formulářové pole se používá k úpravě jednoho pole a je vnitřně propojen s
pole. To může být omezující, proto je také možné vytvořit
*formulářové položky* nejsou tak omezené a mají méně vazeb na konkrétní
životní cyklus.

Přizpůsobitelné formulářové prvky lze přidat do zobrazení formuláře pomocí značky „widget“:

... blok kódu::xml

<widget typu="xxx"/>

Tento typ widgetu bude jednoduše vytvořen při zobrazení formuláře.
vytváření HTML podle definice XML. Mají vlastnosti
s pole (například vlastností „effective_readonly“), ale jsou
Nebyly přiděleny konkrétní pole. A proto nemají metody jako
„get_value()“ a „set_value()“. Musí dědit od „FormWidget“
abstraktní třída.

Formulářové prvky mohou interagovat s poli formuláře posloucháním změn.
získávání nebo měnit jejich hodnoty. Můžou k nim přistupovat prostřednictvím
jejich atributu ~odoo.web.form.FormWidget.field_manager::

místní.WidgetMocnina = instance.web.form.FormWidget.extend({
funkce start():
tento._super();
tento.field_manager.na("field_changed:integer_a", tento, tento.zobrazit_výsledek);
tento.field_manager.on("field_changed:integer_b", tento, tento.zobrazit_výsledek);
tento.zobrazit_výsledek();
        },
funkce display_result():
var výsledek = tento.pole_manažer.get_field_value ("celé číslo a")
tento.field_manager.get_field_value("integer_b");
tento.$el.text("a * b = " + výsledek);
        }
    });

instance.web.form.custom_widgets.add('násobení', 'instance.oepetstore.WidgetMultiplication');

:attr:`~odoo.web.form.FormWidget` je obecně
sám o sobě třída FormView, ale funkce použité z ní by měly
se omezit na ty definované v mixinu třídy `~odoo.web.form.FieldManagerMixin`.
Největší užitek přináší:

* :meth:`~odoo.web.form.FieldManagerMixin.get_field_value(field_name)`
která vrací hodnotu pole.
* Metoda: ~odoo.web.form.FieldManagerMixin.set_values(values) nastaví hodnoty
pole hodnoty, vytvoří mapu „{název_pole: hodnota_ke_zadání}“
* Při každém změně hodnoty pole se vyvolá událost samp:`field_changed:{field_name}`
při změně hodnoty pole s názvem „field_name“

.. cvičení:Zobrazit souřadnice na mapě Googlu

Přidejte do tabulky „product.product“ dvě pole pro uložení zeměpisné šířky a délky.
Pak vytvořte nový widget pro zobrazení zeměpisné šířky a délky.
původ produktu na mapě

Pro zobrazení mapy použijte vložení map Google:

... kódový blok::html




kde „XXX“ je náhradou za zeměpisnou šířku a „YYY“ za délku.
zeměpisná délka.

Zobrazte dvě pole polohy a mapový widget, který používá tyto pole, v novém
stránka poznámkového bloku s výhledem na produkt.



... kódový blok: JavaScript

místní.WidgetCoordinates je rozšíření třídy instance.web.form.FormWidget následovně:
start: function () {
tento._super();
tento.field_manager.na("field_changed:poskytovatel_šířka", tento, tento.zobrazit_mapu);
tento.field_manager.připojit(„field_changed:provider_longitude“, tento, tento.zobrazit_mapu);
tento.zobrazitMapu();
                },
funkce_zobrazení_mapy: function () {
tento.$el.html(QWeb.render("WidgetCoordinates", {
„Šířka“: tento.field_manager.get_field_value („poskytovatel_šířka“) nebo 0
„délka“: tento.pole_manažer.získat_hodnotu pole („poskytovatel_délka“) nebo 0
                    }));
                }
            });

instance.web.form.custom_widgets.add('koordinace', 'instance.oepetstore.WidgetCoordinates');

... kódový blok::xml

<t t-name="WidgetCoordinates">
<iframe width="400" height="300">
src="https://maps.google.com/?ie=UTF8&amp;ll={{latitude}},{{longitude}}&amp;output=embed">
</iframe>


... cvičení: Získat aktuální souřadnice

Přidejte tlačítko, které vrátí souřadnice produktu na místo.
uživatelé, můžete si tyto souřadnice získat pomocí
`JavaScript geolokační API`.

Nyní bychom rádi zobrazili další tlačítko, které automaticky nastaví
souřadnice k aktuální poloze uživatele.

Jednoduchým způsobem je použít funkci určování polohy.
JavaScript API. „Podívejte se na dokumentaci online, abyste věděli, jak ji používat“._

... _Podívejte se na online dokumentaci, abyste věděli, jak ji používat: http://www.w3schools.com/html/html5_geolocation.asp

Prosím, také si všimněte, že uživatel by neměl být schopen
Klikněte na tlačítko v režimu čtení pouze, když je zobrazena stránka formuláře.
vlastní widget by měl správně zpracovávat vlastnost „effective_readonly“
Stejně jako u jakéhokoliv pole by se dalo jedno řešení najít v tom, že by se tlačítko
zmizí, když je „effective_readonly“ pravdivé.



... kódový blok: JavaScript

místní.WidgetCoordinates je rozšíření třídy instance.web.form.FormWidget následovně:
události: {
'klikněte na tlačítko': funkce() {
navigator.geolocation.getCurrentPosition(
this.proxy('přijatá pozice');
                    }
                },
start: function () {
var sup = this._super();
tento.field_manager.na("field_changed:poskytovatel_šířka", tento, tento.zobrazit_mapu);
tento.field_manager.připojit(„field_changed:provider_longitude“, tento, tento.zobrazit_mapu);
tento.on("změna:účinná-jen-pro-čtení", tento, tento.zobrazit_mapu);
tento.zobrazitMapu();
return sup;
                },
funkce_zobrazení_mapy: function () {
tento.$el.html(QWeb.render("WidgetCoordinates", {
„Šířka“: tento.field_manager.get_field_value („poskytovatel_šířka“) nebo 0
„délka“: tento.pole_manažer.získat_hodnotu pole („poskytovatel_délka“) nebo 0
                    }));
tento.$("button").toggle(! tento.get("effective_readonly"));
                },
funkce obdržená pozice (obj):
tento.pole_manažer.nastavit_hodnoty({
"provider_longitude": obj.coords.longitude,
"provozovatel_šířka": obj.coords.latitude
                    });
                },
            });

instance.web.form.custom_widgets.add('koordinace', 'instance.oepetstore.WidgetCoordinates');

... kódový blok::xml

<t t-name="WidgetCoordinates">
<iframe width="400" height="300">
src="https://maps.google.com/?ie=UTF8&amp;ll={{latitude}},{{longitude}}&amp;output=embed">
</iframe>
<tlačítko>Získat současnou polohu</tlačítko>


... jako samostatný pojem od instancí. V mnoha jazycích jsou třídy
Jsou plnohodnotnými objekty a samy o sobě instancí (objektu).
metaklasy), ale zůstává dvě poměrně oddělené hierarchie
mezi třídami a instancemi
... i překrývání rozdílů mezi prohlížeči, byť
Protože se to stalo méně nutným, časem.

.._jQuery: http://jquery.org
_Underscore.js: http://underscorejs.org
... _git: http://git-scm.com
... CSS: http://www.w3.org/Style/CSS/Overview.en.html
... _Jednoduché dědičství v JavaScriptu:
    http://ejohn.org/blog/simple-javascript-inheritance/
... W3C DOM: http://www.w3.org/TR/DOM-Level-3-Core/
... Qt: http://qt-project.org
..._Kakaové boby: https://developer.apple.com/technologies/mac/cocoa.html
..._GTK: http://www.gtk.org
.. šablonový motor: http://cs.wikipedia.org/wiki/Webový_šablonový_motor
... křížové skriptování: http://cs.wikipedia.org/wiki/Kr%C3%ADzov%C3%A9_skriptování
...objekt události jQuery: https://api.jquery.com/category/events/event-object/
... $.ajax: http://api.jquery.com/jQuery.ajax/
..._base64: http://cs.wikipedia.org/wiki/Base64
..._JavaScript geolokace API:
    http://diveintohtml5.info/geolocation.html
..._PostgreSQL: http://cs.wikipedia.org/wiki/PostgreSQL
... argumenty podle pozice:
... argumenty klíčového slova:
    https://docs.python.org/2/glossary.html#term-argument
