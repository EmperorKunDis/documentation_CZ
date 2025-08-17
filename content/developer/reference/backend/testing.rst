..._odkaz/testování:

============
Testování Odoo
============

Existuje mnoho způsobů, jak otestovat aplikaci. V Odoo máme tři druhy
testy

- Jednotkové testy v Pythonu (viz Testování kódu v Pythonu): užitečné pro testování logiky obchodního modelu
- Jednotky testů v Javě (viz Testování kódu v Javě: užitečné pro testování javascriptového kódu v izolaci
- Toury (viz „Testování integrace“): tour simulují skutečnou situaci. Zajišťují, že
Python a části v JavaScriptu se navzájem správně domluví.

..._testování/python:

Testování kódu v Pythonu
===================

Odoo poskytuje podporu pro testování modulů pomocí knihovny „Python Testing Library“
<https://docs.python.org/3/library/unittest.html>.

Abychom mohli napsat testy, musíme definovat podbalík „tests“ v našem modulu.
automaticky kontrolovány na přítomnost testovacích modulů. Tyto moduly by měly mít jméno
začínající „test_“ a importované z „tests/__init__.py“.
např.

... blok kódu:: text

vaše_modul
    ├── ...
├── testy
|    └──__init__.py
|    └── test_bar.py
└───test_foo.py

a soubor „__init__.py“ obsahuje:

od importu test_foo, test_bar

.. varování:

testovací moduly, které nejsou importovány z „tests/__init__.py“, nebudou
běžet

Testovací běžec jednoduše spustí každý testový případ, jak je popsán v oficiálních
Dokumentace k unittestům, ale Odoo nabízí řadu nástrojů a pomocníků
týkající se testování obsahu Odoo (moduly, hlavně):

... třída: odoo.tests.TransactionCase
:členové: prohlížení odkazů, odkaz

... třída: odoo.tests.SingleTransactionCase
:členové: prohlížení odkazů, odkaz

... autoClass: odoo.tests.httpcase
:členové: procházet odkaz, odkaz, otevřít prohlížeč, JavaScript

...autofunkce: odoo.tests.tagged

Výchozí nastavení testů je jednou po tom, co odpovídající modul.
nainstalovány. Případně lze testy nastavit tak, aby se spouštěly po instalaci všech modulů
byl nainstalován a nebyl spuštěn hned po instalaci modulu::

  # kódování: UTF-8
od odoo.tests import HttpCase, tagged

  # Tento test by měl být proveden až po instalaci všech modulů.
@tagged('-at_install', 'post_install')
třída WebSiteVisitorTest(HttpCase):
def test_vytvoření návštěvníka na sledované stránce (self):
stránka = self.env['webová stránka']

Nejčastější situace je použití
:třída ~odoo.tests.TransactionCase a otestovat vlastnost modelu
v každém z metod:

class TestModelA(TransakčníPřípad):
def test_nějaká_akce(self):
record = self.env['model.a'].create({'pole': 'hodnota'})
record.some_action()
self.assertEqual(
pole záznamu
očekávané hodnoty pole

        # další testy...

.. poznámka::

Testovací metody musí začínat „test_“

... třída: odoo.tests.Form
:členové:

... autoklasifikace: odoo.tests.M2MProxy
:členové: přidat, odebrat, vymazat

... autoklasifikace: odoo.tests.O2MProxy
:členové: nový, upravit, odstranit

Testování
-------------

Testy se automaticky spouštějí při instalaci nebo aktualizaci modulů, pokud
Možnost `--test-enable <odoo-bin --test-enable>‘ byla zapnuta při spuštění
Odoo server.

... dokumentace k unittestu: https://docs.python.org/3/library/unittest.html

.._vývojář/odkaz/testování/vybrané:

Výběr testů
--------------

V Odoo lze testy v Pythonu označit pro usnadnění výběru testů při
testování.

Podtřídy tříd :class:`odoo.tests.BaseCase` (obvykle prostřednictvím
:třída:~odoo.tests.TransactionCase
Testy (např. třída odoo.tests.HttpCase) jsou automaticky označeny
„standard“ a „při instalaci“.

Zároveň je nutné vyzvat k účasti na této akci všechny obyvatele města.
~~~~~~~~~~

Možnost `--test-tags <odoo-bin --test-tags>´ může být použita k výběru/filtraci testů.
bude běžet na příkazovém řádku. Implikuje: možnost `--test-enable <odoo-bin --test-enable>`.
takže není nutné specifikovat:
Při použití příkazu:

Toto nastavení je výchozím na „+standard“ znamenající, že testy označené jako „standard“
(výslovně nebo implicitně) bude spouštěn při startu Odoa
s možností `--test-enable <odoo-bin --test-enable>`.

Při psaní testů lze použít dekorátor :func:`~odoo.tests.tagged`.
používané na testovacích třídách k přidávání nebo odebírání štítků.

Argumenty dekorátora jsou názvy štítků, jako řetězce.

... nebezpečí: funkce ~odoo.tests.tagged je dekorátor třídy, nemá žádné
na funkce nebo metody

Štítky lze předcházet znaménkem „-“ (předponou), aby se odstranily místo
přidat nebo vybrat je například pokud nechcete, aby váš test byl proveden
Výchozí nastavení můžete odstranit pomocí „standardního“ štítku.

... kódový blok:: python

importujeme testovací případ transakce z odoo.tests, tagged

@tagged('-standard', 'pěkný')
class NiceTest(Transakce):
        ...

Tento test se nebude spouštět automaticky. Pro jeho spuštění je nutné zadat příslušný tag
musí být zvolen explicitně:

.. kódový blok: konzole

$ odoo-bin --test-tags nice

Poznámka: Testy označené „nice“ budou spuštěny.
*obě* „pěkné“ a „standardní“ testy poskytují více hodnot
:parametr: `--test-tags <odoo-bin --test-tags>`: hodnoty
je *sčítací* (vybíráte všechny testy s *kterýmkoliv* z uvedených štítků).

.. kódový blok: konzole

$ odoo-bin --test-tags nice,standard

Konfigurační přepínač také přijímá předpony „+“ a „-“.
„+“ je implicitní a tedy zcela volitelný. „-“ („mínus“)
předpona je použita k deaktivaci testů označených předponou, i když
jsou vybrány pomocí ostatních specifikovaných značek, například pokud existují „standardní“ testy
jsou také označeny jako „pomalé“ můžete spustit všechny standardní testy *kromě* pomalých
jednotlivci:

.. kódový blok: konzole

$ odoo-bin --test-tags 'standard,-slow'

Když píšete test, který nezdědil od
:třída:~odoo.tests.BaseCase, tento test nebude mít výchozí tagy
musíte je explicitně přidat, aby se test zahrnul do výchozích testů
součástí. To je běžný problém při použití jednoduché třídy „unittest.TestCase“
nebudou se bát, že je někdo přejede:

... kódový blok:: python

import unittest
od odoo.tests import tagged

@tagged('standard', 'při instalaci')
třída SmallTest(testcase.TestCase):
        ...

Kromě značek můžete také specifikovat konkrétní moduly, třídy nebo funkce.
Testovací příkaz. Plná syntaxe formátu přijímaného pomocí příkazu :option:`--test-tags <odoo-bin --test-tags>`.
Je:

... blok kódu:: text

[-][tag][/modul]:[class].[metoda]

Pokud chcete otestovat modul „účetní zásoby“, můžete použít:



$ odoo-bin --test-tags /stock_account

Pokud chcete otestovat konkrétní funkci s unikátním názvem, lze ji specifikovat
přímo:



$ odoo-bin --test-tags .test_dodavatelská faktura předána uživatelem interním uživatelem bez dodavatele

Toto je ekvivalentem



$ odoo-bin --test-tags /account:TestAccountIncomingSupplierInvoice.test_supplier_invoice_forwarded_by_internal_user_without_supplier

Pokud je název testu jednoznačný. Několik modulů, tříd a funkcí
Mohou být specifikovány najednou oddělené čárkou jako u běžných značek.

.._odkaz/testování/tagy:

Speciální tagy
~~~~~~~~~~~~

- „Standard“: Všechny testy Odoo, které dědí od
:třída:~odoo.tests.BaseCase je implicitně označena jako standardní.
:volba `--test-tags <odoo-bin --test-tags>“ také výchozí hodnotu „standard“.

To znamená, že neoznačené testy budou prováděny automaticky při zapnutých testech.
- „at_install“: znamená, že se test provede ihned po instalaci modulu
instalace a před instalací ostatních modulů. To je výchozí stav.
implicitní značka.
- „post_install“ znamená, že test bude proveden po instalaci všech modulů
Výchozí hodnotou je instalace těchto modulů, což je většinou to, co chcete pro testy HttpCase.

Pozor, že toto není výhradně s „at_install“, ale od té doby, co jste
Obecně se nebude chtít ani „post_install“ a většinou je spárováno s
„-at_install“ při označování třídy testu.

Příklady
~~~~~~~~

.. důležité:

Testy budou prováděny pouze v nainstalovaných modulech. Pokud začínáte od
Pokud chcete mít čistou databázi, budete muset nainstalovat moduly s
:volba: `-i odoo-bin -i` alespoň jednou. Poté už není možné
Pokud není nutné aktualizovat modul, pak není třeba
:volba `-u <odoo-bin -u>`, pro jednoduchost lze použít
není uvedeno v příkladech níže.

Spouštět pouze testy z prodejního modulu:

.. kódový blok: konzole

$ odoo-bin --test-tags /sale

Spusťte testy z prodejního modulu, ale ne ty označené jako pomalé:

.. kódový blok: konzole

$ odoo-bin --test-tags '/prodej, -pomalé'

Spouštět pouze testy z výchozího nebo označeného jako pomalý:

.. kódový blok: konzole

$ odoo-bin --test-tags '-standard, pomalý, sklad'

.. poznámka: „-standard“ je implicitní (není vyžadován) a přítomen pro jasnost

Testování kódu v Javě
===============

Testování složitého systému je důležitým opatřením k zabránění regresí a
zaručit, že některé základní funkce stále fungují. Protože Odoo má nezanedbatelný
kódové základny v JavaScriptu je nutné ho otestovat. V této části se podíváme na
diskutovat o praxi testování kódu v izolaci: tyto testy zůstávají
prohlížeč a nemají se dostat na server.

.. odkaz/testování/QUnit:

Testovací sada Quit
----------------

Rámec Odoo používá knihovnu pro testování QUnit jako běžný tester.
QUnit definuje pojmy testů a modulů (sada souvisejících testů).
a poskytuje nám webovou aplikaci, která umožňuje spouštět testy.

Třeba takhle může vypadat test pyUtils:

... kódový blok: JavaScript

QUnit.module("py_utils");

QUnit.test('jednoduchá aritmetika', funkce assert() {
očekávat 2;

var výsledek = pyUtils.py_eval("1 + 2");
assert.strictEqual(výsledek, 3, „měl by správně vyhodnotit součet“);
výsledek = pyUtils.py_eval ("42 % 5");
assert.strictEqual(výsledek, 2, „by měl správně vyhodnotit operátor modulo“);
    });

Hlavní způsob, jak spustit testovací sadu, je mít běžící server Odoo, pak
navigovat prohlížeč na „/web/tests“. Pak se spustí testovací sada.
prohlížečem Javascriptu.

.. obrázek: testování/testy.png


Webová uživatelská rozhraní má mnoho užitečných funkcí: může běžet jen některé podmoduly nebo
filtruje testy, které odpovídají řetězci. Může zobrazit všechny příkazy, úspěšné nebo neúspěšné.
opakovat konkrétní testy...

.. varování:

Zatímco se testovací sada spouští, ujistěte se, že:

    - Váš prohlížeč je v popředí.
    - nemá přiblížení nebo oddálení. Musí mít přesně 100% zvětšení.

Pokud tomu tak není, některé testy selžou bez vysvětlení.

Testovací infrastruktura
----------------------

Níže je stručný přehled nejdůležitějších částí testování.
infrastruktura:

- Existuje balíček aktiv s názvem „web.qunit_suite“. Tento balíček obsahuje
hlavní kód (aktiva společná + aktiva back-endu), některé knihovny a testovací sadu QUnit
runner a níže uvedené testovací balíčky.

- balíček s názvem „web.tests_assets“ zahrnuje většinu aktiv a užitečných programů, které jsou potřebné
testovacími sestavami: vlastními asertivy QUnitu, pomocnými funkcemi pro testování, např. načítáním aktiv požadovaných při testování atd.

- další balíček aktiv, `web.qunit_suite_tests`, obsahuje všechny skripty testů.
To je obvykle místo, kde se přidávají testovací soubory do sady.

- existuje „kontroler“ v webu, který je přiřazen ke všem cestám */web/test*
jen prostě vykreslí šablonu *web.qunit_suite*.

- k provedení testů stačí pouze nasměrovat prohlížeč na cestu */web/tests*.
V takovém případě si prohlížeč stáhne všechny aktiva a QUnit se o ně postará.

- V souboru „qunit_config.js“ je nějaký kód, který v konzole zobrazuje
informace o tom, zda test prošel nebo neprošel.

- chceme, aby robot také běžel tyto testy, takže je v souboru `test_js.py`
který prostě spustí prohlížeč a ukazuje mu adresu URL web/tests. Poznámka:
metoda browser_js spouští hlavní instanci prohlížeče Chrome bez grafického rozhraní.


Modulárnost a testování
----------------------

Společnost Odoo navrhuje své produkty tak, aby každá aplikace mohla měnit chování ostatních částí.
systému. Například doplněk *voip* může upravit widget *FieldPhone*.
používat další funkce. To není vlastně dobré z pohledu
testovací systém, protože to znamená, že test v doplňkové části webu se pokaždé nezdaří.
VoIP doplněk je nainstalován (poznámka: RunBot spouští testy s veškerými doplňky
nainstalovány.

Na druhou stranu je naše testovací systém dobrý, protože dokáže detekovat každou nákazu.
Další modul narušuje některé klíčové funkce. Neexistuje žádné kompletní řešení
Tento problém. Prozatím řešíme tento případ po jednom.

Obvykle není dobrý nápad měnit nějaké jiné chování. Pro naše VoIP
Příkladem je určitě čistší přidání nového widgetu *FieldVOIPPhone*.
upravit pár pohledů, které potřebují. Tímto způsobem je widget *FieldPhone*
a obě lze otestovat.

Přidání nového případu
----------------------

Předpokládejme, že udržujeme doplněk *my_addon* a
chceme přidat test pro nějaký javascriptový kód (například nějakou užitečnou funkci
myFunction, která se nachází v adresáři *.my_addon.utils*. Pro přidání nového testovacího případu je třeba
tohoto:

1. Vytvořte nový soubor *my_addon/static/tests/utils_tests.js*. Tento soubor obsahuje základní kód, který
přidat modul QUnit my_addon do složky utils.

... kódový blok :: JavaScript

odoo.define('my_addon.utils_tests', funkce (vyžadovat),
„použijte přísný režim“;

var utils = require('my_addon.utils');

QUnit.module("můj doplněk", {}, funkce () {

QUnit.module('utils');

        });
        });


2. V souboru *my_addon/assets.xml* přidejte soubor do hlavních testovacích aktiv:

... kódový blok :: XML


<odoo>
<šablona id="testy my addonu" jméno="můj doplněk testy" dědí_id="web.qunit_suite_tests">
<script expr="//script[poslední()]" pozice="po ní"

</xpath>
</vzorec>


3. Restartujte server a aktualizujte soubor my_addon, nebo to udělejte z rozhraní (pro
(zajistit, aby se nový soubor testů načetl).

4. Přidejte testovací případ po definici podtestu utils:

... kódový blok :: JavaScript

QUnit.test("nějaký testovací případ, který chceme otestovat", funkce (přesvědčit se)
očekávat(1);

var výsledek = funkce.myFunction(nějaký argument);
přesvědčit se, že výsledek je stejný jako očekávaný výsledek;
        });

5. Navštivte adresu */web/tests/*, abyste se ujistili, že je test spuštěn

Funkce pomocníků a speciální kontroly
-------------------------------------------

Bez pomoci je těžké otestovat některé části Odoa. Zejména
Viditelné jsou trochu problémové, protože komunikují s serverem a mohou provádět mnoho
rpcs, které je třeba zesměšnit. Proto jsme vyvinuli nějaké speciální
funkce pomocného programu, které se nacházejí v souboru `test_utils.js`.

- Funkce pro simulaci testu: tyto funkce pomáhají nastavit prostředí pro testování.
nejdůležitějším použitím je napodobování odpovědí poskytovaných serverem Odoo.
Funkce používá „falešný server“_. Jedná se o třídu v JavaScriptu, která simuluje
odpovědi na nejčastější metody modelu: číst, hledat_číst, získat_jméno, ...

- DOM pomocníci: užitečné k simulaci událostí/akcí na nějakém konkrétním cíli.
Příkladem je funkce testUtils.dom.click, která klikne na cíl. Pozor, že
bezpečnější než ruční provedení, protože také kontroluje, zda cíl existuje.
a je viditelná.

- Vytvořit pomocníky: jsou nejspíš nejužitečnější funkce, které se exportují
„test_utils.js“. Tyto pomůcky jsou užitečné při vytváření widgetu s falešným
přírodě, a také spoustu drobných detailů, které by měly co nejvíce napodobit
reálných podmínkách. Nejdůležitější je určitě metoda createView_.

- „Přizpůsobené tvrzení“: QUnit lze rozšířit o speciální tvrzení.
Odoo, často testujeme některé vlastnosti DOMu. Proto jsme udělali nějaké
Pomocí těchto tvrzení lze například zjistit, že funkce *containsOnce* vyhodnotí
a widget/jQuery/HTML prvek a selektor, pak se podívá na cíl
přesně jeden zápas pro CSS selektor.

Třeba takhle by mohl vypadat jednoduchý test s vyplněnými formuláři:

... kódový blok: JavaScript

QUnit.test('jednoduché zobrazení skupiny', funkce assert() {
očekávat(1);

var form = testUtils.createView({
Výhled: FormView
model: 'partner',
datum: tento.datum,
arch: 'Formulář pro partnery:'
'</group>
"<field name='foo'/>"
'</skupina>' +
'</form>'
id: 1
        });

assert.containsOnce(formulář, 'table.o_inner_group');

form.Destroy();
    });

Zaměřte se na použití metody createView a funkce containsOnce
Přesvědčení. Dále byl v závěru správně zničen formulářový kontroler.
test.

Nejlepší postupy
--------------

Není důležité, v jakém pořadí:

- všechny testovací soubory by měly být přidány do složky *some_addon/static/tests/*
- pro opravy chyb se ujistěte, že test neprojde bez opravy a projde s ní.
To zajišťuje, že opravdu funguje.
- snažte se mít co nejmenší kód potřebný pro funkci testu.
- Obvykle jsou lepší dva menší testy než jeden velký.
Je snadnější pochopit a opravit.
- Vždy po skončení testu proveďte úklid. Například pokud váš test vytváří widget,
Mělo by ho zničit na konci.
- nemusíte mít plnou a kompletní pokrytí kódu. Ale přidání několika testů pomáhá
hromada: zajišťuje, aby váš kód nebyl úplně zničený, a kdykoli se objeví
Když je chyba opravena, je skutečně mnohem snazší přidat nový test do stávajícího testovacího balíku.
- Pokud chcete zkontrolovat nějakou negativní tvrzení (například že HtmlElement
Pokud tato metoda nefunguje (pokud element nemá specifickou CSS třídu), pak zkuste přidat pozitivní výrok.
stejný test (například provedením akce, která mění stav).
Pomůže se vyhnout zkoušce, která v budoucnu může vést k smrti (například pokud je CSS
Když se třída mění (např. z 1 na 2).

Tipy
----

- pouze jedním testem: můžete (dočasně!) změnit *QUnit.test(...)*
definici do *QUnit.only(...)*, což je užitečné pro zajištění toho, aby QUnit
pouze tento konkrétní test.
- debugovací vlajka: většina funkcí pro tvorbu nástrojů má režim ladění (zapnutý
debug: true parametr). V takovém případě bude cílový widget umístěn v DOM.
místo skrytého svítidla s konkrétním typem žárovky a více informací.
protokoly. Například všechny simulované komunikace sítě budou k dispozici v
Konzole.
- Při práci na nefunkčním testu je běžné přidat vlajku pro ladění, pak
komentář konec testu (zejména destruktor). S tímto
je možné vidět stav widgetu přímo a ještě lépe ho upravovat.
manipulovat s widgetem kliknutím nebo interakcí s ním.

..._odkaz/testování/integrační testování:

Testování integrace
===================

Testování Pythonového kódu a JavaScriptového kódu samostatně je velmi užitečné, ale neprokazuje, že webový klient
a server spolupracují. Chceme-li toho dosáhnout, můžeme napsat jiný druh testu: túry.
Turné je malou scénkou zajímavého obchodního toku. Vysvětluje sekvence kroků,
je třeba dodržet. Testovací spouštěč poté vytvoří virtuální prohlížeč PhantomJs, který se připojí na správnou
URL a simulovat kliknutí a vstupy podle scénáře.

Napsání testovacího turné
-------------------

Struktura
~~~~~~~~~

Pro psaní testovacího turné pro modul „your_module“ začněte vytvořením potřebných souborů:

... blok kódu:: text

vaše_modul
    ├── ...
└── statické
|    └── testy
|        └──toury
|            └── vaše_turistika.js
├── testy
|    └──__init__.py
|    └── test_volani_na_exkurzi.py
└── __manifest__.py

Poté můžete:

- Aktualizujte soubor __manifest__.py, aby se do složky assets přidal soubor your_tour.js.

... kódový blok:: python

"aktiva": {
'web.assets_tests': [
'your_module/static/tests/tours/your_tour.js',
         ],
     },

- aktualizujte soubor „__init__.py“ v adresáři „tests“, aby se do něj importoval soubor „test_calling_the_tour“.

.. viz též:
   - :ref:`Soubor aktiv <reference/assets_bundle>`
   - :ref:`testování/python`

..._testování/javascript/test:

Javascript
~~~~~~~~~~

#Nastavte si svou cestu registrací.

... kódový blok::javascript

importovat turistický zájezd z web_tour.tour;
tour.register('pronajem_produktu_konfigurátor_tour', {
url: '/web',  // Zde můžete specifikovat jakýkoliv jiný startovací URL
      }, [
          // Your sequence of steps
      ]);

#Přidejte krok, který chcete.

Každý krok obsahuje alespoň jeden spouštěč. Můžete buď použít předdefinované kroky
<{GITHUB_PATH}/addons/web_tour/static/src/tour_service/tour_utils.js#L426> nebo napište svůj vlastní
krok.

Níže jsou uvedeny příklady kroků:

Příklad:

... kódový blok::javascript

      // First step
showAppsMenuItem()
      // Second step
      {
spouštěč: '.o_app[data-menu-xmlid="Váš modul.Pokud ano, pak kořenový prvek menu vašeho modulu"]',
jeAktivní: 'komunita', // Volitelné
běh: "kliknout"
      }, {
          // Third step
      },

Příklad:

... kódový blok::javascript

      {
spouštěč: '.js_product:has(strong:contains(Kryt podlahy)) .js_add',
běh: "kliknout"
      },

Příklad:

... kódový blok::javascript

      {
jeAktivní: ["mobilní", "podnikový"]
obsah: „Klikněte na Přidat odkaz na produkt“,
spouštěč: 'a:obsahuje("Přidat produkt")',
pozice nástrojového tipu: „doleva“,
async run(pomocníci) { //Stejné jako run: "kliknout"
pomocníci.kliknout();
          }
      },

Tady jsou některé možné argumenty pro vaše osobní kroky:

- **spouštěč**: Povinný parametr, vybraný prvek nebo selektor, který bude akci spustit.
čekat, až se prvek objeví a zobrazí, než spustíte
akce na něm.
- **akce**: Volitelná akce prováděná na prvku *spouštěč*. Pokud žádná „akce“,
bez akce.

Akce může být:

  - Funkce, která je asynchronní a provádí se s „Tipem“ spouštěče.
kontext („to“) a akční pomocníky jako parametr.
  - Jméno jednoho z pomocníků akce, který bude v
element spouštěče:

... první třídy: o definice seznamu

„kontrola“
Zajišťuje, že se vždy zkontroluje prvek **spouštěč**. Tento pomocník je určen
pouze pro elementy typu checkbox.
„jasné“
Odstraňuje hodnotu prvku **spouštěče**. Tento pomocník je
určené pouze pro elementy typu <input> nebo <textarea>.
„klikněte“
Klikne na prvku spouštěče a provede všechny potřebné kroky.
události.
„dvojklik“
Stejně jako „klik“ s dvěma opakováními.
:samp:`přetáhnout a pustit {cíl}`
Simuluje přetahování prvku **spouštěče** na „cíl“.
:samp:`edit {content}`
„Očistit“ prvky a poté „vyplnit“ obsah.
:samp:`editor {obsah}`
Zaměřte se na prvek „spoušť“ (WYSIWYG) a poté stiskněte „obsah“.
:samp:`obsah {content}`
Zaměřte se na prvky „spoušť“ a poté stiskněte „obsah“. Tento pomocník je
určené pouze pro elementy typu <input> nebo <textarea>.
„plovoucí“
Provádí sekvence nadzvednutí na prvku **spouštěči**.
:samp:`stisknout obsah“
Spouští sekvenci klávesových událostí.
:samp:`rozsah obsahu`
Zaměřte se na prvek **spouštěč** a nastavte hodnotu „obsah“. Tento pomocník je určen
pouze pro elementy typu range.
:samp:`select {value}`
Spouští sekvenci události výběru na prvku **spouštěč**. Vyberte možnost podle jejího
„hodnota“. Tento pomocník je určen pouze pro elementy typu „<select>“.
:samp:`selectByIndex {index}`
Stejně jako u „select“, ale vyberte možnost podle jejího „indexu“. Pozor, první volba má
index 0.
:samp:`vybrat podle štítku {label}`
Stejně jako u „select“, ale vyberte možnost podle jejího „labelu“.
„nezaškrtnout“
Zajišťuje, aby se v poli „spouštěč“ nezobrazovalo zaškrtávací pole. Tento pomocník je určen pro
pouze pro elementy typu checkbox.


- **jeAktivní**: Volitelné
Aktivuje krok pouze v případě, že jsou splněny všechny podmínky pole isActive.
  - Prohlížeč je ve stavu **desktopu** nebo **mobilního zařízení**.
  - Tur se týká buď **komunitní**, nebo **podnikové** edice.
  - Tour se spouští buď v režimu auto (runbot), nebo manuálně (onboarding).
- **nástrojovka**: Volitelné „nahoře“, „vpravo“, „dole“ nebo
„levé“. Jak se má nástrojová lišta vztahovat k cíli
při interaktivních prohlídkách.
- **obsah**: Volitelné, ale doporučené - obsah nástrojového tipu
interaktivní prohlídky, které jsou také zaznamenány do konzole a proto velmi užitečné.
sledovat a ladit automatické trasy.
- **timeout**: Jak dlouho čekat, než se krok „spustí“, v
milisekundy, 10000 (10 sekund).

.. důležité:

Poslední krok(y) turné by měly vždy vrátit klienta zpět do
„stabilní“ stav (např. žádné probíhající editace) a zajistit, aby
nežádoucí účinky (požadavky na síť) dokončily svůj běh, aby se předešlo závodu
podmínky nebo chyby při demontáži.

.. viz též:
   - „Dokumentace jQuery o funkci find <https://api.jquery.com/find/>“

Python
~~~~~~

Pro začátek turné z testu hada vytvořte třídu, která dědí od
:třída odoo.tests.HTTPCase a volání metody start_tour:

... kódový blok:: python

def test_your_test(self):
       # Volitelné nastavení
start_tour("/web", "vaše_turistická_jména", login="admin")
       # Volitelné ověření

Napsání průvodce pro nováčky
--------------------------

Struktura
~~~~~~~~~

Pokud chcete napsat onboarding tour pro modul „your_module“, začněte vytvořením potřebných souborů:

... blok kódu:: text

vaše_modul
    ├── ...
├── data
|  └── vaše_turistika.xml
├── statické/zdrojové/js/tours/vaše_turistická_stezka.js
└── __manifest__.py

Poté můžete aktualizovat soubor __manifest__.py, aby obsahoval soubor your_tour.js v části Assets a soubor your_tour.xml v části Data.

... kódový blok:: python

"data": [
"data/vase_tur.xml",
     ],
"aktiva": {
'web.assets_backend': [
'your_module/statické/zdrojové soubory/js/turistika/your_tour.js',
         ],
     },

Javascript
~~~~~~~~~~

JavaScriptová část je stejná jako u :ref:`testovacího turné <testing/javascript/test>`.

XML
~~~

Když máte svůj záznam v javascriptovém registru, můžete vytvořit záznam „web_tour.tour“ v XML takto:




<odoo>
<záznam id="vaše_cesta" typu "web_tour.tour">
<pole název="název">vašeho zájezdu</pole>
<pole název="pořadí">10</pole>
<položka name="rainbow_man_message">Gratulujeme, bylo to skvělé turné“
</záznam>
</odoo>

- „jméno“: povinné pole, jméno musí být stejné jako v
JavaScriptový registr.
- `sledovací číslo“: Volitelné; určuje pořadí, v jakém se mají provádět
onboardingové prohlídky. Výchozí hodnota je 1000.
- „url“ (volitelné): URL, odkud začít s prohlídkou. Pokud je „url“ nastaveno na hodnotu „False“,
vezměte si URL z registru. Výchozí hodnota je „/odoo“.
- „rainbow_man_message“: Volitelné; zobrazí vzkaz.
efekt duhy na konci turné. Pokud je „rainbow_man_message“ nastaveno na hodnotu „False“,
nejsou žádné efekty duhy. Výchozí hodnota je „Dobrá práce! Prošel jsi všemi kroky této prohlídky.“

Provozování prohlídek na palubě
~~~~~~~~~~~~~~~~~~~~~~~~

Všechny můžete spustit v pořadí, v jakém jsou uvedeny, pomocí přepínače „Nastavení“ v nabídce uživatele.
Můžete spustit konkrétní školicí turné přes:
a kliknutím na „Nástup“ nebo „Zkouška“.

- **Nástup nového zaměstnance**: bude provádět prohlídku interaktivně, což znamená, že prohlídka ukáže, jak postupovat.
čekat na interakci uživatele.
- **Testování**: spustí automaticky celý průchod. To znamená, že všechny kroky budou provedeny.
před uživatelem.

Turistický záznamník
~~~~~~~~~~~~~

Také snadno vytvoříte trasy s nahrávačem tras. Klikněte na:guilabel:`Nahrát trasu`.
nástroj pro pohled na proces přijetí nového zaměstnance. Tento nástroj zaznamená všechny vaše interakce v Odoo.

Vytvořené prohlídky jsou v přehledu nástupních prohlídek označeny jako **Vlastní**. Tyto prohlídky lze také
Exportovat do javascriptového souboru připraveného k umístění do vašeho modulu.

Tipy pro ladění
--------------

Sledování zkoušek v prohlížeči
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Existují tři způsoby s různými obchody:

„watch=True“
**************

Při spouštění testovacího balíčku lokálně s hodnotou „watch=True“
parametr lze přidat do „browser_js“ nebo „start_tour“.
volání:

self.start_tour(„/web“, „název vaší cesty“, sledovat = True)

Tím se automaticky otevře okno Chromu s prohlídkou.
běhat uvnitř ní.

**Výhody**
  - Vždy funguje, pokud má turnus Pythonovou instalaci nebo okolní kód, nebo více kroků.
  - je plně automatizovaný (jen vyberte test, který spustí prohlídku).
  - transakční (vždy by měly být spouštěny opakovaně)
Nevýhody
  - pouze lokálně
  - pouze v případě, že se test/turné může provozovat správně místně.

„debug=True“
**************

Při spouštění testovacího balíčku lokálně se „debug=True“
parametr lze přidat do „browser_js“ nebo „start_tour“.
volání:

self.start_tour(„/web“, „your_tour_name“, True)

To automaticky otevře celoobrazovkové okno prohlížeče Chrome s otevřenou
nástroje pro vývojáře a zarážka ladění v počátku turné.
Je spouštěn pomocí parametrů debug=assets. Pokud dojde k chybě,
debugger zastaví na výjimce.

**Výhody**
  - Stejné výhody jako režim „watch=True“
  - Jednodušší kroky ke sledování
Nevýhody
  - pouze lokálně
  - pouze v případě, že se test/turné může provozovat správně místně.

Spouštět přes prohlížeč
***************

Testovací cesty lze spustit také prostřednictvím rozhraní prohlížeče voláním

... kódový blok: JavaScript

odoo.startTour("tour_name");

v konzoli JavaScriptu nebo zapnutím režimu testů
<frontend/framework/tests_debug_mode> nastavením „?debug=tests“
URL.

**Výhody**
  - jednodušší na běhání
  - Může být použita na výrobních nebo testovacích místech, nejen lokálně.
  - umožňuje běh v režimu „Přivítání“ (manuální kroky).
Nevýhody
  - těžší k použití s testovacími cestami, které využívají nastavení Pythonu
  - nemusí fungovat vícekrát v závislosti na vedlejších účincích cestování

..tip:

Tento způsob můžete použít k pozorování nebo interakci s turistickými skupinami.
které vyžadují instalaci Pythonu:

   - před zahájením dané trasy přidejte *pythonovou* zastávku
(„start_tour“ nebo „browser_js“ volání).
   - když dojde k bodu přerušení, otevřete instanci v prohlížeči.
   - Provést prohlídku

V tomto bodě bude Pythonová konfigurace viditelná pro prohlížeč.
Turisté se mohou těšit na prohlídku.

Možná chcete komentovat volání „start_tour“ nebo „browser_js“.
pokud chcete, aby se testování později pokračovalo podle
příznaky turné.

Snímky obrazovky a záznamy běhu prohlížeče při testování
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Při spouštění testů pomocí příkazového řádku s použitím „HttpCase.browser_js“ se zobrazí
prohlížeč je spuštěn v režimu bez hlavy. Výchozí nastavení předpokládá, že pokud dojde k neúspěchu, bude pořízena obrazová snímka ve formátu PNG
pořízené v okamžiku selhání a napsané

.. kódový blok: konzole

'/tmp/odoo_tests/{db_name}/screenshots/'

Od verze 13.0 byly přidány dvě nové příkazové řádkové argumenty, které umožňují kontrolovat tento chování:
:option:`--snímky obrazovky <odoo-bin --screenshots>` a :option:`--nahrávání obrazovky <odoo-bin --screencasts>“

Kroky introspekce/ladění
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Při pokusu o opravu/ladění turnaje se obrázky (v případě neúspěchu)
nemusí být dostatečné. V takovém případě může být užitečné vidět
Co se děje na každém nebo některých krocích.

Při „onboardingu“ (tedy většinou) je to docela jednoduché.
spouštěné přímo uživatelem) je složitější, když běží
„testovací“ turné nebo při běhu turné přes testovací sadu.
Pokud jde o triky, existují dvě hlavní:

- Vlastnost „krok“ s hodnotou „true“, v režimu ladění (debug = True).

Toto přidá zarážku pro ladění kódu na začátku kroku.
Pak můžete přidat své vlastní, kdekoliv je potřeba.

**Výhody**
    - velmi jednoduché
    - turné pokračuje, jakmile začnete s výkonem trestu
Nevýhody
    - interakce s webovými stránkami je omezená, protože všechny skripty jsou zablokované.

- Vlastnost „krok“ s hodnotou „true“, v režimu ladění (debug = True).

Turisté se na konci schodů zastaví, což umožňuje kontrolu
a interagovat s ní, dokud se vývojář nebude připraven.
se může vrátit k typování **play();** v konzole prohlížeče.

**Výhody**
    - umožňuje interakci s webovou stránkou
    - Žádné zbytečné (pro tuto situaci) rozhraní pro ladění chyb.

- Krok s akcí „debugger“.

Toto lze přidat k existujícímu kroku nebo může být novým samostatným
krok. Jakmile je spuštěn **spoušť** kroku, provede se
zastavit všechny skripty v JavaScriptu.

**Výhody**
    - jednoduchý
    - turné pokračuje, jakmile začnete s výkonem trestu
Nevýhody
    - interakce s webovými stránkami je omezená, protože všechny skripty jsou zablokované.
    - Přerušení se spustí po pokusu o nalezení cíle.
definovaný v kroku.

Testování výkonu
===================

Počet dotazů
------------

Jedním ze způsobů, jak testovat výkon, je měřit dotazy na databázi. Ručně lze tento test provést pomocí
parametrem příkazového řádku `--log-sql`. Pokud chcete určit maximální počet dotazů pro operaci
Můžete použít metodu :meth:`~odoo.tests.BaseCase.assertQueryCount`, která je integrována do tříd testů v Odoo.

... kódový blok:: python

s sebou.assertQueryCount(11):
do_něco()

.. _qunit: https://qunitjs.com/
... _qunit_config.js: https://github.com/odoo/odoo/blob/51ee0c3cb59810449a60dae0b086b49b1ed6f946/addons/web/static/tests/helpers/qunit_config.js#L49
.. _testovací aktiva: https://github.com/odoo/odoo/blob/51ee0c3cb59810449a60dae0b086b49b1ed6f946/addons/web/views/webclient_templates.xml#L594
.. _sada qunit: https://github.com/odoo/odoo/blob/51ee0c3cb59810449a60dae0b086b49b1ed6f946/addons/web/views/webclient_templates.xml#L660
.. _testovací sada qunit: https://github.com/odoo/odoo/blob/51ee0c3cb59810449a60dae0b086b49b1ed6f946/addons/web/views/webclient_templates.xml#L680
... _controller: https://github.com/odoo/odoo/blob/51ee0c3cb59810449a60dae0b086b49b1ed6f946/addons/web/controllers/main.py#L637
... _test_js.py: https://github.com/odoo/odoo/blob/51ee0c3cb59810449a60dae0b086b49b1ed6f946/addons/web/tests/test_js.py#L13
... _test_utils.js: https://github.com/odoo/odoo/blob/51ee0c3cb59810449a60dae0b086b49b1ed6f946/addons/web/static/tests/helpers/test_utils.js
... _mock server: https://github.com/odoo/odoo/blob/51ee0c3cb59810449a60dae0b086b49b1ed6f946/addons/web/static/tests/helpers/mock_server.js
... _překvapení: https://github.com/odoo/odoo/blob/51ee0c3cb59810449a60dae0b086b49b1ed6f946/addons/web/static/tests/helpers/qunit_asserts.js
... _createView: https://github.com/odoo/odoo/blob/51ee0c3cb59810449a60dae0b086b49b1ed6f946/addons/web/static/tests/helpers/test_utils_create.js#L267
