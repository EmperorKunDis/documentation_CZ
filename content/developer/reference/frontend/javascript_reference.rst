.. výrazně::javascript

.. výchozí doména: js

====================
Příručka k JavaScriptu
====================

Tento dokument představuje javascriptový rámec Odoo.
Rámec není velkým programem z hlediska počtu řádků kódu, ale je poměrně
univerzální, protože je v podstatě stroj na převod deklarativního rozhraní
popis do živého aplikace schopného interagovat s každým modelem.
záznamy v databázi. Je možné dokonce používat webový klient k úpravám
webového klienta.

Přehled
========

JavaScriptový rámec je navržen tak, aby pracoval s třemi hlavními případy použití:

- Webový klient: Jedná se o soukromou webovou aplikaci, kde lze zobrazit a
přidávat nebo upravovat obchodní data. Jedná se o jednoduchou aplikaci, která je
znovu načtena, ale nová data se získávají ze serveru pouze tehdy, když je potřebujeme.
- Webová stránka: tento je veřejná část Odoo. Umožňuje neověřeným uživatelům
uživatel procházet nějaký obsah, nakupovat nebo provádět mnoho akcí jako klient.
Web je klasický, obsahuje různé trasy s kontrolory a nějaké
JavaScript, aby fungoval.
- *prodejní místo*: toto je rozhraní pro prodejní místo. Je
specializované jednostránkové aplikace.

Některý JavaScriptový kód je společný pro tyto tři případy použití a je spojen dohromady.
(viz níže v části aktiva). Tento dokument se bude soustředit především na architekturu
webového klienta.

Webový klient
==========

Aplikace na jednu stránku
-----------------------

Webový klient je jednoduchá aplikace, která se neustále aktualizuje: místo
požadovat celou stránku od serveru při každém uživatelském kroku.
Nahrává pouze to, co je potřeba k aktualizaci uživatelského rozhraní (UI).
akce. Při tomto také stará o aktualizaci informací v URL adrese.
Většinou stačí obnovit stránku nebo zavřít prohlížeč a otevřít jej
Vám znovu ukáže stejnou věc.

Přehled kódu webového klienta v jazyce JavaScript
------------------------------

Zde je velmi rychlý přehled klientského webového kódu v modulu :file:`web`.
Stezky budou popsány vzhledem k: `web/static/src`.
Následující popis je záměrně neúplný, cílem je pouze
Dává čtenářům nadhled nad architekturou.

