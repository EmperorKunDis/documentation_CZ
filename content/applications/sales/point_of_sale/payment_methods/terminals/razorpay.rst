========
Razorpay
========

Připojení platebního terminálu Razorpay vám umožní nabídnout svým zákazníkům plynulý způsob platby.
a usnadnit práci pokladních.

.. viz též:
:doc:`Použijte jako platební metodu Razorpay. <../../../../finance/payment_providers/razorpay>`

Konfigurace
=============

... razorpay/credentials:

Najděte své přihlašovací údaje do služby Razorpay
--------------------------------

Vytvořte si účet na Razorpay (<https://razorpay.com/docs/payments/easy-create-account/>) a nastavte ho
na jejich webových stránkách.

Pro nastavení platební metody v Odoo potřebujete následující informace:

- „API klíč <https://razorpay.com/docs/payments/dashboard/account-settings/api-keys/>“
- Uživatelské jméno Razorpay
- Sériové číslo zařízení Razorpay, které najdete pod zařízením nebo na stránce „Razorpay“.
panel nástrojů <https://dashboard.razorpay.com/>`.

Zvolte způsob platby
----------------------------

#Povolte modul POS Razorpay v části „Aplikace a moduly“
platební terminál.
#Vytvořte související platební metodu <../../payment_methods> kliknutím na
:menu:„Prodejní místo -> Konfigurace -> Způsoby platby“.

   #Změňte typ záznamu na „Časopis“ a nastavte jej jako „Bankovní účet“.
   #Vyberte možnost „Razorpay“ v poli „Použití terminálu“.
   #Zadejte své uživatelské jméno do pole „Razorpay Username“ a sériové číslo vašeho zařízení.
do pole „Sériové číslo zařízení“ v poli „Razorpay“.
   #Vyplňte pole „API klíč Razorpay“ API klíčem Razorpay.
<razorpay/credentials>.
   #Nastavte pole :guilabel:`Povolené způsoby platby Razorpay` podle svých potřeb.

.. obrázek:: razorpay/create-method-razorpay.png
:alt:Formulář pro připojení k Razorpay

....... poznámka::
Můžete aktivovat pole „Testovací režim Razorpay“ během testování nebo nechat pole nezaškrtnuté.
výrobu.

Jakmile je způsob platby vytvořen, můžete jej pro své POS zapnout. Chcete-li tak učinit, přejděte na stránku :ref:`POS'.
Nastavení (konfigurace/nastavení)“ a přidejte platební metodu pod záložkou „Platba“.

.. poznámka::
Terminál musí mít alespoň 10% nabitou baterii, aby ho bylo možné používat.
