================
Řazení faktur
================

Při potvrzení faktury vytvoří Odoo jedinečné číslo pro odkaz na fakturu. Výchozím nastavením používá
formát sekvence „INV/rok/zvyšující se číslo“ (např. INV/2025/00001), který začíná
„00001“ každý rok.

Nicméně je možné změnit formát sekvenčního čísla <účetnictví/faktura/resequencing>.
periodicitu a k :ref:`účetním dokladům s masivní re-sekvencí <účetnictví/doklady/masivní re-sekvence>“.

.. poznámka::
Změny v referenčních číslech jsou zaznamenány do chatu.

...účetnictví, fakturace, přeřazení:

Změna výchozího pořadí
=============================

Pro přizpůsobení výchozího pořadí otevřete poslední potvrzenou fakturu a klikněte na tlačítko Reset to
Vytvořit a upravit číslo odkazu na fakturu.

.. obrázek: sekvence/odkaz-na-obrázek.png
:alt: Upravit číslo faktury.

Odoo pak vysvětluje, jaký formát bude aplikován na všechny budoucí faktury. Například pokud
Přidá se měsíc současné faktury a období sekvencí se změní na každý měsíc.
každý rok.

.. obrázek: sekvence/sekvence-dialog.png
:alt: Upravit číslo faktury.

.. tip::
Formát sekvence lze upravovat přímo při vytváření první faktury dané sekvence.
období.

...účetnictví, fakturace, masivní reorganizace

Masivní přeřazení faktur
==========================

Může být užitečné přeřadit více čísel faktur. Například při importu faktur z
další fakturační nebo účetní systém a odkazuje se na předchozí software
Pro letošní rok musí být zachována kontinuita bez obnovení od začátku.

.. poznámka::
Tato funkce je dostupná pouze uživatelům s přístupem správce nebo poradce.

Postupujte takto, pokud chcete změnit číslo faktury:

#Aktivujte režim vývojáře:ref:`<developer-mode>`.
#Otevřete si zástupce „Účetnictví“ a v něm pak záznamy „Faktury zákazníkům“.
#Vyberte faktury, které potřebují nový řádek.
#Klikněte na ikonu „fa-cog“ a zvolte možnost „Změnit pořadí“.
#V poli „Pořadí“ vyberte možnost

   - :guilabel:`Udržet současný pořadí“: Pořadí číslic zůstává stejné.
   - :guilabel:`Řadit podle data účetního období“: Číslo je řazeno podle data účetního období.

#. Zadejte: guilabel:První nová sekvence.
#Klikněte na „Zobrazit změny“ a poté na „Potvrdit“.

.. obrázek: Sekvence/fakturační sekvence.png
:alt: Okno pro nastavení sekvencí

.. poznámka::
   - Pro uvedení místa začátku změny se jako první faktura v nové sérii
jsou zvýrazněny červeně v seznamu faktur pro zákazníky (viz guilabel: Customer Invoices). Toto vizuální označení je trvalé
a pouze informativní.
   - Pokud je v nové sekvenci nějaká nepravidelnost, jako mezery, zrušené nebo smazané
v otevřeném období, pak se zobrazí hlášení „Mezeru ve sledování“ (Guilabel).
:guilabel:`Faktury zákazníkům“ v účetním přehledu. Chcete-li zobrazit podrobnější informace o
klikněte na příslušný fakturu, pak na „Díry v sekvenci“. Tento vizuální ukazatel je dočasný
a zmizí, jakmile bude datum účetního záznamu vstupu na nebo po datu uzamčení.

.. tip::
Resekvence není možná:

   - Pokud je vstup před datem uzavření.
   - Pokud se v pořadí objeví duplicitní záznamy.
   - Když je rozsah neplatný. Například když není v souladu s datem faktury
datum v nové sérii, například použitím série 2024 (INV/2024/XXXXX) pro fakturu s datem
v roce 2025.

V těchto případech se zobrazí chybová hláška „Validace selhala“.
