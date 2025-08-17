================
Zobrazovací plocha pro zákazníka
================

Funkce „Zobrazení zákazníka“ poskytuje zákazníkům v reálném čase informace o stavu pokladny na sekundárním
zobrazit.

.. obrázek:customer_display/display.png
:alt: obrazovka zákazníka

Konfigurace
=============

Podle vašeho nastavení POS může být tato funkce zobrazena na sekundárním monitoru.
<customer_display/local>“, „na jiném zařízení vzdáleně <customer_display/remote>“ nebo
:ref:`další monitor připojený k IoT boxu <zákaznický displej/IoT>“.

Chcete-li tuto funkci aktivovat, přejděte do nastavení POS, posuňte se dolů na položku „Připojená zařízení“
sekci a zaškrtněte políčko :guilabel:`Zobrazit zákazníka“.

.. obrázek::customer_display/feature-setting.png
:alt: Zobrazení nastavení pro zákazníka

... _zobrazení pro zákazníky/lokalita:

Místní
-----

Připojte druhý displej k terminálu pomocí HDMI nebo USB-C kabelu.

#:ref:`Zahájit sezení s terminálem <pos/session-start>“.
#Klikněte na ikonu „Hamburger Menu“ (ikona: „fa-bars“).
#Klikněte na ikonu „pracovní plocha“ (zobrazí se ikona s nápisem „Zákaznický monitor“) pro otevření nového okna, do kterého můžete přetáhnout.
spadnout na druhý obrazovku.

Pro terminály POS s aplikací pro Android a podporou dvou obrazovek

#Aktivujte modul Mobilní bod prodeje v sekci „Aplikace a moduly“
zobrazení pro zákazníky.
#Klikněte na ikonu „Hamburger Menu“ (ikona: „fa-bars“).
#Jakmile je nainstalován, klikněte na ikonu „fa-desktop“ (:guilabel: obrazovka zákazníka)
zobrazení na sekundárním displeji terminálu.

.. _vzdálené_zobrazení/klient:

Vzdálené
------

Připojte se k databázi z jiného zařízení (z jakéhokoliv počítače, tabletu nebo chytrého telefonu) a přejděte na POS.
aplikaci, klikněte na tlačítko vertikální elipsy (:guilabel:`⋮`) na platební kartě, a poté
:guilabel:`Zobrazení zákazníka“ a otevřete zobrazení vzdáleně.

.. poznámka::
Oba zařízení nemusí být připojena do stejné sítě.

.. _zobrazení zákazníka/IoT:

IoT systém
----------

Připojte k databázi IoT box a druhý monitor k IoT boxu. Poté přejděte na
V nabídce „Prodejní místo“ -> „Konfigurace“ -> „Nastavení“, posuňte se dolů na
V sekci „Připojené zařízení“ vyberte políčko „IoT Box“, a poté v rozevíracím seznamu druhé
monitor v poli „Zobrazit zákazníkovi“.

.. obrázek:customer_display/iot-settings.png
:alt: nastavení IOT pro připojení zákaznického displeje

.. poznámka::
Oba zařízení musí být připojena do stejné místní sítě.

.. viz též:
:doc:`../konfigurace/pos_iot`
