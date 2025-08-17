=======================
Přesuny procesních balíčků
=======================

Aplikace Odoo **Barcode** lze použít k zpracování převodů *Batch*, *Wave* a *Cluster*.
Vytvořené v aplikaci Inventář.

.. viz též:
Tento dokument popisuje kroky, jak zpracovat převody v aplikaci **Barcode**.
vytváření převodů naleznete níže:

   - :doc:`../../sklad/přijímání a expedice/vybírání/součástky“
   - :doc:`../../sklad/přijímání a expedice/vybírání/vlnový způsob vybírání
   - :doc:`../inventar/Vyskladnuti/Metody vyskladnuti/Cluster`

Zpracujte várku
-----------------

Nejdříve se přesuňte do nabídky „Čárový kód aplikace –> Operace“ a vyberte typ operace (např.
dodacích objednávek) seskupených do skupin. Zde vyberte kartu pro příslušnou skupinu
přesunout a kliknout na tlačítko „Batch“ v levém panelu.

.. obrázek:: process_transfers/batch-transfer.png
:alt:Stránka s objednávkami na dodání.

Na obrazovce přesunu balíčků jsou produkty v objednávce seskupeny podle místa a každá řádka
barevně rozlišené, aby byly spolu v jedné skladovací zóně.

Poté postupujte podle pokynů k „skenování čárového kódu pro skladovací místo“
první produkt. Skenujte čárový kód produktu a obalu, abyste mohli provést převod. Pro zaznamenání
Množství položek, klikněte na ikonu „fa-pencil“ a zadejte požadované
množství pro sklizeň.

Tento postup opakujte pro všechny produkty a klikněte na tlačítko „Potvrdit“
:guilabel:Dokončeno.

.. poznámka::
Po vytvoření balíčku přepravy a přiřazení balíčku k vyzvednutí navrhuje Odoo zadané
balíček zobrazit jméno *kurzívou* pod názvem produktu, aby si sběrači vždy všimli
produkty do správných krabic.

Produkty ze stejné objednávky jsou označeny stejnou barvou na levé straně. Dokončené vyzvednutí je
jsou zvýrazněny zelenou barvou.

.. příklad::
Ve skupinovém převodu pro 2 kusy „Skříň s dveřmi“, 3 kusy „Akustické blokové stěny“ a 4 kusy „Čtyřmístné
Desky, „3/3“ a „4/4“ značí, že poslední dvě položky v objednávce jsou
kompletní.

„Polovina“ jednotky „Skříň s dvířky“ byla již vybrána a po skenování produktu
barcode pro druhý skříňový systém, Odoo vyzve uživatele k zadání „Skenování sériového čísla“
unikátní sériové číslo pro :ref:`sledování produktů <inventory/product_management/enable-lots>`.

...... obrázek: proces_převodů/soubor.png
:alt:Produkty k vyzvednutí v přehledu čárových kódů.
