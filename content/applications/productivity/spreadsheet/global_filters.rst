==============
Globální filtry
==============

Globální filtry reprezentované ikonou „Filtry“ v horní liště
právo na odoo tabulce, které vám umožní aplikovat jeden nebo více filtrů na všechna odoo data.
byly vloženy do této tabulky.

Tyto filtry jsou zvláště užitečné pro zprávy a přehledy, protože uživatelé mohou snadno a dynamicky
Přizpůsobit pohled na odpovědi na složité obchodní otázky, které se týkají více zdrojů dat.

..tip:
Když se do panelu přidá tabulka s globálními filtry, filtry se zobrazí jako výběr.
nabídky v horní části panelu nástrojů. V tabulce se zobrazují v pravé části okna.
spreadsheet.

.... obrázek: global_filters/dashboard-global-filters.png
:alt:Filtry na celé obrazovce v horní části panelu

K dispozici jsou tři typy globálních filtrů:

- :ref:`Datum <spreadsheet/global-filters/create-date>“: filtruje data podle konkrétního časového rozsahu
s možnostmi „Měsíc/Čtvrtletí“, „Relativní období“ nebo „Od /
Tak.
- :ref:`Vztah <spreadsheet/global-filters/create-relationship>“: filtruje data podle vztahu
pole v souvisejícím modelu, např. pole „Prodavač“ s modelem *Uživatel* nastaveným jako
související model.
- :ref:`Text <spreadsheet/global-filters/create-text>`: filtruje data podle řetězce textu nebo
rozsah předdefinovaných hodnot, např. odkaz na produkt nebo čárový kód.

Na rozdíl od běžného filtru ve formátu tabulky „:icon:`fa-filter`“ :guilabel:`(Přidat filtry)“, který vám umožní
třídit a dočasně skrývat data. Filtry na úrovni aplikace se vztahují na podkladová :ref:`data
<spreadsheet/insert/data-sources>“, filtrování dat před jejich načtením do tabulky.

Když je vytvořen globální filtr, :ref:`souhlasí s poli <spreadsheet/global-filters/field-matching>
pro každý zdroj dat zajišťuje filtr, že se na správnou databázi aplikuje pole :doc:`dat
</aplikace/studio/poli>`.

..tip:
   - Globální filtry fungují tak, že přidávají další podmínky do domén všech zdrojů dat v
Protože se jedná o tabulkový procesor, neměli byste používat stejné podmínky pro globální filtry.
při konfiguraci prvotního seznamu, tabulky nebo grafu ve vaší databázi.
   - Při nastavení výchozích hodnot se zajistí rychlé načítání tabulky nebo panelu.
a poskytuje užitečný první pohled, který lze dále upravit podle potřeby. Například
Filtr „Datum“ mohl být nastaven tak, aby zobrazoval data za posledních 30 dní.

..._tabulka/globální filtry/shoda polí:

Souhlas s používáním souborů cookie
==============

.. důležité:
Tento proces je zásadní, protože při shodě s nesprávnými poli nebo vůbec nezvolené shodě polí
Výsledkem jsou globální filtry, které neukazují požadované výsledky.

Aby fungovaly tak, jak mají, globální filtry musí pracovat s těmi správnými poli v databázi.
Filtr „Datum“ aplikovaný na prodejní data. Model „Objednávka“ obsahuje několik dat
Je důležité určit, které pole je pro filtr relevantní, např. datum objednávky,
datum dodání, očekávané datum nebo datum vypršení platnosti.

Při vytváření globálního filtru podle návodu v části Vytvoření globálních filtrů se používá pole
sekce „Souhlas“ v části „Vlastnosti filtru“ umožňuje určit, zda je pro každý
:ref:`datový zdroj <spreadsheet/insert/data-sources>“ v tabulce, který pole databáze
filtr by měl působit na nebo odpovídat.

