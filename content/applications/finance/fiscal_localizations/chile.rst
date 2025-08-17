=====
Chile
=====

.. tip::
Podívejte se na záznamy dvou webinářů níže pro obecný přehled o lokalizaci a vyhledejte
seznam videí, která vás naučí praktické postupy při používání Odoo v Chile.

   - „Webinář: úvod a ukázka <https://www.youtube.com/watch?v=BHnByZiyYcM>“.
   - „Webinář: Průvodce dodávkou <https://www.youtube.com/watch?v=X7i4PftnEdU>“.
   - Seznam videonávodů
<https://www.youtube.com/playlist?list=PL1-aSABtP6AB6UY7VUFnVgeYOaz33fb4P>.

.. viz též:
   - „Tour chilské aplikace pro lokální lokalizaci“
   - „Chilská lokalizace chytrého průvodce
<https://www.odoo.com/slides/smart-tutorial-localizace-pro-chilské podniky-131>
   - Dokumentace o zákonnosti a souladu s předpisy v oblasti elektronické fakturace v Chile
<../účetnictví/fakturace zákazníků/elektronická fakturace/Chile>

.._chile/konfigurace:

Moduly
=======

:ref:`Instalujte moduly <general/install> a využijte všechny funkce chilské
lokalizace.

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * --:guilabel:Chile - Účetnictví
     - „l10n_cz“
     - Přidává základní účetní funkce, které jsou pro podnikání v Chile nezbytné.
:zkratka SII (Servicio de Impuestos Internos)
   * --:guilabel:`Účetní zprávy Chile“
     - l10n_cl_reports
     - Přidává zprávy *Propuesta F29* a *Balance Tributario (8 sloupců)*.
   * --label:Chile - Elektronické fakturace
     - „l10n_cl_edi“
     - Zahrnuje všechny technické a funkční požadavky na přijímání a generování
faktury a faktury online na základě SII (Servicio de Impuestos Internos)
předpisy.
   * --:guilabel:`Export elektronických výrobků do Chile“
     - l10n_cl_edi_exports
     - Zahrnuje technické a funkční požadavky pro vytváření elektronických faktur k vývozu
zboží podle vnitrostátních daňových a celních předpisů.
   * – :guilabel:"Dodávka faktur v Chile"
     - l10n_cl_edi_stock
     - Zahrnuje všechny technické a funkční požadavky na vytváření dodacích průvodců prostřednictvím webu
služba založená na SII (Servicio de Impuestos Internos) předpisech.

.. poznámka::
   - Odoo automaticky nainstaluje potřebný balíček podle země, ve které se firma nachází
vybrané při vytváření databáze.
   - Modul *Dodání faktury Chile - Elektronické fakturace* je závislý na aplikaci *Sklad*.

.. důležité::
Všechny funkce jsou dostupné pouze tehdy, pokud společnost již dokončila systém fakturace SII.
de Mercado <https://www.sii.cl/factura_electronica/factura_mercado/proceso_certificacion.htm>
certifikační proces.

Informace o společnosti
===================

Přejděte na položku menu „Nastavení -> Firmy: Aktualizace informací“ a zkontrolujte následující společnost
informace jsou aktuální a správně vyplněné:

- :guilabel:`Název společnosti“
- :guilabel:`Adresa“:

  - :label:Ulice
  - :guilabel:`Město“
  - :guilabel:`Stát“
  - :guilabel:`ZIP“
  - :guilabel:`Země“

- Vložte identifikační číslo pro vybraný typ poplatníka.

- :guilabel:`Název aktivity“: vyberte až čtyři kódy aktivit.
- :guilabel:`Popis činnosti společnosti“: zadejte stručný popis činnosti společnosti.

Nastavení účetnictví
===================

Dále přejděte na položku „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ -> „Chilské“.
Přeložte aplikaci a postupujte podle pokynů k nastavení:

- :ref:`Informace o fiskálních otázkách <chile/fiscal-info>“
- :ref:`Elektronické údaje o faktuře <chile/elektronicke-udaje-o-fakture>“
- :ref:`Příchozí e-mailový server DTE <chile/dte-email>`
- :ref:`Certifikáty podepisování <chile/signature-certificates>“

.._chile/fiskální informace:

Daňová informace
------------------

Vyplňte následující pole „Informace o poplatníkovi“:

- Vyberte typ poplatníka klepnutím na pole „Taxpayer Type“ a vyberte typ poplatníka, který se vztahuje.

  - :guilabel:`DPH ovlivňuje (kategorie 1)“: pro faktury, které přenášejí daň na zákazníky
  - :guilabel:`Příjemce poplatku (2. kategorie)`: pro dodavatele, kteří vystavují faktury (Boleta)
  - :guilabel:`Konečný spotřebitel“: pouze vystavuje faktury
  - :guilabel:`Cizinec“

- :guilabel:`SII Office“: vyberte svou společnost a její „SII (Servicio de Impuestos Internos)“.
regionální kancelář

..._faktura-v-čr

Elektronická data faktury
-----------------------

Vyberte své prostředí SII Web Services:

- Guilabel: „SII - Test“: pro testovací databáze používající testové :abbr. „CAFy (Folio
Kód autorizace získaný od SII (Servicio de Impuestos Internos). V tomto režimu
testovat lze přímé spojení, kdy se soubory posílají na SII (Servicio
Daň z příjmů právnických osob`.
- :guilabel:`SII - Produkce“ pro produkční databáze.
- :guilabel:Demo režim: soubory se vytváří a přijímají automaticky v demo režimu,
**nebyly** zaslány do SII (Servicio de Impuestos Internos). Proto byly odmítnuty.
chyby nebo *Přijato s námitkami* se v tomto režimu nezobrazí. Každá interní kontrola může
je možné otestovat v režimu demo. V produkčním prostředí se vyhněte tomuto nastavení.

Poté zadejte „Elektronické účetní doklady“:

- :guilabel:`Rozhodnutí SII č. „
- :guilabel:`Datum rozhodnutí SII“

.. obrázek: chile/faktura-elektronicky.png
:alt:Povinné údaje pro elektronickou fakturu.
:align:center

.. _chile/dte-email:

DTE příchozí e-mailový server
=========================

Kód DTE (Elektronické daňové doklady) může být
aby přijímal e-maily s nároky a potvrzeními od svých zákazníků.
Potřebujete zvolit v menu „Účetnictví“ -> „Konfigurace“ -> „Nastavení“ -> „Lokalizace pro Chile“.
chcete použít *E-mailová schránka pro elektronické faktury* jako zkratku DTE (dokumenty
Elektronické) příchozí poštovní server.

.. důležité::
Pro získání vašich SII dokumentů je nutné mít vlastní e-mailový server.
Informace o tom, jak to udělat, najdete v této dokumentaci:
:doc:`../../obecne/komunikace_e-mailem`

Začněte kliknutím na „Konfigurace příchozích e-mailů od DTE“ a poté klikněte na „Nový“, abyste přidali
server a vyplňte následující pole:

- :guilabel:`Název“: Přidejte serveru název.
- :guilabel:`Typ serveru“: vyberte typ serveru, který používáte.

  - :guilabel:`IMAP server“
  - :guilabel:`POP server“
  - :guilabel:`Vlastní server“: používá vlastní skript k získání e-mailů a vytvoření nových záznamů.
skript najdete v sekci Konfigurace s tímto nastavením.
  - :guilabel:`Gmail OAuth Authentication“: vyžaduje, aby byly vaše přihlašovací údaje k Gmailu nakonfigurovány v
obecné nastavení. Do konfigurace se lze dostat přes odkaz v :guilabel:`Přihlášení
Informace" v sekci "Informace".

- :guilabel:„Server DTE“: zapněte tuto možnost. Při zaškrtnutí této možnosti bude
používala k přijímání elektronických faktur od dodavatelů a komunikací ze SII
(Finanční správa) ohledně vystavených elektronických faktur. V tomto případě se jedná o
E-mailová adresa musí odpovídat oběma e-mailům uvedeným na webu SII.
v části: *Aktualizace údajů o přispěvateli*, *Kontaktní e-mail SII* a *Kontaktní e-mail
Společnosti*.

V záložce „Server a přihlášení“ (pro servery IMAP a POP):

- :guilabel:`Název serveru“: zadejte název nebo IP adresu serveru.
- :guilabel:`Port`: zadejte port serveru.
- :guilabel:`SSL/TLS“: zapněte tuto volbu, pokud jsou spojení šifrována pomocí protokolu SSL/TLS.
- :guilabel:`Uživatelské jméno“: zadejte uživatelské jméno serveru.
- :guilabel:`Heslo“: zadejte heslo k přihlášení do serveru.

.. obrázek: chile/dte-prijimane-email.png
:alt: Konfigurace příchozího e-mailového serveru pro chilské DTE.
:align:center

.. tip::
Před zahájením provozu je doporučeno archivovat nebo odstranit všechny e-maily týkající se faktur dodavatelů.
nejsou nutné k zpracování v Odoo z vaší schránky.

.._čile/certifikát:

Certifikát
-----------

Pro vytvoření elektronické podpisu faktury je potřeba digitální certifikát ve formátu .pfx.
Přidejte jednu, klikněte na „Nastavení certifikátů pro elektronickou identitu“ pod „Elektronická identita“.
Sekce „Certifikáty“. Pak klikněte na tlačítko „Nový“ a nakonfigurujte certifikát:

- Klikněte na „Nahrát soubor“ a vyberte soubor s příponou .pfx.
- :guilabel:`Souborový klíč“: zadejte heslo k souboru.
- „Číslo sériového předmětu“: v závislosti na formátu certifikátu může být pole prázdné.
V případě automaticky vyplněného certifikátu zadejte jeho právního zástupce: abbr.: RUT
(Univerzální daňový systém).
- :guilabel:`Vlastník certifikátu“: vyberte jeden, pokud chcete omezit použití certifikátu na konkrétní
Uživatel. Nechte pole prázdné, pokud chcete sdílet účet s ostatními uživateli fakturace.

.. obrázek: chile/nový-certifikát.png
:alt: Konfigurace digitálního certifikátu.
:align:center

.. varování:
Pokud je pole „Vlastník certifikátu“ nastaveno na konkrétního uživatele a neexistují
certifikáty sdílené s uživateli, pak automatické odesílání elektronických dokumentů a přijímání
uznání je **vypnuté**.

Multiměnová
=============

Oficiální kurz měny je uveden na stránkách „Chilský indikátor <https://mindicador.cl>“.
do políčka:menu_selection:Účetnictví --> Konfigurace --> Nastavení --> Měny: Automatická měna
Rychlosti nastavit interval pro aktualizaci sazby nebo vybrat
další služba.

..._česko/partner-information:

Informace o partnerovi
===================

Konfigurace kontaktů partnera je také nutná pro odeslání SII
elektronické faktury. Otevřete aplikaci Kontakty a vyplňte následující
V poli na novém nebo existujícím kontaktním formuláři.

- :label:Jméno
- :guilabel:`E-mail“
- :guilabel:`Číslo identifikace“
- :guilabel:`Druh daňového poplatníka“
- :guilabel:`Popis aktivity“

V záložce „Elektronické fakturace“:

- :guilabel:`E-mail DTE“: Zadejte e-mailovou adresu odesílatele pro partnery.
- :guilabel:`Cena pro dodací průvodce“: vyberte, zda se v případě nějaké ceny má zobrazovat dodací průvodce.

.. poznámka::
DTE Email je e-mailová adresa, kterou používáte k odesílání elektronických dokumentů.
kontakt, který bude součástí elektronického dokumentu.

.. obrázek: chile/dte-email-faktura-elektronicka.png
:alt:Elektronické faktury pro partnery z Chile.
:align:center

Druhy dokumentů
==============

Účetní dokumenty jsou kategorizovány podle definice SII (Servicio de Impuestos Internos)
druh dokumentu.

Typ dokumentu vytváří automaticky při instalaci lokální verze a lze jej
spravované při přechodu na:menu:Účetnictví --> Konfigurace --> Druhy dokladů.

.. obrázek: chile/chilské dokumenty.png
:alt: Seznam chilských daňových dokumentů.
:align:center

.. poznámka::
Řada dokumentů je vypnutá výchozím nastavením, ale může být aktivována přepínáním.
:guilabel:`Aktivní“ volba.

Použití na fakturách
---------------

Typ dokumentu každé transakce je určen:

- Kniha související s fakturou, která určuje, zda kniha používá dokumenty.
- Podmínka se vztahuje na typ emitenta a příjemce (např. kupující nebo prodejce).
fiskální režim)

Časopisy
========

Knihy prodejů v Odoo obvykle reprezentují podnik nebo lokalitu.

.. příklad::
   - Ventas de Santiago.
   - Ventas Valparaiso.

Pro maloobchodní prodejny je běžné mít jeden deník na jedno :abbr:`POS (Point of Sale)“.

.. příklad::
   - Pokladní 1.
   - Pokladní 2.

Kupní operace lze vést v jednom deníku, ale někdy je používají firmy více
než jeden účetní deník, aby bylo možné zpracovat některé účetní transakce, které nejsou spojeny s dodavatelem.
fakturami. Tuto konfiguraci lze snadno nastavit pomocí následujícího modelu.

.. příklad::
   - Daňové platby státu.
   - Platby zaměstnanců.

Vytvořte prodejní deník
----------------------

Pro vytvoření prodejního deníku přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Deníky“.
Poté klikněte na tlačítko „Nový“ a vyplňte následující požadované informace:

- :guilabel:`Druh“: Vyberte možnost „Prodej“ z rozevírací nabídky pro fakturační deník zákazníka.
- :guilabel:„Typ prodejního místa“: pokud bude účetní deník použit k elektronickým dokumentům,
Vyberte možnost „On-line“. Jinak pokud je časopis použit pro faktury
přenesené z předchozího systému nebo pokud používáte službu SII (Servicio de Impuestos
portálu Internos) k dispozici možnost „Manuální“.
- :guilabel:`Používat dokumenty“: zaškrtněte tento prvek, pokud bude časopis používat typy dokumentů.
pouze pro nákupní a prodejní deníky, které lze přiřadit k různým sadám
dostupných v Chile. Výchozí nastavení pro všechny vytvářené fakturační doklady používá dokumenty.

Dále z karty „Záznamy“ definujte výchozí účet příjmů a
„Přidělená fakturační poznámka“ v sekci „Účetní informace“.
Konfigurace těchto polí je vyžadována pro jednu z případů použití faktury :ref:`<chile/use-cases>`.

.._chile/caf-dokumentace:

CAF
===

Pro každý typ dokumentu, který bude vydán, je nutné mít kód autorizace „folia“ (CAF).
elektronicky. CAF (Folio Authorization Code) je soubor, který SII (Servicio de
Daň z přidané hodnoty) poskytuje emitentovi sériové čísla/čísla pořadí, která jsou povolena pro elektronické
Daňové doklady.

Vaše společnost může požádat o více listin a získat několik kódů autorizace pro listiny (CAF).
spojené s různými rozsahy stran. Tyto :abbr:`CAFs (Folio Authorization Code)` jsou sdílené
všechny časopisy, takže pro každý typ dokumentu je potřeba aktivní :abbr:`CAF (Folio Authorization Code)“.
a bude se vztahovat na všechny tituly.

Prosím, zkontrolujte si „Dokumentaci SII <https://palena.sii.cl/dte/mn_timbraje.html>“.
podrobnosti o získání souborů s kódem autorizace CAF (Folio Authorization Code).

.. důležité::
Potřebujete-li kód autorizace CAF (Folio Authorization Code), požádejte o něj na SII (Servicio de Impuestos
Internos) jsou v režimu certifikace jiné než ve výrobním. Ujistěte se, že máte
V závislosti na vašem prostředí je správně nastavená hodnota :abbr:`CAF (Folio Authorization Code)“.

Nahrát soubory CAF
----------------

Jakmile byly získány soubory CAF (kód autorizace Folio), může být požadavek na vydání certifikátu předán do SII.
Portálu „Daňový úřad“ musí být nahrány do databáze po přechodu na
:menuvolba:Účetnictví --> Konfigurace: Chilský SII --> CAFs“. Pak klikněte na „Nový“
začít konfiguraci. Na formuláři „CAF (Autorizační kód Folio)“ nahrajte svůj „CAF
(Kód autorizace Folio) soubor kliknutím na tlačítko „Nahrát svůj soubor“ a pak klikněte
:guilabel:`Uložit“.

Jakmile je nahrána, její stav se změní na „Ve správě“. V tomto okamžiku, když transakce používá
Pro tento typ dokladu je číslo faktury první stránkou v pořadí.

.. důležité::
Dokumenty musí být aktivní před nahráním :abbr:`CAF (Folio Authorization Code)“
soubory. Pokud některé listy byly použity v předchozím systému, musí být následující platný list
vytvoření první transakce.

Klasifikační schéma
=================

Kniha účetních je součástí datového souboru, který je součástí lokalizace.
modul. Účty jsou automaticky připojeny v:

- Daně
- Neplacená pohledávka
- Neplacené faktury
- Převodní účty
- Úspěšnost konverze

.. viz též:
:doc:`../účetnictví/začínáme/rozvaha“

Daně
=====

Součástí lokální části je automatické vytváření daní spolu s příslušnými finančními
účet a konfigurace. Tyto daně lze spravovat z nabídky „Účetnictví ->
Konfigurace --> DPH“.

Chile má několik druhů daní, nejčastější jsou:

- DPH: běžná sazba DPH může být různá.
- **ILA**: daň z alkoholických nápojů.

.. viz též:
:doc:`../účetnictví/daně“

Použití a testování
=================

Elektronický proces fakturace
---------------------------

V chilské lokalizaci je součástí elektronického fakturačního procesu vydání faktury zákazníkovi a
přijetí faktury dodavatele. Následující schéma vysvětluje, jak jsou informace sdíleny s:abbr:`SII
(Vnitřní daňový úřad), zákazníci a dodavatelé.

.. obrázek: chile/elektronická faktura - průběh.png
:alt:Diagram elektronické fakturace.
:align:center

Emise faktury zákazníkovi
-------------------------

Po vytvoření partnerů a časopisů se vytváří faktury ve standardním režimu.
pro Chile je jedním z rozdílů typ dokumentu, který se automaticky vybere podle
Daňový subjekt. Typ dokladu lze změnit ručně, pokud je potřeba, v faktuře po kliknutí na
:menu:"Účetnictví --> Zákazníci --> Faktury".

.. obrázek: chile/faktura-pro-zakaznika.png
:alt:Výběr typu faktura pro zákazníka.
:align:center

.. důležité::
:guilabel:`Dokument typu 33“ musí mít elektronická faktura alespoň jeden položku s DPH jinak
Služba SII (Servicio de Impuestos Internos) dokument neověřila.

.._chile/elektronické fakturace:

Validace a stav DTE
~~~~~~~~~~~~~~~~~~~~~~~~~

Jakmile jsou doplněny všechny informace o faktuře, buď ručně nebo automaticky při generování z prodeje
objednávku, potvrdit fakturu. Po zadání faktury:

- Soubor DTE (Elektronické daňové dokumenty) vytváří systém automaticky a ukládá
v přepisech hovorů.
- :abbr:`DTE (Elektronické daňové dokumenty)“ :abbr:`SII (Vnitřní daňová služba)“
Stav je nastaven na:guilabel:"Čekající".

.. obrázek: chile/xml-creation.png
:alt:DTE XML soubor zobrazený v chatu.
:synchronizace: střed

Stav DTE (Documentos Tributarios Electrónicos) se aktualizuje automaticky pomocí Odoa.
plánovaná akce, která se spouští každý den v noci, pokud nedojde k odpovědi od SII (Servicio de
K tomu je potřeba okamžitě zavést „Daň z příjmů právnických osob“ (Impuestos Internos), což lze provést i manuálně podle
Stavový diagram průběhu procesu „Elektronické daňové dokumenty“ (zkratka DTE):

.. obrázek: chile/dte-status-flow.png
:alt: Přechod stavu DTE.
:align:center

#Prvním krokem je odeslání DTE do SII.
(Vnitřní daňový úřad`). Toto lze odeslat ručně kliknutím na tlačítko :guilabel:`Odeslat
Tlačítko „Teď“. To vygeneruje číslo faktury SII Tack, které se používá k identifikaci
Zkontrolujte podrobnosti zaslané e-mailem SII (Servicio de Impuestos Internos). Pak
:guilabel:`Stav DTE“ je aktualizován na „Zeptej se na stav“.
#Jakmile je odeslána odpověď služby SII (Servicio de Impuestos Internos), Odoo aktualizuje
:guilabel:`Stav DTE“. Chcete-li to provést ručně, klikněte na tlačítko :guilabel:`Zkontrolovat u SII“.
Výsledek může být buďto :guilabel:`Přijato`, :guilabel:`Přijato s výhradou“ nebo
:guilabel:`Odmítnuto“.

