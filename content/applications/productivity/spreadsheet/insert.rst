============================
Vložte a propojte s daty Odoo
============================

Do Odoo tabulky lze vložit několik prvků z databáze Odoo, a sice:

- seznamy, tedy data ze zobrazení :ref:`výpisu <studio/views/multiple-records/list>`.
- pivotové tabulky, tedy data z :ref:`pivotového pohledu <studio/views/reporting/pivot>`.
- diagramy, tedy data z grafického pohledu na report

Každý pokus o vložení seznamu, tabulky nebo grafu přidává do dokumentu nové zdroje dat.
Vytvoří se nová data zdroje, která propojí tabulku s vaším
Odoo databáze, která získává aktuální informace každýkrát, když se tabulka otevře v prohlížeči.
stránka je znovu načtena nebo se data ručně aktualizují kliknutím na „Data -> Obnovit všechna“.
z nabídky Nástroje.

:ref:`Vložené seznamy <spreadsheet/insert/list>“ a „Vložená tabulka s otáčivými sloupci
<spreadsheet/insert/pivot-table> používají vzorec s funkcí specifickou pro Odoo.
<spreadsheet/insert/list-functions> a :ref:`funkce pro tabulku s výsledky
<vložit/přidat funkce pivot table> pro získání dat ze své databáze a může být
dalších úprav v tabulce. Některé prvky grafů :ref:`vložených
„Vložit graf“ lze upravit, ale nelze s daty manipulovat nebo provádět výpočty.

.. poznámka::
Seznamy, tabulky s otáčivými body a grafy z různých aplikací a modelů lze vložit do stejného
spreadsheet.

..tip:
Pokud chcete používat filtry na úrovni celé aplikace, viz dokumentaci o globálních filtrech.
sešit nebo panel nástrojů, nepoužívejte stejná kritéria k vytvoření výchozího seznamu, přepínač
tabulku nebo graf v databázi.

Je také možné:

- Přidat k položkám nabídky Odoo „klikací odkazy“ (viz.
listů stejné tabulky nebo externích URL
- :ref:`vložte finanční údaje <spreadsheet/insert/financial-data> z databáze Odoo
Odoo specifická tabulka: doc:`funkce <funkce>`
- Připojte se k jinému Odoo tabulkovému procesoru, Excelu nebo Google Tabulkám a vložte do něj
Odoo tabulka

..._sešit/vložit/zdroje dat:

Zdroje dat
============

Zdroje dat, které vytváří každý :ref:`seznam <spreadsheet/insert/list>`, :ref:`rozložený seznam
<spreadsheet/insert/pivot-table> nebo :ref:`grafe <spreadsheet/insert/chart>` je vložen do
Odoo tabulka, propojte tabulku s příslušným model:
v databázi a uchovávat data v tabulce.
aktuální.

Každý zdroj dat je definován vlastnostmi, které lze přistupovat pomocí nabídky „Data“.
zdroje jsou identifikovány jejich příslušným :icon:`oi-view-pivot` :guilabel:`(tabulka s otáčivými sloupci)`
:ikonka „OI-VIEW-LIST“ nebo „FA-BAR-CHART“ a následně
podle jejich ID a názvu např. :icon:`oi-view-pivot`*(#1) Analýza prodejů podle produktu*.

.. obrázek: vložit/data-menu.png
:alt: Zdroje dat uvedené v nabídce Dat

Kliknutím na zdroj dat se zobrazí příslušné vlastnosti v panelu po pravé straně tabulky.

..tip:
   - Vlastnosti panelu lze také otevřít kliknutím pravým tlačítkem na buňku vloženého seznamu nebo rozbalovacího menu.
tabulku a poté kliknout na ikonu „Zobrazit seznam vlastností“ nebo
:ikonka:`oi-view-pivot` :guilabel:`Zobrazit vlastnosti sloupce“, nebo kliknutím na
:guilabel:`(menu)` ikona v pravém horním rohu vloženého grafu a poté kliknutí
:icon:`fa-pencil-square-o` :guilabel:`Upravit“.
   - Jakmile jsou otevřeny vlastnosti konkrétního zdroje dat, zůstanou otevřené i při přecházení
mezi záložkami v tabulkách. Chcete-li zavřít panel vlastností, klikněte na ikonu :icon:`fa-times`.
:guilabel:`(zavřít)` ikona v pravém horním rohu panelu.

.. poznámka::
Odstranění vloženého seznamu nebo tabulky s výchozími hodnotami nebo odstranění listu do nějž byl
neodstranit podkladový zdroj dat. Zdroj dat vloženého seznamu nebo tabulky s otáčivými body
lze smazat pouze vlastnostmi zdroje dat.

V nabídce „Data“ je upozornění na všechna data, ke kterým existuje odpovídající zdroj.
seznam nebo tabulka s výsečemi již v tabulce nejsou.

.. obrázek:: vložit/seznam-smazaných.png
:alt:Varování před nevyužitým seznamem

Při smazání vloženého grafu se však smaže i zdrojová data.

..._tabulka/vložit/seznam:

Vložte seznam
=============

.. důležité:
Před vložením seznamu do tabulky zkontrolujte, že je seznam přizpůsoben vašim potřebám.
jaké pole by měly být viditelné, a jakým způsobem se mají filtrovat a/nebo řadit záznamy.
Váš sešit bude trvat déle načíst a bude méně uživatelsky přívětivý.

Pro vložení seznamu:

#S příslušnou seznamovou zobrazenou v databázi klikněte na ikonku „fa-cog“.
:guilabel:`(Akce)“ ikonu vedle názvu pohledu a poté :menuselection:`Tabulka –>“.
:ikonka:`OI-VIEW-LIST` :vyber menu:`Vložit seznam do tabulky“.

