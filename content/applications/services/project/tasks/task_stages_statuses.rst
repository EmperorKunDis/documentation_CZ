========================
Stavy úkolů a stavové hlášení
========================

Úkoly
===========

Kanbanová zobrazení projektu ukazují úkoly jako sloupce a umožňují aktualizovat
postup svých úkolů pomocí přetažení a ponechání na místě. V většině projektů budou fáze podobné **Nový**
**Ve vývoji**, **Zpětné zadání** atd.

Výchozí nastavení úkolů je projekt specifické, ale lze je sdílet mezi více projekty.
stejný postup.

Vytváření úkolových fází
--------------------

Projekt Odoo neposkytuje výchozí fáze, ale umožňuje vytvářet vlastní fáze přizpůsobené.
na konkrétní potřeby vašeho podnikání. Už po vytvoření nového
projektu <správa projektů/konfigurace>.

Pro vytvoření scény zadejte její název do pole :guilabel:`Stage...`, pak klikněte na :guilabel:`Add`.

..tip:
Klikněte na tlačítko „Zobrazit příklady“ a najdete nápady na jména pro vaši oblast podnikání.

Úprava úkolů v jednotlivých fázích
-------------------

Chcete-li upravit fázi úkolu, klikněte na ikonu „fa-cog“ („cog“) vedle jejího názvu.
Vyberte jednu z následujících možností:

 - :guilabel:`Sbalit“: skrýt stupeň úkolu a všechny úkoly v tomto stupni z pohledu Kanban.
 - :label:Edit:

   - :guilabel:`Jméno“: změnit název fáze.
   - :guilabel:Šablona e-mailu/SMS): automaticky odeslat e-mail nebo SMS s upozorněním na
zákazník, když se úkol dostane do této fáze.
   - :guilabel:`Složené v Kanban“: skrýt stupeň úkolu a všechny úkoly v tomto stupni
Kanban pohled.
   - :guilabel:`Projekty“: sdílet tuto fázi úkolu mezi několik projektů.
   - :guilabel:`Automatizace“: vytvořit :doc:`vlastní pravidla, která spouštějí automatické akce
<../../../studio/automated_actions> (např. vytváření aktivit, přidávání sledujících nebo odesílání
webhookech (poznámka: tímto se aktivuje Studio v databázi, což může ovlivnit
Váš plán cen.

 - :guilabel:`Smazat“: tuto fázi smazat.
 - :guilabel:`Archivovat/Odarchivovat vše“: archivovat nebo odarchivovat všechny úkoly ve fázi.

... projektu / úkolů / úkolových fází / stavů:

Stavy úkolů
=============

Stavy úkolů se používají k sledování stavu úkolů v rámci kanbanového stupně a také k uzavření
pokud je splněna nebo zrušena. Na rozdíl od fází kanbanu nelze jejich nastavení upravit; pět stavů úkolů
existují v Odoo a používají se následovně:

 - :guilabel:„Ve vývoji“: tento stav je vždy nastaven pro všechny úkoly a znamená, že práce na
pracuje se na tom, aby se přesunula do dalšího stupně kanbanu.
 - :guilabel:`Požadované změny“: aby bylo možné upozornit na změny požadované zákazníkem nebo
Před přesunem úkolu na další stupeň kanbanového modelu jsou potřebné interní procesy.
 - :guilabel:„Schváleno“: vyznačuje, že úkol je připraven k dalšímu postupu.
 - :cancelled: zrušit úkol.
 - :guilabel:`Dokončeno“: zavřít úkol, jakmile bude dokončen.

.. poznámka::

   - Stavy úkolů „Žádá se změna“ a „Schváleno“ jsou vymazány, jakmile
úkol je přesunut na jiný kanbanový stupeň. Stav úkolu se vrátí do výchozího nastavení :guilabel:`V
Stav projektu tak, aby měl stav „Žádost o změnu“ nebo „Schváleno“.
Pokud je třeba, aplikují se znovu po dokončení potřebné práce v tomto kanbanovém stupni.
   - Stavy „Dokončeno“ a „Zrušeno“ nezávisí na stavu kanbanového stupně.
Jakmile je úkol označen jako „Dokončeno“ nebo „Zrušeno“, je uzavřen. Pokud je to nutné, může být
Může být znovu otevřen změnou jeho stavu.
