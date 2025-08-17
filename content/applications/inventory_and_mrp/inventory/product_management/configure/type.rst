============
Druh produktu
============

.. |BOM| nahradit za: :abbr:`BOM (Seznam materiálů)`

V Odoo jsou zboží i služby nastavené jako produkty. Při vytváření nového produktu je nutné vyplnit
Několik polí, která je třeba pečlivě vybrat, protože určují způsob fakturace a sledování.
Zboží nebo služby podniku.

Pro konfiguraci stávajícího produktu přejděte na: „Skladové aplikace --> Produkty --> Produkty“.
a zvolte požadovaný produkt ze seznamu. Nebo z nabídky „Produkty“
Klikněte na tlačítko „Nový“ pro vytvoření nového produktu.

.. viz též:
„Odoo Tutorials: Produkt <https://www.youtube.com/watch?v=l6j0ZkP5mLM>“

.. sklad/správa produktů/prodej nebo nákup:

Prodej versus nákup
=====================

Zboží a služby mohou být označeny jako ty, které lze koupit nebo prodat, nebo obojí. Na produktu
formulář, zaškrtněte políčko „Prodej“ pokud je produkt pro zákazníka k dispozici (např.
zboží). Zaškrtněte pole „Nákup“ pokud je produkt možné koupit (např. suroviny).

