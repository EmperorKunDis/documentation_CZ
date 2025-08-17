========================
Napište moduly, které lze do systému importovat
========================

.. důležité:
Tento návod předpokládá znalost návodu server_framework_101.
:doc:`definovat modul data“ návod.

Ačkoliv jako vývojáři preferujeme mít k dispozici plnou sílu Pythonu pro psaní našich modulů,
Někdy je to ale nemožné, typicky na řešeních hostingu spravovaném.
umožňuje nasazení vlastního Python kódu, jako například „Odoo.com <https://www.odoo.com/start>“
platforma.

Ovšem pružnost Odoo má umožňovat úpravy z krabice.
Mnoho je možné s aplikací:doc:`Studiem </aplikace/studio>“, lze zde také definovat
modely, pole a logiku v XML souboru dat definovaném v sekci „Data modulu“ v dokumentaci. To zjednodušuje
vyvíjet, udržovat a nasazovat tyto úpravy.

V tomto návodu se naučíme definovat modely, pole a logiku v souborech XML s daty a balíčcích.
Je možné je rozdělit na moduly. Tyto moduly se někdy nazývají „moduly pro import“, nebo „datové moduly“.
Uvidíme také limity této metody vývoje modulů.

Problematika
=================

Stejně jako v návodu :doc:`server_framework_101`, budeme pracovat s konceptem nemovitostí.

