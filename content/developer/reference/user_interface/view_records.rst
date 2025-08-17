============
Zobrazit záznamy
============

Názory definují, jak by se záznamy měly zobrazovat uživatelům.
Uloženy jako záznamy samotné, což znamená, že lze upravovat nezávisle na modelech, které obsahují.
reprezentovat. Jsou flexibilní a umožňují vysokou míru přizpůsobení obrazovek, které
kontroly. Existují různé typy pohledů, každý z nich reprezentuje
zobrazovací režim: *formát*, *seznam*, *karty*, atd.

.. odkaz/zobrazit záznamy/struktura:

Obecná struktura
=================

Základní pohledy sdílejí obecnou minimální strukturu, která je definována níže. Zástupné symboly jsou označeny
Velká písmena.

... blok kódu::xml

<záznam id="ADDON.MODEL_view_TYPE" model="ir.ui.view">
<pole název="jméno">JMÉNO</pole>
<pole název="model">MODEL</pole>
<položka jméno="arch" typ="xml">
<ZOBRAZENÍ_TYPU>
<výhledy/>
</ZOBRAZENÍ
</p>
</záznam>

.. odkaz/zobrazit záznamy/druhy:

Typy zobrazení
==========

:ref:`Tvar <reference/view_architectures/shape>`
Zobrazit a upravovat data z jednoho záznamu.
:ref:`Seznam <reference/view_architectures/list>`
Zobrazit a upravovat více záznamů.
:ref:`Hledání <reference/view_architectures/search>`
Aplikujte filtry a provádějte vyhledávání. Výsledky se zobrazí v aktuálním seznamu, kartách...
:ref:`Kanban <reference/view_architectures/kanban>`
Zobrazit záznamy jako „karty“, které lze upravit jako malý šablonu.
:ref:`Qweb <reference/view_architectures/qweb>`
Šablonování reportingu, webu...
:ref:`Graf <reference/view_architectures/graph>`
Zobrazte agregovaná data z několika záznamů nebo skupin záznamů.
:ref:`Pivot <reference/view_architectures/pivot>`
Zobrazujte agregace jako „pivotovou tabulku“.
:ref:`Kalendář <reference/view_architectures/calendar>`
Zobrazení záznamů jako události v denním, týdenním, měsíčním nebo ročním kalendáři.
:ref:`Kohorta <reference/view_architectures/cohort>`
Zobrazit a porozumět tomu, jak se některá data mění v čase.
:ref:`Gantt <reference/view_architectures/gantt>`
Zobrazit záznamy jako Ganttovu diagram.
:ref:`Síť <reference/view_architectures/network>` |podnik|
Zobrazují počítané informace v buňkách s čísly; jsou málo konfigurovatelné.
:ref:`Mapa <reference/view_architectures/map>`
Zobrazujte záznamy na mapě a trasy mezi nimi.

.. |podnik| neupravený:: html

<span class="badge" style="barva pozadí:#483D59">Funkce pro podniky</span>

.. odkaz/zobrazit záznamy/pole:

Pole
======

Záznamy odhalují řadu polí.

... autoklasifikace: odoo.addons.base.models.ir_ui_view.View

.... atribut:: jméno

Pouze jako pomůcka k zapamatování si pohledu, když hledáte nějaký v seznamu.
Většina názvů pohledů v Odoo začíná jménem doplňku a končí typem pohledu.
diskutovali.

:požadavky: Volitelné
:typ: :třída ~odoo.pole.Char

.... atribut:: model

Pokud je vztah k modelu, tak odkaz na něj.

:požadavek: Povinný
:typ: :třída ~odoo.pole.Char

.... atribut:: arch

Popis způsobu zobrazení záhlaví podle typu :doc:`zobrazení <zobrazovani_architektury>`.

:požadavky: Volitelné
:typ: :třída:`~odoo.fields.Text

...... atribut:: skupiny_id

Skupiny, které mají právo používat/přistupovat k aktuálnímu pohledu.

Pokud se nový pohled rozšiřuje o existující pohled, bude aplikována pouze pro daného uživatele.
že uživatel má přístup k poskytnuté hodnotě `groups_id`.

:požadavky: Volitelné
:typ: :třída:`~odoo.fields.Many2many` -> :třída:`~odoo.addons.base.models.res_users.Groups

.... atribut:: priorita

Při požadavku na zobrazení s určením modelu a typu se vybere nejnižší shodný výhled.
Priorita je vrácena (je výchozí pohled).

Definuje také pořadí aplikace zobrazení při :ref:`vyřešení pohledu
<odkaz/zobrazení záznamů/dědičnost/vyřešení>“. Když je požadováno zobrazení „id“ a jeho
režim není „primární“, jeho nejbližší rodič s režimem „primární“ je vybrán.

:požadavky: Volitelné
:typ: :třída:`~odoo.fields.integer

...... atribut:: dědění id

