:sirotčinec:

..._jakdokancelář:
..._jakdokončit/modul:

=================
Stavba modulu
=================

.. nebezpečí::
Tento návod je zastaralý. Doporučujeme raději číst :doc:`server_framework_101`.

.. varování:
Tento návod vyžaduje, abyste měli nainstalované Odoo.

Zastavit/spustit Odoo server
==========================

Odoo používá architekturu klient/server, ve které jsou klienty webové prohlížeče.
připojení k serveru Odoo prostřednictvím RPC.

Business logika a rozšíření se obvykle provádí na straně serveru.
Ačkoli podporují funkce klienta (např. nové způsoby reprezentace dat,
interaktivní mapy) lze přidat do klienta.

Aby se spustil server, stačí zadat příkaz :ref:`odoo-bin
v příkazovém řádku v shellu, přidává plný cestu k souboru pokud
nutné:

... kód::bash

odoo-bin

Server se zastaví dvakrát stisknutím „Ctrl-C“ z terminálu nebo
způsobit odstranění příslušného procesu operačního systému.

Vytvořte modul pro Odoo
====================

Serverové i klientské rozšíření jsou baleny jako moduly, které
volitelně v databázi.

Moduly Odoo mohou buď přidat nové podnikové logiky do systému Odoo nebo
změnit a rozšířit stávající logiku podnikání: můžete vytvořit modul, který přidává vaše
účetní předpisy země do podpory účetnictví v Odoo.
další modul přidává podporu pro vizualizaci autobusového parku v reálném čase.

Vše v Odoo začíná a končí moduly.

Složení modulu
-----------------------

Modul Odoo může obsahovat několik prvků:

Objekty podnikání
Tyto zdroje jsou deklarovány jako třídy v Pythonu a automaticky ukládány.
na základě jejich konfigurace

:doc:`Pohledy na objekty <../reference/user_interface/view_architectures>`
Definice objektů uživatelského rozhraní pro podnikání

:ref:`Datové soubory <reference/data>`
XML nebo CSV soubory, které deklarují metadata modelu:

    * :dokumentu „pohledy“ nebo :ref:`zprávy
"<odkaz/zprávy>"
    * konfigurační data (parametrizaci modulů, :ref:`bezpečnostní pravidla <reference/security>`)
    * Demonstrační data
    * a více

:ref:`Webové kontroly <reference/controllers>`
Zpracovávat požadavky webových prohlížečů

Statická data z webu
Obrázky, soubory CSS nebo skripty JavaScript používané webovým rozhraním nebo webem

Modulová struktura
----------------

Každý modul je adresář v rámci adresáře s názvem „modul“. Adresáře s názvem „modul“
jsou specifikovány pomocí příkazu :option:`--addons-path <odoo-bin --addons-path>
option.

..tip:
:klasika: aforismus

většina příkazových řádkových možností lze také nastavit pomocí :ref:`souboru konfigurace


Modul Odoo je deklarován v jeho :ref:`manifestu <reference/module/manifest>“.

Modul je také
„Modul Pythonu <http://docs.python.org/2/tutorial/modules.html#packages>“
s souborem „__init__.py“, který obsahuje příkazy pro dovoz různých verzí Pythonu.
soubory v modulu.

Příkladem je modul s jediným souborem „mymodule.py“ obsahujícím „__init__.py“.
může obsahovat:

z importu modulu mymodule

Odoo poskytuje nástroj k nastavení nového modulu: odoo-bin
Příkaz „<reference/cmdline/server>“ má podpříkazy:
vytvořit prázdný modul:

.. kódový blok: konzole

$ odoo-bin scaffold modul_jmeno_modulu_pustit

Komando vytvoří podsložku pro váš modul a automaticky vytvoří
soubor s běžným kódem pro modul. Většina z nich obsahuje jen komentáře
nebo XML. Většinu z nich vysvětlíme v tomto návodu.

..cvičení:: Tvorba modulu

Použijte příkazový řádek uvedený výše k vytvoření prázdného modulu Open Academy a nainstalujte jej do Odoo.

Objektově relační mapování
-------------------------

Zásadní součástí Odoa je vrstva :abbr:`ORM (Mapování objektů na relační databázi)“.
Tato vrstva umožňuje psát většinu příkazů SQL (strukturovaný dotazovací jazyk)
ručně a poskytuje rozšířitelnost a bezpečnostní služby.

Objekty obchodní logiky jsou deklarovány jako třídy Pythonu, které dědí
Třída Model, která je integruje do automatizovaného
systém odolnosti.

Model lze nakonfigurovat nastavením několika vlastností.
definice, nejdůležitějším atributem je
atribut ~odoo.models.Model._name, který je povinný a určuje jméno pro
model v systému Odoo. Zde je minimálně dostačující definice
model:

od odoo importujeme modely
třída MinimalModel(model.Model):
_name = 'test.model'

Modelová pole
------------

Pole slouží k definování, co může model uchovávat a kde.
definované jako atributy třídy modelu

od odoo importujeme modely a pole

třída LessMinimalModel(model.Model):
_name = 'test.model2'

jméno = fields.Str()

Společné atributy
~~~~~~~~~~~~~~~~~

Stejně jako samotný model, jeho pole lze konfigurovat pomocí
konfigurační atributy jako parametry:

name = fields.Char(povinné=True)

Některé atributy jsou dostupné na všech polích, zde je uvádíme ty nejčastější:

:attr:`~odoo.fields.Field.string` („unicode“, výchozí hodnota: název pole)
Název pole v uživatelském rozhraní (viditelný pro uživatele).
:attr:`~odoo.fields.Field.required` (`bool`, výchozí hodnota: False)
Pokud je hodnota „True“, pole nemůže být prázdné, musí buď mít výchozí hodnotu
musí mít hodnotu nebo musí být při vytváření záznamu vždy nastavena.
:attr:`~odoo.fields.Field.help` („unicode“, výchozí hodnota: „“)
Dlouhý formát poskytuje uživatelům v rozhraní nástrojovou lištu.
:attr:`~odoo.fields.Field.index` („bool“, výchozí hodnota: „False“)
Žádost, aby Odoo vytvořilo „index“ na sloupci.

Jednoduchá pole
~~~~~~~~~~~~~

Existují dvě široké kategorie polí: „jednoduchá“ pole, která jsou atomická
hodnoty uložené přímo v tabulce modelu a „vztahové“ pole propojující
záznamy (stejného typu nebo různých typů).

Příkladem jednoduchých polí je třeba pole typu `~odoo.fields.Boolean`.
:třída:odoo.fields.Datum, třída:odoo.fields.Text

Rezervované pole
~~~~~~~~~~~~~~~

