Zobrazit obsah

========
Náklady
========

Odoo **Náklady** usnadňuje správu výdajů. Po podání zaměstnancem svých nákladů
V Odoo jsou schvalovány manažerskými a účetními týmy. Po schválení pak mohou být
zpracována a vrácena zaměstnanci na úhradu nákladů.

.. viz též:
`Odoo Náklady: stránka produktu <https://www.odoo.com/app/expenses>`_

Nastavení kategorií výdajů
======================

Prvním krokem při sledování výdajů je nastavení různých typů výdajů pro firmu.
(spravované jako kategorie nákladů v Odoo). Každá kategorie může být tak konkrétní nebo obecná,
je potřeba. Přejděte na: `Nastavení aplikace - Výdaje --> Kategorie výdajů` a zobrazí se
současné položky kategorie výdajů v základním zobrazení seznamu.

.. obrázek: výdaje/kategorie.png
:align:center
:alt:Nastavte náklady na produkty.

Pro vytvoření nové položky výdajů klikněte na „New“. Zobrazí se formulář s produktem.
Popisové pole označené guilabel: „Název produktu“.

.. poznámka::
Kategorie výdajů se v Odoo spravují podobně jako produkty. Formulář pro kategorii výdajů je tedy
standardní produktová forma v Odoo a informace zadaná jsou podobné. Nákladové položky budou
Jejich označení se v tomto dokumentu používá jako kategorie výdajů, protože hlavní nabídka je na ně odkazuje.
:guilabel:`Kategorie výdajů“.

Pouze dvě pole jsou nutná, a sice „Název produktu“ a „Jednotka měření“.
Do pole zadejte „Název produktu“ a vyberte jednotku měření ze seznamu
rozbalovací nabídka (většina produktů bude nastavena na :guilabel:`Jednotky`).

.. tip::
Aplikace Sales je místem, kde se vytváří a upravují specifikace jednotek měření (např.
jednotky (mil, nocí atd.)). Vyberte v nabídce :menuselection:`Prodejní aplikace --> Konfigurace --> Nastavení
zajistit, aby se v části „Katalog produktů“ zobrazovaly jednotky měření. Klikněte na
:guilabel:`Jednotky měření“ vnitřní odkaz na :doc:`zobrazení, vytvoření a úpravu jednotek měření
<../inventar-und-mrp/Inventar/Produktverwaltung/Konfigurieren/Einheit>.

.. obrázek: výdaje/nové-výdajové-produkty.png
:align:center
:alt:Nastavte náklady na produkty.

V poli „Cena“ na kartě produktu je výchozí hodnota 0,00.
U konkrétních výdajů se vždy vyplácí určitá částka, ta se uvede do
V opačném případě nechte pole „Cena“ nastaveno na hodnotě 0,00 a zaměstnanci
v žádosti o proplacení nákladů uveďte skutečnou cenu.

.. poznámka::
V poli „Náklady“ je vždy vidět pole „Náklady“, ale na kartě výdajů se zobrazuje pouze tehdy,
:guilabel:`Prodejní cena“ pole je viditelné pouze v případě, že je vybrána „Prodejní cena“ pod
sekci „Znovuúčtování výdajů“. Jinak je pole „Prodejní cena“
skryté.

.. příklad::
Zde jsou příklady, kdy je vhodné nastavit pro konkrétní produkt specifickou hodnotu :guilabel:`Cost`,
:guilabel:`Náklady“ na „0,00“:

   - Jídlo: nastavte hodnotu nákladů na 0,00. Když zaměstnanec zadá výdaj za jídlo
Pokud uvedou skutečnou částku faktury, bude jim vrácena právě tato částka.
Pokud byste si objednali jídlo za 95,23 dolarů, dostali byste zpět 95,23 dolarů.
   - Dojezdová vzdálenost: nastavte hodnotu nákladů na 0,30. Když zaměstnanec uvede výdaj,
„najeté kilometry“, zadávají do pole „Kvantita“ číslo ujetých kilometrů a
a za každých ujetých 100 mil dostali zpět 0,30 $.
     $30.00.
   - „Měsíční parkování“: nastavte „Náklady“ na 75,00 Kč. Když zaměstnanec uvede výdaj za
„měsíční parkování“, náhrada by byla 75 $.
   - Náklady: nastavte hodnotu :guilabel:`Náklady“ na „0,00“. Když zaměstnanec zadá výdaj, který není
pokud jde o stravné, náhrady za cestovní výdaje nebo měsíční parkování, používají produkt „Náklady“ (:guilabel:`Expenses`).
náklady na notebook za 350 dolarů by byly zaznamenány jako položka :guilabel:`Náklady`,
pokud byste chtěli vrátit peníze, bude vám vráceno 350 dolarů.

Vyberte „Účet pro výdaje“ v aplikaci Odoo *Účetnictví*. Doporučujeme zkontrolovat
s účtárnou, aby se zjistilo správné číslo účtu, na který odkazuje v tomto poli.
bude ovlivňovat zprávy.

Zaplaťte daně z každého produktu v polích „Dodavatelské daně“ a „Daň odběratele“.
aplikovatelné. Je považováno za dobrou praxi používat daň, která je konfigurována s :ref:`Daň Zahrnuta
v ceně <dani/zahrnuté v ceně>“. Pokud je tato hodnota nastavena, automaticky se konfigurují daně.

.. viz též:
   - :doc:`náklady/zaznamenávání nákladů“
   - :doc:`náklady/účty za výdaje“
   - :doc:`expenses/approve_expenses`
   - :doc:`výdaje/poštovné a doprava“
   - :doc:`výdaje/proplacení
   - :doc:`náklady/převod nákladů“

..toctree::


výdaje/účetní záznamy
náklady/účetní výkazy
výdaje/schválení výdajů
výdaje/náklady po ukončení
výdaje/vrácení
výdaje/fakturace výdajů
