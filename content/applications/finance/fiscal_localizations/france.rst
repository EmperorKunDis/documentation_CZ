======
Francie
======

... /lokalizace/francie/konfigurace/moduly:

Moduly
=======

Následující moduly související s francouzským lokalizováním jsou k dispozici:

.. seznam tabulkový::
:hlavičkové řádky: 1

    * Jméno
      - Technické označení
      - Popis
    * --:guilabel:Francie - Účetnictví
      - „l10n_fr_account“
      - Francouzská:ref:`daňová lokalizační sada <fiscal_localizations/packages>“, která se vztahuje pouze
společnostem sídlícím na pevninské Francii a nezahrnuje zámořské území.
    * --:guilabel:`Francie - Účetní zprávy“
      - l10n_fr_reporty
      - Export francouzského přiznání k DPH, které lze zaslat na DGFiP, OGA nebo profesionální
účetní.
    * --:guilabel:Francie - Mzdy a účetnictví
      - l10n_fr_hr_mzdy
      - Zahrnuje potřebné účetní informace pro francouzské pravidla výplaty mzdy.
    * ---:guilabel:`Francie - Faktura-X a Chorus Pro``
      - l10n_fr_facturx_chorus_pro
      - Přidá pole potřebná pro odeslání faktur do Chorus Pro
<lokalizace/francie/elektronické fakturace>.
    * Francie - dovoz
      - l10n_fr_fec_import
      - Import standardních souborů FEC, které jsou užitečné pro import účetní historie.
    * --:guilabel:Francie - Ověření prodejního místa na základě DPH (CGI 286 I-3 bis)
      - „l10n_fr_pos_cert“
      - Certifikace proti podvodům s DPH na místě prodeje
<lokalizace/francie/vat-anti-fraud-certification>

.. poznámka::
Jádro modulů lokální verze je nainstalováno automaticky s lokálním nastavením. Ostatní mohou
je nutné je ručně nainstalovat:doc:`</applications/general/apps_modules>`.

.._lokalizace/francie/lok-přehled:

Přehled lokalizace
=====================

Francouzská lokalizace balíčku zajišťuje soulad s francouzskými daňovými a účetními předpisy.
obsahuje nástroje pro správu daní, fiskální pozice, reportování a předdefinovanou strukturu účetních knih
přizpůsobené francouzským standardům.

Francouzský balíček lokalizace poskytuje následující klíčové funkce, které zajišťují soulad s místními
Daňové a účetní předpisy:

- :doc:`../účetnictví/začínáme/rozvaha`: předdefinovaný struktura přizpůsobená francouzskému účetnictví
účetní standardy
- :doc:`../accounting/taxes/fiscal_positions`: automatické daňové úpravy podle zákazníka nebo
stav registrace dodavatele
- Daňové sazby (<../accounting/taxes>) - přednastavené daňové sazby včetně DPH.
nulové sazby a osvobozené možnosti
- :doc:`Mzdy </applications/hr/mzdy>`
- :ref:`Hlášení <localizations/france/reporting>`

..._lokalizace/francie/hlášení:

Reportáž
---------

Instalace aplikace „Francie – Účetnictví“ z modulu „Aplikace a moduly“
Modul `l10n_fr_account` umožňuje přístup k některým specifickým účetním zprávám pro Francii, například:

- :guilabel:`Účetní výkaz (FR)`
- :guilabel:`Výsledovka (FR)`
- :guilabel:`Daňový přehled (FR)`

... /francie/účetnictví:

Účetnictví
==========

..._lokalizace/francie/elektronické fakturace:

Elektronické fakturace
-----------

Portál „Chorus Pro“ <https://portail.chorus-pro.gouv.fr/aife_csm>“, spravovaný agenturou
Financial Information Systems of the State) je oficiální platforma pro podávání elektronických
fakturace pro veřejné francouzské instituce. Umožňuje podnikům odesílat a spravovat faktury, sledovat jejich
stav zpracování a přístup k aktualizacím plateb od ledna 2020 je možné elektronické fakturace
povinná pro všechny obchodní transakce mezi vládou a podniky ve Francii. Odoo podporuje integraci
s Chorus Pro podávat faktury vytvářené v Odoo.

..._lokalizace/francie/elektronické fakturace - konfigurace:

Konfigurace
~~~~~~~~~~~~~

Pro zaslání faktur do Chorus Pro je potřeba následující konfigurace:

#Nainstalujte modul „Francie – Faktury X“ podle návodu v příručce.
s modulem Chorus Pro (`l10n_fr_facturx_chorus_pro`).
#Registrace do systému PEPPOL, neboť faktury jsou odesílány z Odoa na
Choros Pro přes síť :ref:`Peppol <fakturace-online/peppol>`.
#Pokud ještě nemáte účet Chorus Pro, přejděte na stránku „Chorus Pro“.
na stránce <https://portail.chorus-pro.gouv.fr/aife_csm> klikněte na „Vytvořit účet“
Vytvořit si ji.
#.:ref:Nastavte kontaktní formulář pro příslušné zákazníky
<lokalizace/francie/elektronické fakturace kontakty>.

.. viz též:
„Dokumentace Chorus Pro <https://portail.chorus-pro.gouv.fr/aife_documentation>“

..._lokalizace/francie/elektronické fakturace kontakty:

Zákazníci
*********

Přidat fakturu do Chorus Pro lze takto:

#Zajistěte, aby bylo vyplněno pole „Stát“ a poté zvolte „DPH“.
:guilabel:`Identifikační číslo“ a zadejte příslušné číslo.
#V záložce „Prodej a nákup“ zkontrolujte, že je vyplněno pole „SIRET“.
#V záložce „Účetnictví“ vyplňte následující pole v záložce „Zákazník“.
Součástí faktur je:

   - Vyberte „BIS Fakturace 3.0“.
   - V dalším poli zkontrolujte, že je vybráno „Francie - SIREN“, a poté do pole napište „11000201100044“.
