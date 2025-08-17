===================
Analytická účetnictví
===================

Analytická účetnictví pomáhá sledovat náklady a příjmy a analyzovat projekt nebo službu.
profitabilitě. Při vytváření účetních záznamů lze náklady rozdělit na :ref:`účtování
Přes jednu nebo více analytických účtů.

Chcete-li tuto funkci aktivovat, přejděte na: „Účetnictví – Konfigurace – Nastavení“
Povolit v sekci „Analýzy“ položku „Analytická účetnictví“.

.. viz též:
:doc:`Analytický rozpočet <rozpočet>`

...účetnictví/analytické účetnictví/analytické účty:

Analytické účty
=================

Analytické účty poskytují přehled o nákladech a příjmech.

Pro přístup k analytickým účtům přejděte na: „Účetnictví“ - „Konfigurace“ - „Analytické
Účty“. K vytvoření nového analytického účtu klikněte na „Nový“ a vyplňte následující
informace:

- :guilabel:`Analytický účet“: Přidělte jméno analytického účtu.
- :guilabel:`Zákazník“: Vyberte zákazníka spojeného s projektem, pokud je k dispozici.
- :guilabel:`Odkaz na referenci`: Zahrňte odkaz, aby účet byl snadno dohledatelný v případě potřeby.
- :guilabel:`Plán“: Propojit :guilabel:`účet pro analýzu“ s :ref:`plánem
<účetnictví/analytické účetnictví/analytické plány>.
- :guilabel:`Společnost“: V :doc:`multicompany </aplikace/obecné/společnosti/multicompany>`
prostředí, vyberte společnost pomocí analytického účtu. Chcete-li vytvořit analytický účet
Ponechte pole prázdné, pokud je služba dostupná všem firmám.
- :guilabel:`Měna“: Aktualizujte měnu analytického účtu, pokud je třeba.

Poté se vyplní informace o rozpočtu (viz též :doc:`budget <budget>`).

...účetní/analytické plány:

Analytické plány
==============

Analytické plány skupiny: ref: analytické účty <účetnictví/analytická_účetní/analytické_účty>
umožňuje společnosti analyzovat účetnictví, například sledování nákladů a příjmů podle projektu.
oddělení.

Pro přístup k analytickým plánům přejděte na: „Účetnictví -> Konfigurace -> Analytické plány“.
Klikněte na tlačítko „Nový“ pro vytvoření nového plánu, přidejte název a vyplňte následující informace:

- :guilabel:`Rodiče“: Propojte plán s dalším analytickým plánem, pokud je mezi nimi hierarchie
Postaveno.
- :guilabel:`Výchozí aplikovatelnost“: Definujte, jak se plán používá při vytváření nového deníku
vstup:

  - :guilabel:`Volitelné“: Přidání analytického plánu není povinné.
  - :guilabel:`Povinné“: Vstup nelze potvrdit, pokud není vybrán analytický účet.
  - :guilabel:`Není k dispozici“: Plán není dostupný.

- :guilabel:`Barva“: Nastavte barvu pro štítek, který se vztahuje k tomuto konkrétnímu plánu.

Pro vyladění aplikovatelnosti plánu vytvořte novou řádku v záložce „Aplikovatelnost“ a nastavte
tyto pole:

- :guilabel:`Doména“: Vyberte účetní doklady, na které se plán vztahuje.
- :guilabel:`Předpony účtů finančnímu plánu“: Zadejte předponu (předpony) účtu, ke kterému se vztahuje
V případě, že se tato situace stane, platí výše uvedené podmínky.
- :guilabel:`Kategorie produktu“: Vyberte kategorii produktů, ke kterým se plán vztahuje.
- :guilabel:`Použitelnost“:Definujte, jak se plán používá při vytváření nové položky v deníku.
Výchozí aplikační prostor je vždy přehlušen aplikačním prostorem definovaným zde.
- :guilabel:`Společnost“: V :doc:`multicompany </aplikace/obecné/společnosti/multicompany>`
prostředí, vyberte společnost pomocí plánu. Chcete-li zpřístupnit analytický plán všem
Společnosti, nechte pole prázdné.

Dva chytré tlačítka jsou k dispozici:

- :guilabel:Podplány: Mít složitější analytickou strukturu. Klikněte na chytrý tlačítko, pak
Klikněte na tlačítko „New“ pro přidání podplánu. To vytvoří rodičovsko-dětský vztah mezi oběma
plány a pole :guilabel:`Parent` podplánu je automaticky vyplněno hodnotou
původní plán.
- :guilabel:`Analytické účty“: Chcete-li zobrazit analytické účty
<účetnictví/analytické účetnictví/analytické účty> spojené s plánem.

.. poznámka::
Každý analytický plán musí obsahovat alespoň jeden analytický účet.

.. účetnictví / analytické účetnictví / distribuce:

Analytická distribuce
=====================

Distribuci nákladů v jednom nebo více analytických účtech lze nastavit u každé faktury.
<účetnictví/analytické účetnictví/vystavení faktur a zálohových faktur> nebo :ref:`ve velkém
<účetnictví/analytické účetnictví/rozdělování hromadně>.

.. poznámka::
Analytická distribuce je předvyplněna podle aplikovatelnosti a :ref:`analytické
účetní a analytické distribuční modely.