.. příklad::
Pokud second-hand oblečení kupuje levně džínové bundy a prodává je za vyšší cenu,
konečný spotřebitel, produktová forma „Bunda“ může mít obě :guilabel:`Prodej` a
:guilabel:`Koupit“ zaškrtnuté.

Na druhou stranu obchod občas šije nové bundy z džínoviny a nití
suroviny. V produktových formách „Džínovina“ a „Nit“ by měl být pouze nákup.
Tento produkt by se tedy zobrazoval pouze v kategorii „Prodej“.

Zboží versus služby
==================

Při konfiguraci produktu je třeba vybrat typ produktu na
Kartě „Obecné informace“ v podobě produktu. Každý druh produktů má jiný dopad
operace v dalších aplikacích Odoo, jako jsou například **Prodej** a **Nákup**.
Opravdu opatrně.

- :guilabel:`Zboží“: fyzická, materiální věc (např. hamburger až po dům)
- „Služba“: nehmotný, nehmotný produkt (např. oprava, stříhání vlasů, call centrum
(pomoc).
- :guilabel:`Kombinace“: jakýkoliv mix zboží a služeb (např. nové auto (*zboží*) s výměnou oleje
(včetně služeb (*service*)).

.. poznámka::
Protože jsou služby nehmotné, nelze je v aplikaci **Sklad** sledovat.

… skladování, řízení zásob a výroba:

Nastavit zboží
===============

Vybráním „Zboží“ jako „Typu produktů“ se automaticky zobrazí
pár políček a záložek v produktovém formuláři:

- Karta „Výpis“: Zde můžete
:doc:`nákupní a výrobní trasy <../../shipping_receiving/daily_operations/use_routes>`
a v oblasti produktového logistického řízení lze specifikovat například hmotnost výrobku a časový úsek pro zpracování objednávky zákazníka.
- Políčko „Způsob fakturace“: Toto pole
určuje, v jakém bodě prodejního procesu je zákazník fakturován.

.. důležité::
Pole „Zásady fakturace“ (**guilabel:Invoicing Policy**) se zobrazí pouze v případě, že je nainstalována aplikace „Prodej“.

- Pole „Inventář“: Toto zaškrtávací políčko
určuje, zda Odoo eviduje zásoby tohoto produktu.
- Chytré tlačítko: Některá chytrá tlačítka se zobrazí nad formulářem, když je vybrán produkt.
Další zobrazují výběrem metody :guilabel:`Inventarizační stopa`. Například
„Na skladě“ a „Předpovězené“ zobrazují, když je aktivní „Skladová zásoba“.
Vybrané chytré tlačítko na produktu se většinou spojí s operacemi inventáře:ref:`viz


.. obrázek: typ/produkt-form.png
:alt:Označit produkt jako dobrý nebo službu.

... inventarizaci, správu produktů a politiku fakturace:

Způsob fakturace
----------------

Pole „Zásady fakturace“ se zobrazí pouze na kartě produktu, pokud je produkt prodáván (v
tedy pokud je zaškrtnuto pole „Prodej“ a aplikace Sales je nainstalována.

Při konfiguraci produktu pro prodej je nutné zvolit
:dokumentu „způsob fakturace <../../../../sales/sales/invoicing/invoicing_policy>“.
Zvolená politika „Počet objednaných kusů“ vystavuje zákazníkům fakturu až po potvrzení objednávky.
je potvrzeno. Když je vybrána položka „Dodané množství“, zákazníkům jsou fakturovány jednou
Dodávka je dokončena.

.. inventář/správa produktů/sledování zásob:

Sledované a nezasílané zásilky
---------------------------

Záložka „Sklad“ na formuláři produktu určuje mnohé z inventáře Odoo.
operace.

„Sledované“ produkty jsou ty, u nichž je skladováno a evidováno množství. Příklady zahrnují hotové
zboží a často i suroviny nebo součástky potřebné k jeho výrobě.

Při zaškrtnutí položky „Inventarizační seznam“ se objeví vyskakovací okno s nabídkou pro inventarizaci.
sledován jedním z těchto způsobů: „Sériovým číslem“, „Lotem“ nebo
:guilabel:`Podle množství“.

.. obrázek: typ/sledovaný.png
:alt: Konfigurace sledovaného zboží.

Neklasifikované produkty (někdy nazývané jako „nevýrobní“ produkty) jsou obvykle spotřebovány v
Krátký časový úsek, což znamená, že zásoby nepotřebují být udržovány.
Tyto produkty jsou často nezbytné, přesné počítání však není nutné. Příklady zahrnují kancelářské potřeby,
obalový materiál nebo výrobky používané v průmyslu, které nevyžadují individuální sledování.

.. tip::
Zaškrtněte políčko „Sledovat zásoby“ (Guilabel: Track Inventory), pokud je nutné sledovat zásoby produktu.
různých lokalitách, pro ocenění zásob, s čísly šarží a/nebo sériovými čísly nebo při použití
pravidla přeskupování.

.. viz též:
:doc:`Sledování skladovatelných výrobků pomocí čísla šarže a čísla výrobní série <../product_tracking>`

...Inventář / správa produktů / inventarizační operace podle typu produktu:

Inventarizační operace podle druhu zboží
------------------------------------

Zda je zboží sledované nebo ne (sledování zásob/správa produktů/sledování zásob)
ovlivňuje běžné operace s inventářem, jako jsou přesuny a pravidla pro doplnění zásob.

Tabulka níže shrnuje, které operace (a chytré tlačítko) jsou povoleny pro sledovaná zařízení a
neevidované zboží. Kliknutím na položky v grafu se dostanete k podrobnějším informacím a souvisejícímu obsahu.
dokumenty.

.. seznam tabulkový::
:hlavičkové řádky: 1
:prázdné sloupky: 1

   * -Inventarizační operace
     - Sledované
     - Nepozorovaný
   * –:ref:`Množství skladem <sklad/správa produktů/množství skladem>`
     - Ano
     - No
   * – :ref:`Předpokládané množství (sklad/správa zásob/dostupnost)“
     - Ano
     - No
   * – :ref:`Použijte pravidla pro přeskupování zásob <inventory/product_management/replenishment>`
     - Ano
     - No
   * - :ref:`Může být součástí objednávky na nákup <inventory/product_management/po>`
     - Ano
     - Ano
   * – :ref:`Použijte pravidla pro skladování výrobků <skladování/správa produktů/skladování>
     - Ano
     - No
   * – lze vyrobit, zadat k výrobě nebo použít v seznamu materiálů pro výrobu jiného produktu
<Inventář/Řízení zásob/Výroba>
     - Ano
     - Ano
   * –:doc:`Použijte inventarizační úpravy <../../warehouses_storage/inventory_management/count_products>`
     - Ano
     - No
   * – :doc:`Používání metody ocenění zásob <../inventory_valuation/using_inventory_valuation>`
     - Ano
     - No
   * Vytvořit převod skladu
     - Ano
     - Ano
   * – :doc:`Sledování čísla šarže <../product_tracking>`
     - Ano
     - No
   * – :doc:`Může být umístěn v sadě <../../../manufacturing/advanced_configuration/kit_shipping>“
     - Ano
     - Ano
   * - :ref:`Může být umístěn do balíčku <inventář/správa produktů/balíček>
     - Ano
     - Ano
   * - :ref:`Se objevuje v inventárních zprávách <inventory/product_management/report>
     - Ano
     - No

Inventarizační činnost
~~~~~~~~~

.. skladové zásoby/správa produktů/dostupnost:

Skladové a předpokládané množství
*********************************

Množství skladovaného a předpokládaného produktu na základě příchozích a odchozích objednávek
reflektuje se na produktové podobě s dvěma chytrými tlačítky:

- :icon:`fa-cubes` :guilabel:`Množství skladem“: Toto znázorňuje počet jednotek, které jsou aktuálně k dispozici.
k dispozici v zásobách. Klikněte na tlačítko pro zobrazení nebo přidání skladových úrovní pro sledovaný produkt.
- :icon:`fa-area-chart` :guilabel:`Očekávané“: Toto znázorňuje počet jednotek, které se očekávají.
která je k dispozici po odečtení všech objednávek.

Klikněte na tlačítko pro zobrazení předpovědního reportu.

Na druhou stranu nezaznamenané produkty jsou považovány za vždy dostupné. Proto
:guilabel:„Množství na skladě“ není sledována a neexistuje ani „Prognózované“ množství.
k dispozici.

.. skladování, řízení zásob a ukládání zboží:

Pravidla skladování a uskladnění
*************************

Optimalizovat skladování může jak zásilky sledované, tak i nezaznamenané pomocí:

- :icon:`fa-random` :doc:`Pravidla pro skladování <../../shipping_receiving/daily_operations/putaway>“:
To představuje pravidla pro skladování zboží, například kde jej uskladnit při příjmu nové dodávky
přijíždí.
- :icon:`fa-cubes`
:doc:`Skladovací kapacity <../pravidelné-provozní-činnosti/skladování/>“
Toto představuje jakékoliv omezení skladovací kapacity uvedené pro tento produkt. Například sklad
může požadovat, aby v daném čase bylo na skladě maximálně deset (nebo méně) kusů sedaček kvůli jejich velikosti.
velikost.

.. inventář/správa produktů/dodávky:

Dodávky
*************

Pravidla přeřazování
^^^^^^^^^^^^^^^^

Aktivovat mohou pouze sledované produkty.
:dokumentu `pravidla pro přeskladnění <../../warehouses_storage/replenishment/reordering_rules>`,
nákupní objednávky. Nezaznamenané zboží nelze spravovat pomocí pravidel pro opětovné objednání.

Pravidla pro přeskupení lze nastavit přímo na formuláři produktu prostřednictvím
:icon:`fa-refresh` :guilabel:`(obnovit)`

.. poznámka::
Pokud již na produktu existují pravidla pro přeřazení, pak se tato tlačítko přejmenuje na
:guilabel:`Min/Max“, zobrazuje minimální a maximální počet jednotek, které musí být skladem.

.. inventář/správa produktů/po:

Vytvářejte objednávky k nákupu
^^^^^^^^^^^^^^^^^^^^^^

Obě druhy produktů lze zahrnout do poptávky v sekci Nákup.
aplikace. Pokud však obdržíte nezaznamenané produkty, jejich skladová zásoba se při přijetí
ověření příjmu („W/H“).

Tlačítko pro doplnění energie
^^^^^^^^^^^^^^^^^^^^^^

Tlačítko „Doplnit“ s funkcí :guilabel:„Replenish“ umožňuje doplnit všechny položky přímo z produktu.
podle trasy Preferred Route.

.. viz též:
:doc:`Dodávka <../../warehouses_storage/dodavky>`
„Tutoriály Odoo: Metody doplňování výroby
<https://www.youtube.com/watch?v=vtjeMGcG8aM>

… inventář/správa produktů/výroba:

Výroba
~~~~~~~~~~~~~

Může se vyrábět jak sledovaný, tak i nezaznamenaný produkt.
„subdodavatelské“ nebo „zahrnuté do výrobku“.
:doc:`seznam součástek (BOM) <../../../manufacturing/basic_setup/bill_configuration>“.

...Inventar/Produkt-Management/BoM:

Na formuláři pro zadání produktu je několik chytrých tlačítek, která mohou
pro výrobní operace:

- :icon:`fa-flask` :guilabel:`Seznam materiálů“: Tato ikona zobrazuje seznam materiálů, které byly použity při výrobě produktu.
- :icon:`fa-level-up` :guilabel:`Používají v produktech“: Tento seznam ukazuje další výrobky, které obsahují tento produkt.
BoM.

.. inventarizaci, řízení zásob a přesuny mezi prodejnami:

Převod zboží
~~~~~~~~~~~~~~

Přesuny jsou skladovací operace, které zahrnují pohyb zboží. Příklady přesunů
zahrnuje dodání a přijetí
<../../přeprava a příjem/denní operace/příjmy a dodání v jednom kroku>,
:doc:`vnitřní přesuny mezi sklady <../../warehouses_storage/replenishment/resupply_warehouses>
sklady.

Při vytváření převodu pro skladované položky v aplikaci **Sklad** se převody mění na dostupné.
množství na každé lokalitě. Například přesun pěti jednotek z interní lokality
„WH/Sklad“ na „WH/Balicí zóna“ snižuje záznamované množství v „WH/Sklad“ a naopak jej zvýší u
„WH/Balicí zóna“.

Pro neevidované produkty lze vytvářet přesuny, ale přesná množství na každém skladovacím místě jsou
nebyly sledovány.

.. inventář/správa produktů/balení:

Balíčky
~~~~~~~~

Obě druhy produktů lze umístit do balíčku: doc:balík <balicek>.

U neevidovaných produktů se však množství neeviduje a produkt není v
obsah balíčku:guilabel:`Obsah“ (kde se dostanete pomocí volby „Inventář aplikace
--> Produkty --> Balíčky“ a zvolte požadovaný balíček.

.. obrázek: typ/obsah-balíčku.png
:alt:Stránka s obsahem balíčku, která obsahuje seznam jeho obsahu.

Do balíčku byl vložen nezaznamenaný produkt, ale v sekci „Obsah“ není uveden.

Pokud je aktivována funkce „Přesunout celé balíčky“, přesouvání balíčku aktualizuje
místo uložení sledovaných produktů, ale ne obsah nesledovaných produktů.
vlastnost, přejít na:menu-selection:'Skladová aplikace --> Konfigurace --> Typy operací', vybrat
jakoukoli operaci a zaškrtněte políčko „Přesunout celé balíčky“.

...Inventar/Produktverwaltung/Bericht:

Inventarizační zprávy
~~~~~~~~~~~~~~~~~

Na následujících zprávách se objevují pouze sledované produkty.

.. důležité::
Tyto zprávy jsou dostupné pouze pro uživatele,
:doc:`přístup správce <../../../obecné/uživatelé/práva>.

- :doc:`Hlášení o zásobách <../../warehouses_storage/reporting/stock>“: Toto hlášení poskytuje
kompletní seznam všech skladových zásob, které jsou k dispozici, nejsou rezervované, přijaté nebo odeslané a jsou sledovány.
přejděte do sekce „Zprávy“ v aplikaci „Sklad“.
- :doc:`Report o umístění  <../../warehouses_storage/reporting/locations>`: Tento report ukazuje
rozložení produktů podle místa uchovávání (vnitřní, vnější nebo virtuální).
Zpráva je dostupná pouze s aktivovanou funkcí „Uložiště“.
(:menuselection:`Správa zásob --> Konfigurace --> Nastavení`).
:menu_selektor:`Skladová aplikace --> Hlášení --> Sklady“.
- :doc:`Historie přesunů <../../warehouses_storage/reporting/moves_history>“: Tento report
sumarizuje pohyb zboží na skladě a kdy bylo přijato nebo vyexpedováno. Chcete-li zobrazit tento report, přejděte do
:menuselection:`Správa zásob --> Hlášení --> Historie přesunů“.
:ikonka_fa_exchange: tlačítko „V/Z“ na formuláři produktu pro filtrování zpráv
na konkrétní historii pohybu daného produktu.
- :guilabel:`Analýza pohybů“: Tento report poskytuje tabulkové zobrazení převodů zásob.
typ operace.
- :ref:`Hodnotící zpráva o cenných papírech <správy/hospodářské/zprávy/hodnotící-zpráva-o-cennych-papirech>“: Podrobný záznam
z celkové hodnoty všech sledovaných zásob.

