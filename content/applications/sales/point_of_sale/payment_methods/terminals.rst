Zobrazit obsah

=================
Platební terminály
=================

Připojení a integrace platebního terminálu do vašeho systému POS vám umožní přijímat platby prostřednictvím
Možnosti platby včetně kreditních a debetních karet zjednodušují proces placení.

..._konfigurace terminálů:

Konfigurace
=============

Přejděte do části „Nastavení aplikace“ (:ref:`<configuration/settings>`), posuňte se dolů
sekci „Platební terminály“ a zaškrtněte políčko u svého terminálu.

.. obrázek: terminály/platební_terminál.png
:alt: zaškrtávací políčko v nastavení pro zapnutí platebního terminálu

Poté postupujte podle odpovídající dokumentace k nastavení zařízení:

- :doc:`Konfigurace Adyen <terminals/adyen>`
- :doc:`Konfigurace Ingenico <terminals/ingenico>`
- :doc:`Konfigurace Mercado Pago <terminals/mercado_pago>`
- :doc:`Konfigurace Razorpay <terminals/razorpay>`
- :doc:`Konfigurace SIX <terminals/six>`
- :doc:`Konfigurace Stripe <terminals/stripe>`
- :doc:`Konfigurace Tyro <terminals/tyro>`
- :doc:`Konfigurace Viva.com <terminals/viva_com>`
- :doc:`Konfigurace Worldline <terminals/worldline>`

Jakmile je terminál nakonfigurován, můžete vytvořit odpovídající platební metodu a přidat ji do
POS <../payment_methods>.

Platba platebním terminálem
===========================

Při zpracování platby vyberte platební metodu terminálu. Zkontrolujte částku a
Klikněte na tlačítko „Odeslat“. Jakmile je platba úspěšná, stav se změní na „Platba
Úspěšný.“

.. poznámka::
   - Pokud dojde k problémům s propojením mezi Odoo a platebním terminálem, vyžadujte platbu
kliknutím na tlačítko „Zaplaceno“ pro potvrzení objednávky.
|Tato možnost je k dispozici pouze po obdržení chybové zprávy, která vás upozorní na
připojení nebylo zprovozněno.
   - Zrušit žádost o platbu můžete kliknutím na tlačítko „Zrušit“.

.. toctree::


terminály/adyen
terminaly/Ingenico
terminaly/mercado_pago
terminaly/Razorpay
terminály/šest
terminaly/Stripe
terminály/tyro
terminaly/viva_com
terminaly/světelná stopa
