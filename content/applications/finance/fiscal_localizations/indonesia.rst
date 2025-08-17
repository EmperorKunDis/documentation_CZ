=========
Indonésie
=========

... _lokalizace_indonésie/e-faktury:

Modul e-faktury
===============

Modul E-Faktura je nainstalován s indonéskou lokalizační sadou výchozí. Umožňuje
jedna pro vytváření souboru CSV pro jednu fakturu nebo pro sadu faktur, které lze nahrát do
Aplikace **Daňový úřad - e-Faktura**.

.. _lokalizace_indonésie/npwp_nik:

Nastavení NPWP/NIK
-----------------

- | **Vaše společnost**
|Tato informace se používá v lince FAPR ve formátu souboru efektů. Musíte nastavit DPH
číslo na příslušném partnerovi vaší společnosti Odoo. Pokud ne, nebude možné vytvořit
e-fakturu z faktury.
- |**Vaši klienti**
|Zaškrtněte políčko ID PKP, abyste mohli vystavit fakturu pro zákazníka. Můžete použít DPH
pole na kontakt zákazníka, kde je potřeba zadat DIČ pro generování souboru e-Faktura. Pokud vaše
zákazník nemá živnostenské oprávnění, zadá se do stejného pole DPH jen číslo OP.

.. obrázek: indonesia/indonesia-partner-nik.png
:synchronizace: střed

... _lokalizace_indonésie/využití_elektronických_faktur:

Použití
-----

... _lokalizace_indonésie/daňový doklad sn:

Vytvořit sériové číslo daňového dokladu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Přejděte na „Účetnictví > Zákazníci > e-Faktura“. Chcete-li exportovat
pokud chcete vystavit fakturu pro indonéskou vládu jako e-Faktura, musíte zde zadat rozsah
číslo, které vám přidělil stát. Když ověříte fakturu, bude k ní přiřazeno
podle těchto rozsahů. Poté můžete filtrovat faktury k exportu v
v seznamu faktur a klikněte na položku *Akce* a poté na *Stáhnout e-fakturu*.
#Po obdržení nových sériových čísel od indonéského finančního úřadu můžete vytvořit sad
Daňového dokladu seřadit podle pohledu na seznam. Stačí zadat minimální a maximální hodnoty.
Maximální číslo každé skupiny sériových čísel a Odoo automaticky formátuje číslo na 13 míst.
požadované indonéskou daňovou správou.
#Na přepážce je k dispozici počítadlo, které vám řekne, kolik čísel z dané skupiny ještě nebylo použito.

.. obrázek:: indonesia/indonesia-sn-count.png
:align:center

.. _lokalizace_indonésie.csv:

Vytvořit soubor CSV faktury pro jednotlivou nebo hromadnou fakturu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Vytvořte fakturu z menu „Účetnictví“ - „Zákazníci“ - „Faktury“. Pokud je faktura
Kupujícího zemí je Indonésie a kupující je nastaven jako *ID PKP*, Odoo vám umožní
vytvořit e-fakturu.
#Nastavte kód transakce pro fakturu v elektronické podobě. Existují omezení související s kódem transakce a
typ DPH uvedený v řádku faktury.

.... obrázek: indonesia/indonesia-kode-transaksi.png
:align:center

