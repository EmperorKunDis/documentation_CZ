=============
Spojené státy
=============

.. |GAAP| nahradit za: :abbr:`GAAP (generálně přijímané účetní postupy)`
.. |FASB| nahradí:: :abbr:`FASB (Financial Accounting Standards Board)`
.. |SEC| nahradit za: zkratka: `SEC (Securities and Exchange Commission)`
.. |KOA| nahradit za: zkratka: `KOA (Kniha o účtech)`
.. |AR| nahradit:::zkratka: AR (Příjmy v hotovosti)
.. |AP| nahradit za: zkratka: „AP (Placení faktur)“
.. |CFS| nahradit za: zkratka: `CFS (Prohlášení o peněžních tocích)`
.. |NACHA| nahradit za: :abbr:`NACHA (National Automated Clearing House Association)`
.. |ACH| nahradit za :: abbr: `ACH (Automated Clearing House)`

Daňové lokalizace Odoo pro Spojené státy se řídí obecně přijatými
Účetní zásady (GAAP) účetních standardů a pravidel používaných k přípravě finančních výkazů.
jak je uvedeno v účetních standardách finanční správy (FASB) a přijatých Komisí pro cenné papíry (SEC).
Komise pro obchodování s cennými papíry (SEC).

.. viz též:
   - `Rada pro finanční účetnictví (FASB) <https://asc.fasb.org/Home>`_
   - „Komise pro cenné papíry a burzu (SEC)“

Dále je k dispozici série videí na téma účetnictví prostřednictvím e-learningu společnosti Odoo.
platformě. Tyto videa obsahují návod, jak začít od nuly, nastavit konfigurace a dokončit běžné
práce a poskytují podrobné pohledy na některé konkrétní případy použití.

.. viz též:
   - „Návody k Odoo: Účetnictví a fakturace
<https://www.odoo.com/slides/accounting-and-invoicing-19>
   - „Odoo SmartClass: Účetnictví <https://www.odoo.com/slides/smartclass-accounting-121>“

Konfigurace
=============

Níže jsou dostupné moduly v Odoo pro účetní použití ve Spojených státech.

.. poznámka::
Moduly uvedené níže jsou buď pouze pro odkaz nebo volitelné, protože jádro požadavků
provozovat pod americkým daňovým režimem v Odoo jsou již zahrnuty ve výchozím nastavení.
balíček, který byl nainstalován během inicializace databáze.

Zkontrolujte, zda je výchozí balík v používání, přejděte na:
V nastavení a v sekci „Daňové územní celky“ nahoře najděte položku „Obecný daňový obvod“.
Vybrat šablonu grafu, která se objeví vedle pole štítku „Paket“. Tento graf
šablona obsahuje potřebné nastavení pro lokalizaci USA v aplikaci Odoo Accounting.

.... obrázek: Spojené státy/US-L10N-generický šablona grafu.png
:align:center
:alt: Šablona grafu je přednastavena pro lokalizaci USA.

Instalace modulů
--------------------

Nainstalujte následující moduly, abyste získali všechny funkce Spojených států
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 25 25 50

   * Jméno
     - Technické označení
     - Popis
   * --:guilabel: Spojené státy - Účetnictví
     - „l10n_us“
     - Základní účetní modul pro lokalizaci USA.
   * - :ref:`US - Účetní zprávy <l10n_us/reports>`
     - l10n_us_reports
     - Přidává americké účetní zprávy.
   * :-:layout-checku-usa
     - „l10n_us_check_printing“
     - Umožňuje tisk plateb na předtištěný šekový papír. Podporuje tři nejčastější
kontrolovat formáty a bude fungovat bez nutnosti konfigurace s ověřovacími službami z checkdepot.net
<https://checkdepot.net/collections/pocka-na-vyber/odoo>.

       - Zkontrolujte nahoře: Quicken/QuickBooks Standard
<https://checkdepot.net/collections/pockety/odoo+top-check>`_
       - Zkontrolujte střed: Standard Peachtree
<https://checkdepot.net/collections/pockety-na-pc/odoo+stredni-check>`_
       - „Kontrola na dně: Standardní ADP