odkazovaný v Chorus Pro.

..._lokalizace/francie/elektronické fakturace - faktury:

Vystavování faktur do Chorus Pro
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chcete-li zaslat fakturu společnosti Chorus Pro, postupujte takto:

#Přejděte na záložku „Účetnictví“ – „Zákazníci“ – „Faktury“ a otevřete nebo vytvořte fakturu.
#Ujistěte se, že následující pole jsou vyplněna v záložce „Další informace“:

   - „Zákaznický odkaz“: „Provádějící službu“ v Chorus Pro
   - :guilabel:`Smluvní reference“: :guilabel:`Číslo zakázky“ v Chorus Pro
   - :guilabel:`Referenční číslo objednávky“: „Právní zastoupení“ v Chorus Pro

#Zkontrolujte fakturu.
#Klikněte na tlačítko „Odeslat“ a v okně „Tisk a odeslání“ zaškrtněte políčko „Přes Peppol“.
#Klikněte na tlačítko „Odeslat“.

Jakmile je faktura odeslána, stav faktury se změní na „Dokončeno“.

.. viz též:
:ref:`Peppol <elektronické-fakturace/peppol>`

..._lokalizace/francie/fec:

FEC - Účetní záznamy
--------------------------------------

Auditní soubor FEC :dfn:`Fichier des Écritures Comptables` obsahuje všechny účetní záznamy.
všechny záznamy v účetních denících za finanční rok. Zápisy do souboru musí být
musí být uspořádány chronologicky. Od ledna 2014 je každá francouzská společnost povinna vydat
a v případě žádosti finančního úřadu o kontrolu předat tento soubor.

..._lokalizace/francie/fec-import:

FEC Import
~~~~~~~~~~

:doc:`Nainstalujte modul </applications/general/apps_modules>` „Francie – dovoz zboží“
modul pro import souborů FEC z jiného softwaru („l10n_fr_fec_import“).

Chcete-li tuto funkci aktivovat, přejděte do sekce „Účetnictví“ - „Konfigurace“ - „Nastavení“.
:guilabel:`Účetní import“ v sekci „Import“, klikněte na ikonu „oi-arrow-right“ a poté
„Dodání FEC“. V okně „Dodání FEC“ nahrajte soubor FEC a klikněte
:guilabel:`Doprava“.

.. poznámka::
Import FEC souborů z různých let nevyžaduje žádné zvláštní kroky ani výpočty.
pokud více souborů obsahuje zprávy „Reports à Nouveaux“ s počátečním stavem za rok
Tyto záznamy jsou v systému Odoo označeny jako zbytečné a mohou být vymazány.

... /lokalizace/francie/fec-souborové formáty:

Formáty souborů
************

.. poznámka::
   - Soubory FEC musí být ve formátu CSV, protože formát XML není podporován.
   - Soubor FEC CSV je textový soubor s tabulkovou strukturou. První řádek slouží jako
hlavička, která definuje seznam polí pro každý záznam, a každá další řádka představuje
účetní záznam bez konkrétního uspořádání.

FEC soubory musí splňovat následující technické specifikace:

- Kódování: UTF-8, UTF-8-SIG a iso8859_15.
- *Za oddělovač* se považuje jedna z následujících znakových kombinací: středník, lomítko nebo tabulátor.
- Koneční znaky řádku: obě skupiny znaků CRLF (\r\n) a LF (\n) jsou podporovány.
- Formát data: `YYYYMMDD`

... /fr/fec-fields:

Popis a použití polí
**************************

+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|#|Název pole|Popis|Použití|Formát|
+====+===============+======================================+===================================+=================+
|01|Kód časopisu|Kód časopisu                             |`journal.code` a `journal.name` |Alfanumerické  |
|  |               |                                              | pokud není zadána knihovna JournalLib |                 |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|02|JournalLib|Jméno časopisu                            |jméno časopisu|Alfanumerické|
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
| 03 | ErituraNum   | Číslování specifické pro každý časopis   | move.name                        | Alfanumerické  |
|     |              | číslo sekvence vstupu            |                                  |                 |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
| 04 | Datum zápisu do účetnictví | Datum účetní operace             | move.date                        | Datum (yyyyMMdd) |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|05|CompteNum     |Číslo účtu                               |`account.code`                      |Alfanumerické   |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|06|CompteLib   |Název účtu                              |`account.name`                      |Alfanumerické    |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|07|CompAuxNum   |Číslo vedlejšího účtu                       |partner.ref                      |Alfanumerické  |
|     |              | (přijímá NULL)                            |                                  |                 |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|08|CompAuxLib   |Druhý účet - popis účtu               |partner.name                     |Alfanumerické  |
|     |              | (přijímá NULL)                            |                                  |                 |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|09|PoložkaRef       |Odkaz na dokument                          |„přesunutí“ a „název“           |Alfanumerické  |
|     |              |                                             | pokud není zadáno pole „EcritureNum“ |                 |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
| 10 | Kusová položka | Datum dokumentu                         | `move.date`                      | Datum (yyyyMMdd) |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|11|EcritureLib|Záznam v účetnictví - popis položky|`move_line.name`|Alfanumerické|
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
| 12 | Debet         | Počáteční částka                      |`move_line.debit`                 | Plovoucí          |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
| 13 | Kredit         | Počet kreditů                          | `move_line.credit`               | Plovoucí desetinné číslo
|     |              |(Název pole „Kredit“ není povolený) |                            |                 |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|14|Příslušnost účetního záznamu k účetnímu případu | Číslo odpovídajícího účetního záznamu | move_line.fec_matching_number | Alfanumerické
|     |              | (přijímá NULL)                            |                                  |                 |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|15|Datum vstupu do účetnictví|Datum účetního záznamu             |nevyužito                           |Datum (yyyyMMdd) |
|     |              | (přijímá NULL)                            |                                  |                 |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|16|Datum platnosti||Datum ověření účetního záznamu||nepoužívané||Datum (yyyyMMdd)|
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
| 17 | Množství v měně | Počet v měně                            | `move_line.amount_currency`     | Float           |
|     |              | (přijímá NULL)                            |                                  |                 |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|18|Idevise      |Identifikátor měny                     |`currency.name`                   |Alfanumerické  |
|     |              | (přijímá NULL)                            |                                  |                 |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+

Tyto dva pole se objevují ve stejném pořadí jako ostatní a nahrazují je.

+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|12|Částka         |Částka                                |`move_line.debit`              |Plovoucí            |
|     |               |                                          | nebo `přesunout_účet.kredit`         |                 |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+
|13|Senz         |Může být „C“ pro kredit           |určuje proměnnou move_line.debit  |Char            |
|    |               | nebo „D“ pro debet                      | nebo `move_line.debit`            |                 |
+----+---------------+--------------------------------------+-----------------------------------+-----------------+

... /implementace_francouzské_verze

Drobné detaily implementace
**********************

Do účetních jednotek importované z FEC souborů patří: **Účty, deníky, partneři**.
a **Pohyby**. Modul automaticky určuje kódování, oddělovače řádků a znaky oddělující jednotlivé části
do souboru. Následně je provedeno kontrolování, aby každá řádka měla správný počet polí
souhlasí s hlavičkou. Pokud kontrola proběhne úspěšně, celý soubor se přečte, uloží do paměti a
a naskenovány. Následně jsou pak účetní jednotky importovány postupně v pořadí, které je uvedeno níže.

.._lokalizace/francie/účty FEC:

Účty
^^^^^^^^

Každá účetní položka je spojena s účtem identifikovaným v poli :guilabel:`CompteNum`.

..._lokalizace/francie/kód FEC shody:

Souhlas kódu
^^^^^^^^^^^^^

Pokud uživatelský účet s tímto kódem existuje, používá se stávající místo vytvoření nového.
jedna. V Odoo se čísla účtů řídí výchozím počtem číslic fiskální lokalizace.
Modul FEC je spojen s francouzským lokalizací, výchozí délka účtu je šestimístná.
To znamená, že se zaokrouhlují čísla účtů a porovnávají se pouze účty s různými kódy.
kódy v souboru FEC a ty již v Odoo jsou vypočítány pouze na základě prvních šesti číslic
kódy.

.. příklad::
Řádek v souboru s kódem účtu „65800000“ odpovídá existujícímu účtu „658000“ v Odoo.
a stávající účet se používá namísto vytvoření nového.

..._lokalizace/francie/fec-souznění-vlajka:

Společná vlajka
^^^^^^^^^^^^^^^^^

Účet je technicky označen jako *srovnatelný*, pokud první řádek, ve kterém se objevuje, obsahuje
V poli „Zápis do knihy“ je vyplněno pole „EcritureLet“, což znamená, že účetní záznam bude srovnán.
s jiným.

.. poznámka::
Pole může být na řádku prázdné, ale záznam musí být v souladu s
neevidované platby. Účet je označen jako vyrovnaný, jakmile jsou do něj importovány pohybové řádky
Je nezbytné, aby ji vyžadovaly.

..._lokalizace/francie/fec-typ-účtu:

Typ účtu a šablony shodné
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Protože typ účtu není specifikován v formátu FEC, nové účty jsou vytvářeny s
Výchozí typ: guilabel:„Aktiva“. Po dokončení procesu importu jsou shodné s
nainstalovány šablony účetních výkazů. Výchozí hodnota vlajky „srovnat“ je také nastavena touto cestou.

Srovnání je prováděno porovnáním nejlepších číslic, začínající od všech číslic.
Tři číslice a pak dvě.

.. příklad::

   +------------+------------+-----------------+---------------------+---------------------+
|Název      |Kód        |Úplná shoda     |Třímístné porovnání |Dvoumístné porovnání |
   +============+============+=================+=====================+=====================+
|Šablona      | 400000       | 400000         | 400                 | 40                 |
   +------------+------------+-----------------+---------------------+---------------------+
| Číslo účtu | „40100000“ | „40100000“       | „401“             | „40“              |
   +------------+------------+-----------------+---------------------+---------------------+
|  výsledek  |             |                 |                     |  hledaný zápas      |
   +------------+------------+-----------------+---------------------+---------------------+

Tento typ účtu je pak označen jako :guilabel:`payable` a :guilabel:`reconcilable“ na základě
šablona účtu.

