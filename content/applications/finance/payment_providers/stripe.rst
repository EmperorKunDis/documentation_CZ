======
Stripe
======

„Stripe <https://stripe.com/>“ je americká společnost, která poskytuje řešení pro online platby
podnikům přijímat kreditní karty a další způsoby platby.

.. viz též:
   - „Seznam zemí podporovaných společností Stripe <https://stripe.com/global>“
   - „Seznam platebních metod podporovaných společností Stripe <https://stripe.com/payments/payment-methods>“

Vytvořte si účet Stripe s Odoo
====================================

Způsob získání vašich přihlašovacích údajů závisí na typu hostingu:

.. záložky::
...... skupina-tab::Odoo Online

      #Navštivte platebního poskytovatele Stripe.
klikněte na tlačítko „Připojit Stripe“.
      #Projděte si nastavení a potvrďte svou e-mailovou adresu, když vám společnost Stripe zašle
potvrzující e-mail.
      #V závěru procesu klikněte na tlačítko „Souhlasím a odešlu“. Pokud jsou požadovány všechny informace
Pokud je objednávka odeslána, jsou vám zobrazeny informace o Odoo a vaše platební metoda se aktivuje.

.... skupina-tab:: Odoo.sh nebo On-premise

      #Navštivte platebního poskytovatele Stripe.
klikněte na tlačítko „Připojit Stripe“.
      #Projděte si nastavení a potvrďte svou e-mailovou adresu, když vám společnost Stripe zašle
potvrzující e-mail.
      #Na konci procesu klikněte na tlačítko „Souhlasím a odesílám“; poté se vám zobrazí
platbu zajišťuje společnost Stripe v Odoo.
      #:ref:`Zadejte své přihlašovací údaje <stripe/api_keys>.
      #:ref:`Vytvořit webový konektor <stripe/webhook>.
      #Nastavte pole :guilabel:`Stát“ na hodnotu :guilabel:`Zapnuto“.

.. tip::
   - Pro použití stávajícího účtu Stripe: aktivujte režim vývojáře :ref:`<developer-mode>`.
:ref:`Stripe ručně zapnout <platební metody/přidat novou>“. Poté můžete :ref:`vyplnit své
kreditní údaje <stripe/api_keys>`, vytvořte webovou událost <stripe/webhook> a zapněte
poskytovatel platebních služeb.
   - Můžete také otestovat Stripe pomocí :ref:`platebních metod/testovací režim`. Nejprve
„Přihlaste se do svého účtu Stripe <https://dashboard.stripe.com/dashboard>“ a přepněte na
**Testovací režim**. Pak v Odoo aktivujte režim vývojáře:
:ref:`přejít na platebního poskytovatele Stripe <platebni-poskytovatel/podporovane-poskytovatele>`,
:ref:`zaplňte své klíče API <stripe/api_keys>“ testovacími klíči a nastavte
poli „Stát“ na hodnotu „Testovací režim“.

.. _stripe/api_keys:

Vložte své přihlašovací údaje
------------------------

Pokud jsou požadovány vaše **API kredence** pro připojení ke svému účtu Stripe, postupujte takto:

#Navštivte stránku „API klíčů na Stripe“ (<https://dashboard.stripe.com/account/apikeys>), nebo se přihlaste
Stripe dashboard a přejděte na: „Vývojáři -> API klíče“.
#V sekci „Běžné klíče“ zkopírujte „Klíč pro veřejnost“ a
:guilabel:`Tajný klíč“ a uložte je na později.
#V Odoo: „Navštivte platební bránu Stripe“.
#V záložce „Přihlašovací údaje“ vyplňte „Publikovatelný klíč“.
:guilabel:`Tajný klíč“ políčka s hodnotami, které jste dříve uložili.

.. _stripe/webhook:

Vytvořte webovou událost
------------------

Pokud je vaše **Webhook Signing Secret** nutné k propojení s vaším účtem Stripe, můžete vytvořit
Webhook automaticky nebo ručně.

.. záložky::
...... tab::Vytvoření webového hlavičkového odkazu automaticky

Zkontrolujte, zda jsou vyplněny klíče pro publikování a tajné klíče (:ref:`<stripe/api_keys>`) a pak klikněte
:guilabel:`Vytvořte svůj webový konektor“.

....... tab:: Vytvoření webového kroku ručně

      #Přejděte na stránku „Webové smyčky v Stripe“ <https://dashboard.stripe.com/webhooks> nebo se přihlaste
do svého Dashboardu Stripe a přejděte na: „Vývojáři --> Webové události“.
      #V sekci „Hostované koncové body“ klikněte na „Přidat koncový bod“. Pak v
:guilabel:`URL koncového bodu“ pole, zadejte URL databáze Odoo, následované
např. „https://vašespolečnost.odoo.com/payment/stripe/webhook“.
      #Klikněte na tlačítko „Vybrat události“ v dolní části formuláře a poté vyberte následující
události:

          - v sekci „Účtování“: „účtované částky“.
:guilabel:`vrácení peněz.aktualizace`;
          - v sekci „Úmysl zaplatit“:
:guilabel:`platební úmysl. částka k inkasu aktualizována`,
:guilabel:'platební úmysl. platba selhala', :guilabel:'platební úmysl. zpracování' a
:guilabel:"platba.úspěšná";
          - v sekci „Nastavení úmyslu“: „setup_intent.succeeded“.

      #Klikněte na tlačítko „Přidat událost“.
      #Klikněte na tlačítko „Přidat konec“, pak na „Zobrazit“ a uložte svůj
:guilabel:`Tajné podpisy“ na později.
      #V Odoo zvolte navigaci na platební bránu Stripe.
<platby/podporované-poskytovatele>.
      #V záložce „Přihlašovací údaje“ vyplňte pole „Tajný klíč k podpisu webhooku“
hodnotu, kterou jste si dříve uložili.

.. poznámka::
Můžete vybrat jiné události, ale v současné době nejsou zpracovávány systémem Odoo.

Povolit Apple Pay
================

Chcete-li umožnit zákazníkům používat tlačítko Apple Pay k zaplacení jejich objednávek na internetu, přejděte do
Kartě „Nastavení“, zapněte „Povolit expresní platbu“ a klikněte
:guilabel:`Povolit Apple Pay“.

.. viz též:
   - :ref:`Rychlé objednání a Google Pay <platební metody/rychle-objednavani-a-google-pay>`
   - :doc:`../platební_prostředky`
   - :doc:`Používejte terminál Stripe v místě prodeje <../../sales/point_of_sale/payment_methods/terminals/stripe>`