....... poznámka::
Pokud chcete vložit pouze konkrétní záznamy, vyberte příslušné záznamy a klikněte na ikonku
:tlačítko „Akce“ v horní části střední obrazovky.
:ikonka:`oi-view-list` :guilabel:`Vložit do tabulky“.

#V okně, které se otevře, upravte název seznamu, pokud je třeba.

Seznamové jméno se používá v názvu listu a ve vlastnostech :ref:`seznamu
<spreadsheet/insert/list-properties>.

.... obrázek:: vložit/vložit-seznam.png
:alt:Vložení seznamu do tabulky

#Upravte počet záznamů (řádků), které se mají vložit, pokud je třeba.

Výchozí hodnotou je počet záznamů viditelných na první stránce seznamu.
Příklad: pokud seznam obsahuje 150 záznamů, ale viditelných je pouze 80, tento prvek bude zobrazovat 80.

....... poznámka::
Přitom seznam obsahuje aktuální údaje díky propojení s vaší databází.
vložený seznam nebude automaticky rozšiřovat o nové záznamy, například o nový produkt
nová kategorie nebo nový prodejce.

Pokud očekáváte nové záznamy, zvažte přidání dalších řádků při vkládání seznamu.
Záznamy nebo řádky lze také ručně přidat pomocí odkazu :ref:`<spreadsheet/insert/list-add-records>`.
do tabulky byla vložena.

... příklad::
V současné době máte deset kategorií produktů a tyto přidáváte do
sešit. Pokud vytvoříte jedenáctou kategorii produktů a vaše vložená tabulka obsahovala jen deset
řádky, nová kategorie se vloží do příslušné pozice ve výkrese.
Tímto způsobem se odstraní stávající kategorie.

Jedním ze způsobů, jak tomu zabránit, je přidat další řádky:
při vkládání seznamu.

#Klikněte na „Prázdný sešit“ nebo vyberte existující sešit, do kterého by měl být seznam umístěn.
vloženy.

....... poznámka::
Nové tabulky jsou uloženy v aplikaci **Odoo Dokumenty** buď ve složce :icon:`fa-hdd-o`, nebo
:guilabel:`Můj disk“ osobní pracovní prostor nebo, pokud je použito :ref:`centralizace souborů
<soubory/souborová centralizace> je pro tabulky zapnuta.
:guilabel:`Tabulkový procesor“ pracovní plocha.

#Klikněte na tlačítko „Potvrdit“.

Seznam se vloží do nové listu ve výpočetním programu. V dolní liště vidíme
Jméno seznamu následované identifikátorem seznamu, například „*Citáty celkem (Seznam #1)*“. Panel vpravo
na straně obrazovky se zobrazují vlastnosti :ref:`<spreadsheet/insert/list-properties>`.

..tip:
   - Chcete-li zobrazit záznam jednotlivého položky vložené tabulky, klikněte pravým tlačítkem myši na buňku příslušné řádky.
Pak klikněte na ikonu „Oko“ a poté na název sloupce.
z tabulky v navigačním panelu nahoře na stránce.
   - Pro odpojení seznamu vloženého do databáze vyberte celý seznam.
klikněte pravým tlačítkem a vyberte :icon:`fa-clone` :guilabel:`Copy`, pak znovu klikněte
:menuvolba:`Vložit speciální --> Vložit jako hodnotu“.
   - Nezměňte ID sešitu v názvu tabulky, protože vložená tabulka si ponechává tento identifikátor.
celý životní cyklus tabulky. Tento identifikátor se používá v funkcích :ref:`spreadsheet
<spreadsheet/insert/list-functions>`, které získávají data ze vaší databáze.

..._sešit/vložit/funkce seznamu:

Seznam funkcí
--------------

Při vložení seznamu do tabulky se používají následující funkce:
získat hlavičku a pole.

... blok kódu:: text

=ODOO.LIST.HLAVNÍK(list_id, pole_jméno)
=ODOO.LIST(list_id, index, pole)

Argumenty funkce jsou následující:

- `list_id`: ID přiřazené k seznamu, když je vložen do tabulky. První seznam vložený do tabulky
je přiřazena seznamová ID „1“, druhému seznamovému ID „2“ atd.
- „index“: určuje řádek, na kterém se záznam objevil v seznamu před vložením.
První řádek má index 1, druhý index 2 atd.
- `field_name`: technické jméno pole.

