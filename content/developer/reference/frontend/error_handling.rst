==============
Řešení chyb
==============

V programování je řešení chyb složitá věc s mnoha nástrahami.
je ještě náročnější, když píšete kód v rámci omezení frameworku.
protože způsob, jakým chyby řešíte, musí být v souladu s tím, jak rámec chyby vyřizuje.
chyby a naopak.

Tento článek popisuje obecné způsoby, jakým je v JavaScriptu řešeno chybové hlášení.
framework a Owl a dává několik doporučení o tom, jak se s těmito interagovat.
Systémy tak, aby se vyhnuly běžným problémům.

Chyby v JavaScriptu
====================

Předtím, než se ponoříme do způsobu řešení chyb v Odoo a také do toho, jak a kde je
pokud chceme upravit způsob zacházení s chybami, je dobré si uvědomit, že jsme na
stejné stránce, pokud jde o to, co přesně myslíme „chybou“.
překvapivé chování JavaScriptu při zpracovávání chyb.

Třída Error
-----------------

První věc, která nás napadne při řešení chyb, je
vlastní třída Error nebo třídy, které ji dědí. V zbytku článku
když se budeme týkat objektu, který je instancí této třídy, použijeme
Použijte termín *Objekt chyby* v uvozovkách.

Může se hodit cokoliv
----------------------

V JavaScriptu můžete hodit jakýkoliv objekt. Obvykle se používá chybový objekt *Error*.
Ale můžete hodit jakýkoliv jiný předmět a dokonce i primitiva.
doporučit, abyste kdykoli házeli něco jiného než objekt *Error*.
JavaScriptový rámec musí být schopen tyto scénáře zvládnout.
pomůže vám pochopit některá rozhodnutí, která jsme museli učinit.

Při vytváření objektu *Error* sbírá prohlížeč informace o
současný stav „volacího řetězce“ (buď správný volací řetězec, nebo sestavený).
seznam volání pro asynchronní funkce a pokračování slibů). Tato informace je
se nazývá „stopa“ a je velmi užitečná pro ladění programu. Odoo framework zobrazuje
Tento záznam stavu v chybových hláškách, pokud je k dispozici.

Při hodnocení hodnoty, která není objektem Error, prohlížeč stále sbírá
informace o aktuální výzvě, ale tato informace není k dispozici
v JavaScriptu: je k dispozici pouze v konzole vývojových nástrojů, pokud se nejedná o chybu
vyřešené.

Hodit *chybové objekty* nám umožňuje zobrazit podrobnější informace, které
uživatel bude moci v případě potřeby zkopírovat/vložit do hlášení o chybě, ale také
chování chyb je odolnější, protože nám umožňuje filtrovat chyby podle jejich třídy.
při jejich zpracování. Bohužel, JavaScript nemá syntaxi pro
filtrováním chybové třídy v podmínce try/catch, ale relativně snadno můžete
sám/sama:

... kódový blok: JavaScript

try {
doStuff();
}
pokud (!(e je instancí třídy MyErrorClass)),
hodit e; // zachytili jsme chybu, kterou neumíme řešit, znovu ji vyhodíme
    }
    // handle MyErrorClass
  }

Odmítnutí slibu je chyba
-----------------------------

V počátcích přijetí slibů byly slibové závazky často považovány za způsob
ukládat rozdvojený výsledek a „chybu“, což bylo v té době docela běžné.
použít odmítnutí slibu jako způsob, jak signalizovat měkký neúspěch.
Začátek dobrý, prohlížeče a JavaScriptové runtimey dlouho
začal zacházet s odmítnutými sliby stejně jako s hozenými chybami.
všemi směry:

- vložení funkce s asynchronním chováním má stejný efekt jako vrácení Promise, který
s hodnotou, kterou byl hozen, jako důvodem k zamítnutí.
- bloky chybových hlášení v asynchronních funkcích zachytí odmítnuté slibované
odpovídající blok pokusu.
- runtimey shromažďují informace o sestavě odmítnutých slibů.
- Odmítnutá slibovaná operace, která není zachycena synchronně, vyvolá událost.
objekt globální/okno a pokud se nevolá metoda preventDefault na události,
Prohlížeče zaznamenají chybu a samostatné spouštěcí prostředí jako je Node ukončí proces.
- funkce ladiče „zastavit při výjimkách“ zastaví, když jsou slibované odmítnuty

