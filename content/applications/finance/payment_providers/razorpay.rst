========
Razorpay
========

„Razorpay“ je indická společnost poskytující online platby,
a více než 100 platebních metod.

... _payment_providers/razorpay/configure_dashboard:

Konfigurace na panelu Razorpay
===================================

#Přihlaste se do „Dashboardu Razorpay“ (<https://dashboard.razorpay.com/>) a přejděte na
:menu_selecetion:`Nastavení --> Klíče API“. Vytvořte nové klíče a zkopírujte hodnoty
:guilabel:`ID klíče“ a „Tajný klíč“ pole a uložte je na později.
#. | Přejděte do sekce „Nastavení“ > „Webové smyčky“, klikněte na „Vytvořit novou webovou smyčku“.
a zadejte svou adresu databáze Odoo, následovanou /platba/razorpay/webhook.
textové pole „URL webhooku“.
| Například: „https://example.odoo.com/payment/razorpay/webhook“.
#Vyplňte pole „Tajné“ heslem, které si zvolíte, a uložte jej na později.
#Zkontrolujte, zda je platba autorizována, provedena a
:guilabel:"platba.neúspěšná", :guilabel:"vrácení peněz.neúspěšné" a :guilabel:"vrácení peněz.provedeno".
jsou zaškrtnuty.
#Klikněte na tlačítko „Vytvořit webovou událost“.

... platby/razorpay/opakované platby:

.. důležité::
Funkce „Opakované platby“ musí být zapnutá.
je aktivován, pokud chcete provádět opakované platby.
Odeslat požadavek na tým podpory Razorpay na adrese https://razorpay.com/support/#request
umožnit opakované platby.

.. _payment_providers/razorpay/configure_odoo:

Konfigurace v Odoo
=====================

#:ref:`Přejděte na platební metodu Razorpay <platebni-metody/prihlaseni-do-novych-sluzeb> a změňte její
stát na:guilabel:`Zapnuto`.
#V záložce „Přihlašovací údaje“ vyplňte klíčové ID a klíčový tajný kód.
:guilabel:`Tajný klíč webhooku“ s hodnotami, které jste uložili v předchozím kroku
:ref:`platební metody/razorpay/konfigurovat-přístupový-panel`.
#Nastavte si ostatní možnosti podle svého uvážení.

.. důležité::
Pokud nastavíte Odoo tak, aby si účtovala částky ručně:

  - Věnujte pozornost tomu, že ruční zrušení transakce není podporováno společností Razorpay.
  - Po pěti dnech, pokud transakce ještě nebyla zaznamenána, bude automaticky
**neplatné**.

.. viz též:
   - :doc:`../platební_prostředky`
