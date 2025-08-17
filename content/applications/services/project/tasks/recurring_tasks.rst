===============
Opakující se úkoly
===============

Při práci na projektu je často nutné stejnou úlohu opakovat několikrát: například
týdenní schůzky nebo zprávy o stavu. Funkce „opakující se úkoly“ vám umožňuje automatizovat
vytváření těchto úkolů.

.. viz též:
„Tutoriály Odoo: Opakující se úkoly <https://www.odoo.com/slides/slide/recurring-tasks-6958>“

Konfigurace
=============

Pro opakované úkoly přejděte na: „Projekt --> Konfigurace --> Nastavení“, pak
Aktivujte „Opakované úkoly“ a stiskněte „Uložit“.

Založte opakování úkolů
----------------------

V již existujícím úkolu klikněte na tlačítko s ikonou „fa-repeat“ („Opakovat“) vedle
Pole „Uzávěrka“ a poté konfigurujte pole „Opakovat každý“ podle svých požadavků.
potřeby.

Jakmile je nastaveno stav předchozího úkolu, vytvoří se nový úkol ve smyčce.
:guilabel:`Dokončeno“ nebo „Zrušeno“.

Nový úkol je vytvořen na panelu projektu s následující konfigurací:

- :guilabel:`Stage“ je nastaven na první fázi projektu („New“ nebo
(přesný ekvivalent).
- :guilabel:`Jméno“, :guilabel:`Popis“, :guilabel:`Projekt“, :guilabel:`Přiřazení“
:guilabel:`Zákazník“, :guilabel:`Štítky“: jsou kopírovány z původní úlohy;
- :guilabel:`Termín dokončení“ je aktualizován na základě pole „Opakovat každý“ (např. pokud úkol
případně se termín prodlouží o 7 dní (v případě opakování jednou týdně).
- :guilabel:`Míle“, :guilabel:`Časové záznamy“, :guilabel:`Komunikace“
:guilabel:`Aktivita“, :guilabel:`Podúkol“: nejsou **kopírovány** z původního úkolu.

Jakmile je nastaveno opakování, tlačítko „Chytré tlačítko“ v úkolu zobrazuje celkový počet
Stávající relapsy.

Upravit nebo zastavit opakování úkolu
----------------------------

**Upravit** opakování úkolu otevřením posledního úkolu v opakování.
aplikovat na úkoly, které v budoucnu vzniknou.

Pro zastavení opakování úkolu otevřete poslední úkol v opakování a stiskněte tlačítko „Opakovat“.
tlačítko vedle pole „Datum plánované akce“.