.._lokalizace/francie/fec-časopisy:

Časopisy
^^^^^^^^

Časopisy jsou kontrolovány proti existujícím v Odoo, aby se zabránilo duplicitám i při importu
více souborů s opakováním.

Pokud existuje časopis s tímto kódem, použije se stávající časopis namísto vytváření nového.
nový.

Nové časopisy mají připojen k názvu zkratku „FEC-“. Například „ACHATS“
se stává:guilabel:`FEC-ACHATS`.

.. poznámka::
Časopisy nejsou archivovány, takže uživatelé je mohou spravovat podle svého uvážení.

..._lokalizace/francie/fec-noviny-typ:

Určení typu časopisu
^^^^^^^^^^^^^^^^^^^^^^^^^^

Typu časopisu není přiřazen žádný formát (podobně jako u účtů), a je vytvořen
s výchozím typem :guilabel:`obecný“.

Na konci procesu dovozu se stanoví typ časopisu podle následujících pravidel
v souvislosti s příbuznými pohyby a účty:

- | :guilabel:`banka`: Všechny pohyby v těchto knihách obsahují řádek (kredit nebo debet), který ovlivňuje
účet likvidity.
|:guilabel:"hotovost" / :guilabel:"banka" lze zaměnit, takže je přiřazena hodnota :guilabel:"banka".
Toto podmínky splňuje.
- | :guilabel:`prodej`: V těchto časopisech se pohybuje především s kladnými účty na straně dlužníků
úvěry na účtech daňového příjmu.
|Záznamy o vrácení zboží jsou obrácené, tzn. že se na nich zobrazuje kreditní částka jako dluh a debetní částka jako přeplatek.
- | :guilabel:`nákup`: V těchto knihách se pohybují především kreditní linie na účtech splatných.
účetních položek na účtech nákladů.
|Záznamy o vrácení nákupu jsou obrácené, tj. účetní zápis je zadán jako kredit/debet.
- |:guilabel:`generální`: používá se pro vše ostatní.

.. poznámka::
   - Minimálně tři pohyby jsou nutné k identifikaci typu časopisu.
   - Hranice 70 % pohybů musí splňovat kritéria pro určení typu časopisu.

.. příklad::
Předpokládejme, že analyzujeme pohyby, které sdílejí určitý :guilabel:`journal_id`.

   +------------------------------------------------------------+-------+------------+
|Pohyby                                                          |Počet|Procento|
   +============================================================+=======+============+
|které mají prodejní účetní řádek, ale žádný nákupní účetní řádek|0|0|
   +------------------------------------------------------------+-------+------------+
|které mají nákupní účetní případ a žádný prodejní účetní případ| 1     | 25 %       |
   +------------------------------------------------------------+-------+------------+
|které mají v účetnictví položku pro likviditu       | 3     | **75 %**   |
   +------------------------------------------------------------+-------+------------+
| Celkem                                                        | 4     | 100%       |
   +------------------------------------------------------------+-------+------------+

Časopis by byl označen jako „banka“, protože procento pohybu banky (75 %)
Překročila hranici (70 %).

..._lokalizace/francie/fec-partneři:

Kontakty
^^^^^^^^

Každý kontakt má své :guilabel:`Reference` z pole :guilabel:`CompAuxNum`.

.. poznámka::
Tyto pole jsou vyhledatelná na základě předchozích importů FEC pro účely fiskálního a auditorského dohledu.

.. tip::
Podobné a potenciálně duplicitní kontakty lze sloučit pomocí aplikace pro čištění dat.

... /fr/fec-move:

Pohyby
^^^^^

Příspěvky jsou zveřejňovány a vyrovnávány okamžitě po odeslání s :guilabel:`EcritureLet`.
pole, které se používá k shodě s poli v záznamu.

:guilabel:`EcritureNum` představuje název tahů, ale někdy může být nevyplněný.
prázdné. V takových případech se místo něj používá pole :guilabel:`PieceRef`.

..._lokalizace/francie/fec-kulaceni-problem:

Problémy s přibližováním
^^^^^^^^^^^^^^^

Přesnost se počítá podle měny pro částky kreditu a debetu (tj. 0,01
EUR). Pokud je rozdíl v rámci této tolerance, přidá se k pohybu nová linka s názvem
„Rozdíl při zpracování importu“, cílené na následující účty:

- „658 000“ Poplatky za běžný účet, pro další převody
- „758 000“ Různé produkty pro správu běžných účtů, za další kredity

... _lokalizace/francie/fec-chybějící-název-pohybu:

Chybějící název tahu
^^^^^^^^^^^^^^^^^

Pokud pole :guilabel:`EcritureNum` není vyplněno a pole :guilabel:`PieceRef` je prázdné
vhodná k určení názvu pohybu (může být použita jako odkaz na řádek účetního pohybu).
je nemožné určit, které řádky by měly být zařazeny do jednoho pohybu, což v praxi znamená
Vytváření vyvážených pohybů.

V takových případech se pokusíme seskupit všechny řádky podle stejného časopisu a data.
(:guilabel:'JournalLib', :guilabel:'Datum psaní'). Pokud tato skupina vygeneruje vyvážené pohyby
Pokud je součet kreditu roven součtu debetu, pak každá jiná kombinace záznamu a data vytváří nový
přesunout se.

.. příklad::
„ACH“ + „2021/05/01“ --> nový záznam v deníku „ACH“ s názvem „20210501“.

Pokud se tento pokus nezdaří, zobrazí se chybová hláška s uvedením všech řádků přesunu, které jsou považovány za
nevyvážené.

..._lokalizace/francie/fec-informace-o-partnerech:

Kontaktní informace
^^^^^^^^^^^^^^^^^^^

Pokud je v poli uvedena kontaktní informace, bude kopie přenesena do pohybu účetnictví, pokud
cílový titul je typu :guilabel:`platný“ nebo :guilabel:`přijatelný“.

.._lokalizace/francie/fec-export:

FEC Export
~~~~~~~~~~

Pro stažení FEC přejděte na: „Účetnictví > Zprávy > Obecný účetní deník“. Klikněte
Ikona „Kolečko“ (gear) a výběr „FEC“.
okně „Vytvoření souboru FEC“, vyplňte následující pole:

- :guilabel:`Datum začátku“
- :guilabel:`Datum ukončení platnosti“
- :guilabel:`Testový soubor“: Zapněte tuto možnost, abyste mohli otestovat generování souboru s FEC.
- :guilabel:`Vynechat řádky na 0“: Zapněte tuto volbu, pokud je potřeba.
- :guilabel:`Vyloučené časopisy“: Vyberte časopis(y), které chcete vyloučit.

