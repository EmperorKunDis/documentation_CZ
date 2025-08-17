===============
Součásti nemovitosti
===============

Vlastnosti objektu, nebo vlastnosti, umožňují přizpůsobit formulář:ref:`
<studia/zobrazení/obecné/formulář> přidáním různých typů pole :ref:`<vlastnost_pole/přidat>`.
Pole umožňují ukládání a správu informací přidáním hodnot.

... varování: Vlastnosti versus obyčejné pole

Vlastnosti fungují jako pseudofelda, chovají se jako běžné pole, ale nejsou uložené v sloupcích
databáze. Na ně také odkazují definované :ref:`rodičovské záznamy <property-fields/properties-apps>“.

...... příklad::
Přidání vlastnosti do úkolu vloží pole do všech úkolů, které jsou uvnitř stejného
projekt* a úkoly ostatních projektů zůstanou nedotčeny.

.._vlastnost_pole/přidat:

Přidejte pole vlastností
-------------------

Chcete-li přidat první pole vlastnosti do formuláře, klikněte na
Poté vyberte ikonu „Akce“ (ikona „Kolečko“) a zvolte „Přidat vlastnosti“ (ikona „Nástroje“).

V okně pop-up zadejte název nemovitosti, vyberte typ pole (například „Text“ nebo „Číslo“) a poté
konfigurovat pole podle vybraného typu:

.. seznam tabulkový::
:hlavičkové řádky: 1
:šířky: 15 30 55

   * – pole typu
     - Použití
     - Možnosti
   * :- Text:ref:`<studio/fields/simple-fields-text>`
     - Krátký text na jediné řádce
     - Zadejte hodnotu výchozího nastavení, pokud chcete.
   * – :ref:`Záložka <studia/pole/jednoduché_pole_záložka>`
     - Zkontrolovaný nebo nezkontrolovaný stav
     - Vyberte stát „Výchozí“.
   * – :ref:`Číslo <studio/fields/simple-fields-number>`
     - Číselné hodnoty (definice: „kladná, záporná nebo nula bez desetinné čárky“)
     - Zadejte hodnotu výchozího nastavení, pokud chcete.
   * – :ref:`Desetinné číslo <studio/fields/simple-fields-decimal>`
     - Desetinná čísla (dfn:„kladná, záporná nebo nula s desetinnou čárkou“)
     - Zadejte hodnotu výchozího nastavení, pokud chcete.
   * Datum:ref:`<studia/pole/jednoduché-pole-datum>`
     - Vybrat datum v kalendáři
     - Vyberte požadovanou hodnotu „Výchozí“.
   * – :ref:`Datum a čas <studia/poli/jednoduché-pole-datum-cas>`
     - Vybrat datum v kalendáři a čas na hodinách
     - Vyberte požadovanou hodnotu „Výchozí“.
   * – :ref:`Výběr <studia/pole/jednoduché-pole-výběr>`
     - Výběr hodnoty z předdefinovaného výčtu
     - Přidejte možnost výběru kliknutím na ikonu :icon:`fa-plus` a zadejte
:guilabel:`Název možnosti“.

Pokud chcete, nastavte možnost jako výchozí volbu kliknutím na ikonu
tlačítko pro výběr výchozího nastavení.

Přesunout možnosti tahem a pádem pomocí ikony :icon:`oi-draggable`.
tlačítko s popisem „táhlo“.

Odstranit možnost kliknutím na tlačítko s ikonou „odpadkový koš“ (guilabel: Odstranit vlastnost).
   * – :ref:`Štítky <studia/pole/vztahová-pole-štítky>`
     - Výběr více hodnot ve formě štítků
     - Zadejte název štítku a stiskněte klávesu Enter, abyste jej uložili.

Změňte barvu štítku kliknutím na něj a výběrem jiného.
   * :-:ref:`Mnoho k jednomu <studio/fields/relational-fields-many2one>“
     - Vybrání jednoho záznamu z jiného modelu
     - Zadejte název modelu. Konfigurujte jeho doménu podle návodu v části „Vlastní filtry“
filtrovat záznamy, pokud je potřeba.

Vyberte, pokud chcete, hodnotu výchozího nastavení.
   * :-:ref:`Mnoho k mnohu <studijní/pole/vztahová pole – mnoho k mnohu>`
     - Vybrání více záznamů z jiného modelu
     - Zadejte název modelu. Konfigurujte jeho doménu podle návodu v části „Vlastní filtry“
filtrovat záznamy, pokud je potřeba.

Vyberte, pokud chcete, hodnotu výchozího nastavení.
   * --:separator:
     - Spojte několik vlastností pod skládací štítkem
     -

Klikněte mimo okno připnuté lišty, abyste uložili novou vlastnost.

.. poznámka::
   - Zvolte, zda chcete vlastnost zobrazit v kartách pro kanban, seznam nebo kalendář.
pole s možností zobrazení v kartách.
   - Chcete-li přidat další vlastnost, klikněte na ikonu :icon:`fa-plus` vedle tlačítka
v režimu „Přidat vlastnosti“ (v ikoně „fa-cogs“).

