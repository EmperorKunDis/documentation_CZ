=====
Nuvei
=====

„Nuvei“ je kanadská společnost, která poskytuje platební řešení, která pokrývají
Několik zemí v Jižní Americe, Spojené státy a Kanada. Umožňuje firmám přijímat platební karty
a několik místních platebních metod.

.. _payment_providers/nuvei/dashboard:

Konfigurace na dashboardu Nuvei
====================================

#Vytvořte si účet u Nuvei (pokud ještě nemáte), přes naši „stránku s doporučením“ https://pages.nuvei.com/odoo-referral-0/.
#Nuvei používá dvě samostatné brány pro prostředí Sandbox a Production.
„Dashboard Sandboxu <https://sandbox.nuvei.com/login>“ k otestování integrace bez účtování
své zákazníky. Jakmile budete připraveni přijímat platby, přepněte na
„Dashboard výroby <https://cpanel.nuvei.com/login>“.
#Přejděte do levého sloupce na „Nastavení“, vyberte „Moje nastavení integrace“ a poté
Vyberte svou platební stránku v seznamu „Webová stránka“ na záložce „:guilabel:“.
#Zkopírujte hodnoty „ID obchodníka“ a „ID webu“ a uložte je na později.
<platební_provozovatelé/nuvei/odoo>.
#Klikněte na tlačítko „Zobrazit“, zkopírujte „Tajný klíč“ a uložte jej pro pozdější použití.
<platební_provozovatelé/nuvei/odoo>.

.. tip::
Nuvei podporuje další funkce týkající se zpracování chyb z téže stránky, jak je uvedeno výše.
Příkladem možností zpracování neúspěšných transakcí je následující: Zapnout
:guilabel:"Uživatelská past" a přesměruje uživatele zpět na stránku s platbou, aby mohl pokus o platbu
jiný vklad nebo :guilabel:`Odmítnutí obnovy“ zobrazí okno s navrhovanými alternativami.
podobné platební metody.

.. _payment_providers/nuvei/odoo:

Konfigurace v Odoo
=====================

#Přejděte na platební metodu Nuvei a vyplňte
:guilabel:`Identifikátor obchodníka“, :guilabel:`Identifikátor webu“ a „Tajný klíč“.
s informacemi uloženými v kroku :ref:`payment_providers/nuvei/dashboard`.
#Aby se aktivoval poskytovatel, změňte jeho stav na „Povolený“ nebo „Testovací režim“.
#Nastavte si ostatní možnosti podle svého uvážení.

.. tip::
Můžete také otestovat Nuvei pomocí režimu :ref:`testování <payment_providers/test-mode> a vašeho Sandboxu
Hodnoty panelu.

.. platby/nuvei/služby:

Způsoby platby
===============

Většina platebních metod společnosti Nuvei je **regionálně specifická**. Podporované způsoby platby a značky se liší v závislosti na
Seznam zemí naleznete níže:

+---------------------------------+----------------------------------+
|Argentina|                            | Ekvádor|
|                                 |                                  |
|-Boleto|-Karta (AMEX, MasterCard, Visa)|
|- Karta (AMEX, MasterCard, Visa)|- AstroPay TEF (Banco Guayaquil,
|                                         |Banco Pichincha, Facilito)       |
+---------------------------------+----------------------------------+
|Brazílie|                             |Mexiko|
|                                 |                                  |
|-Boleto|-Karta (AMEX, MasterCard, Visa)|
|- Karta (AMEX, MasterCard, Visa) |- SPEI                               |
| - Pix                             | - Oxxo Pay                      |
+---------------------------------+----------------------------------+
|Kanada|                                | Peru|
|                                 |                                  |
|- Kreditní karta (AMEX, MasterCard, Visa)|-Kreditní karta (AMEX, MasterCard, Visa)|
|                                      | - Boleto                        |
+---------------------------------+----------------------------------+
|Čile|                                  |Spojené státy americké|
|                                 |                                  |
|- Kreditní karta (AMEX, MasterCard, Visa)|-Kreditní karta (AMEX, MasterCard, Visa)|
|- WebPay                          |                                   |
+---------------------------------+----------------------------------+
|Kolumbie|                              |Uruguay|
|                                 |                                  |
|- Kreditní karta (AMEX, MasterCard, Visa)|-Kreditní karta (AMEX, MasterCard, Visa)|
|- PSE                              |- místní platby (Abitab,         |
|                                         |    Červená Pagosa)              |
+---------------------------------+----------------------------------+

.. viz též:
:doc:`../platební_prostředky`
