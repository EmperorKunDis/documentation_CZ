====================
Dynamické tabulky s přehledy
====================

Pokud je vložený pohled na databázi Odoo do tabulky, je výchozím nastavením statický.
pivotní tabulka. Každá buňka statické pivotní tabulky obsahuje funkci specifickou pro Odoo:
<spreadsheet/insert/pivot-table-functions-static>“), která získává data ze vaší databáze.

.. obrázek: dynamické tabulky/funkce pivot-statická.png
:alt:Funkce statické buňky tabulky s výpočtem

Když se změní odpovídající data v databázi, například prodeje související s daným čtvrtletím nebo
individuální prodejce, buňky vaší statické tabulky se aktualizují.

Statická tabulka s pivoty však není schopna automaticky rozšířit svůj rozsah na nová data, například prodeje
údaje za nový kvartál nebo pro nově přijatého obchodníka. Není možné ani přidávat, ani manipulovat
rozměry (sloupce nebo řádky) nebo měřítka vlastnostmi tabulky přehledů.

.. poznámka::
Pokud se pokusíte aktualizovat nebo změnit vlastnosti tabulky sestupně, která byla právě vytvořena
Vložený do tabulky se zobrazí chybová hláška v pravém horním rohu obrazovky.

.... obrázek: dynamických tabulek/chyba-v-tabulce-s-pohyblivými sloupci.png
:alt:Chybová hláška při pokusu o manipulaci s pevnou tabulkou

Pro větší pružnost při manipulaci s tabulkou otočných hodnot můžete:
Pivotní tabulka z dynamické tabulky s přehledem.

.._spreadsheet/dynamic-pivot-tables/create

Vytvořte dynamickou tabulku s otáčivými sloupci
============================

Existují dvě hlavní možnosti, jak vytvořit dynamickou tabulku z pevné tabulky:

- *Duplikovat statickou tabulku z vlastností tabulek*:
vlastnosti <spreadsheet/insert/pivot-table-properties>`, klikněte na ikonu „fa-cog“
Klikněte na ikonu „Nástroje“ v pravém horním rohu panelu a poté klikněte na ikonu „Duplikovat“.
:guilabel:`Duplicitní“.

Vytvoří se nový zdroj dat a do nové tabulky se vloží dynamická verze sestavy.
listu. Dynamická tabulka sestav je stejně ozdobená jako původní tabulka sestav.

...... poznámka::
Pokud použijete tento postup, nová dynamická tabulka sestav bude mít následující dostupnou hodnotu ID.
To znamená, že můžete vytvořit více různých pohledů na stejný model, ale s odlišnými daty.
nastavení, skupiny nebo výpočty.

- **Vložte dynamickou tabulku sestav z nabídky Nástroje**: Na listu, který obsahuje vaši statickou
pivotovou tabulku, umístěte kurzor do prázdné buňky. Klikněte na:
:ikona: „Vložit dynamický sloupec“ z nabídky, pak vyberte
relevantní tabulku sloupců.

Přiřadí se nová dynamická tabulka sestav, která má stejné uspořádání jako původní tabulka sestav.

...... poznámka::
Při použití této metody je statická a dynamická pivota připojena k jednomu zdroji dat.
Protože se používá stejná identifikace otáčení, je třeba smazat původní statickou tabulku otáčení.

..tip:
Je také možné přímo zadat funkci
v prázdné buňce tabulky dynamických sloupců.
Avšak s touto metodou je nutné styl tabulky ručně znovu aplikovat.

.. _excel/dynamicky_rozsahy/funkce:

Dynamické funkce tabulky otočných bodů
-----------------------------

V každé buňce místo jedinečné funkce, která získává data ze vaší databáze, je
:ref:`statická tabulka s výpočty <spreadsheet/insert/pivot-table-functions-static>“, dynamická tabulka
je jediným účelem:

... blok kódu:: text

pivot_id, počet řádků, zahrnout celkový součet, zahrnout titulky sloupců, počet sloupců

Argumenty funkce jsou následující:

- `pivot_id`: ID přiřazené při vložení tabulky s otáčivými body. První tabulka
Vložené do tabulky se přiřazuje identifikátor sloupce „1“, druhý identifikátor sloupce „2“ atd.
- „Počet řádků“ a „počet sloupců“: počet řádků a sloupců.
- „include_total“ a „include_column_titles“: hodnoty 0 odstraní celkové číslo a sloupec
Vítězství si připsali v kategorii žen a mužů.

Jedná se o pole funkci, která umožňuje rozšíření tabulky sestav na základě
výsledky funkce.

V horním levém buňce je funkce pro úpravy, pokud na kteroukoliv jinou buněčnou se ukáže.
formulář je šedivý.

.. obrázek: dynamické tabulky/pivot-funkce-dynamicky.png
:alt:Funkce pole dynamické tabulky

..tip:
Pokud je třeba, můžete aktualizovat funkci dynamické tabulky sestav na odstranění prvků jako
celkové nebo sloupcové titulky.

S funkcí otevřenou v řádku formulářů nebo horním levém buňce tabulky sestav přesuňte
po položce s identifikátorem klíčového sloupce a poté zadejte znak ,, abyste se dostali do volitelného pole, které chcete změnit.
Příklad níže ukazuje hodnotu 0 pro [include_total], což odstraňuje řádkový součet a
součet sloupce z tabulky sestavené na základě pivota.

.... obrázek::dynamic_pivot_tables/modify-function.png
:alt:Modifikace funkce dynamické tabulky s klíčovými slovy

.._excel/dynamické_rozšířené_tabulky/upravit:

Manipulovat s dynamickou tabulkou s kalkulačkami
================================

Pro manipulaci s daty v dynamické tabulce sloučení: otevřete vlastnosti tabulky sloučení
<spreadsheet/insert/pivot-table-properties>.

Následující možnosti jsou k dispozici po kliknutí na ikonu :icon:`fa-cog` (:guilabel:`gear`)

- :icon:`fa-exchange` :guilabel:`Otočit osy“: přesunout všechny rozměry reprezentované sloupci na
řádky a naopak.

