=================
Analýza potrubí
=================

Aplikace CRM řídí prodejní kanál od fáze k fázi, jak se vedení a příležitosti pohybují.
od vzniku po prodej (Vyhrazeno) nebo archivní (Ztraceno).

Po uspořádání potrubí použijte vyhledávací možnosti a zprávy dostupné na Pipeline.
Analýza* stránky, abyste se dozvěděli více o efektivitě potrubí a jeho uživatelů.

Pro přístup na stránku „Analýza trubice“ přejděte do: menu: CRM aplikace - Zprávy - Trubice.

.. obrázek:: vítězství a prohry / zobrazení tabulky a přehledového pohledu.png
:align:center
:alt:Otevřete aplikaci CRM a klikněte na záložku Reporting v horní části obrazovky, pak klikněte na Pipeline.

.. _výhra/prohra/trubka:

Procházejte stránku analýzy potrubí
===================================

Po přístupu na stránku „Analýza potrubí“ se zobrazí graf svislých čar ukazujících počet vodičů z
V předchozím roce se automaticky vyplní. Tyčinky znázorňují počet kontaktů v každé fázi prodeje.
trubice, barevně označené tak, aby bylo vidět, v jakém měsíci se kandidát dostal na tuto úroveň.

.. obrázek: win_loss/pipeline-analysis-page.png
:align:center
:alt:Výchozí stav stránky Analýza potrubí je graf s mnoha možnostmi změny.

Interaktivní prvky stránky „Analýza potrubí“ umožňují upravovat graf a zobrazit
různé metriky v několika pohledech. Zleva doprava a shora dolů obsahují tyto prvky:

- :guilabel:`Akce“: zobrazené ikonou „⚙️ (převodovka)“, která se nachází vedle
:guilabel:`Analýza potrubí“ v názvu stránky. Když je kliknuté, objeví se vyskakovací nabídka s třemi
možností s vlastními podnabídkami: :guilabel:`Znalosti“, :guilabel:`Přístrojová deska“.
:guilabel:`Tabulka“. (Podrobnější informace o ukládání a sdílení zpráv naleznete v části
informace)

  - Možnost „Znalosti“ je pro vložení grafu do aplikace nebo odkaz na něj.
článek.
  - Možnost „Plocha“ je pro přidání grafu do panelu v aplikaci Dashboards.
  - Možnost „Tabulka“ (guilabel:Spreadsheet) je pro propojení grafu v tabulce v sekci Dokumenty.
aplikace.
- :guilabel:`Hledat ...“ lišta: zobrazuje filtry a skupiny, které jsou v současné době aplikovány na graf.
Chcete-li přidat nové filtry/skupiny, zadejte je do vyhledávacího pole nebo klikněte na :guilabel:`⬇️ (tlačítko dolů)
ikonu na konci lišty nabídek, která otevře seznam možností. (Viz také :ref:`Možnosti vyhledávání
(více informací najdete na stránce výher a proher).

V pravém horním rohu jsou ikony pro různé zobrazení.
Možnosti (viz např. win_loss/view pro více informací).

- :guilabel:`Graf“ Zobrazuje data v grafech sloupců. Toto je výchozí pohled.
- :guilabel:`Výhled Pivot“: zobrazuje data v kategorizované tabulce s možností přizpůsobení.
- Výhled „Kohorta“: zobrazuje a organizuje data podle jejich „Datum vytvoření“.
a :guilabel:'Datum uzavření' týden, den, měsíc nebo rok (výchozí hodnoty).
- :guilabel:`Seznam“ Zobrazuje data v seznamu.

Na nejvzdálenější levé straně stránky pod nadpisem „Analýza potrubí“
Je zde více konfigurovatelných filtrů a možností zobrazení.

- :guilabel:Měření: otevře se nabídka různých možností měření, které lze vidět v
graf, pivot nebo kohorta. V nabídce „Měření“ nenajdete
listového zobrazení. (Podrobnější informace naleznete v části :ref:`Možnosti měření <win_loss/measure>`)
- :guilabel:`Vložit do tabulky“: otevře okno s možnostmi pro vložení grafu nebo rozbalovacího seznamu.
tabulku do tabulky v aplikaci Dokumenty nebo panelu v aplikaci Dashboard.
Není k dispozici v pohledu na kohortu nebo seznamu.

Při zobrazení grafu jsou k dispozici následující možnosti:

- :guilabel:`Graf sloupců“: přepíná graf na graf sloupců.
- :guilabel:`Svislá osa“: přepne graf na svislou osu.
- :guilabel:'Graf sloupcový': přepne graf na sloupcový.
- :guilabel:„Skládané“: když je vybráno, výsledky každého kroku grafu se zobrazí na vrcholu
sebe navzájem. V případě nevybrání se zobrazují výsledky každé fáze jako samostatné čáry.
- :guilabel:`Sestupně“: přeřadí fáze grafu v sestupném pořadí zleva doprava.
Klikněte na ikonu podruhé, abyste ji vybrali znovu. V závislosti na nastavení filtrů může být tato možnost
být k dispozici.
- :guilabel:`Vzestupně“: přeřadí fáze v grafu od levého okraje ke krajnímu pravému.
Klikněte na ikonu podruhé, abyste ji vybrali znovu. V závislosti na nastavení filtrů může být tato možnost
být k dispozici.

Při zvoleném pohledu na osu jsou k dispozici následující možnosti:

- :guilabel:`Otočení osy“: otočí osy X a Y pro celou tabulku.
- :guilabel:`Rozbalit vše“: Když jsou vybrány další skupiny pomocí :guilabel:`+ (plus
ikony, tlačítko otevře pod každou řádkou skupiny.
- :guilabel:`Stáhnout xlsx“: stahuje tabulku jako soubor Excelu.

... _výhry/prohry na hledání:

Možnosti vyhledávání
--------------

Stránka „Analýza potrubí“ lze upravit různými filtry a možnostmi skupinování.

Chcete-li přidat nová kritéria vyhledávání, zadejte požadovaná kritéria do pole pro vyhledávání nebo klikněte na
:guilabel:`⬇️ (dolů)“ ikonu vedle vyhledávací lišty pro otevření seznamu všech možností.
Podrobnější informace o každé z těchto možností najdete v následujících sekcích.

.. obrázek: win_loss/search-panel-filters-and-group-by-options.png
:align:center
:alt: Kliknutím na šipku dolů vedle vyhledávací lišty se zobrazí nabídka filtrů pro analýzu.

.. záložky::

...... záložka: Filtry

V sekci Filtry mohou uživatelé přidat předdefinované a vlastní filtry do vyhledávání.
kritérií. K jedné vyhledávacímu dotazu lze přidat více filtrů.

      - :guilabel:Můj potrubní systém“: zobrazuje případy, které jsou přiřazeny aktuálnímu uživateli.
      - :guilabel:`Možnosti“: zobrazují kontakty, které byly kvalifikovány jako možnosti.
      - :guilabel:`Vedoucích“: zobrazují vedoucí, které ještě nebyly kvalifikovány jako příležitosti.
      - :guilabel:`Aktivní“: zobrazení aktivních kontaktů.
      - :guilabel:`Neaktivní“: zobrazit neaktivní kontakty.
      - :guilabel:`Vyhráno“: zobrazí se záznamy, které byly označeny jako „Vyhráno“.
      - :guilabel:Ztracené“: zobrazuje seznam epizod, které byly označeny jako „Ztracené“.
      - :guilabel:`Vytvořeno od“: zobrazí leady vytvořené během určitého časového období.
Výchozí hodnota je poslední rok, ale může být upravena podle potřeby nebo úplně odstraněna.
      - :guilabel:`Očekávané uzavření“: zobrazuje smlouvy, které jsou očekávány k uzavření (označené jako „Výhra“) během
Specifický časový úsek.
      - :guilabel:`Datum uzavření“: zobrazuje nabídky, které byly uzavřeny (označeny jako **Vyhráno**) v určitém
Dočasný časový úsek.
      - :guilabel:`Uzavřené“: zobrazují kontakty, které byly uzavřeny (značeno jako „Ztracený“).
      - :guilabel:Přidat vlastní filtr: umožňuje uživatelům vytvořit vlastní filtr s mnoha
možnosti. (Podívejte se na odkaz „Přidání vlastních filtrů a skupin“ pro více informací.)
informace)

...... tab:: Skupina

V části „Skupiny“ lze přidat předdefinované a vlastní skupinové zobrazení.
výsledky vyhledávání. Můžete přidat více skupin, abyste výsledky rozdělili na menší a lépe zvladatelné části.

...............důležité::
Pořadí, ve kterém se skupiny přidávají, ovlivňuje způsob zobrazení finálních výsledků. Zkuste
vybírat stejné kombinace v jiném pořadí, abychom zjistili, co funguje nejlépe pro každé použití
případu.

      - :guilabel:`Prodejce“: seskupuje výsledky podle prodejce, kterému je přiřazený lead.
      - :guilabel:`Tým prodeje“: seskupuje výsledky podle týmu prodeje, kterému je přiřazená poptávka.
      - :guilabel:`Město“: seskupuje výsledky podle města, odkud pochází kontakt.
      - :guilabel:`Země“: seskupuje výsledky podle země, ze které pochází kontakt.
      - :guilabel:`Společnost“: seskupuje výsledky podle společnosti, ke které patří kontakt (pokud existují více)
společnosti jsou aktivovány v databázi.
      - :guilabel:`Stadium“: seskupí výsledky podle fází prodejního procesu.
      - :guilabel:Kampaň: seskupuje výsledky podle marketingové kampaně, ze které pochází kontakt
