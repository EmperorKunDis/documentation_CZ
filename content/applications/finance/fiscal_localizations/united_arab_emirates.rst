====================
Spojené arabské emiráty
====================

..._uae/instalace:

Instalace
============

Instalujte následující moduly, abyste získali všechny funkce **Spojených arabských emirátů.
Lokální verze Emirates:

.. seznam tabulkový::
:hlavičkové řádky: 1

   * Jméno
     - Technické označení
     - Popis
   * – :guilabel:`Spojené arabské emiráty – Účetnictví“
     - „l10n_ae“
     - Výchozí: balík pro daňovou lokalizaci </aplikace/finance/fiscal_localizations>.
Zahrnuje všechny účty, daně a zprávy.
   * --:guilabel:--U.A.E. - Mzdy
     - „l10n_ae_hr_mzdy“
     - Zahrnuje všechny pravidla, výpočty a struktury mezd.
   * – :guilabel:„Mzdy a účetnictví v SAE“
     - „l10n_ae_hr_mzdy“
     - Zahrnuje všechny účty související s modulem mzdy.
   * – :guilabel:`Spojené arabské emiráty – bod prodeje“
     - „l10n_ae_pos“
     - Zahrnuje účtenku v souladu s požadavky Spojených arabských emirátů.

.. obrázek: united_arab_emirates/l10n-ae-modules.png
:align:center
:alt:Vyberte moduly, které chcete nainstalovat.

.. viz též:
:dokumentace:Lokalizace platů v Spojených arabských emirátech


Klasifikační schéma
=================

Přejděte na:menu:Účetnictví --> Konfigurace --> Skladová kniha, abyste viděli všechny výchozí
účty dostupné pro balíček lokalizace Spojených arabských emirátů. Můžete filtrovat podle pole „Kód“ pomocí
čísla na nejlepší straně nebo kliknutím na: „Skupina podle“ -> „Typ účtu“. Můžete
:guilabel:`Povolit“/:guilabel:`Zakázat“ srovnávání nebo konfigurovat specifické účty podle
Vašim potřebám.

.. důležité::
   - Vždy si udržujte alespoň jeden účet příjmů a jeden účet výdajů aktivní.
   - Je také doporučeno nechat si účty s nízkým zůstatkem aktivní, protože se používají pro přechodné platby.
účty v Odoo nebo jsou specifické pro balíček UAE lokalizace.

..... seznamová tabulka::
:hlavičkové řádky: 1

        * - Kód
          - Název účtu
          - Typ
        * - 102011
          - Příjmy za prodej
          - Přijatá pohledávka
        * - 102012
          - Příjmy z prodeje
          - Přijatá pohledávka
        * - 201002
          - Závazky
          - Vyúčtovatelné
        * - 101004
          - Banka
          - Banka a hotovost
        * - 105001
          - Hotovost
          - Banka a hotovost
        * - 100001
          - Převod likvidity
          - Výchozí aktiva
        * - 101002
          - Významné příjmy
          - Výchozí aktiva
        * - 101003
          - Nedoplatky
          - Výchozí aktiva
        * - 104041
          - DPH vstup
          - Výchozí aktiva
        * - 100103
          - DPH přijatá
          - Nepohyblivé aktiva
        * - 101001
          - Bankovní účet s podezřením
          - Aktuální závazky
        * - 201017
          - DPH výstup
          - Aktuální závazky
        * - 202001
          - Provádění služeb na konci životnosti
          - Aktuální závazky
        * - 202003
          - DPH splatná
          - Ostatní závazky
        * - 999999
          - Nepočítané zisky a ztráty
          - Příjmy za aktuální rok
        * - 400003
          - Základní plat
          - Náklady
        * - 400004
          - Příspěvek na bydlení
          - Náklady
        * - 400005
          - Příspěvek na dopravu
          - Náklady
        * - 400008
          - Výplata odstupného
          - Náklady

Daně
=====

