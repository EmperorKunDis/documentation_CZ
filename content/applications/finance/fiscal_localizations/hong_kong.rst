=========
Hongkong
=========

Konfigurace
=============

:ref:`Instalujte následující moduly, abyste získali nejnovější funkce v Hong Kong
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * - :guilabel:Hongkong - účetnictví
     - l10n_hk
     - Základní modul pro správu účetnictví a lokální nastavení pro Hongkong.
   * --:guilabel:Hongkong - mzdy
     - „l10n_hk_hr_mzdy“
     - Povoluje konkrétní lokální funkce pro modul *Odoo Payroll*
aplikace. Tento modul také nainstaluje:guilabel:`Mzdy v Hongkongu s účetnictvím`.
:guilabel:`Dokumenty – Mzdy v Hongkongu“.
   * – Hongkong – mzdy a účetnictví
     - `l10n_hk_hr_payroll_account`
     - Nainstaluje propojení mezi hongkongským mzdovým účetnictvím a účetnictvím.
   * – Dokumenty – Mzdy v Hongkongu
     - „dokumenty_l10n_hk_hr_mzdy“
     - Sloučí formuláře pro zaměstnance IR 56 do aplikace Odoo *Dokumenty*.

FPS QR kódy na fakturách
========================

Platforma pro rychlé platby FPS umožňuje zákazníkům provádět
okamžité platby v hongkongských dolarech nebo renminbi přes internet
a mobilní bankovnictví.

Aktivujte QR kódy
-----------------

Přejděte do sekce „Účetní aplikace“ – „Konfigurace“ – „Nastavení“. Pod položkou „Zákazník
V sekci „Platby“ zaškrtněte políčko vedle funkce „QR kódy“. Pak klikněte
:guilabel:`Uložit“.

Konfigurace účtu u FPS
------------------------------

Přejděte do aplikace „Kontakty“ → „Nastavení“ → „Bankovní účty“ → „Bankovní účty“.
Poté vyberte bankovní účet pro aktivaci FPS a pokračujte nastavením typu proxy a vyplněním
v poli „Zástupný výraz“ podle typu zvoleného.

Pamatujte na zahrnutí čísla faktury do QR kódu zaškrtnutím políčka „Zahrnout odkaz“.
zaškrtávací políčko.

.. obrázek: hong_kong/hk-fps-bank-setting.png
:align:center
:alt: Konfigurace účtu u FIO banky.

.. důležité::
   - Země, ve které je účet držitele vedený, musí být nastavena na „Hong Kong“ v kontaktním formuláři.
   - Město držitele účtu je povinné.
   - Můžete také zahrnout číslo faktury do QR kódu pomocí :guilabel:`Zahrnout
Zaškrtněte políčko „Reference“.

.. viz též:
:doc:`../účetnictví/banka`

Konfigurace bankovního časopisu
--------------------------

Přejděte na: „Účetní aplikace“ -> „Konfigurace“ -> „Deníky“ a otevřete deník bankovních transakcí.
Poté vyplňte pole „Číslo účtu“ a „Banka“, které se nacházejí v
:guilabel:`Záznamy v deníku“ záložka.

.. obrázek: hong_kong/hk-bank-account-journal-setting.png
:align:center
:alt: Konfigurace účtu v časopise Bank Account.

Vystavujte faktury s FPS QR kódy
--------------------------------

Při vytváření nové faktury otevřete záložku „Další informace“ a nastavte položku „Způsob platby“.
Možnost QR kódu: guilabel: EMV Merchant-Presented QR code.

.. obrázek: hong_kong/hk-qr-code-invoice-setting.png
:align:center
:alt: Vyberte možnost předloženého QR kódu obchodníkem.

Zajistěte, aby byl nastaven pole „Příjemce banky“, protože Odoo používá tento údaj k vytvoření
FPS - čárový kód.
