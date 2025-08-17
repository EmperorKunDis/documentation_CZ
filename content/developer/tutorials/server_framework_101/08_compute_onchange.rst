========================================
Kapitola 8: Vypočítané pole a změny
========================================

Vztahy mezi modely jsou klíčovou součástí
jakýkoliv modul Odoo. Jsou nezbytné pro modelování jakéhokoliv podnikatelského případu. Nicméně můžeme chtít
vazby mezi poli v rámci daného modelu. Někdy je hodnota pole určena z
hodnoty jiných polí a časů chceme pomoci uživateli při zadávání dat.

Tyto případy jsou podporovány koncepty vypočítaných polí a onchanges. I když tento kapitol je
Technicky složitá není, ale semantika obou pojmů je velmi důležitá.
Také poprvé napíšeme logiku v Pythonu. Dosud jsme nic nenaprogramovali
kromě definic tříd a deklarací polí.

Výpočetní pole
===============

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/fields/compute`.

.. poznámka::

**Úkol**: na konci této části:

    - Ve vlastnickém modelu se vypočítává celková plocha a nejlepší nabídka.

.. obrázek:: 08_compute_onchange/compute.gif
:align: střed
:alt: Výpočet polí

    - V nabídce nemovitostí by měl být vypočítán datum platnosti a může být aktualizován:

.. obrázek: 08_vypočítat_na_změnu/vypočítat_inverzní.gif
:align: střed
:alt: Výpočetní pole s převrácenou orientací

V našem realitním modulu jsme definovali obytnou plochu i zahradu. Pak
přirozené definovat celkovou plochu jako součet obou polí. Budeme používat pojem počítaný
tj. hodnota daného pole bude počítána z hodnoty jiných polí.

Dosud byly pole ukládána přímo do a získávána přímo ze
databáze. Hodnoty polí mohou být také vypočítány. V takovém případě má pole hodnotu
vytažené z databáze, ale počítané na lince pomocí metody
model.

Pro vytvoření pole s počítanou hodnotou vytvořte pole a nastavte jeho atribut
:attr:`~odoo.fields.Field.compute` na název metody.
Metoda by měla nastavit hodnotu pole, které bylo vypočítáno pro každý záznam.
„sám“.

Podle konvence jsou metody :attr:`~odoo.fields.Field.compute` soukromé, což znamená, že nemohou být
může být volán pouze z vrstvy obchodu (viz
:ref:`návody/serverová-architektura-101/01_architektura“). Soukromé metody mají jméno začínající
podtrhnout „_“

Závislosti
------------

Hodnota pole vypočteného v poli obvykle závisí na hodnotách ostatních polí.
vypočítaný záznam. ORM očekává, že vývojář specifikuje tyto závislosti
na metodu počítání s dekorátorem :func:`~odoo.api.depends`.
Uvedené vazby využívá ORM k spouštění znovupočítání.
pole, pokud některé z jeho závislostí byly změněny:

od odoo importujeme moduly api, fields a models

class TestComputed(models.Model):
name="test.computed"

celkem = pole.Float(výpočet="_vypočítat_celkem")
částka = fields.float

@api.depends('cena')
def _vypočítat_celkové(self):
pro rekord v sobě:
record.celkem = 2.0 * record.množství

.. poznámka: „self“ je kolekce.
:kategorie:aphorismus

Objekt „self“ je tzv. záznamovým souborem, tedy uspořádanou sbírkou
záznamů. Podporuje standardní operace Pythonu na kolekcích, například
„len(sebe)“ a „iter(sebe)“, kromě dalších operací sestav jako „recs1 |
rec2´´.

Procházením „sám sebe“ získáme jednotlivé záznamy, kde každý záznam je
sám o sobě kolekcí velikosti 1. Můžete přistupovat k polím jednotlivých objektů.
záznamy pomocí znaménkové notace, např. „záznam.název“.

Mnoho příkladů vypočítaných polí lze nalézt v Odoo.
„Zde <https://github.com/odoo/odoo/blob/713dd3777ca0ce9d121d5162a3d63de3237509f4/addons/account/models/account_move.py#L3420-L3423>“
Je to jednoduché.

..cvičení: Vypočítejte celkovou plochu.

    - Přidejte pole „celková plocha“ do „majetku“. Je definováno jako součet
„obytná plocha“ a „zahrada“.

    - Přidej pole do formuláře tak, jak je zobrazeno na první obrázku v sekci **Cíl**.

Pro pole vztahů je možné používat cesty skrze pole jako závislosti:

popis = pole.Char(vypočítat = "_vypočítat_popis")
partner_id = fields.many2one('res.partner')

@api.depends('partner_id.name')
def _vypočítat_popis(self):
pro rekord v sobě:
record.description = „Test pro partnera %s“ % record.partner_id.name

