====================
Servisní kalendář
====================

.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`

Zamezení poruch a zablokování pracovišť skladu vyžaduje neustálou údržbu.
údržba. Včasná opravná údržba strojů a nástrojů, které se náhle porouchají, stejně jako
preventivní údržba je klíčová k tomu, aby se takové problémy vyhýbaly.
Provoz běží hladce.

V Odoo Maintenance mohou uživatelé přistupovat k kalendáři údržby a vytvářet, plánovat a upravovat
obě opravárenské a prevenční požadavky na údržbu, aby bylo možné sledovat vybavení i pracoviště.

Vytvořit požadavek na údržbu
==========================

Požadavky na údržbu lze vytvářet přímo z kalendáře údržby.
kalendář, přejděte na:menu: `Údržba aplikace --> Údržba --> Kalendář údržby`.

Pro vytvoření nové žádosti klikněte na jakoukoli část kalendáře. To způsobí otevření „Nové události“.
plovoucí okno. V poli „Název“ přiřaďte novému požadavku název.

.. obrázek: maintenance_calendar/maintenance-calendar-new-event-popup.png
:align:center
:alt: Nové okno pro vytváření událostí.

Kliknutím na tlačítko „Vytvořit“ v okně s výzvou se uloží nový požadavek bez dalších podrobností.
Pokud má být požadavek zrušen, klikněte na tlačítko „Zrušit“.

Pro přidání dalších podrobností a naplánování požadavku na určitý den a čas klikněte na tlačítko „Upravit“.

Kliknutím na tlačítko „Upravit“ se otevře prázdná žádost o údržbu, kde lze zadat různé podrobnosti o
žádost lze vyplnit.

Upravit požadavek na údržbu
------------------------

V poli „Žádost“ přiřaďte nové žádosti název. V poli „Vytvořeno uživatelem“
Z pole „Uživatel“, které se nachází v rozbalovacím menu, vyberte uživatele, který požadavek vytvořil. Výchozí hodnotou je
populace s uživatelem, který vytváří požadavek.

.. obrázek: maintenance_calendar/maintenance-calendar-new-request-form.png
:align:center
:alt: Vytvoření nové žádosti o údržbu.

V poli „Pro“ z rozevírací nabídky vyberte, jestli je tento požadavek vytvářen pro
součástí „Vybavení“ nebo „Střediska práce“.

.. poznámka::
Pokud je v rozevíracím seznamu pole „Pro“ vybráno „Work Center“, zobrazí se dvě
Do formuláře se objeví další pole: „Dílna“ a „Blok dílen“.

V poli „Správní středisko“ vyberte, které správní středisko v skladu bude tato údržba
se týká.

Pokud je zaškrtnutá volba „Blokový pracovní stůl“, není možné plánovat práci.
objednávky nebo jiné požadavky na údržbu během doby trvání této žádosti
které se koná.

Pokud je vybráno pole „Vybavení“ ve výchozím nastavení, vyberte
Který stroj nebo nástroj vyžaduje údržbu ze seznamu „Stroje“.
je vybráno zařízení, v poli kategorie se objeví šedé pole s názvem
Kategorii vybavení, ke kterému se vybavení řadí.

V poli „Šablona listu“ klikněte na vykřičník v případě potřeby.
šablony pracovních listů. Tyto šablony jsou vlastní šablony, které mohou být vyplněny zaměstnanci
Prováděním údržby.

Pod položkou „Kategorie“ se zobrazuje datum požadované podle položky „Datum žádosti“.
aby se údržba mohla uskutečnit.

V poli „Typ údržby“ je k dispozici dvě volitelná tlačítka s možností výběru:
„Korektivní“ a „preventivní“.

:guilabel:`Korektivní“ údržba je pro požadavky, které vznikají z okamžitých potřeb, jako například rozbité
provozní zařízení a zatímco „preventivní“ údržba je pro plánované požadavky, aby se předešlo poruchám
budoucnost.