.... obrázek: chile/dte-status-steps.png
:alt:Identifikační transakce pro fakturu a aktualizaci stavu.
:align:center

.... důležité::
Existují mezičlánky v SII (Serviciqo de Impuestos Internos) před
přijetí nebo odmítnutí. Je doporučeno, abyste **NEKONTINUOVALI** kliknutím na „Přidat ověření“
SII pro hladký průběh zpracování.

.. obrázek: chile/chatter-internal-statuses.png
:alt:Stavy elektronických daňových dokladů.
:synchronizace: střed

#Finální odpověď z úřadu SII může být jednou z těchto
hodnoty:

   - :guilabel:`Přijato“: ukazuje na správnost informací o faktuře, náš dokument je nyní
Je daňově platná a automaticky je odeslána zákazníkovi.
   - :guilabel:'Přijato s výhradami': ukazuje, že informace na faktuře jsou správné, ale existují drobné
Vzhledem k tomu, že chyba byla identifikována, dokument je nyní daňově platný a automaticky
poslané zákazníkovi.
   - :guilabel:`Zamítnuto“: ukazuje, že informace na faktuře jsou chybné a musí být opraveny.
Podrobnosti jsou zasílány na e-mailové adresy, které jste zadali v rámci služby SII (Servicio de Impuestos Internos).
Pokud je správně nakonfigurováno v Odoo, detaily se zobrazí také ve chatu po kliknutí na
e-mailový server je zpracován.

Pokud byla faktura zamítnuta, postupujte prosím podle těchto kroků:

     #Změňte dokument na: guilabel:Návrh.
     #Vyžadované opravy provést na základě zprávy odeslané SII (Servicio
