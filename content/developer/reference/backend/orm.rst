Zobrazit obsah

.._odkaz/orm:

=======
ORM API
=======

.. toctree::


orm/changelog

..automoduly: odoo.models

.. odkaz na model:
.._odkaz/orm/model:

Modelky
======

Modelové pole je definováno jako atribut na samotný model:

od odoo importujeme modely a pole
class AModel(models.Model):
name = "a.model.name"

field1 = fields.char

Upozornění: to znamená, že nemůžete definovat pole a metodu s tím samým
jméno, poslední přepsává všechny předchozí.

Výchozí název pole (viditelný uživateli název) je velkým písmenem.
název pole, který lze přehrát pomocí parametru „string“.

field2 = fields.Integer(string="Popis pole")

Pro seznam polí a parametrů vidíte v :ref:`odkazu na pole
<odkaz/pole>.

Výchozí hodnoty jsou definovány jako parametry na polích, buď jako hodnota:

name = fields.Char(výchozí hodnota="hodnota")

nebo jako funkci volanou k výpočtu výchozí hodnoty, která by měla vracet
hodnota::

def _default_name(self):
vrací sebe sama

jméno = fields.Char(výchozí hodnota = lambda sebe: sebe._default_jmeno)

..rubrice:: API

... autoklasifikátor: odoo.models.BaseModel

...... atribut auto::_auto
.... atribut:: _log_access

Zda by měl ORM automaticky generovat a aktualizovat.
:ref:`reference/fields/automatic/log_access`.

Výchozí hodnota je nastavena na hodnotu, kterou bylo přiřazeno atributu :attr:`~._auto`.

......autoatribut::_tabulka
.. autoatribut:: _sql_check

......autoatribut::_registrace
..autoatribut::_abstrakt
.. autoatribut:: _transient

.. autoatribut:: _name
.. autoatribut:: _description

......autoatribut::_dědit
......autoatribut::_dědí

.. autoatribut:: _rec_name
......autoatribut::_pořadí

.. autoattribute:: _check_company_auto

......autoatribut::_parent_name
... autoatribut:: _parent_store

... autoatribut:: _fold_name

Abstraktní model
-------------

... autoklasifikace: odoo.model.abstract_model

Model
-----

... auto_class: odoo.models.Model

......atribut auto::_auto
......autoatribut::_abstrakt

Přechodný model
--------------

... autoklasifikace: odoo.models.TransientModel
:členové: _přechodná vakuum

......autoatribut:: _transient_max_count
......autoatribut:: _transient_max_hours

.. odkaz/pole:
.._odkaz/orm/pole:

Pole
======

...současný modul: odoo.fields

... autoklasifikace: pole

.._odkaz/pole/základní:

Základní pole
------------

... autoklasifikátor: Boolean

... autoklasifikace: Char()

... třída autoclass: Float

... autoClass: Integer

.._odkaz/pole/pokročilé:

Pokročilá pole
---------------

... autoklasifikátor: Binary()

... autoClass: Html()

... autoClass: Image()

... autoklasifikátor: Monetární

... autoClass: Select()

... autoklasifikace: Text()

.. odkaz/pole/datum:

Datum a čas Hodnoty
~~~~~~~~~~~~~~~~~

:třída Dates a třída Datetimes
Jsou velmi důležitými oblastmi v jakékoliv podnikové aplikaci.
Nesprávné používání může vytvořit neviditelné a bolestivé chyby, viz tento oddíl.
chce poskytnout vývojářům Odoo potřebné znalosti.
aby se vyvarovaly zneužití těchto polí.

Při přiřazování hodnoty do pole Datum/Datum a čas platí následující možnosti:

* Objekt datum nebo datum a čas.
* Struna v správném formátu serveru:

  * „YYYY-MM-DD“ pro pole typu „Datum“
  * „RRRR-MM-DD HH:MM:SS“ pro pole typu „Datum a čas“.

* „Pravda“ nebo „Nic“.

Třída Date a Datetime má metody, které se pokusí provést převod
do kompatibilního typu:

* Funkce `odoo.fields.Date.to_date()` převede na objekt typu `datetime.date`.
* Funkce ~odoo.fields.Datetime.to_datetime převede na objekt :class:`datetime.datetime`.

Příklad:

Pro zpracování dat a časů přicházejících z externích zdrojů:

fields.Datum.z_data(self._context.get('date_from'))

Praktiky při porovnávání dat a času:

* Datumové pole lze porovnávat pouze s objekty datumu.
* Datumové pole může být porovnáno pouze s datem objektu.

.. upozornění: Strings reprezentující data a časové údaje se dají porovnávat.
Vzájemně se však mohou vytvářet nové sloučeniny, které nemusí být očekávané.
Výsledkem je, že datum a časová značka vždy budou větší než
datový řetězec, proto je tento postup **velmi**
se nechce zapojit.

Obvyklé operace s daty a časem, jako je například sčítání, odčítání nebo
Začátek a konec období jsou vystaveny prostřednictvím obou
:třída odoo.fields.Date a :třída odoo.fields.Datetime.
Tyto pomocníky lze také dostat importem modulu „odoo.tools.date_utils“.

.. poznámka: časové pásmo

Datumové pole jsou uložena jako sloupce typu timestamp bez časového pásma v databázi a jsou uchovávána
v časovém pásmu UTC. To je účelové, protože tím se databáze Odoo stane nezávislou na časovém pásmu.
systému hostitele. Časové pásmo se převádí na straně klienta.

... autoClass: Date()
:členové: dnes, kontext_dnes, do_datumu, do_řetězce, začátek, konec, přičítat, odečítat

... třída autoclass: Datetime
:členové: nyní, dnes, kontext_datum, na_datum, na_řetězec, začátek, konec, přičítat, odečítat

.._odkaz/pole/vztahové:

Relacionální pole
~~~~~~~~~~~~~~~~~

... autoklasifikátor: Many2One()

... autoklasifikátor: one2many()

... autoklasifikátor: many_to_many()

... autoklasifikátor: Command()
:členové:
:nečlenové:
:členství: podle zdroje

Pseudovazebná pole
~~~~~~~~~~~~~~~~~~~~~~~~

... autoklasifikátor: Reference()

... autoklasifikace: Many2OneReference()

.. odkaz/pole/výpočet:

Výpočetní pole
~~~~~~~~~~~~~~~

Pole mohou být vypočítána (místo čtení přímo z databáze) pomocí
parametr „vypočítat“. **Musí přiřadit vypočtenou hodnotu pole**. Pokud
používá hodnoty jiných polí, měla by uvést tyto pole
:funkce: ~odoo.api.depends::

od odoo import api
celkem = fields.Float('_compute_total', compute=True)

@api.depends('value','daň')
def _vypočítat_celkový(self):
pro rekord v sobě:
celkem = hodnota záznamu + hodnota záznamu * daň

* závislosti mohou být čárkované cesty, pokud používáte podpole:

@api.depends('line_ids.value')
def _vypočítat_celkový(self):
pro rekord v sobě:
celkem = součet (hodnota řádku pro každý řádek v seznamu hodnot řádků)

* Předdefinované pole nejsou uložena automaticky.
Vyžádané objekty se vrátí. Při nastavení „store=True“ budou uloženy v paměti.
databáze a automaticky zapnout vyhledávání.
* Vyhledávání v poli počítaném lze také zapnout nastavením „vyhledat“.
parametr, hodnota je název metody vracící hodnotu
:ref:`reference/orm/domény`. ::

upper_name = pole.Char(vypočítat='_vypočítat_upper', vyhledávat='_vyhledávat_upper')

def _search_upper(self, operátor, hodnota):
pokud je operátor roven „like“:
operátor = 'ilike'
vrací seznam [('name', operátor, hodnota)]

Metoda vyhledávání je spouštěna před zpracováním domén.
skutečné vyhledávání na modelech. Musí se vrátit doménou odpovídajícímu
podmínka: „operátor pole hodnota“.

… a nebo nastavit obchod na hodnotu True pro doménu vyhledávání?

* Předdefinované pole jsou čitelná výchozí hodnotou. Chcete-li umožnit nastavení hodnoty na předdefinovaném poli, použijte „inverse“.
parametrem je jméno funkce, která obráží výpočet.
nastavení příslušných polí:

dokument = pole.Char(vypočítat = "_get_document", obráceně = "_set_document")

def _get_dokument(self):
pro rekord v sobě:
s otevřeným f = open(cesta_k_souboru_dokumentu_pro_record):
rekord.dokument = f.read()
def _set_dokument(self):
pro rekord v sobě:
pokud není dokument, pokračujte
s otevřeným(f = open(cesta_k_souboru_dokumentu_pro_zaznamenání))
f.write(record.dokument)

* Může být vypočítáno více polí najednou stejným způsobem.
použít stejný postup na všechna pole a nastavit je takto:

sleva_v_procentech = fields.Float('_apply_discount', výpočet=True)
celkem = fields.Float('_apply_discount', compute=True)

@api.depends('hodnota', 'sleva')
def __apply_discount(self):
pro rekord v sobě:
            # Počítat skutečnou slevu z procenta slevy
slevový faktor = hodnota záznamu * slevový faktor
record.sleva.hodnota = sleva
celková cena = hodnota záznamu - sleva

.. varování:

Zatímco je možné používat stejný výpočetní postup pro více objektů,
pole, není vhodné provádět stejnou operaci pro obrácené pole.
metoda.

Při výpočtu inverzního zobrazení se používají všechny pole, která
uvedl, že obrázek je chráněn, což znamená, že jej nelze počítat.
i když jejich hodnota není v mezipaměti.

Pokud se na některém z těchto políček pokusíte přečíst hodnotu a ta není v mezipaměti,
ORM jednoduše vrátí výchozí hodnotu False pro tyto pole.
To znamená, že hodnota obrácených polí (kromě jednoho)
(vyvolávají obrácený postup) nemusí mít správnou hodnotu a
To pravděpodobně naruší očekávané chování zpětného postupu.

.. odkaz/pole/související:

Související obory
~~~~~~~~~~~~~~

Speciálním případem vypočítaných polí jsou pole vztahovaná (proxy), která poskytují
hodnota podsložky na aktuálním záznamu. Jsou definovány nastavením
parametr „související“ a stejně jako běžné vypočítané pole mohou být
ukládá se do paměti

přezdívka = pole.Char(souvisí s 'user_id.partner_id.name', uchovává hodnotu True)

Hodnota souvisejícího pole je dána následujícím postupem
vztahové pole a čtení pole na dosaženém modelu.
seznam polí, která mají být procházena, je určen atributem „related“.

Některé pole vlastností jsou automaticky kopírovány z zdrojového pole.
nejsou přeformátovány: „str“, „pomoc“ a „nutné“ (jen
pokud jsou všechny pole v sekvenci povinná) „skupiny“, „číslice“, „velikost“
„přeložit“, „vyčistit“, „výběr“, „název modelu“, „doména“
„kontext“. Všechny bezsemantické atributy jsou zkopírovány ze zdroje
pole.

Výchozími souvisejícími poli jsou:

* neukládá se
* nebylo kopírováno
* jen pro čtení
* počítané v režimu superuživatele

Přidejte atribut „store=True“, aby se uložil stejně jako vypočítaný.
položky. Související položky se automaticky znovu vypočítají, když
závislosti jsou upraveny.

..tip:

Pokud nechcete, můžete specifikovat přesné závislosti polí.
související pole, které se má znovu vypočítat při změně závislosti::

nickname = fields.Char
partner_id = 'partner_id.name',
závisí na partner_id
        # Nick se vypočítává pouze při změně partnera.
        # je upravena, nikoliv když se mění jméno na partnerovi.

.. varování:

Nelze propojit pole typu :class:`~odoo.fields.Many2many` nebo :class:`~odoo.fields.One2many` v závislosti na polích „souvisejících“.

„související“ lze použít k odkazu na pole :class:`~odoo.fields.One2many`.
:třída odoo.pole.Mnoho2množství pole na jiném modelu v
podmínkou, že se provede pomocí vztahu „Many2One“ na aktuálním modelu.
„One2many“ a „Many2many“ nejsou podporovány a výsledky nebudou
výpočet byl správně proveden::

m2o_id = fields.many2one()
m2m_ids = pole.Many2many()
o2m_ids = pole.One2many

      # Podporované
d_ids = pole.Many2many(související="m2o_id.m2m_ids")
e_ids = pole.One2many(vztahující se na "m2o_id.o2m_ids")

      # Nevyhovuje: použijte vlastní pole s počtem položek namísto
f_ids = pole.MnohoNaMnoho(související="m2m_ids.m2m_ids")
g_ids = pole.One2many(související="o2m_ids.o2m_ids")

.. současný modul: odoo.model

.._odkaz/pole/automatické:

Automatické pole
----------------

.. atribut::Model.id

Identifikátor: třída `field <odoo.fields.Field>`

Pokud je délka aktuálního záznamového souboru rovna jedné, vrátí ID jedinečného záznamu v něm.

Jinak vyvolat chybu.

... atribut::Model.display_name

Jméno: pole typu `char` zobrazené v prohlížeči výchozím způsobem

Výchozí hodnota je stejná jako pole :attr:`~odoo.models.BaseModel._rec_name`.
chování lze přizpůsobit přepsáním metody _compute_display_name

.. _reference/fields/automatic/log_access:

Pole záznamu přístupů
~~~~~~~~~~~~~~~~~

Tyto pole jsou automaticky nastavena a aktualizována, pokud
:attr:`~odoo.models.BaseModel._log_access` je zapnutý. Může být
znefunkčnění, aby se nemusely vytvářet nebo aktualizovat sloupce tabulek pro ně.
nepoužitelný.

Výchozí hodnota metody :attr:`~odoo.models.BaseModel._log_access` je stejná
jako: ~odoo.models.BaseModel._auto

.. atribut::Model.create_date

Datum a čas vytvoření záznamu, :class:`~odoo.fields.datetime`

... atribut:: Model.create_uid

Obchody, které vytvořily rekord, jsou uloženy do pole typu
"res.users".

.. atribut::Model.write_date

Datum poslední aktualizace záznamu, :class:`~odoo.fields.Datetime`

... atribut::Model.write_uid

Obchody, které naposledy aktualizovaly záznam, :class:`~odoo.fields.Many2one` na
"res.users".

.. varování: metoda `~odoo.models.BaseModel._log_access` *musí být* zapnutá
:třída:`~odoo.models.TransientModel`.

.._odkaz/orm/pole/rezervované:

Rezervovaná pole jmen
--------------------

Několik polí je vyhrazeno pro předdefinované chování nad rámec
automatické pole. Jejich definice je na modelu, kde jsou k nim vztahy
chování je žádoucí:

.. atribut: Jméno modelu

výchozí hodnota pro atribut ~odoo.models.BaseModel._rec_name, používaný k
zobrazit záznamy v kontextu, kde je reprezentativní „název“
Je nezbytné.

:třída: :class:`~odoo.fields.Char`

... atribut: Model.active

aktivuje globální viditelnost záznamu.
„Pravda“ je záznam skrytý ve většině vyhledávání a seznamů.

:třída:`~odoo.fields.Boolean