Pokud je tato požadavek spojen s konkrétním |MO|, vyberte z nabídky :guilabel:`Výroba
Pole „Objednávka“.

Vyberte požadovaný tým údržby z rozbalovací nabídky pole „Tým“ a
provést údržbu. V poli „Odpovědný“ vyberte technika zodpovědného za
Žádost.

.. obrázek:obsluha_kalendare/kalendar-vyplneny-vzor.png
:align:center
:alt:Vyplněný požadavek na údržbu.

V poli „Datum“ klikněte na datum, abyste otevřeli kalendářové okno.
popover, vyberte plánovaný termín údržby a klikněte na tlačítko „Použít“ pro uložení data.

Do pole Délka zadejte počet hodin (ve formátu 00:00).
plánuje se údržba.

V poli Priorita vyberte prioritu mezi jednou a třemi hvězdičkami.
Toto ukazuje na důležitost požadavku na údržbu.

Pokud pracujete v prostředí více společností, z rozevírací nabídky pole „Společnost“
vyberte společnost, ke které se tento požadavek na údržbu vztahuje.

Na spodní části formuláře jsou dvě záložky: „Poznámky“ a „Návody“.

V záložce „Poznámky“ zadejte všechnu interní poznámku pro tým nebo servisního technika přiřazeného k
pokud je třeba.

V záložce „Návod“ je možné vybrat jednu ze tří variant volby tlačítka
poskytnout údržbářským týmům nebo technikům pokyny k údržbě. K dispozici jsou různé metody
Pokud jsou pokyny v PDF, Google Slide nebo Text.

.. obrázek: maintenance_calendar/maintenance-calendar-instructions-tab.png
:align:center
:alt:Možnosti záložky Návod na požadavek na údržbu.

Kalendářní prvky
=================

Kalendář údržby nabízí různé pohledy, funkce vyhledávání a filtry, které pomáhají sledovat
o průběhu probíhajících a plánovaných požadavků na údržbu.

Následující části popisují prvky, které se nacházejí v různých pohledech kalendáře.

Filtry a oblíbené položky
---------------------

Přejděte na: „Aplikace pro údržbu --> Údržba -->
Servisní kalendář.

Pro přidání a odstranění filtrů pro třídění dat v kalendáři údržby klikněte na:
(trojúhelník směřující dolů) ikona vedle vyhledávací lišty na horní části stránky.

Výsledný seznam nabídek obsahuje všechny různé filtry uživatelů.
můžete vybrat. Výchozí výběr je „Dělat“ a „Aktivní“, takže všechny otevřené požadavky
Je zobrazena.

..tip:
Chcete-li k kalendáři údržby přidat vlastní filtr, klikněte na tlačítko „Přidat vlastní filtr“.
„Filtr“, který je v sekci „Filtry“ na vyskakovacím menu. To otevře
:guilabel:`Přidat vlastní filtr“ okno.

z okna s vyskakovacím dialogem nastavte vlastnosti nové pravidlo filtru a poté je připraveno k použití.
klikněte na tlačítko „Přidat“.

V levém sloupci seznamu vyhledávání je uvedeno „Oblíbené“ nebo „Hledané“, což jsou
Uložit si ho jako oblíbený, abychom se k němu mohli vrátit později.

.. obrázek: maintenance_calendar/maintenance-calendar-favorites-popover.png
:align:center
:alt: sekce oblíbených filtrů v rozbalovacím menu.

Chcete-li uložit nový výběr oblíbených položek, vyberte požadované filtry. Potom klikněte
:guilabel:Uložit aktuální vyhledávání“. V poli přímo pod tímto :guilabel:Uložit aktuální vyhledávání“ zadejte
jméno do vyhledávání.

Pod zadaným názvem jsou dvě možnosti, buď uložit aktuální vyhledávání jako
„Výchozí filtr“ nebo „Sdílený filtr“.

Vybráním filtru „Výchozí filtr“ nastavíte tento filtr jako výchozí při otevření tohoto kalendáře.
pohled.

Vybráním filtru „Sdílený“ se tento filtr stane dostupný i pro ostatní uživatele.

Jakmile je vše připraveno, klikněte na tlačítko „Uložit“. Po kliknutí se zobrazí nový filtr „Oblíbené“
sloupec „Oblíbené“ a s ikonkou „hvězdičky“ se objeví u názvu filtru.
vyhledávací lišta.