„Vnitřní daně“ v chatovacím okně.
     #Znovu vystavte fakturu.

.. obrázek: chile/odmítnutá faktura.png
:alt:Zpráva při odmítnutí faktury.
:srovnání: střed

Křížové odkazy
~~~~~~~~~~~~~~~~~~

Při vystavení faktury se zohlední informace související s
Zdrojový dokument musí být zaregistrován v záložce „Křížová reference“. Tato záložka je obvykle
Jedná se o účet používaný pro kreditní nebo debetní poznámky. V některých případech může být použit i pro faktury zákazníkům.
dobře. V případě platebních a kreditních poznámek jsou nastaveny automaticky pomocí Odoo.

.. obrázek: chile/křížovka-tabulka-registrace.png
:alt:Dokumenty, které se kříží.
:align:center

..._chile/elektronické faktury pdf report:

Přehled faktur ve formátu PDF
~~~~~~~~~~~~~~~~~~

Jakmile je faktura přijata a schválena SII (Servicio de Impuestos Internos),
PDF dokument je vytisknutý a obsahuje daňové prvky, které ukazují na to, že se jedná o daňový doklad.
platný.

.. obrázek: chile/přijatá faktura s daňovými údaji.png
:alt:Daňové prvky a čárový kód v přijatých fakturách.

.. důležité::
Pokud je váš systém hostovaný v Odoo SH nebo On-Premise, měli byste si nainstalovat pdf417gen
<https://pypi.org/project/pdf417gen/>_ knihovna. Nainstalujte ji pomocí následujícího příkazu:
:příkaz:`pip install pdf417gen`.

Komerční validace
~~~~~~~~~~~~~~~~~~~~~

Jakmile je faktura odeslána zákazníkovi:

#Stav „Partner DTE“ se změní na „Odesláno“.
#Kupující musí odeslat potvrzení o přijetí objednávky e-mailem.
#Poté, pokud jsou obchodní podmínky a údaje na faktuře správné, je vystaven potvrzení o přijetí.
jinak je zaslána reklamace.
#V poli „Stav přijetí DTE“ se aktualizuje automaticky.

.. obrázek: chile/partner-dte-status.png
:alt:Zpráva o komerčním přijetí od zákazníka.
:align:center

Pro zpracování reklamovaných faktur
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Jakmile je faktura přijata SII (Servicio de Impuestos Internos), **není možné ji
by se v Odoo** zrušil. V případě nároku na vašeho zákazníka je správným postupem
s fakturou, která bude buď zrušena nebo opravena. Prosím,
Pro více informací se podívejte na část „Chile/poznámky k úvěru“.

.. obrázek:chile/přijatá faktura.png
:alt:Stav faktury se změnil na uplatněnou.
:align:center

Nejčastější chyby
~~~~~~~~~~~~~

Za odmítnutím ze strany SII stojí několik důvodů.
Ale tady jsou některé z běžných chyb, které můžete udělat a jak je vyřešit:

- | **Chyba:** `RECHAZO - DTE Sin Comuna Origen`
| **Poznámka:** ujistěte se, že je adresa společnosti správně vyplněna včetně státu a města.
- | **Chyba:** `Monto - IVA musí být vykázáno.`
| **Tip:** v položkách faktury by měl být jeden DPH, ujistěte se, že přidáte jednu na každé faktuře
linka.
- | **Chyba:** `Ruta no autorizada para firma.`
| **Poznámka:** zadaná hodnota RUT (Rol Único Tributario) není povolena k fakturaci
:elektronicky ověřit správnost a platnost společnosti RUT (Rol Único Tributario)
v daňovém úřadu SII (Servicio de Impuestos Internos) zaúčtovat elektronicky.
- | **Chyba:**`Datum/Číslo rozhodnutí neplatné RECHAZO- SPLATNÉ: (DTE_Firma[AAAA-MM-DD]
CAF (od - do) > 6 měsíců
| **Poznámka:** Zkuste přidat nový CAF související s touto dokumentací, protože ten, který používáte, vypršel.
- |**Chyba:**`Element '{http://www.sii.cl/SiiDte%7DRutReceptor': Tento prvek se neočekává.
Očekává se ( http://www.sii.cl/SiiDte%7DRutEnvia ).
|  **Tip:**Zkontrolujte, zda jsou v poli „Druh dokumentu“ a „DPH“ nastaveny hodnoty
zákazníkem a v hlavní společnosti.
- | **Chyba:**`Uživatel nemá oprávnění k odesílání zpráv.`
| **Poznámka:** Tato chyba ukazuje, že pravděpodobně vaše společnost neprošla certifikací
procesu <https://www.sii.cl/factura_electronica/factura_mercado/proceso_certificacion.htm>
:abbr:`SII (Servicio de Impuestos Internos)` – Systém daňového účetnictví.
Pokud máte jakýkoliv dotaz k tomuto případu, kontaktujte prosím svého obchodního zástupce nebo podporu zákazníků. Toto oprávnění není
část služeb Odoo, ale můžeme vám nabídnout nějaké alternativy. Pokud jste již prošli
certifikační procesu se tato chyba objevuje při pokusu o přístup k souborům uživatelem jiným než vlastníkem.
certifikát se snaží odeslat soubor :abbr:`DTE (Elektronické daňové dokumenty)` do
:zkratka: „Finanční správa“.
- | **Chyba:** `CARATULA`
| **Poznámka:** Příčin, proč se tento problém může objevit, je pět a všechny jsou spojené s
do části XML *Caratula*.

    - Číslo RUT (jedinečného daňového registračního čísla) společnosti je nesprávné nebo chybí.
    - Vlastník certifikátu:abbr: RUT (Rol Único Tributario) má nesprávné číslo nebo je chybí.
    - Číslo RUT (Rol Único Tributario) společnosti SII (Servicio de Impuestos Internos)
(výchozí hodnota) je nesprávná nebo chybí.
    - Datum vyřešení je nesprávné nebo chybí.
    - Číslo usnesení je nesprávné nebo chybí.

.._chile/platební-poznámky:

Kreditní poznámky
------------

Pokud je potřeba zrušit nebo opravit platnou fakturu, musí být vystaven
generován. Je důležité si uvědomit, že soubor s oprávněním k autorizaci Folia (CAF)
požadované pro účel kreditní poznámky, která je identifikována jako „Typ dokumentu“ „61“.
Abk.: SII (Serviço de Impostos Internos). Prosím, obraťte se na část „CAF“
<chile/caf-documentation> pro více informací o procesu načítání:abbr: CAF (Folio
Autorizační kód) na každém typu dokumentu.

.. obrázek: chile/povolení k úvěru - typ dokumentu.png
:alt: Vytvoření CAF pro účetní doklady.
:align:center

Příklady použití
~~~~~~~~~

Zrušit odkazovaný dokument
**************************

Pokud potřebujete zrušit nebo neplatnou fakturu, přejděte na:
Zákazníci --> Faktury a vyberte požadovanou fakturu. Pak použijte tlačítko „Přidat kredit“
Vyberte možnost „Úplná náhrada“ a zadejte :guilabel:„SII (Servicio de Impuestos
Referenční kód Internosu je automaticky nastaven na „Dokument odkazující“.

.. obrázek: chile/smazat-odkaz-na-dokument.png
:alt:Zrušení odkazu na dokument.
:align:center

Korektní odkazovaný dokument
***************************

Pokud je třeba opravit údaje na faktuře, například ulici na původní
faktura je špatně, pak použijte tlačítko „Přidat kreditní fakturu“, vyberte „Částečná náhrada“
a vyberte možnost „Pouze oprava textu“. V tomto případě se použije :guilabel:`Zdroj SII
Hodnota pole „Kód“ je automaticky nastavena na „Opravuje text odkazovaného dokumentu“.

.. obrázek: chile/kreditni-zaporak-správný-text.png
:alt:Korekční poznámka k odkazovanému dokumentu.
:align:center

Odoo vytvoří kreditní fakturu s opraveným textem na faktuře a cenou 0,00 Kč.

.. obrázek: chile/oprava-textu.png
:alt: Kreditní poznámka s opravenou hodnotou na fakturačních řádcích.
:align:center

.. důležité::
Zkontrolujte, zda je definována položka „Výchozí účet kreditu“ v prodejním deníku.
tento scénář použití.

Opravuje odkazovaný dokument
***********************************

Pokud je třeba upravit částku, použijte tlačítko „Vytvořit kreditní poznámku“ a vyberte
„Částečná náhrada“. V tomto případě je automaticky nastaveno pole „Referenční kód SII“
:guilabel:`Upravte částku v odkazovaném dokumentu“.

.. obrázek: chile/kreditni-zpetna-platba-v-pravem-mnozstvi.png
:alt: Příkaz k úhradě za vrácení částky na správnou částku s použitím referenčního kódu SII 3.
:align:center

Debetní poznámky
-----------

V chilské lokalizaci mohou být vytvářeny kromě platebních příkazů také debetní poznámky pomocí
:guilabel:`Přidat debetní poznámku“ tlačítko s dvěma hlavními použitími.

.._chile/pouziti:

Příklady použití
~~~~~~~~~

Přidejte dluh na fakturách
********************

Hlavním použitím pro debetní poznámky je zvýšení hodnoty stávající faktury.
Vyberte možnost: „Korektura částky v referenčním dokumentu“
:guilabel:`Referenční kód SII“ pole.

.. obrázek: chile/platební-poznámka-správná-částka.png
:alt: Dodatečná debetní poznámka opravující částku v odkazovaném dokumentu.
:align:center

V tomto případě je vložena do položky „Příjem“ automaticky i položka „Zdroj faktury“.
Tabulka „Odkaz“.

.. obrázek: chile/auto-ref-debit-note.png
:alt:Automatické odkazování na fakturu v platebním výměru.
:align:center

.. tip::
Pouze do již přijaté faktury lze vložit záporný doklad.

Zrušit kreditní poznámky
*******************

V Chile se používají k zrušení platného účetního dokladu poznámky o dluhu. Pro jejich vytvoření klikněte na tlačítko:
Tlačítko „Debetní poznámka“ a vyberte možnost „1: Zrušit dokumenty o odkazech“.
:guilabel:`Referenční kód SII“ pole.

.. obrázek: chile/soubor-pro-zrušení-dodatečného-záznamu-výpisu.png
:alt:Dodatečná faktura k zrušení odkazovaného dokladu (kreditní faktury).
:align:center

Faktury dodavatelů
------------

Jako součást chilské lokalizace můžete konfigurovat svůj příchozí e-mailový server tak, aby odpovídal tomu
Registrujete se u SII (Servicio de Impuestos Internos) pro:

- Automaticky přijímat faktury od dodavatelů: DTE (elektronické daňové doklady).
Vytvořit fakturu dodavatele na základě těchto informací.
- Přijatou fakturu automaticky odeslat dodavateli.
- Přijměte nebo uplatněte dokument a pošlete tento stav svému dodavateli.

Recepce
~~~~~~~~~

Jakmile obdržíte e-mail od dodavatele s přílohou DTE (Elektronické daňové dokumenty),
přijato:

#Výpis z účtu dodavatele obsahuje všechny informace obsažené v XML.
#E-mail s potvrzením přijetí je zaslán dodavateli.
#:guilabel:Stav DTE je nastaven na „Přijato“.

Přijetí
~~~~~~~~~~~

Pokud je veškerá komerční informace na faktuře dodavatele správná, pak můžete tento dokument přijmout.
pomocí tlačítka „Přijmout dokument“. Jakmile je to hotové, můžete kliknout na tlačítko „Přijetí DTE“.
Stav změní na „Přijato“ a dodavateli je zasláno potvrzení o přijetí objednávky.

.. obrázek: chile/přijmout-fakturu-od-dodavatele-tlačítko.png
:alt:Tlačítko pro přijetí dodavatelských faktur.
:align:center

Žaloba
~~~~~

Pokud je problém komerční nebo informace na faktuře dodavatele není správná, můžete
Před ověřením si můžete dokument přivlastnit pomocí tlačítka „Zažádat“. Jakmile to uděláte,
:guilabel:„Akceptace DTE“ se změní na „Přiznání“ a odesílá se e-mail s odmítnutím.
Dodavatel.

.. obrázek: chile/claim-vendor-bill-btn.png
:alt:Tlačítko na faktuře dodavatele, aby dodavatel věděl, že celý dokument je komerční
zamítnuty.
:align:center

Pokud uplatníte fakturu dodavatele, stav se změní z :guilabel:`Návrh` na :guilabel:`Zrušit`.
automaticky. Vzhledem k tomu, že se jedná o nejlepší praxi, měly by být všechny požadované dokumenty zrušeny
Nebudou platit pro účetní záznamy.

Elektronická faktura za nákup
---------------------------

Funkce „elektronická faktura“ je součástí modulu l10n_cl_edi.

Jakmile jsou všechny konfigurace hotové pro :ref:`elektronické faktury <chile/electronic-invoice>
(např. nahrát platnou certifikát společnosti, nastavit základní údaje apod.) elektronickou
Pokladní faktury potřebují své vlastní :abbr:`CAFs (Folio Authorization Code)“. Prosím, zkontrolujte
:ref:`Dokumentace CAF <chile/caf-documentation>“ a zkontrolovat podrobnosti o tom, jak získat
:zkratka CAFs (kód autorizace Folio) pro elektronické faktury za nákupy.

Elektronické nákupní faktury jsou užitečné, pokud dodavatelé nejsou povinni posílat elektronicky.
faktura dodavatele za vaši koupi. Přesto však potřebujete dokument, který bude zaslán na
:zkratka SII (Servicio de Impuestos Internos) jako doklad o koupi.

Konfigurace
~~~~~~~~~~~~~

Pro vytvoření elektronické faktury od dodavatele je nutné vystavit fakturu ve
nákupní deník s funkcí „Použít dokumenty“. Je možné upravit již existující
nákupní deník nebo vytvořit nový v následujícím procesu.

Pro úpravu stávajícího nákupního deníku nebo vytvoření nového nákupního deníku přejděte na
Vyberte položku „Účetnictví“ -> „Nastavení“ -> „Knihy“. Pak klikněte na tlačítko „Nový“.
a vyplňte následující požadované informace:

- :guilabel:`Typ“: vyberte „Nákup“ z nabídky pro fakturační deník dodavatele.
- Zaškrtněte pole „Používat dokumenty“: zaškrtněte tento prvek, aby bylo možné vytvářet elektronické dokumenty (v
v tomto případě elektronická faktura).

Vytvořit elektronickou fakturu k nákupu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro vytvoření takového typu dokumentu je nutné vytvořit fakturu dodavatele v Odoo.
Přejděte na položku „Účetnictví“ -> „Dodavatelé“ -> „Faktury“ a klikněte na tlačítko „Nový“.

Po vyplnění všech informací o elektronické faktuře zvolte možnost (46).
Elektronický nákupní doklad“ v poli „Druh dokumentu“.

Po zveřejnění faktury dodavatele:

- Soubor DTE (Elektronický daňový doklad)
a automaticky vložen do konverzace.
- Stav zprávy DTE SII je nastaven na „Čeká na odeslání“.

Odoo automaticky aktualizuje stav DTE každou noc pomocí plánované akce. Chcete-li získat odpověď
od SII (Servicio de Impuestos Internos) okamžitě klikněte na „Odeslat nyní do
Tlačítko „SII“

Příručka pro doručování
--------------

Pro instalaci modulu „Průvodce dodáním“ přejděte na nabídku „Aplikace“ a vyhledejte Chile.
(l10n_cl`). Pak klikněte na tlačítko „Instalovat“ v modulu „Elektronické fakturace – doručení do Chile“.
Průvodce.

.. poznámka::
:guilabel:`Průvodce dodávkou faktur v Chile“ má závislost na :guilabel:`Chile -
Elektronická fakturace. Odoo nainstaluje závislost automaticky, jakmile
:guilabel:`Průvodce dodáním“ modul je nainstalován.

Modul „Příručka pro doručování“ zahrnuje možnost odesílat DTE (Dokumenty daňové povahy).
Elektronické)“ na „SII (Vnitřní daňový úřad)“ a razítko v PDF zprávách pro
dodávky.

Jakmile jsou všechny konfigurace hotové pro :ref:`elektronické faktury <chile/electronic-invoice>
(např. nahrát platný certifikát společnosti, nastavit základní údaje apod.), aby měli dodavatelé
vlastní CAF (Folio Authorization Code). Pro více informací se podívejte na dokumentaci k CAF.
<chile/caf-documentation>“ pro získání podrobností o tom, jak získat „CAF (Folio
Autorizační kód) pro elektronické průvodce dodávkami.

Zkontrolujte následující důležité informace v poli „Dopravní průvodce“:
konfigurace:

- :guilabel:„Z objednávky prodeje“: Dodací průvodce bere cenu produktu z objednávky prodeje a
Záznam o tom, že se tak stalo, je na dokumentu.
- „Od šablony produktu“: Odoo bere cenu, kterou je v šabloně produktu nastavená.
Záznam o tom, že se tak stalo, je na dokumentu.
- :guilabel:`Není uvedena cena“: v přepravním průvodci není uvedena žádná cena.

Elektronické průvodce dodávkou se používají k přesunu zásob z jednoho místa na druhé a mohou představovat
prodej, předvádění, odběr na sklad, a v podstatě jakýkoliv pohyb produktu.

Průvodce dodáním z prodejního procesu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. varování:
Dodací průvodce by neměl být delší než jedna stránka a měl by obsahovat méně než 60 položek.

Při vytvoření objednávky na prodej a jejím potvrzení se generuje dodací objednávka. Po ověření
dodacímu listu, je-li aktivována možnost vytvářet dodací průvodky.

.. obrázek: chile/tvorba-pruvodce-vypovedi.png
:alt:Vytvořit tlačítko Průvodce dodáním na proces prodeje.
:align:center

.. varování:
Když se na tlačítko „Vytvořit dodací průvodce“ klikne poprvé, objeví se varovné hlášení.
s tímto zněním:

„Nebyla nalezena sekvence pro odeslání zprávy. Prosím, nastavte první číslo
v poli pro číslo zásilky

...... obrázek: chile/dodací průvodce - číslo varování.png
:alt:První varovná zpráva o čísle dodávky.
:align:center

Toto varování znamená, že uživatel musí zadat další číslo sekvence, které má Odoo použít.
generovat dodací průvodce (např. další dostupný kód CAF (kód autorizace Folio)),
pouze při vytváření první dodací příručky v Odoo. Po vytvoření prvního dokumentu
správně vygenerované, Odoo použije další dostupné číslo v CAF (Autorizační folii
Vytvořit následující dodací průvodce pomocí souboru „(Code).

Po vytvoření průvodce doručováním:

- Soubor DTE (Elektronický daňový doklad)
je automaticky vytvořen a přidán do :guilabel:`chatteru`.
- Stav zprávy DTE SII je nastaven na „Čeká na odeslání“.

.. obrázek: chile/chatter-delivery-guide.png
:alt:Poznámky k vytváření průvodce doručováním.
:align:center

Stav DTE je automaticky aktualizován systémem Odoo prostřednictvím plánované akce, která se spouští každých
noci. K okamžitému vyřízení žádosti o odpověď SII (Servicio de Impuestos Internos) stiskněte
tlačítko „Odeslat nyní do SII“.

Jakmile je odeslán průvodce doručení, může být poté vytištěn kliknutím na tlačítko „Tisknout dodací lístek“.
Tlačítko „Průvodce“.

.. obrázek: chile/tisknout-průvodce-pro-doručení-výrobku-btn.png
:alt: Návod k tisku v PDF.
:align:center

Příručka pro doručování bude obsahovat daňové prvky, které ukazují, že dokument je daňově platný
vytisknout (pokud je hostována v Odoo SH nebo na On-premise pamatujte, že musíte ručně přidat
Knihovna pdf417gen zmíněná v části Zpráva o faktuře ve formátu PDF.
<chile/elektronická faktura pdf report>.

Elektronický doklad
------------------

Pro instalaci modulu „Elektronický doklad“ přejděte do nabídky „Aplikace“ a vyhledejte
„Chile“ (l10n_cl). Pak klikněte na tlačítko „Instalovat“ v modulu „Chile – Elektronická
Potvrzení o přijetí.

.. poznámka::
:guilabel:"Česko - Elektronická fakturace" má závislost na :guilabel:"Česko - Fakturace
Elektronika. Odoo nainstaluje závislost automaticky, jakmile je aktivována :guilabel:`Daňové
Modul „Průvodce dodáním“ je nainstalován.

Jakmile jsou všechny konfigurace hotové pro :ref:`elektronické faktury <chile/electronic-invoice>
(např. nahrání platného certifikátu společnosti, nastavení hlavních dat apod.), elektronické faktury
potřebují své vlastní „kódy autorizace Folia“ (CAF). Prosím, podívejte se na dokumentaci k CAF.
<česko/dokumentace-kaf> pro zjištění podrobností o tom, jak získat :abbr:`KAFy (Folio
Autorizační kód) pro elektronické účtenky.

Elektronické faktury jsou užitečné v případě, kdy klient nemá zájem o elektronickou fakturu. Výchozí hodnota je
partner v databázi s názvem „Anonymní konečný spotřebitel“ s obecným zkratkovým označením RUT (Roll
Único Tributario) a daňový subjekt typu: guilabel:Konečný spotřebitel. Tento partner může být
může být použita pro elektronické účtenky nebo může být vytvořen nový záznam pro stejný účel.

.. obrázek: chile/elektronický-doklad-o-přijetí.png
:alt: Modul elektronického daňového dokladu.
:align:center

Elektronické účtenky by měly být používány pro konečné spotřebitele s univerzálním identifikačním číslem :abbr:`RUT (Rol Único
Tributario`), může být také použita pro konkrétní partnery. Po vytvoření partnerů a časopisů
a nakonfigurována, elektronické účtenky vznikají ve standardním režimu jako elektronická faktura, ale
v dokladu o prodeji se má vybrat typ dokumentu „Elektronická faktura“:

.. obrázek:chile/dokument-typ-39.png
:alt: Dokument typu 39 pro elektronické faktury.
:align:center

Validace a stav DTE
~~~~~~~~~~~~~~~~~~~~~~~~~

Když jsou vyplněny všechny informace o elektronickém dokladu, postupujte ručně (nebo automaticky) k
ověřit fakturu z objednávky. Výchozí hodnotou je
V poli „Dokumentový typ“ je však třeba zadat správný údaj.
Vyberte „Dokument“ a změňte na „Elektronický doklad“.

Po zveřejnění faktury:

- Soubor DTE (Elektronický daňový doklad) vytváří
a přidána do chatu.
- Stav zprávy DTE SII je nastaven na „Čeká na odeslání“.

.. obrázek: chile/elektronický-pokladní-tiket-stav.png
:alt:Stav vytváření elektronických účtenek STE.
:align:center

Stav DTE je automaticky aktualizován systémem Odoo prostřednictvím plánované akce, která se spouští každých
den v noci. Chcete-li získat okamžitou odpověď od SII (Servicio de Impuestos Internos),
stiskněte tlačítko „Odeslat nyní do SII“.

Prosím, obraťte se na :ref:`DTE Workflow <chile/elektronické ověření faktury>“ pro elektronické
Faktury jsou vytvářeny stejným způsobem jako elektronické doklady o přijetí.

Elektronický vývoz zboží
--------------------------

Pro instalaci modulu „Export do zahraničí“ přejděte na záložku „Aplikace“ a
Hledejte „Chile (l10n_cl)“. Pak klikněte na tlačítko „Instalovat“ v modulu „Elektronické
Exporty zboží do Chile.

.. poznámka::
:guilabel:"Exporty elektronických výrobků do Chile" má závislost na :guilabel:"Chile
   - Elektronická fakturace.

Jakmile jsou všechny konfigurace hotové pro :ref:`elektronické faktury <chile/electronic-invoice>
(např. nahrání platného certifikátu společnosti, nastavení základních dat apod.), elektronické vývozy
Každé zboží potřebuje svůj vlastní :abbr:`CAF (Folio Authorization Code)“. Prosím, podívejte se na :ref:`CAF
dokumentaci „Chile/CAF-Dokumentace“ pro zjištění podrobností o tom, jak získat :abbr:`CAF
(Kód autorizace Folio) pro elektronické faktury.

Elektronické faktury pro vývoz zboží jsou daňovými dokladem, které se používají nejen
, ale také s celními úřady a obsahují
požadované informace.

Kontaktní konfigurace
~~~~~~~~~~~~~~~~~~~~~~

.. obrázek: chile/daně-z-vývozu-spotřebního-zboží.png
:alt:Druh poplatníka potřebný pro modul Elektronické vývozy zboží.
:align:center

Chilské celníky
~~~~~~~~~~~~~~~

Při vytváření elektronické vývozní faktury zboží se nové pole objeví v poli „Další informace“
Tabákové výrobky musí splňovat chilské předpisy.

.. obrázek: chile/chilean-custom-fields.png
:alt:Chilské celní pole.
:align:center

PDF zpráva
~~~~~~~~~~

Jakmile je faktura přijata a schválena SII (Servicio de Impuestos Internos),
PDF dokument je vytisknutý a obsahuje daňové prvky, které ukazují na to, že se jedná o daňový doklad.
platná a nová sekce potřebná pro celní úřad.

.. obrázek: chile/pdf-report-section.png
:alt: PDF část zprávy pro elektronické vývozy zboží.
:align:center

Elektronické fakturace v e-commerce
------------------------------

Pro instalaci modulu „Chilské elektronické obchodování“ přejděte do sekce „Aplikace“, vyhledejte
modul podle jeho technického názvu l10n_cl_edi_website_sale a klikněte na tlačítko „Aktivovat“.

.. obrázek: chile/ecommerce-module-chile.png
:align:center
:alt:eCommerce modul.

Tento modul umožňuje funkce a konfigurace:

- Vytvářet elektronické dokumenty z aplikace *eCommerce*
- Podpora požadovaných fiskálních polí v aplikaci *eCommerce*
- Ve skutečnosti nechá konečný uživatel rozhodnout o tom, který elektronický dokument bude vytvářet.
nákup

Když jsou všechny konfigurace pro chilské elektronické faktury
protokolem „elektronická faktura“ (Chile) je nutné nastavit následující konfigurace pro elektronický obchod.
integrovat se.

Pro konfiguraci webu tak, aby během prodejního procesu generoval elektronické dokumenty, přejděte na
V nabídce „Webová stránka“ -> „Konfigurace“ -> „Nastavení“ -> „Fakturace“ aktivujte
:automatické fakturace“. Aktivací této funkce umožňuje elektronickým dokumentům
je automaticky vytvořen při potvrzení platby přes internet.

.. obrázek: chile/konfigurace-webového-obchodu-chile.png
:align:center
:alt: Zásady fakturace a automatické konfigurace faktury.

Pro funkci automatické fakturace je potřeba, aby platba proběhla on-line a byla potvrzena.
dokumentu musí být pro příslušnou webovou stránku nakonfigurován poskytovatel plateb.

.. poznámka::
Pro informace o tom, kterými platebními poskytovateli lze platit, se podívejte na dokumentaci :doc:`../payment_providers`.
Jaké jsou v Odoo podporované a jak je konfigurovat.

Doporučuje se také nakonfigurovat své produkty tak, aby bylo možné je fakturovat v případě online prodeje.
Platba je potvrzena. Pro potvrzení přejděte na: „Webové stránky –> E-commerce –> Produkty“ a vyberte
vzor produktu požadovaného produktu. Poté nastavte :guilabel:`Způsob fakturace` na
:guilabel:`Počet objednaných kusů“.