vznikly.
      - :guilabel:`Medium“: seskupuje výsledky podle média (e-mail, Google Adwords, webová stránka atd.).
z něhož vznikl kontakt.
      - :guilabel:`Zdroj`: seskupuje výsledky podle zdroje (Vyhledávač, Vzpomínka na lead,
Zprávy (newslettery apod.), odkud klient pochází.
      - :guilabel:`Datum vytvoření“: seskupuje výsledky podle data, kdy byl kontakt přidán do databáze.
      - :guilabel:`Datum konverze“: seskupuje výsledky podle data, kdy byla osoba přeměněna na
příležitost.
      - :guilabel:`Očekávané uzavření“: seskupuje výsledky podle data, kdy je očekáváno uzavření
(označené jako „Vyhrané“).
      - :guilabel:`Datum uzavření“: seskupuje výsledky podle data, kdy byl kontakt označen jako „Vyhráno“.
      - :guilabel:`Ztracený důvod“: seskupuje výsledky podle důvodu, který byl vybrán při označení vedení
„Ztracený.“
      - :guilabel:`Přidat vlastní skupinu“: umožňuje uživatelům vytvořit vlastní skupinu s mnoha
možností. (Podrobnější informace naleznete v kapitole „Přidání vlastních filtrů a skupin“
informace)

.. tab:: Srovnání

Sekce „Srovnání“ umožňuje uživatelům přidávat srovnávací údaje k stejným kritériím vyhledávání.
v jiném časovém období.

Tato možnost je k dispozici pouze v případě, že vyhledávání zahrnuje filtry na základě času.
:guilabel:`Vytvořeno“, :guilabel:`Očekávané uzavření“ nebo :guilabel:`Datum uzavření“.
můžete přidávat více časových filtrů najednou, ale můžete vybrat jen jeden srovnávací filtr.
času.

      - :guilabel:`Předchozí období“: přidává srovnání stejných kritérií z předchozího období.
období.
      - :guilabel:Předchozí rok“: přidá srovnání stejných kritérií z předchozího roku.
rok.



Sekce „Oblíbené“ umožňuje uživatelům uložit vyhledávání pro pozdější použití, takže se nebudou muset
musí být vytvořen znovu a znovu.

Vyhledávání lze uložit, sdílet s ostatními nebo nastavit jako výchozí pro každou příležitost.
:guilabel:`Analýza potrubí“ je otevřena.

      - :guilabel:`Uložit aktuální vyhledávání“: uložte aktuální kritéria pro vyhledávání na později.

        - :guilabel:`Výchozí filtr“: pokud chcete při ukládání vyhledávání zvolit tento filtr jako výchozí, zaškrtněte tuto políčko.