Více se o poli shody dočtete v příslušných kapitolách týkajících se vytváření
:ref:`Datum <spreadsheet/global-filters/create-date>“
:ref:`Vztah <spreadsheet/global-filters/create-relationship>“
:ref:`Text <spreadsheet/global-filters/create-text>“ globální filtry.

.._tabulkový procesor/globální filtry/vytvořit:

Vytvořit globální filtry
=====================

Zvolte požadovaný sešit v aplikaci **Odoo Dokumenty** nebo přes aplikaci **Odoo Dashboardy**.
Přidáváte filtry na panel nástrojů.

..tip:
Chcete-li zobrazit podkladový sešit tabulek s aplikací Dashboards otevřenou,
:ref:`zapnout vývojářský režim <developer-mode>“, pak klikněte na ikonu
:guilabel:`(Upravit)` ikona, která se zobrazí při přejetí myší nad názvem panelu.

Chcete-li přidat nový filtr, klikněte na ikonu :icon:`os-global-filters` a poté pod položkou :guilabel:`Filters
Nová filtrace ... klikněte na „Datum“, „Příbuzní“ nebo „Text“ podle potřeby.
Otevře se panel vlastností filtru.

Při ukládání globálního filtru se zobrazí chybová hláška, pokud některá ze žádaných informací chybí nebo pokud je poskytnutá informace nesprávná.
v části „Souhlas s políčkem“:ref:`<spreadsheet/global-filters/field-matching>`,
zobrazí se chybová hláška „Některá povinná pole nejsou platná“.

..._tabulka/globální filtry/vytvořit datum:

Datum
----

.. poznámka::
A filtr „Datum“ může být použit jen s :ref:`Datem <studio/fields/simple-fields-date>`.
nebo pole :ref:`Datum a čas <studio/fields/simple-fields-date-time>`.

Při otevřeném panelu vlastností filtru:

#Zadejte název nového filtru data do pole „Štítek“.
#Vyberte jednu z následujících možností ze seznamu „Časový rozsah“:

   - :guilabel:Měsíc / Čtvrtletí: umožňuje vybrat konkrétní měsíce a čtvrtletí.
ročníkový výběr roku. Hodnoty :guilabel:`Měsíce“ a :guilabel:`Čtvrtletí“ jsou povoleny
výchozím nastavení. Vypnutím obou hodnot umožňuje filtrování pouze podle roku.

Chcete-li nastavit výchozí hodnotu, povolte
:guilabel:`Automaticky filtrovat podle aktuálního období“ a vybrat, zda chcete filtrovat podle
současný měsíc, čtvrtletí nebo rok.

   - :guilabel:„Relativní období“: umožňuje vybrat si z roletky konkrétní časové úseky vzhledem k
datum v aktuální době (např. „Rok doposud“, „Posledních 7 dní“ apod.)
:guilabel:`Poslední 30 dní“, atd.

Chcete-li nastavit výchozí hodnotu, vyberte jednu z dostupných možností.

   - „Od/Do“ umožňuje „Datum od…“ a „Datum do…“
vybrat pole pro určení konkrétního časového rozmezí (např. „06/05/2024“ do „06/27/2024“).

#V části „Souhlas s poli“ klikněte pod každým zdrojem dat na pole „Datum
Vyberte pole, se kterým by filtr měl souhlasit.

:guilabel:`Výchozí období` umožňuje porovnání posunutím času.
rozsah o jeden nebo dva období v minulosti nebo budoucnosti. Výchozím nastavením není žádné posunutí doby.
K dispozici jsou následující odsazení: :guilabel:`Předchozí“, :guilabel:`Před předchozím“ a „Následující“.
:guilabel:`Po příštím“.

......tip:

Chcete-li porovnávat data efektivně pomocí funkce „Výchozí období“, je nutné duplikovat
relevantní vložený seznam <spreadsheet/insert/list-duplicate> nebo tabulka s výsečemi
<spreadsheet/insert/pivot-table-duplicate>`, pak při nastavování shody polí zvolte
posunutí období pro druhou datovou sadu, ale ne pro první.

Při aplikaci filtru se v původním seznamu nebo tabulce s klíčovými poli zobrazí data za zadané časové období.
vybrána, zatímco druhá zobrazuje data pro období před nebo po tomto časovém rozmezí.
definována.

#Klikněte na tlačítko „Uložit“.

Příklad:
V následujícím příkladu je vytvořen globální filtr „Datum“, který umožňuje převrátit tabulku
a graf, který ukazuje prodejní data za čtvrtletí. Pokud je vybrán pouze jeden rok, jsou zobrazeny údaje za celý rok.
celý rok.

.... obrázek: global_filters/example-date.png
:alt:Filtr na čtvrtletí a rok

V části „Souhlas s polem“ vlastností filtru je pole, ve kterém
:guilabel:`Datum objednání“ je vybrána jako pole shodného data. Shodné pole dat není
potřebné pro filtr *Seznam 1*, protože tento filtr nebudeme používat na zdroji dat v otázce.

.... obrázek::global_filters/field-matching-date.png
:alt:Filtr dat s vybraným sloupcem Datum objednávky jako kritériem
:skalka: 80 %

..._tabulka/globální filtry/vytvořit vztah:

Vztah
--------

.. poznámka::
A filtr „Vztah“ může být použit jen s vazbou „Mnoho na jeden“.

<studia/pole/vztahová pole - jedno k mnoha>“, nebo :ref:`Mnoho k mnohu
pole typu <studia/pole/vztahové-pole-many2many>.

Při otevřeném panelu vlastností filtru:

#Zadejte název nového filtru vztahů do pole „Štítek“.

#V poli „Související model“ začněte psát název modelu, abyste zobrazili seznam všech
modely, pak vyberte vhodný. Jakmile si vyberete jeden z modelů,
:guilabel:`Výchozí hodnota“ a :guilabel:`Možná hodnota“ pole.
:guilabel:`Souhlas s poli“ část.

#. Chcete-li nastavit výchozí hodnotu, vyberte jednu z dostupných možností; tyto jsou záznamy
modelu. Pokud je s tímto modelem spojený model *Uživatel*, pak se použije možnost :guilabel:`Automaticky filtrovat
lze zapnout na aktuálním uživateli.

#.Chcete-li omezit hodnoty zobrazované na obrazovce, zapněte možnost „Omezení hodnot s doménou“, pak
Klikněte na tlačítko „Upravit doménu“ (viz odkaz: Edit domain) a přidejte nebo upravte pravidlo.

#V části „Souhlas s políčkem“ zkontrolujte, jestli je správné pole pro shodu vybráno.
přiřazené každému zdroji dat. Pokud tomu tak není, klikněte pod jménem zdroje dat na
vyberte správné pole.

#Klikněte na tlačítko „Uložit“.

Příklad:
V následujícím příkladu je vytvořen filtr :guilabel:`Relace`, který umožňuje použití tabulky s otáčivými hodnotami.
a graf, který ukazuje prodejní údaje spojené pouze s vybranými obchodníky. Model *User* byl nastaven jako
:guilabel:`Související model“.

.... obrázek:: global_filters/příklad-vztahu.png
:alt:Filtr vazeb na tabulce sestavené z pivtového výstupu

V části „Souhlas s polem“ vlastností filtru je pole, ve kterém
:guilabel:`Prodejce“ byl automaticky přiřazen jako odpovídající pole pro oba sloupce v tabulce sestupně
a graf. Pro pole „Seznam 1“ není potřeba shodné pole, protože tento filtr na něj nepoužijeme.
zdroj dat v otázce.

.... obrázek::global_filters/field-matching-relation.png
:alt: Filtr vztahů s konfigurací modelu uživatele
:skalka: 80 %

..._tabulka/globální filtry/vytvořit text:

Text
----

.. poznámka::
A filtr „Text“ může odpovídat pouze textu („znak“)
<studia/pole/jednoduché-pole-text>, :ref:`Číslo <studia/pole/jednoduché-pole-číslo>` nebo
:ref:`Desetinné pole (float) <studia/poli/jednoduchá-pole-desetinné>“.