..tip:
Kliknutím na jednotlivé buňky se zobrazí příslušná vzorce (pokud existují) ve sloupci Formule.
zobrazit všechny vzorce tabulky najednou, klikněte na :menuselection:`Náhled --->`.
:ikonka:`fa-eye` :menuvyber:`Zobrazit - Vzorce“ na liště nabídek. Příklad níže ukazuje, jak
funkce používané k získání hlaviček a hodnot seznamů.


:alt: Zobrazení vzorců buněk tabulky

..._sešit/vložit/vlastnosti seznamu:

Seznam nemovitostí
---------------

Seznam vlastností se zobrazí na pravé straně obrazovky, když do dokumentu vložíte seznam.
je přístupný v libovolném čase prostřednictvím nabídky „Data“ pomocí kliknutí na příslušnou sekci, jak je uvedeno
ikonou „OI View List“ (seznam) nebo kliknutím pravým tlačítkem na libovolné místo v seznamu.
kliknutím na ikonu :icon:`oi-view-list` a výběrem položky „Zobrazit vlastnosti seznamu“.

Následující vlastnosti seznamu jsou zobrazeny a některé z nich lze upravit:

- :guilabel:„Seznam #“: ID seznamu. Seznamy jsou přiřazovány postupně, jakmile jsou vytvořeny další
vloženy do tabulky.
- :guilabel:`Název seznamu“: název seznamu. Upravte jej, pokud je potřeba. Poznámka: upravit název seznamu
V seznamu vlastností nezmění název listu zobrazený ve jménu listu a naopak.
- :guilabel:`Model“: model, ze kterého byly data extrahovány.
- :guilabel:`Sloupce“: pole modelu, která byla viditelná při vložení seznamu.
- :guilabel:`Doména“: pravidla, která určují, které záznamy se zobrazí. Klikněte
Editovat doménu v rozhraní pro vyhledávání a filtry (viz Editace domény).

...... poznámka::
Když se používají filtry na úrovni celé aplikace („filtry celého webu“), je tento doménový prostor kombinován s vybraným.
hodnoty globálního filtru před načtením dat do tabulky.

- :guilabel:`Třídění“: jaká je třídící metoda, pokud se používá. Chcete-li přidat pravidlo pro třídění, klikněte
:guilabel:`Přidat“, vyberte pole, pak zvolte, jestli se má řazení :guilabel:`Vzestupně“ nebo
:guilabel:`Sestupně“. Odstranit řazení pravidla kliknutím na ikonu „×“
:guilabel:`(smazat)` ikonu.

Duplikovat nebo smazat
Vyberte zdroj dat seznamu, klikněte na ikonu „Převodník“
ikonu, pak klikněte na ikonu „fa-clone“ nebo „fa-trash“ a zvolte
relevantní.

... _tabulka/vložit/správa seznamu:

Spravovat vložený seznam
-----------------------

Jakmile se seznam z databáze Odoo vloží do tabulky Odoo, můžete:

- :ref:`přidat záznamy <spreadsheet/insert/list-add-records>“, tedy řádky
- „Přidat sloupce“ (viz „Vložit pole <spreadsheet/insert/list-add-fields>“, tj. sloupce).
- :ref:`Duplikovat seznam <spreadsheet/insert/list-duplicate>“ k vytvoření nového, identického datového
zdroj
- :ref:`smazat seznam a jeho podkladový zdroj dat <spreadsheet/insert/list-delete>`

.. _spreadsheet/insert/list-add-records:

Přidat záznamy/sloupce do seznamu
~~~~~~~~~~~~~~~~~~~~~~~~~~

K přidání záznamů do seznamu použijte jednu z následujících metod:

- Vyberte poslední řádek tabulky a přejeďte myší nad modrým čtvercem, dokud se neobjeví ikonka plusu.
Klikněte a přetáhněte dolů, abyste přidali požadovaný počet řádků. Buňky nových řádků jsou vyplněny
s příslušným vzorcem (viz :ref:`spreadsheet/insert/list-functions`) pro získání seznamu
hodnoty. Pokud existují v databázi odpovídající údaje, buňky se vyplní.

.... obrázek: vložit/seznam-přidat-záznam.png
:alt:Přidejte záznamy tahem myši do buňky

- Vložte kurzor do horního levého buněčku listu a klikněte na:
V nabídce Nástroje vyberte položku Listy a v rozevíracím seznamu zvolte příslušný seznam.
počet záznamů k vložení a potvrzení. Do seznamu je vložen aktualizovaný seznam.
přepsání předchozího seznamu.

..tip:
Metody uvedené výše lze použít také k přidání dalších prázdných řádků do tabulky ve vašem sešitu.
se může hodit pro seznamy, kde očekáváte další záznamy v databázi.
např. nové kategorie produktů nebo noví prodejci.

…_sešit/vložit/seznam - přidat pole:

Přidat pole/sloupec do seznamu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Přidat pole/sloupec do seznamu:

#Vyberte sloupec vpravo nebo vlevo od místa, kam chcete nový sloupec vložit.
#Klikněte na „Vložit“ – „>“ – „os-insert-col“ – „Vložení sloupce“.
:ikonka: „vložit sloupec před“ nebo :ikonka: „vložit sloupec za“
z nabídky „Sloupce“ nebo kliknutím pravým tlačítkem a poté :icon:`os-insert-col-before
:guilabel:`Vložit sloupec vlevo“ nebo :icon:`os-insert-col-after“ :guilabel:`Vložit sloupec vpravo“
Je to vhodné.
#Zkopírujte hlavičku libovolného sloupce, vložte ji do hlavičky nového sloupce a stiskněte
„Vstup“.
#Dvojklikem na novém hlavičkovém sloupci otevřete pole s názvem, který se objeví v uvozovkách.
konec vzorce; seznam všech technických názvů polí souvisejícího modelu
Vyskytuje se.

.... obrázek: vložit/seznam-přidat-sloupce.png
:alt:Přidat pole/sloupce upravíte vzorec

#Vyberte vhodný název pole a stiskněte klávesu Enter. V hlavičce se objeví název pole.

......tip:
Pro získání technického názvu pole přejděte na příslušný pohled, aktivujte režim vývojáře
<developer-mode>`, pak zkontrolujte název pole po najetí myší na otazník vedle
název pole.