filtr vyhledávání, když je otevřena stránka „Analýza potrubí“.
        - :guilabel:`Sdílené“: pokud chcete uložit vyhledávání, zaškrtněte tuto položku, aby bylo k dispozici ostatním
uživatelé.

... vítězství/prohry/vlastní filtry:

Přidejte vlastní filtry a skupiny
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kromě předdefinovaných možností v poli vyhledávání může být na stránce „Analýza potrubí“
Také využít vlastní filtry a skupiny.

Vlastní filtry jsou složité pravidla, která dále upravují výsledky vyhledávání. Naopak vlastní skupiny
zobrazit informace v uspořádanějším stylu.

**Přidat vlastní filtr:**

1. Na stránce „Analýza potrubí“ klikněte na ikonu „svislý šipek“.
:guilabel:`Hledat ...“ lišta.
2. V rozevíracím seznamu klikněte na položku „Přidat vlastní filtr“.
3. Zobrazí se okno s názvem „Přidat vlastní filtr“ (:guilabel:„Stát“) s výchozím pravidlem.
je v poli ____) tvořeném třemi jedinečnými poli. Tyto pole lze upravit tak, aby odpovídala vašim potřebám.
a do jednoho vlastního filtru lze přidat více pravidel.
4. Chcete-li upravit pravidlo, začněte kliknutím na první pole ([:guilabel:`Země“]) a vyberte možnost.
z roletkového menu. První pole určuje hlavní předmět pravidla.
5. Dále klikněte na druhé pole a vyberte možnost z roletky.
určuje vztah mezi prvním a třetím polem a obvykle je to buď „je“ nebo „není“.
Je to prohlášení, ale může být také větší nebo menší než prohlášení a podobně.
6. Nakonec klikněte na třetí pole a vyberte možnost z rozbalovací nabídky.
definuje sekundární předmět pravidla.
7. S vybranými všemi třemi poli je pravidlo kompletní.

   - **Přidat další pravidla:** klikněte na tlačítko „Nový pravidlo“ a opakujte kroky 4–7, pokud je to nutné.
   - Chcete-li smazat pravidlo, klikněte na ikonu :guilabel:`🗑️ (koš)` vpravo od pravidla.
   - **Pro vytvoření nového pravidla:** klikněte na ikonu „+“ vedle
pravidlo.
   - **Vytvořit složitější pravidla:** klikněte na ikonu „Přidat větve“ vedle
pravidlo. Toto přidává další modifikátor pod pravidlem pro vkládání „všechny“ nebo „jakýkoliv“.

.. obrázek: win_loss/custom-filter-add-branch.png
:align:center
:alt:Funkce přidání větve umožňuje vytvářet složitější celé nebo libovolné výroky pro pravidla.

8. Jakmile jsou všechny pravidla přidána, klikněte na tlačítko „Přidat“ pro přidání vlastního filtru do vyhledávání.
kritérií.

   - **Chcete-li odstranit vlastní filtr:** klikněte na ikonu „✖️ (x)“ vedle filtru v
vyhledávací lišta.

**Přidat vlastní skupinu:**

1. Na stránce „Analýza potrubí“ klikněte na ikonu „svislý šipek“.
hledání.
2. V rozbalovacím seznamu vyberte možnost „Přidat vlastní skupinu“.
3. Přejděte dolů na seznam možností a vyberte jednu nebo více skupin.

   - **Chcete-li odstranit vlastní skupinu:** klikněte na ikonu :guilabel:`✖️ (x)` vedle vlastní skupiny v
vyhledávací lišta.

.. výhra/prohra/měření:

Měřicí možnosti
-------------------

Výchozí nastavení měří celkový počet leadů na stránce „Analýza trubice“.
které splňují kritéria hledání, ale mohou být upraveny tak, aby měřily jiné položky.

Pro změnu vybraného měřítka klikněte na tlačítko „Měřítka“ v levém horním rohu
stránce a vyberte jednu z následujících možností ze seznamu:

- :guilabel:`Dny k přidělení“: měří počet dní, které uplynuly od chvíle, kdy byl kontakt přidělen
výrobu.
- :guilabel:`Dny do uzavření“ měří počet dní, které trvalo získat vedení (značku
**Vyhrála**).
- :guilabel:`Dny k přeměně na zákazníka“ měří počet dnů, které uplynuly od chvíle, kdy byl kontakt označen za potenciálního zákazníka.
příležitost.
- :guilabel:'Počet přesahujících dnů': měří počet dní, o které se objem obchodu překročil
Datum očekávaného uzavření obchodu.
- :guilabel:`Očekávaný měsíční obrat“: měří očekávaný měsíční obrat v případě, že se jedná o lead.
- :guilabel:`Očekávaný příjem“: měří očekávaný příjem vůči jednotlivým kontaktům.
- :guilabel:`Proporcionální měsíční opakovaný příjem“: měří procentuální měsíční opakovaný příjem vedeného zákazníka.
- :guilabel:`Proporcionální opakované příjmy“: měří proproporcionální opakované příjmy vůči jednotlivým kontaktům.
- :guilabel:`Částečná výše příjmů“: měří částečnou výši příjmů vedení.
- :guilabel:`Opakující se příjmy“: měří opakující se příjem vedení.
- :guilabel:`Počet“: měří celkový počet záznamů, které odpovídají vyhledávacím kritériím.

.. _výhry/prohry/zhlédnutí:

Zobrazit možnosti
------------

Po konfiguraci filtrů, skupin a měření můžete na stránce „Analýza potrubí“
zobrazit data různými způsoby. Výchozí grafický pohled lze změnit
k pohledu na páteřní oblast, kohortu nebo seznamu.

Pro změnu potrubí na jiný pohled klikněte na jedno ze čtyř ikon prohlížení umístěných v
vpravo nahoře na stránce „Analýza potrubí“.

.. záložky::

....... tabulka:: Grafické zobrazení

Graf je výchozím výběrem pro stránku „Analýza potrubí“.
zobrazuje analýzu jako buďto: graf sloupců, čárový graf nebo kruhový graf.

Tento pohled je užitečný pro rychlé vizualizování a porovnávání jednoduchých vztahů, jako jsou
počet vedení ve každé fázi nebo vedení přiřazená ke každému
:guilabel:`Prodejce“.

Výchozí graf měří počet leadů v každé skupině, ale tento může být změněn.
změnit kliknutím na tlačítko „Měření“ a vybráním jiné možnosti
z výsledného seznamu.

.. obrázek:: win_loss/graph-view.png
:align: střed
:alt: Zobrazení grafu zobrazuje analýzu jako sloupcový, čárový nebo kruhový graf.

...............tip:
Při použití sloupcového grafu v tomto pohledu zvažte odstranění možnosti „Skládaný“.
aby bylo výsledkové rozložení lépe čitelné.

... tab::Pohled na sloupce

Pohled na páku zobrazuje výsledky analýzy jako tabulku. Výchozí nastavení je takové, že tabulka
výsledky podle fází prodejního procesu a měřítka: guilabel:"Očekávaný obrat".

Pohled na data v ose je užitečný pro analýzu podrobnějších čísel než grafický pohled umožňuje.
nebo pro přidání dat do tabulky s vlastními formulemi, jako je tomu u aplikace Excel
soubor.

.. obrázek:: win_loss/pivot-view.png
:align: střed
:alt: Zobrazení Pivot View zobrazuje analýzu jako tabulku.

Tři ikony v horním levém rohu stránky plní následující funkce:

      - :guilabel:`Otočení osy“: otočí osy X a Y pro celou tabulku.
      - :guilabel:`Rozbalit vše“: Když jsou vybrány další skupiny pomocí :guilabel:`+ (plus
tlačítko otevře pod každou řádkou skupiny ikon.
      - :guilabel:`Stáhnout xlsx“: stahuje tabulku jako soubor Excelu.

.. poznámka::
Skupina Stage nelze odstranit, ale měření lze změnit.
kliknutím na tlačítko „Měření“ a výběrem jiného možného nastavení.

....... Zobrazení kohorty

Kohortový pohled zobrazuje analýzu jako časové období (kohorty), které lze nastavit na dny.
týdny, měsíce nebo roky. Výchozím výběrem je „Týden“.

Tato možnost zobrazení je užitečná zejména pro porovnání, jak dlouho trvalo uzavření obchodu.

.. obrázek: win_loss/cohort-view.png
:align: střed
:alt: Zobrazení kohorty zobrazuje analýzu jako jednotlivé týdny v roce.

Zleva doprava a shora dolů sloupce v grafu představují následující:

      - :guilabel:`Vytvořeno v“: sloupce této tabulky představují týdny v daném roce.
v databázi existují záznamy odpovídající vyhledávacím kritériím.

        - Při nastavení na „Týden“ znamená řádek s označením „W52 2023“ výsledky
se uskuteční v týdnu 52 roku 2023.
      - :guilabel:`Měření“: druhá sloupec grafu je měření výsledků.
Výchozí hodnotou je „Počet“, ale lze ji změnit kliknutím na
:guilabel:`Měření“ tlačítko a vybrat možnost z rozbalovací nabídky.
      - :guilabel:`Datum uzavření - den/týden/měsíc/rok“: tato sloupec se podívá na to, jaké procento
Výsledky měření byly v následujících dnech, týdnech, měsících či letech uzavřeny.
      - :guilabel:'Průměr': tato řádka poskytuje průměr všech ostatních řádků v sloupci.

Kohortní pohled můžete také stáhnout ve formátu Excel kliknutím na tlačítko :guilabel:`Stáhnout`.
ikona v levém horním rohu stránky.

....... tab:: Zobrazení seznamu

V seznamovém zobrazení je zobrazen pouze jeden seznam všech kontaktů, které vyhovují kritériím hledání.
vedení otevírá záznam pro další zkoumání. Další detaily, jako například :guilabel:`Country`,
:guilabel:`Střední“, a další lze přidat do seznamu kliknutím na :guilabel:`Filtry“.
ikona v pravém horním rohu seznamu.

Tento pohled je užitečný pro zobrazení mnoha záznamů najednou.

.. obrázek:: win_loss/list-view.png
:align: střed
:alt: Zobrazení seznamu zobrazí pouze jednu sekvenci všech záznamů, které odpovídají vyhledávacím kritériím.

Kliknutím na ikonu :guilabel:`⚙️ (převodovka)` se otevře nabídka akcí s možnostmi pro
následující:

      - :guilabel:`Dokumenty importu“: otevře stránku pro nahrání tabulky dat, stejně jako
šablonu tabulky, která usnadní formátování dat.
      - :guilabel:`Exportovat vše“: stáhne seznam jako soubor xlsx pro Excel.
      - :guilabel:'Znalosti': vloží pohled nebo odkaz na seznam do článku
aplikace Knowledge
      - :guilabel:`Přístrojová deska“: přidá seznam do „Moje Přístrojová deska“ v aplikaci „Přístrojové desky“.
      - :guilabel:`Sešit“: odkazuje na nebo vkládá seznam do tabulky ve složce „Dokumenty“.
aplikace.

.. poznámka::
V seznamovém pohledu kliknutím na tlačítko „Nový“ se zavře seznam a otevře novou nabídku.
stránce. Kliknutím na tlačítko „Vytvořit kontakt“ se otevře okno pro vytváření kontaktů.
Žádná z těchto funkcí není určena k ovlivňování seznamového výhledu.

... výsledky zápasů a reporty:

Vytvářet zprávy
==============

Po pochopení, jak používat stránku s analýzou potrubí (<win_loss/pipeline>)
Stránka „Analýza potrubí“ může být použita k vytváření a sdílení různých zpráv. Mezi
předdefinované možnosti a vlastní filtry a skupiny, téměř jakýkoli kombinací je možný.

Jakmile je report vytvořený, lze jej uložit do oblíbených položek, sdílet s dalšími uživateli a/nebo přidat
dashboardy a tabulkové procesory (výhry/ztráty, zprávy o úspěchu).

Několik běžných zpráv, které lze vytvořit pomocí stránky „Analýza potrubí“, jsou podrobně popsány
dále.

.. _výhra/prohra:

Zprávy o výhře a prohře
----------------

Výhra/prohra je výpočet aktivních nebo dříve aktivních kontaktů v trubici, které byly buď označeny
jako „Vyhrané“ nebo „Prohráno“ za určité období. Výpočet počtu vyhraných příležitostí
ztratíte příležitosti, týmy mohou zjistit klíčové ukazatele výkonnosti (KPI), které přeměňují leady
do prodeje, jako jsou konkrétní týmy nebo členové týmů, určité reklamní média a kampaně atd.
on.

.. matematika::
\begin{equation}
Ratio výher a proher = \frac{Vyhrané příležitosti}{Ztracené příležitosti}


Zpráva o výhře a prohře filtruje kontakty z minulého roku, ať už vyhrané nebo prohrané, a seskupuje je.
podle fáze v potrubí. Vytváření tohoto hlášení vyžaduje vlastní filtr a skupinování
výsledky podle:guilabel:`Stage`.

.. obrázek: win_loss/hledané-kriterium-pro-základní-výhru-a-prohru.png
:align:center
:alt:Kritéria pro vyhledávání výsledků hry/prohry jsou Vytvořeno, Stádium a Aktivní je v pravdě nebo nepravdě.

Postupujte podle níže uvedených kroků, abyste vytvořili zprávu o výhře nebo prohře.

1. Přejděte na:menu: „CRM aplikace -> Zprávy -> Pipeline“.
2. Na stránce „Analýza potrubí“ klikněte na ikonu ⬇️ vedle
vyhledávací lištu, abyste otevřeli vyskakovací nabídku filtrů a skupin.

.... obrázek:: win_loss/filters-for-basic-win-loss-report.png
:synchronizace: střed
:alt: Vyhledávací nabídka obsahující filtry pro základní výsledkový přehled.

3. V rozbalovacím seznamu, který se objeví, klikněte pod nadpisem „Skupina“ na „Stadium“.
4. Pod nadpisem Filtry klikněte na tlačítko Přidat vlastní filtr, abyste otevřeli další okno.
menu.
5. V okně „Přidat vlastní filtr“ klikněte na první položku
:guilabel:`Přesně shoduje s následujícími pravidly:‘ sekce. Výchozí hodnotou tohoto pole je
:guilabel:`Země“.
6. Kliknutím na první pole se zobrazí podmenu s mnoha možnostmi výběru.
podmenu, najděte a vyberte možnost „Aktivní“. To automaticky naplní
ostatní pole.

První pole zobrazuje: :guilabel:`Aktivní“. Druhé pole zobrazuje: :guilabel:`Je“. A nakonec
Třetí pole obsahuje: :guilabel:`set`.

Ve zkratce pak celý příkaz vypadá takto: :guilabel:`Active je nastaveno`.
7. Klikněte na „Nový pravidlo“, změňte první pole na „Aktivní“ a poslední pole na
:guilabel:`nepovinné“. Celkově pravidlo zní :guilabel:`Aktivní není nastavený“.
8. Klikněte na tlačítko „Přidat“.

.. obrázek: win_loss/add-custom-active-filter.png
:align:center
:alt:Náhled nabídky Přidat vlastní filtr, která zobrazuje dvě pravidla: (1) je aktivní a (2) není aktivní.

Výkaz nyní zobrazuje celkový počet případů, ať už „vyhraných“ nebo „prohrál“, rozdělených podle
jejich fází v CRM kanálu. Po najetí myši na část grafu se zobrazí počet leadů
taková fáze.

.. obrázek: win_loss/basic-win-loss-report.png
:align:center
:alt:Základní zpráva o výhře a prohraných zápasech, která všechny vedené hráče seřadí podle fáze.

Upravte zprávy o výhře a prohře
~~~~~~~~~~~~~~~~~~~~~~~~~~

Po vytvoření zprávy o výhře a prohře uvažujte o použití možností níže.
Přizpůsobit zprávu různým potřebám.

Příklad:
Prodejní manažer může seskupit výhry a prohry podle obchodníků nebo týmů, aby viděl, kdo má nejvíce.
nejlepší konverzní poměr. Nebo tým pro marketing může skupit podle zdrojů nebo médií, aby zjistil, kde
Jejich reklama je nejúspěšnější.

.. záložky::

...... záložka Filtry a skupiny

Chcete-li přidat další filtry a skupiny, klikněte na ikonu :guilabel:`⬇️ (zpětného lomítka)“, vedle vyhledávacího pole.
v nabídce a vyberte jednu nebo více možností z roletky.

Některé užitečné možnosti zahrnují:

      - :guilabel:`Vytvořeno na“: nastavením tohoto filtru na jiný časový úsek, například
Pro aktuálnější výsledky lze použít posledních 30 dní nebo poslední čtvrtletí.
      - Kliknutím na možnost „Přidat vlastní filtr“ a procházením mnoha
v rozbalovacím seznamu otevře další kritéria pro vyhledávání, jako například: guilabel:"Poslední
Stage Update nebo Lost Reason.
      - Klikněte na „Přidat vlastní skupinu > Aktivní“.
odděluje výsledky na **Vyhrané** (:guilabel:`true`) nebo **Prohrané** (:guilabel:`false`).
Zobrazuje stav, kdy jsou kontakty označeny jako „Vyhrané“ nebo „Prohráno“.
      - :guilabel:`Více skupin“: přidat více výběrů „Skupit podle“ k rozdělení
výsledky rozdělit do větších a lépe spravovatelných částí.

        - Přidání :guilabel:„Prodavač“ nebo :guilabel:„Tým prodejců“ rozbije celkový počet
Vede v každé fázi.
        - Přidání :guilabel:„Střední“ nebo :guilabel:„Zdroj“ může odhalit, které marketingové cesty generují
více prodejů.

.. obrázek:: win_loss/search-panel-filters-and-group-by-options.png
:align: střed
:alt:Vyhledávací nabídka je otevřená a filtry Vyhráno/Prohrané jsou zvýrazněny.

... tab::Pohled na sloupce

Výchozí nastavení zobrazuje skupiny výsledků vítězství a prohry podle :guilabel:`Stage` a měření
:guilabel:`Očekávaný příjem“.

Abychom si mohli doplnit tabulku,

      1. Klikněte na tlačítko „⬇️ (svislá šipka)“ vedle vyhledávacího pole.
      2. V rozevíracím seznamu nahraďte skupinu „Stage“ něčím jako
:guilabel:'Prodejce' nebo :guilabel:'Média'.
      3. Klikněte na tlačítko „Měření“ a klikněte na „Počet“, abyste přidali počet
Vrací se zpět do zprávy.

         - Další užitečné měřítko pro zobrazení na hodinovém pásmu zahrnuje:
:guilabel:`Dny k uzavření“.

.. obrázek: win_loss/win-loss-pivot-view.png
:align: střed
:alt:Výsledkový přehled v Pivot View zobrazuje data tabulkově.

...............důležité::
V případě zobrazení na ploše může být tlačítko „Přidat do tabulky“ šedé kvůli
Zpráva obsahující:guilabel:`duplicitní skupiny“. Chybu lze opravit nahrazením
:guilabel:`Skupina Stage“ v hledaném poli s jinou možností.

....... tab:: Zobrazení seznamu

V seznamovém zobrazení je vítězný/prohraný výkaz zobrazen na jedné stránce všemi kontakty.

Pro lepší organizaci seznamu klikněte vedle vyhledávací lišty na :guilabel:`⬇️ (dolů)´ a
přidat další relevantní skupiny nebo přeorganizovat stávající. Chcete-li změnit uspořádání podskupin, odstraňte
všechny možnosti „Skupit podle“ a přidat je v požadovaném pořadí.

Abychom do seznamu přidali další sloupce:

      1. Klikněte na ikonu filtrů v pravém horním rohu stránky.
      2. Vyberte možnosti ze seznamu, který se zobrazí. Mezi užitečné filtry patří např.:

         - Kampaň: Zobrazuje marketingovou kampaň, která vytvořila každý kontakt.
         - **Média**: Zobrazuje reklamní média (banner, direct, email, google adwords, telefon,
Webová stránka, e-mailová adresa atd., ze které pochází každý kontakt.
         - **Zdroj**: Zde se uvádí zdroj každé poptávky (newsletter, zpětné volání, vyhledávač atd.).

.. obrázek:: win_loss/win-loss-list-view.png
:align: střed
:alt:V zobrazení seznamu je vše přehledně uspořádáno a snadno čitelné.

... _výhry-prohry/zápasy-reporty:

Uložte a sdílejte zprávy
======================

Po vytvoření zprávy lze kritéria vyhledávání uložit, takže se při příštím hledání zobrazí
nemusí se v budoucnu znovu vytvářet. Uložené vyhledávání automaticky aktualizuje své výsledky
Každýkrát, když se zpráva otevře.

Dále lze zprávy sdílet s dalšími lidmi nebo je přidat do tabulek/přehledů pro větší
přizpůsobení a snadnější přístup.

.. záložky::

....... záložka Uložit do oblíbených

Pro uložení zprávy na později:

      1. Na stránce „Analýza potrubí“ klikněte na ikonu „↓ (svislá čára)“.
do vyhledávacího pole.
      2. V rozbalovacím seznamu, který se objeví, pod nadpisem „Oblíbené“, klikněte
:guilabel:`Uložit aktuální vyhledávání“.
      3. V dalším seznamovém poli zadejte název pro zprávu.

         - Zatrhnutím políčka „Výchozí filtr“ nastavíte tento výstup jako výchozí analýzu při
je otevřena stránka „Analýza potrubí“.
         - Zatrhnutím políčka „Sdílené“ se tento report stane dostupný ostatním uživatelům.

      4. Konečně klikněte na tlačítko :guilabel:`Uložit“. Zpráva je nyní uložena pod :guilabel:`Oblíbené“
hlavičce.

.. obrázek:: win_loss/save-to-favorites.png
:align: střed
:alt:V sekci Oblíbené klikněte na tlačítko Uložit aktuální vyhledávání a uložte si zprávu pro pozdější použití.

...... tab:: Přidat do sešitu

Vkládání zprávy do tabulky nejen uchovává kopii zprávy, ale také umožňuje uživatelům
přidat grafy a vzory jako do souboru Excel.

Pro uložení zprávy jako tabulky:

      - **V grafu nebo v přehledu Pivot**:

        1. Klikněte na tlačítko „Vložit do tabulky“.
        2. V okně, které se objeví, klikněte na možnost „Potvrdit“.

      - **V kohortě nebo v seznamu**:

        1. Klikněte na ikonu „⚙️ (převodovka)“.
        2. Vyberte možnost „Spreadsheet“ v seznamu, který se objeví.
        3. V dalších krocích vyberte buď možnost „Vložit do tabulky“ nebo
:guilabel:`Odkaz v tabulce“.

Uložené zprávy jsou viditelné v aplikaci *Dokumenty*.

.. obrázek:: vítězství/prohra/výhled v tabulce.png
:align:center
:alt:Pohledy na data se zvláště hodí do tabulek.

...............tip:
Po úpravě tabulky a přidání dalších vzorců se pak zamyslete nad tím, zda ještě nezbylo něco
celou tabulku do panelu. Použitím této metody lze tabulku přidat na
veřejná lišta namísto pouze „Moje lišta“.

         1. Klikněte na položku „Soubor > Přidat do panelu nástrojů“.
         2. V okně, které se objeví, pojmenujte tabulku a vyberte „Pohled
Zprávu uložte do složky „Section“.
         3. Klikněte na tlačítko „Vytvořit“.

... tab::Přidat na panel

Přidání zprávy na panel ukládá ji pro pozdější použití a usnadňuje její zobrazení vedle ostatních
:guilabel:`Můj panel“.

Přidat zprávu do :guilabel:`Můj panel nástrojů`:

      1. Na stránce „Analýza trubice“ klikněte na ikonu „⚙️ (převodovka)“.
      2. V rozbalovacím seznamu vyberte možnost „Přístup k panelu“.
      3. V rozevíracím seznamu Add to my dashboard zadejte název pro zprávu (např.
Výchozí název je :guilabel:`Pipeline`.
      4. Klikněte na tlačítko „Přidat“.

Pro zobrazení uloženého hlášení:

      1. Přejděte zpět na hlavní stránku aplikací a přejděte do sekce „Dashboardy - Můj“.
Dashboard.

.. obrázek:: win_loss/add-to-dashboard.png
:align: střed
:alt: Chcete-li se dostat k uložené zprávě, otevřete aplikaci Dashboard a klikněte na My Dashboard.

.. viz též:
   - :doc:`../získání kontaktů/převod“
   - :doc:`../acquire_leads/send_quotes`
   - :doc:`../pipeline/ztratene-prilezitosti`
