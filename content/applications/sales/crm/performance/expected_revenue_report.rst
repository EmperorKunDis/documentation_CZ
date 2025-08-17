=======================
Očekávaný výnosový report
=======================

*Očekávaný příjem* je celkové hotovostní hodnota očekávaných zakázek, které mají být uzavřeny do určitého data.
obvykle koncem aktuálního měsíce.

Očekávaný výnosový report sestaví všechny aktivní vstupy do prodejního kanálu, které mají stanovenou očekávanou hodnotu.
datum ukončení a srovnává výkonnost prodejních týmů v daném časovém rámci.

.. obrázek: očekávaný příjem report/očekávaný příjem zavírací.png
:align:center
:alt: Detail očekávaného data ukončení v aplikaci CRM.

Pulling a monthly expected revenue report allows sales managers to see which team members are reaching
jejich cíle a kdo může potřebovat další pomoc při uzavírání důležitých obchodů.

Vytvořte očekávaný výnosový report
=================================

Pro vytvoření očekávaného příjmu je třeba nejprve přejít na: „CRM aplikace --> Zprávy -->
Trubka“. To otevře panel „Analýza trubky“.

.. důležité:
Dashboard Pipeline Analysis obsahuje několik filtrů v poli hledání výchozí. Odstraňte
Tyto filtry použijte před přidáním dalších vlastních filtrů.

V horním levém rohu zprávy klikněte na položku „Metriky“ a poté vyberte „Očekávaný příjem“.
z rozbalovací nabídky.

Na horní části stránky klikněte na ikonu ⬇ (trojúhelník směřující dolů) vedle
:guilabel:`Hledat…“ a otevřít seznam, který obsahuje :guilabel:`Filtry“.
„Skupina“, „Oblíbené“ a pod „Filtry“ klikněte
„Přidat vlastní filtr“, což otevře okno „Přidat vlastní filtr“.

.. očekávané příjmy podle reportu:

Přidejte vlastní filtry
------------------

Pro vytvoření očekávaného výnosového hlášení je nutné vytvořit filtry pro následující
podmínky:

 - :ref:`Očekávaný datum ukončení <expected_revenue_report/closing-date>“:
zahrnují obchodní příležitosti, které by měly být uzavřeny v určitém časovém rámci.
 - :ref:`Vynechat nezařazené kontakty <expected_revenue_report/unassigned-leads>“: vynechává kontakty
bez přiřazeného obchodníka.
 - :ref:`Konkrétní prodejní týmy <expected_revenue_report/sales-team>“: omezuje výsledky na pouze
Vedoucí prodejců, kteří jsou přiřazeni ke konkrétnímu týmu prodeje. Tento filtr je nepovinný a neměl by být zahrnut, pokud
zpráva je určena pro celou společnost.

... očekávané příjmy podle data ukončení:

Přidejte filtr očekávaného termínu uzavření
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V okně „Přidat vlastní filtr“ klikněte do prvního pole nového pravidla.
Do pole „Hledat…“ zadejte Expected Closing nebo posuňte se dolů a vyberte ho ze seznamu.
Klikněte do druhého pole a vyberte možnost „je nastaven“. To omezuje výsledky na pouze ty, které obsahují
výsledky, kde je uvedená odhadovaná doba uzavření.

Dále klikněte na ikonu „+“ vedle pravidla a duplikujte jej.

..tip:
Použitím ikony „+“ lze snadno vytvořit více pravidel založených na stejném základě.
filtr

V druhém poli nové pravidlo vyberte možnost „je mezi“ z nabídky.
vytváří časový rámec, ve kterém musí dojít k očekávanému datu uzavření pro zahrnutí vedení
výsledcích.

Klepněte na každé datumové pole jednotlivě a použijte okno kalendáře pro přidání jak začátku, tak konce.
konec platnosti pravidla. Toto je obvykle začátek a konec aktuálního měsíce nebo fiskální
čtvrtina.

.. očekávaný příjem reportu nezařazených kontaktů:

Vyřaďte nezařazené kontakty
~~~~~~~~~~~~~~~~~~~~~~~~

Po filtrování očekávaného termínu uzavření smlouvy přidejte nové pravidlo. Potom klikněte do nového
první pole pravidla a zadejte Salesperson do pole „Hledat…“, nebo přejeďte
seznam, ve kterém vyberete:guilabel:je nastaveno“.
menu, což vylučuje všechny výsledky bez přiřazeného prodejce.

.. očekávaný příjem reportu / prodejní tým:

Přidejte filtr pro obchodní týmy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. poznámka::
Tento filtr je nepovinný. Chcete-li zobrazit výsledky pro celou společnost, nezadávejte tento filtr.
pokračovat na:ref:`Zobrazit výsledky <expected_revenue_report/view-results>“.

Chcete-li omezit výsledky zprávy na jednu nebo více prodejních týmů, klikněte na „Nová pravidla“. Poté
klikněte na první pole pro nové pravidlo a zadejte Sales Team do pole „Hledat…“ nebo
Přejděte dolů a vyhledejte v seznamu.

V druhém poli pravidla vyberte možnost „je v“ z nabídky.
Operátor omezuje výsledky na prodejní týmy uvedené v další kolonce.

V neposlední řadě klikněte do třetího pole a buď: vyberte si z celého seznamu, který je v
přepínač nabídky nebo zadejte první pár písmen názvu týmu prodeje, abyste rychle
Vyhledejte ji jako parametr.