Odoo vytváří několik polí ve všech modelech. Tyto pole jsou
spravované systémem a neměly by být přepisovány. Mohou se číst, pokud
užitečné nebo nezbytné:

:attr:`~odoo.fields.Model.id` (:třída:`~odoo.fields.Id`)
Jedinečný identifikátor záznamu v jeho modelu.
:attr:`~odoo.fields.Model.create_date` (:třída:`~odoo.fields.Datetime`)
Datum vzniku záznamu.
:attr:`~odoo.fields.Model.create_uid` (:třída:`~odoo.fields.Many2one`)
Uživatel, který vytvořil záznam.
:attr:`~odoo.fields.Model.write_date` (:třída:`~odoo.fields.Datetime`)
Datum poslední úpravy záznamu.
:attr:`~odoo.fields.Model.write_uid` (:třída:`~odoo.fields.Many2one`)
uživatel, který naposledy upravil záznam.

Speciální pole
~~~~~~~~~~~~~~

Výchozí nastavení Odoo také vyžaduje pole „jméno“ na všech modelech pro různé
zobrazování a vyhledávání chování. Pro tyto účely se používá pole
přepsané nastavením vlastnosti :attr:`~odoo.models.Model._rec_name`.

.. cvičení:Definujte model

Definujte nový datový model *Kurz* v modulu *openacademy*. Kurs má název a
popis kurzu, který musí obsahovat název.

Datové soubory
----------

Odoo je velmi datově orientovaný systém. Chování se přizpůsobuje
Část kódu modulu v Pythonu je v datech, které jsou nastaveny při načítání.

Tip: některé moduly slouží pouze k přidání dat do Odoo
:klasika: aforismus

Data modulu jsou deklarována pomocí souborů :ref:`dat <reference/data>`, XML souborů.
„<záznam>“ prvku. Každý „<záznam>“ prvek vytváří nebo aktualizuje databázi
rekord.

... blok kódu::xml



<záznam modelu = "{název modelu}" identifikátor = "{identifikátor záznamu}">
<pole název={název pole}>{hodnota}</pole>
</záznam>



* „Model“ je název pro odoo modelu, který se používá k záznamům.
* „id“ je „externí identifikátor“, který umožňuje odkazovat na záznam
(bez nutnosti znát jeho identifikátor v databázi).
* „<field>“ prvky mají „name“, což je název pole v
modelu (např. „popis“). Jejich tělo je hodnotou pole.

Datové soubory musí být deklarovány v seznamu nahrávaných souborů, mohou
být vyhlášen v seznamu „Data“ (vždy načtené) nebo v seznamu „Demo“.
(pouze v režimu demonstrace).

.. cvičení: Vytvořte demonstrační data

Vytvořte ukázkové datové sady, které naplní model Courses několika ukázkovými kurzy.

..tip:
Obsah datových souborů se načítá pouze při instalaci nebo aktualizaci modulu.

