==================================
Kapitola 3: Modelové a základní pole
==================================

Na konci předchozí kapitoly jsme se dozvěděli, že
vytvořit modul v Odoo. V tuto chvíli je však stále prázdná skořápka, která nám neumožňuje
ukládat jakékoliv data. V našem modulu nemovitostí chceme ukládat informace týkající se
vlastnosti (jméno, popis, cena, obytná plocha...), které jsou uloženy v databázi. Rámec Odoo poskytuje
nástroje usnadňující interakci s databází.

Před pokračováním v cvičení se ujistěte, že je nainstalovaný modul „majetek“, tedy
musí se zobrazit jako „Nainstalováno“ v seznamu aplikací.

.. varování:

Nepoužívejte globální proměnné, které lze měnit.

Jedna instance Odoo může běžet několik databází současně v rámci jednoho procesu Pythonu.
Distribuované moduly mohou být nainstalovány na každém z těchto databází, a proto nelze spoléhat
globální proměnné, které by se měnily podle nainstalovaných modulů.

Objektově relační mapování
=========================

**Poznámka k překladu**: dokumentace týkající se této problematiky je uvedena v
:ref:`reference/orm/model` API.

.. poznámka::

**Cíl**: Na konci této části by měla být vytvořena tabulka „estate_property“:

... kódový blok :: text

$ psql -d rd-demo
rd-demo=SELECT COUNT(*) FROM estate_property;
počet
        -------
            0


Zásadní součástí Odoo je vrstva ORM.
Tato vrstva umožňuje, aby se většina příkazů SQL psala ručně.
a poskytuje rozšiřitelnost a zabezpečení služeb.

Objekty obchodní logiky jsou deklarovány jako třídy Pythonu, které dědí
Třída Model, která je integruje do automatizovaného
systém odolnosti.

Model lze nakonfigurovat nastavením atributů v jeho
definice, nejdůležitějším atributem je
atribut ~odoo.models.Model._name, který je povinný a definuje jméno pro
model v systému Odoo. Zde je minimální definice
model:

od odoo importujeme modely

class TestModel(models.Model):
name="test_model"

Tato definice je dostatečná pro generování databáze s tabulkou nazvanou test_model.
všechny modely jsou uloženy v adresáři models a každý model je definován samostatně.
Pythonový soubor.

Podívejte se na definici tabulky „crm_recurring_plan“ a na odpovídající Python
soubor se importuje:

1. Model je definován v souboru „crm/models/crm_recurring_plan.py“.
(viz zde <https://github.com/odoo/odoo/blob/e80911aaead031e7523173789e946ac1fd27c7dc/addons/crm/models/crm_recurring_plan.py#L1-L9>).
2. Soubor „crm_recurring_plan.py“ je importován do souboru „crm/models/__init__.py“.
(viz „tady <https://github.com/odoo/odoo/blob/e80911aaead031e7523173789e946ac1fd27c7dc/addons/crm/models/__init__.py#L15>“).
3. Soubor „models“ je importován v souboru „crm/__init__.py“.
(viz zde <https://github.com/odoo/odoo/blob/e80911aaead031e7523173789e946ac1fd27c7dc/addons/crm/__init__.py#L5>).

... cvičení:Definovat model nemovitostí.

Na základě příkladu v modulu CRM vytvořte potřebné soubory a složky pro
„soubor nemovitostí“.

Když se soubory vytváří, přidejte minimální definici pro
„model majetku“.

Každá změna souborů v Pythonu vyžaduje restartování serveru Odoo.
serveru přidáme parametry „-d“ a „-u“:

.. kódový blok: konzole

$ ./odoo-bin --addons-path=addons,../enterprise/,../tutorials/ -d rd-demo -u estate

„-u estate“ znamená, že chceme upgradovat modul „estate“, tedy ORM
přidat novou tabulku do databáze. V tomto případě vytvoří novou tabulku.
že aktualizace by měla být provedena na databázi „rd-demo“. Příkaz „-u“ by měl být vždy použit
kombinace s „-d“.

Během startu byste měli vidět následující varování:

... blok kódu:: text

    ...
UPOZORNĚNÍ rd-demo odoo.models: Model nemovitosti nemá vlastnost popis
    ...
UPOZORNĚNÍ rd-demo odoo.modules.loading: Model nemovitosti nemá žádné přístupová pravidla, zvažte jejich přidání ...
    ...

Pokud tomu tak je, pak byste měli být v pořádku. Pro jistotu si ověřte s „psql“, jak je ukázáno níže
**Sen**.

.. cvičení: Přidejte popis.

Přidejte do svého modelu „_description“ a vyřešte jednu z výstrah.

Modelová pole
============

**Poznámka k překladu**: dokumentace týkající se této problematiky je uvedena v
:ref:`reference/orm/fields` API.

Pole definují, co může model uchovávat a kde jsou data uložena.
definované jako atributy v modelovém třídě:

od odoo importujeme pole a modely

class TestModel(models.Model):
name="test_model"
_description = „Test Model“

jméno = fields.Str()

V poli „název“ je použito pole :class:`~odoo.fields.Char`, které bude reprezentováno jako Python
unicode „str“ a SQL „VARCHAR“.

Typy
-----

.. poznámka::

**Úkol**: Na konci této sekce by měly být v tabulce přidány některé základní pole
„majetkové vlastnictví“

... kódový blok :: text

$ psql -d rd-demo

rd-demo = #\d;

Sloupec     |           Typ          | Srovnávání | Nulovost | Výchozí hodnota
        --------------------+-----------------------------+-----------+----------+---------------------------------------------
id                |číslo               |           | není povinné |nextval('soubor_nemovitostí_id_seq'::regclass)
create_uid        | celé číslo                |           |          |
create_date         | datum bez časového pásma |           |          |
write_uid          | celé číslo                |           |          |
write_date        | čas bez časového pásma |           |          |
jméno                  | charakteristická varianta   |           |          |
popis             |  text                       |           |          |
poštovní směrovací číslo | charakteristika | délka | datový typ
dostupnost datumem | datum                       |           |          |
očekávaná cena      | dvojnásobný přesný typ       |           |          |
prodejní cena     |  dvojnásobná přesnost       |           |          |
ložnice            | celé číslo             |           |          |
obytná plocha       | celé číslo                |           |          |
fasády            | celé číslo                |           |          |
garáž              |  logická hodnota           |           |          |
zahrada            |  logická hodnota           |           |          |
plocha zahrady      | celé číslo                  |           |          |
orientace zahrady | charakterové pole            |           |          |
Indexy:
„estate_property_pkey“ primární klíč, B-strom (id)
Zahraniční klíčové omezení:
"majetek_vlastnictví_create_uid_fkey" FOREIGN KEY (create_uid) REFERENCES res_users(id) ON DELETE SET NULL
„estate_property_write_uid_fkey“ FOREIGN KEY (write_uid) REFERENCES res_users(id) ON DELETE SET NULL


Existují dvě široké kategorie polí: „jednoduchá“ pole, která jsou atomická
hodnoty uložené přímo v tabulce modelu a „vztahové“ pole, která spojují
záznamy (stejného nebo jiného modelu).

Jednoduché příklady pole jsou :class:`~odoo.fields.Boolean`, :class:`~odoo.fields.Float`,
:třída odoo.fields.Char, třída odoo.fields.Text, třída odoo.fields.Date
a třída:~odoo.fields.Selection

... cvičení: Přidejte základní pole do tabulky nemovitosti.

Přidejte do tabulky následující základní pole:

    ========================= =========================
pole                      typ
    ========================= =========================
jméno                    Char
popis                   Text
poštovní směrovací číslo   Char
datum dostupnosti          Datum
očekávaná cena             Float
prodejní cena              Float
ložnice                    Integer
obytná plocha              Integer
fasády                    Integer
garáž                     logická
zahrada                   logická
plocha zahrady            Integer
orientace zahrady          výběr
    ========================= =========================

Pole „orientace“ musí mít čtyři možné hodnoty: „sever“, „jih“, „východ“
a „Západ“. Seznam je definován jako seznam dvojic, viz
`tady <https://github.com/odoo/odoo/blob/b0e0035b585f976e912e97e7f95f66b525bc8e43/addons/crm/report/crm_activity_report.py#L31-L34>`__
například.

Při přidání polí do modelu je nutné restartovat server s příkazem „-u estate“.

.. kódový blok: konzole

$ ./odoo-bin --addons-path=addons,../enterprise/,../tutorials/ -d rd-demo -u estate

Připojte se k „psql“ a zkontrolujte strukturu tabulky „estate_property“. Zjistíte, že
Přidali jsme také několik dalších políček do tabulky, na které se vrátíme později.

Společné atributy
-----------------

.. poznámka::

**Úkol**: Po dokončení této části by měly sloupce „název“ a „očekávaná cena“
v tabulce „majetek“ není omezeno na NULL:



rd-demo = #\d;

Sloupec     |           Typ          | Srovnávání | Nulovost | Výchozí hodnota
        --------------------+-----------------------------+-----------+----------+---------------------------------------------
        ...
jméno              | textová hodnota           |           | není povinné
        ...
očekávaná cena    | dvojnásobný přesný typ      |           | není povinné
        ...

Stejně jako samotný model lze pole konfigurovat pomocí
konfigurační atributy jako parametry:

name = fields.Char(povinné=True)

Některé atributy jsou dostupné na všech polích, zde je uvádíme ty nejčastější:

:attr:`~odoo.fields.Field.string` („str“, výchozí hodnota: název pole)
Název pole v uživatelském rozhraní (viditelný pro uživatele).
:attr:`~odoo.fields.Field.required` (`bool`, výchozí hodnota: False)
Pokud je „true“, pole nemůže být prázdné. Musí buď mít výchozí hodnotu, nebo
musí mít hodnotu nebo musí být při vytváření záznamu vždy nastavena.
:attr:`~odoo.fields.Field.help` (`str`, výchozí hodnota: `''`)
Poskytuje dlouhé nápovědy pro uživatele v rozhraní.
:attr:`~odoo.fields.Field.index` („bool“, výchozí hodnota: „False“)
Žádost, aby Odoo vytvořilo „index“ na sloupci.

..cvičení:Nastavit atributy pro existující pole.

Přidejte následující atributy:

    ========================= =========================
pole                      atribut
    ========================= =========================
název                     povinné
očekávaná cena          požadovaná
    ========================= =========================

Po obnovení serveru by měly být obě pole neprázdná.

Automatické pole
----------------

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/pole/automatické“.

Možná jste si všimli, že vaše modely mají několik polí, která jste nikdy nedefinovali.
Odoo vytváří několik polí ve všech modelech. Tyto pole jsou
spravované systémem a nelze je napsat, ale lze je číst.
užitečné nebo nezbytné:

:attr:`~odoo.fields.Model.id` (:třída:`~odoo.fields.Id`)
Jedinečné označení záznamu modelu.
:attr:`~odoo.fields.Model.create_date` (:třída:`~odoo.fields.Datetime`)
Datum vzniku záznamu.
:attr:`~odoo.fields.Model.create_uid` (:třída:`~odoo.fields.Many2one`)
Uživatel, který vytvořil záznam.
:attr:`~odoo.fields.Model.write_date` (:třída:`~odoo.fields.Datetime`)
Datum poslední úpravy záznamu.
:attr:`~odoo.fields.Model.write_uid` (:třída:`~odoo.fields.Many2one`)
Uživatel, který naposledy upravil záznam.


Nyní, když máme první vytvořený model, můžeme
Přidejte nějakou bezpečnost <04_securityintro>!


..[#auto_fields] lze deaktivovat automatické vytváření některých
pole <odkaz/pole/automatické/log_access>
...[#rawsql] psaní přímo do SQL dotazů je možné, ale vyžaduje opatrnost, protože
přebíhá všechna odoo autentizační a bezpečnostní opatření.

..._index databáze:
    https://use-the-index-luke.com/sql/preface
.._ORM:
    https://en.wikipedia.org/wiki/Object-relational_mapping
.._SQL:
    https://en.wikipedia.org/wiki/SQL
