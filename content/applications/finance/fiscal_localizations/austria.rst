=======
Rakousko
=======

Konfigurace
=============

:ref:`Nainstalujte následující moduly, abyste získali všechny funkce rakouské
lokalizace.

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * --:guilabel:`Účetnictví - Rakousko“
     - l10n_at
     - Výchozí:balík fiskální lokace <fiscal_localizations/packages>.
   * – :guilabel:`Účetní zprávy Rakouska“
     - l10n_at_reports
     - Přidává lokální verze finančních zpráv
   * :- guilabel:"Rakouský export SAF-T"
     - l10n_at_saft
     - Přidává vývoz do SAF-T.

.. viz též:
:doc:`Dokumentace o zákonnosti a souladu s předpisy v Rakousku


Finanční výkazy
=================

K dispozici jsou následující místní zprávy:

  - Výkaz zisku a ztráty podle § 224 UGB <https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001702&Artikel=&Paragraf=224&Anlage=&Uebergangsrecht=>
  - Zisk a ztráta podle § 231 UGB <https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10001702&Artikel=&Paragraf=231&Anlage=&Uebergangsrecht=>_ (celkové náklady)

.. viz též:
:doc:`Účetní zprávy <../accounting/reporting>`

SAF-T (Standard Audit File for Tax)
===================================

Rakouské daňové úřady mohou požadovat SAF-T. Modul pro vývoz rakouského SAF-T umožňuje export
výkaz v XML formátu.

Konfigurace
-------------

Tato část vysvětluje, jak nakonfigurovat databázi tak, aby obsahovala všechny informace požadované
SAF-T je k dispozici. Pokud něco chybí, zobrazí se upozornění s uvedením informací, které jsou potřeba
Bude zobrazena při exportu.

Informace o společnosti
~~~~~~~~~~~~~~~~~~~

Otevřete databázi: guilabel:Nastavení. V sekci „Firmy“ klikněte
„Aktualizovat informace“ a ujistěte se, že jsou správně vyplněny následující pole:

- :guilabel:`Adresa“, poskytne alespoň následující informace:

  - :label:Ulice
  - :guilabel:`Město“
  - :guilabel:`ZIP“
  - :guilabel:`Země“

- :guilabel:`Telefon“
- :guilabel:`ID společnosti“ a zadejte daňové identifikační číslo vaší společnosti
- :guilabel:`Daňové číslo“ poskytnutím, pokud je k dispozici, svého „UID-Nummer
(Daňové identifikační číslo, včetně zeměpisného kódu).

Kontaktní osoba
**************

K vaší společnosti musí být alespoň jeden kontaktní člověk propojený v aplikaci Kontakty a:

  - Zajistěte, aby byl typ kontaktu nastaven na:guilabel:`Osobní“.
  - Vyberte svou společnost v poli „Název společnosti“.
  - Zadejte alespoň jednu telefonní číslo pomocí pole :guilabel:`Telefon`, nebo :guilabel:`Mobil`.

Informace o zákazníkovi a dodavateli
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Použijte aplikaci „Kontakty“ a do pole „Adresa“ zadejte adresu jakéhokoliv partnera, který se v
faktury, dodací listy nebo platby.

Pro partnery ve formě společností vyplňte DIČ (včetně zemního kódu).
:guilabel:`Daňové identifikační číslo“ pole.

Nastavení účetnictví
~~~~~~~~~~~~~~~~~~~

Přejděte na: „Účetnictví“ - „Konfigurace“ - „Nastavení“. Pod položkou „Rakousko
V sekci „Lokalizace“ vyplňte následující pole:

- :guilabel:`Kód NACE“
- :guilabel:`Metoda hodnocení zisku“

.. viz též:
„Informace o hospodářských komorách na webu rakouské vlády
<https://www.wko.at/service/zahlen-daten-fakten/oenace.html>

Mapování účetních knih
~~~~~~~~~~~~~~~~~~~~~~~~~

Rakouské specifikace SAF-T definují účetní knihu. Všechny důležité účty pro
Export SAF-T musí být označen příslušným účtem z této KOA.

Potřebné informace o mapování jsou dodávány přidáním tagů k účtům. Například přidáním
Tag „1000“ přiřadí účet virtuálně k účtu SAF-T s kódem „1000“.
číslo lze používat, dokud existuje účet v SAF-T COA s tímto kódem.

Modul „Účetnictví – Rakousko“ přidává štítek pro každý účet SAF-T COA. Dále
automaticky mapuje mnoho účtů z výchozího rakouského COA.

Můžete zkusit exportovat hlášení SAF-T, abyste se ujistili, že nejsou nezařazené účty (nebo jsou zařazeny).
více účtů SAF-T). V případě problémů s konfigurací se zobrazí upozornění
nebo mapování. Kliknutím na „Zobrazit problémové účty“ zobrazíte je.

.. viz též:
:doc:`Dokumentace k účetnímu deníku <../accounting/get_started/chart_of_accounts>`

Exportování přiznání k DPH
--------------------------

Pro vývoz SAF-T reportu přejděte na: „Účetnictví –> Zprávy –> Obecný účetní deník“. Klikněte
vpravo od tlačítka „PDF“ a vyberte „SAF-T“.

.. obrázek: austria/austria-saft-button.png
:alt: Tlačítko pro export souboru ve formátu XML