Po provedení některých změn nezapomeňte použít příkaz :ref:`odoo-bin -u openacademy
<reference/cmdline> a uložte změny do databáze.

...jaktovys/modul/akce:

Akce a menu
-----------------

Akce a menu jsou běžné záznamy v databázi, obvykle deklarované
datové soubory. Akce může být spuštěna třemi způsoby:

#kliknutím na položky nabídky (které jsou spojeny s konkrétními akcemi).
#kliknutím na tlačítka v pohledech (pokud jsou spojena s akcemi).
#jako kontextové akce na objekt

Protože menu jsou trochu složitá na deklarování, je zde „<menuitem>“
zkratka pro deklarování „ir.ui.menu“ a připojení jej k odpovídající
Díky tomu se pohybuje lépe.

... blok kódu::xml

<záznam modelu „ir.actions.act_window“ s ID „action_list_ideas“>
<pole jméno="název">Nápady</pole>
<field name="res_model">ideaprojekt</field>
<položka název="zobrazení">seznam,formulář</položka>
</záznam>
<menuitem id="menu_ideas" parent="menu_root" name="Ideas" sequence="10"
action="akce_seznam_názorů"/>

.. nebezpečí::
:klasika: aforismus

Akce musí být deklarována před odpovídající nabídkou v souboru XML.

Sekvence datových souborů je prováděna postupně. Akce „id“ musí být v databázi přítomná před
lze vytvořit nabídku.

... cvičení: Vytvořit nové položky v nabídce

Vytvořte nové položky nabídky pro přístup k kurzu pod nabídkou OpenAcademy. Uživatel by měl být schopen
do:

   - zobrazit seznam všech kurzů
   - Vytvářet/upravovat kurzy

Základní názory
===========

Zobrazení definují způsob zobrazení záznamů modelu. Každý typ zobrazení
zobrazuje způsob vizualizace (seznam záznamů, graf jejich hodnot).
agregace, ...). Zobrazení lze požadovat obecně prostřednictvím jejich typu
(např. seznam partnerů) nebo přímo přes jejich ID.
požadavky, ve kterém je správný typ a nejnižší priorita.
použít (takže nejnižší priorita každého typu je výchozí pohled pro tento
typ).

:ref:`Přizpůsobení zobrazení <reference/view_records/inheritance>` umožňuje upravit zobrazení
deklarována jinde (přidáním nebo odebráním obsahu).

Výchozí deklarace pro obecný pohled
------------------------

Výhled je deklarován jako záznam modelu „ir.ui.view“.
je implicitně obsaženo v základním prvku pole „arch“:

... blok kódu::xml

<zaznamenání typu „ir.ui.view“ s ID „view_id“>
<políčko jméno="name">view.name</políčko>
<pole název="model">objektní_název</pole>
<field name="priority" eval="16"/>
<položka jméno="arch" typ="xml">
<!-- zobrazit obsah: formulář, seznam, graf, ... -->
</p>
</záznam>

.. nebezpečí: obsah pohledu je XML.
:klasika: aforismus

V poli „arch“ musí být tedy deklarováno jako „type=„xml““, aby bylo správně vyhodnoceno.

listové zobrazení
----------

Seznamový pohled, také nazývaný seznamový pohled, zobrazuje záznamy v tabulkové podobě.

Jejich základním prvkem je „<list>“. Nejjednodušší forma zobrazení seznamu je
zobrazuje všechna pole, která se mají zobrazit v tabulce (každé pole jako sloupec):

... blok kódu::xml

<seznam typu="Idea list">
<pole název/>
<pole název="inventor_id"/>


...jaktose/modul/viz/formulář:

Formuláře
----------

Formuláře se používají k vytváření a úpravě jednotlivých záznamů.


Jejich základním prvkem je „<form>“. Skládají se z vysoké úrovně struktury
elementy (skupiny a poznámkové bloky) a interaktivní prvky (tlačítka a pole):

... blok kódu::xml

<form string="Formát myšlenky">
<skupina kolon="4">
<skupina řádky="2" sloupec="2">

<pole název/>
<sloupec jméno="vynálezce_id"/>
</skupina>

<skupina řádky="2" sloupec="2">

<field name="aktivní"/>
<field name="invent_date" readonly="1"/>
</skupina>

<table class="notebook" width="100%" cellspacing="0" cellpadding="0">

<položka name="description" nolabel="1"/>



<pole název="stát" />
</skupina>


...cvičení: Přizpůsobení vzhledu formuláře pomocí XML

Vytvořte si vlastní pohled na formulář pro objekt kurzu. Zobrazovaná data by měla být: jméno a
popis kurzu.

... cvičení: Notebooky

V zobrazení kurzu vložte popis do záložky, aby se snadněji hledal.
Později přidat další záložky s dalšími informacemi.

Formulářové pohledy mohou také používat prostý HTML pro více flexibilní uspořádání:

... blok kódu::xml

<form string="Idea Form">
<hlavička>
<tlačítko typu "potvrdit" jméno akce "potvrzení"
style="display:none; visibility:hidden;" class="oe_highlight" />
<tlačítko typu "Označit jako hotové" název akce "akce_hotovo"

<tlačítko typu "Obnovit jako návrh" pojmenované "akce - návrh"
viditelné="stav ne v ['potvrzeno', 'dokončeno']" />
<položka jméno="stát" widget="statusbar"/>

<list>
<div class="oe_title">
<label for="name" class="oe_edit_only" string="Název myšlenky" />
<h1><field name="name"/></h1>

<separator string="Obecné" colspan="2" />
<skupina řádky="2" sloupec="2">
<položka název="popis" placeholder="Popis myšlenky...">

</list>


Počet zobrazení
------------

Vlastní nastavení vyhledávání upravuje pole pro vyhledávání spojené s pohledem na seznam.
jiných agregovaných pohledů). Jejich kořenovým prvkem je „<search>“ a jsou
obsahující pole definující, které pole lze vyhledávat:

... blok kódu::xml

<hledání>
<pole název/>
<položka jméno="vynálezce_id"/>


Pokud pro daný model neexistuje žádné vyhledávací rozhraní, Odoo vytvoří nové, které umožňuje
hledání v poli „jméno“.

..cvičení: Hledání kurzů

Povolit vyhledávání kurzů podle jejich názvu nebo popisu.

Vztahy mezi modely
========================

Záznam z modelu může být spojen s jiným záznamem z jiného modelu.
Příkladem je propojení záznamu o objednávce s klientským záznamem obsahujícím
klientských dat, je také spojena s jejími záznamy o prodejních objednávkách.

... cvičení: Vytvořit model sezení

Pro modul Otevřená akademie považujeme za vhodný model pro *sessiony*: session
Jedná se o konkrétní výuku předmětu v určitém čase pro určitou skupinu studentů.

Vytvořte model pro *session*. Session má jméno, datum zahájení a
dobu trvání a počet míst k sezení. Přidejte akci a položku nabídky, která zobrazí
jim. Nový model zobrazte v nabídce.

Relativní pole
-----------------

Vztahová pole spojují záznamy buď stejného typu (hierarchie), nebo
Mezi různými modely.

Relativní typy pole jsou:

:třída:`Many2one(jiný_model, na_smazání='set null') <odoo.polí.Many2one>`
Jednoduchý odkaz na jiný objekt:

print(foo.jiný_id.název)

......viz také: „cizí klíče <http://www.postgresql.org/docs/12/static/tutorial-fk.html>“

:třída:`One2many(jiný model, příbuzné pole) <odoo.pole.One2many>`
Virtuální vztah, opak :class:`~odoo.fields.Many2one`.
A:klasa:~odoo.fields.One2many chová se jako kontejner záznamů
Při přístupu k ní dochází ke vzniku (možná prázdné) sady záznamů:

pro jiné v foo.jiné_idy:
print(jméno_druhého)

...... nebezpečí::

Protože je :class:`~odoo.fields.One2many` virtuální vztah,
musí být pole typu :class:`~odoo.fields.Many2one`.
:samp:`{jiné_model}‘ a jeho název *musí být* :samp:`{příbuzné_pole}`

:třída:`Many2many(jiný model) <odoo.field.Many2many>`
Oboustranná mnohoúhelníková vztahová závislost, kdy každý záznam na jedné straně může být spojen s jakýmkoliv záznamem na druhé straně.
k jakémukoli počtu záznamů na druhé straně. Chová se jako kontejner
záznamy, přístup k nim také může vést ke sadu záznamů prázdné.

pro jiné v foo.jiné_idy:
print(jméno_druhého)

.. cvičení: Mnoho-k-jednomu vztahy

Použijte mnoho2jedno, abyste změnili modely *Kurz* a *Sesion*, aby odrážely jejich
vztah k ostatním modelům:

   - Kurz má uživatele s právy; hodnota pole je záznamem
vložený model „res.users“.
   - Na každé lekci je instruktor, hodnota pole je záznamem o
vložený model „res.partner“.
   - Sesní je spojen s kurzem, hodnota pole je záznam
modelu „openacademy.course“ a je povinný.
   - Upravte pohledy.

..cvičení::Inverzní vztah 1:množství

Použijte obrácený vztah pole s více hodnotami one2many a upravte modely tak, aby odrážely
vztah mezi kurzy a sekcemi.

... cvičení:: Mnoho-mnoho vztahů

Použijte pole vztahů mnoho k mnoha a upravte model *Session*, aby se vztahoval na
každé sezení pro určitý soubor účastníků. Účastníci budou reprezentováni
partnera, takže se budeme vztahovat k vestavěnému modelu „res.partner“.
Abychom se přizpůsobili pohledu na věc.

Dědictví
===========

Model dědičnosti
-----------------

Odoo poskytuje dvě mechanismu dědičnosti, které umožňují rozšířit existující model.
modulárním způsobem.

První dědění umožňuje modulu změnit chování
model definovaný v jiném modulu:

- Přidat pole do modelu.
- překrýt definici polí v modelu
- přidat omezení do modelu.
- přidat metody do modelu
- přebít existující metody v modelu.

Druhý dědický mechanismus (delegace) umožňuje propojit každou záznamovou jednotku
modelu k rekordům v rodičovském modelu a poskytuje průhledný přístup ke
pole hlavního záznamu.

.. obrázek::../odkazy/zadni-konec/orm/dědičné metody.png
:align:center

.. viz též:
   * :attr:`~odoo.models.Model._inherit`
   * :attr:`~odoo.models.Model._inherits`

Zobrazit dědictví
----------------