Následně klikněte na tlačítko „Vytvořit“.

.. viz též:
   - Oficiální technická specifikace (fr)
<https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000027804775>
   - „Test-Compta-Demat (Oficiální nástroj pro testování FEC)
<https://github.com/DGFiP/Test-Compta-Demat>`

... /lokalizace/francie/daňový doklad:

Daňová přiznání
--------------

*Liasse fiscale* je soubor standardizovaných finančních dokumentů, které
podniky musí ročně předkládat finančnímu úřadu, který je komplexně shrnuje.
finanční činnosti a určuje korporátní daně.

„Teledec“ je platforma, která se používá k přípravě a podání daňového přiznání pomocí dat
z účetních záznamů. Synchronizovat svá účetní data uložená v Odoo s
Elektronicky zašlete své společnosti daňové přiznání do DGFiP (Generální finanční ředitelství).
Publiques), postupujte takto:

#:ref:`lokalizace/francie/účet teledec`
#:ref:`lokalizace/francie/teledec-registrace
#:ref:`lokalizace/francie/teledéčko synchronizace`

.._lokalizace/francie/teledec-účet:

Vytvoření účtu na Teledecu
~~~~~~~~~~~~~~~~~~~~~~~~

Vytvořit účet na Teledecu můžete přes stránku „Teledec Account Creation Page <https://www.teledec.fr/s-enregistrer>“.
a do pole „E-mailová adresa“ zadejte e-mailovou adresu. Zvolte silné heslo
Přijmout obchodní podmínky zaškrtnutím políčka a klikněte na tlačítko „Registrovat se“.
Uložit. Poté zadejte klávesovou zkratku SIREN (Systém identifikace podniků).
Identifikační číslo obchodního rejstříku) společnosti.

