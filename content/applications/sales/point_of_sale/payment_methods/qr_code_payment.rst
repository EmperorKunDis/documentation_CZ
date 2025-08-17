================
Platby pomocí QR kódu
================

Platby prostřednictvím QR kódu umožňují uživatelům vytvořit kód, který mohou zákazníci naskenovat pomocí svého mobilního bankovnictví.
aplikace pro zahájení převodu nebo okamžitou platbu.

Konfigurace
=============

Aktivujte a nastavte platby pomocí QR kódu
------------------------------------

Přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Nastavení“.

#Aktivujte nebo upgradujte balíček fiskální lokality své země podle:guilabel:`Fiscal
Řádku „Lokalizace“ k přístupu ke všem účetním funkcím specifickým pro danou zemi.
#Aktivujte pole „Kód QR“ v sekci „Platby zákazníků“.

Pak podle typu QR kódu postupujte dle příslušné dokumentace.
stránku z následující tabulky, abyste je nastavili.

.. seznam tabulkový::
:šířky: 20 20 20 40
:hlavičky: 1

   * – Druhy QR kódů
     - Název modulu
     - Technické označení
     - Popis
   * Pix
     - :doc:`Brazilské účetnictví<../../../finance/fiscal_localizations/brazil>`
     - „l10n_br“
     - Základní modul pro správu účetního rozvrhu a lokalizaci pro Brazílii.
   * FPS
     - :doc:`Hong Kong - účetnictví<../../../finance/fiscal_localizations/hong_kong>`
     - „l10n_hk“
     - Základní modul pro správu účetnictví a lokalizaci pro Hongkong.
   * – QRIS
     - :doc:`Indonéský - Účetnictví<../../../finance/fiscal_localizations/indonesia>`
     - l10n_id
     - Základní modul pro správu účetního rozvrhu a lokalizaci pro Indonésii.
   * PayNow
     - :doc:`Singapur - Účetnictví<../../../finance/fiscal_localizations/singapore>`
     - „l10n_sg“
     - Základní modul pro správu účetních výkazů a lokalizaci pro Singapur.
   * – QR-faktura
     - :doc:`Švýcarsko - Účetnictví<../../../finance/fiscal_localizations/switzerland>`
     - „l10n_cz“
     - Základní modul pro správu účetního deníku a lokalizaci pro Švýcarsko.
   * – PromptPay
     - :doc:`Thajsko - Účetnictví<../../../finance/fiscal_localizations/thailand>`
     - „l10n_th“
     - Základní modul pro správu účetního výkazu a lokalizaci pro Thajsko.
   * VietQR
     - :doc:`Vietnam - Účetnictví<../../../finance/fiscal_localizations/vietnam>`
     - l10n_vn
     - Základní modul pro správu účetního rozvrhu a lokalizaci pro Vietnam.
   * EPC
     - :doc:`Účet SEPA QR kód<../../../finance/accounting/customer_invoices/epc_qr_code>`
     - „account_qr_code_sepa“
     - Tento modul přidává podporu pro generování QR kódu SEPA Credit Transfer.

Vytvořte platební metodu
-------------------------

#Otevřete aplikaci Point of Sale.
#Přejděte na „Nastavení“ -> „Způsoby platby“ a vytvořte způsob platby.
#Založte si účetní knihu v bance.
#Vyberte položku „Aplikace banky (QR kód)“ pod záložkou „Propojení“.
#Vyberte možnost „Formát QR kódu“ z nabídky.

   - Vyberte pole „SEPA Credit Transfer QR“, pokud jste součástí Evropského prostoru platebních služeb.
(SEPA).
   - Zvolte: guilabel:„QR kód obchodníka předložený EMV“ pro ostatní typy QR kódu.

.. obrázek: qr_code_payment/qr-payment-methods-setting.png
:alt: Konfigurace metody placení prostřednictvím QR kódu
:skalka: 85 %

.. důležité:
Aby bylo možné platit QR kódy, musí být v účetní knize alespoň jedna definovaná bankovní
zaregistrované v aplikacích bank.

Jakmile je metoda platby vytvořena, přejděte do nastavení :ref:`POS <configuration/pos>“ a přidejte
Způsob platby na vašem POS v sekci „Platba“.

.. obrázek: qr_code_payment/qr-configuration-setting.png
:alt:Zapnout metodu placení přes QR kód
:skalka: 85 %

Registrujte platby pomocí QR kódů
================================

Při zpracování platby vyberte platební metodu pro platbu QR kódem. Vytvoří se
a zobrazeny na obrazovce pro zákazníka, který je může skenovat a platit pomocí své mobilní aplikace pro bankovnictví.

.. obrázek: qr_code_payment/qr-payment-example.png
:alt:Příklad platby přes QR kód
:skalka: 75 %

Klikněte na tlačítko „Potvrdit platbu“ (Guilabel:Confirm Payment) k potvrzení transakce.

.. důležité:
Odoo neověřuje platbu z banky. Uživatelé by měli ověřit platby provedené prostřednictvím banky.
validitu před potvrzením v registru POS.