<https://checkdepot.net/collections/pockety-na-karty/odoo+Dno-Peněženka>`_

   * - :ref:`NACHA platby <l10n_us/nacha>`
     - l10n_us_payment_nacha
     - Export platby jako soubor NACHA pro použití v USA.
   * – :ref:`Zpráva 1099 <l10n_us/1099-report>`
     - l10n_us_1099
     - Exportujte údaje o příjmech z formuláře W-2 pro podání přiznání třetí straně.
   * :-:ref:`Avatax <l10n_us/taxes-avatax>`
     - „účet_s_avatary“
     - Modul pro integraci s :doc:`AvaTaxem <../accounting/taxes/avatax> v Odoo.
   * - :ref:`Spojené státy - Mzdy <l10n_us/payroll>`
     - „l10n_us_hr_payroll“
     - Zahrnuje potřebné pravidla pro mzdy v USA, včetně:

       - Podrobnosti o zaměstnanci
       - Smlouvy o pracovním poměru
       - Smlouvy založené na cestovním pase
       - Slevy a odpočty
       - Povolit konfigurace pro základní, hrubou a čistou mzdu
       - Příplatkový list zaměstnance
       - Součástí je integrace s řešením pro správu listů

   * - :ref:`Spojené státy - Mzdy s účetnictvím <l10n_us/payroll>`
     - l10n_us_hr_payroll_account
     - Obsahuje potřebné účetní informace pro pravidla platná v USA.
   * – :ref:`Spojené státy – Mzdy – Export do ADP <l10n_us/adp>`
     - „l10n_us_hr_payroll_adp“
     - Exportujte pracovní údaje do softwaru pro mzdy ADP.

.. _l10n_us/coa:

Klasifikační schéma
=================

:doc:`Účetní kniha (COA) <../accounting/get_started/chart_of_accounts>` pro Spojené státy
Státy lokalizace v Odoo jsou podle standardu |GAAP| strukturovány s účty seskupenými do
sedm hlavních kategorií, které odpovídají číselným hodnotám předcházejícím jednotlivým záznamům v deníku:

- Příjmy: zůstatek peněz (nebo kreditu), který je vůči podniku dlužen za dodané zboží nebo služby
dodané nebo použité, ale ještě nezaplacené zákazníky. Kód časopisu pro AR je
začínající na :guilabel:`1`.
- **Vypořádané závazky**: krátkodobé závazky podniku vůči svým věřitelům nebo dodavatelům.
nebyly ještě zaplaceny. Jako zdroj informací je uveden kód periodika označený (či začínající) zkratkou
:guilabel:`2`.
- **Akciová hodnota**: částka peněz, která by byla vrácena akcionářům společnosti, pokud by se prodaly všechny její akcie.
V případě likvidace byly majetkové hodnoty vypořádány a všechny závazky společnosti byly uhrazeny.
Zajištěnost je označena číslem periodika, které začíná na nebo obsahuje znak :guilabel:`3`.
:guilabel:`9`.
- **aktiva**: položky uvedené na účetní bilanci, které mají ekonomickou hodnotu nebo jsou schopny
generovat v budoucnu peněžní toky, jako je stroj, finanční nástroj nebo
patent. Zásoby jsou označeny číslem periodika, které začíná na znaku :guilabel:`1`.
- **Závazky**: odkazují na finanční dluhy nebo závazky společnosti, které vznikly během jejího trvání.
z obchodních operací. Závazky jsou označeny kódem účetního deníku, který je buďto označen nebo začíná
:guilabel:`2`.
- *Příjem* je synonymem pro *čistý zisk*. Jedná se o zisk společnosti po zaplacení všech výdajů.
všechny relevantní výdaje z prodejního příjmu vynaložené. Náklady jsou označeny kódem účetní knihy

- Náklady: náklady, které společnost vynaloží na dosažení zisku. Náklady jsou
indikované kódem časopisu označeným (nebo začínajícím) znakem „:guilabel:`6`“.

.. tip::
Předdefinované účty jsou součástí Odoa, jako součást |CoA|, který je nainstalován s USA
balíček pro místní nastavení. Účty uvedené níže jsou přednastaveny tak, aby prováděly určité operace
v rámci Odoo. Je doporučeno, aby tyto účty nebyly smazány; pokud je však potřeba provést změnu,
přejmenujte účty namísto toho.

...... seznamová tabulka::
:hlavičky: 1
:sloupky: 1

     * --:guilabel:Typ
       - :guilabel:`Název účtu“
     * :-:guilabel:`Vybavení“
       - |:guilabel:`Suspendovaný účet banky“
| :guilabel:`Výjimečné příjmy“
| :guilabel:`Nedoplatky“
|:guilabel:`Převod likvidity“
|:guilabel:`Ocenění akcií“
|: guilabel:`Stock Interim (Přijato)`
| :guilabel:`Stock Interim (Dodané)`
| :guilabel:`Náklady na výrobu“
     * -- :guilabel:`Příjem“
       - | :guilabel:`Zisk z devizových operací“
| :guilabel:`Rozdíl v hotovosti“
| :guilabel:`Zisk z cash discountu“
     * --:label:Náklady
       - |:guilabel:`Ztráta z cashbacku“
|:guilabel:`Ztráta z devizových operací“
| :guilabel:`Rozdíl v hotovosti“
     * – :guilabel:Současný roční výnos
       - :guilabel:`Nedotované zisky a ztráty“
     * -- :guilabel:`Příjmový účet“
       - :guilabel:`Příjmy za prodej“
     * :- guilabel:Doplatit
       - :guilabel:`Zálohy“

