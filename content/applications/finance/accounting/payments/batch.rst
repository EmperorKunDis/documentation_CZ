==============
Skládané platby
==============

Skládání plateb od více zákazníků nebo dodavatelů do jedné platby umožňuje
generování podrobných pokladních dokladů nebo platebního souboru s referencí várky.
používá se během procesu sjednocení účtů, aby byly shodné bankovní transakce s
příslušné platby. Tato funkce je zejména užitečná při zasílání :doc:`SEPA Direct Debit
placení <batch_sdd>“, vložením hotovostních plateb nebo :ref:`šeků <účetnictví/platby/šeky>“.
generování výstupních souborů platebního příkazu, např. :doc:`SEPA <pay_sepa>` nebo :ref:`NACHA <l10n_us/nacha>`.

Konfigurace
=============

Pro zapnutí hromadných plateb přejděte na: „Účetnictví --> Konfigurace --> Nastavení“, posuňte
a do sekce „Platby zákazníků“ a zapnout „Sběrné platby“.

...účetní/soubor/vytvoření:

Vytváření balíčků
==============

Pro vytvoření hromadné platby postupujte takto:

#Ujistěte se, že všechny platby, které mají být zahrnuty do bloku, byly :ref:`zaregistrovány
<účetnictví/platby/z faktury - daňový doklad>.
#Přejděte na: „Účetnictví“ -> „Zákazníci“ -> „Platby“.
#Vyberte platby, které chcete zahrnout do souboru.

.. poznámka::
Všechny platby v transakční sadě musí používat stejný způsob platby. Pokud je potřeba, mohou být platby seskupeny.
pomocí pole „Způsob platby“.

#Klikněte na tlačítko „Vytvořit sérii“ nebo klikněte na ikonu „fa-cog“ a vyberte
:guilabel:`Vytvořit hromadnou platbu“.
#Vyberte si platby v blokové fakturaci a zkontrolujte vybrané platby. Pokud byly některé jednotlivé platby přehlédnuty,
Klikněte na tlačítko „Přidat řádek“ a vyberte chybějící platby, které mají být zahrnuty do souboru.
#Jakmile budou všechny platby zahrnuty, klikněte na tlačítko „Potvrdit“ a poté na „Ukončit“.

.. poznámka::
Jednou potvrzená platba již nelze do bloku přidat.

.. tip::
   - Klikněte na tlačítko „Tisk“ pro stažení seznamu zaplacených částek.
   - Pro zobrazení stávajících hromadných plateb přejděte na: „Účetnictví“ -> „Zákazníci“ -> „Hromadné platby“.
„Platby“.

Bankovní vyrovnání
-------------------

Jakmile jsou v databázi vytvořeny transakce bankovního účtu :doc:`(viz. /bank/transactions)`, můžete
:ref:`sjednotit je s hromadnou platbou <sjednocení/hromadné platby>“.

.. viz též:
   - :doc:`../platební_karty`
   - :doc:`batch_sdd“