.. tip::
Chcete-li upravit existující vlastnost, přejeďte kurzorem nad ní:

   - Klikněte na tlačítko „Plnicí pero“ (použijte klávesovou zkratku Ctrl+Shift+P) pro otevření okna s přehledem a upravit
vlastnost. V okně přesunu myší klikněte na ikonku „nahoru“ (:icon:`fa-chevron-up`) nebo „dolů“
(dolů) šipku dolů pro posun vlastnosti nahoru nebo dolů.
   - Klikněte na ikonu „Odpadkový koš“, pak na „Smazat“ a poté na „Smazat“.
vlastnictví je trvalé.
   - Použijte ikonu „OI-Draggable“ („páčka pro přetahování“) k přetažení vlastnosti.
přeorganizovat nebo přeskupit.

.._vlastní pole/vlastnosti aplikace:

Vlastnosti mezi aplikacemi
----------------------

Vlastnosti objektu lze definovat v formuláři ve výhledu „Formulář“ (viz. studio/views/general/form).
modelů. Jakmile je vlastnost nastavena, sdílí ji všechny záznamy spojené se stejným „rodičem“.

... seznamová tabulka::
:šířky: 20 40 40
:hlavičkové řádky: 1
:sloupek: 1

        * - Aplikace
          - Model
          - Rodič
        * --:guilabel:`Účetnictví“
          - :ref:`Příjem a rozpoznání aktiv <vytvoření vstupu o příjmech a rozpoznání aktivit>`

:doc:`Půjčka </aplikace/finance/účetnictví/banka/půjčky>`
          - :ref:`Model aktiv <aktiva/model-aktiv>`

:ref:`Časopis <cheat_sheet/journals>`
        * --:guilabel:`Ocenění“
          - :ref:`Hodnocení zaměstnanců <hodnoceni/manual>`
          - :ref:`Oddělení <zaměstnanci/vytvořit-oddeleni>`
        * :- guilabel:"CRM"
          - :doc:`Vedení / příležitost </applications/sales/crm/acquire_leads/email_manual>`
          - :ref:`Prodejní tým <crm/sales-team-dashboard>`
        * – :guilabel:Zaměstnanci
          - :ref:`Zaměstnanec <employees/general-info>`
          - Společnost:ref:`<zaměstnanci/obecné informace>`
        * :- guilabel:Akce
          - :doc:`Registrace na akci </aplikace/marketing/akce/registrace_na_akci>`
          - :ref:`Událost <events/new-event>`
        * :- guilabel:flotila
          - :doc:`Vozidlo </aplikace/hr/flotila/nové vozidlo>`
          - :ref:`Model vozidla <fleet/add-model>`
        * :-:frontdesk
          - :ref:`Návštěvníci na recepci <frontdesk/list>`
          - :ref:`Stanice <frontdesk/stations>`
        * -- :guilabel:`Pomocná služba“
          - :ref:`Lístek <helpdesk/follow>`
          - :ref:`Tým Helpdesku <helpdesk/create-team>`
        * -- :inventar:
          - :ref:`Skladová položka/Sériové číslo <Inventář/Produktový management/Upravit skladovou položku/Sériové číslo>“

:doc:`Převod


:ref:`Přeprava v balíčku <inventář/různé/přeprava v balíčku>“
          - :ref:`Varianta produktu <produkty/přidat-varianty-produktů>`

:ref:`Typ operace <inventar/produktverwaltung/operation-type-setting>`

:ref:`Typ operace <inventar/produktverwaltung/operation-type-setting>`
        * --:knowledge
          - :ref:`Článek znalostí <knowledge/articles_editing/create-article>`
          - :ref:`Rodičovská stránka <knowledge/articles_editing/create-article>`
        * :-:údržba
          - :ref:`Údržba <údržba/správa_vybavení/přidat_nové_vybavení>`
          - :ref:`Kategorie vybavení <údržba/správa vybavení/přidat nové vybavení>`
        * – :guilabel:`Zasedací místnosti“
          - Pokoj
          - Kancelář
        * -- :guilabel:`Plánování“
          - :ref:`Přesunutí <plánování/rolech>`
          - :ref:`Rolí <planning/roles>`
        * -- :guilabel:`Projekt“ / :guilabel:"Služba v terénu"
          - :ref:`Úkol <vytváření úkolů/konfigurace úkolu>`
          - :ref:`Projekt <projektové řízení/konfigurace>`
        * – :guilabel:Nábor
          - :ref:`Uchazeč <nastavení/rychlé přidání uchazeče>`

:ref:`Pozice v zaměstnání <pracovní příležitosti/nová pracovní pozice/edit>

Kandidát
          - :ref:`Pracovní pozice <job-position/create-job-position>`

:ref:`Společnost <general/companies/company>`

:ref:`Společnost <general/companies/company>`
        * --:repair
          - :ref:`Oprava <opravy/opravy/oprava>`
          - :ref:`Společnost <general/companies/company>`
        * --:guilabel:Prodej/atd.
          - Produkt
          - Kategorie