Odkaz na nadřazený pohled, ze kterého je děděno
<výběr/zobrazení záznamů/dědičnost> se použije. Její hodnota je výchozí.
rodič s atributem „ref“ s hodnotou :code:`ref="ADDON.MODEL_parent_view_TYPE"`

Název doplňku (před tečkou) není nutný, pokud dědění probíhá na záznamu v databázi.
stejný modul.

Podrobnější informace najdete v části :ref:`reference/view_records/inheritance`.

:požadavky: Volitelné
:typ: :třída:`~odoo.fields.many2one

...... atribut:: režim

Pouze pokud tento pohled dědí z jiného pohledu (je nastaveno pole `inherit_id`).

.. atribut: rozšíření

Pokud je požadována zobrazení, vyhledá se nejblíže umístěné primární zobrazení (pomocí `inherit_id`). Pak
všechny pohledy, které dědí z něj, se aplikuje tento pohledový model.

... atribut: primární

Nejbližší primární pohled je plně rozlišený (i když používá jiný model než ten, který byl zvolen).
Současný (aktuální) pohled na věc. Pak následuje :ref:`specifikace dědičnosti
jsou aplikovány specifikace <reference/view_records/inheritance/specs> a výsledek je používán jako by
Architektura skutečného pohledu je tedy taková, jaká byla v době jeho vzniku.

