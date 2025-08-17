=====
Indie
=====

..._Indie/instalace:

Instalace
============

Instalujte následující moduly, abyste získali všechny funkce indické
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * -- :guilabel:Indický účetnictví
     - „l10n_in“
     - Výchozí:balík lokalizace daní:
   * – :guilabel:Indická e-fakturace
     - „l10n_in_edi“
     - :ref:`Indická integrace elektronického fakturování <india/e-invoicing>`
   * :- guilabel:„Indický e-waybill“
     - l10n_in_edi_ewaybill
     - :ref:`Integrace indického e-way billu <india/e-waybill>`
   * :- guilabel:„Sklad Indian E-waybill“
     - „l10n_in_ewaybill_stock“
     - :ref:`Vytvoření e-waybillu z aplikace Sklad <india/e-waybill-stock>
   * – :guilabel:`Indický – Zkontrolujte stav DPH“
     - „l10n_in_gstin_status“
     - :ref:`Indická kontrola čísla DPH <india/gstin_status>`
   * Indický - GSTR India eFiling
     - l10n_v_zprávách_gstr
     - :ref:`Vrácení indické DPH <india/gst-filing>`
   * – :guilabel:`Indické účetní zprávy“
     - l10n_in_reports
     - :ref:`Indické daňové zprávy <india/gstr_reports>`

.. obrázek: indie/indie-moduly.png
:alt: Moduly pro indické lokalizace

..._Indie/elektronické faktury:

Indická konfigurace
====================

V sekci „Nastavení“ -> „Uživatelé a společnosti“ -> „Společnosti“ přidejte svůj :guilabel:`PAN`.
:guilabel:`DIČ“. DIČ je nezbytný pro určení typu poplatníka
GSTIN je nutný pro vytváření elektronických faktur a E-waybillů.

Elektronická fakturace
================

Odoo je v souladu s požadavky indické elektronické fakturační systém Indická služba DPH (GST).

Nastavení
-----

..._indie/e-fakturace-api:

Registrace do systému NIC e-Faktura
~~~~~~~~~~~~~~~~~~~~~~~~~~

Musíte se zaregistrovat na portál elektronických faktur Národního informačního centra (NIC) a
**Přístupové údaje API**. Potřebujete je k tomu, abyste si v aplikaci Odoo nastavili účetní program.
<Indie/konfigurace fakturačního systému>.

#Přihlaste se do portálu „NIC e-Faktura“ kliknutím na
:guilabel:`Přihlášení“ a zadáním svého „Uživatelského jména“ a „Hesla“.

.. poznámka::
Pokud jste již zaregistrováni na portálu NIC, použijte stejné přihlašovací údaje.

.. obrázek:: india/e-invoice-system-login.png
:alt:Registrace systému Odoo na portálu pro elektronické faktury

#. Z nabídky přejděte na: „Registrace API –> Uživatelské údaje –> Vytvořit API
Uživatel`;
#Po této akci byste měli obdržet kód :abbr:`OTP (jednorázový heslo)` na svém registrovaném mobilním telefonu.
číslo. Zadejte kód OTP a klikněte na „Přijmout OTP“;
#Vyberte „Díky GSP“ jako rozhraní API a nastavte „Tera Software Limited“.
GSP a zadejte uživatelské jméno a heslo pro vaši API. Jakmile je hotovo,
Klikněte na tlačítko „Odeslat“.

.... obrázek: india/submit-api-registration-details.png
:alt:Přihlášení pomocí specifických uživatelského jména a hesla API

..._indie/elektronická fakturace:

Konfigurace v Odoo
~~~~~~~~~~~~~~~~~~~~~

