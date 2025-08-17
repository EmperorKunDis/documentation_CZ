==================
Manuální rezervace
==================

... _Inventarizační metody / Rezervace / Ručně:

.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`

Na rozdíl od metody rezervace *Při potvrzení*, při které se rezervace provádí automaticky, metoda ruční rezervace **ne**
automaticky rezervovat produkty.

Výrobky se místo toho musí ručně zkontrolovat na dostupnost poté, co byla objednávka potvrzena.
a požadované množství musí být ručně rezervováno.

.. viz také:
:doc:`O rezervačních metodách <../reservation_methods>`

Konfigurace
=============

Chcete-li nastavit rezervační metodu na „Manuálně“, přejděte do aplikace Inventář:
Konfigurace --> Typy operací. Pak vyberte požadovaný „Typ operace“
konfigurovat nebo vytvořit nový kliknutím na „New“.

V záložce „Obecné“ najděte pole „Způsob rezervace“ a vyberte
:guilabel:`Ručně“.

.. obrázek: ručně/ruční operace typu.png
:align:center
:alt: pole rezervace na formuláři pro objednávku dodání.

.. poznámka::
Když je změněn typ operace na „Pokladní doklad“,
:guilabel:`Typ operace“ formuláři, rezervace není k dispozici.

Průběh práce
========

Chcete-li vidět metodu rezervace ručně v akci, vytvořte novou |SO| přejděte na
:menu:Prodejní aplikace --> Nová.

V poli „Zákazník“ přidejte zákazníka. Pak v záložce „Částky objednávky“ klikněte
:guilabel:'Přidat produkt' a vyberte produkt, který chcete přidat do nabídky z roletky.
Nakonec v sloupci „Množství“ upravte požadované množství produktu k prodeji.

Jakmile bude objednávka připravena, klikněte na tlačítko „Potvrdit“.

Klikněte na zelené ikonu „📈 (oblast grafu)“ v řádku produktů, abyste zjistili cenu produktu.
Nástroj „Dostupnost“ v podobě nápovědy. Tento nástroj odhaluje rezervovaný počet jednotek pro tuto objednávku.
Protože je nastavená rezervace na „Manuálně“, číslo rezervovaných míst je 0.
Jednotky.

Níže je však uvedeno „Dostupné skladem“. To proto, že množství je dostupné.
Je nutné si je rezervovat ručně.

.. poznámka::
Pokud není dostatečné množství skladových zásob pro produkt zahrnutý v SO,
:guilabel:`📈 (oblastní graf)` ikona je červená místo zelené.

Výsledkem je místo zobrazení rezervovaného počtu jednotek pro objednávku zobrazení :guilabel:`Dostupnost`.
Popisek nástroje zobrazuje „Rezervováno“ a odhaluje dostupný počet jednotek (např. „0 Jednotek“).

Dále pokud není nastavená doplňková zásoba nebo živý příjem, také čte: guilabel:„Není
„Dostupnost v budoucnu“, červeným písmem.

.. obrázek: ručně/ručně dostupnost - nápověda.png
:align:center
:alt: Potvrzená objednávka s vybraným nástrojem pro zobrazení dostupnosti produktu.

Jakmile je potvrzeno, přejděte do aplikace „Inventář“ a najděte
Kartu „Přijaté objednávky“ na stránce „Přehled skladových zásob“.

Karta „Objednávky“ zobrazuje aktuální stav živých objednávek včetně těch
s stavem čekající objednávky. Objednávky s tímto stavem ukazují, že produkty v těchto
objednávky nebyly ještě rezervovány nebo vůbec nejsou skladem.

.. obrázek: ručně/ručně-doručovací-objednávky-karta.png
:align:center
:alt:Karta úkolu pro objednávky s stavem čekající na vyřízení.

Chcete-li vidět předchozí vytvořené |SO|, klikněte na tlačítko „Čeká“ (v tomto
případu „8 čekání“).

Najděte dodací objednávku (DO) spojenou s |SO|, které jste vytvořili dříve, a klikněte na řádek
na něj koukat.

V poli „Dodací objednávka“ na formuláři je stav v poli „Dostupnost produktu“
je uvedeno jako „Dostupné“ v žlutém písmu místo zeleného. To proto, že je dostatečný počet kusů skladem
Je k dispozici pro tento typ objednávky, ale zatím nebyla rezervována žádná kvantita.

V záložce „Provoz“ v řádku „Produkt“ jsou čísla
Sloupec „Požadavky“ a sloupec „Množství“ neodpovídají.

V tomto případě je v sloupci „Požadavek“ uvedeno 10,00 a ve sloupci „Množství“
listy 0.

.. obrázek: ručně/ručně-dodací-list-formulář.png
:align:center
:alt:Formulář pro objednávku dodání s dostupností produktů a rezervovaným množstvím.

Chcete-li ručně rezervovat požadované množství produktu pro tento nákupní příkaz, klikněte na
:guilabel:„Zkontrolovat dostupnost“ tlačítko v horní části formuláře. To způsobí, že se stav „Dostupný“ změní
V poli „Dostupnost produktu“ zelená a změní číslo v
Sloupec „Množství“ k odpovídajícímu sloupci „Požadavky“.

Je to proto, že je dostatečné množství skladem k rezervaci pro objednávku.

Jakmile bude vše připraveno, klikněte na tlačítko „Zkontrolovat“.

..tip:
Můžete si zadat více objednávek s stavem „Čeká na vyřízení“ najednou a nastavit je na
Stav „Připraveno“.

Pro zobrazení inventáře otevřete aplikaci „Inventář“, která zobrazí „Inventář
Stránka „Přehled“. Stránku „Přehled“ lze také zobrazit kliknutím na
:menu_selektor:`Inventář aplikace --> Přehled.

Z přehledu inventáře se dostanete na stránku s tlačítkem „Čekající“ (#)
:guilabel:`Objednávky“ kartu.

Pak zaškrtněte políčka vedle požadovaných objednávek nebo zaškrtněte políčko v hlavičce.
řádku, na nejvzdálenější levou stranu, vybrat všechny objednávky najednou.

Pak klikněte na tlačítko „Zkontrolovat dostupnost“ v horní části stránky.

Pokud má každý vybraný produkt v objednávce dostatečné množství skladem, rezervuje se
produkty a přesune objednávku do stavu „Připraveno“. Jakmile obdrží objednávku v stavu „Připraveno“,
stavu se objednávka zobrazí v seznamu „Čeká na vyřízení“.

Pokud není dostatečné množství skladem, objednávka si zachovává svůj aktuální stav a zůstává na
seznam.

.... obrázek: manuálně/manuálně-zjistit-dostupnost.png
:srovnání: do středu
:alt:Seznam objednávek v čekajícím stavu a tlačítko pro zjištění dostupnosti.

.. viz také:
   - :doc:`Při potvrzení rezervace <at_confirmation>`
   - :doc:`Před plánovaným termínem rezervace <before_scheduled_date>`
