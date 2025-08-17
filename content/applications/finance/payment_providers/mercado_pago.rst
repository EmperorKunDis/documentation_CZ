============
Mercado Pago
============

„Mercado Pago <https://www.mercadopago.com/>“ je internetová služba pro placení, která pokrývá několik
státy, měny a způsoby platby v Latinské Americe.

..._platební_prostředky/mercado_pago/konfigurovat_panel:

Konfigurace na dashboardu Mercado Pago
=======================================

#Přihlaste se do „Dashboardu Mercado Pago“ (https://www.mercadopago.com.mx/developers/panel/)
a vyberte svou aplikaci nebo vytvořte novou.
#Vyberte v levém sloupci stránky aplikace možnost „Kreditní karty“.
Vyberte odvětví a v případě potřeby zadejte doménu. Klikněte na tlačítko „Aktivovat kreditní kartu“.
„Výrobní“.
#Kopírujte „Token přístupu“ a uložte si ho na později.

.. tip::
Pokud chcete Mercado Pago vyzkoušet jako testovací verzi, zvolte v levém menu možnost „Testovací kreditní karty“.
stránce přihlášení, pak zkopírujte testovací „Přístupový token“.

.. obrázek: mercado_pago/mp-credentials.png
:alt:Produkční a testovací kreditní účty v Mercado Pago.

.. _platební_poskytovatelé/mercado_pago/konfigurovat_odoo:

Konfigurace v Odoo
=====================

#Navštivte stránku s platebními metodami a změňte platební metodu na
stát na:guilabel:`Zapnuto`.
#V záložce „Přihlašovací údaje“ vyplňte pole „Token přístupu“ hodnotou, kterou jste si uložili.
v kroku :ref:`platebních služeb/mercadopago/konfigurovat-dashboard`.
#Nastavte si ostatní možnosti podle svého uvážení.

.. viz též:
   - :doc:`../platební_prostředky`
   - „Webinář Mercado Pago a Odoo“ <https://www.youtube.com/watch?v=CX8vPHMb1ic>
