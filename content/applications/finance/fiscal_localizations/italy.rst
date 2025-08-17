=====
Itálie
=====

.._italie/moduly:

Konfigurace
=============

Instalujte následující moduly, abyste získali všechny funkce italského
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1
:prázdné sloupky: 1

   * Jméno
     - Technické označení
     - Popis
   * – Itálie – Účetnictví
     - „l10n_it“
     - Výchozí:balík lokalizace daní:
   * Italie – elektronické faktury
     - l10n_it_edi
     - Implementace e-faktur
   * – Itálie – Daňové doklady v elektronické podobě
     - l10n_it_edi_srazek
     - Srážka z e-faktury
   * – Itálie – Účetní zprávy
     - l10n_it_reports
     - Zeměpisně specifické zprávy
   * – Itálie – Sklad DDT
     - l10n_it_stock_ddt
     - Dopravní listy - DDT

.. viz též:
:dokumentace o zákonnosti a souladu s předpisy v Itálii


Informace o společnosti
-------------------

Nastavení informací o společnosti zajistí, že vaše databáze účetnictví bude správně nastavena.
informace, přejděte na: „Nastavení“ – „Obecné nastavení“, a v části „Společnosti“.
sekci klikněte na „Aktualizovat informace“. Zde vyplňte pole:

- :guilabel:`Adresa“: adresa společnosti
- :guilabel:`DPH“: DPH společnosti;
- :guilabel:`Daňové identifikační číslo“: daňové identifikační číslo společnosti.
- :guilabel:`Daňový systém“: daňový systém, pod kterým společnost spadá;

.. obrázek:italy/firma.png
:alt:Poskytnutí informací o společnosti

Konfigurace daní
-------------------

Mnohé funkce elektronického fakturování jsou zavedeny prostřednictvím daňového systému Odoo. Proto musí být
správně nakonfigurované tak, aby vystavovaly faktury správně a uměly řešit další případy účtování.

Italská lokalizace obsahuje předdefinované příklady daní pro různé účely.

..._daňové osvobození:

Daňové osvobození
~~~~~~~~~~~~~

Použití prodejních daní ve výši **nuly procenta** (0 %) je podle italských úřadů
Vyhledat přesnou :guilabel:`Druh osvobození od daně z přírody“ a :guilabel:`Zákonný odkaz“.
Odůvodnit výjimku provedenou na řádku faktury.

.. příklad::
Exportní clo v EU lze použít jako referenci („0 % EU“, štítek faktury „00eu“).
naleznete pod položkou „Účetnictví -> Konfigurace -> Daně“. Exporty jsou od DPH osvobozeny.
a proto je nutné vyplnit pole „Odškodnění“ a „Právní odkaz“.

.. obrázek:italy/osvobození od daně.png
:alt:Nastavení osvobození od daně

.. viz též:
Ve skutečnosti existuje mnoho kódů „Dotace na ochranu přírody“ a „Zákonný odkaz“.
aby jste si ověřili nejnovější verzi dostupnou, abyste měli aktuální informace o:

   - „Dokumentace italských úřadů <https://www.agenziaentrate.gov.it/portale/web/guest/aree-tematiche/fatturazione-elettronica>“
   - Oficiální průvodce s názvem „Zpracování daňového osvobození <https://www.agenziaentrate.gov.it/portale/documents/20143/451259/Guida_compilazione-FE-Esterometro-V_1.9_2024-03-05.pdf/67fe4c2d-1174-e8de-f1ee-cea77b7f5203>“

.. poznámka::
Pokud chcete použít jiný typ osvobození, přejděte na: „Účetnictví“ →
Konfigurace --> DPH“, vyberte podobný druh daně, pak klikněte na ikonu ozubeného kolečka a vyberte
:guilabel:"Duplikát". V záložce "Pokročilé možnosti" přidejte :guilabel:"Odpuštění".
a klikněte na :guilabel:`Uložit“.

.. tip::
**Přejmenujte** své daně v poli „Název“ podle jejich „Odpuštění“.
je snadno odlišitelné.

.._italie/dph-v-zaplacenou-slozenku:

Režim osoby povinné k dani
==============

Reverzní fakturace je daňový mechanismus, který přenáší odpovědnost za zaplacení DPH na
dodavatel zákazníkovi. Zákazníci platí DPH sami přímo:abbr:AdE (Agentura pro evropské fondy).
Entrata). Jsou různé typy:

- |:guilabel:`Vnitřní odpočet DPH“ (pro prodej v rámci ČR)
|Způsob zdanění přechází na kupujícího u určitých druhů výrobků a služeb.
- |:guilabel:`Vnější zpětná daň“ (pro prodeje v rámci EU)
|DPH je splatná v zemi dodání nebo ve státě, kde se služba vykonává.
Pokud je kupující italská firma, pak Evropská unie nabízí mechanismus, který umožňuje prodejci
aby přenesl svou odpovědnost na kupujícího.

Faktury
--------

Faktury zákazníků s režimem odpočtu DPH neobsahují částku DPH, ale :abbr:`AdE (Agenzia delle Entrate)
Entrata) vyžaduje od prodávajícího uvedení důvodu osvobození od daně a zákona, na jehož základě je daňová povinnost omezena.
Referenční číslo, které umožňuje zpětný odběr. Odoo poskytuje sadu speciálních nulových daní
Může být přiřazena ke každé položce daňového dokladu s odběratelem, která je nejčastěji používaná.
konfigurace.

