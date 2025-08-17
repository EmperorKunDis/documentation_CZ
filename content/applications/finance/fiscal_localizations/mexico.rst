======
Mexiko
======

... _katalog satelitů: http://www.sat.gob.mx/tramitesyservicios/Paginas/catalogos_emision_cfdi_
http://www.kramerius.cz/data/praha/benesovsky/0124-0035/complemento_ce.htm

.. |SAT| nahradit za: :abbr:`SAT (Daňová správa)“
.. |DIOT| nahradit: zkratka: DIOT (Informační prohlášení o třetích stranách)
.. |PAC| nahradit za: abbr: PAC (Proveedor Autorizado de Certificación/Authorized Certification
Provozovatel)
.. |RFC| nahradit za: abbr:`RFC (Federální rejstřík poplatníků)`
.. |PPD| nahradit:: :abbr:`PPD (Pago en Parcialidades o Diferido/Payment in Installements or
Deferované)
.. |PUE| nahradit za: :abbr:`PUE (Pago en una Sola Exhibición/Payment in a Single Exhibition)`
.. |CFDI| nahradí: zkratka: CFDI (Daňový doklad v digitální podobě přes internet)

Webináře
========

Na videu z mexické lokalizace je také k dispozici. Toto video popisuje, jak tuto lokalizaci provést.
lokalizace od nuly včetně nastavení konfigurací a dokončení běžných
pracovních postupů a poskytuje podrobný pohled na několik konkrétních případů použití.

- „Webinář s plnou ukázkou <https://www.youtube.com/watch?v=5cdogjm0GCI>“.

Úvod
============