Naším cílem je vytvořit novou aplikaci pro správu nemovitostí ve stylu (i když
jednodušší cestou k návodu :doc:`server_framework_101`. Zde budeme definovat modely, pole a
logiku v XML souborech namísto Pythonu.

Na konci této příručky budeme schopni v naší aplikaci dosáhnout následujícího:

- Spravovat nemovitosti, které jsou k prodeji
- Tyto vlastnosti zveřejněte na webu
- Nabídky přijímejte online na webu
- Fakturujte kupujícího až když se nemovitost prodá

Modulová struktura
================

Stejně jako u každého vývojového projektu je jasná struktura snadnější k řízení a údržbě kódu.

Oproti standardním modulům Odoo, které používají oba soubory v jazyce Python i XML, jsou moduly dat pouze ve formátu XML.
Protože se očekává, že váš pracovní strom bude vypadat nějak takhle:

... kódový blok:: bash

majetek
├── actions
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└── models
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└── security
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└── views
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
└── __init__.py
└── __manifest__.py

Vaše jediné Python soubory budou soubory :file:`__init__.py` a :file:`__manifest__.py`.
Soubor __manifest__.py bude stejný jako u jakéhokoli modulu Odoo, ale také jej bude dovážet.
modelů v seznamu „Data“.

Nezapomeňte seřadit soubory v části „Data“ ve :file:`__manifest__.py“ podle závislostí.
obvykle začínají modelem souboru.

Soubor __init__.py je prázdný, ale je potřebný pro to, aby Odoo rozpoznal modul, pokud jej kdykoli
chcete nasadit svůj modul klasickým způsobem (přidáním do cesty adonů). Není to striktně
je nezbytný pro moduly, které budou importovány, ale je dobrým zvykem jej ponechat.

Instalace modulu
====================

Pro nasazení modulu budete potřebovat vytvořit archiv modulu a nahrát jej na svůj
Odoo instanci. Zkontrolujte, zda je na vaší instanci nainstalován modul „base_import_module“.
Pak se přihlaste do části „Aplikace“ -> „Import modulu“ a nahrajte soubor ZIP. Musíte
v režimu vývojáře (viz developer-mode) a zobrazit položku „Import Modul“.

Pokud upravíte modul, budete muset vytvořit nový soubor ZIP a nahrát jej znovu.
Nabídne všechny údaje v modulu. Pozor však na to, že některé operace nejsou možné.
například změnit typ pole, které jste vytvořili dříve.
modul (stejně jako odstraněné pole) se nebude automaticky mazat. Obecně nejjednodušší způsob, jak
je vyřešit tento problém tak, že se začne s čistou databází nebo před nahráním modulu odinstaluje.
novou verzi.

Při nahrávání modulu se zobrazí dvě možnosti:

- „Nutné spuštění“: pokud je vaše modul již nainstalován a znovu jej nahrajete, zkontrolujte to
Tato volba způsobí aktualizaci všech dat označených jako „noupdate=“ v XML souborech.
- „Import ukázkových dat“: je zřejmé, co znamená

Je také možné použít modul pomocí příkazu odoo-bin v konzole.
nástroj s příkazem deploy:

... kódový blok:: bash

$ odoo-bin deploy <cesta_k_modulu> https://<vaše_odoo_instalace> --login <váš_login> --heslo <váš_heslo>

Tato příkazová řádka také přijímá možnost „--force“, která je ekvivalentní k :guilabel:`Nutit inicializaci“
volba v průvodci.

Pozor, uživatel, který používáte k nasazení modulu, musí mít oprávnění „Administrace/Nastavení“.

..cvičení::

   #Vytvořte následující složky a soubory:

      - :file:`/home/$USER/src/tutorials/estate/__init__.py`
      - :file:`/home/$USER/src/tutorials/estate/__manifest__.py`

Soubor __manifest__.py by měl definovat pouze název a závislosti našich balíčků.
moduly. Jediným nutným rámcovým modulem je „base“ (a „base_import_module“ –
Přestože váš modul není vlastně závislý na něm, bez něj nebudete moci
(importujte svůj modul).

   #Vytvořte archiv svého modulu a nahrajte jej do vaší instace Odoo.

Modelové a základní pole
=======================

Jak asi tušíte, definování modelů a polí v XML souborech není tak jednoduché jako v Pythonu.

Jelikož se čte soubor dat postupně, musíte definovat prvky v pořadí odpovídajícím jejich umístění ve skutečném souboru.
Příkladem je to, že musíte definovat model před tím, než budete moci definovat pole na tomto modelu.
musí definovat pole před přidáním do pohledu.

Navíc je XML mnohem složitější než Python.

Začněme definováním jednoduchého modelu, který bude reprezentovat nemovitost v sekci „models“.
adresář našeho modulu.

Odoo modely jsou uloženy v databázi jako záznamy typu „ir.model“. Stejně jako každý jiný záznam mohou být
definované v XML souborech:

... blok kódu::xml



<záznam id="model_realitní nemovitost" model="ir.model">
<pole název="název">nemovitost</pole>
<field name="model">x_estate.property</field>
</záznam>


Poznámka: Všechny modely a pole definované v souborech dat musí být předponěny znakem „x_“; toto je
je povinný a používá se k rozlišení modelů a polí definovaných v souborech Pythonu.

Stejně jako u klasických modelů definovaných v Pythonu, Odoo automaticky přidá několik polí do modelu:

- :attr:`~odoo.fields.Model.id` (:třída:`~odoo.fields.Id`)
Jedinečný identifikátor záznamu modelu.
- :attr:`~odoo.fields.Model.create_date` (:třída:`~odoo.fields.Datetime`)
Datum vzniku záznamu.
- :attr:`~odoo.fields.Model.create_uid` (:třída:`~odoo.fields.Many2one`)
Uživatel, který vytvořil záznam.
- :attr:`~odoo.fields.Model.write_date` (:třída:`~odoo.fields.Datetime`)
Datum poslední úpravy záznamu.
- :attr:`~odoo.fields.Model.write_uid` (:třída:`~odoo.fields.Many2one`)
Uživatel, který naposledy upravil záznam.

Můžeme také přidat několik polí do našeho nového modelu. Přidejme si tedy nějaká jednoduchá pole, jako například jméno (string).
prodejní cena (plovoucí), popis (v HTML), a poštovní směrovací číslo (v znakovém řetězci).

Stejně jako pro modely jsou pole jen záznamy v modelu „ir.model.fields“ a lze je
definované jako takové v datech:

... blok kódu::xml



<!-- ...definice modelu z předchozích řádků... -->
<záznam id="název nemovitosti" typu="ir.model.fields">
<field name="model_id" ref="nemovitost.model_real_estate_property" />
<pole name="jméno">x_jméno</pole>
<políčko name="field_description">Jméno</políčko>
<položka jméno="ttype">char</položka>
<field name="required">true</field>
</záznam>

<položka id="prodejní cena nemovitosti" typu="ir.model.fields">
<field name="model_id" ref="nemovitost.model_real_estate_property" />
<field name="name">x_prodejní cena</field>
<políčko name="field_description">Prodejní cena</políčko>
<field name="ttype">float</field>
<field name="required">true</field>
</záznam>

<záznam id="popis nemovitosti" typu="ir.model.fields">
<field name="model_id" ref="nemovitost.model_real_estate_property" />
<field name="name">x_description</field>
<field name="popis">Popis</field>
<položka name="ttype">html</položka>
</záznam>

<záznam id="pole_nemovitost_ulice" typu="ir.model.fields">
<field name="model_id" ref="nemovitost.model_real_estate_property" />
<pole jméno="název">x_postcode</pole>
<políčko name="field_description">PSČ</políčko>
<položka jméno="ttype">char</položka>
</záznam>


Můžete nastavit různé atributy pro nový prvek. Pro základní prvky patří mezi ně:

- `název pole`: technický název pole (musí začínat znakem „x_“).
- `field_description`: popis pole
- `pomoci`: nápověda k poli zobrazená v rozhraní
- `type`: typ pole (např. `char`, `integer`, `float“, „html“, atd.)
- `povinné pole`: zda je pole povinné nebo ne (výchozí hodnota: „Pravda“)
- `readonly“: zda pole je čtené nebo nikoliv (výchozí hodnota: „False“)
- `index“: zda pole je indexováno nebo ne (výchozí hodnota: „False“)
- kopírovat: zda se pole kopíruje při duplikaci záznamu nebo ne (výchozí hodnota: True
pro ne-relační a ne-vypočítané pole je False, pro relační a vypočítané pole True
- `přeložitelný“: zda pole je přeložitelné nebo ne (výchozí hodnota: „Pravda“)

Příznaky také umožňují kontrolovat filtrování HTML a další pokročilé
vlastnosti; pro kompletní seznam vlastností odkazujte na databázi dostupnou v modelu ir.model.fields
v menu „Nastavení -> Technické -> Databázová struktura -> Položky“ nebo
viz definici modelu v modulu „base“.

..cvičení::

Do tabulky přidejte tyto základní pole:

   ========================= ========================= =======================
pole                      typ                          povinné
   ========================= ========================= =======================
x_datum_dostupnosti      Datum
očekávaná cena              Float                     True
x_ložnic                   Integer
x_životní_plocha           Integer
x_facades                  Integer
garáž x_garage           Logická
x_zahrada                  Logická
x_zahrada                  Integer
x_orientace_zahrady        Výběr
   ========================= ========================= =======================

Pole „orientace zahrady“ musí mít čtyři možné hodnoty: „sever“, „jih“, „východ“.
a „Západ“. Seznam musí být vytvořen tak, že se nejprve vytvoří pole „ir.model.fields“.
rekord pro pole samotné, pak vytvářejí záznamy typu ir.model.fields.selection. Tyto
Záznamy mají tři pole: „ID pole“, „název“ (jméno v uživatelském rozhraní) a „hodnota“ (hodnota
v databázi (pokud je nastaveno pole „sequence“, pak určuje pořadí).
seřazení je zobrazeno v uživatelském rozhraní (sestupně, s nižšími hodnotami na začátku).

Výchozí hodnoty
--------------

V Pythonu lze vlastní výchozí hodnoty nastavit pomocí „default“ parametru pole.
deklaraci. V datových modulech jsou výchozí hodnoty nastaveny vytvořením záznamu „ir.default“.
Pro každý prvek pole lze nastavit výchozí hodnotu. Například je možné
„cena_prodávaného“ pole na „100000“ pro všechny nemovitosti vytvořením následujícího záznamu:

... blok kódu::xml


<!-- ...definice modelu z předchozích řádků... -->
<záznam id="výchozí prodej nemovitosti" model="ir.default">
<field name="cena" vztah="estate.field_real_estate_property_selling_price" />
<field name="json_value">100000</field>
</záznam>


Pro podrobnější informace se obraťte na model „ir.default“ v databázi dostupné na
:menu „Nastavení“ --> „Technické“ --> „Akce“ --> „Vlastní výchozí nastavení“.
viz vzor definice modelu v modulu base.

.. varování:
Tyto výchozí hodnoty jsou statické, ale mohou být nastaveny společností a/nebo uživatelem pomocí „user_id“.
a pole „company_id“ v záznamu „ir.default“. To znamená, že pokud je dynamický
Například nelze nastavit výchozí hodnotu „dnes“ pro pole „datum dostupnosti“.

Bezpečnost
========

Bezpečnost modulů dat je stejná jako u modulů v Pythonu a lze ji najít
v dokumentu „server_framework_101/04_securityintro“.

Podrobnosti najdete v tomto návodu.

..cvičení::

   #Vytvořte soubor ir.model.access.csv v příslušné složce a definujte jej v
souboru __manifest__.py

   #Udělte čtení, zápis, vytváření a odpojení skupině „base.group_user“.

......tip:
Ve výpisu chyb vám dává většinu řešení :-)

Názory
=====

Zobrazení jsou uživatelské rozhraní, které umožňuje interakci s daty.
v souborech XML a nachází se v adresáři views vašeho modulu.

Začínáme s vývojem aplikace v prostředí Django.
Serverového rámce, viz kapitola „server_framework_101/06_basicviews“, se zde nebudeme zabývat podrobněji.

...cvičení: Přidat základní uživatelské rozhraní do modulu estate.

Přidejte základní uživatelské rozhraní do modulu „majetek“, abyste mohli sledovat, vytvářet, upravovat a mazat
Realitní nemovitosti.

   - Vytvořte akci pro model „x_estate.property“.
   - Vytvořte stromový pohled na model „x_estate.property“.
   - Vytvořte pohled na formulář pro model „x_estate.property“.
   - Přidejte pohledy k akci.
   - Přidejte položku do hlavního menu, aby uživatelé mohli přistupovat k akci.

Vztahy
=========

Skutečnou moc systémů s vazbami, jako je Odoo, spočívá ve schopnosti propojit záznamy.
V běžném modulu Pythonu lze definovat nové pole v modelech pro připojení k dalším modelem
v jediné řádce kódu. V datovém modulu je to stále možné, ale vyžaduje o něco víc
práce nohama, protože nemůžeme používat stejnou syntaxi jako v Pythonu.

Jako v :doc:`server_framework_101/07_relations` přidáme několik vztahů do našeho „majetku“.
modul, do kterého přidáme odkazy na:

- kupující nemovitosti
- Makléř, který nemovitost prodal.
- druh nemovitosti: rodinný dům, byt, mezonet, zámek...
- seznam štítků charakterizujících vlastnost: útulné, zrekonstruované…
- seznam přijatých nabídek

Mnoho-na-jedno
-----------

Mnoho-k-jednomu je jednoduchý odkaz na jiný objekt. Například k definování odkazu na
„res.partner“, můžeme definovat novou položku v našem modelu:

... blok kódu::xml

<odoo>
<!-- ...definice modelu z předchozího příkladu... -->

<položka jméno="model_id" odkaz="estate.model_real_estate_property"/>
<políčko jméno="název">x_partner_id</políčko>
<políčko name="field_description">Zákazník</políčko>
<políčko jméno="ttype">many2one</políčko>
<položka jméno="vztah">res.partner</položka>



U polí s více hodnotami lze nastavit několik atributů k podrobnějšímu popisu vztahu:

- `vztah`: název modelu, ke kterému se má vztahovat (povinné pole)
- `ondelete`: akce, která se provede při smazání záznamu (výchozí hodnota: „setnull“).
- `doména`: filtr domény, který se má aplikovat na vztah

..cvičení::

   #Vytvořte nový typ „x_estate.property.type“ s následujícími poli:

      ========================= ========================= =======================
pole                      typ                          povinné
      ========================= ========================= =======================
'jméno'                    Char                      True
      ========================= ========================= =======================

   #Přidejte akci, zobrazení seznamu a položku nabídky pro model „x_estate.property.type“.

   #Přidejte práva přístupu k modelu „x_estate.property.type“ pro uživatele.

   #Vytvořte následující pole v modelu „x_estate.property“:

      ========================= ====================================== =======================
pole                      typ                                          povinné
      ========================= ====================================== =======================
'x_property_type_id'        Many2One ('x_estate.property.type') True
`x_partner_id` (kupující)  One2many (`res.partner`)
`x_user_id` (prodejce) Many2one (`res.users`)
      ========================= ====================================== =======================

   #Zahrňte nové pole do formuláře vlastností objektu „x_estate.property“.

Mnoho-na-mnoho
------------

Mnoho-k-mnoha je vztah k seznamu objektů. V našem příkladu definujeme mnoho-k-mnoho
vztah k novému modelu „vlastnost.tag“. Tento tag představuje vlastnost
například: zrenovovaný, útulný apod.

Každá nemovitost může mít mnoho štítků, jeden štítek může být přiřazen k mnoha nemovitostem.
typický mnoho-na-mnoho vztah.

Poly-na-poly pole jsou definována stejně jako poly-na-jedno pole, ale s ttype
na hodnotu many2many. Atribut relation je také nastaven na název modelu
k ní odkazovat. Další atributy lze nastavit pro kontrolu vztahu:

- `relation_table`: název tabulky, která se má použít pro vztah
- „sloupec1“ a „sloupec2“: názvy sloupců, které se mají použít pro vztah

Tyto atributy jsou nepovinné a měly by být obvykle specifikovány pouze tehdy, pokud
Jsou to pole mnoho-k-mnoho mezi dvěma modely, aby se předešlo konfliktu. Většinou
ORM Odoo bude schopna určit správnou tabulku a sloupce vztahů k použití.

..cvičení::

   #Vytvořte nový model „x_estate.property.tag“ s následujícími poli:

      ========================= ========================== =======================
pole                      typ                          povinné
      ========================= ========================== =======================
'jméno'                    Char                      True
      ========================= ========================== =======================

   #Přidejte akci, seznam a položku nabídky pro model „x_estate.property.tag“.

   #Přidejte práva přístupu k modelu „x_estate.property.tag“ pro umožnění přístupu uživatelům.

   #Vytvořte následující pole v modelu „x_estate.property“:

      ========================= ======================================
pole                      typ
      ========================= ======================================
`x_vlastnický_pozemkový_číselník`  Many2many (`x_majetek.vlastnické_pozemky`)
      ========================= ======================================

   #Přidejte nový prvek do formuláře vzoru modelu „x_estate.property“.

Jeden k mnoha
-----------

Jedna-k-mnoha je vztah k seznamu objektů. V našem příkladě definujeme jednu-k-mnoho
vztah k novému „x_estate.property.offer“ modelu, který představuje nabídku
vytvořený zákazníkem za účelem koupě nemovitosti.

Jedno pole na mnoho je definováno stejně jako mnoho polí na jedno, ale s ttype
na hodnotu one2many. Atribut relation je také nastaven na název modelu
k ní odkazovat. Další vlastnost musí být nastavena pro kontrolu vztahu:

- `vztahovací pole`: název pole na vztahovaném modelu, které obsahuje
odkaz na základní model (políčko s mnoha hodnotami k jedné hodnotě). Tento odkaz slouží ke spojení obou modelů
spolu.

..cvičení::

   #Vytvořte nový model „x_estate.property.offer“ s následujícími poli:

      ========================= ================================== ============ ===================
pole                      typ                                  povinné   hodnoty
      ========================= ================================== ============ ===================
'cena'                    Float                               True
'x_status'                  Výběr                                                   Přijaté, Odmítnuté
'x_partner_id'             Many2One ('res.partner')          True
'x_property_id'            Many2One ('x_estate.property')    True
      ========================= ================================== ============ ===================

   #Přidejte práva přístupu k modelu „x_estate.property.offer“ pro uživatele.

   #Vytvořte stromový pohled a formulář s poli cena, partner_id a status.
|Není nutné vytvářet akci nebo nabídku.

   #Přidejte pole „x_offer_ids“ do vašeho modelu „x_estate.property“ a v jeho formuláři.

Spočítané a příbuzné pole
===========================

Pole vypočítaná v aplikaci
---------------

Výpočetní pole jsou základním konceptem v Odoo a slouží k definování polí, která se počítají.
na základě jiných polí. Toto je užitečné pro pole, která jsou odvozena z jiných polí, jako například
součet podúdajů (sčítání ceny všech položek v objednávce na prodej).

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/fields/compute`.

Moduly dat mohou definovat pole libovolného typu, ale jsou omezené ve srovnání s Pythonem.
modulů. Ve skutečnosti jsou moduly dat určeny k nasazení na systémy, které neumožňují libovolné
kód, který může být spuštěn, je velmi omezený.

.. poznámka::
Všechny programy v Pythonu, které jsou napsané pro moduly dat, se spouští v bezpečném prostředí,
operace, které lze provést. Například nemůžete do projektu přidávat knihovny, nemůžete
nemůžete přistupovat k žádným souborům operačního systému a dokonce ani tisknout na konzoli. Některé nástroje jsou poskytovány,
ale tento fakt se liší podle typu sandboxového prostředí, které je použito.

V případě metod pro výpočet je pískoviště velmi omezené a poskytuje pouze nejnutnější věci.
služeb pro provedení kódu. Kromě vlastností Pythonu obsahuje také
mít přístup k modulům datetime, dateutil a time (např. pro pomoc s datem)
výpočty)

Dále je třeba poznamenat, že při spuštění v sandboxu je „přidělování teček“ zakázáno, takže nemůžete psát
„vlastnost.celková plocha = 1“ v metodě „vypočítat“. Musíte použít přístup k položce:
„property[‚x_total_area‘] = 1“. Dotovou notací pro přístup k poli funguje normálně:
„property.x_garden_area“ vrátí hodnotu pole „x_garden_area“.


Dříve jsme definovali dva „oblast“ pole na našem modelech „x_estate.property“: „living_area“.
a „zahrada“. Chcete-li definovat pole vzorce na modelech, které vrátí součet obou
oblasti můžeme do datového modulu přidat následující kód:

... blok kódu::xml

<odoo>
<!-- ...definice modelu z předchozího příkladu... -->
<záznam id="pole_celková_plocha_nemovitosti" typu="ir.model.fields">
<položka jméno="model_id" odkaz="estate.model_real_estate_property"/>
<pole název="název">x_total_area</pole>
<políčko name="field_description">Celková plocha</políčko>
<položka jméno="ttype">float</položka>
<položka jméno="závisí">x_obytná plocha, x_zahrada</položka>
<pole název="počítač"> <![CDATA[
pro vlastnost sebe sama:
vlastnost['celková plocha'] = vlastnost.plocha bytu + vlastnost.zahrada
            ]]>
</položka>



.. poznámka::
Ve serverových akcích se v cyklu opakovaně používá proměnná records. V případě pole vypočítaného na základě jiných polí se použije
opakujete na proměnné self, která obsahuje pole, ve kterém je pole vypočítáno.

Atribut „závisí“ se používá k definování polí, na která se počítané pole vztahuje.
Atribut „compute“ se používá k definování kódu, který se provádí pro výpočet pole (pomocí
Python kód).

Oproti tomu v Python modulech jsou pole počítaná výchozími hodnotami uložena automaticky. Pokud chcete počítané pole
nebude uložena (například kvůli výkonu nebo kvůli zabránění „roztažení“ databáze), můžete nastavit „store“
připisovat hodnotu „false“. To samé platí pro „readonly“: pokud chcete, aby vaše vypočítaná pole nebyla
editovatelné, musíte nastavit atribut „readonly“ na hodnotu „True“.

Sekce CDATA se používá k označení obsahu jako řetězce, nikoli XML.
Tím se zabrání tomu, aby parsovatel zkoušel interpretovat Pythonový kód jako XML nebo přidávat
přebytečný prostor a podobně při instalaci modulu do databáze.

..cvičení::

   #Přidejte do modelu „x_estate.property“ vypočítaný sloupec, který vrací součet
„x_obytná_plocha“ a „x_zahrada“ pole, jak je vidět výše.
   #Zahrňte pole do formuláře v zobrazení modelu „x_estate.property“.

.. poznámka::
Na rozdíl od modulů v Pythonu není možné definovat zpětnou nebo vyhledávací metodu.
vypočítané pole.

Související obory
--------------

Související pole jsou zjednodušenou verzí vypočítaných polí, která odráží hodnotu jiného pole.
pomocí vztahu mnoho-jedna.

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`odkaz/pole/související“.

Související pole mohou být libovolného typu (typ pole na druhé straně vztahu
přechod (traversal). Jsou definovány tak, jako by se pole přidávalo přímo do modelu s
přidání atributu „související“, který určuje cílovou položku na souvisejícím modelu.
, která obsahuje hodnotu, kterou se má zrcadlit.

Příkladem je například přímý přístup k zemi kupujícího přímo ze
„x_estate.property“ modelu můžeme do našeho datového modulu přidat následující kód:

... blok kódu::xml

<odoo>
<!-- ...definice modelu z předchozího příkladu... -->
<rekord id="pole nemovitost země" typu="ir.model.fields">
<položka jméno="model_id" odkaz="estate.model_real_estate_property"/>
<políčko jméno="název">x_country_id</políčko>
<políčko name="field_description">Země kupujícího</políčko>
<políčko jméno="ttype">many2one</políčko>
<pole název="vztah">res.country</pole>
<field name="související">x_partner_id.země_id</field>



Atribut „related“ se používá k určení cílového pole na modelu, který je s aktuálním modelem spojen.
obsahuje hodnotu, která má být zrcadlena. Tato musí být seznam polí oddělených tečkou.

Kód a logika podnikání
=======================

Akce serveru
--------------

V modulu Pythonu můžete definovat jakýkoliv metodický postup na vašem modelech. Jedním z běžných způsobů použití je
je přidat metody „akce“ do vašeho modelu, a poté je vázat na tlačítka uživatelského rozhraní.
(např. potvrdit citaci, vystavit fakturu atd.)

Ten samý efekt lze v datovém modulu dosáhnout definicí
:ref:`Akce serveru <reference/actions/server>“ vázané na váš model. Akce serveru reprezentují
logické části, které se spouštějí dynamicky na serveru. Tyto akce lze nastavit ručně
v databázi přímo přes
V nabídce „Nastavení“ – „Technické“ – „Akce“ – „Serverové akce“.
typy; v našem případě použijeme typ „kód“, který nám umožní spustit jakýkoliv kód Pythonu.
sandboxové prostředí.

Toto prostředí obsahuje několik nástrojů, které vám pomohou interagovat s databází Odoo:

- „env“: prostředí záznamu
- „Model“: vzorový záznam
- „uživatel“ a „uid“: aktuální uživatel a jejich identifikační číslo
- „datetime“, „dateutil“, „timezone“ a „time“: knihovny, které pomáhají s datem a časem
počítání
- „float_compare“: funkce pro porovnání dvou hodnot s přesností dané
- „b64encode“ a „b64decode“: funkce pro kódování a dekódování hodnot v základě 64
- „Kommando“: třída, která pomáhá při vytváření složitých výrazů a příkazů (viz „Kommando“
třída v :ref:`referenci ORM <reference/fields/relational>

Dále máte přístup k záznamovému souboru, ve kterém je akce prováděna (obvykle pouze jeden
Záznamy provedené z pohledu formulářů a více záznamů provedených z pohledu objektů.
výpisu) prostřednictvím proměnných „záznam“ a „záznamy“.

.. poznámka::
Pokud vaše akce musí vrátit akci klientovi (například přesměrovat uživatele na
jiný pohled (tj. přiřadíte ji proměnné „akce“ ve vašem serveru).
kód akce. Sandbox kódu zkontroluje proměnné definované ve vašem kódu po jeho spuštění.
Výkonnost a automaticky vrátí ji, pokud detekuje přítomnost proměnné „akce“.

Pokud je nainstalován modul „webová stránka“, bude v kontejneru kódu dostupný objekt „žádost“.
a můžete přiřadit objekt „odpověď“ proměnné „odpověď“, abyste vrátili odpověď.
klientovi v podobném duchu, což je podrobněji popsáno v
:ref:`návody/importovatelné moduly/webové kontroly`.

Příklad: můžeme definovat akci na modelu „x_estate.property“, která nastaví hodnotu „x_status“
všechny své nabídky „odmítla“:

... blok kódu::xml

<záznam id="akce_x_vlastnictví_odmítnout_veškeré nabídky" typu="ir.actions.server">
<políčko name="jméno">Odmítnout všechny nabídky</políčko>
<položka jméno="model_id" odkaz="estate.model_real_estate_property"/>
<položka jméno="stát">kód</položka>
<field name="code"> <![CDATA[
pro nemovitost v evidenci:
vlastnost.x_nabídky.napsat ({"x_status": "odmítnuté"})
]]></field>
</záznam>

Tuto akci lze zahrnout jako tlačítko do formuláře vzoru modelu „x_estate.property“ takto:
přidat následující uzel „tlačítko“:ref:`<reference/view_architectures/form/button>“ do hlavičky našeho
formulářový pohled:

... blok kódu::xml

<!-- definice formuláře z vašeho kódu ... -->
<hlavička>

</hlavička>

Je také možné přidat vstup do ikonky ozubeného kola (:icon:`fa-gear`):
vyhněte se přidávání tlačítek na pohledy, které jsou již přeplněné. Chcete-li tak učinit, můžete své akce vázat
modelu a konkrétním typům pohledů:

... blok kódu::xml

<záznam id="akce_x_vlastnictví_odmítnout_veškeré nabídky" typu="ir.actions.server">
<políčko name="jméno">Odmítnout všechny nabídky</políčko>
<položka jméno="model_id" odkaz="estate.model_real_estate_property"/>
<položka jméno="stát">kód</položka>
<vlastnost jméno="vazba_model_id" odkaz="nemovitost.model_reality"/>
<položka název="způsob zobrazení typu vazby">strom, formulář</položka>
<field name="code"> <![CDATA[
pro nemovitost v evidenci:
vlastnost.x_nabídky.napsat ({"x_status": "odmítnuté"})
]]></field>
</záznam>

Tím se akce stane dostupnou v ikoně „Nástroje“ (:icon:`fa-gear`) u „x_estate.property“.
v seznamu (když je vybraná jedna nebo více záznamů pomocí zaškrtávacího políčka), v zobrazení pohledu a v zobrazení formulářů.

..cvičení::

   #Přidejte akci serveru do modelu „x_estate.property.offer“, která nastaví hodnotu „x_status“.
pole nabídky na „Přijato“ a aktualizuje prodejní cenu a kupujícího nemovitosti
k níž je nabídka připojena podle toho, co vyplývá z této akce. Tato akce by měla označit i všechny ostatní nabídky
na stejném pozemku jako „Odmítnutí“.
   #Zahrnout tlačítko v seznamu nabídek, které umožňuje provést tuto akci.

.. obrázek:importovatelné moduly/tlačítko přijetí nabídky.png
:align: center

Přebírání modelů Pythonu
------------------------

Ve vlastnostech uživatelského rozhraní
~~~~~~~~~~~~~~~

Oproti tomu v Python modulech nelze metodu Pythonového modelu čistě převzít.

Je však možné (v některých případech) nahradit prvky uživatelského rozhraní, které volají
Tyto metody a získat přístup k těmto metodám v akci serveru.

Typickým příkladem je integrace s aplikací „Prodej“ v Odoo. Představme si, že vaše
Modul nemovitostí je integrován s aplikací prodej tak, že když se prodá určité zboží
(např. nabídku na správu prodeje nemovitosti) chcete automaticky vytvořit novou nemovitost
zaznamenat do svého modulu.

Aby se vám to podařilo, budete potřebovat:

- Vytvořit akci serveru, která volá původní metodu tlačítka, a přidat vlastní logiku před
nebo po této metodě
- nahradit tlačítko v pohledu vlastním tlačítkem, které volá akci na serveru

... blok kódu::xml

<zaznamenání id="přidat objednávku prodeje" typu="ir.ui.view">
<pole název="jméno">prodej.objednávka.formulář.dědictví</pole>
<field name="model">objednávka</field>
<vlastnost jméno="dědictví_id" odkaz="prodej.zobrazit_objednávku_formulář" />
<položka jméno="arch" typ="xml">
<xpath expr="//button[@name='action_confirm'][@type='object']/@attributes">
<attribut name="typ">akce</attribut>
<atribut name="název">majetek.akce_x_majetek_vytvořit_z_prodejního_objednávky</atribut>
</xpath>
<!-- protože tlačítko je v původním pohledu dvakrát, musíme ho nahradit dvakrát -->
<xpath expr="//button[@name='action_confirm'][@type='object']/@attributes">
<attribut name="typ">akce</attribut>
<atribut name="název">majetek.akce_x_majetek_vytvořit_z_prodejního_objednávky</atribut>
</xpath>
</p>
</záznam>


<textField name="jmeno">Potvrdit a vytvořit vlastnost z prodejního příkazu</textField>
<field name="model_id" ref="objednavka.model_sales_order"/>
<položka jméno="stát">kód</položka>
<field name="code"> <![CDATA[
pro každý řádek v záznamu:
objednávka.potvrdit()
typ_nemovitosti = env['x_estate.property.type'].sudo().search([('x_name', '=', 'Další')], limit=1)
property = env['x_estate.property'].sudo().create(
'x_name': objednávka.název,
'očekávaná cena': 0
„prodejní cena“: 0,
'x_sale_order_id': objednávka.id
'x_property_type_id': property_type.id
        })
]]></field>
</záznam>

Pomocí automatických pravidel
~~~~~~~~~~~~~~~~~~~~

Automatické pravidlo je způsob, jak automaticky provádět akce na záznamy v databázi podle
specifické spouštěče, jako například změna stavu, přidání štítku atd. Mohou být užitečné při vázání chování
životní cyklus záznamů například zasláním e-mailu při přijetí nabídky.

Použití automatizačních pravidel pro rozšíření standardního chování může být robustnější než uživatelsky definované
přístup, protože bude fungovat i v případě, že se životní cyklus spustí jiným způsobem než přes
tlačítko (např. prostřednictvím webhooku nebo přímým voláním metody; například při citaci
Přes portál nebo e-shop. Jsou ale o něco náročnější na nastavení
správně, protože je nutné zajistit, aby automatizace běžela pouze v správný okamžik.
např. nastavit konkrétní pole pro sledování apod.

**Dokumentace**: kompletnější dokumentace k tomuto tématu naleznete v
:/aplikace/studio/automatizované-akce/.

.. poznámka::
Automatické pravidla nejsou součástí modulu „Základní“; přicházejí s modulem „Základní automatizace“.
modul; pokud tedy definujete automatizační pravidla ve vašem datovém modulu, musíte se ujistit, že
„base_automation“ je součástí vašich modulů.

Jednou nainstalované, automatické pravidla se spravují v
:menu:`Nastavení --> Technické --> Automatizace --> Automatizační pravidla“

Automatické pravidlo je zvláště užitečné při propojení datového modulu s již existujícím standardem Odoo.
modul. Dataové moduly nemohou metody přehrávat, protože automatizace je vázaná na změny životního cyklu
standardních modelů je běžným způsobem, jak rozšířit standardní moduly.

Pokud bychom naši předchozí ukázku přepsali pomocí automatizačních pravidel, změnilo by se
by bylo potřeba:

- akce serveru by už neměla volat původní metodu tlačítka (místo toho by měla volat původní
metoda vyvolá změnu, která spustí automatizační pravidlo).
- přídavná část není potřeba
- musíme definovat automatizační pravidlo, které spustí akci serveru na příslušném události.

... blok kódu::xml


<field name="název">Vytvořit vlastnost z prodejního příkazu</field>
<field name="model_id" ref="objednavka.model_sales_order"/>
<položka jméno="stát">kód</položka>
<field name="code"> <![CDATA[
pro každý řádek v záznamu:
typ_nemovitosti = env['x_estate.property.type'].sudo().search([('x_name', '=', 'Další')], limit=1)
property = env['x_estate.property'].sudo().create(
'x_name': objednávka.název,
'očekávaná cena': 0
„prodejní cena“: 0,
'x_sale_order_id': objednávka.id
'x_property_type_id': property_type.id
        })
]]></field>
</záznam>


<field name="název">Vytvořit vlastnost z prodejního příkazu</field>
<field name="model_id" ref="objednavka.model_sales_order"/>
<položka jméno="spouštěč">on_state_set</položka>
<pole název="trg_selection_field_id" odkaz="sale.selection__sale_order__state__sale"/>


</záznam>

Poznámka: ID XML vlastností (viz. :ref:`XML ID <tutorials/define_module_data/xml_id>`) pro standardní modely a pole Odoo
hodnoty výběru a další informace lze najít přímo v instanci Odoo kliknutím na odpovídající
v technických nabídkách a pomocí položky „Zobrazit metadatové informace“ v nabídce pro ladění. ID XML
pro modely jsou prostě jenom názvy modelů s tečkami nahrazenými podtržítky a předponou „model_“.
(např. „sale.model_sale_order“ je „sale.order“, jak je definováno v modulu „sale“); ID XML pro
pole je název modelu s tečkami nahrazenými podtržítky a předponou „field_“, tedy název modelu.
název a název pole (např. „sale.field_sale_order__name“ je identifikátor XML pro pole „název“
modelu „prodej.objednávka“, který je definován v modulu „Prodej“.

... /tutoriály/importovatelné moduly/webové kontroly:

Webmaster
-------------------

HTTP kontroly v Odoo jsou obvykle definovány v adresáři souborů :file:`controllers` modulu.
V modulu dat lze definovat serverové akce, které chovají jako kontroler, pokud
Modul webové stránky je nainstalován.

Při instalaci modulu webu mohou být akce serveru označeny jako „K dispozici na webu“.
a dána cesta (plná cesta je vždy předponována /webové stránky/akce/, aby se předešlo kolizím URL).
globální objekt požadavku je k dispozici v místním rozsahu kódu serverového postupu.

Objekt „žádost“ poskytuje několik metod, které umožňují přístup k tělu žádosti:

- `request.get_http_params()`: extrahovat klíčová slova a hodnoty z dotazovacího řetězce a formulářů
je přítomna v těle (oboje „application/x-www-form-urlencoded“ a „multipart/form-data“).
- `request.get_json_data()`: extrahovat JSON data z těla požadavku.

Protože nelze z vnitřku akce serveru vrátit hodnotu, je nutné definovat odpověď
můžete se vrátit tak, že přiřadíte objekt reakce proměnné „odpověď“, který bude
se vrátil na webové stránky automaticky.

Tady je příklad jednoduchého webového ovladače, který vrátí seznam vlastností.
když je načtena adresa URL /webová stránka/akce/nemovitost/:

... blok kódu::xml

<záznam id="server_akce_seznam_nemovitostí" model="ir.actions.server">
<pole název="název">Kontrolor seznamu majetku</pole>

<field name="web_zveřejněn">true</field>
<pole název="webová cesta">nemovitost</pole>
<položka jméno="stát">kód</položka>
<field name="code"> <![CDATA[
html = 'html = "<html><body><h1>Vlastnosti</h1><ul>'
for vlastnictví v požadavku.env['x_estate.property'].search([]):
html += f'<li>{vlastnost.x_name}</li>'
html += '</ul></body></html>'
odpověď = požadavek.vytvořit_odpověď(html)
]]></field>
</záznam>

Pro usnadnění generování je v objektu request k dispozici několik užitečných metod.
objekt odpovědi:

- „request.render(šablona, qcontext=None, lazy=True, **kw)“ k vykreslení šablony QWeb pomocí
xmlid; navíc předáváme další klíčová slova parametrům objektu werkzeug.Response (např. pro nastavení
cookies, hlavičky atd.
- „request.redirect(location, code=303, local=True)“ k přesměrování na jinou adresu URL; „local“
argument slouží k určení, zda se přesměrování má vztahovat na web nebo ne
(výchozí hodnota je True).
- „request.notfound()“ vrátit výjimku „werkzeug.HTTPException“ k oznámení chyby 404.
webové stránky.
- „request.make_response(data, hlavičky = None, cookies = None, stav = 200)“ k ručnímu vytvoření
Objekt Werkzeug.Response; argument status je kód stavu HTTP, který se má vrátit (výchozí hodnota:
  200).
- „request.make_json_response(data, headers=None, cookies=None, status=200)“ k ručnímu vytvoření
JSONový odpověď; data budou zformátována pomocí utilitky `json.dumps`; tato funkce může být užitečná
aby umožnila server-server komunikaci prostřednictvím volání API.

Pro podrobnosti o implementaci nebo jiných (méně častých) metodách se obraťte na objekt Request.
v modulu odoo.http.

Pozor, že bezpečnostní obavy jsou ponechány na vývojáři (obvykle prostřednictvím pravidel nebo
Používáním příkazu „sudo“ k přístupu do záznamů.

.. poznámka::
Model, který je použit v poli akce serveru s názvem „model_id“, musí být veřejně přístupný.
uživatel pro provedení zápisu, jinak se tato akce serveru nebude spouštět.
vrátí chybovou hodnotu 403. Způsob, jak přístup odepřít, je spojit akci serveru s modelem
to je již veřejně přístupné, typickým příkladem je například odkazování na
akci serveru na model „ir.filtry“.

..cvičení::

Přidejte do modulu JSON API, aby externí služby mohly získat seznam vlastností
na prodej.

   #Přidat nový pole „x_api_published“ do modelu, který kontroluje, zda jsou vlastnosti
zveřejněné na API nebo ne
   #Přidejte záznam o přístupovém právu, který umožní veřejným uživatelům číst a psát do modelu.
   #. zabránit jakémukoli zápisu ze strany veřejného uživatele přidáním pravidla pro zápisovou operaci
s nemožným doménovým jménem (např. [('id', '==', False)])
   #Přidejte pravidlo záznamu, aby vlastnosti označené jako „x_api_published“ mohly být čteny.
veřejný uživatel
   #... přidat akci serveru, která vrátí seznam vlastností ve formátu JSON při zadání URL
/webová stránka/akce/nemovitost

Nádech JavaScriptu
========================

Přenositelné moduly nemohou obsahovat soubory v jazyce Python, ale pro JavaScript existuje žádný takový omezení.
soubory. Přidání skriptů do vašeho modulu, který je možné importovat, je stejné jako přidání
standardní modul v Odoo.

To znamená, že do importovatelného modulu lze přidat nové komponenty pole nebo i zcela nové pohledy.

Jako příklad přidáme do modulu „Estate“ jednoduchou „prohlídku“. Prohlídky jsou běžnou součástí
Odoo vás dříve učil používat aplikaci, aby se noví uživatelé mohli snadno zorientovat.

Velmi malá trasa s jediným krokem lze přidat vložením souboru do složky „static/src/js/tour.js“:

... kódový blok::js

import { registry } z "@web/jádro/registry";


registry.kategorie("web_tour.tours").přidat('soukromé prohlídky', {
url: "/web",
kroky: () => [
spouštěč: '.o_app[data-menu-xmlid="estate.menu_root"]',
obsah: „Začněte prodávat své nemovitosti prostřednictvím této aplikace!“
        }],
    });

Poté je nutné soubor zahrnout do příslušného balíčku v seznamu manifestů:

.. kódový blok:: py

    {
„název“: „Realitní kancelář“,
        # [...]
„aktiva“:
„web.assets_backend“: [
„/estate/static/js/tour.js“,
            ],
        },
    }

Potřebujete také přidat záznam XML v novém souboru estate_tour.xml ve složce data, aby váš
Tur je zobrazena:

... blok kódu::xml

<záznam id="prohlídka sídla" typu="web_tour.tour">
<pole název="jméno">soukromá prohlídka s průvodcem</pole>
<položka jméno="pořadí">2</položka>
<text field="rainbow_man_message">Vítejte, přeji vám příjemné objevování.“</text>
</záznam>

.. poznámka::
Oproti běžným modulům Pythonu se v importovatelných modulech nepodporuje globální expanze.
Proto musíte uvést každý soubor, který chcete zahrnout do modulu, zvlášť.