Speciální metody:

....automethode::Model.toggle_active
......automethod:Model.action_archive
... metoda: Model.action_unarchive

.. atribut::Model.stát

stupně životního cyklu objektu, používané atributem „Stavy“
:třída:`fields <odoo.fields.Field>`.

:třída:`~odoo.fields.Selection

.. atribut: Model.parent_id

výchozí hodnota atributu ~._parent_name, používaná k uspořádání
záznamy v hierarchické struktuře a umožňuje „dítě“
a „rodič“ a „dítě“ v doménách.

:třída:`~odoo.fields.many2one

.. atribut: Model.parent_path

Při nastavení atributu ~._parent_store na hodnotu True se používá k uložení hodnoty odrážející
stromovou strukturu atributu :attr:`~._parent_name` a optimalizovat operátory
„dítě“ a „rodič“ v doménách vyhledávání.
Musí být deklarován s „index=True“, aby správně fungoval.

:třída:`~odoo.fields.Char

.. atribut: Model.company_id

Hlavní pole používané pro chování více společností v Odoo.

Používá se metodou :meth:~odoo.models._check_company, která kontroluje soulad s více společnostmi.
Definuje, zda je záznam společný mezi firmami (bez hodnoty) nebo pouze
přístupná uživatelům konkrétní společnosti.

:třída:`~odoo.fields.many2one
:typ: :třída:`~odoo.addons.base.models.res_company`

