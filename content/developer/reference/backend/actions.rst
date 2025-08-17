=======
Akce
=======

Akce definují chování systému v reakci na akce uživatele: přihlášení.
tlačítko akce, výběr faktury, ...

Akce může být uložena do databáze nebo vrácena přímo jako slovník.
např. metody tlačítek. Všechny akce mají dva povinné atributy:

„typ“
kategorie aktuální operace určuje, které pole mohou být vyplněny.
jak je používána a jaký význam má
„jméno“
krátký uživatelsky čitelný popis akce, který se může zobrazovat v
Klientské rozhraní

Klient může získat akce ve čtyřech formách:

*  „Nedá se věřit“
pokud je otevřená nějaká akční okna, zavřete ji
*  Nit
pokud se shoduje s akcí klienta:ref:`<reference/actions/client>`, interpretovat jako
jinak je považujte za číslo
*  Číslo
číst odpovídající záznam o akci z databáze, může být databáze
identifikátor nebo :term:`externí ID
*  Slovník
považovat za popis klientské akce a provést

.. odkaz/vazby:

Šněrování
========

Kromě dvou povinných atributů mají všechny akce také *volitelné*
atributy používané k prezentaci akce v kontextovém menu libovolného modelu:

„vazební model“
Specifikuje, ke které metodě se akce vztahuje.

....... poznámka: Pro akce serveru použijte „model_id“.

„binding_type“
určuje typ vazby, která je převážně kontextovým menu.
akce se objeví pod

„akce“ (výchozí hodnota)
Specifikuje, že akce se objeví v nabídce :menuselection:`Akce`.
kontextové menu vázaného modelu.
„hlášení“
Specifikuje, že akce se objeví v nabídce :menuselection:`Tisk`.
kontextové menu vázaného modelu.
„vázané typy zobrazení“
oddělené čárkou seznamy typů pohledu, pro které je akce viditelná.
kontextové menu, převážně „seznam“ a / nebo „formulář“. Výchozí hodnota je „seznam,formulář“
(včetně seznamu a formuláře)

.. odkaz/akce/okno:

Okna („ir.actions.act_window“)
==========================================

Nejčastěji používaný typ akce sloužící k prezentaci vizualizací modelu
:doc:`zobrazení <../user_interface/view_records>“: akce okna definuje sadu zobrazení
(a případně konkrétní pohledy) na model (a případně konkrétní záznam).
model).

Jeho obory jsou:

„res_model“
představit názory
„pohledy“
seznamu „(ID zobrazení, typ zobrazení)“. Druhý prvek každé dvojice
je kategorie pohledu (seznam, formulář, graf ...), a první je
volitelný identifikátor databáze (nebo „False“). Pokud není žádný identifikátor poskytnut, klient
by měl vrátit výchozí pohled daného typu pro požadovaný objekt.
model, který se provádí automaticky.
:metoda:meth:`~odoo.models.Model.fields_view_get`) je první typ vlastností,
list je výchozím typem zobrazení a bude otevřený ve výchozím nastavení, když se spustí akce
je provedeno. Každý typ zobrazení by se měl v seznamu objevit maximálně jednou.
„res_id“ (volitelné)
pokud výchozí pohled je „formulář“, určuje záznam, který se má načíst (jinak
mělo být vytvořeno nové rekordní maximum).
„search_view_id“ (volitelné)
„(id, jméno)“ pár, „id“ je identifikátor databáze pro konkrétní
Zobrazit vyhledávání pro akci. Výchozí hodnota je načítání výchozího
vyhledávací pohled na model
„cíl“ (volitelné)
zda by měly být otevřeny v hlavním obsahovém prostoru („aktuální“).
v plném režimu („plná obrazovka“), nebo v dialogu/přesunutí („nový“).
„hlavní“ místo „aktuální“, aby se odstranily chlébové kousky. Výchozí hodnota
„současný“.
„kontext“ (volitelné)
další kontextová data, která se předávají pohledům
„doména“ (volitelně)
filtrování domény, aby se implicitně přidalo k všem vyhledávacím dotazům
„limit“ (volitelné)
Počet záznamů zobrazovaných v seznamech výchozím nastavením. Výchozí hodnota je 80.
webový klient

Například otevřít zákazníky (s partnerem s vlajkou „zákazník“),
listového a formulářového zobrazení:

    {
„typ“: „ir.actions.act_window“,
„res_model“: „res.partner“,
„názory“: [[Falešné, „seznam“], [Falešné, „tvar“]]
„doména“: [[„klient“, „=“, true]]
    }

