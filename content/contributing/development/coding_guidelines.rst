.. výrazně:: had

=================
Pravidla pro psaní kódu
=================

Tato stránka představuje kódovací pravidla Odoo. Ty mají za cíl zlepšit
kvalita kódu aplikací Odoo. Vlastně správný kód zvyšuje čitelnost a usnadňuje
údržba pomáhá při ladění, snižuje komplexnost a podporuje spolehlivost.
Tyto pokyny by měly být aplikovány na každý nový modul a všechny další vývojové aktivity.

.. varování:

Při úpravě stávajících souborů v verzi **stable** se používá původní styl
vždy přednostně používat. Jinými slovy, prosím, nikdy ne
upravit stávající soubory, aby se tyto pokyny aplikovaly. To zabraňuje narušení
historie změn kódu. Dif by měl být co nejmenší.
podrobnosti se dozvíte v našem „návodu k zaslání pull requestu <https://odoo.com/submit-pr>“.

.. varování:

Při úpravách souborů v složce master (vývojová verze) používejte tyto
pouze pro modifikovaný kód nebo pokud je většina souboru
podrobena revizi. Jinými slovy, měnit strukturu souborů pouze v případě, že byla
podstatné změny. V takovém případě proveďte nejprve **přesunutí**, pak aplikujte
změny související s funkcí.

Modulová struktura
================

.. varování:

Pro moduly vyvíjené komunitou je silně doporučeno používat
modul s předponou, například vaším názvem společnosti.

Adresáře
-----------

Modul je uspořádán v důležitých adresářích. Ty obsahují obchodní logiku;
Pokud se na ně podíváte, měli byste pochopit účel modulu.