Recordsety
==========

Interakce s modelem a záznamy se provádí pomocí Recordsetu, což je uspořádaný
soubor záznamů stejného typu.

.. varování: I přes své jméno je v současné době možné
záznamy obsahují duplicitní záznamy. To se může v budoucnu změnit.

Metody definované na modelech jsou prováděny na objektu RecordSet a jejich „self“
recordset::

class AModel(models.Model):
name = "a.model"
def a_metoda(self):
            # self může být cokoli mezi 0 záznamy a všemi záznamy v
            # databáze
self.vykonat_operace()

Opakování na záznamovém setu vytvoří nové sady *jednoho záznamu*.
„jednotlivci“, podobně jako iterace nad Pythonovským řetězcem vrací řetězce.
jednotlivé znaky:

def do_operace(self):
print(self) # =>a.model(1, 2, 3, 4, 5)
pro rekord v sobě:
print(record) # => a.model(1), pak a.model(2), pak a.model(3), atd.

Přístup do pole
------------

Nástroje Recordset poskytují „aktivní záznam“: pole modelu lze číst a
psané přímo z nahrávky jako atributy.

.. poznámka::

Při přístupu k ne-relačním polím v seznamu záznamů, které mohou obsahovat více
záznamy použijte metodu:

celkové množství = součet (self.mapped('qty'))