Příklad je uveden s poli :class:`~odoo.fields.Many2one`, ale platí pro
:třída odoo.fields.Many2many nebo třída odoo.fields.One2many. Příklad najdete
„tady <https://github.com/odoo/odoo/blob/713dd3777ca0ce9d121d5162a3d63de3237509f4/addons/account/models/account_reconcile_model.py#L248-L251>“.

Zkusíme to v našem modulu s následujícím cvičením!

...cvičení: Vypočítejte nejlepší nabídku.

    - Přidejte pole „best_price“ do „estate.property“. Je definováno jako nejvyšší (tedy maximální) z
nabídky „cena“.

    - Přidej pole do pohledu formuláře tak, jak je znázorněno na první obrázku v sekci **Úkol**.

Tip: možná budete chtít vyzkoušet metodu `~odoo.models.BaseModel.mapped`. Podívejte se
`tady <https://github.com/odoo/odoo/blob/f011c9aacf3a3010c436d4e4f408cd9ae265de1b/addons/account/models/account_payment.py#L686>`__
například.

Inverzní funkce
----------------

Můžete si všimnout, že pole vypočítaná v poli jsou ve výchozím nastavení čtená pouze. To je očekávané, protože
uživatel není povinen hodnotu nastavit.

V některých případech může být užitečné stále moci nastavit hodnotu přímo. V našem příkladu s nemovitostmi
Můžeme definovat platnost nabídky a datum platnosti. Rádi bychom
buď dobu nebo datum, přičemž jeden z nich ovlivňuje druhý.

Pro podporu této funkce poskytuje Odoo možnost použití „obrácené“ funkce:

od odoo importujeme moduly api, fields a models

class TestComputed(models.Model):
name="test.computed"

celkem = pole.FloatingPoint(výpočet="_vypočítat_celkově", inverzní="_inverzní_celkem")
částka = fields.float

@api.depends('cena')
def _vypočítat_celkové(self):
pro rekord v sobě:
record.celkem = 2.0 * record.množství

def __inverzní_součet(self):
pro rekord v sobě:
record.množství = record.celkem / 2.0

Příkladem může být
„tady <https://github.com/odoo/odoo/blob/2ccf0bd0dcb2e232ee894f07f24fdc26c51835f7/addons/crm/models/crm_lead.py#L308-L317>“.

Metoda vypočítání nastaví pole, zatímco metoda inverze nastaví pole.
závislosti.

Poznámka: metoda „inverzní“ je volána při ukládání záznamu, zatímco
Metoda „vypočítat“ je volána při každé změně jejích závislostí.

...cvičení: Vypočítejte platnost nabídky.

    - Přidejte následující pole do modelu „nabídka nemovitosti“:

    ========================= ========================= =========================
pole                    typ                        výchozí
    ========================= ========================= =========================
validita                   Integer               7
datum_termín            Datum
    ========================= ========================= =========================

Kde „date_deadline“ je vypočítaný prvek, který je definován jako součet dvou polí.
nabídku: „create_date“ a „validity“. Definujte vhodné obrácené funkce
Protože uživatel může nastavit buď datum, nebo platnost.

Tip: pole „create_date“ se vyplní pouze při vytváření záznamu, protože je vyplněno jen při jeho vytvoření.
musí mít záložní řešení, které zabrání pádu při vytváření.

    - Přidejte pole do zobrazení formuláře a seznamu, jak je znázorněno na druhém obrázku v části **Úkoly**.

Doplňující informace
----------------------

Kalkulované pole se v databázi neukládají automaticky. Proto je také **nepovinné
Možné vyhledávat v poli počítaném, pokud není definována metoda „vyhledávání“. Toto téma je mimo rámec
tohoto tréninku, tak se mu nebudeme věnovat. Příklad najdete
„tady <https://github.com/odoo/odoo/blob/f011c9aacf3a3010c436d4e4f408cd9ae265de1b/addons/event/models/event_event.py#L188>“.

Další možností je uložit pole s atributem „store=True“.
obvykle pohodlné, ale pozor na potenciální nárůst výpočetní zátěže přidávaný do vašeho modelu. Používejme znovu
Příklad:

popis = pole.Char("_compute_description", True)
partner_id = fields.many2one('res.partner')

@api.depends('partner_id.name')
def _vypočítat_popis(self):
pro rekord v sobě:
record.description = „Test pro partnera %s“ % record.partner_id.name

Každé změně názvu partnera je automaticky přepočítána „popis“.
Všechny záznamy, které se k němu vztahují! To může být velmi nákladné na znovu vypočítání.
Miliony záznamů potřebují znovu vypočítat.