- :file:`module_loader.js`: tento soubor definuje modul Odoo v jazyce JavaScript
systému. Musí být načten před jakýmkoliv jiným modulovým souborem JavaScriptu.
- Souborová složka „core“: tato složka obsahuje kód, který tvoří nejnižší úroveň javascriptu.
rámec a lze ho použít v webovém klientovi stejně jako na webových stránkách, portálu.
a aplikace prodeje na místě.
- :složka `weblient/`: tato složka obsahuje soubory specifické pro webový klient a
Tento materiál nelze použít na webových stránkách nebo v prodejních bodech, jako je manažer akcí a
služba akce.
- :soubor: `webclient/webclient.js`: tento soubor je komponenta webového klienta.
obal pro akční kontejner a navigační lištu a dělá několik věcí.
Jedná se o požadavky na začátek aplikace, například načtení stavu URL.
- :složka webového klienta: tato složka obsahuje kód, který je zodpovědný za zobrazování
a přepínání mezi akcemi.
- :složka views/: tato složka obsahuje kód pro infrastrukturu zobrazení.
jako většina pohledů (některé typy pohledu jsou přidány jinými doplňky).
- :file:`views/fields/`: obsahuje definici různých komponent polí,
jako některé služby používané více poli.
- :souboru`search/`, který definuje pohled na vyhledávání (není to pohled
v pohledu klienta pouze z pohledu serveru


Co dělat, když se soubor nenačte/neaktualizuje
------------------------------------------

Existuje mnoho různých důvodů, proč se soubor nemusí správně načíst.
Jaké jsou některé věci, které můžete zkusit, abyste problém vyřešili?

- Ujistěte se, že jste svůj soubor uložili; zapomenout na to se stává i těm nejlepším z nás.
- Podívejte se na konzolu (obvykle otevíranou klávesovou zkratkou F12),
pro chyby.
- Zkuste přidat do začátku souboru příkaz console.log(), abyste viděli, jestli
zda byla souborová data uložena nebo ne. Pokud nebyla, mohou být v nesprávném formátu.
balíček aktiv nebo balíček aktiv nemusí být aktuální.
- V závislosti na vašich nastaveních nemusí server znovu vytvářet balíčky aktiv.
Po úpravě souboru existuje několik možností, jak tento problém vyřešit:

  - restartování serveru ho nutí zkontrolovat, jestli je aktivační balík v pořádku.
datum, kdy bude požadováno
  - V režimu ladění je možnost v nabídce ladění (tlačítko s ikonou „fa-bug“ v navigační liště).
aby server načetl aktuální balíček aktiv bez nutnosti restartování.
  - Pokud spustíte server s možností `--dev=xml`, bude server kontrolovat
pokud je aktuální každý, když ji požádáte. Doporučujeme vám používat
tuto možnost při aktivním vývoji, ale ne v produkci.

- Ujistěte se, že po změně kódu obnovíte stránku. V současné době Odoo ne
mít žádný mechanismus pro přetaktování modulů.


Nahrávání javascriptového kódu
=======================

Velké aplikace jsou obvykle rozděleny na menší soubory, které je třeba stáhnout.
spojené dohromady. Některý soubor může vyžadovat použití kódu definovaného v
další soubor. Existují dvě možnosti sdílení kódu mezi soubory:

- používání globálního rozsahu (*okno*) k čtení/zápisu odkazů na nějaké
objekty nebo funkce

- pomocí modulového systému, který poskytne způsob, jakým mohou jednotlivé moduly exportovat nebo importovat
hodnoty a zajistí jejich správné načtení v požadovaném pořadí.

Pracovat v globálním rozsahu je možné, ale má to řadu problémů:

- Je těžké zajistit, aby se detaily implementace nezobrazily: funkce
deklarace v globálním rozsahu jsou přístupné pro všechny ostatní kódy.

- Existuje jediný prostor jmen, což vytváří velký potenciál pro konflikty při pojmenovávání.

- Závislosti jsou implicitní: pokud kus kódu závisí na jiném, je v pořadí
Takže je důležité, jaké jsou na nich náklady, ale těžké je zaručit.

Modulový systém pomáhá vyřešit tyto problémy: protože moduly specifikují své
závislosti, modulový systém je schopen je načíst v požadovaném pořadí nebo vygenerovat chybu.
jestliže chybí závislosti nebo jsou cyklické. Moduly také vytvářejí svůj vlastní prostor jmen.
a může si vybrat, co exportovat, čímž se zabrání odhalení podrobností implementace a
jmenovací kolize.

Přestože můžeme používat moduly ES přímo, existuje několik
nevýhody této metody: každé modulové rozhraní vyžaduje síťový oblouk, který
stává se velmi pomalým, když máte stovky souborů a mnoho souborů v Odoo potřebuje
jsou přítomny, i když nebyly do systému vloženy z nějakého důvodu, protože prostě přidávají kód
a ne naopak, jak se původně předpokládalo.

Proto má Odoo systém balíčků aktiv. V těchto balíčcích je JavaScript
soubory jsou ES moduly s speciální poznámkou na začátku. Tyto moduly budou
Sbalit a přeložit tak, aby byly použitelné naším modulovým naložitelem. I když můžete
píšete kód, který tento modulový systém nepoužívá, obecně se nedoporučuje.

(viz:ref:`frontend/modules/native_js`)


Opravné třídy
----------------

Přestože se snažíme poskytovat rozšíření bodů, které nevyžadují, je
někdy je nutné upravit chování stávající třídy přímo na místě.
cílem je mít mechanismus, který umožní změnit třídu a všechny budoucí/přítomné instanci.
Toho je dosaženo pomocí funkce utilitního nástroje „patch“:

... kódový blok: JavaScript

import {Hamster} z "@web/jádro/hamster"
import { patch } z "@web/core/utils/patch";

patch(Hamster.prototype, {
spustit(sleep) {
super.spát(...argumenty);
console.log("zzz");
        },
    });

Při opravách metod je potřeba opravit prototyp třídy, ale pokud byste
chcete-li opravit statickou vlastnost třídy, musíte ji samotnou opravit.

Opravy jsou nebezpečné a měly by se provádět s opatrností, protože
změnit všechny instanci třídy, i když byly již vytvořeny.
vyhněte se podivným problémům, opravy by měly být aplikovány co nejdříve.
nejvyšší úrovně vašeho modulu. Přidávání tříd na běhu může vést k extrémně
je obtížné odhalit problémy, pokud třída již byla inicializována.

Registry
==========

Obecná potřeba v ekosystému Odoo je rozšířit nebo změnit chování
základní systém zvenčí (instalací aplikace, tedy jiného
modul). Například může být potřeba přidat nový widget pole v některých pohledech.
v případě této a mnoha dalších je obvyklé postupovat tak, že se nejprve vytvoří požadovaný komponent.
Pak je přidáte do registru (registrační krok) a zbytek webového klienta
je si vědom své existence.

V systému je několik registrů. Registry, které se používají
do rámce jsou kategorie hlavního registru, které lze importovat z
:js:data:`@web/core/registry`

evidenční pole
V poli registru pole je uvedeno všechno pole známé webovému klientovi.
Kdykoli je potřeba pole widgetu v nějakém pohledu (obvykle formulář nebo seznam/kanban),
Takže se na něj podívá. Typickým příkladem je tento scénář:

...... kódový blok:: javascript

import { registry } z "@web/core/registry";
třída PadField je dědičná od třídy Component.

registry.kategorie("pole").přidat("pad", {
komponenta: PadField
podporované typy: ["char"]
        // ...
      });

zobrazit rejstřík
Tento registr obsahuje všechny známé pohledy na stránky z webového klienta.

registr smluv
Veškeré kroky klienta sledujeme v tomto registru.
Je to místo, kam se podívá správce akcí, když potřebuje vytvořit klienta.
akce klienta může být funkcí – funkci se volá, když je klient aktivní
akce je vyvolána a návratová hodnota bude prováděna jako další akce.
pokud je třeba – nebo komponentu sovy, která se zobrazí při provádění této akce.

Služby
========

V rámci webového klienta existují některé obavy, které nelze vyřešit jedinou
součástí, protože se týká více součástí nebo je potřeba
držet stav aplikace po dobu, kdy je aplikace aktivní.

Služby jsou řešením těchto problémů: vznikají při aplikaci
startup, jsou k dispozici komponentám prostřednictvím háčku „useService“ a zůstávají
živý po celou dobu trvání aplikace.

Příkladem je služba *orm*, jejímž úkolem je umožnit interakci s
objekty na serveru.

Níže je uveden jednoduchý příklad implementace služby orm:

... kódový blok: JavaScript

import { registry } z "@web/jádro/registry";
exportní konstanta OrmService je následující:
start() {
return {
číst(...){...},
write(..., ...) { ... }
unlink(..., ...) { ... }
                ...
            }
        },
    };
registry.kategorii("služby").přidat("orm", OrmService);

Používání služeb
--------------

Služby jsou k dispozici v prostředí, ale obecně by se měly používat přes
Hoook „useService“, který zabraňuje volání metod služby po
komponenta byla zničena a zabraňuje dalšímu kódu v provádění po
metoda volání, pokud byl komponent zničen během volání.

... kódový blok: JavaScript

class SomeComponent extends Component {
setup() {
tento.orm = použít službu ("orm");
        }
        // ...
získat modelovou ID aktivity (model)
vrací tento objekt ORM voláním metody modelu „get_activity_view_id“ s parametry z tohoto objektu.
        }
    }

Hovořil s serverem
---------------------

Při práci s Odoo existují dvě základní použití: v jednom případě je nutné volat
metoda na (pythonském) modelu (to jde přes kontroler /web/dataset/call_kw),
nebo je nutné přímo zavolat do řídicího centra (k dispozici na některých trasách).

* Volání metody v pythonovém modelu se provádí prostřednictvím služby orm:

...... kódový blok:: javascript

return tento.orm.volat(„nějaký model“, „nějaká metoda“, [něco, nějaké argumenty]);

* Přímo volání kontroleru se provádí přes službu RPC:

...... kódový blok:: javascript

return tento.rpc("/nějaká/cesta/", {
některé: param
      });

.. poznámka::
RPC služba ve skutečnosti nevykonává, co je obecně chápáno jako
vzdálené volání procedury (RPC), ale z důvodu historického vývoje
Všechny požadavky na síťové služby v jazyce JavaScript se obecně označují jako RPC.
z předchozího odstavce vyzdvihnuté, chcete-li volat metodu na
Pokud chcete použít model, měli byste použít službu orm.

Oznámení
=============

Odoo má standardní způsob komunikace různých informací.
uživatel: oznámení, která se zobrazují v pravém horním rohu uživatelského rozhraní.
Typy oznámení se řídí bootstrapy toastů:

- *informace*: užitečné pro zobrazení nějaké zpětné vazby jako důsledek
akce, která nemůže selhat.

- *úspěch*: uživatel provedl akci, která někdy může selhat, ale tentokrát ne.

- *varování*: uživatel provedl akci, která mohla být pouze částečně dokončena.
Užitečné i v případě, že něco nefunguje správně, ale není to způsobeno uživatelem.
Je to spíš taková teorie.

- Úspěch: uživatel se pokusil o akci, ale nebyla dokončena.


Notifikace mohou být také použity k tomu, aby se uživateli položila otázka bez rušení.
jejich práci: například telefonní hovor přijatý prostřednictvím VoIP: označitelné upozornění
Mohly by být zobrazeny dvěma tlačítky pro „Přijmout“ nebo „Odmítnout“.

Zobrazování oznámení
------------------------

Existují dvě možnosti, jak zobrazit notifikace v Odoo:

- Služba „oznámení“ umožňuje komponentám zobrazovat oznámení z JavaScriptu.
kód voláním metody add.

- Klientská akce *zobrazit_upozornění* umožňuje spustit zobrazení
o oznámení z Pythonu (např. v metodě, která se volá při uživatelském
kliknutím na tlačítko typu objekt (toto klientské akce využívá oznámení
služby.

Nastavení upozornění má několik možností:

- Název: řetězec (volitelný). Tento text se zobrazí na horní části jako nadpis.

- *zpráva*: řetězec, volitelný. Obsah oznámení. Může být značkovaný
objekt pro zobrazení formátovaného textu.

- *lepivý*: boolean, volitelné (výchozí hodnota je false). Pokud je pravda,
zůstane na obrazovce až do chvíle, kdy ho uživatel odmítne. Jinak bude
se automaticky uzavřít po krátké pauze.

- Typ: řetězec, volitelný (výchozí hodnota „upozornění“). Určuje styl
oznámení. Možné hodnoty: „informace“, „úspěch“, „varování“ a „nebezpečí“.

- *classname*: řetězec (volitelný). To je název třídy CSS, který bude
je automaticky přidán do oznámení. To může být užitečné pro stylizaci
Přestože je jeho používání znepokojivé.

Níže jsou uvedeny příklady, jak zobrazit notifikace v Javě:

... kódový blok: JavaScript

    // note that we call _t on the text to make sure it is properly translated.
tento.notifikace.přidat(
název:_t("Úspěch"),
zpráva: _t("Vaše žádost o podpis byla odeslána.")
    });
tento.notifikace.přidat(
titulek: _t("Chyba"),
zpráva: _t("Jméno filtru je povinné."),
typ: „nebezpečí“,
    });

A v Pythonu:

... kódový blok:: python

    # poznámka, že voláme funkci _() na textu, abychom se ujistili, že je správně přeložený.
def show_notification(self):
return {
„typ“: „ir.actions.client“,
„tag“: „zobrazit upozornění“,
"params": {
„nazev“: _("Úspěch"),
'message': _('Vaše žádost o podpis byla odeslána.'),
„lepkavý“: False
            }
        }

Systray
=======

Systray je vpravo část nabídky v rozhraní, kde je webová stránka.
Klient zobrazuje několik widgetů, například nabídku pro zasílání zpráv.

Když systémový tray vytvoří navigační lišta, bude hledat všechny registrované
systray položky a zobrazit je.

Pro současné systémové položky tray není k dispozici žádný specifický API. Jsou to komponenty Owl.
a komunikují se svým okolím stejně jako ostatní součásti, například
interakci s službami.

Přidání nového systémového položky na liště
-------------------------

Položky můžete přidat do systémové lišty pomocí registru „systray“:

... kódový blok: JavaScript

import { registry } z "@web/jádro/registry"
class MySystrayComponent extends Component {
        ...
    }
registry.kategorie("systray").přidat(„MySystrayComponent“, „MySystrayComponent“, { pořadí: 1 });

Položky v systémovém tácku jsou seřazeny podle pořadí v systémovém tácku.
registr.

Správa překladů
======================

Některé překlady se provádí na straně serveru (ve skutečnosti všechny textové řetězce, které jsou zobrazeny nebo
serverem zpracovávána, ale v souborech statických je potřeba
přeložit. Aktuálně to funguje takto:

- Každý přeložitelný řetězec je označen speciální funkcí *_t_*
- Tyto řetězce používá server k vytvoření správných souborů PO.
- Každý požadavek na webového klienta bude volat cestu */web/webclient/translations*.
který vrací seznam všech přeložitelných termínů.
- Při spuštění programu se při každém volání funkce _t bude hledat v tomto seznamu
aby našel překlad, a pokud žádný nenalezne, vrací originální řetězec.
Je-li nalezena.

Pozor, překlady jsou vysvětleny podrobněji, ze strany serveru
v dokumentu /developer/howtos/translations.

... kódový blok: JavaScript

import {_t} z "@web/jádro/lokalizace/přeložení";

class SomeComponent extends Component {
statická proměnná exampleString je nastavena na hodnotu _t("tohle by se mělo přeložit");
        ...
someMethod() {
const str = _t("nějaký text");
        }
    }

Pozor, při použití funkce překladu je nutné dbát na to, že se jako parametr
Argument nelze dynamicky vytvářet, protože je extrahován staticky z kódu.
generuje soubory PO a slouží jako identifikátor pro překlad pojmů. Pokud
Do řetězce je potřeba vložit nějaký dynamický obsah, podporuje to zástupné proměnné:

... kódový blok: JavaScript

import {_t} z "@web/jádro/lokalizace/přeložení";
const str = _t("Ahoj %s, máš %s nepřečtených zpráv.", uživatelské jméno, počet nečtených zpráv);

Pozor, jak je sama stuha pevně připevněná. To umožňuje funkci překladu
získat přeložený řetězec před jeho použitím pro interpolaci.


Sesnídání
=======

Webový klient potřebuje nějaké informace od Pythonu, aby mohl správně fungovat.
vyhnout se dalšímu zpátečnímu výjezdu do serveru tím, že v JavaScriptu provedete síťovou požadavek.
Tato informace je přímo vložena do stránky a lze ji přistupovat pomocí JS
přes modul @web/session.

Přidání informací do sezení
---------------------------------

Když je načtena cesta /web, server tuto informaci vloží do skriptu
tag. Informace se získá voláním metody session_info.
model „ir.http“. Můžete tento metod přehrát, aby se do informací o
návrat do slovníku.

... kódový blok:: python

od odoo importujeme modely
od odoo.http import požadavek

třída IrHttp(model.AbstractModel):
dědí z ir.http

def session_info(self):
výsledek = super(IrHttp, self).session_info()
result['nějaký klíč'] = získat nějakou hodnotu z databáze
vrátí výsledek

Nyní lze hodnotu získat v JavaScriptu přečtením ji z relace:

... kódový blok: JavaScript

import { session } z "@web/session"
const myValue = session['some_key'];
    ...

Pozor, tento mechanismus je navržen tak, aby snížil množství komunikace.
potřebné pro klienta webu, aby bylo připravené. Je vhodné pouze pro data, která jsou
je levné vypočítat (pomalý výzva k session_info zpozdí načítání pro web).
klient pro každého) a pro data, která jsou potřebná na začátku inicializace
proces.

