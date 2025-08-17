=========
Singapur
=========

Přidejte k fakturám QR kódy pro platbu přes PayNow
===============================

PayNow je platební služba, která umožňuje zákazníkům provádět okamžité domácí platby.
individuálními a obchodníky v singapurských dolarech prostřednictvím internetového a mobilního bankovnictví.

Aktivujte QR kódy
-----------------

Přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Nastavení“. Pod položkou „Zákazník
V sekci platby aktivujte funkci :guilabel:`QR kódy`.

Konfigurace účtu PayNow
---------------------------------

Přejděte na:menu:„Kontakty -> Konfigurace -> Bankovní účty“ a vyberte bankovní účet,
aktivujte službu PayNow. Zadejte typ proxy a hodnotu proxy
podle zvoleného typu.

.. důležité::
   - Země držitele účtu musí být nastavena na „Singapur“ v kontaktním formuláři.
   - Město držitele účtu je povinné.
   - Můžete také zahrnout číslo faktury do QR kódu pomocí :guilabel:`Zahrnout
Zaškrtněte políčko „Reference“.

.. obrázek: singapore/sg-paynow-bank-setting.png
:alt: Konfigurace účtu PayNow

.. viz též:
:doc:`../účetnictví/banka`

Konfigurace bankovního časopisu
--------------------------

Přejděte na záložku „Účetnictví“ – „Nastavení“ – „Knihy“, otevřete bankovní knihu a pak vyplňte
v poli „Číslo účtu“ a „Banka“ pod záložkou „Účetní případ“.

.. obrázek:singapore/sg-bank-account-journal-settings.png
:alt: Konfigurace účtu banky

Vystavujte faktury s QR kódy PayNow
-----------------------------------

Při vytváření nové faktury otevřete záložku „Další informace“ a nastavte položku „Způsob platby“.
Možnost „QR kód“ pro *EMV QR kód obchodníka předložený zákazníkovi*

.. obrázek: singapore/sg-qr-code-invoice-setting.png
:alt: Vyberte možnost předloženého platebního kódu QR

Zajistěte, aby pole „Příjemce banky“ bylo nastavené na tuto instituci, protože Odoo používá toto pole k
generovat QR kód pro službu PayNow.

.. _singapur/zaměstnanost-hero:

Mzdový systém Employment Hero
=======================

Pokud vaše podnikání již funguje s :doc:`Employment Hero
„<https://www.payroll-hero.com/hr/payroll/payroll_localizations/employment_hero>“, můžete použít náš konektor jako
alternativní řešení pro mzdy.

.. důležité::
Konfigurovat API služby Employment Hero pro **Singapur**.
použijte následující hodnotu jako :guilabel:`URL pro výplatu mzdy“: „HTTPS://apisg.yourpayroll.io/“.

