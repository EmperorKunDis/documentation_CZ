=======
Rumunsko
=======

Konfigurace
=============

Instalujte následující moduly, abyste získali všechny funkce rumunštiny.
lokalizace.

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * --:guilabel:Účetnictví v Rumunsku
     - l10n_ro
     - Výchozí:balík fiskální lokace <fiscal_localizations/packages>.
   * – :guilabel:`Export SAF-T z Rumunska“
     - „l10n_ro_saft“
     - Modul pro generování D.406 vyhlášky v formátu SAF-T.

.. obrázek: románie/románia-moduly.png
:alt:Moduly pro rumunskou lokalizaci

.. viz též:
:doc:`Dokumentace o zákonnosti a souladu s předpisy při vystavování faktur v Rumunsku


Deklarace D.406
=================

Od 1. ledna 2023 musí společnosti registrované k dani v Rumunsku hlásit své
účetní údaje měsíčně nebo čtvrtletně v přiznání k dani z příjmů fyzických osob - D.406.

Odoo poskytuje všechny potřebné nástroje pro vývoz dat této deklarace ve formátu SAF-T XML, který
Mohou ověřit a podepsat pomocí softwaru poskytnutého rumunským daňovým úřadem.

.. poznámka::
V současné době podporuje Odoo pouze generování měsíční/čtvrtletní D.406
(obsahující záznamy o příjmech a výdajích, faktury dodavatelů, účty za služby a platby).
(včetně aktiv a požadované deklarace, včetně majetku) nejsou podporovány.

Konfigurace
-------------

Společnost
~~~~~~~

- Pod položkou „Nastavení“ – „Obecné nastavení“ v sekci „Společnosti“ klikněte na
:guilabel:`Aktualizace informací“ a vyplňte název země, města a
:guilabel:`Telefonní číslo“.
- Vyplňte číslo CUI (Codul Unic de Inregistrare) nebo CIF (*Codul de Identificare Fiscală).
*identifikační daňovou číslo (pro zahraniční společnosti) do pole „Číslo společnosti“
bez předpony „RO“ (např. 18547290).
- Pokud je vaše společnost registrována k DPH v Rumunsku, vyplňte pole číslo daňového identifikačního čísla.
včetně předpony „RO“ (např. „RO18547290“). Pokud společnost není
Ve vztahu k DPH v Rumunsku nemusíte do pole „Daňové identifikační číslo“ vyplnit žádné hodnoty.
- Otevřete aplikaci Kontakty a vyhledejte svou společnost. Otevřete profil vaší společnosti a v
v záložce „Účetnictví“ klikněte na tlačítko „Přidat řádek“ a zadejte číslo svého bankovního účtu.
nebyl ještě informován. Ujistěte se, že profil je nastaven jako „Společnost“ nad jménem.

  - Musíte mít alespoň jednoho kontaktního člověka propojeného s vaší společností v aplikaci Kontakty.
Pokud není žádný kontaktní člověk propojen, vytvořte nového kliknutím na tlačítko „Nový“ a nastavte ho
jako „Osoba“ a vyberte svou firmu v poli „Název společnosti“.

Klasifikační schéma
~~~~~~~~~~~~~~~~~

Pro vytvoření souboru přijatelného pro rumunskou daňovou agenturu musí být účetní osnova
z oficiálního rozvahového účtu, například:

- účetní osnovy pro obchodní společnosti (*PlanConturiBalSocCom*)
a) v případě, že je společnost založena s rumunskou lokalizací nebo
- účetní osnovy pro společnosti, které používají „IFRS“ (*PlanConturiIFRS*)

V nastavení účetnictví pod položkou „Nastavení“ -> „Jazyk“ nastavte
:guilabel:'Účetní základ' odráží účetní předpisy a rozvrh účtů používané
Společností.