Pro zapnutí služby fakturace v Odoo přejděte na: „Účetnictví --> Konfigurace -->
Nastavení > Elektronické fakturace v Indii“, zadejte uživatelské jméno
:guilabel:`Heslo“ dříve nastavené pro API.

.. obrázek:indie/faktura-online-nastavení.png
:alt:Nastavení služby fakturace elektronicky

... _india/e-fakturace-účetnictví:

Časopisy
********

Pro automatické odesílání elektronických faktur do portálu NIC pro elektronické faktury musíte nejprve nakonfigurovat své *prodejní*
journal zvolením v menu „Účetnictví“ -> „Nastavení“ -> „Journály“ a otevření vašeho prodeje.
deníku a v záložce „Pokročilé nastavení“ pod záložkou „Elektronické údaje“.
Vyměnit, povolit: „Faktura v elektronické podobě (IN)“ a uložit.

... _india/e-fakturace-proces:

Průběh práce
--------

.._indie/ověření faktury:

Kontrola faktury
~~~~~~~~~~~~~~~~~~

Jakmile je faktura ověřena, zobrazí se na horní části potvrzení. Odoo automaticky
Po nějaké době nahrává na portál e-fakturace NIC podepsaný soubor s platnými fakturami ve formátu JSON.
chcete fakturu ihned zpracovat, klikněte na tlačítko „Zpracovat nyní“.

.. obrázek:indie/fakturace-elektronicky.png
:alt:Indická potvrzení o elektronické fakturaci

.. poznámka::
   - Soubor podepsaný pomocí JSON najdete v přílohách zprávy.
   - Stav dokumentu lze zkontrolovat pod
:guilabel:`EDI dokument“ nebo „Daňový doklad v elektronické podobě“ na faktuře.

... _indie/faktura-pdf-report:

Přehled faktur ve formátu PDF
~~~~~~~~~~~~~~~~~~

Jakmile je faktura ověřena a odeslána, lze vytisknout zprávu o faktuře ve formátu PDF.
zahrnuje: abbr: IRN (Referenční číslo faktury), guilabel: Ack. No (číslo potvrzení) a
„Datum uznání“ (ack. date), „QR kód“ a „Certifikát“. Tyto údaje potvrzují, že faktura je platná.
Daňový doklad.

.. obrázek: indie/faktura.png
:alt: IRN a čárový kód

... _indiadisruption:

Zrušení faktury v elektronické podobě
~~~~~~~~~~~~~~~~~~~~~~

Pokud chcete zrušit elektronickou fakturu, přejděte na záložku „Další informace“ a vyplňte
Zadejte důvod zrušení do políčka „Důvod zrušení“ a komentář do pole „Poznámky“. Pak stiskněte tlačítko „Požádat o
Zrušení EDI“. Stav pole „Elektronická fakturace“ se změní na „Zrušeno
Zrušit.

.. důležité::
Provedením takového kroku se ruší oba dokumenty, a to :ref:`daňový doklad elektronicky <india/e-invoicing>`
<Indie/elektronický nákladní list>.

.. obrázek:indie/zrušení faktury.png
:alt: důvod a poznámky k zrušení

.. poznámka::
   - Pokud chcete zrušit odvolání před zpracováním faktury, klikněte na tlačítko:guilabel:`Zavolat
Off EDI Cancellation`.
   - Jakmile požádáte o zrušení elektronické faktury, Odoo automaticky zašle podepsaný soubor ve formátu JSON.
NIC portál fakturace. Klikněte na „Zpracovat nyní“, pokud chcete zpracovat
fakturu ihned.

..._indie/elektronické faktury - negativní řádky:

Zpracování záporných položek v elektronických fakturách
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Černé čáry se obvykle používají k zobrazení slev nebo úprav spojených s konkrétními položkami.
produktů nebo celosvětových slev. Portál vlády zakazuje zasílání dat s negativními hodnotami.
takže je potřeba převést podle kódu HSN a sazby DPH. To se provádí
automaticky prostřednictvím Odoo.

.. příklad::

Pojďme si ukázat příklad.

   +---------------------------------------------------------------------------------------------------+
|                                            **Podrobnosti o produktu**                                        |
   +=======================+==============+==================+==============+==============+===========+
|  Název produktu       |   Kód HS        |  bez DPH         |  Počet kusů      |  Sazba DPH      | Celkem
   +-----------------------+--------------+------------------+--------------+--------------+-----------+
|Produkt A            | 123456      | 1.000          | 1           | 18 %         | 1.180
   +-----------------------+--------------+------------------+--------------+--------------+-----------+
|Produkt B            | 239345      | 1 500         | 2           | 5 %         | 3 150    |
   +-----------------------+--------------+------------------+--------------+--------------+-----------+
