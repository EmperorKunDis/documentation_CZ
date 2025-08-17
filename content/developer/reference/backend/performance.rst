:custom-css: performance.css

===========
Výkon
===========

.._výkon/profilování:

Profilování
=========

...:odoo.tools.profiler

Profilování je o analýze provádění programu a měření agregovaných dat. Tyto data mohou
je doba trvání každé funkce, provedených dotazů na databázi…

Profilování samo o sobě výkon programu nezlepšuje, ale může být velmi užitečné.
v nalezení problémů s výkonem a určení, které část programu za ně může být zodpovědná.

Odoo poskytuje integrovaný nástroj pro profilování, který umožňuje zaznamenat všechny provedené dotazy a stav
stopy během provádění. Může být použita k profilování buď sady požadavků uživatelské relace nebo
určité části kódu. Profilování může být buď zkontrolováno s integrovaným „speedscope
<https://github.com/jlfwong/speedscope>`_ :dfn:`otevřený zdrojový kód aplikace, která umožňuje vizualizovat grafy spalování“
výhled nebo analyzován s vlastními nástroji po uložení do souboru JSON nebo do databáze.

.._výkon/profilování/zapnout:

Povolte profiler
-------------------

Profiler lze zapnout buď z uživatelského rozhraní, což je nejjednodušší způsob,
umožňuje profilování pouze požadavků na webové stránky nebo z Pythonového kódu, což umožňuje profilování jakéhokoli kusu kódu
včetně testů.

.. záložky::

....... tab::Povolit z uživatelského rozhraní

      #:ref:`Povolit vývojářský režim <developer-mode>“.
      #Před zahájením sezení profilování musí být profilér zapnut na celé databázi.
To lze provést dvěma způsoby:

         - Otevřete nástroje pro vývojáře:ref:`<developer-mode/tools>`, pak přepněte
:tlačítko „Zapnout profilování“ a následně se zobrazí průvodce, který navrhne sadu časových úseků pro
profilování. Klikněte na tlačítko :guilabel:`ZAPNĚTE PROFILOVÁNÍ GLOBÁLNĚ`.

.. obrázek: výkon/zapnout_profilovacího_průvodce.png

         - Přejděte na:guilabel:`Nastavení --> Obecné nastavení --> Výkon“ a nastavte požadovanou dobu
pole :guilabel:`Povolit profilování do“.

      #Po zapnutí profileru na databázi mohou uživatelé zapnout profiler i ve svém sezení.
Protože se jedná o vývojářské nástroje, je zapotřebí v nastavení vybrat možnost „Zapnout profilování“
znovu. Výchozí doporučené možnosti: guilabel:"Záznam
SQL a :guilabel:Záznamy stop jsou povoleny. Chcete-li se dozvědět více o různých možnostech,
Vydejte se na adresu:ref:performance/profiling/collectors.

.. obrázek: výkon/profilování_nabídka_pro_ladění.png

Při zapnutém profilování jsou všechny požadavky na server profilovány a uloženy.
záznam typu ir.profile. Takové záznamy jsou seskupeny do aktuální seance profilování.
začíná od okamžiku, kdy byl profiler zapnutý, a končí v momentě jeho vypnutí.

.. poznámka::
Online databáze Odoo nelze profilovat.

...... tab:: Zapnout z Pythonového kódu

Pokud chcete profilovat konkrétní metodu nebo část kódu, může být ruční spuštění profileru užitečné.
kód. Tento kód může být test, výpočetní metoda, celé zatížení atd.

Profiler z Pythonu spustíte jako kontextový manažer. Můžete specifikovat, co chcete sledovat.
Pokud chcete profilovat pomocí parametrů, je k dispozici zkratka pro profilování tříd testů:
:kód: `self.profile()`). Podrobnější informace o tom, jak sbírat profily naleznete v kapitole
parametru „sběratelé“.

... příklad::

... kódový blok: Python

s profilerem():
do_stuff()

... příklad::

... kódový blok: Python

s Profilerem (shromažďovače = ['sql', periodický shromažďovač (interval = 0,1) ] ):
do_stuff()

... příklad::

... kódový blok: Python

s sebou.profile():
s vlastním self.assertQueryCount(__system__=1211):
do_stuff()

.. poznámka::
Profiler je volán mimo funkci assertQueryCount, aby zachytil všechny dotazy provedené
při opuštění kontextového manažera (např. při flushe).

... autoklasifikátor: Profiler()
:special-members: __init__

Když je profiler zapnutý, všechny provedení metody jsou profilovány a uloženy do
záznam typu ir.profile. Takové záznamy jsou seskupeny do jedné sekce profilování.
Zejména u použití dekorátorů :code:`@warmup` a :code:`@users`.