Názory
-----

Kalendář údržby je k dispozici ve šesti různých pohledech: Kalendář
(výchozí), „Kanban“, „Seznam“, „Pohled“, „Graf“ a
:label:Aktivita.

.. obrázek: maintenance_calendar/maintenance-calendar-view-type-icons.png
:align:center
:alt: Ikony pro různé typy kalendářů údržby.

Kalendář
~~~~~~~~~~~~~

Výchozí pohled zobrazující kalendář je „Kalendář“ (viz obrázek).
otevřené. V tomto typu zobrazení je k dispozici několik možností pro třídění a seskupování informací o
žádosti o údržbu.

V horním levém rohu stránky je vyskakovací nabídka nastavená na „Týden“ (výchozí stav).
Kliknutím na tento seznam odhalíte různé časové období, v nichž může být kalendář
Zobrazení: den, měsíc a rok. Dále je možné zvolit
:guilabel:`Zobrazit víkendy“, výchozí volba. Pokud je nevybrána, víkendy se na grafu
kalendář.

.. obrázek: maintenance_calendar/maintenance-calendar-period-dropdown.png
:align:center
:alt:Možnosti kalendáře.

Vlevo od této nabídky je ikonka :guilabel:`⬅️ (levý směr)` a :guilabel:`➡️ (pravý směr)`
přesunout kalendář v čase dopředu nebo dozadu).

Vpravo od rozbalovací nabídky nastavené na „Týden“ je výchozí „Dnes“.
tlačítko. Po stisku tlačítka se kalendář vrátí na dnešní datum, ať už je jakékoliv datum.
je zobrazena před kliknutím na ni.

Na pravé straně stránky je sloupec s kalendářem, který je zmenšený.
dnešní datum a seznam techniků s požadavky
je nyní otevřený. Klikněte na ikonu „přístupový panel“ v horní části této lišty, abyste jej otevřeli nebo zavřeli.
příslušenství.

.. poznámka::
Seznam Technik pouze zobrazí, pokud jsou technici přiřazeni k otevřeným požadavkům.
individuální technici jsou uvedeni pouze v případě, že jsou uvedeni jako odpovědný za alespoň
1 žádost o údržbu.

Kanbanový pohled
~~~~~~~~~~~

S pohledem „Kanban“ jsou zobrazeny všechny otevřené požadavky na údržbu v kanbanovém stylu.
sloupy v různých fázích procesu údržby.

Každá požadavek na údržbu se zobrazuje samostatně v kartě úkolu a každá karta úkolu lze přetahovat.
na jinou fázi kanbanového potrubí.

Každá sloupec má název (např. :guilabel:`In Progress`). Při najetí myší nad hlavičkou sloupce se zobrazí
:guilabel:„Nástroje“ (gear) ikonu. Kliknutím na :guilabel:„Nástroje“ (gear) ikonu se zobrazí seznam možností
tlačítka: „Sbalit“, „Upravit“, „Automatizace“ a „Smazat“.

.. obrázek: maintenance_calendar/maintenance-calendar-kanban-column.png
:align:center
:alt:Možnosti sloupců pro fázi v kanbanovém pohledu.

Kliknutím na tlačítko „Sbalit“ se sloupec skryje.

Kliknutím na tlačítko „Upravit“ se otevře okno s názvem „Edit: (stáž)“, ve kterém je
přesné jméno odpovídající fázi, kde lze upravit podrobnosti sloupce. Následující jsou sloupec
upravitelné možnosti:

.. obrázek: maintenance_calendar/maintenance-calendar-edit-stage-popup.png
:align:center
:alt:Edit in progress okno.

- :guilabel:`Název“: název fáze v kanbanovém řetězci.
- :guilabel:„Složená v hlavní trubce“: když je tato položka zkontrolována, sloupec této fáze se automaticky skládá do
typu zobrazení „Kanban“.
- :guilabel:`Potvrzení požadavku“: pokud tuto políčko nezaškrtnete a typ požadavku na údržbu je
nastaven na *Servisní středisko*, při údržbě se pro příslušné servisní středisko nevygeneruje dovolená.
Vytvoří se požadavek. Pokud je zaškrtnuté pole, pracoviště je automaticky zablokováno pro
uvedená doba trvání, a to buď k určenému datu, nebo co nejdříve, pokud je pracoviště
nejsou dostupné.
- :guilabel:`Sekvence“: pořadí v procesu údržby, ve kterém se tento krok objevuje.
- :guilabel:`Požadavek dokončen“: pokud je zaškrtnuté, tento box ukazuje, že tato fáze je konečným krokem
proces údržby. Požadavky přesunuté do této fáze jsou uzavřeny.

Jakmile je hotovo, klikněte na tlačítko „Uložit a zavřít“ nebo pokud nebyly provedeny žádné změny, klikněte na tlačítko „Zrušit“.
nebo klikněte na ikonu „X“, abyste zavřeli okno s upozorněním.

Zobrazení seznamu
~~~~~~~~~

Při výběru pohledu „Seznam“ se zobrazí všechny otevřené požadavky na údržbu v seznamu.
informace o každé požadavku uvedené v příslušné řádce.

V tomto typu zobrazení jsou následující sloupce informací:

- :guilabel:`Předmět“: jméno, které bylo přiřazeno požadavku na údržbu.
- :guilabel:`Zaměstnanec“: zaměstnanec, který původně vytvořil požadavek na údržbu.
- :guilabel:`Technik“: osoba odpovědná za požadavek na údržbu.
- :guilabel:`Kategorie“: kategorii, do které patří opravované vybavení.
- :guilabel:`Stadium“: stádium údržby, ve kterém se aktuálně nachází požadavek.
- :guilabel:`Společnost“: pokud se v prostředí více společností nachází společnost z databáze, ve které je požadavek
přidělené.

Pohled na střed
~~~~~~~~~~

S vybraným pohledem Pivot jsou zobrazeny požadavky na údržbu v tabulce s přepočtem.
Může být přizpůsoben tak, aby zobrazoval různá data.

Pro přidání dalších dat do tabulky s klíčovými hodnotami klikněte na tlačítko „Měření“ pro zobrazení seznamu
menu. Výchozí volbou je „Počet“. Další možnosti pro přidání do tabulky jsou
„Přidat dovolenou“, „Délka“ a „Opakovat“.

.. obrázek: maintenance_calendar/maintenance-calendar-measures-menu.png
:align:center
:alt: Zobrazuje možnosti měření na stránce s výhledem Pivot.

Tlačítko „Vložit do tabulky“ se nachází napravo od tlačítka „Měření“.
Kliknutím na tlačítko se zobrazí okno s názvem „Vyberte tabulku, do které chcete vložit
pivot.'.

V tomto okně se nachází dvě záložky: „Tabulky“ a „Přístroje“. Klikněte
do jedné z těchto záložek a vyberte tabulku nebo panel v databázi, do které chcete přidat tento rozbalovací seznam.
table do. Jakmile bude připravena, klikněte na tlačítko „Potvrdit“. Pokud by tato tabulka neměla být vložena do sešitu
nebo klikněte na tlačítko „Zrušit“, nebo klikněte na ikonu „X“ pro zavření okna.

Vpravo od tlačítka „Vložit do tabulky“ jsou tři tlačítka:

- :guilabel:`Otočit osy“: otočí se osa x a y v tabulce s daty pro výchozí bod.
- :guilabel:`Rozbalit vše“: všechny dostupné sloupce a řádky tabulky s pivtovatými daty se rozbalí na maximum.
- :guilabel:`Stáhnout xlsx“: Pivotová tabulka se stáhne jako soubor .xlsx.

