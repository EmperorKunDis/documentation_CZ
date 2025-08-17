====
Tyros
====

Připojení terminálu **Tyro** :doc:`pro platby <../terminals> umožňuje nabídnout plynulý způsob placení
plynout k vašim zákazníkům a usnadnit práci pokladních.

.. důležité:
**Terminály Tyro** jsou podporovány pouze v **Austrálii**.

.._přístupová konfigurace:

Konfigurace
=============

Párujte terminál s vaším POS systémem
--------------------------------------

#Klikněte na ikonu „fa-bars“ (i s hamburgerem) a „Nastavení plateb“ v
terminal.
#Zadejte heslo správce.
#. Posunutím dolů a kliknutím na „Párování s POS“
#Klikněte na tlačítko „Párování s terminálem“.
#Uložte si :guilabel:`MID“ (Merchant ID) a :guilabel:`TID“ (Terminal ID), které jsou nyní
zobrazené na obrazovce.

.. poznámka::
   - Heslo pro správu je heslo, které jste si zvolili při konfiguraci terminálu.
   - Kroků k dosažení obrazovky pro párování se může lišit v závislosti na typu terminálu.
jak konfigurovat různé terminály, najdete na webu Tyro.
<https://www.tyro.com/setup/>`.

Zvolte způsob platby
----------------------------

#Nainstalujte modul POS Tyro:ref:`<general/install>`.
#Vytvořit nový způsob platby:

   - Přejděte na: `Nastavení prodejního místa --> Platby --> Platební metody` a klikněte
:guilabel:`Nový“.
   - Nastavte položku „Deník“ jako „Banka“.
   - Vyberte pole „Terminál“ v poli „Propojení“.
   - Vyberte položku „Tyro“ v poli „Propojit s“.
   - Vyplňte pole „Tyro Merchant ID“ a „Tyro Terminal ID“ zadáním MID.
(ID obchodníka) a :abbr:`TID (identifikátor terminálu)` zobrazené na terminálu.
#Chcete-li spárovat platební metodu s terminálem, klikněte na tlačítko „Spojit se zařízením“.
Akce pošle požadavek na párování do terminálu, což trvá několik sekund.

.... obrázek: tyro/create-payment-method.png
:alt:Formulář pro vytvoření nového způsobu platby.

.... důležité::
Pole „Režim Tyro“ musí být nastaveno na „Provozní režim“.

Přidejte platební metodu na POS.
--------------------------------

Přidat platební metodu do svého terminálu:

#Přejděte do nastavení POS:ref:`<configuration/settings>`.
#Vyberte bod prodeje v poli „Bod prodeje“.
#Přidejte platební metodu pod pole „Způsoby platby“ v poli „Platba“.
části.
