==========
Živé vysílání
==========

Jakmile jsou hotové všechny práce na návrhu webu a vývoji, je čas nasadit ho do vývojového nebo
databáze produkce.

.. /webové-šablony/spuštění-na-živou/modul-import:

Modulární import
=============

... /webové-šablony/spuštění-na-živou/modul-import/saas:

Odoo SaaS
---------

Postupujte takto při prvním dovozu modulu:

#Vytvořte archiv svého modulu.
#Připojte se k databázi projektu.
#Zapněte vývojářský režim.
#Přejděte do složky „Aplikace“, vyhledejte modul „base_import_module“ a nainstalujte jej, pokud je třeba.
#Klikněte na položku „Import modulu“ v nabídce.
#Nahrajte svůj soubor ZIP, zaškrtněte políčko „Začít od nuly“ a klikněte na tlačítko „Importovat aplikaci“.

.. obrázek: going_live/screenshot-import-module.png
:alt:Import modulu do Odoo Online

Pokud potřebujete znovu importovat modul po provedení nějakých změn, postupujte stejně, ale před
Přidejte modul, otevřete nabídku vývojáře a vyberte možnost „Stát se superuživatelem“.
Režim superuživatele, odhlásit se a znovu přihlásit.

.. důležité:
   - Nezapomeňte zaškrtnout políčko „Povolit inicializaci“ pouze v případě, že modul importujete podruhé.
Pokud ano, existující data mohou být ztracena. ([:ref:`Související s noupdate=1 <webové-tematické-stránky/strany-s-tematikou/noupdate>“]).
   - Velikost souboru ve formátu ZIP musí být menší než 50 MB.

.. viz též:
   - „Elearning Odoo: Registrace domény zdarma <https://www.odoo.com/slides/slide/register-a-free-domain-name-1663>“

... /webové-šablony/spuštění/modul-import/sh:

Odoo.sh
-------

Přejděte na záložku „Aplikace“ a klikněte na položku „Aktualizovat seznam aplikací“. Vyhledejte svůj modul
v seznamu a nainstalujte ji.

.. viz též:
:doc:`Úvod do Odoo.sh <../../../administration/odoo_sh/overview/introduction>`

... _webové šablony/spuštění webu/co dál:

Co bude dál?
============

Po importu a instalaci modulu a před spuštěním si zkontrolujte SEO.
směřuje i na vaši doménu.

.. viz též:

*SEO a přesměrování*

   - :/doc/:applications/websites/website/pages/seo
   - :ref:`webové stránky/stránky/přesměrování URL“

**Název domény**

   - :ref:`doménové jméno/existující“