Moduly lokální mexické verze Odoo umožňují podepisování elektronických faktur dle
specifikace SAT pro verzi 4.0 CFDI <http://omawww.sat.gob.mx/
tramitesyservicios/Paginas/documentos/Anexo 20 Guia de llenado CFDI.pdf>, která je vyžadována zákonem.
1. ledna 2022. Tyto moduly také přidávají relevantní účetní výstupy (např.: DIOT,
umožňuje zahraniční obchod a vytváření dodacích průvodců.

.. poznámka::
Pro elektronické podepisování dokumentů v Odoo je nutné zajistit aplikaci „Sign“.
nainstalovány.

.. viz též:
:dokumentace o právní a regulační situaci v Mexiku


Konfigurace
=============

Požadavky
------------

Před konfigurací mexické lokalizace je nutné splnit následující požadavky
moduly v Odoo:

... požadavky na mx:

#Mít registraci v SATu s platným RFC.
#Máte certifikát digitální pečeti?
certifikát digitální pečeti>_(CSD).
#Vyberte si poskytovatele certifikace (Proveedor Autorizado de Certificación/Authorized Certification Provider).
V současné době spolupracuje Odoo s následujícími PAC: „Solución Factible
<https://solucionfactible.com/>, „Quadrum (dříve Finkok) <https://cfdiquadrum.com.mx/>“
„Svěží myšlení – chytřejší web <https://sw.com.mx/>“.
#Máte znalosti a zkušenosti s fakturací, prodejem a účetnictvím v Odoo. Tato dokumentace
**pouze** obsahuje potřebné informace k používání Odoo.

Instalace modulů
------------------

:ref:`Instalujte následující moduly, abyste získali všechny funkce mexického
lokalizaci. Moduly účetnictví a kontaktů jsou nutné k instalaci.
pro tuto konfiguraci:

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 25 25 50

   * Jméno
     - Technické označení
     - Popis
   * --label:Mexiko - Účetnictví
     - l10n_mx
     - Výchozí balíček pro daňovou lokalizaci :doc:`<../fiscal_localizations>` přidává účetnictví.
charakteristiky pro lokalizaci do Mexika, jako například: nejčastější daně a grafické znázornění
účty - na základě kódu skupiny účtů SAT
<http://www.gob.mx/cms/uploads/attachment/file/151586/codigo_agrupador.pdf>.
   * :- guilabel:EDI pro Mexiko
     - „l10n_mx_edi“
     - Zahrnuje všechny technické a funkční požadavky na generování a ověření
:doc:`Dokumenty elektroniky <../účetnictví/fakturace zákazníků/elektronická fakturace>` — založené
na technické dokumentaci zveřejněné společností SAT. To vám umožní zaslat faktury (s
nebo bez doplňků a platby komplementárních plateb vládě.
   * --:label:EDI verze 4.0 pro Mexiko
     - „l10n_mx_edi_40“
     - Nezbytné pro vytváření XML dokumentů s správnými specifikacemi CFDI 4.0.
   * --:guilabel:`Zprávy o mexické lokalizaci Odoo“
     - l10n_mx_reports
     - Adaptuje zprávy pro elektronické účetnictví v Mexiku: rozvahu, vyrovnání a
|DIOT|.
   * -- :guilabel:Mexiko - Zprávy o uzavření
     - „l10n_mx_reports_close“
     - Nezbytné k vytvoření uzavíracího záznamu (známého také jako „pohyb na měsíc 13“).
   * :- guilabel:Odoo Mexické XML Policie Export
     - l10n_mx_xml_polizas
     - Umožňuje vývoz souborů XML pro účetní záznamy, které jsou povinné k auditu.
   * --:guilabel:`Odoo Mexické XML Policie Exportní most Edi“
     - l10n_mx_xml_polizas_edi
     - Doplněk modulu l10n_mx_xml_polizas.

.. poznámka::
Při instalaci databáze od nuly a výběru Mexika jako země se Odoo
automaticky nainstaluje následující moduly: „Účetnictví – Mexiko“, „EDI pro
Mexiko“, „EDI verze 4.0 pro Mexiko“.

Následující moduly jsou volitelné. Je doporučeno je nainstalovat pouze v případě, že potřebujete
požadavek. Ujistěte se, že jsou pro podnikání nezbytné.

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 25 25 50

   * Jméno
     - Technické označení
     - Popis
   * --:label:EDI pro Mexiko (Pokročilé funkce)
     - „l10n_mx_edi_extended“
     - Přidává do faktur komplement vnějšího obchodu: právní povinnost při prodeji výrobků
zahraničí.
   * – :guilabel:`EDI verze 4.0 pro Mexiko (COMEX)“
     - „l10n_mx_edi_extended_40“
     - Adaptuje modul l10n_mx_edi_extended pro CFDI 4.0.
   * :- guilabel:Mexiko - elektronická dodací příručka
     - „l10n_mx_edi_stock“
     - Vám umožní vytvořit „Carta Porte“: Fakturu, která prokáže vládě, že jste
zasílání zboží mezi A & B s podepsaným elektronickým dokumentem.
   * „Průvodce elektronickým doručováním pro Mexiko (CFDI 4.0)“
     - l10n_mx_edi_stock_40
     - Adaptuje modul l10n_mx_edi_stock pro CFDI 4.0
   * --:guilabel:Odoo Mexiko pro sklad a přistání
     - „l10n_mx_edi_landing“
     - Umožňuje spravovat celní čísla související s přistavenými náklady v elektronických dokumentech.

Nastavte svou společnost
----------------------

Po instalaci správných modulů je další krok ověření, že vaše společnost je nakonfigurována
s správnými údaji. Chcete-li tak učinit, přejděte na:
a vyberte možnost „Aktualizace informací“ pod vaším názvem společnosti.

Do vzniklého formuláře zadejte celou adresu, včetně:
„Stát“, „Země“ a „DIČ“.

Podle požadavků CFDI 4.0 musí být uvedeno jméno hlavního kontaktu společnosti *.
shodovat se s vaším obchodním názvem zapsaným v SAT, bez zkratky právnické osoby.

.. obrázek: mexico/mx-company-info.png
:alt:Povinnosti hlavní kontaktní osoby pro správné vystavování faktur.

.. důležité::
Z právního hlediska musí mexická společnost používat místní měnu (MXN).
Odoo neposkytuje funkce pro správu alternativní konfigurace. Pokud chcete spravovat
jinou měnu, nechť je výchozí měnou MXN a použijte seznam cen
místo toho použijte „<../../sales/sales/products_prices/prices/pricing>“.

Dále přejděte na položku: „Nastavení“ – „Účetnictví“ – „Elektronická fakturace (MX)“ – „Daňová evidence“.
Vyberte si z nabídky režim, který se vztahuje na vaši společnost, a klikněte
:guilabel:`Uložit“.

.. obrázek:mexiko/mx-daňový režim.png
:alt: Konfigurace daňového režimu v Nastavení účetnictví.

.. tip::
Pokud chcete otestovat lokální verzi pro Mexiko, můžete společnosti nastavit skutečnou adresu
v rámci Mexika (včetně všech polí) a přidejte „EKU9003173C9“ jako :guilabel:„DPH“ a „Škola
„KEMPER URGATE“ jako název společnosti. Pro daňovou regulaci použijte
:guilabel:`Generál de Ley Osobní osoby“.

Kontakty
--------

Pro vytvoření kontaktu, který lze fakturovat, přejděte na: „Kontakty --> Vytvořit“. Pak zadejte
kontaktní jméno a příjmení včetně adresy: :guilabel:`PSČ`, :guilabel:`Stát`,
:guilabel:`Země“ a „DIČ“.

.. důležité::
Stejně jako u vaší vlastní společnosti musí mít všechny kontakty správný obchodní název
registrované u SAT. To platí i pro režim DPH, který je také nutné zaregistrovat u SAT.
v záložce MX EDI.

Daně
-----

Některé další konfigurace pro typ faktoru a daňové objekty musí být přidány do daně z přidané hodnoty.
Aby správně podepisovaly faktury.

Faktorový typ
~~~~~~~~~~~

Pole „Druh faktury“ je přednastaveno v základních daních. Pokud jsou vytvářeny nové daně, musíte
Ujistěte se, že tento prvek nastavíte. Chcete-li tak učinit, přejděte na:
Dáte „Daně“, pak zapnete pole „Typ faktury“ v záložce „Pokročilé možnosti“.
všechny záznamy s nastaveným atributem „Druh daně“ na hodnotu „Prodej“.

.. obrázek: mexico/mx-factor-type.png
:alt: Konfigurace prodejní daně.

.. tip::
Mexiko má dvě různé varianty nulové DPH, aby se vypořádalo s dvěma scénáři:

   - *bez DPH* nastaví :guilabel:`Typ faktoru“ na :guilabel:`Sazba“
   - *Bez DPH* nastavilo pole „Typ faktury“ na hodnotu „Za odběr“.

Daňový předmět
~~~~~~~~~~

Jedním z požadavků CFDI 4.0 je, že výsledný soubor XML musí (nebo nemusí) být rozdělen
snížit daně z provozu. Existují tři různé možné hodnoty, které se přidávají do XML
soubor:

- „01“: Není předmětem daně – tato hodnota se automaticky přidá, pokud v poli faktury neobsahuje
jakékoliv daně.
- „02“: Předmět daně – tento výchozí stav se vztahuje na jakoukoli řádku faktury, která obsahuje daň.
- „03“: Předmět daně, který není nucen k rozebírání – tento stav lze vyvolat na požádání
určitým zákazníkům nahradit hodnotu 02.

Pro použití hodnoty „03“ přejděte na: Menu > Kontakty - faktura vašeho zákazníka - MX EDI
tabulku, a zaškrtněte políčko „Žádné rozdělení daně“.

.. obrázek: mexico/mx-tax-breakdown.png
:alt:Na kartě MX EDI zákaznického faktury není možnost rozložení daní.

.. důležité::
Hodnota „Žádné rozdělení daně“ se vztahuje pouze na konkrétní daňové režimy a/nebo daně.
Nejprve se poraďte s účetním, zda je pro vaši firmu nutné před podáním žádosti o půjčku
úprava.

Jiné daňové konfigurace
~~~~~~~~~~~~~~~~~~~~~~~~

Při registraci platby v Odoo provede pohyb daní z účetní osnovy
Převést zůstatek účtu* na účet uvedený v záložce „Definice“. Tento pohyb je osvobozen od daně
bude použita základní daňová složka („Impuesto sobre las Ventas en Base al Flujo de Efectivo“)
záznam v den přeřazení daní. **Nedělejte s tímto účtem nic**.

Pokud vytvoříte novou daň v sekci „Účetnictví“ -> „Konfigurace“ -> „Daně“, musíte přidat
správné pole „Daňové sazby“ pro ně („DPH“, „DPH“ nebo „IEPS“). Odoo podporuje pouze tyto
tři skupiny daní.

.. obrázek:mexiko/mx-daňový-konfigurátor.png
:alt:Daňové účty dostupné pro Odoo.

Produkty
--------

Pro konfiguraci produktů přejděte do sekce „Účetnictví“ - „Zákazníci“ - „Produkty“, pak vyberte
produkt, nebo vytvořit nový. V záložce „Účetnictví“ a v
Pole „Kategorie produktu“ v poli „UNSPSC Product Category“, vyberte kategorii, která reprezentuje produkt.
tento proces lze provést ručně nebo pomocí:doc:`většího nahrání dat <../../essentials/export_import_data>“.

.. poznámka::
Všechny produkty musí mít spojený s nimi kód |SAT|, aby se zabránilo ověřování
chyby.

Elektronická fakturace
--------------------

PAC kredit
~~~~~~~~~~~~~~~

Po zpracování soukromého klíče (CSD)
<https://www.sat.gob.mx/aplicacion/16660/genera-y-descarga-tus-archivos-a-traves-de-la-aplicacion-
certifikát s SATem musíte registrovat přímo u PACu (viz požadavky).
ještě před tím, než začnete vytvářet faktury pomocí Odoo.

Jakmile si vytvoříte účet u kterékoliv z těchto služeb, přejděte do sekce :menuselection:`Nastavení -->
Účetnictví --> Elektronické fakturace (MX`). V sekci „MX PAC“ zadejte název
Váš PAC s vašimi přihlašovacími údaji (:guilabel:uživatelské jméno PAC a :guilabel:heslo PAC).

.. obrázek: mexico/mx-pac-account.png
:alt:Konfigurace PAC kreditů z účetních nastavení.

.. tip::
Pokud nemáte přihlašovací údaje, ale chcete si vyzkoušet elektronickou fakturaci, můžete aktivovat
zaškrtněte políčko „Testovací prostředí MX PAC“ a vyberte možnost „Fakta Solucion“.
|PAC|. Nemusíte zadávat uživatelské jméno ani heslo pro testovací prostředí.

certifikáty typu .cer a .key
~~~~~~~~~~~~~~~~~~~~~~~~~~

