=======
Ekvádor
=======

S ekvádorskou lokalizací mohou být vytvářeny elektronické dokumenty pomocí XML a fiskální
foliový záznam, elektronická podepisování a přímé propojení na finanční úřad SRI.

Podporované dokumenty jsou faktury, kreditní a debetní doklady, nákupní uhrazení a
Srážky.

Lokalizace zahrnuje také automatizaci, která usnadňuje předpovídání srážkové daně, která se bude vztahovat na
každou fakturu o koupi.

.. viz též:
   - „Tour App - Lokace Ekvádoru“ <https://www.youtube.com/watch?v=BQOXVSDeeK8>
   - „Chytrý návod – Lokace Ekvádoru
<https://www.odoo.com/slides/smart-tutorial-lokalizace-ekvádoru-170>
   - Dokumentace o zákonnosti a souladu s předpisy v Ekvádoru


.. tip::
   - **SRI**: *Úřad pro vnitrostátní příjmy*, vládní organizace, která vykonává dohled nad platbami
daní v Ekvádoru.
   - Certifikát SRI: Dokument nebo digitální kredit vystavený SRI, který je pro
splnění ekvádorských daňových zákonů.
   - **EDI**: Elektronický výměnný systém, který se týká elektronické přenosy
dokumenty.
   - **RIMPE**: *Zjednodušený režim pro podnikatele a obchodníky*, typ daňového poplatníka, který splňuje
pro SRI.

... /ekvádor/modul-instalace:

Moduly
=======

Instalujte následující moduly, abyste získali všechny funkce
ekvádorská lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 25 25 50

   * Jméno
     - Technické označení
     - Popis
   * – EKUADORSKÝ ÚČETNÍ
     - l10n_ec
     - Výchozí balík pro daňové lokalizace :doc:`<../fiscal_localizations>` přidává účetnictví.
charakteristiky pro ekvádorskou lokalizaci, které představují minimální konfiguraci
požadované pro společnost, která chce v Ekvádoru podle pokynů stanovených
:zkratka: „SRI (služba vnitřních příjmů)“. Instalace modulu se provádí automaticky a načítá:
rozvaha, daně, typy dokladů a podpory daní.
Generování formulářů 103 a 104 je automatické.
   * --:účetní EDI v Ekvádoru
     - „l10n_ec_edi“
     - Zahrnuje všechny technické a funkční požadavky na generování a ověření
:dokument: „Dokumenty elektroniky <../účetnictví/fakturace zákazníků/elektronická fakturace>“ založené na
technickou dokumentaci vydanou SRI. Autorizovanými dokumenty jsou: faktury,
Kreditní poznámky, debetní poznámky, srážky a likvidace nákupů.
   * – :guilabel:`Účetní zprávy Ekvádoru“
     - „l10n_ec_reports“
     - Zahrnuje všechny technické a funkční požadavky na vytváření formulářů 103 a 104.
   * :- guilabel:Ekvádor - Zpráva o atmosférickém tlaku
     - l10n_ec_reports_ats
     - Zahrnuje všechny technické a funkční požadavky na vytvoření souboru XML s hlášením ATS
připravené k nahrání do formuláře DIMM.
   * :- guilabel:Ekvádorská webová stránka
     - l10n_ec_website_sale
     - Zahrnuje všechny technické a funkční požadavky na generování automatických elektronických
faktury za prodej na webu.
   * :-:Prodejní místo v Ekvádoru
     - l10n_ec_edi_pos
     - Zahrnuje všechny technické a funkční požadavky na generování automatických elektronických
faktury z prodeje na pokladně.
   * – :guilabel:Průvodce dodávkou v Ekvádoru
     - l10n_ec_edi_stock
     - Zahrnuje všechny technické a funkční požadavky na vytvoření elektronického doručení:
průvodce <lokalizace/ekvádor/elektronické doručení - průvodce>.

.. poznámka::
V některých případech, například při aktualizaci na verzi s dalšími moduly, tyto moduly nemusí být
bude nainstalován automaticky. Chybějící moduly lze ručně
:doc:`nainstalovány </aplikace/obecné/aplikační moduly>“.

.. viz též:
:doc:`/aplikace/hr/mzdy/lokalizace-mzdových výpočtů“ jsou dokumentovány samostatně.

..._lokalizace/ekvádor/specifika:

Přehled lokalizace
=====================

Ekvádorská lokalizace zajišťuje soulad s ekvádorským daňovým a účetním systémem.
směrnice. Obsahuje nástroje pro správu daní, fiskální pozice, výkaznictví a předdefinované
účetní kniha přizpůsobená standardům Ekvádoru.

Ekvádorská lokalizační sada poskytuje následující klíčové funkce, které zajišťují soulad
lokální daňové a účetní předpisy:

- :doc:`../účetnictví/začínáme/rozvaha“: předdefinovaný struktura, která je v souladu s nejnovějšími
standardy ekvádorské Superintendencia de Compañías, které jsou rozdělené do několika kategorií a
je plně kompatibilní s účetnictvím NIIF
- :ref:`Produkty <lokalizace/ekvádor/produkty>`
- „Daňové sazby“: přednastavené daňové sazby včetně běžné DPH
nulové sazby a osvobozené možnosti
- :doc:`../accounting/taxes/fiscal_positions`: automatické daňové úpravy podle zákazníka nebo
stav registrace dodavatele
- „Dokumenty <lokality/ekvádor/dokumenty>“: klasifikace transakcí, jako
*faktury zákazníků* a *dodavatelské faktury* pomocí definovaných typů dokumentů stanovených vládou.

