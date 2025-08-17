==================
Vnitřní přesuny
==================

Vnitřní převody peněz lze řešit v Odoo. Nejlépe se hodí dva účty, jeden bankovní a druhý hotovostní.
převádět peníze mezi vlastními účty.

.. viz též:
:ref:`Jak přidat další bankovní účet <účetnictví/banka/vytvořit>`

Konfigurace
=============

Vaše databáze automaticky vytvoří interní převodní účet na základě vaší společnosti.
:dokumentu:<../../fiskální_lokalizace> a v závislosti na legislativě vaší země.
změnit výchozí účet „Vnitřní převod“, přejděte na „Účetnictví –>
Konfigurace --> Nastavení a posuňte se dolů do části „Výchozí účty“.

Převést peníze mezi jednotlivými bankami
======================================================

Pokud se peníze převádějí z jedné banky nebo hotovostní pokladny do druhé, objeví se jako dvě
transakce na příslušných účtech, ať už vznikly ručně nebo
dováží se nebo je synchronizován bankou.
vyberte „Vnitřní převody“ jako :guilabel:`výkazový model <reconciliation_models>
tlačítko. Toto tlačítko pro modelu vyrovnání zapisuje transakci do :guilabel:`Vnitřní
Transferový účet.

.. tip::
Při zpracování transakce si nezapomeňte zaevidovat obě výstupní transakce na účetnictví, které odesílá
platba a příchozí transakce na deník, který přijímá platbu.

.. příklad::
Příkladem může být převod 1000 dolarů z banky A do banky B:

   - Bankařský časopis (Banka A)

..... seznamová tabulka::
:hlavičkové řádky: 1
:sloupek: 1

        * – Účet
          - **Debet**
          - **Zdroj**
        * - Účet v bance A
          -
          - $1,000
        * - **Vnitřní převod účet**
          - **$1,000**
          -

   - Bankovní noviny (Banka B)


..... seznamová tabulka::
:hlavičkové řádky: 1
:sloupek: 1

        * – Účet
          - **Debet**
          - **Zdroj**
        * - Účet v bance B
          - $1,000
          -
        * - **Vnitřní převod účet**
          -
          - **$1,000**

.. viz též:
   - :doc:`usmíření“
   - :doc:`model_souznění“