- *data/*: demo a data xml
- *modelů/*: definice modelu
- *kontroly/*: obsahuje kontrolery (HTTP trasy)
- *pohledy/*: obsahuje pohledy a šablony
- *statické soubory/*: obsahuje webové zdroje oddělené do složek *css/, js/, img/, lib/, ...*.

Další volitelné adresáře tvoří modul.

- *čaroděj/ka*: seskupuje dočasné modely („modely.TransientModel“) a jejich zobrazení
- *report/*: obsahuje tisknutelné zprávy a modely založené na SQL vztazích. V této složce jsou také objekty Pythonu a XML vzorky
- *testy/*: obsahuje testy v Pythonu


Název souboru
-----------

Název souboru je důležitý pro rychlé vyhledání informací v celé řadě doplňků Odoo.
Tato část vysvětluje, jak pojmenovat soubory ve standardním modulu Odoo.
Příkladem je aplikace „Zahradnictví“ (<https://github.com/tivisse/odoodays-2018/tree/master/plant_nursery>).
Zahrnuje dva hlavní modely: *plant.nursery* a *plant.order*.

V případě modelů rozdělte obchodní logiku na skupiny modelů, které patří
stejný hlavní model. Každý set leží v určitém souboru, který je pojmenován podle jeho hlavního modelu.
Pokud existuje pouze jeden model, jeho název je stejný jako název modulu.
dědičný model by měl být vlastním souborem, aby pomohl porozumět tomu, jak byl ovlivněn.
modely.

... blok kódu:: text

addons/zahradnictví/
|-- modely/
|  |-- plant_nursery.py (hlavní model)
|    |-- plant_order.py (další hlavní model)
|  |--res_partner.py (děděný model Odoo)

Co se týče bezpečnosti, měly by být použity tyto hlavní soubory:

- První je definice práv přístupu v souboru `ir.model.access.csv`.
- Skupiny uživatelů jsou definovány v souboru :file:`<modul>_groups.xml`.
- Pravidla záznamu jsou definována v souboru :file:`<model>_security.xml`.

... blok kódu:: text

addons/zahradnictví/
|-- bezpečnost/
|  |-- ir.model.access.csv
|  |-- skupiny_pěstitelských_zahrad.xml
|   |-- zahradnictví_bezpečnost.xml
|  |-- plant_order_security.xml

Co se týče pohledu na zadní stranu, měly by být rozděleny stejně jako modely a končit příponou
„_views.xml“. Zobrazení v zadní části jsou seznamy, formuláře, kanban, aktivity, grafy, pivota, …
pohledů. K rozdělení pomocí modelu v pohledech hlavní nabídky nejsou propojeny s konkrétními akcemi
mohou být extrahovány do volitelného souboru „<modul>_menus.xml“. Šablony (QWeb
stránky, které jsou určeny pro zobrazení portálu/webové stránky, se ukládají do samostatných souborů s názvem
„<model>_templates.xml“.

... blok kódu:: text

addons/zahradnictví/
|-- pohledy/
|  | - plant_nursery_menus.xml (volitelná definice hlavních menu)
|  | - plant_nursery_views.xml (zadní pohledy)
|  | - plant_nursery_templates.xml (portálové šablony)
|  | - plant_order_views.xml
|  | - plant_order_templates.xml
|  | - res_partner_views.xml

V případě dat je nutné je rozdělit podle účelu (demonstrační nebo data) a hlavního modelu. Pro názvy souborů
bude hlavním modelem jméno s příponou "_demo.xml" nebo "_data.xml". Například
pro aplikaci s demem a daty pro hlavní model i podtypy
aktivity a šablony e-mailů související s modulem pošty:

... blok kódu:: text

addons/zahradnictví/
|-- data/
|  |-- plant_nursery_data.xml
|   |-- plant_nursery_demo.xml
|  |-- mail_data.xml

Co se týče kontrolerů, obecně všichni kontrolerové patří do jednoho kontroleru.
obsahující soubor s názvem „<modul_jmeno>.py“. Stará konvence v Odoo je
Nezapomeňte pojmenovat tento soubor „main.py“, ale je považován za zastaralý. Pokud potřebujete dědit
existujícího modulu z jiného modulu v „<název děděného modulu>.py“.
Příkladem je přidání portálového kontroleru do aplikace v souboru „portal.py“.

... blok kódu:: text

addons/zahradnictví/
|-- kontroler/
|  |-- plant_nursery.py
|  |-- portal.py (dědící z portálu/kontrolerů/portál.py)
|  |-- hlavní.py (zastaralý, nahrazený souborem plant_nursery.py)

Konkrétně u statických souborů se chová JavaScript stejně jako
Pythonové modely. Každý komponent by měl být v samostatném souboru s významným názvem.
Například v modulu pošty jsou widgety aktivit umístěny v souboru „activity.js“.
Podsložky mohou také sloužit k uspořádání „balíčku“ (viz modul web).
podrobněji (pro více informací). Logika by měla být stejná i u šablon v Javě
widgety (statické XML soubory) a pro jejich styly (soubory SCSS). Neodkazujte
data mimo Odoo (obrázky, knihovny): nevyužívejte URL obrázku, ale kopírujte
do kódu namísto toho.

Pro *čaroděje* je pojmenování stejné jako pro modely v Pythonu:
„<transient>.py“ a „<transient>_views.xml“. Oba soubory se umísťují do průvodce
adresář. Toto pojmenování pochází z aplikací staré verze Odoo, které používaly průvodce
klíčové slovo pro přechodné modely.

... blok kódu:: text

addons/zahradnictví/
|-- wizard/
|  |-- make_plant_order.py
|  |-- make_plant_order_views.xml

V případě statistických výstupů vytvořených pomocí Pythonu/SQL a klasické zobrazení
Název je následující:

... blok kódu:: text

addons/zahradnictví/
|--report/
|  |-- plant_order_report.py
|  |-- zprávy_o_řádu_rostlin.xml

V případě tisknutelných zpráv, které obsahují především zpracování dat a Qweb
Název šablon je následující:

... blok kódu:: text

addons/zahradnictví/
|--report/
|  |-- plant_order_reports.xml (akce, papírová podoba, ...)
|  |-- plant_order_templates.xml (reportovací šablony v XML)

Takže kompletní strom našeho modulu v Odoo vypadá takto

... blok kódu:: text

addons/zahradnictví/
|-- __init__.py
|-- __manifest__.py
|-- kontroler/
|  |_ __init__.py
|  |-- plant_nursery.py
|  |--portal.py
|-- data/
|  |-- plant_nursery_data.xml
|   |-- plant_nursery_demo.xml
|  |-- mail_data.xml
|-- modely/
|  |_ __init__.py
|  |-- plant_nursery.py
|  |-- plant_order.py
|  |--res_partner.py
|--report/
|  |_ __init__.py
|  |-- plant_order_report.py
|  |-- zprávy_o_řádu_rostlin.xml
|  |-- plant_order_reports.xml (akce, papírová podoba, ...)
|  |-- plant_order_templates.xml (reportovací šablony v XML)
|-- bezpečnost/
|  |-- ir.model.access.csv
|  |-- skupiny_pěstitelských_zahrad.xml
|   |-- zahradnictví_bezpečnost.xml
|  |-- plant_order_security.xml
|-- statické soubory/
|    |--img/
|   |   |-- my_little_kitten.png
|   |   |-- troll.jpg
|    |-- lib/
|   |   |-- externí knihovna
|   |-- src/
|  |  |-- js/
|  |  |  |  |-- widget_a.js
|  |  |  |  | -- widget_b.js
|   |   |-- sass/
|   |   |   |-- widget_a.scss
|  |  |  | -- widget_b.scss
|   |   |-- xsl/
|   |   |   |-- widget_a.xml
|   |   |   |-- widget_a.xml
|-- pohledy/
|  |-- sazenice_menu.xml
|  |-- plant_nursery_views.xml
|  |-- šablony pro pěstírny rostlin (plant_nursery_templates.xml)
|   |-- pohledy_řádu_rostlin.xml
|  |-- šablony prořezů rostlin (plant_order_templates.xml)
|   |-- res_partner_views.xml
|-- wizard/
|  |--make_plant_order.py
|  |--make_plant_order_views.xml

.. poznámka: Názvy souborů by měly obsahovat pouze „[a-z0-9_]“ (malá písmena).
alfanumerické a „_“

Upozornění: Používejte správné oprávnění souborů a složek: pro složku 755 a pro soubor 644.

... přispívání/vývoj/XML-návod:

XML soubory
=========

Formát
------

Pro vyhlášení rekordu v XML je doporučeno použít notaci záznamu (**record** pomocí značky *<record>*):

- Před „model“ umístěte atribut „id“.
- Pro pole deklarace je první atribut „name“. Pak umístěte
*hodnota* buď v poli „field“, nebo v hodnotě „eval“
atribut a nakonec další atributy (widget, možnosti, ...).
seřazené podle důležitosti.

- Zkuste seskupit záznamy podle modelu. V případě vzájemných závislostí
Pokud je v akci/menu/výhledu nějaká konvence, která se tímto pravidlem řídí, pak by tato konvence neměla být aplikována.
- Použijte pojmenování definované v následujícím bodě
- Tag *<data>* se používá jen k nastavení neaktualizovatelných dat pomocí „noupdate=1“.
Pokud je v souboru pouze neaktualizovatelná data, lze zadat „noupdate=1“.
je nastaven na značce „<odoo>“ a neobsahuje značku „<data>“.

... blok kódu::xml

<zaznamenání id="view_id" model="ir.ui.view">
<pole název="name">view.name</pole>
<položka jméno="model">objekt_jméno</položka>
<field name="priorita" eval="16"/>
<položka jméno="arch" typ="xml">
<seznam>
<pole název="my_field_1"/>

</seznam>
</p>
</záznam>

Odoo podporuje vlastní značky, které fungují jako syntaktická cukr:

- menuitem: použijte jej jako zkratku k vyhlášení „ir.ui.menu“
- Šablona: použijte ji k vyhlášení QWebView, který vyžaduje pouze část „arch“ zobrazení.

Tyto značky jsou přednostnější než poznámka *record*.


XML identifikátory a pojmenování
------------------

Bezpečnost, Pohled a Akce
~~~~~~~~~~~~~~~~~~~~~~~~~

Využijte následující vzor:

* Pro menu: :samp:`{<model_name>}_menu`, nebo :samp:`{<model_name>}_menu_{do_stuff}` pro podmenu.
* Pro pohled: :samp:`{<model_name>}_view_{<view_type>}`, kde *view_type* je
„Kanban“, „Formulář“, „Seznam“, „Hledání“...
* Pro akci: hlavní akce respektuje:samp:`{<model_name>}_action`.
Další jsou označeny znakem samp:_<podrobnosti>, kde <podrobnosti> je
nízké písmeno, které stručně vysvětluje akci. Toto je používáno jen tehdy,
Veškeré akce jsou pro model deklarovány.
* Pro akce na okně: přidejte k názvu akce informace o konkrétním pohledu.
jako například:samp:`{<model_name>}_action_view_{<view_type>}`
* Pro skupinu: :samp:`{<modul_jmeno>}_skupina_{<skupina_jmeno>}` kde *skupina_jmeno*
Jméno skupiny je obvykle „uživatel“, „správce“ apod.
* Pro pravidlo: :samp:`{<název modelu>}_rule_{<skupina, která se týká>}` kde
*znepokojená skupina* je zkrácený název pro skupinu „uživatel“
pro „model_name_group_user“, „veřejný“ pro veřejného uživatele a „firma“.
pro více společností (...),

Název by měl být stejný jako identifikátor XML s tečkami místo podtržítka. Akce
mělo by mít skutečné jméno, protože se používá jako zobrazované jméno.

... blok kódu::xml

<!-- pohledy  -->
<záznam id="názvového pohledu formuláře" model="ir.ui.view">
<políčko jméno="název">model.název.zobrazení.formulář</políčko>
        ...
</záznam>

<záznam id="názvového pohledu kanban" typu="ir.ui.view">
<field name="name">model.name.view.kanban</field>
        ...
</záznam>

<!-- akce -->
<záznam id="název_modelu_akce" model="ir.act.window">
<pole název="název">Hlavní akce</pole>
        ...
</záznam>

<záznam id="název_akce_dítě_seznam" model="ir.actions.act_window">
<pole jméno="název">Přístup ke dětem modelu</pole>
</záznam>

<!-- menu a podmenu -->
<menuitem
id="model_name_menu_root"
name="Hlavní menu"
pořadí="5"
    />
<menuitem
id="název modelu menu/akce"
name="Podmenu 1"
rodič="modul_jmeno.modul_jmeno_menu_kořen"
akce="model_name_akce"
sekvence="10"
    />

<!-- bezpečnostní opatření -->
<záznam id="modul_jméno_skupina_uživatel" typu="res.groups">
        ...
</záznam>

<záznam id="název_pravidla_veřejného" model="ir.rule">
        ...
</záznam>

<záznam id="název-firmy-pravidlo" typu="ir.rule">
        ...
</záznam>

Dědění XML
~~~~~~~~~~~~~~

XML identifikátory děděných pohledů by měly používat stejný identifikátor jako originální záznam.
Pomáhá najít všechny dědictví na jediný pohled. Konečné identifikátory XML jsou předponovány
Moduly, které je vytvářejí, se nesetkávají.

Název by měl obsahovat příponu „.inherit.{podrobnosti}“, aby bylo snadnější pochopit
překrývá svým názvem účel, na který se díváme.

... blok kódu::xml

<záznam id="model_view_form" model="ir.ui.view">
<field name="název">model.view.form.dědictví.modul2</field>

        ...
</záznam>

Nové primární pohledy nevyžadují přídavný znak „inherit“, protože jsou novými záznamy
je založen na prvním.

... blok kódu::xml

<záznam id="modul2.model_view_form" model="ir.ui.view">
<field name="name">model.view.form.modul2</field>

<field name="mode">primární</field>
        ...
</záznam>

... přispívání/vývoj/pravidla pro Python:

Python
======

.. varování:

Nezapomeňte si přečíst :ref:`Pitvy bezpečnosti <reference/security/pitfalls>`.
i sekci, kde se píše bezpečný kód.

Možnosti PEP8
------------

Použití linteru může pomoci ukázat varování nebo chyby v syntaxi a semantice.
Zdrojový kód se snaží respektovat standard Pythonu, ale některé z nich lze ignorovat.

- E501: linka příliš dlouhá
- E301: očekávalo se 1 prázdné řádky, nalezeno bylo 0
- E302: očekával jsem dvě prázdné řádky, ale našel jsem jen jeden.

Dovoz
-------

Do země se objednávají

#. Externí knihovny (jedna na řádek, seřazené a rozdělené v python standardní knihovně)
#Do Česka se dováží „odoo“
#. Import modulů z Odoo (vzácně a pouze pokud je nutné).

V těchto 3 skupinách jsou importované linky řazeny abecedně.

... kódový blok:: python

    # 1: dovoz modulů Python
importujte base64
import re
import time
od datetime import datetime
    # 2. dovoz odoo
importujte odoo
od odoo importuje se příkazy, podtržítky, API, pole a modely
z odoo.tools.safe_eval import safe_eval jako eval
    # 3: dovoz z odoo přídavků
od odoo.addons.web.controllers.main import login_redirect
od odoo.addons.web.models.website import slug

Idiomatika programování (Python)
----------------------------------

- Vždy dávejte přednost čitelnosti před stručností nebo použitím jazykových funkcí či idiomů.
- Nepoužívejte „.clone()“.

... kódový blok:: python

    # špatný
nový_složkový_seznam = seznam_my_dict.kopie
nový_seznam = starý_seznam.copy()
    # dobrý
nový_seznam = seznam(my_seznam)
nový_seznam = seznam(starý_seznam)

- Pythonová slovníková databáze: vytváření a aktualizace

... kódový blok:: python

    # -- vytvoření prázdného seznamu
my_dict = {}
my_dict2 = {}

    # -- tvorba s hodnotami
    # špatný
my_dict = {}
my_dict['foo'] = 3
my_dict['bar'] = 4
    # dobrý
my_dict = {'foo': 3, 'bar': 4}

    # -- aktualizovat slovník
    # špatný
my_dict['foo'] = 3
my_dict['bar'] = 4
my_dict['baz'] = 5
    # dobrý
my_dict.update({'foo': 3, 'bar': 4, 'baz': 5})
my_dict = dict(my_dict, **my_dict2)

- Používejte významná jména proměnných, tříd a metod
- Nepoužitá proměnná: Dočasné proměnné mohou kód zjednodušit tím, že dávají
jména na objekty, ale to neznamená, že byste měli vytvářet dočasné proměnné
vždycky:

... kódový blok:: python

    # bezpředmětné
schema = kw["schema"]
params = {'schema': schema}
    # jednodušší
params = {'schema': kw['schema']}

- Opakované návratové body jsou v pořádku, pokud jsou jednodušší

... kódový blok:: python

    # trochu složitá a s nepotřebnou proměnnou pro dočasné uložení
def axes(self, osa):
osy = []
pokud je typ osy stejný jako u pole,
osy = axis
jinak:
osy.append(osu)
vrací osy

     # jasnější
def axes(self, osa):
pokud je typ osy stejný jako u pole,
vrátí seznam (osy) # klonuje osy
jinak:
vrací seznam s jediným prvkem

- Znalost základních funkcí: Měli byste mít alespoň základní povědomí o všech
vlastní funkce Pythonu (http://docs.python.org/library/functions.html)

... kódový blok:: python

value = my_dict.get('key', None) # velmi velmi zbytečné
value = my_dict.get('key') # dobré

A také „jestliže 'klíč' v my_dict“ a „jestliže my_dict.get('klíč')“ jsou velmi odlišné
Význam je důležitý, takže si dejte pozor na správný výběr.

- Naučte se používat seznamové výrazy: Použijte seznamový výraz, slovníkový výraz a
základní operace pomocí „map“, „filter“, „sum“ atd. Tyto operace dělají kód
Je snadněji čitelný.

... kódový blok:: python

    # ne příliš dobrý
cube = []
for i v řadě rez:
cube.append((i['id'], i['name']))
    # lepší
cube = [(i['id'], i['name']) pro i v res]

- Sbírky jsou také booleovými hodnotami: V Pythonu má mnoho objektů „booleovou“ hodnotu
když jsou hodnoceny v kontextu logických výrazů (například v příkazech if). Mezi ně patří kolekce
(seznamy, diktáty, sady, ...), které jsou „nepravdivé“ prázdné a „pravdivé“, pokud obsahují
položky:

... kódový blok:: python

bool([]): je False
bool([1]) je pravdivé
bool([False]) je True

Takže můžete napsat „pokud nějaká_sada:“ místo „pokud délka(nějaká_sada):“.


- Opakujte se na opakovatelných objektech

... kódový blok:: python

    # vytvoří dočasný seznam a zkontroluje, jestli je v něm
for klíč v seznamu klíčů my_dict:
„udělat něco...“
    # lepší
for klíč v my_dict:
„udělat něco...“
    # přistupování k klíč-hodnotové dvojici
for klíč, hodnotu v seznamu my_dict.items():
„udělat něco...“

- Použijte funkci setdefault

... kódový blok:: python

    # delší... těžší na čtení
hodnoty = {}
pro prvek v iterátoru:
pokud se hodnota elementu nevyskytuje v hodnotách:
hodnoty[element] = []
hodnoty[element] += další_hodnota

    # lepší... použijte metodu setdefault
hodnoty = {}
pro prvek v iterátoru:
values.setdefault(element, []).append(other_value)

- Jako dobrý programátor dokumentujte svůj kód (docstring u metod, jednoduché
komentáře k problematickému kódu).
- Kromě těchto pokynů můžete najít také následující odkaz
zajímavé: https://david.goodger.org/projects/pycon/2007/idiomatic/handout.html
(trochu zastaralé, ale velmi aktuální)

Programování v Odoo
-------------------

- Vyhněte se vytváření generátorů a dekorátorů, používejte jen ty, které jsou poskytovány
Odoo API.
- Jako v Pythonu použijte metody „filtrované“, „mapované“, „seřazené“ atd.
zlepšit čitelnost kódu a jeho výkon.

Propagujte kontext
~~~~~~~~~~~~~~~~~~~~~

Kontext je „zmrzlý slovník“, který nelze měnit. Chcete-li volat metodu
jiném kontextu by měla být použita metoda „s kontextem“:

... kódový blok:: python

records.s novým kontextem().dělat věci() # všechen kontext je nahrazen
records.s kontextem (**přidané_kontexty).vykonat_další_akce() # hodnoty přidaného kontextu představují výchozí hodnoty

.. varování:
Přenášení parametru v kontextu může mít nebezpečné vedlejší účinky.

Protože hodnoty se šíří automaticky, může se objevit nějaké neočekávané chování.
Voláním metody „create()“ modelu s klíčem *default_my_field* v kontextu
nastaví výchozí hodnotu pole my_field pro daný model.
Ale pokud se během tvorby objeví jiné objekty (například prodejní objednávka a její linie),
Pokud do pole s názvem *my_field* vložíte nějaký obsah, bude mít i výchozí hodnotu.

Pokud potřebujete vytvořit klíčový kontext ovlivňující chování nějakého objektu
Vyberte dobré jméno a nakonec přidejte název modulu.
izolovat její dopad. Příkladem jsou klávesy modulu „Pošta“:
*mail_create_nosubscribe*, *mail_notrack*, *mail_notify_user_signature*, ...

Myšlenka prodloužitelnosti
~~~~~~~~~~~~~~~~

Funkce a metody by neměly obsahovat příliš mnoho logiky: měly by být co nejmenší.
a jednoduché metody jsou vhodnější než málo velkých a složitých metod.
Dobré pravidlo je rozdělit metodu, jakmile bude mít více než jednu
zodpovědnost (viz http://cs.wikipedia.org/wiki/Zásada_jediného_zadavatele).

Kódování byznysové logiky do metody se vyhýbejte, protože zabraňuje
snadno rozšiřitelný pomocí podmodulu.

... kódový blok:: python

    # Nebuďte takoví.
    # změna domény nebo kritérií znamená přepsání celé metody
def action(self):
...  # dlouhý metod
partneři = self.env['res.partner'].search(komplexní doména)
e-mailové adresy = filtrované partnerství (pomocí libovolných kritérií) a zobrazení e-mailové adresy

    # lepší, ale taky ne.
    # Změna logiky silně ovlivňuje duplikaci částí kódu.
def action(self):
        ...
partneři = self._get_partnerů()
emaily = partneři._get_emails()

    # lepší
    # minimální přehrávání
def action(self):
        ...
partneři = self.env['res.partner'].vyhledat(self._získání domény partnera)
e-maily = partners.filtrované(lambda r: r._filter_partners()).map('e-mail')

Následující kód je nadbytečný pouze pro ilustraci, ale čitelnost
Musí se zvážit a vyvážit.

Dále pojmenujte své funkce podle pravidel: malé a správně pojmenované funkce
začátek čitelného a udržovatelného kódu a pevnější dokumentace.

Tato doporučení jsou také platná pro třídy, soubory, moduly a balíčky.
(Více viz http://cs.wikipedia.org/wiki/Kyklomatická_komplexita)

Nikdy neprovádějte transakci
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Odoo framework je zodpovědný za poskytování transakčního kontextu pro
všechny volání metody RPC. Princip je takový, že při každém volání metody
na začátku každé volání RPC a závazně se vrací při návratu volání.
před přenosem odpovědi klientovi RPC nějak takto:

... kódový blok:: python

def execute(self, db_name, uid, obj, metoda, *args, **kw):
db, pool = pooler.get_db_and_pool(db_name)
        # Vytvořit transakční kurzor
cr = db.cursor()
pokus:
res = pool.spustit_cr(cr, uid, obj, metoda, *args, **kw)
cr.commit() # vše je v pořádku, zavoláme metodu commit
kromě výjimky Exception:
cr.rollback() # chyba, vrátit všechno zpět
zvednout
Konečně:
cursor.close() # vždy zavřít kurzor, který byl otevřen ručně
vrací se hodnota res

Pokud dojde k chybě při provádění RPC volání, transakce
a vrátit se zpět do původního stavu systému.

Podobně systém nabízí i samostatnou transakci při provedení
testovacích sad, takže ji lze vrátit nebo nevrátit podle serveru
startupové možnosti.

Důsledkem je, že pokud ručně zavoláte metodu „cr.commit()“ kdekoliv,
velmi vysoká pravděpodobnost, že narušíte systém různými způsoby, protože
budou způsobovat částečné zavádění a tím i nečisté obnovy.
Mezi nimi například:

#nepřesné obchodní údaje, obvykle ztráta dat
#.synchronizace pracovních postupů, dokumenty zaseknuté natrvalo
#testy, které nelze vrátit zpět čistě a začnou znečišťovat
databáze a spouštění chyby (i když žádná chyba nevyskytne).
v průběhu transakce

Tady je velmi jednoduchá pravidla:
Nikdy byste neměli volat metodu „cr.commit()“ sami, **KROMĚ TOHO**, že
Vytvořili jste si vlastní databázový kurzor explicitně! A situace, kdy se
Tyto věci jsou výjimečné.

A pokud jste si vytvořili vlastní kurzor, pak musíte s ním zacházet
chybových případů a správného obnovení, stejně jako řádně uzavřít kurzor.
máte hotovo.

A na rozdíl od obvyklého názoru vám ani nemusíte volat „cr.commit()“.
v následujících situacích:
- v metodě „_auto_init()“ objektu třídy „models.Model“:
případně o něj pečuje metoda inicializace doplňků nebo transakce v ORM.
Vytváření vlastních modelů
- v zprávách: „zavázat se“ je také vyřešeno rámcem, takže můžete
aktualizovat databázi i z uvnitř hlášení
- v metodách modelu Transient: tyto metody se volají přesně tak, jak
běžné modely. Modely v rámci transakce a s odpovídajícím
„cr.commit()/rollback()“ na konci
- atd. (viz obecné pravidlo výše, pokud máte pochybnosti!).

Všechny „cr.commit()“ volání mimo rámec serverového framework musí být
mít **konkrétní komentář** vysvětlující, proč jsou naprosto nezbytné,
Ano, jsou správné a proč je nezastaví. Jinak
Budou odstraněny!

Používejte metodu překladu správně
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Odoo používá metodu podobnou GetTextu nazvanou „underscore“ (`_()`) k označení toho,
Statická proměnná používaná v kódu musí být překládána při spuštění.
Tento způsob je k dispozici v „self.env._“ pomocí jazyka
environmentální.

Používání této látky je spojeno s několika velmi důležitými pravidly, které musí být dodrženy, aby se zabránilo
práci a vyhnout se plnění překladů zbytečným odpadem.

Základní metoda by měla být používána jen pro statické řetězce psané ručně
V kódu nebude fungovat překlad hodnot polí, jako jsou názvy produktů.
atd. To se dělá místo toho použitím vlajky přeložení na příslušném
pole.

Metoda přijímá nepovinný pozice nebo pojmenovaný parametr.
Pravidlo je velmi jednoduché: volání metody podtržítka by měla být v
tvar „self.env._(literální řetězec)“ a nic jiného:

... kódový blok:: python

_ = self.env_.

    # dobré: jednoduché struny
error = 'Tento záznam je uzamčen!'

    # dobrý: řetězce s formátovacími vzorci
chyba = _('Záznam %s nelze upravit!', record)

    # i toto: vícřádkové literální řetězce
chyba = _("Toto je špatný příklad vícřádkového textu
O rekordu %s!""", rekord)
chyba = _('Záznam %s nelze upravit')
po ověření!“, zaznamenal.

    # špatné:Pokusí se přeložit po formátování řetězce
    #      ((pozor na závorky!))
    # Tohle nefunguje a překlad zkazí.
chyba = _('Záznam %s nelze upravit!') % record

    # špatné: formátování mimo překlad
    # Toto se nebude týkat záložního mechanizmu v případě špatného překladu
chyba = _('Záznam %s nelze upravit!') % record

    # špatně: dynamické řetězce, řazení řetězců atd. jsou zakázány!
    # Tohle nefunguje a překlad zkazí.
error = _("""" + que_rec["question"] + "\"\n")

    # špatné: hodnoty pole jsou automaticky přeloženy rámcovou knihovnou
    # Je to k ničemu a nebude fungovat tak, jak si myslíte:
chyba = _("Produkt %s je vyprodaný!") % _(produkt.jméno)
    # A následující samozřejmě nebude fungovat, jak bylo již vysvětleno:
error = _("Zboží %s je vyprodáno!" % produkt.jméno)

    # Místo toho můžete provést následující a vše bude přeloženo.
    # včetně názvu produktu, pokud je jeho pole definováno jako
    # přeložit vlajku správně nastavenou:
chyba = _("Produkt %s není k dispozici!" , produkt.jméno)


Dále si také uvědomte, že překladatelé budou muset pracovat s přesnými hodnotami
které jsou předány funkci __, takže se pokuste je udělat snadno
pochopit a udržet falešné znaky a formátování na minimu.
musí být vědomi formátovacích vzorců jako „%%s“ nebo „%%d“, nových řádků atd.
je nutné zachovat, ale je důležité tyto používat rozumně a zřetelně
mánii:

... kódový blok:: python

    # Špatné: Ztěžuje práci s překlady
error = "'" + otázka + _("' \nProsím zadejte celé číslo.

    # Ok (dbejte na umístění závorek také!).
chyba = _("Odpověď na otázku číslo %s není platná.\n"
"Prosím zadejte celé číslo.", otázka)

    # Lepší
chyba = _("Odpověď na otázku %(title)s není platná.\n")
"Prosím zadejte celé číslo."

V obecném případě v Odoo se při práci s řetězci raději používá „%“ než „.format()“.
a místo toho používejte „%(varname)“.
z pozice (když se musí nahradit více proměnných). To dělá
překlad pro komunitní překladatelé snadnější.

Symboly a zásady
-----------------------

- Název modelu (s notací tečkou, předponou modulu):
    - Při definování modelu Odoo použijte jednotné číslo jména (např. *res.partner*)
a *prodej.objednávka* místo *dodavatelé.část* a *prodej.objednávky*).
    - Při definování Odoo transientu (průvodce): použijte „<related_base_model>.<akce>“
kde *related_base_model* je základní model (definovaný v adresáři *models/*), který je s tímto modelem spojen.
k přechodnému a *akce* je krátký název pro to, co dělá přechodný. Vyhněte se slovu „mág“.
Například: „účet.faktura.vytvořit“, „projekt.úkol.předat.soubor“, …
    - Při definování modelu reportu (*report*) (např. SQL vhledů): použijte
„<související základní model>.report.<akce>“, založené na konvenci Transient.

- Odoo Python Class: používejte CamelCase (objekt orientovaný styl).


... kódový blok:: python

class AccountInvoice(models.Model):
        ...

- Proměnná jméno:
    - Používejte velká písmena pro proměnné modelu.
    - Používejte podtržené nízké písmeno pro běžné proměnné.
    - Přidejte ke svému proměnnému jméno *_id* nebo *_ids*, pokud obsahuje záznamové ID nebo seznam ID. Nemělo by být použito „partner_id“, aby se zobrazila hodnota res.partner

... kódový blok:: python

Partner = self.env['res.partner']
partneři = Partner.prohledat(idy)
partner_id = partners[0].id

- Pole „one2many“ a „many2many“ by měla mít vždy na konci příponu *_ids* (příklad:sale_order_line_ids).
- Pole „Many2One“ by měla mít jako příponu *_id* (příklad: partner_id, uživatelský_id, ...).
- Metodické konvence
    - Metoda počítání: vzor metody je *_počítat_<název pole>*
    - Vyhledávací metoda: Vzor pro vyhledání je *_vyhledávání_<název pole>*
    - Výchozí metoda: Vzor výchozí metody je *_default_*_<název položky>.
    - Metoda výběru: vzor metody výběru je *_vybírání_*
    - Metoda onchange: Vzor metody onchange je *_onchange_<název pole>*
    - Metoda omezení: vzor metody omezení je *_check_<omezení_jméno>*
    - Metoda akce: metoda akce je předponována *action_*
Používá totiž pouze jednu tabulku, takže přidejte „self.ensure_one()“
na začátku metody.

- V atributu model by měl být
    #Soukromé atributy („_name“, „_description“, „_inherit“, „_sql_constraints“, …)
    #. Výchozí metoda a „default_get“
    #.Deklarace pole
    #Metody počítání, inverze a vyhledávání v stejném pořadí jako deklarace pole
    #Metoda výběru (metody používané k návratu hodnot vypočítaných pro pole výběru).
    #Omezuje metody („@api.constrains“) a metody při změně hodnoty („@api.onchange“).
    #Metody CRUD (převzaté metody ORM).
    #Metody akce
    #A nakonec jiné obchodní metody.

... kódový blok:: python

class Event(models.Model):
        # Soukromé atributy
_name = 'event.event'
_description = 'Akce'

        # Výchozí metody
def _default_name(self):
            ...

        # Oznámení o polích
jméno = pole.Char(string="Jméno", výchozí hodnota = _výchozí_jméno)
reserved_seats = fields.Integer('Rezervovaná místa', string='Reserved Seats',
readonly=True, počítá se v metodě _compute_seats)
dostupné_místo = pole.Integer('Dostupná místa', uložit=True
readonly=True, počítá se v metodě _compute_seats)
cena = fields.Integer(string='Cena')
typ_události = pole.Výběr (string="Typ", výběr='_vyber_typ')

        # vypočítat a prohledávat pole stejným způsobem jako pole deklarovaná
@api.depends('seats_max', 'registration_ids.state', 'registration_ids.nb_register')
def _vypočítat_mandáty(self):
            ...

@ApiModel
def __typ_vybraného(self):
vrací seznam

        # Omezení a změny
@api.vztahuje('seats_max','seats_available')
def _check_seats_limit(self):
            ...

@api.onchange('datum_začátku')
def __onchange_date_begin__(self):
            ...

        # Metody CRUD (a name_search, _search, ...) převezmou
def __init__(self, values):
            ...

        # Metody akce
def validate(self):
self.zajistit_jednu()
            ...

        # Obchodní metody
def mail_user_confirm(self):
            ...

... přispívat/vývoj/js_pravidla:

Javascript
==========

Organizace statických souborů
-------------------------

Odoo přidružené aplikace mají některá pravidla, jak strukturovat různé soubory. Vysvětlíme
jak by měly být uspořádány webové aktiva.

První věc, kterou byste měli vědět, je, že server Odoo bude poskytovat (staticky) všechny soubory.
umístěné v adresáři „*statické/*“, ale s předponou názvu doplňku. Například
Pokud je soubor umístěn v adresáři *addons/web/static/src/js/some_file.js*, pak bude
staticky dostupný na adrese URL *vaše-odoo-server.com/web/static/src/js/nějaký_soubor.js*

Konvence je organizovat kód podle následující struktury:

- *statické soubory*: všechny statické soubory

  - *static/lib*: tady by měly být umístěny js knihovny v podadresáři.
Takže všechny soubory knihovny jQuery jsou v adresáři addons/web/static/lib/jquery
  - *statické zdroje*/zdrojový kód*: obecný adresář s názvem statický zdroj

    - *static/src/css*: všechny soubory CSS
    - *statické/písmo*
    - *statické obrázky*
    - *statické/zdrojové soubory JS*

      - *statické/zdrojové soubory js/tour*: uživatelské soubory s průvodci (návody, ne testy)

    - *static/src/scss*: soubory s příponou .scss
    - *statické/zdrojové soubory XML*: všechny šablony QWeb, které budou vykresleny v JavaScriptu

  - *statické/testy*: zde ukládáme všechny soubory týkající se testů.

    - *statické soubory/testy/tour*: zde ukládáme všechny soubory testů pro turnaje (ne tutoriály).

