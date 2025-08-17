=======================
Hlášení nezastižených osob
=======================

Nedokončené případy jsou případy, u kterých máte naplánované aktivity, které jsou buď v pořádku nebo již splatné.
Každá aktivita je v systému Odoo sledována a pokud má být splněna do určitého data, systém pošle uživateli e-mailovou zprávu.
je přiděleno.

Zpráva o nezpracovaných příležitostech zahrnuje všechny aktivní příležitosti v potrubí s pohledávkami nebo s prodlením.
aktivity, které umožňují prodejnímu manažerovi identifikovat příležitosti, na kterých je třeba okamžitě pracovat.

Sales manažeři mohou pomocí denního nevyřízeného požadavků reportu připomenout svým týmům, aby se věnovali
dokončit výjimečné aktivity předtím, než se stanou pozdními, pomáhat zabránit zanedbaným kontaktům a posilovat
aktivní chování svých obchodníků.

Příklad:

Prodejní manažer začíná svůj den tím, že si přečte nevyřízené poptávky a poté přepne na
V seznamovém pohledu vidí následující:

.... obrázek: unattended_leads_report/unattended-leads-example.png
:synchronizace: střed


Jejich člen týmu Mitchell má dvě vedení v fázi návrhu aktivit.
splatné.

Ikona žlutého tlačítka „☎️“ značí, že vedoucí projektu „Modern Open Space“ má telefon.
telefonní hovor, který byl naplánovaný na dnešek. Červená ikonka „✉️“ (poštovní schránka) značí, že je plánováno 5 VP
Vedoucí pracovníků má v plánu e-mailovou aktivitu, která je již přesčasována.

Kliknutím na odkaz „5 křesel ve vedení“ se objeví záznam o tomto kontaktu a manažer prodeje zkontroluje
chvilku. Vidí, že e-mail byl naplánován na odeslání před dvěma dny, ale Mitchel nikdy neoznačil
tuto činnost jako hotovou.

.... obrázek:unattended_leads_report/přeplněné aktivity - e-mail.png
:synchronizace: střed
:alt: Příklad upozornění na nedodané aktivity v chatovací místnosti vedoucího.

.. důležité:
Pro vytvoření nevyužívaného zprávy o prodejích musí být týmy obchodníků pravidelně využívány aktivity
v CRM kanálu, na jednotlivých kartách leadů a příležitostí.

Není možné sestavit kompletní zprávu, pokud obchodníci nebudou používat
*Aktivita* se objevuje v *hádání*.

Pro více informací se podívejte na:doc:`Aktivita <../../../essentials/activities>

Vytvořte nezpracovaný report o leadrech
=================================

Chcete-li vytvořit nehlídaný report o leadrech, nejprve přejděte na: „Aplikace CRM -> Zprávy ->
Klikněte na tlačítko „Pipeline“ a otevřete panel „Analýza trubek“. Klikněte do pole „Hledat…“
Nahoře na stránce a odstranit všechny výchozí filtry.

.. poznámka::
Filtr „Vytvořeno“ může zůstat aktivní, protože tato proměnná může být užitečná k zahrnutí do
zprávě.

Poté přidejte vlastní filtry kliknutím na ikonu „🔻“ (trojúhelník směřující dolů) vedle
tlačítko „Hledat…“ otevřít rozbalovací nabídku, která obsahuje „Filtry“.
„Skupina“, „Oblíbené“ a „Filtry“. Pod sloupcem „Filtry“
klikněte na „Přidat vlastní filtr“, což otevře okno „Přidat vlastní filtr“.

Okno „Přidat vlastní filtr“ (pop-up) umožňuje vytvářet více specifické filtry.

Přidejte vlastní filtry
------------------

Pro vytvoření nezpracovaných zpráv o potenciálních zákaznících je třeba nastavit filtry pro následující
podmínky:

 - :ref:`Nedodržované aktivity <unattended_leads_report/past-due>“: omezuje výsledky na pouze ty, které
v čele s úkoly, které jsou již po splatnosti. Toto lze upravit tak, aby zahrnovalo
aktivity, které mají proběhnout v den, kdy je zpráva generována.
 - :ref:`Nedostatečně přiřazené kontakty <unattended_leads_report/exclude-unassigned>“: vynechává kontakty bez
určený prodejce.
 - „Specifické prodejní týmy“: omezuje výsledky na pouze ty, které obsahují
Vedoucí prodejců, kteří jsou přiřazeni ke konkrétnímu týmu prodeje. Tento filtr je nepovinný a neměl by být zahrnut, pokud
zpráva je určena pro celou společnost.

... unattended leads report/past due:

Přidej filtr pro nedokončené aktivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Klikněte na první pole pro nové pravidlo a zadejte do pole „Hledat…“ slovo „Aktivita“, nebo
Přejděte dolů a vyhledejte jej v seznamu. Pak vedle položky :guilabel:`Aktivita“ klikněte
:guilabel:`> (větší než signa)“ otevře nové podmenu se sekundárními podmínkami.

Do pole „Hledat…“ zadejte „Datum splatnosti“, nebo prohledejte seznam pomocí šipek nahoru a dolů. Klikněte
:guilabel:`Datum splatnosti“ k přidání do pravidla.