Další věc, kterou je třeba zmínit, je, že pole vypočítané vlastnosti může záviset na jiném poli vypočítané vlastnosti.
chytřejší, aby správně vypočítal všechny závislosti v požadovaném pořadí... ale někdy
náklady na zhoršený výkon.

Ve většině případů je třeba při definování pole počítaného typu brát v potaz výkon. Čím více
komplexní pole je vaše pole pro výpočet (např. s mnoha závislostmi nebo když vypočítané pole
závisí na počtu vypočítaných polí), čím více polí bude vypočítáno, tím déle se výpočet protáhne. Vždy si proto nechte dostatek času
hodnotit náklady na vypočítané pole předem. Většinou se tak děje jen v případě, že váš kód
Dostane se na produkční server, který zjistíte, že zpomaluje celý proces. Nechladí :-(

Na změny
=========

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:func:`~odoo.api.onchange`:

.. poznámka::

**Cíl**: na konci této části by mělo být zahradničení povoleno s výchozím rozsahem 10.
orientace na sever.

.. obrázek:: 08_compute_onchange/onchange.gif
:align: střed
:alt: Načtení

V našem modulu nemovitostí chceme také pomoci uživateli s vkládáním dat. Když například
pole je nastaveno, chceme dát výchozí hodnotu pro plochu zahrady i orientaci.
Dále chceme, aby se pole „zahrada“ vrátilo na nulu a aby se zahradní plocha sčítala.
orientace odebrat. V tomto případě hodnota daného pole mění hodnotu
jiných oborech.

Mechanismus „onchange“ poskytuje způsob, jakým lze aktualizovat uživatelské rozhraní.
formulář bez uložení do databáze, pokud uživatel vyplní
hodnota pole. K tomu definujeme metodu, kde „self“ představuje
zaznamenat záznam do formuláře a ozdobit jej funkcí :func:`~odoo.api.onchange`.
určit, která pole je spouští.
„self“ bude zobrazeno na formuláři:

od odoo importujeme moduly api, fields a models

class TestOnchange(models.Model):
name="test.onchange"

jméno = pole.Char(string="Jméno")
popis = pole.Char(string="Popis")
partner_id = fields.many2one('res.partner', string='Partner')

@api.onchange('partner_id')
def __onchange_partner_id(self):
self.name = „Dokument pro %s“ % (self.partner_id.name)
self.popis = "Popis pro %s" % (self.partner_id.jméno)

V tomto příkladu se změna partnera promítne také do názvu a popisu hodnoty.
uživatel, zda chce později změnit jméno a popis hodnoty. Dále je třeba mít na paměti, že
smyčka na „self“, protože metoda je spouštěna pouze v formuláři, kde „self“ je vždy
jediný záznam.

..cvičení: Nastavte hodnoty pro zahradu a orientaci.

Vytvořte v modelu „estate.property“ metodu „onchange“, abyste mohli nastavit hodnoty pro
plocha zahrady (10) a orientace (sever) při nastavení zahrady na hodnotu True. V opačném případě pole vymažte.

Doplňující informace
----------------------

Metoda OnChanges může také vrátit neblokovanou výstrahu.
(`příklad <https://github.com/odoo/odoo/blob/cd9af815ba591935cda367d33a1d090f248dd18d/addons/payment_authorize/models/payment.py#L34-L36>`).

Jak je používat?
================

Pro používání vypočítaných polí a události OnChange neexistuje žádné striktní pravidlo.

V mnoha případech můžete použít obě pole k dosažení stejného výsledku. Vždy
doporučuje využívat počítané pole, protože se spouští i mimo kontext formuláře.
používat onchange k přidání logiky do vašeho modelu. To je velmi špatná myšlenka, protože
Při vytváření záznamu programově se změny nevyvolávají automaticky, ale
V podobě zobrazení formuláře.

Obvyklou pastí vypočítaných polí a události OnChange je pokusit se být „příliš chytrý“ tím, že přidáte příliš mnoho
logiky, což může vést k opačnému výsledku, než byl očekáván: uživatel je zmatený z
Všechna automatizace.

Předdefinovaná pole jsou snadněji laditelná: takové pole je nastaveno metodou, takže je snadné
sledovat nastavení hodnoty. Naopak události OnChanges mohou být matoucí: je velmi obtížné
znát rozsah metody onchange. Protože několik metod onchange může nastavit stejná pole,
snadno se stává obtížným sledovat, odkud pochází hodnota.

Při používání uložených počítaných polí se soustřeďte na závislosti. U počítaných polí
závisí na ostatních vypočítaných polích, změna hodnoty může spustit velké množství znovu počítání.
To vede k špatným výkonům.

V následujícím oddílu :doc:`<09_actions>` se dozvíme, jak spustit některé
logiku podnikání při kliknutí na tlačítka.