Pravidla pro kódování v JavaScriptu
----------------------------

- „použijte přísný režim“ je doporučeno pro všechny soubory JavaScript
- Použijte linter (jshint, ...).
- Nikdy nepřidávejte minifikované knihovny JavaScriptu
- Používejte CamelCase pro deklaraci třídy

Přesnější pokyny pro JS jsou podrobně popsány v „github wiki <https://github.com/odoo/odoo/wiki/Javascript-coding-guidelines>“.
Můžete se také podívat na existující API v JavaScriptu, pokud zadáte do vyhledávače „Javascript“.
Seznam použité literatury.

... _přispívání/kódování_směrnicích/sass:

CSS a Sass
============

... _přispívat/kódovat_směrnice/sass/formátování:

Syntax a formátování
---------------------

.. záložky::

... kódový blok:: HTML SCSS

.o_foo, .o_foo_bar, .o_baz {
výška: $o-statusbar-height;

.o_qux {
výška: $o-statusbar-height * 0.5;
         }
      }

.o_corge {
pozadí: $o-list-footer-bg-color;
      }

.. kódová tabulka:: css

.o_foo, .o_foo_bar, .o_baz {
výška: 32 px;
      }

.o_foo .o_quux, .o_foo_bar .o_quux, .o_baz .o_qux {
výška: 16 px;
      }

