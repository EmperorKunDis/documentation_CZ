============
Odstranění metody LIFO
============

Strategie odstranění „poslední vstup, první výstup“ (LIFO) vybírá nejnovější produkty skladem podle
datum, kdy byly zboží přijaty do skladu.

Každý pokyn k nákupu produktů pomocí strategie LIFO (poslední vstupy, první výstupy)
převod je vytvořen pro sériové číslo, které bylo nejnověji přijato do skladu (tj. poslední).
číslo/sériové číslo, které bylo přijato do skladového zásobování.

.. viz také:
:doc:`O odstraňovacích strategiích <../removal_strategies>`

.. varování::
V mnoha zemích je LIFO (poslední vstup, první výstup) zakázané, protože může vést k tomu, že se zboží
Může vést k dodání starých, vypršelých nebo zastaralých výrobků zákazníkům.

Pojďme si ukázat příklad s produktem „Kamenný blok“, který je sledován:
V poli „Sklad“ v kartě produktu. V poli „Způsob odstranění“
pro kategorie produktu cihly je nastaveno: guilabel:First-In, Last-Out (FILO)

.. viz také:
   - :ref:`Nastavte strategii odstraňování skladů <inventory/warehouses_storage/removal-config>“
   - :ref:`Nastavit sledování skladových položek <sklad/skladové zásoby a skladování/nastavení skladových položek>`
   - :ref:`Zkontrolujte datum příjezdu <inventář/sklady a skladování/datum příjezdu>“

Následující tabulka uvádí skladové cihly a jejich různé čísla sériových výrobků.

.. seznam-tabulka::
:hlavičkové řádky: 1
:sloupek: 1

   * -
     - LOT 1
     - LOT2
     - LOT3
   * -Na skladě
     - 10
     - 10
     - 10
   * - :ref:`Vytvořeno dne <inventory/warehouses_storage/arrival_date>`
     - 1. června
     - 3. června
     - 6. června

Chcete-li vidět strategii odstranění v akci, vytvořte objednávku na dodání zboží.
za sedm cihel přesunutím se na obrazovku „Prodejní aplikace“ a vytvořením nové
citát.

Potvrďte prodejní objednávku, abyste vytvořili dodací objednávku. Tímto způsobem si rezervujete nejnovější dodání
čísla používají strategii LIFO (poslední vstup, první výstup).

Pro zobrazení podrobného výpisu klikněte na ikonu „⦙≣ (seznam bodů)“, která se nachází v
pravicových produktů cihelného zdivu v záložce „Dodávky“ v nabídce „Operace“.
dodržet pořadí. To způsobí, že se otevře okno „Přesun zboží“ s názvem „Otevřený přesun“.

V okně „Přesun otevřeného skladu“ se v poli „Odebrat z“ zobrazí
množství, které je nutné vybrat k naplnění požadavku, se bere z .
cihly z písku, nejnovější cihly z písku od společnosti „LOT3“ jsou vybírány podle metody LIFO (poslední vstup,
Strategie „První ven“).

.. obrázek: lifo/cihlové-bloky-vybírající.png
:align:center
:alt:Podrobná operace ukazuje, které položky jsou vybírány pro expedici.
