===================================
Kapitola 14: Stručná historie QWeb
===================================

Dosud byla grafická úprava našeho modulu nemovitostí spíš omezená.
Přehled je jednoduchý, protože stačí seznam polí. To samé platí
pro formát pohledu: přestože se používají některé značky, jako například „<group>“ nebo „<page>“,
je velmi málo, co se týká návrhu.

Abychom však naší aplikaci dali jedinečný vzhled, je nutné udělat další krok.
další a umět vytvářet nové pohledy. Dále pak i další funkce jako například PDF reporty nebo
Stránky webu potřebují jiný nástroj, který by byl vytvářen s větší flexibilitou: šablonovací motor.

Možná už jste se setkali s existujícími motory, jako je Jinja (Python), ERB (Ruby) nebo
Větvička (PHP). Odoo má svůj vlastní zabudovaný motor: :ref:`reference/qweb`.
QWeb je primární šablonovací engine používaný v Odoo. Jedná se o XML šablonovací engine a
hlavně pro generování fragmentů a stránek ve formátu HTML.

Možná jste již narazili na „kanban board“ v Odoo, kde jsou záznamy
zobrazené v karetním stylu. Takovou podobu si připravíme pro náš modul nemovitostí.

Příklad: Výhled na kanban
===============================

**Poznámka k použití**: dokumentace související s touto tématikou je dostupná na
:ref:`reference/view_architectures/kanban`.

.. poznámka::

**Cíl**: Na konci této části by měla být vytvořena kanbanová vizualizace vlastností:

.. obrázek:: 14_qwebintro/kanban.png
:align: střed
:alt: Zobrazení kanban

V našem realitním systému bychom rádi přidali kanbanový pohled pro zobrazení nemovitostí.
výhledy jsou standardními výhledy Odoo (stejně jako formulářové a seznamové výhledy), ale jejich struktura je mnohem
flexibilní. Skutečností je, že struktura každé karty je směsí prvků formuláře (včetně základních HTML).
a QWeb. Definice kanbanového pohledu je podobná jako definice seznamu a formuláře
výhledy, s výjimkou jejich kořenového prvku „<Kanban>“. V nejjednodušší podobě je kanbanový výhled
vypadá takto:

... blok kódu::xml

<kanban>
<šablony>
<t t-name="kanban-box">







Pojďme si tento příklad rozebrat.

- „<šablony>“: definuje seznam šablon :ref:`reference/qweb`. Pro kanbanové pohledy je nutné
nejméně jeden šablonový vzor „kanban-box“, který se bude zobrazovat jednou pro každý záznam.
- „<t t-name="kanban-box">“: „<t>“ je místo pro vložení příkazů QWeb. V tomto případě
je používán k nastavení „název“ šablony na „kanban-box“.
- „<název pole>“: tento řádek přidá pole „název“ do výstupu.

... cvičení: Vytvořte minimální kanbanovou projekci.

Použijte jednoduchý příklad uvedený níže a vytvořte minimální kanban pro nemovitosti.
jediné pole, které se zobrazí je „jméno“.

Tip: do „zobrazení“ odpovídající položky musíte přidat „kanban“.
„ir.actions.act_window“.

Jakmile je v Kanbanu funkční pohled, můžeme začít s jeho zlepšováním. Pokud chceme zobrazit prvek
podmíněně můžeme použít příkaz „t-if“ (viz odkaz na :ref:`reference/qweb/conditionals`).

... blok kódu::xml

<kanban>
<pole název="stát"/>
<šablony>
<t t-name="kanban-box">


<div t-if="record.state.raw_value === 'new'">
To je nové.






Přidali jsme pár věcí:

- „t-pokud“: „<div>“ je zobrazen, pokud je podmínka pravdivá.
- „rekord“: objekt s veškerými požadovanými atributy jako jeho vlastnostmi. Každý atribut
dvě atributy „hodnota“ a „neupravená hodnota“. První je formátován podle aktuálního
Jedná se o uživatelské parametry a druhá je přímá hodnota z metody čtení modelu.

V předchozím příkladu bylo pole „name“ přidáno do prvku „<templates>“, ale pole „state“
Je mimo něj. Když potřebujeme hodnotu pole, ale nechceme ji zobrazit v pohledu,
Je možné ho přidat mimo „<šablony>“.

...cvičení: Vylepšete pohled na kanban.

Do zobrazení Kanban přidejte následující pole: očekávaná cena, nejlepší cena, prodejní cena a
tagy. Pozor: nejlepší cena se zobrazuje pouze v případě, že dostanete nabídku, zatímco
Prodávající může zobrazit prodejní cenu pouze v případě, že bude nabídka přijata.

Podívejte se na vizuální příklad v části **Cíl**.

Abychom měli konečně hotovo, musíme si ještě udělat pořádek v pohledu: výchozím nastavením se pak všechny vlastnosti zobrazí podle typu.
Můžete se podívat na různé možnosti popsané v
:ref:`reference/view_architectures/kanban`.

... cvičení: Přidat výchozí seskupování.

Použijte vhodný atribut k seskupení vlastností podle typu výchozím způsobem. Musíte také zabránit
přetahování a plošné vkládání.

Podívejte se na vizuální příklad v části **Cíl**.

Kanbanové pohledy jsou příkladem, že vždy je dobré začít od existujícího.
a upravit ji, namísto aby jste začali od nuly. Existuje mnoho možností a tříd
k dispozici, takže čtěte a učte se!

... šablonování:
    https://en.wikipedia.org/wiki/Template_processor
... _kanban board:
    https://en.wikipedia.org/wiki/Kanban_board