Odoo místo toho modifikuje stávající pohledy na místě (přepíše je).
poskytuje vlastnost dědičnosti, kdy se na nadřazené „rozšířené“ pohledy aplikují dětské pohledy.
kořenové názory a mohou přidávat nebo odstraňovat obsah ze svých rodičů.

Výhled rozšíření odkazuje na svého rodiče pomocí pole „inherit_id“ a
místo jednoho pohledu je pole „arch“ složeno z libovolného počtu
„Xpath“ prvky, které vybírají a mění obsah svého rodičovského pohledu:

... blok kódu::xml

<!-- zlepšený seznam kategorií nápadů -->
<záznam id="idea_category_list2" typu="ir.ui.view">
<field name="name">id.kategorie.seznam2</field>
<položka jméno="model">ideální kategorie</položka>
<vlastnost jméno="dědičný id" odkaz="id_kategorie_seznamu"/>
<položka jméno="arch" typ="xml">

id po ní -->
<xpath expr="//field[@name='description']" position="after">
<políčko jméno="ideas_ids" text="Počet nápadů"/>
</xpath>
</p>
</záznam>

„expr“
XPath výraz vybírající jediný prvek v nadřazeném pohledu.
Pokud neodpovídá žádnému prvku nebo více než jednomu, vyvolá chybu.
„položka“
Operace aplikovaná na shodný prvek:

„uvnitř“
přidává tělo „xpath“ na konec shodného prvku
„vyměnit“
nahradí shodný prvek tělem „xpathu“, přičemž nahradí všechny výskyty uzlu „$0“.
v novém těle s původním prvkem
„předtím“
vloží tělo „xpath“ jako sourozence před shodným prvkem
„Po“
vloží tělo „xpaths“ jako sourozence po shodném prvku
„atributy“
upravuje atributy shodného prvku pomocí speciálních
„atribut“ prvky v těle „XPathu“.

..tip:
Když se shoduje pouze jedna položka, lze atribut „position“ nastavit přímo.
na prvku, který má být nalezen. Oba dědění pod sebou budou mít stejný výsledek.

... kódový blok :: XML

<xpath expr="//field[@name='description']" position="after">
<pole název="idea_ids"/>
</xpath>

<položka name="description" pozice="později">
<pole název="idea_ids"/>
</p>


...cvičení: Upravujte stávající obsah

   * Použijte dědičnost modelů k úpravám stávajícího modelu Partner a přidejte
„učitel“ logický prvek a mnoho-množství pole odpovídající
vztah partnera sezení
   * Použijte dědičnost pohledu a zobrazte tyto pole ve formuláři pro partnery.

Domény
~~~~~~~

V Odoo jsou :ref:`reference/orm/domains` hodnotami, které kódují podmínky
záznamy. Doména je seznam kritérií používaných k výběru podmnožiny modelu
záznamy. Každé kritérium je trojice s názvem pole, operátorem a hodnotou.

Příkladem je použití na produktu *Produkt*, kdy se vybere následující doména
všechny služby s jednotkovou cenou nad 1000:

[('produktové_druhy', '==', 'služba'), ('jednotková_cena', '>', 1000)]

