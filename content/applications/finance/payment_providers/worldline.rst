=========
Worldline
=========

Společnost „Worldline“ <https://worldline.com/> je francouzským podnikem a čtvrtým největším na světě
Poskytovatel platebních služeb.

Nastavení ve Worldline
=====================

.._světelná stopa/API uživatel:

Vytvořte uživatele API
------------------

Doporučuje se zřídit uživatele **API**, který by měl zajistit vytváření transakcí mezi Odoo.
Konfigurace Worldline zůstává v bezpečí i když jsou kompromitovány přihlašovací údaje. Kromě toho
nemusí se často měnit hesla jako u běžných účtů.

Vytvoření uživatele API provedete takto:

#Přihlaste se do portálu „Worldline Merchant Portal“
Klikněte na ikonu „fa-th“ („menu“) a vyberte „Back Office“.
#Přejděte do sekce „Nastavení“ a klikněte na „Nový uživatel“.
#Nastavte následující pole:

   #Uveďte uživatelské ID, jméno uživatele, e-mailovou adresu a
:guilabel:`Časové pásmo“ podle vašeho výběru.
   #Zadejte pole „Profil“ hodnotou „Admin“.
   #Zapnout: gui-label:"Speciální uživatel pro API".

.. tip::
   - Pokud uživatele máte nastaveného, zkontrolujte, že je aktivován bez chyby.
   - Pro ověření platebního toku s Worldline použijte jejich „testovací prostředí“.
<https://merchant-portal.preprod.worldline-solutions.com/>`_ spolu s režimem testování
<platební_prostředky/testovací režim>.

.._světelná stopa/nastavení:

Nastavte Worldline pro Odoo
-------------------------

Nyní musí být Worldline nakonfigurována tak, aby přijímala platby z Odoo.

#V obchodním portálu přejděte na: „Nastavení -> Platby -> API“.
:guilabel:`Vytvořit klíč API“. Zkopírujte „ID klíče API“ a „Tajný klíč API“.
a uložte je na později:ref:`<wordline/odoo-configuration>`.
#Přejděte na „Vývojáři“ – „Webové události“ a klikněte na „Vytvořit klíč webových událostí“.
Zkopírujte „ID webového zpětného volání“ a „tajný klíč webového zpětného volání“
uložit je na později:ref:`(viz <wordline/odoo-configuration>)
#. | Klikněte na tlačítko „Přidat webový odkaz“, zadejte URL vaší databáze Odoo a
do pole „URL“ v poli „Konec bodu“, a poté stiskněte tlačítko „Potvrdit“.
| Například: „https://example.odoo.com/payment/worldline/webhook“.

..._slovo/odoo-konfigurace:

Nastavení v Odoo
================

Nastavit Worldline v Odoo:

#Navštivte platebního poskytovatele Worldline a změňte jeho
stát na:guilabel:`Zapnuto`.
#V záložce „Přihlašovací údaje“ zadejte PSPID svého účtu Worldline a
vyplnit klíč API, tajný klíč API a webhookový klíč.
:guilabel:`Tajný klíč webhooku“ s hodnotami, které jste uložili v kroku
Odoo <worldline/setup>.
#Nastavte si ostatní možnosti podle svého uvážení.

.. viz též:
:doc:`../platební_prostředky`
