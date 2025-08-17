:custom-css:showcase_tables.css

==================
Zobrazení architektury
==================

Architektura obecná
====================

Architektura pohledu je definována pomocí XML dat, která jsou interpretována prostřednictvím JavaScriptového rámce.

Pro většinu pohledů existuje soubor definující atributy a možné architektury s příponou „.rng“.
Některé pohledy nejsou ani tímto souborem ovládány, protože přijímají obsah v HTML nebo kvůli výkonu
důvodu.

.. poznámka::
Vzhledem k aktuálnímu kontextu a oprávněním uživatele se může lišit způsob zobrazení.

.. viz též:
:doc:`zobrazit záznamy“

.. odkaz/zobrazení architektury/Pythonové výrazy:

Pythonový výraz
=================

Při hodnocení atributů uzlu, například modifikátoru readonly, je možné použít Python
výraz, který se provede v prostředí s přístupem k následujícím proměnným:

- Názvy všech polí v aktuálním pohledu obsahující hodnotu aktuálního záznamu
s výjimkou pole „skryté“ v :ref:`přehledu <reference/view_architectures/list/field>`.
relativní pole jsou uvedena jako seznam ID.
- ID aktuálního záznamu.
- `parent“: záznam, který odkazuje na kontejner; pouze uvnitř podvýhledů :ref:`relational
pole <studia/pole/vztahová pole>`;
- `kontext (diktovník)`: aktuální pohled na kontext;
- `uid (int)`: ID aktuálního uživatele;
- „dnes“: aktuální místní datum ve formátu „RRRR-MM-DD“.
- „nyní“ (str): aktuální místní čas ve formátu „YYYY-MM-DD hh:mm:ss“.

Příklad:
... kódový blok :: XML

<pole název="pole_a" čtení="True"/>
<položka název="pole_b" skryté="(context.get('ukáž_mě') a pole_a == 4)"/>

Příklad:
... kódový blok :: XML

<pole name="pole_a"/>
<pole jméno="x2m">
<!-- podvýřez -->
<form>
<polozka název="pole_b" skryté="rodič. pole_a"/>

</p>

.. odkaz/zobrazení architektury:

Tvar
====

Formulářové pohledy se používají k zobrazení dat ze záznamu. Skládají se z běžného HTML
s dalšími semantickými a strukturálními komponentami.

Kořenovým prvkem prohlížeče formulářů je „form“.

... blok kódu::xml

<form>
       ...


.. odkaz/zobrazení architektury/tvar/kořen:

Kořenové atributy
---------------

Povinné atributy lze přidat do kořenového prvku form, aby se upravil vzhled.

... zahrnuje: view_architectures/root_attribute_string.rst

... zahrnuje: view_architectures/root_attribute_create.rst

... zahrnuje soubor: view_architectures/root_attribute_edit.rst

.. atribut: duplicitní
:noindex:

Povolte nebo zakážete duplikaci záznamů v pohledu pomocí tlačítka **Akce**.

:volitelné
:typ: bool
:default: „Pravda“

... zahrnuje: view_architectures/root_attribute_delete.rst

.. atribut::js_class
:noindex:

Název komponenty JavaScriptu, kterou bude webový klient namísto formulářového pohledu.

:volitelné
:typ: str
:default: „“

.. atribut::disable_autofocus
:noindex:

Vypněte automatické zaostřování na první políčko ve výhledu.

:volitelné
:typ: bool
:výchozí hodnota: „Pravda“

.. odkaz/výhled architektur/tvar/semantika:

Semantické komponenty
-------------------

Semantické komponenty jsou vázány na systém Odoo a umožňují s ním interagovat.

Formuláře přijímají následující děti komponenty sémantiky: :ref:` pole
<odkaz/zobrazení architektury/formulář/textové pole>`, :ref:`Text <odkaz/zobrazení architektury/formulář/textový popis>`
:ref:`tlačítko <odkaz/zobrazení architektur/formulář/tlačítko>“
:ref:`reference/view_architectures/form/chatter`,
:ref:`reference/view_architectures/form/attachment`.

Zástupné znaky jsou označeny velkými písmeny.

.. odkaz/výhled architektur/formát/pole:

`pole`: zobrazení hodnot pole
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Element „pole“ zobrazuje (a umožňuje úpravu, pokud je to možné) jediné pole aktuálního záznamu.

Použití pole v rámci jednoho pohledu na formulář je podporováno a pole může přijmout
různé hodnoty atributů „neviditelný“ a „čtení pouze“. Tyto pole mohou mít stejnou
hodnoty, ale jejich zobrazení se může lišit. Chování není garantováno v případě více polí
existují s různými hodnotami atributu „required“.

... blok kódu::xml

<form>
<pole název pole/>


Atributy prvku „pole“ jsou následující:

... zahrnuje: view_architectures/field_attribute_name.rst

.. atribut: id
:noindex:

ID uzlu. Užitečné, pokud je ve výběru několik stejných polí (viz
:ref:`reference/view_architectures/form/label`).

:volitelné
:typ: str
:výchozí hodnota:Název pole

... zahrnuje: architektury/pole_atributu_string.rst

.. atribut: pomoc
:noindex:

Nápověda, která se zobrazí při najetí kurzorem na pole nebo jeho název.

:volitelné
:typ: str
:default: „“

.. atribut: možnosti
:noindex:

Možnosti konfigurace pole widgetu (včetně výchozích widgetů), jako v Pythonu
výraz, který vyhodnocuje na seznamu.

Pro pole vztahů jsou k dispozici následující možnosti: „no_create“, „no_quick_create“.
„neotevřít“, „nepřidávat“ a „nedat“.

...... příklad::
... kódový blok::xml



:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:výchozí hodnota: `{}`

... zahrnout: view_architectures/field_attribute_readonly.rst

... zahrnuje: view_architectures/field_attribute_required.rst

... zahrnují: view_architectures/generic_attribute_invisible.rst

... zahrnuje: view_architectures/generic_attribute_groups.rst

.. atribut:: doména
:noindex:

Filtry použít při zobrazení existujících záznamů pro výběr jako v Pythonu
hodnota je doménou:ref:`<reference/orm/domains>`.

...... příklad::
... kódový blok::xml



:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:default: `[]`
:rozsah: Relativní pole

.. atribut: kontext
:noindex:

......::obsáhlé dokumentace všech magických kontextových hodnot (TYPE_view_ref, group_by,
hledat_v_poli_FIELD...

Kontext pro získávání možných hodnot a vytváření nebo vyhledávání záznamů jako v jazyce Python
výraz, který vyhodnocuje na seznamu.

...... příklad::
... kódový blok::xml

<pole jméno="fname" kontext="{"
'VZHLED_odkaz_referenci': 'PŘÍSLUŠENSTVÍ.MODEL_vzorek_VZHLED',
"skupit": "NÁZEV POLE",
'default_FIELD_NAME': ANY
'search_default_FIELD_NAME': True,
'DALŠÍ_OBCHODNÍ_KLÍČ': libovolný
           }"/>

:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:výchozí hodnota: `{}`
:rozsah: Relativní pole

.. atribut: nenázev
:noindex:

Zda se pole s popisem skrývá nebo ne.

:volitelné
:typ: bool
:výchozí hodnota: „Pravda“
:rozsah:Pole, která jsou přímo dítětem elementu `group`.

.. atribut: místo
:noindex:

Pomocná zpráva, která se má zobrazit v prázdných polích. Může nahradit pole ve složitějších formulářích.
Ale nemělo by se jednat o příklad dat, protože uživatelé mohou zaměnit místní text s vyplněným
pole.

:volitelné
:typ: str
:default: „“

.. atribut:: režim
:noindex:

Seznam zobrazovacích režimů (typů zobrazení), které mají být použity pro spojené záznamy pole.
Povolené režimy jsou: „seznam“, „formulář“, „kanban“ a „graf“.

:volitelné
:typ: str
:default: „seznam“
:rozsah: pole :třída:`~odoo.fields.One2many` a pole :třída:`~odoo.fields.Many2many

... zahrnují: view_architectures/generic_attribute_class.rst

.. atribut: název souboru
:noindex:

Název pole souvisejícího s názvem souboru, které poskytuje název souboru.

:volitelné
:typ: str
:default: „“
:rozsah: :třída:`~odoo.fields.Binary` pole

.. atribut:: heslo
:noindex:

Zda pole uchovává heslo, takže by jeho obsah neměl být zobrazován.

:volitelné
:typ: bool
:výchozí hodnota: „Pravda“
:rozsah: :třída:`~odoo.fields.Char` pole

... atribut:: kanban_view_ref
:noindex:

Specifický kanbanový záznam má své vlastní ID XML. To by mělo být použito při zobrazení konkrétního
výběru záznamů v mobilním prostředí.

:volitelné
:typ: str
:default: „“
:rozsah: Relativní pole

... atribut: default_focus
:noindex:

Zda je pole zaostřené, když se otevře pohled. Může být aplikováno pouze na jedno pole v pohledu.

:volitelné
:typ: bool
:výchozí hodnota: „Pravda“

.. poznámka::
:ref:`Vztahové pole <studio/fields/relational-fields> mohou obsahovat specifické podvýhledy.“

...... příklad::
... kódový blok::xml

<field name="children_ids">
<seznam>
<pole název/>
</seznam>
<form>
<pole id/>
<pole název/>
</form>
</field>

.. odkaz/výhled architektury/formát/název:

`label`: pole pro zobrazení názvu položky
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Když komponenta pole (:ref:`<reference/view_architectures/form/field>`) není umístěna přímo
v rámci skupiny (viz. vlastnost reference/view_architectures/form/group), nebo pokud má atribut nolabel
set, pole není automaticky zobrazeno vedle jeho hodnoty. Komponenta „label“
ruční alternativa zobrazení štítku pole.

... blok kódu::xml

<form>
<div class="col col-md-auto">
<label for="POLE_JMENO" string="LABEL"/>

<pole název="POLE_NAZEV" třída="oe_inline"/>
</div>
</div>


Atributy prvku label mohou být následující:

.. atribut:: pro
:noindex:

Odkaz na pole spojené s štítkem. Může jít buď o název pole, nebo
její ID (atribut „id“ nastavený na poli :ref:`<reference/view_architectures/form/field>`).

Pokud je ve výhledu více polí stejného typu a existuje několik „štítků“
komponenty spojené s těmito poli, tyto štítky musí mít jedinečné atributy „for“.
V tomto případě odkazujeme na atribut „id“ odpovídajících políček.

:požadavek:Povinné
:typ: str

.. atribut: řetězec
:noindex:

Zobrazovaný název.

:volitelné
:typ: str
:výchozí:Popis pole z definice pole na modelu

... zahrnují: view_architectures/generic_attribute_class.rst

... zahrnují: view_architectures/generic_attribute_invisible.rst

.. odkaz/zobrazení architektury/tvar tlačítka:

„tlačítko“: zobrazení tlačítek pro akce
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

... blok kódu::xml

<form>
<tlačítko typu "objekt" jméno="akce" popis="popisek"/>
<tlačítko typu "objekt" jméno="AKCE" ikonou="FONT_AWESOME"/>


Element „tlačítko“ může mít následující atributy:

... zahrnuje soubor view_architectures/button_attribute_type.rst

... zahrnuje: view_architectures/button_attribute_name.rst

... zahrnout: view_architectures/button_attribute_string.rst

... zahrnují: view_architectures/button_attribute_icon.rst

... zahrnuje: view_architectures/button_attribute_help.rst

... zahrnuje soubor: view_architectures/button_attribute_context.rst

... zahrnuje: view_architectures/generic_attribute_groups.rst

... zahrnují: view_architectures/generic_attribute_invisible.rst

... zahrnují: view_architectures/generic_attribute_class.rst

.. atribut: speciální
:noindex:

Chování tlačítka pro zobrazení formuláře v dialogovém okně. Může mít dvě různé hodnoty:

.... atribut:: uložit


Uložte záznam a zavřete dialogové okno.

.... atribut:: zrušit


Zavřít okno bez uložení změn.

...... příklad::
... kódový blok::xml

<tlačítko special="cancel" ikonou="fa-trash"/>

:volitelné
:typ: str
:default: „“

.. atribut: potvrdit
:noindex:

Před provedením tlačítka je nutné zobrazit a uživateli přijmout potvrzující zprávu.
akce.

...... příklad::
... kódový blok::xml

<tlačítko jméno="akce_zničit_bránu" název="Odešlete Goa'ulda" typ="objekt" potvrzení="Potvrzujete akci?">

:volitelné
:typ: str
:default: „“

.. atribut:: data-hotkey
:noindex:

Zkratka klávesnice (podobná jako přístupová klávesa) která je přiřazena tlačítku.
aktivní stiskem klávesy Alt spolu s vybraným znakem nebo spolu s klávesou
„Shift“ klávesa a zvolený znak, pokud je „Shift +“ připojen k hodnotě.

...... příklad::
... kódový blok::xml

<tlačítko typu "objekt" jméno="akce_potvrdit" string="Potvrdit" data-hotkey="c"/>
<button typ="objekt" jméno="akce_trhat" název="Trhnout list" data-hotkey="shift+k"/>

:volitelné
:typ: str
:default: „“

.. odkaz/výhled architektury/tvar chatu:

Chatovací prvek
~~~~~~~~~~~~~~

Chatovací widget je komunikační a záznamový nástroj, který umožňuje
posílat e-maily kolegům nebo zákazníkům přímo z záznamu (úkol, objednávka, faktura, událost, poznámka...).

Přidá se do něj prvek div s třídou oe_chatter, když se model zdědí
Mixin „mail.thread“.

Příklad:
... kódový blok :: XML

<form>
<listina>
              ...
</list>
<div class="oe_chatter">
<pole název="message_follower_ids"/>
<pole název="activity_ids"/>
<položka jméno="message_ids" volby="OPTIONS"/>

</form>

.. odkaz/zobrazení architektury/tvar/příloha:

Náhled připojených souborů
~~~~~~~~~~~~~~~~~~~~~~~~~~

Předpřítomný widget pro náhled přílohy je přidán pomocí prázdného tagu div s třídou
„o_předběžný_návrh“.

Příklad:
... kódový blok :: XML

<form>
<listina>
              ...
</list>
<div class="o_attachment_preview"/>
<form>

.. Reference/Zobrazení architektury/Forma/Strukturální:

Strukturální součásti
---------------------

Strukturální prvky poskytují strukturu nebo „vizuální“ vlastnosti s malým logickým významem. Jsou používány jako
elementy nebo skupiny elementů v pohledech na formuláře.

Formulářové pohledy přijímají následující děti strukturálních komponent: :ref:`skupina
<odkaz/zobrazení architektury/formulář/skupina>“, :ref:“list <odkaz/zobrazení architektury/formulář/list>“
:ref:`počítač <reference/view_architectures/form/computer>`
:ref:`počítač <reference/view_architectures/form/computer>`
:ref:`nový řádek <reference/view_architectures/form/newline>“
:ref:`oddělovač <reference/view_architectures/form/separators>`,
:ref:`hlavička <reference/view_architectures/form/header>“
:ref:`<reference/view_architectures/form/footer>`
:ref:`reference/view_architectures/form/button_container`,
:ref:`reference/view_architectures/form/title_container`.

Zástupné znaky jsou označeny velkými písmeny.

.._reference/view_architectures/form/group:

`skupina“: definujte uspořádání sloupců
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „skupina“ se používá k definování uspořádání sloupců v formulářích. Výchozí hodnotou je dvě sloupce.
A nejjednodušší děti skupin mají pouze jednu sloupec.

:ref:`pole <reference/view_architectures/form/field>` prvků, které jsou přímo podřízeny skupinám
ve výchozím nastavení zobrazit „štítek“ a šířku sloupce obou polí mají stejnou hodnotu 1.

Děti jsou položeny na rovinu (snaží se naplnit další sloupec, než změní řádek).

... blok kódu::xml

<form>
<skupina>
           ...
</skupina>


Element „skupina“ může obsahovat následující atributy:

.. atribut: řetězec
:noindex:

Název skupiny zobrazený v titulku.

:volitelné
:typ: str
:default: „“

.. atribut: col
:noindex:

Počet sloupců v skupině.

:volitelné
:typ: int
:default: 2

.. atribut::
:noindex:

Počet sloupců, které se vezme do dětského prvku.

:volitelné
:typ: int
:default: 1

... zahrnují: view_architectures/generic_attribute_invisible.rst

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * 
:align: střed

      * 

<skupina>


</skupina>
<skupina>
<skupina>


</skupina>
<skupina>

<pole name="f"/>

</skupina>
</skupina>
<skupina kolonky="12">

<pole name="h" />
</skupina>
<skupina kolon="4">

</skupina>
</skupina>

... odkaz/výhled architektur/formát/list:

`layout`: udělejte layout reagujícím
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „list“ může být použit jako přímý potomek prvek formuláře
<reference/view_architectures/form> pro užší a reagující formulář
(střední stránka, okraj ...). Obvykle obsahuje:
Elementy „<reference/view_architectures/form/group>“.

... blok kódu::xml

<form>
<list>
           ...
</list>


.. odkaz/zobrazení architektury/tvar/poznámkový blok:

„notebook“ a „stránka“: přidat záložky
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Element „poznámkový blok“ definuje sekci s kartami. Každá karta je definována pomocí dětského prvku „stránka“.

Prvek „poznámkový blok“ by neměl být umístěn v rámci prvku „skupina“.

... blok kódu::xml

<form>
<notebook>
<stránka značky="LABEL">
               ...

</notebook>


Element „stránka“ může mít následující atributy:

.. atribut: řetězec
:noindex:

Název záložky.

:volitelné
:typ: str
:default: „“

... zahrnují: view_architectures/generic_attribute_invisible.rst

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * — .. obrázek: view_architectures/form_notebook.svg
:align: střed

      * 

<form>


                         ...
</stránka>

                         ...
</stránka>
</počítači>
</form>

.. odkaz/zobrazení architektury/formát/nový řádek:

„nový řádek“: začíná novou skupinu řádků
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „nový řádek“ se používá v rámci :ref:`skupiny <reference/view_architectures/form/group>`.
elementy k ukončení současného řádku dříve a přechod na nový řádek bez vyplnění
zbytku sloupce předem.

... blok kódu::xml

<form>
<skupina>
           ...

           ...
</skupina>


.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * 
:align: střed

      * 

<form>

<skupina string="Titulek 1.1">...</skupina>



</skupina>
</form>

.. odkaz/výhled architektury/formát/oddělovač:

`separátor`: přidat horizontální odsazení
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „separátor“ přidává vertikální odsazení mezi prvky v rámci skupiny.

... blok kódu::xml

<form>
       ...
<separator/>
       ...


Element „<separator>“ může mít následující atributy:

.. atribut: řetězec
:noindex:

Název jako nadpis sekce.

:volitelné
:typ: str
:default: „“

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * 
:align: střed

      * 

<form>
<skupina>
</FIELD>

</FIELD>
<skupina>
<POLE/>
<separator string="Titul 2"/>
<POLE/>

<skupina>
<POLE/>
<POLE/>

</skupina>
</form>

..tip:
Element „separátor“ může být použit k dosažení vizuální separace mezi prvky, které jsou umístěny vedle sebe.
vnitřní „skupinový“ prvek, aniž by se tyto prvky vertikálně vyrovnávaly.

.. odkaz/výhled architektury/formát hlavičky:

„hlavička“: zobrazení tlačítek pro práci s procesy a stav
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Eleмент „hlavička“ v kombinaci s :ref:`listem <reference/view_architectures/form/sheet>“.
Tento prvek poskytuje plnohodnotné umístění nad samotnou listovou plochou, které se obvykle používá k zobrazení postupu.
tlačítka <odkaz/pohledy na architekturu/formulář/tlačítko> a pole
Element <odkaz/zobrazení architektury/formulář/pole> zobrazuje stavovou lištu.

... blok kódu::xml

<form>
<hlavička>
<TLAČÍTKA/>

<list>
           ...
</list>


Příklad:

... kódový blok :: XML

<hlavička>




.. _reference/view_architectures/form/footer:

„Footer“: Zobrazit tlačítka dialogu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Element „footer“ se používá k zobrazení tlačítka:ref:`<reference/view_architectures/form/button>
elementy na konci dialogů.

... blok kódu::xml

<form>
<list>
           ...
</list>
<footer>
<TLAČÍTKA/>
</p>


Příklad:
... kódový blok :: XML

</footer>
<tlačítko text="Uložit" special="save"/>
<tlačítko typu="objekt" název="my_action" třída="btn-primary">
<tlačítko>Discard</tlačítko>


Pokud není uveden žádný prvek „patička“, bude se zobrazit standardní tlačítko pro uložení nebo odmítnutí.
je přednastavená a lze ji také odstranit, pokud chcete nahradit standardní tlačítka v formuláři nebo x2many
dialogy pomocí atributu replace, který má výchozí hodnotu True, pokud není specifikován.
Pokud nastavíte hodnotu na „false“ (nebo 0), bude se zobrazovat uvedený „footer“.
Nastavení výchozích tlačítek namísto jejich nahrazování.

Příklad:
... kódový blok :: XML

<footer replace="0">
<tlačítko typu="objekt" jméno="my_action" třída="btn-primary">


.. odkaz/zobrazení architektury/tvar/přístup k tlačítku:

Koš s tlačítky
~~~~~~~~~~~~~~~~~

Elementy obsahující tlačítko lze vytvořit s
Element „div“ s třídou „button_box“.

... blok kódu::xml

<form>
<div name="button_box">
<TLAČÍTKA/>
</div>
<form>

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * 
:align: střed

      * 

<form>
<div id="button_box">



<button type="submit">

<form>

.. _reference/view_architectures/form/title_container:

Záhlaví kontejneru
~~~~~~~~~~~~~~~

Element kontejneru pole <reference/view_architectures/form/field> lze vytvořit pomocí
element div s třídou oe_title.

... blok kódu::xml

<form>
<list>
<div class="oe_title">
<H1><FIELD/></H1>

</list>
<form>

.. odkaz/výhled architektury/nastavení:

Nastavení
========

Nastavení je zobrazením, které upravuje formát :ref:`<reference/view_architectures/form>`.
slouží k zobrazení nastavení na jednom místě. Od obecných formulářových pohledů se liší tím, že
Mají vyhledávací lištu a boční panel.

Příklad:

... kódový blok :: XML

<aplikace název="CRM" jméno="crm">
<settings typ="hlavička" string="Fůů">
<políčko název="foo" titul="Fů?"/>
<tlačítko jménoAkce typ="objekt" string="Tlačítko"/>
</nastavení>
<blok titul="Název skupiny BAR">
<param help="to je pásek" dokumentace="/aplikace/technické/weby/nastavení/to_je_pásek.html">
<pole name="bar" />
</nastavení>
<nastavení>string="To je velká BAR" company_specific="1">
<pole name="bar" />
</nastavení>

<blok titulem skupiny „Foo“>
<nastavení typu="Nastavení pro osobní účet" pomoc="to je plné nastavení pro osobní účet">
Toto je jiný prostředí.
</nastavení>

</aplikace>

.. _reference/view_architectures/settings/components:

Součásti
----------

Nastavení akceptuje pole :ref:`<reference/view_architectures/form/field>` a :ref:`<reference/view_architectures/form/label>`.
<odkaz/zobrazení architektury/tvar/text> a :ref:`tlačítko
<odkaz/zobrazení architektury/tvar/tlačítko> prvků:
Viditelné architektonické prvky (viz reference/view_architectures/form>) a tři další dětské elementy:
:ref:`aplikace <reference/view_architectures/settings/app>` a :ref:`blok
<odkaz/výhled architektury/nastavení/blok>“ a „:ref:“ nastavení
<odkaz/zobrazení architektury/nastavení/nastavení>>.

Zástupné znaky jsou označeny velkými písmeny.

.. odkaz/výhled/architektury/nastavení/aplikace:

`app`: deklarovat aplikaci
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „aplikace“ se používá k deklarování aplikace na stránce nastavení. Vytvoří záznam s
logo aplikace na liště pohledu. Dále slouží jako oddělovač při vyhledávání.

... blok kódu::xml

<form>
<app string="JMÉNO" name="TECHNICKÝ NÁZEV">
       ...
<app></app>


Atributy prvku „aplikace“ mohou být následující:

.. atribut: řetězec
:noindex:

Název aplikace.

:požadavek:Povinné
:typ: str

.. atribut: jméno
:noindex:

Technické označení aplikace (název modulu).

:požadavek:Povinné
:typ: str

.. atribut:: logo
:noindex:

Relativní cesta k logu.

:volitelné
:typ: cesta
:default: Cesta vypočítaná pomocí atributu „název“: :file:`/{název}/statické/popis/icon.png`

...vše: atribut dokumentu notApp

... zahrnuje: view_architectures/generic_attribute_groups.rst

... zahrnují: view_architectures/generic_attribute_invisible.rst

.. odkaz/zobrazení architektur/nastavení bloků:

`blok`: deklarovat skupinu nastavení
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „blok“ se používá k vyjádření skupiny nastavení. Tato skupina může obsahovat titulek a
Popis

... blok kódu::xml

<form>
<app string="JMÉNO" name="TECHNICKÝ NÁZEV">
           ...
<blok titul="TITLE">
               ...
</blok>
           ...
<app></app>


Element „blok“ může mít následující atributy:

.. atribut:: název
:noindex:

Název bloku nastavení. Lze vyhledat na jeho hodnotu.

:volitelné
:typ: str
:default: „“

.. atribut: pomoc
:noindex:

Popis bloku nastavení. Lze hledat podle jeho hodnoty.

:volitelné
:typ: str
:default: „“

... zahrnuje: view_architectures/generic_attribute_groups.rst

... zahrnují: view_architectures/generic_attribute_invisible.rst

.. odkaz/zobrazení architektury/nastavení/nastavení:

`nastavení`: vyhlásit nastavení
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Element „settings“ se používá k vyjádření nastavení samotného.

První :ref:`pole <reference/view_architectures/form/field>` v nastavení se používá jako
hlavní pole. Je umístěno v levém panelu pokud je to logické pole a na vrcholu pravého panelu
panel jinak. Pole se také používá k vytvoření štítku nastavení, pokud není atribut „string“
definováno.

Prvek „settings“ může také obsahovat další prvky (např. HTML). Všechny tyto prvky jsou
v pravém sloupci.

... blok kódu::xml

<form>
<app string="JMÉNO" name="TECHNICKÝ NÁZEV">
<blok titul="TITLE">
               ...
<settings name="SETTING_NAME">
                   ...
<pole název pole/>
                   ...
</nastavení>
               ...
</blok>
<app></app>


Element „<settings>“ může obsahovat následující atributy:

.. atribut: typ
:noindex:

Výchozí nastavení je vizuálně odděleno na dvou panelech (levém a pravém) a používá se k editaci
Přiřazené pole :ref:`<reference/view_architectures/form/field>`. Při definování typu „hlavička“
místo toho se použije speciální nastavení, které se používá k upravení rozsahu
jiných nastavení. Například v aplikaci Webové stránky se tento parametr používá k indikaci
která webová stránka se používají ostatní nastavení. Hlavička je vizuálně reprezentována jako banner na
nahoře na obrazovce.

:volitelné
:typ: str
:default: „“

.. atribut: řetězec
:noindex:

Text použitý jako název nastavení.

:volitelné
:typ: str
:default:Popis prvního pole

.. atribut:: název
:noindex:

Text použitý jako nápověda.

:volitelné
:typ: str
:default: „“

.. atribut: pomoc
:noindex:

Popis nastavení. Tento text se zobrazuje hned pod názvem nastavení (s
třída „text-muted“.

:volitelné
:typ: str
:default: „“

.. atribut: společnost_zaměstnavatel
:noindex:

Zda je nastavení specifické pro danou společnost. Pokud ano, zobrazí se vedle názvu nastavení ikonka.

Přijímá pouze hodnotu „1“.

:volitelné
:typ: str
:default: „“

.. atribut: dokumentace
:noindex:

Cesta k dokumentaci nastavení. Pokud je zadáno, ukazuje se vedle ikona pro kliknutí.
- nastavení štítku. Cesta může být buď absolutní nebo „relativní cesta“_ v případě, že je relativní.
Je vztahováno k „https://www.odoo.com/documentation/<verze>“.

:volitelné
:typ: `cesta_`
:default: „“

... zahrnuje: view_architectures/generic_attribute_groups.rst

... zahrnují: view_architectures/generic_attribute_invisible.rst

.. odkaz/výhled architektury/seznam:

Seznam
====

Kořenovým prvkem seznamového pohledu je prvek „list“ (dříve „strom“).

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * — ... obrázek: view_architectures/list.svg
:align: střed

      * 

<seznam>
                 ...
</list>

... odkaz/zobrazení architektury/seznam/kořen:

Kořenové atributy
---------------

Povinné atributy mohou být přidány do kořenového prvku list, aby bylo možné zobrazit vlastní pohled.

... zahrnuje: view_architectures/root_attribute_string.rst

... zahrnuje: view_architectures/root_attribute_create.rst

... zahrnuje soubor: view_architectures/root_attribute_edit.rst

... zahrnuje: view_architectures/root_attribute_delete.rst

.. atribut import
:noindex:

Zapnout/vypnout import záznamů z dat na pohledu.

:volitelné
:typ: bool
:default: „Pravda“

.. atribut:: export_xlsx
:noindex:

Zapnout nebo vypnout export záznamů do dat na pohledu.

:volitelné
:typ: bool
:default: „Pravda“

.. atribut::editovatelný
:noindex:

Umožněte upravovat záznamy v zobrazení přímo na místě a umožněte vytvářet nové záznamy ze sloupce seznamu.
Může mít dvě různé hodnoty:

...... atribut:: top


Nový rekord vytváříme z vrcholu seznamu.

.... atribut:: spodní


Nové záznamy se vytvářejí z konce seznamu.

Architektura pro formulářový pohled :ref:`<reference/view_architectures/form>` je odvozena
z seznamového pohledu. Většina atributů platných pro pole a tlačítka na formuláři je tak přijímána
- v seznamovém pohledu, i když nemusí mít žádný význam, pokud je seznamový pohled neupravitelný.

.... důležité::
Toto chování je vypnuto, pokud je atribut edit nastaven na hodnotu False.

:volitelné
:typ: str
:default: „“

.. atribut:: multi_edit
:noindex:

Aktivujte funkci víceúrovňového editování, která umožňuje aktualizovat pole na stejnou hodnotu pro více polí.
záznamy najednou.

Přijímá pouze hodnotu „1“.

:volitelné
:typ: str
:default: „“

.. atribut: otevřená forma
:noindex:

Zobrazte tlačítko na konci každé řádky, které otevře záznam v zobrazení formuláře.

Pokud je pohled neupravitelný, nemá žádný vliv.

:volitelné
:typ: bool
:výchozí hodnota: „Pravda“

... zahrnují: view_architectures/root_attribute_default_group_by.rst

... zahrnuje: :: view_architectures/root_attribute_default_order.rst

.. atribut:: dekorace-<styl>
:noindex:

Styl, který se má použít k řádkům shodujících záznamů jako k Pythonovskému výrazu,
na logickou hodnotu.

„<styl>“ musí být nahrazen jedním z „bf“ (tučné písmo), „it“ (kurzíva), „info“, „varování“, „nebezpečí“.
„povolené“, „primární“ a „úspěšné“.

...... příklad::
... kódový blok::xml

<list decoration-danger="(qty &gt; limit)">
             ...
</seznam>

:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:výchozí hodnota: „Pravda“

.. atribut: limit
:noindex:

Výchozí velikost stránky. Musí být vždy kladné číslo.

:volitelné
:typ: int
:default: „80“ pro seznamy a „40“ pro formuláře

.. atribut: groups_limit
:noindex:

Počet skupin na stránce při zobrazení seznamu, který je seskupený. Musí být přesně
positivní.

:volitelné
:typ: int
:default: „80“ pro seznamy a „40“ pro formuláře

.. atribut:: rozbalit
:noindex:

Zda se v seznamovém pohledu zobrazí skupiny jako výchozí.

.... upozornění::
Může být pomalé v závislosti na počtu skupin.

:volitelné
:typ: bool
:výchozí hodnota: „Pravda“

... zahrnuje: view_architectures/root_attribute_sample.rst

.. odkaz/výhled architektury/seznam komponent:

Součásti
----------

Výpisy polí přijímají následující děti prvky: :ref:`field
<odkaz/výhled architektur/seznam/pole>`, :ref:"tlačítko
<odkaz/zobrazit_architektury/seznam/tlačítko>`, :ref:`skupovat
<odkaz/výhled architektur/seznam/skupinový výběr>`, :ref:"hlavička
<odkaz/zobrazení architektury/seznam/hlavička>`, :ref:"kontrolu a vytvářet
<odkaz/zobrazit architektury/seznam/kontrola>.

Zástupné znaky jsou označeny velkými písmeny.

.. odkaz/výhled architektur/seznam/pole:

`pole`: zobrazení hodnot pole
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „pole“ zobrazuje (a umožňuje editaci) jedno pole všech aktuálních záznamů.
v podobě sloupku.

Použití stejného pole v seznamovém výhledu vícekrát není podporováno.

... blok kódu::xml

<list>
<pole název pole/>


Atributy prvku „pole“ jsou následující:

... zahrnuje: view_architectures/field_attribute_name.rst

... zahrnuje: architektury/pole_atributu_string.rst

.. atribut:: volitelný
:noindex:

Změňte viditelnost pole na volitelnou. Sloupec pole může být skrytý nebo zobrazený podle potřeby.
tlačítko v hlavním panelu aplikace.

Může mít dvě různé hodnoty:

...... atribut:: show


Karta pole se zobrazuje automaticky.

...... atribut:: skrýt


pole je skryté výchozím nastavením.

...... příklad::
... kódový blok::xml

<pole název="fname_a" volitelné="zobrazit"/>
<pole název="fname_b" volitelné="skrýt"/>

:volitelné
:typ: str

... zahrnout: view_architectures/field_attribute_readonly.rst

... zahrnuje: view_architectures/field_attribute_required.rst

... zahrnují: view_architectures/generic_attribute_invisible.rst

... zahrnuje: view_architectures/generic_attribute_column_invisible.rst

... zahrnuje: view_architectures/generic_attribute_groups.rst

.. atribut:: dekorace-<styl>
:noindex:

Styl, který se má použít na pole shodného záznamu jako Pythonový výraz
hodnotí na logickou hodnotu.

„<styl>“ musí být nahrazen jedním z „bf“ (tučné písmo), „it“ (kurzíva), „info“, „varování“, „nebezpečí“.
„povolené“, „primární“ a „úspěšné“.

...... příklad::
... kódový blok::xml

<field name="jméno" dekorace-bf="1"/>
<vlastnost jméno="množství" dekorace-info="stav == 'návrh'" />

:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:výchozí hodnota: „Pravda“

.. atribut:: součet, průměr
:noindex:

Agregát, který se zobrazí na konci sloupce. Aggregace je vypočítána pouze
zobrazených záznamů. Operace agregace musí odpovídat příslušnému
pole „agregátor“.

...... příklad::
... kódový blok::xml

<pole název="Sent" součet="Celkem"/>
<field name="kliknutí/prohlédnutí" avg="Průměr"/>

:volitelné
:typ: str
:default: „“

.. atribut: šířka
:noindex:

Vždy se snaží optimalizovat dostupný prostor mezi sloupci. U některých typů polí se
To se dělá tím, že se nadefinuje šířka závislá na typu pole. Například víme přesně,
počet pixelů potřebných k zobrazení data, takže můžeme zajistit sloupec pro pole datumu
nepotřebuje více místa než je nutné, takže zbytek prostoru může být využíván pro
jiných sloupců. Avšak rámec nemůže odhadnout vhodnou šířku pro všechny typy polí.
Příkladem mohou být pole typu char, která lze použít k uložení velkých hodnot nebo třímístných kódů zemí.
V případě druhém lze šířku nastavit přímo v archu (například pomocí atributu width="40px").
šířka (vždy v pixelech), která je potřebná k zobrazení hodnot uvnitř buněk.
Poté bude sloupec součtem hodnoty a mezer vlevo a vpravo od buňky.

:volitelné
:typ: str
:default: „“

.. atribut: nenázev
:noindex:

Zda mají být v poli sloupců nadpisy prázdné. Pokud je nastavena hodnota True, nebude možné sloupec řadit.

Přijímá pouze hodnotu „1“.

:volitelné
:typ: str
:default: „“

.. poznámka::
Když je seznam zobrazen ve skupině, agregované číselné pole jsou zobrazovány pro každou skupinu.
pokud je v skupině příliš mnoho záznamů, objeví se na pravé straně řádku skupiny posuvník.
důvodu je špatná praxe mít numerické pole v poslední sloupcový seznam.
situace, kdy se dá seskupit. Avšak pro pole s příliš mnoha hodnotami není problémem.
Ve formuláři se nezobrazují, protože nelze seskupit.

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * 
:align: střed

      * 

<seznam>

<field name="cena" sum="Celkem"/>
<field name="měna_id"/>

</list>

.. odkaz/zobrazení architektur/seznam/tlačítko:

„tlačítko“: zobrazení tlačítek pro akce
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

... blok kódu::xml

<list>
<tlačítko typu "objekt" jméno="akce" popis="popisek"/>
<tlačítko typu "objekt" jméno="AKCE" ikonou="FONT_AWESOME"/>


Element „tlačítko“ může mít následující atributy:

... zahrnuje soubor view_architectures/button_attribute_type.rst

... zahrnuje: view_architectures/button_attribute_name.rst

... zahrnout: view_architectures/button_attribute_string.rst

... zahrnují: view_architectures/button_attribute_icon.rst

... zahrnuje: view_architectures/button_attribute_help.rst

... zahrnuje soubor: view_architectures/button_attribute_context.rst

... zahrnuje: view_architectures/generic_attribute_groups.rst

... zahrnují: view_architectures/generic_attribute_invisible.rst

... zahrnuje: view_architectures/generic_attribute_column_invisible.rst

... zahrnují: view_architectures/generic_attribute_class.rst

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * 
:align: střed

      * 

<seznam>




<field name="měna_id"/>

</list>

.. odkaz/výhledy architektury/seznam/skupiny podle:

`groupby`: definovat hlavičky skupin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Element „groupby“ se používá k definování hlaviček skupin s tlačítkem
elementy <reference/view_architectures/list/button> při seskupování záznamů podle
Pole :attr:`~odoo.fields.Many2one`, které také přijímá pole :ref:`field
elementy typu <odkaz/zobrazení architektury/seznam/pole> lze použít jako modifikátory. Tyto pole
patří do modelu Many2One a jsou načítány v rámci jedné operace.

