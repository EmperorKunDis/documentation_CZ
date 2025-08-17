
.._odkaz/data:

==========
Datové soubory
==========

Odoo je velmi datově orientovaný a velká část definice modulů tak
definice různých záznamů, které spravuje: UI (nabídky a pohledy)
Bezpečnost (práva přístupu a pravidla záznamů), zprávy a jednoduchá data jsou všechna
definované na základě záznamů.

Struktura
=========

Hlavním způsobem definice dat v Odoo je prostřednictvím XML souborů s daty: široká struktura
XML souboru je následující:

* Každý počet operací v kořenovém prvku „odoo“

... blok kódu::xml


<!-- kořenové prvky datového souboru -->
<odoo>
<operace/>
        ...


Datové soubory jsou prováděny po sobě, operace mohou odkazovat pouze na výsledek
operací, které byly dříve definovány

.. poznámka::

Pokud je očekáváno, že obsah souboru dat bude použit jen jednou,
může specifikovat vlajku „noupdate“ s hodnotou 1. Pokud je součástí
Data v souboru se očekává použít jednou, můžete tento kus umístit
souboru v doméně <data noupdate="1">.

... kódový blok :: XML

<odoo>
<data noupdate="1">

<operace/>
</data>

<!-- (Znovu načteno při instalaci a aktualizaci (odoo-bin -i/-u) -->
<operace/>


Klíčové operace
===============

.. odkaz/datum/záznam:

„rekord“
----------

„rekord“ vhodně definuje nebo aktualizuje databázový záznam.
sledujícími atributy:

„model“
název modelu, který má být vytvořen (nebo aktualizován).
„id“
je vnější identifikátor tohoto záznamu. Je silně
Je doporučeno, aby se jedna

    * umožňuje pozdější definice buďto upravit nebo
odkazovat na tento záznam
    * pro úpravu záznamu, záznam k úpravě
„kontext“
kontext, který se používá při vytváření záznamu
„forcecreate“
v režimu aktualizace, zda se má vytvořit záznam, pokud neexistuje

Požaduje vnější identifikátor, výchozí hodnota je „True“.

„pole“
---------

Každý záznam může obsahovat „tag“ pole, který definuje hodnoty, které se mají nastavit
vytvoření rekordu. Rekord bez pole použije všechna výchozí nastavení
hodnoty vytvářet nebo nic nedělat (aktualizovat).

Atribut „název pole“ je pro pole povinný.
a různé metody, jak definovat hodnotu samotnou:

Nic
pokud není pro pole zadána hodnota, bude implicitně nastaven „False“
na hřišti. Může se použít k vyčištění pole nebo k zabránění použití výchozí hodnoty
pro pole.
„vyhledat“
pro pole vztahů, viz:
pole na modelu objektu.

Zhodnotí doménu, vyhledá vzorec pole pomocí ní a nastaví
výsledky vyhledávání jako hodnotu pole. Využije pouze první výsledek
pole je :class:`~odoo.fields.many2one
„ref“
pokud je uveden atribut „ref“, jeho hodnota musí být platná
:term:`externí ID“, které se vyhledá a nastaví jako hodnotu pole.

Nejčastěji pro :class:`~odoo.fields.Many2one` a
:třída:odoo.pole.Reference
„typ“
pokud je uveden atribut „typ“, používá se k interpretaci a převodu
obsah pole. Obsah pole lze poskytnout prostřednictvím
vnější soubor pomocí atributu „soubor“ nebo prostřednictvím těla uzlu.

K dispozici jsou následující typy:

„xml“, „html“
extrahuje děti pole „field“ jako jediný dokument, vyhodnocuje
libovolné zadané vnější ID s formátem „%(external_id)s“.
„%%“ může být použito k vytvoření skutečných znaků „%“.
„soubor“
zajišťuje, aby obsah pole byl platný cestou k souboru v aktuálním adresáři.
modelu se uloží pár {modul}, {cesta} jako hodnota pole
„char“
nastavuje obsah pole přímo jako hodnotu pole bez
úpravy
„base64“
base64_kóduje obsah pole, užitečné v kombinaci s „file“
*atribut* pro načtení např. obrazových dat do příloh
„int“
Převádí obsah pole na celé číslo a nastavuje jej jako hodnotu pole.
hodnota
„plovoucí“
převádí obsah pole na číslo s plovoucí desetinnou čárkou a nastavuje jej jako hodnotu pole.
hodnota
„seznam“, „tupl“
mělo obsahovat libovolný počet elementů „hodnota“ s tím samým
vlastností jako „pole“, každý prvek se vyhodnocuje jako položka
vytvořený seznam nebo pole a generovaná kolekce je nastavena jako
hodnota pole
„eval“
pro případy, kdy předchozí metody nejsou vhodné, funkce „eval“
atributy jednoduše vyhodnocují jakýkoli Python výraz, který jim je poskytnut.
nastaví výsledek jako hodnotu pole.

Evaluační kontext obsahuje různé moduly („čas“, „datum“ apod.).
„timedelta“, „relativedelta“), funkce pro řešení externích
identifikátory („ref“) a objekt modelu pro aktuální pole, pokud
aplikovatelné („obj“)

„smazat“
----------

Tag „smazat“ může odstranit libovolný počet předem definovaných záznamů.
Má následující vlastnosti:

„model“
model, ve kterém je určitý záznam smazán
„id“
externí ID záznamu, který chcete odstranit
„vyhledat“
:ref:`doménu <reference/orm/domains>`, abyste našli záznamy modelu.
odstranit

„id“ a „hledání“ jsou exkluzivní

„funkce“
------------

Tag „funkce“ volá metodu v modelech s předanými parametry.
Má dvě povinné parametry „model“ a „name“, které určují příslušně
model a název metody, kterou má být volána.

Parametry lze poskytnout pomocí „eval“ (výsledkem by měla být sekvence).
parametrů, které se volají metodou s).
hodnoty)

... blok kódu::xml

<odoo>
<data nenastavit="1">
<záznam id="partner_1" typ="res.partner">
<pole name="jméno">Odude</pole>


<funkce modelu "res.partner" s názvem "send_inscription_notice">
eval="[[ref('partner_1'), ref('partner_2')]]"

<funkce model="res.users" jméno="odeslat upozornění na vstupní lístek VIP">
<funkce hodnota="[[('vip','==',True)]]" typ="res.partner" jméno="hledat"/>
</funkce>
</data>

<zaznamenání id="model_form_view" model="ir.ui.view">
            ...



... ignoroval tvrzení

.._odkaz/údaje/zkratky:

Zkratky
=========

Protože některé důležité strukturální modely Odoo jsou složité a náročné.
Dataové soubory poskytují kratší alternativy definic,
:ref:`záznamová značka <reference/data/record>“

„menuitem“
------------

Definuje záznam „ir.ui.menu“ s řadou výchozích hodnot a zpětných volání:

„rodič“
    * Pokud je nastaven atribut „rodič“, měl by být nastaven jako :term:`externí identifikátor
jiného položky nabídky, která slouží jako nové položce rodič
    * Pokud není zadán žádný „rodič“, pokusí se interpretovat atribut „jméno“.
jako „/“ oddělená sekvence názvů nabídek a najít místo v nabídce
hierarchii. V tomto výkladu jsou automaticky zobrazeny podmenu.
vytvořen
    * Jinak je menu definováno jako „hlavní“ položka nabídky (ne jako nabídka).
bez rodičů
„jméno“
Pokud není uveden atribut „name“, zkusí se zjistit název menu
a případně i další akce, jinak používá ID nahrávky
„skupiny“
„skupiny“ je interpretována jako oddělená čárkou sekvence
:term:`externí identifikátory“ pro modely „res.groups“. Pokud je
:term:`externí identifikátor` je předcházeno znaménkem mínusu („-“).
je odstraněn z skupin v nabídce
„akce“
pokud je uveden, atribut „akce“ by měl být identifikátorem externím.
akce, která se spustí při otevřeném menu
„id“
externí identifikátor položky nabídky

.. odkaz/datum/šablona:

„vzor“
------------

Vytváří QWebový pohled, který vyžaduje pouze „arch“
sekci pohledu a umožňuje několik volitelných atributů:

„id“
vnější identifikátor pohledu
„název“, „dědičný identifikátor“ a „priorita“
Stejně jako odpovídající pole v „ir.ui.view“ (pozn.: „inherit_id“
mělo být :term:`externím identifikátorem`
„primární“
pokud je nastaven na „Pravda“ a kombinován s „inherit_id“, definuje pohled
jako primární
„skupiny“
oddělený čárkou seznam skupin :term:`externích identifikátorů`.
„stránka“
pokud je nastaveno na hodnotu „Pravda“, šablona představuje webovou stránku (propojitelnou).
smazatelná
„volitelné“
„povoleno“ nebo „zakázáno“, zda je možné vypnout pohled (v
(vizuální rozhraní webové stránky) a jeho výchozí stav. Pokud je nevyplněno, vždy
zapnuto.

.._odkaz/údaje/datový soubor CSV:

Soubory dat ve formátu CSV
==============

XMLová data jsou flexibilní a popisná sama o sobě, ale velmi obsáhlá.
vytváření většího množství jednoduchých záznamů stejného typu.

Pro tento případ lze použít také soubory s příponou csv_, což je často uvedeno pro
:ref:`práva přístupu <odkaz na bezpečnostní/ACL práva>“:

* název souboru je:soubor:`{model_name}.csv`
* první řádek obsahuje pole k zápisu a speciální pole „id“.
pro :term:`externí identifikátory“ (používané při vytváření nebo aktualizaci).
* Každá další řada vytváří nový záznam.

Tady jsou první řádky souboru dat definujících státy.
„res.country.state.csv“

...literalinclude::data/res.country.state.csv
:jazyk:text

převést do čitelnějšího formátu:

.. tabulka::
:soubor: data/res.country.state.csv
:hlavičkové řádky: 1
:class: stolní, přehozený, malý

Pro každý řádek (záznam):

* První sloupec je vnější ID záznamu, který má být vytvořen nebo
aktualizace
* druhá sloupec je vnější identifikátor země, který se má propojit.
to (musí být předem definovány objekty země)
* třetí sloupec je pole „název“ pro „stát“.
* Čtvrtá sloupec je pole „kód“ pro „stát“.

..._base64: https://tools.ietf.org/html/rfc3548.html#section-3
... .csv: https://cs.wikipedia.org/wiki/Separátor_oddělených_čárkami
