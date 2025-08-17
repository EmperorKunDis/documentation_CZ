====================
Sled faktur od dodavatele
====================

Při potvrzení dodavatelské faktury vytvoří Odoo jedinečný referenční číslo dodavatelské faktury.
používá sekvence formátu „BILL/rok/měsíc/početní hodnota“ (např. „BILL/2025/01/00001“).
restartuje každý rok od čísla 00001.

Je však možné změnit formát sekvenčního řazení:
a její periodičnost a k:ref:`fakturám za masivní sekvenování
<účetnictví/faktury dodavatelů/hromadné přeřazení>.

.. poznámka::
Změny v referenčních číslech jsou zaznamenány do chatu.

...účetnictví, faktury dodavatelů a přesuny:

Změna výchozího pořadí
=============================

Pro přizpůsobení výchozího pořadí otevřete poslední potvrzenou fakturu dodavatele a klikněte na tlačítko „Resetovat na
Vyberte a upravte číslo odkazu na fakturu dodavatele.

.. obrázek: sekvence/odkaz na sekvenci - číslo.png
:alt:Upravit číslo faktury dodavatele.

Odoo poté vysvětluje, jaký formát byl detekován a jak se bude aplikovat na všechny budoucí faktury od dodavatelů. Například
Pokud bude odvolán současný fakturační měsíc, období sekvence se změní na
místo každého měsíce.

.. obrázek: sekvence/sekvence-dialog.png
:alt:Upravit číslo faktury dodavatele.

.. tip::
Formát sekvence lze upravovat přímo při vytváření první faktury dodavatele daného
doba sekvence.

...účetnictví/faktury dodavatelů/hromadné přeřazování:

Výrobce masivně sekvenovaných vzorků fakturuje
==============================

Může být užitečné přeřadit více čísel faktur od dodavatelů. Například při importu faktur
faktury z jiného účetního systému a odkaz pochází ze staršího softwaru.
Pro letošní rok musí být zachována kontinuita bez obnovení od začátku.

.. poznámka::
Tato funkce je dostupná pouze uživatelům s přístupem správce nebo poradce.

Postupujte podle těchto kroků, abyste přesunuli čísla faktur dodavatelů:

#Aktivujte režim vývojáře:ref:`<developer-mode>`.
#V seznamu faktur od dodavatelů vyberte faktury, které potřebují nový řádek.
#Klikněte na ikonu „fa-cog“ a zvolte možnost „Změnit pořadí“.
#V poli „Pořadí“ vyberte možnost

   - :guilabel:`Udržet současný pořadí“: Pořadí číslic zůstává stejné.
   - :guilabel:`Řadit podle data účetního období“: Číslo je řazeno podle data účetního období.

#. Zadejte: guilabel:První nová sekvence.
#Klikněte na „Zobrazit změny“ a poté na „Potvrdit“.

.. obrázek:soubor/soubor-účet-sekvenování-souboru.png
:alt: Okno pro nastavení sekvencí

.. poznámka::
   - Aby bylo zřejmé, kde se změna řazení začala, první faktura v novém pořadí je
jsou zvýrazněny červeně v seznamu „Faktury dodavatele“ (viz guilabel: Vendor Bills). Tento vizuální znak je trvalý
a pouze informativní.
   - Pokud je v nové sekvenci nějaká nepravidelnost, jako mezery, zrušené nebo smazané
v otevřeném období, pak se zobrazí hlášení „Mezeru ve sledování“ (Guilabel).
:guilabel:"Faktury dodavatelů" v části účetnictví. Chcete-li zobrazit podrobnější informace o
spojené faktury dodavatele, klikněte na tlačítko „Díry v sekvenci“. Toto vizuální označení je dočasné.
a zmizí, jakmile bude datum účetního záznamu vstupu na nebo po datu uzamčení.

.. tip::
Resekvence není možná:

   - Pokud je vstup před datem uzavření.
   - Pokud se v pořadí objeví duplicitní záznamy.
   - Když je rozsah neplatný. Například když datum úhrady nesedí s
datum v nové sérii, například použít sérii 2024 (BILL/2024/MM/XXXX) pro fakturu dodavatele
datované do roku 2025.

V těchto případech se zobrazí chybová hláška „Validace selhala“.