.. obrázek: chile/objednané-množství-produktu.png
:align:center
:alt: Konfigurace fakturační politiky v produktech.

Fakturační toky
~~~~~~~~~~~~~~~

Klienti z Chile budou moci vybrat, jestli potřebují fakturu nebo hlasovací lístek.
nákup s přidaným krokem v průběhu objednávky.

.. obrázek: chile/select-edi-docs-ecommerce.png
:align:center
:alt:Možnost pro dokumenty v EDI pro klienty.

Pokud si zákazník zvolí možnost „Elektronická faktura“, je nutné vyplnit
vyplněny včetně popisu činnosti a identifikačního čísla
a jejich:guilabel:DTE e-mail.

.. obrázek: chile/daňové pole faktury e-commerce.png
:align:center
:alt:Povinné fiskální pole pro požadavek na vystavení faktury.

Pokud si klient zvolí možnost „Elektronické faktury“, bude přesměrován na další
krok a elektronický dokument bude vytvořen pro kontakt *Konečný spotřebitel Anonymní*.

Klienti ze zemí mimo Chile budou mít automaticky vygenerované elektronické faktury
Odoo pro ně.

.. poznámka::
Pokud je nákup na internetu vyžaduje vývoz, zákazník bude potřebovat kontaktovat vaši
společnost vygenerovat elektronickou vývozní fakturu (*dokument typu 110*), což lze provést z
aplikace *Účetnictví*.

Elektronické fakturace na prodejních místech
----------------------------------

Pro instalaci modulu „Chilean Module for Point of Sale“ přejděte do sekce „Aplikace“.
aplikace na hlavním panelu Odoo, vyhledání modulu podle jeho technického názvu
„l10n_cl_edi_pos“ a klikněte na tlačítko „Aktivovat“.

.. obrázek: chile/pos-edi-module-chile.png
:align:center
:alt: modul pro zpracování objednávek a fakturace.

Tento modul umožňuje následující funkce a konfigurace:

- Vytvářet elektronické dokumenty z aplikace POS
- Podpořte požadované daňové pole pro kontakty vytvořené v aplikaci Point of Sale
- Umožňuje konečnému uživateli rozhodnout o typu elektronického dokumentu, který má být vytvořen.
nákup
- V lístcích na DPH bude možné čárový kód nebo pětimístný kód