.. viz též:
   - :doc:`../účetnictví/začínáme/rozvaha“
   - :doc:`../účetnictví/začínáme/tabulka-slovníček-pojmů`

Zobrazit, upravovat a třídit účty
-----------------------------

Přejděte na stránku „Dashboard Chart of Accounts“ v Odoo kliknutím na:
--> Konfigurace --> Účetnictví: Skladová kniha.

Na panelu „Přehled účtů“ vytvořte nové účty kliknutím na
Tlačítko „Nový“ v pravém horním rohu panelu a vyplnění
příslušný formulář <chart-of-account/create>. Procházejte a třídějte existující účty pomocí
Specifické filtry „Filtr“ a „Skupina“ k dispozici v hledání
kliknutím na tlačítko „Přidat do košíku“.

Kliknutím na ikonu :icon:`fa-caret-down` :guilabel:`(caret down)` zobrazíte účty podle kategorie.
Přejděte do rozbalovací nabídky a pod položkou „Filtry“ najděte jednotlivé výběry.
Kliknutím na konkrétní kategorii se zobrazí pouze účty, které odpovídají danému filtru.

Zobrazit všechny dostupné typy účtů, odstraňte ve filtru v poli vyhledávání a pak klikněte
Ikona „fa-caret-down“ (caret down) pro přístup k rozbalovací nabídce.
Vyberte pole „Typ účtu“ pod nadpisem „Seskupit podle“. Zobrazí se všechny
Typy účtů v tabulce.

.. obrázek: united_states/us-l10n-coa-account-types.png
:align:center
:alt: Skupina účtů podle typu účtu.

Kromě struktury je v americké účetní osnově mnoho dalších klíčových rozdílů.
ve srovnání s ostatními zeměmi:

- **Specifika**: Americké účetní standardy (US GAAP) často vyžadují podrobnější účetnictví než některé jiné země.
To může zahrnovat samostatné účty pro různé typy příjmů, výdajů a aktiv.
podrobnější informace ve finančních výkazech.
- **Povinnosti v oblasti regulačních předpisů**: V USA existují konkrétní povinnosti stanovené
ať už jde o požadavky organizací jako je |SEC| pro veřejně obchodované společnosti, které mohou ovlivnit
strukturu a obsah COA, aby splňovaly standardy pro hlášení.
- **Praktiky v odvětvích**: V některých oblastech Spojených států mohou být účetní postupy specifické.
požadavky nebo speciální struktury |COA|. Například finanční instituce často mají
účty specifické pro půjčky, investice a úrokový výnos.
- Daňové přemýšlení: |COA| může také zahrnovat daňová přemýšlení, jako jsou účty pro
příspěvky na odpočet úroků, závazky a daňové rezervy, aby se zajistilo dodržování daňových předpisů.
usnadnit podání daňového přiznání.

Tyto rozdíly nakonec by měly být odráženy v samotné struktuře |COA|, přičemž je třeba přidat
nových účtů, pokud je to nutné, aby vyhověly požadavkům amerického účetnictví.

.. viz též:
   - :ref:`Vytvořit nový účet <chart-of-account/create>`
   - :doc:`../../základy/vyhledávání`

... _l10n_us/taxes:

Daně
=====

Daňové sazby a co se považuje za danitelné se v USA liší podle právního řádu. Výchozí *Prodej*
A daň z převodu vlastnictví se automaticky vytvoří, když je nainstalována aplikace Odoo „Účetnictví“.
Pro správu stávajících nebo konfiguraci dalších daní přejděte na:
Konfigurace --> DPH“.

...

AvaTax
------

**Avalara AvaTax** je cloudbasedový software pro výpočet daní a dodržování předpisů, který integruje
Odoo pro několik lokalizací. Propojení AvaTax s Odoo poskytuje reálný čas a specifický region
daňové výpočty při prodeji, nákupu a fakturaci položek v databázi.

.. důležité::
AvaTax je k dispozici pro integraci do databází/firem, které mají pobočky ve Spojených státech.
Státy a Kanada. Podrobnější informace najdete v dokumentaci k účetnictví Avataxu na téma daňové země.
informace.

.. viz též:
Řešení pro integraci a konfiguraci účtu AvaTax naleznete v příslušných článcích dokumentace.
Odoo databáze:

   - :doc:`Integrace AvaTaxu <../účetnictví/daně/avatax>`
   - :doc:`Portál Avalara pro správu daní <../accounting/taxes/avatax/avalara_portal>`
   - :doc:`Vypočítat daně s AvaTax <../accounting/taxes/avatax/avatax_use>`
   - Daňová souladnost USA: Video o e-learningu AvaTax

   - Podpora společnosti Avalara: „O AvaTaxu“
<https://community.avalara.com/support/s/document-item?language=en_US&bundleId=dqa1657870670369_dqa1657870670369&topicId=About_AvaTax.html&_LANG=enus>

...

Zprávy
=======

K dispozici je několik :doc:`výběrů zpráv <../účetnictví/reporting>`, které jsou k dispozici pro USA.
lokalizace v podmenu „Účetnictví - Zprávy“ pod položkou „Aplikace účetnictví“:

- :ref:`Výkaz zisku a ztráty <účetnictví/zprávy/výkaz zisku a ztráty>“: „snímek“ finanční situace společnosti
pozice v určitém čase, která obsahuje přehled majetku společnosti.
základní kapitál, závazky a vlastní kapitál.
- :ref:`Zisk a ztráta <účetnictví/zprávy/rozvaha>“: jinak známý jako *P&L výkaz* nebo
*Výkaz zisku a ztráty* poskytuje souhrn příjmů, výdajů a zisků/ztrát společnosti za
určité období.
- :ref:`Výkaz o peněžních tocích <l10n_us/cash-flow-statement>“: ukazuje, kolik hotovosti a ekvivalentů v hotovosti
společnost obdržela a utratila v daném časovém úseku.
- :ref:`Shrnutí výkonné části<účetnictví/zprávy/výkonná část>“: shrnující zpráva, která pokrývá
významné ukazatele finanční pozice společnosti, jako jsou tržby, zisk a
dluh.
- :ref:`Daňový výkaz <účetnictví/výkazy/daňový výkaz>“: oficiální formulář předkládaný finančnímu úřadu
které vykazují příjmy, výdaje a další relevantní informace o dani. Daňové přiznání umožňuje daňovým poplatníkům
vypočítat daňovou povinnost, naplánovat termíny plateb daně nebo požádat o vrácení přeplatku.
daňového přiznání v Odoo lze provádět měsíčně, každé dva měsíce, čtvrtletně, každé čtyři měsíce.
a pololetně.
- :guilabel:`Soubor účetních záznamů“: zpráva, která zobrazuje hotovostní transakce (bez ohledu na deník).
s výpisem po transakci. Výpis je viditelný pouze v hlášeních *US - Accounting Reports*.
(modul l10n_us_reports) nainstalován.
- :ref:`Zpráva 1099 <l10n_us/1099-report>“: stahování souboru CSV s platbami, které byly provedeny nezaměstnaným osobám.
doba pro podání elektronicky v třetí straně. Viditelné pouze s *1099 Reporting*.
(modul l10n_us_1099 nainstalován).