Protože se jedná o odmítnuté slibování, Odoo Framework zachází s nimi stejně.
tak jako hozené chyby. Nedělejte odmítnuté sliby na místech, kde by
nevyvolat chybu a vždy odmítnout slib s objektem *Error*, který obsahuje chybovou zprávu.
důvodu.

„chybové“ události nejsou chyby
-----------------------------

S výjimkou událostí error na okně a událostí error na jiných objektech
například tagy <media>, <audio>, <img>, <script> a <link>.
Objekty XMLHttpRequest nejsou chyby. V tomto článku se „chyba“
Specificky se vztahuje pouze na hozené hodnoty a odmítnuté sliby. Pokud potřebujete
chcete-li se vypořádat s chybami na těchto prvcích nebo je chtít považovat za chyby, potřebujete
explicitně přidat událostní posluchače pro danou událost:

... kódový blok: JavaScript

const scriptEl = document.createElement("script");
scriptEl.src = "https://příklad.cz/třetí-strana-skript.js";
return nový Promise((resolve, reject) => {
scriptEl.addEventListener("error", odmítnout);
scriptEl.addEventListener("load", vyřešit);
hlavičku dokumentu doplní o scriptEl.
  });

Životní cyklus chyb v rámci Odoo JS frameworku
================================================

Vyhozené chyby se vrátí zpět do jejich volacího stromu, aby našly příslušnou výjimku
jim. Způsob, jakým je chyba řešena, závisí na tom, jaký kód se při ní objeví.
odvíjení volání. Ačkoli existuje nekonečné množství míst
chyby mohou být vyhozeny z nějaké části, existuje jen málo možných cest do rámce
kód pro zpracování chyb.

Vrhnout chybu na úrovni modulu
----------------------------------------------

Když se načte modul Javového skriptu, je spuštěn kód v horním úrovni tohoto modulu.
může vyvolat chybu. Zároveň může být doplněn o dialogové okno s výzvou k opravě.
Je kritický okamžik pro JavaScriptový rámec a některé moduly, které vykazují chyby.
může zabránit spuštění celého rámcového kódu, takže jakákoliv chybová hlášení
Tato fáze je „nejlepší snaha“. Chyby, které se vyskytnou při načítání modulu, by však měly být vždy
A minimálně si v prohlížeči zobrazit chybovou hlášku. Protože tento typ
chyba je kritická a aplikace se nemůže vrátit do původního stavu.
Váš kód tak, aby se modul nemohl v definici vyhodit.
Každé chybové hlášení a zpracování, které se v této fázi odehraje, je pouze
cílem pomoci vám, vývojáři, opravit kód, který vyvolal chybu.
Nenabízíme žádný mechanismus pro přizpůsobení způsobu, jakým se tyto chyby řeší.

Chybová služba
-----------------

Pokud je chyba vyhozena, ale nikdy nechycena, spustí runtime událost.
globální objekt („okno“). Druh události závisí na tom, zda byl chybový stav
synchronně nebo asynchronně: chyby vyvolané synchronními výjimkami
událost „chyba“ a chyby vyhozené z asynchronního kontextu.
Promise, které byly odmítnuty, vysílají událost „unhandledrejection“.

Rámec JS obsahuje službu, která se stará o zpracování těchto událostí:
chybová služba. Když obdrží jednu z těchto událostí, chybová služba začíná vytvářením
nový objekt Error, který se používá k zabalení chyby, která byla vyhozena; protože
může být hodnota jakákoliv a slib může být zrušen se všemi hodnotami včetně „undefined“
nebo „null“, což znamená, že není zaručeno, že obsahuje jakoukoliv informaci.
můžeme do něj uložit jakoukoliv informaci. Pro obalování používáme objekt Error
získat nějaké informace o hodnotě, která byla vyhozena, aby se mohla použít jednotně.
do rámcového kódu, který má zobrazovat informace o všech druzích chyb.

