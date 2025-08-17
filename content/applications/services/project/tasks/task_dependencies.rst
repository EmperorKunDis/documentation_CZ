=================
Závislost úkolů
=================

Odoo Project vám umožňuje rozdělit projekty na úkoly a založit mezi nimi vztahy.
úkoly, které určují pořadí jejich provedení. Úkolové závislosti zajišťují, že určité úkoly
začínají až po dokončení předchozích úkolů.

Pro nastavení závislostí úkolů v projektu přejděte do nabídky „Projekt“ -> „Konfigurace“ ->
Nastavení, zapněte „Závislosti úkolů“ a klikněte na „Uložit“.

Nastavte závislosti úkolů
=====================

Závislosti úkolů lze vytvořit z formuláře úkolu nebo z projektu ve formě Ganttova diagramu pomocí propojení
nástupnická úloha (tj. úkol, který je blokován jinými úkoly), na které navazuje předchozí úkol(y)
blokování následného úkolu).

Pro vytvoření závislosti úkolů z formuláře úkolu přejděte na požadovaný úkol a
V záložce „Zablokované“ klikněte na „Přidat řádek“. Kliknutím na „Zobrazit“ se dostanete
předchozí úkol. K přístupu k následujícím úkolům z předchozího úkolu klikněte na
tlačítko „Blokované úkoly“.

Vytvořit závislost úkolu z pohledu Ganttova diagramu. Na předcházející úkol myší přejeďte, pak
Klikněte na jeden z bodů, který se objeví kolem něj. Přetáhněte a vložte bod do následujícího úkolu.
zobrazuje závislost na předcházejícím úkolu a následném úkolu.

.. obrázek: task_dependencies/task-dependency.png
:skalka: 80 %
:alt:Závislost úkolů

Odoo automaticky spravuje postup úkolů podle jejich závislosti. Následné úkoly jsou přiřazeny
Stav „Čeká na vyřízení“ a nemůže být přesunut do stavu „Ve výrobě“, dokud jejich předchůdce
úkol je označen jako „Schválený“, „Zrušený“ nebo „Dokončený“.

Odstraňte závislosti
===================

Pro odstranění závislosti úkolu postupujte takto:

- Přejděte na záložku „Blokované“ a klikněte na ikonu :icon:`fa-times`.
tlačítko s názvem (:guilabel:`times`).
- Z pohledu Ganttovy diagramu klikněte na červené tlačítko s ikonou „x“ (zobrazením „x“)
centrum šipky, když na ni myší přejedete.