... l10n_us/report-filters:

Podle typu zprávy jsou na horní části panelu k dispozici určité filtry:

- filtr dat, který je označen ikonou „kalendář“ před textem
datum ve formátu MM/DD/YYYY. Použijte tento parametr k výběru konkrétního data nebo data v rozmezí pro zprávu.
- filtr „Srovnání“, který porovnává zprávní období s jiným.
jiné
- filtr časopisu, který je znázorněn ikonou „Kniha“ (book) a výchozím
nastavení: „Všechny časopisy“. Tento filtr použijte k určení, které časopisy mají být zahrnuty
v zprávě.
- filtr typu „vstupy“, který je označen ikonou :icon:`fa-filter` :guilabel:`(filtr)`
Výchozí nastavení „Pouze vložené položky, účetní metoda“. Tento filtr používejte k určení
jaké záznamy v deníku by měly být zahrnuty do zprávy (např. publikované nebo napsané).
například typ účetního systému (tj. daňový nebo výnosový).

  - Tento filtr má také několik možností zobrazení, například „Skrýt hranice na nule“.
:větší relevance, včetně možnosti rozdělení horizontálně s názvem `Split Horizontally`, aby se zpráva
nad okrajem obrazovky, což odstraňuje potřebu procházení.


:srovnání: střed
:alt:Filtr metody účtování pro zprávy, který pokrývá metodu oceňování vytvořené zásoby a metodu hotovostní.

- *desetinný* filtr, který standardně zahrnuje i částky s haléři, jak je uvedeno
:guilabel:`V nastavení .$`. Použijte ostatní možnosti v rozevíracím seznamu k změně čísla v
hlásit celá čísla ([:guilabel:`V $“]), tisíce ([:guilabel:`V K“]) nebo miliony
formátech (*.m$).
- filtr *přizpůsobení zprávy*, který je označen ikonou :icon:`fa-cogs` :guilabel:`(gears)` a používá se
tento filtr k přizpůsobení současných sekcí a položek v zprávě nebo k vytvoření nových zpráv.
požadované.

.. viz též:
   - :doc:`Účetní výkaznictví <../accounting/reporting>`
   - :doc:`../../základy/vyhledávání`

... _l10n_us/1099-report:

Zpráva o příjmech z prodeje
-----------

Zpráva o výdělcích dostupná po instalaci modulu „Výdělek“ pomocí příkazu
modul (l10n_us_1099), který zahrnuje platby prováděné nezaměstnaným osobám za určité období.
období. Využijte k dispozici ke stažení souboru CSV z hlášení v Odoo pro elektronické podání platby 1099
přes třetí stranu.

Pro vytvoření zprávy 1099 přejděte na: „Účetnictví“ → „Zprávy“ → „Správa“.
Klikněte na tlačítko „1099 Report“ pro otevření dialogového okna „1099 Report“.

Nejprve zadejte rozsah dat transakcí, které chcete ohlásit, do pole „Datum začátku“ a
:guilabel:`Datum ukončení“ pole.

Poté upravte záznamy v deníku, které se zobrazují na průvodci. Klikněte na tlačítko „Přidat řádek“ pro přidání
chybějící položky. Ujistěte se, že odstraníte všechny položky, které nemají být součástí zprávy
kliknutím na ikonu „fa-times“ a poté na řádek.

Konečně, když jsou všechny potřebné položky zahrnuty v hlášení formuláře 1099, klikněte na tlačítko „Vytvořit“.
tlačítko. To stáhne soubor CSV, který seskupuje transakce podle příjemce.
Platby.

... _l10n_us/cash-flow-statement:

Výkaz o peněžních tocích
-------------------

Přejděte na stránku „Výkaz o peněžních tocích“ (CFS) kliknutím na:
Hlášení --> Zpráva o výsledku hospodaření: Výkaz o peněžních tocích. Zde lze vygenerovat zprávu o peněžním toku
použít různé filtry, které jsou k dispozici na horní části stránky.
přístrojová deska.

Odoo používá metodu přímého pohybu peněz k sestavení výkazu o peněžních tocích, která měří skutečné peníze.
příjmy a výdaje z obchodních operací, např. když je od zákazníků přijato hotovost
Při platbách hotově dodavatelům.

Výchozí účet je označen některým ze tří výchozích štítků :guilabel:.
Dashboard „Skladová kniha“ bude součástí zprávy, která obsahuje:
„Provozní aktivity“, „Finanční aktivity“ a „Investiční aktivity“.
Extraordinární aktivity“.

.. obrázek: united_states/us-l10n-cash-flow-statement-tags.png
:align:center
:alt:Příklady účtů označených v Odoo, které jsou zahrnuty v rozvaze.

Dále pak v Odoo výkaz o peněžních tocích:

- je omezen na knihu bank a kasu, aby odrážela peníze vstupující nebo opouštějící účet.
- obsahuje také účty „Náklady“, které ukazují protistranu transakcí vůči „Bance“ nebo „Hotovosti“.
deníkové záznamy, přičemž vyloučí aktivity |AR| a |AP|.

.. příklad::
Vytvořte fakturu dodavateli za 100 dolarů jako provozní výdaj (nebo ne |AP|). Tímto způsobem se **nebude odrážet**
transakce na výkazu peněžních toků. Je však nutné zaregistrovat odpovídající platbu ve výši 100 $.
a transakce se projeví na výkazu zisku a ztrát jako:guilabel:`Výdaje za hotovost
„Provozní aktivity“.

