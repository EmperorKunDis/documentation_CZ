=====
Adyen
=====

„Adyen“ je nizozemská společnost, která nabízí několik způsobů online plateb
možností.

.. viz též:
   - :ref:`platební metody/přidat novou`
   - :doc:`../platební_prostředky`

.. poznámka::
Adyen spolupracuje pouze s klienty, které zpracovávají více než 10 milionů ročně nebo vystavují faktury za
**minimální počet** transakcí **za měsíc** **1.000**.

Konfigurace
=============

.. viz též:
:ref:`platební metody/přidat novou`

Nejprve kontaktujte podporu společnosti Adyen a zapněte pro vás možnost :guilabel:`vícečetného částečného vybírání plateb`.

Karta Povolení
---------------

Odoo potřebuje vaše **API Credentials** k propojení s vaším účtem Adyen, který obsahuje:

- Účet obchodníka: Kód účtu obchodníka, který chcete použít s Adyenem.
- [:ref:`API klíč <adyen/api_and_client_keys>“]: API klíč uživatele webové služby.
- „Klíč klienta“: Klíč klienta webové služby.
- :ref:`HMAC klíč <adyen/hmac_key>“: HMAC klíč webhooku.
- URL pro Checkout API: základní adresa pro všechny koncové body Checkout API.
- URL opakujícího se API: základní URL pro koncové body opakujícího se API.

Můžete si své přihlašovací údaje zkopírovat do svého účtu na Adyen a vložit je do příslušných polí pod
kartu Přihlašovací údaje.

.. důležité::
Pokud se snažíte o testování pomocí účtu pro testování společnosti Adyen, přejděte na
:menu_selecce:`Účetnictví --> Konfigurace --> Poskytovatelé platebních služeb“. Tam klikněte na
:guilabel:`Adyen“, zapněte režim testování a zadejte své přihlašovací údaje do
:guilabel:`Přihlašovací údaje“ záložka.

.. _adyen/api_and_client_keys:

API klíč a klientský klíč
~~~~~~~~~~~~~~~~~~~~~~

Chcete-li získat klíč API a klientský klíč, přihlaste se do svého účtu Adyen, přejděte na
:menu:"Vývojáři --> Zákaznický účet".

- Pokud již máte uživatele API, otevřete jej.
- Pokud ještě nemáte uživatele API, klikněte na tlačítko **Vytvořit nové přihlašovací údaje**.

Přejděte na: `Nastavení serveru --> Autentizace` a zkopírujte nebo vytvořte svůj **API klíč**.
Buďte opatrní při zadávání klíče API, protože vám nebude umožněno jej později znovu získat bez generování nového.
jedna.

Nyní přejděte do nastavení klienta (Authentification) a zadejte nebo vytvořte své
Klíč klienta. Toto je také místo, kde můžete povolit platby z vašeho
webové stránky <adyen/allowed_origins>.

.. _adyen/hmac_key:

HMAC klíč
~~~~~~~~

Chcete-li získat klíč HMAC, budete potřebovat konfigurovat webový konektor „Standardní oznámení“.
Přihlaste se do svého účtu u společnosti Adyen a poté přejděte na: „Vývojáři“ -> „Webové události“ -> „Přidat webovou událost“.
--> Přidat standardní oznámení“.

.. obrázek: adyen/adyen-add-webhook.png
:align:center
:alt: Konfigurujte webový konektor.

V nastavení „Obecné -> Servery -> URL“ zadejte adresu svého serveru.
a poté se připojí na adresu /payment/adyen/notification.

.. obrázek: adyen/adyen-webhook-url.png
:align:center
:alt:Zadejte adresu URL pro oznámení.

Poté zadejte: „Menu > Zabezpečení > HMAC klíč > Vytvořit“. Dávejte pozor, abyste si klíč zkopírovali.
bude později zakázáno bez vytvoření nového.

.. obrázek: adyen/adyen-hmac-key.png
:align:center
:alt: Vytvořte klíč HMAC a uložte jej.

Musíte uložit webový konektor, abyste jej vytvořili.

.. _adyen/urls:

URL adresy API
~~~~~~~~

Všechny URL API společnosti Adyen obsahují předponu specifickou pro oblast zákazníka, která je generována společností Adyen. Chcete-li nakonfigurovat
URL adresy postupujte takto:

#Přihlaste se do svého účtu u společnosti Adyen a pak přejděte na: „Vývojáři --> URL adresy API“.
#Kopírujte prefix vašeho živého zákaznického prostoru (tj. datového centra) a uložte jej do
Later.

.... obrázek: adyen/adyen-api-urls.png
:alt:Kopírujte předponu pro Adyen API

#V Odoo: „Přejděte na platební metodu Adyen“ (<platebni_metody/prihlaseni_k_novemu_platebni_metode>).
#V poli „URL služby Checkout“ zadejte následující URL a nahraďte „vaše_předpona“
předchozí uložený prefix:
„https://vaše_předpona-checkout-live.adyenpayments.com/checkout“
#V poli „Opakovaná adresa URL“ zadejte následující URL a nahraďte „yourprefix“
předchozí uložený prefix:
„https://vaše_předpona-pal-live.adyenpayments.com/pal/servlet/Recurring“.

.. poznámka::
Pokud se snažíte otestovat Adyen, můžete použít následující adresy URL místo těchto:

   - :guilabel:`URL Checkout API“: „https://checkout-test.adyen.com“
   - :guilabel:`Opakující se API URL“: „https://pal-test.adyen.com/pal/servlet/Recurring“

Adyen účet
-------------

... _adyen/allowed_origins:

Povolit platby z konkrétního původu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro umožnění platby z vašeho webu postupujte podle kroků v :ref:`adyen/api_and_client_keys`.
Přejděte na svého uživatele API a přejděte do části „Add allowed origins“ a přidejte URL adresy z
kde budou platby provedeny (URL serverů, na kterých jsou hostovány vaše instance Odoo).

.. obrázek: adyen/adyen-allowed-origins.png
:align:center
:alt:Umožňuje platby zadané ze specifické domény.

Zablokovat kartu
----------------------

Adyen vám umožňuje získat částku manuálně namísto okamžitého zachycení.

Chcete-li nastavit tento nástroj, zapněte možnost „Manuální snímání částky“ v Odoo, jak je uvedeno v
:ref:`dokumentace poskytovatelů platebních služeb <platebni_poskytovatele/manualni_sber>.

Pak otevřete svůj účet pro obchodníky u společnosti Adyen, přejděte na „Účet“ -> „Nastavení“ a nastavte
Zapněte režim **manuální**.

.. obrázek: adyen/adyen_capture_delay.png
:align:center
:alt:Nastavení zpoždění v Adyen

.. upozornění:
   - Pokud si nastavíte Odoo tak, aby částky zadávala ručně, ujistěte se, že jste nastavili
*návod* pro Adyen. Jinak bude transakce zablokována v autorizovaném stavu
Odoo.

.. poznámka::
   - Po **sedmi dnech**, pokud ještě nebyla transakce zaznamenána, má zákazník právo
**zrušit** ho.

.. viz též:
:doc:`../platební_prostředky`
