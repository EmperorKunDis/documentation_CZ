=========================
Správa více zaměstnanců
=========================

Odoo POS nabízí funkci „Přihlášení zaměstnanců“, která umožňuje více uživatelům
:ref:`přihlásit se do režimu POS <pos/employee_login/use>“. Aktivací této funkce umožníte
Tyto kroky:

- Vyberte konkrétní uživatele, kteří mohou „přihlásit se do POS“ (<pos/employee_login/use>).
- :ref:`Přidělte základní nebo pokročilé oprávnění <pos/employee_login/configuration> těmto uživatelům.“
- :ref:`Sledujte zaměstnance, kteří se podílejí na každé objednávce pro vylepšenou analýzu <pos/analytics>“.

... /pracovníka/přihlašování/konfigurace:

Konfigurace
=============

Přejděte do sekce „PoS Interface“ v části :guilabel:`PoS Interface` a přihlaste se k vícenásobnému uživateli.
Nastavení <konfigurace/nastavení>. Pak

#Aktivujte funkci „Přihlášení pomocí zaměstnanců“.
#Přidejte zaměstnance s **základními funkcemi POS** v poli „Základní práva“.
#Přidejte zaměstnance s **rozšířenými funkcemi POS** do pole :guilabel:`Dovolené funkce`.

.. obrázek:employee_login/activate-setting.png
:alt: nastavení pro více pokladních míst v POS

.. poznámka::
   - Ponechání pole „Základní práva“ prázdné umožňuje všem zaměstnancům přihlásit se.
   - Ponecháním pole „Další práva“ prázdné udělujete rozšířená práva pouze uživatelům Odoo.

..tip:
Klikněte na tlačítko s ikonou „vertikální elipsa“ v pravém horním rohu.
a kartu POS a „Upravit“ pro přístup ke konfiguraci z hlavního panelu POS.

.. viz též:
:doc:`../obecne/uzivatele/prava_pristupu`

.. záložky::
.. tab:: Základní práva

Zaměstnanci s oprávněním k základnímu přístupu mohou v POS provádět následující akce:

**Správa relací:**

      - :ref:`Otevřete sezení POS <pos/session-start>“.
      - :ref:`Provádějte hotovostní operace (<pos/cash-register>)“.
      - Zamkněte aktuální sezení POS.

**Prodejní transakce:**

      - :ref:`Proces běžných prodejních transakcí <pos/sell>`.
      - :ref:`Zpracování vrácení peněz <pos/refund>`.
      - :doc:`Přístup a zpracování objednávek <shop/sales_order>“.
      - :ref:`Nastavit zákazníky <pos/customers>“.
      - Přístup k historii objednávek včetně současných objednávek.

**Ceny a slevy:**

      - Zvolte ručně jiný ceník: doc:`cena <pricing/pricelists>`.
      - Zadejte slevový kód.
      - :doc:`Ručně aplikovat slevy <cena/slevy>“.
      - Manuálně změňte cenu produktu (<pos/sell>).
      - Přepněte mezi: doc:`daňovými pozicemi <ceny/fiskální_pozice>“.

....... tab:: Povolené práva

Kromě základních práv mají zaměstnanci s rozšířenými právy také možnost:

      - Přihlaste se do rozhraní Odoo Backend.
      - Vytvářet produkty.
      - :ref:`Ukončit aktuální sezení POS <pos/session-close>“.

.. _pos/employee_login/use:

Použití
================

Přihlášení
----------

Jakmile je funkce „Přihlásit se pomocí zaměstnanců“ zapnutá, musí zaměstnanci přihlásit do :ref:`obchodu
sesí a připojit se k POS rozhraní. Mohou:
<pos/employee_login/badge>`, klikněte na ikonu „fa-users“ (ikona „uživatelé“)
jméno z seznamu oprávněných uživatelů nebo zadáním jejich hesla
„PIN“ do pole „Zadejte svůj PIN“.

.. obrázek::employee_login/log-in.png
:alt:Okno přihlášení, které se otevře při aktivním režimu více pokladen

Přepínání mezi uživateli během aktivní relace (viz :ref:`povolení relace <pos/session-start>`):
Jméno přihlášeného zaměstnance v pravém horním rohu obrazovky POS a vyberte uživatele, který chcete přepnout.

..tip:
V případě chybějícího skenování klikněte na ikonu „čárový kód“ (ikona „Barcode“) pro skenování
čárové kódy pomocí webové kamery.

.. _pos/employee_login/badge:

Přihlášení pomocí štítků
----------------------

Zaměstnanci se mohou přihlásit pomocí své karty. Chcete-li nastavit přihlášení na základě karty, přidělte jedinečný identifikátor karty.
profil zaměstnance v modulu **Zaměstnanci**:

#Nyní se přesuňte do modulu „Zaměstnanci“.
#Otevřete formulář pro konkrétního zaměstnance.
#Přejděte na záložku „Nastavení“.
#Kategorie „Přítomnost / bod prodeje / výroba“ nabízí dvě možnosti:

   - Do pole „ID štítku“ zadejte ručně jakékoliv ID štítku.
   - Klikněte na tlačítko „Vytvořit“ a automaticky vám bude přidělena jedinečná identifikace štítku.
#Klikněte na tlačítko „Tisk štítku“ pro generování kódu, který reprezentuje přidělené číslo štítku.

Pokud chcete přepnout uživatele v otevřené POS sezení pomocí štítku, musíte nejprve zablokovat sezení.
Klikněte na ikonu „fa-lg fa-lock“ (:guilabel:„zamčeno“) a poté se vrátíte zpět na obrazovku přihlášení.
Zaměstnanec může svou identifikační kartu přiložit ke čtečce, aby se přihlásil.

.. _pos/zaměstnanec/přihlašovací kód:

Přidání PIN kódu
-----------------

Z důvodu zvýšené bezpečnosti mohou zaměstnanci být nuceni zadat kód PIN při každém přihlášení do terminálu.
session. Pro nastavení hesla pro zaměstnance:

#Nyní se přesuňte do modulu „Zaměstnanci“.
#Otevřete formulář pro příslušného zaměstnance.
#Přejděte na záložku „Nastavení“.
#Zadejte požadovaný číselný kód do pole :guilabel:`PIN Code`.
:guilabel:`Přítomnost/Prodej/Výroba“ kategorii.

.. poznámka::
PIN kód musí obsahovat pouze sekvenci číslic.