.... obrázek:united_states/us-l10n-operating-expenses-example.png
:align:center
:alt: Příklad faktury zaregistrované jako provozní výdaj v rámci výkazu o peněžních tocích.

…_l10n_us/hotovostni-sleva:

Sleva v hotovosti
=============

Slevu z ceny lze nastavit v aplikaci „Účetnictví“ pod položkou „Platební podmínky“.
Doba splatnosti lze nastavit s hotovostní slevou a sníženou daní.

.. viz též:
:doc:`../účetnictví/fakturace/hotovostní slevy“

...

Vyplňování šeků
==============

Využívat šeky je stále běžnou platební praxí v USA. Ujistěte se, že máte správný formát šeků pro Spojené státy
Modul pro lokalizaci USA („l10n_us_check_printing“) je nainstalován podle odkazu:

Pro tisk šeků z Odoo přejděte na: „Účetnictví--> Konfigurace-->
Nastavení a najděte sekci „Dodavatelské platby“. Zde zaškrtněte políčko „Šeky“
zaškrtávací políčko, které odhaluje několik polí pro konfiguraci kontroly.

Vyberte předtištěný nebo prázdný štítek „Zkontrolovat rozložení“ z rozevírací nabídky:

- :guilabel:`Tisková kontrola (Horní) – USA“
- :guilabel:`Tisková kontrola (Střední) - USA“
- :guilabel:`Tisková kontrola (Dno) - USA“
- :guilabel:`Tisk prázdné šekové knížky (shora) - USA“
- :guilabel:`Tisk prázdné šekové karty (střední) - USA“
- :guilabel:`Tisk prázdného šeku (dolní část) - USA“

Dále vyberte, zda chcete nebo nechcete zaškrtnout políčko „Vyžadovat více stránek“.

Pokud je třeba, nastavte volitelně :guilabel:`Zkontrolujte horní okraj“ a :guilabel:`Zkontrolujte levý okraj“.

Jakmile jsou všechny konfigurace kontrolních bodů dokončené, uložte nastavení pomocí tlačítka „Uložit“.

.. tip::
Formáty předtištěných šeků (šeky bez prázdných políček) vyžadují předtištěný papír od třetích stran.
„Předtištěné šeky od CheckDepot.net <https://checkdepot.net/collections/odoo-checks>“
doporučeno.

.. důležité::
Využijte jeden z volných formulářů pro tisk informací o šeku, když je potřeba.
vyžaduje použití obou :abbr:`MICR (Magnetic Ink Character Recognition)“ inkoustů nebo tonerů, které
s normami pro tisk šeků, stejně jako s papírem pro kvalitu šeku
<https://checkdepot.net/collections/blank-check-paper/products/top-format-blank-check-paper-cdt164>.
Další informace, například název společnosti, číslo účtu a číslo šeku, se tiskne při
vytvoření šeku na libovolnou částku.

