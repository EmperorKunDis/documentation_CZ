=====================
Modelové situace usmíření
=====================

Modelové schéma pro vyrovnání je používáno k automatizaci procesu vyrovnávání bankovních účtů.
Toto je zvláště užitečné při zpracování opakujících se položek, jako jsou například poplatky za bankovní účet.
Může být také užitečná při zpracování slevy na faktuře.

Každý model je vytvořen na základě :ref:`typů modelu <models/types> a :guilabel:`transakce banky
podmínky“.

.. viz též:
   - :doc:`bankovní synchronizace“
   - „Návody k Odoo: Modelová řešení (<https://www.odoo.com/slides/slide/reconciliation-models-6858>).“

..._model/typ:

Typy modelů usmíření
==========================

Modelové konfigurace jsou dostupné po kliknutí na: „Účetnictví“ -> „Konfigurace“.
Banky: Modelové účty. Pro každý modelový účet musí být nastaven typ.
Existují tři typy modelů:

- :guilabel:`Tlačítko pro generování protějšku“: vytvoří se tlačítko v výsledném záznamu
část pohledu na vyrovnání bankovního účtu. Když je kliknutá, tato tlačítko generuje protichůdnou položku
vyrovnat s aktivní transakcí podle pravidel stanovených v modelech.
model určí účet(y) protistrany, částku(y), štítek(y) a analytický údaj.
distribuce.
- :guilabel:`Pravidlo pro navržení protějšku v transakci`: používá se při opakujících se transakcích k shodě
transakci do nové položky na základě podmínek, které musí odpovídat informacím o transakci.
- :guilabel:`Pravidlo pro shodu s fakturami/fakturami“: používá se k opakovaným transakcím, aby se transakce shodovaly
k existujícím fakturám, zálohám nebo platbám podle podmínek, které musí odpovídat informacím na
transakci.

Výchozí modely vyrovnání
=============================

V Odoo jsou k dispozici různé modely podle fiskální lokalizace společnosti.
Tyto mohou být aktualizovány, pokud je potřeba. Uživatelé také mohou vytvářet své vlastní modely slučování kliknutím
:label:Nový.

.. důležité::
Pokud se záznam shoduje s několika rekonstrukcemi, použije se první z nich v pořadí modelů.
je použita, můžete si změnit pořadí tím, že přetáhnete a položíte ukazatel vedle názvu.

.... obrázek::reconciliation_models/list-view.png
:alt:Změnit pořadí modelů v seznamovém zobrazení.

Účtenky v dokonalé shodě
----------------------------

Tento model by měl být na vrcholu seznamu modelů, protože umožňuje Odoo navrhnout shodné
faktury nebo fakturace s bankovním převodem podle stanovených podmínek.

.. obrázek:rekonstrukce_modelu/faktury-a-prijmy-v-pohode.png
:alt:Nastavte pravidla, která vyvolají sjednocení.

Odoo automaticky vyrovnává platbu při výběru možnosti „Automatické ověření“ a
Podmínky jsou ideální. V takovém případě očekává na výpisu z účtu
zadejte referenci faktury/platby (pokud je vybrána „Štítek“).
(když je vybrána volba „Partner je nastaven“), aby se zobrazilo správné partnerství a provedeno spojení.
platba proběhne automaticky.

Částečná shoda faktur, pokud je nedoplacená
-----------------------------------------

Tento model předpokládá fakturu zákazníka nebo dodavatelskou fakturu, které částečně odpovídají platbě, když
Výše přijaté částky je o něco nižší než výše faktury, například v případě
Slevy na hotové peníze. Rozdíl se vyrovnává s účtem uvedeným v
:guilabel:`záznamy pro protějšek“ v záložce.

Rekonciliační model: Type je Rule to match invoices/bills a
Nastavte přípustnou toleranci platby.

.. obrázek:reconciliation_models/partial-match.png
:alt:Nastavte pravidla, která vyvolají sjednocení.

.. poznámka::
Příplatek za platbu je pouze pro nižší platby. Je ignorován, pokud jde o vyšší platby.
Pokud je přeplatek obdržen.

.. viz též:
:doc:`../fakturace/hotovostni-sleva`

Přímka s poplatky za bankovní služby
-------------------

Tento model navrhuje protějšek podle pravidel nastavených v tomto modelu. V případě českého jazyka je
model usmíření: typ je „pravidlo pro navržení protikladu“ a
Příkladem použití proměnné :guilabel: je např. identifikace informací označených
:guilabel:`Poplatky za bankovní služby“ v poli popisu transakce.

.. obrázek:: bankovní poplatky
:alt:Nastavte pravidla, která vyvolají sjednocení.

.. poznámka::
„Vzorce regulárních výrazů“ (anglicky „Regular Expressions“, zkráceně „Regex“) lze používat
Odoo různými způsoby prohledávat, ověřovat a upravovat data v systému. RegEx může být
Je silná, ale také složitá, takže je důležité ji používat rozvážně a s dobrým porozuměním.
z těch vzorů, se kterými pracujete.

Pro použití regulárních výrazů ve vašich modelech pro vyrovnání účtů nastavte :guilabel:`Typ transakce`.
do pole „Regex“ a přidejte svůj výraz. Odoo automaticky získává výraz.
transakce, které odpovídají vašemu regulárnímu výrazu a podmínkám specifikovaným ve vaší modelu.

.. obrázek::rekonciliace_modely/regex.png
:alt:Použití regulárních výrazů v Odoo

Mapování partnerů
===============

Partnerské mapování umožňuje nastavit pravidla pro automatické přiřazení transakcí k správnému partnerovi.
partnerský účet, ušetřit čas a snížit riziko chyb, které mohou nastat při ruční
sjednocení. Například můžete vytvořit pravidlo pro mapování příchozích plateb s
Specifické referenční číslo nebo klíčové slovo v popisu transakce. Při příchozím platebním příkazu
splňuje tyto kritéria, pak se Odoo automaticky přiřadí k příslušnému zákazníkovi.

Pro vytvoření pravidla pro mapování partnerů přejděte na záložku „Mapování partnerů“ a zadejte
:guilabel:`Hledat text v štítku“, :guilabel:"Hledat text v poznámkách“ a :guilabel:"Spolupracovník“.

.. obrázek: partner-mapping.png
:alt: definice partnerství
