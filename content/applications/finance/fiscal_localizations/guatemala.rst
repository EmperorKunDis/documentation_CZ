=========
Guatemala
=========

.. |SAT| nahradit za: :abbr:`SAT (Superintendencia de Administración Tributaria)`
.. |EDI| nahradit za: zkratka: `EDI (Elektronický výměnný obchod)`
.. |UUID| nahradit za: zkratku UUID (Univerzální jedinečný identifikátor)

.. _guatemala/intro:

Úvod
============

S guatemalskou lokalizací můžete přistupovat k daňovému úřadu Superintendencia de
Generovat elektronické dokumenty pomocí svého XML, fiskálního listu a
elektronickou značku.

Podporované dokumenty jsou:

- :guilabel:`Faktura - faktura“,
- :guilabel:`Faktura měnící se“,
- :guilabel:`Faktura pro malého plátce DPH“,
- :guilabel:`Poznámka k úvěru - NCRE“,
- :guilabel:`Faktura k úhradě“,
- :guilabel:`NABN - Předplatné“
- :guilabel:`Faktura pro malého plátce DPH“,
- :guilabel:`Faktura s exportním doplňkem“.

Pro místní lokalizaci je nutný účet „Infile“ <https://infile.com.gt/>, který umožňuje uživatelům
vytvářet elektronické dokumenty v rámci systému Odoo.

.. viz též:
:doc:`Dokumentace o právní platnosti a dodržování předpisů vztahujících se na fakturaci elektronickou v Guatemale


Pojmy
--------

Ve všech guatemalských lokalizacích jsou používány následující termíny:

- **SAT**: Superintendencia Nacional de Administración Tributaria je vládní agentura, která má na starosti
vymáhání daní v Guatemale.
- **FEL**: Systém elektronické fakturace na dálku (Factura Electrónica en Línea) je povinný pro SAT
Guatemala, kde podniky musí vydávat a spravovat elektronické dokumenty v souladu s
místní předpisy.
- **EDI**: Elektronický výměnný obchod je označení pro zasílání elektronických dokumentů.
- **Infile**: je třetí stranou, která usnadňuje elektronickou výměnu informací.
dokumenty mezi společnostmi a guatemalskou vládou.
- **UUID**: unikátní alfanumerický kód přidělený SAT
každý ověřený elektronický dokument v systému FEL používaném pro sledovatelnost a oficiální
validace.
- **Slova a fráze**: Typy slovních spojení s konkrétními kódy scénářů se používají v guatemalské lokalizaci
aby vyhověly požadavkům SAT. Tyto položky se přidávají podle režimu emitenta
příjemce a typ operace. Tyto fráze se používají v dokumentech XML a PDF.
- Kód zřízení: Jedinečný identifikátor přidělený SAT každé podnikatelské instituci
která je pro elektronické fakturace nutná.
- Květákový kvintet: Oficiální měna Guatemaly, reprezentovaná symbolem GTQ. Tento je základní
měnou pro všechny finanční transakce v guatemalské lokalizaci.

Konfigurace
=============

Instalace modulů
--------------------

:ref:`Nainstalujte následující moduly, abyste získali všechny funkce guatemalského
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 25 25 50

   * Jméno
     - Technické označení
     - Popis
   * --:guilabel:`Guatemala - Účetnictví“
     - „l10n_gt“
     - Výchozí balíček pro daňovou lokalizaci <../fiscal_localizations>. Přidává účetnictví
charakteristiky pro guatemalskou lokalizaci, které představují minimální konfiguraci
požadované pro provozování společnosti v Guatemale podle směrnic stanovených SATem.
Instalace modulu automaticky načte účetní knihu a daně.
   * --:guilabel:`Účetnictví Guatemaly EDI“
     - „l10n_gt_edi“
     - Zahrnuje všechny technické a funkční požadavky na generování a ověření
:dokument: „Dokumenty elektroniky <../účetnictví/fakturace zákazníků/elektronická fakturace>“ na základě
technické dokumentace zveřejněné na stránkách SAT. Seznam povolených dokumentů je uveden v sekci
nad textem <guatemala/intro>.

.. poznámka::
V případě, že je databáze vytvořena, Odoo automaticky nainstaluje základní modul **Guatemala - Účetnictví**.
nainstalované s vybranou zemí Guatemala. Aby však bylo možné elektronické fakturace, je nutné
Modul **Účetnictví Guatemaly (l10n_gt_edi)** musí být ručně nainstalován.
<obecné/instalace>.

Společnost
-------

Pro konfiguraci informací o společnosti otevřete aplikaci **Nastavení**, posuňte se dolů a vyberte
V sekci „Společnosti“ klikněte na „Aktualizovat informace“, a nakonfigurujte následující:

- :guilabel:`Název společnosti“
- včetně ulice, města, státu
:guilabel:`Zip“, a :guilabel:`Stát“
- :guilabel:`Daňové identifikační číslo“: Zadejte identifikační číslo pro vybraný typ poplatníka.
- :guilabel:`Daňové přiznání“: Zvolte daňovou příslušnost společnosti, která je typem
Řízený společností.
- :guilabel:`Právní název společnosti“: Právní název společnosti používaný v XML a PDF dokumentech.
- :guilabel:`Kód zřízení“: Nutná součást XML při vytváření elektronického dokumentu.
Pokud tento údaj nebude vyplněn, všechny elektronické dokumenty budou zamítnuty.

Zjistit kód „Establishment“ ve svém účtu SAT na adrese https://portal.sat.gob.gt/
Vyberte položku „FEL --> Správa zařízení“. Seznam registrovaných
Zobrazují se i příslušné kódy.

.. důležité::
Po nastavení společnosti v sekci Nastavení databáze přejděte na kontaktní formulář společnosti.
a ověřit, že číslo identifikace je nastaveno na typ NIT.

Elektronické fakturační kreditní karty
--------------------------------

V Guatemale je elektronické fakturace povinná pro většinu podniků. Odoo se připojuje k
autorizovaný poskytovatel Infile, aby vytvořil a podal elektronické dokumenty k SAT
Validace.

Před vydáním elektronických dokumentů musíte konfigurovat a propojit Odoo s Infilem, abyste zajistili
jsou řádně ověřeny a přidělena oficiální |UUID|.

Infile
~~~~~~

Zaregistrujte se na stránkách společnosti „Infile“ <https://infile.com.gt/> a podepište s ní služební smlouvu.
Potřebné kreditní údaje pro vložení do Odoo.

Odoo
~~~~

V Odoo po dokončení procesu Infile přejděte na:
Konfigurace --> Nastavení“, posuňte se dolů do části „Guatemalská lokalizace“ a
Postupujte takto:

#Vyberte prostředí „Webové služby Infile“, buď „Test“ nebo
:guilabel:`Výroba“.
#Vložte:guilabel:Infile Credentials:

   - :guilabel:`Jméno uživatele nebo předpona souboru WS“
   - :guilabel:`Token v souboru“
   - :guilabel:`Záložní klíč“

#Klikněte na tlačítko „Uložit“.

.. poznámka::
Kreditní údaje Infile jsou poskytovány společností Infile a jsou nutné pro test i produkční verzi.
výrobní prostředí. Pokud nejsou k dispozici, kontaktujte podporu Infile.

.. tip::
Demoverze je určena pouze pro testování a negeneruje žádné právní dokumenty, klíče UUID ani
fiskální složky. K použití demoverze není potřeba účet Infile ani přihlašovací údaje.

Mnoho měn
~~~~~~~~~~~~~~

Oficiální směnný kurz v Guatemale je stanoven Bankou Guatemaly. Odoo může
Připojit se přímo k jeho službám a získat směnný kurz buď automaticky nebo ručně.

.. viz též:
:doc:`Mnoho měn <../accounting/get_started/multi_currency>`

Hlavní data
-----------

Klasifikační schéma
~~~~~~~~~~~~~~~~~

:doc:`Účetní kniha <../accounting/get_started/chart_of_accounts>` je nainstalována výchozím nastavením
Do sady dat zahrnutých v modulu lokalizace jsou pak účty přidány.
automaticky v daních, pohledávkách a závazcích.

Účty lze přidávat nebo mazat podle potřeby společnosti.

Kontakty
~~~~~~~~

V kontaktních formulářích je nutné vyplnit následující pole:

- :guilabel:`Název společnosti“
- včetně ulice, města, státu
:guilabel:`Zip“, a :guilabel:`Stát“
- :guilabel:`Číslo identifikace“:

  - :guilabel:`Typ identifikace“: vyberte typ identifikace.
  - :guilabel:`Číslo“: Požadováno k potvrzení elektronické faktury.

.. poznámka::
automaticky do XML a PDF každé elektronické faktury zahrnout konkrétní frázi
Kontakt vyberte v poli „Vybrané fráze“ na záložce „Prodej a nákup“.
kontaktní formulář.

Daně
~~~~~

Jako součást modulu lokální Guatemaly jsou automaticky vytvářeny daně s jejich konfigurací
a související finanční účty.

Elektronické faktury
===================

Jakmile je databáze úspěšně nakonfigurována, mohou být vytvořeny a odeslány elektronické dokumenty.

Jakmile jsou faktury zákazníků <../accounting/customer_invoices> ověřeny, mohou být odeslány.
elektronicky na SAT přes Infile s vyplněnými následujícími poli:

- :guilabel:`Zákazník“: Zadejte informace o zákazníkovi.
- :guilabel:`Typ dokumentu GT“: vyberte typ dokumentu, který chcete vytvořit, například
:guilabel:`Faktura elektronická“ nebo :guilabel:"Faktura pro změnu“. Výchozí hodnotou je
typ dokumentu je nastaven na :guilabel:`FACT`.
- :guilabel:`Datum splatnosti“: Vypočítá, zda je faktura v současné době splatná nebo ne.
- :guilabel:`Prodejní kniha“: Vyberte prodejní knihu.
- :guilabel:`Produkty“: Uveďte produkt (produkty) se správnými daněmi.

Po dokončení klikněte na tlačítko „Potvrdit“.

.. poznámka::
Pokud potřebujete přidat konkrétní frázi na základě transakce, přejděte do :guilabel:`Další informace`.
záložku a přidat odpovídající frázi do :guilabel:`GT Phrases“. Tyto fráze se používají v XML
a dokumenty ve formátu PDF.