... blok kódu::xml

<list>
       ...
<group by="FIELD_NAME">
<TLAČÍTKA/>
<POLE/>
</skupina>


Atributy prvku „group by“ mohou být následující:

.. atribut: jméno
:noindex:

Název pole typu :attr:`~odoo.fields.Many2one`, které se má použít jako hlavička.

Speciální :ref:`tlačítko <reference/view_architectures/list/button>` s atributem `type="edit"`
bude definována pro otevření formuláře pole Many2one.

:požadavek:Povinné
:typ: str

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * 
:align: střed

      * 

<seznam>





<group by="partner_id">
<tlačítko typu "edit" jméno="edit" ikonou="fa-edit" titulem="Edit"/>


</skupina>
</list>

.. poznámka::
V poli uvnitř tagu groupby se používá pouze k vyzvednutí a uložení hodnoty.
nikdy nebyla zveřejněna.

.. odkaz/zobrazení architektury/seznam/hlavička:

„hlavička“: Zobrazit tlačítka pro práci s procesem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

... blok kódu::xml

<list>
<hlavička>
<TLAČÍTKA/>

       ...


Element „hlavička“ přijímá následující podřízené prvky:

.. atribut:: tlačítko
:noindex:

Element „tlačítko“ umožňuje definovat tlačítka v ovládacím panelu. Je stejný jako element
:ref:`tlačítko v seznamovém zobrazení <odkaz/architektura-zobrazeni/seznam/>“, ale přijímá
další vlastnost, pokud je umístěna uvnitř tagu header:

...... atribut:: zobrazit


Tlačítko by mělo být vždy k dispozici bez nutnosti vybírat záznamy.

Přijímá pouze hodnotu „vždy“.

... příklad::

... kódový blok::xml






:požadavky: Volitelné
:typ: str
:výchozí hodnota: „“

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * 
:align: střed

      * 

<seznam>
<hlavička>






</list>

.. odkaz/výhled architektur/seznam/kontrola:

„Kontrola“ a „Vytvoření“: přidat tlačítka pro vytváření přímo do textu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Element „control“ definuje řádek ovládání, který přijímá tlačítka pro vytváření nových polí. Každé tlačítko pro vytváření nového pole
definované pomocí prvku create.

... blok kódu::xml

<list>
<kontrola>
<vytvořit>LABEL</vytvořit>
<TLAČÍTKA/>
</control>
       ...


Atributy nemá ani prvek „control“.

Element „vytvořit“ může mít následující atributy:

.. atribut: řetězec
:noindex:

Text tlačítka.

:požadavek:Povinné
:typ: str

.. atribut: kontext
:noindex:

Kontext, který se do kontextu pohledu přidá při volání tlačítka jako Python
výraz, který vyhodnocuje na seznamu.

:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:výchozí hodnota: `{}`

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * 
:align: střed

      * 

<seznam>




<kontrola>
<vytvořit>Přidat položku</vytvořit>

<create string="Přidat poznámku" context="{'default_type': 'note'}"/>
</control>
</list>

.. poznámka::
Použití prvku control dává smysl pouze v případě, že seznam je uvnitř
:třída :class:`~odoo.fields.One2many` nebo :class:`~odoo.fields.Many2many`. Pokud je vytvořený prvek
je definována, přepsává výchozí tlačítko „Přidat řádek“.

.. odkaz/výhled architektury/vyhledávání:

Hledání
======

Výhledy pro vyhledávání jsou odlišné od ostatních typů výhledu v tom, že nejsou používány k zobrazení obsahu.
Přestože se vztahují k určitému modelu, používají se ke filtrování obsahu jiného pohledu (obvykle
souhrnné pohledy, např.:
:ref:`reference/view_architectures/graph`.

Kořenovým prvkem vyhledávacích pohledů je „vyhledat“.

Nemá žádné atributy.

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * – ... obrázek: view_architectures/search.svg
:align: střed

      * 

<hledani>
                 ...


.. odkaz/výhled architektury/vyhledávání/komponenty:

Součásti
----------

Vyhledávací pohled přijímá následující dětské prvky:
<odkaz/výpis architektur/hledání/pole>`, :ref:`filtr
<odkaz/výhled architektur/vyhledávání/filtr>, :ref:"oddělovač
<odkaz/zobrazit architektury/hledat/oddělovač>, :ref:`skupina
<odkaz/zobrazit architektury/hledat/skupina> a :ref:`přístupový panel
<odkaz na architekturu/vyhledávání/vyhledávací panel>.

Zástupné znaky jsou označeny velkými písmeny.

.. odkaz/výhled architektury/vyhledávání/pole:

„pole“: filtr podle hodnoty pole
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Element „pole“ definuje domény nebo kontexty s uživatelsky zadanými hodnotami. Při vyhledávání se
generované pole domén se spojí s filtry pomocí operátoru AND.

... blok kódu::xml

<hledání>
<pole název pole/>


Atributy prvku „pole“ jsou následující:

.. atribut: jméno
:noindex:

Jméno pole, na které se má filtrovat.

:požadavek:Povinné
:typ: str

... zahrnuje: architektury/pole_atributu_string.rst

.. atribut:: operátor
:noindex:

Výchozí vlastnost pole je tvořit domény ve tvaru :samp:`[(name, {operator}, value)]`, kde „name“
je název pole a „hodnota“ je hodnota poskytnutá uživatelem, možná filtrovaná nebo
transformovány (např. uživatel je očekáván výběr hodnoty pole s *značkou*, nikoliv samotnou hodnotu).
hodnota samotná).

Atribut „operátor“ umožňuje přepsat výchozí operátor, který závisí na typu pole.
typ (např. „=“ pro pole s plovoucí desetinnou čárkou, ale „like“ pro pole s pevnou desetinnou čárkou a „child_of“ pro mnoho2jedna).

:volitelné
:typ: str
:default: „=“

.. atribut:: filtr_doména
:noindex:

Doména používaná jako vyhledávací doména pole, jako výraz v Pythonu, který se vyhodnotí na
:ref:`doménu <reference/orm/domains>`.

Může použít proměnnou self k vložení hodnoty, kterou poskytla do vlastního doménového jména.
aby vytvářely výrazně více flexibilní domény než při použití atributu „operátor“ samotného o sobě (například
(hledání v několika polích najednou).

Pokud jsou oba atributy „operátor“ a „filtr domény“ poskytnuty, pak „filtr domény“ má přednost.
přednost.

:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:default: `[]`

.. atribut: kontext
:noindex:

Kontext sloučit do kontextu zobrazení vyhledávání, jako je Python
výraz, který vyhodnocuje na seznamu.

Může obsahovat hodnoty poskytnuté uživatelem, které jsou k dispozici v proměnné self.

:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:výchozí hodnota: `{}`

.. atribut:: doména
:noindex:

Filtry, které se mají použít k výsledkům doplňování pro pole umožňující automatické doplnění (např.
:třída:`~odoo.fields.Many2one`).

:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:default: `[]`

... zahrnuje: view_architectures/generic_attribute_groups.rst

... zahrnují: view_architectures/generic_attribute_invisible.rst

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * — ... obrázek: view_architectures/search_field.svg
:align: střed

      * 

<hledani>


<field name="měna_id"/>



.. odkaz/výhled architektury/vyhledávání/filtr:

`filtr`: vytvořit předdefinované filtry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „filtr“ se používá k vytvoření předdefinovaných filtrů, které lze přepínat ve zobrazení vyhledávání.
Umožňuje přidávat do vyhledávacího kontextu data:dfn:kontext, který je předán datovému pohledu
vyhledávání, filtrování nebo přidávání nových sekcí do vyhledávacího filtru.

... blok kódu::xml

<hledání>
<filtr typu="LABEL" doménou="DOMAIN"/>


Atributy prvku „filtr“ mohou být následující:

.. atribut: jméno
:noindex:

Technické označení filtru. Může se použít k :ref:`zapnutí výchozího stavu
<reference/view_architectures/search/defaults> nebo jako :ref:`dědičný háček
<odkaz/zobrazit záznamy/dědičnost>.

:požadavek:Povinné
:typ: str

.. atribut: řetězec
:noindex:

Štítek filtru.

:požadavek:Povinné
:typ: str

.. atribut: pomoc
:noindex:

Nápověda, která se zobrazí při najetí kurzorem na filtr.

:volitelné
:typ: str
:default: „“

.. atribut:: doména
:noindex:

Doména, kterou je třeba přidat k doméně akce jako součást vyhledávací domény.

:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:default: `[]`

.. atribut:: datum
:noindex:

Název pole typu „datum“ nebo „datum a čas“, na které se má filtrovat.

Při použití této vlastnosti se vytvoří sada filtrů dostupných ve podmenu.
:guilabel:`Filtry“ nabídka. Filtry jsou časově závislé, ale ne dynamické v tom smyslu, že
že jejich domény jsou hodnoceny při instanci kontrolního panelu.