.. účetnictví/analytické účetnictví/distribuce faktur a zálohových faktur:

Analytická distribuce na fakturách nebo složenek
------------------------------------------

K analýze distribuce klikněte na sloupec „Analytická distribuce“ při vytváření
:ref:`faktura <účetnictví/faktury/vytvoření>` nebo :ref:`daňový doklad <účetnictví/dodavatelské faktury/vytvoření>“.

.. poznámka::
Položka „Analytická distribuce“ je povinná pouze v případě, že se jedná o analytický plán.
<účetnictví/analytické účetnictví/analytické plány> je nastaveno jako „Povinné“ v buňce
pole „Výchozí aplikovatelnost“ v plánu analýzy nebo pole „Aplikovatelnost“
pole na analytické čáře plánu.

V okně Analytik vyberte požadované analytické účty.
Různé: Zobrazení plánů analýz v sloupcích. Poté rozdělte náklady mezi
účty změnou procenta.

.. obrázek: analytic_accounting/analytic-distribution.png
:alt: vytvořit šablonu distribuce

...účetnictví/analytické účetnictví/distribuce masivní:

Analytická distribuce po hromadě
------------------------------

Pro hromadné úpravy analytických účtů v několika položkách najednou přejděte na: menu:Účetnictví
Účetnictví --- Záznamy do knihy --- a vyberte záznamy, které je třeba aktualizovat. Klikněte na
Sloupec „Analytická distribuce“ a přidejte požadovanou distribuci do
Kolonku „Analytika“, pak klikněte na ikonu „X“ (křížek)
:guilabel:`Potvrdit“. Analytická distribuce je pak přidána k vybraným položkám časopisu.

...účetní/analytické distribuční modely:

Analytické modely distribuce
----------------------------

Analytické distribuční modely automaticky aplikují konkrétní distribuci na základě definovaných kritérií.

Pro vytvoření nového modelu distribuce analýz přejděte na: „Účetnictví -> Konfigurace ->
Analytické distribuční modely“, klikněte na „Nový“ a nastavte podmínky, které musí model splňovat
aplikovat automaticky:

.. poznámka::
   - Pro splnění všech uvedených podmínek musí být model analytického rozdělení
aplikovat analytický model distribuce na základě individuálních podmínek, vytvořit
separátní analytické distribuční modely pro každou podmínku.
   - Analytické distribuční modely lze kombinovat a seřazovat tak, aby byly distribuovány
více modelů, pokud jsou propojeny s různými
:ref:`analytické plány <účetnictví/analytická účetní evidence/analytické plány>“.
přetáhněte a pusťte modely pomocí ikonky :icon:`oi-draggable` :guilabel:`(Draggable)` .

- :guilabel:`Předpony účtů“: Aplikujte distribuční model pouze na položky v deníku, které
účty, které začínají konkrétními předponami.
- :guilabel:`Partner`: Aplikujte distribuční model pouze na položky časopisu, které se týkají konkrétního
partner.
- :guilabel:`Produkt“: Aplikujte distribuční model pouze na položky periodik, které se týkají konkrétního
produktu.
- :guilabel:`Společnost“: V :doc:`multicompany </aplikace/obecné/společnosti/multicompany>`
předmětem zájmu konkrétní společnosti.
Aplikovat ji na všechny společnosti a pole nechat prázdné.
- „Analytická distribuce“: „Analytická distribuce
<účetnictví/analytické účetnictví/analytická distribuce> a bude aplikována při výše uvedených
Pokud jsou splněny podmínky.

.. příklad::
Každý příspěvek do účtu „Údržba“ (601000) by měl být označen jako
a automaticky rozděleno v analytickém plánu podle oddělení následovně:

   - 60 % do účtu „Výroba“
   - 30 % na účet pro marketingovou analýzu
   - 10 % na účet pro analýzu „Admin“

aby se tato distribuce automatizovala, lze nastavit :guilabel:`Předčíslí účtu“ na „601“.
:guilabel:`Služby (601000)` je jediný účet v rozvaze, který začíná
   `601`.

Pokud jsou v účtu další položky, jako například „Elektřina (601100)“ nebo „Plyn (601200)“,
v účetní osnově, bude se tato distribuce vztahovat i na oba, protože sdílejí
stejným předponám.

Pro definování dalších kritérií použijte ikonu „Nastavení“ (adjust settings)
zobrazit další sloupce nebo kliknout na tlačítko „Zobrazit“ u individuálního distribučního modelu analýzy.

- :guilabel:`Distribuční kategorie partnera“: Tento distribuční model použijte jen u položek v časopisech, které
partnerem v konkrétní kategorii.
- :guilabel:`Kategorie produktu“: Aplikujte tento distribuční model na položky novin, které se týkají produktů
v konkrétní kategorii.

.. tip::
Alternativně lze vytvořit analytickou distribuční model z
:guilabel:`Analytická“ okna kliknutím na :guilabel:`Nová modelová“

   - ať už při vystavování faktury a vyplňování analytického rozdělení
"<účetnictví/analytické účetnictví/výdejové faktury a daňové doklady>“
   - nebo když:ref:`masivně upravujete analytické účty
v několika položkách zároveň.