.. viz též:
:doc:`../účetnictví/platby/výplaty“

... _l10n_us/mzdy:

Mzdy
=======

Aplikace *Mzdy* je zodpovědná za výpočet mzdy zaměstnance s přihlédnutím k veškerým
mzdu, dovolenou a nemocenské, benefity a slevy. Aplikace *Mzdy* získává informace ze
aplikace *Přítomnost zaměstnanců*, *Časové listy*, *Volno*, *Zaměstnanci* a *Náklady*, k výpočtu
odpracované hodiny a odměna každého zaměstnance.

Když používáte externího poskytovatele mzdy, jako je například společnost ADP, musíte vyexportovat různé
údaje související s mzdami, jako jsou záznamy o pracovních dnech, vrácení výdajů, daně, provize a další.
relevantní data, takže je lze nahrát do mzdového systému, který pak vydá skutečné
výplatní pásky nebo přímo vloží peníze na účet zaměstnance.

Před exportem mezd je nutné nejprve ověřit a zkontrolovat práce.
Další informace najdete v dokumentaci „vstupy do práce“ (doc:work_entries)
V souvislosti s ověřováním pracovních vstupů.

Jakmile jsou pracovní záznamy ověřeny, mohou být exportovány do ADP.

Po vyplacení mezd zaměstnancům lze platby zpracovat do sestav, ověřit a
přidány do příslušných účetních deníků, aby byly všechny finanční záznamy v Odoo aktuální.

Povinné informace
--------------------

Je důležité mít aplikaci „Zaměstnanci“ nainstalovanou a všechny informace o zaměstnancích.
obydlené. V několika polích v obou záznamů o zaměstnancích :ref:`<l10n_us/payroll-employee-records>` se
stejně jako v pracovních smlouvách (viz <l10n_us/payroll-employee-contracts>) jsou nutné.
správně zpracovat mzdu zaměstnance. Zajistit vyplnění následujících polí v příslušných
míst.

https://www.irs.gov/pub/irs-pdf/f425106.pdf

Personální záznamy
~~~~~~~~~~~~~~~~

V každém záznamu zaměstnance je různá data, která aplikace *Mzdy* vyžaduje pro správné
zpracování výplatních pásek, včetně různých informací o bance, daních a práci.

Přejděte na aplikaci „Zaměstnanci“ a vyberte záznam zaměstnance, abyste mohli zobrazit sekce
formulář zaměstnance, který přímo ovlivňuje *Mzdy*:

- Karta „Informace o práci“

  - :guilabel:`Adresa práce“: ukazuje, kde se zaměstnanec nachází včetně státu, ve kterém
Ať už se jedná o výpočet daně, nebo jinou částku.
  - :guilabel:„Čas práce“: určuje způsob výpočtu mzdy a zda zaměstnanec dostane
přesčas.

- Karta „Osobní údaje“:

  - :guilabel:`Číslo SSN“: poslední čtyři číslice sociálního pojištění zaměstnance
na výplatních páskách.
  - :guilabel:`Číslo účtu“: číslo účtu spojené s platbou v souboru NACHA.

- Karta „Nastavení HR“:

  - :guilabel:`Stav daňového přiznání federální vlády“: stav daně, který zaměstnanec používá pro platby daní
výpočty, které mohou být odlišné od jejich státního postavení.
  - :guilabel:`Státní daňový stav“: daňový status, který zaměstnanec používá pro svou část daně
výpočet záloh na dani z příjmu.
  - :guilabel:`Formulář W-2“: daňový formulář ukazující souhrn mzdy, daní a benefitů vyplácených zaměstnancům
zaměstnanci za daňový období (obvykle jeden rok).
  - :guilabel:`Formulář W-4“: formulář, který pomáhá vymezit částku federálních daní, která má být odečtena
zaměstnanci, který platí společnost IRS.

... _l10n_us/payroll-employee-contracts:

Smlouvy o pracovním poměru
~~~~~~~~~~~~~~~~~~

Další informace se nachází v pracovní smlouvě a také ovlivňuje
Aplikace pro mzdy.

Přejděte na stránku „Zaměstnanci -> Zaměstnanci -> Smlouvy“ a vyberte smlouvu.
zaznamenat části smlouvy, které přímo ovlivňují *Mzdy*:

- :guilabel:`Obecné informace“:

  - :guilabel:`Typ struktury mzdy: Spojené státy: Zaměstnanec“ definuje, kdy je zaměstnanec placen.
pracovní dobu a typ vstupu do práce.
  - :guilabel:`Zdroj vstupu do práce“: určuje, jak se počítají pracovní vstupy.

- Karta „Informace o mzdě“:

  - :guilabel:`Číslo SSN“: poslední čtyři číslice sociálního pojištění zaměstnance
na výplatních páskách.
  - :guilabel:`Způsob výplaty mzdy“: určuje, zda je zaměstnanec placen fixní mzdou nebo
Mzda za hodinu.
  - :guilabel:`Plánované platby“: určuje, jak často je zaměstnanec placený, buď :guilabel:`Ročně“,
:guilabel:`Půlročně“, :guilabel:`Čtvrtletně“, :guilabel:`Dvouměsíčně“, :guilabel:`Měsíčně“
:guilabel:`Půlročně“, :guilabel:`Dvakrát ročně“, :guilabel:`Ročně“ nebo :guilabel:`Denně“.
Nejčastější jsou měsíční, pololetní (24 plateb za rok) nebo dvoutýdenní (26 plateb za rok).
  - :guilabel:'Mzda, roční a měsíční náklady': slouží k zobrazení celkových nákladů na zaměstnance.
doporučuje nejprve vyplnit platbu za rok, protože se automaticky vyplní ostatní
pole.
  - :guilabel:`Před zdaněním příspěvky“: vyplňte tento odstavec podle výběru zaměstnance.
Předdaniové výhody snižují hrubou mzdu a tím i základ daně.
v horní části výplatního lístku.
  - :guilabel:`Příjmy po zdanění“: tyto příjmy jsou odečteny až poté, co byly vypočítány daně.
Tyto se objevují na konci výplatního lístku před zobrazením čisté částky.

.. viz též:
:doc:`Dokumentace zaměstnanců <../../hr/employees/new_employee>`

... _l10n_us/adp:

Export pracovních vstupů do ADP
--------------------------

Požadavky
~~~~~~~~~~~~

Pro vytvoření zprávy, která může být nahrána do ADP, je potřeba provést několik prvotních konfiguračních kroků
, které je třeba nejprve dokončit.

Nejdříve se ujistěte, že modul „Export do ADP“ („l10n_us_hr_payroll_adp“) je
:ref:`nainstalovaný <general/install>“.