.. viz též:
:doc:`../účetnictví/začínáme/rozvaha“

Zákazník a dodavatel
~~~~~~~~~~~~~~~~~~~~~

Vyplňte pole „Země“, „Město“ a „PSČ“ každého partnera.
se objevují na fakturách, dodacích listinách nebo platbách přes aplikaci **Kontakty**.

Pro partnery ve formě společností je nutné vyplnit DIČ (včetně zemi předpony).
„Daňové identifikační číslo“ pole. Pokud je váš partner společností sídlící v Rumunsku, můžete místo toho vyplnit
číslo CUI (bez předpony „RO“) v poli „Identifikátor společnosti“.

Daň
~~~

Musíte uvést „římský typ DPH“ (tříciferné číslo) a „římský typ DPH“ (čtyřciferné číslo).
SAF-T daňový kód (6místné číslo) na každou z daní, které používáte. Toto je již nyní vyřešeno pro daně
které jsou v Odoo přednastaveny. Chcete-li tak učinit, přejděte na: „Účetnictví“ -> „Konfigurace“ ->
Daň“, vyberte daň, kterou chcete upravit, klikněte na záložku „Další možnosti“ a zadejte
políčko pro daňový typ a daňový kód.

.. poznámka::
Daňový typ a daňové číslo jsou kódy definované rumunským finančním úřadem pro D.406
deklaraci. Tyto lze nalézt v příloze Excel, která je k dispozici jako pomůcka pro vyplnění
deklaraci, kterou naleznete na webových stránkách rumunské daňové správy <https://www.anaf.ro/anaf/internet/ANAF/despre_anaf/strategii_anaf/proiecte_digitalizare/saf_t/>.

.. viz též:
:doc:`../účetnictví/daně“

Produkt
~~~~~~~

Pro některé druhy zboží je nutné nastavit kód NC (Cod NC):
na výrobku, jak je vyžadováno zákonem v Rumunsku:

- obchodní transakce dovozu/exportu.
- nákupy/dodávky potravinářského zboží snížené DPH.
- vývozy a dovozy v rámci EU, které jsou předmětem podání Intrastatu.
- akvizice/dodávky podléhající místnímu obrácenému DPH (podle kódu NC).
- transakce s výrobky podléhající spotřební dani, u nichž se spotřební daň stanoví na základě KN C.

Pokud není pro neposkytovací výrobek uveden kód INTRASTAT, bude použit výchozí kód „0“.

Pro konfiguraci kódu „Intrastat“ přejděte do
Vyberte „Účetnictví“ -> „Zákazníci“ -> „Produkty“, vyberte produkt a
V záložce „Účetnictví“ nastavte položku „Kód zboží“.

.. viz též:
:doc:`../účetnictví/výkaznictví/INTRASTAT`

Faktura dodavatele
~~~~~~~~~~~

Musíte zaškrtnout políčko „Je faktura odběratele (RO)“ v záložce „Další informace“.
faktura od dodavatele, která je zároveň samofakturací (tj. faktura, kterou vystavíte sám na sebe ve chvíli, kdy
o fakturační dokumentaci obdržené od dodavatele.

Vytváření prohlášení
--------------------------

Export dat
~~~~~~~~~~~~~~~~~~~

Pro vývoz XML pro hlášení D.406 přejděte na: „Účetnictví -> Zprávy ->
Vyberte „Účetní knihu“ a klikněte na „SAF-T“.

.. obrázek: romania/romania-saft-button.png
:align:center
:alt: Klikněte na tlačítko „SAF-T“ a vyexportujte deklaraci v XML formátu D.406.

Poté můžete ověřit a podepsat soubor XML pomocí softwaru pro ověřování dat z rumunského finančního úřadu.
*DUKIntegrátor*.

Podepsání zprávy
~~~~~~~~~~~~~~~~~~

Stáhněte a nainstalujte ověřovací software DUKIntegrator, který je k dispozici na webových stránkách rumunské
Daňová agentura <https://www.anaf.ro/anaf/internet/ANAF/despre_anaf/strategii_anaf/proiecte_digitalizare/saf_t/>`.

Jakmile vytvoříte XML, otevřete „DUKIntegrator“ a vyberte soubor, který právě vytvořili.

Klikněte na položku „Potvrdit a vytvořit PDF“ pro vytvoření **nepodpisovaného** PDF souboru obsahujícího váš výkaz.
:guilabel:`Validace + vytvoření PDF s podpisem“ k vytvoření podepsaného PDF souboru, který obsahuje vaši zprávu.

.. obrázek: románie/románska-dukátová-integračná-minca.png
:align:center
:alt:Program pro ověřování DUKIntegratoru.

Pokud validátor *DUKIntegrator* zjistí chyby nebo nesoulad v datech, vygeneruje soubor
To vysvětluje chyby. V tomto případě je třeba opravit tyto nesrovnalosti ve vašich datech.
před podáním zprávy do rumunské daňové agentury.
