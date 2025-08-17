==================================
Kapitola 3: Přizpůsobení zobrazení Kanban
==================================

Získali jsme pochopení pro mnoho možností nabízených webovým rámcem.
dalším krokem bude přizpůsobení kanbanového pohledu. Tento projekt je komplexnější a ukáže
některé nezanedbatelné aspekty rámce. Cílem je procvičit se v komponování pohledů a koordinaci
různé aspekty uživatelského rozhraní a provádět je v udržitelném způsobu.

Bafien měl nejlepší nápad na světě: smíšený pohled na kanban a seznam by byl ideální pro vaše
potřebuje! Zkrátka chce mít na levém okraji zobrazení kanbanu v CRM seznam zákazníků. Když
klikněte na zákazníka v levém sloupci, zobrazí se pouze karty s daným zákazníkem.
odkazující na tento zákazník.

.. varování: Cíl

.. obrázek: 03_customize_kanban_view/overview.png
:synchronizace: střed

..spoiler:: Řešení

Řešení každé úlohy kapitoly jsou uveřejněna na
„oficiální repozitář návodů k použití Odoo
<https://github.com/odoo/tutorials/commits/{CURRENT_MAJOR_BRANCH}-master-odoo-web-framework-solutions/awesome_kanban>.

1. Vytvořte nový kanbanový pohled
===========================

Protože upravujeme zobrazení kanbanu, začněme tím, že ho rozšíříme a použijeme naši úpravu
kanbanový pohled na CRM.

#Vytvořte nový prázdný komponent, který dědí z komponenty KanbanController.
:file:`@web/views/kanban/kanban_controller.
#Vytvořte nový objekt zobrazení a přiřaďte všechny klíče a hodnoty z kanbanView.
:soubor: @web/views/kanban/kanban_view. Změňte klíč kontroleru tak, že do něj vložíte svůj nový
vytvořil kontrolor.
#Zaregistrujte ji v registru pohledů pod názvem „awesome_kanban“.
#Aktualizujte kanbanovou kartu CRM v souboru `awesome_kanban/views/views.xml`, aby používala rozšířený pohled.
Toho lze dosáhnout nastavením atributu „js_class“ v uzlu kanban.

.. viz též:

`Příklad: Vytvořte nový pohled, který se vztahuje na existující <https://github.com/odoo/odoo/blob/0a59f37e7dd73daff2e9926542312195b3de4154/addons/todo/static/src/views/todo_conversion_form/todo_conversion_form_view.js>`_.

2. Vytvořte komponentu CustomerList
==================================

Budeme potřebovat zobrazit seznam zákazníků, takže proč ne vytvořit komponentu?

#Vytvořte komponentu CustomerList, která zobrazuje pouze div s nějakým textem.
#Mělo by mít vlastnost selectCustomer.
#Vytvořte nový šablonu, která se bude vztahovat na (XPath) šablonu kanbanového ovládacího prvku web.KanbanView a přidá
„Seznam zákazníků“ vedle kanbanového rendereru. Přidejte prázdnou funkci jako „vybrat zákazníka“.
Ale zatím.

......tip:

Můžete použít tento XPath v šabloně, abyste přidali div před komponentu renderer.

... kódový blok::xml

<xpath expr="//t[@t-component='props.Renderer']" position="before">
               ...
</xpath>

#Přidejte do kanbanového ovladače třídu CustomerList a vytvořte její podtřídy.
#Zkontrolujte, zda vidíte svou součástku v kartovém pohledu.

.. obrázek: 03_customize_kanban_view/customer_list_component.png
:align:center

.. viz též:

:ref:`Dědičnost šablon <reference/qweb/template_inheritance>`

3. Nahrání a zobrazení dat
========================

#Upravte komponentu CustomerList tak, aby načetla seznam všech zákazníků v metodě onWillStart.
#Zobrazte seznam v šabloně pomocí t-foreach.
#Při výběru zákazníka volá funkci selectCustomer.

.. obrázek: 03_customize_kanban_view/customer_data.png
:align:center

.. viz též:

   - „Příklad: získání záznamů ze šablony <https://github.com/odoo/odoo/blob/986c00c1bd1b3ca16a04ab25f5a2504108136112/addons/project/static/src/views/burndown_chart/burndown_chart_model.js#L26-L31>“

