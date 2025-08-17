=======
AsiaPay
=======

„AsiaPay“ je poskytovatel platebních služeb, který byl založen v Hongkongu a
s pokrytím několika asijských zemí a platebními metodami.

... _platební_prostředky/asiapay/konfigurovat_přístupový_panel:

Konfigurace na dashboardu společnosti AsiaPay
==================================

#Přihlaste se do dashboardu společnosti AsiaPay podle účtu poskytnutého společností AsiaPay.

   - „PayDollar“: Pro trhy v Hongkongu
CN, MO, TW, SG, MY, IN, VN, NZ a AU
   - „PesoPay <https://www.pesopay.com/b2c2/eng/merchant/index.jsp>“: Pro trh v PH
   - „SiamPay <https://www.siampay.com/b2c2/eng/merchant/index.jsp>“: Pro trh v Thajsku
   - „BimoPay <https://www.bimopay.com/b2c2/eng/merchant/index.jsp>“: Pro trh v Indonésii

#. Přejděte na „Profil“ → „Účet“. Zkopírujte hodnoty
:guilabel:`Měna“ a :guilabel:`Heslo“ pole a uložte je na později.
#. | Přejděte do sekce „Profil“ → „Nastavení účtu“ a zapněte možnost
:guilabel:`Návratová hodnota odkazu (datový proud)`;
|Zadejte adresu databáze Odoo následovanou /platba/asijská platba/webhook/.
:guilabel:`Vrácená hodnota odkazu (datový proud)“ pole textu. Například:
"https://vašespolečnost.odoo.com/platba/asiamoney/webhook";
|Klikněte na tlačítko „Test“ a zkontrolujte, jestli je webový konektor v pořádku.
#Klikněte na tlačítko „Aktualizovat“ pro dokončení konfigurace.

.. _platební_prostředky/asiapay/konfigurovat_odoo:

Konfigurace v Odoo
=====================

#Navštivte platebního poskytovatele AsiaPay a změňte jeho stav.
na: `Zapnuto`.
#|V záložce „Přihlašovací údaje“ vyberte značku svého účtu u společnosti Asiapay. Pak
vyplnit pole „Obchodní identifikátor“ a „Tajný klíč“,
:guilabel:`Měna“ v záložce „Nastavení“ s hodnotami, které jste uložili při
krok:ref:`platební_prostředky/asiapay/konfigurovat_přístupový_panel`;
|Výchozí nastavení platební brány AsiaPay je takové, že ověřuje tajný hash s hašem
funkce „SHA1“. Pokud je na váš účet nastaven jiný algoritmus,
<payment_providers/asiapay/configure_dashboard>`, aktivujte režim vývojáře
a nastavte stejnou hodnotu do pole :guilabel:`Secure Hash Function`.
:guilabel:`Přihlašovací údaje“ záložce.
#Nastavte si ostatní možnosti podle svého uvážení.

.. viz též:
   - :doc:`../platební_prostředky`