|Sleva na produkt A | 123456       | -100          | 1           | 18 %        | -118      |
   +-----------------------+--------------+------------------+--------------+--------------+-----------+

Tady je transformovaná reprezentace:

   +-------------------------------------------------------------------------------------------------------------+
|                                               **Podrobnosti o produktu**                                                |
   +==================+==============+==================+==============+==============+==============+===========+
|  Název produktu  |   Kód HS  |  bez DPH  |  Množství  |  Sleva  |  Sazba DPH  | Celkem
   +------------------+--------------+------------------+--------------+--------------+--------------+-----------+
|Produkt A       | 123456      | 1.000          | 1            | 100         | 18 %        | 1,062    |
   +------------------+--------------+------------------+--------------+--------------+--------------+-----------+
|Produkt B         | 239345      | 1 500           | 2           | 0           | 5 %          | 31 500
   +------------------+--------------+------------------+--------------+--------------+--------------+-----------+

V této konverzi byly negativní linie převedeny na pozitivní slevy, které byly zachovány.
přesné výpočty založené na kódu HSN a sazbě DPH. To zajišťuje snadnější a
standardizované zobrazení v záznamu o elektronické fakturaci.

..._indie/ověřit-elektronickou fakturu

Kontrola faktur v systému GST
~~~~~~~~~~~~~~~~~~~~~~~~~~

Po odeslání elektronické faktury můžete ověřit, zda byla podepsána systémem GST e-Invoice.
webové stránky samotné.

#Stáhněte si soubor JSON z příloh. Najdete ho v chatu k příspěvku, který je s tímto příspěvkem spojený.
faktura.
#Otevřete portál „NIC e-fakturace <https://einvoice1.gst.gov.in/>“ a přejděte na
:menu_vyber:`Hledat --> Zkontrolovat podepsaný fakturační doklad“;
#Vyberte soubor ve formátu JSON a odešlete jej.

.. obrázek::india/verify-invoice.png
:alt: vyberte soubor JSON pro ověření faktury

Pokud je soubor podepsaný, zobrazí se potvrzující zpráva.

.... obrázek:india/podepsaný-faktura.png
:alt: ověřená faktura v elektronické podobě

... _indie/e-waybill:

E-Way Bill
==========

... _indie/e-waybill-setup:

Nastavení
-----

Odoo je v souladu s požadavky indického systému elektronické cestovní faktury pro DPH (e-waybill).

.. _india/e-waybill-api:

Registrace do systému API na portálu e-Waybill
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Musíte se zaregistrovat na portálu elektronického fakturačního dokladu NIC (Národní informační centrum)
**Přístupové údaje API**. Potřebujete je k tomu, abyste si v aplikaci Odoo nastavili účetní program.
<Indie/konfigurace e-waybill>.

#Přihlaste se do portálu „E-Way Bill“ na adrese https://ewaybillgst.gov.in/.
:guilabel:`Přihlášení“ a zadáním svého „Uživatelského jména“ a „Hesla“.
#Otevřete si v menu „Přihlášení“ možnost „Registrace – pro GSP“.
#Klikněte na tlačítko „Odeslat SMS“. Jakmile obdržíte kód na svém registrovaném mobilním čísle,
zadejte ji a klikněte na „Přijmout SMS“.
#Zkontrolujte, zda společnost „Tera Software Limited“ již není na seznamu registrovaných poskytovatelů softwaru a ERP. Pokud ano, použijte
přihlášení do portálu NIC. V opačném případě postupujte podle dalších kroků;

.. obrázek: indie/e-waybill-gsp-list.png
:alt: Seznam registrovaných GSP/ERP

#Vyberte možnost „Přidat/Nový“, vyberte „Tera Software Limited“ jako název GSP a vytvořte
:guilabel:`Uživatelské jméno“ a „Heslo“ pro vaši API a klikněte na „Přidat“.

.. obrázek: indie/e-waybill-registration-details.png
:alt: Registrace podrobností o API

.. _indie/konfigurace e-waybillu:

Konfigurace v Odoo
~~~~~~~~~~~~~~~~~~~~~

Pro nastavení služby E-Way bill přejděte na: „Účetnictví --> Konfigurace --> Nastavení“
-->Indický elektronický přepravní list --> Nastavení e-waybill“ a zadejte své uživatelské jméno
:guilabel:`Heslo“.