Při otevřeném panelu vlastností filtru:

#Zadejte název nového filtru v poli „Štítek“.
#Pokud chcete, zapněte možnost „Omezit hodnoty na rozsah“. Po zapnutí této funkce můžete zadat
Spustit buňky v rozsahu tabulky buď zadáním rozsahu nebo výběrem jejich obsahu ze samotné tabulky.
#Pokud chcete, zadejte hodnotu výchozího nastavení:
#V sekci „Soulad polí“ klikněte pod názvem zdroje dat.
a vyberte pole, na které se filtr „Text“ má vztahovat.

#Klikněte na tlačítko „Uložit“.

Příklad:
V následujícím příkladu byla vytvořena globální filtrace :guilabel:`Text`, která umožňuje uživateli vybrat
produkt z filtru „Produkty“ a pouze v tabulce a grafu zobrazit
údaje o prodejích konkrétního produktu.

.. obrázek:: global_filters/example-text.png
:alt:Globální filtry nastavené v tabulce s otáčivým středem

V dialogovém okně Filtr vlastností je možné zobrazit hodnoty filtru v poli Možná hodnota.
je omezena na rozsah „Produkty (Seznam 1)“!A2:A34. To odpovídá rozsahu
obsahující název produktu v seznamu vloženém do tabulky.

.... obrázek: global_filters/field-matching-text.png
:alt: Filtr s omezeným rozsahem
:skalka: 80 %

S touto konfigurací lze filtrovat tabulku sestav a graf podle názvu produktu.
Vybrat jednu z předdefinovaných hodnot dostupných v textovém filtru. V tomto případě
:guilabel:`Nábytek“ již byl vybrán jako :guilabel:`Kategorie produktu“, což znamená
že se mohou vybrat pouze produkty z této kategorie jako možné hodnoty.

Dalšími důvody jsou například to, že hodnoty v rozsahu byly získány dynamicky ze serveru databáze.
V tomto případě je filtr textu také dynamický a odráží změny provedené na těchto hodnotách.

Spravujte a používejte globální filtry
=============================

Klikněte na ikonu „Filtry“ v pravém horním rohu odoo tabulky.
přistupovat k globálním filtrům, které pro tuto tabulku vytvořili.

Je možné:

- Použijte jeden nebo více globálních filtrů a vyberte pro ně vhodná nastavení, pokud je to nutné.

..tip:
Při znovu načtení prohlížeče se všechny globální filtry vrátí do svého výchozího stavu nebo výchozí hodnoty.
hodnotu, pokud je to vhodné.
globální filtry, které byly použity, klikněte na položku „Údaje“ a poté na „Obnovit všechna data“.
nabídka.

- **Změňte pořadí filtrů** stisknutím na filtru a použitím
:icon:`os-thin-drag-handle` :guilabel:`(přetahovací rukojeť)` ikonu pro změnu pozice.
- Zrušit výchozí nebo vybrané filtrační hodnoty kliknutím na ikonu „fa-times“
:guilabel:`(Zobrazit vše)` ikonu vedle hodnoty filtru.
- Upravte existující filtr klepnutím na ikonu :icon:`fa-cog` :guilabel:`(Edit)` pro otevření
Filtr lze upravit vlastnostmi filtru, které jsou k dispozici pod tlačítkem „Vlastnosti filtru“.
- **Smazat existující filtr** vybráním ikony :icon:`fa-cog` :guilabel:`(Upravit)` pro otevření
Poté zvolte vlastnosti filtru a klikněte na „Odebrat“.
