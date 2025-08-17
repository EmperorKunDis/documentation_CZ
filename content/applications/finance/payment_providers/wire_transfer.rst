==============
Převody peněz
==============

Zaplacení prostřednictvím „Převodu“ umožňuje uživatelům poskytnout pokyny k platbě.
například číslo účtu a referenci, kterou je třeba uvést při platbě. Tyto pokyny jsou
zobrazené po tom, co si zákazník vybere platební metodu „Převod peněz“ a klikne na
:tlačítko „Zaplaťte teď“ na konci procesu objednávky na vašem e-shopu nebo
na zákaznické portále.

.. obrázek: wire_transfer/payment_instructions_portal.png
:skalka: 80 %
:alt:Platební pokyny na zákaznickém portálu

.. poznámka::
   - Tento způsob je snadno dostupný a vyžaduje minimální nastavení, ale není efektivní.
Procesově. Doporučujeme nastavit si :doc:`platebního poskytovatele <../payment_providers>
místo toho.
   - Online objednávky zůstávají v stavu „Poptávka odeslána“ (tj. nezaplacená objednávka), dokud
přijmout platbu a ručně potvrdit objednávku.

.. tip::
**Převod peněz** může být použita jako vzor pro jiné způsoby platby, které jsou zpracovávány
přidáním manuálních úkonů, jako jsou kontroly, přejmenování nebo kopie.

Konfigurace
=============

Pro konfiguraci převodu peněz:

#:ref:`Přejděte na platební metodu převod peněz <payment_providers/supported_providers>“.
#V záložce „Konfigurace“ vyberte, zda chcete vytvořit poznámku nebo komunikaci.
vedle pokynů k úhradě by měla být zobrazena:

   - :guilabel:`Na základě odkazu na dokument“: číslo objednávky nebo faktury
   - „Založeno na zákaznické identifikaci“: zákaznická identifikace

#Zapněte možnost „QR kódy“ v části „Možnosti“.

.. poznámka::
:doc:`Potřeba dalšího účetního nastavení <../accounting/customer_invoices/epc_qr_code>“
využívat QR kódy.

#Definujte platební pokyny v záložce „Zprávy“. Pokud je zadáno číslo účtu, pak se použije :doc:`bankovní
<../účetnictví/banka> již byla definována a automaticky se k ní přidává číslo účtu.
výchozí zpráva generovaná Odoo. Můžete ji také přidat později a aktualizovat zprávu
kliknutím na tlačítko „Znovu načíst zprávu“.

.. obrázek:: wire_transfer/payment_instructions.png
:alt:Definice platebních pokynů

#Nastavte pole :guilabel:`Stát“ na hodnotu :guilabel:`Zapnuto“.

.. tip::
Můžete také otestovat převody peněz pomocí :ref:`platebních metod/testovací režim`.

.. viz též:
:doc:`../platební_prostředky`