- :ref:`Společnost a kontakty <lokalizace/ekvádor/spolecnost-kontakty>`
- :ref:`Elektronické dokumenty <lokalizace/ekvádor/elektronické-dokumenty>`
- :ref:`Srážková daň <lokalizace/ekvádor/srazkova-dana>`
- :ref:`Tiskárny <lokalizace/ekvádor/tiskárny>`
- :ref:`Zadržení daně <localizations/ecuador/withholding>`
- :ref:`Hlášení <lokalizace/ekvádor/hlášení>`

... /ekvádor/produkty:

Produkty
--------

Pokud má produkt jakékoliv daňové srážky, musí být
Nastavení na produktovém formuláři. Pro provedení takového nastavení přejděte na:
Zboží“. V záložce „Obecné informace“ zadejte jak „Dodací daně“, tak
:guilabel:`Zadržení zisku“.

..._lokalizace/ekvádor/daně:

Daně
-----

Pro správu daní přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Daně“.
Další konfigurace může být vyžadována pro následující typ daně:

- :guilabel:`Název daně“: Formát závisí na typu daně:

  - 
| `IVA [procenta] (104, [kód formuláře] [kód podpory] [zkrácený název podpory])`
|Příklad: „Sazba DPH 12 % (104, kód podpory daně z přidané hodnoty IVA)“
  - |**Pro daňové srážky z příjmu**:
|`Kód ATS [procento srážky] [název srážky]`
|Příklad: „Kód ATS 10 % z původního zdroje“

- :guilabel:`Daňová podpora“: Konfigurace pouze pro DPH. Tato volba se používá k registraci nákupu
srážky ze mzdy.
- :guilabel:`Kód ATS“: Konfigurace pouze pro srážkové kódy daně z příjmu, protože je nutné
zaregistrovat srážku.

V záložce „Definice“:

- :guilabel:'Daňové sítě': Konfigurujte kód daňového přiznání 104, pokud se jedná o DPH.
103 pokud jde o kód zdanění příjmu.

.. viz též:
:doc:`Nastavení daní <../účetnictví/daně>`

..._lokalizace/ekvádor/dokumenty:

Druhy dokumentů
--------------

Chcete-li získat nebo nakonfigurovat typy dokumentů, přejděte na:
Druhy dokumentů“. Každý typ dokumentu může mít v každém časopise, kde je přiřazen, svou jedinečnou sekvenci.
část lokalizace dokumentu zahrnuje typ dokumentu a zemi, kde je dokument platný.
Dále je tato data vytvářena automaticky při instalaci modulu lokalizace.
Povinné položky pro dokumenty jsou zahrnuty výchozí hodnotou a nemusí se měnit.

..._lokalizace/ekvádor/firma-kontakt:

Společnost a kontakt
-------------------

.. viz též:
:doc:`Nastavte kontakt pro společnost nebo jednotlivce <../../essentials/contacts>`

Pro účely lokalizace na kontaktním formuláři je nutné vyplnit následující pole:

- :guilabel:`Jméno“: Zadejte jméno společnosti nebo osoby.
- :guilabel:`Adresa“: Podpole „Ulice“ je pro potvrzení elektronických faktur povinné.
- :guilabel:Číslo identifikace: Pro společnost zadejte :guilabel:IČ. Pro fyzické osoby
Zadejte číslo cedulky nebo pasu.
- :guilabel:`Typ daňového poplatníka SRI“: Vyberte typ daňového poplatníka SRI kontaktu.
- :guilabel:`Telefonní číslo“: Zadejte telefonní číslo společnosti nebo osoby.
- :guilabel:`E-mailová adresa“: Zadejte e-mailovou adresu společnosti nebo jednotlivce. Tato e-mailová adresa se používá k odesílání elektronických
například faktury.

.. poznámka::
Značení „SRI Taxpayer Type“ uvedené v kontaktním formuláři určuje, zda se jedná o DPH a
V případě použití této kontaktní osoby se aplikují srážkové daně.
na faktuře dodavatele.

..._lokalizace/ekvádor/elektronické dokumenty:

Elektronické dokumenty
--------------------

Pro nahrání informací o elektronických dokumentech přejděte na: „Účetnictví --> Konfigurace
→ Nastavení“, a posuňte se do části „Místní nastavení“.

Zadejte následující informace, začínající sekcí „Elektronická fakturace“:

- :guilabel:`Název společnosti“
- „Režim“: Vyberte, zda společnost spadá do „Běžného režimu (bez
dodatečné zprávy v režimu RIDE) nebo je kvalifikována jako v režimu RIMPE.
- :guilabel:`Speciální daňový identifikátor“: Pokud je společnost kvalifikována jako speciální poplatník, vyplňte
toto pole s příslušným daňovým identifikačním číslem společnosti.
- :guilabel:Povinné účetnictví“: Zapněte tuto možnost, pokud je potřeba.

:guilabel:„Zadržování“ sekce:

- :guilabel:`Spotřební materiál“: Zadejte kód sazby DPH, která se používá při nákupu zboží.
- :guilabel:`Služby“: Zadejte kód sazby DPH používané při nákupu služeb.
- :guilabel:`Kreditní karta“: Zadejte kód sazby daně z příjmu, která se používá při nákupu s
kreditní karty.
- :guilabel:Číslo srážkového agenta: Zadejte číslo rozhodnutí o srážkovém agentovi společnosti.
aplikovatelné.

:guilabel:„Připojení k SRI“:

- Vyberte soubor certifikátu společnosti. Klikněte
:ikonka: „pravý směr“ :guilabel:„Certifikáty SRI“ pro nahrání jednoho, pokud je třeba.
- :guilabel:`Používat produkční servery“: Zapněte tuto volbu, pokud se elektronické dokumenty používají v
produkční prostředí; v případě testovacího prostředí je nechte deaktivované.

:guilabel:Účty pro srážkovou daň

- :guilabel:`Daňový základ“: Zadejte účet daňového základu společnosti.
- :guilabel:`Daňový základ“: Zadejte daňovou položku pro nákupy společnosti.

.. důležité::
Při použití testovacího prostředí jsou datové zprávy EDI odeslány na testovací servery.

.. poznámka::
   - Hodnoty zadané do políčka „Zboží“ a „Služby“ v sekci „Výběr daně“.
jsou používány jako výchozí hodnoty pro domácí platby **pouze tehdy, když** nejsou nastavené srážky na *SRI.
Druh poplatníka*.
   - Vložená hodnota zadržení kreditní nebo debetní karty je vždy aplikována, když se používá kreditní nebo debetní karta.
používán způsob platby prostřednictvím karty SRI.

..._lokalizace/ekvádor/srážková daň:

Srážková daň
---------------

.. poznámka::
Tato konfigurace se použije pouze v případě, že SRI uzná společnost jako plátce daně z příjmu právnických osob.
V tomto kroku můžete přeskočit.

Pro konfiguraci srážky DPH přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Druh poplatníka“.
SRI. Poté nastavte název daňového subjektu typu DPH a název zboží.
Srážková daň“ a „Dodatečná daň z přidané hodnoty“.

.. tip::
Pokud je typ poplatníka „Rimpe“, nastavte „Srážku zisku“.
procenta.

..._lokalizace/ekvádor/tiskárna:

Tiskárna ukazuje
--------------

Pozice tiskárny je nutné nastavit pro každý typ elektronického dokumentu, který se používá, například pro zákazníka
faktury, kreditní doklady a záporné faktury.

Pro konfiguraci tiskových bodů přejděte do sekce „Účetnictví“ - „Konfigurace“
Časopisy. Pro každý elektronický dokument klikněte na „Nový“ a zadejte následující informace
v deníkovém tvaru:

- :guilabel:Název periodika: Zadejte v tomto formátu: [Subjekt emise] - [Místo emise] [Dokument
Typ, např. „001-001 Prodejní dokumenty“.
- :guilabel:`Typ“: Odkazuje na typ časopisu; vyberte „Prodej“.

Jakmile je vybrán typ, doplňte následující pole:

- :guilabel:`Používat dokumenty?“: Zapněte tuto volbu, pokud je v zemi povoleno daňové přiznání.
je použito, protože je to standardní konfigurace. Pokud ne, zvolte možnost záznamu účetnictví
vstupy nezpůsobené daňovým dokladem, jako jsou například faktury, platby daní nebo účetní záznamy
záznamy.
- :guilabel:`Příjemce emisí“: Zadejte číslo zařízení.
- :guilabel:`Výstupní bod“: Zadejte výstupní bod tiskárny.
- :guilabel:`Adresa emise“: Zadejte adresu zařízení.

V záložce „Účetní položky“ v sekci „Účetní informace“ vyplňte
v následujících polích:

- :guilabel:`Výchozí účet příjmu“: Zadejte výchozí účet příjmu.
- :guilabel:`Sekvenční kreditní poznámky“: Zapněte tuto volbu, pokud by měly být
vzniklé z tiskového bodu (tj. deníku).
- :guilabel:`Poznámky k účtům“: Zapněte tuto možnost, pokud chcete, aby byly
vzniklé z tiskového bodu (tj. deníku).
- :guilabel:Krátký kód: Zadejte jedinečný pětidílný kód pro sekvenci účetních vstupů (např.
VT001).

Faktury, kreditní a debetní poznámky musí používat stejný účet jako
„Výrobní místo“ a „místo subjektu“, které by mělo být pro každé periodikum jedinečné.

V posledním kroku v záložce „Další nastavení“ zkontrolujte položku „Daňový doklad“.
zaškrtávací políčko pro zasílání faktur v XML/EDI formátu.

.. viz též:
:doc:`../účetnictví/fakturace zákazníků/elektronická fakturace“

..._lokalizace/ekvádor/srážková daň:

Zadržování
-----------

Pro definování deníku srážkových plateb přejděte na: „Účetnictví > Konfigurace > Deníky“.
Pro každý srážkový deník klikněte na tlačítko „Nový“ a zadejte následující informace:

- :guilabel:`Název periodika“: Zadejte tento formát: „[Zpracovatel] - [Místo emise] [Dokument typu]“.
např. `001-001 Srážková daň`.
- :guilabel:`Typ“: Odkazuje na typ časopisu. Vyberte „Různé“.
- :guilabel:Zadržení typu: Vyberte :guilabel:Nákupní zadržení.

Jakmile jsou vybrány pole „Typ“ a „Společnost“, doplňte následující položky:

- :guilabel:`Příjemce emisí“: Zadejte číslo zařízení.
- :guilabel:`Výstupní bod“: Zadejte výstupní bod tiskárny.
- :guilabel:`Adresa emise“: Zadejte adresu zařízení.

V záložce „Účetní položky“ v sekci „Účetní informace“ vyplňte
v následujících polích:

- :label:Výchozí účet: Konfigurace výchozího účtu pro příjem.
- :guilabel:Krátký kód: Zadejte jedinečný pětidílný kód pro sekvenci účetních vstupů (např.
„WT001“.

V posledním kroku v záložce „Další nastavení“ zkontrolujte položku „Daňový doklad“.
zaškrtávací políčko pro zasílání faktur v XML/EDI formátu.

... /lokalizace/ekvádor/hlášení:

Reportáž
---------

Ekvádorské společnosti podávají daňové zprávy do SRI s Odoo podporou dvou hlavních:
103** a **104**.

Pro získání těchto výkazů přejděte na: „Účetnictví“ – „Výkazy“ – „Daňový přiznání“. Klikněte
Ikona „Zpráva“ a výběr čísla 103 nebo 104.

..._lokalizace/ekvádor/zpráva-103:

Zpráva č. 103
~~~~~~~~~~

Tento formulář obsahuje srážky z příjmu za určité období a může být podán měsíčně nebo
polovinu roku. Obsahuje informace o základu daně, výši daně a kódech daně a lze ji použít pro
Reporting o udržitelném rozvoji.

..._lokalizace/ekvádor/zpráva-104:

Zpráva č. 104
~~~~~~~~~~

Tento report obsahuje DPH, daň z přidané hodnoty srážkovou a lze jej vytvořit měsíčně nebo
polovinu roku. Obsahuje informace o základu daně, výši daně a kódech daně a lze ji použít pro
Reporting o udržitelném rozvoji.

..._lokalizace/ekvádor/ats:

Zpráva ATS
~~~~~~~~~~

Pro stažení zprávy o transakčním jednoduchém připojení ve formátu XML
Nainstalujte modul „Zpráva ATS“ („l10n_ec_reports_ats“) pomocí příkazu :doc:`install </applications/general/apps_modules>`.

.. poznámka::
Ekvádorský modul ATS Report závisí na předchozím nainstalování aplikace Accounting.
a ecuadorský modul EDI.*

.. _lokalizace/ekvádor/ats-konfigurace:

Konfigurace
*************

Pro vydávání elektronických dokumentů je nutné společnost nakonfigurovat tak, jak je uvedeno v
:ref:`elektronická faktura <lokalizace/ekvádor/firma-kontakt>` sekce. V :abbr:`ATS (Anexo
Transaccional Simplificado`, každý dokument vytvářený v Odoo, například faktury
<localizations/ecuador/customer-invoice>`, :ref:`faktury od dodavatelů <localizations/ecuador/vendor-bill>`,
„Prodej“ a „Nákup srážkové daně“.
<lokalizace/ekvádor/úhrada daňového odpočtu>`, :ref:`daňové doklady
<localizations/ecuador/kreditni-pozice>, a :ref:`débetní poznámky <localizations/ecuador/debetni-poznamky>
je zahrnuta.

... /lokalizace/ekvádor/ats-dodavatelské faktury:

Faktury dodavatelů
^^^^^^^^^^^^

Při vytváření faktury pro dodavatele zaregistrujte autorizaci
číslo z faktury dodavatele. Chcete-li tak učinit, přejděte na:
a vyberte fakturu. Poté zadejte číslo faktury od dodavatele
V poli „Autorizační číslo“.

... /ecuador/ats-credit-debit-notes:

Příkaz k úhradě a faktura
^^^^^^^^^^^^^^^^^^^^^^

Při vytváření :ref:`kreditu <localizations/ecuador/credit-notes>` nebo :ref:`debetního
<lokalizace/ekvádor/účetní poznámky> poznámku ručně nebo pomocí importu, propojte ji s prodejem
fakturu, kterou mění.

.. poznámka::
Některé informace je nutné uvést do dokumentů před stažením :abbr:`ATS (Anexo
souboru „Transaccional Simplificado“. Například přidejte číslo autorizace a SRI.
Pokud je potřeba, způsob platby* k dokumentům.

..._lokalizace/ekvádor/ats-xml-generování:

Výroba XML
**************

Pro vygenerování zprávy o ATS (Anexo Transaccional Simplificado) přejděte na
Vyberte položku „Účetnictví“ -> „Zprávy“ -> „Daňová přiznání“. Zvolte období pro požadované ATS.
(Zjednodušený transakční přehled) „report“, pak klikněte na „ATS“. Pak nahrajte stáhnutý
XML soubor do formulářů *.DIMM Formularios*.

.. poznámka::
Při stažení zprávy o transakčním jednoduchém přílohám (ATS) generuje Odoo
Pop-up varování uživatele v případě chybějících nebo nesprávných dat.
soubor XML stále lze stáhnout.

.._lokalizace/ekvádor/účetnictví:

Účetnictví
==========

... /lokalizace/ekvádor/prodejní dokumenty:

Prodejní dokumenty
---------------

..._lokalizace/ekvádor/faktura-pro-klienta:

Faktura pro zákazníka
~~~~~~~~~~~~~~~~

Faktury zákazníků, elektronické dokumenty: vytvořené z objednávek nebo ručně
<../účetnictví/fakturace/přehled>, musí obsahovat následující údaje a po ověření
jsou zasílány na SŘ:

- :guilabel:`Časopis“: Vyberte možnost odpovídající tiskárně bodu faktury zákazníka.
- :guilabel:`Dokumentový typ“: Zadejte dokumentový typ v tomto formátu: „(01) Faktura“.
- :guilabel:`Způsob platby (SRI)“: Vyberte způsob, jakým bude faktura zaplacena.

..._lokalizace/ekvádor/úvěrové poznámky:

Kreditní účet zákazníka
~~~~~~~~~~~~~~~~~~~~

:doc:`Kreditní poznámky zákazníků <../účetnictví/faktury/kreditní_poznamek_zakazniku>` jsou elektronické
Dokumenty zaslané do SRI, které byly ověřeny.
<účetnictví/kreditní poznámky/vystavit kreditní poznámku> lze zaregistrovat pouze ze schválené (odeslané)
faktura.

Zatímco je dokument typu :guilabel:`Credit Note`, udržujte na pozici :guilabel:`Document Type“ :guilabel:`(04) Credit Note“.
okno.

Vystavení kreditní faktury probíhá stejným způsobem jako vystavení :ref:`faktury
<účetnictví/vystavení faktury>.

.. poznámka::
Při vytváření prvního kreditního dokladu vyberte možnost „Zrušit“ a přiřaďte první kreditní doklad.
číslo nebo, pokud není zadáno, Odoo přiřazuje jako první číslo faktury „NotCr 001-001-000000001“.

..._lokalizace/ekvádor/účetní poznámky:

Dodací list kupujícího
~~~~~~~~~~~~~~~~~~~

:ref:`Faktury k úhradě <účetnictví/fakturace/vystavit-fakturu-k-uhradě>` jsou elektronické dokumenty zasílané
Společnosti SRI, která je již schválena. Pouze registrované společnosti mohou být zaregistrovány na základě platného (zaslaného) faktury.

V okně „Použít konkrétní účet“ v dialogovém okně „Vytvořit debetní poznámku“ vyberte
tiskárna pro fakturu nebo nechat prázdnou, aby se použil stejný deník jako u původní
faktura.

... /ekvádor/srážky ze mzdy zákazníka:

Zadržování zákazníkem
~~~~~~~~~~~~~~~~~~~~

„Zadržované platby klienta“ jsou papírové dokumenty vystavené klientem za účelem
zadržení prodeje. Mohou být zaevidovány pouze na základě ověřené (zaslané) faktury.

V faktuře klikněte na tlačítko „Srážka“ a doplňte následující informace v
Okno „Zadržení zákazníka“:

- :guilabel:`Číslo dokumentu“: Zadejte číslo srážkové daně.
- :guilabel:Vyberte srážkové daně, které zákazník odečítá.

Před ověřením srážkové daně zkontrolujte, že částky pro každou daň jsou stejné jako původní
dokument.

..._lokalizace/ekvádor/nákupní dokumenty:

Kupní smlouva
------------------

..._lokalizace/ekvádor/faktura dodavatele:

Faktura dodavatele
~~~~~~~~~~~

:doc:`Faktury dodavatelů <../accounting/vendor_bills>“, neelektronické dokumenty vytvořené z nákupu
příkazem nebo ručně vyžaduje konkrétní fakturu dodavatele
<lokalizace/ekvádor/faktury dodavatelům - deník>.

... /lokalizace/ekvádor/faktury dodavatelů - deník:

Faktura dodavatele
********************

Použijte následující konfiguraci pro nastavení knihy dodavatelských faktur.

- Vyberte „Koupit“ jako „Typ“.
- Nepočítáme-li „Likvidace nákupu“, pak nezaškrtávejte tento políček.
- Přidejte položku „Výchozí účet pro výdaje“.

Při konfiguraci faktury dodavatele se ujistěte také o vyplnění následujících ekvádorských polí:

- :guilabel:`Dokumentní typ“: Zadejte tento dokumentový typ: „(01) Faktura“.
- :guilabel:`Číslo dokumentu“: Zadejte číslo dokumentu.
- :guilabel:`Způsob platby (SRI)`: Vyberte způsob, jak zaplatit fakturu dodavatele.

.. důležité::
Při vytváření daňového odpočtu z nákupu ověřte, že jsou správné základy (základní částky). Pokud
částka daně v faktuře od dodavatele musí být upravena kliknutím na tlačítko „Upravit“. Nebo
z karty „Položky časopisu“ vyberte položku „Upravit“ a nastavte si úpravu podle svého uvážení.

..._lokalizace/ekvádor/nákupy-likvidace:

Likvidace koupě
~~~~~~~~~~~~~~~~~~~~

Elektronické dokumenty o „výkupu likvidace“ jsou zasílány do SRI poté, co byly ověřeny.
vydat je při nákupu, ale prodejce neposkytuje fakturu z důvodu jednoho nebo více
z následujících důvodů:

- Prováděli práce nezletilí občané Ekvádoru.
- Zahraniční společnosti poskytovaly služby bez rezidence nebo sídla v Ekvádoru.
- Nákup zboží nebo služeb od fyzických osob nezapsaných v RÚIAN, které nemohou vystavit
faktury nebo zákaznické faktury.
- Zaměstnanci musí být v případě náhrady za nákup zboží nebo služeb závislí.
vztah zaměstnance na plný úvazek.
- Členové kolektivních orgánů poskytli služby při výkonu své funkce.

V těchto případech je vhodné použít :ref:`účetní zápis
Musí být vytvořen soubor s názvem „<lokalizace/ekvádor/nákupní a likvidační deník>“.

... /koupě-a-likvidace-deník/:

Vytvořte knihu likvidace nákupů
*************************************

Pro vytvoření záznamu o likvidaci nákupů zadejte následující informace:

- :guilabel:`Název periodika“: Zadejte tento formát: „[Zpracovatel] - [Místo emise] [Dokument typu]“.
např. „001-001 Nákupy likvidací“.
- :guilabel:`Typ“: Odkazuje na typ časopisu. Vyberte „Koupit“.

Jakmile je vybrán typ, doplňte následující pole:

- Zatrhněte políčko „Likvidace nákupu“: Zapněte likvidace nákupů.
- :guilabel:`Používat dokumenty?“: Zapněte tuto volbu, pokud je v zemi povoleno daňové přiznání.
je použito, protože je to standardní konfigurace. Pokud ne, zvolte možnost záznamu účetnictví
vstupy nezpůsobené daňovým dokladem, jako jsou například faktury, platby daní nebo účetní záznamy
záznamy.
- :guilabel:`Příjemce emisí“: Zadejte číslo zařízení.
- :guilabel:`Výstupní bod“: Zadejte výstupní bod tiskárny.
- :guilabel:`Adresa emise“: Zadejte adresu zařízení.
- :guilabel:Krátký kód: Zadejte jedinečný pětidílný kód pro sekvenci účetních vstupů (např.
„PT001“.

V posledním kroku v záložce „Další nastavení“ zkontrolujte položku „Daňový doklad“.
zaškrtávací políčko pro zasílání faktur v XML/EDI formátu.

..._lokalizace/ekvádor/nákup-likvidace-založení:

Vytvořit nákupní likvidaci
*****************************

Likvidace nákupu vytvořené z objednávek nebo ručně ze faktur dodavatele musí obsahovat
následujících dat:

- :guilabel:Dodavatel: Zadejte informace o dodavateli.
- :guilabel:`Deník nákupu a likvidace“: Vyberte deník „Nákup a likvidace“ s tiskárnou
bod.
- :guilabel:`Dokumentní typ“: Zadejte tento dokumentový typ: „(03) Rozúčtování nákupu“.
- :guilabel:`Číslo dokumentu“: Zadejte číslo dokumentu (pořadí). Toto musí být zadáno pouze jednou.
a pořadí bude automaticky přiřazeno k následujícím dokumentům.
- :guilabel:`Způsob platby (SRI)`: Vyberte způsob, jakým chcete fakturu zaplatit.
- :guilabel:`Produkty“: Uveďte produkt s odpovídajícími daněmi.

Následně ověřte :guilabel:`Splatnost nákupu“.

..._lokalizace/ekvádor/nákupní srážka:

Srážka z kupní ceny
~~~~~~~~~~~~~~~~~~~~

„Souhrnné informace o nákupu“ jsou elektronické dokumenty, které se odesílají na SRI po jejich ověření.
jen v případě, že byla zaevidována na základě ověřené (zaslané) faktury.

V faktuře klikněte na položku „Srážka“ a vyplňte následující pole:
Okno „Zadržet“:

- :guilabel:`Číslo dokumentu“: Zadejte číslo dokumentu (pořadí). Toto musí být zadáno pouze jednou.
a sekvence bude automaticky přiřazena pro další dokumenty.
- :guilabel:„Zadržet řádky“: daně se automaticky zobrazí podle konfigurace
produkty a dodavatele. Zkontrolujte, zda jsou daně a podpora daní správné. Pokud ne, upravte a vyberte
správné daně a daňová podpora.

Poté ověřte: „Srážková daň“.

.. poznámka::
Druhy podpory daně musí být nakonfigurovány na faktuře dodavatele. Chcete-li tak učinit, přejděte
je aplikován na faktuře dodavatele a změna je provedena v položce „Dodací adresa“.

Srážková daň se dělí na dvě nebo více řádků podle počtu dvou nebo více
Použijí se sazby zadržení.

.. příklad::
Odoo navrhuje srážkovou daň ve výši 30 % s podporou DPH 01. Daň lze zvýšit na 70 %.
do nové řádky s tím samým daňovým zvýhodněním. Odoo umožní, pokud bude součet základu stejný
:guilabel:`Celková částka faktury dodavatele“

..._lokalizace/ekvádor/náklady na cestovné:

Vrácení nákladů
---------------------

Vracení nákladů se vztahuje na tyto případy:

- :guilabel:`Osoba“: náhrada zaměstnanci za různé výdaje (např. nákup
likvidace)
- :guilabel:`Právnická osoba“: náhrada nákladů vzniklých při zastupování


Aby bylo možné uhradit výdaje, zajistěte si vystavení :ref:`účetní deníku
Pro individuální nebo prodejce vytvořená složka „<localizations/ecuador/purchase-liquidation>“.
účetní kniha pro právnickou osobu (<localizations/ecuador/vendor-journal>).

.. poznámka::
V záznamu o fakturách dodavatelů se ujistěte, že jsou nastaveny následující nezbytné konfigurace pro právní
subjekt:

   - Vyberte „Koupit“ jako „Typ“.
   - Nepočítáme-li „Likvidace nákupu“, pak nezaškrtávejte tento políček.
   - Přidejte položku „Výchozí účet pro výdaje“.

Poté vytvořte náhradu za fakturu dodavatele:
Použijte knihu „Zrušení nákupu“ nebo „Faktura dodavatele“. Na faktuře dodavatele nastavte
následujících polích:

- :guilabel:`Dodavatel“: Tento prvek by měl být zaměstnancem.
- :guilabel:`Typ dokumentu“: Zkontrolujte, zda je tento prázdný prostor správně vyplněn z deníku.
- :guilabel:`Způsob platby (SRI)`: Vyberte způsob platby.
- Karta „Způsoby úhrady“: Klikněte na „Automaticky vyplnit řádky faktury“.
do faktury zadávat položky nebo přidávat výdaje postupně a poskytnout následující údaje pro
každou položku výdajů:

  - :guilabel:`Číslo partnera nebo číslo autorizace“
  - :guilabel:`Datum“
  - :guilabel:`Dokument typu“
  - :guilabel:`Číslo dokumentu“
  - :guilabel:`Základ daně“
  - :guilabel:`Daň“

Poté klikněte na tlačítko „Potvrdit fakturu dodavatele“ a „Zpracovat nyní“. Potvrzení faktury dodavatele
účet pro úhradu likvidace zásob a odpočet z této likvidace vzniklý.
Výpis z účtu dodavatele obsahuje informace o vrácení peněz.

.. obrázek: ecuador/l10n-ec-individual-flow.png
:alt:Vrácení nákladů.

... /ecuador/elektronické doručení průvodce:

Elektronická příručka pro doručování
-------------------------

Elektronický průvodce dodávkou v Ekvádoru je právní dokument, který podporuje přepravu
zboží nebo zboží mezi jednotlivými místy v rámci národního území. Vydává
odesílatel zboží a snaží se evidovat a zdůvodnit pohyb produktů, aby se vyhnul právním nebo daňovým
účetní požadavky, které jsou vyžadovány daňovým úřadem (SRI).

.. důležité::
Ujistěte se, že nainstalujete aplikaci „Ecuadorian“ z modulu „Aplikace“ v části „Obecné“.
Modul Průvodce dodávkou („l10n_ec_edi_stock“).

..._lokalizace/ekvádor/nákladní automobil:

Transporter
~~~~~~~~~~~

Nejprve vytvořte nový kontakt (přepravce) podle návodu:
a vyplňte kontaktní údaje jako „Společnost“. Ujistěte se, že následující pole jsou
kompletní:

- :guilabel:`Číslo identifikace“: Vyberte :guilabel:`RUC“ a zadejte číslo RUC dopravce.
- :guilabel:`Druh daňového poplatníka“: Vyberte „Firmy – Právnické osoby“ jako partnery
převést výpočet odvodů DPH do automatického režimu.

.. obrázek: ecuador/l10n-ec-carrier-contact.png
:alt: Konfigurace kontaktu s přepravcem.

... /lokalizace/ekvádor/soubor-certifikátu:

Certifikát pro SRI
~~~~~~~~~~~~~~~~~~~~~~~~

Pro nahrání certifikátu pro SRI přejděte na: „Účetnictví -> Konfigurace ->
Přejděte do sekce „Nastavení“ a klikněte na
:icon:`oi-arrow-right` :guilabel:`Certifikáty SRI“ v sekci :guilabel:`Připojení SRI“. Pak
Vytvořit nový certifikát klikněte na tlačítko „New“ a vyplňte následující pole:

- :guilabel:`Název certifikátu`: Název certifikátu.
- :guilabel:`Soubor s certifikátem“: Pomocí tlačítka „Nahrát soubor“ nahrajte SRI.
certifikát.
- :guilabel:`Heslo certifikátu“: Zahrňte heslo k dešifrování souboru PKS, pokud je požadováno.

Jakmile je certifikát vytvořený, klikněte na tlačítko „Nastavení“ a přejděte zpět do nastavení a zkontrolujte
certifikát se vybere v poli „Soubor certifikátu pro SRI“ a v poli „Použít
zaškrtnuto je políčko pro produkční servery.

..._lokalizace/ekvádor/konfigurace skladu:

Konfigurace skladu
~~~~~~~~~~~~~~~~~~~~~~~

Nejprve je třeba vytvořit nový sklad.
<../../inventar-und-mrp/Inventar/Lager/Warenwirtschaft/Lager>.
sledující data pro každou skladovnu, která generuje elektronickou dodací příručku:

- :guilabel:`Entita bodu“: číslo emisní entitě udělené SRI
- :guilabel:`Místo emise“: číslo místa emise uvedené v SRI
- „Další číslo pro sledování zásilky“: číslo pro sledování přepravy (upravitelné po prvním
(tedy zachování skladu).

..._lokalizace/ekvádor/vygenerovat elektronickou dodávku:

Vytvořit elektronickou průvodku dodávkou
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Jednou za čas je nutné provést dodání.
v průběhu prodejního procesu vytváříme zásoby a ujistěte se, že jsou vyplněny následující pole
sekci „Průvodce dodáním“ v záložce „Příplatky“:

- :guilabel:`Dodavatel“: Zadejte kontakt zadaný v části „Kontakty“.
- :guilabel:`Registrační značka“: Zadejte registrační značku vozidla.
- :guilabel:`Důvod převodu“: Výchozí hodnota je „Odeslání zboží“, upravte podle potřeby.
- :guilabel:`Datum zahájení“: Automaticky nastaveno na datum vytvoření (upravitelné).
- :guilabel:`Datum ukončení“: Automaticky nastaveno na 15 dní po datu zahájení (upravitelné).

.. obrázek: ecuador/l10n-ec-delivery-guide-settings.png
:alt: Nastavení doručovacího průvodce.

Klikněte na tlačítko „Přidat“, pak na „Zkontrolovat“ a nakonec na „Vytvořit průvodce dodáním“.
informace bude k dispozici v sekci „Průvodce dodáním“:

- :guilabel:`Datum schválení“: datum, kdy vláda dokument schválila.
- :guilabel:`Číslo autorizace“: Autorizační číslo EDI (stejné jako přístupový klíč).
- :guilabel:`Stav dodacího průvodce“: stav dodacího průvodce.

... obrázek: ecuador/l10n-ec-authorization-number.png
:alt: Autorizační číslo.

Pro zaslání XML a PDF lze poslat e-mail na kontakt uvedený v poli :guilabel:`Dodací adresa
Pole „Adresa“ - tento krok je volitelný a provádí se ručně. Tlačítko „Odeslat e-mail“ potřebuje
kliknutí.

.. obrázek: ecuador/l10n-ec-delivery-guide-pdf.png
:alt: Průvodce dodáním ve formátu PDF.

..._lokalizace/ekvádor/e-commerce:

e-commerce
=========

Modul ATS Report umožňuje následující:

- Vyberte způsob platby SRI pro každou konfiguraci platebního nástroje.
- Zákazníci mohou během nákupu na internetu zadat své identifikační číslo a typ.
- Vygenerovat automaticky platnou elektronickou fakturu pro Ekvádor na konci procesu objednávky.

.. viz též:
:doc:`Dokumentace e-commerce <../../websites/ecommerce>`

..._lokalizace/ekvádor/on-line-platby:

Online platby
---------------

Pro možnost provádět platby online přidejte příslušného poskytovatele platebních služeb (dokument:platební metody).
konfigurovat potřebné platební metody (<payment_providers/payment_methods>) a je nutností.
zaškrtnout pole „Metoda platby SRI“ pro každý způsob platby.

.. poznámka::
Přidání :guilabel:`SRI platební metody` je nutné k tomu, aby se správně vygeneroval elektronický
faktura z prodeje přes internet. Vyberte způsob platby, abyste se dostali do nastavení platební metody
pole.

..._lokalizace/ekvádor/faktura-bez-přijetí:

Automatická faktura
-----------------

Faktury lze vytvářet po dokončení procesu objednávky.

.. tip::
E-mailový vzor faktury lze upravit v poli „Vzor e-mailu pro fakturu“
pod volbou „Automatická faktura“.

.. důležité::
Pro fakturaci se používá první prodejní deník v pořadí priorit.
:guilabel:`Časopis“ nabídka.

... /ekvádor/ecommerce-workflow:

Typ a číslo identifikace
------------------------------

Během procesu platby bude mít klient možnost uvést své
identifikační typ a číslo. Tato informace je nutná pro vytvoření elektronické faktury
Po správném dokončení nákupu.

.. poznámka::
Kontrola je prováděna za účelem ověření, zda pole „Identifikační číslo“ bylo vyplněno a má
správný počet číslic. Pro identifikaci RUC je nutných 13 číslic a pro ceduli 9
jsou požadovány číslice.

Po dokončení procesu placení je vytvořen potvrzený daňový doklad, který lze odeslat ručně nebo
asynchronně k SRI.

..._lokalizace/ekvádor/prodejní místo:

Elektronické fakturace na prodejním místě
==================================

Ujistěte se, že modul pro obchodní místo („l10n_ec_edi_pos“) je nainstalován.
, abyste mohli využít následující funkce a konfigurace:

- Vyberte platební metodu SRI v každém nastavení platební metody.
- Při vytváření nového kontaktu na POS zadejte ručně typ a číslo identifikace zákazníka.
- Vygenerovat automaticky platnou elektronickou fakturu pro Ekvádor na konci procesu objednávky.

..._lokalizace/ekvádor/konfigurace platebního metodu:

Konfigurace platebního metody
----------------------------

Vytvořit platební metodu pro bod prodeje <../../sales/point_of_sale/payment_methods>.
Přejděte na „Prodejní místo --> Konfigurace --> Způsoby platby“. Pak nastavte
V poli platebního nástroje zadejte „SRI Payment Method“.

... /lokalizace/ekvádor/fakturace:

Fakturační toky
---------------

… /ecuador/identifikace-typ-cislo:

Typ a číslo identifikace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokladní P0S může vytvořit nový kontakt pro zákazníka, který požaduje
faktura z otevřené pokladny.

Modul Ecuadorian Module for Point of Sale přidává do formuláře pro vytvoření kontaktu dvě nové pole:
:guilabel:`Typ identifikace“ a „Daňové identifikační číslo“.

.. poznámka::
Protože délka identifikačního čísla se liší podle typu identifikace, Odoo
automaticky kontroluje pole „Daňové identifikační číslo“ při ukládání kontaktního formuláře.
zajistit správnou délku, vědět, že typy „RUC“ a „Občanství“
V případě kreditní karty je nutné zadat 16 číslic a u debetní karty 8 číslic.

.._lokalizace/ekvádor/anonymní konečný spotřebitel:

Elektronická faktura: anonymní konečný spotřebitel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Když klienti nepožádají o elektronickou fakturu za nákup, Odoo automaticky nastaví
zákazníkovi jako:guilabel:`Konečný spotřebitel`, a vystaví mu elektronickou fakturu stejně.

.. poznámka::
Pokud si klient vystaví fakturu kvůli vrácení zboží tohoto typu, bude mu vystavená faktura.
měly být vystaveny na základě skutečných kontaktních údajů klienta. Kreditní poznámky nelze vystavovat pro
*Konečný spotřebitel* a může být spravován přímo z režimu POS session (viz <pos/refund>).

..._lokalizace/ekvádor/specifický zákazník:

Elektronická faktura: specifický zákazník
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud zákazník požádá o fakturu za svůj nákup, je možné vybrat nebo vytvořit kontakt.
s daňovými informacemi. To zajišťuje, že faktura bude vystavena s přesnými údaji o zákazníkovi.

.. poznámka::
Pokud si klient vystaví fakturu kvůli vrácení zboží tohoto typu, bude mu vystavená faktura.
a proces vrácení může být řízen přímo z relace POS:ref:`<pos/refund>`.
