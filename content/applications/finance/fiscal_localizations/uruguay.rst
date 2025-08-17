=======
Uruguay
=======

.. |DGI| nahradí za: zkratka: DGI (Dirección General Impositiva)
.. |EDI| nahradit za: zkratka: `EDI (Elektronický výměnný obchod)`
.. |CAE| nahrazuje: zkratka `CAE (Certificado de Autorización de Emisión)`

.. _uruguay/intro:

Úvod
============

S uruguayskou lokalizací můžete vytvářet elektronické dokumenty s jeho XML, fiskálními údaji.
elektronickou podpis a připojení k finančnímu úřadu Dirección General Impositiva (DGI).
Uruware.

Podporované dokumenty jsou:

- „Faktura elektronicky“, „Kreditní faktura elektronicky“ a „Debetní faktura elektronicky“.
- :guilabel:`Elektronický lístek“, „Elektronická faktura“, „Elektronický debetní doklad“
- :guilabel:`Export faktury v elektronické podobě“, :guilabel:`Export kreditní faktury v elektronické
e-Faktura Debetní Dodatek.

Lokalizace vyžaduje účet u Uruwary, který umožňuje generovat elektronické dokumenty
v rámci Odoo.

.. viz též:
:doc:`Dokumentace o zákonnosti a souladu s předpisy v Uruguayi


Pojmy
--------

V uruguayské lokalizaci jsou používány následující termíny:

- **DGI**: *Dirección General Impositiva* je vládní organizace, která dohlíží na dodržování daní.
platby v Uruguayi.
- **EDI**: Elektronický výměnný obchod je označení pro zasílání elektronických dokumentů.
- **Uruware**: je třetí stranou, která usnadňuje elektronickou výměnu
dokumenty mezi společnostmi a uruguayskou vládou.
- **CAE**: *Doklad o udělení emisního povolení* je dokument, který požaduje finanční úřad.
webové stránky pro vystavování elektronických faktur.

Konfigurace
=============

Instalace modulů
--------------------

:ref:`Nainstalujte moduly <general/install> a získáte všechny funkce uruguayského
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 25 25 50

   * Jméno
     - Technické označení
     - Popis
   * – Uruguay – Účetnictví
     - „l10n_uy“
     - Výchozí balíček pro daňovou lokalizaci <../fiscal_localizations>. Přidává účetnictví
charakteristiky pro uruguayskou lokalizaci, které představují minimální konfiguraci
požadované pro podnikání v Uruguayi podle pokynů stanovených DGI.
Instalace modulu automaticky načte: účetní knihu, daně, typy dokumentů a
daně podporované typy.
   * --:label:Účetnictví Uruguay EDI
     - „l10n_uy_edi“
     - Zahrnuje všechny technické a funkční požadavky na generování a ověření
:dokument: „Dokumenty elektroniky <../účetnictví/fakturace zákazníků/elektronická fakturace>“ na základě
technických dokumentací zveřejněných DGI. Seznam povolených dokumentů je uveden v sekci
nad Uruguayí.

.. poznámka::
Odoo automaticky nainstaluje základní modul **Účetnictví – Uruguay** při instalaci databáze
s výběrem země „Uruguay“. Aby však bylo možné elektronické fakturace, je nutné v nastavení **Uruguay
Modul účetního EDI (**`l10n_uy_edi`) musí být ručně nainstalován podle odkazu :ref:`instalace <general/install>`.

Společnost
-------

Pro konfiguraci informací o společnosti otevřete aplikaci **Nastavení**, posuňte se dolů a vyberte
V sekci „Společnosti“ klikněte na „Aktualizovat informace“, a nakonfigurujte následující:

- :guilabel:`Název společnosti“
- včetně ulice, města, státu
:guilabel:`Zip“, a :guilabel:`Stát“
- :guilabel:Daňové identifikační číslo: zadejte identifikační číslo pro vybraný typ poplatníka.
- :guilabel:`Hlavní kód pobočky DGI“: tento je součástí XML při vytváření elektronického dokumentu. Pokud
Pokud je tento údaj nevyplněný, budou všechny elektronické dokumenty zamítnuty.

Chcete-li najít DGI hlavní kód pobočky, postupujte takto:

  #Otevřete si účet DGI („Účet DGI <https://servicios.dgi.gub.uy/serviciosenlinea>“).
:menu_selection:`DGI online služby --> Jednotný daňový registr --> Vyhledávání dat“.
  #Vyberte možnost menu „Registrační údaje - Výpis dat o subjektech“.
  #Otevřete vygenerovaný PDF a získáte hlavní kód pobočky DGI z pole „Domicilio Fiscal“ (položka „Guia Label“).
část „Číslo místnosti“.