Faktury dodavatelů
------------

Italské společnosti, které jsou v režimu obrácené daňové povinnosti, musí zaslat informace z faktury přijaté na
Abk.: AEI (Agentura pro příjmy).

.. poznámka::
Samostatně vygenerované soubory XML pro přiznání k DPH musí být vystaveny a odeslány na :abbr:`AdE (Agenzia Delle Entrate)`
pro zpětnou účtovanou fakturu.

Při vystavování dodacího listu jsou k dispozici daně z přenesení daňové povinnosti pro
V poli „Dani“ zadejte hodnotu, kterou chcete použít. Můžete si také prohlédnout dostupné daně kliknutím na
V sekci „Účetnictví“ -> „Nastavení“ -> „Daně“ zjistíte, že pro 10 % DPH a 22 %
Začaly se vybírat také služební daně. Důvodem je automatické nastavení italského fiskálního systému
položky, které jsou automaticky aktivovány v daňovém seznamu.

..._italie/sítě:

Daňové sazby
---------

Italská lokalizace má vlastní sekci pro :ref:`sazebník daně <daňové přiznání/sazebníky>`.
daň z přenesení břemene. Tyto sazebníky jsou označitelné značkou :ref:`VJ <italy/grids>`, a
je možné najít v menu: „Účetnictví“ - „Zprávy“ - „Auditní zprávy: daňové přiznání“.

.. obrázek:italy/gridy.png
:alt:Obratová daňová síť z přílohy č. 10 Daňového přiznání

..._italské e-fakturace:

Elektronické fakturace
===========

Sdí je systém elektronického fakturování.
„Elektronické fakturace“ systém používaný v Itálii, který umožňuje odesílání
a přijímání elektronických faktur od a do zákazníků. Dokumenty musí být v XML
formátu EDI (Elektronický datový výměnný formát) nazvaném FatturaPA a formálně schváleným
systém před dodáním.

Pro přijímání faktur a oznámení je potřeba služba SdI (Sistema di Interscambio)
musí být informováni, že uživatelské soubory musí být odeslány do Odoo a zpracovány za něj.
takže musíte nastavit kód cílové destinace v AdE (Agentura pro elektronickou komunikaci):
Portál „Entrate“).