.. poznámka::
Pokud potřebujete ke faktuře přidat dodatek, můžete tak učinit v položce :guilabel:`Obchodní podmínky.
pole podmínek. Příloha bude součástí XML dokumentu a může být použita k poskytnutí
další informace nebo poznámky k faktuře.

Po potvrzení faktury klikněte na tlačítko „Odeslat“. V zobrazeném průvodci zkontrolujte
Zapněte zaškrtávací políčka „Odeslat do SAT“ a „E-mailem“, abyste mohli odeslat XML do SAT.
prostřednictvím webové služby Infilu a faktury s platnou doložkou k e-mailovému účtu klienta.
„Odeslat“. Následně se zobrazí následující obrazovka:

- Vytvoří se XML dokument.
- Vytvoří se UUID.
- XML se zpracovává souběžně pomocí Infile.

  - Pokud je soubor přijat, zobrazí se v chatu a klientovi bude zaslán e-mail s
Odesílá se soubor :file:`pdf` a :file:`xml`.
  - Pokud soubor obsahuje chyby, zobrazí se varovné hlášení s důvodem (důvody) a e-mail nebude odeslán.

.. obrázek: guatemala/pdf-xml-chatter-guatemala.png
:alt:Elektronické dokumenty k dispozici v chatovacím okně.

V položce „SAT“ se pak zobrazí následující:

- :guilabel:`Datum a časová značka“: Časové razítko uložené při vytváření XML.
- :guilabel:`GT Status“: Stav výsledku získaného v odpovědi SAT. Pokud soubor obsahuje chyby,
Pokud je zpráva varovná, zobrazí se důvod(y) a e-mail nebude odeslán.
- :guilabel:`UUID“: Jedinečný identifikátor přidělený elektronickému dokumentu |SAT|.
- :guilabel:`Stáhnout certifikát“: Stáhnout odeslaný XML soubor i v případě, že výsledek byl
byla zamítnuta.

.. obrázek: guatemala/sat-tab-elektronicka-dokumentace.png
:alt:Dokument EDI je k dispozici v záložce SAT.

..._lokalizace/guatemala/platební poznámky:

Dodací a fakturační listy
----------------------

Chcete-li odeslat fakturu nebo kreditní poznámku do Infile, nejprve vytvořte
<účetnictví/přijaté faktury/vystavení debetní poznámky> nebo :ref:`pozvánka na debet
<účetnictví/vystavení kreditní faktury/>.

Poté klikněte na tlačítko „Odeslat do SAT (Guatemalský EDI)“ v okně „Odeslat“.
pro reálné ověření. Po úspěšném ověření je do
fakturu v PDF.

Exportní faktury
---------------

Exportní faktury musí splňovat následující podmínky:

- Typ identifikace zákazníka musí být „DPH“, „Občanský průkaz“ nebo
:guilabel:`Zahraniční identifikace“.
- V následujících polích musí být definován zákaznický fakturační doklad v záložce „Další informace“ pod
v sekci „Účetnictví“:

   - :guilabel:`Incoterms“
   - :guilabel:`GT Phrases“: :guilabel:`Typ 4 kód 1“
   - :guilabel:`Dodavatelská společnost“

- Všechny řádky faktury musí obsahovat daně nastavené na 0 %.

.. obrázek: guatemala/l10n-gt-faktura-zadavatele.png
:alt: Hlavní údaje exportního faktury.