Poté musí mít společnost v nastavení firmy zadaný kód ADP. Pro jeho zadání přejděte na
:menu:„Mzdy“ --> „Konfigurace“ --> „Nastavení“. Zadejte do pole :guilabel:„ADP kód“
sekci „Lokalizace USA“.

Dalším krokem je uvést správný kód ADP v poli *Externí kód* pro
každý typ vstupu, na který se odkazuje.

Konečně každý zaměstnanec musí mít v pracovní smlouvě vyplněn kód ADP.
Přejděte na: menu-selection: „Zaměstnanecká aplikace“, vyberte záznam zaměstnance a otevřete: gui-label: „Personal
Karta Nastavení. V sekci ADP kód zadejte :guilabel:`ADP Code`.

Kód „ADP Code“ je způsob, jakým společnost ADP identifikuje konkrétního zaměstnance, obvykle
šestimístné číslo.

.. viz též:
   - :ref:`mzdy/nová práce“
   - :/doc/:hr/zamestnanci/novy-zamestnanec

Exportní data
~~~~~~~~~~~

Jakmile jsou ověřeny záznamy o práci (viz doc:work_entries), informace mohou být
Exportovat do souboru CSV, který lze následně nahradit v ADP.

Pro vývoz dat přejděte na: „Mzdová aplikace --> Hlášení --> Spojené státy: ADP
Export“, pak klikněte na „Nový“. Následně zadejte „Datum začátku“ a „Datum ukončení“.
pro práci s kalendářem v podobě připnuté lišty.

Poté zadejte pole „Identifikátor sady“ hodnotou „:guilabel:Batch ID“. Doporučení pro toto pole je
zadat datum ve formátu „RRRR-MM-DD“, následované jakýmkoliv znakem k odlišení.
Specifický výrobní šarže, například název oddělení nebo jakékoliv jiné charakteristické vlastnosti šarže.

Do příslušného pole zadejte „Popis sady“. Tento popisek by měl být krátký
popisný, ale odlišný od :guilabel:`Název souboru s daty`.

Zajistěte, aby správná společnost vyplňovala pole :guilabel:`Company`. Vyberte požadovanou společnost pomocí
pokud je potřeba.

Nakonec přidejte informace o pracovním vstupu zaměstnance do seznamu. Klikněte na tlačítko „Přidat řádek“ a
Pop-up okno „Přidat zaměstnance“ se načte. Seznam lze filtrovat podle :doc:`dokumentace
„Hledat“ a snadno najít zaměstnance, kteří mají být přidáni do seznamu.

.. tip::
Řiďte se datovým vývozem v několika skupinách namísto jedné velké, která obsahuje všechna data.
zaměstnanci. To pomáhá smysluplně rozlišit jednotlivé dávky a zpracování je díky tomu
celkově udržitelné. Nejčastěji se zaměstnanci dělí podle oddělení nebo na základě výše mzdy
(hodinová nebo platem).

Vyberte zaměstnance, kteří mají být přidáni do seznamu, zaškrtnutím políčka vedle jejich jména.
vybraní zaměstnanci jsou vybráni, klikněte na tlačítko „Vybrat“ v levém dolním rohu.
A zaměstnanci se objevují v seznamu.

Pro vytvoření souboru CSV klikněte na tlačítko „Vytvořit“ v pravém horním rohu.

... https://www.irs.gov/pub/irs-pdf/f8352.pdf

ACH – elektronické převody
==========================

Automatizovaná centrální banka (ACH) je moderní způsob převodu peněz elektronicky mezi
bankovní účty, které nahradily tradiční papírové metody. ACH platby jsou běžně používané pro
přímé vklady, platby účtů a obchodní transakce.

Přijímat platby ACH: integrace platebního poskytovatele
--------------------------------------------------

Platby ACH jsou podporovány integracemi platebních služeb Authorize.net a Stripe v Odoo.

.. viz též:
   - :ref:`Nastavení služby Authorize.net pro platby ACH (Odoo) <authorize/ach_payments>`
   - Dokumentace o zpracování platebních příkazů pro malé firmy společnosti Authorize.net

   - :doc:`Nastavení Stripe pro platby ACH (Odoo) <../payment_providers/stripe>`
   - „Dokumentace Stripe k ACH Direct Debit <https://docs.stripe.com/payments/ach-debit>“

.. _l10n_us/nacha:

Převádějte peníze: soubory NACHA
--------------------------

Odoo může vytvořit soubor kompatibilní s Národním automatizovaným systémem pro zpracování plateb (NACHA) |ACH|.
odeslat na účet společnosti. Každý jednotlivý *Bank* časopis, který chce společnost zaplatit svým dodavatelům
s, do databáze Odoo je potřeba vložit konfigurační sekci NACHA.

Konfigurace
~~~~~~~~~~~~~

Nejprve přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Deníky“. Otevřete
bankovní časopis a klikněte na záložku „Výstupy“.

.. obrázek: us-l10n-nacha-settings.png
:align:center
:alt: Konfigurace NACHA (National Automated Clearing House Association) v Odoo.

.. poznámka::
Následující informace o konfiguraci |NACHA| obvykle poskytuje finanční společnost.
instituci, jakmile bude schváleno posílání plateb přes jejich účet.