...... příklad::
... kódový blok::xml

<filtr typu="datum vytvoření" jméno="filtr_vytvoreni_data" datum="vytvoreni_data"/>

Výchozí filtry obsahují vyhledávací pole s různými podfiltry, které vám umožní filtrovat dle měsíců, čtvrtletí a let.
Dále můžete vytvářet vlastní podfiltry, které umožňují filtrovat na základě domén.
Tyto vlastní filtry musí mít následující atributy: „název“, „řetězec“ a „doména“.

...... příklad::
... kódový blok::xml

<filtr typu="Datum vytvoření" název="filter_create_date" datum="create_date">
<filter name="create_date_last_30_days" string="Posledních 30 dní" domain="[('create_date', '>', datetime.datetime.combine(context_today() - relativedelta(days=30), datetime.time(23, 59, 59)).to_utc())]"/>
</filtr>

Poznámka: Všechny vlastní filtry definované touto cestou jsou navzájem vylučující a také s ostatními podfiltry.

:volitelné
:typ: str
:default: „“

.. atribut:: start_month
:noindex:

Nejranější měsíc, který se objeví v roletce filtru data jako odchylka od aktuálního měsíce.

...... příklad::
... kódový blok::xml

<filtr typu="Datum vytvoření" název="filter_create_date" datum="create_date" měsíc_začátek="-3"/>

Pokud je aktuální měsíc únor, nejstarším měsícem v rozevíracím seznamu bude listopad.

:volitelné
:typ: int
:default: "-2"
:rozsah:Filtry s neprázdným atributem „datum“

.. atribut:: konec_měsíce
:noindex:

Poslední měsíc, který se objeví v roletce filtru data jako odstupný měsíc oproti aktuálnímu měsíci.

...... příklad::
... kódový blok::xml

<filtr typu="Datum vytvoření" jméno="filter_create_date" datum="create_date" konec_měsíce="2"/>

Pokud je aktuální měsíc únor, poslední měsíc v rozevíracím seznamu bude březen.

:volitelné
:typ: int
:default: „0“
:rozsah:Filtry s neprázdným atributem „datum“

.. atribut:: start_year
:noindex:

Nejstarší rok, který se objeví v roletce filtru data jako odchylka od aktuálního roku.

...... příklad::
... kódový blok::xml



Pokud je aktuální rok 2024, nejdříve vybíratelný rok v rozevíracím seznamu bude 2021.

:volitelné
:typ: int
:default: "-2"
:rozsah:Filtry s neprázdným atributem „datum“

.. atribut:: konec
:noindex:

Nejnovější rok, který se objeví v roletce filtru data jako odstup od aktuálního roku.

...... příklad::
... kódový blok::xml

<filtr řetězec="Datum vytvoření" název="filter_create_date" datum="create_date" konec_rok="2"/>

Pokud je aktuální rok 2024, poslední rokem v seznamu bude 2025.

:volitelné
:typ: int
:default: „0“
:rozsah:Filtry s neprázdným atributem „datum“

.. atribut: default_period
:noindex:

Výchozí doba filtru na základě času (s atributem date). Musí být jedním z následujících nebo
oddělený čárkami seznam platných filtrů.

Platné filtrační ID zahrnují následující:

   - „první čtvrtina“, „druhá čtvrtina“, „třetí čtvrtina“ a „čtvrtá čtvrtina“.
   - Jedna z „měsíc“, „měsíc-x“ a „měsíc+x“, kde x je nečisté celočíselné hodnoty mezi startovním měsícem a koncovým měsícem.
   - Jedno z „rok“, „rok-x“ a „rok + x“, kde „x“ je celé číslo mezi „start_year“ a „end_year“.
   - Jméno libovolného vlastního filtru definovaného uvnitř filtru, předpona „custom_“.

Filtr musí být ve výchozím nastavení filtrů aktivovaných při inicializaci pohledu.

...... příklad::
... kódový blok::xml

<filtr typu="datum vytvoření" název="filtr_create_date" datum="create_date" výchozí období="rok,měsíc-1"/>

...... příklad::
... kódový blok::xml

<filtr název="filtr_create_date" datum="create_date" výchozí období="custom_create_date_last_30_days">
<filter name="create_date_last_30_days" string="Posledních 30 dní" domain="[('create_date', '>', datetime.datetime.combine(context_today() - relativedelta(days=30), datetime.time(23, 59, 59)).to_utc())]"/>
</filtr>

:volitelné
:typ: str
:výchozí hodnota: „měsíc“, nebo nejbližší hodnota k aktuálnímu měsíci, pokud je tato hodnota nedostupná
:rozsah:Filtry s neprázdným atributem „datum“

... zahrnují: view_architectures/generic_attribute_invisible.rst

... zahrnuje: view_architectures/generic_attribute_groups.rst

.. atribut: kontext
:noindex:

Kontext se sloučil s doménou akce, aby vytvořil vyhledávací doménu.

Klíč kontextu s hodnotou pole může být použit k definování skupiny dostupné v
nabídka „Skupit podle“ nebo „Filtr“. Pokud je pole typu „datum“ nebo „datum a čas“, filtr
generuje podmenu nabídky :guilabel:`Skupina po“ s následujícími možnostmi
dostupné: :guilabel:`Rok`, :guilabel:`Čtvrtletí“, :guilabel:`Měsíc“, :guilabel:`Týden“
:guilabel:`Den“. Když filtr používáte v základním nastavení aktivovaných filtrů ve výhledu
inicializace jsou záznamy automaticky seskupeny podle měsíce. Toto lze změnit použitím
Syntaxe „datumové pole: intervál“.

...... příklad::
... kódový blok::xml

<filtr typu="kategorie" název="skupina_podle_kategorie" kontext={'skupit podle': 'id kategorie'}/>
<filtr typu="Vytvořeno" jméno="groupby_create_date" kontext="{'group_by': 'create_date:week'}"/>

....... poznámka::
Výsledky funkce read_groups, která jsou seskupeny podle pole, mohou být ovlivněny jejím parametrem group_expand.
atribut, který umožňuje zobrazit prázdné skupiny v případě potřeby. Pro více informací se podívejte na
:třída:~odoo.fields.Field

:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:výchozí hodnota: `{}`

.. upozornění:
Řetězce filtrů (bez nefiltrujících prvků je oddělujícím) jsou považovány za vzájemně obsahující.
kompozitní: budou se skládat pomocí operátoru „nebo“ místo obvyklého „a“.

...... příklad::
... kódový blok::xml

<filtr doménou="([('stát', '==', 'návrh')])"/>
<filtr doménou="([('stav', '=', 'hotovo')])"/>

Zobrazují se záznamy, jejichž pole „stav“ je nastaveno na hodnotu „návrh“ nebo „hotovo“.

...... příklad::
... kódový blok::xml

<filtr doménou="([('stát', '==', 'návrh')])"/>

<filtr doménou="([('zpoždění', '<', 15)])"/>

Záznamy, jejichž pole „stav“ je nastaveno na hodnotu „návrh“ a zároveň pole „zpoždění“ je menší než 15.

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * 
:align: střed

      * 

<hledani>





.. odkaz/výhled architektury/vyhledávání/oddělovač:

`separátor`: oddělit skupiny filtrů
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „separátor“ slouží k oddělení skupin filtrů.
v jednoduchých vyhledávacích pohledech. V komplexnějších vyhledávacích pohledech
:ref:`skupina <reference/view_architectures/search/group>` je doporučena.

... blok kódu::xml

<hledání>
<FILTRY/>
<separator/>
<FILTRY/>


Atributy může přijímat pouze prvku „separátor“.

.. odkaz/výhled architektury/vyhledávání/skupina:

„skupina“: oddělené skupiny filtrů
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „skupina“ se používá k oddělení skupin filtrů.
v přeplněných vyhledávacích pohledech. V jednodušších vyhledávacích pohledech
může být nahrazeno prvkem :ref:`oddělovačem <reference/view_architectures/search/group>`.

... blok kódu::xml

<hledání>
<skupina>
<FILTRY/>
</skupina>


Prvek „skupina“ nemá žádné atributy.

.. _reference/view_architectures/search/searchpanel:

`searchpanel`: Zobrazit vyhledávací panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „searchpanel“ zobrazuje vyhledávací lištu vlevo od vícezáznamových pohledů. Umožňuje
rychle filtrovat data na základě zadaných polí.

... blok kódu::xml

<hledání>
<vyhledávací panel>
<POLE/>
</vyhledávací panel>


Elemenet „vyhledávací panel“ přijímá pouze dětské prvky „pole“.

Element „pole“ použitý jako podřízený prvek elementu „vyhledávací panel“ může mít následující
atributy:

.. atribut: jméno
:noindex:

Jméno pole, na které se má filtrovat.

:požadavek:Povinné
:typ: str

... zahrnuje: architektury/pole_atributu_string.rst

.. atribut:: vybrat
:noindex:

Chování a zobrazení pole. Může mít dvě různé hodnoty:

...... atribut: jeden


Maximálně lze vybrat jednu hodnotu. Podporované typy polí jsou „many2one“ a „selection“.

...... atribut:: multi


Je možné vybrat více hodnot. Podporované typy polí jsou „many2one“, „many2many“ a
„výběr“.

:volitelné
:typ: str
:default: „jeden“

... zahrnuje: view_architectures/generic_attribute_groups.rst

.. atribut: ikonka
:noindex:

Ikona hřiště.

:volitelné
:typ: str
:default: „“

.. atribut: barva
:noindex:

Barva hřiště.

:volitelné
:typ: str
:default: „“

Když má atribut „select=one“, může mít následující další
atributy:

.. atribut:: hierarchizovat
:noindex:

Zda dětské kategorie mají být pod nadřazenou kategorii nebo na stejné hierarchické úrovni
úrovni.

:volitelné
:typ: bool
:default: „Pravda“
:rozsah: :třída:`~odoo.fields.many2one` pole

Pokud má prvek „pole“ nastaveno atributy „select=multi“, může mít následující další
atributy:

... atribut::enable_counters
:noindex:

Pokud jsou počítadla zaznamenaných hodnot vypočítána a zobrazena, pokud nejsou nulová.

......tip:
Toto atributy existuje, aby se zabránilo dopadu na výkon. Další způsob, jak řešit výkonnost
problém je v přehlcení metod search_panel_select_range a search_panel_select_multi_range
metody.

:volitelné
:typ: bool
:výchozí hodnota: „Pravda“

.. atribut:: rozbalit
:noindex:

Zda se mají zobrazovat kategorie a filtry, které nemají žádné záznamy.

:volitelné
:typ: bool
:výchozí hodnota: „Pravda“

.. atribut: limit
:noindex:

Maximální počet hodnot, které lze pro pole získat. Pokud je dosaženo limitu, nejsou žádné
zobrazené na vyhledávacím panelu a místo chybové hlášky se zobrazí výsledek vyhledávání. Pokud je nastavená na nulu, všechny hodnoty
vyzvednout.

:volitelné
:typ: int
:default: 200

.. atribut:: doména
:noindex:

Podmínky, které musí splňovat rekordy.

...... příklad::
... kódový blok::xml

<vyhledavacislovicek>
<pole název="oddělení_id"/>
<položka jméno="manažer_id" vybírat="více" doména="[('oddělení_id', '==', oddělení_id)]"/>
</vyhledávací panel>

:volitelné
:typ: :ref:`Pythonový výraz <reference/view_architectures/python_expression>`
:default: `[]`

.. atribut:: groupby
:noindex:

Název pole, podle kterého se mají hodnoty seskupit.

:volitelné
:typ: str
:default: „“
:rozsah: pole :class:`~odoo.fields.Many2one` a :class:`~odoo.fields.Many2many`

.. _reference/architektury/hledat/výchozí:

Výchozí vyhledávání
---------------

Hledané pole a filtry lze konfigurovat pomocí akce „kontext“
:samp:`search_default_{name}` klíčů. Hodnota musí být hodnotou, kterou chceme nastavit poli.
filtry musí být buď logická hodnota nebo číslo.

Příklad:
S proměnnou pole „foo“ a filtrem „bar“ bude následující kontext akce hledat „foo“.
„acro“ a „bar“ zobrazit vždy:

... kódový blok:: python

      {
:'search_default_foo': 'acro'
'vyhledávací lišta': 1
      }

Numerická hodnota (mezi 1 a 99) může být použita k určení pořadí výchozích filtrů *by group*.

Příklad:
S filtry „foo“ a „bar“, které jsou vlastně skupinovými filtry, se následně načte akční kontext.
„bar“, pak „foo“.

... kódový blok:: python

      {
:'search_default_foo': 2
'vyhledávací lišta': 1
      }

.. reference/vzory/kanban:

Kanban
======

Názory kanbanu se používají jako „kanbanová tabule <https://cs.wikipedia.org/wiki/Kanbanová_tabule>“
Vizualizace: zobrazují záznamy jako „karty“, polovinou cesty mezi seznamem
<odkaz/zobrazení architektur/seznam> a <odkaz/zobrazení architektur/formulář>.

Záznamy mohou být seskupeny do sloupců pro použití v vizualizaci nebo ovládání průběhu pracovního postupu (např. úkoly nebo
správu průběhu prací) nebo nezařazené (pouze pro vizualizaci záznamů).

Kořenovým prvkem kanbanových pohledů je „kanban“.

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * – ... obrázek: view_architectures/kanban.svg
:align: střed

      * 

<kanban>
                 ...
</kanban>

.. poznámka::
Kanban zobrazuje náklad a maximálně deset sloupců. Každý další sloupec je uzavřený, ale může být znovu otevřen.
Stále je možné otevřít uživatelem.

.. odkaz/zobrazení architektury/Kanban/kořen:

Kořenové atributy
---------------

Povinné atributy lze přidat do kořenového prvku kanban, aby bylo možné zobrazit pohled podle potřeby.

... zahrnuje: view_architectures/root_attribute_string.rst

... zahrnuje: view_architectures/root_attribute_create.rst

... zahrnuje soubor: view_architectures/root_attribute_edit.rst

... zahrnuje: view_architectures/root_attribute_delete.rst

... zahrnují: view_architectures/root_attribute_default_group_by.rst

... zahrnuje: :: view_architectures/root_attribute_default_order.rst

.. atribut: třída
:noindex:

Přidejte třídy HTML do kořenového HTML prvku v pohledu.

:volitelné
:typ: str
:default: „“

.. atributy: příklady
:noindex:

Klíč v registru příkladů KanbanExamplesRegistry, který je možné procházet při tvorbě nového
sloupec v skupinovém zobrazení kanbanu.

......viz také::
„Použití příkladu v modulu utm
<{GITHUB_PATH}/addons/utm/static/src/js/utm_campaign_kanban_examples.js>

:volitelné
:typ: str
:default: „“

.. atribut: skupina_vytvorit
:noindex:

Zda je viditelná lišta „Přidat novou sloupec“.

:volitelné
:typ: bool
:default: „Pravda“

.. atribut: skupina_smazat
:noindex:

Zda lze sloupce odstranit pomocí nabídky Nastavení.

:volitelné
:typ: bool
:default: „Pravda“

.. atribut:: skupina_uprav
:noindex:

Zda lze sloupce upravovat v nabídce Nastavení.

:volitelné
:typ: bool
:default: „Pravda“

.. atribut: skupiny_přesouvatelné
:noindex:

Zda lze sloupce přeskládat.

:volitelné
:typ: bool
:default: „Pravda“

.. atribut:: records_draggable
:noindex:

Zda lze při skupinovém zobrazení kanbanu přetahovat záznamy.

:volitelné
:typ: bool
:default: „Pravda“

.. atribut::archivovatelný
:noindex:

Zda záznamy patřící do sloupce lze archivovat a rozbalit, když je pole aktivní
definované na modelech.

:volitelné
:typ: bool
:default: „Pravda“

.. atribut:: rychlé vytvoření
:noindex:

Zda by mělo být možné vytvářet záznamy bez přepínání do zobrazení formuláře.

:volitelné
:typ: bool
:výchozí hodnota: „Pravda“, pokud je v kanbanovém pohledu seskupeno mnoho2jedno, výběr, znak nebo logická pole
jinak je „Pravda“

.. atribut: rychlé vytvoření pohledu
:noindex:

Odkaz na formulář zobrazení architektury v sekci „Formuláře“ se otevře při použití
rychlé vytváření záznamů.

:volitelné
:typ: str
:default: „“

... atribut::on_create
:noindex:

Akce, kterou se má spustit při kliknutí na tlačítko „Vytvořit“.

Pokud je nastaven na hodnotu „quick_create“, místo toho se používá rychlé vytváření záznamů. Pokud je rychlé vytváření
Pokud je funkce vypnutá, je spuštěna standardní akce pro vytváření.

:volitelné
:typ: str
:default: „“

.. atribut:: může_otevřít
:noindex:

Výchozí chování je takové, že po kliknutí na kartu kanbanu se zobrazí příslušný záznam v podobě formuláře.
Toto chování lze vypnout nastavením atributu `can_open` na hodnotu `False`.

:volitelné
:typ: bool
:default: „Pravda“

.. atribut: zvýraznění barvy
:noindex:

Název pole typu Integer používaného k vybarvení levého okraje kartiček Kanban.

:volitelné
:typ: str

... zahrnuje: view_architectures/root_attribute_sample.rst

.. _reference/view_architectures/kanban/components:

Součásti
----------

Kanban přijímá následující děti prvky: :ref:` šablony
<odkaz na architekturu/výhled kanban/šablony>`, :ref:"pole
<odkaz/zobrazení architektury kanban/hlavička>, :ref:"hlavička
<odkaz/zobrazení architektury kanban/hlavička>`, :ref:`postupová lišta
<odkaz/zobrazení architektury/kanban/postupová lišta>.

... reference/viz-architektury/kanban/šablony:

`šablony“: definujte strukturu karet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „šablony“ se používá k definování šablon QWeb, které strukturují
Kanban karty.