.. poznámka::
Pokud účet již existuje, klikněte na tlačítko „Uživatelský účet je registrován“.

.._lokalizace/francie/teledec-registrace:

Informace o registraci společnosti a účetním období
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro registraci společnosti na Teledec klikněte v levém menu na „Vaše společnosti“ a poté
:guilabel:`Uložit vaši firmu“ (Save your business) a ujistěte se, že vyplníte následující
informace o společnosti v poli „Kontaktní údaje“ (Contact details).
Sekce „Zástupce právní“ (Legal representative):

- :guilabel:`Název společnosti`: Název společnosti.
- Forma právní subjektivity: Vyberte právní formu společnosti.
- :guilabel:`Účty jsou uzavřeny do: Datum uzávěrky.
- :guilabel:`Daňový režim a způsob podání daňového přiznání“: Vyberte daňový režim a způsob podání daňového přiznání.
- :guilabel:`Sídlo společnosti“: Sídlo společnosti.
- :guilabel:`Jméno právního zástupce`: Jméno právního zástupce.
- :guilabel:`V zastoupení za: `: Funkce právního zástupce.
- :guilabel:`Telefonní číslo“: Telefonní číslo.

Klikněte na tlačítko „Uložit“ (Save).
:guilabel:`Obecné informace o vyhlášeném cvičení“
daňovém roce). Pak vyplňte informace o finančním roce, například začátek a konec fiskálního roku
datum nebo datum ukončení a dobu trvání předchozího účetního období. Po uložení se zobrazí
Zahrnuty jsou i dokumenty z daňového přiznání, včetně běžných formulářů.
Ty, které jsou přizpůsobeny daňovému přiznání společnosti.

