=========
Schválení
=========

.. |ECO| nahradit za: zkratku: `ECO (Engineering Change Order)`
.. |ECN| nahrazuje: zkratka: `ECN (Engineering Change Notices)`

.._plm/schválení:

Informujte zainteresované osoby a manažery automaticky přiřazením schvalovatelů k fázím:ref:`inženýrství
změny objednávek (ECOs) jsou pod přísným dohledem. Změny lze provést pouze po přiřazení
schvaluje je. Schválení zajišťuje kontrolu členů týmu, což zabraňuje chybám a
předčasných kroků.

.. viz též:
:ref:`Konfigurace scény <plm/eco/scene-config>`

Přidejte schvalovatele
=============

Chcete-li přidat schvalovatele, nejprve se přihlaste do aplikace PLM a klikněte na kartu projektu.
Klikněte na tlačítko „ECO“ pro otevření grafu Ganttu ECO.

Na stránce „Změny v projektu“ přejeďte kurzorem nad požadovanou etapou a vyberte
Klikněte na ikonu „Nástroje“ (vlevo dole) a poté na „Upravit“.

.. poznámka::
Schvalovatelé mohou být přidáni na jakýkoliv stupeň, ale jsou nejdůležitější v *ověření*.
před finální fází uzavření, která aplikuje |ECO| a aktualizuje :abbr:`BoM (Fakturu).
„Materiály“. To umožňuje zúčastněným stranám kontrolovat, jak a kdy se provádějí změny.

Podrobnější informace najdete v dokumentaci o typech stádií (plm/eco/stage-config).

V okně „Upravit“ klikněte na tlačítko „Přidat řádek“, které se nachází pod
:guilabel:`Schválení“. Pak zadejte pozici nebo titul schvalujícího pod :guilabel:`Role“
(např. „Inženýrský manažer“, „Tým kvality“ atd.) a vyberte příslušného uživatele z
záložky.

..._plm/schválení/druh schválení:

Typy schválení
--------------

Dále nastavte :guilabel:`Typ schválení“ na „Je nutné schválit“, „Schvaluje“.
Ale schválení je nepovinné“, nebo „Komentáře“.

Příklad:
Přidat „Mitchell Admin“ jako povinného schvalovatele pro |ECOs| v kroku „Validated“.
typu „Zavedení nového produktu“ |ECO|.

Schválení ze strany týmu kvality a marketingu **není** potřeba, aby se prováděly změny v |ECO|
protože jejich „Typ schválení“ je nastaven na „Schvaluje“, ale schválení
„volitelné“ a „pouze komentáře“, v závislosti na tom, co chcete.

.. obrázek: schválení/schvalující.png
:alt:Nastavte schvalovatele, který „musí schválit“ ECO v „Potvrzené“ fázi.

Správa schválení
================

Schválení úkolů lze sledovat přes menu „PLM aplikace“.
vybrat kartu pro typ |ECO|, která zobrazuje počet otevřených úkolů přiřazených jim.

.. obrázek: schválení/ověření - přehled.png
:alt:Zobrazení počtu schválených úkolů a tlačítka pro otevření filtrovaného seznamu ECO.

Tady je, co každá tlačítka na kartě projektu dělá:

#Tlačítko „Změny v projektu“ zobrazí počet probíhajících změn (ECO).
typu. Po kliknutí na tlačítko se otevře pohled Ganttu stránky :guilabel:`Engineering Change Orders`.
#:guilabel:`Moje kontroly“ zobrazuje počet |ECOs|, které musí schválit nebo zamítnout.
Kliknutím na tlačítko se zobrazí ECO, které čeká na schválení nebo byly zamítnuty (označené červeně).
:guilabel:`Zablokovaný“ stav).
#Tlačítko „Všechny kontroly“ zobrazuje počet ECO, které čekají na schválení nebo zamítnutí.
kdokoliv z schvalovatelů. Kliknutím na něj se zobrazí tyto nevyřízené |ECOs|.
#:guilabel:'Aplikovat' zobrazuje počet |ECOs| na které je potřeba aplikovat změny.
Kliknutím na tlačítko se zobrazí všechny |ECOs| k schválení a změně.
ověřovací fáze.

Uživatelé se mohou podívat na zeleně označené „Dokončeno“ a už jsou schváleny.
kliknout na tlačítko „Zobrazit formulář“ a poté kliknout na tlačítko „Použít změny“.

..tip:
Schválení ECO lze přistupovat, spravovat a naplánovat další kroky v sekci „Aktivita“.
Podrobnější informace najdete v dokumentaci k aktivitám, viz :doc:`Activities documentation <../../../essentials/activities>`.
sloučit pracovní postupy řízení.

Schválit ECO
------------

Přejděte do fáze ověření jako přihlášený uživatel s přiděleným schvalovatelem, abyste viděli
tlačítka „Přijmout“, „Odmítnout“ a „Aplikovat změny“.

Schválit |ECO| a aplikovat změny do výroby: zkratka „BoM (Bill of Materials)“
Klikněte na tlačítko „Potvrdit“ a poté na „Uplatnit změny“.

Poznámka: Tlačítko „Aplikovat změny“ nebude fungovat, pokud není schváleno.
Byl kliknutý první. Dále uchovává historii kliknutých tlačítek.

.. varování:
Pokud žádný schvalující nemá typ schválení „Je nutné schválit“, pak se použije typ schválení „Aplikovat“.
Tlačítko „Změnit“ bude fungovat i bez kliknutí na tlačítko „Schválit“.
první.
