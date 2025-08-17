===========
Flutterwave
===========

„Flutterwave <https://flutterwave.com/>“ je nigerijská společnost poskytující online platby.
s pokrytím několika afrických zemí a platebními metodami.

.. _platební_poskytovatelé/flutterwave/nastavit_přístupový_panel:

Konfigurace na Flutterwave Dashboard
======================================

#Přihlaste se do „Dashboardu Flutterwave“ (https://dashboard.flutterwave.com/) a přejděte na
:menu_selecce:"Nastavení --> API". Zkopírujte hodnoty veřejného klíče a
:guilabel:`Tajný klíč“ položky a uložte je na později.
#. | Přejděte do sekce „Nastavení“ -> „Webové smyčky“ a zadejte adresu databáze Odoo, následovanou
do pole „Text URL“ zadejte `/payment/flutterwave/webhook`.
| Například: „https://vašespolečnost.odoo.com/platba/flutterwave/webhook“.
#Vyplňte pole „Tajný haš“ heslem, které si vytvoříte a uložíte jeho hodnotu na později.
#Ujistěte se, že jsou zaškrtnuty všechny zbývající políčka.
#Klikněte na tlačítko **Uložit**, abyste konfiguraci dokončili.

.. obrázek: flutterwave/flutterwave-settings.png
:alt: Nastavení Flutterwave

.._platební_poskytovatelé/flutterwave/konfigurovat_odoo:

Konfigurace v Odoo
=====================

#Přejděte na stránku „Provádění plateb prostřednictvím Flutterwave“ a změňte její
stát na:guilabel:`Zapnuto`.
#V záložce „Přihlašovací údaje“ vyplňte veřejný a soukromý klíč.
:guilabel:`Tajný klíč webhooku“ s hodnotami, které jste uložili v předchozím kroku
:ref:`platební metody/flutterwave/konfigurovat-přístupovou-stránku`.
#Nastavte si ostatní možnosti podle svého uvážení.

.... důležité::
Pokud se rozhodnete povolit ukládání platebních metod, doporučujeme povolit pouze platby kartou.
z Dashboardu Flutterwave, protože karty lze uložit jako platební tokeny. Chcete-li tak učinit, přejděte na
Flutterwave Dashboard a poté na „Nastavení“ -> „Nastavení účtu“.

.. viz též:
   - :doc:`../platební_prostředky`