.o_corge {
pozadí: #EEEEEE;
      }

- čtyři (4) mezerové odsazení, žádné tabulátory.
- sloupce maximálně široké 80 znaků;
- otevírací závorka (`{`): prázdný prostor za posledním selektorem;
- Zavírací závorka („}“): na nové řádky.
- jedna řádka na každou deklaraci.
- smysluplné využití mezer.

.. spoiler::Návrhová nastavení pro Stylelint

... blok kódu:: html

„stylelint.config“: {
„pravidla“:
              // https://stylelint.io/user-guide/rules

              // Avoid errors
"blokování prázdných řádků": true,
"kratší varianta vlastnosti bez opakujících se hodnot": true
"deklarace-bloku-bez-zjednodušených-vlastností-překrývá-vlastnosti": true,

              // Stylistic conventions
„výřez“: 4

„funkce, čárka, mezera za ní“: „vždy“,
"funkce-ve-závorkách-vnitřní-mezera": "nikdy",
„funkční mezera po funkci“: „vždy“,

„jednotka“: „snížená“,

"hodnota-seznamu-oddělovač-mezera-po-zadejte": "vždy jedna řádka",

„Prohlášení – běžný mezerový oddíl po“: „Nikdy“,
„vyhlášení-zavináč-mezera-před“: „vždy“,
„Deklarace – mezeru za tečkou:“ „Vždy“,
„declaration-colon-space-before“: „Nikdy“,

"blok-uzavírací-závorka-prázdná-řádka-před": "nikdy",
"blokový odstavec s mezerou před otevřeným závorkovým blokem": "vždy",

"selector-attribute-brackets-space-inside": "nikdy",
"selektor-seznam-oddělovač-mezera-po-zadejte": "vždy jedna řádka",
"selector-list-comma-space-before": "nikdy-jednořádkový",
          }
      },