...............tip:
Je možné, že analýza výsledků profilování metody volané několikrát bude komplikovaná.
protože všechny volání jsou seskupeny v záznamu o stavu. Přidejte **kontext výkonnosti**
jako kontextový manažer, který rozdělí výsledky do několika rámců.

... příklad::

... kódový blok:: python

pro index v rozsahu od 0 do max_index:
s ExecutionContext(current_index=index): # Identifikace každého volání v rámci výsledků SpeedScopeu.
do_stuff()

.._výkon/profilování/analýza:

Analyzujte výsledky
-------------------

Procházet výsledky profilování je možné pouze v případě, že je profiler zapnutý
databáze <výkon/profilování/zapnout>“, pak otevřete nástroje pro vývojáře
„Nástroje pro vývojáře“ a klikněte na tlačítko v pravém horním rohu profilování.
sekci. Seznam záznamů ir.profile seřazených podle profilovacího cyklu se otevře.

.. obrázek: výkon/profilování webu.png
:align:center

Každý záznam má kliknutelnou odkazovou adresu, která otevře výsledky měření rychlosti v novém okně.

.. obrázek: výkon/flamegraph_example.png
:align:center

Speedscope spadá mimo rozsah této dokumentace, ale existuje mnoho nástrojů k vyzkoušení: vyhledávání
vyznačování podobných rámců, zvětšení rámečku, časová osa, levý těžký, dvouoké zobrazení...

Odoo vytváří různé zobrazení podle aktivovaných možností profilování.
Dostupné z horního menu.

.. obrázek: výkonnostní/rychlostní režimy
:align:center

- Ve výchozím nastavení se zobrazuje vše, co je k dispozici. Výběrem „Zkombinovat“ se zobrazí všechny dotazy a stopy spojené dohromady.
- Výhled „Současná kombinace bez kontextu“ zobrazuje stejný výsledek, ale ignoruje uložené provedení.
kontextu <výkon/profilování/zapnout>.
- Vidíte všechny SQL dotazy, jako by byly spuštěny po sobě.
další, bez jakéhokoliv logického vzorce Pythonu. Tento je užitečný pouze pro optimalizaci SQL.
- Viditelná tabulka :guilabel:`sql (hustota)` zobrazuje pouze všechny SQL dotazy, mezi nimiž je mezera.
může být užitečné při odhalování problémů v SQL nebo Python kódu a při identifikaci oblastí, kde
mohlo by se spouštět mnoho malých dotazů najednou.
- V zobrazení :guilabel:`frames` jsou vidět pouze výsledky periodického sběru.
<výkon/sledování/sběr/periodické>.

.. důležité:
I když byl profiler navržen tak, aby byl co nejlehčí, může stále ovlivnit
výkon, zejména při použití kolektoru :ref:`Synchronní.
<výkon/profilování/sběrky/synchronizace>. To je důležité při analýze výsledků SpeedScope.

...výkon/profilování/sběr dat:

Sběratelé
----------

Profilér se týká *kdy* profilování, sběrači se pak starají o *co*.

Každý sběratel se specializuje na shromažďování profilovacích dat vlastním formátem a způsobem. Mohou být
individuálně zapínatelné z uživatelského rozhraní prostřednictvím jejich vlastního přepínače.
:ref:`nástroje vývojářského režimu <developer-mode/tools>“ nebo z Pythonového kódu prostřednictvím jejich klíče.
třída.

V současné době je k dispozici v Odoo čtyři sběratele:

.. seznam tabulkový::
:hlavičky: 1

   * - Jméno
     - Přepínač
     - Klíč Python
     - Třída Python
   * – :ref:`SQL sběrník <výkon/profilování/sběrače/sql>
     - :guilabel:`Záznam SQL“
     - sql
     - „SqlCollector“
   * - :ref:`Periodický sběr dat <výkon/profilování/sběr dat/periodické sběry>`
     - :guilabel:`Záznamy o stopách“
     - „traces_async“
     - PeriodicCollector
   * – :ref:`QWeb sběrce <výkonnost/profilování/sběrače/qweb>
     - :guilabel:`Záznam qweb“
     - „qweb“
     - QwebCollector
   * – :ref:`Synchronní sběr dat <výkon/profilování/sběr dat/synchronní>`
     - No
     - „synchronizace stop“
     - „Synchronizátor“

Výchozí nastavení profileru zahrnuje SQL a periodické sběrnice.
uživatelské rozhraní nebo Python kód.

…výkon/profilování/sběrače/SQL:

SQL sběrce
~~~~~~~~~~~~~

SQL sběrník ukládá všechny dotazy k databázi v aktuálním vláknu (pro všechny).
(tj. kurzory) a také stacktrace. Přidaná složka analyzovaného vlákna je přesnost sběrače
pro každou dotazovou frázi, což znamená, že použití na mnoho malých dotazů může ovlivnit dobu zpracování.
další profiléři.

Je zvláště užitečné při ladění počtu dotazů nebo přidání informací do periodického sběrače
<výkon/profilování/sběrače/periodické> v kombinaci s přehledem rychlosti.

... autoklasifikátor: SQLCollector

...výkon/profilování/sběrače/periodické:

Periodický sběrce
~~~~~~~~~~~~~~~~~~

Tento sběrač běží v samostatném vláknu a ukládá stavové záznamy analyzovaného vlákna při každé
interval. Interval (výchozí hodnota je 10 ms) lze definovat pomocí možnosti
uživatelské rozhraní nebo parametr interval v Pythonovském kódu.

.. varování:
Pokud je interval nastaven na velmi nízkou hodnotu, profilování dlouhých požadavků vyvolá problémy s pamětí.
Pokud je nastaven interval na velmi vysokou hodnotu, dojde k zobrazení informací o krátkých funkcích.
ztracené.

Je to jedna z nejlepších metod analýzy výkonnosti, protože by měla mít velmi nízký dopad na
výkonu díky samostatnému vláknu.

... autoClass: PeriodicCollector

...výkon/profilování/sběrače/QWeb:

QWeb sběrač
~~~~~~~~~~~~~~

Tento sběratel ušetří čas výpočtu Pythonu a dotazy všech direktiv.
Sběrník <výkonu/profilování/sběrače/SQL>, přičemž náklady na provedení mohou být důležité,
mnoho malých příkazů. Výsledky jsou odlišné od ostatních sběračů v oblasti shromážděných dat.
a lze je analyzovat pomocí vlastního widgetu ve formuláři „ir.profile“.

Je především užitečný pro optimalizaci výhledu.

... autořízení: QWebCollector

...výkon, profilování, sběr dat a synchronizaci:

Synchronizátor sběrače
~~~~~~~~~~~~~~

Tento sběrce ukládá stoh na každý volání a návrat funkce a běží v jednom vláknu.
Tento faktor výrazně ovlivňuje výkon.

Může být užitečné při ladění a pochopení složitých toků a sledování jejich provádění v kódu.
Je však nevhodný pro analýzu výkonu, protože má vysokou přetížitelnost.

... třída AutoClass: SyncCollector

...výkon, profilování a chyby:

Příčiny špatného výkonu
--------------------

- Buďte obezřetní s náhodností. Opakované provedení může vést k různým výsledkům. Například
spouštěč během provádění.
- Pozor na blokování hovorů. V některých případech může externí funkce c_call trvat delší dobu
vypuštěním GIL, což vede k neočekávaným dlouhým rámcům s periodickým sběračem
<výkon/profilování/sběrače/periodický>. Toto by měl detekovat profiler a dát
varování. Profiler lze spustit ručně před takovými voláními, pokud je to potřeba.
- Všímejte si mezipaměti. Profilování předtím, než se do ní uloží „pohled“ a „aktiva“ atd., může vést k
různé výsledky.
- Buďte si vědomi nákladů profilovacího programu.
Přetížení <performance/profiling/collectors/sql> může být důležité, pokud je spousta malých dotazů.
jsou spuštěny. Profilování je praktické k odhalení problému, ale můžete chtít vypnout profiler
aby se změna v kódu mohla měřit.
- Výsledky profilování mohou být náročné na paměť. V některých případech (např. při profilování instalace nebo dlouhého
(tedy požadavek), je možné, že se dostanete na hranici paměťového limitu, zejména při renderování rychloměru.
výsledky, které mohou vést k chybě HTTP 500. V tomto případě budete možná muset spustit server s
větší limit paměti: `--limit-memory-hard $((8*1024**3))`.

...výkonu/dobré praxe:

Dobré praxe
==============

...výkonu/dobré praxe/soubor:

Operace s více soubory
----------------

Při práci s recordsety je vždy lepší provádět operace ve více krocích.

Příklad:
Nepoužívejte metodu, která spouští dotazy SQL při procházení záznamového setu, protože to tak udělá
pro každý záznam v sadě.

... první třídy: špatný příklad
... kódový blok:: python

def _vypočítat počet (self):
pro rekord v sobě:
doména = [('related_id', '==', rekord.id)]
record.počet = jiný_model.vyhledávací_počet(doména)

Vynechte místo toho pole „search_count“ a nahraďte jej poli „_read_group“, abyste mohli provést jednu dotazovou SQL pro celý
soubor záznamů.

......: dobrý příklad
... kódový blok:: python

def _vypočítat počet (self):
doména = [('related_id', 'in', self.ids)]
counts_data = jiný model._čtení skupiny (doména, ['related_id'], ['__count'])
mapped_data = slovník (counts_data)
pro rekord v sobě:
record.počet = mapper_data.get(record, 0)

....... poznámka::
Tento příklad není optimální ani správný vždy. Je pouze náhradou za
„search_count“. Další možností je předčítání a počítání obráceného pole One2Many.

Příklad:
Nezaznamenávejte jeden rekord za druhým.

... první třídy: špatný příklad
... kódový blok:: python

for jméno v ['foo', 'bar']:
model.create({'name': jméno})

Využijte místo toho metodu pro sčítání hodnot a zavolejte na objekt metodu „vytvořit“.
Většinou nemá žádný vliv a pomáhá rámci optimalizace výpočtů polí.

......: dobrý příklad
... kódový blok:: python

vytvořit_hodnoty = []
for jméno v ['foo', 'bar']:
create_values.append({'name': jméno})
rekordy = model.vytvořit(hodnoty vytváření)

Příklad:
Nezpracovávejte pole záznamu v rámci jednoho průchodu smyčkou, zatímco procházíte jednotlivé záznamy.

... první třídy: špatný příklad
... kódový blok:: python

pro každý id v record_ids:
model.prohlížet(id záznamu)
record.foo # Jedna dotazováno je provedeno na každý záznam.

Vyhledejte celý záznamový soubor.

......: dobrý příklad
... kódový blok:: python

records = model.prohlížet(record_ids)
pro záznam v seznamu:
record.foo # Jedna dotazová příkaz je proveden pro celou sadu záznamů.

Můžeme si ověřit, že záznamy jsou předvyhledávány ve skupinách pomocí pole „prefetch_ids“, které
zahrnuje každý z identifikátorů záznamu. Prohlížení všech záznamů najednou je nepraktické,

Pokud je potřeba, lze použít metodu with_prefetch k vypnutí předběžného načítání v sekvencích:

... kódový blok:: python

pro každé hodnoty v seznamu hodnot:
zpráva = self.procházet(hodnoty['id']), s předvoláním sebe sama.

...výkonu/dobré praxe/algoritmické složitosti:

Snížit algoritmickou složitost
---------------------------------

Algorithmická složitost je měřítkem, jak dlouho by algoritmus trval k dokončení.
velikosti vstupu. Když je složitost vysoká, růst času na výpočet může být velmi rychlý s rostoucí
se zvětšuje. V některých případech lze algoritmickou složitost snížit tím, že se připraví vstup
Data správně.

Příklad:
Pro daný problém vezměme naivní algoritmus sestavený ze dvou vnořených cyklů.
složitost v O(n²).

... první třídy: špatný příklad
... kódový blok:: python

pro záznam v sobě:
pro výsledek v výsledcích:
pokud je výsledek ['id'] roven hodnotě záznamu:
record.foo = výsledky['foo']
přerušit

Pokud všechny výsledky mají jiný identifikátor, můžeme připravit data tak, abychom snížili jejich složitost.

......: dobrý příklad
... kódový blok:: python

mapped_result = {výsledek['id']: výsledek['foo'] pro výsledek v results}
pro záznam v sobě:
record.foo = mapper.get(record.id)

Příklad:
Vybráním špatné struktury dat pro uložení vstupu může dojít k kvadratické složitosti.

... první třídy: špatný příklad
... kódový blok:: python

invalidní identifikátory = seznam identifikátorů, které jsme získali vyhledáním v doméně.
pro záznam v sobě:
pokud je id záznamu v seznamu neplatných ID,
              ...

Pokud je `invalid_ids` datovou strukturou podobnou seznamu, složitost algoritmu může být kvadratická.

Vyhněte se používání operací sestav jako převodu na setu pomocí hodnoty `invalid_ids`.

......: dobrý příklad
... kódový blok:: python

neplatné_idy = set(neplatné_idy)
pro záznam v sobě:
pokud je id záznamu v seznamu neplatných ID,
              ...

V závislosti na vstupu lze použít i operace s datovým souborem.

......: dobrý příklad
... kódový blok:: python

invalidní_idy = self.vyhledat(doména)
pro rekord v sobě - neplatné ID:
          ...

.. výkonu/dobré praxe/index:

Použijte indexy
-----------

Indexy databáze mohou pomoci zrychlit vyhledávání, ať už je provedeno přes nebo skrze uživatele.
Uživatelské rozhraní.

... kódový blok:: python

name = pole.Char(string="Jméno", index=True)

.. varování:
Buďte opatrní, abyste neindexovali každý prvek, protože indexy zabírají místo a ovlivňují výkon.
výkonu jedné z příkazů INSERT, UPDATE nebo DELETE.
