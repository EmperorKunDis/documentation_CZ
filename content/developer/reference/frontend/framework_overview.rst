==================
Přehled rámce
==================

Úvod
============

Odoo Javascript framework je sada funkcí/bloků, které poskytuje
„Web/“ doplněk, který pomáhá při tvorbě aplikací Odoo běžících v prohlížeči.
Odoo je totiž JavaScriptový rámec jedné stránky.
obvykle známý jako webový klient (k dispozici na adrese „/web“).

Webový klient začínal jako aplikace vytvořená pomocí vlastní třídy a widgetu
systém, ale nyní přechází na používání vlastních tříd JavaScriptu.
a sova jako součást systému. To vysvětluje, proč jsou oba systémy aktuálně
používání v kódu.

Z hlediska architektury je webový klient jednoduchou aplikací.
nemusí požadovat celou stránku z serveru každýkrát, když uživatel provede
akce. Namísto toho požaduje pouze to, co potřebuje, a pak nahrazuje / aktualizuje
přizpůsobit aktuální obrazovku a také spravuje URL tak, aby bylo v souladu s
současný stav.

JavaScriptový rámec (celý nebo některé jeho části) se používá i v jiných situacích.
například webové stránky nebo prodejní místo. Tato část je zaměřena
na webovém klientovi.

.. poznámka::

V prostředí Odoo je běžné vidět slova frontend a backend.
jako synonyma pro webové stránky Odoo (veřejné) a webového klienta, resp.
Toto pojmenování není možné zaměňovat s běžnějším použitím
prohlížeč (frontend) a server (backend).

.. poznámka::

V této dokumentaci se slovo „komponenta“ vždy vztahuje na nový Owl.
komponenty a widget odkazuje na staré widgety Odoo.

.. poznámka::

Všechny nové vývojové aktivity by měly být prováděny v Owlu, pokud možno!

Struktura kódu
==============

Složka „web/static/src“ obsahuje všechny „web/“ skripty (a CSS a
šablony) kódek. Zde je seznam nejdůležitějších složek:

- „jádro/“ většinu nízkých úrovních funkcí
- „políčka“ všechny komponenty pole
- „views/“ všechny komponenty JavaScriptu pro zobrazení („form“, „list“, …)
- „vyhledávací“ ovládací panel, vyhledávací lišta, vyhledávací panel, …
- „webklient/“ specifická kódová část pro webový klient: navigační lišta, nabídka uživatele, služba akce, …

„web/statické/zdroje“ je kořenový adresář. Vše uvnitř může být jednoduše
Do jazyka lze přidat pomocí předpony „@web“. Například takto můžeme do jazyka přidat
funkci „memoize“ nacházející se v adresáři „web/static/src/core/utils/functions“:

... kódový blok: JavaScript

import { memoizovat } z '@web/jádro/funkce/funkce';

Webová architektura
======================

Jako již bylo zmíněno, webový klient je aplikace pro vydavatele. Níže uvedený
zjednodušenou verzi svého vzoru:

... blok kódu::xml

<t t-name="web.WebClient">

<Navigační lišta/>
<ActionContainer/>




Jak vidíme, je to vlastně obal pro navigační lištu, aktuální akci a
další komponenty. „ActionContainer“ je vyšší řádový komponent
Ta zobrazí aktuální akční kontroler (tedy klientskou akci nebo
konkrétní pohled v případě akcí typu „act_window“). Správa akcí
Je to obrovská část jejich práce: akční služba si pamatuje hromadu
všechny aktivní akce (zobrazené v chlebovém kroku) a koordinuje je.
změna.

Další zajímavou věcí je „MainComponentsContainer“: je
pouze komponenta, která zobrazuje všechny registrované komponenty.
registru „hlavních komponent“. Díky tomu mohou ostatní části systému rozšířit
webový klient.

..._frontend/framework/environment:

Životní prostředí
===========