Případ, kdy byste chtěli převzít hodnotu mode při použití inherit_id je delegace
dědění. V tom případě je vaše odvozená vrstva oddělena od svého rodiče a zobrazuje
shodovat se s jedním nebude shodovat s druhým. Předpokládejme, že jeden dědí po zobrazení spojeném
s rodičovským modelem a chce upravit odvozenou zobrazení, aby zobrazila data ze zdrojové tabulky.
model, musí být nastaven na hodnotu `primární`, protože je základem (a
Pokud ano, pak pouze jeden výhled pro tento odvozený model. Jinak by měl být :ref:`výhled shodný
pravidla pro dědění a rozlišení nebudou platit.

Podrobnější informace najdete v části :ref:`reference/view_records/inheritance`.

:požadavky: Volitelné
:typ: :třída:`~odoo.pole.Výběr`: `doplněk` / `primární
:default: `přípona souboru`

.. poznámka::
Výchozí kontext a práva uživatele mohou také ovlivnit schopnost zobrazit obsah.

.. odkaz/zobrazení záznamů/dědictví:

Dědictví
===========

Dědičnost umožňuje přizpůsobit dodané pohledy. Například lze přidat
obsah jako moduly, nebo zobrazit různé displeje podle akce.

Názory dědění mají obecně podobnou strukturu, jak je definována níže. Zástupné symboly jsou označeny v
krycích obalů. Tento syntetický pohled aktualizuje uzly cílené XPath a jiný cílený svým názvem
a atributy.

... blok kódu::xml

<zaznamenání ID="PŘÍSLUŠENSTVÍ.MODEL_ZOBRAZENÍ_TYPU" model="ir.ui.view">
<položka jméno="model">MODEL</položka>

<pole název="mode">MODE</pole>
<položka jméno="arch" typ="xml">
<xpath expr="XPATH" pozice="POZICE">
<OBSAH/>
</xpath>
<NODE ATTRIBUTY="Hodnoty" pozice="Pozice">
<OBSAH/>
</NODE>
</p>
</záznam>

Pole „inherit_id“ a „mode“ určují řešení pohledu.
<odkaz/zobrazit záznamy/dědičnost/vyřešení>“. Elementy „xpath“ nebo „NODE“ ukazují na
:ref:`dědičnost specifikace <reference/view_records/inheritance/specs>“. Specifikace dědičnosti
atributy specifikují pozici dědičnosti podle :ref:`<reference/view_records/inheritance/position>`.

.. odkaz/zobrazit záznamy/dědictví/vyřešení:

Výhled na řešení
---------------

Tato řešení vytvářejí finální „arch“ pro požadovanou nebo shodující se „primární“ perspektivu takto:

#Pokud má pohled nadřízeného, je jeho nadřazený plně vyřešen, pak zadané dědění pro aktuální pohled
jsou aplikovány.
#Pokud není pohled nadřazený žádnému jinému pohledu, jeho „oblouk“ se použije tak, jak je.
#Děti aktuálního pohledu s režimem „rozšíření“ jsou vyhledány a jejich dědické speciály
aplikován hloubkový (první je aplikována dětská zobrazení, pak jejich děti a poté sourozenci).

Dědictví se aplikuje podle pole „inherit_id“. Pokud má několik záznamů v pohledu dědění,
stejný pohled, řazení je určeno „důležitostí“.

Výsledkem aplikace dětských názorů je konečný „oblouk“.

.. všechno: POZNÁMKA k polím view_get a odkaz na ORM?

.. odkaz/zobrazení záznamů/dědičnost/specifikace:

Specifikace dědění
-----------------

Specifikace dědění se aplikují postupně a zahrnují:

#. identifikátor prvku, který odkazuje na děděný prvek v nadřazeném pohledu;
#dětský prvek, který upravuje dědičný prvek.

Existují tři typy hledačů prvků:

- Prvek „xpath“ s atributem „expr“. Atribut „expr“ je „XPath
výraz XPathu \ [#hasclass]_ aplikovaný na aktuální arch
shodné s prvním uzlem, který najde.
- Eleмент pole s atributem „jméno“, shodný se stejným prvkem pole.

...... poznámka::
Ostatní atributy jsou ignorovány.

- Jakýkoliv další prvek s názvem shodným s prvním a stejnými atributy.

...... poznámka::
Atributy „položka“ a „verze“ se ignorují.

... [#hasclass]Do rozšíření QWebu je přidána funkce pro snadnější shodu s výhledem:
'hasclass(*classes)' vyhovuje, pokud kontextový uzel má všechny zadané třídy.

Příklad:
... kódový blok :: XML

<xpath expr="page[@name='pg']/group[@name='gp']/field" position="inside">
<field name="description"/>


<div name="name" position="replace">
<field name="jmeno2"/>
</div>

.. odkaz/zobrazit záznamy/dědictví/pozice:

Pozice dědické
--------------------

Dědické vlastnosti přijímají volitelný atribut „položka“, který má výchozí hodnotu „vnitřní“.
specifikuje, jak by měla být upravena shodná uzlová struktura.

.. atribut: uvnitř

Obsah dědického specifikátoru se připojuje k shodné uzlu.

...... příklad::

... kódový blok::xml

<notebook position="inside">
<stránka>Novinka</stránka>
                 ...
</stránka>
</notebook>

.. atribut:: po

Obsah dědického specifikátoru je připojen k rodičovské noze shodného uzlu po shodě.
uzlík.

...... příklad::

... kódový blok::xml

<xpath expr="//field[@name='x_field']" position="after">
<pole název="x_další_pole"/>
</xpath>

.. atribut:: před

Obsah dědického specifikátoru je připojen k rodičovské noze shodného uzlu před shodným uzlem.
uzlík.

...... příklad::

... kódový blok::xml

<pole název="x_field" pozice="před">
<pole název="x_další_pole"/>
</field>

.. atribut: nahradit

Obsah dědického specifikátoru nahrazuje shodný uzlík. Každý textový uzlík obsahující pouze znaky „$0“
v rámci obsahu specifikace je nahrazen kopií shodného uzlu, což má za následek faktické zabalení
shodný uzlík.

...... příklad::

... kódový blok::xml

<xpath expr="//field[@name='x_field']" position="replace">
<div class="wrapper">
                 $0

</xpath>

.. atribut: atributy

Specifikace dědictví by měla obsahovat pouze atributy, každý s vlastním
Atribut „jméno“ a volitelný obsah těla.

   - Pokud má atribut tělo, je k atributu s názvem odpovídajícím jeho jménu přidán nový atribut.
přesně shodný uzl s hodnotou textu atributu.
   - Pokud je v atributu „attribute“ žádný obsah, atribut s názvem „name“ se z atributu odstraní.
shodné uzly.
   - Pokud má prvek „attribut“ atribut „add“ nebo „remove“, nebo obojí, hodnota
atributu jména u shodných uzlů se znovu vypočítá, aby zohlednil hodnotu (hodnoty)
„přidat“, „odebrat“ a volitelné atributy „oddělovače“ s výchozím nastavením na „,“.
hodnota(y) oddělená znakem „oddělovač“. Znak „odstranit“ odstraňuje hodnotu(y) oddělené znakem „oddělovač“.

...... příklad::
... kódový blok::xml

<pole název="x_pole" pozice="atributy">
<atribut name="neviditelný">True</atribut>
<vlastnost jméno="class" přidat="mt-1 mb-1" odebrat="mt-2 mb-2" oddělovač=" "/>
</field>

.. atribut:: přesun

Atribut „position="move"“ je nastaven na obsah dědění, aby bylo možné specifikovat, jaké uzly
jsou přesunuty vzhledem k elementu určenému specifikací dědění, na kterém je umístěna atributová hodnota „položka“.
Musí být také nastaveny s hodnotami „v rámci“, „nahradit“, „po“ nebo „před“.

...... příklad::
... kódový blok::xml

<xpath expr="//@target" position="po">
<xpath expr="//@node" pozice="přesunout"/>
</xpath>

<field name="target_field" position="after">
<pole název="my_field" pozice="move"/>
</field>

.. _odkaz/zobrazit záznamy/model Commons:

Modelové komunity
=============

... autoklasifikace: odoo.addons.base.models.ir_ui_view.View
:noindex:

......automatickým metodám:: Model.get_views
.... metoda __automethod__: Model.get_view