„digitální certifikáty společnosti
Musí být nahrán na adresu <http://www.gob.mx/tramites/ficha/certificado-de-sello-digital/SAT139>
sekci „Certifikáty MX“. Chcete-li tak učinit, přejděte na „Nastavení“ >
Účetnictví --> Elektronické fakturace (MX`). V sekci „Certifikáty MX“ vyberte
:guilabel:Přidejte řádek“ a okno se otevře. Klikněte na „Vytvořit“, a poté nahrajte
certifikát ve formátu „.cer“ (soubor s příponou „.cer“), certifikační klíč
(souboru .key) a heslem vašeho certifikátu. Nakonec klikněte na tlačítko „Uložit“.
& Zavřít“.

.. obrázek:mexiko/mx-certifikaty.png
:alt:Vstupy pro nahrání certifikátu a klíče.

.. tip::
Pokud ještě nemáte sjednaný jeden z kontraktů |PAC|\s a chcete si vyzkoušet elektronickou fakturaci,
můžete použít následující certifikáty zkoušky SAT:

   - :download:`Certifikát <mexico/certificate.cer>`
   - :download:`Klíč certifikátu <mexico/certificate.key>`
   - Heslo: „12345678a“

Průběh práce
=========

Elektronická fakturace
--------------------

Fakturační proces v Odoo je založen na „Příloze 20
<http://www.sat.gob.mx/transacciones/versiones/v4.0/Anexo_20.pdf>
fakturace pro SAT.

Faktury zákazníků
~~~~~~~~~~~~~~~~~

Pro vystavení faktury z Odoo je nutné vytvořit zákaznickou fakturu pomocí standardního vystavování faktur.
příkazem „flow <../accounting/customer_invoices>“.

Při úpravách dokumentu se mohou měnit i platební metody (správná :guilabel:`Platební cesta`)
Nebo například:guilabel:`Použití`, které zákazník může vyžadovat, lze přidat.)

Po potvrzení faktury zákazníka se objeví modrá zpráva s textem: „Faktura zákazníka byla potvrzena.“
faktura bude zpracována asynchronně službou e-fakturace: CFDI (4.0).

Stisknutím tlačítka „Odeslat nyní“ se dokument předá vládě, aby mohl být
podpisem. Po obdržení podepsaného dokumentu od vlády byl :guilabel:`Daňový výměr“
V dokumentu se objeví pole a přílohou v chatu je přiložen soubor XML.

.. tip::
Pokud kliknete na tlačítko „Znovu“ v poli „Stav SAT“ faktury, můžete
zkontrolovat, zda je soubor XML platný v aplikaci |SAT|.

Pokud jste ve testovacím prostředí, vždy dostanete zprávu „Not Found“.

Pro odeslání podepsané faktury e-mailem můžete poslat oba soubory (XML a PDF) najednou.
přímým způsobem z Odoo kliknutím na tlačítko „Odeslat a vytisknout“. Můžete také stáhnout PDF
na váš počítač, kliknutím na tlačítko „Tisk“ a výběrem požadovaného tisku.
volba.

Kreditní poznámky
~~~~~~~~~~~~

Zatímco faktura je dokument typu „I“ (Ingreso), kreditní poznámka je dokument typu „E“ (Egreso).

Jedinou změnou je standardní postup pro vystavení kreditních poznámek
<../účetnictví/faktury zákazníkům/kreditní poznámky> je to tak, že jako podmínka pro SAT
je vztah mezi fakturou a kreditními poznámkami prostřednictvím daňového rejstříku.

Pro splnění této podmínky přidá pole :guilabel:`CFDI Origin` tuto vazbu pomocí znaku „01|“.
a následně faktura původního dodavatele.

.. obrázek: mexico/mx-vytvoreni-kreditni-zpatky.png
:alt: Příklad čísla původu CFDI.

.. tip::
Pro automatické přidání pole „Původ“ CFDI použijte pole „Přidat kredit
Využít tlačítko „Poznámka“ místo vytváření poznámky ručně.

Doplňkové platby
~~~~~~~~~~~~~~~~~~~

Platební politika
**************

Jednou z novinek v mexické lokalizaci je pole „Zásady platby“.
SAT dokumentaci jsou dvě platby:

- „PUE“ („Pago en una Sola Exhibición/Payment in a Single Exhibition“)
- „PPD“ (Platba v částech nebo odložená platba)

......viz také::
:doc:`../dokumentace/inventarizace-a-mrp/inventar/správa-produktů/hodnota-za-skladování/náklady-na-přepravu`

Rozdíl je v položce „Datum splatnosti“ nebo „Platební podmínky“.

Pro konfiguraci faktur PUE přejděte na :menuselection:`Účetnictví --> Zákazníci --> Faktury`.
a buď vyberte fakturu s datem splatnosti v tomtéž měsíci nebo zvolte platební lhůtu.
To neznamená změnu splatnosti dluhu (splatnost ihned, 15 dní, 21 dní, všechny termíny spadající do
v aktuálním měsíci.

.. obrázek: mexico/mx-pue-payment.png
:alt:Příklad faktury s požadavky na PUE.

.. tip::
Některé z výchozích platebních podmínek lze spravovat přímo v
:menu_selecce:`Účetnictví --> Konfigurace --> Platební podmínky`.

Pro konfiguraci faktur vytvořených pomocí |PPD| přejděte do sekce „Účetnictví > Zákazníci > Faktury“ a
Vyberte fakturu s datem splatnosti po první den následujícího měsíce.
se vztahuje, pokud je váš termín splatnosti („Termín platby“) stanoven na následující měsíc.

.. obrázek:mexiko/mx-ppd-platebni-obrazky.png
:alt:Příklad faktury s požadavky na PPD.

.. důležité::
Protože politika |PPD| předpokládá, že faktura nebude v tuto chvíli zaplacena,
V případě faktur PPD je správným způsobem platby pole „99 – Por definir“
definovat).

Průtok plateb
************

V obou případech je postup platby v Odoo stejný, viz dokumentace:
Hlavní rozdíl spočívá v tom, že platby spojené s fakturami PPD vyvolávají vytvoření dokumentu typu „P“.
pago

Pokud je platba spojena s fakturou PUE, může být zaevidována pomocí asistenta a přiřazena
s příslušným daňovým dokladem. Pro přechod na tuto stránku klikněte na: menu výběru:Účetnictví - zákazníci
Faktury“ a vyberte fakturu. Pak klikněte na tlačítko „Registrace platby“. Faktura
status se změní na „Ve stavu platby“, protože platba je skutečně ověřena, když je připsána na účet
usmíření.

.. viz též:
:doc:`../účetnictví/banka/srovnání“

Tento proces je stejný pro faktury PPD, ale přidání vytváření elektronického
dokument „<../účetnictví/fakturace zákazníků/elektronická fakturace>“ znamená nějaké další požadavky.
připojit k dokumentu, aby jej mohl správně zaslat na SAT.

Z faktury je nutné potvrdit konkrétní způsob platby, kde jste obdrželi
platby. Proto nelze pole „Způsob platby“ nastavit na hodnotu 99 – Por definir
((Definovat).

Pokud chcete v záložce „Účetnictví“ zákazníka přidat číslo účtu,
kontaktní karta musí mít platný účet.

.. poznámka::
Přesné konfigurace jsou v příloze č. 20 k SAT
<http://www.sat.gob.mx/transaccionesyservicios/Paginas/Anexo20.html>. Obvykle
:guilabel:`Číslo účtu“ musí být 10 nebo 18 číslic pro převody, 16 pro kreditní nebo debetní karty.

Pokud je platba spojena s fakturou podepsanou v souladu s politikou platebních podmínek (PPD), Odoo
generuje příslušný doplněk k platbě automaticky po stisku tlačítka „Zpracovat
Teď.

.. obrázek:mexiko/mx-podpis-doplněk.png
:alt:CFDI (4.0) Služba zpracování plateb v rámci elektronické fakturace.

.. varování:
Platba v měně MXN nelze použít k zaplacení více faktur v amerických dolarech. Namísto toho by platba
mohou být rozděleny na více platebních příkazů pomocí tlačítka „Registrace platby“ v
příslušné faktury.

Zrušení faktur
~~~~~~~~~~~~~~~~~~~~~

Lze zrušit elektronické dokumenty, které byly zaslány do SATu. Podle „Reforma Fiscal 2022
<https://www.sat.gob.mx/consultas/91447/nuevo-esquema-de-cancelacion> od 1. ledna 2022
Pro splnění těchto dvou požadavků je nutné:

- S každou žádostí o zrušení musíte uvést důvod.
- Po uplynutí 24 hodin od vystavení faktury je nutné požádat klienta o schválení zrušení objednávky.
Pokud dojde k reakci po uplynutí 72 hodin, je zrušení automaticky zpracováno.

Zrušení faktury je možné z následujících důvodů:

- 01 - Chybná faktura (s příslušným dokladem)
- 02 - Faktura s chybami (bez náhrady)
- 03 - Operace nebyla provedena
- 04 -Nominační operace související s celosvětovou fakturou

Zahájit zrušení objednávky proveďte v menu: „Účetnictví –> Zákazníci –> Faktury“ a vyberte
Vystavte fakturu k zrušení a klikněte na „Požadavek zrušit“. Poté se přihlaste
:ref:`lokalizace/mexiko/01-faktura-zrušení` nebo
podle příslušných částí „lokalizací/mexiko/02-03-04-faktura-zrušení“ v závislosti na zrušení
důvod.

.. tip::
Alternativně požádejte o zrušení v záložce CFDI kliknutím
:guilabel:`Zrušit“ na řádku položky.

..._lokalizace/mexiko/01-faktura-zrušení:

Důvod zrušení 01 - Chybně vystavená faktura (s přílohou)
***************************************************************************

#V okně „Zrušení faktury“ vyberte „01 – Vystavená faktura“.
s chybami (se souvisejícím dokumentem)` z pole „Důvod“ a klikněte
:guilabel:"Vytvořit náhradní fakturu" pro vytvoření nového návrhu faktury. Tento nový návrh faktury
Zaúčtování nové faktury nahrazuje předchozí fakturu včetně souvisejícího CFDI.
#Potvrďte návrh a odeslat a vytisknout fakturu.
#Návrat k původní faktuře (tedy faktuře, ze které jste poprvé požadovali
zrušení (zrušení). Pozor, pole „Změněno na“ se objevuje s odkazem na
novou fakturu.
#Klikněte na tlačítko „Zrušit požadavek“. V okně „Zrušení požadavku CFDI“ klikněte na
:guilabel:`01 - Vystavená faktura s chybami (s příslušným dokumentem)` je automaticky
vybrána v poli „Důvod“.
#Klikněte na tlačítko „Potvrdit“.

Zrušení faktury je pak vytvořeno s důvodem na kartě „CFDI“.

.. obrázek:mexiko/mx-faktura-zruseni-dvou-duvodu-01.png
:alt:Zrušená položka faktury v záložce CFDI.

.. poznámka::
   - Pokud klient odmítne zrušení faktury, položka pro zrušení faktury je ze zálohové faktury odebrána.
:guilabel:`CFDI“ tabulka.
   - Při použití důvodu zrušení „*01 - Faktura vystavená s chybami (s příslušným dokumentem)“
Předčíslí „04|“ může být v poli „Daňové identifikační číslo“. To je interní předčíslí.
používané společností Odoo k dokončení zrušení a **neznamená**, že důvod zrušení
byl 04 - Nominativní operace související s celosvětovou fakturou.

..._lokalizace/mexiko/02-03-04-faktura-zrušení:

Důvody zrušení 02, 03 a 04
***********************************

V okně „Poptávka na zrušení CFDI“ vyberte požadované zrušení.
Zrušení potvrdit a důvod zadat.

Při tomto způsobu zrušení faktury se vytvoří liniový položkový doklad s důvodem ve formátu CFDI.
tabulka

.. poznámka::
Pokud klient odmítne zrušení faktury, položka pro zrušení faktury se ze sestavy vymaže.
:guilabel:`CFDI“ tab.

Zrušení plateb
*********************

Je také možné zrušit platbu doplňku. To provedete přes platební příkaz v sekci
Vyberte „Účetnictví“ -> „Zákazníci“ -> „Platby“, a vyberte „Požadavek na EDI
Zrušení“. Stejně jako u faktur se objeví modrá tlačítka. Klikněte na „Proces nyní“ a
Dokument bude odeslán na SAT. Po několika sekundách můžete kliknout na tlačítko :guilabel:`Připojit znovu`, abyste potvrdili
současný stav SATu.

Poté je stav platby přesunut na :guilabel:`Zrušeno“.

.. poznámka::
Stejně jako faktury, když vytváříte nový *Platební doplněk*, můžete přidat vztah k
originálního dokumentu přidáním „04|“ a fiskální částky do pole „Původní CFDI“ v :guilabel:„Originální CFDI“.

Fakturace speciálních případů
~~~~~~~~~~~~~~~~~~~~~~~~~~~

CFDI veřejnosti
**************

Pokud zákazník, kterému prodáváte zboží nebo služby, nevyžaduje fakturu, použijte CFDI pro veřejnost *.
musí být vytvořen.

Pokud použijete jméno zákazníka „Publico en general“, dojde k chybě. To je
Hlavní změnou v CFDI 4.0 je, že faktury s tímto konkrétním názvem budou potřebovat další
údaje, které Odoo v současné době nepodporuje. Pro vytvoření CFDI do veřejných financí je tedy potřeba
Přidejte jakýkoli název pro zákazníka, který není „PUBLIKUM IN GESAMTHEIT“. (Například: „ZÁKAZNÍK FINANČNÍHO TRHU“)

Dále je nutné přidat kód ZIP vaší společnosti.
Výchozí hodnota je nastavena na „XAXX010101000“, a fiskální režim vašeho zákazníka musí být
zařazeno jako „Bez daňových povinností“.

.. obrázek:mexiko/mx-cfdi-pro-verejnost.png
:alt: Konfigurace pole pro veřejného zákazníka CFDI.

Multiměnová
*************

Hlavní měnou v Mexiku je MXN. Zákonem jsou všechny mexické společnosti povinny používat tento druh měny.
možné zasílat a přijímat faktury (a platby) v různých měnách. Pro možnost použití
:doc:`Multiměnový účet <../accounting/get_started/multi_currency>“ a přejděte na
V nabídce „Účetnictví“ -> „Nastavení“ -> „Měny“ nastavte :guilabel:`Mexické banky“.
„Služby“ v sekci „Převod měn“. Poté nastavte
V poli „Intervál“ zadejte časové období, na které chcete aktualizovat směnný kurz.

Takto bude mít soubor XML dokumentu správný kurz a celkovou částku.
v cizí měně i v MXN.

Je velmi doporučeno používat pro každou měnu vlastní účet.
<../účetnictví/banka/cizí měna>.

.. poznámka::
Jedinými měnami, které automaticky aktualizují svůj kurz každý den, jsou: USD, EUR, GBP a
JPY.

.. obrázek: mexico/mx-multicurrency-1.png
:alt: Konfigurace více měn v nastavení účetnictví.

Zálohy
*************

Může se stát, že vám zákazník zaplatí předem za služby, které musíte uplatnit.
a později vyúčtovat. V Odoo je nutné správně propojit faktury s každým
další s polem „CFDI Origin“. Pro jeho nastavení je nutné mít vytvořené pole „Prodej
Aplikace „Prodej“ nainstalována.

.. viz též:
„Oficiální dokumentace pro registraci záloh v Mexiku
<http://www.sat.gob.mx/transacciones-y-servicios/Documentos/Caso_uso_Anticipo.pdf>.

Nejprve přejděte do aplikace „Prodeje“ a vytvořte produkt Anticipo a nakonfigurujte jej.
Značka „Produktová kategorie“ musí být „Služba“, a používat značku „Kategorie UNSPSC“.
musí být: „84111506 Fakturace“.

Pak přejděte na: „Prodej“ – „Nastavení“ – „Fakturace“ – „Zálohy“, a doplňte
Produktem Anticipo jako výchozím.

Vytvořte prodejní objednávku s celkovou částkou a vytvořte zálohu (buď pomocí procenta nebo
sjednané částce. Pak dokument podepište a zaregistrujte platbu.

Když dojde čas na vystavení konečné faktury, vytvořte ji znovu ze stejného prodeje.
pořadí. V průvodci vytvářením faktur vyberte „Běžný doklad“ a odstraňte zaškrtnutí
:guilabel:`Odečítejte splátky“.

Poté zkopírujte položku „Daňový doklad“ z první faktury a vložte ji do
:guilabel:`Původní CDFI“ druhé faktury přidáním předčíslí „07|“ před hodnotu. Pak podepište
dokumentu.

Po tomto vytvořte kreditní fakturu pro první fakturu. Zkopírujte pole „Daňový doklad“ z
druhý daňový doklad a vložte ho do pole „Původ CFDI“ faktury s připojením předpony
„07|“. Pak dokument podepište.

S tímto se všechny elektronické dokumenty propojí dohromady. Posledním krokem je úplné zaplacení nového
faktura. Na nové faktuře se nachází v dole účetní doklad
:guilabel:`Dluhy vynikající kvality“ – přidejte je jako platbu. Nakonec zaregistrujte zbývající částku
„Registrace platby“ v nástroji „Průvodce“.

Vnější obchod
--------------

Externí obchod je doplněk k běžnému faktuře, který přidává určité hodnoty jak v XML, tak
PDF, tedy faktury pro zahraničního zákazníka podle „saturnských“ pravidel.
<https://www.sat.gob.mx/tramitesyservicios/Paginas/complemento_comercio_exterior.htm>

- Specifická adresa příjemce a odesílatele
- Přidání tarifního poplatku :guilabel:Tariff Fraction, který určuje typ produktu
- Pravý :guilabel:`Incoterm` (mezinárodní obchodní podmínky) a další (*certifikát
původu a speciálních jednotek měření)

Tímto se usnadňuje správná identifikace vývozců a dovozců, kromě rozšíření
popis prodávaného zboží.

Od 1. ledna 2018 je pro poplatníky s vývozní činností podmínkou vedení zahraničního obchodu
typ A1. Zatímco současný CFDI je verze 4.0, obchod s cizími státy je aktuálně ve verzi 1.1

Pro využití této funkce je potřeba nainstalovat moduly :guilabel:`l10n_mx_edi_extended` a
Musí být nainstalovány balíčky s označením guilabel:l10n_mx_edi_extended_40.

.. důležité::
Před instalací se ujistěte, že vaše firma potřebuje tuto funkci. Konzultujte s účetním
Nejprve, pokud je třeba, nainstalujte všechny potřebné moduly.

Konfigurace
~~~~~~~~~~~~~

Kontakty
********

Pro konfiguraci kontaktu pro obchod s externími subjekty přejděte na:
Zákazníci --> Zákazníci a zvolte si svou „Společnost“. Podle požadavků CFDI 4.0
abyste do kontaktu přidali platný kód ZIP, obchodní doplněk vám
požadavek, aby vaše :guilabel:`Město“ a :guilabel:`Stát“ byly také platné.
Pole musí odpovídat oficiálnímu katalogu SAT <sat-catalog_> nebo dostanete chybu.

.. varování:
Přidejte pole „Město“ a „Stát“ do kontaktních údajů společnosti, ne do informací o společnosti.
sám. Kontakt na vaši firmu najdete v sekci „Účetnictví“ - „Zákazníci“.
Zákazníci.

Pole „Lokalita“ a „Číslo kolonie“ jsou volitelná a mohou být přidána v
firmě přímo v:menu:Nastavení --> Obecné nastavení --> Firmy. Tyto dva poli
musí být shodná s daty v SAT.

.. obrázek: mexico/mx-external-trade-rescompany.png
:alt:Povinné pole pro obchodní společnost zapsanou v obchodním rejstříku.

Pro konfiguraci kontaktních údajů pro zahraničního příjemce klikněte na:
Vyberte položku „Zákazníci“ – „Zákazníci“, a vyberte kontakt zahraničního zákazníka. Kontakt musí mít
Následující pole je nutné vyplnit, aby nedošlo k chybě:

#Veškerá společnost, včetně adresy s platným kódem :guilabel:`ZIP“ a cizí
:guilabel:`Země“.
#Formát cizího čísla DPH: guilabel:VAT (daňové identifikační číslo, například: Kolumbie
   `123456789-1`)
#V záložce „MX EDI“ je nutné vyplnit adresu, na kterou zákazník obdrží zboží po dobu
dočasně (:guilabel:`Dočasné“) nebo trvale (:guilabel:`Trvalé“).

.. důležité::
Pokud byl nový kontakt vytvořen duplikací již existujícího kontaktu z Mexika, ujistěte se, že
odstranit jakékoliv přenesené informace z pole „Daňový režim“. Dále se také ujistěte, že
zapnout možnost „Žádné rozdělení daně“. Vybráním této možnosti se skryjí povinné položky.
jsou potřebné pro konfiguraci kontaktů v obchodě s cizími zeměmi.

.. obrázek: mexico/mx-external-trade-customer-contact.png
:alt:Povinné pole pro externího obchodního partnera.

.. poznámka::
Výsledný XML a PDF soubor obsahují automaticky nahrazené :guilabel:`DPH“.
VAT pro zahraniční transakce: „XEXX010101000“.

Produkty
********

Všechny produkty obchodu s cizími zeměmi mají čtyři povinné pole, z nichž dvě jsou exkluzivní
vnější obchod.

#Vnitřní odkaz na produkt je v záložce „Obecné informace“.
#Hmotnost produktu musí být větší než 0.
#„Pravý“ tarif: guilabel: „Tarif
částku v záložce „Účetnictví“.
#:guilabel: UMT Aduana odpovídá :guilabel: Celní tarifní frakci.

.. obrázek:mexiko/meziunijni-obchod-produkty.png
:alt:Povinné pole pro obchodní produkty vnějšího obchodu.

.. tip::
   - Pokud kód tarifní frakce Univerzity Manchesteru je 01, správný kód UMT Aduana
je „kg“.
   - Pokud je kód tarifní části v UoM „06“, správný kód pro :guilabel:`UMT Aduana“
je „Jednotky“.

Fakturační tok
~~~~~~~~~~~~~~

Před vystavením faktury je důležité zvážit, že externí obchodní faktura
musíte převést částky svého produktu na americké dolary. Proto je nutné použít:
„Účetnictví“ musí být zapnuté a „Měna“ musí být aktivována na
sekci „Měna“. Správnou službou je „Mexické peso“.
Banky.

Pak nastavíte správný kurz v sekci „Účetnictví -> Nastavení ->
Měna“, zbývající pole jsou: „Značka“ a volitelné „Certifikát“.
Zdroj v záložce „Další informace“.

.. obrázek:mexiko/mezoobchod-jinak.png
:alt:Další informace o produktu v záložce Obchod s cizími zeměmi.

Nakonec podepište fakturu stejným způsobem jako běžnou fakturu a klikněte na
tlačítko „Spustit nyní“.

Příručka pro doručování
--------------

„Cartu de Pas“ lze získat na úřadě pro cestovní doklady
námořní doklad: dokument, který uvádí druh, množství a cíl nákladu.

Od 1. prosince 2021 byla pro všechny dopravce implementována verze 2.0 tohoto CFDI.
prostředníky a vlastníky zboží. Odoo je schopna vygenerovat typ dokumentu „T“ (Traslado), který
Na rozdíl od jiných dokumentů vzniká dodací list místo faktury nebo platby.

Odoo může vytvářet soubory XML a PDF s (nebo bez) pozemní přepravou a zpracovávat materiály.
Jsou považovány za nebezpečné.

Pro použití této funkce je potřeba modul :guilabel:`l10n_mx_edi_extended`.
:guilabel:`l10n_mx_edi_extended_40“, „l10n_mx_edi_stock“
Musí být nainstalován modul :guilabel:`l10n_mx_edi_stock_40`.

Kromě toho je nutné mít vlastní :doc:`Seznam věcí
Instalovány jsou také aplikace „Sklad“ (<../../inventory_and_mrp/inventory>) a „Prodej“ (<../../sales/sales>).

.. důležité::
Odoo nepodporuje typ dokumentu „I“ (Ingreso) v rámci systému Carta Porte pro leteckou nebo námořní přepravu.
Před provedením jakýchkoliv úprav se poraďte s účetním, zda je tato funkce potřebná.

Konfigurace
~~~~~~~~~~~~~

Odoo spravuje dva různé typy CFDI:

- **Žádné federální dálnice**: Toto je použito, pokud je vzdálenost do cíle menší než 30 km.
<http://www.sat.gob.mx/transporte/autotransporte/preguntas-frecuentes.pdf>.
- **Federální doprava**: Používá se, pokud je vzdálenost do cíle více než 30 km.

Kromě běžných požadavků na fakturaci (RFC zákazníka, UNSPSC)
kód atd.), pokud používáte „Žádné federální dálnice“, není potřeba žádná externí konfigurace.

Pro společnost Federal Transport je potřeba přidat do kontaktů, vozidel a sestav několik konfigurací.
produktů. Tyto konfigurace jsou přidány do souborů XML a PDF.

Kontakty a vozidla
*********************

Stejně jako vlastnost obchodu s cizími zeměmi je adresa společnosti i konečného zákazníka
musí být kompletní. ZIP kód, město a stát musí souhlasit
s „Oficiálním katalogem pro dveřní kování Carta Porte“

.. tip::
Pole „Lokalita“ je pro obě adresy nepovinné.

.. obrázek:mexiko/mx-dodací-průvodce-kontakty.png
:alt:Kontakt pro konfiguraci doručení.

.. důležité::
Adresa pro doručení je nastavena v položce „Sklad -->
Konfigurace --> Skladování a logistika --> Sklady. Zde je nastavená adresa společnosti
Výchozí adresa se dá změnit podle vaší správné skladové adresy.

Další přidanou funkcí je nabídka „Nastavení vozidla“ v
:menuinventar--> nastavení--> Mexiko“. Tento menu vám umožní přidat všechny informace
související s vozidlem použitým k doručení objednávky.

Všechna pole jsou povinná pro vytvoření správného průvodce dodáním.

.. tip::
Políčka „Registrační značka vozidla“ a „Číslo registrace“ musí obsahovat mezi
5 až 7 znaků.

V sekci „Zprostředkovatelé“ musíte přidat provozovatele vozidla.
povinné položky pro tento kontakt jsou DPH a Řidičský průkaz.

.. obrázek:mexiko/mx-dodavatelsky-pruvodce-vozidlo.png
:alt: Konfigurace vozidla pro přepravu zásilek.

Produkty
********

Podobně jako u běžného fakturace musí mít všechny produkty kategorii UNSPSC. Kromě
Kromě toho existují dvě další konfigurace produktů, které se týkají dodacích průvodců:

- Vlastnost „Druh produktu“ musí být nastavena na hodnotu „Skladovatelný produkt“, aby se mohly provádět pohyby zásob.
Vznikla.
- V záložce „Sklad“ by měl být v poli „Hmotnost“ hodnota vyšší než 0.

.. varování:
Vytvoření dodacích podmínek produktu s hodnotou 0 vyvolá chybu.
:guilabel:`Hmotnost“ již byla v objednávce uložena a je potřeba vrátit
produkty a znovu vytvořte objednávku (a průvodce dodáním) s správnými množstvími.

.. obrázek: mexico/mx-delivery-guide-products.png
:alt: Průvodce konfigurací produktu.

Prodej a pohyb zásob
~~~~~~~~~~~~~~~~~~~~~~~~

Nejprve je třeba vytvořit a potvrdit prodejní objednávku.
:menu „Prodej“ -> „Objednávka“. To vytvoří tlačítko „Dodání“, na které klikněte
a poté zkontrolujte převod pomocí funkce „Validate“.

Po nastavení stavu na :guilabel:`Done` můžete upravit převod a vybrat
„Dopravní typ“ (buď „Žádné federální dálnice“ nebo „Federální dálnice“).
Doprava`).

Pokud má vaše dodací průvodce typ :guilabel:`Žádné federální silnice“, můžete si převod uložit a
Pak klikněte na tlačítko „Vytvořit průvodce dodáním“. Výsledný XML soubor naleznete v chatu.

.. poznámka::
Kromě UNSPSC v každém produktu jsou dodací průvodce, které používají No Federal
Vysokorychlostní silnice nevyžadují žádné speciální konfigurace, které by se posílaly vládě.

Pokud má vaše dodací průvodce typ „Federální doprava“, pak v záložce „MX EDI“
se objeví. Tam zadejte hodnotu větší než 0 do políčka „Vzdálenost od cíle (km)“
vyberte nastavení vozidla použité pro tuto dodávku.

.. obrázek: mexico/mx-delivery-guide-federal-transport.png
:alt: Návod k nastavení tabulky pro přenos MX EDI.

Nebezpečné nebezpečí
*****************

Některé hodnoty v poli :guilabel:`UNSPSC Category` jsou zohledněny ve „SAT katalogu“
<http://www.sat.gob.mx/tramitesyservicios/Paginas/complemento_carta_porte.htm> jako nebezpečný
rizik. Tyto kategorie vyžadují další zvážení při vytváření dodacích pokynů s
:guilabel:`Federální doprava“.

Nejprve vyberte svůj produkt v sekci „Sklad --> Zboží --> Zboží“. Pak
:guilabel:`Účetnictví“ kartě, políčka „Kód nebezpečného materiálu (MX)“ a
:guilabel:`Nebezpečná obalová látka (MX)` musí být vyplněna správným kódem z katalogu SAT.

.. obrázek: mexico/mx-delivery-guide-hazards-designation.png
:alt: Příručka pro doručování nebezpečných látek, požadované pole.

V nabídce „Nastavení -> Mexiko -> Nastavení vozidla“ jsou uvedeny údaje z
:guilabel:`Pojištění životního prostředí“ a „Pojištění životního prostředí“ musí být podány.
A pak pokračujte v běžném procesu vytváření průvodce dodávkou.

.. obrázek:mexiko/mx-dodací-průvodce-nebezpečí-pro životní prostředí.png
:alt: Průvodce dodáním požadovaných údajů pro prostředí pojišťovny.

Kontrolní čísla
---------------

Deklarace celní (Pedimento Aduanero) je fiskální dokument, který potvrzuje, že všechny
Placené příspěvky do finanční instituce (SAT) včetně dovozu a vývozu
zboží.

Podle přílohy číslo 20 <http://www.sat.gob.mx/tramitesyservicios/Paginas/anexo_20.htm>
CFDI 4.0, v dokumentech, kde jsou dodané zboží ze zásilky dovážené přímo, je pole
:guilabel:`Číslo celního úřadu“, musí být přidán na všechny řádky produktů, které jsou součástí operace.

Pro instalaci je nutné nainstalovat modul :guilabel:`l10n_mx_edi_landing`, kromě
:doc:`Skladová evidence <../../inventory_and_mrp/inventory>“, :doc:`Nákup
<../../skladovani-a-mpr/naskupovani> a :doc:`Prodej <../../prodej/prodej>“.

.. důležité::
Nezaměňujte tuto funkci s obchodem se zahraničím. Celní čísla jsou přímo spojena
dovozem zboží a obchodní doplněk se týká vývozu.
účetní, pokud je tato funkce potřebná před jakýmikoliv změnami.

Konfigurace
~~~~~~~~~~~~~

Odoo používá k určení správného celního čísla pro konkrétní fakturu :doc:`náklady na dovoz.
<../../inventar-und-mrp/inventar/produktverwaltung/Inventarisierungswert/Landkosten>.
Vyberte položku „Správa inventáře“ > „Konfigurace“ > „Nastavení“ > „Ocenění“. Zkontrolujte, zda
Aktivujte položku „Náklady na dopravu“.

Začněte vytvářet produkt typu „služba“ s názvem „Pedimento“. V záložce „Nákup“
Aktivujte políčko „Splátka“, vyberte „Metodu rozdělení“ a klikněte na tlačítko „Použít“.

Pak nakonfigurujte položky s celními čísly, které jsou uložitelné. Pro tento účel vytvořte uložitelnou
produkty a ujistěte se, že v poli „Kategorie produktu“ je následující konfigurace.

- :guilabel:`Metoda nákladového účetnictví“: Buď :guilabel:`FIFO“ nebo :guilabel:`AVCO“
- :guilabel:`Ocenění zásob“: :guilabel:"Automatické"
- :guilabel:`Účet ocenění cenných papírů“: :guilabel:`115.01.01 Skladové zásoby“
- :guilabel:`Stock Journal“: :guilabel:"Hodnota zásob"
- :guilabel:`Účet vstupu do zásob“: :guilabel:"115.05.01 Zboží ve skladování"
- :guilabel:`Výstupy z obchodu s cennými papíry“: „115.05.01 Zboží v přepravě“

.. obrázek: mexico/mx-landing-configuration.png
:alt: Obecná konfigurace skladovatelných výrobků.

.. obrázek: mexico/mx-landing-configuration-category.png
:alt: Konfigurace kategorie skladového zboží.

Nákupní a prodejní tok
~~~~~~~~~~~~~~~~~~~~~~~

Po konfiguraci produktu postupujte podle standardního nákupního průvodce.
<../../inventar-a-mrp/naskupovani>.

Vytvořte objednávku z menu: „Nákupy“ - „Objednávky“ - „Dodací list“. Poté potvrďte
povolení zobrazit tlačítko „Pokladní doklad“ v seznamu chytrých tlačítek. Klikněte na „Pokladní doklad“.
tlačítko k ověření faktury.

Přejděte na záložku „Skladové zásoby“ – „Provoz“ – „Náklady na skladování“, vytvořte nový záznam a přidejte
převod, který právě vytvoříte, a oba: produkt „Pedimento“ a štítek „Číslo celního úřadu“.

Pokud chcete, můžete přidat částku nákladů. Poté ověřte celkovou cenu dopravy.
:guilabel:`Přidáno“, všechny produkty spojené s tímto dokladem mají přiřazeno celní číslo.

.. varování:
Můžete přidat číslo Pedimentos pouze jednou, takže se ujistěte, že přiřazujete správné číslo.
číslo převodu (převodů).

.. obrázek: mexico/mx-landing-inventory.png
:alt:Číslo celního úřadu na záznamu o nákladech spojených s přistáním letadla.

Nyní vytvořte prodejní objednávku a potvrďte ji. To by mělo spustit tlačítko „Dodání“ chytré značky.
Zkontrolujte, zda je platná.

Nakonec vytvořte fakturu z objednávky a potvrďte ji. Fakturační řádek související s vaší
výrobek má v sobě celní číslo, které by mělo odpovídat celnímu číslu přidávanému do
Vytvořený záznam *Náklady na dopravu*.

.. obrázek: mexico/mx-landing-invoice.png
:alt: Celní číslo na potvrzené prodejní objednávce produktu.

Elektronické účetnictví
---------------------

Pro Mexiko „Elektronická účetní kniha
<https://www.sat.gob.mx/aplicacion/42150/envia-tu-contabilidad-electronica>
povinnost vést účetnictví a vkládat do něj záznamy elektronickou cestou a vést účetní
informace měsíčně na webu www.sat.cz.

Skládá se z tří hlavních souborů XML:

#Aktualizovaný seznam účtů, který používáte v současné době.
#.Měsíční vyrovnání, včetně závěrečného zápisu, také známého jako: *Trial Balance Month 13*.
#Exportu účetních záznamů do vašeho generálního
ledger.

Výsledné soubory XML splňují požadavky „Anexo Técnico de Contabilidad Electrónica
1.3 <https://www.gob.mx/cms/uploads/attachment/file/151135/Anexo24_05012015.pdf>.

Dále můžete vytvořit DIOT.
<https://www.sat.gob.mx/declaracion/74295/presenta-tu-declaracion-informativa-de-operaciones-con
tercero-(diót)->`_:Zpráva o účetních záznamu dodavatele, které zahrnují DPH.
Exportováno do souboru .txt.

Pro použití těchto zpráv je potřeba modul:guilabel:`l10n_mx_reports`,
:guilabel:`l10n_mx_reporty_uzavření“, :guilabel:`l10n_mx_xml_pojistky“
:guilabel:`l10n_mx_xml_polizas_edi“ musí být nainstalovány a také „:doc:Účetní
<../účetnictví/začínáme>.

.. důležité::
Specifické vlastnosti a povinnosti zpráv, které odesíláte, se mohou měnit podle
do vašeho daňového režimu. Vždy kontaktujte svého účetního, než jakýkoli dokument pošlete
vláda.

.. _l10n_mx/účetní kniha:

Klasifikační schéma
~~~~~~~~~~~~~~~~~

V Mexiku se používá účetní kniha s
specifický vzor založený na kódu skupinového účtu SAT
<http://www.sat.gob.mx/fichas_tematicas/buzon_tributario/Documentos/codigo_agrupador.pdf>.

Můžete vytvořit jakýkoli účet, pokud je dodržen pravidelný vzorec:
„NNN.YY.ZZ“ nebo „NNN.YY.ZZZ“.

.. příklad::
Například 102.01.99 nebo 401.01.001.

Při vytváření nového účtu v sekci „Účetnictví“ - „Konfigurace“ - „Výkaz zisku a ztráty“
Účty“, s vzorem skupinového kódu „|SAT|“ se ve správném řádku objeví
:guilabel:`Štítky“ a váš účet se objeví v zprávě o *COA*.

Jakmile vytvoříte všechny své účty, ujistěte se, že jsou správně přidány :guilabel:`Tagy`.

.. poznámka::
Nemůžete používat žádný vzor, který končí sekcí nulou (například „100.01.01“, „301.00.003“ nebo
„604.77.00“. To způsobuje chyby v hlášení.

Jakmile je vše nastaveno, přejděte na: „Účetnictví“ – „Zprávy“ – „Saldo“.
klikněte na ikonu „fa-caret-down“ („svislá šipka“) vedle tlačítka „PDF“ a
Vyberte: guilabel: COA SAT (XML). To vytvoří soubor XML s vašimi účty, který můžete
Nahrát přímo na webovou stránku SATu.

Účetní vyrovnání
~~~~~~~~~~~~~

Výsledky účetního rozvahového listu ukazují počáteční zůstatek, kredit a celkový zůstatek vašich účtů.
aby jste k nim přidali správný :ref:`kódování skupiny <l10n_mx/chart-of-accounts>`.

Pro vytvoření této zprávy ve formátu XML přejděte na: „Účetnictví“ - „Zprávy“ -
Zkouška rovnováhy“. Vyberte měsíc, který chcete stáhnout v kalendáři a klikněte na
:ikonka „svislá čára“ (zobrazená jako ikona „dolů“) vedle tlačítka „PDF“, a poté
:guilabel:`SAT (XML)`

.. obrázek:mexiko/mx-reporty-rozvaha.png
:alt: Zpráva o zúčtování.

.. poznámka::
Odoo negeneruje souhrnné vyrovnání závazků a pohledávek.

Měsíční závěrka k 13. měsíci
**********************

Hlášení za měsíc 13 je závěrečný účet, který ukazuje všechny změny nebo pohyby v
účetnictví uzavřít za rok.

Vytvořit ho můžete takto:

#Přejděte na kartu „Účetnictví“ -> „Účetní knihy“ a vytvořte nový záznam.
změnit všechny částky, vyvážit kredit a/nebo dluh každé z nich.
#V záložce „Další informace“ zapněte možnost „Měsíční závěrka v měsíci 13“.
#Přejděte na „Účetnictví“ – „Zprávy“ – „Saldo“, klikněte na kalendář a vyberte
:guilabel:`Měsíc 13“.
#Klikněte na ikonu „svislý šipka“ („svislá šipka“) vedle tlačítka „PDF“,
vyberte:guilabel:'SAT (XML)'.

.. obrázek:mexiko/mx-zpravodajství-účetní závěrka 13. report.png
:alt:Zpráva o závěrkovém deníku za měsíc 13.

Účetní kniha
~~~~~~~~~~~~~~

Zákonem je stanoveno, že všechny transakce v Mexiku musí být zaznamenány digitálně. Od doby, kdy Odoo automaticky vytváří veškeré
podkladní záznamy o fakturaci a platbách. Exportujte své záznamy
aby vyhověla kontrolám a případným vratkám daní ze strany SATu.

.. tip::
Můžete filtrovat podle období nebo podle časopisu dle aktuálních potřeb.

Pro vytvoření XML přejděte do: „Účetnictví“ – „Zprávy“ – „Obecný účetní deník“, klikněte na
:ikonka „svislá čára“ (zobrazená jako ikona „dolů“) vedle tlačítka „PDF“, a poté
:guilabel:`XML (Polizas)“. V okně „Možnosti exportu XML Polizas“ vyberte mezi čtyřmi
různé typy exportu:

- :guilabel:Daňová kontrola
- :guilabel:`Certifikace auditu“
- :label:Vrácení zboží
- :guilabel:`Odměna“

Pro :guilabel:`Daňová kontrola“ nebo :guilabel:`Certifikace auditu“ musíte napsat
„Číslo objednávky“ poskytnuté společností SAT. Pro „Vrácení zboží“, nebo
„Kompenzace“, musíte napsat své „Číslo procesu“, které vám také poskytne
|SAT|.

.. poznámka::
Pokud chcete tento report vidět bez odeslání, použijte ABC6987654/99 pro :guilabel:`Objednávku
číslo a „AB123451234512“ pro pole „Číslo procesu“.

Zpráva DIOT
~~~~~~~~~~~

DIOT (Deklarace informativní o operacích s třetími stranami)
Provoz s třetími stranami je další povinností u SATu, kde aktuální stav
z kreditních a nekreditních plateb, srážek a vratných DPH z faktur od dodavatelů.
jsou poskytovány Společnosti pro atomovou energii (SAT).

Na rozdíl od ostatních zpráv je |DIOT| nahrán do softwaru poskytovaného společností |SAT|, který obsahuje
Formulář A-29. V Odoo si můžete stáhnout záznamy o svých transakcích jako soubor .txt.
je možné nahrát do formuláře a vyhnout se tak přímočarému zachycení těchto dat.

Soubor transakcí obsahuje celkový počet vašich plateb zaevidovaných v fakturách dodavatelů, rozdělených
do příslušných typů DPH. Pole „DPH“ a „Země“ je povinné
pro všechny dodavatele.

Pro vytvoření zprávy DIOT přejděte na: „Účetnictví -> Zprávy -> Daňové zprávy“.
Vyberte měsíc, který chcete stáhnout v kalendáři, pak klikněte na ikonu „fa-caret-down“
(guilabel:'down arrow') vedle tlačítka 'PDF' a vyberte 'Report: DIOT (MX)'
a stáhnout soubor s příponou .txt.

.. obrázek: mexico/mx-reports-diot-example.png
:alt:Faktura prodejce, která je již zaplacena.

.. důležité::
V poli „Typ operace“ v sekci „Účetnictví“ je nutné vyplnit pole „L10N Mx“.
každého z vašich dodavatelů, abyste zabránili chybám při ověřování. Ujistěte se, že vámi používaná
Každý zákazník má nastavenou zemi pro :guilabel:`L10N Mx Nationality`, aby se automaticky objevila.

.... obrázek: mexico/mx-reports-diot-contact.png
:alt:DIOT informace o kontaktu dodavatele.