... _přispívat/kódovat_směrnice/sass/vlastnosti_pořadí:

Pořadí nemovitostí
----------------

Zadávejte vlastnosti z „venku“ dovnitř, začínat od pozice a končit dekorativními pravidly
(např. font, filtr atd.)

:ref:`Sklopené proměnné v SCSS <přispívat/kódování_směrnic/scss/sklopené_proměnné_v_scss>“
:ref:`Proměnné CSS <contributing/coding_guidelines/scss/css_variables> musí být umístěny na začátku
v horní části a následuje prázdná řádka oddělující je od ostatních deklarací.

.. kódový blok:: html

.o_element {
-vnitřní mezera: šířka hrany + mezera pod legendou

--element-margin: 1rem;
--plocha-prvek: 3 rem;

@include o-položka-absolutní(1rem);
zobrazení: blok;
okraj: var(--element-margin);
šířka: vypočítaná hodnota (--element-size) + vnitřní mezera (${-$inner-gap});
hranice: 0;
hrana: 1 rem;
pozadí: modré;
font-size: 1rem;
filtr: rozmazání (2 px);
   }

... /přispívat/kódovat/sass/nazývání konvencí:

Název konvencí
------------------

Název konvence v CSS je velmi užitečný při tvorbě kódu, který je přísnější, průhlednější a
informativní.