Služba chybové hlášení ukládá kompletní staptrace vyvolané chyby do této obálky.
Objekt chyby a při režimu ladění „aktivní zdrojové mapy“ používá zdrojové mapy k přidání
informace v tomto záznamu o sestavení, které obsahuje funkci
každé rámce zásobníku. Pozice funkce v balíčkovaných aktivitách je zachována, protože
Může být užitečný v některých scénářích. Když chyby mají „příčinu“, tento proces také odvine
„příčina“ řetězec pro sestavení kompletní staptrace. Zatímco „příčina“ pole
na objekty chyby je standardní, některé hlavní prohlížeče stále nezobrazují celý
stacktrace chybových řetězců. Proto tuto informaci ručně přidáváme.
Toto je zvláště užitečné v případě chybových hlášení uvnitř háčků Owl, o tom později.

Jakmile chyba obalu obsahuje všechny požadované informace, spouštíme proces
opravdu řešit chybu. K tomu účelu se služba chyb postupně spojuje
všechny funkce zaregistrované v registru error_handlers, dokud nebude jedna z těchto funkcí
vrací hodnotu pravdivou, která signalizuje, že chyba byla vyřešena. Po tomto
Pokud nebyl na události chyba volán preventivní příkaz a pokud služba chybová
schopnost přidat staplingový záznam do objektu chyby, který je volán službou chyby
Zabránit chybě a zobrazit stromové struktury v konzole.
Je to proto, že některé prohlížeče nezobrazují řetězec chyb správně.
a výchozí chování události je zaznamenání chyby v prohlížeči, takže jednoduše
překrýt chování, které umožňuje zaznamenat kompletní stromy výjimek. Pokud služba pro zpracování chyb
pokud nemáme k dispozici informace o sestavě chyby, kterou jsme hodili, nevoláme
`preventDefault“. K tomu může dojít při hodnocení nechybových hodnot: řetězců a nedefinovaných hodnot.
nebo jiných náhodně vzniklých objektů. V těchto případech si prohlížeč sám zaznamenává stavový řádek.
protože má tyto informace, ale neposkytuje je kódům JavaScriptu.

Registr error_handlers
-----------------------------

Registr error_handlers je hlavní cestou pro rozšíření způsobu, jakým JS framework
vykonává „univerzální“ chyby. Univerzální chyby znamenají v tomto kontextu chyby, které mohou nastat
V mnoha místech, ale mělo by se to řešit jednotně. Příklady:

- UserError: když uživatel zkouší provést operaci, kterou by měl vykonat Python
Pokud je pro obchodní důvody neplatný, pak kód v Pythonu vyvolá výjimku typu UserError,
Funkce RPC vrhá v JavaScriptu odpovídající chybu. To má potenciál
aby se mohlo stát na jakémkoli RPC kdekoli a nechceme, aby vývojáři museli řešit tyto problémy.
tento druh chyby explicitně ve všech těchto místech a chceme, aby se stejné chování dělo
všude: zastavte aktuálně běžící kód (což je dosažitelné pomocí throw).
a zobrazit dialog, který vysvětluje uživateli, co se stalo špatně.
- Chyba přístupu: stejné důvody jako u chyb uživatelů: může se stát v kterékoli fázi a
být zobrazena stejně, ať se děje kdekoliv
- LostConnection: stejné důvody znovu.

Vložení chyby do komponenty Owl
-------------------------------------

Registrace nebo modifikace součástí Owl je hlavním způsobem, jakým můžete rozšířit
funkčnosti webového klienta. Většina chyb tedy vzniká uživatelským
Jedním z možných scénářů je, že byl nějakým způsobem vypuštěn ze součásti Owla. Existuje několik možností:

- Vložení nastavení komponenty nebo během renderování
- Vyhození z uvnitř cyklu životního cyklu
- Vyvolání z událostního zpracovatele

Vyvoláním chyby z události nebo funkce nebo metody volané přímo
nebo kód Owla ani rámce JS.
kód je v zásobníku volání. Pokud chybu nechytíte, přistane přímo ve
chybová služba.

Když dojde k chybě při nastavení komponenty nebo během renderování, Owl zachytí
chybu a postupuje po hierarchii komponent, umožňující komponentám, které jsou registrovány
Chybové zpracovatele s „hookem onError“, které se pokusí chybu vyřešit. Pokud je
je nikým nezpracovávána, sova aplikaci zničí, protože je pravděpodobné, že
korupční stát.

.. viz též:
„Zpracování chyb v dokumentaci Owl <https://github.com/odoo/owl/blob/master/doc/reference/error_handling.md>“

Uvnitř Odoo je několik míst, kde nechceme, aby celá aplikace
při chybě havaruje a tak rámec má několik míst, kde používá
Hooku onError. Akční služba zabalí akce a pohledy do komponenty, která s nimi zachází
chyby. Pokud klientské akce nebo pohledy při zobrazování vyvolají chybu, pokusí se
se vrátit k předchozí akci. Chyba je odeslána do služby chyb
Aby se zobrazila chybová hláška i tak. Podobná strategie je používána v většině
místo, kde rámec volá do „uživatelského“ kódu: většinou zastavíme zobrazování
chybový komponenta a zobrazí chybové okno.

Při chybě v funkci zpětného volání háčku Owl vytvoří nový
Objekt chyby, který obsahuje informace o zásobníku, kde byla háčková funkce zaregistrována.
a nastaví příčinu na původní hodnotu, protože seznam
stopa původního chybového stavu neobsahuje žádné informace o tom, který komponenta zaregistrovala
Tento háček a kde je, obsahuje pouze informace o tom, co se tímto háčkem nazývá.
Háčky jsou volány kódem sovy, většina těchto informací je obecně neúplná.
pro vývojáře, ale vědět kde byla zaregistrována a kterým komponentou.
Je velmi užitečný.

Když se objeví chyba, která zní „OwlError: došlo k následující chybě v <hookName>“,
Ujistěte se, že si přečtete oba díly kompozitního záznamu o stavu:

.. kódový blok::
:vyznačit-řádky: 4,12

Chyba: V onMounted došlo k chybě „Moje chyba“.
při zahájení chyby
při načtení
v MyComponent.setup
nový komponentní uzel
v šabloně Root
v metodě MountFiber._render
v metodě render()
v metodě ComponentNode.initiateRender

Příčina: Chyba: Moje chyba
v metodě someMethod komponenty ParentComponent
v MountFiber.complete
v metodě Scheduler.processFiber
v metodě Scheduler.processTasks

První zvýrazněná řádka vám sdělí, který komponent zaregistroval událost „mounted“.
zavěšení, zatímco druhá zvýrazněná linie ukazuje na funkci, která vyvolala chybu.
V tomto případě volá dětská komponenta funkci, kterou dostala jako vlastnost
její rodičovskou složku a funkce je metodou rodičovské složky.
informací může být užitečná, protože metoda mohla být omylem spuštěna
dítě (nebo v nějakém bodě životního cyklu, kde by nemělo), ale také
Ať už je v metodě rodiče chyba.

Označování chyb jako vyřešených
-------------------------

V předchozích sekcích jsme hovořili o dvou způsobech registrace chybových handlerů: jedním
Přidává je do registru „error_handlers“ a druhý používá funkci „onError“.
sokolníkovi. V obou případech musí rozhodčí určit, zda chybu označí
vyřešené.

onError
~~~~~~~~~

Pokud je v Owlu uvedená funkce onError, tak se chyba považuje za
pokud ji nevrátíte zpět, bude vám zpracována sovími hlasy.
interfáz je pravděpodobně nesynchronizovaná s stavem aplikace, protože chyba
zabránil sově dokončit nějakou práci. Pokud nemůžete chybu vyřešit,
Měl byste ji vrátit a nechat ostatní kód se s tím vypořádat.

Pokud chcete zachovat stav aplikace, musíte zahodit výjimku.
může být znovu zpracována bez chyb. V tomto bodě byste měli vrátit výjimku
Nebude se o tom hovořit. V některých případech je to žádoucí, ale v většině případů
místo toho byste měli tento problém odeslat na samostatnou záložku mimo
Sova. Nejjednodušší způsob, jak to udělat, je vytvořit odmítnutý slib s chybou
Jako důvod odmítnutí uvedla:

... kódový blok: JavaScript

import { Komponenta, naChybu } z "@odoo/owl";
klas MyComponent prodlouží třídu Component
setup() {
onError( (error) => {
          // implementation of this method is left as an exercise for the reader
tento.odstranitChybujícíPodkomponentu();
Promise.reject(chyba); // vytvořit odmítnutý slib bez jeho předání
        });
      }
    }

Toto způsobuje prohlížeč, který v okně zahájí událost „unhandledrejection“.
přivolá funkci pro zpracování chyb v rámci JavaScriptového frameworku.
většinou tím, že otevřou dialog s informacemi o chybě. To je strategie
, který je používán interně službou akce a dialogu k zastavení renderování
rozbité akce nebo dialogy, přestože stále hlásí chybu.

Handler v registru „error_handlers“
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Každý handler, který je přidán do registru error_handlers, může označit chybu jako
a může být chápáno dvěma způsoby.

První způsob je takový, že může zpracovatel vrátit hodnotu pravdivou. To znamená, že
handler zpracoval chybu a něco udělal, protože chyba je
obdržel odpovídající typ chyby, který je schopen zpracovat. Obvykle to znamená
Otevřel dialog nebo upozornění, aby uživatele varoval před chybou. To zabrání
chybu odvolá zpět do volání následujících handlerů s vyšším číslem pořadí.

Další možností je zavolat metodu preventDefault na události chyby: tato má jiný
smyslu. Po rozhodnutí, že je schopen s chybou zacházet, musí
zda chybu, kterou obdržel, je něco, co se může stát.
běžném provozu a pokud ano, měla by volat metodu preventDefault().
použitelné pro chyby v podnikání, jako jsou chyby přístupu nebo chyby ověření: uživatelé mohou
sdílet odkazy na zdroje, ke kterým nemají přístup.
se pokusit zachránit záznam, který je v neplatném stavu.

Pokud není volána funkce preventDefault(), je chyba považována za neočekávanou.
Pokud se něco stane během testu, test selže, protože je obvykle indikativní
chybného kódu.


Vyhýbejte se chybám co nejvíce
=========================================

Chyby se objevují na mnoha místech a zde jsou důvody, proč byste je měli řešit.
Nebuďte agresivní, nevyhazujte je.

Chyby jsou drahé
--------------------

Protože chyby musí odvíjet volací strom a shromažďovat informace při tom,
Vyhazování chyb je pomalé. Dále jsou obecně optimalizovány runtime JavaScriptu
s předpokladem, že výjimky jsou vzácné a tudíž je zpravidla sestavuje
kód s předpokladem, že nebude vyvolávat výjimky, a spadnout do pomalejšího kódu.
pokud se někdy stane.

Chyby při hodnocení ztěžují ladění
--------------------------------------

JavaScriptové debugger, jako je například ten zahrnutý v nástrojích pro vývojáře Chromu a Firefoxu.
měly mít funkci, která umožňuje přerušit provádění kódu při výjimce.
Může také zvolit, jestli se zastaví jen na zachycených výjimkách nebo i na nezachycených.
výjimky.

Když chybu vložíte do kódu, který volá Owl nebo JavaScript
rámci (např. pole, pohled, akce, komponenta, ...) protože řídí
Zdroje, které potřebují chytit chyby a prohlížet je, aby se rozhodli, zda chyba
je kritický a aplikace by měla spadnout, nebo pokud chyba je očekávaná a má
musí být zacházeno určitým způsobem.

Proto většina chyb, které jsou vyhozeny uvnitř kódu JavaScriptu
byli někdy chyceni a i když se mohou vrátit do vody,
Takže používání funkce „zastavit na nevyvolané výjimky“ je v podstatě k ničemu.
Při práci v Odoo se vždycky zastaví v rámci JavaScriptu.
kód, místo kódu, který původně vyvolal chybu.

„Přerušení na chyby zachycené v rámci programu“ je však stále velmi užitečné, protože
přerušuje provádění na každém výjimce a odmítnuté slibu. To umožňuje
vývojář zastavit a zkontrolovat kontext provádění, když dojde k výjimce
situace nastane.

Pokud však výjimky hodně chybí, pak je tento postup správný.
jsou vyhozeny běžně a jakákoliv akce na stránce může způsobit zastavení spouštění.
a vývojář by mohl muset projít mnoho „běžných“ výjimek, než
Dokáží se dostat k skutečné výjimečné situaci, o které mají zájem. V některých případech
Když kliknete na tlačítko přehrávání v ladiči, odstraní se soustředění z webové stránky.
i znepřístupnit zajímavou hodovou situaci bez použití klávesové zkratky
pro obnovení provádění, které vede k špatné zkušenosti vývojáře.


Přerušení narušuje normální průběh kódu
-------------------------------------------

Při chybě může být kód, který by měl vždy běžet, přeskočen.
Může způsobit mnoho jemných chyb a úniků paměti. Příklad:

... kódový blok: JavaScript

eventTarget.addEventListener(„event“, handler);
nějakáFunkce();
eventTarget.removeEventListener("event", handler);

V tomto bloku kódu přidáme posluchače události na cílovou událost, pak zavoláme funkci.
která může odeslat událost na cílový objekt. Po volání funkce odstraníme událost
posluchač.

Pokud funkce „someFunction“ vyhodí výjimku, událostní posluchač nikdy nebude odstraněn. To znamená, že
Paměť spojená s tímto událostním zpracovatelem je v podstatě uvolněna a nikdy nebude
pokud se samotný událostní cíl nevyčistí.

Kromě toho, že se paměť uvolnila, to znamená, že může být
volání události, která se spouští pro důvody jiné než volání funkce „someFunction“.
Jedná se o chybu.

Proto je nutné volání obalit do bloku try a uklízení do bloku finally.
Blok „konečně“:

... kódový blok: JavaScript

eventTarget.addEventListener(„event“, handler);
try {
nějakáFunkce();
} nakonec {
eventTarget.removeEventListener("event", handler);
    }

Ačkoliv tímto se vyhnete problémům uvedeným výše, kromě toho je potřeba více kódu.
Pokud je funkce nebezpečná, znamená to také, že může vyvolat výjimku. To by bylo nepřekonatelné, pokud byste ji obalili
všechny kódy, které mohou vyvolat výjimku v bloku try/finally.

Chyby zachycovat
===============

Někdy je potřeba volat do kódu, který známý chyby hází a chcete
Řešit některé z těchto chyb. Dva důležité věci, na které je potřeba pamatovat:

- Vyhoďte chyby, které nejsou typem chyb, které očekáváte.
a kontrolu instance
- Zkuste mít blok pokusu co nejmenší. To zabrání chybám, které nejsou
ten, který se snažíte chytit. Obvykle by měl blok try obsahovat přesně
Jediný výrok.

... kódový blok: JavaScript

proměnná nějakáHodnota;
try {
nějakáHodnota = nějakáFunkce();
      // do not start working with someVal here.
} catch (e) {
pokud (!(e je instancí třídy MyError)),
vyhodit e;
      }
nějakéVal = null;
    }
    // start working with someVal here

Při použití try/catch je to jednoduché, ale snadno se můžete nechtěně zabalit.
větší část kódu v případě, kdy pracujete s Promise.catch

... kódový blok: JavaScript

then(someFunction() => (someVal) => {
      // work with someVal
}));
pokud (!(e je instancí třídy MyError)),
vyhodit e;
      }
vrátí nula.
    });

V tomto příkladu je blok chyb skutečně zachytáváním všech chyb v celém tehdejším
blok, což není to, co chceme. V tomto konkrétním případě proto, že jsme se
filtrem podle typu chyby, necháváme si chybu pro sebe, ale můžete vidět
že je mnohem snazší tak učinit, pokud očekáváme jediný typ chyby a rozhodneme
Nebylo by nutné provádět kontrolu instance. Pozor však na rozdíl od předchozího příkladu
null nemůže projít cestou kódu, která používá nějaký proměnný.
chytací podmínky by měly být co nejblíže tomu, že mohou hodit.
A měla by se vždy filtrovat podle typu chyby.

Chybovou kontrolu průběhu programu
=======================

Pro důvody uvedené výše byste se měli vyvarovat chyb při provádění rutinních úkonů.
věci, a zejména pro řízení proudu. Pokud se očekává, že funkce bude nefunkční
aby plnila svou práci v pravidelných intervalech, měla by komunikovat neúspěchy bez
hazardovat výjimkou. Pojďme se podívat na příklad kódu:

... kódový blok: JavaScript

proměnná nějakáHodnota;
try {
nějakáHodnota = nějakáFunkce();
} catch (e) {
pokud (!(e je instancí třídy MyError)),
vyhodit e;
      }
nějakéVal = null;
    }

Kód má mnoho problémů. První je ten, že chceme
Proměnná someVal musí být přístupná po bloku try/catch, aby mohla
a nemůže být konstantní, protože potřebuje přiřazení.
po inicializaci. To ztěžuje čtení později, protože nyní máte
dát si pozor na možnost přidělení této proměnné později v kódu.

Druhým krokem je zjištění, že chyba je skutečně tímto typem.
chyby, kterou jsme očekávali zachytit, a pokud ne, vrátíme chybu zpět. Pokud ne
Takže se můžeme dostat do situace, kdy spolkne chyby, které byly ve skutečnosti neočekávané.
správně je hlásit, například bychom mohli chytit a spolknout chybu TypeError, pokud
podkód se pokouší přistupovat k vlastnosti na „null“ nebo „undefined“.

Nakonec je to velmi složité a snadno se může stát, že uděláte chybu: pokud
Pokud zapomenete přidat „try/catch“, pravděpodobně skončíte s výjimkou. Pokud přidáte
„try/catch“ blok, ale zapomněli na překvapivé chyby, které se snažíte zahltit.
nepříbuzné chyby. A pokud se chcete vyhnout přidělování proměnné, můžete
Přesunout celý blok kódu, který používá proměnnou dovnitř bloku try. Čím více
Čím více máte v bloku try, tím pravděpodobněji chytíte nezpůsobené chyby.
a spolknout je, pokud jste zapomněli filtrovat podle typu chyby. Dále také přidává odsazení
celý blok a můžete dokonce skončit s vícenásobnými „try/catch“ bloky.
Konečně, je obtížné určit, která z těchto linií se skutečně očekává, že bude hodit.
chyba.

Následující části popisují některé alternativní přístupy, které můžete použít místo
s chybami.

Vrátit hodnotu null nebo nevyjádřenou
----------------------------

Pokud funkce vrací primitiv nebo objekt, můžete obecně použít „null“ nebo
„nepřesně definované“ pro vyjádření, že nemohlo splnit svůj účel. To je vše
většině případů. Kód nakonec vypadá nějak takto:

... kódový blok: JavaScript

const nějakáHodnota = nějakáFunkce();
    // further
if (someVal není null) { /* udělej něco */ }

Jak vidíte, je to mnohem jednodušší.

Vrátit objekt nebo pole
-------------------------

V některých případech je hodnota null nebo undefined součástí očekávaného výstupu.
V těchto případech můžete místo toho vracet objekt s obalem nebo dvoučlenný pole.
obsahuje buď návratovou hodnotu nebo chybu:

... kódový blok: JavaScript

const { val: nějakáHodnota, err } = nějakáFunkce();
pokud (err) {
vrátí se zpět.
    }
    // do something with someVal as it is known to be valid

Anebo s pole:

... kódový blok: JavaScript

const [chyba, nějakáHodnota] = nějakáFunkce();
pokud (err) {
vrátí se zpět.
    }
    // do something with someVal as it is known to be valid

.. poznámka::

Při použití dvoučlenného pole je vhodné mít chybu jako první
element, aby bylo těžší ho přehlédnout náhodou při deklarování proměnných.
musíte explicitně přidat místo nebo čárku, abyste se vyhnuli chybě.
chyba je druhým prvkem, takže snadno můžeme jen dekonstruovat první.
elementu a přehlédne chybu.

Kdy chyby hodit
====================

Předchozí části nabízely mnoho dobrých důvodů pro vyhýbání se chybám. Co tedy
Příklady případů, kdy je nejlepší chybu vyhodit?

- Obecné chyby, které se mohou stát na mnoha místech, ale měly by být řešeny stejně všude.
Příkladem je např. chyba přístupu, která se může stát na jakémkoliv RPC a vždy bychom chtěli zobrazit
informace o tom, proč uživatel nemá přístup.
- Nějaká podmínka, která by měla být vždy splněna pro nějakou operaci, není splněna;
např. zobrazení není možné, protože doména je neplatná. Tyto typy chyby
Tyto chyby se obvykle neočekávají a ukazují na nesprávný kód.
nebo se datová struktura poškodí. Vyhozením dojde k tomu, že systém selže a zabrání tak dalšímu použití
jejichž provoz je v rozbitém stavu.
- Při procházení hluboké datové struktury v cyklu může být chyba mnohem
ergonomičtější a méně chybovou než manuální kontrola chyb a jejich odeslání
jejich procházením mnoha úrovněmi hovorů. To by mělo být v praxi velmi vzácné a
To je nutné vzít v úvahu při všech výhodách, které jsou zmíněny v tomto článku.
