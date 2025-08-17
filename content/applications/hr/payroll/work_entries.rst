============
Dílčí položky práce
============

Přiřazení pracovních položek k zaměstnanci se provádí automaticky v aplikaci *Mzdy*, na základě mzdy.
struktura typu <platové výměry/struktury typu>, a z *Plánování*, *Přítomnost* a *Čas volna*.
Žádosti o přijetí.

Dashboard „Pracovní vstupy“ aplikace „Mzdy“ poskytuje vizuální přehled o
individuální záznamy o pracovní činnosti pro každého zaměstnance.

Pro otevření panelu navigujte na: „Mzdy“ --> „Pracovní vstupy“ --> „Pracovní vstupy“.

Na panelu „Příchod do práce“ se pracovní příležitosti zobrazují v abecedním pořadí podle
jméno zaměstnance. Celý měsíc je zobrazen s vyznačeným aktuálním dnem
žlutá.

Pokud existují nějaké konflikty :ref:`<payroll/conflicts>`, které je třeba vyřešit, panel
výchozí nastavení filtruje pouze záznamy s konfliktními hodnotami.

Chcete-li zobrazit všechny záznamy práce, klikněte na
ikona „Odebrat“ („✖“) v filtru „Konflikt“ na liště „Hledání…“.
A všechny záznamy práce se zobrazují v seznamu.

.. obrázek:: work_entries/work-entries-overview.png
:align:center
:alt: Zobrazení konfliktů na panelu s přehledem všech pracovních vstupů zaměstnance.

... _vypočítat mzdu/upravit pohled:

Změnit pohled na pouze jednu denní položku, týden nebo měsíc, klikněte na
„Měsíc“. Vyskakovací nabídka se zobrazí s možnostmi „Den“, „Týden“ a
nebo:guilabel:`Měsíc“. Kliknutím na jednu z možností se zobrazí pouze údaje pro tuto konkrétní volbu.

Použijte ikony „⬅️ (levý směr)“ a „➡️ (pravý směr)“ na levé a pravé straně.
boku tlačítka „Měsíc“ k nastavení zobrazených dat. Šipky upravují datum podle
na zvoleném typu času.

Příkladem je například volba „Měsíc“, kdy se po každém kliknutí posune ukazatel o jeden měsíc.
šipka. Pokud je vybrána šipka „Týden“ nebo „Den“, čas se posune o týden nebo den
za každé stisknutí šipky.

Kdykoliv se vrátit na pohled obsahující aktuální den, klikněte na tlačítko „Dnes“.

... _mzdové účetnictví/nový vstup do práce:

Přidat nový záznam práce
====================

Pokud je v pracovním záznamu chybějící položka, která se má přidat, například nemocenská dovolená, nebo pokud zaměstnanec zapomněl
zadat čas příchodu a odchodu z pracovní směny, kliknout na „Nový“ v panelu „Přihlášení do práce“,
Vytvořit nový záznam práce.

Vyskytne se okno s příkazem „Vytvořit“.

Do formuláře zadejte následující informace:

- :guilabel:`Popis“: zadejte krátký popis práce, například „Čas nemocenské“. Pokud
Pokud je pole nevyplněné, automaticky se vyplní po výběru zaměstnance. Výchozí
Vstup je „Přítomnost: (Zaměstnanec)“.
- :guilabel:`Zaměstnanec“: vyberte zaměstnance, pro něhož je pracovní záznam určen, z roletkového menu.
- :guilabel:`Typ vstupu do práce“: vyberte typ vstupu do práce pomocí
rozbalovací nabídka.
- Do políčka „Od“ a „Do“ zadejte začátek („Od“) a konec („Do“).
datum a čas vstupu do práce.

