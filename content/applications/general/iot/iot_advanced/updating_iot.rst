==================
Aktualizace systému IoT
==================

Vzhledem k komplexnosti systémů IoT může pojem „aktualizace“ odkazovat na několik procesů včetně:

- :ref:`Aktualizace obrazu a jádra systému IoT <iot/updating_iot/image-code>“
- :ref:`Aktualizace handlerů <iot_updating_iot/handlers>, které zahrnují rozhraní a ovladače.“

.. _iot/aktualizace_iot/obrazový kód:

Aktualizace obrázku a jádra
==========================

.. záložky::

... skupina-tab:: IoT box

Pro ověření, zda je zařízení pro internet věcí aktuální (a případně jej aktualizovat), přejděte na
domovská stránka <iot/iot-box/homepage>“, klikněte na tlačítko „:icon:`fa-cogs`“ („:guilabel:`cogs`“)
v horním pravém rohu a pak v sekci „Verze“ klikněte na „Aktualizovat“.

.. tip::
:ref:`Zapněte vývojářský režim <developer-mode>, abyste viděli aktuální verze IoT Hub.
obraz a jádro krabice.

**Aktualizace obrázku**

Aby se aktualizovala obrazová data IoT krabičky, je nutné vyměnit její paměťovou kartu.
„BalenEtcher“ (<https://etcher.balena.io>), zdarma dostupný nástroj pro zápis disku
obrázky na paměťové karty.

.. poznámka::
         - Aktualizace obrazu systému IoT je často nutná po aktualizaci databáze Odoo.
novější verze.
         - Pro přehrávání paměťové karty je zapotřebí počítač s čtečkou/adaptérem na micro SD kartu.
         - Alternativní software pro zápis mikro SD karty je Raspberry Pi Imager
<https://www.raspberrypi.com/software/>`.

      #„Stáhněte si balenaEtcher.“ <https://etcher.balena.io/#download-etcher>
      #Vložte paměťovou kartu z IoT boxu do počítače nebo adaptéru.
      #Otevřete aplikaci BalenaEtcher, klikněte na „Zápis z URL“ a zadejte následující URL:
„http://nightly.odoo.com/master/iotbox/iotbox-latest.zip“.
      #Klikněte na tlačítko „Vybrat cíl“ a vyberte paměťovou kartu.
      #Klikněte na tlačítko „Flash“ a počkejte, až proces skončí.

.. obrázek:: aktualizace_iot/etcher-flash.png
:alt:  Formátování SD karty pomocí balenaEtcher

**Aktualizace jádra**

Aby jste aktualizovali jádro zařízení IoT boxu, klikněte na :guilabel:`Update“ pod :guilabel:`IoT Box Update“.
v okně „Aktualizace“.

..............
Proces může trvat déle než 30 minut. **Nedělejte nic s iot boxem, tedy nesuňte ho do nabíječky nebo jej nevypínáme**
V tomto případě by takové chování mohlo zařízení zanechat v nesourodém stavu a vyžadovat Internet věcí.
krabici, která bude znovu naprogramována novým obrázkem.

...... skupina-tab:: Windows virtuální IoT

Aktualizovat obraz a kód virtuálního zařízení s operačním systémem Windows:
<iot/windows_iot/odinstalovat> a :ref:`nainstalovat nejnovější verzi <iot/windows-iot/instalace>`.
balení.

.. _iot_updating_iot/handlers:

Aktualizace ovladače
=======================

Aby byly aktualizovány ovladače a rozhraní systému IoT a aby byly v souladu s
upravil kód serverového ovladače například tak, aby vyřešil problémy s zařízeními:
nefungují správně s IoT systémem, postupujte takto:

#Připojte se k:
stránce domovské stránky a klikněte na tlačítko „Kolečka“ (ikona: „fa-cogs“)
vpravo nahoře.
#Klikněte na tlačítko „Aktualizovat“ v sekci „Verze“.
#V okně „Aktualizace“ klikněte na „Znovu aktualizovat ovladače“.

.. důležité::
Pokud máte on-premise nebo Odoo.sh
</administration/odoo_sh/overview/introduction>` databáze musí být nakonfigurován.
Aby byl kód handlerů aktuální, aby zahrnoval nejnovější opravy a záplaty.

.. poznámka::
Řídicí aktualizace se také provádějí automaticky při každém restartování systému IoT, pokud
volba „Automatické aktualizace ovladačů“ je v nastavení „Technické informace“ zakázána.
informace“ v poli „IoT systém“ v Odoo.