4. Aktualizovat hlavní nástěnku
==============================

#Vložte funkci selectCustomer do kanbanového ovladače a přidejte správnou doménu.

......tip:

Protože interakce s výsledky vyhledávání není úplně jednoduchá, zde je ukázka k vytvoření
filtr:

... kódový blok::js

tento.env.searchModel.vytvořit nové filtry ([] [{
popis: partner_name
doména: [[„partner_id“, „==“, partner_id]],
jeZAwesomeKanban: true, // tento klíč slouží k pozdějšímu získání filtrů
         }])

#Po kliknutí na více zákazníků se zobrazí, že starý filtr zákazníka není nahrazen.
Zajistěte, aby při kliknutí na zákazníka byl starý filtr nahrazen novým.

......tip:

Tento kousek kódu vám umožní získat filtry zákazníků a přepínat je.

... kódový blok::js

const customerFilters = this.env.searchModel.getSearchItems( (searchItem) =>
searchItem.jeZAwesomeKanban
         );

pro každý filtr zákazníka z filtrů zákazníků
Pokud je filtr zákazníka aktivní,
tento.env.searchModel.přepínání hledaného výrazu (ID filtru zákazníka).
            }
         }

#Upravte šablonu, aby funkce CustomerList selectCustomer dostala skutečnou hodnotu.

.. poznámka::

Můžete použít symbol

aby se ujistil, že klíč „isFromAwesomeKanban“ nebude kolidovat s klíči jiných
může přidat do objektu.

.. obrázek: 03_customize_kanban_view/customer_filter.png
:align:center

5. Zobrazit pouze zákazníky, kteří mají aktivní objednávku
====================================================

V poli „opportunity_ids“ v tabulce „res.partner“ umožníme uživateli filtrovat výsledky podle
zákazníci s alespoň jednou příležitostí.

#Přidejte do komponenty CustomerList vstup typu checkbox s názvem „Aktivní zákazníci“.
vedle něj.
#Změna hodnoty zaškrtávacího políčka by měla filtrovat seznam zákazníků.

.. obrázek: 03_customize_kanban_view/active_customer.png
:align:center
:skalka: 60 %

6. Přidejte vyhledávací lištu do seznamu zákazníků
========================================

Přidejte pole pro vstup nad seznam zákazníků, které umožní uživateli zadat řetězec a filtrovat
zobrazení zákazníků podle jejich jména.

..tip:
Můžete použít funkci fuzzyLookup z :soubor:@web/core/utils/search.
filtr

.. obrázek: 03_customize_kanban_view/customer_search.png
:align:center
:skalka: 60 %

.. viz též:

   - Kód: Funkce fuzzylookup <https://github.com/odoo/odoo/blob/235fc69280a18a5805d8eb84d76ada91ba49fe67/addons/web/static/src/core/utils/search.js#L41-L54>
   - Příklad: Použití fuzzyLookup

addons/web/static/tests/core/utils/search_test.js#L17>

7. Refaktoruj kód tak, aby používal t-model
=====================================

Pro vyřešení předchozích dvou cvičení jste pravděpodobně použili událostní slyšen na vstupech.
Podívejme se, jak bychom to mohli udělat v deklarativnější formě s tzv.
`<{OWL_PATH}/doc/reference/input_bindings.md>`

#Ujistěte se, že máte objekt reagující na skutečnost, že filtr je aktivní.
(něco jako
:kód: `this.state = useState({ zobrazitAktivníZákazníky: false, hledanéSlovo: "" }).
#Upravte kód tak, aby přidal vlastnost „zobrazení zákazníků“, která se vrací aktuální seznam.
zákazníků.
#Změňte šablonu a použijte t-model.

8. Paginujte zákazníky!
======================

#Přidejte do CustomerList pager:ref:`<frontend/pager>`. Zákazníky načtěte a zobrazte jen prvních 20.
zákazníci.
#Každýkrát, když se změní pager, by měl být aktualizován seznam zákazníků.

Tohle je docela těžké a v kombinaci s filtrováním prováděným
předchozí cvičení. Je třeba vzít v úvahu mnoho specifických případů.

.. obrázek: 03_customize_kanban_view/customer_pager.png
:align:center
:skalka: 60 %
