==================
Zacílení na publiku
==================

Pole „Zaměření“ a „Filtr“ na formuláři kampaně, také nazývané
*doména*, obsahuje parametry, které definují cílovou skupinu pro dosah kampaně (tj.
jedinečné záznamy v databázi (např. kontakty, importované seznamy atd.)

- :guilabel:`Target“: určuje typy záznamů dostupných k použití v kampani, například
:guilabel:`Přední/příležitost“, :guilabel:`Registrace události“, :guilabel:`Kontakt“ a přiřazený
záznamový model určuje pole dostupná po celou dobu kampaně včetně
políčka dostupná v sekci Filtr a dynamické položky.
- :guilabel:`Uložit jako oblíbený filtr“: ukládá aktuální :guilabel:`Filtr“ pro budoucí použití s
současný model „Cíl“ a lze jej spravovat z „Marketingové automatizace“.
aplikace --> Nastavení --> Menu oblíbených filtrů.
- :guilabel:`Uničnost na základě“: určuje pole :guilabel:`Cíl“ modelu, kde by se měly duplikáty
se vyhnout. Klasicky se používá pole :guilabel:`E-mail`, ale může být použito jakékoliv dostupné pole.
nebyla použita.
- :guilabel:`Filtr“: obsahuje interaktivní formulář s konfigurovatelnou logikou, který umožňuje další filtrování
cílové parametry podle zvoleného modelu „Cíl“. Podrobnější informace naleznete v
:ref:`marketing_automation/definice-filtrů` části.
- :guilabel:`Zahrnout archivované záznamy“: umožňuje nebo zakazuje zahrnutí archivovaných záznamů do cílového souboru.
diváci.

..tip:
Uživatelé s oprávněním „Zodpovědný“ mohou být přiřazeni k kampani aktivací
:ref:`vývojářský režim`.

.. poznámka::
Každá aktivita v kampani může cílit na podskupinu cílové skupiny.
:doc:`workflow_activities“ dokumentace pro více informací.

... _marketing_automation/definice-filtrů:

Definování filtrů
================

Výchozí konfigurace kampaně „Filtr“ je nastavena na „Zahrnout všechny záznamy“,
Ukazuje, že kampaň cílí na všechny záznamy v modelu „Cíl“.

Pro vyladění pravidel filtru kampaně klikněte na tlačítko „+ Přidat podmínku“.
ukázat novou řadu s konfigurovatelnými parametry pravidel. Podívejte se na :ref:`Vyhledávání, filtrování a seskupování
Pro více informací o vytváření filtračních pravidel se podívejte na dokumentaci pro záznamy <hledání/vlastní filtry>.

.. obrázek: cílová skupina/filtry domén.png
:align:center
:alt: Nová řádka filtru v kampani Filters.

Na spodní části filtru je tlačítko „Počet záznamů“ označené znakem #, které ukazuje celkový počet
Počet cílených záznamů v této doméně. Kliknutím na tlačítko „Záznamy“ se zobrazí
Pop-up okno „Vybrané záznamy“, ve kterém lze zobrazit cílové záznamy.

..tip:
Aktivujte režim vývojáře pomocí tlačítka „Vývojářský režim“ a zobrazte si technické názvy polí a datové typy.
textovém poli pod filtrem pravidel, abyste mohli zobrazit a upravovat doménu.
ručně.

Příklad:
Zacílit na všechny kontakty a příležitosti z aplikace CRM v stádiu New.
Pokud očekávaný příjem přesahuje 1 000 $, mělo by být zadáno následující:

   - :guilabel:`Cíl“: „Příležitost/šance“
   - :guilabel:`Uničnost na základě“: „E-mail (lead/příležitost)“
   - Filtr:Souhlasit s:Všechny (svislá šipka dolů)
podle následujících pravidel:

     #:guilabel:`Stage“ je v „New“
     #:guilabel:`Očekávaný příjem“ :guilabel:`> 1.000“
     #:guilabel:`jakýkoliv ⬇️ (směrem dolů)“:guilabel:`z:

        - :guilabel:`Typ“ :guilabel:`=“ :guilabel:`Přední
        - :guilabel:„Typ“ :guilabel:„=“ :guilabel:„Příležitost“

S výše uvedenou konfigurací cílí kampaň na :guilabel:`157 záznamů`.

.... obrázek: cílová skupina/filtr scénář 1.png
:synchronizace: střed
:alt: Konfigurace domény v kampani Marketing Automation.

.. viz též:
   - :ref:`Dokumentace pro vývojáře domén <reference/orm/domains>`
   - :doc:`workflow_activities“
   - :doc:`testovani_běhání“
   - :doc:`pochopení metrik“