Hodnoty pole lze také přistupovat jako k položkám v seznamu, což je elegantnější a
bezpečnější než funkce „getattr()“ pro dynamické názvy polí.
Přiřazení hodnoty pole vyvolá aktualizaci databáze:

>>> jméno_záznamu
Příklad: Jméno
>>>record.firma_id.jmeno
Název společnosti
>>>record.jméno = "Bob"
>>> pole = "jméno"
>>>record[pole]
Bob

.. varování:

Pokus o čtení pole na více záznamů vyvolá chybu pro ne-relativní položky.
pole.

Přístup k vztahovému poli (:class:`~odoo.fields.Many2one`)
:třída:`~odoo.fields.One2many`, :třída:`~odoo.fields.Many2many`)
Vždy vrátí objekt Recordset, který je prázdný, pokud pole není nastaveno.

Záznamy v mezipaměti a předčítání
----------------------------

Odoo udržuje cache pro pole záznamů, takže ne každé pole
Přístup k databázi vytváří požadavek na databázi, což by bylo pro výkon špatné.
Následující příklad dotazuje databázi pouze na první výrok:

record.jméno           # první přístup čte hodnotu z databáze
record.jméno           # druhý přístup získá hodnotu ze cache

Aby se předešlo čtení jednoho pole na jeden záznam najednou, Odoo předčítá záznamy
a pole, která následují nějaké heuristické pravidlo pro dosažení dobrého výkonu.
se čte z daného záznamu, ORM skutečně čte pole na větším
Výsledky se ukládají do mezipaměti pro pozdější použití.
recordset je obvykle recordset, ze kterého pochází záznam při iteracích.
Kromě toho jsou všechna jednoduchá pole uložená (boolean, integer, float, char, text, date)
Datum a výběr (many2one) jsou získávány společně.
sloupce tabulky modelu a jsou efektivně vyhledávány v rámci stejného dotazu.

Pojďme se podívat na následující příklad, kde „partner“ je záznamové pole s 1000
databáze. Bez předčítání by smyčka provedla 2000 dotazů na databázi.
S předčtením je proveden pouze jeden dotaz:

pro partnery v partnerech:
print partner.name          # první průchod předběžně načítá 'name' a 'lang'
                                    # a dalších oborech na všech „partnerech“
tisknout partner.lang

Prefetchování funguje i na sekundárních záznamcích: když jsou v relačním poli
četl, jejich hodnoty (které jsou rekordy) se předpokládají pro budoucí předběžné načítání.
Přístup k jednomu z těchto sekundárních záznamů předčítá všechny sekundární záznamy.
stejný model. To dělá následující příklad generovat pouze dvě dotazy, jednu
pro partnery a jeden pro země::

země = set()
pro partnery v partnerech:
země = partner.země_id           # první průchod předpřipravení všech partnerů
země.add(zemi.název)         # první průchod předvybírá všechny země

.. viz též:
Metody :meth:`~odoo.models.Model.search_fetch`.
:metoda ~odoo.models.Model.fetch může být použita k naplnění mezipaměti
záznamy, obvykle v případech, kdy se nevyužívá předčítací mechanismus
dobře.


..._odkaz/api/dekorátory:

Metoda dekorátorů
=================

