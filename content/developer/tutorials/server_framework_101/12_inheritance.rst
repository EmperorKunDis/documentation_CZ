=======================
Díl 12: Dědictví
=======================

Odoo je velmi silný v tom, že se skládá z modulů. Modul je zaměřen na konkrétní obchodní potřebu, ale
Moduly mohou mezi sebou komunikovat, což je užitečné pro rozšíření funkcí stávajícího
modul. Například v našem scénáři s nemovitostmi chceme zobrazovat seznam nemovitostí prodávajícího
přímým vstupem do běžného uživatelského rozhraní.

Ale než se podíváme na konkrétní dědění modulů v Odoo, podívejme se, jak můžeme upravit
chování metod Create, Retrieve, Update a Delete.

Dědičnost v Pythonu
==================

.. poznámka::

**Úkol**: na konci této části:

    - Nebylo by možné smazat vlastnost, která není nová nebo zrušená.

.. obrázek: 12_dědičnost/odpojit.gif
:align: střed
:alt:Odpojit

    - Když je vytvořen návrh, stav nemovitosti by se měl změnit na „Předložený návrh“.
    - Nemělo by být možné vytvořit nabídku s nižší cenou než je stávající nabídka

.... obrázek: 12_dědičnost/vytvorit.gif
:align: střed
:alt: Vytvořit

V našem modulu nemovitostí jsme nikdy nic specifického nevyvíjeli, abychom mohli
standardní operace CRUD. Odoo poskytuje potřebné
nástroje k tomu. Ve skutečnosti už takové akce jsou součástí našeho modelu díky klasické
Dědičnost v Pythonu

od odoo importujeme pole a modely

class TestModel(models.Model):
name="test_model"
_description = „Test Model“

        ...

Naše třída „TestModel“ dědí od třídy „~odoo.models.Model“, která poskytuje
:metoda: ~odoo.model.Model.create, metoda: ~odoo.model.Model.read, metoda: ~odoo.model.Model.write
a metoda:meth:`~odoo.models.Model.unlink`.

Tyto metody (a jakákoliv jiná definovaná na třídě Model) lze rozšířit o
specifická obchodní logika:

od odoo importujeme pole a modely

class TestModel(models.Model):
name="test_model"
_description = „Test Model“

        ...

@ApiModel
def __init__(self, vals):
            # Zkus nějakou logiku, změň hodnoty...
            ...
            # Poté zavolejte metodu super, aby byla spuštěna metoda rodičovská.
return super().create(válců)

Konstruktor dekorátoru funkce:~odoo.api.model je nutný pro metodu:~odoo.models.Model.create
metoda proto, že obsah objektu Recordset „sám“ není v kontextu vytváření relevantní.
Není však nutné pro ostatní metody CRUD.

Důležité je také poznamenat, že i když můžeme přesměrovat přímo
Metoda ~odoo.models.Model.unlink je většinou nežádoucí, protože
dekorátor:metoda func:~odoo.api.ondelete. Metody označené tímto deklarátorem budou
volá se během metody ~odoo.models.Model.unlink a vyhýbá se některým problémům, které mohou nastat při
odinstalováním modulu modelu, když je přímo překrýváno metoda :meth:`~odoo.models.Model.unlink`.

V Pythonu 3 je „super()“ ekvivalentní „super(TestModel, self)“. Druhá varianta může být nutná
Když potřebujete volat metodu rodiče s upraveným záznamem.

.. nebezpečí::

    - Je velmi důležité vždy volat metodu super(), aby se zabránilo narušení proudu.
jenom v několika velmi specifických případech, kdy nechcete volat.
    - Vždy se ujistěte, že vracená data jsou konzistentní s metodou rodičovským způsobem. Například
metoda rodiče vrací „dict()“, vaše přepracování musí také vrátit „dict()“.

... cvičení: Přidat logiku do metod pro vytváření, čtení, aktualizaci a mazání.

    - Zamezte smazání vlastnosti, pokud není ve stavu „New“ nebo „Cancelled“.

Tip: vytvořte novou metodu s dekorátorem :func:`~odoo.api.ondelete` a pamatujte, že
„self“ může být záznamová sada se více než jedním záznamem.

    - Při vytváření nabídky nastavte stav nemovitosti na „Nabídka přijata“. Také vygenerujte chybu, pokud uživatel
se pokouší vytvořit nabídku s nižším množstvím než existující nabídka.

Tip: pole „property_id“ je k dispozici v proměnné „vals“, ale je to „int“.
instancovat objekt „estate.property“, použijte „self.env[model_name].browse(value)“
(`příklad <https://github.com/odoo/odoo/blob/136e4f66cd5cafe7df450514937c7218c7216c93/addons/gamification/models/badge.py#L57>`__)