.. obrázek:indie/e-waybill-configuration.png
:alt:Nastavení e-way billu v Odoo

.. _india/e-waybill-workflow:

Průběh práce
--------

.. _indie/e-waybill-send:

Vystavte fakturu E-Way.
~~~~~~~~~~~~~~~~~~

Pro odeslání faktury EET potvrďte zákaznickou fakturu/dodací list a klikněte na „Odeslat E-Way
faktura.

.. obrázek:indie/tlačítko-pro-odeslání-e-waybillu.png
:alt:Tlačítko pro zaslání e-dokumentu na fakturách

..._indie/fakturaci-e-way:

Kontrola faktury
~~~~~~~~~~~~~~~~~~

Jakmile byla faktura vystavena a odeslána pomocí tlačítka „Odeslat E-Way fakturu“, obdržíte potvrzení.
zobrazí se zpráva.

.. obrázek: indie/e-waybill-process.png
:alt:Indická potvrzení o elektronickém faktuře

.. poznámka::
   - Soubor podepsaný pomocí JSON najdete v přílohách zprávy.
   - Odoo automaticky po nějaké době nahraje podepsaný soubor ve formátu JSON na portál vlády. Klikněte
:guilabel:`Zpracovat nyní“ pokud chcete hned zpracovávat fakturu/fakturační dopis.

Přehled faktur ve formátu PDF
~~~~~~~~~~~~~~~~~~

Poté, co jste podali elektronickou cestovní fakturu, můžete tisknout účet za přepravu v PDF. Účet obsahuje
Číslo E-way bill a platnost E-way bill.

.. obrázek:indie/e-waybill-invoice-report.png
:alt:Číslo a datum potvrzení přepravního listu

... _india/e-waybill-cancellation:

Zrušení e-way bill
~~~~~~~~~~~~~~~~~~~~~~~

Pokud chcete zrušit E-way bill, přejděte na záložku „E-Way Bill“ v souvisejících
fakturu a vyplnit pole „Důvod zrušení“ a „Poznámky k zrušení“. Pak
klikněte na „Požádat o zrušení EDI“.

.. důležité::
Provedením takového kroku se zruší oba :ref:`elektronické faktury <india/e-invoicing>` (pokud je to možné).
:ref:`Faktura E-Way <indie/e-waybill>.

.. obrázek:indie/e-waybill-cancellation.png
:alt: Důvod a poznámky k zrušení

.. poznámka::
   - Pokud chcete zrušit odvolání před zpracováním faktury, klikněte na:guilabel:`Zrušit
„EDI Zrušení“.
   - Jakmile požádáte o zrušení E-Way Billu, Odoo automaticky odesílá soubor s podepsaným JSONem na
vládní portál. Klikněte na „Zpracovat fakturu“ pokud chcete zpracovat fakturu.
ihned.

.._indie/e-waybill-sklad:

Vytváření e-dokladů z faktur a dodacích listů
----------------------------------------------------

.. poznámka::
Zajistěte, aby modul **Sklad E-Way bill** byl nainstalován:ref:`<general/install>`.
:ref:`Nastavení E-Way bill je dokončeno <india/e-waybill-setup>`.

Vytvořit E-Way bills z:
v sekci „Denní operace“ v zásobách.
Aplikaci nainstalujte podle těchto kroků:

#. Přejděte do sekce „Skladové zásoby“ – „Provoz“ – „Dodávky“.
Vyberte operaci „Příjmy“ a zvolte existující fakturu nebo vytvořte novou.

#Klikněte na tlačítko „Vytvořit fakturu/fakturu“.

.. poznámka::
Pro vytvoření E-way billu:

      - Dodací objednávka musí být ve stavu „hotovo“ (tj. ověřená).
      - Pokladní doklad musí mít stav „Připraveno“ nebo „Dokončeno“.

#Klikněte na tlačítko „Vytvořit e-Waybill“ a ověřte si e-Waybill a pošlete jej do NIC e-Way.
portál s účty.

.......
Pro použití faktury E-way jako dokladu pro dodání zboží bez jeho odeslání do NIC
Portál e-Waybill, klikněte na „Použít jako fakturu“.

K tisku faktury nebo pokladního dokladu klikněte na ikonu „fa-cog“ a vyberte
:icon:`fa-print` :guilabel:`Ewaybill / Dodací lístek“.

