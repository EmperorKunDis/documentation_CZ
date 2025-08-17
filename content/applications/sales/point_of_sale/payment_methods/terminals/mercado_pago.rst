============
Mercado Pago
============

Připojení platebního terminálu umožňuje nabídnout svým zákazníkům plynulý způsob platby a usnadnit jim tak
Práci vašich pokladních.

.. důležité:
pouze terminály pro bezkontaktní platby Point Smart v Argentině, Brazílii a Mexiku
podporovány. Lze je zakoupit na webu „Mercado Pago“
<https://www.mercadopago.com.mx/herramientas-para-vender/lectores-de-punto>.

.. viz též:
„Online platby Mercado Pago
<https://www.mercadopago.com.mx/herramientas-para-vender/check-out#benefits-checkout>

..._konfigurace-platební-brány-mercado-pago:

Konfigurace
=============

#Vytvořte si účet „Mercado Pago“ (https://www.mercadopago.com.mx/).
#Připojte terminál Point Smart k obchodu a pokladně pomocí
dokumentaci „Mercado Pago“ <https://vendedores.mercadolibre.com.ar/nota/locales-una-herramienta-para-mejorar-la-gestion-de-tus-puntos-de-venta/>“.

....... poznámka::
Všechny zakoupené terminály se automaticky zobrazí na vašem panelu Mercado.

#Nastavte svůj terminál Point Smart do režimu „Prodejna“.

.... upozornění::
Odoo nepodporuje režim samostatného provozu :guilabel:`Standalone`.

#Vytvořte aplikaci Point Smart (viz. odkaz na vytvoření aplikace).
#. :ref:`Vytvořte si přihlašovací údaje <pos-mercado-pago-credentials>“.
#:ref:`Vytvořte a nakonfigurujte související platební metodu <pos-mercado-pago-method>“.

..._aplikace_pro_platby_Pago_Market:

Aplikace Point Smart
-----------------------

Vytvořte novou aplikaci z vývojářského panelu Mercado Pago
<https://www.mercadopago.com/developers>_ podle dokumentace aplikací společnosti Mercado Pago
<https://www.mercadopago.com.mx/ayuda/20152>`, a zvolte:
Osoba platby.

..._pos-mercado-pago-credentials:

Kvalifikace
-----------

Jakmile je aplikace Point Smart vytvořena, jsou potřeba tři přihlašovací údaje:

- Přístupový token, který používá Odoo k volání služby Mercado Pago.
- Tajný klíč webového konektoru, který používá Odoo k ověření oznámení odeslaných službou Mercado Pago.
- Číslo sériového čísla na zadní straně vašeho terminálu Point Smart.

Získáte přístupový token a tajný klíč webového konektoru následujícím způsobem:
dokumentace <https://www.mercadopago.com.mx/developers/en/docs/your-integrations/credentials>.
Poté je vložte do Odoo při tvorbě platebního metodu.

.. důležité:
Pro konfiguraci webhooků přidejte adresu vaší databáze Odoo (např.
https://mojefirma.odoo.com/) následované /pos_mercado_pago/notification (např.
„https://mojefirma.odoo.com/pos_mercado_pago/notification“).

.. obrázek:: mercado_pago/webhooks.png
:alt: Konfigurace webových smyček na Mercado Pago.

..._metoda-plateb-na-trhu-pago:

Způsob platby
--------------

#Přejděte do sekce „Prodejní místo“ – „Konfigurace“ – „Nastavení“ a zapněte „Mercado“.
Pago pod záložkou „Platební terminály“.
#Vytvořte související platební metodu <../../payment_methods> kliknutím na
:menu:„Prodejní místo -> Konfigurace -> Způsoby platby“.
#. Zadejte typ záznamu jako:guilabel:`Banka`
#Vyberte pole „Použít platební terminál“ a zvolte „Mercado Pago“.
#Vyplňte povinná pole následujícími přihlašovacími údaji:


   - Do pole „Token uživatele produkce“ zadejte přístupový token.
   - Zadejte hodnotu pole „Tajný klíč produkce“ pomocí tajného klíče webového zpětného volání.
   - Do pole „Terminál S/N“ zadejte sériové číslo terminálu. Můžete ho najít na
zadní část terminálu.
   - Klikněte na tlačítko „Nutit PDV“ a aktivujte režim prodejního místa.

.. obrázek:: mercado_pago/payment-method.png
:alt:Formulář pro vytvoření nového způsobu platby.

Zvolte způsob platby v nastavení :ref:`POS <configuration/settings>`, přidejte
je do pole „Způsob platby“ pod položkou „Platba“.
část.

.. důležité:
Každá akce provedená na terminálu by měla vyvolat oznámení v rozhraní POS. Zajistěte
:ref:`tajný klíč webového konektoru <pos-mercado-pago-credentials> je správně nakonfigurován, pokud nejste
oznámena.
