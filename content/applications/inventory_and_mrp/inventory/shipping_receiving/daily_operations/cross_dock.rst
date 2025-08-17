====================================
Organizujte křížový sklad v skladu
====================================

Křížové skladování je proces odesílání produktů přímo zákazníkům.
bez nutnosti je ukládat do skladu. Náklaďáky jsou jednoduše vyloženy v oblasti *Cross-Dock*,
Zboží přeorganizovat a naložit do další dodávky.

.. obrázek: cross_dock/cross1.png
:align:center

.. poznámka::
Pro více informací o tom, jak uspořádat sklad, navštivte náš blog: „Co je křížové nakládání a
Je pro mě?


Konfigurace
=============

V aplikaci „Inventář“ otevřete: menuselection:„Nastavení --> Nastavení“ a aktivujte
*Multistopové trasy*.

.. obrázek: cross_dock/cross2.png
:align:center

.. poznámka::
Provedením takového kroku se také aktivuje funkce *Uložiště*.

Nyní by měly být obě směry přepravy konfigurovány tak, aby pracovaly ve dvou krocích.
konfiguraci přejděte do: „Sklad --> Konfigurace --> Sklady“ a upravte ji.
sklad.

.. obrázek:: cross_dock/cross3.png
:align:center

Tato úprava povede k vytvoření trasy Cross-Docking, která se nachází
:menu:„Soubor inventáře“ -> „Konfigurace“ -> „Trasy“.

.. obrázek: cross_dock/cross4.png
:align:center

Nastavte produkty s Cross-Dock Routingem
========================================

Vytvořte produkt, který používá trasu Cross-Dock a pak v záložce sklad vyberte
směry „Koupit“ a „Skladové přepravy“. V záložce Koupit zadejte dodavatele, od kterého nakupujete.
produkt a stanovit za něj cenu.

.. obrázek: cross_dock/cross5.png
:align:center

.. obrázek: cross_dock/cross6.png
:align:center

Jakmile je hotovo, vytvořte pro produkt objednávku na prodej a potvrďte ji. Odoo automaticky vytvoří dvě
převody, které budou spojeny s prodejním příkazem. První je převod z položky *Input
Místo* k místu výstupu* odpovídající pohybu produktu v *Cross-docku*.
oblast. Druhý je objednávka dodání z výstupního místa do vašeho cílového místa.
Oba jsou ve stavu *Čekáme na další operaci*, protože ještě musíme objednat produkt.
dodavatel.

.. obrázek: cross_dock/cross7.png
:align:center

.. obrázek: cross_dock/cross8.png
:align:center

Nyní přejděte do aplikace „Nákup“. Tam najdete objednávku nákupu, kterou automaticky vytvořil
spuštěné systémem. Zkontrolujte jej a přijměte produkty v místě *Vstupní umístění*.

.. obrázek: cross_dock/cross9.png
:align:center

.. obrázek: cross_dock/cross10.png
:align:center

Když jsou produkty přijaty od dodavatele, můžete se vrátit k původnímu prodejnímu příkazu.
a ověřit vnitřní přenos z „Vstupu“ do „Výstupu“.

.. obrázek: cross_dock/cross11.png
:align:center

.. obrázek: cross_dock/cross12.png
:align:center

Dodací objednávka je nyní připravena k zpracování a může být také ověřena.

.. obrázek: cross_dock/cross13.png
:align:center

.. obrázek: cross_dock/cross14.png
:align:center