Definice struktury karty může být rozdělena do několika šablon pro lepší přehlednost, ale alespoň
musí být definován jeden základní šablonový soubor „karta“.

Můžete definovat další šablonu: menu. Pokud je definována, zobrazí se v rozbalovacím menu
jejíž se dá dosáhnout pomocí vertikální elipsy ( :guilabel:`⋮`) v pravém horním rohu karty.

Šablony jsou napsané v jazyce :ref:`JavaScript QWeb <reference/qweb/javascript>`.

... blok kódu::xml

<kanban>
<šablony>
<t t-name="karta">
<pole název/>
</t>



.. varování:

Tyto šablony jsou vytvořeny pomocí QWeb, nikoli šablonami Owl (<https://github.com/odoo/owl>), což znamená, že
Příkazy typu „t-on-click“ nejsou k dispozici.

Pole
******

V rámci těchto šablon lze použít prvek „field“, který umožňuje zobrazit pole. Může mít následující
atributy:

... zahrnuje: view_architectures/field_attribute_name.rst

Výchozí nastavení je takové, že pole jsou nahrazena tagem span obsahujícím jejich formátovanou hodnotu.
Pokud je specifikován atribut „widget“, pak jejich zobrazení a chování závisí na
odpovídající widget. Hodnota atributu widget může být různá, včetně:

...... atribut::handle
:noindex:

Povoluje přesouvání záznamů pomocí tahání a pustění myší, používající příslušné pole jako pořadí.

...... atribut:: barvy_kanbanu
:noindex:

Povoluje úpravu barvy pole (celé číslo). Kombinováno s kořenovým atributem `highlight_color`.
umožňuje upravit barvu karet.

Podívejte se na část :ref:`Výstup <reference/js/widgets>`, abyste zjistili
různé widgety a jejich možnosti.

Kontext renderování
*****************

Šablony kanbanu, které jsou vykreslovány pomocí motoru QWeb (viz reference/qweb/javascript), mají
*kontext renderování*, sada proměnných v šablonách obsahující užitečné informace
a nástroje. Tady jsou dostupné proměnné:

.. atribut: rekord
:noindex:

Objekt, který obsahuje všechny pole definovaná v pohledu. Každé pole má dvě atributy: `value`
a „raw_value“. První je formátován podle aktuálních parametrů uživatele, zatímco druhý
je neupravená hodnota (například ID pole mnoho k jednomu). Tento objekt je užitečný například pro
používání hodnot polí v podmínkách t-if. Pro zobrazení doporučujeme používat
tagu pole.

...... příklad::
... kódový blok::xml

<kanban>
<šablony>
<pole název="je_firma" />
<t t-name="karta">


</t>

</kanban>

.. atribut: widget
:noindex:

Objekt s dvěma klíči definujícími dostupné akce pro uživatele:

   - „editovatelné“: pravda, pokud uživatel může upravovat záznamy, nebo nepravda.
   - „smazatelné“: pravda, pokud uživatel může smazat záznamy, jinak nepravda.

Toto je užitečné pro podmíněné zobrazení prvků, které vyžadují konkrétní přístupová práva.

...... příklad::
... kódový blok::xml

<kanban>
<šablony>
<t t-name="karta">

</t>
<t t-name="menu">

</t>

</kanban>

.. atribut: kontext
:noindex:

Aktuální kontext se šíří buď z akce, která otevírá kanbanový pohled, nebo z jedno-málo.
nebo pole mnoho-k-mnoho, které vloží kanbanový pohled do formuláře.

... atribut:: čtení
:noindex:

Ukazuje, že je pohled čtenářský.

:typ: bool

.. atribut:: výběr
:noindex:

Zda se při výběru pole mnoho k jednomu nebo mnoho k mnoha zobrazí kanbanový pohled.
(prostředí).

:typ: bool

.. atribut::luxon
:noindex:

objektu „luxon“ <https://moment.github.io/luxon/api-docs/index.html>
manipulovat s hodnotami dat a času.

.. atribut: JSON
:noindex:

Javascriptová knihovna JSON <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON>
objekt jména prostoru, který obsahuje metodu „parse“, která umožňuje převádět hodnoty políček JSON do JavaScriptu
Předměty.

Tlačítka a odkazy
*****************

Zatímco většina šablon kanban je standardními QWeb šablonami:ref:`<reference/qweb>`, kanban
tlačítka a odkazy s atributem „type“ jsou zvláštní způsob.
vykonávat jiné operace než jejich standardní funkce v HTML. Atribut „type“ může mít hodnotu
hodnoty „akce“ a „objektu“ tlačítka :ref:`<reference/view_architectures/list/button>“.
nebo následující hodnoty:

.... atribut: otevřený
:noindex:

Kliknutím na prvek se zobrazí záznam karty v podobě formuláře.

.... atribut::delete
:noindex:

Kliknutím na prvek se smaže záznam karty a odstraní se karta.

.. atribut:: archiv
:noindex:

Kliknutím na prvek se archivuje záznam karty a odstraní se karta.

.. atribut: unarchive
:noindex:

Kliknutím na prvek se archivuje záznam karty a odstraní se karta.

.. atribut: set_cover
:noindex:

Kliknutím na prvek se zobrazí dialogové okno pro výběr obrázku, který bude sloužit jako obrázek pokrytí záznamu.

Widgety
*******

Prvek „widget“ umožňuje vložit dynamicky generovaný (v JavaScriptu) HTML do karet.
má povinný atribut „name“, který odkazuje na implementaci v JavaScriptu (komponenta Owl).
registrovaný do registru „view_widgets“.

...: dokumentovat widgety pro zobrazení a standardní widgety

Podívejte se na část :ref:`Widget <reference/javascript_reference/view_widgets>`, abyste objevili různé
widgety a jejich možnosti.

Sestavy
*******

Několik karetových rozložení lze snadno získat pomocí běžných HTML prvků a „Bootstrap utility
třídami <https://getbootstrap.com/docs/5.0/utilities/api/>`_. Výchozí třída je `flexbox
obal <https://developer.mozilla.org/cs/docs/Web/CSS/Flexibilní_boxový_layout/Základní_pojmy_flexboxu>
s řádkovým směrem.

Příklad:
... kódový blok :: XML

<kanban>
<šablony>
<t t-name="karta">
<field class="fw-bold fs-5" name="display_name"/>
<položka třídy text-muted s názvem "parent_id"/>
<položka jméno="tag_ids" widget="many2many_tags"/>

</šablony>
</kanban>

Element HTML „footer“ je nastaven tak, aby se přilepil na spodní část karty, a funguje jako flexbox
obal s směrem řádku, který umožňuje snadno zobrazit několik polí na stejné lince.

Příklad:
... kódový blok :: XML

<kanban>
<šablony>
<t t-name="karta">
<field class="fw-bold fs-5" name="display_name"/>
<položka třídy text-muted s názvem "parent_id"/>
<položka jméno="tag_ids" widget="many2many_tags"/>
<footer>




</šablony>
</kanban>

Pro zobrazení některého obsahu, například obrázku, na straně karty lze použít tagy „aside“ a „main“.
elementy s třídou „flex-row“ na kartě. Hlavní element je flexboxový kontejner podobný
karta je, když není „výstřel“.

Příklad:
... kódový blok :: XML

<kanban>
<šablony>
<t t-name="card" class="flex-row">
<aside>

</odstavec>
<hlavní třída="ms-2">
<field class="fw-bold fs-5" name="display_name"/>



<položka jméno="priority" widget="priority"/>
<field class="ms-auto" name="activity_ids" widget="kanban_activity"/>

</hlavní>

</šablony>
</kanban>

..tip:
Příjmení třídy „o-kanban-aside-full“ nastavené na prvek „aside“ odstraňuje mezeru, takže
obrázek se rozšíří na okraj karty.

... reference/view_architectures/kanban/field:

`pole`: deklarujte další pole pro čtení
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Element „pole“ může být také použit mimo šablony kanbanu:ref:`template
<odkaz/zobrazení architektury/kanban/šablony>. V tomto případě umožňuje deklarovat pole, která jsou
nejsou zobrazeny na kartě, ale přesto je nutné je stáhnout, například proto, že se jejich hodnota používá
v podmínce „pokud“.

Příklad:
... kódový blok :: XML

<kanban>
<šablony>
<pole název="je_firma"/>
<t t-name="karta">
<pole název/>
<field t-if="!record.is_company.raw_value" name="parent_id">

</šablony>
</kanban>

.. _reference/view_architectures/kanban/header:

„Hlavička“: Zobrazení tlačítek v ovládacím panelu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „hlavička“ se používá k vložení vlastních tlačítek do ovládacího panelu.

... blok kódu::xml

<kanban>
<hlavička>
         ...

      ...


Element „hlavička“ přijímá pouze děti v podobě tlačítka, stejně jako u :ref:`seznamového výpisu tlačítek`.
Elementy tlačítek pro zobrazení architektur.

Element „tlačítko“ použitý jako potomek elementu „hlavička“ může mít následující
Další atributy:

.. atribut:: zobrazit
:noindex:

Zobrazovací režim tlačítka. Může mít dvě různá hodnota:

...... atribut:: zobrazit


Tlačítko se zobrazí pouze v případě, že jsou vybrány nějaké záznamy; jejich akce se vztahuje na
vybrané záznamy.


...... atribut:: vždy


Tlačítko je vždy zobrazeno, i když nejsou vybírány žádné záznamy.

.... důležité::
:Pouze zobrazení režimu vždy je k dispozici, protože není možné vybírat záznamy
v kanbanovém pohledu.

...... příklad::
... kódový blok::xml

<hlavička>
<tlačítko jméno="vždy zobrazit" typ="objekt" řetězec="Vždy zobrazeno" zobrazení="vždy"/>
<tlačítko typu="objekt" název="vyberToDo" výchozí hodnota="Zobrazeno při výběru"/></button>
</hlavička>

:volitelné
:typ: str
:default: „zobrazit“

.. odkaz/zobrazení architektury/Kanban/pokročilá nabídka:

`progressbar`: Zobrazení průběžných čar nad sloupci
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prvek „progressbar“ se používá k definování průběžného indikátoru, který se zobrazuje nad sloupci kanbanu.
skupinové zobrazení kanbanu.

... blok kódu::xml

<kanban>
<pokročilý-průběh-výpočtu field="POZNÁMKA K POLOŽCE"/>
       ...


Element „progressbar“ může mít následující atributy:

.. atribut: pole
:noindex:

Název pole, které obsahuje podskupiny průběžného posuvníku.
Jsou založeny na tom, že...

:požadavek:Povinné
:typ: str

.. atribut: barvy
:noindex:

Přidělování hodnot pole pro postupovou lištu k hodnotám barev „mute“, „success“ a „warning“.
a „nebezpečí“.

:požadavek:Povinné
:typ: JSON


.. atribut: sum_field
:noindex:

Název pole pro použití v součtu zobrazeném vedle pruhu s postupem. Pokud není nastaveno, celkový
Ve výchozím nastavení se zobrazuje počet záznamů.

:volitelné
:typ: str
:default: „“

.. varování: Možná struktura a zobrazení jejího vykreslování

...... seznamová tabulka::
:třída: o-showcase-table

      * 
:align: střed

      * 

<kanban>

barvy="{'plánované': 'úspěch', 'dnes': 'varování', 'předčasné': 'nebezpečí'"

<šablony>
                     ...

</kanban>

.. vše::
  - CSS specifické pro kanban
  - kanbanové struktury widgetů (výřez, podrobnosti, ...).

… VŠECHNY NÍŽE UVEDENÉ POHLEDY JEŠTĚ NEBYLY PŘEVEDENY NA NOVOU REFERENČNÍ DOKUMENTAČNÍ FORMÁTOVANOU

.. odkaz/výhled architektury/QWeb:

QWeb
====

Výchozí pohled na QWeb je :ref:`reference/qweb` šablona vložená do pohledu.
„arch“. Nemají konkrétní kořenový prvek. Protože QWebové zobrazení nemá
musí mít specifický kořenový prvek a jejich typ musí být explicitně uveden (může
Nemělo by se odvozovat z kořenového prvku pole „arch“.

QWeb má dvě použití:

* Mohou být použity jako šablony pro přední části, v takovém případě
:ref:`reference/data/vzorový soubor` by měl být použit jako zkratka.
* Mohou být použity jako skutečné QWeb názory (otevřené v akci), ve kterých
pokud by měly být definovány jako běžný pohled s explicitním „typem“ (v
a model.

Hlavní přírůstky k základnímu qweb-as-template jsou v qweb-as-view:

* qweb-as-view má zvláštní případ pro „<nav>“ prvek, který nese CSS
třída „o_qweb_cp_buttons“: její obsah by měly být tlačítka a bude
extrahovány a přesunuty do oblasti tlačítek na panelu ovládání, „<nav>“ samotné
bude odstraněna, což je obcházení problému s názvy ovládacích panelů, které neexistují.
přesto
* qweb-as-view renderování přidává několik položek k standardnímu renderování qwebu
kontext:

... první třídy: o definice seznamu

„model“
model, ke kterému je vázán pohled QWeb
„doména“
doména poskytovaná vyhledávacím pohledem
„kontext“
kontext nabízený v pohledu na vyhledávání
„záznamy“
nebojíte se, že vám někdo přečte vaše poštovní schránky.
chceme iterovat záznamy a ne provádět složitější operace
(např. seskupování)
* qweb-as-view také poskytuje další způsoby zobrazení:

  - „_qweb_prepare_context(view_id, doména)“ připraví kontext pro zobrazení
specifické pro qweb-as-view
  - Metoda „qweb_render_view(view_id, doména)“ je volána klientem
a zavolá metody přípravy kontextu a nakonec
„env['ir.qweb'].render()“.

.. odkaz/zobrazení architektury/graf:

Graf
=====

Grafický pohled se používá k vizualizaci agregací nad určitým počtem záznamů nebo
záznamové skupiny. Její základní prvek je „<graph>“, který může obsahovat následující
atributy:

.. první třídy: o definice

„typ“ (volitelné)
jeden z „bar“, „pie“ a „line“, typ grafu, který se má použít

„skládaný“ (volitelné)
používá se pouze pro „sloupcový“ graf. Při nastavení na hodnotu 0 zabráníte tomu, aby se v rámci skupiny zobrazovaly sloupce.
aby se na něj dalo dát.

„disable_linking“ (volitelné)
nastaveno na hodnotu „1“, aby se zabránilo přesměrování kliknutí na graf do zobrazení seznamu.

„příkaz“ (volitelné)
pokud je nastaveno, hodnoty osy X budou seřazeny podle jejich měřítka výchozí
V případě, že je v pořadí dána priorita („ASC“ nebo „DESC“), používá se jen pro „bar“.
„koláčové“ grafy.

„string“ (volitelné)
text zobrazený v navigačním panelu při přepnutí na seznamový pohled.

... zahrnuje: view_architectures/root_attribute_sample.rst

Jediným povoleným prvkem v grafickém zobrazení je „pole“, které může mít
sledujícími atributy:

.. první třídy: o definice

„jméno“ (povinné)
název pole, které chcete použít v pohledu. Pokud se používá pro seskupování
než agregace

„neviditelný“ (volitelné)
Pokud by se tak skutečně stalo, pole nebude obsaženo ani v aktivních opatřeních,
měřitelné parametry.

„typ“ (volitelné)
pokud je nastaveno na „měřit“, pole se použije jako agregovaná hodnota v
skupina místo kritéria pro seskupování. Funguje pouze u posledního pole
s tímto atributem, ale je užitečný i pro jiné pole s atributem řetězec.


„interval“ (volitelné)
na pole datum a čas, skupinuje podle zadaného intervalu („den“,
„týden“, „měsíc“, „čtvrtletí“ nebo „rok“ namísto skupinování podle
Specifický datum a čas (s konstantním rozlišením sekundy nebo dne).
Výchozí je „měsíc“.

„string“ (volitelné)
je používán jen u pole s atributem „type=“ measure “.
zobrazí pole v grafickém zobrazení, přebije výchozí funkci stringu v Pythonu
atribut pole.

Měření jsou automaticky vygenerována z polí modelu; pouze
Používají se agregovatelné pole, které jsou také abecedně řazené.
seřazené podle pole řetězce.

.. varování:

grafické agregace se provádí na obsahu databáze, nikoliv na uložených datech.
funkční pole nelze použít v grafických zobrazeních


V grafických zobrazeních může „pole“ obsahovat atribut „widget“, který určuje jeho formát.
Widget by měl být pole formátoru, jehož nejzajímavější jsou
„plovoucí“ a „peněžní“.

... blok kódu::xml

<položka jméno="pracovní hodiny - zavírací doba" widget="float_time"/>

.. odkaz/zobrazení architektury/pivot:

Pivot
=====

Pohled na sestavu se používá k vizualizaci agregací jako tabulka s „převrácenými“ sloupci.
element je „<pivot>“ s následujícími atributy:

.. první třídy: o definice

„disable_linking“ (volitelné)
Položku nastavte na „1“, aby se odstranily odkazy v buňkách tabulky na zobrazení seznamu.
„display_quantity“ (volitelné)
Při nastavení na „1“ se zobrazí sloupec Množství výrobku.
„default_order“ (volitelné)
Název měřítka a řazení (vzestupně nebo sestupně), které se má použít jako výchozí
v pohledu.



<pivot výchozí řazení="foo vzestupně">
<pole název="foo" typ="měřítko"/>
</sloupcovém grafu>

Jediným povoleným prvkem v rámci pohledu Pivot je „pole“, které může obsahovat
sledujícími atributy:

.. první třídy: o definice

„jméno“ (povinné)
název pole, které chcete použít v pohledu. Pokud se používá pro seskupování
než agregace

„string“ (volitelné)
jméno, které se bude používat k zobrazení pole v rozbalovacím pohledu.
přebírá výchozí atribut pole String v Pythonu.

„typ“ (volitelné)
Ukazuje, zda pole slouží jako kritérium pro seskupení nebo jako
agregovaná hodnota v rámci skupiny. Možné hodnoty jsou:

... první třídy: o definice seznamu

„řádek“ (výchozí hodnota).
Skupiny jsou seskupeny podle zadaného pole a každá skupina dostane svou vlastní řádku.
„kol“
Vytváří skupiny sloupcového typu
„měřit“
pole pro agregaci v rámci skupiny
„Interval“
na pole datum a čas, skupinuje podle zadaného intervalu („den“,
„týden“, „měsíc“, „čtvrtletí“ nebo „rok“ namísto skupinování podle
datum a čas (s rozlišením na sekundy) nebo datum (s rozlišením na den).

„neviditelný“ (volitelné)
jestliže je pravdivá, pole se neobjeví ani v aktivních opatřeních.
v selektivních měřítkách (užitečné pro pole, která nemají smysl agregovat).
např. pole v různých jednotkách (např. € a $)

... zahrnuje: view_architectures/root_attribute_sample.rst

Měření jsou automaticky vygenerována z polí modelu; pouze
Používají se agregovatelné pole, které jsou také abecedně řazené.
seřazené podle pole řetězce.

.. varování:

jako grafické zobrazení, tak i agregace dat na obsah databáze
což znamená, že funkční pole, která nejsou uložená, nelze používat v rozbalovacích pohledech


V pohledu Pivot lze „pole“ vybavit atributem „widget“, který určuje jeho formát.
Widget by měl být pole formátoru, jehož nejzajímavější jsou
„datum“, „čas“, „plovoucí čas“ a „peněžní“.

Příkladem může být třeba následující pohled na časovou osu:

<sloupcový řádek Timesheet>
<sloupce jméno="zaměstnanec_id" typ="řádek"/>
<položka jméno="datum" interval="měsíc" typ="sloupec"/>



.. odkaz/zobrazení architektury/kalendář:

Kalendář
========

Kalendářové zobrazení ukazuje záznamy jako události v denním, týdenním, měsíčním nebo ročním
kalendář.

.. poznámka: Výchozí kalendář bude zobrazen kolem aktuální data
(dnes). Můžete předat kontextu akce specifické datum.
abyste mohli nastavit počáteční zaměření kalendáře na období (viz režim).
datum (klíčový kontext pro použití je initial_date)

Jejich základním prvkem je „<kalendář>“. K dispozici jsou atributy
kalendářovým zobrazením jsou:


řetězec (výchozí hodnota je „““)

Tento název okna se zobrazí pouze v případě, že otevřete akci bez názvu.
jejíž cílem je „nový“ (otevření dialogu).

Vytvořit:
bool(výchozí hodnota: „Pravda“)

Zapněte nebo vypněte tvorbu záznamů na pohledu.

Edit:
bool(výchozí hodnota: „Pravda“)

Zapněte nebo vypněte nahrávání na pohledu.

:delete:
bool(výchozí hodnota: „Pravda“)

Vyberte možnost „Zakázat/povolit smazání záznamu“ v sekci Akce.

.. první třídy: o definice

„datum začátku“ (povinné pole)
název pole záznamu, které obsahuje datum začátku události
„datum zastavení“
název pole záznamu obsahující datum ukončení události.
„datum_zastavení“ je poskytnuto, pokud se záznamy stane možným přesunout pomocí „přetáhněte a pusťte“.
přímo v kalendáři
„date_delay“
alternativou k „date_stop“ je „duration“, která poskytuje délku události místo
datum ukončení (jednotka: den)
„barva“
název pole záznamu, které bude použito pro segmentaci barev. Záznamy v
stejné barvy jsou přiřazeny stejným odstínům v kalendáři.
barvy jsou přidělovány polosnadno.
Zobrazil jméno/avatar viditelného záznamu v bočním panelu
„form_view_id“
zobrazit, když uživatel vytváří nebo upravuje událost. Poznámka: pokud je tento atribut nastaven na hodnotu true,
Pokud není nastaveno, kalendářový pohled se vrátí k ID formuláře.
aktuální akce, pokud nějaká je.
„event_open_popup“
Pokud je nastavena možnost event_open_popup na hodnotu true, pak se v kalendářním pohledu zobrazí
otevřít události (nebo záznamy) v dialogovém okně FormViewDialog. Jinak se otevře událost
v novém pohledu na formulář (s funkcí do_action)
„rychlé vytvoření“
umožňuje rychlé vytváření událostí na kliknutí: požádá uživatele pouze o „název“
(kde se tato hodnota ukládá, lze ovládat prostřednictvím
„rec_name“ a pokusí se vytvořit nový události s pouze tímto a kliknutým.
události. Pokud selže rychlé vytvoření, vrátí se do plného režimu dialogu
„rychle vytvořit id pro zobrazení“
Při nastavení atributu „quick_create“ a vytvoření uživatelem se zobrazí
událost místo výchozího dialogu.
„vytvořit pole jména“
název pole záznamu obsahujícího textovou reprezentaci záznamu.
to se používá při vytváření záznamů prostřednictvím „rychlého vytvoření“.
„celý den“
jméno logického pole v záznamu, které ukazuje na to, zda odpovídající
událost je označena jako celodenní (a délka nehraje roli)
„móda“
Výchozí zobrazení kalendáře při načítání.
Případné atributy jsou: „den“, „týden“, „měsíc“ a „rok“.
„škály“
Seznam oddělených čárkami měřítek, které mají být poskytnuty. Výchozím nastavením jsou všechny měřítka.
dostupné. Podívejte se na režim pro možné hodnoty stupnice.
„vytvořit“, „smazat“
umožňuje vypnout příslušnou akci ve výhledu nastavením
příslušný atribut na hodnotu „false“
„<pole>“
deklaruje pole pro agregaci nebo použití v logice kanbanu. Pokud je
Jen je zobrazeny v kalendářních kartách.

Pole mohou mít další atributy:

... první třídy: o definice seznamu

„neviditelný“
použít „Pravda“ k skrytí hodnoty na kartách
„avatar_field“
pouze pro pole x2many, aby se místo jména zobrazovalo avatar.
v kartách
„write_model“, „write_field“ a „filter_field“.
můžete přidat filtr a uložit výsledek do definovaného modelu.
filtr se přidá do bočního panelu. „Filter_field“ je volitelný a umožňuje
Vyžaduje, abyste specifikovali pole, které bude obsahovat stav filtru.
„filtry“ a „barva“.
použijte „Pravda“ pro přidání pole filtru v bočním panelu. Můžete specifikovat
pole „barva“ slouží k barevné úpravě zaškrtávacího políčka.


Model Common
-------------

...současný modul: odoo.addons.base.models.ir_ui_view
...autoatribut::Model._datum_jmeno
:noindex:

.. odkaz/zobrazení architektury/aktivita:

Aktivita
========

Výhled aktivit slouží k zobrazení činností spojených s záznamy.
Data jsou zobrazena v grafu, kde záznamy tvoří řádky a aktivita
vkládá sloupce. První buňka každé řady zobrazuje (upravitelnou, viz
„šablony“, velmi podobně jako :ref:`reference/view_architectures/kanban`) kartu reprezentující
odpovídající záznam. Když na ostatní buňky kliknete, zobrazí se podrobnější popis.
zobrazuje se všechna aktivita stejného typu v rekordu.

.. varování:

Zobrazení aktivit je k dispozici pouze tehdy, pokud je nainstalován modul „e-mail“.
a pro modely, které dědí z „mail.activity.mixin“.

Kořenovým prvkem v pohledu „Aktivita“ je „<activity>“, přijímá následující
atributy:

.. první třídy: o definice

„string“ (povinné)
Název, který by měl popsat pohled

Možné děti prvku View jsou:

.. první třídy: o definice

„pole“
deklaruje pole, které má být použito v aktivitě *logika*. Pokud je pole jen zobrazeno
V aktivitách není nutné ji předem deklarovat.

Možné atributy jsou:

... první třídy: o definice seznamu

„jméno“ (povinné)
název pole, ze kterého se má vytáhnout

„šablony“
definuje šablony pro reference a QWeb. Definice karet může být
rozdělit na více šablon pro lepší čitelnost, ale v případě zobrazení aktivit je nutné definovat
má alespoň jeden základní šablonový vzor „aktivita-box“, který se zobrazí jednou pro každou
rekord.

Ve výchozím nastavení používá aktivní pohled převážně standardního javascriptového QWebu.
a poskytuje následující proměnné kontextu
viz reference/zobrazit architektury/kanban pro více informací.

... první třídy: o definice seznamu

„widget“
:js:class:`ActivityRecord` lze použít k získání některých
metainformace. Tyto metody jsou k dispozici také přímo v
šablonovém kontextu a nemusí se přistupovat pomocí „widget“.
„rekord“
objekt, který má všechny požadované pole jako atributy. Každý prvek má
dvě atributy „hodnota“ a „neupravená hodnota“.

.. odkaz/výhled architektury/kohorta:

Kohorta
======

.. neupravený::html

<span class="badge" style="background-color:#AD5E99">Funkce pro podniky</span>

Kohortový pohled se používá k zobrazení a porozumění tomu, jak některá data mění.
doba. Například představte si, že pro daný obchod jsou klienti
se přihlásit k nějaké službě. Potom lze v kohortním pohledu zobrazit celkový počet
z každého předplatného měsíčně a studovat rychlost odchodu klientů z služby
(obrat) Když kliknete na buňku, zobrazí se vám nová akce.
v níž uvidíte pouze záznamy, které se nacházejí v časovém rozmezí buňky.
Tato akce obsahuje seznamový a formulářový pohled.

.. poznámka: Výchozí nastavení kohorty používá stejné seznam a formulářové zobrazení jako
definované na akci. Můžete předat seznamový nebo formulářový pohled.
do kontextu akce, aby se nastavily/přepsaly pohledy, které budou
použít (klíče kontextu, které mají být použity, jsou form_view_id a list_view_id)

Například zde je velmi jednoduchý pohled na kohortu:

... blok kódu::xml



Kořenový prvek v pohledu na kohortu je <cohort> a přijímá následující
atributy:

.. první třídy: o definice

„string“ (povinné)
Název, který by měl popsat pohled

„datum začátku“ (povinné)
Platné datum nebo časové pole. Toto pole je prohlížečem chápáno jako datum nebo čas.
začátek záznamu

„datum_konce“ (povinné)
Platné datum nebo časové pole. Toto pole je prohlížečem chápáno jako datum nebo čas.
datum ukončení rekordu. To je pole, které určí míru odlivu.

„disable_linking“ (volitelné)
Při hodnotě „1“ se nebudou kliknutí na buňky sestav přesměrovávat do zobrazení seznamu.

„režim“ (volitelné)
Řetězec popisující režim. Měl by být buď „churn“ nebo
„zadržení“ (výchozí hodnota). Režim odlivu začíná na 0 % a postupně se zvyšuje.
V případě udržení se sazba bude pohybovat kolem 100 % a postupně klesat.

„časová osa“ (volitelné)
Řetězec popisující časovou osu. Měl by být buď „vpřed“ nebo „vzad“ (výchozí hodnota).
Timeline vpřed bude zobrazovat data od data_start do data_stop, zatímco zpětné datumové čáry
bude zobrazovat data od date_stop do date_start (když je date_start v budoucnosti / větší
než datum_konec.

„interval“ (volitelné)
Řetězec popisující časový úsek. Měl by být „den“, „týden“, „měsíc“.
(výchozí hodnota) nebo 'rok'.

„měření“ (volitelné)
Pole, které lze agregovat. Toto pole bude použito k výpočtu hodnot.
pro každou buňku. Pokud není nastaveno, v pohledu na kohortu se počítá počet výskytů.

„<pole>“ (volitelné)
umožňuje specifikovat konkrétní pole pro jeho správu z dostupných měření.
hlavním účelem je skrýt pole z vybíratelných měření:

... první třídy: o definice seznamu

„jméno“ (povinné)
název pole, které se má použít ve výhledu.
„string“ (volitelné)
jméno, které se bude zobrazovat v pohledu na kohortu, převezme přednost před
výchozí atribut pole pro typ String v Pythonu.
„neviditelný“ (volitelné)
pokud je pravdivá, pole se neobjeví ani v aktivních opatřeních, ani ve volitelných.
metriky (vhodné pro pole, která nemají smysl agregovaná, například pole v různých
jednotky (např. € a $).
Pokud je hodnota doménou, doména se vyhodnocuje v kontextu aktuální řádky.
rekord, pokud je odpovídající vlastnost nastavena na buňce.
„widget“ (volitelné)
alternativní zobrazení pole.

... zahrnuje: view_architectures/root_attribute_sample.rst

.. odkaz/výhled architektury/síť:

Síť
====

.. neupravený::html

<span class="badge" style="background-color:#AD5E99">Funkce pro podniky</span>

Omezení
-----------

Tento pohled je v procesu dokončení, může být rozšířen nebo upraven.

* byly testovány pouze sloupce „datum“ a „výběr“, „mnoho2jedna“.
jsou jen formálně implementovány a podporovány, ale nebyly testovány.
„datum a čas“ není implementován vůbec.
* Sloupcové buňky jsou těžko konfigurovatelné a musí být numerické
* Výchozí nastavení zakazuje automatickou korekci buněk a musí být konfigurováno, aby bylo povoleno.
* „Vytvořit“, „Upravit“ a „Smazat“ metadat ACL se automaticky neaktualizuje
nastaven na základní pohled z důvodu omezení v „fields_view_get“
postprocesing (je pevně daný seznam výhledů, které jsou podporovány)
(těchto vlastností).

Schema
------

Vlastní schéma a další ověření je v tomto modulu pro zobrazení sítě.
Architektura je:

„<síťka>“
architektonický kořenový prvek

    * povinný atribut „string“
    * volitelné atributy „vytvořit“, „upravit“ a „smazat“.
    * volitelné atributy „upravit“ a „upravit_jméno“.

„Vyrovnání“ může být buď „objekt“ nebo „akce“, aby bylo možné určit
zda se má provádět přizpůsobení buňky metodou volání
nebo provedení akce. Metoda „adjust_name“ poskytuje odpovídající metodu
jméno a ID akce.

V obou případech jsou k dispozici parametry přizpůsobení.
„souřadnice“ člena kontextu v případě „objektu“, parametry
jsou také poskytovány jako parametry funkce (vedle prázdné
seznam id):

„řádková doména“
doména shodná s celou řádkou upraveného buňky
„sloupec_pole“
název sloupce pro upravenou buňku
„hodnota sloupce“
hodnota sloupce pro upravenou buňku
„celočíselný pole“
plocha měřítka upravené buňky
„změna“
rozdíl mezi starou hodnotou buňky a upravenou.
Může být kladná nebo záporná.

    * volitelné atributy „skrýt celkovou částku řádku“ a „skrýt celkovou částku sloupce“

„skrýt celkové číslo řádku“
nastavit na pravdu, aby se skryla celá řádka (výchozí hodnota je false)
„skrýt celkové číslo“
nastavit na pravdu, aby se skryl celkový sloupec (výchozí hodnota je false)

    * volitelný atribut „barchart_total“

„barchart_total“
nastavit na „pravdu“, aby se zobrazila grafická osa pod tabulkou, která je založena na
celkové hodnoty sloupců (výchozí hodnota je false).

    * volitelné atributy „create_inline“ a „display_empty“

„create_inline“
nastavit na „pravdu“, aby se zobrazila další řádka v dolní části sítě.
„Přidat řádek“ tlačítko (výchozí hodnota „false“). Když je nastaveno na „true“, „Přidat řádek“ tlačítko
z ovládacího panelu je skrytý. Když nejsou k dispozici žádné informace a když je nastaveno
není nastaveno (takže se zobrazí nápověda), tlačítko „Přidat řádek“ z nabídky
na obrazovce se zobrazuje ovládací panel, aby uživatel mohl vytvořit první záznam.
„pouze_prázdné“
nastavit na „pravdu“, aby se mřížka zobrazovala i bez dat (výchozí hodnota je „false“).
Při tomto nastavení je uživatel schopen sledovat aktuální období (jako datum).
V záhlaví sloupců jsou zobrazeny (jako připomínka - pokud nejsou žádné hodnoty a tento stav je aktivní).
Pokud není atribut nastaven, místo sítě se zobrazí nápověda.

„<tlačítko>“ (0+)
Běžné tlačítka pro akce v pohledu hlavy

    * povinný atribut „string“ (popisek tlačítka)
    * povinný atribut „typ“, buď „objekt“ nebo „akce“.

.. poznámka: tlačítka pro práci s pracovním postupem nejsou podporována

    * povinný atribut „jméno“, buď název metody nebo
identifikátor akce, kterou chcete provést
    * volitelný „kontext“

Serverový zpětný volání je poskytován se všemi ID záznamů zobrazených v
buď jako ID předané metodě („objekt“ tlačítko), nebo
kontextu „aktivní ID“ („tlačítka pro akci“)

„<řádek>“ (1+)
Sloupcové pole „Skupina“ bude nahrazeno filtrem skupiny z pohledu vyhledávání
pokud vůbec existují.

Pořadí polí „řádek“ ve vzhledu určuje jejich hloubku seskupení:
pokud první pole je „škola“ a druhé „věk“, pak záznamy
Budeme je seskupovat podle „školy“ a v rámci každé školy podle „věku“.

„<pole typu="sloupec">“ (1)
Sloupec pro seskupení polí.

Kolonka "col" může obsahovat 0 nebo více prvků „<range>“ s uvedením
nastavitelné sloupcové rozsahy. „Rozsah“ prvky mají následující
povinné atributy

"jméno"
Může být použito k přehrání výchozího rozsahu (první výchozí).
přes kontext „grid_range“
„struna“
přepínač zobrazení rozsahu (viditelný uživateli)
„span“
symbolické jméno pro celou řadu sloupců, která se zobrazí najednou.
zobrazení může vyvolat stránkování.

Pro pole „datum“ jsou aktuálně platná rozmezí „týden“ a „měsíc“.
„krok“
symbolické jméno kroku mezi jednou sloupcovou hodnotou a předchozí/následující

Pro pole „datum“ je aktuálně jediný platný rozsah „den“.
„<pole typu „měření“>“ (1)
Políčko buňky, automaticky sčítané (pomocí „read_group“).

Pole měření může obsahovat atribut „widget“, který umožňuje jeho
zobrazit.

Interakce serveru
-------------------

Kromě volitelných tlačítek má sada zobrazení mřížky nyní k dispozici dvě metody:

* Funkce „read_grid“ (poskytovaná na všech modelech modulovým rozhraním) vrací téměř
celé obsahy sítě jako dikta:

  * Názvy sloupců jsou seznam slovníků s následujícími klíči:

„hodnoty“ (povinné)
Toto odpovídá slovníku s klíčem na každém poli „řádku“, hodnoty jsou
Vždy ve tvaru „[hodnota, název]“.
„doména“ (povinný parametr)
doménu jakéhokoliv záznamu v řádku zdroje této sloupcové hlavičky.
Je nutné kopírovat záznamy při přizpůsobování buněk.

  * Názvy sloupců je seznam slovníků s alespoň jedním klíčovým slovem:

„hodnoty“ (povinné)
viz hodnoty nadpisu řádku
„doména“ (povinný parametr)
viz hodnota domény sloupce
„současný“ (volitelné)
logická hodnota, označuje sloupec

  * mřížová data jako seznam řádků, každý z nich je seznamem buněk a každá buňka je slovníkem
s následujícími klíči:

„hodnota“
numerická hodnota spojená s buňkou
„doména“
doména shodná s záznamy buňky (předpokládejme, že je neprůhledná)
„velikost“
počet záznamů v buňce
„čtení pouze“ (volitelné)
pravdivá hodnota, která ukazuje na konkrétní buňku.
upravitelný klientem
„třídy“ (volitelné)
a seznam tříd (jako řetězců), které chcete přidat na obal buňky (mezi
buňka (buňku TD a potenciálně editovatelný prvek v buňce).

Pokud dojde k konfliktu mezi tímto seznamem a základními třídami (předponou
Pokud je v seznamu tříd zadána hodnota (např. „o_grid_cell_“), jsou ignorovány všechny ostatní třídy.

Pozor, že sítě jsou husté, pokud dotazování databáze nevyvolá žádný výsledek.
Skupina, která se shoduje s buňkou, vygeneruje prázdnou buňku s výchozími hodnotami.
hodnoty pro požadované klíče.
  * „prev“ a „next“, které mohou být buď falešné (žádné číslování stránek), nebo
do vlastního kontextu zobrazení, aby se „četlo“ do mřížky.
předchozí nebo další stránku, mělo by se předpokládat, že je neprůhledná

* „read_grid_domain(pole, rozsah)“ (poskytované všemi modely v rámci modulu).
Vrací doménu shodnou s aktuálně konfigurovaným „pásmem“ mřížky.
Také je prováděno interně funkcí „read_grid“, ale může být užitečné nebo nutné.
volat nezávisle, např. s odděleným „search_count“.
„čtení skupiny“.

* „upravit sítě“, které ještě nemají univerzální implementaci
a jejich semantika se pravděpodobně bude vyvíjet v čase a s případy použití.

Serverové háčky
------------

Funkce „read_grid“ vyvolává řadu háčků, které umožňují přizpůsobit její chování.
operace z uvnitř bez nutnosti přepsání celého metodu:

„_grid_formát_buňku(skupina, pole buňky)“
převádí výstup z read_group (skupina-po-skupině) na buňky v
formát popsaný výše (součástí „sítě dat“).
„_grid_make_empty_cell(řádek_domény, sloupec_domény, pohled_domény)“
generuje prázdnou verzi buňky (pokud neexistuje odpovídající skupina).
„_grid_column_info(název, rozsah)“
generuje objekt ColumnMetadata na základě typu sloupce a ukládá hodnoty
buď se vrátí přímo (jako součást funkce „read_grid“) nebo se použije dotaz.
převést „read_group“ na „read_grid“:

„skupina“
skutečné pole/dotaz pro sloupce
„doména“
doménu, na kterou se má použít „čtená skupina“ v případě sloupce pole.
případně může být prázdný
„prev“ a „next“.
kontextové segmenty, které budou předány funkci „read_grid“ pro stránky.
a po této aktuální. Pokud je „false“, vypne se stránkování v tom
směr
„hodnoty“
hodnoty sloupců zobrazit na „aktuální stránce“, každá hodnota je
slovník s následujícími klíči:

„hodnoty“
slovník mapující pole na hodnoty pro celou sloupcovou hodnotu
obvykle jenom „jméno“ -> hodnota
„doména“
doménové shody s konkrétní sloupcovou hodnotou
„je aktuální“
„Pravda“ pokud by měla být aktuální sloupec zvýrazněn
případně „Pravda“, jinak „Falešná“
„formát“
jak formátovat hodnoty sloupce/typů z „read_group“
formátování na formát „číst_síť“ (shodný s hodnotami v
ColumnInfo

ACL
---

* Pokud není viditelná oblast editovatelná, jednotlivé buňky nebudou editovatelné.
* Pokud není pohled vytvářen, tlačítko „Přidat řádek“ nebude
zobrazena (v současné době vytváří nový prázdný záznam).

Kontextové klíče
------------

„rozsah sítě“
vybírá, která rozsahová oblast má být použita výchozím způsobem, pokud je v pohledu více
rozsahy
„přídavná hmotnost“
pokud je to možné, používá se jako výchozí kotva sloupcových rozsahů místo
takové, jaké „read_grid“ definuje jako výchozí.

Pro pole datum se používá jako referenční datum okolo kterého bude
vypočítána. Výchozí datumové kotvy je „dnes“ (v časovém pásmu uživatele).

.. _reference/view_architectures/gantt:

Ganttova diagram
=====

.. neupravený::html

<span class="badge" style="background-color:#AD5E99">Funkce pro podniky</span>

Ganttovy grafy správně zobrazují Ganttovy diagramy (pro plánování).

Kořenovým prvkem pro pohledy Gantt je „<gantt/>“, nemá žádné děti, ale
Vyberte následující atributy:


řetězec (výchozí hodnota je „““)

Tento název okna se zobrazí pouze v případě, že otevřete akci bez názvu.
jejíž cílem je „nový“ (otevření dialogu).

Vytvořit:
bool(výchozí hodnota: „Pravda“)

Zapněte nebo vypněte tvorbu záznamů na pohledu.

Edit:
bool(výchozí hodnota: „Pravda“)

Zapněte nebo vypněte nahrávání na pohledu.

:delete:
bool(výchozí hodnota: „Pravda“)

Vyberte možnost „Zakázat/povolit smazání záznamu“ v sekci Akce.

.. první třídy: o definice

„datum začátku“ (povinné pole)
název pole, které poskytuje datum a čas začátku události pro každou
rekord.
„datum_konec“ (povinné)
název pole, které poskytuje konečnou dobu trvání události pro každou
rekord.
„závislostní pole“
název pole „many2many“, které poskytuje závislost mezi dvěma záznamy.
Pokud se B odvozuje z A, „závislostní pole“ je pole, které umožňuje získat A
z B. Oba tyto pole a pole „dependency_inverted_field“ se používají k
spojit pilulky a přesunout je na jiné místo.
„výchozí pole závislosti“ (povinné, pokud je „pole závislosti“ zadáno)
název pole „many2many“, které poskytuje obrácenou závislost
„závislostní pole“. Pokud B závisí na A, „pole obrácené závislosti“ je
pole, které umožňuje získat hodnotu B ze hodnoty A.
„barva“
název pole používaného k vybarvení pilulek podle jejich hodnoty
„Výzdoba - {$name}“
„Pythonový výraz“, který vyhodnotí na hodnotu „pravda“

umožňuje změnit styl textu buňky podle odpovídající hodnoty
atributy záznamu.

„{$name}“ může být jedním z následujících „barvy pro kontext bootstrap“ („nebezpečí“,
„info“, „sekundární“, „úspěch“ nebo „varování“.

Definujte podmíněné zobrazení záznamu v řádku ve stylu textu na základě odpovídajícího
atributy záznamu.

Hodnoty jsou Pythonové výrazy. Pro každý záznam je vyhodnocen příslušný výraz.
se vlastnostmi alba jako kontextovými hodnotami a pokud je „pravda“,
V případě, že se použije odpovídající styl, je na řádku aplikována tato hodnota. Níže jsou uvedeny další možné hodnoty
k dispozici v kontextu:

  * „uid“: ID aktuálního uživatele
  * „dnes“: aktuální místní datum ve tvaru „YYYY-MM-DD“.
  * „nyní“: stejné jako „dnes“ s přidáním aktuální doby.
Toto číslo je formátováno jako „YYYY-MM-DD hh:mm:ss“.



<gantt dekorace-info="stav == 'návrh'"
dekorace-nebezpečí="stát == 'potřebuji pomoc'"
dekorace-bf="stavy == 'zaneprázdněno'"
      ...

„default_group_by“
název pole pro seskupování úkolů
„disable_drag_drop“
pokud je nastaveno na pravdu, v grafickém zobrazení Ganttu nebude podpora přetahování.
„konzolidační“
jméno pole, ve kterém se zobrazí součet hodnoty v buňce záznamu
„konsolidace_max“
slovořadí s klíčem ve sloupci „Group by“ a maximální agregací.
hodnota, která se zobrazí před červeným zvýrazněním buňky

„konzolidační vyloučení“
název pole, které popisuje, zda úkol má být vyloučen
z konsolidace
pokud je nastaveno na hodnotu true, zobrazí se pruhovaná oblast v konzolidační čáře
„vytvořit“, „buňka_vytvořit“, „upravit“, „smazat“, „plán“
umožňuje provést příslušnou akci v pohledu nastavením
příslušný atribut na „false“ (výchozí hodnota je „true“).

    * „Vytvořit“: Pokud je povoleno, bude k dispozici tlačítko „Přidat“.
panel pro vytváření záznamů.
    * „cell_create“: Pokud je povoleno „create“ a „cell_create“, tlačítko „**+**“ se zobrazí.
zobrazeno při přejetí myší nad buňkou časového slotu, aby se vytvořil nový záznam na tomto slotu.
    * „upravit“: Pokud je povoleno, otevřené záznamy budou ve stavu pro úpravy (tedy upravitelné).
    * „plán“: Pokud je povoleno „upravit“ a „zobrazit“, bude zobrazen tlačítko „lupa“.
na časové intervaly, kde se neplánované záznamy přidávají do tohoto časového intervalu.

...... příklad::

Pokud nechcete vytvářet záznamy na Ganttových diagramu a začátku a konci
datum je nutné zadat do modelu, plánování by mělo být vypnuté
protože nikdy nebude nalezena žádná stopa.
„kompenzace“
Podle velikosti stupnice je nutné k dnešnímu počtu přičíst různý počet jednotek
výchozí období. Příklady: Offset +1 v týdnu default_scale otevře
ganttovský pohled na příští týden a v přednastavené škále měsíců se otevře
Ganttovo zobrazení dvouměsíční historie.
„postup“
název pole poskytujícího procento dokončení události záznamu.
mezi 0 a 100
„struna“
název grafického pohledu
„Přesnost“
Objekt JSON, který specifikuje přesnost snímání pro každou pilulku na každé váze.

Poznámka: Hodnoty stupně „den“ jsou (výchozí hodnota: „hodina“):

  - „hodina“: zaznamenává časy, které se automaticky přizpůsobí celým hodinám (např. 7:12 se stane 8:00).

  - „hodina: půl“: zaznamenává časy, které se přizpůsobují hodinám a půl (např. 7:12 se stane 7:30).

  - „hodina:čtvrt hodiny“: zaznamenává časy, které se přizpůsobují půlhodinám (např. 7:12 se stane 7:15).

Možné hodnoty měřítka „týden“ jsou (výchozí: „den: polovina“):

  - „den“: záznamy časů se automaticky přizpůsobí celým dnům (např. 7:28 ráno se stane 23:59:59 hodinami předchozího dne, 10:32 večer se stane 12:00 hodinami tohoto dne)

  - „den:půl“: zaznamenává časy, které se přibližují k půlhodinám (např. 7:28 ráno se stane 12:00)

Možné hodnoty měřítka „měsíc“ jsou (výchozí: „den:půl“):

  - „den“: záznamy časů se automaticky přizpůsobí celým dnům (např. 7:28 ráno se stane 23:59:59 hodinami předchozího dne, 10:32 večer se stane 12:00 hodinami tohoto dne)

  - „den:půl“: zaznamenává časy, které se přibližují k půlhodinám (např. 7:28 ráno se stane 12:00)

Velikost „rok“ se vždy přizpůsobí celému dni.

Příklad přesného atributu: „{„den“: „hodina:čtvrtina“, „týden“: „den:půl“, „měsíc“: „den“}“.
„celková řádka“
booleovou hodnotu, která určuje, zda řádek obsahující celkový počet záznamů
bude zobrazeno. (Výchozí hodnota je „false“.)
„složit první úroveň“
Boolean, který určuje, zda je možné každou řadu sbalit při seskupení.
jedno pole. (výchozí hodnota „false“, skládání začíná při seskupování dvou polí).
„zobrazit nedostupnost“
Boolean k označení dat vracených funkcí „gantt_unavailability“.
model je k dispozici uvnitř Ganttova pohledu. Záznamy lze stále naplánovat
v nich, ale jejich nedostupnost je vizuálně zobrazena. (Výchozí hodnota: „false“)
„výchozí měřítko“
výchozí měřítko při zobrazení pohledu. Možné hodnoty jsou (výchozí: „měsíc“):

  * „den“
  * „týden“
  * „měsíc“
  * „rok“

„škály“
seznam povolených měřítek pro tento pohled oddělený čárkou. Výchozí hodnotou je všechny měřítka
Povoleny jsou pouze tyto hodnoty. Pro možné hodnoty měřítka, které lze v tomto seznamu použít, viz „default_scale“.

„šablony“
definuje šablonu „gantt-popover“ používanou pro reference/qweb.
když uživatel přejede myší nad jedním z záznamů v grafu Gantt.

Ganttovský pohled používá převážně standardní :ref:`javascript qweb
a poskytuje následující kontextové proměnné:

... první třídy: o definice seznamu

„widget“
:js:class:`GanttRow“, může být použita k získání některých
metainformace. Metoda „getColor“ sloužící k převodu barevného čísla na barvu
Je také k dispozici přímo v kontextu šablony bez použití widgetu.

„on_create“
Pokud je při kliknutí na tlačítko „Přidat“ v zobrazení vybráno místo otevření obecného dialogu spuštění akce klienta.
tento by měl obsahovat identifikátor XML (např.: „na_vytvoření = % (můj_modul.můj_průvodce) d “

„form_view_id“
zobrazení, které se zobrazí při vytváření nebo úpravě záznamu. Poznámka: Pokud je tato vlastnost nastavena,
Pokud není nastaveno, grafické zobrazení Ganttu se vrátí k ID formuláře.
aktuální akce, pokud nějaká je.

„dynamický rozsah“
pokud je nastaveno na hodnotu true, grafické zobrazení začíná u prvního záznamu.
a ne od začátku roku/měsíce/dne.

„Štítek na pilulku“
Pokud je nastaveno na hodnotu true, čas se zobrazí v nálepce pilulky při nastavení stupnice na týden nebo měsíc.
„7:00 ráno – 11:00 dopoledne (4 hodiny) – úkol 1 v DST“

„miniaturní obrázky“
Tímto způsobem se zobrazí náhled vedle názvu skupiny, pokud je skupina vztahovým polem.
Očekává se pythonový seznam klíčů, které jsou názvy polí na aktuálním modelu.
Hodnoty jsou názvy pole, které obsahuje náhled na příbuzný objekt.

Příklad: úkoly mají pole user_id, které odkazuje na uživatele. Model res.users má pole image, které obsahuje profilovou fotografii.
Pak:



<gantt
start_datum="start_datum"
date_stop="date_stop"
náhledy="{'user_id': 'obrázek 128'}"
      >


Zobrazí uživatelské avatary vedle jména, pokud jsou uživatelé seskupeni podle ID uživatele.

... zahrnuje: view_architectures/root_attribute_sample.rst

.. odkaz/výhled architektury/mapa:

Mapa
===

.. neupravený::html

<span class="badge" style="background-color:#AD5E99">Funkce pro podniky</span>

Tento pohled umožňuje zobrazit záznamy na mapě a trasu mezi nimi. Záznamy jsou reprezentovány špendlíky. Dále také umožňuje vizualizaci polí modelu v okně, které je spojeno s pinem daného záznamu.

.. poznámka::

Model, na který je aplikována tato sada pohledu, by měl obsahovat pole mnoho1no „res.partner“ a pole „res.partner“ by mělo obsahovat pole adresy a souřadnic, protože seznam záznamů je založen na poli „res.partner“.

API
---

Aplikace využívá API služby pro zpracování dat o poloze, aby získala dlaždice (zadní plán mapy), prováděla geoforwarding (převod adres na soubor souřadnic) a stahovala trasy.
Tato funkce využívá dvě rozhraní API, OpenStreetMap a MapBox. Výchozím nastavením je použito OpenStreetMap, které umožňuje zobrazit „tile“_ a provádět „geoforwarding“_. Toto rozhraní nevyžaduje token.
Jakmile je v obecných nastaveních poskytnut platný „MapBox“_ token, přepne se pohled na MapBox API. Toto API je rychlejší a umožňuje výpočet trasy. Token lze získat přihlášením do MapBox.

Strukturální součásti
---------------------

Kořenovým prvkem pohledu je „<map>“. Může mít následující atributy:


.. první třídy: o definice

„res_partner“
Obsahuje pole res.partner, které je typu many2one. Pokud není zadáno, vytvoří se prázdný objekt.
„Výchozí řazení“
Pokud je pole zadáno, pohled přebije výchozí řazení modelu. Pole musí být součástí modelu, na který se pohled aplikuje, nikoli z „res.partner“.
„routování“
Pokud je zadáno číslo 1, zobrazí se trasy mezi záznamy. Zobrazení vyžaduje platný token MapBox a alespoň dva umístěné záznamy (tj. záznamy mají vlastnost partner many2one a partner má adresu nebo platná souřadnice).
„skrýt_jméno“
zda skrýt jméno u bodu v poppupu (výchozí hodnota je „0“).
„skrýt adresu“
zda skrýt adresu v okně pro pin (výchozí hodnota: 0).
„skrýt_nadpis“
zobrazit titulek v seznamu nálepek (výchozí hodnota: „0“).
„Panel“
Zobrazovaný řetězec jako název seznamu pinu. Pokud není zadán, je název akce nebo „položky“ v případě, že se nejedná o akci.
„limit“
Maximální počet záznamů, které se mají zobrazit (výchozí hodnota je „80“). Musí jít o kladné celé číslo.

„<map>“ může obsahovat více „<field>“ prvků. Každý „<field>“ prvek je interpretován jako řádek v okně s popiskem bodu. Následující jsou atributy pole:

.. první třídy: o definice

„jméno“
Pole pro zobrazení.
„struna“
Text, který se má zobrazit před obsahem pole. Může sloužit jako popis.

Třeba taková mapka:
... kódový blok :: XML

<map res_partner="partner_id" default_order="date_begin" routing="1" hide_name="1">
<field name="partner_id" string="Jméno zákazníka"/>


.._atribut „přístupový klíč“: https://www.w3.org/TR/html5/editing.html#the-accesskey-attribute
.. „Bootstrap kontextová barva“: https://getbootstrap.com/docs/3.3/components/#available-variations
.. _„Čárkové oddělené hodnoty“: https://cs.wikipedia.org/wiki/Čárkové_oddělené_hodnoty
… „plovoucí“: https://developer.mozilla.org/cs/docs/Web/CSS/float
... „geoforwarding“: https://nominatim.org/release-docs/develop/
.. _HTML_: https://cs.wikipedia.org/wiki/HTML
.._celé číslo: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
.. _klávesová zkratka_: https://cs.wikipedia.org/wiki/Klávesová_zkratka
... „MapBox“: https://docs.mapbox.com/api/
... „Odoo“: https://www.odoo.com/
…_cesta“: https://cs.wikipedia.org/wiki/Path_(počítače)
.. _pivotní tabulka_: https://cs.wikipedia.org/wiki/Pivotní_tabulka
... „Pythonový výraz“: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
.._„relativní cesta“: https://cs.wikipedia.org/wiki/URL
...„registrace“: https://account.mapbox.com/auth/signup/
... „tile“: https://wiki.openstreetmap.org/wiki/Tile_data_server