.. tip::
   - Sloupec „Stav“ (Stav) ukazuje postup podání dokumentů.
   - Klikněte na „Dokončit“ pro dokončení dokumentu a poté klikněte na „Uložit“.
   - Pro tisk prázdné verze prohlášení klikněte na „Tisknout prohlášení“.
Vyberte možnost „Tisknout prohlášení s upozorněním“.

..._lokalizace/francie/teledéček_synchronizace:

Synchronizace s Odoo
~~~~~~~~~~~~~~~~~~~~

Chcete-li, aby Odoo automaticky vyplnilo údaje pro :guilabel:`Liasse fiscale“, klikněte
„Jiné akce“ (Ostatní akce) v pravém horním rohu a vyberte
„Synchronizovat s jiným programem“ (Synchronize with other software).
:guilabel:`Synchronizovat tuto řadu s Odoo“ (Synchronizovat tuto řadu s Odoo).

V okně „Synchronizovat tuto řadu s Odoo“ vyplňte následující
informace pro dokončení synchronizace:

- :guilabel:`Název/URL databáze Odoo“: Název nebo URL databáze Odoo.
celé URL adresy databáze, zapnout:guilabel:"Chci dát celou URL mimo odoo.com"
volitelná položka.
- :guilabel:`Jméno uživatele`: Jméno spojené s účtem Odoo.
- :guilabel:`API klíč`::ref:`Vytvořený API klíč pro instanci Odoo<api/external_api/keys>“.