..

Indická kontrola stavu DPH
=========================

Modul „Indický – Zkontrolujte stav DPH“ umožňuje ověřit stav
:zkratka GSTIN (identifikační číslo daně z přidané hodnoty) přímo v Odoo.

Pro ověření stavu čísla DPH kontaktu přejděte na formulář zákazníka/dodavatele a klikněte
Vedle pole „GSTIN“ je tlačítko „Zkontrolovat stav DPH“.

Pro ověření stavu čísla DPH zadaného v faktuře/faktuře přejděte na fakturu/fakturu a klikněte
tlačítko „Obnovit“ (ikonka „fa-refresh“) vedle pole „Stav GST“.

.. obrázek:indie/faktura-s-dph.png
:alt:Zkontrolujte stav DPH faktury

Zobrazuje se oznámení, které potvrzuje aktualizaci stavu a datum ověření GSTIN.
jsou zaznamenány v chatu kontaktu.

.._indie/gst:

Podání indického daňového přiznání
========================

.. _indie/gst-api:

Povolit přístup k API
-----------------

Chcete-li podat daňové přiznání v Odoo, musíte nejprve povolit přístup k API na portálu GST.

#Přihlaste se do portálu GST („GST Portal <https://services.gst.gov.in/services/login>“), zadáním svého
:guilabel:`Uživatelské jméno“ a :guilabel:`Heslo“, přejděte na svůj profil v sekci „Můj profil“.
menu**;

.. obrázek::india/gst-portal-my-profile.png
:alt:Klikněte na Můj profil v profilu

#Vyberte možnost „Správa přístupu k API“ a poté klikněte na „Ano“, abyste povolili přístup k API.

.... obrázek::india/gst-portal-api-yes.png
:alt:Klikněte na Ano

.. poznámka::
Je doporučeno nastavit hodnotu :guilabel:`Doba platnosti` na :guilabel:`30 dní`, aby se předešlo potřebě
časté přihlašování tokenů.

#Tímto způsobem se zobrazí možnost „Délka“ v rozevíracím seznamu. Vyberte délku svého
preferenci a klikněte na tlačítko „Potvrdit“.

.. _india/gst_configuration:

Indická služba GST v Odoo
--------------------------

Jakmile na portálu GST povolíte přístup k API (viz india/gstr_api), můžete si nastavit
:guilabel:`Služba indické DPH“ v Odoo.

Přejděte do sekce „Účetnictví“ – „Konfigurace“ – „Nastavení“ – „Indická služba DPH“.
:guilabel:`Uživatelské jméno GST“. Klikněte na tlačítko :guilabel:`Odeslat SMS“, zadejte kód a nakonec
:validace:

.. obrázek:: india/gst-setup.png
:alt:Prosím, zadejte své uživatelské jméno portálu GST jako Username

.. _indie/gst_workflow:

Podání daňového přiznání
------------------

Pokud máte správně nakonfigurovaný „Indian GST Service“, můžete podat daňové přiznání. Přejděte na
„Účetnictví“ -> „Zprávy“ -> „Indie“ -> „Období podání DPH“ a vytvořit nový **GST
Vraťte se na období, pokud neexistuje. V Odoo je soubor vrácení DPH zpracován ve třech krocích:

.. poznámka::
**Periodicita daňového přiznání** může být
:doc:`podle přání uživatele <../accounting/reporting/tax_returns>
potřebám.

..._indie/gst-1:

Odešlete formulář GSTR-1
~~~~~~~~~~~

#Klikněte na tlačítko „Zpráva GSTR-1“ a ověřte si zprávu před
a nahrát ho na **portál GST**.

.... obrázek: indie/gst-gstr-1-overit.png
:alt:GSTR-1 ověřit

