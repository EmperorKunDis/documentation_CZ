====================
Správa uživatelských účtů
====================

Uživatelé v aplikaci Lunch zaplatí za produkty přímo z účtu aplikace Lunch.
Pokud chcete mít peníze na svém účtu, musíte je manažer aplikace Lunch převést.
uživatelský účet.

.. důležité::
Přidávat prostředky a spravovat uživatelské účty může pouze uživatel s oprávněním :guilabel:`Administrátor
pro aplikaci Lunch. Toto je ověřeno přechodem do nastavení aplikace
-->:icon:`oi-arrow-right`:guilabel:`Správa uživatelů“. Pak klikněte na uživatele, abyste zobrazili jejich různé
nastavení a oprávnění.

Pro více informací se podívejte na :doc:`Přístupová práva <../../general/users/access_rights/>“.
dokumentace.

Aplikace **Lunch** se **nepropojuje** s žádným softwarovým nebo hardwarovým produktem.
Nebyly spojeny s žádným účtem pro platby nebo s jakýmikoliv finančními prostředky.
účty ani nemohou být kreditní karty uživatelů účtovány.

Aplikace Lunch společnosti Odoo **pouze** umožňuje ruční zadávání hotovostních transakcí, které jsou
Aplikaci Lunch, která je v rukou jejího manažera. Každá společnost si musí sama vytvořit metodu, jak
Na obědy se přidává peníze.

.. příklad::
Několik příkladů, jak lze peníze organizovat a převádět v rámci společnosti:

   - Peníze jsou předány manažerovi aplikace Lunch, který pak aktualizuje účet uživatele.
   - Peníze jsou automaticky odečteny z výplaty uživatele a poté je spravuje aplikace Lunch.
aktualizuje účet, když jsou vyplaceny mzdy. Toto vyžaduje:ref:`přidání přílohy s výplatní páskou
pro výplatní pásku uživatele v aplikaci *Mzdy*.
   - Firmy mohou prodávat „jídelní lístky“ za stanovenou cenu (například jeden lístek stojí 5 dolarů). Uživatelé
Mohou si zakoupit lístky od manažera aplikace Lunch, který pak aktualizuje účet uživatele.

...oběd/hotovostní pohyby:

Pohyby hotovosti
==========

Přidávat prostředky na účty uživatelů je možné pouze po jednotlivých převodech, které musí být zaznamenány zvlášť.
zaznamenat nebo vytvořit nový pohyb hotovosti, přejděte na: menu „Obědová aplikace -> Správce -> Hotovost
Přesunout“. To odhalí panel „Měnové pohyby“.

Na panelu „Pohyby v hotovosti“ jsou všechny pohyby v hotovosti zobrazeny ve výchozím seznamovém zobrazení.
zobrazení každého záznamu s datem, uživatelem, popisem a
:guilabel:`Částka“. Celková částka všech hotovostních pohybů se zobrazuje na dně
:guilabel:`Částka“ sloupec.

.. obrázek: uživatelské účty/hotovost.png
:alt: Zobrazení seznamu všech pohybů na účtu.

Přidejte peníze
---------

Přidat peníze na účet oběda kliknutím na tlačítko „Nový“, které se nachází v pravém horním rohu
příkazovém řádku Cash Moves.

Vyplňte následující informace na formulář „Pohyby hotovosti“:

- :guilabel:`Uživatel“: vyberte uživatele, který vkládá hotovost na svůj účet z nabídky. Pokud
uživatel není v databázi, lze ho vytvořit zadáním jeho jména do pole :guilabel:`User
pole a klikněte buď na „Vytvořit uživatele“ nebo „Vytvořit a upravit…“, abyste vytvořili
uživatele a upravit formulář „Vytvoření uživatele“.
- :guilabel:`Datum“: vyberte datum transakce pomocí kalendáře.
- :guilabel:`Částka“: zadejte částku, kterou chcete přidat na stravovací účet.
- :guilabel:`Popis transakce“: zadejte stručný popis transakce.

.. obrázek: uživatelské účty/převod peněz formulář.png
:alt:Formulář pro převod 40 dolarů vyplněný v hotovosti.

Kontrolní účty
================

Přehled všech transakcí v aplikaci Lunch, včetně hotovostních vkladů a nákupů.
můžete vidět na hlavním panelu „Hlavní účty“. Chcete-li se dostat k tomuto panelu, přejděte na
:menuselection:`Obědová aplikace --> Správce --> Kontroly účtů.“

Všechny transakce jsou seskupeny podle zaměstnance a uživatelé se řadí abecedně podle svého jména.
jméno. Na konci uživatelského jména se objevuje číslo. To značí pořadové číslo jednotlivce
Záznamy evidované pro tento uživatel.

Výchozí pohled je skrýt všechny transakce jednotlivých uživatelů. Chcete-li zobrazit všechny transakce pro daného uživatele
Klikněte na ikonu „fa-caret-right“ (trojúhelník) v levém sloupci vedle požadovaného jména.
rozšířit konkrétní skupinu.

Každý záznam obsahuje pole „Datum“, „Uživatel“, „Popis“ a
:guilabel:`Částka“.

.. obrázek: uživatelské účty/účty pro správu.png
:alt: Panel s přehledem účtů s rozbalenými transakcemi dvou zaměstnanců.

.. důležité::
Seznam pouze zobrazuje různé transakce v aplikaci Lunch a neumožňuje
které mají být provedeny v příslušných záznamů.

Pohyby hotovosti lze upravit, ale pouze z :ref:`dashboardu Pohyby hotovosti <lunch/cash-moves>`.
nikoli z panelu „Kontrolní účty“.

Není možné upravit žádné záznamy týkající se produktu.
