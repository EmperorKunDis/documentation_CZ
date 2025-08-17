==========
Lucembursko
==========

Konfigurace
=============

:ref:`Instalujte následující moduly, abyste získali všechny funkce luxemburštiny
lokalizace:

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * --:guilabel:Účetnictví - Lucembursko
     - „l10n_lu“
     - Výchozí:balík lokalizace daní:
   * – :guilabel:`Lucembursko - Účetní zprávy“
     - l10n_lu_reports
     - Zeměpisně specifické zprávy
   * – :guilabel:`Lucembursko – Roční zpráva o DPH“
     - l10n_lu_reporty_roční_dph
     - Zeměpisně specifické zprávy

.. obrázek: luxembourg/modules.png
:align:center
:alt:Tři moduly pro lokální fiskální balíček pro Lucembursko na Odoo

.. tip::
Instalací modulu :guilabel:`Lucembursko - účetní výkazy“ se nainstalují všechny tři moduly.
jednou.

.. viz též:
:dokument: „Legalita a soulad s předpisy při elektronické fakturaci v Lucembursku“


Standardní účetní osnova - PCN 2020
=====================================

Balíček pro daňové lokalizace společnosti Odoo pro Lucembursko zahrnuje
Aktuální Standardní účetní osnova (PCN 2020), která je platná od ledna 2020.

eCDF daňové přiznání
===============

Daňové přiznání v Lucembursku vyžaduje konkrétní soubor XML k nahrání na eCDF.

Pro stažení přejděte na: „Účetnictví –> Zprávy –> Zprávy o auditu –> Daňová zpráva“.
klikněte na tlačítko „Export prohlášení o ekologickém čističi vzduchu“.

.. viz též:
   - :doc:`../účetnictví/výkaznictví/daňové přiznání
   - „Elektronická platforma pro shromažďování finančních dat (eCDF)“

Daňový přiznání za rok
=================

Můžete vytvořit soubor XML, který můžete elektronicky podat daňovou zprávu na finanční úřad.

Chcete-li tak učinit, přejděte na: „Účetnictví“ -> „Zpráva“ -> „Lucembursko“ -> „Roková daňová zpráva“, klikněte
V poli „Vytvořit“ zvolte možnost „Rok“.

Souhrnné roční vyúčtování je automaticky generováno. Manuálně můžete přidat hodnoty pro všechny
pole pro vyplnění kompletního ročního hlášení.

.. obrázek: luxembourg/roční daňový přehled.png
:align:center
:alt:Odoo Účetnictví (lokalizace pro Lucembursko) vygeneruje roční daňové přiznání.

Pro úplnost můžete použít informace uvedené v daňovém výkazu.
takže jděte na: „Účetnictví“ – „Zprávy“ – „Auditní zprávy“ – „Daňová zpráva“, pak klikněte na
Vyberte si v rozevíracím seznamu „Zpráva o dani“ a zvolte typ zprávy, kterou chcete zobrazit.

.. obrázek: luxembourg/tax-report-types.png
:align:center
:alt:Drobný návod k používání daňového formuláře

Konečně klikněte na tlačítko „Export XML“ pro stažení souboru XML.

.. poznámka::
Pro tuto funkci je nutné mít nainstalovaný modul „Vyúčtování DPH za rok Luxemburg“.

FAIA (SAF-T)
============

**FAIA (Fichier d’Audit Informatisé AED)** je standardizovaný a strukturovaný soubor, který usnadňuje
výměna informací mezi účetním systémem daňového subjektu a správcem daně.
Lucemburská verze doporučeného formátu SAF-T (Standard Audit File for Tax) navrženého Mezinárodní organizací pro ekonomickou spolupráci a rozvoj.

Odoo může vytvořit soubor XML, který obsahuje všechny položky účetního období.
pravidla stanovená luxemburskými daňovými úřady pro elektronické účetní záznamy.

.. poznámka::
Tato funkce vyžaduje instalaci modulu „Účetní zprávy – Luxembursko“.

Export souboru ve formátu FAIA
----------------

Přejděte na „Účetnictví –> Zprávy –> Kontrolní zprávy –> Obecný účetní deník“ a klikněte na
:guilabel:`FAIA“.
