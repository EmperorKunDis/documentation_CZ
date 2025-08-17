======
PayPal
======

„PayPal“ je americká internetová platební brána dostupná po celém světě a
Jedna z mála, která neúčtuje poplatky za předplatné.

.. poznámka::
Zatímco PayPal je k dispozici ve více než 200 zemích a regionech.
<https://www.paypal.com/webapps/mpp/country-worldwide>`, pouze některé měny jsou
podporované <https://developer.paypal.com/docs/reports/reference/paypal-supported-currencies>

.. _payment_providers/paypal/configurace-paypal:

Konfigurace v PayPal
=======================

#„Přihlaste se do rozhraní pro vývojáře PayPalu <https://developer.paypal.com/dashboard/>“.
#Klikněte na „Aplikace a přihlašovací údaje“ a klikněte na „Vytvořit aplikaci“.
#Zadejte název aplikace a klikněte na tlačítko „Vytvořit aplikaci“.
#Kopírujte „ID klienta“ a „Tajný klíč“ a uložte je.
:ref:`později <platební_prostředky/paypal/konfigurace_odoo>`.

.. důležité::
Pokud používáte jména nebo adresy zákazníků obsahující akcentovaná nebo ne-latinková písmena,
**musí** nastavit formát kódování platební žádosti odeslané společností Odoo na PayPal, aby se
neúspěšné transakce bez předchozího upozornění. Chcete-li tak učinit, přejděte na tlačítko PayPal
nastavení <https://www.paypal.com/cgi-bin/websrc?cmd=_profile-language-encoding> a klikněte
:guilabel:`Další možnosti“ a nastavte pole „Kódování“ na „UTF-8“.

Pokud se snažíte otestovat PayPal, přihlaste se do svého účtu :ref:`PayPal Sandbox.
</payment_providers/paypal/testing> a „Nastavte formát kódování pro svůj testovací účet


.. tip::
Pro šifrované platby na webu a chyby EWP_SETTINGS zkontrolujte dokumentaci PayPal.
<https://developer.paypal.com/docs/online/>`.

... _payment_providers/paypal/configuration-odoo:

Konfigurace v Odoo
=====================

#:ref:`Přejděte na platební metodu PayPal <platebni_metody/prihlaseni_novy_ucet>“.
#V záložce „Přihlašovací údaje“ zadejte e-mail spojený s vaším účtem PayPal.
Pak vyplňte pole „Klientské ID“ a „Tajné klientské heslo“ hodnotami, které jste si zvolili.
uložené v kroku :ref:`payment_providers/paypal/configuration-paypal`.
#Klikněte na tlačítko „Vytvořit webovou událost“.
#Nastavte pole „Stát“ na hodnotu „Povoleno“, a ujistěte se, že je nastavený poskytovatel plateb PayPal.
je :guilabel:`Zveřejněno“.
#Nastavte zbývající možnosti podle svých přání.

.. _payment_providers/paypal/testing:

Testování
=======

PayPal nabízí dva testovací účty, které můžete používat k simulaci transakcí v reálném čase:

-  Obchodní účet (např. ab-1abc12345678@business.example.com), který můžete používat jako obchodní účet;
-  Základní osobní účet (např. pro použití jako účet zákazníka)
`ba-9cba87654321@personal.example.com`.

Pro ověření práce s platbami prostřednictvím PayPal v Odoo:

#Přihlaste se na stránku „Paypal Developer Site“ (https://developer.paypal.com/) pomocí svého účtu PayPal.
přihlašovací údaje a jít na:menu:Testing Tools --> Sandbox Accounts.
#Klikněte na ikonu „fa-ellipsis-v“ („Guilabel: ellipsis“) vedle obchodního účtu Sandbox.
a vyberte možnost „Zobrazit / Upravit účet“.
#Zkopírujte e-mail, identifikační číslo klienta a tajný klíč a uložte je pro
další krok.
#V Odoo: „Nastavit platební bránu PayPal“
s hodnotami z předchozího kroku a nastavte pole :guilabel:`Stav` na
:guilabel:`Testovací režim“.

Poté můžete provést testovací transakci pomocí osobního účtu zkušební verze Odoo.

.. viz též:
   - :ref:`platební metody/testovací režim
   - :doc:`../platební_prostředky`