Výchozí kritéria se automaticky spojují pomocí implicitního AND. Logické operátory
„&“ (a „AND“), „|“ (nebo „OR“) a „!“ („NOT“) lze použít k explicitnímu spojení
kriterií. Používají se v předponové pozici (operátor je vložen před
argumenty, nikoliv mezi sebou (např. vybrat produkty „které jsou
služby nebo mít jednotkovou cenu, která není mezi 1000 a 2000“

    ['|',
('produktové_druhy', '==', 'služba')
        '!', '&',
('cena_jednotky', '>=', 1000)
['cena_za_jednotku' < 2000]

K relačnímu poli lze přidat parametr „doména“, který omezuje platnost
záznamy pro vztah při pokusu o výběr záznamů v uživatelském rozhraní.

... cvičení:Domény na relační pole

Při výběru instruktora pro *Session* se zobrazují pouze instruktoři (partneři).
Pokud je nastavená hodnota „instruktor“ na „pravda“, měla by být viditelná.

...cvičení: Komplexnější domény

Vytvořte nové kategorie partnerů *Učitel/Úroveň 1* a *Učitel/Úroveň 2*.
Lektorem jednoho bloku může být buď lektor, nebo učitel
(v jakémkoliv stupni).

Přednastavené hodnoty a pole s výpočtem
==================================

Dosud byly pole ukládána přímo do a získávána přímo ze
databáze. Hodnoty polí mohou být také počítané. V takovém případě je hodnota pole
vytažené z databáze, ale počítané na lince pomocí metody
model.

Pro vytvoření pole s počítanou hodnotou vytvořte pole a nastavte jeho atribut
:attr:`~odoo.fields.Field.compute` na název metody.
Metoda by měla jednoduše nastavit hodnotu pole, na které se počítá pro každý záznam.
„sám“.

… nebezpečí: „sám“ je kolekce
:klasika: aforismus

Objekt „self“ je záznamový soubor, tedy seřazená sbírka záznamů. Podporuje
standardní operace s kolekcemi v Pythonu, jako je „len(self)“ a „iter(self)“, navíc i další sady.
operace jako „rec1 + rec2“.

Přejděte přes „sám“ a získáte záznamy jeden po druhém, kde každý záznam je sám o sobě sbírkou
Velikost 1. Pole jednotlivých záznamů lze přistupovat a přiřazovat pomocí znaménka tečky, například
„název záznamu“.

... kódový blok:: python

import random
od odoo importujeme modely, pole a API

třída ComputedModel(model.Model):
name = 'test.computed'

jméno = pole.Char(vypočítat='_vypočítat_jméno')

def _vypočítat_jméno(sebe):
pro rekord v sobě:
record.název = str(random.randint(1, 10**6))


Závislosti
------------

Hodnota pole vypočítaného v poli obvykle závisí na hodnotách ostatních polí.
vypočítaný záznam. ORM očekává, že vývojář specifikuje tyto závislosti
na metodu počítání s dekorátorem :func:`~odoo.api.depends`.
Uvedené vazby využívá ORM k spouštění znovupočítání.
pole, pokud některé z jeho závislostí byly změněny:

od odoo importujeme modely, pole a API

třída Předpokládaný model (model.Model):
_name = 'test.vypočtené'

jméno = pole.Char(výpočet = '_compute_name')
value = fields.Integer

@api.depends('value')
def _vypočítat_jméno(self):
pro rekord v sobě:
record.jméno = "Záznam s hodnotou %s" % record.hodnota

..cvičení:: Výpočetní pole

   * Přidejte procento obsazených míst k modelu Session
   * Zobrazte pole v seznamu a formuláři
   * Zobrazte pole jako postupovou lištu

Výchozí hodnoty
--------------

Každému poli lze přiřadit výchozí hodnotu. V definici pole přidejte možnost
„default=X“, kde „X“ je buďto hodnota Pythonu (logická, celé číslo)
plovoucí číslo nebo řetězec, nebo funkce přijímající záznamové sady a vracící hodnotu

name = fields.Char(výchozí hodnota = "Neznámé")
user_id = fields.many2one('res.users', default=lambda self: self.env.user)

.. poznámka::
Objekt „self.env“ umožňuje přístup k parametry požadavku a dalším užitečným věcem:

    - „self.env.cr“ nebo „self._cr“ je objekt databázového *kursoru*; je
sloužící k dotazování databáze
    - „self.env.uid“ nebo „self._uid“ je aktuální uživatelův identifikátor v databázi
    - „self.env.user“ je záznam aktuálního uživatele
    - „self.env.context“ nebo „self._context“ je kontextová složka
    - „self.env.ref(xml_id)“ vrací záznam odpovídající XML id
    - „self.env[název_modelu]“ vrací instanci daného modelu

... cvičení:Aktivní objekty - Výchozí hodnoty

   * Nastavte výchozí hodnotu start_date na dnešní den (viz
:třída:~odoo.fields.Datum
   * Přidejte pole „active“ do třídy Session a nastavte session jako aktivní pomocí
výchozí.

Onchange
========

„Onchange“ mechanismus poskytuje způsob, jak může klientské rozhraní aktualizovat
formulář se vždy aktualizuje, když uživatel vyplní hodnotu do pole, aniž by cokoliv uložil.
do databáze.

Příkladem může být situace, kdy model obsahuje tři pole „cena“, „jednotková cena“ a
„cena“ a chcete aktualizovat cenu na formuláři při jakémkoli změně
pole je upraveno. K tomu definujte metodu, kde „self“ představuje
zaznamenat záznam v přehledu formulářů a ozdobit jej funkcí:
Určit, na jakém poli se má spustit.
„sám“ bude zobrazen na formuláři.

... blok kódu::xml


<pole název="částka"/>
<vlastnost jméno="jednotková cena"/>
<field name="cena" readonly="1"/>

... kódový blok:: python

   # handler události onchange
@api.onchange('množství', 'jednotková cena')
def __onchange_price__(self):
       # automaticky se měnící pole
self.cena = self.množství * self.jednotková cena
       # Může volitelně vracet varování a domény.
return {
„varování“: {
„Něco špatného se stalo“,
„Bylo to opravdu hodně zlé“,
           }
       }

Pro pole s počítanými hodnotami je chování „na změnu“ vloženo do výchozího nastavení.
hrát si s formou *Session*: změnit počet sedadel nebo účastníků.
„Pozice obsazených míst“ se automaticky aktualizuje.

.. cvičení:: varování

Přidejte výslovný onchange k upozornění na neplatné hodnoty, jako je například záporná
počet míst nebo více účastníků než je míst k sezení.

Omezení modelu
=================

Odoo nabízí dvě způsoby, jak nastavit automaticky ověřené invarianty:
:funkce Pythonu omezení <odoo.api.constrains> a
:attr:`SQL omezení <odoo.models.Model._sql_constraints>“.

Pythonová omezení jsou definována jako metody, které jsou dekorovány
:func:`~odoo.api.constrains`, která je vyvolána na záznamové sadě.
specifikuje pole, která jsou zapojena do omezení, takže omezení
automaticky vyhodnocen, když se jedna z nich změní.
vznést výjimku, pokud není splněna jeho invariantní podmínka::

od odoo.exceptions import ValidationError

@api.vztahuje_se('věk')
def _check_something(self):
pro rekord v sobě:
pokud je věk uživatele větší než 20:
vyvolat ValidationError("Váš záznam je příliš starý: %s" % record.age)
        # Všechny záznamy prošly testem, nevrátí se nic

... cvičení: Přidat omezení v Pythonu

Přidejte omezení, které zkontroluje, že instruktor není v seznamu.
účastníky vlastního semináře.

SQL omezení je definováno pomocí atributu modelu
:attr:`~odoo.models.Model._sql_constraints`. Druhá je přiřazena seznamu
trojic „(název, SQL definice, zpráva)“, kde „název“ je
platný název omezení SQL, „sql_definition“ je výraz tabulkového omezení
A „zpráva“ je chybová zpráva.

... cvičení: Přidat omezení v SQL

S pomocí dokumentace PostgreSQL přidejte následující
omezení:

   #ZKONTROLUJTE, ZDA JE POPIS KURZU A NÁZEV KURZU ROZDÍLNÉ
   #. Dávejte jméno kurzu jedinečné

...cvičení: Cvičení 6 - Přidání duplicitního možného výběru

Protože jsme přidali omezení na unikátnost názvu kurzu, není
již možné duplikovat funkci „Duplikovat“ (:menu „Formulář –>
Duplikát.

Znovu implementujte vlastní metodu „kopírovat“, která umožňuje duplikovat kurz.
objekt, změna původního názvu na „Kopie [původní název]“.

Pokročilé zobrazení
==============

listové zobrazení
----------

Seznamy mohou obsahovat doplňující atributy, které ještě více přizpůsobí.
chování:

„Výzdoba - {$name}“
umožňuje změnit styl písma řádku podle odpovídajícího
atributy záznamu.

Hodnoty jsou Pythonové výrazy. Pro každý záznam se vyhodnocuje výraz.
s atributy alba jako kontextovými hodnotami a pokud je „pravda“,
se aplikuje styl odpovídající řádku. Níže jsou uvedeny další hodnoty
dostupné v kontextu:

    * „uid“: ID aktuálního uživatele
    * „dnes“: aktuální místní datum ve tvaru „YYYY-MM-DD“.
    * „nyní“: stejné jako „dnes“ s přidáním aktuální doby.
Toto číslo je formátováno jako „YYYY-MM-DD hh:mm:ss“.

„{$name}“ může být „bf“ („font-weight: bold“).
(„písmo: kurzívou“), nebo jakýkoliv „výchozí barevný styl“.
<https://getbootstrap.com/docs/3.3/components/#available-variations>`_ („danger“,
„info“, „ztišený“, „primární“, „úspěch“ nebo „varování“.

... kódový blok :: XML

<seznam text="Kategorie nápadů" dekorace-info="stav=='návrh'"
dekorace-nebezpečí="stav=='vyhozené'"
<pole název/>
<pole název="stát" />


„upravitelné“
Nebo „„top““ nebo „„bottom““. Umožňuje upravovat seznam v místě
(nebo se musíte projít přes formulářový pohled) je hodnota
místo, kde se nové řádky objevují.

.. cvičení:: Barvení seznamu

Upravit zobrazení seznamu relací tak, aby trvaly méně než
5 dní je modrá a ta trvající více než 15 dní jsou
jsou červené.

Kalendáře
---------

Zobrazuje záznamy jako události v kalendáři. Jejich kořenovým prvkem je „<calendar>“
Nejčastějšími vlastnostmi těchto lidí jsou:

„barva“
Název pole používaného pro *segmentaci barev* (barvy).
automaticky rozděleny do událostí, ale události stejné barvy
(záznamy, které mají stejnou hodnotu pro pole „@color“) budou
stejné barvy.
„datum začátku“
pole záznamu, které obsahuje datum a čas začátku události
„datum_konec“ (volitelné)
záznamu pole, které obsahuje datum a čas konce události
„struna“
pole záznamu, které definuje štítek pro každý kalendářní termín

... blok kódu::xml

<kalendářní řádek="Myšlenky" datum_začátku="datum vynálezu" barva="ID vynálezce">
<pole název/>


.. cvičení: Kalendář

Přidejte kalendářový pohled do modelu Session, který umožní uživateli zobrazit
akce spojené s Akademií otevřených dveří.

Počet zobrazení
------------

Vyhledávací pole „<field>“ může obsahovat atribut „@filter_domain“, který přebírá
doménu pro vyhledávání na zadaném poli. V dané doméně
„self“ představuje hodnotu zadanou uživatelem. V následujícím příkladu je
používá se k vyhledávání v obou polích „název“ a „popis“.

Vyhledávací pohled může také obsahovat „<filtr>“ prvky, které slouží jako přepínače.
předdefinované vyhledávání. Filtry musí mít jednu z následujících vlastností:

„doména“
přidat zadanou doménu do aktuálního vyhledávání
„kontext“
přidat kontextu k aktuálnímu vyhledávání a použít klíč „group_by“ pro skupinování
výsledky na zadaném názvu pole

... blok kódu::xml

<hledaný řetězec="Nápady">
<pole název/>
<field name="description" string="Jméno a popis"
filtr_doména="['|', (self, 'ilike', 'jmeno'), (self, 'ilike', 'popis')]"/>
<položka jméno="vynálezce_id"/>
<políčko jméno="státní_id" widget="vybrané hodnoty"/>

<filtr název="my_ideas" string="My Ideas"
doménou="([('inventar_id', '=' ,uid)])"/>
<skupina>
<filtr jméno="skupina_podle_vynálezce"
kontextu={'skupina_podle': 'inventar_id'}"/>
</skupina>


Pro použití ne-výchozího vyhledávacího pohledu v akci je nutné jej propojit pomocí
„hledání“ pole záznamu akce.

Akce také může nastavit výchozí hodnoty pro vyhledávací pole.
„kontext“ pole: klíče kontextu ve tvaru
:samp:`search_default_{field_name}` inicializuje pole *field_name*.
poskytuje hodnotu. Filtry vyhledávání musí mít možnost „@name“ jako volitelnou
výchozí a chovat se jako logické hodnoty (mohou být zapnuté výchozím nastavením).

..cvičení: Hledání názorů

   #Přidejte tlačítko pro filtrování kurzů, u kterých je aktuální uživatel
zodpovědný v přehledu hledání kurzů. Udělejte ho výchozím nastavením.
   #Přidat tlačítko pro seskupení kurzů podle zodpovědného uživatele.

Ganttova diagram
-----

.. varování:
Pro zobrazení Ganttova diagramu je nutný modul web_gantt, který je součástí verze Enterprise.
verze vydání „Instalace“.

Horizontální pruhové grafy se obvykle používají k zobrazení plánování a pokroku projektu.
jejich základní prvek je „<gantt>“.

... blok kódu::xml

<gantt string="Nápady"
date_start="datum vynálezu"
date_stop="datum ukončení"
postup="postup"
default_group_by="inventarni_cislo" />

..cvičení: Ganttovy diagramy

Přidejte do nástroje Ganttovu diagramovou schému, která umožní uživateli zobrazit plánování sezení.
do modulu Otevřené akademie. Sessions by měly být seskupeny podle instruktora.

Grafické zobrazení
-----------

Grafické zobrazení umožňuje agregovaný přehled a analýzu modelů, jejich kořenových složek
element je „<graf>“.

.. poznámka::
Pivotová zobrazení (element „<pivot>“) a vícerozměrná tabulka umožňují výběr filtrů.
rozměry, aby získali správné agregované datové soubory před přechodem na grafický přehled.
Pohled na osu sdílí stejnou definici obsahu jako grafové pohledy.

Grafické zobrazení má čtyři režimy zobrazení, výchozím je zvolený režim.
Atribut „@type“.

Bar (výchozí)
sloupcový graf, kde první rozměr určuje skupiny.
horizontální osa, ostatní rozměry definují agregované sloupce v každé skupině.

Výchozí polohou je vedle sebe, ale lze je také stohovat.
„@stohovatelná=“Pravda““ na „<graf>“
Line
2rozměrná čára
Pizza
dvourozměrný koláč

V grafickém zobrazení je pole „<field>“ s povinným atributem „@type“.
hodnoty:

„řádek“ (výchozí hodnota)
pole by mělo být agregováno výchozím způsobem
„měření“
pole by mělo být agregováno, nikoliv seskupeno podle

... blok kódu::xml

<graf string="Celkový výsledek nápadu podle vynálezce">
<položka jméno="vynálezce_id"/>
<pole název="skóre" typ="měřítko"/>


.. varování:
Grafické zobrazení provádí agregace hodnot v databázi, nefunguje s výpočtem, který není uložen.
pole.

.. cvičení: Grafické zobrazení

Přidejte do objektu Session grafický pohled, který zobrazuje pro každý kurz
počet účastníků ve formě sloupcového grafu.

Kanban
------

Používají se k uspořádání úkolů, výrobních procesů atd. Jejich základní prvek je
„Kanban“.

Kanbanový pohled zobrazuje sadu karet, které mohou být seskupeny do sloupců. Každá karta
je rekord a každá sloupec hodnoty agregačního pole.

Pro příklad mohou být úkoly projektu uspořádány podle fází (každá sloupec je
účastníkem, nebo odpovědným (každá sloupec je uživatel) atd.

Kanbanové pohledy definují strukturu každé karty jako směs prvků formulářů.
(včetně základního HTML) a :ref:`reference/qweb`.

.. cvičení: Pohled na kanban

Přidejte nástroj pro zobrazení kanbanu, který seskupuje lekce podle kurzu (sloupce jsou
takže kurzy).

Bezpečnost
========

Kontrolní mechanismy přístupu musí být nakonfigurovány tak, aby bylo dosaženo soudržného zabezpečení.
politika.

Základní přístupy k řízení přístupu na základě skupin
-------------------------------------

Skupiny jsou vytvářeny jako normální záznamy na modelech „res.groups“ a udělovány
Přístup k nabídce přes definice nabídek. Přestože však nemáte nabídku, objekty mohou
stále mohou být přístupné nepřímo, takže skutečná úroveň oprávnění (čtení)
psát, vytvářet, odpojit) musí být definovány pro skupiny. Obvykle jsou
Prostřednictvím souborů CSV uvnitř modulů. Je také možné omezit přístup
konkrétní pole v zobrazení nebo objektu pomocí atributu skupin pole.

Práva přístupu
-------------

Přístupová práva jsou definována jako záznamy modelu „ir.model.access“.
právo přístupu je spojeno s modelem, skupinou (nebo bez skupiny pro globální
přístup) a sadu oprávnění: číst, psát, vytvářet, odstraňovat. Takový přístup
práva jsou obvykle vytvořena souborem CSV pojmenovaným podle jeho modelu:
„ir.model.access.csv“.

... blok kódu:: text

id,název,model_id/id,skupina_id/id,čtení,zápis,vytváření,odkazování
access_idea_idea,idea.idea,model_idea_idea,base.group_user,1,1,1,0
access_idea_vote,idea.vote,model_idea_vote,base.group_user,1,1,1,0

.. cvičení: Přidání oprávnění přístupu prostřednictvím rozhraní Odoo

Vytvořte nového uživatele „John Smith“. Pak vytvořte skupinu
„OpenAcademy / Session Read“ s přístupem k čtení pro model „Session“.

...cvičení:Přidejte kontrolu přístupu pomocí souborů dat do vašeho modulu

Používáním datových souborů

   * Vytvořte skupinu *OpenAcademy/Manager* s plnými právy na všechny
OpenAcademy modely
   * Učební jednotky a kurzy musí být přístupné všem uživatelům

Rekordní pravidla
------------

Záznamová pravidla omezují přístupové práva na podmnožinu záznamů dané
model. Pravidlo je záznamem modelu „ir.rule“ a je spojeno s
model, pole skupin (množina-mnoho) a oprávnění k nim.
Omezení se vztahuje na doménu. Doména určuje, ke kterým záznamům
Přístup je omezený.

Například tato pravidla zabraňují smazání kontaktů, které nejsou
v státním režimu „zrušit“. Pozor, hodnota pole „skupiny“ musí následovat
stejná konvence jako metoda: `~odoo.models.Model.write()` v rámci ORM.

... blok kódu::xml

<záznam id="smazání zrušeno" typu="ir.rule">
<field name="jméno">Lze smazat pouze zrušené poptávky.</field>
<položka jméno="model_id" odkaz="crm.model_crm_lead"/>
<pole name="skupiny" hodnota="[(4, odkaz na 'tým prodeje. skupina manažera')]"/>
<pole name="perm_read" hodnota="0"/>
<field name="perm_write" eval="0"/>
<vlastnost jméno="perm_create" hodnota="0"/>
<pole název="perm_unlink" hodnota="1"/>
<pole název="doména_povinně">[('stát','=','zrušit')]</pole>
</záznam>

..cvičení: Zaznamenávání pravidel

Přidejte pravidlo záznamu pro model Kurzy a skupinu
„OpenAcademy/Manager“, který omezuje přístupy „write“ a „unlink“
zodpovědné osoby za kurz. Pokud kurz nemá zodpovědnou osobu, všichni uživatelé
musí být schopni ji upravit.

..._jakdokončit/modul/krok za krokem:

Kouzelníci
=======

Mágové popisují interaktivní sezení s uživatelem (nebo dialogová okna) takto:
dynamické formuláře. Kouzelník je prostě model, který rozšiřuje třídu
:třída odoo.model.TransientModel namísto
Třída: ~odoo.models.Model. Třída
Třída TransientModel dědí z třídy Model
a znovu použít všechny své stávající mechanismy s následujícími zvláštnostmi:

- Čáry jsou neustále odstraňovány, protože jsou automaticky smazány.
z databáze po určité době. Proto se jim říká
*přechodný*.
- Wizard Records mohou odkazovat na běžné záznamy nebo na záznamy kouzelníků prostřednictvím vztahového
pole (mnoho2jedno nebo mnoho2mnoho), ale běžné záznamy nemohou odkazovat na záznamy z katalogu přes
pole typu many-to-one.

Chceme vytvořit kouzelníka, který umožňuje uživatelům přidávat účastníky na konkrétní událost.
pro jednu lekci nebo pro seznam všech lekcí najednou.

.. cvičení:Definujte kouzelníka

Vytvořte šablonu pro průvodce s mnoho-k-jednomu vztahem k Session.
model a mnoho-množstevní vztah s modelem Partner.

Spouštění kouzelníků
-----------------

Čarodějové jsou prostě jenom „akce okna“ s atributem „target“.
pole nastavené na hodnotu „nový“, které otevře pohled
(obvykle:ref: 'form <howtos/module/views/form>') v samostatném dialogu.
Akce může být spuštěna pomocí položky nabídky, ale obecněji je spouštěna
tlačítko.

Další způsob, jak spustit kouzelníky, je skrze nabídku „Akce“ v
seznam nebo tabulkový pohled. To se provádí pomocí pole „vázání modelu“
akce. Přiřazením hodnoty této položky se akce zobrazí na pohledech modelu
Akce je „vázána“ na něj.

.. kód::xml


<políčko jméno>Spusťte průvodce</políčko>
<položka jméno>wizard.model.name</položka>
<field name="zobrazovací mód">formulář</field>
<vlastnost name="cíl">nový</vlastnost>
<pole název="vazba_model_id" odkaz="model_kontext_model_odkaz"/>
</záznam>

..tip:
Zatímco kouzelníci používají běžné pohledy a tlačítka, obvykle stačí na jakékoliv tlačítko kliknout.
- formulář by nejprve uložil formulář, pak zavřel dialogové okno.
často nežádoucí u kouzelníků, existuje zvláštní atribut „special=cancel“
dostupných, které okamžitě uzavře průvodce bez uložení formuláře.

... cvičení: Spusťte průvodce

   #Vytvořte vlastní pohled na formulář pro průvodce.
   #Přidejte akci, která ji spustí v kontextu modelu *Session*.
   #.Definujte výchozí hodnotu pole session v průvodci; použijte
parametru kontextu „self._context“ k získání aktuální relace.

..cvičení: Přihlášení účastníků

Přidejte tlačítka do průvodce a implementujte odpovídající metodu pro přidání
účastníci dané sekce.

...cvičení:Přihlásit se na více přednášek

Upravit vzorce pro registraci účastníků tak, aby se mohli zaregistrovat na více
sezení.

Internacionalizace
====================

Každý modul může poskytnout své vlastní překlady v adresáři i18n.
soubory s názvem LANG.po, kde LANG je kód pro lokalizaci jazyka.
Jazyk a země v případě, že se liší (např. pt.po nebo
pt_BR.po). Přeložení bude načteno automaticky v Odoo pro všechny
povolené jazyky. Vývojáři vždy používají angličtinu při tvorbě modulu, pak
Exportovat modulové termíny pomocí funkce exportu POT v Odoo
(:menu_selection:"Nastavení --> Překlady --> Import/Export --> Export
Přeložit (bez specifikace jazyka), vytvořit šablonu modulu POT
souboru a poté vytvořit překlady souborů PO. Mnoho integrovaných vývojových prostředí má pluginy nebo režimy
pro editaci a sloučení souborů PO/POT.

..tip:
Portable Object soubory generované Odoo jsou publikovány na platformě pro překlad Odoo.
<https://translate.odoo.com/>`, což usnadňuje překlad softwaru.

... blok kódu:: text

|- nápad/  # Modulární adresář
|- lokalizace/ # Lokální soubory
| - idea.pot # Přeloženo z Odoo
| - cs.po # Czech translation
| - cs.po # Czech
        | (...)

..tip:
Výchozí export POT od OpenERP extrahuje pouze štítky uvnitř souborů XML nebo
uvnitř definice pole v Pythonovém kódu, ale jakýkoliv řetězec Pythonu
přeloženy takto, že je obklopí funkce :func:`odoo._`.
(např. "_(Název)``")

.. cvičení: Přeložit modul

Vyberte si druhý jazyk pro svou instalaci Odoo. Přeložte
modul využívající funkce poskytované systémem Odoo.

Reportér
=========

Tiskové zprávy
---------------

Odoo používá reportovací motor založený na :ref:`reference/qweb`.
„Bootstrap“ a „Wkhtmltopdf“.

Zpráva je kombinací dvou prvků:

* „ir.akce.report“ s různými základními parametry pro
report (výchozí typ, zda se má report uložit do databáze
... po generaci, ...



<záznam id="faktury" model="ir.actions.report">
<polozka name="název">Faktury</polozka>
<položka název="model">účet.faktura</položka>
<field name="report_type">qweb-pdf</field>
<field name="report_name">účet.report_faktura</field>
<field name="report_file">účet.report_faktura</field>
<sloupce jméno="připojení_používá" hodnota="Pravda"/>
<field name="příloha">(stav_objektu() in ('otevřený', 'zaplaceno')) a
(„INV“ + (objekt.číslo nebo „“).replace(„/“, „“) + „.pdf“)
<vlastnost jméno="vazba_model_id" odkaz="účet - faktura"/>
<položka jméno="vazba_typ">report</položka>
</záznam>

..tip:

Protože je to převážně standartní akce, viz též :ref:`jak na to/moduly/wizard`.
Většinou je užitečné přidat zprávu jako kontextový prvek.
seznam a/nebo pohled na model, který je předmětem zprávy.
„vazební model“ pole.

Zde používáme „binding_type“, abychom mohli vytvořit zprávu.
místo nabídky „akce“ je nabídka „zpráva“.
Technická rozdíl, ale umístění prvků na správném místě pomáhá uživatelům.

* Standardní QWeb pohled na skutečnou zprávu:



<t t-call="web.html_container">
<t t-foreach="dokumenty" t-as="o">
<t t-call="web.externi_layout">

<h2>Název zprávy</h2>

</t>
</t>


Standardní zpracování obsahuje řadu prvků, z nichž nejdůležitější jsou
důležitý člověk:

„dokumenty“
pro které je tiskováno hlášení
„uživatel“
uživatel tisknoucí zprávu

Protože jsou zprávy běžnými webovými stránkami, lze je získat prostřednictvím URL adresy.
parametry výstupu lze upravit prostřednictvím této adresy URL například pomocí HTML
verze zprávy „Faktura“ je dostupná prostřednictvím
http://localhost:8069/report/html/account.report_invoice/1 (if ``account`` is
a verzi ve formátu PDF.
http://localhost:8069/report/pdf/account.report_invoice/1.

.. odkaz/zadní část/reporty/tiskové zprávy/bez stylů:

.. nebezpečí::

Pokud se zdá, že vaše PDF zpráva chybí styl (tj. text)
Pokud se stránka zobrazí, ale styl a uspořádání je odlišné od verze HTML (pravděpodobně
proces vašeho wkhtmltopdf nemůže dosáhnout na váš webový server, aby si stáhl tyto soubory.

Pokud se podíváte do protokolu svého serveru a uvidíte, že CSS stylů není používáno
Pokud se stahuje při generování PDF zprávy, je to nejspíš problém.

Proces wkhtmltopdf bude používat systémový parametr „web.base.url“,
kořenový adresář všech odkazovaných souborů, ale tento parametr je automaticky
aktualizován pokaždé, když se do systému přihlásí administrátor. Pokud váš server
za nějakým druhem proxy, který není dostupný. Tento problém lze vyřešit tak, že
přidáním jednoho z těchto parametrů systému:

   - „report.url“, který odkazuje na URL dostupný z vašeho serveru
(nejspíš „http://localhost:8069“ nebo něco podobného). Bude
používána výhradně pro tento účel.

   - Pokud je nastaveno na hodnotu „true“, bude funkce „web.base.url.freeze“ zastavena.
automatické aktualizace „web.base.url“.

...cvičení: Vytvořit zprávu pro model Session

Pro každou sekci by mělo zobrazit název sekce, její začátek a konec.
a zobrazit seznam účastníků jednání.

Dashboardy
----------

...cvičení: Vytvořte panel nástrojů

Definujte panel obsahující grafickou zobrazení, které jste vytvořili, a sekce.
kalendářový pohled a seznam kurzů (přepínatelný do tabulkového
Zobrazení) by mělo být dostupné prostřednictvím položky v nabídce.
a automaticky se zobrazí v prohlížečovém klientovi při přístupu na hlavní stránku
menu je vybráno.

..[#auto_fields] lze deaktivovat automatické vytváření některých
pole <odkaz/pole/automatické/log_access>
...[#rawsql] psaní neupravených SQL dotazů je možné, ale vyžaduje opatrnost, protože
přebíhá všechna odoo autentizační a bezpečnostní opatření.

..._index databáze:
    https://use-the-index-luke.com/sql/preface
..._POEdit: https://poedit.net
... Dokumentace PostgreSQL
.._tabulková omezení:
    https://www.postgresql.org/docs/12/static/ddl-constraints.html
.._Python: https://python.org
.._XPath: https://www.w3.org/TR/xpath
.._twitter bootstrap: https://getbootstrap.com
..._wkhtmltopdf: https://wkhtmltopdf.org