#S vybraným nadpisem klikněte na modrý čtverec v pravém dolním rohu.
buňky sloupce jsou naplněny vhodným vzorcem, který získá hodnoty seznamu. Pokud
Pokud jsou v databázi odpovídající data, buňky se vyplní.

..._sešit/vložit/duplicitní seznam:

Duplikovat seznam
~~~~~~~~~~~~~~~~

Duplikace seznamu pomocí vlastností seznamu vytvoří další zdroj dat.
různé operace na stejných datech v jedné tabulce.

Se seznamovými vlastnostmi otevřenými klikněte na ikonu „fa-cog“
Poté vyberte ikonu „(gear)“ a zvolte možnost „Duplikovat“.

Nový zdroj dat je přiřazen k dalším volným ID seznamu. Například pokud nejsou žádné další seznamy
vložené mezitím, duplikace výsledků *Seznamu č. 1* vede k vytvoření *Seznamu č. 2*.

Oproti vložení seznamu není duplicitní seznam automaticky vložen do tabulky.
Pro vložení proveďte následující kroky:

#Přidejte novou listovku kliknutím na ikonu „os-plus“ v levém dolním rohu.
tabulky.
#Klikněte na nabídku „Data“ a poté vyberte možnost „Znovu vložit seznam“.
seznam.
#Zadejte počet záznamů, které chcete vložit, a klikněte na „Potvrdit“.
#Upravte pole „Název seznamu“ vlastností, pokud je potřeba.
#. Přejmenujte list kliknutím na záložku listu, výběrem možnosti „Přejmenovat“ a zadáním
nový název listu.

.. poznámka::
Vložený seznam lze zkopírovat a vložit nebo duplikovat list, na který byl vložen.
Vložený řádek nezaloží novou datovou sadu. Když změníte vlastnosti seznamu,
Takže by se tento seznam dostal k veřejnosti a ovlivnil by i všechny kopie.

..._vložení/seznam/smazání:

Smazat seznam
~~~~~~~~~~~~~

Chcete-li zcela odstranit seznam a podkladový zdroj dat ze šablony, proveďte následující
kroky v jakémkoliv pořadí:

- Smažte tabulku v excelovém souboru pomocí svého oblíbeného způsobu, například klávesových zkratek nebo prostřednictvím samotného Excelu.
menu nebo odstraněním listu. Tím se smaže vizuální reprezentace dat.
- V nabídce vlastností seznamu (viz Spustit > Vložit > Seznam vlastností) klikněte na
:ikona „fa-cog“ (kolečko) a poté ikona „fa-trash“ („smazat“). Toto smaže
datový zdroj seznamu z tabulky.

..._excel/vlozit/tabulka s agregacemi

Vložte tabulku s otáčivými body
====================

..tip:
Přeměna vložené tabulky s agregacemi na dynamickou tabulku umožňuje
Vám umožní přidávat, odstraňovat a měnit rozměry (tj. sloupce a řádky) a míry.
Proto je možné vložit základní tabulku s minimální konfigurací, převést ji na
Pokud chcete použít dynamickou tabulku sestav, pak ji můžete upravit přímo v tabulce.

Pro vložení tabulky s otáčivým středem:

#S otevřeným pohledem na příslušnou hlavní tabulku v databázi klikněte na tlačítko „Vložit do sešitu“.
#V okně, které se otevře, upravte název sloupce, pokud je potřeba.

Toto jméno se používá v názvu listu a vlastnostech tabulky s výsečemi
<spreadsheet/insert/pivot-table-properties>.

.. obrázek: vložit/vložit-tabulku-s-položkami.png
:alt:Vložení tabulky s výsečemi do listu

#Klikněte na prázdný list nebo vyberte existující tabulku, do které chcete vložit tabulku s agregacemi.
musí být vloženy.

