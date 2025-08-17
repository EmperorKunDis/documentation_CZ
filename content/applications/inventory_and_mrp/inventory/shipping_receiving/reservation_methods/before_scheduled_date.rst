=================================
Před termínem rezervace
=================================

... metody inventarizace a rezervace před plánovaným datem:

.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`

Metoda rezervace s předstihem umožňuje uživatelům vybrat konkrétní počet dnů.
před termínem dodání, kdy jsou zahrnuty produkty v
Prodejní objednávka (PO) by měla být rezervována.

.. viz také:
:doc:`O rezervačních metodách <../reservation_methods>`

Konfigurace
=============

Chcete-li nastavit rezervační metodu na „Před plánovaným datem“, přejděte do sekce :menuselection:`Skladové aplikace
Vyberte možnost „Konfigurace“ a poté vyberte požadovaný typ operace.
konfigurovat nebo vytvořit nový kliknutím na „New“.

V záložce „Obecné“ najděte pole „Způsob rezervace“ a vyberte
:guilabel:`Před plánovaným datem“.

.. obrázek: před_plánovaným_datem/před-plánovaným-datem-konfigurace.png
:align:center
:alt: pole rezervace na formuláři pro objednávku dodání.

.. poznámka::
Když je změněn typ operace na „Pokladní doklad“,
:guilabel:`Typ operace“ formuláři, rezervace není k dispozici.

Jakmile je vybrána rezervace, objeví se pod ní nové pole s názvem „Rezervace před plánovaným datem“.
Počet dní před a počet dní před, kdy je hvězdička můžete změnit.
Výchozí hodnota je „0“.

Změna hodnoty :guilabel:`dny předem` změní maximální počet dní před plánovaným
datum, kdy by měly být rezervovány výrobky.

Změna hodnoty :guilabel:`dny předtím, kdy byl označen jako hvězda` změní maximální počet dní před tím, než se někdo stal hvězdou
datum, kdy by měly být rezervovány produkty, pokud jsou převedeny (oblíbené).

Příklad:
Zde je nastavená hodnota :guilabel:`days before` na 2 dny předem a hodnota :guilabel:`days
když je hodnota starred nastavena na 3.

To znamená, že produkty jsou rezervovány dva dny před plánovaným datem dodání pro běžné objednávky.
a tři dny před datem plánovaného doručení pro hvězdné převody.

.... obrázek:: před_plánovaným_datem/před-plánovaným-datem-dní-před.png
:srovnání: do středu
:alt: Rezervace před termínem s pevnou hodnotou.

Toto je konfigurace, která byla použita pro následující průběh procesu uvedený níže.

Upravit produkt
-----------------

Před použitím rezervačního postupu s předem stanoveným datem se ujistěte, že máte vytvořený *klientský kontakt.
Čas* se přidává k produktům, které plánují prodávat touto metodou.

Pro toto vyberte v nabídce „Nastavení aplikace“ -> „Zboží“ -> „Zboží“.
Požadovaný produkt pro konfiguraci.

V sekci „Produkt“ klikněte na záložku „Sklad“, a pod záložkou „Dodavatelé“
sekci a změňte hodnotu v poli „Doba dodání zákazníkům“.

Pro tento příklad pracovního postupu změňte na 5 dní.

Tímto se stanoví datum dodání tohoto konkrétního produktu na pět dní po vytvoření
o prodejní objednávce.

.. obrázek: před plánovaným datem / před plánovaným datem - doba zpracování požadavku zákazníka.png
:align:center
:alt: Forma produktu s nastaveným termínem dodání pro zákazníka v záložce Sklad.

Průběh práce
========

Chcete-li vidět metodu rezervace předem stanoveného data v akci, vytvořte novou |SO| kliknutím na
:menu:Prodejní aplikace --> Nová.

Do pole „Zákazník“ vložte zákazníka, pak ve sloupci „Objednávkové řádky“ klikněte
:guilabel:'Přidat produkt' a vyberte si z roletky produkt, který má nastavenou
*doba dodání pro zákazníka*, přidat do cenové nabídky.

Nakonec v sloupci „Množství“ upravte požadované množství produktu k prodeji.

Pro tento vzorec průchodu nastavte hodnotu :guilabel:`Quantity` na 10.

Jakmile bude objednávka připravena, klikněte na tlačítko „Potvrdit“.

Klikněte na zelené ikonu „📈 (oblast grafu)“ v řádku produktů, abyste zjistili cenu produktu.
Nástroj „Dostupnost“ v podobě nápovědy. Tento nástroj odhaluje rezervovaný počet jednotek pro tuto objednávku.
Protože je nastaven rezervační způsob na „Před plánovaným datem“, bude množství :guilabel:`Rezervováno“
zobrazuje „0 jednotek“.

