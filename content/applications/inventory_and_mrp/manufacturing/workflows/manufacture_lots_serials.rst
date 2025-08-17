========================================
Výroba s čísly a sériovými čísly
========================================

.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |MOs| nahradí za: zkratku: `MOs (Manufacturing Orders)`

V Odoo se používají čísla „*loty“ a „*sériová čísla“, aby bylo možné identifikovat a sledovat produkty v Odoo.
čísla se používají k přidělování jedinečných čísel konkrétním výrobkům, zatímco čísla šarží se používají k
přiřadit jedno číslo více kusům konkrétního produktu.

Při výrobě produktů sledovaných pomocí čísla šarže nebo sériového čísla vyžaduje Odoo číslo šarže nebo sériové číslo.
číslo, které je přiřazeno každému výrobku před dokončením výroby. Toto číslo zajišťuje, že každý
produkt je správně sledován od okamžiku, kdy se do zásob dostane.

Nastavte produkty pro sledování
===============================

Odoo automaticky sleduje množství každého produktu na skladě, ale nejednotlivé jednotky.
produktu. Pro sledování šarže nebo sériového čísla musí být povoleno pro každý produkt zvlášť.

Chcete-li sledovat produkt pomocí čísla šarže nebo sériového čísla, začněte tím, že se přesunete na :menuselection:`Sklad
→ Konfigurace → Nastavení“, pak se posuňte dolů do části „Sledovatelnost“ a zaškrtněte
zaškrtněte políčko „Sériové číslo“ a nakonec klikněte na „Uložit“.

Dále klikněte na položku „Produkty“ -> „Produkty“ a vyberte produkt, který chcete sledovat. Ujistěte se, že
Zatrhněte políčko „Inventář“ v záložce „Obecné informace“. Od této chvíle
Pokud je funkce sériového čísla zapnutá, objeví se vedle zaškrtnuté položky v rozevíracím seznamu.

Klikněte na položku „Skladové zásoby“. Výchozí je „Počtu“
vybrané, které sledují pouze množství skladem. Vyberte: guilabel:"Počet" pro sledování produktu
pomocí čísla šarže nebo :guilabel:`Sledování produktu pomocí jedinečného sériového čísla“.

.. viz též:
:doc:`Skladové položky <../../inventory/product_management/product_tracking/lots>`
:doc:`Sériová čísla <../inventar/produktverwaltung/produktnachverfolgung/seriennummern>`

Sériová výroba
========================

Pro výrobu produktu sledovaného po loty začněte tím, že se přesunete na:
Operace --> Výrobní objednávky“. Klikněte na „Nový“ pro vytvoření nové výrobní objednávky.
MO).

V poli „Produkt“ vyberte produkt sledovaný pomocí šarží a zadejte požadovanou
Klikněte na „Potvrdit“.

Jakmile je potvrzeno MO, objeví se pole „Číslo šarže“ v horní části
|MO| pole. Výchozí hodnota je prázdná.

Chcete-li do pole „Číslo šarže“ vložit číslo šarže, klikněte na
:icon:`fa-plus-square-o` :guilabel:`(plus)` ikona vedle pole. To udělá automaticky
generuje hodně čísel, používá nejbližší volné číslo a zadává ho do pole.

Alternativně klikněte na pole „Číslo šarže“ a vyberte již existující číslo šarže.
nebo ručně zadat nové číslo položky a kliknout na „Vytvořit“ v rozevíracím seznamu.

.. obrázek: výroba_sérií/série-číslo-pole.png
:alt: pole „Číslo šarže“ na MO.

Jedna z těchto metod přiřazuje produktům v |MO| číslo šarže před výrobou.
ukončeno. Výrobu lze také dokončit a uzavřít kliknutím na
„Vyrobit vše“, bez přiřazení čísla šarže. To automaticky vygeneruje a
přiřazuje hodně, použije další volné číslo.

Sériové výrobě čísel
===========================

