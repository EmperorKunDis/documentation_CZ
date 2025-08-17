=====================
Profitabilita projektu
=====================

Při zpracování fakturovatelných projektů je nezbytné určit, zda vaše projekty přinášejí
zisk. Zjišťování výnosnosti projektu zahrnuje sledování nákladů na zdroje, které byly použity k
zajistit realizaci projektu, například náklady na zaměstnance, materiál použitý, nákupy, výdaje nebo pozáruční servis.
služeb a srovnávat je s příjmy projektu.

Profitabilita projektu je sledována na všech fakturovatelných projektech v :doc:`projektovém přehledu <project_dashboard>`.
Projekty.

Chcete-li získat přístup k panelu projektu, otevřete aplikaci **Projekt** a přejděte na
použitý projekt. Klikněte na ikonu „fa-sliders“ („Slider“) pro přidání
:guilabel:`Přístupový panel“ do horní lišty projektu.

..tip:
Můžete také přistupovat na :doc:`přístupovou stránku projektu <project_dashboard>`, pokud se nad
kartu projektu, kliknutím na ikonku „vertikální elipsa“ (:guilabel:`fa-ellipsis-v`) a výběrem
:guilabel:`Přístrojová deska“.

Profitabilitní panel je na pravé straně projektového panelu a zobrazuje údaje o
všechny spojené s projektem a jeho
:dokumentu „Analytická účetní evidence“ (viz aplikace Finance, podúčet Reporting, analytická účetní evidence).
dělí se na dvě hlavní části: „příjmy“ (< projekt/ziskovost projektu/příjmy >), které
zobrazuje rozdělení příjmů z projektu.
:ref:`náklady <projekt/ziskovost projektu/náklady>“ vaší společnosti.
zobrazené v obou sekcích například stejný výkaz zisku a ztrát je uveden pod štítkem :guilabel:`Příjem
za práci a pod položkou „Náklady“ s částkou mzdy,
Zaměstnanci.

.. obrázek: projekt_ziskovosti/dashboard-ziskovosti.png
:alt: Dashboard projektu.

Výnosy uvedené v ziskovosti jsou rozděleny do tří sloupců:

 - :guilabel:`Očekávané“: částky očekávané na základě stávajících objednávek nebo faktur.
 - „Faktura“ (příjmy) nebo „Přijatá faktura“ (náklady): částky se přesouvají do této
sloupec v okamžiku dodání práce nebo zboží, např.
:doc:`Časovka </aplikace/služby/časovky>` byla vytvořena nebo ověřena.
byla objednávka doručení označena jako dokončená nebo ručně aktualizována na dodané množství.
objednávka na prodej.
 - „Vystaveno“ nebo „Zaplaceno“: částky se přesouvají do této sloupce, jakmile je faktura vystavena.
nebo faktura byla potvrzena.

Na stejném principu je dále rozdělená sekce příjmů na:guilabel:`Prodané`.
Sloupce „Dodáno“ a „Fakturováno“. Použijte :icon:`fa-caret-right
Ikona „:guilabel:'arrow'“ umožňuje zobrazit podrobné rozdělení pro každou řádek.

..tip:
V horní části projektu použijte :ref:`přístupovou lištu <project/project-management/top-bar>`, abyste snadno mohli přistupovat a upravovat
záznamy spojené s projektem z pohledu jeho rentability v kanbanovém pohledu na projekt.

.. důležité:
Aby se záznam zobrazil na panelu výkonnosti, musí být propojen s
projekt a jeho analytický účet:doc:`</applications/finance/accounting/reporting/analytic_accounting>`.

Následující záznamy lze zobrazit v přehledu o zisku.

.. projekt/ziskovost projektu/tržby:

Tržby
--------

 - :guilabel:`Časové listy“: příjmy z časových listů,
rozdělen podle zvolené politiky fakturace produktu (např.
:doc:`Předplacené / pevné ceny </účetnictví/prodej/fakturace/fakturační politika>`
:doc:`Na základě časových listů </applications/sales/sales/invoicing/time_materials>`,
:doc:`Na základě milníků </applications/sales/sales/invoicing/milestone>“.
 - :guilabel:`Materiály“: celková prodejní cena produktů prodaných prostřednictvím objednávek na prodej
projektu.
 - :guilabel:`Faktury zákazníků“: celkový počet faktur spojených s projektem.
 - :guilabel:`Předplatné“: celkový prodejní ceny
:doc:`předplatné </prodej/smlouvy/předplatné>“ spojené s projektem.
 - :guilabel:`Úhrada kupní ceny“: celkem
:doc:`zálohy na projekty </aplikace/prodej/fakturace/záloha/>“.
 - :guilabel:`Náklady“: jakékoliv :doc:`náklady </aplikace/finance/náklady>`
:doc:`přičtena k faktuře zákazníkovi </aplikace/prodej/fakturace/náklady/>.

.._projekt/ziskovost projektu/náklady:

Náklady
-----

 - :guilabel:`Časové listy“: celkové náklady na sledování času zaměstnanců prostřednictvím „časových listů“.
</aplikace/služby/časové listy>“, založené na zaměstnanci
:ref:`Nastavení HR <employees/hr-settings>`.
 - :guilabel:`Nákupní objednávky“: celkové náklady
:doc:`objednávky </applications/inventory_and_mrp/purchase/manage_deals> spojené s
projektu. Ty mohou pokrývat zboží, materiál nebo i poddodavatelské služby. Tento záznam
Vystupuje poté, co je vystaven faktura od dodavatele.
 - :guilabel:`Materiál“: celkové náklady na produkty zahrnuté v
:doc:`pohyby zásob </applications/inventory_and_mrp/inventory/dodávky a přijímání zásob>` (dodávky a
účetních dokladů, které byly pro projekt schváleny. Tato sekce se zobrazí pouze v případě, že
:guilabel:`Analytické náklady“ byly povoleny
:menu „Sklad --> Konfigurace --> Typy operací“ pro aplikovatelné operace.
zajišťuje, že během přesunu zásob je sledován náklad na produkt.
 - :guilabel:`Náklady“: celkové náklady na :doc:`náklady </aplikace/finance/náklady>“ spojené s
projektů, které byly podány a schváleny.
 - :guilabel:`Faktury dodavatele“: celkové náklady na
:dokument: „Faktury dodavatelů“ v sekci „Spravovat smlouvy“ v části „Nákup“.
analytický účet projektu.
 - :guilabel:`Objednávky výroby“: celkové náklady na objednávky výroby spojené s projektem
analytický účet.
 - :guilabel:`Jiné náklady“: jakékoliv jiné náklady spojené s analytickým účtem projektu.