.. poznámka::
Ve více společnostech je potřeba v Odoo nastavit následující konfigurace:

   - Uživatel spojený s vygenerovaným klíčem API musí mít
:ref:`přístup <obecné/firemní/uživatelé> k firmě určené pro synchronizaci.
   - Tato společnost musí být také nastavena jako výchozí pro uživatele, a to pomocí :guilabel:`Default Company`, protože Teledec vždy
se synchronizuje s výchozím společností uživatele.

Dále klikněte na tlačítko „Importér“ a synchronizujte data z Odoo.
Okno „Potvrzení synchronizace sériového čísla s Odoo“ zkontrolujte částky a
udělat všechny potřebné změny a pak kliknout na tlačítko :guilabel:`Importovat zůstatek`.
synchronizace daňového přiznání s Odoo a import zůstatku.

.. důležité::
Pokud kliknete na tlačítko „Importovat zůstatek“, mohou být přepsány nebo změněny manuální aktualizace.
předtím.

Pro provedení platby a odeslání prohlášení správci daně klikněte na:guilabel:`Platba & odeslání
z prohlášení.

.._lokalizace/francie/pos:

Prodejní místo
=============

... /fr/vat-anti-fraud-certification:

Certifikace proti podvodům s DPH
----------------------------

Od ledna 2018 platí ve Francii a jejích zámořských územích nové protikorupční zákony
teritorií (DOM-TOM). Tato legislativa stanovuje specifické požadavky na integritu
zabezpečení, uložení a archivace prodejních dat. Odoo těmto právním požadavkům vyhovuje
a modul, který je ke stažení v certifikátu shody.

Pro společnosti je povinné mít v prodejně pokladní systém proti podvodům, například Odoo (čl. 286 CGI, odst. 3bis).
Daňovým subjektem ve Francii nebo v zámořském území je někdo, kdo má zákazníky - spotřebitele (B2C). Tato pravidla se
Všem firmám, ale OSVČ od DPH jsou zasaženy.

.. viz též:
   - Často kladené otázky
<http://www.economie.gouv.fr/files/files/directions_services/dgfip/controle_fiscal/actualites_reponses/logiciels_de_caisse.pdf>
   - Oficiální prohlášení
<http://www.impots.gouv.fr/portail/bofip/10691-PGP.html?identifiant=BOI-TVA-DECLA-30-10-30-20160803>
   - „Článek 88 zákona o financích z roku 2016
<https://www.legifrance.gouv.fr/affichTexteArticle.do?idArticle=JORFARTI000031732968&categorieLien=id&cidTexte=JORFTEXT000031732865>`_

... /lokalizace/francie/pos-odoo-certifikace:

Odoo certifikace
~~~~~~~~~~~~~~~~~~

Finanční správa požaduje od všech firem doložit certifikát o shodě, který potvrzuje, že
jejich software je v souladu s předpisy proti podvodům. V případě porušení může být uložena pokuta ve výši 7500 eur.
nařízené.

.. poznámka::
„Tento certifikát <https://www.odoo.com/my/contract/french-certification/>“ uděluje společnost Odoo
SA pro uživatele Odoo Enterprise.

Pro získání certifikátu postupujte podle těchto kroků:

#Instalovat aplikaci „Francie – Zákaz podvodů s DPH“ z modulu „Aplikace a moduly“.
Certifikace pro modul Point of Sale (CGI 286 I-3 bis) („l10n_fr_pos_cert“).
#Zadejte pole „Stát“ na záznamu společnosti v aplikaci „Obecné informace / Firmy“.
aby byly vstupy šifrovány pro kontrolu nezměnitelnosti.
#Stáhněte si povinný „certifikát o shodě“.
<https://www.odoo.com/my/contract/french-certification/>, dodané společností Odoo SA.

