=======
IoT box
=======

Pro začít používat IoT box:

#Ujistěte se, že máte platnou předplatnou „IoT boxu“ navíc k
vaše předplatné Odoo.
#Připojte své zařízení k internetovému boxu.
#:ref:`Připojte k síti IoT box <iot/iot_box/network>.
#.:doc:`Připojte k vaší databázi Odoo IoT box <connect>“.

.. viz též:
„Videonávod: Jak nastavit a používat Odoo IoT Box: Průvodce pro začátečníky <https://www.youtube.com/watch?v=w2_Dcm3r_7o&ab_channel=Odoo>“

.. poznámka::
Zařízení lze také připojit po přidání krabičky IoT do sítě a/nebo po propojení.
databáze; přesto může být nutné restartovat IoT box.

... _iot/iot_box/síť:

Síťová konektivita
==================

IoT box lze připojit k síti pomocí :ref:`Ethernetu <iot/iot_box/network-ethernet>`, nebo
:ref:`Wi-Fi <iot/iot_box/sit_wi-fi>“.

.. důležité::
Všechny zařízení musí být připojena k stejné síti: IoT box, zařízení (zařízení), které je připojeno
do IoT krabičky a počítač připojený na Odoo.

... _iot/iot_box/síť ethernet:

Ethernet
--------

Zapojte síťový kabel do ethernetového portu v IoT boxu a volného portu na vašem routeru.
Připojit krabici IoT k napájení.

.. _iot/iot_box/síť_wifi:

Wi-Fi
-----

Zkontrolujte, zda není k internetu věcí připojený ethernetový kabel a postupujte podle těchto pokynů:

  #Připojte krabici IoT k napájení a počkejte pár minut, než se zapne.
  #Přihlaste se do nastavení Wi-Fi a vyberte síť vašeho IoT boxu. Název sítě je
formát IoTBox-xxxxxxxxxxxxxx (kde xxxxxxxxxxxxx je jedinečný identifikátor).
  #Připojte se k síti Wi-Fi v zařízení IoT a přihlaste se do něj. Váš prohlížeč by měl být automaticky
otevřít a přesměrovat na domovskou stránku „IoT boxu“ (<iot/iot-box/homepage>).

.. poznámka::
V závislosti na operačním systému může prohlížeč neotevřít a přesměrovat na krabičku IoT.
Webovou stránku lze otevřít ručně a navštívit adresu „http://10.11.12.1“.
nebo jakoukoli URL začínající **http** (např. „http://odoo.com“).

  #Na domovské stránce zařízení IoT klikněte na „Nastavení“ vedle „Stav internetu“.
části.
  #Počkejte pár minut na skenování dostupných sítí, vyberte síť, zadejte
Heslo Wi-Fi a klikněte na tlačítko „Připojit“.

.. poznámka::
Jakmile je zařízení připojeno k síti Wi-Fi, přestane vysílat své Wi-Fi signály a
Pokud počítač nebude automaticky připojen k původní síti, musíte se k ní znovu připojit.
ručně.

.. _iot/iot-box/homepage:

Stránka domovské stránky IoT boxu
================

Chcete-li zobrazit domovskou stránku IoT boxu, otevřete webový prohlížeč **na stejné síti jako je IoT box** a
Přejděte na IP adresu IoT boxu.

.. obrázek: iot_box/iot-homepage.png
:scale: 75 %
:alt: Domovská stránka zařízení IoT box

IP adresu IoT boxu lze získat následujícím způsobem:

- připojení k externímu monitoru: na obrazovce se zobrazuje IP adresa.

.... obrázek: iot_box/iot-pos-display.png
:skalka: 75 %
:alt:Přístroj na prodejní ploše s IP adresou IoT boxu

- připojení krabice IoT k tiskárně „podporovaného dokladu nebo štítku“ (https://www.odoo.com/app/iot-hardware)
s kabelem USB: automaticky se tiskne IP adresa.
- připojení k administračnímu rozhraní směrovače, ke kterému je připojen IoT box, nebo
třetí strany, která skenuje síť.

Jakmile je box připojen k databázi Odoo, můžete se dostat na jeho domovskou stránku
z Odoo otevřením aplikace IoT a kliknutím na odkaz zobrazený v kartě IoT boxu.
