==================
Definujte modulová data
==================

.. důležité:
Tento návod je pokračováním návodu :doc:`server_framework_101`. Ujistěte se, že jste si přečetli
dokončil ji a použijte modul „majetek“, který jste postavili, jako základ pro cvičení v této
návod.

Typy dat
==========

Hlavní data
-----------

Hlavními daty jsou obvykle součástí technických nebo obchodních požadavků na modul.
slovy, taková data jsou často nutná pro správnou funkci modulu. Tato data budou vždy
nainstalovaný při instalaci modulu.

Technické údaje jsme již dříve viděli, protože jsme definovali :doc:`výhledy
<../reference/user_interface/view_records> a :doc:`akce <../reference/backend/actions>“.
Jedná se o jednu z forem hlavních dat.

Kromě technických dat lze definovat také obchodní údaje, například země, měny, jednotky měření.
a také úplné lokalizace země (právní zprávy, definice daní, rozvaha) a mnoho
více...

Demo data
---------

Kromě základních dat, které jsou podmínkou pro správnou funkci modulu, máme rádi
pro ilustraci dat:

* Pomozte obchodním zástupcům rychle předvádět své produkty.
* Máme sadu funkčních dat pro vývojáře, kteří mohou nové funkce otestovat a vidět, jak tyto nové funkce vypadají.
s daty, která by si možná sama nepřidala.
* Testovat, zda jsou data načtena správně a nevyvolává se chyba.
* Nastavte většinu funkcí, které chcete používat při vytváření nové databáze.

Demo dat se načte automaticky při spuštění serveru, pokud jste neřekli, že je nepoužíváte.
chcete, můžete to udělat v databázovém manažeru nebo příkazovou řádkou.

.. kódový blok: konzole

$ ./odoo-bin -h
Použití: odoo-bin [možnosti]

Možnosti:
-v                  zobrazit číslo verze programu a ukončit
-h, --help           zobrazit tuto nápovědu a ukončit

Běžné možnosti:
    [...]
--bez-demonstrace WITHOUT_DEMO
vypnout načítání ukázkových dat pro moduly, které se mají nainstalovat
(oddělené čárkou, použijte „všechny“ pro všechny moduly).
-d a -i. Výchozí je žádné
  [...]

$ ./odoo-bin --addons-path=... -d db -i account --without-demo=all

Oznámení o zpracování osobních údajů
================

Manifest
--------

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`Manifesty modulů<reference/module/manifest>.

Data jsou buď deklarována ve formátu CSV nebo v XML.
Každý soubor, který obsahuje data, musí být přidán do seznamu pro jejich načtení.

Klíč, který je v manifestu k použití pro přidání nových dat, je „data“ pro hlavní data a „demo“
demo dat. Oba hodnoty by měly být seznamem řetězců reprezentujících relativní cesty k souborům
Vyhlášení dat.

Obvykle je ukázková data v adresáři „demo“, pohledy a akce jsou ve složce „views“.
soubory s bezpečnostními daty jsou v adresáři „security“, ostatní soubory jsou uloženy v
Soubor „data“.

Pokud vypadá váš pracovní strom takto:

... kódový blok:: bash

majetek
└── data
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└── demo
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└── models
│   ├── *.py
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└── security
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└── views
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└──__init__.py
└── __manifest__.py

Váš manifest by měl vypadat takto:

... kódový blok:: python

  # *-*- kódování: UTF-8 *-*-

  {
"název": "Realitní kancelář",
„závisí“: [
          ...
      ],
"data": [
„soubor bezpečnostních pravidel/ir.model.access.csv“,# Soubory CSV a XML jsou načítány na stejném místě
„views/nabídka-nemovitosti-výhledy.xml“, # Výhledy jsou také daty
„data/master_data.xml“, # Rozdělte data do více souborů podle modelu
      ],
"demo": [
„demo/demo_data.xml“.
      ]
„aplikace“: True
  }

ČSSD
---

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`Soubory CSV<reference/data/csvdatafiles>“.

Nejjednodušší způsob, jak deklarovat jednoduchá data, je použití formátu CSV. Ten však má omezení
vlastností: používejte ho pro dlouhé seznamy jednoduchých modelů, jinak raději XML.

... blok kódu:: text

id, pole_a, pole_b, vztahované_id:id
1,hodnotaA1,hodnotaB1,modul.přidruženýID
id2,hodnotaA2,hodnotaB2,modul.připojenéID

Tip: Váš editor pravděpodobně má doplněk, který umožňuje zvýraznění syntaxe souborů CSV.

  * „Atom <https://atom.io/packages/rainbow-csv>“.
  * „PyCharm/IntelliJ <http://plugins.jetbrains.com/plugin/10037-csv-plugin>“.
  * „Vím <https://github.com/mechatroner/rainbow_csv>“.
  * „Visual Studio <https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv>“.