....... poznámka::
Nové tabulky jsou uloženy v aplikaci **Odoo Dokumenty** buď ve složce :icon:`fa-hdd-o`, nebo
:guilabel:`Můj disk“ osobní pracovní prostor nebo, pokud je použito :ref:`centralizace souborů
<soubory/souborová centralizace> je pro tabulky zapnuta.
:guilabel:`Tabulkový procesor“ pracovní plocha.

#Klikněte na tlačítko „Potvrdit“.

Pivotová tabulka je vložena do nové listu ve výpočetní tabulce. V dolním liště se objeví záložka
Zobrazuje název tabulky sestavované na základě hodnoty následovaný identifikátorem tabulky, např. *Analýza prodejů podle prodeje
Tým (Sloupcový graf č. 1)*. V pravém horním rohu obrazovky se zobrazují vlastnosti sloupcové tabulky
<spreadsheet/insert/pivot-table-properties>.

..tip:
   - Pro zobrazení záznamů odkazovaných jednotlivými buňkami tabulky s výběrem dat klikněte pravým tlačítkem myši na danou buňku.
Pak klikněte na ikonu „Oko“ a poté na název sloupce.
z tabulky v navigačním panelu nahoře na stránce.
   - Pro odpojení vloženého sloupce tabulky a databáze vyberte celý sloupec.
klikněte pravým tlačítkem a vyberte možnost „Kopírovat“ (ikona „fa-clone“, gui label „Copy“), pak
zvolte možnost „Vložit speciálně“ – „Vložit jako hodnotu“.
   - Nepřidávejte do názvu listu ID tabulky sestav, protože vložená tabulka sestav si ponechává tento identifikátor.
pro celou dobu životnosti tabulky. Tento identifikátor je používán v odkazu na
funkcí z rozhraní <spreadsheet/insert/pivot-table-functions-static>, které vyčtou vaše
databáze.

..._tabulkový procesor/vložit/funkce tabulek/statické

Funkce tabulky s otáčivými body
---------------------

Vložená tabulka sloučených dat, která nebyla převedena na dynamickou tabulku
<dynamické tabulky sestavené na základě pivotů> používají následující funkce:
pole hodnot, tj.:

... kódový blok:: text

=PIVOT.HEADER(pivot_id, [doménové pole jméno, ...], [doménový hodnota, ...])
=PIVOT.Hodnota(pivot_id, měřitelný název, [název pole domény, ...], [hodnota domény, ...])

Argumenty funkcí jsou následující:

- `pivot_id`: ID přiřazené ke vkládání tabulky s otáčivými body. První tabulka s otáčivými body, která byla vložena
V tabulce se přiřazuje identifikátor sloupců „1“, druhý identifikátor sloupců „2“ atd.
- `název měřené veličiny`: technický název měřeného jevu následovaný typem agregace.
např. „produkt_jednotka_množství:součet“.
- `název pole domény`: technický název pole používaného jako rozměr, např. „uživatelské ID“, nebo pokud
dimenzí je časový úsek, technický název pole data, následovaný časovým úsekem.
např. „date_order:month“.
- `domain_value`: ID záznamu nebo datum či čas, pokud je dimenze časový úsek
cílený na určité období.

..tip:
Kliknutím na jednotlivé buňky se zobrazí příslušná vzorce (pokud existují) ve sloupci Formule.
zobrazit všechny vzorce tabulky najednou, klikněte na :menuselection:`Náhled --->`.
:ikonka:`fa-eye` :menuvyber:`Zobrazit - Vzorce“ na liště nabídek. Příklad níže ukazuje, jak
funkce používané k získání hlaviček a hodnot statické tabulky.

.. obrázek: vložit/tabulkové výpočty.png
:alt:Funkce statické tabulky s výpočty

..._tabulka/vložit/převodní tabulka:

Vlastnosti tabulky sloučení
----------------------

Vlastnosti tabulky otočných polí se zobrazí na pravé straně obrazovky, když do dokumentu vložíte tabulku otočných polí.
Mohou být kdykoli přístupné pomocí nabídky „Data“ v horním menu kliknutím na příslušný sloupec.
jako předcházející ikoně „OI View Pivot“ (pivot) nebo kliknutím na libovolné místo
pivtové tabulce a kliknutím na ikonu „Zobrazit vlastnosti pivtové tabulky“ (guilabel: Zobrazit vlastnosti pivtové tabulky).

Následující vlastnosti tabulky s otáčivými sloupci jsou zobrazeny a některé z nich lze upravit:

- :guilabel:`ID tabulky s výpočty (pivot) #“: ID tabulky s výpočty je přiřazeno v pořadí, ve kterém jsou přidávány
Pivotové tabulky se vkládají do listu ve formátu tabulky.
- :guilabel:`Jméno tabulky odvozené z rozsahu“: jméno tabulky odvozené z rozsahu. Upravte, pokud je třeba.
Vlastnosti tabulky s výchozími hodnotami nezmění jméno zobrazené v názvu listu a naopak.
- :guilabel:`Model“: model, ze kterého byly data extrahovány.
- Sloupce a řádky: rozměry, které používáte k zařazení nebo seskupení dat.
z modelu.
- :guilabel:`Měření“: co měříte nebo analyzujete na základě rozměrů, které máte
vybrána.

..tip:
Pokud se pokusíte změnit sloupce, řádky nebo měřítka v tabulce s převráceným výčtem,
vložen do tabulky, objeví se chyba nahoře vpravo na obrazovce.

.. obrázek:: dynamic_pivot_tables/pivot-table-error.png
:alt:Chybová hláška při pokusu o manipulaci s pevnou tabulkou

Pro úpravu vlastností tabulky sestav převést statickou tabulku na dynamickou.
:ref:`dynamická tabulka s výpočty <spreadsheet/dynamic-pivot-tables/create>“.

- :guilabel:`Doména“: pravidla, která určují, které záznamy se zobrazí. Klikněte
Editovat doménu v rozhraní pro vyhledávání a filtry (viz Editace domény).

...... poznámka::
Když se používají filtry na úrovni celé aplikace („filtry celého webu“), je tento doménový prostor kombinován s vybraným.
hodnoty globálního filtru před načtením dat do tabulky.

Duplikovat nebo odstranit
Vyberte „vložit“ > „Pivtová tabulka“ > „Zdroj dat“ a klikněte na ikonu „fa-cog“.
:guilabel:`(převodovka)` ikona, pak ikona „Duplikovat“ nebo „Smazat“.
:delete:

..._tabulka/vložit/sloučení tabulek:

Spravovat vloženou tabulku s výsledky
------------------------------

Jakmile do Odoo tabulky vložíte pivtovou tabulku z databáze Odoo, můžete:

- :ref:`Převést ji na dynamickou tabulku s agregacemi <spreadsheet/dynamic-pivot-tables/create>`, abyste
manipulovat s rozměry a měřítky
- :ref:`duplikovat tabulku s výběrem dat <spreadsheet/insert/pivot-table-duplicate>`,
stejná zdrojová data
- :ref:`smazat tabulku s výchozími daty


..._tabulka/vložit/převodní tabulka:

Duplikovat tabulku s výpočty
~~~~~~~~~~~~~~~~~~~~~~~

Duplikace tabulky s otáčivými body prostřednictvím vlastností tabulky s otáčivými body vytváří další zdroj dat.
umožňuje provádět na stejných datech různé operace v jednom sešitu.

Příkladem může být shlukování stejných dat podle různých dimenzí nebo použití :doc:`globálního
filtrů <global_filters> k překrytí data a vytvoření tabulek srovnávajících aktuální
údaje z předchozího období.

Pro duplikaci tabulky s otáčivými body proveďte následující kroky:

#S otevřenými vlastnostmi tabulky pivotu :ref:`<spreadsheet/insert/pivot-table-properties>`, klikněte
Poté vyberte ikonu „Nástroje“ (zobrazenou jako ikona „kolečko“, tj. „gear“) a potom ikonu „Duplikovat“.

Duplikovaná tabulka s výpočty je automaticky vložena do nové listu ve formátu tabulky.
v pravém panelu se otevřou vlastnosti tabulky s výchozími hodnotami.
#Upravte název vlastností a listu, pokud je třeba.

Nový zdroj dat je přiřazen k dalším volným identifikátorům tabulek převrácení. Například pokud neexistují žádné další volné identifikátory tabulek převrácení,
Mezi tím byly vloženy tabulky, které duplikují výsledky *Pivot #1*.
*Otočný bod č. 2*.

.. poznámka::
   - Duplikací vložené tabulky s výsledky pomocí kopírování a vkládání nebo duplikací listu
nebude vytvářet nový zdroj dat. Protože by se změnily vlastnosti tabulky otočení,
se na kopie tabulky s výchozími hodnotami.
   - Při kopírování tabulky s pivoty je nová tabulka vždy automaticky dynamickou tabulkou.
<dynamické tabulky sestupně>.

..._spreadsheet/insert/pivot-table-delete:

Smazat tabulku s výchozími hodnotami
~~~~~~~~~~~~~~~~~~~~

K úplnému odstranění tabulky s výpočty a podkladového zdroje dat v aplikaci Excel proveďte
Kroků v jakémkoliv pořadí:

- Smažte tabulku v excelovém souboru pomocí svého oblíbeného způsobu, například klávesových zkratek nebo prostřednictvím samotného Excelu.
menu nebo odstraněním listu. Tím se smaže vizuální reprezentace dat.
- Vlastnostech panelu vlastností (viz:ref:`spreadsheet/insert/pivot-table-properties`) relevantního
klikněte na ikonu „gear“ (ikona „šroubovák“) a poté na ikonu „delete“ (ikona „koš“).
Tím se smaže zdroj dat pro tabulku přechodů.

…_vložení tabulky/vložení grafu:

Vložte graf
==============

Pro vložení grafu z databáze Odoo do tabulky Odoo:

#Ve vašem databázovém programu otevřete příslušnou grafickou zobrazení a klikněte na tlačítko „Vložit do tabulky“.
#V okně, které se otevře, upravte název grafu, pokud je třeba.

#Klikněte na „Prázdný sešit“ nebo vyberte existující sešit, do kterého by měl být graf vložen.
vloženy.

....... poznámka::
Nové tabulky jsou uloženy v aplikaci **Odoo Dokumenty** buď ve složce :icon:`fa-hdd-o`, nebo
:guilabel:`Můj disk“ osobní pracovní prostor nebo, pokud je použito :ref:`centralizace souborů
<soubory/souborová centralizace> je pro tabulky zapnuta.
:guilabel:`Tabulkový procesor“ pracovní plocha.

#Klikněte na tlačítko „Potvrdit“.

Grafy se vkládají na první list tabulky.

..tip:
Kliknutím na bod v grafu se otevře příslušný pohled v databázi. V ukázce
Kliknutím na „Jessica Childs“ se zobrazí seznam všech prodejů, které tento obchodník uskutečnil.
shodovat se s doménou grafu.

.... obrázek: vložit/klikatelný odkaz na graf.png
:alt:Klikatelný odkaz na menu Odoo a klikatelná data

..._sešit/vložit/vlastnosti grafu

Vlastnosti grafu
----------------

Když do tabulky vložíte graf, vlastnosti grafu se zobrazí na pravé straně
obrazovce. Přístup k nim máte kdykoliv přes nabídku „Data“ v horní liště pomocí kliknutí na příslušný graf.
Předchází mu ikona :icon:`fa-bar-chart` :guilabel:`(chart)` nebo přejděte myší na graf.
Pak klikněte na ikonu „fa-bars“ a „fa-pencil-square-o“.
:edit-guilabel:

Vlastnosti grafu: ikona „fa-sliders“ a „Nastavení“ a ikona „fa-paint-brush“
Karty „Návrh“ vám umožní upravit různé prvky grafu.

Konfigurace
~~~~~~~~~~~~~

Karta Konfigurace obsahuje následující sekce:

- :guilabel:`Typ grafu“: typ grafu. Výchozí hodnota ukazuje typ grafu, který
v grafickém zobrazení databáze před vložením grafu do tabulky.