..._lokalizace/francie/pos-proti-podvodům:

Anti-podvodné funkce
~~~~~~~~~~~~~~~~~~~

Antifraudový modul nabízí následující funkce:

- :ref:`Nepřenositelnost <lokalizace/francie/pos-nepřenositelnost>`
- :ref:`Bezpečnost <lokality/francie/pos-bezpecnost>`
- :ref:`Skladování <localizations/france/pos-storage>`

... /fr/pos-inamodifikovatelnost:

Nepřenositelnost
**************

Všechny metody k zrušení nebo změně klíčových dat v objednávkách na prodejním místě, fakturách a účetních položkách jsou
deaktivována pro společnosti sídlící ve Francii nebo v jakémkoli zámořském území.

.. poznámka::
V prostředí více společností jsou dopadnuty pouze dokumenty těchto společností.

.._lokalizace/francie/bezpecnostni-opatreni:

Bezpečnost
********

K zajištění nesmazatelnosti jsou všechny objednávky nebo záznamy zašifrovány při ověření.
(nebo haš) je vypočítán z klíčových dat dokumentu a haše předchozích dokumentů.
Modul zavádí rozhraní pro testování nezměnitelnosti dat. Test selže, pokud dojde k jakémukoliv
Informace je upravena v dokumentu po jeho ověření. Algoritmus znovu vypočítá všechny hašovací funkce
a porovnává je s počátečními. V případě selhání systém ukazuje první
pozměněný dokument zaznamenaný v systému.

Pouze uživatelé s přístupem :doc:`administrátorů </applications/general/users/access_rights>
zahájit kontrolu nezměnitelnosti:

- Pro objednávky na prodejně přejděte do: „Systémové nastavení“ - „Zprávy“ - „Kontrola nezměnitelnosti POS“.
- Pro záznamy do deníku přejděte na: „Fakturace / Účetnictví --> Konfigurace --> Nastavení“.
V sekci „Zprávy“ klikněte na „Stáhnout kontrolu nezměnitelnosti dat“.
Report.

.._lokalizace/francie/přístřešky:

Skladování
*******

Systém také zpracovává automatické uzavírání obchodů denně, měsíčně a ročně. Takové uzavírky
vypočítat celkový prodej za období a součet všech prodejů od prvního
Záznam v systému.

Chcete-li zobrazit uzavřené transakce, přejděte na: „Prodejní místo“ - „Zprávy“ - „Uzavření prodeje“.
:menu-vyber->Fakturace/Účetnictví-->Zprávy-->Uzavření obchodu.

.. poznámka::
   - Zavírací operace počítají celkové částky pro účetní případové studie prodejních knih (Typ záznamu = Prodeje).
   - Pro více společnostní prostředí jsou takové zavírání prováděna společnostmi.
   - Příkazy POS se zaznamenávají jako zápisy v deníku při ukončení POS relace. Uzavření POS
se může kdykoli udělat. Modul uživatele nutí k tomu, aby to dělali každý den.
obnovení relace, která byla otevřena více než před 24 hodinami. Taková relaci je nutné zavřít
znovu prodávat.
   - Výsledný součet období je počítán z všech účetních záznamů, které byly po posledním uzavření
stejného typu bez ohledu na datum jejich vystavení. Při zaznamenání nové prodejní transakce
uzavřený období se započítá do dalšího závěrku.

.. tip::
Pro účely testování a ověření lze uzavírky ručně vytvářet v režimu vývojáře:
</developera-režimu>. Chcete-li tak učinit, přejděte na: „Nastavení“ -> „Technické“ -> „Plánované akce“.
V seznamu plánovaných akcí otevřete požadovanou akci „Uzavření prodeje“ a klikněte
:guilabel:`Spustit ručně“.

.._lokalizace/francie/povinnosti:

Povinnosti
~~~~~~~~~~~~~~~~

Odinstalací této modulu se smaže bezpečnostní haše. To znamená, že systém již nebude
zajistit integritu dat z minulosti.

Uživatelé jsou zodpovědní za svůj systém Odoo a musí ho obezřetně provozovat. Změna zdrojového kódu
Odpovědnost za zajištění integrity dat nesmí být přenášena na jiné osoby.

Odoo není odpovědný za jakékoliv problémy s funkčností modulu, pokud jsou způsobeny nezajištěnou
aplikace třetích stran.
