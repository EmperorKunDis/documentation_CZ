========
Viva.com
========

Služba **Viva.com** nabízí platební řešení prostřednictvím terminálu **viva.com Terminal**
aplikace pro fyzické a virtuální terminály.

.. poznámka::
   - Terminály Viva.com nevyžadují :doc:`IoT Box </applications/general/iot>
fungovat.
   - „Ve většině evropských zemí <https://developer.viva.com/about-viva/>“ podporuje používání Viva.com
platební terminály.
   - Aplikace Viva.com Terminal promění chytrý telefon s čipem NFC na „platební terminál“.
<https://www.viva.com/en-gb/blog/tap-on-phone-turn-your-phone-into-a-mobile-card-reader>.

.. důležité:
Odoo podporuje pouze měnu euro s využitím služby viva.com.

.. viz též:
   - „Seznam podporovaných terminálů <https://www.vivawallet.com/shop/terminals/terminals-4>“
   - „Seznam podporovaných platebních metod“

..._viva/konfigurace:

Konfigurace viva.com
======================

Pro konfiguraci terminálu Viva.com přejděte na webovou stránku „Viva.com <https://www.viva.com>“, vytvořte si
účet a pak postupujte podle těchto kroků:

#Ve webovém rozhraní Viva.com přejděte na záložku „Nastavení“ -> „Přístup k API“ -> „Obecné“.
#Zkopírujte „ID obchodníka a klíč API“.
<https://developer.viva.com/getting-started/find-your-account-credentials/merchant-id-and-api-key/>`.
#Kopírujte „ID klienta“ a „generované tajné heslo (kreditní API)“.
<https://developer.viva.com/getting-started/find-your-account-credentials/pos-apis-credentials/>`.
#Stáhněte si aplikaci Viva.com Terminal na zařízení, pak vygenerujte a zkopírujte „aktivační kód
<https://euhelp.viva.com/cs/clanky/5316775-jak-aktivovat-terminal-viva-com>.
#Na panelu Viva.com přejděte na: „Prodej“ → „Prodejní transakce“ → „Fyzické“.
Platby --> Přístupové terminály.
#Vytvořte nový „platební terminál“ a vložte kód aktivace.
<https://euhelp.viva.com/cs/clanky/5316775-jak-aktivovat-terminal-viva-com>.
#Zkopírujte:guilabel:Terminál ID, který byl vytvořen při aktivaci terminálu.

.. varování:
API klíče POS se zobrazují jen jednou. Uchovejte si kopii, abyste je mohli chránit.

.. poznámka::
   - Kredence POS API jsou pro API, které používají autentizaci založenou na heslech, včetně těch pro Android.
a aktivace terminálu pro iOS a „Cloud Terminal API“.
<https://developer.viva.com/apis-for-point-of-sale/card-terminals-devices/rest-api/>`.

Konfigurace Odoo POS
======================

Chcete-li propojit terminál viva.com s Odoo Point of Sale, postupujte podle těchto kroků:

#Přejděte na „Prodejní místo –> Konfigurace –> Nastavení“ a posuňte se dolů k
v sekci „Platební terminály“, zapněte platební terminál „Viva Wallet“ a klikněte
:guilabel:`Uložit“.
#Přejděte do sekce „Prodejní místo“ -> „Konfigurace“ -> „Způsoby platby“ a vytvořte nový.
platba metodou <../../payment_methods>.
#Nastavte pole „Deník“ na hodnotu „Banka“.
#Zadejte pole „Spojení“ hodnotu „Konec“.
#Nastavte pole „Spojit s“ na „Viva Wallet“.
#Vložte do odpovídajícího pole informace zkopírované z:ref:`viva.com <viva/configuration>`.
pole:

   - :guilabel:`ID obchodníka“
   - :guilabel:`API klíč“
   - :guilabel:`ID klienta“
   - :guilabel:`Tajný klíč klienta“
   - :guilabel:`ID terminálu“

#Uložte formulář a zkopírujte vygenerovanou adresu webového kroku z :guilabel:`Viva Wallet Webhook
pole Endpoint.
#Přejděte na účet viva.com a zkopírujte webhook URL do
„odpovídající pole
<https://developer.viva.com/webhooks-for-payments/transaction-payment-created/>
#V Odoo přejděte na: „Důležité nastavení prodejny“ (viz: „Konfigurace a nastavení“)
do sekce „Platba“ a přidejte vytvořený způsob platby do sekce „Platba“.
pole metod.
#Klikněte na tlačítko „Uložit“.
