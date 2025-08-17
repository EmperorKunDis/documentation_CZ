========
Ingenico
========

Připojení platebního terminálu umožňuje nabídnout svým zákazníkům plynulý způsob platby a usnadnit jim tak
Práci vašich pokladních.

.. důležité:
   - Platební terminály Ingenico vyžadují :doc:`IoT systém <applications/general/iot>.
   - Ingenico je v současné době k dispozici pouze ve třech zemích - Belgii, Nizozemsku a Lucembursku.
   - Odoo pracuje s terminály Ingenico Lane/, Desk/, a Move/, protože podporují TLV
komunikační protokol prostřednictvím TCP/IP.

Konfigurace
=============

Propojte systém Internetu věcí
---------------------

Připojení terminálu Ingenico k Odoo je funkcí, která vyžaduje systém IoT.
informace o tom, jak propojit systém IoT s vaší databází, prosím přečtěte si :doc:`IoT
dokumentace </aplikace/obecné/iot>“.

Nastavte terminály Lane/Desk/Move 5000 pro společnost Ingenico BENELUX
----------------------------------------------------------------

#Stiskněte tlačítko funkce (:guilabel:`F` na Lane/5000, :guilabel:`⦿` na Desk/5000 a
Přesunout(Move/5000).
#Přejděte na:menu-selection:Kasa menu --> Nastavení menu a zadejte heslo pro nastavení (výchozí:
   `2009`).
#Vyberte možnost „Změnit připojení“ a stiskněte tlačítko „OK“ na další obrazovce.
#Vyberte „TCP/IP“ a „IP adresu“.
#Na další obrazovce zadejte adresu vašeho systému Internet věcí (IP).
#Zadejte číslo 9000 jako port a stiskněte tlačítko OK na další obrazovce.

V tomto bodě se terminál restartuje a měl by být zobrazen na formuláři systému IoT v Odoo.

.. obrázek::ingenico/payment_terminal_02.png
:align:center

Zvolte způsob platby
----------------------------

Zapnout platební terminál:ref:`v aplikačních nastaveních <configuration/settings> a
Vytvořte související platební metodu <../../payment_methods>. Zadejte typ účetního záznamu jako
Vyberte „Banka“ a v poli „Použít platební terminál“ vyberte „Ingenico“.
Poté vyberte svůj terminál v poli „Způsob platby“.

.. obrázek: ingenico/payment-method.png

Jakmile je platební metoda vytvořena, můžete si ji vybrat ve svých nastaveních POS. Chcete-li tak učinit, přejděte na
Vyberte možnost „Nastavení POS“ (konfigurace/nastavení), klikněte na „Upravit“ a přidejte platební metodu.
pod záložkou „Platby“.