Názory
=====

Slovo „výhled“ má více významů, tato část je o architektuře
javascriptový kód pohledů, nikoliv struktura archu nebo cokoli jiného.
jinak.

Zatímco pohledy jsou jen součástí sovy, většina vestavěných pohledů má stejné
struktura: komponenta s názvem „SomethingController“, která je kořenovou složkou prohlížeče.
Tento komponent vytváří instanci nějakého „modelu“ (objekt, který je odpovědný za
správu dat) a má podkomponentu nazvanou „renderer“, která se stará o
logika zobrazení.

.. odkaz na widgety:

Pole
======

Dobrá část uživatelského zážitku z webového klienta je o úpravách a vytváření dat.
Taková práce se dělá s pomocí pole widgetů, které jsou si vědomy políčka
a konkrétních podrobností o tom, jak by měla být hodnota zobrazována a upravována.

.. odkaz/odkaz na javascript/výplň pole:

Dekorace
-----------

Stejně jako v seznamovém pohledu mají pole widgety jednoduchou podporu pro dekorace.
Účelem dekorací je mít jednoduchý způsob, jak určit barvu textu podle
nejaktuálnější stav záznamu. Například:

... blok kódu::xml

<field name="stát" dekorace-nebezpečí="množství &lt; 10000"/></field>

Platné označení dekorace je:

- „dekorace-bf“
- „dekorace“
- „dekorace - nebezpečí“
- „dekorace-info“
- „dekorace utlumená“
- „dekorace-primární“
- úspěšné dekorace
- „varování o dekoracích“

