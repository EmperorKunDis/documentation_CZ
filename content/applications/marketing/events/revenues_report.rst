===============
Účetní závěrka
===============

Aplikace **Odoo Events** vytváří na základě dat a analýz souvisejících s událostmi přizpůsobené zprávy.
Tyto zprávy mohou být zaměřeny na *Účastníky* nebo *Příjmy*.

Následující dokumentace se zaměřuje na způsoby hlášení související s událostí *Příjmy*.

Stránka o příjmech
=======================

Pro přístup na stránku s výstupy pro účastníky přejděte do části „Aplikace událostí“ - „Výstupy“
Příjmy.

.. obrázek: výnosy_report/výchozí pohled.png
:align:center
:alt:Výchozí pohled na stránce hlášení příjmů v aplikaci Odoo Events.

Výchozí stránka „Příjmy“ se zobrazuje jako graf (ikona „fa-line-chart“
:guilabel:`(Čára)“ s :icon:`fa-database“ :guilabel:`(Vrstvené)“ daty. Výchozí filtry
:guilabel:„Neplacené vstupenky“ a :guilabel:„Datum konání akce: (rok současný)“, jsou uvedeny na
vyhledávací lišta.

..tip:
Chcete-li se dozvědět více o různých grafových zobrazeních (a možnostech grafového zobrazení), podívejte se na odkaz:
návodů v části „Zpráva/Použití grafu“.

Stránka „Zisky“ lze také zobrazit jako :ref:`pivotovou tabulku
<reporting/views/pivot>`, kliknutím na ikonu „OI-View-Pivot“ (Pivot)
v pravém horním rohu.

Opatření
--------

Volba konkrétních měřítek je rychlým způsobem, jak si přizpůsobit
stránky s výsledky.

Ať už si vyberete jakýkoliv pohled, měřítka na stránce s výkazem příjmů jsou
sleduje: „Příjmy“, „Nepočítané příjmy“ a „Počet“.

.. poznámka::
V základním grafickém zobrazení stránky s výkazem příjmů je vidět pouze
:guilabel:`Příjmy“ je nastaveno v rozbalovacím seznamu „Měřítka“.

V grafickém zobrazení lze vždy vybrat pouze jednu ze měřítek.

Při výběru možnosti „Výchozí“ jsou všechny možnosti „Měření“ vybrány automaticky.

- :guilabel:`Příjmy“: ukazuje příjmy vygenerované z akcí.
- :guilabel:`Nepočítané příjmy“: zobrazuje nepočítané příjmy vzniklé na akcích.
- :guilabel:`Počet účastníků“: zobrazuje celkový počet registrovaných osob, které se na akci zúčastnily.

Filtry a možnosti skupinování
----------------------------

Chcete-li zobrazit rozbalovací nabídku filtrů a možností seskupení pro vytvoření přizpůsobených zpráv, klikněte na
Ikona „svislý šipka“ („down arrow“) vedle vyhledávací lišty.

Tím se otevře rozbalovací nabídka s filtry, které jsou uspořádány do sloupců.
<hledat/přednastavené filtry>“, „Skupiny“ <hledat/skupina>, a „Oblíbené“
<vyhledávání/oblíbené položky>.

.. poznámka::
Pokud je zvolena filtrační možnost v sloupci „Filtry“ (např. výchozí),
:guilabel:`Datum začátku události: (rok)` filtru se objeví sloupec „Srovnání“, ve kterém je
možnosti porovnání pro odpovídající volbu filtru, která je vybrána.

Pouze jednu volbu lze provést z sloupce :guilabel:`Srovnání“ najednou.

.. viz též:
:doc:`../základy/vyhledávání`

Možnosti filtru
~~~~~~~~~~~~~~

V sloupci Filtry v rozbalovacím menu megamenu jsou různé události.
možnosti, které lze využít k vytvoření zprávy na míru podle určitých kritérií.

V sloupci Filtry lze vybrat více možností najednou.

Sloupec Filtry obsahuje následující možnosti:

- :guilabel:`Nepovinné vstupenky“: vstupenky/registrace, které nebyly zdarma.
- :guilabel:`Zdarma“: vstupenky/registrace, které byly dříve zdarma.
- :guilabel:`Čekající platba“: vstupenky na akce nebo registrace, které byly zakoupeny, ale stále nebyly zaplaceny.
platba čeká.
- :guilabel:`Prodáno“: vstupenky na akci, které byly úspěšně prodány (a zaplaceny).
- Klikněte na ikonu „fa-caret-down“ (svislá šipka dolů)
zobrazí se seznam měsíců, čtvrtletí a let. Vyberte libovolný počet z těchto možností k zobrazení
zjistit, kolik registrací bylo během určitého časového období.
- :guilabel:`Připravované/Proběhlé“: zahrnuje informace o příjmech pro události, které jsou buď
aktuálně probíhající nebo které se mají v budoucnu stát.
- :guilabel:`Ukončené události“: zahrnují informace o příjmech související s již proběhlými událostmi
místo.
- Klikněte na ikonu „fa-caret-down“ (směrový špendlík)
zobrazí se seznam měsíců, čtvrtletí a let. Vyberte si libovolný počet těchto možností pro označení
dat, která se týkají příjmů z události, využít jako filtr pro události s určitým datem začátku.
- Klikněte na ikonu „fa-caret-down“ (zobrazení dolů)
zobrazí se seznam měsíců, čtvrtletí a let. Vyberte si libovolný počet těchto možností pro označení
dat o příjmech, které lze filtrovat podle termínu konání akce.
- :guilabel:`Zveřejněné události“: Vyberte tuto možnost, abyste zobrazili příjmovou související data pro zveřejněné
události.
- :guilabel:`Přidat vlastní filtr“: Vytvořte vlastní filtr pro analýzu příjmů spojených s událostí.
se dozvědět více, podívejte se na dokumentaci k tématu :ref:`vlastních filtrů <hledání/vlastní-filtry>“.

Možnosti skupinování
~~~~~~~~~~~~~~~~

V poli „Skupina“ v rozbalovacím menu megamenu jsou různé události.
možnost vytvářet vlastní skupiny dat.

Můžete vybrat více možností „Skupina podle“.

Sloupec „Skupina“ má následující možnosti:

- :guilabel:`Typ události“: Skupina dat podle typu události.
- :guilabel:`Události“: Organizujte data do jednotlivých skupin oddělených událostmi.
- :guilabel:`Produkt“: Skupina dat podle produktu registrace na události.
- :guilabel:`Vstupenky“: Skupina dat založená na typu vstupenek zakoupených účastníky.
- :guilabel:`Stav registrace“: Skupujte data podle stavu registrací.
- :guilabel:`Stav objednávek na prodej“: Skupujte data podle stavu objednávek souvisejících s událostmi.
- :guilabel:`Zákazník“: Skupina dat podle zákaznických záznamů.
- :guilabel:`Přidat vlastní skupinu“: Klikněte na ikonu :guilabel:`(svislá čára)`
zobrazí se vyskakovací okno s možnostmi skupin. Klikněte na požadovanou možnost a Odoo přidá
Přidejte ji do sloupce „Skupina“. Můžete vybrat více položek.

Vzorek zprávy: analýza vstupenek na akci (grafečky)
============================================

Následující je příkladem, jak různé filtry a možnosti seskupování vytvářejí užitečné analýzy.
Graf s výsledky zisku z akce. V tomto případě se jedná o konfigurace, které ukazují prodej nebo
Zdarma vstupenky na veřejně publikované akce, s měřítkem odděleným podle typu vstupenky a události.

.. obrázek: příjmy_zpráva/analýza vstupenek.png
:align:center
:alt: Vzorek výstupu analýzy vstupenek s jedinečnými filtry a skupinami.

Pro vytvoření takového hlášení přejděte na: „Aplikace událostí –> Zprávy –> Tržby“.
výchozí grafický pohled, ale odstraňte výchozí filtry z vyhledávací lišty.

Pak klikněte na ikonu „fa-caret-down“ vedle vyhledávací lišty, abyste
zobrazit rozbalovací nabídku filtrů a možností seskupení.

Zde vyberte filtry „Volné“ a „Prodáno“.

Pak je třeba vybrat pouze data související s již zveřejněnými událostmi.
Možnost „Zveřejněné události“ v sloupci „Filtry“.

Dále v sloupci „Skupina“ vyberte „Akce“ a „Vstupenka“.
možností, a to v tomto pořadí. Takto se totiž shromažďují data podle události, pak podle lístku
typu, který poskytuje užitečnější sadu dat pro analýzu.

.. důležité:
Řazení možností v sloupci „Skupina“ má přímo vliv na výběr.
jaká je prezentace dat na zprávě.

Zde můžete přidat další konfigurace pro podrobnější data, pokud si je přejete.

Pokud nejsou přidány žádné další filtry nebo skupiny, Odoo zobrazí grafickou reprezentaci dat.
se vztahem ke všem volným nebo prodaným vstupenkám na zveřejněné akce, seskupené podle akce a uspořádané
*vstupenka* typu.

Vzorový výstup: analýza typu události (tabulka s otáčivými sloupci)
================================================

Následující je příkladem, jak různé filtry a možnosti seskupování vytvářejí užitečné analýzy.
Pivotový report související s příjmy z akce. V tomto případě se jedná o konfigurace, které obsahují údaje o
jaké příjmy jednotlivé typy akcí vynesly, aby bylo možné zjistit, které akce jsou nejvýdělečnější.
zisková.

.. obrázek:: příjmy_report/analýza_typů_akcí.png
:align:center
:alt:Zpráva o analýze událostí s jedinečnými filtry a skupinami vytvořenými pro tento příklad.

Nejprve přejděte na :menuselection:`Akce aplikace --> Zprávy --> Příjmy“ a přepněte se do sloupcového výpisu.
vizuál tabulky, kliknutím na ikonu „OI-VIEW-PIVOT“ (Pivot) v pravém horním rohu
roh.

Zachovejte výchozí filtry („Neplacené požadavky“ a „Datum začátku události (rok):“)
vyhledávací lištu.

Dále otevřete nabídku „Měření“ a vyberte možnost „Počet“.
Protože tento výkaz se bude zabývat pouze příjmy.

Poté klikněte na ikonu „+“ nad názvy sloupců a vyberte
:guilabel:'Typ události' z rozevírací nabídky.

S těmito konfiguracemi jsou všechny příjmy z akcí (a jejich
přidružené registrace) jsou zobrazeny a uspořádány podle typu události (zobrazeno jako rozbalitelný seznam).
sloupy.
