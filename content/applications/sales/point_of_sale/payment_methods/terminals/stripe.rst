======
Stripe
======

Připojení platebního terminálu umožňuje nabídnout svým zákazníkům plynulý způsob platby a usnadnit jim tak
Práci vašich pokladních.

.. důležité:
   - Platební terminály Stripe nevyžadují :doc:`IoT box </applications/general/iot>
   - Stripe terminály lze používat v mnoha zemích, ale ne po celém světě. Zkontrolujte „globální
dostupnost pro terminál Stripe <https://support.stripe.com/questions/global-availability-for-stripe-terminal>.
   - Integrace služby Stripe funguje s „Chytrými čtečkami terminálu <https://docs.stripe.com/terminal/smart-readers>“

.. viz též:
   - :doc:`Stripe jako poskytovatel platebních služeb <../../../../finance/payment_providers/stripe>`
   - „Seznam způsobů platby podporovaných společností Stripe <https://stripe.com/payments/payment-methods>“

Konfigurace
=============

Zvolte způsob platby
----------------------------

Aktivujte Stripe v nastavení přes: menuselection:Prodejna --> Konfigurace -->
Nastavení --> Platební terminály a zapnutí: guilabel:Stripe.

Pak vytvořte platební metodu:

- Přejděte na „Prodejní místo“ - „Konfigurace“ - „Způsoby platby“, klikněte
:guilabel:`Vytvořit“ a do pole „Metoda“ zadejte název svého způsobu platby.
- Zadejte pole „Deník“ jako „Banka“ a pole „Použít platební terminál“
pole jako :guilabel:`Stripe`;
- Do pole „Sériové číslo terminálu Stripe“ zadejte sériové číslo platebního terminálu.
- Klikněte na tlačítko „Nezapomeňte dokončit Stripe Connect před použitím této platební metody.“

.. obrázek: stripe/create-method-stripe.png
:align:center
:alt: vytvoření platební metody

.. poznámka::
   - Klikněte na tlačítko „Povolit pro identifikované zákazníky“ a umožněte tento způsob platby pouze pro identifikované
zákazníky. Pro všechny neověřené zákazníky, aby mohli platit přes Stripe, nechte
:guilabel:`Poznámka k identifikaci zákazníka“ je nezaškrtnutá.
   - Účet „Výjimečný“ a účet „Zprostředkovatelský“ mohou zůstat prázdné, pokud
použít výchozí účty.
   - Vyhledejte sériové číslo terminálu pod zařízením nebo na „dashboardu“ Stripe.
<https://dashboard.stripe.com>.

Připojte Stripe k Odoo
----------------------

Klikněte na „Připojit Stripe“. Tím se automaticky přesměrujete na stránku s konfigurací.
Vyplňte všechny informace, abyste vytvořili účet Stripe a propojili jej s Odoo. Jakmile jsou formuláře
Pokud je integrace dokončena, klíče API (:guilabel:Publikovatelný klíč a :guilabel:Tajný klíč) lze získat na
Webové stránky společnosti Stripe. Chcete-li tak učinit, klikněte na „Získání klíče tajného a veřejného“.
Klepněte na klávesy a vložte je do příslušných políček v Odoo. Vaše terminál
připravené k použití v POS.

.. obrázek: proužek/proužek-připojení.png
:align:center
:alt: spojení ve tvaru proužku

.. poznámka::
   - Pokud používáte Stripe výhradně v POS terminálu, budete potřebovat jen tzv. Secret Key
váš terminál.
   - Pokud používáte Stripe jako poskytovatele platebních služeb, stát může zůstat nastaven na
:guilabel:`Znepřístupněno“.
   - Pro databáze hostované **on-premise** nefunguje tlačítko „Připojit Stripe“.
ručně vyzvednout klíče API, přihlásit se do svého „dashboardu Stripe“.
<https://dashboard.stripe.com>`, zadejte do vyhledávacího pole „API“ a klikněte
:guilabel:`Vývojáři > API“.

Nastavte platební terminál
------------------------------

Přejděte na svém platebním terminálu doprava, klikněte na „Nastavení“, zadejte správný PIN kód a potvrďte
a vyberte svou síť.

.. poznámka::
   - Uživatelské zařízení a terminál musí sdílet stejnou síť.
   - Pokud je připojení k internetu realizováno prostřednictvím Wi-Fi sítě, musí být tato síť zabezpečena.
   - Při přístupu k nastavení terminálu je nutné zadat administrátorský PIN. Výchozí hodnota
kód je „07139“.

Přiřaďte platební metodu k terminálu
--------------------------------

Chcete-li přidat platební metodu do svého bodu prodeje, přejděte na:
Konfigurace --> Nastavení. Vyberte POS, posuňte se dolů do části „Platby“ a
Přidejte svůj způsob platby pro Stripe v poli „Způsoby platby“.

Řešení problémů
===============

Platební terminál není dostupný ve vašem účtu Stripe
---------------------------------------------------

Pokud platební terminál ve vašem účtu Stripe není k dispozici, musíte ho ručně přidat:

#Přihlaste se do svého „Dashboardu Stripe“ (https://dashboard.stripe.com/) a přejděte na
:menu_vyber:`Dashboard Stripe --> Platby --> Čtečky --> Lokality“;
#Přidejte umístění kliknutím na tlačítko „+ Nové“ nebo vyberte již vytvořenou lokaci.
#Klikněte na tlačítko „Nový“ v poli „Čtenáři“ a vyplňte požadované
informace.

.. poznámka::
Musíte zadat registrační kód. K jeho získání přejeďte prstem na pravou stranu zařízení.
zadejte administrátorský PIN kód (výchozí hodnota je 07139), ověřte a klikněte na tlačítko :guilabel:`Vytvořit
„registrační kód“.