.. poznámka::
Systém provádí základní ověření, aby se ujistil, že požadavky portálu GST jsou splněny.
Možné problémy zahrnují:

      - **Špatná daňová aplikace:** Daňový typ neodpovídá :guilabel:`Daňové pozici`
místo :guilabel:`IGST“ pro transakce mezi státy použito :guilabel:`CGST/SGST“.
:guilabel:`IGST“ namísto „CGST/SGST“ pro transakce v rámci státu.
      - **Chybějící kód HS:** K produktu nebyl přiřazen žádný kód HS.
      - **Nesprávný kód HS pro služby:** Kód HS pro službu nezačíná na „99“ nebo je
Není správné.
      - **Nesoulad s kódem jednotkové ceny (UQC):** Kód jednotkové ceny (UQC) neodpovídá indickým standardům DPH.

Pokud selže jakákoliv kontrola, systém upozorní uživatele varováním a vyznačí chybu.
rozdíly a poskytnout přímý odkaz na postižené řádky.

.. obrázek: indie/gst-gstr-1-validace.png
:alt:Varování při ověřování GSTR-1

#Klikněte na tlačítko „Vytvořit“ a zobrazí se vám výsledky ve formátu tabulky.

.... obrázek: indie/gst-gstr-1-generovat.png
:alt:GSTR-1 vygenerovat

.... obrázek::india/gst-gstr-1-spreadsheet-view.png
:alt: Zobrazení tabulky v aplikaci GSTR-1

#Pokud je správný report GSTR-1, pak klikněte na tlačítko „Odeslat do GSTN“ a odeslat jej.
portálu. Stav zprávy GSTR-1 se změní na „Odeslání“.

.... obrázek: indie/gst-gstr-1-zasilani.png
:alt:GSTR-1 v stavu odeslání

#Po několika sekundách se stav zprávy GSTR-1 změní na :guilabel:`Čeká na
Status. To znamená, že hlášení GSTR-1 bylo odesláno na portál GST a je
ověřené na portálu GST.

.... obrázek::india/gst-gstr-1-waiting.png
:alt:GSTR 1 v stavu čekající na status

#Jakmile je zpráva odeslána, stav se buď změní na :guilabel:`Sent`, nebo :guilabel:`Error
v faktuře. Stav „Chyba v faktuře“ ukazuje, že některé faktury nejsou
musí být správně vyplněny, aby mohly být ověřeny na portálu GST.

   - Pokud stav formuláře GSTR-1 je:guilabel:„Odesláno“, znamená to, že váš formulář GSTR-1 je připravený k
musí být podány na portálu GST.

.. obrázek: indie/gst-gstr-1-sent.png
:alt:GSTR-1 Odesláno

   - Pokud stav formuláře GSTR-1 je:guilabel:Chyba v faktuře, lze kontrolovat faktury
chyby v chatu. Po vyřešení problémů může uživatel kliknout
:guilabel:`Přidat do GSTN“ a znovu odeslat soubor na **portál GST**.

.... obrázek::india/gst-gstr-1-error.png
:alt:Chyba v faktuře

#Klikněte na tlačítko „Uzavření“ po podání hlášení GSTR-1 na portálu GST.
status zprávy se změní na „Podáno“ v Odoo.

.. obrázek: indie/gst-gstr-1-podaný.png
:alt:GSTR-1 v stavu Pending

..._indie/gst-2b:

Přijmout GSTR-2B
~~~~~~~~~~~~~~~

Uživatelé si mohou stáhnout zprávu GSTR-2B na portálu GST. Tato automaticky vyrovnává
výkaz GSTR-2B s vašimi fakturami v Odoo.

#Klikněte na tlačítko „Získat souhrn GSTR-2B“ a zobrazí se vám souhrn GSTR-2B. Po několika sekundách
status zprávy se změní na „Čeká na přijetí“. To znamená, že Odoo se snaží
obdržet zprávu GSTR-2B ze stránky GST.

.... obrázek: indie/gst-gstr-2b-čeká.png
:alt: GSTR-2B v očekávání přijetí

#Jakmile se po několika sekundách stav GSTR-2B změní na „Vyžaduje údržbu“, zobrazí se vám ikona s názvem „Potřebuje servis“:
Proces „Zpracováno“. To znamená, že Odoo se snaží shodovat **GSTR-2B** report s vašimi fakturami v Odoo.

.. obrázek: india/gst-gstr-2b-processed.png
:alt: GSTR-2B v očekávání přijetí

#Jakmile je hotovo, stav zprávy GSTR-2B se změní na buď „Souhlasí“ nebo
:guilabel:`Částečně shodné“;

   - Pokud je stav :guilabel:`Matched`:

.. obrázek: indie/gst-gstr-2b-matched.png
:alt:GSTR-2B Matched

   - Pokud je stav :guilabel:`Partially Matched“, můžete zkontrolovat a upravit faktury.
kliknutím na tlačítko „Zobrazit vyrovnané faktury“. To zobrazí kategorizované nesrovnalosti.
jako faktury chybějící v Odoo nebo GSTR-2. Po provedení nezbytných oprav klikněte
:guilabel:`re-match“ aktualizovat shodu a zajistit přesnost před konečným schválením
zpráva.

.. obrázek:: india/gst-gstr-2b-částečně.png
:alt:GSTR-2B částečně shodný

... _indie/gst-3:

Zpráva o GSTR-3
~~~~~~~~~~~~~

Hlášení GSTR-3 je měsíční souhrn prodejů a nákupů.
Tento návrat je automaticky vygenerován extrahováním informací z formulářů GSTR-1 a GSTR-2.

#Uživatelé mohou porovnat zprávu GSTR-3 s dostupnou zprávou GSTR-3 na
portálu GST kliknutím na „Zprávu o GSTR 3“.

#Jakmile byl uživatelem ověřený report GSTR-3 a daňová částka na portálu GST
je zaplacen. Jakmile je platba provedena, lze tento záznam uzavřít kliknutím na :guilabel:`Závěrečný vstup`.

.. obrázek:: india/gst-gstr-3-not_filed.png
:alt:GSTR-3

#V poli „Závěrečný vstup“ zadejte částku DPH zaplacenou na portálu GST pomocí chalan a
Klikněte na tlačítko „Vytvořit závěrečný záznam“ a poté klikněte na tlačítko „Zavřít“.

.. obrázek:indie/gst-gstr-3-post.png
:alt:GSTR-3 Post Entry

#Jakmile je podání odesláno, stav zprávy GSTR-3 se změní na „Podáno“.

.... obrázek:indie/gst-gstr-3-filed.png
:alt:GSTR-3

.. _indie/gst_reporty:

Daňové přiznání
===========

.. _indie/gst-1_zpravodajství:

Hlášení GSTR-1
-------------

Hlášení GSTR-1 je rozděleno do sekcí. Zobrazuje základní částku
:zkratka CGST (Dáň z přidané hodnoty státu), :zkratka SGST (Dáň z přidané hodnoty států)
:zkratka IGST (integrovaná daň z přidané hodnoty), a :guilabel:„CES“ pro každou sekci.

.... obrázek:india/gst-gstr-1-sale-report.png
:alt: Hlášení GSTR-1

... /indie/gst-3-report/:

Zpráva o GSTR-3
-------------

Zpráva o výsledku kontroly „GSTR-3“ obsahuje různé části:

- Podrobnosti o dodávkách vstupujících a odcházejících, které jsou předmětem **zpětného zdanění**
- Příslušný: zkratka ITC (daňový kredit).
- Hodnoty výjimek „bez daně“, „s nulovou sazbou“ a „bez DPH“.
- Podrobnosti o dodávkách mezi státy pro nezaregistrované osoby.

.. obrázek::indie/gst-gstr-3-report.png
:alt: Zpráva o stavu GSTR-3

Zpráva o zisku a ztrátě (VÝNOSY A ZTRÁTY)
---------------------------

Toto je zpráva o zisku a ztrátě, která zobrazuje zůstatky za **Začátek obchodu** a
„Zavírací zásoba“. Pomáhá uživatelům, kteří používají kontinentální účetnictví, přesně určit náklady na
zboží (tj. otevřený sklad + nákupy během období - uzavřený sklad).