Pro výrobu produktu sledovaného pomocí sériových čísel začněte tím, že se přesunete na
:menuvolba:Výroba -> Provoz - > Objednávky výroby. Klikněte na tlačítko:
vytvořit nový MO.

V poli „Produkt“ vyberte produkt sledovaný pomocí sériových čísel a zadejte
Požadované množství: klikněte na „Potvrdit“ pro potvrzení objednávky.

Jakmile je potvrzeno MO, objeví se pole „Číslo šarže“ v horní části
|MO| pole. Výchozí hodnota je prázdná.

Další výrobní proces se odvíjí podle počtu jednotek v MO.

Výroba jednotlivých kusů
-----------------------

Pokud se vyrábí pouze jednotka produktu, kliknutím na tlačítko „Vyrobit všechny“ se zavře
|MO| a automaticky generuje a přiřazuje další volné sériové číslo, které se objevuje v
:guilabel:„Číslo šarže“

Přiřadit sériové číslo bez uzavření |MO| lze ručně zadáním čísla do
V poli „Číslo šarže“ a klikněte na „Vytvořit číslo“, nebo klikněte
:icon:`fa-plus-square-o` :guilabel:`(plus)` ikona vedle pole pro automatické vyplnění
další volné číslo.

.. obrázek: výroba_sérií/série-číslo-pole.png
:alt: pole „Číslo šarže“ na MO.

Výroba jednotek v sérii
--------------------------

.. důležité:
Při výrobě produktu sledovaného pomocí sériových čísel lze vytvořit MO pro více
jednotky. Při přidělování sériových čísel jednotlivým jednotkám však dochází k tomu, buď na konci výroby nebo
dříve se MO rozdělí na více MO s jednotkou produktu v každém z nich.

Každý rozštěpený |MO| je identifikován číslem, které bylo přidáno na konec původního |MO|
číslo.

...... příklad::
|MO| `WH/MO/00109` obsahuje dvě jednotky „Židle“, produkt sledovaný pomocí sériových čísel.
každému kusu židle je přiřazen unikátní sériový číslo, což způsobuje rozdělení MO na dvě části.
|MOs|, každý obsahuje jednotku židle. |MOs| jsou označeny jako „WH/MO/00109-001“ a
„WHO/MH/00109-002“.

Přiřadit sériové číslo každému jednotlivému kusu |MO| lze stisknutím tlačítka :guilabel:`Produce All`, které otevře
Pop-up okno Batch Production.

V poli „První lot / SN“ se automaticky vyplní další dostupný
sériové číslo. V poli „Počet sériových čísel“ je výchozím nastavení počet jednotek,
výroby. Hodnoty obou polí lze změnit ručně.

Klikněte na tlačítko „Vytvořit“ a vytvořte požadovaný počet sériových čísel, začínajících
číslo, které je zadáno do pole „První lot / SN“. Čísla sérií jsou zobrazena v textu
spodní části okna a po vytvoření lze ručně změnit.

K přiřazení sériových čísel bez dokončení výroby stiskněte tlačítko „Příprava MO“.
Tím se |MO| rozdělí na jednotlivé |MOs|, jeden pro každou jednotku původního |MO|. Každý z nich je
a lze je uzavírat jednotlivě.

K přiřazení sériových čísel a dokončení výroby stiskněte tlačítko „Výroba“.
rozdělí |MO| na jednotlivé |MOs|, jeden pro každou jednotku v původním |MO|. Všechny |MOs| jsou
Zavřeno, výroba je ukončena.

.. obrázek: výroba_sérií/seriová výroba.png
:alt:Okno „Sériové výrobky“, z něhož lze sériová čísla přiřadit.

Po kliknutí na „Připravit MO“ nebo „Výroba“ se zobrazí aplikace „Výroba“.
automaticky zobrazí první ze dvou položek rozdělené na části (např. „WH/MO/00109-001“). Chcete-li zobrazit a přistupovat k
zastavte rozdělení |MOs| a klikněte na chytrý tlačítko „Předobjednávky“ v horní části obrazovky.