..tip:
Do pravidla „Prodejní tým“ lze přidat více týmů, kde každý parametr je zpracován jako
„nebo“ (např. „kdokoliv“) operátor v logice vyhledávání.

.. obrázek: očekávaný výnos report/vlastní filtry.png
:align:center
:alt:Přidejte okno s přizpůsobenými filtry, které jsou konfigurovány pro očekávaný příjem.
zpráva.

.. očekávané příjmy:

Zobrazit výsledky
============

Na horní části formuláře „Přidat vlastní filtr“ je možnost vybrat „jakýkoliv“.
:guilabel:`všechny“ pravidla. Pro správné spuštění zprávy jsou nutná pouze záznamy, které odpovídají **všem**
Filtrů by mělo být zahrnuto následujících. Před přidáním filtrů se ujistěte, že je vybráno všechny
v tomto oboru vybrána.

.. obrázek: očekávaný výnos zprávy/přesně shoduje se s filtrem.png
:align:center
:alt:Vyberte možnost všech filtrů v okně Přidat vlastní filtr.

Na konci formuláře „Přidat vlastní filtr“ klikněte na „Přidat“.

Zobrazit možnosti
------------

Očekávaný výnosový report využívá více pohledů. Výchozí grafický pohled lze
používá se k identifikaci prodejců, kteří mají přinést nejvíce příjmů, zatímco v pohledu na seznam
Pivotový pohled poskytuje více podrobností o konkrétních obchodech.

.. záložky::

....... tab:: Grafické zobrazení

Zobrazení grafu se používá k vizualizaci dat a je užitečné při identifikaci vzorů a
trendy.

*Sloupcový graf* se používá k zobrazení distribuce dat v několika kategoriích nebo mezi
několik prodejců.

*Grafy čarového typu* jsou užitečné pro zobrazení sezónních změn v průběhu času.

Píšťalky jsou užitečné pro zobrazení distribuce nebo srovnání dat mezi malým počtem
kategorií nebo prodejců, konkrétně jak tvoří významnou část celku
obrázek.

Výchozí pohled pro očekávané příjmy je sloupcový graf sestupně. Chcete-li změnit na
různé grafické zobrazení, klikněte na jednu ze symbolů v horním levém rohu zprávy. Obě
Svislý graf a sloupcový graf jsou k dispozici v přehledovém zobrazení, ale u koláčového grafu ne.

.. obrázek:: očekávaný_příjem_výkazu/grafy-ikonky.png
:align: střed
:alt: Detailní pohled na grafické ikony v přehledu analýzy trubky v aplikaci CRM.

Ikony grafu v pořadí: sloupcový graf, čárový graf, koláčový graf, skládaný.

...... tab:: Zobrazení seznamu

V seznamovém pohledu je zobrazena všechna očekávaná uzavření, která jsou určena k datu.
datum. Kliknutím na záznam v seznamovém zobrazení otevřete záznam pro podrobné analýzy, ale mnoho
Informace lze získat i ze základního pohledu.

Pro přepnutí na seznamový pohled klikněte na ikonu „≣ (seznam)“ v pravém horním rohu.
zprávě.

.. obrázek: očekávaný výnos reportu/seznam ikon.png
:align: střed
:alt: Detailní pohled na ikonu pro zobrazení seznamu v aplikaci CRM.

Pro přidání dalších metrik do zprávy klikněte na tlačítko „Další možnosti“ uvedené v
:guilabel:`přepínač` v pravém horním rohu seznamu.

.. obrázek:: očekávaný příjem/přepínač.png
:align: střed
:alt: Detailní pohled na tlačítko v aplikaci CRM.

Kliknutím na ikonu přepínače v seznamovém zobrazení se otevře nabídka dalších možností.

Vyberte si další metriky z rozbalovací nabídky a přidejte je do seznamu. Některé
užitečné mohou být například volby :guilabel:`Očekávaný závěr“ a :guilabel:`Pravděpodobnost“.

....... Zobrazení na základě hodnot

Viditelnost vázání je uspořádána tak, aby všechny očekávané uzavřené obchody byly zobrazeny na
dynamická tabulka.

Pro přepnutí na sestavu ve formátu Pivot klikněte na ikonku „Pivot“ v pravém horním rohu zprávy.

.. obrázek: očekávaný výnosový report/pivtový pohled/ikonka.png
:align: střed
:alt: Detailní pohled na ikonu pro přepnutí do režimu zobrazení vztahů ve CRM aplikaci.

Při výběru této zobrazení osy X ukazuje na stupně.
potrubí, zatímco osa Y automaticky seskupuje výsledky podle data jejich vytvoření. Chcete-li přepnout
klikněte na ikonu přepínání ([:guilabel:`⇄`]) v horní části zprávy.

Pokud chcete přidat další měření do zprávy, klikněte na tlačítko „Měření“ v horní části okna.
v horním levém rohu zprávy. Vyberte si další metriky ze seznamu.

Chcete-li přidat skupinu do sloupce nebo řádku v rozhraní Pivot, klikněte na :guilabel:`➕ (plus sign)`.
„Celkem“, a poté vyberte jednu ze skupin. Chcete-li ji odstranit, klikněte na
:guilabel:`➖ (mínusová značka)` a vyberte příslušnou možnost.

Klikněte na tlačítko „Vložit do tabulky“ a přidejte zobrazení řádků do editační tabulky.
formátu v aplikaci Dashboards. Pokud je nainstalována aplikace Dokumenty, můžete zprávu
Mohou být vloženy do prázdné nebo již existující tabulky a exportovány.