Anebo otevřít detailní pohled na konkrétní produkt (získaný samostatně).
dialog::

    {
„typ“: „ir.actions.act_window“,
„res_model“: „produkt.produkt“,
„pohledy“: [[False, „formulář“]],
„res_id“: produkt_id
„cíl“: „nový“,
    }

Akce v okně databáze mají několik různých polí, která byste měli ignorovat
klienty, především k použití v seznamu „pohledů“:

„zobrazení“ (výchozí hodnota „seznam, formulář“)
oddělený čárkou seznam typů zobrazení jako řetězec (bez mezer). Všechny tyto typy budou
přítomná v generovaném seznamu „výhledů“ (s alespoň jedním výhledem s hodnotou False pro view_id).
„view_ids“
M2M \ [#nebo m2m]_ pro zobrazení objektů definuje počáteční obsah
„názory“

...... poznámka: Výhledy okna můžete také čistě definovat pomocí „ir.actions.act_window.view“.

Pokud plánujete umožnit více pohledů na svou modelovou strukturu, doporučujeme používat
ir.actions.act_window.view místo akce „view_ids“

... kódový blok::xml

<záznam modelu „ir.actions.act_window.view“ s ID „test_action_tree“>
<pole název="pořadí" hodnota="1"/>
<vlastnost jméno="zobrazení">seznam</vlastnost>
<field name="view_id" ref="view_test_tree"/>
<položka jméno="aktivní okno" odkaz="test_akce"/>


„view_id“
specifický pohled přidán do seznamu „výhledů“, pokud jeho typ je součástí
„list view“ a nebyl již obsazený jedním z pohledů.
„view_id“

Tyto se nejčastěji používají při definování akcí z :ref:`reference/data`:

... blok kódu::xml

<zaznamenání typu "ir.actions.act_window" s ID "test_action">
<pole název="název">Testovací akce</pole>
<položka jméno="res_model">some.model</položka>
<field name="view_mode">graf</field>
<vlastnost jméno="view_id" odkaz="my_specific_view"/>
</záznam>

Použije „můj specifický pohled“ i když není výchozím pohledem.
model.

Složení „views“ na straně serveru je následující:

* získat každý „(ID, typ)“ z „view_ids“ (seřazené podle „pořadí“)
* Pokud je „view_id“ definován a jeho typ není již vyplněn, připojte
„(ID, typ)“
* pro každý nevyplněný typ v „view_mode“ přidejte „(False, typ)“.

.. vše::

    * „užívání“?
    * „skupiny_id“?
    * „filtr“?

...[#nebojdeoM2M] nejedná se o M2M: přidává pole pro sekvence a může být
tvořený pouze jedním typem, bez identifikátoru prohlížeče.

.. odkaz/akce/URL:

Akce URL („ir.actions.act_url“)
====================================

Povolit otevření URL (webové stránky/webové stránky) pomocí akce v Odoo. Lze upravit
Dva polemi:

„URL“
adresa, na kterou se má otevřít při aktivování akce
„cíl“ (výchozí hodnota „nový“)
k dispozici jsou tyto hodnoty:

    * „nový“: otevře URL v novém okně/stránce
    * „Sám sebe“: otevře odkaz v aktuálním okně/stránce (nahradí skutečný obsah).
    * „stáhnout“: přesměruje na stahovací URL


příklad:

::

    {
„typ“: „ir.actions.act_url“,
„url“: „https://odoo.com“,
„cíl“: „sám“,
    }

Toto nahradí stávající část obsahu stránkou hlavní domovské stránky.

.. odkaz/akce/server:

Serverové akce („ir.actions.server“)
======================================

... autoklasifikace: odoo.addons.base.models.ir_actions.IrActionsServer

Povolit spouštění složitého serverového kódu z jakéhokoliv platného umístění akce.
dva pole jsou pro klienta důležitá:

„id“
identifikátor v databázi pro spuštění akce serveru
„kontext“ (volitelné)
kontextová data, která se použijí při spouštění akce serveru

Veškeré záznamy uložené v databázi jsou výrazně bohatší a mohou provádět celou řadu
specifické nebo obecné akce na základě jejich „stavu“. Některé pole (a
chování (tj. chování odpovídající dané situaci) jsou sdíleny mezi státy:

„model_id“
Odoo model spojený s akcí.

„stát“

* „kód“: Spouští Python kód zadaný jako „kód“.

* „Vytvořit objekt“: Vytváří nový záznam modelu „crud_model_id“, který odpovídá specifikacím „fields_lines“.

* „Write object“: Aktualizuje současný záznam podle specifikací „Lines fields“

* „multi“: Spouští několik akcí, které jsou uvedeny v „child_ids“.

Státní pole
------------

Podle stavu je chování definováno různými poli.
Za každým polem je uveden stát, který má zájem o danou věc.

„kód“
Uveďte kus Pythonového kódu, který se má spustit při volání akce



<záznam typu „ir.akce.server“ s ID „tisk_instanci“>
<políčko jméno="název">Partner Server Action</políčko>
<pole název="model_id" odkaz="model_res_partner"/>
<pole název="stát">kód</pole>
<pole jméno="kód">
vytvořit varování (s názvem record.name)
</p>
</záznam>

...... poznámka::

Kódový segment může definovat proměnnou „akce“, která bude
vráceny klientovi jako další akce, kterou je třeba provést:

... kódový blok::xml

<záznam modelu „ir.akce.server“ s ID „tisk_instanci“>
<pole název="název">Partner server akce</pole>
<vlastnost jméno="model_id" odkaz="model_res_partner"/>
<položka jméno="stát">kód</položka>
<pole název="kód">
pokud by platila nějaká podmínka
akce = {
„typ“: „ir.actions.act_window“,
"zobrazovací režim": "formulář"
"res_model": record.název
"res_id": record.id,
                      }
</položka>
</záznam>

Pokud klient splní některé podmínky, bude ho požádat o vyplnění formuláře.
stav

......Tento typ akce je obvykle jediný, který vznikne z datových souborů
<odkaz/údaj>`, ostatní typy než
:ref:`reference/actions/server/multi` jsou jednodušší než Python kód pro definování
z uživatelského rozhraní, ale ne ze souborů dat.

„crud_model_id“ (vytvořit)
model, ve kterém vytváří nový záznam
„link_field_id“ (vytvořit)
mnoho k jednomu „ir.model.fields“, které určuje pole m2o aktuálního záznamu
na které má být nový rekord nastaven (modely by měly odpovídat).

„fields_lines“ (vytvořit/napsat)
pole, která se mají přepsat při vytváření nebo kopírování záznamu.
:třída:~odoo.fields.One2many s poli:

„col1“
„ir.model.fields“ k nastavení v konkrétním modelu
(„crud_model_id“ pro vytváření, „model_id“ pro aktualizace)
„hodnota“
hodnota pole, vyhodnocená pomocí „typ“
„typ“ („hodnota“|„odkaz“|„rovnice“)
Pokud „hodnota“, pak pole „hodnota“ je interpretováno jako literální hodnota
(pokud je převedená), pokud pole „výraz“ obsahuje hodnotu
vyhodnocen jako Python výraz.

„dítě_id“ (více)
Specifikujte vícenásobnou podakci („ir.actions.server“) k provedení v stavu multi.
Pokud samotné podakce vrací akce, poslední
Jeden bude vrácen klientovi jako další akce multi.

.. odkaz/akce/server/kontext:

Kontext hodnocení
------------------

K dispozici je několik klíčů v kontextu hodnocení nebo okolo
serverové akce:

* „model“ je objekt, který je s akcí spojen pomocí „model_id“.
* „rekord“ nebo „rekordy“, které spouštějí akci, mohou být neplatné.
* „env“ prostředí Odoo
* Moduly „datetime“, „dateutil“, „time“ a „timezone“ v jazyce Python
* „log: log(zpráva, úroveň='info')“ funkce pro záznam informací o ladění do tabulky ir.logging
* Konstruktor „Varování“ pro výjimku „Varování“

.. odkaz/akce/zpráva:

Zpráva o akcích („ir.actions.report“)
======================================

Spouští tisk zprávy.

Pokud definujete svůj výkaz pomocí značky <record> místo značky <report>.
chcete, aby se akce zobrazila v nabídce tisk ve výhledu modelu, musíte
musí být také specifikován „binding_model_id“ z odkazu na reference/bindings.
nemusí být nastaven „binding_type“ na „report“, protože
Pokud nechcete, aby se implicitně používalo „ir.actions.report“, můžete si vybrat jinou možnost.


„jméno“ (povinné)
použít jako název souboru, pokud není specifikován parametr „print_report_name“.
V opačném případě je užitečný jen jako mnemotechnická pomůcka pro popis zprávy.
při hledání v nějakém seznamu
„vzor“ (povinný)
základním modelem vašeho hlášení
„report_type“ (výchozí hodnota je „qweb-pdf“)
buď „qweb-pdf“ pro PDF zprávy nebo „qweb-html“ pro HTML
„report_name“ (povinné)
název (interní identifikátor) šablony QWeb použité k zobrazení výstupu
„Tisknout název zprávy“
Pythonový výraz definující název zprávy.
„groups_id“
:třída: `~odoo.fields.Many2many` pole pro skupiny, které mohou vidět/používat
současná zpráva
„multi“
pokud je nastaven na hodnotu „Pravda“, akce se nezobrazí v zobrazení formuláře.
„papírový formát“
:třída: `~odoo.fields.Many2one` pole do formátu papíru, který chcete
použít pro tento výkaz (pokud není uvedeno jinak, bude použit formát společnosti).
„použití připojení“
pokud je nastaven na „Pravda“, tak se zpráva vytvoří pouze jednou poprvé, když
požadovány a následně z archivovaného hlášení znovu vytisknuty.
a každý den se znovu generuje.

Může být použita pro reporty, které musí být vytvořeny jen jednou (například
důvodu)
„připoutanost“
Python výraz, který definuje název zprávy.
přístupná jako proměnná „objekt“

.. odkaz/akce/klient:

Akce klienta („ir.actions.client“)
======================================

Spouští akci, která je implementována výhradně na straně klienta.

„štítek“
identifikátor akce na straně klienta, libovolný řetězec.
klient by měl vědět, jak se v takové situaci zachovat.
„params“ (volitelné)
Pythonovou slovníkovou datovou sadu k zaslání klientovi spolu
značka klientské akce
„cíl“ (volitelné)
zda se má klientské akce zobrazit v hlavním obsahovém prostoru
(„současný“), v plném režimu („plná obrazovka“) nebo ve formě dialogu/připnutí
(„nový“). Použijte „hlavní“ místo „aktuální“, abyste vymazali chléb s křupavým povrchem.
Výchozí hodnota je „aktuální“.

::

    {
„typ“: „ir.actions.client“,
„tag“: „pos.ui“
    }

klientovi nařídí spustit rozhraní prodejního místa, server o tom nemá tušení
Jak funguje rozhraní POS.

.. viz též:
   - :ref:`Návod: Akce klienta <howtos/web/client_actions>`

.. _reference/akce/cron:

Plánované akce („ir.cron“)
===============================

Akce spouštěné automaticky na předem definované frekvence.

„jméno“
Název plánované akce (hlavně pro zobrazení v protokolu)

„interval_number“
Počet jednotek interval_type mezi dvěma provedeními akce

„interval_type“
Jednotka měření časového intervalu („minuty“, „hodiny“, „dny“, „týdny“, „měsíce“)

„model_id“
Model, na který se bude tato akce volat

„kód“
Obsah kódu akce.
Může být prostá volání metody modelu:

.. kódový blok:: python

metoda<metodní_název>().

„nextcall“
Datum a čas dalšího plánovaného provedení této akce

„důležitost“
Priorita akce při provádění více akcí najednou


Pokročilé použití: Batching
----------------------

Při provádění plánované akce je vhodné se pokusit o skupinování postupu.
aby se nezaměstnával jeden pracovník na dlouhou dobu, což by mohlo vést k výjimkám v čase.

Odoo poskytuje jednoduchou API pro zpracování akcí v rámci balíčku.

... kódový blok:: python

self.env['ir.cron']._notify_progress(dokončeno=XX:int, zbývá=XX:int)

Tento způsob umožňuje plánovači zjistit, zda bylo dosaženo pokroku a jestli je
Stále zbývá práce, která musí být hotová.

Výchozí nastavení je takové, že plánovač se pokusí zpracovat 10 balíků najednou.
Pokud zbývají ještě nějaké úkoly po těchto deseti blocích, provede se nová volání cronu
v co nejkratším termínu.

Pokročilé použití: Spouštěče
----------------------

Pro složitější použití nabízí Odoo pokročilejší způsob spouštění.
akce přímo z obchodního kódu.

... kódový blok:: python

action_record._trigger(at=XX:datum)

Bezpečnost
--------

Aby se předešlo spravedlivému využívání zdrojů mezi plánovanými akcemi, některé bezpečnostní opatření zajišťují
správné fungování vašich plánovaných akcí.

- Pokud se při plánované akci třikrát za sebou vyskytne chyba nebo časový limit,
bude považována za neúspěšnou.
- Pokud je plánovaná akce prováděna pětkrát po sobě v rozmezí alespoň
Po sedmi dnech bude zablokována a správce databáze bude o této skutečnosti informován.