Jako aplikace Owl definuje vlastní prostředí (komponenty
může k němu přistupovat pomocí „this.env“. Zde je popis, co Odoo přidává do
Společný objekt „env“:

.. seznam tabulkový::
:šířky: 25 75
:hlavičky: 1

   * – Klíč
     - Hodnota
   * „Qweb“
     - vyžadované od sovy (obsahuje všechny šablony).
   * „bus“
     - :ref:`hlavní autobus <frontend/framework/bus>“, který slouží k koordinaci některých obecných událostí
   * „služby“
     - všechny nasazené služby: ref:<frontend/services> (obvykle se přistupuje
(s využitím funkce useService).
   * – „debug“
     - řetězec. Pokud není prázdný, webový klient je v režimu ladění:
   * „-_t“
     - překladová funkce
   * – isSmall
     - Pravda/nepravda. Pokud je hodnota pravdivá, webový klient je v současné době ve zobrazení pro mobilní zařízení (šířka obrazovky <= 767 px).

Takže například přeložit řetězec v komponentě (poznámka: šablony jsou
automaticky přeložené, takže v tomto případě není potřeba žádný konkrétní krok).
se toho nemusí bát:


... kódový blok: JavaScript

const someString = this.env._t('nějaký text');

.. poznámka::

Mít odkaz na prostředí je docela silné, protože poskytuje
přístup k veškerým službám. To je užitečné v mnoha případech: např.
uživatelské nabídky jsou většinou definovány jako řetězec, funkce přijímající proměnnou „env“
jako jediný parametr. To je dostatečné pro vyjádření všech potřeb uživatelského menu.

Stavební bloky
===============

Většina webového klienta je postavena na několika typech abstrakcí: registrů,
služby, komponenty a háčky.

Registry
----------

:ref:`Registry <frontend/registries>` jsou v podstatě jednoduchá klíčová/hodnotová mapa
, které uchovávají určitý druh objektů. Jsou důležitou součástí
rozšířitelnost uživatelského rozhraní: jednou, když je nějaký objekt zaregistrován, zbývá ostatnímu webu
může ji používat. Například v poli registru se nachází všechny komponenty pole
(nebo widgety), které lze použít v pohledech.

... kódový blok: JavaScript

import { Komponenta } z "@odoo/owl";
import { registry } z „./jádro/registry“;

třída MyFieldChar je dědicem komponenty
        // some code
    }

registry.kategorie("pole").přidat("my_field_char", MyFieldChar);

Pozor, že si nejprve do našeho projektu přeneseme hlavní registr z „@web/core/registry“ a pak otevřeme
podregistru „pole“.

Služby
--------

:ref:`Služby <frontend/services>` jsou dlouhodobé kusy kódu, které poskytují
vlastností, které mohou být do aplikace importovány komponentami (s „useService“) nebo jinými
služby. Dále mohou deklarovat sadu závislostí. V tomto smyslu jsou služby
jsou v podstatě systémem DI (injekcí závislosti). Například „notifikace“
Tato služba umožňuje zobrazit oznámení nebo „rpc“ služba je
správný způsob, jak požádat odoo server.

Následující příklad registruje jednoduchou službu, která zobrazuje notifikaci.
každých pět vteřin:

... kódový blok: JavaScript

import { registry } z „./jádro/registry“;

const služby = registru.kategorie („služby“);

const myService = {
závislosti: ["notifikace"]
start(env, { notification }) {
let counter = 1;
setInterval(function () {
notifikace.add(`Tik tik ${counter++}“);
            }, 5000);
        }
    };

serviceRegistry.add("myService", myService);

Součásti a háky
--------------------

Komponenty a háky jsou myšlenky, které pocházejí z
„Systém komponent pro sovy <https://github.com/odoo/owl/blob/master/doc/readme.md>“.
Odoo komponenty jsou prostě součástí webového klienta, který je tvořen.

