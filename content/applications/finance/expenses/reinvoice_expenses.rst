===================
Znovuúčtování výdajů
===================

Pokud jsou náklady sledovány na projektech zákazníků, mohou být automaticky vráceny.
zákazníkovi. Toho se dosáhne vytvořením výdaje:
pokud se objednávka zadá do prodeje, je k ní přičtena a poté vytvořena faktura.
<náklady/faktura_zpětně/>.

Další krok je potom schválení výdajového hlášení (<expenses/reinvoice-approve>) a následně účetní.
oddělení:ref: „zveřejňuje záznamy o příjmech a výdajích <náklady/přeúčtování schválené>“.

Konečně, když je faktura za náklady zveřejněna v časopise, náklady se objeví na uvedeném místě.
:zkratka SO (prodejní objednávka). Poté je :ref:`fakturována <expenses/reinvoice>
Takže zákazník platí za náklady.

.. důležité::
Schválení výdajů, přičtení výdajů k účetnictví a vystavení faktury za :abbr:`SOs (Sales
Pouze pro uživatele s odpovídajícím přístupem (viz :doc:`práva přístupu`).
<../../povoleni/uživatele/práva>.

.. viz též:
Tento dokument poskytuje návod k vytvoření, podání, schválení a zveřejnění.
zveřejňování výdajů. Pro podrobné pokyny k jakémukoliv z těchto kroků se obraťte na
následující dokumentaci:

   - :doc:`Záznamy o výdajích <../expenses/log_expenses>`
   - :doc:`Zprávy o výdajích <../expenses/expense_reports>`
   - :doc:`Schválení výdajů <../expenses/approve_expenses>`
   - :doc:`Zadání výdajů v účetnictví <../expenses/post_expenses>`

Nastavení
=====

Nejdříve specifikujte účetní politiku pro každou kategorii výdajů. Přejděte na: menu: `Výdaje
app --> Nastavení --> Kategorie výdajů“. Klikněte na kategorii výdajů, abyste viděli výdaje.
Kategorie. V sekci „Fakturace“ klikněte na tlačítko vedle požadované položky.
výběr pro:guilabel:Znovuúčtování výdajů

- :guilabel:`Ne“: Nákladová položka nelze znovu fakturovat.
- :guilabel:Na náklady“: Faktury na účetnictví zaúčtují výdaje v ceně, která je nastavena pro daný výdaj
formulář kategorie.
- :guilabel:`Prodejní cena“: Nákladová položka vystavuje fakturu za prodejní cenu, kterou je na nákladové položce nastavená.

..._výdaje/faktura-přijatá:

Vytvořit výdaj
=================

Nejprve při vytváření nové položky výdajů (viz. stránka „Výdaje“), je třeba zadat správné informace.
aby byla vystavena faktura na úhradu nákladů pro zákazníka. Vyberte z roletky
:zkratka SO (objednávky)“ k přidání výdajů do pole „Zpětné fakturaci zákazníkovi“.

Dále vyberte analytickou položku, na kterou je výdaj zaúčtován. Může jich být více.
pokud si budete přát.

Chcete-li přidat další „Distribuci analýzy“, klikněte na řádek, který se zobrazí.
Popisovací okno „Analytika“. Klikněte na „Přidat řádek“, vyberte požadovaný
Vyberte možnost „Analytická distribuce“ z rozevírací nabídky. Pokud vyberete více než jednu
:guilabel:`Analytická distribuce“, pole „Procento“ **musí být upravena“.
Výchozí hodnotou je 100%, upravte procenta všech políček tak, aby
všechny vybrané účty dávají celkem 100 %.

.. příklad::
Společnost zabývající se malířskými pracemi souhlasila s malováním kancelářského objektu, který obsahuje dvě různé společnosti.
předběžnou kalkulaci se koná schůzka na pracovišti, kde je projekt projednáván.

Oba podniky se dohodly na tom, že uhradí cestovné zaměstnanců malířské firmy.
vytváření výdajů za cestovné a ubytování, obě společnosti jsou uvedeny v
:guilabel:`Analytická distribuce“ pro 50 %.

..._náklady/fakturační report:

Vytvořte výkaz o nákladech
========================

Po vytvoření výdajů je nutné zadat výkaz výdajů:
a:ref:`podáno <náklady/podat>“, stejně jako všechny ostatní výdaje.

Jakmile je podána faktura za náklady, tlačítko „Prodejní objednávky“ se zobrazí jako ikona peněz.
je viditelný v horní části obou výkazů o nákladech a každé jednotlivé položce.
vrácené zpět.

.. obrázek: reinvoice_expenses/reinvoice-expense.png
:align:center
:alt:Zajistěte, aby byl zákazník na faktuře označen.

.. důležité::
Vyberte správný poznámkový záznam „SO (Prodejní objednávka)“ v poli „Zákazník k přeúčtování“.
**kritické**, protože po odeslání výkazu nákladů se automaticky vystavuje faktura.
je schválený.

Záložka „Klient na fakturaci“ lze měnit pouze do okamžiku, kdy je vystavena výkazu o nákladech.
**schválený**. Po schválení výdajového hlášení je pole :guilabel:`Zákazník pro opětovné vyúčtování“
již nelze měnit.

.._náklady/přijetí faktury schválit:

Schválit a zveřejnit výdaje
=========================

Před schválením výdajového hlášení (doc:approve_expenses) se ujistěte, že
V sekci „Analytická distribuce“ je vyplněno pro každou položku výdajů.

Pokud je v poli „Analytické rozložení“ chybí hodnota, přiřaďte správné účty z
nabídce rozbalovacího menu a klikněte na tlačítko „Schválit“.

.. obrázek: reinvoice_expenses/analytic-dist.png
:align:center
:alt:Výkaz nákladů s vyplněnými všemi řádky rozdělení analytické distribuce.

.. poznámka::
Tlačítko „Schválit“ se objeví pouze po podání výdajového hlášení.
<výdaje/odeslat>.

Účtárna obvykle zajišťuje účtování zápisů do knihy jízd.
<../expenses/post_expenses>`. Pro přidání výdajů do účetního deníku klikněte na:guilabel:`Přidat
Deníková záznamu. Jakmile je nákladový výkaz schválen, může být zveřejněn.

:abbr:`SO (Objednávka prodeje)` je aktualizována pouze po zadání účetních záznamů.
zápisy do deníku jsou zveřejněny a náklady se objevují na odkazovaném :abbr:`SO (objednávka prodeje)“.

.. výdaje / faktura vystavená zpětně:

Fakturační výdaje
================

Po schválení výdajového hlášení a zadání účetních případů se vytvoří :abbr:`SO
(Objednávka prodeje) je aktualizována a zákazník může být fakturován.

Vyberte výkaz o nákladech a klikněte na tlačítko „Smart Button“ s ikonou peněz vedle položky „Přijaté objednávky“.
otevřít fakturu „SO (Sales Order)“. Náklady, které se mají znovu vyúčtovat, se nyní zobrazují na faktuře „SO (Sales
Pokyny`).