Po vložení grafu jsou k dispozici další typy grafů. Klikněte na rozbalovací nabídku
vybrat pro data vhodný typ grafu.

...... záložky::

.. tab:: Řádek

.. obrázek: vložit/graf-typ-čára.png
:alt:Ikona grafu

:guilabel:`Čára“: nejlepší pro zobrazení trendů nebo změn v čase, například prodej
růst v průběhu měsíců nebo teplotní výkyvy.

.. obrázek:: vložit/graf-typ-svislá-kostka.png
:alt: Ikona sloupcového grafu

:guilabel:`Skládaná čára“: užitečné pro vizualizaci kumulativních trendů, kde se skládají několik řad
přispívat k celku, například příjmům podle oddělení v čase.

.. sloupec

.. obrázek:: vložit/graf-typ-sloupec.png
:alt: Ikona sloupcového grafu

:guilabel:`Sloupec“: ideální pro porovnání hodnot mezi kategoriemi, jako jsou například tržby na jednu
produkt nebo tržby podle regionu.

.. obrázek:: vložit/graf-typ-sloupcový-zaplněný.png
:alt: Ikona sloupcového grafu

:guilabel:`Sloupcový graf“: zobrazuje vztahy části k celku u kategorií, například
regionální příspěvky na celkové tržby.

.. tab:: Plocha

.. obrázek:: vložit/graf-typ-plocha.png
:alt: Ikona oblastního grafu

:guilabel:`Oblast“: podobná jako čárový graf, ale vyplňuje plochu pod čarami, aby se zvýraznila
velikosti, ideální pro sčítání metrik v čase.

.. obrázek:: vložit/graf-typ-plocha-sestupně.png
:alt: Ikona sloupcového grafu

:guilabel:`Skládaná oblast“: zobrazuje složení změn v čase, například trh
podle kategorie produktu.

.. tab:: Koláč

.. obrázek: vložit/graf-typ-koláč.png
:alt: Ikona grafu

:guilabel:"Koláč": nejlepší pro zobrazení poměrů nebo procent celku, například trhu
podíl nebo rozpočtové přidělení.

... tab:: Jiná

Při vytváření grafu z dat ve formě tabulky je lepší použít možnost „Vložit“ namísto „Zobrazit“.
Kromě výše uvedených grafů jsou k dispozici také následující typy grafů:

.. obrázek:: vložit/graf-typ-svisla-kombinace.png
:alt: Ikona grafu

:guilabel:`Kombinace“: kombinuje více typů grafu (např. čáry a linky) k porovnání různých
datových typů nebo vyznačit klíčové metriky vedle trendů.

.. obrázek:: vložit/graf-typ-svislý.png
:alt: Ikona grafu

:guilabel:`Sloupec“: podobný jako sloupcový graf, ale svislý, což je lepší pro porovnávání
dlouhé názvy kategorií nebo datových sad.

.. obrázek:: vložit/graf-typ-svislý-sloupec.png
:alt: Ikona sloupcového grafu

:guilabel:`Skládané sloupce“: zvýrazňuje součet příspěvků v rámci kategorií, často používané
v analýze demografické nebo alokační.

.. obrázek:: vložit/graf-typ-koláček.png
:alt: Ikona doughnutového grafu

:guilabel:`Koláček“: Varianta sloupcového grafu s prázdným středem, která nabízí podobné informace.
použití, ale s moderním vzhledem.

.. obrázek: vložit/graf-typ-rozptyl.png
:alt: Ikona diagramu rozptylu

:guilabel:`Scatter“: ideální pro analýzu vztahů nebo korelací mezi dvěma čísly
proměnné jako cena versus prodané množství.

.. obrázek: vložit/graf-typ-skládací-přístroj.png
:alt: Ikona grafu

:guilabel:`Gauge“: zobrazuje pokrok k dosažení cíle nebo jediného klíčového ukazatele, například
výkon proti cíli.

... obrázek: vložit/kartografický-typ-skóre.png
:alt: Ikona skóre

:guilabel:`Skóre karty“: používá se pro shrnutí klíčových ukazatelů výkonnosti (KPI).
formátu, jako jsou celkové tržby nebo konverzní poměry, a porovnejte s referenčním bodem nebo předchozím
hodnota.

.. obrázek: vložit/obrazový-typ-vodopád.png
:alt: Ikona vodopádu

:guilabel:'Vodopád': ideální pro vizualizaci kumulativních účinků sekvence pozitivních a
negativní hodnoty, například zisk/ztráta.

.. obrázek:: vložit/obrazový-příkaz-typ-demografické-pyramidy.png
:alt: Ikona grafu populace

:guilabel:`Piramida obyvatelstva“: speciální graf pro porovnávání distribuce, často používaný
v oblasti demografie, například analýze věku a pohlaví.