„Záložky“ („Hooks“) jsou
cestu k faktorizaci kódu, i když závisí na životním cyklu. To je
kompozitním/funkčním způsobem vložení funkce do komponenty.
Jako takový mixin.

... kódový blok: JavaScript

funkce použít aktuální čas ()
const [state, setState] = useState({now: new Date()});
const update = () => state.nyní = nový datum;
let timer;
onWillStart(() => timer = setInterval(update, 1000));
při odpojení aplikace zavolej funkci clearInterval(timer);
vrací stav.
    }

Kontext
=======

Důležitý koncept v jazyce JavaScript Odoo je kontext: poskytuje způsob
aby kód poskytl více kontextu pro funkci nebo RPC, aby ostatní části
systém může na tyto informace správně reagovat. Nějakým způsobem je to jako taška
informace, která se šíří všude. Je užitečná v některých situacích, např.
jako oznámení Odoo serveru, že model RPC pochází z konkrétní formulářové stránky.
nebo aktivací/deaktivací některých funkcí v komponentě.

Ve webovém klientu Odoo existují dvě různé kontexty:
*akční kontext* (tedy musíme být opatrní při používání slova „kontext“:
může znamenat něco jiného v závislosti na situaci.

.. poznámka::
Objekt „kontext“ může být užitečný v mnoha případech, ale je třeba být obezřetný.
Nebuďte k němu příliš kreativní. Mnoho problémů lze vyřešit běžnými způsoby bez
upravuje kontext.

.. _frontend/framework/user_context:

Kontext uživatele
------------

Uživatelský kontext je malý objekt obsahující různé informace související s
současným uživatelem. Je k dispozici prostřednictvím služby „uživatel“:

... kódový blok: JavaScript

klas MyComponent prodlouží třídu Component
setup() {
const user = useService("user");
console.log(user.kontext);
        }
    }

Obsahuje následující informace:


.. seznam tabulkový::
:šířky: 20 20 60
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * – „povolené_firmy“
      - `int[]`
      - seznam aktivních identifikátorů společností uživatele
    * „Lang“
      - „smyčka“
      - kód uživatelského jazyka (například „en_us“)
    * „TZ“
      - „smyčka“
      - časové pásmo uživatele (například „Evropa/Brusel“)

V praxi služba „orm“ automaticky přidává kontext uživatele ke každé z
jejich požadavků. Proto se obvykle nevyplatí dovážet ho přímo
většině případů.

.. poznámka::
První prvek pole `allowed_company_ids` je hlavní společnost uživatele.

Akční kontext
--------------