Chcete-li získat přístup k dani, přejděte na: „Účetnictví --> Konfigurace --> Daně“.
Aktivovat nebo deaktivovat, nebo: „Nastavit </applications/finance/accounting/taxes/>“
Daňové položky, které se týkají vašeho podnikání kliknutím na ně. Pamatujte si jen nastavit daňové účty na 5 %
daňová skupina, jako ostatní nepotřebují uzavírat. Proto je zapnutý režim vývojáře
„Vývojářský režim“ a přejděte do „Konfigurace -> Daňové skupiny“. Poté nastavte
„Daňový účet (splatná daň)“, „Daňový účet (příjem daň)“ a
„Předběžná platba daně“ pro skupinu 5 %.

.. poznámka::
Odoo podporuje RCM (Reverse Charge Mechanism).

.. obrázek: united_arab_emirates/uae-localization-taxes.png
:align:center
:alt:Předběžný pohled na daňový balíček pro lokalizaci Spojených arabských emirátů.

Směnné kurzy
=======================

Aktualizovat směnný kurz, přejděte na: „Účetnictví“ > „Konfigurace“ >
Nastavení --> Měny. Klikněte na tlačítko aktualizace (zobrazené jako :guilabel:`↻`) vedle
:guilabel:`Další běh“ pole.

Pro automatické spouštění aktualizace v předem stanovených intervalech změňte hodnotu
:guilabel:`Ručně“ na požadovanou frekvenci.

.. poznámka::
Výchozím je služba burzy centrální banky Spojených arabských emirátů. K dispozici jsou i další poskytovatelé.
jsou k dispozici v poli :guilabel:`Služba`.

Pravidla pro odměňování
------------

Při aplikaci těchto pravidel na pracovní smlouvu přejděte do: „Mzdy --> Smlouvy -->
Smlouvy“ a vyberte smlouvu zaměstnance. V poli „Typ struktury mzdy“ zadejte
vyberte:guilabel:"Zaměstnanec Spojených arabských emirátů".

.. obrázek: united_arab_emirates/uae-localization-salary-structure.png
:align:center
:alt:Vyberte typ platové struktury, která se má použít na smlouvu.

Pod záložkou „Informace o mzdě“ najdete podrobnosti jako například:

- :guilabel:`Mzda“
- „Příspěvek na bydlení“
- „Dopravní příspěvek“
- :guilabel:`Jiné příplatky“
- :guilabel:`Počet dní“: používá se k výpočtu :ref:`poskytování služeb
<ukončení poskytování služeb v UAE>.

.. poznámka::
   - Srážky se vypočítávají podle pravidel spojených s nevyužitým volnem.
typ;
   - Ostatní slevy nebo náhrady se provádějí ručně pomocí jiných vstupů.
   - Přesčasy se přidávají ručně, a to pomocí volby v nabídce „Vstupy práce“ -> „Vstupy práce“.
   - Přílohy k mzdě vytvoříte klepnutím na: „Smlouvy“ -->
Přílohy mzdy“. Poté vytvořte přílohu a vyberte „Zaměstnanec“.
a typu (Přidělení platu, Přiřazení platu, Výživné).

.. tip::
Chcete-li zabránit tomu, aby se pravidlo objevilo na výplatní pásce, přejděte do: `Výplata --> Konfigurace
--> „Pravidla“. Klikněte na „Zaměstnanecký platový systém Spojených arabských emirátů“, vyberte pravidlo pro skrytí a
odebrat zaškrtnutí položky „Zobrazení na výplatní pásce“.

... _uae-end-of-service-provision:

Ukončení poskytování služeb
------------------------

Provize je definována jako celkový měsíční příjem dělený třiceti a následně vynásobený
Počet dnů uvedených v poli „Délka“ na spodní části smlouvy.

Poté se srážka vypočítá podle mzdy, která je spojena s dvěma účty: **Konec
Služba Indemnity (Nákladový účet) a Služba na konci služby (Závazky dlouhodobé)
účet)**. Ten se používá k úhradě **výplaty za odchod do penze**, a to tím, že je s ní vyrovná
účet závazků.

.. poznámka::
Konečná částka za službu se vypočítává z hrubé mzdy a datumů začátku a konce služby.
pracovní smlouvu zaměstnance.

Faktury
--------

Místní balíček Emirátů umožňuje vytvářet faktury v angličtině, arabštině nebo obojím.
lokalizace také obsahuje řádek pro zobrazení částky DPH za jednotlivé řádky.