- „Doména“: pravidla, která určují, které záznamy se zobrazí. Klikněte na „Upravit doménu
Vyberte možnost „Přidat nebo upravit pravidla“ (<search/custom-filters>).
- :guilabel:`Odkaz na menu Odoo“: přidat :ref:`klikací odkaz <spreadsheet/insert/clickable-links>“
od grafu k položce v Odoo, tedy konkrétnímu pohledu na model.

Design
~~~~~~

Podle typu grafu má karta „Návrh“ jednu nebo více možností.
části.

Ve sekci „Obecné“ můžete upravit následující prvky:

- :guilabel:`Barva pozadí“: Přidejte nebo změňte barvu pozadí kliknutím na barevnou tečku.
Vyberte jeden ze standardních barev nebo klikněte na ikonu „+“ pro manuální výběr vlastního barevného
barva.
- :guilabel:`Název grafu“: Upravte název grafu, pokud je třeba. Formát písma, horizontální
Vzhled a barva titulku lze upravit pomocí editoru.
- :guilabel:`Vodorovná osa“: Zvolte, zda je vodorovná osa umístěna na levé nebo
vodorovných, sloupcových a oblastních grafů.
- :guilabel:`Pozice legendy“: Změňte pozici legendy nebo zvolte, že nebude žádná.
- Zapněte možnost „Zobrazit hodnoty“ (Enable :guilabel:`Show values`) a přidejte číselné hodnoty k bodům dat.
graf.
- Povolte možnost „Zobrazit trendovou čáru“ v poli „Guilabel“, abyste mohli přidat trendovou čáru do grafů svislých sloupců a oblastí.

Pro čárové, sloupcové a oblastní grafy je k dispozici sekce „Osa“ (:guilabel:`Axis`), kde můžete přidat titulek pro jednu nebo obě osy.
osy. Formátování písma, horizontální zarovnání a barva titulku lze upravit pomocí
editor.

..._spreadsheet/insert/clickable-links:

Vložte klikatelné odkazy
======================

Přidání odkazů na související nebo podpůrné informace může udělat váš report nebo panel více
Uživatelsky přívětivý a efektivní.

Můžete vložit klikatelný odkaz z jakéhokoli buňky ve výkresu.
do:

- Odoo položka nabídky
- další list v rámci stejné tabulky
- externí URL

.. poznámka::
   - Když na odkazu na položku nabídky kliknete, dostanete se stejným výsledkem jako kdybyste se v menu Odoo pohybovali.
aplikace např. položka nabídky :guilabel:`Prodeje/Objednávky/Nabídky“ odpovídá výchozímu pohledu
při navigaci na:menu:sales --> orders --> quotations.
   - Je také možné vložit klikací odkaz na konkrétní pohled modelu do tabulky.
Začíná od pohledu samotného. Tento způsob však vkládá každý nový odkaz do nové listy.
Je efektivnější vytvářet odkazy na konkrétní pohledy z tabulky.

Můžete vložit klikatelný odkaz z jakékoliv tabulky (viz:spreadsheet/insert/clickable-links-table>).
Odoo položka menu.

..._vložení odkazu do buňky:

Vložte klikatelný odkaz z buňky
-----------------------------------

Vložit klikací odkaz z buňky:

#Klikněte na tlačítko „Vložit“ v nabídce nebo
Klikněte pravým tlačítkem na buňku a poté klikněte na ikonu „Vložit odkaz“ nebo „Vložit hypertextový odkaz“.
Pokud chcete dosáhnout požadovaného výsledku, proveďte jednu z následujících akcí:

   - Klikněte na ikonu „fa-bars“ (menu), pak vyberte možnost „Připojit Odoo menu“. Vyberte
vhodný položku z seznamu nebo klikněte na „Hledat více“ pro výběr ze seznamu
všechny položky nabídky. Klikněte na tlačítko „Potvrdit“.
   - Klikněte na ikonu „fa-bars“ (menu), pak na „Spojovací list“, a poté vyberte
aktuální list tabulky.
   - Do pole „Odkaz“ zadejte URL adresu.

#Zadejte nebo upravte název odkazu v poli „Text“.
#Klikněte na tlačítko „Potvrdit“.

..._spreadsheet/insert/klikací odkazy graf:

Vložte klikatelný odkaz z grafu
------------------------------------

Pro vložení klikacího odkazu z grafu na položku menu Odoo:

#Přejděte na horní pravou část grafu a klikněte na ikonku „Nástroje“
ikona, pak :icon:`fa-pencil-square-o` :guilabel:`Edit“. Vlastnosti grafu se zobrazí v pravé části
obrazovky.
#V dolní části panelu vlastností grafu pod ikonou „Slider“
Pane, klikněte pod nadpisem „Odkaz na nabídku Odoo“, pak vyberte nabídku.

Nahoře vpravo nad grafem se zobrazí nový symbol :icon:`fa-external-link`.
Ikonka „(externí odkaz)“ byla přidána.

...spreadsheet/insert/financial-data:

Vložte finanční údaje
=====================

Při tvorbě reportů a dashboardů se může hodit zahrnout některá účetní data.
například identifikátory účtů, kredity a dluhy pro konkrétní účty a data začátku a konce
Daňový rok.

:ref:`Odoo specifické funkce tabulkového procesoru <spreadsheet/functions/odoo> umožňují získat takové
účetní data z vaší databáze a vložte je do tabulky.
