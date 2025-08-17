=================
Vytvářejte PDF zprávy
=================

.. důležité:
Tento návod je pokračováním návodu :doc:`server_framework_101`. Ujistěte se, že jste si přečetli
dokončil ji a použijte modul „majetek“, který jste postavili, jako základ pro cvičení v této
návod.

Dříve jsme se dozvěděli o serverovém rámci QWeb (viz kapitola 10.14).
Kde byla použita pro vytvoření kanbanového pohledu. Teď se podíváme na jednu z funkcí QWebu
další hlavní použití: vytváření PDF zpráv. Běžnou poptávkou je schopnost vytvářet dokumenty
zaslat zákazníkům a použít v rámci firmy. Tyto zprávy lze využít k souhrnnému a grafickému zobrazení
informace v uspořádaném šablonu, který podporuje různé obchodní aktivity.
Dále můžeme do našich zpráv přidat naše firemní hlavičku a patičku s minimálním navýšením námahy.

Dokumentace k tomuto tématu je uvedena v :ref:`reference/qweb`.
:ref:`reference/reporty/report`, a :ref:`reference/akce/report
část odkazu na akce.

Struktura souborů
==============

Většina PDF zprávy je její šablona QWeb. Obvykle také potřebuje odpovídající
„ir.akce.report“ vložit zprávu do logiky modulu.
Není přísný pravidlo pro názvy souborů nebo jejich umístění, ale tyto dvě části jsou
obvykle uloženy ve dvou samostatných souborech v adresáři „report“ na úrovni vašeho modulu.
adresář. Pokud modul obsahuje mnoho nebo více dlouhých reportů, pak jsou často uspořádány
logicky v různých souborech pojmenovaných podle zpráv, které obsahují. Všechny akce
Protože zprávy jsou obvykle uloženy v stejném souboru s příponou „_report.xml“, ať už jde o
Počet zpráv, které obsahuje.

Protože se očekává, že váš pracovní strom bude vypadat nějak takhle:

... kódový blok:: bash

majetek
└── models
│   ├── *.py
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└──report
│    └── vlastnictví_nemovitostí.xml
│     └──estate_property_reports.xml
└── security
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└── views
│     └── *.xml
└──__init__.py
└── __manifest__.py

Nezapomeňte přidat do souboru „__manifest__.py“ všechny soubory, které budou použity vaším šablonovým a akčním pohledem.
V tomto případě chcete přidat soubory do seznamu „Data“ a pamatovat si, že soubory uvedené v manifestu
jsou načítány po sobě!

Základní zpráva
============

.. poznámka::

**Úkol**: Na konci této části budeme schopni vytisknout zprávu, která zobrazuje všechny nabídky pro
majetek.

.. obrázek:: pdf_reporty/jednoduchý_report.png
:synchronizace: střed
:alt: Jednoduchý PDF report

V našem příkladu s nemovitostmi je mnoho užitečných zpráv, které bychom mohli vytvořit. Jednoduchá zpráva
je ten, který zobrazuje všechny nabídky nemovitosti.

Údaje o zprávě
-----------

Než začneme, potřebujeme nějaká data, abychom je mohli použít v našich zprávách.
bude moc zajímavý. Při vytváření zpráv budete potřebovat nějaká data k otestování vašeho kódu
a zkontrolovat, že výsledný vzhled je takový, jaký očekáváte. Vhodné je testovat s daty, která pokryjí většinu
nebo všechny očekávané použití. Dobrá reprezentativní sada pro naši jednoduchou zprávu je:

* Mají alespoň 3 nemovitosti, kde je u jedné „prodáno“, u druhé „nabídka přijata“ a u třetí „nová“.
* Nabídky na alespoň 2–3 nemovitosti, které „prodáme“ a „přijmeme nabídku“.

Pokud nemáte sadu dat jako tuto, můžete buď:

* Dokončete návod k definování modulu, pokud jste ho ještě nedělali. Přidejte další
Přidejte případy k vašim ukázkovým datům (možná budete muset vytvořit novou databázi, do které se dají ukázková data načíst).
* Manuálně vytvořte data ve vaší databázi.
* Zkopírujte tento soubor dat

do nové složky (Data) v modulu majetku a zkopírujte tyto řádky
<https://github.com/odoo/technical-training-solutions/blob/{BRANCH}-J_reports/estate/__manifest__.py#L21-L23>
do souboru __manifest.py__ (můžete vytvořit novou databázi, do které se nahrají ukázkové údaje).

Před pokračováním projděte svá data v databázi a ujistěte se, že jsou taková, jaká očekáváte.
Samozřejmě můžete přidat data až po tom, co napíšete kód svého reportu, ale pak už nebudete moci
Postupně testujte části vašeho kódu, jakmile je napíšete. To vám umožní zkontrolovat chyby a
V dlouhodobém horizontu je ladění kódu pro složité zprávy obtížnější.

Minimální šablona
----------------

Minimální funkční šablona je k vidění v sekci „Minimální funkční šablona“.
Dokumentace „Reference / Zprávy / Šablony“. Můžeme upravit tento příklad tak, aby vytvořil
Naše minimální vlastnictví nabízí šablonový soubor:

... blok kódu::xml


<odoo>
<šablona id="nabídka nemovitostí">
<t t-foreach="dokumenty" t-as="vlastnost">


<div class="page">
<h2>



<strong>Očekávaná cena: </strong>


<table class="table">


<th>Cena</th>












</t>
</t>




Většina položek specifických pro Odoo (tj. nejsou HTML) je vysvětlena v části minimálního použitelného šablonu.
Některé další funkce našeho šablony jsou:

* Použití atributu „class="table"“, takže naše tabulka bude mít hezké formátování.
(v tomto případě používáme jeho třídu tabulky), a třídy Font Awesome (použitelné pro přidávání ikon).
může být použita ve vašem šabloně pro zprávy.
* Použijeme „t-set“, „t-value“, „t-foreach“ a „t-as“, abychom mohli procházet všechny „offer_id“.

Pokud už máte zkušenosti s webovými šablonovacími motory, pak jsou pro vás příkazy QWeb (tj. příkazy začínající písmenem „t“),
nepotřebují příliš vysvětlování a stačí se podívat na jejich :ref:`dokumentaci <reference/qweb>`.
přeskočte na další pododstavce.

A jinak vás vyzýváme, abyste se o nich dozvěděli víc.
„Wikipedie“ (viz https://cs.wikipedia.org/wiki/Šablonový_procesor) má dobrý obecný popis, ale
Hlavní myšlenkou je, že QWeb poskytuje schopnost dynamicky generovat webový kód na základě dat Odoo.
jednoduché příkazy. Například QWeb může přistupovat k datům a metodám záznamového souboru a zpracovávat jednoduché programové operace
Například nastavení a přístup k proměnným s dočasným platností. Například v předchozím příkladu:

* „t-set“ vytváří dočasnou proměnnou „nabídky“, jejíž hodnotu nastavuje „t-value“ na aktuální
„seznam nabídek“ v „recordsetu s pozemky“.
* Použití „t-foreach“ a „t-as“ je ekvivalentní k Pythonu:

.. kódový blok:: Python

pro nabídku v nabídkách:

Reportáž z akce
-------------

Nyní máme šablonu, takže ji musíme v aplikaci zpřístupnit pomocí „ir.actions.report“.
Praktickým příkladem funkce „ir.actions.report“ je
„tady <https://github.com/odoo/odoo/blob/0e12fa135882cd5095dbf15fe2f64231c6a84336/addons/event/report/event_event_reports.xml#L20-L30>“
odpovídající
„tento šablonový soubor <https://github.com/odoo/odoo/blob/0e12fa135882cd5095dbf15fe2f64231c6a84336/addons/event/report/event_event_templates.xml#L5>“.
Vše je vysvětleno v dokumentaci :ref:`<reference/actions/report>`.

„Ir.actions.report“ se nejčastěji používá v nabídce „Tisk“ ve zobrazení modelu.
například „binding_model_id“ určuje, které modely mají být zobrazeny v hlášení a Odoo
automaticky vám ho přidá. Další běžným případem použití této akce je propojení s
tlačítko, jak jsme se dozvěděli v :doc:`server_framework_101/09_actions`. Je to užitečné pro zprávy
Které mají smysl pouze v určitých podmínkách. Například když chceme udělat „Finální prodej“.
reportu, pak můžeme připojit tlačítko „Prodejní informace“ k formuláři, které se zobrazí pouze v případě
nemovitost je „prodáno“.

.. obrázek: pdf_reports/tiskove_menu.png

:alt: Tlačítko pro tisk nabídky

Možná jste si všimli nebo se ptáte, proč náš vzor formuláře cykluje přes objekt Recordset. Když
šablona je předána více než jednomu záznamu, může vytvořit jeden PDF report pro všechny záznamy.
Použitím tlačítka „Tisk“ v seznamovém zobrazení s více vybranými záznamy bude možné si toto ověřit.

Podání oznámení
-------------

Nakonec víte, kde vytvářet své soubory a jak by měly vypadat. Šťastné zpracovávání zpráv!

...cvičení: Zpracujte zprávu.

    - Přidejte nabídku nemovitostí z minimální šablony do tiskové nabídky vlastností.

    - Zlepšete zprávu přidáním dalších dat. Podívejte se na **cíl** této části, abyste viděli, co dalšího
data, která můžete přidat a klidně ještě více.

    - Bonus: Přidejte do svého flexibilního reportu nějakou logiku, aby se zobrazily nemovitosti bez nabídky.
Pak se nebudeme snažit vytvořit tabulku, ale napsat něco o tom, že zatím žádné nabídky nemáme. Tip: budete
je třeba použít „t-if“ a „t-else“.

Zkontrolujte, zda jsou vaše PDF reporty v souladu s daty, jaké očekáváte.


Podšablony
=============

.. poznámka::

**Úkol**: Na konci této části budeme mít podšablonu, kterou použijeme ve dvou zprávách.

.. obrázek:: pdf_reporty/report_podsložka.png
:synchronizace: střed
:alt:Report pomocí podšablony

Důvodem použití podšablon je jednak zjednodušení čtení kódu při práci s
dlouhé nebo složité šablony. Druhým je možnost používat kód znovu, kde je to možné. Naše jednoduchá vlastnost nabízí
report je užitečný, ale seznam nemovitostí může být užitečný pro více než jeden šablonový report.
Jedním z příkladů je například report, který uvádí všechny nabídky na nemovitosti prodávajícího.

Zkuste pochopit, jak volat podšablonu, přečtením
Dokumentaci o něm a/nebo podívat se na
„příklad <https://github.com/odoo/odoo/blob/0e12fa135882cd5095dbf15fe2f64231c6a84336/addons/portal/static/src/xml/portal_chatter.xml#L147-L160>“
(QWeb používá stejné kontrolní toky, ať už je to pro zprávu nebo pohled v Odoo).

..cvičení: Vytvořte a použijte podšablonu.

    - Oddělte část nabídky na stůl do vlastního šablony. Nezapomeňte zkontrolovat, že
původní zpráva po opravě stále tiskne správně.

    - Přidejte nový výstup pro „res.users“, který vám umožní tisknout všechny nemovitosti
které jsou viditelné ve svém formuláři (tj. v aplikaci „Nastavení“). Zahrňte nabídky pro každou
z těchto prodejců v téže zprávě. Například: od „binding_model_id“ v této
Pokud se případ nebude nacházet v modulu majetku, budete potřebovat „ref="base.model_res_users"“.

Vaším cílem by mělo být dosáhnout podobného výsledku jako na obrázku v části **Cíl** této sekce.

Nezapomeňte zkontrolovat, že vaše hlášení odpovídají očekávaným datům!

Zpráva o dědictví
==================

.. poznámka::

**Cíl**: Na konci této části zdědíme vlastnost report v „účtu nemovitosti“.
modul.


:synchronizace: střed
:alt: Děděný report

Dědění v QWebu používá stejné „xpath“ prvky jako dědění v :ref:`zobrazeních <reference/view_records/inheritance>“.
Šablona QWeb odkazuje na svůj rodičský šablonu jinak, ještě snadněji lze provést přidáním
atribut „dědičný id“ pro prvek „šablona“ a nastaví jej na hodnotu *modul.parent_template_id*.