:ref:`ir.actions.act_window<reference/actions/window>“ a
:ref:`ir.actions.client<reference/actions/client>` podporují volitelný parametr „kontext“.
Toto pole je char, který reprezentuje objekt. Kdykoliv odpovídající
akce je načtena v webovém klientovi a tento kontextový prvek bude vyhodnocen jako
objekt a předána komponentě odpovídající akci.

... blok kódu::xml

<položka jméno="kontext">{hledání výchozího zákazníka: 1}</položka>

Může se používat mnoha různými způsoby. Například pohledy přidávají
akce kontextu ke každé požadavku na server. Další důležitý použití je
aktivovat nějaký filtr vyhledávání výchozím nastavením (viz příklad výše).

Občas se stane, že provádíme nové akce ručně (tedy programově, v JavaScriptu).
Je užitečné, když je možné rozšířit kontext akce. To lze provést pomocí
Argument „případného kontextu“.

... kódový blok: JavaScript

    // in setup
let actionService = použijte službu ("akce");

    // in some event handler
actionService.doAction("addon_name.něco", {
další kontext:
default_period_id: defaultPeriodId
        }
    });

V tomto případě bude načteno akce s id xml_id „addon_name.něco“.
a do jeho kontextu bude přidán parametr default_period_id s hodnotou 1.
velmi důležitý případ použití, který umožňuje vývojářům spojovat akce dohromady poskytováním
informace o další akci.

.._frontend/framework/pyjs:

Interpret jazyka Python
==================

Odoo framework obsahuje integrovaný malý interpret jazyka Python. Jeho účelem
Je důležité hodnotit malé výrazy v Pythonu.
Odoo má modifikátory napsané v Pythonu, ale je potřeba je vyhodnotit.
prohlížeč.

Příklad:

... kódový blok: JavaScript

import { vyhodnotit výraz } z „@web/jádro/py_js/py“;

eval("(1 + 2*{'a': 1}).get('b', 54) + v") # vrací hodnotu 142


„Py“ JavaScript kód obsahuje 5 funkcí:

..js:funkce:: tokenizovat(výraz)

:param string expr: výraz, který se má rozložit na tokeny
:vrací: Token[] a seznam tokenů

...:parse(tokeny):

:param Token[] tokeny: seznam tokenů
:vrací: strukturu abstraktního syntaktického stromu (AST) reprezentující výraz

.. funkce:parseExpr(expr)

:param str expr: řetězec reprezentující platný výraz v Pythonu
:vrací: strukturu abstraktního syntaktického stromu (AST) reprezentující výraz

..js:funkce: vyhodnotit (ast, kontext)

:param AST ast: struktura AST, která reprezentuje výraz
:param Object kontext: objekt, který poskytuje další hodnotový kontext
:vrací: jakýkoliv výsledek vyjádření vzhledem k kontextu

…: funkce: hodnotit výraz (výraz, kontext)

:param str expr: řetězec reprezentující platný výraz v Pythonu
:param Object kontext: objekt, který poskytuje další hodnotový kontext
:vrací: jakýkoliv výsledek vyjádření vzhledem k kontextu

.._frontend/framework/domains:

Domény
=======

Obecně řečeno, domény v Odoo představují sadu záznamů, které odpovídají nějakému
určité podmínky. V jazyce JavaScript jsou obvykle reprezentovány buď jako
seznam podmínek (nebo operátorů: „|“, „&“ nebo „!“ v předponovém zápisu) nebo jako řetězec
operátory. Nemusí být standardizovány (předpona & je implicitně zahrnuta, pokud
nutné). Například:

... kódový blok: JavaScript

  // list of conditions
  []
[[„a“, „=“, 3]]
[[["a", "=", 1], ["b", "=", 2], ["c", "=", 3]]]
["&","&",["a","=",1],["b","=",2],["c","=",3]]
["&","!",["a","=",1],"|",["a","=",2],["a","=",3]]

  // string expressions
"([‚some_file‘, ‚>‘, a)]"
["[('datum','>=', (dnes() - datum.timedelta(dny=30)).format('YYYY-MM-DD'))]"]
"([('date', '!='), False])"

Řetězová výrazu jsou silnější než seznamové výrazy: mohou obsahovat
Python výrazy a nehodnotící hodnoty, které závisí na nějakém kontextu hodnocení.
Manipulace s řetězci je však obtížnější.

Odoo poskytuje objekt „Doména“, protože domény jsou v klientovi prohlížeče velmi důležité.
třída:

... kódový blok: JavaScript

new Domain([["a", "=", 3]]).contains({ a: 3 }) // true

const doména = nový Domén (["&", "&", ["a", "=", 1], ["b", "=", 2], ["c", "=", 3]]);
domain.contains({a: 1, b: 2, c: 3}); // true
domain.contains({a:-1, b:2, c:3}); // false

    // next expression returns ["|", ("a", "=", 1), ("b", "<=", 3)]
Domain.or([[["a", "=", 1]], "[('b', '<=', 3)]"]).toString();

Tady je popis třídy Domain:

..js:class::Domain([descr])

:parametrem: popis domény
:typ: string | pole libovolných typů | Doména

..js:metoda::obsahuje(záznam)

:parametru objektu record: objekt záznamu
:vrací: bool

Vrací hodnotu True, pokud záznam odpovídá všem podmínkám specifikovaným doménou.

.. metoda: toString()

:vrací: řetězec

Vrací popis domény ve formě řetězce

... metoda:toList([kontext])

:param Object kontext: kontext hodnocení
:vrací: libovolný objekt

Vrací seznam popisů domén. Pozor, tato metoda vyžaduje uvedení
volitelný objekt kontextu, který bude použit k nahrazení všech volných proměnných.

... kódový blok :: JavaScript

nový Doménový objekt (výraz) ('a', '>', b)).Vypsat seznam s hodnotou b = 3;

Třída Domain poskytuje také čtyři užitečné statické metody pro kombinování domén:

... kódový blok: JavaScript

    // ["&", ("a", "=", 1), ("uid", "<=", uid)]
Domain.and(["a" => 1], "[('uid', '<=', uid)]").toString();

    // ["|", ("a", "=", 1), ("uid", "<=", uid)]
Domain.or([[["a", "=", 1]], "[('uid', '<=', uid)]"].toString());

    // ["!", ("a", "=", 1)]
Domain.not(["a", "=", 1]).toString();

    // ["&", ("a", "=", 1), ("uid", "<=", uid)]
Domain.combine(["[" + ["a", "=", 1]] + "," + "[('uid', '<=', uid)]"], "AND").toString();


...staticmethod::Domain.a(domény)

:parametrem je seznam reprezentací domén
:druhy domén: řetězec[] | pole pole[] | pole Domény[]
:vrací: Doména

Vrací doménu, která reprezentuje vzájemné prolínání všech domén.

...staticmethod::Domain nebo (domény)

:parametrem je seznam reprezentací domén
:druhy domén: řetězec[] | pole pole[] | pole Domény[]
:vrací: Doména

Vrací doménu, která reprezentuje všechny domény.

...staticmethod::Domain.ne(doména)

:parametrem je reprezentace domény
:typ doména: řetězec | pole libovolných hodnot | Doména
:vrací: Doména

Vrací doménu, která reprezentuje negaci domény zadané jako argument

...staticmetoda::Domain.combine(domény, operátor)

:parametrem je seznam reprezentací domén
:druhy domén: řetězec[] | pole pole[] | pole Domény[]
:param operátor: operátor
:typ operátoru: „A“ nebo „NEBO“

:vrací: Doména

Vrací doménu, která reprezentuje buď křížení nebo spojení všech.
doménách v závislosti na hodnotě argumentu operátoru.

..._frontend/framework/bus:

Autobus
===

Webový klient obsahuje objekt :ref:`prostředí <frontend/framework/environment>`, který obsahuje událost
autobus s názvem „bus“. Jeho účelem je umožnit různým částem systému správně
synchronizovat se bez propojení. „Env.bus“ je sova
„EventBus <https://github.com/odoo/owl/blob/master/doc/reference/event_bus.md>“
který by měl sloužit k oznamování globálních událostí.


... kódový blok: JavaScript

   // for example, in some service code:
env.bus.on("WEB_CLIENT_READY",null, doSomething);

Tady je seznam událostí, které mohou být spuštěny na tomto autobusu:

.. seznam tabulkový::
:hlavičky: 1

   * - Zpráva
     - Náklad
     - Spoušť
   * „ACTION_MANAGER:UI-UPDATED“
     - režim, který ukazuje, která část uživatelského rozhraní byla aktualizována („aktuální“, „nový“ nebo „celá obrazovka“).
     - vykonání požadované akce je předáno do správy
   * „- ACTION_MANAGER:UPDATE“
     - další informace o vykreslování
     - akční manažer dokončil výpočet dalšího rozhraní
   * „MENU: ZMĚNA APLIKACE“
     - žádný
     - Aplikace aktuálního menu služby se změnila
   * „-ROUTE_CHANGE“
     - žádný
     - URL hash byl změněn
   * „RPC:POŽADAVKY“
     - rpc id
     - právě začal požadavek RPC.
   * „RPC: ODPOVĚĎ“
     - rpc id
     - je dokončena požadavek RPC
   * „WEB_CLIENT_READY“
     - žádný
     - webový klient byl spuštěn
   * „FOCUS-VIEW“
     - žádný
     - Hlavní pohled by se měl soustředit
   * „VYČISTIT KACHNY“
     - žádný
     - Všechny interní cache by měly být vymazány.
   * „PŘÍPRAVENÉ ZMĚNY“
     - seznam funkcí
     - Všechny pohledy s nezavřenými změnami by měly zavřít a poslat zpět volání v seznamu.


Objekt prohlížeče
==============

JavaScriptový rámec také poskytuje speciální objekt „prohlížeč“, který
poskytuje přístup k mnoha prohlížečovým API, jako je „location“, „localStorage“
nebo „setTimeout“. Například takhle by se dalo použít funkce
Funkce „browser.setTimeout“:

... kódový blok: JavaScript

import { browser } z "@web/jádro/prohlížeč/browser";

    // somewhere in code
browser.setTimeout(nějakáFunkce, 1000);

Je především zajímavá pro testování: všechny kódy, které používají objekt prohlížeče
je možné snadno otestovat, když se v rámci doby trvání
test.

Obsahuje tyto prvky:

.. seznam tabulkový::

  * – „addEventListeners“
    - cancelAnimationFrame
    - clearInterval
  * – clearTimeout
    - konzole
    - „Datum“
  * „vyhledat“
    - „historie“
    - „lokalní úložiště“
  * „Lokalita“
    - „navigátor“
    - „otevřený“
  * „náhodný“
    - „přidat posluchače“
    - „requestAnimationFrame“
  * – „sessionStorage“
    - setInterval
    - setTimeout
  * – „XMLHttpRequest“
    -
    -

.. _frontend/framework/debug_mode:

Režim ladění
==========

Odoo může někdy fungovat v speciálním režimu, který se nazývá „debug“ režim.
Pro dvě hlavní účely:

- zobrazovat další informace/pole pro některé konkrétní obrazovky.
- poskytnout nějaké další nástroje, které by pomohly vývojářům ladit rozhraní Odoo.

Režim ladění je popsán řetězcem. Prázdný řetězec znamená, že je zapnutý režim ladění.
režim není aktivní. Jinak je aktivní. Pokud řetězec obsahuje slovo „aktiva“ nebo
„testy“, pak jsou aktivovány příslušné konkrétní podmódy (viz níže).
módy mohou být aktivní zároveň, například s řetězcem „aktiva, testy“.

Aktuální hodnota režimu ladění lze přečíst v části :ref:`konfigurace<frontend/framework/configuration>`:
„env.debug“.

..tip:

Pro zobrazení menu, pole nebo vzhledových prvků pouze v režimu ladění je potřeba cílit
skupina base.group_no_one:

... kódový blok :: XML

<field name="jmeno" groups="skupina_bez_nikoho"/>

.. viz též:
   - :ref:`Zapněte ladicí režim <developer-mode>“


... _frontend/framework/assets_debug_mode:

Režim aktiva
-----------

Podrežim „debug=assets“ je užitečný pro ladění javascriptového kódu: po jeho aktivování
balíčky :ref:`aktiv<reference/assets>` již nejsou minifikovány a zdrojové mapy
jsou také vytvářeny, což je užitečné při ladění všech druhů JavaScriptového kódu.

... _frontend/framework/tests_debug_mode:

Testovací režim
----------

Další podmod je „testy“: pokud je zapnutý, server vstřikuje
složku web.assets_tests do stránky. Tato složka obsahuje převážně testovací trasy
(turné, jejichž cílem je otestovat funkci, nikoli ukázat něco zajímavého)
uživatelé). Mód „testy“ je pak užitečný pro spuštění těchto tras.

.. viz též:
    - „Repozitář sovy <https://github.com/odoo/owl>“