Nejprve klikněte na buď na řádek „Od“ nebo „Do“, aby se zobrazilo kalendářové okno.
Okno. Vyberte datum pomocí správného měsíce a roku, kliknutím na :guilabel:`< (vlevo
a pak klikněte na konkrétní den.

Poté vyberte čas kliknutím na hodinové nebo minutové pole v dolní části okna.
kalendář a vyberte si požadovanou dobu pro hodiny i minuty.

Pokud jsou datum a čas správné pro vstup, klikněte na tlačítko :guilabel:`Apply`.
- „Doba“: zobrazuje hodiny podle „Od“ a „Do“.
Při změně pole se mění i pole :guilabel:`To` (pole :guilabel:`From` se nemění).
(změna).

Jakmile zadáte požadované informace, klikněte na tlačítko „Uložit a zavřít“, abyste uložili vstup a zavřeli
přechodné okno.

.. obrázek: work_entries/create.png
:align:center
:alt:Vyplnění záznamu vytvoření formuláře v Odoo.

.. platové účty / konflikty:

Konflikty
=========

Konflikt se vždy objeví u jakéhokoliv požadavku, který nebyl schválený, jako například nemocenská nebo dovolená.
přítomnost chyb v záznamu práce, jako jsou nevyplněné povinné položky. Konflikty
musí být vyřešeny, než mohou být vystaveny výplatní pásky.

Každá pracovní položka, která má konflikt k vyřešení, je označena na hlavním panelu v záložce „Pracovní položka“.
dashboard, který lze zobrazit po kliknutí na:
Pracovní záznamy“. Výchozí nastavení zobrazuje pouze konflikty, které je nutné vyřešit.

Konflikty jsou označeny oranžovým trojúhelníkem v pravém horním rohu každého díla.
vstup. Kliknutím na konkrétní záznam práce se zobrazí datum a čas pro konkrétní záznam práce, pak
Klikněte na tlačítko „Upravit“ pro zobrazení podrobností konfliktu v okně.

.. obrázek:: work_entries/konflikt-pop-up.png
:align:center
:alt:Řádek konfliktů, který obsahuje podrobnosti o konkrétním konfliktu.

Konflikt je stručně vysvětlen v oranžovém rámečku v okně :guilabel:`Open`.
se objevuje.

V poli „Popis“, „Zaměstnanec“ a „Druh vstupu do práce“ jsou uvedeny
levém okně přesunout. Datum a časové rozpětí „Od“ a „Do“, jak je
Dále je zde uveden celkový čas (v hodinách) v poli Doba trvání.

Pokud je konflikt způsoben žádostí o dovolenou, která nebyla schválena, pak se jedná o :guilabel:`Dovolená`.
Pole se zobrazí na levé straně s typem dovolené v popisu.

.. obrázek: work_entries/conflict-details.png
:align:center
:alt:Podrobné okno konfliktu, které se objeví po kliknutí na tlačítko Upravit.

Konflikt času
------------------

Nejčastější pracovní spory vstupují do práce kvůli žádostem o volno, které byly podány, ale nebyly ještě schváleny.
schválené, což vede k tomu, že pro zaměstnance existují dva záznamy o pracovní době (jeden za dovolenou a druhý
pro běžnou práci).

Pokud dojde k konfliktu kvůli požadavku na volno, který je v systému pro stejný čas jako běžné
žádost o dovolenou již existuje, požadavek na volno je zadán v poli „Dovolená“.

Časová doba mimo konflikt lze vyřešit buď v okně pro přidání práce nebo ve více detailním čase.
okno s upozorněním, které se objeví na požádání.

Usnesení o vstupu do zaměstnání
~~~~~~~~~~~~~~~~~~~~~

Chcete-li vyřešit konflikt s časovou dotaci na tomto okně přehledu práce, klikněte na tlačítko „Schválit čas“.
Tlačítko „Off“ k schválení žádosti o dovolenou a vyřešení konfliktu v záznamu práce.

Tlačítka „Přijmout dovolenou“ a „Odmítnout dovolenou“ zmizí. Klikněte na
Tlačítko „Uložit a zavřít“ k uzavření okna s upozorněním. Konflikt zmizí ze seznamu
„Přihláška do práce“ panelu, protože konflikt byl vyřešen.

Rozhodnout o dovolené
~~~~~~~~~~~~~~~~~~~~~~~~~~~

K vyřešení konfliktu s časem dovolené na podrobné žádosti o volno klikněte na
Tlačítko „Vnitřní odkaz“ na konci řádku „Čas volna“.
Pokud je požadavek přijat, objeví se v novém okně s informacemi o požadavku. Požadavek lze upravit, pokud je to nutné.

Klikněte na tlačítko „Potvrdit“ k potvrzení požadavku a pak klikněte na tlačítko „Uložit a zavřít“.
tlačítko pro uložení změn a vrátit se zpět do okna konfliktu při vkládání práce.

.. obrázek:work_entries/time-off-details.png
:align:center
:alt: Žádost o dovolenou ve větším rozsahu.

Nyní je tlačítko „Přijmout dovolenou“ skryté a zobrazené je pouze tlačítko „Odmítnout dovolenou“.
Je vidět.

Pokud schválení bylo chybou, může být požadavek odmítnut zde kliknutím na tlačítko „Odmítnout“
Tlačítko „Volno“.

Od té doby, co byl čas volna schválen v okně času volna, klikněte na tlačítko „X“ v pravém horním rohu
a zavřít okno. Konflikt zmizí z panelu „Vstup do práce“, protože
Bylo vyřešeno.

... /výplatní pásky/obnovit záznamy o práci:

Obnovit záznamy práce
=======================

Při obnově pracovních vstupů jsou přepsány všechny ručně provedené změny, například vyřešené konflikty.
A práce jsou znovu vytvořeny (nebo znovu vytvořeny) z aplikací, které je vytvořily.

Tento způsob korekce velkého množství konfliktů je doporučen, aby byly všechny záznamy správné.
Konflikty mohou být řešeny individuálně, pokud jsou
vzniklé z jiné aplikace je nejlepší praxí zajistit záznamy v ostatních aplikacích
Jsou také správné. Proto se doporučuje řešit tyto konflikty v aplikacích,
vytvořil konflikt.

Dalším důvodem pro doporučení této metody je, že při obnovení pracovních záznamů
konflikt se znovu objeví, pokud je v související aplikaci nevyřešený.

Nejdříve zajistěte vyřešení problémů v konkrétních aplikacích, které způsobily vstup do práce.
konfliktů.

Dále klikněte na tlačítko „Obnovit záznamy o práci“ v horní části okna „Práce“.
Přihlášení do administrace a v okně se zobrazí tlačítko „Obnovení pracovního záznamu“.

Vyberte položku „Zaměstnanci“ z rozevírací nabídky a upravte
políčko „Od“ a „Do“, aby se zobrazila správná doba.

Klikněte na tlačítko „Obnovit záznamy o práci“ a záznamy o práci se znovu vytvoří.
pokud je dokončeno, okno se zavře.

.. obrázek: work_entries/regenerate-details.png
:align:center
:alt: Obnovit záznam práce pro konkrétního zaměstnance.

.. příklad::
Zaměstnanec má špatně vytvořené pracovní záznamy, které pocházejí z aplikace *Plánování*, protože
byly přiděleny dvě pracovní stanice současně. To by mělo být opraveno v *Plánování*.
místo aplikace *Mzdy*.

Pro opravu této chyby upravte rozvrh zaměstnance v aplikaci Plánování tak, aby byl
je správně přiřazen pouze jedné pracovní stanici. Pak v aplikaci Mzdy znovu vygenerujte výplatní lístky
pro konkrétního zaměstnance v daném časovém období.

Aplikace *Mzdy* pak stáhne nové a opravené údaje z aplikace *Plánování* a vytvoří nový výpočet.
správné záznamy o práci pro daného zaměstnance. Všechny konflikty pro tento zaměstnanec jsou nyní vyřešeny.

Výpočet výplatních pásek
===================

Chcete-li vytvořit výplatní pásky, přejděte do období, ve kterém by měly být vystaveny.
generovat. Zajistěte, aby se filtr „Konflikt“ odstranil. Když je požadovaný platový období
klikněte na tlačítko „Vytvořit výplatní pásky“.

.. tip::
Pokud tlačítko „Vytvořit výplatní pásky“ není aktivní (je světle fialové místo tmavě modré),
fialová barva) ukazuje na konflikt nebo datum vybrané v budoucnosti.
Vyřešte všechny konflikty před vytvořením výplatních pásek.

Když je kliknut na tlačítko „Vytvořit výplatní pásky“, objeví se vstup pro více položek na samostatné stránce.
za zvolené období.

Název série se vyplní do pole „Název série“ v předvoleném rozmezí „Od (datum) do (datum)“.
formát.

Datumová hranice platnosti výplatních pásek se zobrazuje v poli „Období“ a společnost
je uveden v poli „Společnost“ a není možné jej měnit.

Klikněte na tlačítko „Vytvořit náhledový záznam“ a vytvořte výplatní pásky pro celou sadu.

Klepněte na tlačítko „Mzdy“ v horní části stránky, abyste zobrazili všechny mzdy.
série.

.. obrázek:: práce_vstupů/generovat_platby.png
:align:center
:alt:Informace, která se zobrazuje při tvorbě výplatních pásek.

Tisk výplatních pásek
-----------------

Nejprve si zobrazte jednotlivé mzdy kliknutím na „Mzdy“
tlačítko na stránce s objednávkou.

Dále vyberte výplatní pásky k tisku ze seznamu „Výplatní pásky“. Klikněte na zaškrtávací políčko vedle každé
vytisknout výplatní pásku nebo klikněte na políčko vedle názvu sloupce „Referenční číslo“, abyste vybrali
všechny výplatní pásky najednou.

Klepněte na tlačítko „Tisk“ a vytvoří se soubor ve formátu PDF s vybranými výplatními páskami.

.. obrázek: work_entries/print-paychecks.png
:align:center
:alt:Tlačítko pro tisk výplatních pásek.

.. poznámka::
Tlačítko „Vytisknout“ se nezobrazí, dokud není vybrána alespoň jedna výplatní páska.
seznam.

Čas na hlášení
==================

Pokud je žádost o dovolenou podána na časový úsek, který byl již zpracován v výplatním lístku,
Žádost o dovolenou se objevuje na stránce Time Off v aplikaci Payroll, která je dostupná
navigace na:menu-selecetion:Mzdy - Pracovní doba - Odpovědnost za odpracovanou dobu.

Na stránce „Čas dovolené“ se žádost zobrazí s stavem „Přesunout na příští rok“.
pracovní smlouva. Důvodem je, že zaměstnanec byl již za tento den zaplacen a byl zaznamenán jako pracovní doba
strávené v práci, jako obyčejný pracovní den.

Aby byly správně vypočítány dovolené zaměstnance, musí být žádost o čas volna aplikována.
dalšímu výplatnímu období. To nejen zajišťuje aktuální stav žádostí o volno, ale také
odstraňuje potřebu opakovaně vkládat pracovní úvazky, rušit výplatní pásky a znovu vydávat výplatní pásky.

Nejčastější scénář, kdy k této situaci dochází, je ten, že výplatní pásky zpracováváme den nebo dva předem.
před koncem platové období a zaměstnanec náhle onemocní v posledních dnech platového období
době. Zaměstnanec požádá o dovolenou na den, který byl již vyplacen na mzdovém listu jako
běžný pracovní den. Namísto zrušení výplatního listu, úpravy záznamů o práci a znovuvydání
výplatní pásku, Odoo umožňuje požadavky na dovolenou aplikovat na následující výplatní období.
namísto.

Pro zobrazení všech žádostí o dovolenou, které musí být odloženy na další výplatní pásku, přejděte na
:menuvolba-->Mzdy-->Čas na dovolenou k vyúčtování“. Výchozí filtr pro tuto
report je: guilabel:"Odložit".

Všechny žádosti o volno, které se vztahují na následující platový období, jsou zobrazeny s
„Mzdový list státu“ do „Odložit na příští mzdový list“.

.. obrázek::work_entries/time-off-to-report.png
:align:center
:alt: Seznam všech žádostí o volno, které nebyly schváleny před vystavením výplatních pásek.

Přesunout více vstupů dovolené
-------------------------------

Klikněte na políčko v levém sloupci vedle řádku pracovního záznamu, který chcete odložit.
vstupy do seznamu pracovníků, klikněte na políčko vedle názvu sloupce „Zaměstnanci“
na prvním místě.

Jakmile je vybrána jakákoliv položka práce, objeví se na horní hraně zprávy dvě tlačítka:
Tlačítko „Vybráno“ a tlačítko „Akce“. Tlačítko „(#) Vybrané“ znamená
kolik záznamů je nyní vybráno.

Když jsou vybrány všechny požadované záznamy práce, klikněte na tlačítko „Akce“ a otevře se nabídka
se zobrazí několik možností. Klikněte na položku „Odložit do příštího měsíce“ v seznamu a všechny vybrané
Vstupy jsou odloženy na následující měsíc.

.. obrázek: work_entries/batch-defer.png
:align:center
:alt: Tlačítko akcí a tlačítka vybrané, které se objeví po provedení jakékoliv volby.

Odložte vstupy do individuálního volna
---------------------------------

Požadavky na dovolenou uvedené v seznamu „Čas dovolené k vyřízení“ lze odložit jednotlivě.

Klikněte na požadavek na dovolenou a zobrazí se podrobnosti o tomto požadavku.

Specifické podrobnosti o žádosti o dovolenou se zobrazují v levém sloupci a všechny
požadavky zaměstnance na dovolenou se zobrazují v pravé části, včetně požadavku
vlevo dole).

Klikněte na tlačítko „Zpráva do dalšího měsíce“
na vrcholu. Jakmile je zpracováno, zmizí tlačítko „Zpráva do dalšího měsíce“ a
Změna z „Vyčkat na další výplatní pásku“ na „Výpočet
v současném výplatním lístku.

Chcete-li se vrátit na seznam „Čas dovolené pro hlášení“, klikněte na „Dovolená“ v
Navigace pomocí kousků chleba.

.. obrázek: work_entries/single-defer.png
:align:center
:alt:Podrobnosti o dovolené pro individuální požadavek, který musí být odložen.

.. viz též:
:ref:`Nastavení pracovních vstupů <pracovni-vstupy-nastavit>`
