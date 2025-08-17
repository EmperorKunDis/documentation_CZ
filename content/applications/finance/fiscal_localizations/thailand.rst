========
Thajsko
========

Konfigurace
=============

Instalujte balíček 🇹🇭 Thailand, abyste získali všechny
charakteristika thajské lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * --:guilabel:„Thajsko – Účetnictví“
     - „l10n_th“
     - Výchozí:balík lokalizace daní:
   * -- :guilabel:„Účetní zprávy Thajska“
     - l10n_th_reports
     - Zemědílné účetní závěrky

.. obrázek:thailand/moduly.png
:alt: Lokální moduly pro Thajsko

Účetní kniha a daně
===========================

Daňové balíčky pro místní fiskální úpravy v Thajsku zahrnují následující daně:

- DPH 21 %
- Bez DPH
- Srážková daň
- Srážková daň z příjmu

Daňový přehled
==========

Odoo umožňuje uživatelům vytvářet soubory Excel, které lze použít k podání DPH na finančním odboru
Thajsko.

Přiznání k dani z přidané hodnoty a k dani z nabytí nemovitých věcí
-----------------------------

Pro vytvoření zprávy o daních z prodeje a nákupu přejděte na: „Účetnictví -> Zprávy -> Daň
Zpráva. Vyberte konkrétní čas nebo časový úsek v daňovém výkazu a klikněte
„DPH-202-01“ (xlsx) pro daň z přidané hodnoty a „DPH-202-02“ (xlsx) pro daň z přidané hodnoty.

.. obrázek:thailand/tax-report.png
:alt:Thajské zprávy o dani z přidané hodnoty

Zadržení přiznání k dani z příjmů fyzických osob
--------------------------

Výkaz o příjmech a výdajích zveřejňuje souhrnné částky sražených daní z příjmů právnických osob.
daňové přiznání (výdaje) z faktur od dodavatelů podle položky „PND 53 (TH)“.
:guilabel:`PND3 (TH)` daňové hlášení. Je nainstalováno s thajským jazykem.

.. obrázek::thailand/pnd-report.png
:alt:PND daňové přiznání

.. poznámka::
Zaměstnanecké srážky z příjmu zaměstnavatele (v rámci ČR) jsou daní používanou v případě, že společnost
srazil daň z příjmů ze služeb „**Osobní (PND3)**“ nebo „**Korporátní (PND53)**“.
pronájem, půjčování, doprava, pojištění, správní poplatky, poradenství apod.

Daňový přehled PND umožňuje uživatelům vytvořit soubor CSV pro faktury, které lze nahrát na
„Příprava RD pro aplikaci Thajského elektronického podání (e-Filing) <https://efiling.rd.go.th/rd-cms/>“.

Pro vytvoření souboru PND ve formátu CSV přejděte na: „Účetnictví - Zprávy - Daňový výkaz“ a vyberte
určité datum nebo časový úsek v daňovém přiznání a klikněte na :guilabel:`PND3` nebo :guilabel:`PND53`.

Vytváří soubory „Zpráva o dani PND3.csv“ a „Zpráva o dani PND53.csv“, které obsahují všechny
Výdajový fakturační řádek s příslušnou srážkovou daní.

.. obrázek:thailand/pnd3-pnd53.png
:alt:Soubory PND3 a PND53 ve formátu CSV

.. varování:
Odoo nemůže generovat přímo zprávu PND nebo PDF, ani potvrzení o sražené dani.
Exportovat musíte vytvořené soubory :file:`Tax Report PND3.csv` a :file:`Tax Report PND53.csv`.
do externího nástroje pro převod na sestavu daňového výměru nebo soubor PDF.

Daňový doklad
===========

Přehled o DPH ve formátu PDF lze vytisknout z Odoa pomocí modulu Fakturace. Uživatelé
mít možnost tisknout PDF faktury pro běžné i daňové doklady.
Daňové doklady lze v Odoo zobrazit kliknutím na tlačítko „Vytisknout faktury“. Běžné faktury mohou uživatelé
vytisknout jako „daňový doklad“ kliknutím na tlačítko „Nastavení“ - „Tisk“ - „
Faktura pro obchodní účely.

.. obrázek:thailand/faktura-dph.png
:alt: Tisk faktury

Nastavení hlavní kanceláře nebo pobočky
----------------------------------

Informace o sídle společnosti a čísle pobočky lze zadat v aplikaci Kontakty.
v aplikaci otevřete kontaktní formulář společnosti a pod záložkou „Prodej a nákup“:

- Pokud je kontakt identifikován jako pobočka, zadejte do pole
:guilabel:`Firma“ pole.
- Pokud je kontakt hlavním sídlem, nechte pole „Identifikátor společnosti“ prázdné.

.. obrázek:thailand/kontakt.png
:alt: Sídlo společnosti / pobočka

.. tip::
Tyto informace se používají v PDF hlášení o dani z přidané hodnoty a ve vývozu PND daňového přiznání.

QR kód PromptPay na fakturách
=============================

QR kód **PromptPay** je QR kód, který lze přidat na faktury a umožnit zákazníkům platit své účty.
fakturami pomocí mobilní aplikace podporující službu PromptPay. QR kód je generován na základě
**fakturační částka** a jedna z následujících informací o obchodníkovi:

- Ewallet ID
- Daňové identifikační číslo obchodníka
- Mobilní číslo

Aktivujte QR kódy
-----------------

Přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Nastavení“. Pod položkou „Zákazník
V sekci platby aktivujte funkci :guilabel:`QR kódy`.

Konfigurace účtu v aplikaci PromptPay QR
---------------------------------------

Přejděte na: `Kontakty --> Konfigurace --> Bankovní účet` a vyberte bankovní účet pro
který chcete aktivovat pro platby prostřednictvím QR kódu. Zadejte typ proxy a vyplňte
Závisí na zvoleném typu a je uvedena v poli „Hodnota proxy“.

.. důležité::
   - Město držitele účtu je povinné.
   - Zaškrtávací políčko Include reference nefunguje pro QR kódy PromptPay.

.. obrázek:thailand/qr-promptpay-bank.png
:alt: Konfigurace účtu PromptPay

.. viz též:
:doc:`../účetnictví/banka`

Konfigurace bankovního časopisu
--------------------------

Přejděte na záložku „Účetnictví“ – „Nastavení“ – „Knihy“, otevřete bankovní knihu a pak vyplňte
v poli „Číslo účtu“ a „Banka“ pod záložkou „Účetní doklady“.

.. obrázek: thailand/qr-bank-journal.png
:alt: Konfigurace účtu banky

Vystavujte faktury s QR kódem PromptPay
-------------------------------------

Při vytváření nové faktury otevřete záložku „Další informace“ a nastavte položku „Způsob platby“.
Možnost QR kódu: guilabel: EMV Merchant-Presented QR code.

.. obrázek:thailand/faktura-s-qr-kodem-emv.png
:alt: Vyberte možnost předloženého platebního kódu QR

Zajistěte, aby pole „Příjemce banky“ bylo nastavené na tuto instituci, protože Odoo používá toto pole k
generovat QR kód pro platbu PromptPay.