..automodul: odoo.api
:členové: závisí, závislosti_kontextu, omezuje, při změně, vrací, automatické čištění, model, model_vytvořit_více

.. .současný modul:: odoo.api

.. ... autodata:: model
.. . . auto data: závisí
.. . autodata: omezuje
.. .autodata:: načtení
.. .autodata: vrací
.. . autodata: autovakuum

... vše: S verzí 2.0: automatický dekorátor

...: Přidat odkaz na Views
  * Možné je potlačit spoušť z konkrétního pole přidáním
„on_change=“0““ v pohledu:

<položka název on_change="0"/>

nebude vyvolávat žádné změny v rozhraní, když uživatel upraví pole.
i když existují funkční pole nebo explicitní onchange, které se na toto vztahují
pole.

.. odkaz na ORM a prostředí:

Životní prostředí
===========

... aktuální modul:: odoo.api

... autoklasifikace: prostředí

... kódový blok:: bash

>>> records.env
<Objekt prostředí ...>
>>> records.env.uid
    3
>>> records.env.user
res.user(3)
>>>records.env.cr
<Objekt myši ...>

Při vytváření záznamového souboru z jiného záznamového souboru je
dědičné. V prostředí lze získat prázdný záznam v
jiný model a dotazujte tento model:

... kódový blok:: bash

>>>self.env['res.partner']
partner().
>>>self.env['res.partner'].search([('is_company', '=', True), ('customer', '=', True)])
res.partner(7, 18, 12, 14, 17, 19, 8, 31, 26, 16, 13, 20, 30, 22, 29, 15, 23, 28, 74)

Některé neaktivní vlastnosti umožňují přístup k prostředí (kontextuálním) datům:

...autoatribut::Environment.lang
... autoatributu: Environment.user
...autoatribut::Environment.company
...autoatribut::Environment.firmy

Užitečné metody ochrany životního prostředí
--------------------------

...automethod:Environment.ref
..automethod:Environment.is_superuser
...automethod:Environment.is_admin
...automethode::Environment.is_system
...automethode:Environment.execute_query

Změna prostředí
------------------------

.. současný modul: odoo.model

...automethod:Model.s kontextem

...automethod:Model.with_user

...automethod:Model.s_spolecností

...automethod:Model.with_env

...automethod:Model.sudo

.._reference/orm/sql:

Výkonnost SQL
-------------