Pod sekcí označenou „Konfigurace NACHA“ jsou pole potřebná k vytvoření
Vytvořte soubor NACHA/ACH, který můžete odeslat na účet společnosti. Nejprve zadejte číslo směrovacího kódu
finanční instituci v oblasti označené štítkem „Okamžitá cílová destinace“. Tato informace je
je běžně k dispozici na internetu a obecně se liší podle místa pobočky. Toto číslo je obvykle
Poskytnuté při prvotním nastavení účtu.

Dále do pole s názvem „Registrovaný název finanční instituce“ zadejte
:guilabel:`Země“. Tuto informaci poskytne banka nebo kreditní unie.

Po poli „Země“ následuje pole „Okamžitý původ“. Zadejte
Do pole zadejte devítimístné identifikační číslo společnosti nebo identifikační číslo zaměstnavatele (EIN).
poskytnuté finanční institucí.

Dále zadejte číslo identifikace společnosti, které je desetimístné a skládá se z
spojit devítimístné identifikační číslo společnosti nebo číslo zaměstnavatele (EIN) s dalšími
číslo na začátku sekvence, které často bývá „1“. Zkontrolujte u finanční
první číslo by měl instituce ověřit, aby se ujistila, že je správné, protože tento údaj je poskytován.
pro schválené účty.

Zadejte následně číslo identifikátoru původního finančního institutu (DFI) podle značky :guilabel:`Originating DFI Identification`, které by mělo obsahovat přidělené
8místné číslo finanční instituce.

.. důležité::
Do této části zadejte přesné číselné hodnoty, které uvedla finanční instituce společnosti.
(např. banka nebo družstevní záložna) jim je poskytla, jinak hrozí neúspěšné |NACHA|
konfigurace v Odoo.

.. obrázek: united_states/us-l10n-nacha-dropdown.png
:align:center
:alt:Nastavení NACHA s vybraným výchozím kódem položky.

Další pole má dvě možnosti: „Kód standardní vstupní třídy“. Vyberte
položky v rozbalovacím menu napravo od pole a vyberte buď „Korporátní kredit nebo debet (CCD)“
nebo:guilabel:`Předem sjednané platby a vklady (PPD)“. Tato informace bude poskytnuta
finanční instituce. Výchozí hodnotou je „Korporátní kredit nebo debet (CCD)“.

Poslední možností je: „Vytvořené vyvážené soubory“. Zaškrtněte políčko vedle
pole, abyste mohli zvolit možnost „Vygenerované vyvážené soubory“. Konzultujte s účetním společnosti.
finančního poradce, který vám pomůže učinit informované rozhodnutí pro tento obor.

Manuálně uložte konfiguraci kliknutím na ikonku „Cloud Upload“
ikonu nebo odhlásit se z obrazovky a nechat aplikaci uložit automaticky. Konfigurace je nyní dokončena.

... _l10n_us/batch-payment:

Vytvořit hromadnou platbu
~~~~~~~~~~~~~~~~~~~~

Teď si každou platbu v Odoo zaznamenejte pomocí platebního metodu |NACHA|.

.. viz též:
:ref:`Zadání plateb v Odoo <účetnictví/platební příkazy/z platebního dokladu faktury>“

.. důležité::
Buďte si vědomi termínu pro platby provedené v den podání žádosti. Pokud je soubor dat s budoucí datumem,
spojené s každou platbou nebo soubor musí být odeslán před datem uzávěrky, pokud jsou data
musí být včetně dnešního data. Přesný čas pro připsání peněz na účet zjistíte u finanční instituce
za zpracování stejnodenních plateb.

Jakmile jsou všechny platby, které mají být zahrnuty v souboru |NACHA| |ACH|, provedeny, je potřeba
jejich vytvoření z nabídky „Akce“ ve složce „Ikony“.

Pro vytvoření hromadné platby přejděte na stránku plateb kliknutím na:menuselection:Účetnictví
Výběr dodavatelů –> Platby. Zvolte všechny platby, které mají být zahrnuty do |NACHA| |ACH|
soubor, zaškrtnutím políček vlevo od sloupců.

.. obrázek: united_states/us-l10n-create-batch-payments.png
:align:center
:alt:V okně plateb je vyznačeno akční menu s volbou vytvořit hromadnou platbu
vybráno.

.. důležité::
Všechny platby v transakční sadě musí sdílet stejný způsob platby NACHA.

Dále přejděte do sekce „Skládané platby“ (v menu zvolte „Účetnictví –> Příjemci –> Skládané platby“).
Klikněte na platbu, kterou právě vytvořili a pak klikněte na záložku „Exportovaný soubor“.
generovaný soubor je uveden s datem vytvoření pod :guilabel:`Generation Date`. Klikněte na :icon:`fa-download`
Tlačítko „Stáhnout“ (download) pro stažení souboru.

.. obrázek: united_states/us-l10n-batch-file.png
:align:center
:alt:Vyexportovaný soubor označený v seznamu plateb s odkazem na stažení.

Pokud je třeba provést nějaké úpravy, klikněte na tlačítko „Znovu vygenerovat exportní soubor“.
nový soubor NACHA.

.. viz též:
   - :doc:`../účetnictví/platby/souhrnné platby
   - :doc:`Přímé inkaso v Evropě <../accounting/payments/batch_sdd>`