.... obrázek: nezajištěné_případy_report/aktivity-vzhledem-k-datu.png
:synchronizace: střed
:alt:Vlastní filtr s důrazem na možnosti pro aktivity a termíny splatnosti.

Poté klikněte do dalšího pole a vyberte možnost: guilabel:<= z nabídky.
operátor zahrnuje všechny aktivity s termínem do a včetně vybraného data.
pole.

Třetí pole může zůstat takové, jaké je dnes, nebo se upravit podle potřeby.

..._nepřidělené_zprávy_o_problému/vyloučit_nepřiřazené:

Vyřaďte nezařazené kontakty
~~~~~~~~~~~~~~~~~~~~~~~~

Po filtrování aktivit přidejte nový pravidlo. Pak klikněte do prvního pole pro
nový pravidlo a zadejte do pole „Hledat…“ nebo přejeďte myší na vyhledávání
seznam, kde se může nacházet.

V poli druhé části pravidla vyberte možnost „je nastaven“.
Operátor vylučuje všechny kontakty, které nebyly přiřazeny konkrétnímu obchodníkovi.

... nehlídané vedení reportu prodejního týmu:

Přidejte prodejní tým
~~~~~~~~~~~~~~~~

.. poznámka::
Tento filtr je nepovinný. Chcete-li zobrazit výsledky pro celou společnost, nezadávejte tento filtr.
pokračovat na:ref:`Zobrazit výsledky <unattended_leads_report/view-results>

Chcete-li omezit výsledky zprávy na jednu nebo více prodejních týmů, klikněte na „Nová pravidla“. Poté
klikněte na první pole pro nové pravidlo a zadejte Sales Team do pole „Hledat…“ nebo
Přejděte dolů a vyhledejte v seznamu.

V druhém poli pravidla vyberte možnost „je v“ z nabídky.
Operátor omezuje výsledky na prodejní týmy vybrané v následujícím poli.

V posledním poli vyberte požadovaný prodejní tým z roletky. Může jich být více.
Mohou být přidány do pole, kde je každý parametr ošetřen operátorem „nebo“ („například“ „jakákoliv“).
logiku vyhledávání.

.. obrázek: unattended_leads_report/configured-custom-rules.png
:align:center
:alt: Příklad okna filtru s nastavenými pravidly.

Příklad okna pro přidání vlastního filtru s nastavenými pravidly.

... _nehlídané_zprávy o nehodě/zobrazit výsledky:

Zobrazit výsledky
============

Na horní části formuláře „Přidat vlastní filtr“ je možnost vybrat „jakýkoliv“.
:guilabel:`všechny“ pravidla. Pro správné spuštění zprávy jsou nutná pouze záznamy, které odpovídají **všem**
Filtrů by mělo být zahrnuto následujících. Před přidáním filtrů se ujistěte, že je vybráno všechny
v tomto oboru vybrána.

.. obrázek: nezajištěné_výsledky_reportu/všeobecný_filtr.png
:align:center
:alt: Příklad oznámení nevyřízených aktivit v chatovací místnosti vedoucího.

Po konfiguraci filtrů klikněte na tlačítko „Přidat“. Výsledný report zobrazuje všechny kontakty.
přiřazený prodejci, kde je aktivita po splatnosti nebo má být uhrazena dnes.
Zobrazení je sloupcový graf, kde vodiče jsou seskupeny podle *etapy*.

Pro seskupení výsledků podle obchodníků klikněte na ikonu :guilabel:`🔻 (trojúhelník směřující dolů)“.
pravé straně lišty „Hledat…“ otevřít vyskakovací nabídku, která obsahuje „Filtry“.
:guilabel:„Skupina“, „Oblíbené“ a pod nadpisem „Skupina“
vyberte položku Salesperson.

.. poznámka::
Možnost seskupit podle :guilabel:`Sales Team“ je také dostupná v sekci :guilabel:`Group By“.
hlavičce.

Pro přepnutí na zobrazení seznamu klikněte na ikonu „≣ (seznam)“ v pravém horním rohu.
obrazovka.

..tip:
Kliknutím na ikonu :guilabel:`(přepínač)` se otevře nabídka dalších sloupců, které lze přidat.
přidány do zprávy.

Některé z možností, které jsou pro tento výkaz užitečné, zahrnují:

   - :guilabel:`Aktivita“: souhrn posledních aktivit pro tento kontakt.
   - :guilabel:`Očekávaný termín uzavření“: očekávané datum, kdy bude vedení získáno.
   - :guilabel:`Pravděpodobnost“: odhadovaná úspěšnost na základě fáze.

.... obrázek: unattended_leads_report/additional-options.png
:synchronizace: střed
:alt:Vlastní filtr s důrazem na možnosti pro aktivity a termíny splatnosti.

.. viz též:
:doc:`Aktivita <../../../essentials/activities>`