..tip:
Převrácení os poskytuje nový pohled na data, možná přinesou nové informace.
poznatky. V závislosti na objemu dat však může vést k chybám #SPLIT.
se stane, když se pokusíte vytisknout řadu hodnot, ale něco blokuje tyto hodnoty.
buňky, jako jsou jiné datové řádky, sloučené buňky nebo hranice aktuální listiny.

Přesouváním kurzoru nad buňkou obsahující #SPILL zobrazíte chybu.

- :icon:`fa-clone` :guilabel:`Duplikovat“: duplikovat dynamickou tabulku sestav a vytvořit nová data
zdroj s jedinečnými vlastnostmi.
- :icon:`fa-trash` :guilabel:`Smazat“: k odstranění zdroje dat dynamické tabulky.

...... poznámka::
Pokud odstraníte zdroj dat pro tabulku přechodu, neodstraníte vizuální reprezentaci.
data. Smazat tabulku z listu v programu Excel pomocí vašeho oblíbeného způsobu, například klávesnicí
příkazy, menu tabulek nebo odstraněním listu.

..._spreadsheet/dynamic-pivot-tables/manipulate-dimensions

Rozměry
----------

Rozměry tabulky s otáčením, tedy způsob uspořádání dat, jsou umístěny v poli :guilabel:`Sloupce
a „řádky“ podle toho, jak se zobrazily v přehledové tabulce ve vaší databázi, tj. před
Pivotová tabulka byla vložena do sešitu.

Můžete:

- Přidat nové rozměry kliknutím na tlačítko „Přidat“.
- odstranit existující rozměry kliknutím na ikonu „Odstranění“
relevantní rozměr
- změnit pořadí zobrazovaných rozměrů v poli sloupců nebo řádků
kliknutím a tahem rozměru na požadované místo v příslušné sekci
- změnit osu, na které je zobrazena dimenze, kliknutím a táhnutím dimenze.
:guilabel:`Sloupce“ na :guilabel:`Řádky“ nebo naopak
- změnit pořadí hodnot rozměru vybráním možnosti „Vzestupně“
:guilabel:`Sestupně“, nebo :guilabel:`Nesrovnaně“ v poli :guilabel:`Řadit podle“
- pro rozměry dat nebo času vyberte požadovanou „granularitu“ z nabízených možností
nabídka

..._tabulka/dynamické tabulky/upravit měřítko:

Opatření
--------

Měřítka vaší tabulky otočných hodnot, tedy co měříte nebo analyzujete na základě
rozměry, které jste si vybrali, jsou uvedeny v pořadí, v jakém se objevily ve svislém zobrazení.
databáze.

Můžete:

- zavést nové metriky, včetně:ref:`vypočítaných metrik
<spreadsheet/dynamic-pivot-tables/manipulate-measures-calculated-measures>`, kliknutím
:guilabel:`Přidat“
- ukrýt (:ikonka: „fa-eye“), zobrazit (:ikonka: „fa-eye-slash“) nebo smazat (:ikonka: „fa-trash“) existující měření
- upravit název stávajících opatření kliknutím na název opatření
- změnit pořadí měřítek kliknutím a tahem myši na měřítko.
požadovaná pozice
- změnit způsob zobrazení měření kliknutím na ikonu „fa-cog“ (gear) a poté
vybráním požadované možnosti z nabídky, např. :guilabel:`z celkového počtu %“.
:guilabel:`Řadit podle nejmenšího po největší“. Data v tabulce se dynamicky aktualizují, když používáte různé
jsou vybrány.
- vyberte, jak se měření agregují například: guilabel:Sum, guilabel:Average
:guilabel:`Minimální“

... _excel/dynamické_rozšířené_tabulky/upravujte_měřítka_a_vypočtená_měřítka:

Vypočítané opatření
~~~~~~~~~~~~~~~~~~~

Pokud požadovaná měřítka nebyla v původním roztaženém objektu, je možné přidat vypočtené měřítko.
výhled. Například může být přidána výpočetní metrika, která ukazuje průměrný příjem na objednávku nebo
marže na produkt.

Přidat vypočítanou míru:

#V sekci „Měřítka“ vlastností tabulky přesunutí klikněte na tlačítko „Přidat“.
#Pod seznamem kalkulovaných měřítek klikněte na ikonu „Formule“ a poté na „Přidat kalkulovanou měrnou jednotku“.
#Přejmenujte vypočítanou měrnou jednotku kliknutím na název a zadáním nového názvu.
#Klikněte na řádek začínající znakem „=“ a vložte formuli.

...... příklad::
V následujícím příkladu je průměrná výše tržby na objednávku počítána vydělením součtu prodeje.
podle počtu objednávek.

.. obrázek: dynamické tabulky/počítaná měřidla.png
:alt: Vzorec pro výpočet měřené veličiny

#Vyberte, jak měření chcete agregovat, vybráním hodnoty z roletky.

..tip:
Použití statické tabulky s kloubem má své výhody. Například je možné vidět funkce
za jednotlivými buňkami. Chcete-li tuto možnost využít, vyberte příslušnou část dynamického
pivotovou tabulku, zkopírujte ji a vložte do prázdné části listu. Klikněte na jakýkoliv vložený buňky.
podívejte se na funkci :ref:`Odoo <spreadsheet/functions/odoo>`, která se používá k získání dat.