Grafický pohled
~~~~~~~~~~

Při zvoleném grafickém pohledu se mezi vyhledávacím oknem a vizualizací objeví následující možnosti
zobrazení dat. Tyto graf specifické možnosti jsou umístěny vpravo od
tlačítka „Měření“ a „Vložení do tabulky“.

.. obrázek: maintenance_calendar/maintenance-calendar-graph-view-icons.png
:align:center
:alt:Grafické ikony v seznamu grafů.

Uživatelé mohou zobrazit data pomocí tří různých typů grafů:

- :guilabel:`Svislá osa“: Zobrazení dat v svislé ose.
- :guilabel:`Svislá osa“: data jsou zobrazena v svislé ose.
- :guilabel:`Kruhová grafika“: datum je zobrazeno v kruhovém grafu.

Při zobrazení dat jako grafu sloupcového grafu lze data formátovat následovně
způsoby:

- :guilabel:`Skládané“: datové body jsou na grafu skládány.
- :guilabel:`Sestupně“: datum je zobrazeno v sestupném pořadí.
- :guilabel:`Vzestupně“: datum je zobrazeno vzestupným pořadím.

Při zobrazení dat jako grafu :guilabel:`Line Chart` lze data formátovat následovně
způsoby:

- :guilabel:`Skládané“: datové body jsou na grafu skládány.
- :guilabel:`Součet“: Data se postupně hromadí.
- :guilabel:`Sestupně“: datum je zobrazeno v sestupném pořadí.
- :guilabel:`Vzestupně“: datum je zobrazeno vzestupným pořadím.

