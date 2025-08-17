
..._frontend/služby:

========
Služby
========

Služby jsou dlouhodobé kusy kódu, které poskytují funkci. Mohou být
importované komponentami (pomocí metody „useService“) nebo jinými službami.
může deklarovat sadu závislostí. V tomto smyslu jsou služby v podstatě
DI systém „vpravení do závislosti“. Například služba „oznámení“
poskytuje způsob zobrazení oznámení nebo „rpc“ služba je vhodná
cesta, jak požádat odoo server.

Následující příklad registruje jednoduchou službu, která zobrazuje notifikaci.
každých 5 sekund:

... kódový blok: JavaScript

import { registry } z "@web/jádro/registry";

const myService = {
závislosti: ["notifikace"]
start(env, { notification }) {
let counter = 1;
setInterval(function () {
notifikace.add(`Tik tik ${counter++}“);
            }, 5000);
        }
    };

registry.kategorie("služby").přidat("můjSlužba", mySlužba);

Při spuštění webového klienta se všechny služby obsažené v souboru „services“
registru, přičemž název použitý v registru je název služby.

.. poznámka::

Většina kódu, který není součástí komponenty, by měla být zabalena do služby.
Pokud funkce má nějaký vedlejší účinek, je to velmi užitečné pro testování.
účelům: testy mohou zvolit, které služby jsou aktivní, takže je menší šance
pro nežádoucí vedlejší účinky, které narušují kód testovaný.

Definice služby
==================

Služba musí implementovat následující rozhraní:

..js:data:závislosti

Volitelný seznam řetězců. Je to seznam všech závislostí (ostatních služeb).
že tato služba potřebuje

..js:start(env, deps)

:param Environment env: aplikační prostředí
:param Object deps: všechny požadované závislosti
:vrací: hodnotu služby nebo slib<hodnota služby>

Toto je hlavní definice služby. Může vrátit buď hodnotu, nebo
slib. V tom případě si služba jen počká na slib.
převést na hodnotu, která je pak hodnotou služby.

Některé služby nemusí mít žádnou hodnotu. Mohou jen dělat svou práci bez ohledu na
musí být přímo volány jiným kódem. V takovém případě bude mít hodnotu
na hodnotu „null“ v proměnné „env.services“.

..js:data::async

Volitelná hodnota. Pokud je zadaná, měla by být buď „pravda“ nebo seznam řetězců.

Některé služby musí poskytovat asynchronní API. Například služba rpc.
služba je asynchronní funkcí nebo službou `orm`, která poskytuje sadu
funkce pro volání serveru Odoo.

V takovém případě je možné, že komponenty, které využívají službu,
před koncem asynchronní funkce. Většinou se tak stane
asynchronní volání funkce musí být ignorováno. Jinak by se
Potenciálně velmi nebezpečné, protože podkladový komponent není aktivní.
Značka „async“ je způsob, jak toho dosáhnout: signalizuje službě vytvářejícímu službu
že všechny asynchronní volání z komponent by měly být ponechány v očekávání.
komponenta je zničena.


Používání služby
===============

Služba, která je závislá na jiných službách a má správně vyhlášené
„závislosti“ jen získá odkaz na příslušné služby
v druhém parametru metody „start“.

Hook „useService“ je správným způsobem, jak použít službu v komponentě.
jednoduše vrací odkaz na hodnotu služby, která může být následně použita
komponentu později. Například:

... kódový blok: JavaScript

import { rpc } z "@web/jádro/síť/rpc";

klas MyComponent prodlouží třídu Component
setup() {
onWillStart(() => {
const výsledek = vyčkat na RPC ...;
        })
      }
    }

Seznam použité literatury
==============

.. seznam tabulkový::
:šířky: 25 75
:hlavičky: 1

   * -Technické jméno
     - Stručný popis
   * - :ref:`cookies <frontend/services/cookie>`
     - číst nebo měnit soubory cookie
   * - :ref:`efekt <frontend/services/effect>`
     - zobrazit grafické efekty
   * :-:ref:`http <frontend/services/http>`
     - vykonávat nízké úrovně http volání
   * – :ref:`oznámení <frontend/services/notifications>`
     - zobrazit oznámení
   * – router <frontend/services/router>
     - spravovat URL prohlížeče
   * :-:ref:`rpc <frontend/services/rpc>`
     - odesílat požadavky na server
   * –:ref:`skrollač <frontend/služby/skrollač>`
     - zpracovávat kliknutí na prvky Anchor
   * – :ref:`název <frontend/services/name>`
     - číst nebo měnit název okna.
   * – :ref:`uživatel <frontend/services/user>`
     - poskytuje nějaké informace o aktuálním uživateli

..._frontend/services/cookie:

Služba cookies
--------------

Přehled
~~~~~~~~

- Technické označení: „cookies“
- Závislosti: žádné

Poskytuje způsob, jak s cookies manipulovat. Například:

... kódový blok: JavaScript

cookieService.setCookie("hello", "odoo");

API
~~~

..js:data:aktuální

Objekt, který reprezentuje každý soubor cookie a jeho hodnotu (nebo prázdnou řetězcovou hodnotu).

..js:funkce:setCookie(název, hodnota, doba platnosti)

:param  string   name: jméno souboru cookie, který má být nastaven
:param hodnota libovolná: volitelné. Pokud je zadána, bude se soubor cookie nastavit na tuto hodnotu
:parametr number ttl: volitelný. čas v sekundách před smazáním souboru cookie (výchozí hodnota = 1 rok)

Nastaví soubor cookie s názvem name na hodnotu value s maximální dobou platnosti ttl

.. funkce:deleteCookie(jméno)

:param  str  name: jméno souboru cookie

Smaže cookies s názvem 'name'.

..._frontend/services/effect:

Efektivní služba
--------------

Přehled
~~~~~~~~

* Technické označení: „efekt“
* Závislosti: žádné

Efekty jsou grafické prvky, které se mohou na stránce zobrazit dočasně a obvykle slouží k poskytnutí zpětné vazby uživateli, že se něco zajímavého stalo.

Dobrým příkladem je třeba duhový muž:

.. obrázek:services/rainbow_man.png
:alt: Efekt duhy
:šířka: 600



Takto se může zobrazit:

... kódový blok: JavaScript

const effectService = useService("effect");
effectService.add({
typ: „duhový muž“, // lze vynechat, výchozí typ je již „duhový muž“
zpráva: „Bum! Nejlepší výkon týmu za posledních 30 dní.“
    });

.. varování ::
Háček useEffect není spojený s efektem služby.

API
~~~

..js:funkce: add(options)

:param objekt options: možnosti efektu. Ty se předají podkladovému komponentu efektu.

Zobrazit efekt.

Možnosti jsou definovány takto:

... blok kódu:: ts

rozhraní EffectOptions {
    // The name of the desired effect
typ?: řetězec;
[parametr: řetězec]: libovolný.
  }

Dostupné efekty
~~~~~~~~~~~~~~~~~

Aktuálně je jediným efektem duhový muž.

RainbowMan
**********

... kódový blok: JavaScript

effectService.add({ typ: "duha" });

.. seznam tabulkový::
:šířky: 20 40 40
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * – `params.Component`
      - „owl.Component“?
      - Komponentní třída, kterou je nutné vytvořit uvnitř RainbowManu (bude nahrazovat zprávy).
    * – `params.props`
      - „objekt?=“
      - Pokud je parametr Component nastaven, mohou být jeho vlastnosti přeneseny touto proměnnou.
    * „params.message“
      - „string = „Dobrá práce!““
      - Zprávou je oznámení, které drží duhový muž.

Pokud jsou efekty vypnuté pro uživatele, nebude se objevovat žádný duhový muž a pouze běžná notifikace.
Pokud se tak nestane, bude zobrazeno jako výchozí.

Pokud jsou efekty zapnuté a parametr Component je definován, parametr message se nepoužívá.

Zpráva je buď prostý řetězec, nebo řetězec reprezentující HTML.
(pokud chcete interakce v DOM, použijte preferovaně parametry.Component).
    * – „params.messageIsHtml“
      - „Pravda“
      - Přiřazeno hodnotě true, pokud zpráva představuje HTML a bude správně vložena do DOMu.
    * – „params.img_url“
      - „struna?=/web/statické obrázky/smile.svg“
      - URL obrázku, který se má zobrazit uvnitř duhy.
    * – `params.fadeout`
      - „(pomalý|střední|rychlý|žádný)“==„střední“
      - Zpoždění pro Rainbowmana, aby zmizel.

„rychle“ udělá z Rainbowmana rychle pryč.

„střední“ a „pomalé“ se trochu déle zobrazí, než zmizí (lze použít v případě delšího textu v proměnné param).

„ne“ udrží na obrazovce Rainbowmana, dokud uživatel neklikne někde mimo Rainbowmana.


Jak přidat efekt
~~~~~~~~~~~~~~~~~~~~

... /frontend/services/effect_registry/:

Účinky jsou uloženy v registru nazvaném „účinky“.
Nový efekt můžete přidat jménem a funkcí.

... kódový blok: JavaScript

const effectRegistry = registry.kategorie("efektů");
effectRegistry.add("duhový muž", rainbowManEffectFunction);

Funkce musí splňovat tuto API:

..js:function::<nový efekt funkce>(současné prostředí, parametry)

:param Env env: prostředí, které služba obdrží

:parametrem objektu params: parametry, které byly přijaty z funkce add na službě.

:návratová hodnota: „(komponenta, vlastnosti) nebo prázdné“ Komponenta a její vlastnosti nebo nic.

Tato funkce musí vytvořit komponentu a vrátit ji. Tento komponent je umístěn uvnitř
komponenty účinku.

Příklad
~~~~~~~

Řekněme, že chceme přidat efekt, který dodá stránce šedavý nádech.

... kódový blok: JavaScript

import { registry } z "@web/core/registry";
import { Komponenta, xml } z "@odoo/owl";

třída SepiaEffect je dědicem komponenty
statický šablona = `
<div styl="
pozice: absolutní;
levý: 0;
top: 0;
šířka: 100%;
výška: 100%;
pointer-events: none;
pozadí: rgba(196,135,0, 0.4);

    `;
  }

exportní funkce sepiaEffectProvider(env, parametry = {})
return {
Komponenta: SepiaEffect
      };
  }

const effectRegistry = registry.kategorie("efektů");
effectRegistry.add("sepia", sepiaEffectProvider);


A pak zavolejte někam, kam chcete a uvidíte výsledek.
Tady se jí volá v souboru webclient.js, aby byla viditelná všude pro příklad.

... kódový blok: JavaScript

const effectService = useService("effect");
effectService.add({ typ: 'sepia' });

.. obrázek:services/odoo_sepia.png
:alt:Odoo v šedé
:šířka: 600


.._frontend/services/http:

Http služba
------------

Přehled
~~~~~~~~

* Technické jméno: „http“
* Závislosti: žádné

Většina interakcí mezi klientem a serverem v odoo je „RPC“ („XMLHTTPRequest“), což jsou nízké úrovně.
Kontrola požadavků může být někdy nutná.

Tato služba umožňuje odesílat požadavky „GET“ a „POST“ (<https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods>).

API
~~~

..js:async funkce:get(cesta, čtení metoda = "json")

:param string trasa: URL, na kterou se má odeslat požadavek

:vrací: výsledek požadavku v formátu definovaném parametrem readMethod.

Odesílá požadavek GET.

..js:async funkce:post(cesta [,parametry = {} ,čtení metoda = "json"] )

:param string trasa: URL, na kterou se má odeslat požadavek


:vrací: výsledek požadavku v formátu definovaném parametrem readMethod.

Vyšle požadavek na server.

Příklad
~~~~~~~

... kódový blok: JavaScript

const httpService = použít službu ("http");
const data = (await httpService.get("https://something.com/posts/1"));
  // ...
čekat na požadavek na „https://něco.cz/posts/1“ s následujícími parametry:

..._frontend/services/notification:

Informační služba
--------------------

Přehled
~~~~~~~~

* Technické označení: „oznámení“
* Závislosti: žádné

Služba „oznámení“ umožňuje zobrazit oznámení na obrazovce.

... kódový blok: JavaScript

const notificationService = useService("notification");
notificationService.add("Jsem velmi jednoduchá notifikace");

API
~~~

..js:funkce:add(zpráva, [možnosti])

:param  str   message: zpráva, která se má zobrazit
:parametrem je objekt options, který obsahuje možnosti oznámení.
:vrací: funkci pro zavření notifikace

Zobrazí upozornění.

Definice možností je uvedena v:

...... seznamová tabulka::
:šířky: 15 30 55
:hlavičkové řádky: 1

      * - Jméno
        - Typ
        - Popis
      * „Titul“
        - string
        - Přidejte název do oznámení
      * – „typ“
        - „Varování“ | „Nebezpečí“ | „Úspěch“ | „Informace“
        - Změní barvu pozadí podle typu
      * „lepkavý“
        - logická
        - Zda oznámení zůstane až do vyhození
      * – „class“
        - string
        - Další třída CSS, která bude přidána k notifikaci.
      * – onClose
        - funkce
        - zpětná volba, která se spustí při zavření oznámení
      * – „tlačítka“
        - tlačítko[] (viz níže)
        - seznam tlačítek, které se mají zobrazit v oznámení
      * – autocloseDelay
        - číslo
        - doba v milisekundách, po kterou se oznámení zavře automaticky


Tlačítka jsou definována takto:

...... seznamová tabulka::
:šířky: 15 30 55
:hlavičkové řádky: 1

      * - Jméno
        - Typ
        - Popis
      * – „jméno“
        - string
        - Text tlačítka
      * – „onClick“
        - funkce
        - volání, které se má spustit při kliknutí na tlačítko
      * – „primární“
        - logická
        - zda tlačítko má být stylizováno jako primární tlačítko

Příklady
~~~~~~~~

Upozornění na prodej s tlačítkem, které vás přesměruje na nějakou stránku s provizí.

... kódový blok: JavaScript

  // in setup
tento.notifikační služba = použít službu ("notifikace");
tento.akčníSlužba = použít službu ("akce");

  // later
tato.notifikačníSlužba.přidat("Dokončili jste obchod!",
název: „Gratulace“,
typ: "úspěch",
tlačítka: [
        {
jméno: „Vidíte komisi“,
onKliknutí: () => {
tento.akčníSlužba.vykonatAkci("komise_akce");
            },
        },
    ],
  });

.. obrázek:services/notification_service.png
:šířka: 600 pixelů
:alt: Příklad oznámení


Oznámení, které se zavře po druhé:

... kódový blok: JavaScript

const notificationService = useService("notification");
const close = notifikaceSlužba.add("Zavřu se rychle");
setTimeout(zavřít, 1000);

.._frontend/services/router:

Router Service
--------------

Přehled
~~~~~~~~

- Technické označení: „Router“
- Závislosti: žádné

Služba „Router“ nabízí tři funkce:

* informace o aktuální trase
* možnost aplikace aktualizovat URL podle stavu
* poslouchá každou změnu haše a ostatní aplikace informuje.

API
~~~

..js:data:aktuální
:noindex:

Aktuální trasa je dostupná pomocí klíče „current“. Je to objekt
s těmito informacemi:

   * „cesta (řetězec)“: cesta pro aktuální umístění (nejspíš / web)
   * `hledání (objekt)`: slovník, který mapuje každé klíčové slovo hledaného výrazu (dotazovací řetězec).
z URL na jeho hodnotu. Prázdný řetězec je hodnota, pokud žádná hodnota nebyla
výslovně uvedeno
   * `hash(objekt)`: stejné jako výše, ale pro hodnoty popsané v hash.

Příklad:

... kódový blok: JavaScript

  // url = /web?debug=assets#action=123&owl&menu_id=174
const { cesta, vyhledávání, hash } = služby routeru aktuální.
console.log(pathname); //   /web
console.log(hledání); //   { debug="assety" }
console.log(hash); //   { akce: 123, sova: '', menu_id: 174 }

Aktualizaci URL provádí metoda pushState:

..js:funkce:pushState(hash: objekt, [replace?: booleovská hodnota])


:parametrem boolean replace se nahradí URL, pokud je nastaven na hodnotu true, jinak
hodnoty z hash se aktualizují.

Za každou dvojici klíč-hodnota v objektu hash se aktualizuje URL. Pokud je hodnota
Pokud je nastaven na prázdný řetězec, klíč se přidá do URL bez odpovídající hodnoty.
hodnota.

Pokud je pravdivé, pak „replace“ argument říká směrovači, že URL hash by měl být
úplně nahrazeny (takže hodnoty, které nejsou obsaženy v objektu hash, budou odstraněny).

Tato metoda neobnoví stránku, ani ji nenapadne vyvolat
události hashchange ani události ROUTE_CHANGE v hlavním autobusu (viz frontend/framework/bus).
Je to proto, že tento způsob je určen pouze k aktualizaci URL. Kód volající
tato metoda má za úkol zajistit, aby se obrazovka aktualizovala.
Ale dobře.

Příklad:

... kódový blok: JavaScript

  // url = /web#action_id=123
routerService.pushState({ menu_id: 321 });
  // url is now /web#action_id=123&menu_id=321
routerService.pushState({ yipyip: "" }, replace: true);
  // url is now /web#yipyip


Nakonec metoda „redirect“ přesměruje prohlížeč na zadanou URL adresu:

..js:funkce:redirect(url, časový limit)


:param: bool wait: pokud je tato hodnota nastavena na true, čeká se na připravenost serveru a poté se provede redirekce

Přesměrujte prohlížeč na „url“. Tato metoda znovu načítá stránku.
Argument se používá jen zřídkakdy: je užitečný v některých případech, kdy víme, že
server bude nedostupný na krátkou dobu, obvykle hned po instalaci nějakého rozšíření.
aktualizace nebo instalace operačního systému.

.. poznámka::
Řízení směrování vydává událost „ROUTE_CHANGE“ na hlavní sběrnici:
pokaždé, když se změní aktuální trasa.

.._frontend/services/rpc:

Služba RPC
-----------

Přehled
~~~~~~~~

- Technické označení: „rpc“
- Závislosti: žádné

Služba „rpc“ poskytuje jedinou asynchronní funkci pro odesílání požadavků
serveru. Volání kontroleru je velmi jednoduché: cesta by měla být první
Druhým parametrem může být argument a „parametry“ objekt.

... kódový blok: JavaScript

import { rpc } z "@web/jádro/síť/rpc";

   // somewhere else, in an async function:
const result = await rpc("/my/route", {some:"value"});

.. poznámka::

Poznámka: služba „rpc“ je považována za nízkou úroveň.
pouze pro interakci s kontroloři Odoo. Pro práci s modelem (který
Je tedy nejdůležitějším použitím (a také jediným, které je v současné době podporováno) a měl by se používat služba „orm“.
Ve skutečnosti se ale jedná o úplně jiný druh zvířete, který je vlastně mnohem nebezpečnější.

API
~~~

..js:funkce:rpc(trasa, parametry, nastavení)

:param  string  route:  cílová trasa požadavku
:param Object params: (volitelné) parametry, které byly odeslány na server
:parametru Objekt nastavení: (volitelně) požadavky na nastavení (viz níže)

Objekt „nastavení“ může obsahovat:

    - „xhr“, což by mělo být „XMLHTTPRequest“ objekt. V takovém případě
„RPC“ metoda pouze použije ji namísto vytvoření nové.
Je užitečná při přístupu k pokročilým funkcím knihovny XMLHTTPRequest.
    - „tichý (logická hodnota)“ Pokud je nastaveno na „pravdu“, webový klient nebude
zpětná vazba, že je nevyřízený RPC.

Služba „rpc“ komunikuje se serverem pomocí „XMLHTTPRequest“.
objekt, který je konfigurován tak, aby pracoval s obsahovým typem „application/json“. Takže jasně
obsah požadavku musí být serializovatelný do formátu JSON. Každý požadavek provedený
Tato služba používá metodu „POST“ v rámci protokolu HTTP.

Chyby serveru vrací odpověď s kódem HTTP 200, ale „rpc“
Služba je považuje za chybu.

Řešení chyb
~~~~~~~~~~~~~~

RPC může selhat z důvodu dvou hlavních příčin:

* nebo server Odoo vrátí chybu (takže tento typ chyby nazýváme „chyba serveru“).
V případě, že se tak stane, vrátí požadavek HTTP s kódem HTTP 200, ale
objekt odpovědi, který obsahuje klíč „chyba“.

* nebo je jiný typ sítě.

Pokud selže RPC, pak:

* slib reprezentující RPC je odmítnut, takže volající kód spadne.
pokud se s ní nevypořádá.
* na hlavní aplikační sběrnici je spuštěn událostní signál „RPC_ERROR“. Hodnota události
obsahuje popis chyby:

Pokud je chyba na straně serveru (serverový kód vyhodil výjimku). V tom případě
událostní hlavička bude obsahovat objekt s následujícími klíči:


  * „typ = server“
  * „message(string)“
  *
„kód(číslo)“

  *
„name(str)“ (volitelné, používá se službou chyby pro hledání vhodného
dialog, který se má použít při řešení chyby.

  * „subtype(string)“ (volitelné, často používané k určení názvu dialogu)
  * „data(objekt)“ (volitelný objekt, který může obsahovat různé klíče mezi nimiž je
„debug“: hlavní informace o ladění (s výčtem volání funkcí).

Pokud se jedná o síťovou chybu, pak popis chyby je prostě objekt
„{typ: 'síť'}“.
Při chybě v síti se zobrazí :ref:`notifikace <frontend/services/notification>`.
zobrazena a server je pravidelně kontaktován, dokud neodpoví.
Oznámení je uzavřeno, jakmile server odpoví.

..._frontend/services/scroller:

Služba Scroll
----------------

Přehled
~~~~~~~~

- Technický název: „Posuvník“
- Závislosti: žádné

Každýkrát když uživatel klikne na odkaz v prohlížeči, tato služba automaticky posouvá
na cíl (pokud je to vhodné).

Služba přidá posluchače události, aby zjistila, kdy dojde k „kliknutí“ na dokumentu. Služba kontroluje
pokud se v atributu href obsaženém v selektoru nachází platný výraz, který umožňuje odlišit ankery a Odoo.
akcí (např. <a href="#target_element">). Pokud není, nic nedělá.

Pokud se zdá, že byl kliknutý odkaz, spustí se událost „SCROLLER:ANCHOR_LINK_CLICKED“ na hlavním aplikačním busu.
cílená na prvek. Tato událost obsahuje vlastní událost, která obsahuje „element“ odpovídající a jeho „id“ jako referenci.
Může umožnit dalším částem zacházet s chováním vzhledem k samotným kotvám.
pokud by se mělo zabránit tomu, aby k němu došlo. Pokud se nezabrání, pak uživatelské rozhraní
posunout se na cílový prvek.

API
~~~

Následující hodnoty obsahuje vysvětlený výše uvedený událostní typ „anchor-link-clicked“.

.. seznam tabulkový::
:šířky: 25 25 50
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * „Element“
      - „HTML prvek | null“
      - Zaškrtávací políčko, na které se odkazuje tag <a>
    * – „id“
      - „smyčka“
      - ID obsažené v atributu href
    * „Original Ev“
      - „Událost“
      - Původní událost kliknutí

.. poznámka::
Služba pro posouvání obsahu vydává událost „SCROLLER:ANCHOR_LINK_CLICKED“ na hlavní autobus (viz. :ref:`hlavní autobus <frontend/framework/bus>`).
Pokud chcete zabránit výchozímu chování posouvání služby Scroll, musíte použít metodu preventDefault() na události.
posluchači, abyste mohli správně implementovat své chování z posluchače.

..._frontend/services/title:

Titulní služba
-------------

Přehled
~~~~~~~~

- Technické jméno: „název“
- Závislosti: žádné

Služba „Title“ nabízí jednoduchou API, která umožňuje číst/upravovat dokument
název. Například pokud je aktuální název dokumentu „Odoo“, můžeme jej změnit
„Odoo 15 – Apple“ pomocí následujícího příkazu:

... kódový blok: JavaScript

   // in some component setup method
const titleService = useService("title");

titleService.setParts({ odoo: „Odoo 15“, fruit: „Jablko“ });

API
~~~


Služba „Title“ pracuje s následujícím rozhraním:

... blok kódu:: ts

rozhraní Parts {
[klíč: řetězec]: řetězec | null;
   }

Každý klíč představuje identitu části titulu a každá hodnota je
Zobrazovaný řetězec nebo hodnota null, pokud byl odstraněn.

Jeho API je:

..js:data:aktuální
:noindex:

To je řetězec, který reprezentuje současný název. Je strukturován takto:
takto: „hodnota_1 – … – hodnota_n“, kde každá hodnota_i je (nepovinné)
hodnota nalezená v objektu Parts (vráceném funkcí getParts).

..js:funkce::getParts

:vrací: části aktuálního objektu Parts, který je udržován službou titulů

..js:funkce:setParts(součásti)

:param Parts parts: objekt reprezentující požadovanou změnu

Metoda „setParts“ umožňuje přidávat, nahrazovat nebo mazat několik částí titulu.
Odstranění části (hodnoty) se provádí nastavením příslušného klíče na hodnotu null.

Pozor, že lze měnit pouze jednu část bez ovlivnění ostatních
části. Například pokud je název složen z následujících částí:

... kódový blok::javascript

{ odoo: "Odoo", akce: "Import" }

s aktuálním nastavením „Odoo – Import“

... kódový blok::javascript

setParts({
akce: null,
      });

Změní název na „Odoo“.


.._frontend/services/user:

Uživatelská podpora
------------

Přehled
~~~~~~~~

* Technické označení: „uživatel“
* Závislosti: `rpc`

Služba „uživatel“ poskytuje hromadu dat a několik funkcí, které pomáhají.
uživatel, který je sítí propojený.


API
~~~

.. seznam tabulkový::
:šířky: 25 25 50
:hlavičkové řádky: 1

    * - Jméno
      - Typ
      - Popis
    * „kontext“
      - „Objekt“
      - :ref:`kontext uživatele <frontend/framework/user_context>
    * „- db“
      - „Objekt“
      - Informace o databázi
    * – „home_action_id“
      - „(číslo | nepravdivé)“
      - ID akce, která bude sloužit jako domov pro uživatele
    * – „jeAdmin“
      - „logická“
      - Zda uživatel je administrátor (skupina base.group_erp_manager nebo superuživatel).
    * „- jeSystém“
      - „logická“
      - Zda je uživatel součástí systémové skupiny (base.group_system)
    * „lang“
      - „struna“
      - Jazyk použitý
    * „jméno“
      - „struna“
      - Uživatelské jméno
    * – „partnerId“
      - „číslo“
      - ID partnera uživatele
    * „TZ“
      - „struna“
      - Časová zóna uživatele
    * – „id uživatele“
      - „číslo“
      - ID uživatele
    * – „uživatelské jméno“
      - „struna“
      - Alternativní přezdívka uživatele


..js:funkce: aktualizovat kontext (aktualizace)

:param objekt update: Objekt, který aktualizuje kontext

aktualizovat uživatelský kontext s předaným objektem.

... kódový blok :: JavaScript

updateKontext(true)

..js:funkce: odstranit z kontextu (klíč)

:param  string  klíč: klíč cílového atributu

odstranit hodnotu s daným klíčem z kontextu uživatele (viz frontend/framework/user_context)

... kódový blok :: JavaScript

userService.odstranitZ kontextu ("je přítel")

..js:funkce:hasGroup(skupina)

:param  string  skupina: id xml pro vyhledání skupiny

:návratová hodnota: `Promise<boolean>` je uživatel v skupině

zjistit, zda uživatel patří do skupiny

... kódový blok :: JavaScript

const jeVProdejníSkupině = (await uživatelský servis.máSkupinu("sale.group_sales"))