#Přejděte na portál „Italské úřady“ (https://ivaservizi.agenziaentrate.gov.it/portale)
ověřit
#Přejděte do sekce „Faktury a potvrzení“.
#Zadejte uživatele jako daňovou osobu pro DPH, kterého chcete nastavit elektronickou adresu.
#V nabídce „Služby k dispozici“ -> „Daňová evidence“ -> „Registrace“.
adresu pro elektronické faktury, vložte adresu Odoo.
:guilabel:`Destinační kód“ „K95IV18“, a potvrďte.

EDI režim a autorizace
--------------------------

Protože soubory procházejí servery Odoo před odesláním na SdI (Sistem
di Interscambio) nebo obdržené vaší databází, musíte povolit Odoo k zpracování vašich souborů.
z vaší databáze. Chcete-li tak učinit, přejděte na:
Elektronické fakturace.

K dispozici jsou tři režimy:

- |:label:"Demonstrace"
|Tento režim simuluje prostředí, ve kterém jsou faktury zasílány vládě. V tomto režimu
faktury je nutné stáhnout ručně jako soubory XML a nahrát do systému AdE
Webové stránky agentury Agenzia delle Entrate.
- | :guilabel:`Test (experimentální)`
|Tento režim odesílá faktury na neprodukční službu, tedy například na testovací.
:abbr:`AdE (Agenzia delle Entrate)“. Uložením této změny se všechny společnosti v databázi přesměrují na
použít tuto konfiguraci.
- |:guilabel:`Oficiální“
|Toto je produkční režim, který odesílá vaše faktury přímo do:abbr:`AdE (Agentura pro elektronickou
Entrate`.

Jakmile si vyberete režim, musíte přijmout podmínky služby zaškrtnutím políčka „Povolit
Odoo zpracovat faktury“ a pak „Uložit“. Nyní můžete zaznamenávat své transakce v Odoo.
Účetnictví.

.. varování:
Vybrat buď „Test (experimentální)“ nebo „Oficiální“ je **nevratné**.
Například v režimu „Oficiální“ nelze vybrat „Test“.
(výzkumné) nebo :guilabel:Demo. Doporučujeme vytvořit **samostatnou databázi** pro testování
pouze pro účely uvedené v těchto podmínkách.

.. poznámka::
V režimu testování se musí všechny faktury odeslané *muset* týkat partnera.
z následujícího falešného :guilabel:`Destinace kódu“ dávaného :abbr:`AdE (Agentura pro
„0803HR0“ – „N8MIMM9“ – „X9XX79Z“. Všechny skutečné výrobky: guilabel: „Codice Destinario“
Vaše zákazníky nebude služba testování považovat za platné.

.. obrázek::italie/edi.png
:alt:Nastavení elektronické fakturace

.._italy/elektronické fakturace:

Proces
-------

Podání faktur do SdI (Systému pro mezinárodní výměnu) pro Itálii je elektronické.
Proces používaný pro přenos daňových dokladů v XML formátu mezi společnostmi a
:zkráceně „AdE (Agentura pro daně)“ s cílem snížit chyby a ověřit správnost operací.

.. poznámka::
Stav faktury lze zkontrolovat pomocí pole :guilabel:`SdI State`. XML soubor
Je přiložen k faktuře.

.. obrázek:italy/edi-process.png
:alt:Architektura systému EDI

Vytváření dokumentů XML
~~~~~~~~~~~~~~~~~~~~~~

Odoo vytváří potřebné XML soubory jako přílohy faktur ve formátu FatturaPA, který je požadován.
agenturou pro správu daní Agenzia delle Entrate). Jakmile jsou vybrany faktury potřebné k úhradě, přejděte na
Vyberte možnost „Akce“ a klikněte na „Odeslat a tisknout“.

.. obrázek:italie/edi-menu.png
:alt:Náhled a tisk

Když se otevře okno s výběrem akcí, je možné vybrat „Vytvořit
Soubor XML generuje přílohy.

.. obrázek:italy/edi-send-and-print.png
:alt: Dialog pro odeslání a tisk

XML soubor i jednou PDF verzi lze nalézt jako přílohu faktury.

.. obrázek::italy/edi-attachments.png
:alt:Přílohy EDI

Předložení na SDI
~~~~~~~~~~~~~~~~~

Možnost „Odeslat do finančního úřadu“ v dialogovém okně „Odeslat a tisknout“ odešle
připojení k proxy serveru, který shromažďuje všechny požadavky a pak je přesměruje
Webové služby kanálu pro SDI (Systém výměny informací). Zkontrolujte stav odeslání
Vygenerovat fakturu pomocí tlačítka „Zkontrolovat odeslání“ v horní části stránky s fakturou.

Zpracování od SDI
~~~~~~~~~~~~~~~~~

:abbr: SdI (Systém výměny informací) přijímá dokument a kontroluje jej na případné chyby.
stupni, faktura je ve stavu zpracování v procesu „Sdílená infrastruktura“, jak je vidět na faktuře. Faktura
mu také přiřazuje číslo transakce „FatturaPA“, které se zobrazuje v
Karta „Elektronická fakturace“. Kontroly mohou trvat proměnlivou dobu od několika sekund
podle fronty faktur zaslaných po celé Itálii.

.. obrázek:italy/edi-processing.png
:alt:Zkontrolujte tlačítko Odeslat a stav zpracování

Přijetí
~~~~~~~~~~

Pokud je dokument platný, zaznamená se a bude považován za daňově platný agenturou
delle Entrate), která bude pokračovat v archivování na :guilabel:„Záložní úložiště (Conservazione
Substituční péče) na žádost prostřednictvím portálu Agentury.

.. varování:
Odoo nenabízí „Substituční konzervaci“.
<https://www.agid.gov.it/index.php/it/piattaforme/conservazione> požadavky. Jiní poskytovatelé
a:abbr:`AdE (Agenzia delle Entrate)` poskytují bezplatné a certifikované úložiště, které splňuje
specifikace požadované zákonem.

Kód Destinace SdI (Sistema di Interscambio) se pokouší přeposlat
fakturu zákazníkovi na uvedenou adresu, ať již se jedná o e-mailovou adresu typu „PEC“ nebo
:zkratka: SdI (Sistema di Interscambio)
kanály. Maximálně se pokusíme 6x za 12 hodin, takže i když neúspěšné, tento proces může
a trvat až tři dny. Stav faktury je:guilabel:`Přijato SDI, Předáno partnerovi“.

Možná odmítnutí
~~~~~~~~~~~~~~~~~~

Ve srovnávacím systému SdI mohou být nesrovnalosti v kompilaci, možná i
formální. V tomto případě je faktura ve stavu „Odmítnutá SDI“.
Observace Sistema di Interscambio jsou vloženy na horní část faktury.
vadě stačí odstranit přílohy faktury a vrácenou fakturu vrátit.
:guilabel:„Návrh“, a opravte chyby. Jakmile bude faktura připravena, může být znovu odeslána.

.. poznámka::
Pro obnovení XML musí být odstraněna jak příloha XML, tak i PDF zpráva.
Poté jsou oba pakety znovu vygenerovány, což zajišťuje, že vždy obsahují stejná data.

.. obrázek:italie/edi-odmítnut.png
:alt: Stát odmítnutý EDI

Doručeno
~~~~~~~~~~~~~~~~~~~~

Faktura byla doručena zákazníkovi, ale můžete mu zaslat i kopii.
v PDF formátu e-mailem nebo poštou. Jeho stav je: `Guilabel:Accepted by SDI, Delivered to Partner`.

Pokud SdI nemůže kontaktovat vašeho zákazníka, mohou být
registrované na portálu AdE (Agenzia delle Entrate). V tomto případě stačí jen zajistit zaslání
fakturu v PDF e-mailem nebo poštou. Faktura je pak ve stavu:
Stav partnera Delivery Failed.

Daňová integrace
---------------

Když obdržíte fakturu od dodavatele, buď z papíru nebo
Finanční správa může požadovat odeslání některých informací o dani z importovaného souboru XML.
integraci zpět do systému SdI (Sistema di Interscambio). K tomu dochází v případě transakce,
Pokud se stane, že je z nějakého důvodu osvobozen od daně, stává se daňovým poplatníkem.

.. příklad::
Zde je neúplný seznam:

   - | :ref:`italie/dodatečné zdanění
|Jako kupující musíte platit daně z toho, co nakoupíte, a zapojit daňové informace.
:guilabel:`Zpětná daň“
   - |:ref:`italy/split-payment`
|Jako „obchodník s veřejnou správou“ musíte platit daně a integrovat
daňové informace. Ujistěte se, že nahradíte „0 % DPH“ na faktuře dodavatele
jste dostali správně s daní z rozděleného účtu.
   - |:guilabel:`Vlastní spotřeba“
|Když jako podnikatel používáte majetek, který jste si koupili pro obchodní účely, pro osobní potřebu
Vaše daň z příjmu se však zvýší o částku, kterou jste původně jako náklady na podnikání odpočítali.

Odoo může zjistit, že faktura od dodavatele lze vyložit jako dokument typu, který podléhá dani.
integrace, viz část :ref:`italy/dokumenty`.

.. důležité::
Ujistěte se, že nahradíte na faktuře od dodavatele zadanou hodnotu „0 % DPH“ za hodnotu „0 % DPH“.
Jedná se o poplatky, které máte zaplatit na účet :abbr:`AdE (Agenzia delle Entrate)“. Po kliknutí na tlačítko
na vrchní část faktury pro jednoho dodavatele a pošlete je.

Pokud kliknete na tlačítko „Odeslat daňovou integraci“, otevře se soubor XML s příslušnými
:guilabel:`Dokumentový typ“ je vytvořen, připojen k faktuře a odeslán jako u faktur.

.... obrázek:italy/edi-tax-integration-button.png
:alt:Tlačítko pro integraci s EDI SEND

.._italie/dokumenty:

Druhy dokumentů
--------------

:abbr:`SdI (Sistema di Interscambio)` vyžaduje od podniků zasílání faktur a dalších
dokumenty prostřednictvím EDI (Elektronický výměnný formát).

Následující kódy „Dokumentního typu“ všechny technicky identifikují různé obchodní případy použití.

TD01 – Faktury
~~~~~~~~~~~~~~~

Toto představuje běžný scénář pro všechny faktury vyměňované prostřednictvím SdI.
(Systém výměny zboží). Každá faktura, která nespadá do některé ze specifických zvláštních případů
je zařazen jako standardní faktura, identifikovaná polem „Typ dokladu“ s hodnotou TD01.

TD02 - Zálohy
~~~~~~~~~~~~~~~~~~~~

Faktury o zálohách se importují/exportují s jiným kódem typu dokumentu
„TDO2“ je jiný než běžné faktury. Při dovozu faktury se vytvoří běžná dodavatelská faktura.

Odoo exportuje transakce jako „TD02“, pokud jsou splněny následující podmínky:

#Je to faktura.
#Všechny řádky faktury jsou spojeny s prodejními objednávkami na zálohu.

TD04 - Kreditní poznámky
~~~~~~~~~~~~~~~~~~~

Jedná se o standardní scénář pro všechny vydané **úvěrové poznámky** klientům z České republiky, když potřebujeme
formálně uznat, že prodávající snižuje nebo ruší dříve vystavenou fakturu.
Příkladem může být případ nadměrného účtování, chybných položek nebo přeplatku. Stejně jako faktury musí být
zaslány do SdI (Systému pro výměnu dat), jejich dokumentový typ je TD04

TD07, TD08, TD09 - Jednoduché fakturace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Zjednodušené faktury („TD07“), kreditní dopisy („TD08“) a debetní dopisy („TD09“) lze použít pro ověření
domácí transakce do výše 400 eur (DPH zahrnuto). Jeho postavení je stejné jako u běžných
faktura s menším množstvím informací.

Pro zjednodušenou fakturu je nutné splnit následující podmínky:

#:guilabel:`Faktura zákazníka“ odkaz: jedinečné číslování s „bez mezerami“.
#:guilabel:`Datum faktury“: datum vystavení faktury;
#:guilabel:`Informace o společnosti“: úplné informace o prodejci (číslo DPH/DIČ, jméno a plnou adresu).
pod: „Obecné nastavení > Firmy (oddíl)“
#:guilabel:`DPH“: daňové identifikační číslo kupujícího (na partnerovi);
#:guilabel:`Celkem“: Celková částka faktury včetně DPH.

Odoo exportuje faktury do EDI (Elektronického datového výměnu) v zjednodušené podobě, pokud:

#Je to domácí transakce (tj. partner je z Itálie).
#Povinné položky vaší společnosti (:guilabel:„DIČ“ nebo :guilabel:„Daňové identifikační číslo“,
:guilabel:`Daňový režim“ a plnou „Adresu“).
#Partnerovu adresu není možné plně specifikovat (tj. chybí město nebo PSČ).
#Součet DPH je nižší než 400 eur.

.. poznámka::
400 eurový limit byl stanoven v „vyhlášce ze dne 10. května 2019 v Gazzetě“.
Officialní <https://www.gazzettaufficiale.it/eli/id/2019/05/24/19A03271/sg> zpráva. Doporučujeme vám
zkontrolovat aktuální oficiální hodnotu.

TD16 – Vnitřní obrácená daňová povinnost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vnitřní obratové transakce (viz :ref:`italy/tax-exemption`)
Pokud jsou splněny následující podmínky, je vývoz do země s režimem reverse charge (viz italy/reverse-charge) označen jako TD16.

- Je to faktura dodavatele.
- Má alespoň jednu daň na fakturačních řádcích, která cílí na některou z těchto sazeb DPH.


TD17 - Nákup služeb v zahraničí
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Když kupujete služby od **nečlenských zemí EU** nebo **mimo EU**, fakturu vám zašle
služba s cenou bez DPH, protože v Itálii není zdanitelná. Daň z přidané hodnoty platí kupující.
v Itálii.

- V rámci EU: kupující vstupuje do faktury obdržené s informací o DPH.
Itálie (tj. **integrace faktury dodavatele a daně z přidané hodnoty**);
- Mimo EU: kupující vystavuje sám sobě fakturu (tj. **vlastní daňové doklady**).

Odoo exportuje transakci jako „TD17“, pokud jsou splněny následující podmínky:

- Je to faktura dodavatele.
- Má alespoň jeden daňový řád na fakturačních liniích, který cílí na daňovou síť:

- Všechny řádky faktury buď obsahují služby jako produkty nebo daň s
:guilabel:`Služby“ jako „oblast daně“.

TD18 - Nákup zboží v EU
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Faktury vystavené v rámci EU mají **jednotný formát**, proto je možné pouze integrace
Je nutný fakturační doklad.

Odoo exportuje transakci jako „TD18“, pokud jsou splněny následující podmínky:

- Je to faktura dodavatele.
- Partner je z členské země EU.
- Má alespoň jednu daňovou položku na faktuře, která cílí na daňový řád:
- Všechny řádky faktury buď obsahují položku „Spotřební materiál“ jako produkt nebo daň s
:guilabel:`Zboží“ jako „Daňový objekt“.

TD 19 - Nákup zboží ze zálohy DPH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nákup zboží od zahraničního dodavatele, ale zboží je již v Itálii ve státní dani.
vkladní knížka**.

- Z EU: kupující vystaví fakturu s DPH, která je součástí
Itálie (tj. **integrace faktury dodavatele a daně z přidané hodnoty**);
- Mimo EU: kupující vystaví fakturu sám sobě (tj. „fakturace na sebe“).

Odoo exportuje transakci jako „TD19“, pokud jsou splněny následující podmínky:

- Je to faktura dodavatele.
- Má alespoň jeden daňový řádek na faktuře, který cílí na daňovou síť:
- Všechny řádky faktury buď obsahují produkt „Zboží spotřebního charakteru“ nebo daň s
:guilabel:`Zboží“ jako „Daňový objekt“.

TD24 - Odložené faktury
~~~~~~~~~~~~~~~~~~~~~~~~

Splatnost faktury se odkládá na pozdější dobu než je prodej zboží nebo
poskytování služeb. Daňový doklad musí být vystaven nejpozději do 15.
den v měsíci následujícím po dodání zboží uvedeném na dokumentu.

Jedná se o souhrnnou fakturu, která obsahuje seznam více prodejů zboží nebo služeb.
v měsíci. Podnik je oprávněn služby **skupit do jedné faktury**, obvykle
Vystavené na konci měsíce pro účely účetnictví. Zálohové faktury jsou výchozím bodem
Velkoobchodníci s opakovanými zákazníky.

Pokud jsou zboží přepravovány dopravcem, každá dodávka má spojený s ní **Dokumento di trasporto**.
Dopravní doklad (DDT) nebo Dopravní listina. Zálohová faktura musí obsahovat podrobnosti o
Všechny tyto informace pro lepší sledování.

.. poznámka::
Elektronické fakturace odložených faktur vyžaduje modul l10n_it_stock_ddt.
V tomto případě se v elektronické faktuře používá speciální dokumentový typ „TD24“.

Odoo exportuje transakce jako „TD24“, pokud jsou splněny následující podmínky:

#Je to faktura.
#Je spojen s dodávkami, jejichž DDT má jiný datum než datum vydání.
fakturu.

TD28 – San Marino
~~~~~~~~~~~~~~~~~

Faktury
********

San Marino a Itálie mají zvláštní dohody o elektronických fakturách. Proto se v takovém případě používají
bude aplikovat pravidla obvyklého způsobu účtování, můžete použít příslušný :guilabel:`Dokumentový typ`, který závisí na
faktura typu: „TD01“, „TD04“, „TD05“, „TD24“, „TD25“. Příplatky nejsou vyžadovány
Odoo. Uživatel je však požádán státem o:

- Vyberte daň s nastavením „Druh osvobození“ na „N3.3“.
- Použijte obecný zkratkový kód SdI (Sistema di Interscambio) 2R4GTO8.

Faktura je pak přeposlána do kanceláře v San Marinu, která fakturu předá správnému podniku.

Faktury dodavatelů
************

Když je vystaven papírový daňový doklad ze San Marina, musí jej předložit každá italská společnost.
do Agenzia delle Entrate (ADE) uvedením typu dokumentu v e-faktuře
pole s speciálním hodnotou „TD28“.

Odoo exportuje transakci jako „TD28“, pokud jsou splněny následující podmínky:

#Je to faktura dodavatele.
#Má alespoň jednu daňovou položku na faktuře, která cílí na daňové sítě: odkaz `VJ <italy/grids>`.
#Zemí partnera je **San Marino**.

Obchodní vztahy mezi veřejnou správou a podnikatelským sektorem (B2G)
======================================

Podniky veřejné správy jsou podrobovány větší kontrole než soukromé firmy.
Jak nakládají s penězi daňových poplatníků.
Tento proces přidává několik kroků do standardního postupu:
Administrativní subjekty mohou faktury buď přijmout, nebo odmítnout.

.. poznámka::
:abbr:`PA (Veřejná správa)` podniky mají šestimístný :guilabel:`Kód cílové destinace“.
nebo také zkratka CUU (Codice Univoco Ufficio), což je povinné, PEC adresa nemůže
V tomto případě se může použít.

.. viz též:
„Seznam všech podniků, které patří do veřejné správy včetně jejich názvů“
Kód cílové země <https://www.agenziaentrate.gov.it/portale/web/guest/aree-tematiche/fatturazione-elettronica>

CIG, CUP, DatiOrdineAcquisto
----------------------------

Zajistit efektivní sledovatelnost plateb veřejné správy pomocí elektronických faktur
vydané veřejným správním orgánům musí obsahovat:

- Kromě případů vyloučení z obchodu s ovocem a zeleninou
zákonem č. 136/2010 Sb., o oběhu bankovek a mincí a o změně zákona o České národní bance, ve znění pozdějších předpisů
- V případě faktur souvisejících s veřejnými pracemi se jedná o kód CUP (Codice Unico di Progetto).

Pokud je to nutné v XML souboru, může AdE pouze provádět platby
elektronické faktury, pokud soubor XML obsahuje CIG (Codice Identificativo Gara).
:zkratka: CUP (Código Único de Proyecto).

.. poznámka::
CUP (Codice Unico di Progetto) a CIG (Codice Identificativo Gara) musí
být zahrnuty v jednom ze souborů „DatiOrdineAcquisto“, „DatiContratto“ nebo „DatiConvenzione“.
tagy „Datum přijetí“ nebo „Doklady spojené s fakturou“.

Tyto odpovídají elementům s názvem :guilabel:`CodiceCUP` a :guilabel:`CodiceCIG“ z
elektronický fakturační soubor XML, jehož tabulku lze nalézt na webových stránkách vlády
<http://www.fatturapa.gov.it/>`.

..._italy/split-payment:

Splátkový prodej
-------------

Mechanismus „Splatná částka“ funguje podobně jako mechanismus „Italské zpětné fakturace“.

.. příklad::
Když italská firma fakturuje PA (veřejné správě) – tedy například
úklidové služby pro veřejnou budovu - obchodní činnost :abbr:`PA (Veřejná správa)`
Sám si daň z přidané hodnoty ohlásí správci daně a dodavatel jen vybere.
správnou dani s příslušným štítkem „Daňová výjimka“ pro své fakturační řádky.

Konkrétní fiskální pozice „Scissione dei Pagamenti“ je k dispozici pro partnery
příslušející do :abbr:`Veřejné správy“.

Proces
-------

..._italie/digitální podpis:

Digitální kvalifikovaný podpis
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro faktury a účty určené pro PA (Veřejnou správu) je nutné použít **Digitální kvalifikovaný
Každý soubor zaslaný prostřednictvím SDI vyžaduje podpis.
XMLový soubor musí být ověřen pomocí certifikátu, který buď:

- inteligentní karta
- **token USB**;
- :zkratka HSM (hardwarový bezpečnostní modul).

.. varování:
Odoo **nemůže** elektronicky podepisovat dokumenty za vás. Když je kód Codice
Pokud je detekován příjemce, pak se zastaví proces EDI (Electronic Data Interchange) a
faktura je nastavena na stav „Potřebuje podpis uživatele“. Můžete si ji stáhnout
dokument v XML, podepíšete ho pomocí libovolného poskytovatele digitálního kvalifikovaného podpisu.
program a odeslat jej přes portál „AdE (Agenzia Delle Entrate)“.

Přijetí nebo odmítnutí
~~~~~~~~~~~~~~~~~~~~~

.. varování:
Odoo neumí odeslat podepsané faktury do :abbr:`PA (veřejné správy)“ podniků.
Tyto státy nelze přímo spustit pomocí Odoa. Když nahrajete fakturu na :abbr:`AdE
(Agenzia delle Entrate) portálu. Odoo obdrží oznámení a zkontroluje správnost
:guilabel:`Stát SdI“ na faktuře.

Po obdržení faktury přes SDI (Systém pro výměnu informací) došlo k úhradě prostřednictvím PA (veřejného
Administrativa) má 15 dní na přijetí faktury. Pokud ano, pak je proces u konce.
Pokud podnikatelská sféra odmítne fakturu, je stále platná
Jakmile je přijata SDI (Systém mezinárodního obchodu), musíte vydat kredit.
poznámku k vyrovnání a odeslat ji do systému SdI.

Vypršené termíny
~~~~~~~~~~~~~

Pokud se vám do 15 dnů neozve firma PA (Veřejná správa), kontaktujte
fakturou a příkazem k úhradě.
Vám přišel e-mail s upozorněním na blížící se termín. S nimi můžete domluvit a ručně nastavit
Ve faktuře uveďte správně stát SdI.

Fiskální tiskárny pro POS
=============================

Daňové předpisy vyžadují použití ověřených zařízení typu tiskárna nebo server pro zajištění
Součástí je také bezpečná komunikace s finanční správou a vystavování daňových dokladů.
automaticky přenášet daňová data denně. Tiskárny RT určené pro jednotlivá terminálová místa jsou schopné
transakce, tisk faktur a podávání zpráv úřadům, zajišťující integritu dat a dodržování předpisů.

Simulační režim
---------------

.. varování:
Protože simulační režim posílá data úřadům, měl by být zapnutý pouze v případě, že
začátek procesu konfigurace tiskárny. Jakmile je tiskárna přepnuta do režimu výroby,
režimu nelze vrátit do simulačního režimu.

Pro ověření nastavení tiskárny s Odoo zkontrolujte nastavení tiskárny v režimu simulace.
v následujícím znění:

#Ujistěte se, že je fiskální tiskárna nastavena na výchozí stav: tiskárna zapnutá, cyklus spouštění dokončený.
a žádný probíhající obchod.
#Zadejte „3333“.
#Tlačítko „Chiave“. Na obrazovce se zobrazuje „Scelta Funzione“.
#Zadejte číslo 14. Na obrazovce se zobrazí „Apprendimento“.
#Zadejte číslo 62. Na obrazovce se zobrazí „Simulazione“.
#. Chcete-li z „ne“ udělat „si“, stiskněte klávesu „X“.
#Stiskněte tlačítko „Contante“.
#Press: guilabel:"Klíč".

Pro konfiguraci tiskárny pro výrobu opakujte kroky uvedené výše.

.. poznámka::
Pro ověření konfigurace tiskárny je nutné nejprve získat fyzické zařízení a registrovat ho.
příslušné orgány.

Nastavení tiskárny pro práci s Odoo
----------------------------------------

Fiskální tiskárny mají fungovat pouze v místní síti, což znamená, že tiskárna a
zařízení musí být připojeno k aplikaci „Odoo Point of Sale“
stejné síti.

Fiskální tiskárny jsou obvykle konfigurovány tak, aby používaly HTTP jako výchozí protokol.
Nastavení musí být aktualizována, aby bylo možné podporu protokolu HTTPS na tiskárně povolit. To lze provést buď
software pro konfiguraci tiskárny EpsonFPWizard nebo klávesnice připojené k tiskárně.

Pro nastavení fiskálního tiskárny pomocí klávesnice postupujte takto:

#Ujistěte se, že je fiskální tiskárna nastavena na výchozí stav: tiskárna zapnutá, cyklus spouštění dokončený.
a žádný probíhající obchod.
#Zadejte „3333“.
#Tlačítko „Chiave“. Na obrazovce se zobrazuje „Scelta Funzione“.
#Zadejte „34“. Na obrazovce se zobrazí:„Webový server“.
#Tlačítko stiskněte třikrát, dokud se na obrazovce neobjeví „Webový server: SSL“.
#. Chcete-li převést hodnotu „0“ na „1“, stiskněte tlačítko :guilabel:`X`.
#Pro potvrzení stiskněte tlačítko „Contante“ třikrát.
#Press: guilabel:"Klíč".

Pak se přihlaste do tiskárny pomocí zařízení, které běží na :doc:`Odoo Point of Sale.
, tak aby rozpoznal certifikát tiskárny.

Chcete-li schválit a nainstalovat certifikát tiskárny, postupujte takto:

#Připojte se k tiskárně otevřením prohlížeče a zadáním adresy „https://<ip-tiskárny>“ do
adresní řádku. Zobrazí se varovná zpráva o bezpečnostním riziku „Potenciální bezpečnostní riziko“.
#Klikněte na „Pokročilé“ a zobrazí se možnosti schválení certifikátu.
#Klikněte na tlačítko „Pokračovat“ a potvrďte certifikát.

Pak je třeba zajistit, aby se aplikace „Odoo Point of Sale“
fiskální tiskárna, přejděte na: „Prodejní místo“ – „Konfigurace“ – „Nastavení“.
sekci „Připojené zařízení“ a přidejte IP adresu do sekce „Italský fiskální tiskárna“.
IP adresu a zapnout:guilabel:Používat HTTPS.

Ri.Ba. (Ricevuta Bancaria)
==========================

„Ri.Ba.“ („Ricevuta Bancaria“) je v Itálii běžně používanou platební metodou, kde obchodník požaduje
Prostřednictvím své banky, která požadavek předá přímo bance klienta a získá
odpovědnost za sběr. To umožňuje automatizaci plateb a snižuje rizika pro dodavatele.

Obchodník obvykle nahraje do internetového bankovnictví soubor s pevnou strukturou, který obsahuje seznam plateb.
portál.

.. poznámka::
   - Ri.Ba. jsou výhradně pro domácí platby v Itálii. Pro opakované mezinárodní
platby, použijte příkaz „SEPA Direct Debit (SDD) <../účetnictví/platby/soubor_sdd>“

Konfigurace
-------------

#Zkontrolujte, zda je modul „l10n_it_riba“ nainstalován.
#Přejděte do sekce „Nastavení“ -> „Uživatelé a společnosti“ -> „Společnosti“ a vyberte společnost,
Použije Ri.Ba.
#Vyplňte požadované pole „Kód SIA“.

.... obrázek:italy/sia-code.png
:alt:Kód SIA společnosti

.. poznámka::
Společnost SIA kód identifikuje podniky v italské bankovní síti a používá se
přijímat peníze prostřednictvím konkrétních platebních metod. Skládá se z jedné písmena a čtyř číslic
(např. T1234) a lze je obvykle najít na portálu banky nebo získat kontaktováním banky.

#Zajistit, aby účet společnosti měl italský IBAN.

......viz také::
Jak nastavit: `Bankovní účty <../accounting/bank>

Přijímejte faktury od RI.BA
-------------------------------

Platby typu „Ri.Ba.“ lze zadávat z faktur.
(:menu_selection:"Účetnictví --> Zákazníci --> Faktury").

.. důležité::
Zajistěte, aby faktura obsahovala partnera s italským číslem účtu IBAN.

Poté musí být všechny platby seskupeny v jednom **zálohovaném platebním příkazu**.

.. viz též:
   - :doc:`Množstevní platby <../účetnictví/platby>`
   - Vytvořit platbu ve více krocích (<../accounting/payments/batch>)

Jakmile stisknete tlačítko „Potvrdit“ pro Batch Payment, objeví se :abbr:`Ri.Ba. (Ricevuta
Soubor „Bancaria“) je vytvořen a připojen k platbě ve skupině, takže jej můžete stáhnout a nahrát.
přes internetové bankovnictví vaší banky.

.. obrázek:italy/riba-attachment.png
:alt: Příloha souboru Ri.Ba
