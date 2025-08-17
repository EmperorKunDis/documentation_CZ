=====
Egypt
=====

... egypt/instalace:

Instalace
============

Instalujte následující moduly, abyste získali všechny funkce egyptské
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * – Egypt – Účetnictví
     - „l10n_eg“
     - Výchozí:balík lokalizace daní:
   * --:guilabel:Propojení s egyptským fakturami
     - „l10n_eg_edi_eta“
     - :ref:`Egyptská daňová správa (ETA) elektronické fakturace <egypt/e-invoicing>`

...Egypt / elektronické fakturace:

Egyptská elektronická fakturace
====================

Odoo splňuje požadavky na elektronické faktury podle Egyptské daňové správy (ETA).

.. důležité::
Egyptská elektronická fakturace je dostupná od verze Odoo 15.0. Pokud je potřeba, pak lze provést :doc:`výměnu
</administration/upgrade> vaši databázi.

.. viz též:
   - „Video:Egypt e-fakturace <https://www.youtube.com/watch?v=NXuBPLR4pVw>“
   - :doc:`/administration/upgrade`

... egypt/e-fakturace-eta-portal:

Registrujte si Odoo na svém portálu ETA
--------------------------------

Musíte se zaregistrovat do svého portálu ETA, abyste dostali přístupové údaje pro API.
Tyto kódy do:ref: „konfigurace aplikace účetnictví v Odoo“ <egypt/fakturační-konfigurace>.

Přejděte na portál ETA a zobrazte si profil vaší společnosti kliknutím na „Zobrazit profil daňového poplatníka“.

.. obrázek:egypt/taxpayer-profile.png
:align:center
:alt:Kliknutím na „Zobrazit profil daňového subjektu“ v portálu fakturace ETA

Dále přejděte do sekce „Zástupci“ a pak klikněte na „Registrace ERP“.
Zadejte název ERP systému (např. „Odoo“), ostatní pole nechte prázdná.

.. obrázek:egypt/add-erp-system.png
:align:center
:alt:Vyplnění formuláře pro registraci ERP systému na portálu ETA.

Jakmile úspěšně registrujete svůj web, zobrazí se vám na něm vaše API klíče:

- ID klienta
- Klientské tajné klíče 1
- Klientské tajné klíče 2

.. poznámka::
   - ETA by vám měla poskytnout uživatelské jméno a heslo pro přístup k jejich online portálu.
   - Požádejte také o přístup do předprodukčního portálu od společnosti ETA.
   - Tyto kódy jsou důvěrné a měly by být bezpečně uloženy.

...egypt/e-fakturace:

Konfigurace v Odoo
---------------------

Chcete-li propojit svou databázi Odoo s vaším účtem v portálu ETA, přejděte na:
Konfigurace --> Nastavení --> ETA E-fakturační nastavení“ a zadejte hodnotu „:guilabel:ID klienta ETA“.
„Tajné“ heslo „ETA Secret“, které jste získali při registraci Odoo na portálu ETA
<egypt/e-invoicing-eta-portal>. Zadejte hranici pro fakturaci, pokud je třeba.

.. obrázek:egypt/eta-api-integration.png
:align:center
:alt: Konfigurace přihlašovacích údajů pro elektronické faktury v Odoo

.. důležité::
   - **Zkontrolujte si svůj předprodukční portál**, než začnete vydávat skutečné faktury na produkci.
ETA portál.
   - Přihlašovací údaje pro prostředí předprodukce a produkce jsou odlišné. Ujistěte se, že
Při přechodu z jednoho prostředí do druhého aktualizujte informace o Odoo.
   - Pokud ještě nebylo provedeno, vyplňte své podrobné údaje o společnosti s plnou adresou, zemí a
Daňové identifikační číslo.

..._egypt/fakturace-na-dálku-a-kódy-etas:

Kódy ETA
~~~~~~~~~

Elektronické fakturace funguje s sadou kódů poskytnutých ETA. Můžete používat „Dokumentaci ETA
<https://sdk.preprod.invoicing.eta.gov.eg/codes/>_ kódování vašich podnikatelských atributů.

Většina těchto kódů je automaticky zpracovávána systémem Odoo, pokud máte nastavené :ref:`větve
<egypt/e-fakturace-odvětví>“, „zákazníci“ <egypt/e-fakturace-zákazníci> a „produkty“
„Egypt/elektronické fakturace“ jsou správně nakonfigurované.

- Informace o společnosti:

  - Daňové identifikační číslo společnosti
  - | Identifikátor pobočky
|Pokud máte pouze jednu pobočku, použijte „0“ jako kód pobočky.
  - Kód typu aktivity

- Další informace:

  - |Kódy výrobků
|Váš produkt by měl být označen a přiřazen k jeho **GS1** nebo **EGS** kódu.
  - Daňové kódy
|Většina daňových kódů je již v Odoo nakonfigurována podle :guilabel:`ETA Code (Egypt)“
pole. Doporučujeme vám zkontrolovat, zda kódy odpovídají vašim daním.

.. viz též:
   - „SDK pro elektronické faktury a příjmy v Egyptě - Tabulky kódu
<https://sdk.preprod.invoicing.eta.gov.eg/codes/>
   - :doc:`../účetnictví/daně`

... egypt/fakturace-v-odvetvích:

Banky
~~~~~~~~

Vytvořte kontakt a deník pro každou pobočku vaší firmy a nakonfigurujte její nastavení ETA.

Pro toto nastavení přejděte na položku „Účetnictví“ -> „Konfigurace“ -> „Deníky“, pak klikněte na
:guilabel:`Vytvořit“.

