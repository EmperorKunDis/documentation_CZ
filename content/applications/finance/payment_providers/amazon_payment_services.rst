=======================
Amazon Payments
=======================

„Amazon Payment Services <https://paymentservices.amazon.com/>“ nebo APS je online poskytovatel plateb
sídlem v Dubaji nabízející několik možností online plateb.

..._platebních_poskytovatelů/aps/konfigurovat_přístupový_panel:

Konfigurace na dashboardu APS
==============================

#Přihlaste se do svého „Dashboardu Amazon Payment Services“ (_https://fort.payfort.com/_) a přejděte na
:menu: „Nastavení integrace“ – „Zabezpečení“. Vytvořte
:guilabel:`Přístupový kód“ pokud ještě nebyl vygenerován. Zkopírujte hodnoty
:guilabel:`Identifikátor obchodníka“, :guilabel:`Kód přístupu“, :guilabel:`Příkaz k ověření SHA“
:guilabel:`Odpověď SHA“ políčka a uložte je na později.
#Zadejte adresu databáze Odoo do pole „Původní URL“ například takto:
Poté klikněte na tlačítko „Uložit změny“.
#Navigujte na: „Nastavení integrace“ – „Technické nastavení“ a klikněte na
:guilabel:`Přesměrování“. Ujistěte se, že je nastaveno :guilabel:`Stav“ na „Aktivní“ a vyberte
Předvolené způsoby platby pod názvem „Způsob platby“ v sekci :guilabel:`Doplňující informace“.
#. | Vyberte možnost „Odeslat parametry odpovědi“ a nastavte hodnotu na „Ano“
Následované v adrese „/platba/aps/vratka“ v :guilabel:„Adresa přesměrování“.
| Například „https://vašespolečnost.odoo.com/platby/aps/vrácení“.
|Zadejte svou databázi URL a poté připojení / platby / webhooku
pole „Odpověď na přímou transakci“ a pole „URL pro oznámení“.
| Například „https://vašespolečnost.odoo.com/platby/aps/webhook“.
|Klikněte na tlačítko „Uložit změny“.
#Pod položkou „Nastavení integrace > Vzhled platební stránky“ můžete upravit
vzhled a funkce stránky platebních služeb Amazonu (kde zákazníci vyplňují své údaje).
údaje o platební kartě (např. při placení).

.. _platební_prostředky/aps/konfigurace_odoo:

Konfigurace v Odoo
=====================

#:ref:`Přejděte na platební službu Amazon Payment Services <platebni_sluzby/prihlaseni_do_noveho_uctu>“
změnit svůj stav na „Povolené“ a ujistit se, že je „Zveřejněné“.
#V záložce „Přihlašovací údaje“ vyplňte „Identifikátor obchodníka“.
:guilabel:"Přístupový kód", :guilabel:"Frazeologie požadavku na SHA" a :guilabel:"Odpověď na SHA".
hodnoty, které jste uložili v kroku :ref:`payment_providers/aps/configure-dashboard`.
#Nastavte si ostatní možnosti podle svého uvážení.
