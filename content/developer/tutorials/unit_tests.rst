===================================
Ochraňte svůj kód pomocí jednotek testování
===================================

.. důležité:
Tento návod je pokračováním návodu :doc:`server_framework_101`. Ujistěte se, že jste si přečetli
dokončil ji a použijte modul „majetek“, který jste postavili, jako základ pro cvičení v této
návod.

**Dodatečné informace**:
„Testovací rámec Odoo: naučte se nejlepší postupy“ __
(Odoo Experience 2020) na YouTube.

Napíjení testů je nezbytné z mnoha důvodů, zde je pouze výčet některých z nich:

* Ujistěte se, že kód nebude v budoucnu prolomen
* Určete rozsah vašeho kódu
* Uveďte příklady použití
* Je to jedna z cest, jak technicky dokumentovat kód.
* Pomozte si při kódování tím, že stanovíte cíl předtím, než se vydáte za ním

Testování během provozu
=============

Než se naučíme psát testy, musíme vědět, jak je spouštět.

.. kódový blok: konzole

$ odoo-bin -h
Použití: odoo-bin [možnosti]

Možnosti:
-v                  zobrazit číslo verze programu a ukončit
-h, --help           zobrazit tuto nápovědu a ukončit

  [...]

Testovací konfigurace:
--test-file=TEST_FILE
Spusťte testovací soubor v Pythonu.
--test-enable      Zapnout jednotkové testy.
--test-tags=TEST_TAGS
Seznam specifikací oddělených čárkou, které se použijí k filtrování testů.
Vykonat. Povolit testy jednotek, pokud je nastavena. Filtr spec má
formát: [-][tag][/modul][:třída][.metoda] -
určuje, zda chceme testy zahrnout nebo vyloučit
stejném místě, jako je tento tag.
dekorátorem @tagged (všechny třídy testů mají
„standard“ a „při instalaci“ tagy až do té doby, než je uživatel explicitně
(viz dokumentace k dekorátorům). Znak „*“ bude
Pokud je tag vynechán v režimu zahrnutí, jeho hodnota se shoduje s hodnotou
Pokud je hodnota standardní, pak se vyloučí.
režimu, jeho hodnota je '*'. Modul, třída a metoda
Bude odpovídat názvu modulu, třídě testu
název a jméno metody testu. Příklad: --test-tags
:TestClass.test_func,/test_module,externí Filtrování
a provádění testů se děje dvakrát: hned po
každé instalaci nebo aktualizaci modulu a na konci
moduly načítání. Na každé fázi jsou testy filtrovány

„při instalaci“ a „po instalaci“ odpovídajícím způsobem.
--screencasty=DIR  Screencasty budou uloženy v adresáři DIR/db_name/screencasts.
--screenshots=DIR  Snímky obrazovky budou uloženy v adresáři DIR/db_name/screenshots.
Výchozí je adresář /tmp/odoo_tests.

$ # spustit všechny testy účtu a modulů nainstalovaných účtem
$ # není testováno, zda jsou již nainstalované závislosti
$ # to chvilku trvá, protože musíte nainstalovat moduly, ale at-install
$ # a post_install jsou respektovány
$ odoo-bin -i account --test-enable
# spustit všechny testy v tomto souboru
$ odoo-bin --test-file=addons/account/tests/test_account_move_entry.py
$# Testovací značky vám pomohou filtrovat velmi snadno
$ odoo-bin --test-tags=/account:TestAccountMove.test_custom_currency_on_account_1

Integration Bots
================

.. poznámka: Tato část je určena pouze pro zaměstnance společnosti Odoo a lidi, kteří přispívají do
„github.com/odoo“. Vlastní CI doporučujeme, jinak.

Při psaní testu je důležité zajistit, aby vždy prošel i po změnách.
použít na zdrojový kód. K automatizaci této činnosti používáme vývojovou praxi zvanou
Kontinuální integrace (CI). Proto máme několik botů, které spouští všechny testy na různých
momenty.
Ať už pracujete pro Odoo nebo ne, pokud se snažíte něco sloučit do složky „odoo/odoo“,
„odoo/enterprise“, „odoo/upgrade“ nebo na odoo.sh, musíte projít CI. Pokud jste
pracujete-li na jiném projektu, měli byste přemýšlet o vlastním CI.

Runbot
------

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
„FAQ Runbotu <https://runbot.odoo.com/doc>“.

Většina testů se spouští na serveru „Runbot <https://runbot.odoo.com>“ při každém pushnutí změny
GitHub.

Stav závazku/větve můžete vidět na přehledové obrazovce bota.

Pro každou větev se vytvoří balíček. Balíček obsahuje konfiguraci a
série.

Soubor je sada budov, které závisí na parametrech balíčku.
Sériová výroba je zelená, pokud jsou všechny sestavené verze zelené.

Slovo „build“ označuje spuštění serveru. Může se dělit na podskupiny. Obvykle existují buildy
Pro komunitní verzi, pro firemní verzi (pouze pokud existuje firemní větve, ale
a migraci větve.
Stavba je zelená, pokud jsou všechny podstavby také zelené.

Sub-build je pouze částí plného buildu, který se používá k zrychlení CI.
proces. Obvykle se používá k rozdělení testů po instalaci na čtyři paralelní instance.
Sub-build je zelený, pokud všechny testy prošly a nebyl nalezen žádný chybový/varovný log.

.. poznámka::
  * Všechny testy se provádějí bez ohledu na změny, které byly provedeny. Oprava překlepu v chybové zprávě nebo
Refactorace celého modulu spouští stejné testy. Všechny moduly budou nainstalovány také. To znamená,
Něco nemusí fungovat ani když je robot zelený, tedy pokud se vaše změny vztahují na modul, který robot
modul, který se změnami pracuje, není závislý na něm.
  * Moduly lokálních verzí (tj. moduly specifické pro danou zemi) nejsou nainstalovány na Runbotu (s výjimkou
(tj. obecný modul) a některé moduly s externími závislostmi mohou být také vyloučeny.
  * Nocí se spouští další testy: moduly, lokalizace, jednotlivé
moduly instalace, víceúrovňové sestavení pro náhodné chyby atd.
Tyto proměnné se neuchovávají v standardním CI, aby se zkrátila doba provádění.

Můžete se také přihlásit do sestavení vytvořeného robotem Runbot. K dispozici jsou tři uživatelé: „admin“, „demo“ a
„portál“. Heslo je stejné jako přihlášení. To se hodí pro rychlé otestování věcí na různých
verze bez nutnosti je stahovat lokálně. Kompletní protokoly jsou také k dispozici, které se používají pro
monitoring.

Robodoo
-------

Váš level bude muset být o něco vyšší, než je potřeba k získání práv na svolávání
robodoo, ale i tak pár poznámek.

Robodoo je ten, kdo vám na vaše Pull Requests přidává tagy s aktuálním stavem CI. Ale také je to člověk, který vás
integruje vaše změny do hlavních repozitářů.

Když je poslední sestavení zelené, může revizor požádat robodoo o sloučení vaší aktualizace (je
„přeskočení“ než „sloučení“). Poté se přepne na mergebot.

Mergebot
--------

„Mergebot“ <https://mergebot.odoo.com> je poslední testovací fáze před spojením Pull Requestu.

Přidá nové závazky do vašeho větve, která nejsou ještě na cílovém místě a znovu spustí testy.
jednou a dokonce i v podnikové verzi, i když jen něco měníte.
komunita.

Tento krok může selhat s chybovou zprávou „Staging failed“. To může být způsobeno

* Nedeterministická chyba, která je již na cílovém zařízení. Pokud jste zaměstnancem Odoo, můžete si to ověřit
tyto zde: https://runbot.odoo.com/runbot/errors
* nepřesnost, kterou jste zavinili, ale nebyla detekována před testováním.
* neslučitelnost s dalším závazkem, který byl spojen předtím a co se pokoušíte o sloučení
* neslučitelnost s úložištěm pro firmy, pokud jste prováděli změny pouze v komunitním repozitáři.

Vždy se ujistěte, že problém nepochází z vaší strany, a pak požádejte o opakování: přepracovat
Váš větvený kód na cílové platformě a znovu spustit testy místně.

Moduly
=======

Odoo je modulární, takže testy také musí být modulární. To znamená, že testy jsou definovány
modul, který přidává funkčnost, kterou chcete přidat, a testy nemohou záviset na funkčnosti
přicházející z modulů, které nejsou závislé na vašem modulu.

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`Speciální značky<reference/testing/tags>“.

... kódový blok:: python

od odoo.tests.common import TransactionCase
od odoo.tests import tagged

  # CI bude tyto testy provádět až po instalaci všech modulů.
  # Nezavádí se ihned po instalaci té definující.
@tagged('post_install', '-at_install')  # přidat „post_install“ a odstranit „at_install“
třída PostInstallTestCase(Transakční případ):
def test_01(self):
          ...

@tagged('at_instalace') # výchozí
třída AtInstallTestCase(Transakční případ):
def test_01(self):
          ...


Pokud chcete otestovat chování, které lze změnit instalací jiného modulu, potřebujete
zajistit, aby byl nastaven atribut „at_install“; jinak můžete použít atribut „post_install“, abyste zrychlili
CI a zajistit, aby nebylo změněno, pokud by nemělo.

Napsání testu
==============

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
„Testování Pythonu <https://docs.python.org/3/library/unittest.html>“
a:ref:`Testování Odoo<reference/testing>“.

Před psaním testu je třeba zvážit několik věcí

* Testy by měly být nezávislé na datech, které jsou v databázi (včetně testovacích dat).
* Testy neměly ovlivňovat databázi zanecháváním nebo měněním zbytkových dat. To se obvykle provádí
testovacího rámce provedením rollbacku. Proto nikdy nevoláte metodu „cr.commit“ v testu
(ani jinde v obchodním zákoníku).
* Pro opravu chyby by měl test selhat před aplikací opravy a poté by měl být úspěšný.
* Nebuďte zbytečně kreativní a nezkoušejte něco, co už bylo otestováno jinde; můžete věřit ORM. Většina testů
V obchodních modulech by měly být testovány pouze obchodní procesy.
* Data by neměla být nutné do databáze přepisovat.

Poznámka: Vzpomínáme si na „onchange“, který se vztahuje pouze na formulářové pohledy, nikoli na změnu atributů.
v Pythonu. To platí i pro testy. Pokud chcete simulovat Form view, můžete použít
„odoo.tests.Form“.

Testy by měly být v adresáři „test“ na kořenovém adresáři vašeho modulu. Každý soubor s testem má
měly začínat „test_“ a importovat se v souboru „__init__.py“ složky s testy.
importovat složku/modul s testy do „__init__.py“ modulu.

... kódový blok:: bash

majetek
└── models
│   ├── *.py
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└── tests
│    └── test_*.py
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└──__init__.py
└── __manifest__.py

Všechny testy by měly rozšiřovat „odoo.tests.common.TransactionCase“. Obvykle definujete
„setUpClass“ a testy. Po napsání „setUpClass“ máte k dispozici „env“.
třídy a může začít interagovat s ORM.

Tyto testovací třídy jsou postaveny na základě modulu „unittest“ v Pythonu.

... kódový blok:: python

od odoo.tests.common import TransactionCase
od odoo.exceptions import UserError
od odoo.tests import tagged

  # CI bude tyto testy provádět až po instalaci všech modulů.
  # Nezavádí se ihned po instalaci té definující.
@tagged('post_instalace', '-při instalaci')
třída EstateTestCase(transakční testovací třída):

@classmethod
def setUpClass(cls):
          # přidat do souboru environmentální proměnnou a mnoho dalších věcí.
super(EstateTestCase, cls).setup_class()

          # Vytvořit data pro každý test. To udělejte v metodě setupClass
          # v rámci nastavení nebo v každém testovacím případě snižujeme dobu testování a
          # Duplicitní kód.
cls.vlastnictví = cls.env['nemovitost'].create([...])

def test_vytvoreni_oblasti(self):
"„Zkontrolujte, zda je celkový plošný obsah vypočítán správně.“"
self.vlastnosti.plocha_obytná = 20
self.assertRecordValues(self.properties, [
{'název': ..., 'celková plocha': ...}
{'název': ..., 'celková plocha': ...}
          ])


def test_akce_prodat(self):
„„Prodáváte-li nemovitost, měly by se chovat všechny věci tak, jak mají.““
self.vlastnosti.akce_prodáno()
self.assertRecordValues(self.properties, [
{'jméno': ..., 'stát': ...}
{'jméno': ..., 'stát': ...}
          ])

s sebou.assertRaises(UserError):
self.vlastnosti.zakázané_akce_na_prodanou_nemovitost

.. poznámka: Pro lepší čitelnost rozdělte své testy do více souborů podle jejich rozsahu.
testy. Můžete také mít třídu, která by měla být základní pro většinu testů, např.
Třída může definovat celé nastavení modulu. Například v
„účet <{GITHUB_PATH}/addons/account/tests/common.py>“.

… cvičení: Aktualizace kódu tak, aby nikdo nemohl:

  - Vytvořit nabídku na prodanou nemovitost
  - Prodat nemovitost bez přijatých nabídek

a vytvořit testy pro obě tyto případy. Dále zkontrolujte, že nemovitost může být prodána
musí být správně označen jako prodaný po jeho prodeji.


... cvičení: Někdo neustále narušuje obnovení zahrady a orientace, když odškrtnete
Zahrada je zkontrolována, aby se to už nikdy neopakovalo.

... tip::Tip: pamatujte si poznámku o třídě Form výše.
