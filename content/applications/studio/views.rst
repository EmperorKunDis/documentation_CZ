=====
Názory
=====

Viditelné objekty jsou rozhraním, které umožňuje zobrazit data uložená v modelu.
<model_module_app>. Model může mít několik pohledů, které jsou prostě různými způsoby zobrazení.
stejná data. V Studiu jsou pohledy uspořádány do čtyř kategorií: :ref:`obecných
<studia/zobrazení/všeobecné>“, :referencem:“více záznamů <studia/zobrazení/více-záznamů>“, :referencem:“časová osa
<studia/výhledy/časová osa>, a :ref:`zprávy <studia/výhledy/zprávy>`.

..tip:
   - Chcete-li změnit výchozí pohled na model, přejděte do
:guilabel:`Názory“, klikněte na ikonu „fa-ellipsis-v“ (:guilabel:`Ellipsis“) vedle
požadovaný výhled a klikněte na tlačítko „Nastavit jako výchozí“.
   - Můžete upravovat pohledy pomocí vestavěného XML editoru: Zapněte režim vývojáře
<developer-mode>`, přejděte do pohledu, který chcete upravit, vyberte záložku „Pohled“ a
klikněte na:guilabel:`</> XML`.

... důležité:
Pokud upravujete pohled pomocí editoru XML, vyhněte se přímo změnám v standardním pohledu.
a děděné pohledy, protože by se během aktualizací nebo upgradů modulů resetovaly a ztratily.
Vždy se ujistěte, že vyberete správnou nástavbu vlastních pohledů na Studio: Když upravíte
zobrazení v ateliéru tahem myši a pádem nového pole, například konkrétního ateliéru
dědí pohled a odpovídající cestu XPath, která definuje upravenou část pohledu.
automaticky vygenerované.

.._studia/výhledy/obecné:

Obecná hlediska
=============

.. poznámka::
Níže uvedené nastavení najdete pod záložkou „Zobrazení“ není-li uvedeno jinak.
Jinak.

.._studio/views/general/form:

Tvar
----

Vidíme formulář pro vytváření a úpravu záznamů, například
kontakty, objednávky, produkty atd.

- Pro strukturování formuláře použijte vložený prvek „Tabulek a sloupců“ (:guilabel:).
:guilabel:`+ Přidat“ záložka.
- Aby uživatelé nemohli vytvářet, upravovat nebo mazat záznamy, zaškrtněte políčko „Nemůže vytvářet“,

- Pro přidání tlačítka klikněte na „Přidat tlačítko“ v horní části formuláře, zadejte „Popisek“
a vyberte akci tlačítka:

  - :guilabel:`Spustit akci serveru“: vyberte akci „Server“
bude z rozevírací nabídky.
  - :guilabel:`Volání metody“: specifikujte existující metodu v Odoo.

- Chcete-li změnit název nebo styl tlačítka, klikněte na něj a upravte jeho :guilabel:`Název` nebo
:guilabel:`Třída“ (buď „btn-primary“ nebo „btn-secondary“) v záložce „Vlastnosti“.
- Chcete-li přidat chytrý tlačítko, klikněte na ikonu „Plus“ v pravém horním rohu.
rohu formuláře. Zadejte :guilabel:`Label`, vyberte :guilabel:`Icon` a vyberte
:ref:`související pole <studio/fields/relational-fields-related-field>“.

Příklad:

.... obrázek:: views/form-objednávka-prodeje.png
:alt:Výběr formuláře prodejního příkazu

.._studio/views/obecne/aktivita:

Aktivita
--------

Viditelnost „Aktivita“ s ikonou „fa-clock-o“ slouží k plánování a přehledu
aktivity spojené s záznamy (e-maily, telefonáty atd.).

.. poznámka::
Tento pohled lze upravit pouze v aplikaci Studio pomocí úpravy kódu XML.

Příklad:

.. obrázek:: views/activity-lead-opportunity.png
:alt: Zobrazení aktivit v modelu lead/opportunity

.._studio/views/generální/hledat:

Hledání
------

Viditelnost :guilabel:`Hledání` :icon:`oi-search` se přidává na vrchol ostatních viditelností k filtrování, seskupování a
hledat záznamy.

- Chcete-li přidat vlastní filtry a strukturovat je pomocí oddělovačů, přejděte na
:guilabel:`+ Přidat“ záložku a přetáhněte je pod záložku „Filtry“.
- Chcete-li přidat existující pole pod vyhledávací nabídku, přejděte na kartu „Přidat“ a
přetáhněte a vložte pod pole :guilabel:`Autocompletion Fields“.

Příklad:

.... obrázek:: views/search-project-kanban.png
:alt: Zobrazení vyhledávání projektu na kartě Kanban

.._studia/zobrazení/více záznamů:

Několik pohledů na záznamy
======================

.. poznámka::
Níže uvedené nastavení najdete pod záložkou „Zobrazení“ není-li uvedeno jinak.
Jinak.

.._studio/views/multiple-records/kanban:

Kanban
------

Viditelnost „Kanban“ často slouží k podpoře obchodních toků tím, že pohybuje
záznamy mezi fázemi nebo jako alternativní způsob zobrazení záznamů uvnitř karet.

.. poznámka::
Pokud existuje pohled „Kanban“, je používán výchozím způsobem pro zobrazení dat na mobilních zařízeních
místo :ref:`Zobrazení seznamu <studio/views/multiple-records/list>`.

- Aby uživatelé nemohli vytvářet nová data, označte políčko „Nemůže vytvářet“.
- Pro vytváření záznamů přímo ve výhledu v minimalistické podobě umožňuje :guilabel:`Rychlý
Vytvořit.
- Pro výchozí skupování záznamů vyberte pole podle :guilabel:`Default Group By`.

Příklad:

.... obrázek:: views/kanban-project.png
:alt:Kanbanový pohled na projekt

.._studia/zobrazení/více záznamů/seznam:

Seznam
----

Vidíte-li seznamy mnoha záznamů najednou, použijte zobrazení „Seznam“.
záznamy a upravovat jednoduché záznamy.

- Aby uživatelé nemohli vytvářet, upravovat nebo mazat záznamy, zaškrtněte políčko „Nemůže vytvářet“,

- Pro vytváření a úpravu záznamů přímo ve výhledu vyberte buď :guilabel:`Add record at
„Dno“, „Přidat záznam na vrch“ nebo „Otevřít formulář“ pod
:guilabel:`Při vytváření záznamu“.

...... poznámka::
Tímto způsobem se uživatelé nemohou otevřít záznamy v :ref:`Zobrazení formuláře <studio/views/general/form>`.
:guilabel:`Seznam“

- Pro editaci více záznamů najednou zaškrtněte políčko „Masová úprava“.
- Chcete-li změnit způsob výchozího řazení záznamů, vyberte pole podle položky „Seřadit podle“.
- Pro výchozí skupování záznamů vyberte pole podle :guilabel:`Default Group By`.
- Chcete-li přidat tlačítko, klikněte na „Přidat tlačítko“ v horní části seznamu, zadejte „Popisek“
a vyberte akci tlačítka:

  - :guilabel:`Spustit akci serveru“: vyberte akci „Server“
bude z rozevírací nabídky.
  - :guilabel:`Volání metody“: specifikujte existující metodu v Odoo.

..tip:
Chcete-li ručně přesunout záznamy, přidejte ikonu „přetahování“ (:guilabel:„ruční ovládání“)
:ref:`Číselné pole <studio/fields/simple-fields-integer>“ s widgetem :guilabel:`Handle“.

.. obrázek:: views/list-drag-handle.png
:alt:Ikona táhla, která umožňuje ruční řazení záznamů v seznamovém zobrazení

Příklad:

.... obrázek:: views/list-sales-order.png
:alt: Zobrazení seznamu prodejních objednávek

.._studia/zobrazení/více záznamů/mapa:

Mapa
---

Zobrazení „Mapa“ s ikonou „fa-map-marker“ se používá k zobrazení záznamů na mapě. Například
slouží v aplikaci Field Service k plánování trasy mezi různými úkoly.

.. poznámka::
A :ref:`Políčko Many2One <studio/fields/relational-fields-many2one> spojené s modelem *Kontakt*
je nutné aktivovat pohled, protože kontaktní adresa slouží k určení polohy záznamů na mapě.

- Pro výběr typu kontaktu na mapě vyberte jej pod tlačítkem :guilabel:`Kontakt
Hřiště.
- Zakrýt jméno nebo adresu záznamu lze zaškrtnutím políčka „Skryj jméno“ nebo „Skryj
Adresa.
- Chcete-li přidat informace z dalších polí, vyberte je pod tlačítkem „Další pole“.
- Pro zobrazení trasy mezi různými záznamy zaškrtněte políčko „Zapnout navigaci“ a
vyberte pole, které bude použito k řazení záznamů pro routování.

Příklad:

.... obrázek: views/map-task.png
:alt: Zobrazení mapy úkolového modelu

.._studia/výhledy/časová osa:

Zobrazení časové osy
==============

.. poznámka::
   - Když poprvé aktivujete jednu ze zobrazení časové osy, musíte vybrat datum:
<studia/pole/jednoduché-políčka-datum> nebo :ref:`Datum a čas
pole typu <studio/fields/simple-fields-date-time> by měla být použita k definování, kdy se má
záznamy začínají a končí, aby je bylo možné zobrazit v pohledu. Můžete upravit
:guilabel:`Datum začátku“ a :guilabel:`Datum ukončení“ po aktivování zobrazení.
   - Níže uvedené nastavení najdete pod záložkou „Výhled“ není-li uvedeno jinak.
Jinak bychom se na něj mohli dívat jinak.

.._studio/views/timeline/calendar:

Kalendář
--------

Výhled kalendáře slouží k prohlížení a správě záznamů uvnitř
kalendář.

- Vytvářet záznamy přímo v pohledu namísto otevření Formulářového pohledu
<studia/zobrazení/obecné/formulář>`, aktivní :guilabel:"Rychlé vytvoření".

...... poznámka::
Toto funguje pouze u konkrétních modelů, které lze vytvořit rychle pomocí pouhého názvu.
většina modelů nepodporuje rychlé vytváření a otevírá :guilabel:`Formulář`.
povinné pole.

- Pro barevné označení záznamů v kalendáři vyberte pole pod štítkem :guilabel:`Barva`.
Stejná hodnota pro dané pole se zobrazuje stejnou barvou.

...... poznámka::
Protože je omezený počet barev, může se stát, že stejná barva bude přiřazena různým
hodnoty.

- Pro zobrazení události trvající celý den na začátku kalendáře vyberte pole „Zatržítko“.
„Studio/Základní pole/Jednoduché pole – checkbox“ určuje, zda se akce koná celý den.

- Pro výběr výchozího časového měřítka používaného k zobrazení událostí vyberte :guilabel:`Den`, :guilabel:`Týden`.
:guilabel:`Měsíc“ nebo :guilabel:`Rok“ pod :guilabel:`Výchozím zobrazovacím režimem“.

.. poznámka::
Můžete také použít pole :guilabel:`Zpoždění`, které zobrazí dobu trvání události v hodinách.
výběrem :ref:`Dezimalního pole <studio/fields/simple-fields-decimal>` nebo :ref:`Číselného pole
pole typu „jednoduché pole – celé číslo“ na modelu, které určuje délku trvání
Ale pokud nastavíte pole „Datum ukončení“, pole „Zpoždění“ nebude fungovat.
berou v potaz.

Příklad:

.... obrázek:: views/kalendarni_udaj.png
:alt: Zobrazení kalendáře události v modelu události

.. _studia/pohledy/časová osa/skupina:

Kohorta
------

Viditelnost „Kohorta“ (zobrazení „Sledování kohorty“) se používá ke zkoumání životního cyklu záznamů.
doba. Například je používán v aplikaci Předplatné pro zobrazení udržení předplatných.
sazba.

- Zobrazit měřítko (tj. součet hodnoty určitého pole) v tabulce výchozím způsobem, vyberte
a:guilabel:`Měřicí pole“.
- Pro výběr časového intervalu, který se použije jako výchozí pro skupování výsledků, vyberte:
:guilabel:`Týden“, :guilabel:`Měsíc“ nebo :guilabel:`Rok“ pod :guilabel:`Intervalem“.
- Chcete-li změnit kohortu „Modus“, vyberte buď „Zachování“ (procento)
zaznamenaných hodnot v čase, začíná na 100 % a s časem klesá.
:guilabel:`Churn“ :dfn:"procento záznamů, které se v čase přesouvají ven - začíná
„Výsledkem je, že se nám podařilo snížit počet úmrtí na 0 % a tento trend bude pokračovat.“
- Chcete-li změnit způsob, jakým se postupuje po sloupcích, vyberte buď
:guilabel:`Vpřed“ (od 0 do +15) nebo :guilabel:`Zpět“ (od -15 do 0). Pro většinu účelů
používán je časový úsek „Vpřed“.

Příklad:

.. obrázek:: views/cohort-subscription.png
:alt: Přehled kategorií v modelu předplatného

.._studia/výhledy/Ganttova diagramu:

Ganttova diagram
-----

Pohled Gantt je používán k předpovídání a zkoumání celkového pokroku.
záznamy. Záznamy jsou reprezentovány čárou pod časovou osou.

- Pokud nechcete, aby uživatelé vytvářeli nebo upravovali záznamy, vyjměte zaškrtávací políčko „Může vytvořit“ nebo „Může upravovat“.
Edit.
- Vyplnit buňky šedou barvou, pokud by se tam neměla vytvářet záznam (například o víkendech).
zaměstnanců, zaškrtněte políčko „Zobrazit nedostupnost“.

...... poznámka::
Podkladový model musí tuto funkci podporovat a podpora pro ni nemůže být přidána pomocí
Studio. Je podporováno pro aplikace Projekt, Volno, Plánování a Výroba.

- Chcete-li zobrazit celkovou řadu na dně, zaškrtněte políčko „Zobrazit celkovou řadu“.
- Pro seskupení více záznamů do jedné řádky zaškrtněte políčko „Seskupit první úroveň“.
- Pro výběr způsobu, jakým jsou záznamy ve sloupcích v tabulce zobrazovány podle skupin (např. podle zaměstnance nebo projektu) vyberte
a pole pod :guilabel:`Výchozí skupinou“.
- Pro výběr výchozího časového měřítka pro zobrazení záznamů vyberte „Dnes“, „Týden“
:guilabel:'Měsíc' nebo :guilabel:'Rok' pod :guilabel:'Výchozí měřítko'.
- Pro barevné zvýraznění záznamů na obrazovce vyberte pole pod :guilabel:`Barva`. Všechny záznamy sdílející
Stejná hodnota pro daný prvek se zobrazuje stejnou barvou.

...... poznámka::
Vzhledem k omezenému počtu barev může být stejná barva přiřazena různým hodnotám.

- Pro určení, jak přesně se měl každý časový úsek rozdělit, vyberte
:guilabel:`Čtvrt hodiny“, :guilabel:`Půl hodiny“ nebo :guilabel:`Hodina“ pod :guilabel:`Den
„Přesnost“ pod „Půl dne“, „Den“ nebo „Týden přesnosti“ v závislosti na tom, jaké údaje chcete zobrazit.
:guilabel:`Měsíční přesnost“.

Příklad:

.. obrázek:: views/gantt-planning.png
:alt:Ganttovský pohled plánovacího modelu

.._studio/zpravodajství

Zobrazování pohledů
===============

.. poznámka::
Níže uvedené nastavení najdete pod záložkou „Zobrazení“ není-li uvedeno jinak.
Jinak.

.._studia/výhledy/reporting/pivot:

Pivot
-----

Viditelnost Pivot je používána k prozkoumání a analýze dat obsažených v
v interaktivních záznamových knihách. Je zvláště užitečné pro agregaci číselných dat a vytváření
kategorie a prohlížet data rozbalováním a skládáním různých úrovní dat.

- Pro přístup k všem záznamům, jejichž data jsou agregována pod buňkou, zaškrtněte políčko „Přístup ke
buňka.
- Pro rozdělení dat do různých kategorií vyberte pole podle:guilabel:„Skupování sloupců“

- Pro přidání různých typů dat k měření pomocí pohledu vyberte pole pod
:guilabel:`Měření“.
- Zobrazit počet záznamů tvořících agregovaná data v buňce, zaškrtněte políčko :guilabel:`Zobrazit
počítat.

Příklad:

.... obrázek:: views/pivot-purchase-report.png
:alt: Zobrazení sloupců v Pivotu

.._studio/zpravodajství/graf:

Graf
-----

Viditelnost grafu :guilabel:`Graph` :icon:`fa-area-chart` se používá k zobrazení dat ze záznamů v bodech.
Svislá osa nebo sloupcový graf.

- Pro změnu výchozího grafu vyberte „Bar“, „Line“ nebo „Pie“ pod
:guilabel:`Typ“.
- Pro výběr výchozího rozměru dat (kategorie) vyberte pole pod názvem :guilabel:`První rozměr
a pokud je potřeba, další pod :guilabel:`Druhá dimenze“.
- Pro výběr typu dat, která budou měřena pomocí pohledu, vyberte pole pod
:guilabel:`Měření“.
- *Pro barové a čárové grafy pouze*: Chcete-li seřadit různé kategorie dat podle jejich hodnoty, vyberte
:guilabel:`Vzestupně“ (od nejnižší hodnoty k nejvyšší) nebo :guilabel:`Sestupně“ (od nejvyšší
nejnižší) podle:guilabel:`Řazení`.
- *Pro barové a koláčové grafy pouze*: Chcete-li zobrazit všechny záznamy, jejichž data jsou agregována pod datem
kategorii v grafu, zaškrtněte políčko „Přidat záznamy z grafu“.
- *Pro jen barové grafy*:Pokud používáte dva rozměry dat (kategorie), zobrazte oba sloupce nahoře
se vzájemně překrývají, pokud zaškrtnete :guilabel:`Skládaná grafika`.

Příklad:

.... obrázek: views/graph-sales-report.png
:alt: Graf zobrazující vývoj prodejů v aplikaci Model Analýza trhu
:skalka: 75 %