Do žádného z modelů vlastnictví v tabulce „majetek“ jsme nepřidali nové pole, ale stále můžeme přidat informace
k našemu stávajícímu vlastnickému průkazu. Například víme, že jakékoliv nemovitosti „prodané“ již budou mít fakturu
vytvořené pro ně, takže můžeme tuto informaci přidat do našeho hlášení.

...cvičení: Dědit zprávu.

    - Rozšíření vlastností zprávy o nějaké informace o faktuře. Můžete se podívat na **cíl** této
sekci pro inspiraci (tj. vytiskněte řádek, pokud je vlastnost hotová, jinak nic nevytiskněte).

Znovu si ověřte, že vaše zprávy odpovídají očekávaným datům!

Doplňkové funkce
===================

Všechny následující doplňkové funkce jsou popsány dále v části :ref:`reference/reports/report`.
dokumentace, včetně návodu k použití každého z nich.

Překlady
------------

Všichni víme, že Odoo je používáno v mnoha jazycích díky automatickému a ručnímu překládání. QWeb reporty nejsou
Výjimka! Pozor, někdy se překlady nezobrazí správně, pokud je v textu zbytečný mezer.
textového obsahu šablony, takže se jim vyhněte, pokud je to možné (zejména přední mezeru).

Zprávy jsou webové stránky.
---------------------

Možná už vás nebaví slyšet, že QWeb vytváří HTML, ale opakujeme to znovu. Jedním z
Pěkné vlastnosti reportů psaných pomocí QWeb je, že lze zobrazit přímo v prohlížeči.
Toto může být užitečné, pokud chcete vložit odkaz na konkrétní zprávu.
obvyklé bezpečnostní kontroly budou stále platit, aby se zabránilo neautorizovaným uživatelům v přístupu k zprávám.

Čárové kódy
--------

Odoo má zabudovaný nástroj pro tvorbu obrázků čárových kódů, díky kterému mohou být čárové kódy vloženy do vašich zpráv.
Podívejte se na odpovídající
„kód <https://github.com/odoo/odoo/blob/0e12fa135882cd5095dbf15fe2f64231c6a84336/addons/web/controllers/main.py#L2044-L2046>“
zobrazit všechny podporované typy čárových kódů.