Atribut :attr:`~odoo.api.Environment.cr` na prostředí je
pozice aktuální databázové transakce a umožňuje provádět příkazy SQL přímo.
ať už pro dotazy, které jsou obtížné vyjádřit pomocí ORM (například složitější
nebo z důvodu výkonnosti:

self.env.cr.execute("some_sql", params)

.. varování:
Vykonávání neupraveného SQL obchází ORM a tím pádem i bezpečnostní pravidla Odoo.
Prosím, ujistěte se, že vaše dotazy jsou ošetřeny při použití vstupu od uživatele a raději používejte
ORM nástroje, pokud skutečně nepotřebujete používat SQL dotazy.

Doporučený způsob stavění SQL dotazů je použití objektu wrapper

... autoklasifikace: odoo.nástroje.SQL

... metoda: SQL.join
......automethode::SQL.identifikátor

Důležité je vědět, že modely nemusí být vždy přesné.
databáze aktualizuje okamžitě. Ve skutečnosti je to kvůli výkonu takto nastaveno.
zpožďuje přepočítání polí po úpravě záznamů. A některé databáze
Aktualizace jsou také zpožděné, proto je třeba před dotazem na databázi
zajistit, aby obsahovala potřebná data pro dotaz. Tato operace je
a provádí očekávané aktualizace databáze.

Příklad:

.. kódový blok:: python

        # zajistit, aby v databázi byla aktuální hodnota partner_id
self.env['model'].flush_model(["partner_id"])

self.env.cr.execute(SQL("SELECT id FROM model WHERE partner_id IN %s", ids))
ids = [řádek[0] pro řádek v seznamu objektů self.env.cr.fetchall()]

Před každou dotazovací SQL příkaz musí být vyprázdněna data potřebná pro tento příkaz.
Existují tři úrovně pro splachování, každá s vlastním API. Můžete buď
vše, všechny záznamy modelu nebo některé konkrétní záznamy. Protože
odložení aktualizací zlepšuje výkon v obecném smyslu. Doporučujeme být konkrétní.
Při čištění.

...automethode: odoo.api.Environment.flush_all

...automethod::Model.flush_model

...automethod:Model.flush_recordset

Modelové aplikace používají stejný kurzor a objekt Environment
obsahuje různé cache, tyto cache musí být neplatné po jakémkoliv
databáze v syrovém SQL nebo další použití modelů se mohou stát nesourodými.
je nutné vymazat cache při použití příkazů „CREATE“, „UPDATE“ nebo „DELETE“.
SQL, ale ne „SELECT“ (který jen čte databázi).

Příklad:

.. kódový blok:: python

        # zajistit, aby v databázi byla aktuální hodnota státu
self.env['model'].flush_model(["stát"])

self.env.cr.execute("UPDATE model SET state=%s WHERE state=%s", ['nový', 'starý'])

        # vymazat stav z mezipaměti
self.env['model'].invalidace_modelu(["stát"])

Stejně jako u splachování lze vymazat celý mezipaměť nebo paměť všech
záznamy modelu nebo konkrétní záznamy. Dokonce i
neplatnost konkrétních polí v některých záznamů nebo všech záznamů modelu.
Cache obecně zlepšuje výkon, doporučujeme být konkrétní.
neplatnost.

...automethode: odoo.api.Environment.invalidate_all

... metoda:Model.invalidate_model

...automethode::Model.invalidate_recordset

Metody výše udržují cache a databázi v souladu s sebou navzájem.
Pokud byly v databázi změněny počítané pole závislosti,
musí informovat modely o tom, že se mají vypočítané pole znovu vypočítat.
to, co rámec potřebuje vědět je, jaké pole se změnilo na kterém
dokumenty.

Příklad:

.. kódový blok:: python

        # zajistit, aby v databázi byla aktuální hodnota státu
self.env['model'].flush_model(["stát"])

        # použijte vrácení, abyste zjistili, které řádky byly změněny
self.env.cr.execute("UPDATE model SET state=%s WHERE state=%s RETURNING id", ['nový', 'starý'])
ids = [řádek[0] pro řádek v seznamu objektů self.env.cr.fetchall()]

        # vymazat mezipaměť a oznámit aktualizaci rámci
záznamy = self.env['model'].browse(idy)
records.invalidate_recordset(["stát"])
records.modify(['stát'])

Je třeba zjistit, které záznamy byly změněny. Existuje mnoho způsobů, jak
Provedení této akce může vyžadovat další dotazy na databázi. V příkladu výše provedeme
výhodou „RETURNING“ v příkazu PostgreSQL pro získání informací
bez dalšího dotazu. Po provedení vyčištění mezipaměti zneplatněním
vyvolat metodu „modifikovaný“ na upravených záznamů s poli, která
byly aktualizovány.

...automethod:Model.modifikovany


.._odkaz/orm/modely/crud:

Běžné metody ORM
==================

.. současný modul: odoo.model

Vytvořit/aktualizovat
-------------

... vše: api.model_create_multi informace

...automethod:Model.create

...automethod:Model.copy

...automethod:Model.default_get

...automethod:Model.name_create

...automethod:Model.Write

Hledat/Číst
-----------

...automethod::Model.prohlížet

...automethod::Model.search

...automethod:Model.search_count

...automethode::Model.search_fetch

...automethod:Model.name_search

...automethod:Model.fetch

...automethod:Model.read

...automethod:Model._read_group

...automethod:Model.read_group

Pole
~~~~~~

...automethod:Model.fields_get

.._odkaz/orm/domény:

Domény pro vyhledávání
~~~~~~~~~~~~~~

Doména je seznam kritérií, každé kritérium je trojice (buď
„seznam“ nebo „tupla“ z položek „(název pole, operátor, hodnota)“, kde:

* „pole_jméno“ („str“)
jméno pole aktuálního modelu nebo cesta vztahem.
a:klasa:~odoo.fields.Many2one používající znaménkovou notaci např. „ulice“
nebo „partner_id.země“. Pokud je pole datumovým (časovým), můžete také
Specifikovat část dat pomocí „'field_name.granularity'“. Podporované
granularity jsou „rok_číslo“, „čtvrtletí_číslo“, „měsíc_číslo“, „ISO_týdenní_číslo“
„den v týdnu“, „den v měsíci“, „den v roce“, „hodina“, „minuta“
„`druhé číslo`“.
Všechny používají celé číslo jako hodnotu.

* „operátor“ („str“)
operátor, který porovnává „název pole“ s „hodnotou“.
Operátoři jsou:

    ``=``
rovná se
    ``!=``
nepovídá
    ``>``
větší než
    ``>=``
nebo větší než
    ``<``
méně než
    ``<=``
menší nebo rovno
    ``=?``
nebo rovná se (vrací „pravdu“, pokud je „hodnota“ buď „None“ nebo
„Pravda“ nebo „nepravda“, jinak chová jako „==“
„=podobně“
hodnotu vzoru „hodnota“. Znak podtržítka se používá k vyhledání
„_“ v tomto vzoru znamená libovolný jednotlivý znak.
znaménko procenta „%“ odpovídá libovolnému řetězci nul nebo více znaků.
„jako“
hodnota pole „field_name“ odpovídá vzoru „%value%“. Podobně jako
„=like“, ale před porovnáním „hodnotu“ obalí znakem procenta
„ne jako“
neodpovídá vzoru „%hodnota%“.
„Ilike“
případně „nezáleží na velikosti písmen“
„nepřipadá mi to příjemné“
případně „nepodobné“
„=iLíbí se mi“
případně „=like“ bez ohledu na velikost písmen
„v“
Je rovno libovolnému z položek v „hodnota“, takže pokud je „hodnota“ prázdná,
seznam položek
„nejsou v“
Je nerovno všem položkám z „value“.
„dítě“
je dítětem („potomkem“) „hodnotového“ záznamu (hodnota může být buď
jednotlivý položky nebo seznam položek.

Výpočet bere v úvahu semantiku modelu (tj. sleduje
pole vztahů pojmenované
:attr:`~odoo.models.Model._parent_name`).
„rodič“
je rodičem záznamu „hodnota“ (hodnota může být buď
jednotlivý položky nebo seznam položek.

Výpočet bere v úvahu semantiku modelu (tj. sleduje
pole vztahů pojmenované
:attr:`~odoo.models.Model._parent_name`).
„kdokoli“
shoduje se s jakýmkoliv záznamem vztahového procházení
„název pole“ (:třída:`~odoo.fields.many2one`)
:třída odoo.pole.One2many nebo :třída odoo.pole.Many2many
splňuje hodnotu poskytnutého doménového jména „value“.
„nevšechny“
shoduje, pokud není žádný záznam v procházení vztahu.
„název pole“ (:třída:`~odoo.fields.many2one`)
:třída odoo.pole.One2many nebo :třída odoo.pole.Many2many
splňuje hodnotu poskytnutého doménového jména „value“.

* „hodnota“
proměnného typu a musí být s názvem porovnatelné (pomocí „operátoru“).
pole.

Kritéria domény lze kombinovat pomocí logických operátorů v tvaru *prefix*:

``'&'``
logické operátory AND, výchozí způsob kombinace kritérií za sebou
další. Arita 2 (používá následující 2 kritéria nebo kombinace).
``'|'``
logické *NEBO*, arita 2.
``'!'``
logické NE, arita 1.

....... poznámka:: Většinou k vynechání kombinací kritérií
Obecně se jedná o individuální kritérium s negativním tvarem (např. „==“).
„! =“ a „<“ – „> =“, což je jednodušší než vynechání pozitivního výrazu.

Příklad:

Hledat partnery s příjmením začínajícím na *ABC*, kteří mají telefonní číslo obsahující *7620*:

[(‚název‘, ‚=‘, ‚ABC‘),
['|', ('telefon','ilike','7620'), ('mobil', 'ilike', '7620')]

Hledat prodejní objednávky, které mají alespoň jednu položku s
produkt, který je vyprodaný::

[('fakturační stav', '=' , 'na fakturu')
(‚order_line‘, ‚any‘, [(‚product_id.qty_available‘, ‚<=‘, 0)])]


Hledat všechny partnery narozené v únoru::

[(‚narozeniny.měsíc‘, ‚=‘, 2)]

Odpojit
------

...automethod::Model.unlink

.. odkaz na ORM/záznamy/informace:

Informace o rekordu
-----------------------

...autoatributy::Model.ids

.. atribut:: env

Vrací prostředí uvedeného záznamového setu.

:typ: ~odoo.api.Environment

.. všechno:: Dokumentace prostředí

...automethod:Model.existuje

...automethod:Model.ensure_one

...automethod:Model.get_metadata

..._odkaz/orm/záznamy/operace:

Operace
----------

Záznamové sady jsou neměnné, ale stejný typ setů lze kombinovat pomocí
různé operace sestav, které vrací nová záznamová pole.

... přidání zachová pořadí, ale může dojít k duplicitě

* „rekord v sérii“ se vrátí, zda „rekord“ („musí být 1-prvkový“)
(sada) je v „setu“. „Nenalezený záznam“ je obrácená podmínka.
operace
* „set1 <= set2“ a „set1 < set2“ vrací, zda je „set1“ podmnožinou
z „set2“ (resp. striktní).
* „set1 >= set2“ a „set1 > set2“ vrací, zda je „set1“ množina s přesahem
z „set2“ (resp. striktní).
* „set1 | set2“ vrací sjednocení obou záznamových sad do nové záznamové sady.
obsahující všechny záznamy, které jsou v obou zdrojích
* „set1 & set2“ vrací křížení dvou záznamových sad, nový záznamový soubor.
obsahující pouze záznamy, které jsou v obou zdrojích.
* „set1 – set2“ vrací nový záznamový soubor, který obsahuje pouze záznamy „set1“.
které nejsou v „set2“

Recordsety jsou iterovatelné, takže k dispozici je obvyklá sada nástrojů pro Python.
transformace (:func:`python:map`, :func:`python:sorted`)
Funkce itertools.ifilter() atd., které však vždy buď
Python: seznam nebo Python: iterátor, což znamená, že nemůže
volat metody na jejich výsledky nebo používat operace sestav.

Recordset proto poskytuje následující operace, které vrací samotné Recordsety
Pokud je to možné:)

Filtr
~~~~~~

...automethod:Model.filtrovaný

...automethod::Model.filtrovaný_doménový_účet

Mapa
~~~

..automethod::Model.mapped

.. poznámka::

Od verze 13 podporuje více-vztahové pole přístup jako mapovaný volání:

... kódový blok: Python 3

records.partner_id # == records.map('partner_id')
records.partner_id.bank_ids # == records.mapped('partner_id.bank_ids')
records.partner_id.mapped('jméno') # == records.mapped('partner_id.jméno')

Třídění
~~~~

...automethod:Model.srovnat

Skupinování
~~~~~~~~

...automethod::Model.skupiny

.. odkaz/ORM/dědičnost:

Dědění a rozšíření
=========================

Odoo nabízí tři různé způsoby, jak rozšířit modely v modulárním stylu:

* Vytváření nového modelu na základě stávajícího, přidání nových informací do
kopie, ale ponechání původního modulu v původním stavu
* rozšiřování modelů definovaných v jiných modulech na místě a nahrazování předchozích.
verze
* přidělování některých polí modelu záznamům, které obsahuje

.. obrázek: orm/dědičnost_metody.png


Klasické dědičství
---------------------

Při použití metody :attr:`~odoo.models.Model._inherit`
Když se spojí atributy ~odoo.models.Model._name, Odoo vytvoří nový
model, který využívá stávající (poskytnutý prostřednictvím
:attr:`~odoo.models.Model._inherit`) jako základ. Nový model získává všechny
pole, metody a informace o typu (výchozí hodnoty atd.) ze své základny.

... kódový blok:: python

class Dědění0(models.Model):
_name = 'dědictví.0'
popis = „Nulové dědictví“

jméno = fields.Str()

def call(self):
vraťte se k sobě a zkontrolujte „model 0“

def check(self, s):
return "Toto je záznam číslo {} s názvem {}".format(s, self.name)

třída Dědičnost1(model.Model):
_name = "dědictví.1"
_inherit = "dědění.0"
_popis = „Dědičnost 1“

def call(self):
vrací sebe sama po provedení kontroly „model 1“

a používání:

a = vytvořit objekt z environmentu ['inheritance.0'], kde je uvedeno jméno 'A'.
b = vytvořit objekt (env['inheritance.1']), kde je uvedené jméno B

a.call()
b.call()

Vyplatí se:

„Toto je model 0 záznam A“
„Toto je záznam B z modelu 1“

Druhý model dědí metodu „check“ z prvního modelu a
„název“ pole, ale převedla metodu „volání“, jak tomu bývá u standardních
:ref:`Dědičnost v Pythonu <python:tut-inheritance>“.

Prodloužení
---------

Při použití metody :attr:`~odoo.models.Model._inherit`, ale bez
:attr:`~odoo.models.Model._name`, nový model nahradí stávající.
tj. rozšíření v původním místě. To je užitečné pro přidání nových polí nebo metod
stávající modely (vytvořené v jiných modulech), nebo upravit nebo přizpůsobit
jim (např. změnit jejich výchozí řazení):

class Extension0(models.Model):
_name = 'rozšíření.0'
_description = 'Nula'

jméno = fields.Char(výchozí hodnota je "A")

třída Extension1(models.Model):
dědí z "extension.0"

popis = fields.Text(výchozí hodnota "Prodloužené")

... kódový blok: python3

record = vytvořit objekt s nulovým počtem položek.
record.read()[0]

Výnosy budou::

{'jméno':'A','popis':'Prodloužené'}


.. poznámka::

Také vám poskytne různé automatické pole :ref:`výběru.
pokud nebyly vypnuty.

Delegace
----------

Třetí dědické mechanismus poskytuje větší pružnost (je možné jej upravit)
v průběhu běhu), ale méně síly: použitím metody
model deleguje vyhledání jakéhokoli pole, které není na aktuálním modelu.
„dětské“ modely. Delegace se provádí přes
Pole typu Reference se automaticky nastaví na rodičovské objekty
model.

Hlavní rozdíl je v významu. Při použití delegace má model
místo „je jedna“ má „je jeden“, což mění vztah ve složeném výrazu
místo dědictví::

class Screen(models.Model):
_name = 'delegace.obrazovka'
popis = 'Obrazovka'

velikost = pole.Double(string="Velikost obrazovky v palcích")

class Keyboard(models.Model):
_name = 'delegace.klávesnice'
_description = 'Klávesnice'

layout = fields.Char(string="Layout")

třída Laptop(model.Model):
name = "delegace.notebook"
_description = 'Notebook'

_inherits = {
„Delegace.Obrazovka“: „ScreenId“,
„delegace.klávesnice“: „klávesnicový_identifikátor“,
        }

name = fields.Char(string="Jméno")
výrobce = pole.Char(string="Výrobce")

        # Laptop má displej
screen_id = fields.Many2one('delegace.obrazovka', required=True, ondelete="cascade")
        # Notebook má klávesnici
klávesnice_id = fields.many2one('delegace.klávesnice', required=True, ondelete='cascade')

... kódový blok: python3

record = delegace.laptop.vytvořit({
'screen_id': delegace.obrazovka.vytvořit(velikost = 13.0).id
'klávesnice_id': delegace.klávesnice.vytvořit(layout = 'QWERTY').id
    })
velikost záznamu
record.layout

Výsledkem bude:

    13.0
„QWERTY“

a lze psát přímo na pole přidělené::

record.write({'velikost': 14.0})

.. varování: metody nejsou dědičné při použití delegace dědičnosti.
jen pole

.. varování:

    * Funkce _inherits je v podstatě implementována. Pokud můžete, vyhněte se jí.
    * Připojený operátor _inherits je v podstatě neimplementován, nemůžeme tedy garantovat žádné chování na konečném výstupu.


Inkrementální definice polí
-----------------------------

Pole je definováno jako atribut třídy na modelové třídě. Pokud
je rozšířen, lze také pole definovat znovu
pole stejného jména a typu v podtřídě.
V tom případě jsou atributy pole převzaty z rodičovské třídy.
a převedeny na podtřídy.

Například třetí třída pod sebou přidává pouze nápovědu na pole
„stát“

class First(models.Model):
name = "foo"
stát = pole.Výběr(..., povinné=True)

class Second(models.Model):
dědí z foo
stát = pole.Výběr(pomocná hláška = "Blah blah blah")

.. odkaz/výjimky:

Řízení chyb
================

...automoduly: odoo.exceptions
:členové: AccessDenied, AccessError, CacheMiss, MissingError, RedirectWarning, UserError, ValidationError