Po nastavení společnosti v sekci „Nastavení databáze“ přejděte do části :menuselection:`Kontakty“.
Vyhledejte svou společnost a ověřte následující:

- typ společnosti je nastaven na „Společnost“.
- identifikační číslo: guilabel: Identifikace čísla: guilabel: Typ je: guilabel: RUT/RUC.

... _l10n_uy/uruware-account:

Vytvořte si účet na Uruware
------------------------

Chcete-li si založit účet na Uruware, postupujte podle těchto kroků:

#Zkontrolujte, zda máte platnou předplatnou Odoo.
#Najděte nastavení přihlašovacích údajů Uruware, když se dostanete na:
Konfigurace --> Nastavení.
#. Projděte dolů do sekce „Uruguayská lokalizace“ a vyberte prostředí
(nebo :guilabel:`Produkce“ nebo :guilabel:`Testování“).
#Klikněte na tlačítko „Vytvořit účet Uruware“.

Při tomto kroku je odesláno e-mailové upozornění na adresu spojenou s vaším předplatným Odoo.
heslo, které vám umožní přihlásit se do portálu společnosti Uruware a založit si účet.

.. tip::
  - E-mail s přihlašovacími údaji není okamžitý, může trvat až 48 hodin, než se účet
vzniknout.
  - Firma musí mít nastavené „Daňové identifikační číslo“ (Guilabel), aby mohla vytvořit účet na Uruwaru.
  - Heslo zaslané e-mailem má platnost 24 hodin. V tomto případě si heslo obnovte pomocí funkce *Zapomenuté heslo*.
odkaz na portál Uruware.

.. poznámka::
Toto jednání vytvoří účet na Uruware s následujícími informacemi:

   - Legální jméno (razón social)
   - RUT od firmy
   - Uživatelské jméno (e-mailová adresa pro odběr nebo například „RUT“.odoo“; např. „213344556677.odoo“)
   - Odkaz na databázi Odoo

Pro správné vytvoření vašeho účtu prosím doplňte chybějící informace shora.

Jakmile je účet vytvořen a dostanete e-mail s přihlašovacími údaji, zkontrolujte
účty přímo v testovacím portálu Uruware „Testing Portal“ <https://odootest.ucfe.com.uy/Gestion/>_.
„Produkční portál <https://prod6109.ucfe.com.uy/Gestion/>“:

Přihlaste se pomocí údajů o uživatelském účtu v e-mailu do odpovídajícího („Test
<https://odootest.ucfe.com.uy/Gestion/> nebo <https://prod6109.ucfe.com.uy/Gestion/>
portál.

V portálu Uruware je potřeba provést následující kroky, aby bylo možné vystavovat faktury z Odoo:

#Dokončete a opravte informace o společnosti.
#Přidejte svůj digitální certifikát.
#Přidejte své CAE (Certifikát o autorizaci k vydání) pro každý dokumentový typ, který plánujete
vydat.
#Nastavte formát PDF, který chcete vytisknout a zaslat svým zákazníkům.

.. důležité::
Ujistěte se, že máte dvě účty, jeden pro testování a druhý pro produkci. Certifikát je
Pro oba prostředí je potřeba CAE (Certificate of Authorization for Emission), ale jen pro jedno z nich.
potřebné pro výrobu.

.. viz též:
   - Tutoriály Odoo: Uruguayská lokalizace

   - „Fórum Odoo pomoci: Uruguay
<https://www.odoo.com/forum/help-1?search=l10n_uy>

Elektronická data faktury
-----------------------

Konfigurovat údaje elektronické faktury je potřeba nakonfigurovat prostředí a přihlašovací údaje.
Projděte si sekci „Účetnictví“ - „Konfigurace“ - „Nastavení“ a přejeďte dolů k
:guilabel:`Lokalizace Uruguay“

Nejprve vyberte prostředí UCFE Web Services:

- :guilabel:`Produkce“: pro produkční databáze. V tomto režimu jsou elektronické dokumenty odesílány na
|DGI| prostřednictvím společnosti Uruware pro jejich ověření.
- :guilabel:`Testování“: pro testovací databáze. V tomto režimu lze otestovat přímé toky dat.
s daty, které byly zaslány do testovacího prostředí DGI přes Uruware.
- :guilabel:`Demo“: soubory se vytváří a přijímají automaticky v režimu demo, ale nejsou odeslány
do |DGI|. Proto se v tomto režimu nezobrazí chyby při odmítnutí. Každá interní
ověření lze otestovat v režimu demo. V produkčním systému se tato volba nedoporučuje.

.. poznámka::
Používání režimu Demo nevyžaduje účet u Uruware.

Poté zadejte :guilabel:`Uruware Data`:

- :guilabel:`Uruware WS Password“
- :guilabel:`Obchodní kodex“
- :guilabel:`Kód terminálu“

