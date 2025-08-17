=============
Přenesená daňová ztráta
=============

Při zpracování daňových přiznání lze využít funkci **daňové opravy**, která umožňuje přenášet částky mezi jednotlivými obdobími.
do jiné bez vytváření nových záznamů.

Vznikla proto, aby vyhověla právním požadavkům konkrétních lokalit, kde je nutné
přenesena z období do období (například protože součet řádku je záporný).

Tato funkce je v zemích, kde je vyžadována, jako například ve Francii nebo Belgii, aktivní výchozí hodnotou.
Itálie. Není potřeba žádné specifické konfigurace.

Pojďme si vzít příklad belgické společnosti, která vytvořila kreditní poznámku ve výši 100 pro jednu ze svých
zákazníci. DPH činí 21 %.

.. obrázek: daňový přenos/belgický příklad.png
:align:center
:alt:Ilustrační obrázek s poznámkou

V tomto případě je podle místních předpisů možné v poli číslo 81 daňového přiznání uvést zápornou částku.
Musí se prohlásit vládě za nulu a záporná částka se převede na
další období.

Pokud se přesuneme na :menuselection:`Účetnictví -> Zprávy -> Daňový výkaz“, zobrazí se okno v řádku 81
Vysvětluje, že částka bude přenesena do dalšího období.

.. obrázek: daňový přenos/pop-up.png
:align:center
:alt: upozornění na přenesení částky do dalšího období

V době uzavření daňového období ukazuje daňový přiznání, že částka byla přenesena z
předchozí období. Ukazuje také částku, která se přenese na tuto řádek v příštím
období založené na existujících transakcích a přenesení částky ze starého období.

.. obrázek: daňový přenos/daňové přiznání.png
:align:center
:alt:Ilustrační foto daňového přiznání
