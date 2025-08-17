===================
Analýza pracovního vstupu
===================

Výchozí zpráva *Analýza pracovních vstupů* poskytuje přehled o ověřených pracovních vstupech.
aktuální měsíc. Chcete-li zobrazit tento výkaz, přejděte na: `Výplatní aplikace --> Zprávy -->
Analýza vstupu na trh práce“.

Výsledky práce se zobrazují v tabulce s výchozím filtrem „Tento měsíc:
Měsíc(Rok) a :guilabel:Potvrzeno. Různé typy :doc:`pracovních vstupů` naplňují
řádky, zatímco hodnoty „Celkem“ vyplňují viditelnou sloupcovou tabulku.

Pro změnu zobrazených informací klikněte na ikonu „+“ vedle hlavního menu.
sloupec, který zobrazuje rozbalovací nabídku dostupných metrik. Klikněte na jednu ze skupin dostupných metrik.
a data jsou dále uspořádána podle zvoleného metriku. Výchozí možnosti jsou: guilabel:'Práce
Typ vstupu“, „Zaměstnanec“ a „Oddělení“. Pokud je databáze více společnostmi,
Možnost „Společnost“ se také objevuje.

Srovnání analýzy pracovního vstupu
==============================

Je možné porovnat záznamy o pracovních činnostech za jeden časový úsek s předchozím časovým obdobím.
Pokud chcete porovnat tento údaj, nejprve přejděte na: `Payroll app --> Reporting --> Work Entry
Analýza.

Dále klikněte na ikonu „fa-caret-down“ (spodní šipka) v poli pro vyhledávání, což odhalí
klikněte na jednu z možností v sekci „Srovnání“ pod ikonou
:guilabel:`Aktuální měsíc: Předchozí období“ nebo „Aktuální měsíc: Předchozí rok“.

Zpráva aktualizuje a zobrazuje data pro aktuální časové období, data pro vybrané předchozí
doba trvání i rozdíl mezi nimi v procentech.

.. obrázek: work_entry_analysis/work-entry-comparison.png
:alt:Pivotová tabulka srovnávající pracovní záznamy za aktuální měsíc a předchozí měsíc.

.. poznámka::
Pokud nejsou pro konkrétní typ :ref:`pracovního záznamu <payroll/work-entries>
době, nebude se v záznamu objevit. To ale neznamená, že pracovní vstup typu
neexistuje nebo není nakonfigurována.

Navíc pokud se z filtru „Aktuální měsíc: (Měsíc) (Rok)“ odstraní výchozí hodnota :guilabel:`Current month: (Month)(Year)`
vyhledávací liště, sloupec „Srovnání“ se **neobjevuje**; musí být časový rámec.
vybrat pro zobrazení sloupce „Srovnání“.

Případ použití: porovnání přesčasových hlášení
====================================

Je možné upravit zprávu o analýze pracovních vstupů tak, aby ukazovala pouze přesčasy.
záznamy o pracovní době zaměstnanců za určité období. Chcete-li zobrazit tato data, nejprve přejděte na
Výchozí výstupní zpráva „Analýza mzdového vstupu“ se nachází na adrese:
Analýza vstupu na trh práce“.

Dále klikněte na ikonu „fa-caret-down“ (spodní šipka) v poli pro vyhledávání, což odhalí
rozbalovací nabídce. Pod sloupcem Filtry klikněte na tlačítko Přidat vlastní
Filtr“, v okně se zobrazí „Přidat vlastní filtr“.

Vyberte možnost z rozbalovací nabídky „Druh vstupu do práce“ pro první pole a nechte prostřední
pole tak, jak je (s vyplněním pole :guilabel:`je v`), a vyberte :guilabel:`Pracovní doba přesčas“.
poslední pole. Klikněte na „Přidat“ a všechny ostatní typy pracovních vstupů zmizí.
Ve sloupci „Pracovní doba přesčas“ se objevují pouze hodnoty.

Srovnat přesčasy z aktuálního měsíce s předchozím měsícem a zjistit, který měsíc byl více
přesčas odpracovaný, klikněte na ikonu „svislý znak“ (záporná čára) v hledání
baru. V sekci „Srovnání“ pod ikonou „Nastavení“ klikněte na „Tento měsíc:
Předchozí období“. Klikněte mimo rozbalovací nabídku, abyste ji zavřeli.

Nyní se v zprávě zobrazují přesčasy za aktuální měsíc a předchozí.
měsíc, spolu s „Variantou“, v procentech.

Pro zobrazení zaměstnanců s nejvíce přesčasovou prací klikněte na ikonu :icon:`fa-plus-square` :guilabel:`Přesčasy
Hodiny, které odhalují seznam možností. Klikněte na tlačítko „Zaměstnanec“ a všichni zaměstnanci s
zobrazí se záznam o přesčasové práci za aktuální nebo předchozí měsíc.

V tomto případě lze zjistit, že nejvíce přesčas pracoval:guilabel:`Marc Demo`.
„srpen 2024“, zatímco „Beth Evans“ pracovala nejvíce přesčasových hodin.
„Září 2024“. Dále „Mitchell Admin“ měla největší odchylku.
změna s -100% změnou z :guilabel:`srpna 2024` na :guilabel:`září 2024`.

.. obrázek: work_entry_analysis/variation.png
:alt:Porovnání přesčasů za září 2024 a srpen 2024.