#Odoo automaticky vybere další volné číslo sériového čísla ze seznamu čísel e-faktury (viz
(viz část výše (:ref:`<localization_indonesia/tax_invoice_sn>`) a vytvořit fakturu.
číslo jako součet kódu transakce a sériového čísla. Můžete si to prohlédnout na faktuře
formulář v podobě stránky *Další informace* ve sloupci *Daň z přidané hodnoty*.

....... obrázek:: indonesia/indonesia-e-faktury-sn.png
:align:center

#Jakmile je faktura vystavena, můžete vygenerovat a stáhnout e-Fakturu z nabídky *Akce*.
položka *Stáhnout fakturu v elektronické podobě*. Zaškrtávací políčko *Vytvořeno CSV* bude vybrané.

.. obrázek: indonesia/indonesia-csv-vytvoreny.png
:align:center

#Můžete vybrat více faktur v seznamovém zobrazení a vytvořit soubor e-Faktura.csv.

.. _lokalizace_indonésie/kód_transakce_fp:

Kód transakce FP (Transakční kód)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Následující kódy jsou dostupné při generování e-Faktury.
- 1. Pro neplátce DPH (běžný zákazník)
- 2. Pro správce daně
- 3. Pro ostatní sběratele než státní podniky
- 04 DPP Nilai Lain (PPN 1 %)
- 06. Převod jiného druhu (zahraniční turista)
- 07 Zpětný převod, který není zdaněn (speciální ekonomická zóna / Batam)
- 08 Vydání, které je osvobozeno od cla na dovoz určitého zboží
- Článek 16D zákona o dani z přidané hodnoty

.. _lokalizace_indonésie/vyměnit fakturu:

Oprava faktury, která byla odeslána a stáhla se: funkce opravy faktury
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zrušte původní chybný doklad v Odoo. Například změníme kód transakce na
01 až 03 pro INV/2020/0001.
#Vytvořte novou fakturu a nastavte zrušenou fakturu v poli *Změnit fakturaci*. V tomto poli
Můžeme vybírat pouze faktury v stavu Zrušeno od stejného dodavatele.
#Jakmile potvrdíte, Odoo automaticky použije stejný sériový číslo e-Faktury jako zrušené a
vystavená faktura, která nahradila třetí číslici původního sériového čísla hvězdičkou (*1*) (jak bylo požadováno).
nahradit fakturu v aplikaci e-Faktur.

.. obrázek: indonesia/indonesia-replace-invoice.png
:align:center

..._lokalizace_indonésie/reset_e-faktury:

Oprava faktury, která byla odeslána, ale stále nebyla stažena: Obnovení e-Faktury
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Zrušte fakturu a vytvořte novou.
#Klikněte na tlačítko „Obnovit fakturu“.
#. Sériové číslo bude deaktivováno a my tak budeme moci fakturu vrátit do stavu návrhu, upravit ji
a přidělit nový sériový číslo.

.. obrázek: indonesia/indonesia-e-faktur-reset.png
:align:center

... _lokalizace_indonésie/qris-qr:

QR kód na fakturách - QRIS
========================

„QRIS“ je digitální platební systém, který umožňuje zákazníkům provádět platby
platby pomocí skenování QR kódu z jejich oblíbené elektronické peněženky.

.. důležité::
Podle dokumentace k „QRIS API <https://qris.online/api-doc/create-invoice.php>“
QRIS platí pouze 30 minut. Proto není součástí zpráv
odeslané zákazníkům a je k dispozici pouze na portálu zákazníka.

Aktivujte QR kódy
-----------------

Přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Nastavení“. Pod položkou „Zákazník
V sekci platby aktivujte funkci :guilabel:`QR kódy`.

Konfigurace účtu QRIS
-------------------------------

Přejděte na: `Kontakty --> Konfigurace --> Bankovní účet` a vyberte bankovní účet pro
které chcete aktivovat QRIS. Zadejte klíč a identifikační číslo QRIS API
na základě informací poskytnutých QRIS.

.. důležité::
V kontaktním formuláři musí být zemi uživatele nastaveno na „Indonésie“.

.. obrázek: indonesia/qris-setup.png
:alt: Konfigurace účtu QRIS

.. viz též:
:doc:`../účetnictví/banka`

Konfigurace bankovního časopisu
--------------------------

Přejděte na záložku „Účetnictví“ – „Nastavení“ – „Knihy“, otevřete bankovní knihu a pak vyplňte
v poli „Číslo účtu“ a „Banka“ pod záložkou „Účetní případ“.

.. obrázek: indonesia/journal-bank-config.png
:alt: Konfigurace bankovního časopisu

Vystavujte faktury s QR kódy QRIS
---------------------------------

Při vytváření nové faktury otevřete záložku „Další informace“ a nastavte položku „Způsob platby“.
Možnost QR-kódu nahradit QRIS.

.. obrázek: indonesia/faktura-qris.png
:alt: Vyberte možnost QR kódu QRIS

Zajistěte, aby pole „Příjemce banky“ bylo nastavené na tuto instituci, protože Odoo používá toto pole k
generovat QR kód QRIS.
