Zobrazit obsah
:skrýt obsah stránky:
Nebylo nalezeno žádné související video.

========================
Internet věcí (IoT)
========================

Odoo Internet of Things (IoT) umožňuje propojit fyzické zařízení jako čtečky čárových kódů nebo účtenkové tiskárny.
tiskárny, platební terminály, měřicí přístroje atd.) do databáze Odoo pomocí systému IoT.

Podporované systémy IoT jsou následující:

- :doc:`IoT box <iot/iot_box>“: mikropočítač, zařízení „plug and play“ (tj. program Odoo IoT)
(předinstalované).
- :doc:`Virtuální Windows IoT <iot/windows_iot>“: Program pro Windows, který lze nainstalovat
na počítači s operačním systémem Windows.

.. poznámka::
   - :zkratka MRP (plánování materiálových požadavků), včetně kamer a měřicích nástrojů
Není kompatibilní se virtuálními zařízeními IoT od společnosti Microsoft.
   - Může být použito více systémů IoT současně.
   - Je také možné vytvořit virtuální počítač Windows na počítači MacOS nebo Linuxu.
Tato možnost není podporována v Odoo a nebude poskytnuta žádná pomoc při řešení problémů.

... _iot/iot/iot-subscription:

Předplatné za IoT box
====================

Pro průmyslové využití systémů IoT je nutná předplatná za IoT box. Pokud máte problémy s
kontaktujte správce databáze nebo poskytovatele služeb Odoo pro pomoc.

.. tip::
Pokud je předplatné spojeno s uživatelem portálu „Odoo.com <https://www.odoo.com>“, zkontrolujte
informace na stránce s předplatným portálu.

.. viz též:
   - „Souladné zařízení IoT“ (https://www.odoo.com/app/iot-hardware)
   - „Návody Odoo: Návody pro internet věcí (IoT)
<https://www.odoo.com/slides/internet-of-things-iot-175>
   - „FAQ systému IoT <https://www.odoo.com/app/iot-faq>“
   - „Zázračný list – Odoo Internet of Things [PDF]


.. karty:

......karta: IoT box
:target: iot/iot_box
:velké:

Nainstalujte IoT box.

...... karta:: Windows virtuální IoT
:target: iot/windows_iot
:velké:

Nastavte virtuální Windows IoT.

......karta: Připojení systému IoT k Odoo
:target: iot/connect

Připojte systém IoT k databázi Odoo a řešte případné problémy s připojením.

...... karta: Zařízení
:target: iot/zařízení

Připojte zařízení jako tiskárny, obrazovky, měřicí nástroje atd. k systému Internetu věcí.

......karta: HTTPS certifikát
:target: iot/iot_advanced/https_certifikát

Zkontrolujte, zda je vaše systém a databáze splňují požadavky na certifikát HTTPS
generaci a řešit případné související problémy.

......karta: Aktualizace systému Internet věcí
:target: iot/iot_advanced/aktualizace_iot

Aktualizujte obrazovku, jádro a ovladače svého systému IoT, abyste mohli využít nejnovější opravy pro IoT
a funkce nebo obnovit systém IoT, pokud je třeba.

..toctree::


iot/iot_box
iot/windows_iot
iot/connect
iot/iot_advanced
iot/zařízení
