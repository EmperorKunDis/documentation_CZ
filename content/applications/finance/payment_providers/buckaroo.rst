========
Buckaroo
========

„Buckaroo“ je nizozemská společnost, která nabízí několik způsobů online plateb
možností.

.. _platební_prostředky/buckaroo/konfigurovat-panel:

Konfigurace na Buckaroo Plaza
===============================

#Přihlaste se na stránku „Buckaroo Plaza“ <https://plaza.buckaroo.nl>, přejděte do nabídky „Můj Buckaroo“ a
Vyberte webové stránky a klikněte na záložku „Nastavení push“.
#Zatrhněte políčko „Povolit odpověď s odkladem“ v seznamu možností „Odpovědi s odkladem a push“.
oddíl.
#Zadejte adresu URL vaší databáze Odoo, následovanou /platba/buckaroo/webhook.
:guilabel:`Textové pole Push URI Success/Pending“ a „Textové pole Push URI Failure“. Například:
„https://vašespolečnost.odoo.com/platba/buckaroo/webhook“.
#Zanechte ostatní pole v původním stavu a klikněte na tlačítko „Uložit“.
#V záložce „Obecné“ zkopírujte klíč webu (tedy klíč používaný k jedinečnému identifikaci
identifikovat váš web s Buckarem a uložit si ho na později.
#Zobrazit:menu_selection:Nastavení -> Zabezpečení -> Tajný klíč, zadejte nebo vygenerujte
:guilabel:`Tajný klíč“ a klikněte na „Uložit“. Uložte klíč pro pozdější použití.

Konfigurace v Odoo
=====================

#:ref:`Přejděte do sekce „Platební poskytovatelé“ a změňte stav na
na: `Zapnuto`.
#V záložce „Přihlašovací údaje“ vyplňte „Klíč webu“ a „Tajný klíč“.
pole s hodnotami, které jste si uložili v předchozím kroku
:ref:`platební služby/buckaroo/nastavení dashboardu`.
#Upravte si možnosti v ostatních záložkách podle svého uvážení.

.. viz též:
:doc:`../platební_prostředky`