Níže je však uvedeno „Dostupné skladem“. To proto, že množství je dostupné.
V tomto příkladu je termín plánovaného datum pět dní od data objednávky.

Pokud je rezervace až dva dny před plánovaným doručením, nebude ji
produkty do té doby.

.. poznámka::
Pokud není dostatečné množství skladových zásob pro produkt zahrnutý v SO,
:guilabel:`📈 (oblastní graf)` ikona je červená místo zelené.

Výsledkem je místo zobrazení rezervovaného počtu jednotek pro objednávku zobrazení :guilabel:`Dostupnost`.
Popisek nástroje zobrazuje „Rezervováno“ a odhaluje dostupný počet jednotek (např. „0 Jednotek“).

Dále pokud není nastavená doplňková zásoba nebo živý příjem, také čte: guilabel:„Není
„Dostupnost v budoucnu“, červeným písmem.

.. obrázek:: před_plánovaným_datem/před-plánovaným-datem-dostupnost-nástrojového-tipu.png
:align:center
:alt: Potvrzená objednávka s vybraným nástrojem pro zobrazení dostupnosti produktu.

Klikněte na tlačítko „Dodání“ a zobrazí se vám formulář objednávky dodání.

V dodacím listu je uveden stav v poli „Dostupnost produktu“ jako
„Dostupné“, v žlutém písmu namísto zeleného. To proto, že je dostatečný počet položek skladem
Tento produkt je v pořadí, ale zatím nebylo vyhrazeno žádné množství.

Zkontrolujte pole „Datum plánovaného termínu“, které je nad poli „Dostupnost produktu“.
zobrazuje datum pěti dnů od data vytvoření objednávky, což znamená, že produkty nejsou
rezervováno do tří dnů od dnešního data (dva dny před plánovaným termínem dodání).

.. obrázek: před termínem/před plánovaným datem - dodací příkaz formulář.png
:align:center
:alt:Formulář pro objednávku dodání s dostupností produktů a rezervovaným množstvím.

V záložce „Provoz“ na řádku „Produkt“ jsou uvedeny čísla
Sloupec „Požadované množství“ a sloupec „Množství“ neodpovídají (v tomto případě je
Sloupec „Požadavek“ obsahuje hodnotu 10,00, zatímco sloupec „Množství“ obsahuje nulu.

Sloupec „Množství“ obsahuje hodnotu 0, protože produkty nejsou rezervovány dva dny předem.
Před jejich dodací datumem. Odoo automaticky rezervuje produkty na stanovený termín
při které se sloupce „Požadavek“ a „Množství“ shodují.

..tip:
Pokud by měly být produkty v |SO| rezervovány dříve než na termín plánované rezervace,
rezervace lze ručně přehrát. Chcete-li manuálně zarezervovat produkty dříve než je naplánováno,
Klikněte na tlačítko „Zkontrolovat dostupnost“ v horní části formuláře.

To zbarví stav „Dostupné“ v poli „Dostupnost produktu“ na zeleno.
změní číslo v sloupci „Množství“ na shodné s hodnotou ve sloupci „Požadavky“.

Jakmile bude připravena, klikněte na tlačítko „Zkontrolovat“.

.. viz také:
   - :doc:`Rezervace ručně <manually>`
   - :doc:`Při potvrzení rezervace <at_confirmation>`