... cvičení: Přidejte několik typů nemovitostí pro modul „nemovitosti“: rezidenční,
Obchodní, průmyslové a pozemkové. Tyto by měly být vždy nainstalovány.

XML
---

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`Soubory dat<reference/data>“.

Při vytváření složitějších dat může být užitečné nebo dokonce nutné je vytvářet pomocí XML.

... blok kódu::xml

<odoo>
<záznam id="id1" typ="tutorial.example">
<pole název="pole_a">hodnotaA1</pole>
<pole name="pole_b">hodnotaB1</pole>
</záznam>

<záznam id="id2" typ="tutorial.example">
<pole název="pole_a">hodnotaA2</pole>
<pole name="pole_b">hodnotaB2</pole>
</záznam>


...cvičení: Vytvořte nějaká ukázková data pro modul „majetek“.

  ================== ==================== ======================
pole                 hodnoty                hodnoty
  ================== ==================== ======================
jméno              Velký dům           Karavan
stát                Nové                 Zrušené
popis             Pěkný velký dům v obytném voze
poštovní směrovací číslo 12345          54321
date_availability 2020-02-02 1970-01-01
očekávaná cena      1 600 000             100 000
prodejní cena                             120 000
ložnice                 6                   1
obytná plocha       100                   10
fasády             4                     4
garáž            pravda               nepravda
zahrada            Pravda
zahrada            100000
orientace zahrada jih
  ================== ==================== ======================

Data Extension
~~~~~~~~~~~~~~

Během jádrového tréninku jsme viděli v kapitole „server_framework_101/12_dědičnost“
mohla dědit (rozšiřovat) existující pohled. Tento případ byl zvláštním případem datového rozšíření: jakákoliv data mohla být
rozšířený o modul.

Pokud přidáváte nové pole do stávajícího modelu v novém modulu, možná budete chtít
těmto polím na záznamu vytvořeném v modulech, které jsou pro vás závazné. To se provádí tím, že
ID XML záznamu, který chcete rozšířit. Tento případ nebude nahrazovat, v tomto případě nastavíme
„pole c“ na zadanou hodnotu pro obě záznamy.

... blok kódu::xml

<odoo>
<záznam id="id1" typ="tutorial.example">
<pole název="pole_c">hodnotaC1</pole>
</záznam>

<záznam id="id2" typ="tutorial.example">
<pole name="pole_c">hodnotaC2</pole>
</záznam>



„ref“
~~~~~~~

Související pole lze nastavit pomocí klíče „ref“. Hodnota tohoto klíče je „xml_id“ pole.
záznam, ke kterému chcete vytvořit odkaz. Pamatujte na to, že „xml_id“ je složen ze jména modulu, kde
Data jsou nejprve vyhlášena, následuje tečka a „id“ záznamu (jenom „id“
funguje i v případě, že se nacházíte ve stejném modulu jako on).

... blok kódu::xml

<odoo>
<záznam id="id1" typ="tutorial.example">
<field name="related_id" ref="modul.relatedid"/>
</záznam>


... cvičení: Vytvořte několik nabídek na prodej nemovitostí, které jste vytvořili.

Vytvářejte nabídky pomocí partnerů definovaných v „base“

  ============== ========= ======= ========
Partner      Nemovitost  Cena  Platnost
  ============== ========= ======= ========
Azure Interior Big Villa 10000   14
Azure Interior Big Villa 1500000 14
Deco Addict    Velký dům 1500001 14
  ============== ========= ======= ========

...cvičení: Ujistěte se, že oba vaše ukázkové nemovitosti byly vytvořeny s nastavením typu nemovitosti na rezidenční.

„eval“
~~~~~~~~

Hodnota, kterou chcete přiřadit pole, není vždy pouze jednoduchý řetězec a může být nutné ji vypočítat.
Může být také použit k optimalizaci vložení souvisejících hodnot nebo proto, že omezení nutí
Přidat související hodnoty v sadě. Podívejte se na odkaz:
<návody/definovat modulová data/x2m>.

... blok kódu::xml

<odoo>
<záznam id="id1" typ="tutorial.example">
<položka jméno="rok" hodnota="datum.nyní().rok + 1"/>
</záznam>


... cvičení: Nabídky, které jste přidali, by měly vždy být v datu odpovídajícím instalaci
modul.

„vyhledat“
~~~~~~~~~~

Někdy je potřeba zavolat na ORM, aby provedl „hledání“. To není možné s formátem CSV.

... blok kódu::xml

<odoo>
<záznam id="id1" typu="účetní položka move line">
<field name="account_id" search="[
('user_type_id', '=', ref('account.data_account_type_direct_costs'))
['company_id', '==', obj().env.company.id]]
        "/>
</záznam>


V tomto kódu je potřeba proto, že se hlavní data odvíjejí od lokality
nainstalovány.

„funkce“
~~~~~~~~~~~~

Pokud se chystáte načítat data, můžete také potřebovat spustit kód Pythonu.

... blok kódu::xml

<funkce model="tutorial.example" jméno="akce_validace">
<value eval="[ref('faktura_demo_1')]"/>


...cvičení: ověřte jednu z nabídek vzorkového datového souboru pomocí tlačítka „Přijmout nabídku“.
jiní.


.. _tutorials/define_module_data/x2m:

Přidejte pole X2many
-----------------

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
Třída: ~odoo.fields.Command

Pokud chcete přidat související data do pole One2many nebo Many2many, můžete tak učinit pomocí
:třída metod Command.

... blok kódu::xml

<odoo>
<záznam id="id1" typ="tutorial.example">
<pole name="related_ids" eval="[
Command.create({
"jméno": "Jsem My",
            }),
Command.create({
'jméno': 'Vaše jméno'
            }),
Command.link(odkaz na model.xml_id),
        ]"/>
</záznam>


...cvičení: Vytvořte jednu novou vlastnost, ale tentokrát s několika nabídkami vytvářenými přímo uvnitř
Jedna pole s odkazem na nabídky.

Přístup k datům
==================

Upozornění: Nikdy neměli přistupovat k datům z demoverze mimo deklarovanou demoverzi, ani v
testy.

Existuje několik způsobů, jak se k hlavním nebo demonstračním datům dostat.

V Pythonovském kódu můžete použít metodu „env.ref(self, xml_id, raise_if_not_found=True)“.
vrací seznam, který je spojen s „xml_id“, které zadáte.

V XML můžete používat klíč ref takto

... blok kódu::xml

<odoo>
<záznam id="id1" typ="tutorial.example">
<field name="related_id" ref="modul.relatedid"/>
</záznam>


Volá metodu ref a ukládá ID záznamu v poli related_id.
záznamu typu „tutorial.example“ s ID „id1“.

V CSV musí být název sloupce doplněn o „:id“ nebo „/id“.

... blok kódu:: text

id,parent_id:id,název
„dítě1“, „modul.rodič“, „Jméno1“
„dítě2“, „modul.rodič“, „Jméno2“
„dítě3“, „modul.rodič“, „Jméno3“

V SQL je to složitější, viz část „Pokročilé informace“.
<návody/definovat modulová data/xml_id>.

Upozornění: Uživatel může kdykoliv smazat data. Vždy píšete kód obranně a vycházíte z toho
účet.




Pokročilé
========

.. _tutorials/define_module_data/xml_id:

Co je to XML ID?
-------------------

Protože nechceme v každé tabulce databáze mít sloupec „xml_id“, potřebujeme
mechanismus pro uložení. Toho se dosáhne pomocí modelu „ir.model.data“.

Obsahuje název záznamu (tj. „xml_id“) spolu s modulem, ve kterém je definován.
model definující její identitu a ID.

Žádné novinky
---------

Záznamy vytvořené s „noupdate“ vlajkou nebudou aktualizovány při upgradu modulu,
Vytvořil je, ale vznikne, pokud dosud neexistovaly.

.. poznámka: „odoo-bin -i modul“ obchází tuto volbu a vždy načítá data, ale normálně
Není vhodné to dělat na produkčním serveru.

... blok kódu::xml

<odoo noupdate="1">
<záznam id="id1" model="model">
<pole název="fieldA" hodnota="true"/>
</záznam>



Import jako SQL
-------------

V některých případech se může vyplatit provést import přímo v SQL. To je však z důvodu
obchází všechny funkce ORM, pole s počítanými hodnotami včetně metadat a omezení Pythonu.

.. poznámka: Používání neupraveného SQL obecně obchází ACL a zvyšuje riziko vstřikování.

**Poznámka**: :ref:`Bezpečnost v Odoo<reference/security>`

* Může urychlit dovozní čas o hodně
`s obrovskými soubory <https://github.com/odoo/enterprise/blob/d46cceef8c594b9056d0115edb7169e207a5986f/product_unspsc/hooks.py#L19>.
* Pro složitější dovozy, jako je
`přeložení <https://github.com/odoo/odoo/blob/e1f8d549895cd9c459e6350430f30d541d02838a/odoo/addons/base/models/ir_translation.py#L24>.
* Může být nutné
`zavést databázi <https://github.com/odoo/odoo/blob/e1f8d549895cd9c459e6350430f30d541d02838a/odoo/addons/base/data/base_data.sql>.