.... obrázek: indie/ziskovost-a-ztrátovost.png
:alt: Zpráva o zisku a ztrátě

.._indie/tds-tcs-pratelsky-povoleni:

Aktivní hlídání prahu TDS/TCS
=======================

Provize TDS a TCS jsou daňovými položkami.
V indickém právu vyvolaný při překročení stanovené hranice transakcí. Tento upozornění
Uživatele upozorňuje na překročení stanovených limitů a aplikaci
vhodného TDS/TCS.

Chcete-li si Odoo nastavit tak, aby vám poradil, kdy máte aplikovat DDT/TCS, nastavte sekci „DDT/TCS“
pole na příslušném účtu v rozvaze. Odoo zobrazí upozornění s nápadem
oddíl TDS/TCS, pod který může být uplatněna daň při vystavení faktury nebo účtu.

Konfigurace
-------------

#Navigujte na: „Účetnictví“ -> „Konfigurace“ -> „Nastavení“.
#V sekci „Integrace Indie“ zapněte funkci „TDS a TCS“.
#Navigujte na: menu „Účetnictví“ -> „Konfigurace“ -> „Skladová kniha“.
#Klikněte na požadovaný účet a nastavte pole „Sazba DDT / TCS“.

.. poznámka::
Sekce TDS/TCS jsou přednastaveny s hodnotami prahových limitů. Pokud potřebujete tyto limity změnit,
limity, přejděte na „Účetnictví“ -> „Nastavení“ -> „Daně“. V části „Další nastavení“
záložce Možnosti klikněte na ikonu :icon:`fa-arrow-right` :guilabel:`(interní odkaz)`
:guilabel:`Sekce“ pole.

.. obrázek: india/tds-tcs-section-modify.png
:alt: Modifikace sekce TDS/TCS

Použití TCS/TDS na fakturách a účtech
--------------------------------------

Na základě účtu použitého na faktuře pro klienta nebo dodavatele ověřuje Odoo hranici TCS/TDS.
limit. Pokud je uvedený limit v sekci „TCS/TDS“ účtu překročen, Odoo
zobrazí upozornění, které navrhuje použití vhodných TCS/TDS. Upozornění zmizí poté, co
Aplikuje se TCS/TDS.

.. obrázek:india/tcs-warning.png
:alt:Rada TCS

Sazba DPH se aplikuje přímo na řádky faktury. Chcete-li použít sazbu TDS, klikněte
:guilabel:"Vstup TDS" chytrý tlačítko na faktuře dodavatele/platby. V okně lze specifikovat
podrobnosti o DPH. Potvrďte vstup, abyste mohli aplikovat DPH.

.. obrázek:indie/tds-apply.png
:alt: Příloha TDS

V Odoo se agregovaný celkový počet vypočítává pro partnery s identickým číslem PAN, a to v rámci všech
pobočky společnosti.

.. příklad::

...... seznamová tabulka::
:hlavičkové řádky: 1
:šířky: 10 20 10 20 15

      * – **Branča**
        - **Klient**
        - Faktura
        - *Částka transakce (Rs)*
        - **Číslo PAN**
      * – IN – MH
        - XYZ Enterprise – GJ
        - Faktura č. 1
        - ₹50,000
        - ABC-PX1234E
      * – IN – MH
        - XYZ Enterprise – GJ
        - Faktura 2
        - ₹30,000
        - ABC-PX1234E
      * – IN – MH
        - XYZ Enterprise - MH
        - Faktura 3
        - ₹40,000
        - ABC-PX1234E
      * – IN – DL
        - XYZ Enterprise – GJ
        - Faktura č. 4
        - ₹20,000
        - ABC-PX1234E
      * – IN – GJ
        - XYZ Enterprise - MH
        - Faktura 5
        - ₹60,000
        - ABC-PX1234E

   -  *Součet celkem* = 50 000 + 30 000 + 40 000 + 20 000 + 60 000 = ₹200 000
   -  Součet pro všechny zákazníky (XYZ Enterprise - GJ, MH, DL), kteří sdílejí stejné číslo PAN
ABCX1234E v celé síti je 200 000 rupií.
