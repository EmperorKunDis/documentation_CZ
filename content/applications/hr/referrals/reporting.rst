=========
Reportáž
=========

Funkce hlášení v aplikaci **Referrals** pomáhá personalistům a manažerům zjistit, odkud pochází uchazeči.
přihlašují se ze zaměstnaneckého počítače, pokud jsou doporučeni současným zaměstnancem. Dále je možné
počet uchazečů přijatých, zamítnutých a stále v procesu náboru pro každý médium.

.. důležité::
Přístup k reportování má pouze uživatel s právy administrátora aplikace **Nábor**.
bude součástí aplikace **Referrals**.

Analýza zaměstnaneckých doporučení
==================================

Pro přístup k zprávě *Analýza zaměstnaneckých referencí* přejděte na:
Zpráva“. Toto načte zprávu „Analýza doporučení zaměstnanců“, v předvoleném
:icon:`fa-bar-chart` :guilabel:`Bar Chart“.

Graf je zobrazen v :icon:`fa-database` :guilabel:`Skupinový“ pohledu s počtem
osy x a zdroj, označený jako „Medium“, odkud pochází žadatel
(např. *Facebook*, *LinkedIn*, *E-mail*, atd.) na ose X. Pokud médium **nevyskytuje se**
report, který ukazuje, že z daného média nebyly žádné doporučení.

Zobrazují se odměny za všechna kola, včetně: guilabel:'Nepřijat' (odmítnut).
„Ve výrobě“, „Nabíráme“ a „Pracujeme“. Výchozí filtr je nastaven na aktuální měsíc.

Přejíždějte myší nad kteroukoli z čar, abyste viděli okénko s konkrétními daty pro daný graf.

V tomto pohledu je zřejmé, který :guilabel:`Medium` je nejúspěšnější.

.. příklad::
V tomto příkladu jsou obě :guilabel:`E-mailová adresa` a :guilabel:`LinkedIn“ médii s nejvyšším počtem
přesměrování, ale „E-mail“ má nejvíce přijatých zaměstnanců.

.... obrázek:: reporting/employee-report.png
:alt: Výchozí zpráva v aplikaci Referrals.

Příklad použití: zaměstnanecké doporučení
-------------------------

Jedním z možných způsobů využití této funkce je posouzení, které zaměstnanci doporučují nejvyšší kvalitu.
uživatelů. To se dělá tím, že se zkoumá, kolik jejich doporučení nakonec přijme zaměstnání.

V tomto příkladu jsou data analyzována za účelem určení, který zaměstnanec má nejvyšší počet zaměstnanců.
příspěvky za aktuální rok.

Pro zobrazení této informace nejprve klikněte na ikonu „Pivot“ (viz obrázek).
v pravém horním rohu. Poté odstraňte aktuální filtr v poli vyhledávání.

Klikněte na ikonu „fa-caret-down“ (spodní šipka) v vyhledávacím poli, abyste zobrazili seznam.
Najít v nabídce „Datum“ (v seznamu filtrů vedle ikony „fa-filter“). Po kliknutí na tento odkaz se zobrazí
Níže uvedené rozbalovací nabídce časových období a klikněte na aktuální rok (v tomto případě
:guilabel:`2024“).

Dále klikněte na „Míry“ :guilabel:`Measures` :icon:`fa-caret-down“, pak vyberte „Získané body“ a
Klikněte na obrazovce kamkoliv, abyste skryli tyto metriky.
kliknutím na tlačítko „Drop-Down Menu“ v levém horním rohu obrazovky.

Zobrazená data ukazují, kolik celkových žadatelů každý zaměstnanec doporučil a kolik z nich bylo přijato.
Tyto uchazeči byli přijati pro letošní rok.

V tomto případě lze zjistit, že nejúspěšnějším odkazem je:guilabel:Bob Wilson.
s třemi zaměstnanými doporučeními a devíti celkovými doporučenými uchazeči. Dále:guilabel:Mitchell
Admin má nejhorší výkon v oblasti doporučení, protože má jen jednoho uchazeče a žádné přijaté zaměstnance.

Tato informace může být pro tým náboru užitečná, aby zjistil, kdo je nejaktivnější.
referraly v rámci společnosti a kdo je nejúspěšnější z pohledu náboru.

.. obrázek::reporting/employee-counts.png
:alt: Zákaznická zpráva, která ukazuje, které zaměstnanci mají nejvíce doporučení a přijatých pracovníků.

.. tip::
Pivotová tabulka lze vložit do nového nebo existujícího :doc:`sešitu
pokud si přejete, můžete vložit do tabulky pomocí příkazu

K tomu stačí kliknout na tlačítko „Vložit do tabulky“ umístěné nad grafem. Po jeho stisknutí se zobrazí okno s
Okno se zobrazí a zeptá se, do které tabulky chcete vložit plovoucí graf. Vyberte požadovaný
tabulku nebo panel z nabízených možností. Nebo vyberte: „Vyprázdněný
Vytvořit nový sešit.

Klikněte na tlačítko „Potvrdit“ a vybraný sešit se otevře s novou tabulkou v něm.

Tabulka je uložena v aplikaci Dokumenty. Tato aplikace **musí být**
nainstalovaný pro použití možnosti „Vložit do tabulky“.