.. obrázek: uruguay/elektronické fakturační údaje.png
:alt:Povinné údaje pro elektronickou fakturu.

.. poznámka::
Tyto údaje lze získat na portálu Uruware po konfiguraci :ref:`Uruwarového účtu
<l10n_uy/uruware-account>.

Chcete-li získat heslo Uruware WS, přejděte na:
Editovat a hledat záložku „Validátory a další informace“.
:guilabel:`Heslo WS“.

Chcete-li získat „Obchodní kód“, přejděte na „Konfigurace“ -> „Branch“.

Pro získání kódu terminálu přejděte do nabídky „Konfigurace“ a poté na „Bod výdeje“.

Hlavní data
-----------

Klasifikační schéma
~~~~~~~~~~~~~~~~~

:doc:`Účetní kniha <../accounting/get_started/chart_of_accounts>` je nainstalována výchozím nastavením
Do sady dat zahrnutých v modulu lokalizace jsou pak účty přidány.
automaticky v daních, pohledávkách a závazcích.

Účty lze přidávat nebo mazat podle potřeby společnosti.

.. viz též:
:doc:`../účetnictví/začínáme/rozvaha“

Kontakty
~~~~~~~~

Pro vytvoření kontaktu přejděte do aplikace Kontakty a vyberte možnost „Nový“.
zadat následující informace:

- :guilabel:`Název společnosti“
- :guilabel:`Adresa“:

  - :guilabel:`Ulice“: vyžadováno k potvrzení elektronické faktury.
  - :guilabel:`Město“
  - :guilabel:`Stát“
  - :guilabel:`ZIP“
  - :guilabel:`Země“: vyžadováno k potvrzení elektronické faktury.

- :guilabel:`Číslo identifikace“:

  - :guilabel:`Typ identifikace“: vyberte typ identifikace.
  - :guilabel:`Číslo“: vyžaduje potvrzení elektronické faktury.

Daně
~~~~~

Jako součást uruguayské lokalizační modulu se automaticky vytváří daň s její konfigurací
a související finanční účty.

.. obrázek: uruguay/dane.png
:alt:Dani pro Uruguaj.

Druhy dokumentů
~~~~~~~~~~~~~~

Některé účetní transakce, jako například faktury zákazníkům a dodavatelské faktury jsou klasifikovány podle dokumentu.
typy. Tyto jsou definovány vládními finančními úřady, v tomto případě DGI.

Každému typu dokumentu lze přiřadit jedinečný pořadí v daném časopise. Data jsou vytvářena
automaticky při instalaci lokální modul a informace potřebné pro
Typy dokumentů jsou zahrnuty výchozí hodnotou.

Zkontrolovat typy dokumentů zahrnuté v lokalizaci, přejděte na:
--> Konfigurace --> Druhy dokumentů“.

.. poznámka::
V Uruguayi musí být |CAE| nahrány do Uruware. Sekvence (a PDF) jsou přijímány v Odoo
z Uruwary na základě jejich CAE. CAE se používají jen v produkci. Testovací verze obsahují pouze
musí být nastaven rozsah sekvencí používaných v Uruwaru.

.. obrázek: uruguay/dokumenty.png
:alt: Druhy dokumentů pro Uruguay.

Prodejní knihy
~~~~~~~~~~~~~~

Vytvořit a potvrdit elektronický dokument, který bude ověřen |DGI|, obchodním deníkem
je nutné konfigurovat následovně:

- Výchozí nastavení položky „Druh fakturace“ je „Elektronická“. Toto je nutné, aby
posílat elektronické dokumenty prostřednictvím webové služby na uruguayskou vládu přes Uruware.
volba, :guilabel:`Manuální“, je pro otevřené faktury, které byly dříve razítkovány v jiném systému.
příkladu v DGI.
- :guilabel:`Používat dokumenty?“: Zapněte tuto možnost, pokud se v tomto časopise budou používat dokumenty z uvedeného seznamu.
z dokumentů v Odoo.

Průběh práce
=========

Jakmile si nastavíte databázi, můžete vytvářet své dokumenty.

Prodejní dokumenty
---------------

Faktury zákazníků
~~~~~~~~~~~~~~~~~

:doc:`Faktury zákazníků <../účetnictví/faktury_zákazníků>` jsou elektronické dokumenty, které se
ověřené jsou zasílány do DGI prostřednictvím Uruwaru. Tyto dokumenty lze vytvořit z vaší objednávky nebo
ručně. Musí obsahovat následující údaje:

- :guilabel:`Zákazník“: zadejte informace o zákazníkovi.
- :datum splatnosti: vypočítá, zda je faktura splatná nyní nebo později (dluh nebo kredit).
respektive).
- :guilabel:`Časopis“: vyberte elektronický prodejní časopis.
- :guilabel:`Dokumentní typ“: Dokumentový typ v tomto formátu například „(111) faktura elektronicky“.
- :guilabel:`Produkty“: specifikujte produkt (produkty) s platnými daněmi.

.. poznámka::
Každý dokumentový typ má svůj specifický kreditní a debetní doklad (např.
:guilabel:`(111) Daňový doklad v elektronické podobě“ má :guilabel:`(112) Dodatečný daňový doklad v elektronické podobě“.

Kreditní účet zákazníka
~~~~~~~~~~~~~~~~~~~~

:doc:`Faktura k úhradě zákazníkovi <../accounting/customer_invoices/credit_notes> je elektronická
dokument, který je po ověření odeslán na DGI prostřednictvím Uruwary. Je nutné mít ověřený
(vystavte) fakturu pro zaregistrování kreditní poznámky. Na faktuře klikněte na tlačítko „Kreditní poznámka“
přejděte na stránku „Vytvořit fakturu“ a vyplňte následující informace:

- :guilabel:`Důvod kreditní faktury“: zadejte důvod pro vystavení kreditní faktury.
- :guilabel:`Časopis“: vyberte časopis, který má být elektronický a má nastavené :guilabel:`Použití
Dokumenty?“
- :guilabel:`Dokument typu“: vyberte typ faktury.
- :guilabel:`Datum obratu“: zadejte datum.

Dodací list kupujícího
~~~~~~~~~~~~~~~~~~~

„Faktura pro odběratele“ (viz dokumentace „Faktura pro odběratele“) je elektronická
dokument, který je po ověření odeslán na DGI prostřednictvím Uruwary. Je nutné mít ověřený
(vystavte) fakturu pro registraci záporného dokladu. Na faktuře klikněte na ikonku
ikonu „akční nabídka“ (:guilabel:`akční nabídka`), vyberte možnost „Dodací list“ a přejděte na
Vyplňte následující informace v dialogovém okně „Vytvořit kreditní fakturu“:

- :guilabel:`Důvod“: Zadejte důvod pro vystavení poznámky k účtu.
- :guilabel:`Časopis“: Vyberte časopis, který má být elektronický a má nastavené :guilabel:`Použít
Dokumenty?“
- :guilabel:`Kopírovat řádky faktury“: Zaškrtněte políčko, pokud chcete kopírovat řádky faktury do poznámky k úhradě.
- :guilabel:`Datum debetní poznámky“: Zadejte datum.

.. poznámka::
Potvrďte fakturu a vytvořte ji s interním odkazem. Dokument pak odešlete na
Uruware, klikněte na tlačítko „Odeslat a vytisknout“ a zaškrtněte políčko „Vytvořit CFE“.
Po zpracování dokumentu je z Uruwary přinesen právní dokument sekvenční číslo.
Zajistěte si, aby byly k dispozici CAE v Uruwaru.

.. poznámka::
Validovaný dokument je z Uruware stáhnut podle specifikace od
uruguayské vlády (Dirección General de Información, DGI).

Přílohy a výhrady
========================

Poznámky a komentáře přidané do elektronického dokumentu se nazývají „poznámky“ (notes) nebo „doplňující informace“ (disclosures).
je povinná nebo nepovinná. Chcete-li vytvořit novou přílohu, přejděte na:
Konfigurace --> Přílohy a odhalení“ a klikněte na „Nový“.

Zadejte následující informace:

- :guilabel:`Název“: název dodatku nebo povinné informace.
- :guilabel:`Typ poznámky“: Vyberte typ poznámky a tato se přidá do konkrétní části XML.
- :guilabel:Je povinné uvádět: Vyberte tuto možnost, pokud je text povinným oznámením.
Je to další informace.
- :guilabel:`Obsah“: Přidejte celý text dodatku nebo výkladu.

Legenda a další informace o produktu
---------------------------------------------

Chcete-li přidat k produktu nebo k XML další informace nebo legendu, je nutné
Přednastavené přílohy a uvedení produktu v daňovém dokladu. Přidejte *legendu* do
:guilabel:„Zveřejnění“ pole produktu uvedeného v řádku.

Legenda a další informace
----------------------------------

Chcete-li přidat do elektronické faktury nebo XML další informace či legendu, otevřete fakturu.
Přejděte na záložku „Další informace“ a vyberte požadované přílohy v záložce „Přílohy a
Zobrazení „Zveřejnění“. Přílohy a zveřejňované informace, které jsou zde přidány, se objeví v XML i viditelně ve
PDF dokument.

Týká se následujících typů připojení:

- Dokument
- Vydavatel
- Příjemce
- Přílohy

.. poznámka::
Přidat do elektronického dokumentu dočasný poznámku lze pomocí :guilabel:`Podmínky použití
pole. Tato informace bude zaslána v dodatku faktury, ale nebude uložena pro případné vyhledávání.
budoucí dokumenty.