Model dědičnosti
=================

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/orm/dědičnost`.

V našem modulu nemovitostí bychom rádi zobrazili seznam nemovitostí spojených s makléřem
přímou volbou v Nastavení / Uživatelé a společnosti / Zákazníci ve formuláři Zobrazení.
model „res.users“ a přizpůsobit jeho pohled na zobrazení.

Odoo nabízí dvě mechanismu pro dědění, které umožňují rozšíření stávajícího modelu v modulární podobě.

První dědění umožňuje modulům upravit chování modelu definovaného v
další modul od:

- přidáním polí do modelu.
- překrývání definice polí v modelu
- přidáním omezení do modelu.
- přidáním metod do modelu.
- přebírat existující metody v modelu.

Druhý dědický mechanismus (delegace) umožňuje každému záznamu modelu být propojen
dokumentace rodičovského modelu a poskytuje průhledný přístup k
polí tohoto rodičovského záznamu.

.. obrázek: 12_dědictví/metody-dědění.png

:alt: Metody dědičnosti

V Odoo je první mechanismus zcela jasně nejvíce používaný. V našem případě chceme přidat pole do
existující model, tedy budeme používat první mechanismus. Například:

od odoo importujeme pole a modely

třída Dědičný model (modelů.Model):
_inherit = "dědičný model"

nový_položka = pole.Char(string="New Field")

Praktický příklad, kdy jsou do dvou polí přidány
Model najdeme
„tady <https://github.com/odoo/odoo/blob/60e9410e9aa3be4a9db50f6f7534ba31fea3bc29/addons/account_fleet/models/account_move.py#L39-L47>“.

Podle konvence je každý zděděný model definován v samostatném souboru Pythonu. V našem příkladu by to bylo
„models/inherited_model.py“.

...cvičení:Přidejte pole do uživatelů.

    - Přidejte pole do „res.users“:

    ===================== ================================================================
pole             typ
    ===================== ================================================================
property_ids           Jedno2množství v opačném směru od pole, které odkazuje na prodejce.
„majetek, nemovitost“
    ===================== ================================================================

    - Přidejte doménu do pole, aby se zobrazily pouze dostupné vlastnosti.

V dalším kroku přidáme pole do výpisu a zkontrolujeme, že vše funguje tak, jak má.

Zobrazit dědictví
================

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/zobrazit záznamy/dědičnost`.

.. poznámka::

**Úkol**: Na konci této sekce bude seznam dostupných vlastností propojených
zobrazit se v uživatelském formuláři prodejce

.. obrázek: 12_dědičnost/user.png
:align: střed
:alt:Uživatelé

Odoo místo toho modifikuje stávající pohledy na místě (přepíše je).
poskytuje vlastnost dědičnosti, kdy se na vrcholu „rozšířených“ pohledů zobrazují dětské pohledy.
kořenové názory. Tyto rozšíření mohou přidávat i odstraňovat obsah z jejich rodičovského pohledu.

Prodloužený pohled na objekt odkazuje na svého rodiče pomocí pole „inherit_id“.
Místo jediného pohledu obsahuje pole „arch“ několik
„Xpath“ prvky, které vybírají a mění obsah svého rodičovského pohledu:

... blok kódu::xml

<záznam id="dědičný model/výhled formulář" model="ir.ui.view">
<položka jméno>dědičný.vzorec.formulář.dědictví.test</položka>
<položka jméno="model">dědičný.model</položka>
<položka jméno="dědičný id" odkaz="dědičný model/výhled/formulář"/>
<položka jméno="arch" typ="xml">
// to the form -->
nový_pole po něm -->
<xpath expr="//field[@name='description']" position="after">
<pole název="nové pole" />
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
upravuje atributy shodných prvků pomocí speciálních
„atribut“ prvky v těle „XPathu“.

Při shodě s jediným prvkem lze atribut „position“ nastavit přímo
na prvku, který má být nalezen. Oba dědění mají stejný výsledek.

... blok kódu::xml

<xpath expr="//field[@name='description']" position="after">
<pole název="idea_ids"/>
</xpath>

<položka název="description" pozice="později">
<pole název="idea_ids"/>


Příkladem pro dědičnost pohledu může být
„tady <https://github.com/odoo/odoo/blob/691d1f087040f1ec7066e485d19ce3662dfc6501/addons/account_fleet/views/account_move_views.xml#L3-L17>“.

...cvičení: Přidejte pole do zobrazení uživatelů.

Přidejte pole „property_ids“ do formuláře „základní uživatelé“ v novém listu záznamníku.

Tip: příklad dědění uživatelského pohledu najdete například
`tady <https://github.com/odoo/odoo/blob/691d1f087040f1ec7066e485d19ce3662dfc6501/addons/gamification/views/res_users_views.xml#L5-L14>`__.

Dědičnost je v Odoo široce využívána kvůli jejímu modulárnímu konceptu. Neváhejte si přečíst
Související dokumentace pro více informací!

V další kapitole se dozvíme, jak
interagovat s dalšími moduly.

.._XPath: https://www.w3.org/TR/xpath