Každá dekorace *dekorace-X* bude přiřazena k třídě CSS *text-X*, která je
standardní třída CSS pro bootstrapping (s výjimkou *text-it* a *text-bf*, které jsou
Odoo a odpovídají kurzívě a tučnému písmu. Pozor na
Hodnota atributu dekorace by měla být platným výrazem v Pythonu.
bude hodnocena v kontextu rekordu.

Nenávazné pole
---------------------

Zde dokumentujeme všechny ne-relativní pole dostupná výchozí hodnotou, v žádném konkrétním pořadí.
pořádku.

Číslo celé („celé číslo“)
Toto je výchozí typ pole pro pole typu integer.

    - Podporované typy polí: integer

Možnosti:

    - `type`: nastavení typu vstupu („text“ výchozí hodnota, lze nastavit na „číslo“)

V režimu úprav je pole zobrazeno jako vstup s atributem typu
nastavení na „číslo“ (takže uživatel může využít nativní podporu zejména v
mobilním zařízením). V tomto případě je výchozí formátování vypnuto kvůli možné neslučitelnosti.

... kódový blok::xml

<políčko jméno="int_value" možnosti={'typ':'číslo'}/>

    - „krok“: nastavte krok na hodnotu nahoru a dolů při stisknutí tlačítka
(pouze pro vstup typu číslo, výchozí hodnota je 1)

... kódový blok::xml

<políčko jméno="int_value" možnosti={"typ": "číslo", "krok": 100}/>

    - „formát“: zda se číslo má formátovat. („pravda“ je výchozí hodnotou).

Výchozí formátování čísel je podle parametrů lokálního nastavení.
Tato volba zabrání tomu, aby hodnota pole byla formátována.

... kódový blok::xml

<políčko jméno="int_value" možnosti='{"formát":false}'/>

Plovoucí („float“)
Toto je výchozí typ pole pro pole typu float.

    - Podporované typy polí: float

Atributy:

    - „číslice“: zobrazovaná přesnost

... kódový blok::xml

<pole název="faktor" čísla="[42,5]"/>

Možnosti:

    - `type`: nastavení typu vstupu („text“ výchozí hodnota, lze nastavit na „číslo“)

V režimu úprav je pole zobrazeno jako vstup s atributem typu
nastavení na „číslo“ (takže uživatel může využít nativní podporu zejména v
mobilním zařízením). V tomto případě je výchozí formátování vypnuto kvůli možné neslučitelnosti.

... kódový blok::xml

<políčko jméno="int_value" možnosti={'typ':'číslo'}/>

    - „krok“: nastavte krok na hodnotu nahoru a dolů při stisknutí tlačítka
(pouze pro vstup typu číslo, výchozí hodnota je 1)

... kódový blok::xml

<položka jméno="int_value" možnosti={"typ": "číslo", "krok": 0,1}/>

    - „formát“: zda se číslo má formátovat. („pravda“ je výchozí hodnotou).

Výchozí formátování čísel je podle parametrů lokálního nastavení.
Tato volba zabrání tomu, aby hodnota pole byla formátována.

... kódový blok::xml

<políčko jméno="int_value" možnosti={'formát': False}/>

Čas (float_time)
Cílem tohoto widgetu je zobrazit správně hodnotu plovoucí desetinné čárky, která reprezentuje
časový úsek (v hodinách). Takže například hodnota „0,5“ by měla být formátována jako „0:30“.
nebo „4,75“ odpovídá času „4:45“.

    - Podporované typy polí: float

Plovoucí faktor („float_factor“)
Tento widget má za cíl zobrazit správně hodnotu s plovoucí desetinnou čárkou, která byla převedena pomocí faktoru
například hodnota uložená v databázi je 0,5.
faktor je 3, hodnota widgetu by měla být formátována na 1,5.

    - Podporované typy polí: float

Plovoucí přepínač („float_toggle“)
Cílem této lišty je nahradit pole vstupu tlačítkem obsahujícím kód.
rozsah možných hodnot (v nastavení). Každý klik umožňuje uživateli procházet
v rozsahu. Účelem je omezit hodnotu pole na předdefinovaný výběr.
Dále podporují faktorovou konverzi jako widget float_factor (Interval hodnot)
mělo být výsledkem převodu.

    - Podporované typy polí: float

... kódový blok :: XML



Logická („logická“)
Toto je výchozí typ pole pro pole typu boolean.

    - Podporované typy polí: boolean

Char (char)
Tento je výchozí typ pole pro pole typu char.

    - Podporované typy polí: char

.. odkaz/odkaz na javascript/odkaz na datumové pole:

Datum (date)
Tento je výchozí typ pole pro pole typu „datum“. Jeho obsahem je text.
krabice a datový výběr.

    - Podporované typy polí: date

Možnosti:

    - `min_date` / `max_date`: nastavuje limity pro přijatelné hodnoty. Výchozí hodnota je
přijaté datum je **1000-01-01** a nejpozdější je **9999-12-31**.
Povolené hodnoty jsou datum ve formátu SQL („yyyy-MM-dd HH:mm:ss“) nebo „dnes“.

... kódový blok::xml

<políčko název="datum" možnosti={'min_date': 'dnes', 'max_date': '2023-12-31'} />

    - warn_future: zobrazí varování, pokud hodnota je v budoucnosti (vzhledem k dnešnímu datu).

... kódový blok::xml

<políčko typu "datum" s nastavením "{ 'varování_budoucí': true }">

.. odkaz/odkaz na javascript/odkaz na datumové pole:

Datum a čas (datum a čas)
Toto je výchozí typ pole pro pole typu Datum a čas. Hodnoty jsou vždy
v časovém pásmu klienta.

    - Podporované typy polí: datetime

Možnosti:

    - viz: „Datumové pole“ (viz reference v části JavaScript)

    - „Rozšíření“: přidávané hodnoty, které generují dostupné minuty v časovém vyhledávači.
Tato hodnota se nemění, pouze počet dostupných možností.
výběr ze seznamu (výchozí hodnota: 5).

... kódový blok::xml

<vlastnost jméno="datumové pole" volby={"zpracování": 10}/>

    - `show_seconds`: pokud je nastaveno na „false“, skryje sekundy z pole datum a čas.
pole stále přijímá datum a časové hodnoty, ale sekundy jsou skryty.
UI (výchozí hodnota: `true`).

... kódový blok::xml

<políčko typu "datum a čas" widget="datetime" možnosti = "{ 'zobrazit sekundy': false }"/>

    - `show_time`: pokud je nastaveno na „false“, skryje se část datumu a času.
pole stále přijímá datum a časové hodnoty, ale část času bude skryta.
UI (výchozí hodnota: `true`).

... kódový blok::xml

<položka jméno="datumové pole" widget="datum" možnosti={"zobrazit čas":false}/>

Datový rozsah (daterange)
Tento widget umožňuje uživateli vybrat datum začátku a konce z jednoho výběru.

    - Podporované typy polí: „datum“, „datum a čas“

Možnosti:

    - viz položku „Datum“ v sekci „Reference“ nebo „Datum a čas“ v sekci „Referenční dokumenty“.

    - `start_date_field`: pole používané k získání a nastavení hodnoty začátku datového rozsahu
(není možné používat s proměnnou end_date_field).

... kódový blok::xml

<položka jméno="end_date" widget="daterange" možnosti={'start_date_field': 'start_date'}/>

    - `end_date_field`: pole pro získání/nastavení koncového data rozsahu
(nelze použít s proměnnou start_date_field).

... kódový blok::xml



Dny zbývající k uplatnění („remaining_days“)
Toto widget lze použít na pole s datem a časem. V režimu read-only zobrazuje
dílčí rozdíl mezi hodnotou pole a dneškem. Widget se vždy aktualizuje
do běžného pole pro datum nebo čas v režimu úprav.

    - Podporované typy polí: „datum“, „datum a čas“

Monetární
Toto je výchozí typ pole pro pole typu monetární. Používá se k
zobrazit měnu. Pokud je v nastavení zadána pole s měnou, bude se zobrazovat.
použít tuto, jinak se vrátí k výchozí měně (v dané relaci).

    - Podporované typy polí: monetární, float

Možnosti:

    - `currency_field`: další pole, které by mělo být mnoho2jedno na měnu.

... kódový blok::xml

<položka jméno="hodnota" widget="měnová jednotka" možnosti={" měnový políčko": " měna_id"} />

Text (text)
Toto je výchozí typ pole pro pole typu text.

    - Podporované typy polí: text


Přidržet („hold“)
Tato pole slouží k zobrazení jako „záložka“ a umožňuje přeskládání.
různé záznamy tahem myši.

..... upozornění: Musí být uvedeno v poli, podle kterého jsou záznamy seřazeny.
.... varování: Mít více polí s ovládacím prvkem „handle“ na stejném seznamu není podporováno.

    - Podporované typy polí: integer


E-mail (e-mail)
Toto pole slouží k zadání e-mailové adresy. Hlavním důvodem pro použití je, že
je zobrazen jako odkaz s vhodným atributem href a ve čteném režimu.

    - Podporované typy polí: char

Telefon
Toto pole zobrazuje telefonní číslo. Hlavním důvodem k jeho použití je, že
je zobrazen jako odkaz s vhodným href, ve čteném režimu.
jen v některých případech: chceme, aby se odkaz stal aktivním pouze tehdy, pokud zařízení může
zavolat na tento konkrétní telefonní číslo.

    - Podporované typy polí: char

URL (url)
Toto pole zobrazuje URL adresu (v režimu čtení). Hlavním důvodem pro jeho použití je
že je zobrazen jako odkaz s příslušnými třídami CSS a href.

Dále lze upravit texty vnořených odkazů pomocí atributu *text*.
(nezmění se hodnota href).

    - Podporované typy polí: char

... kódový blok :: XML

<políčko jméno="foo" widget="url" text="Nějaká URL adresa" />

Možnosti:

    - „webová cesta“: (výchozí hodnota je „false“) – pokud není již nastaveno
(v případě, že je tato volba nastavena) začíná hodnotou „http://“.
to „pravda“, což umožňuje přesměrování na vlastní webové stránky databáze.

Doména (doména)
Pole „doména“ umožňuje uživateli vytvořit technickou předponu domény.
Díky stromovitému rozhraní a zobrazením vybraných záznamů v reálném čase.
V režimu ladění je také možné zadat předponový znak
přímo (nebo stavět složitější domény, které umožňuje stromová rozhraní).
neumožňují.

Zde je nutné poznamenat, že se jedná o statické domény (nejsou podporovány dynamické výrazy nebo přístup
do proměnné kontextu.

    - Podporované typy polí: char

Možnosti:

    - „Model“: název pole typu „char“, které kóduje hodnotu „res_model“, na kterou se vztahuje doména.

    - „složený“ (výchozí hodnota: „false“): pokud je tato vlastnost nastavena na „true“, pole domény se zobrazí kompaktně a rozbalí se
sama sebe na základě interakce uživatele.

    - in_dialog (výchozí hodnota: false): pokud je nastaveno na true, widget otevře dialogové okno při editaci
doménu a výchozí je zobrazena v seznamu pod hodnotou.

Tlačítko odkazu („link_button“)
Widget „LinkButton“ ve skutečnosti jen zobrazuje štítek s ikonou.
hodnota textu jako obsah. Odkaz je kliknutelný a otevře nové okno prohlížeče.
okno s hodnotou URL.

    - Podporované typy polí: char

Soubor obrázku (obrázek)
Toto widget slouží k zobrazení binární hodnoty jako obrázku. V některých případech
server vrací hodnotu bin_size místo skutečného obrázku (bin_size je hodnota
reprezentující velikost souboru (např. „6.5kb“). V takovém případě se widget
vytvoří obrázek s atributem zdroje odpovídajícím obrázku na webu.
server.

    - Podporované typy polí: „binární“

Možnosti:

    - `preview_image“: pokud je obrázek načítán pouze jako „bin_size“, pak
tato volba je užitečná k informování webového klienta, že výchozí název pole
není jméno aktuálního pole, ale jméno jiného pole.

... kódový blok::xml

<oblast název="obrázek" widget="obrázek" možnosti={"předběžný obrázek": "obrázek_128"} />

    - `povolené přípony souborů`: přípona souboru, kterou může uživatel vybrat v dialogovém okně pro výběr souboru
(výchozí hodnota je „image/*“)

(viz atribut „accept“ v tagu input typu file)

Soubor s binárním obsahem („binární“)
Univerzální widget pro ukládání/stahování binárního souboru.

    - Podporované typy polí: „binární“

Atributy:

    - „název souboru“: uložení binárního souboru ztratí jeho název, protože
ukládá binární hodnotu. Jméno souboru lze uložit do jiného pole.
že do pole v pohledu je nutné nastavit atribut „název souboru“.

... kódový blok::xml

<pole jméno="datas" soubor="datas_fname"/>

Možnosti:

    - `povolené přípony souborů`: přípona souboru, kterou může uživatel vybrat v dialogovém okně pro výběr souboru

(viz atribut „accept“ v tagu input typu file)

Priorita („priorita“)
Toto widget se zobrazuje jako sada hvězdiček, které uživatel může kliknout.
a nebo ne. Toto je užitečné například při označování úkolu jako vysoké
prioritou.

Pozor, že tento widget také funguje v režimu „jen pro čtení“, což je neobvyklé.

    - Podporované typy polí: „vybraná hodnota“

Obrázek připojený k příspěvku („příloha obrázku“)
Obrázek pro pole typu „množství k jednomu“. Pokud je pole nastaveno, tento obrázek se zobrazí.
zobrazena jako obrázek s odpovídajícím zdrojovým URL. Tento widget nemá
různé chování v režimu pro editaci nebo pouze pro zobrazení, je užitečné pouze k
obrázek.

    - Podporované typy polí: many2one

... kódový blok :: XML



Výběr štítku („label_selection“)
Toto widgeto zobrazuje jednoduchou neupravitelnou štítek. Tento je pouze užitečný pro
zobrazit nějaké informace, nikoli je upravovat.

    - Podporované typy polí: „vybraná hodnota“

Možnosti:

    - `třídy“: mapování výběru hodnoty na název CSS třídy

... kódový blok::xml

<pole
jméno="stát"
widget="label_vyber"
options={
"klasifikace": {
'návrh': 'výchozí',
'cancel': 'default'
'none': 'nebezpečí',
                    },
                }"
            />

Státní výběr („state_selection“)
Toto je speciální výběrové tlačítko, které předpokládá, že záznam má nějakou
pevně zakódované pole, které je v pohledu: „stage_id“, „legend_normal“.
„legend_blokovaná“, „legend_dokončená“. Toto se používá především k zobrazení a změně
stav úkolu v projektu s dalšími informacemi zobrazenými
rozbalovací nabídka.

    - Podporované typy polí: „vybraná hodnota“

... kódový blok :: XML

<položka jméno="kanban_state" widget="state_selection"/>

Státní výběr - Zobrazení seznamu („list.state_selection“)
V seznamovém zobrazení je výchozím nastavením pole „state_selection“ název vedle ikony.

    - Podporované typy polí: „vybraná hodnota“

Možnosti:

    - `hide_label`: skrýt název ikony vedle ní

... kódový blok::xml



Oblíbené („boolean_favorite“)
Tento widget se zobrazuje jako prázdná nebo plná hvězdička podle toho, jestli je
hodnota. Pozor, že lze také editovat v režimu pouze pro čtení.

    - Podporované typy polí: boolean

Přepínač („pravda/nepravda“)
Zobrazuje přepínač pro zobrazení booleovského výrazu.
pole typu „logická“ hodnota, které se používá především pro jiné vzhledy.

    - Podporované typy polí: boolean

Stat Info (statinfo)
Tento widget má sloužit k zobrazení statistických informací v tlačítku „Stat“.
V podstatě jen štítek s číslem.

    - Podporované typy polí: integer, float

Možnosti:

    - Pokud je zadáno pole „Štítek“, widget použije hodnotu pole „Štítek“ jako text.

... kódový blok::xml

<button
name="%(aktuální výplatní lístek - řádky)d"
ikonou "fa-money"
typ="akce"
            >
<pole
name="mzda_počet"

string="Mzda"
options={"label_field": "label_tasks"}
                />


Procentní koláč („percentpie“)
Tento widget má sloužit k zobrazení statistických informací v tlačítku „Stat“.
To je podobné jako widget statinfo, ale informace jsou zobrazeny jinak.
*diagram sloupcový* (prázdný až plný). Zde je hodnota interpretována jako
procento (číslo mezi 0 a 100).

    - Podporované typy polí: integer, float

... kódový blok :: XML



Indikátor pokroku („progressbar“)
Zobrazte hodnotu jako posuvník (od 0 do nějaké hodnoty).

    - Podporované typy polí: integer, float

Možnosti:

    - „editovatelné“: Boolean určující, zda je hodnota „editovatelná“.

    - `current_value`: získat aktuální hodnotu ze sloupce, který musí být ve výsledném pohledu

    - `max_value`: získat nejvyšší hodnotu pole, které musí být v pohledu

    - `edit_max_value`: Boolean, který určuje, zda je možné upravovat hodnotu `max_value`.

    - `název`: název barev, zobrazený na vrcholu barev

-> nevyplněno, použijte místo toho atribut title (ne možnost) pokud je pojem nutné přeložit

... kódový blok :: XML

<pole
name="nepřítomnost dnes"
widget="průběžný proužek"
options="{
'současná hodnota': 'dnes nepřítomna'
'max_value': 'celkový počet zaměstnanců',
editovatelné: false,
            }"
        />

Panel grafů („dashboard_graph“)
Toto je více specializovaný widget, který se hodí k zobrazení grafu reprezentujícího
sada dat. Například se používá v přehledu kanban účetnictví.

Předpokládá, že pole je JSON sérializací souboru dat.

    - Podporované typy polí: char

Atributy:

    - `graph_type`: řetězec, může být buď „line“ nebo „bar“.

... kódový blok::xml



Editor Ace („ace“)
Tento widget je určený pro pole Text a poskytuje editor Ace.
pro editaci XML a Pythonu.

    - Podporované typy polí: `char`, `text`

Štítek („Badge“)
Zobrazuje hodnotu uvnitř bootstrapového štítku pilulky.

    - Podporované typy polí: `char`, `selection`, `many21

Výchozí barva pozadí je světle šedá, ale lze ji přizpůsobit.
pomocí mechanizmu dekorace pole podle odkazu na stránce Reference v JavaScriptu.
Například zobrazit červený štítek za určitých podmínek:

... kódový blok :: XML

<položka jméno="foo" widget="badge" dekorace-nebezpečí="stav = 'zrušit'" />

Relativní pole
-----------------

Výběr (výběr)

    - Podporované typy polí: „vybraná hodnota“

Atributy:

    - `náhradní text`: řetězec, který se zobrazuje při výběru žádné hodnoty

... kódový blok::xml

<políčko jméno="tax_id" widget="vybrané hodnoty" placeholder="Vyberte daň" />

Rádio („rádio“)
Toto je podpole pole FielSelection, ale specializované na zobrazení všech položek.
validní volby jako rámečky s tlačítky.

Pozor, pokud se používá na mnoho2jedno poli, pak se provede více rpc k vyzvednutí
jména souvisejících záznamů.

    - Podporované typy polí: „vybraná hodnota“, „mnoho k jedné“

Možnosti:

    - `horizontální“: pokud je hodnota „pravda“, budou tlačítka s možnostmi zobrazena vodorovně.

... kódový blok::xml



Výběr štítku (selection_badge)
To je podpole pole „vybrané položky“, ale specializované na zobrazení všech položek.
platné volby jako čtvercové nálepky.

    - Podporované typy polí: „vybraná hodnota“, „mnoho k jedné“

... kódový blok :: XML

<položka jméno="doporučený typ aktivity" widget="tlačítko výběru">

Many2One („many2one“)
Výchozí widget pro pole mnoho k jednomu.

    - Podporované typy polí: many2one

Atributy:

    - `can_create`: umožňuje vytváření souvisejících záznamů
(přednost před možností no_create).

    - `can_write`: umožňuje upravovat související záznamy (výchozí hodnota: „true“)

Možnosti:

    - `quick_create`: umožňuje rychlé vytváření souvisejících záznamů (výchozí hodnota: true)

    - `no_create`: zabrání vytváření souvisejících záznamů - skryje oba položky **Vytvořit „xxx“**
a položky nabídky „Vytvořit a upravit“ (výchozí hodnota: false)

    - `no_quick_create`: zabrání rychlému vytváření souvisejících záznamů – skryje tlačítko „Vytvořit „xxx““.
položka rozbalovací nabídky (výchozí hodnota: false)

    - `no_create_edit`: skrytí položky „Vytvořit a upravit“ v nabídce (výchozí hodnota: false)

    - `create_name_field`: pokud je tato možnost nastavena při vytváření souvisejícího záznamu
hodnota proměnné create_name_field bude vyplněna hodnotou vstupu
(výchozí hodnota je „jméno“)

    - `always_reload“: Boolean, výchozí hodnota je „false“. Pokud je nastaveno na „true“, widget bude vždy
provést další funkci „name_get“, která získá hodnotu názvu. Tato funkce se používá pro
situace, kdy je metoda „name_get“ přepsána (prosím nedělejte to).

    - `no_open`: Boolean, výchozí hodnota je „false“. Pokud je nastavena na „true“, mnohoúhelník nebude
při kliknutí na něj (v režimu pro čtení) přesměrovat na záznam

... kódový blok :: XML

<vlastnost jméno="měna_id" možnosti="{&#39;nepřidat: pravda, neotevírat: pravda&#39;}"/>

Many2One Barcode ('many2one_barcode')
Widget pro pole typu „many2one“ umožňuje otevřít fotoaparát mobilního zařízení (Android/iOS) k naskenování čárového kódu.

Specializace pole typu many2one, kde uživatel může používat nativní fotoaparát k skenování čárového kódu.
Pak používá funkci name_search, která hledá tento řetězec.

Pokud je tento widget nastaven a uživatel aplikaci nepoužívá,
pokud nebude, bude se vracet na standardní pole typu „many2one“ („Many2OneField“)

    - Podporované typy polí: many2one

Mnoho-k-jednomu avatar („many2one_avatar“)
Toto widget se podporuje pouze na poli typu „many2one“, které odkazují na model,
dědí z mixinu `image.mixin`. V režimu readonly zobrazuje obrázek
přidružený záznam vedle jeho „zobrazovaného jména“. Pozor, že „zobrazované jméno“ není
v tomto případě klikatelný odkaz. V editaci se chová stejně jako běžný
`many2one`.

    - Podporované typy polí: many2one

Více než jeden uživatel avatara (many2one_avatar_user)
Toto widget je specializací widgetu `Many2OneAvatar`. Když se objeví avatar,
kliknutí otevřeme okno chatu s příslušným uživatelem. Tento widget může
je možné nastavit pouze na pole typu „many2one“ směřující k modelu „res.users“.

    - Podporované typy polí: `many2one` (směřující na `res.users`)

Many2One Avatar Employee (`many2one_avatar_employee`)
Same jako `many2one_avatar_user`, ale pro pole typu `many2one`, které ukazují na objekt typu `hr.employee`.

    - Podporované typy polí: `many2one` (směřující na pole `hr.employee`)

Many2many (many2many)
Výchozí widget pro pole typu „mnoho k mnoha“.

    - Podporované typy polí: many2many

Atributy:

    - `mode`: řetězec (výchozí hodnota zobrazení)

    - `doména`: omezit data na konkrétní doménu

Možnosti:

    - `create_text`: umožňuje přizpůsobit text zobrazený při vkládání nového záznamu

    - `link_domain`: doména určující, zda lze do vztahu přidávat záznamy (výchozí hodnota: `true`).

    - `unlink“: doména určující, zda lze záznamy ze vztahu odstranit (výchozí hodnota: „true“).

Soubor s binárním obsahem (soubor many2many_binary)
Tento widget umožňuje uživateli nahrávat nebo mazat soubory najednou.

Poznámka: Tento widget je specifický pro model „ir.attachment“.

    - Podporované typy polí: many2many

Možnosti:

    - `povolené přípony souborů`: přípona souboru, kterou může uživatel vybrat v dialogovém okně pro výběr souboru

(viz atribut „accept“ v tagu input typu file)

Mnoho k mnohu tagy („many2many_tags“)
Zobrazte pole typu many2many jako seznam štítků.

    - Podporované typy polí: many2many

Možnosti:

    - `vytvořit“: doména určující, zda lze nová tag vytvářet (výchozí hodnota: „pravda“).

... kódový blok::xml



    - `color_field`: název numerického pole, které by mělo být v pohledu přítomné.
Barva bude vybrána podle její hodnoty.

... kódový blok::xml

<položka název="kategorie_id" widget="many2many_tagy" možnosti={'barva_pole': 'barva'} />

    - „no_edit_color“: nastavte na „true“, abyste odstranili možnost změnit barvu štítků
(výchozí hodnota je „false“).

... kódový blok::xml

<položka jméno="kategorie_id" widget="mnoho-místo-mnoho_tagy" možnosti={'barva_pole': 'barva', 'nepovoleno_editovat_barvu': true} />

    - `edit_tags`: nastavte na hodnotu „true“, abyste mohli aktualizovat záznamy související s tagem kliknutím na tagy.
(výchozí hodnota je „false“).

... kódový blok::xml

<položka jméno="kategorie_id" widget="many2many_tagy" možnosti={'edit_tags': true}/>

Mnoho k mnohu - Přehled formulářů (form.many2many_tags)
Specializace widgetu many2many_tags pro formuláře. Obsahuje některé další
kód, který umožňuje úpravu barvy štítku.

    - Podporované typy polí: many2many

Many2many Tags - Pohled na kanban (`kanban.many2many_tags`)
Specializace widgetu many2many_tags pro kanbanové pohledy.

    - Podporované typy polí: many2many

Mnoho-množstevní checkboxy (many2many_checkboxes)
Toto pole zobrazuje seznam zaškrtávacích políček, které umožňují uživateli vybrat
podmnožina volby. Pozor, zobrazený počet hodnot je omezen na
„100“. Toto omezení není nastavitelné, jednoduše umožňuje řešit extrémní případy
kde je tento widget špatně nastaven na poli s obrovským komodálem.
V případě více záznamů je vhodnější seznamový pohled, který umožňuje stránkování a filtrování.

    - Podporované typy polí: many2many

One2many („one2many“)
Výchozí widget pro pole typu „one2many“.
Většinou zobrazuje data v podlistovém nebo podkanbanovém pohledu.

    - Podporované typy polí: one2many

Možnosti:

    - `vytvořit“: doména určující, zda lze vytvářet související záznamy (výchozí hodnota: „pravda“).

    - `delete“: doména určující, zda lze smazat související záznamy (výchozí hodnota: „true“).

... kódový blok::xml



    - `create_text`: řetězec, který slouží k přizpůsobení textu tlačítka „Přidat“.

... kódový blok::xml

<políčko jméno="želvy" možnosti="{'vytvořit_text': 'Přidat želvu'}" />

Statusová lišta (status bar)
To je pole specifické pro formuláře, které se zobrazují v horní části stránky.
mnoha forem, které představují proud a umožňují vybrat konkrétní stav.

    - Podporované typy polí: „vybraná hodnota“, „mnoho k jedné“

Reference („reference“)
pole „reference“ je kombinací výběru (pro model) a
pole typu `many2one` (pro jeho hodnotu). To umožňuje výběr záznamu v databázi.
arbitrární model.

    - Podporované typy polí: `char`, `reference`

Možnosti:

    - `model_field`: název modelu, který obsahuje model záznamů, které lze vybrat.
Pokud je tato volba nastavena, část pole „reference“ s výběrem není zobrazena.

.. odkaz/odkaz na javascript/výhled na widgety:

Widgety
-------

Páska („webová páska“)
Tento widget zobrazuje lištu v pravém horním rohu karty nebo listu prohlížeče.
například pro označení archivovaných záznamů.

... kódový blok :: XML

<widget name="web_ribbon" title="Archiv" bg_color="text-bg-danger"/>

Atributy:

    - „Název“: zobrazený text na liště.
    - „nástrojová lišta“: zobrazený text v nástrojové liště.
    - `bg-class`: název třídy, kterou se má na liště nastavit, obvykle pro definování barvy lišty.

Týdenní dny (week_days)
Tento widget zobrazuje seznam tlačítek s pondělím až nedělí, jedno tlačítko pro každý den.
a umožnit uživateli vybrat podmnožinu z možností.

... kódový blok :: XML

<widget name="týdenní dny"/>

Kroky klienta
==============

Klientský prvek je komponenta, která může být zobrazena jako hlavní prvek v
webový klient zabírající celé místo pod navigačním lištovým menu, stejně jako „akční okno“.
Toto je užitečné, pokud potřebujete komponentu, která není příliš úzce spjata s existujícím
výhled nebo konkrétní model. Například aplikace Diskuse je akcí klienta.

Termín „klientské akce“ má různé významy v závislosti na kontextu:

- z pohledu serveru je to záznam modelu ir_action.
s pole typu char označeným tagem *
- Z pohledu webového klienta je to komponenta Owl registrovaná v
registr akcí pod stejným klíčem jeho značku

Každý položka nabídky je spojena s akcí klienta, takže otevření této položky bude
vyhledejte definici akce na serveru a pak zkontrolujte její značku v akci
registru, získá komponentní definici. Tato komponenta se pak zobrazí
akční kontejner.

Přidání akce klienta
----------------------

Akce klienta je komponenta, která bude ovládat část obrazovky pod
Navbar. Definice klientské akce je stejně jednoduchá jako vytvoření komponenty Owl
Přidáme ho do seznamu akcí.

... kódový blok: JavaScript

import { registry } z "@web/jádro/registry";
class MyClientAction extends Component { ... }
registry.kategorie("akce").přidat("můj vlastní akční krok", KlientskáAkce);

Pak je třeba vytvořit klienta.
akční záznam (záznam modelu „ir.actions.client“) s vhodným
Atribut „tag“:

... blok kódu::xml

<záznam id="my_client_action" model="ir.actions.client">
<pole name="jméno">Nějaké jméno</pole>
<políčko jméno="tag">my-custom-action</políčko>
</záznam>