|Vyhněte se selektorům „id“ a předponujte své třídy „o_<název modulu>“, kde „<název modulu>“ je
technické jméno modulu („prodej“, „chat“, …) nebo hlavní trasa vyhrazená modulem
(hlavně pro moduly webu, tj. např. o_forum pro modul website_forum).
| Jedinou výjimkou z této pravidla je webový klient, který používá jen předponu „o_“.

Při vytváření tříd a proměnných se vyhněte příliš specifickým názvům. Při pojmenovávání prvků sestupné struktury zvolte
„Prapradědeček“ přístup.

.. první třídy: bglight
Příklad:

......container:: varování varování-nebezpečí

Ne

.. kódový blok:: html

<div třída="o_element_wrapper">
<div třída="o_element_wrapper_entries">
<span class="o_element_wrapper_entries_entry">
<a class="o_element_wrapper_entries_entry_link">Vstup</a>

</div>


... kontejner:: varování varování-úspěch

      Do

.. kódový blok:: html

<div třída="o_element_wrapper">
<div třída="o_element_entries">
<span class="o_element_entry">
<a class="o_element_link" href="http://www.cambridge.org/core/journals/american-journal-of-physiology-lungs-and-breathing/article/abs/the-effects-of-pulmonary-hypertension-on-lung-volume-and-capacity/1072398A46E5B5F5D5C4672171801B61">Vstup</a>