Když se na data podíváte jako na graf „Kruh“, všechna důležitá data jsou zobrazena automaticky.
a žádné další možnosti formátování nejsou k dispozici.

Zobrazení aktivit
~~~~~~~~~~~~~

Při výběru pohledu „Aktivita“ jsou zobrazeny všechny otevřené požadavky na údržbu.
řádku s možností plánování aktivit souvisejících s těmito požadavky.

.. obrázek: maintenance_calendar/maintenance-calendar-activity-view-type.png
:align:center
:alt:Požadavky na údržbu v pohledu aktivit.

Požadavky na údržbu jsou uvedeny v sloupci „Požadavek na údržbu“ jako aktivity.
Kliknutím na požadavek se otevře okno s informacemi o požadavku, které ukazuje stav požadavku.
požadovat a odpovědný technik. Pro objednání činnosti přímo z vyskakovacího okna klikněte
:guilabel:`+ Zaplánovat aktivitu“. To otevře okno „Zaplánovat aktivitu“.

V okně zvolte typ aktivity, vložte stručný popis.
Vytvořte termín splatnosti, vyberte odpovědného uživatele v poli „Přiřazené uživatele“
pole.

.. obrázek: maintenance_calendar/maintenance-calendar-schedule-activity-popover.png
:align:center
:alt:Pop-up okno pro aktivitu v rozvrhu.

Do prázdného pole pod šedě vyznačeným textem zadejte další poznámky k nové aktivitě.
:guilabel:`Záznam...“ pole. Když je kliknuté, změní se na „Zadejte znaku '/' pro příkazy“.

Jakmile je připraveno, klikněte na tlačítko „Nastavit“ a poté zvolte možnost „Zařadit do plánu“.
:guilabel:'Vytvořit plán a označit jako dokončené' k uzavření aktivity a klikněte na 'Dokončeno a naplánovat další'
zavřít aktivitu a zahájit novou nebo kliknout na tlačítko „Zrušit“ pro zrušení aktivity.

Při zobrazení „Aktivita“ je k dispozici každý typ aktivit dostupný při plánování.
Aktivita je uvedena vlastním sloupcem. Tyto sloupce jsou: guilabel:„E-mail“,
:guilabel:Schůzka, :guilabel:Žádost o údržbu, :guilabel:Úkol, :guilabel:Nahrát
Dokument“, „Žádost o podpis“ a „Schválení“.

K naplánování aktivity s konkrétním typem aktivity klikněte na jakýkoli prázdný řádek v
sloupec pro požadovaný požadavek na údržbu a klikněte na ikonu „+“ . Tím
otevře okno Odoo, kde lze aktivitu naplánovat.

.. obrázek: maintenance_calendar/maintenance-calendar-odoo-activity-popup.png
:align:center
:alt:Pop-up okno kalendáře aktivit v Odoo.

.. viz také:
   - :doc:`požadavky na údržbu“
   - :doc:`add_new_equipment`