Pro konfiguraci kontaktů s požadovanými fiskálními informacemi přezkoumejte:
V části „Informace o partnerovi“ nebo přímo upravte kontakt. Přejděte na
:menuselection:`Prodejní místo --> Objednávka --> Zákazník --> Detail“ a upravte libovolnou z následujících položek
pole:

- :label:Jméno
- :guilabel:`E-mail“
- :guilabel:`Typ identifikace“
- :guilabel:`Druh daňového poplatníka“
- :guilabel:`Typ Giro“
- :guilabel:`E-mail DTE“
- :guilabel:`RUT“

.. obrázek: chile/fiskální-požadavky-pro-předložení-v-soudu.png
:align:center
:alt:Kontakt s daňovou informací vytvořenou z POS.

Pro konfiguraci produktů přejděte na: `Kasa --> Produkty --> Produkty`.
Vyberte záznam produktu. V kartě „Prodej“ v dialogovém okně pro editaci produktu je nutné označit
produkt jako „K dispozici pro POS“, což produkt dělá dostupným k prodeji v
Aplikace „Body prodeje“.

.. obrázek: chile/dostupne-v-pocitacech-produkt.png
:align:center
:alt: Produkt s daňovou informací vytvořený z POS.

Volitelně jsou k dispozici následující funkce pro konfiguraci v položce :menuselection:`Punktový
Prodej --> Konfigurace --> Nastavení --> sekce Faktury a příjmy:

- :guilabel:'Použijte QR kód na lístku': tato funkce umožňuje vytisknout QR kód na lístek uživatele.
účtenku, aby mohli pohodlně požádat o fakturu ihned po nákupu.
- :guilabel:`Vytvořit kód na lístku“: tato funkce umožňuje vytvářet pětimístný kód
účtenka, která umožňuje uživateli požádat o fakturu prostřednictvím zákaznického portálu

.. obrázek: chile/qr-code-ticket.png
:align:center
:alt: Konfigurace pro generování QR nebo pětimístných kódů na lístcích.

Fakturační toky
~~~~~~~~~~~~~~~

Následující části pokrývají fakturační toky aplikace Point of Sale.

Elektronické účtenky: anonymní uživatel
***************************************

Při nákupu jako neregistrovaný uživatel, který nepožaduje elektronickou fakturu, používá
automaticky vybere kontakt „Anonymní konečný spotřebitel“ pro objednávku.
Vytváří elektronický daňový doklad.

.. obrázek: chile/faktura-prijemka-vyber.png
:align:center
:alt:Automatické vybrání kontaktu pro neznámého koncového spotřebitele.

.. poznámka::
Pokud zákazník požádá o vystavení kreditní faktury kvůli vrácení zboží, měla by být
Vytvořené pomocí aplikace *Účetnictví*. Podrobnosti viz dokumentaci kreditních poznámek a vrácených částek
pro podrobné pokyny.

Elektronické účtenky: specifický zákazník
**************************************

Když uživatel nakoupí bez požadavku na elektronický fakturační doklad, Odoo automaticky
Vyberte kontakt pro objednávku jako „Konečný spotřebitel anonymní“ a
vybrat nebo vytvořit požadovaný kontakt s fiskálními informacemi pro účtenku.

.. obrázek: chile/kontakt-pro-elektronickou-fakturu.png
:align:center
:alt: Vybrat kontakt pro přijetí.

.. poznámka::
Pokud klient požádá o vystavení daňového dokladu kvůli vrácení zboží tohoto druhu, bude mu vystavena
Provedení poznámky a návratu lze spravovat přímo z POS sezení.

Elektronické faktury
*******************

Když si klienti vyžádají elektronickou fakturu, je možné zvolit nebo vytvořit požadovaný kontakt.
s daňovými informacemi. Při platbě vyberte možnost „Faktura“.
Vytvořit dokument.

.. obrázek: chile/faktura-v-platbě.png
:align:center
:alt: Výběr způsobu platby při placení faktury.

.. poznámka::
Pro oba typy elektronických faktur a faktur, pokud se zboží nepodléhá dani, je Odoo
Tento fakt detekuje a vytvoří správný typ dokumentu pro daňově osvobozené prodeje.

Vrácení zboží
*******

Pro elektronické účtenky (ne pro faktury vystavené pro *Consumidor Final Anónimo*) a elektronické faktury
je možné řídit proces vrácení produktů prodaných na objednávku z :abbr:`POS (Point of Sale)“
kliknutím na tlačítko „Vrácení“.

.. obrázek: chile/vraceni-penez.png
:align:center
:alt: Možnost vrácení peněz v aplikaci POS.

Objednávky lze vyhledávat podle stavu objednávky nebo kontaktu a zvolit pro vrácení peněz.
na původní objednávce klienta.

.. obrázek: chile/vyber-obchod-vraceni-zbozi.png
:align:center
:alt:Výběr způsobu vrácení peněz.

Když je platba vrácení zboží ověřena, Odoo vygeneruje potřebný kreditní doklad s odkazem na
originální faktura nebo dodací list, částečně nebo úplně rušící dokument.

.. viz též:
„Chytrý návod – Elektronická fakturace pro maloobchodníky
<https://www.youtube.com/watch?v=B2XuWmtlmno&t=360s>.

Finanční výkazy
=================

Daňová rovnováha v osmi sloupcích
--------------------------------

Tento výkaz podrobně popisuje jednotlivé účty (s jejich příslušnými zůstatky) a třídí je.
podle původu a určují úroveň zisku nebo ztráty, kterou podnik měl v
hodnotí období časové.

Tento výkaz najdete v sekci „Účetnictví“ -> „Vyhodnocení“ -> „Výsledovka“.
Vybrat v poli „Zpráva“ možnost „Saldo chilského rozpočtu (8 sloupců)“.


.. obrázek: chile/lokace-rozpočtového vyrovnání.png
:alt:Místo, kde se nachází Report Balance Tributario de 8 Columnas.
:align:center

.. obrázek: chile/8-kolonkový-rozpočtový-saldo-zpráva.png
:alt:Saldo chilského státního rozpočtu (8 sloupců).
:align:center

Návrh F29
-------------

Formulář F29 je nový systém, který umožnil SII (Servicio de Impuestos Internos)
Daňoví poplatníci a nahrazuje knihy nákupů a prodejů. Tento výkaz je integrován do výkazu
Registr (ŘP) a Registr prodejů (ŘPV). Jeho účelem je podpora transakcí souvisejících s
DPH, zlepšení kontroly a vykazování.

.. důležité::
Zpráva Propuesta F29 (CL) v Odoo pokrývá základní právní požadavky jako první návrh
pro vaši konečnou daňovou deklaraci.

Tento rekord je dodán elektronickými daňovými doklady (DTE), které byly obdrženy od
zkratka: SII (Servicio de Impuestos Internos).

Tento výkaz najdete v sekci „Účetnictví – Zprávy – Daňové zprávy“ a vyberte
volba „Zpráva“ a volba „Návrh F29 (CL)“.

.. obrázek: chile/locate-propuesta-f29-report.png
:alt:Místo, kde se nachází zpráva o Propuesta F29 (CL).
:align:center

Je možné nastavit sazbu PPM (Provisional Monthly Payments rate) a
„Proporční faktor pro účetní období“ z nabídky „Účetnictví ->
Konfigurace --> Nastavení.

.. obrázek: chile/f29-report.png
:alt:Výchozí PPM a proporční faktor pro zprávu Propuesta F29.
:align:center

Manuálně v zprávách kliknutím na ikonu :guilabel:`✏️ (tužka)`.

.. obrázek: chile/manual-ppm-f29-report.png
:alt: Ruční PPM pro zprávu o Propuesta F29.
:align:center