</div>


Kromě kompaktnosti tento přístup usnadňuje údržbu, protože omezuje potřebu přejmenovávání
Když dojde ke změně v DOM.

... přispívat/kódovat podle pokynů/SCSS/proměnné SCSS:

Proměnné SCSS
~~~~~~~~~~~~~~

Naše standardní konvence jsou $o-[kořen]-[prvek]-[vlastnost]-[modifikátor] s:

* $-o
Předpona.
* [kořen]
Buď komponenta **nebo** název modulu (komponenty mají přednost).
* [prvek]
Volitelné označení vnitřních prvků.
* [vlastnost]
Vlastnost nebo chování definované proměnnou.
* „[příslovce]“
Nepovinný modifikátor.

Příklad:

... kódový blok: scss

$o-blok-barva: hodnota;
$o-block-title-color: hodnota;
$o-block-title-color-hover: hodnota;

... /přispívání/kódování/skss/skalární proměnné skss:

Proměnné SCSS (skalární)
~~~~~~~~~~~~~~~~~~~~~~~

Tyto proměnné jsou deklarovány v bloku a zvenčí nejsou dostupné.
Naše standardní konvence jsou „$ - [název proměnné]“.

Příklad:

... blok kódu:: html

.o_element {
-vnitřní mezera: vypočítat něco;

margin-right: -vnitřní mezera;

.o_element_dite {
margin-right: -vnitřní mezera * 0,5;
         }
      }