Název časopisu zadejte podle oboru vaší společnosti a nastavte :guilabel:`Typ` jako
„Prodej“. Následně otevřete záložku „Další nastavení“ a vyplňte
:guilabel:`Nastavení pro Egypt“ sekce:

- V poli „Branch“ vyberte kontakt pro danou pobočku nebo jej vytvořte.
- Nastavte pole „Kód činnosti ETA“.
- Zadejte „ID větve ETA“ (:guilabel:`ETA Branch ID`) (použijte „0“, pokud máte pouze jednu větev).

.. obrázek:egypt/branch-journal.png
:align:center
:alt: Konfigurace prodejního deníku egyptské společnosti

.. důležité::
Vybraný kontakt v poli „Branch“ musí být nastaven jako „Company“.
(**ne jako Individuální**), a položky :guilabel:`Adresa“ a :guilabel:`Daňové identifikační číslo“.
Musí být vyplněny.

... egypt/elektronické fakturace zákazníkům:

Zákazníci
~~~~~~~~~

Ujistěte se, že formuláře pro kontaktování zákazníků jsou správně vyplněny, aby byly vaše elektronické faktury platné:

- Typ kontaktu: Individuální nebo Firma
- :guilabel:`Země“:
- :guilabel:`Daňové identifikační číslo“: Daňové identifikační číslo nebo Obchodní rejstřík pro společnosti. Národní identifikace pro jednotlivce.

.. poznámka::
Upravit kontaktní formuláře zákazníků můžete kliknutím na: „Účetnictví“ --> „Zákazníci
-->Klienti.

... egypt/elektronické fakturace:

Produkty
~~~~~~~~

Ujistěte se, že vaše produkty jsou správně nakonfigurované, aby byly platné elektronické faktury:

- :guilabel:`Produktový typ“: skladovatelné produkty, spotřební zboží nebo služby.
- :guilabel:`Jednotka měření“: pokud používáte skladovou knihu a funkci „Jednotky měření“ aktivní.
Velikost měření „<../../inventory_and_mrp/inventory/product_management/configure/uom>“.
- :guilabel:`Čárový kód“: čárový kód GS1 nebo EGS
- „Čárový kód ETA“ (pod záložkou „Účetnictví“): pokud čárový kód ne
musí odpovídat kódu výrobku ETA.

.. poznámka::
Upravit produkty můžete v sekci „Účetnictví“ -> „Zákazníci“ -> „Produkty“.

... egypt/elektronické fakturace, USB autentizace

USB autentizace
------------------

Každý, kdo potřebuje elektronicky podepisovat faktury, musí mít svůj vlastní USB klíč pro autentizaci.
Vystavit fakturu do portálu ETA přes ERP.

.. poznámka::
Můžete kontaktovat ETA (Egyptská daňová správa) nebo Egypt Trust.
<https://www.egypttrust.com/>, abyste si mohli tato klíčová zařízení zakoupit.

..._egypt/e-fakturace-lokalni-pripad:

Nainstalujte Odoo jako místního proxy na svém počítači
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Odoo místní server funguje jako most mezi vaším počítačem a databází Odoo, která je uložena v cloudu.

Stáhněte si instalační soubor komunity Odoo z stránky https://www.odoo.com/page/download a spusťte
instalace na váš počítač.

Vyberte instalaci s názvem „Odoo IoT“.

.. obrázek:egypt/install-odoo-local-proxy.png
:align:center
:alt:Vybrání „Odoo IoT“ při instalaci Odoo Community.

.. poznámka::
Tato instalace Odoa funguje pouze jako server a neinstaluje žádné aplikace Odoa na váš počítač.
počítač.

Po dokončení instalace zobrazí instalační program vaše **přístupové tokeny** pro místní Odoo.
Zástupce. Zkopírujte token a uložte jej na bezpečném místě pro pozdější použití.

.. viz též:
   - „Odoo: Stáhněte si Odoo <https://www.odoo.com/page/download>“
   - :doc:`../../../administration/on-premise`

.._egypt/e-invoicing-usb-configuration

Nastavte USB klíč
~~~~~~~~~~~~~~~~~~~~~

Jakmile je na vašem počítači nainstalován místní proxy server, můžete ho propojit s databází Odoo.

#Přejděte na „Účetnictví“ -> „Konfigurace“ -> „USB“. Klikněte na
:guilabel:`Vytvořit“.
#Vložte název společnosti a ETA USB pin, který vám byl přidělen vaší USB klíč
poskytovatel a token přístupu poskytnutý na konci místního proxy.
instalace „Egypt/Fakturace elektronickou cestou - místní proxy“ a poté klikněte na tlačítko „Uložit“.
#Klikněte na „Získat certifikát“.

.. obrázek:egypt/usb-flash.png
:align:center
:alt:Vytváříme nový USB disk pro elektronické fakturace egyptské společnosti.