.. poznámka::
Výdajovém příkazu může být odkazováno na více než jeden :abbr:`SO (Sales Order)“.
:zkratka SO (objednávky) je odkazována, kliknutím na tlačítko „Objednávky“ se otevře
a seznam všech položek s názvem „Prodejní objednávka“ spojených s tímto výkazem o nákladech. Klikněte na
a:abbr:`SO (Prodejní objednávka)` pro otevření detailů jednotlivých :abbr:`SO (Prodejních objednávek)“.

Náklady jsou uvedeny v záložce „Dodací lístky“ v kartě „Obchodní objednávka“.

.. obrázek: reinvoice_expenses/so-details.png
:align:center
:alt:Výdaje uvedené v objednávce se zobrazí po kliknutí na ni.

Dále klikněte na „Vytvořit fakturu“ a zobrazí se okno s názvem „Vytvořit faktury“.
Vyberte, zda je faktura :guilabel:`Standardní faktura“, :guilabel:`Předplatba (procento)“ nebo
a:guilabel:Záloha (pevná částka). Pak klikněte na:guilabel:Vytvořit návrh faktury.
Vytvoří návrh faktury pro zákazníka. Klikněte na tlačítko „Potvrdit“ k potvrzení faktury a
Zákazník je fakturován za náklady.