.. viz též:
„Soubor dokumentace k Sassu
<https://sass-lang.com/documentation/variables#scope>

... přispívat/kódovat/příkazy/sass/mixiny:

Mixiny a funkce SCSS
~~~~~~~~~~~~~~~~~~~~~~~~~

Naše standardní konvence jsou „o-[název]“. Používejte popisné názvy. Když pojmenujete funkci, použijte slovesa.
imperativní tvar (např. „dostat“, „udělat“, „aplikovat“…).

Název nepovinných argumentů v proměnných ve tvaru
<přispívání/kódování/skloňované SCSS proměnné/>, takže `$-[argument]`.

Příklad:

... blok kódu:: html

@mixin o-avatar ($-velikost: 1,5 em, $-poloměr: 100 %)
šířka: $size;
výška: $size;
border-radius: $ - radius;
      }

@funkce o-invert-color($-barva, $-množství: 100%) {
$-inverzní: změnit-barvu ($-barva, $-odstín: odstín ($-barva) + 180);

@vrací směs (-inverzní, -barva, -množství).
      }

.. viz též:
   - „Mixiny na dokumentaci k Sassu <https://sass-lang.com/documentation/at-rules/mixin>“
   - „Funkce v dokumentaci k SAS <https://sass-lang.com/documentation/at-rules/function>“

... přispívání/kódování/pravidla pro Sass/CSS proměnné:

Proměnné CSS
~~~~~~~~~~~~~

V Odoo se používání proměnných CSS omezuje na doménu HTML. Používejte je k **kontextuálnímu** přizpůsobení
design a grafická úprava.

Naše standardní konvence jsou BEM, takže „--[root]__[element]-[property]--[modifier]“, s:

* [kořen]
Buď komponenta **nebo** název modulu (komponenty mají přednost).
* [prvek]
Volitelné označení vnitřních prvků.
* [vlastnost]
Vlastnost nebo chování definované proměnnou.
* „[příslovce]“
Nepovinný modifikátor.

Příklad:

... kódový blok: sass

.o_kanban_record {
--KanbanRecord-šířka: hodnota
--KanbanRecord__obrázek-okraj: hodnota;
--KanbanRecord__picture-border--active: value;
     }

     // Adapt the component when rendered in another context.
.o_form_view {
--kanbanový záznam - šířka: jiná hodnota
--KanbanRecord__obrázek-okraj: jiná hodnota
--KanbanRecord__picture-border--active: jiná hodnota
     }

... přispívat/kódovat/pravidla/sass/proměnné používat

Použití proměnných CSS
--------------------

V Odoo se používání proměnných CSS omezuje na doménu, což znamená, že jsou použity pro **kontextuální**
upravit návrh a uspořádání, namísto řízení globálního systému designu. Tyto jsou obvykle používány
Když jsou vlastnosti komponenty proměnlivé ve specifických kontextech nebo jiných okolnostech.

Tyto vlastnosti definujeme uvnitř hlavního bloku komponenty a poskytujeme výchozí hodnoty pro případ, že některá z nich nebude nastavena.

Příklad:

... kódový blok: scss
:komentář: :soubor:`my_component.scss`

.o_MyComponent {
barva: var(--MyComponent-barva, #313131);
      }

... kódový blok: scss


.o_MyDashboard {
         // Adapt the component in this context only
--MyComponent-barva: #017e84;
      }

.. viz též:
„Proměnné CSS na stránkách webu MDN
<https://developer.mozilla.org/cs/docs/Web/CSS/Používání vlastních CSS vlastností>

... přispívání/kódování/pravidla pro SCSS/CSS/SCSS proměnné používat:

Proměnné CSS a Sass
~~~~~~~~~~~~~~~~~~~~~~

I když se zdají být podobné, proměnné typu „CSS“ a „SCSS“ chovají zcela odlišně. Hlavní
Rozdíl je v tom, že proměnné typu „SCSS“ jsou imperativní a kompilují se pryč, zatímco proměnné typu „CSS“
*deklarativní* a zahrnuty do konečného výstupu.

.. viz též:
„Rozdíl proměnných CSS/SCSS na dokumentaci SASS
<https://sass-lang.com/documentation/variables#:~:text=CSS%20proměnné%20jsou%20zahrnuty%20do,použít%20bude%20stejný>

V Odoo používáme nejlepší z obou světů: používání proměnných „SCSS“ k definování systému pro návrh
Při kontextových adaptacích se volí „CSS“.

Implementace předchozího příkladu se může zlepšit přidáním proměnných v SCSS, aby
získat kontrolu na vrcholu a zajistit konzistenci s ostatními komponentami.

Příklad:

... kódový blok: scss
:předmět: :soubor: `secondary_variables.scss`

$o-komponenta-barva: $o-hlavní-textová barva;
$o-dashboard-color: $o-info;
      // [...]

...: kódový blok
:caption: :file:`component.scss`

.o_component {
barva: var(--MyComponent-color, #{$o-component-color});
      }

...: kódový blok
:předpis: :soubor:`dashboard.scss`

.o_dashboard {
--MyComponent-barva: #{$o-panel-barva}
      }

... přispívání/kódování/sass/kořen:

Pseudo-třída :root
~~~~~~~~~~~~~~~~~~~~~~~~

Definování proměnných CSS na pseudo-třídě :root je technika, kterou obvykle nepoužíváme.
UI společnosti Odoo. Tato praxe je běžně používána k přístupu a změnám CSS proměnných na celém webu.
Tohle lze vyřešit použitím Sassu namísto CSS.

Výjimky z této pravidla by měly být poměrně jasné, jako například šablony sdílené mezi balíčky.
vyžadují určitou úroveň kontextové osvícenosti, aby byly správně zobrazeny.
