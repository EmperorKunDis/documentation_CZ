=========
Daňové jednotky
=========

.. důležité::
Toto se vztahuje pouze na více společnostní prostředí.

Jednotka DPH je skupina plátců daně z přidané hodnoty, která je právně nezávislá na sobě navzájem.
jsou ekonomicky, organizačně a finančně propojené a proto jsou považovány za jedno
Plátce DPH. **Daňové jednotky** nejsou povinné, ale pokud se vytvoří, pak společnosti tvořící
jednotka musí patřit do stejné země, používat stejnou měnu a jedna společnost musí být
jakožto „zastupující“ společnost v rámci „daňového celku“. Daňové celky obdrží konkrétní
Daňové identifikační číslo určené pouze pro daňová přiznání. Společnosti, které jsou součástí koncernu, si ponechávají své daňové identifikační číslo
pro komerční účely.

.. příklad::
Společnost A dluží DPH ve výši 300 000 EUR a společnost B může získat zpět 280 000 EUR
DPH. Tvoří daňovou jednotku, která se vyrovnává dvěma částkami a musí být spolu uvedena.
jen zaplatit DPH ve výši 20.000 Kč.

Konfigurace
=============

Vytvořit daňovou jednotku, přejděte na: „Účetnictví“ -> „Konfigurace“ -> „Daňové jednotky“.
Klikněte na „New“. Zadejte jméno jednotky, vyberte zemi a
:guilabel:`Společnosti“ do jednotky „Hlavní společnost“, a
:guilabel:`Daňové identifikační číslo“ společnosti, která je součástí dané daňové jednotky.

Fiskální pozice
---------------

Vzhledem k tomu, že transakce mezi osobami tvořícími jednu daňovou jednotku nejsou předmětem DPH, je možné
vytvořit mapování daní (daňovou pozici) <../taxes/fiscal_positions>, aby se
aplikace DPH na vnitrostátní transakce.

Ujistěte se, že je vybrána konkrétní dceřiná společnost, pak přejděte na:
Konfigurace --> Daňové pozice, vytvořte novou **daňovou polohu** a klikněte na
V záložce „Mapování daní“ vyberte daň obvykle používanou pro
transakcím, které nejsou součástí daňového přiznání, a v poli „Daň k uplatnění“ vyberte nulový procentní sazbu.
Transakce, které jsou součástí celku.

Proveďte stejný postup pro záložku „Mapování účtů“, pokud je třeba, a opakujte celý proces
**každé** dceřiné společnosti v databázi.

.. Příklad:
Podle vašeho lokálního balíčku :doc:`lokalizace </aplikace/finance/fiskální_lokalizace>“ se daně
může být odlišná od obrázku zobrazeného na obrazovce.

.. obrázek: daňové jednotky/daňová místa.png
:alt: Mapování daňového zatížení pro daňové jednotky

Poté přidělte daňovou pozici otevřením aplikace **Kontakty**. Hledejte **členy**
firma a otevřít kartu kontaktu. Klikněte na záložku „Prodej a nákup“ a v
V poli „Daňová pozice“ zadejte daňovou pozici vytvořenou pro daný **daňový celek**.
Postup opakujte pro každou kartu společnosti ve formátu souboru, v databázi společností.

.. viz též:
:doc:`../dane/daňové-položky.

Daňový přehled
==========

Společnost zastupující daňové subjekty může získat agregovaný přehled o dani za dané období kliknutím na
„Účetnictví -> Vyúčtování -> Daňové přiznání“ a vybrat „Daňový subjekt“.
„Daňové jednotky“. Tento výkaz obsahuje souhrnné transakce všech „členů“
Export XML obsahuje jméno a DIČ hlavní společnosti.

.. obrázek: daňové jednotky/report.png
:alt: daňová jednotka daňový přiznání
