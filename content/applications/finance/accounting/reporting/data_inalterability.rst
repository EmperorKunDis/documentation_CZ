================================
Zpráva o kontrole nezměnitelnosti dat
================================

Daňové úřady v některých zemích vyžadují, aby společnosti prokázaly, že jejich zaznamenané účetní položky jsou
nezaměnitelné, což znamená, že po získání záznamu již nelze provádět žádné změny.

Protože Odoo vytváří pro každý zabezpečený vstup jedinečný otisk prstu pomocí algoritmu SHA-256, je možné jej používat k ověřování.
Tento otisk prstu se nazývá haš. Haš je vytvořen z klíčových dat záznamu
hodnoty „název“, „datum“, „časopis“, „firma“, „pohyb kreditu“, „pohyb debetu“, „účet“ a
(pole „partner_id“), přičemž je k sobě připojí a vloží do funkce SHA-256, která pak
výstup je pevnou délkou (256 bitů). Hashovací funkce je deterministická (:dfn:`deterministic
stejný vstup vždy vytvoří stejný výstup“): jakákoliv drobná úprava původních dat by
Změnit výsledný haš. Proto se často používá algoritmus SHA-256.
dalším pro ověření integritních dat.

Dále je k předchozímu záznamu přidán i jeho hash, čímž se vytvoří **šifrovací řetězec**.
Tento je používán k zajištění, aby se později nezobrazil nový záznam mezi dvěma zabezpečenými záznamy.
by narušila řetězec hašůvání.

.. poznámka::
Hashy vypočítané algoritmem SHA-256 jsou teoreticky nejedinečné, protože existuje omezený počet
Počet možných hodnot je však vysoký: 2²⁵⁶, což je opravdu mnoho
větší než počet atomů ve známém vesmíru. Proto se hašovací funkce považují za jedinečné
v praxi.

.. _data-inalterability/inalterability_features:

Vlastnosti nezměnitelnosti
=======================

Funkce nezměnitelnosti lze aktivovat zapnutím funkce „bezpečného vkládání s hašováním“
Možnost „Nepřenositelná“ nebo „Omezená“ na jakémkoliv časopise nebo pomocí bezpečného vstupu do systému.
<data-inalterability/wizard>“.

- Do formuláře záznamu se přidají dva indikátory.
Ukazují, zda je vstup ostražený či nikoliv.

  - Ikona „zamknutí“ nebo „odblokování“ (ikona „zámečku“) vedle stavu „Odesláno“.
  - Zatrhnutí položky „Zabezpečeno“ v záložce „Další informace“.

- Filtr „Nezabezpečeno“ je k dispozici v zobrazení seznamu položek a zápisů.
Může se použít k vyhledání zápisů v deníku, které ještě nebyly zabezpečeny.
- Možnost otevřít dialogové okno pro zabezpečené vstupy je zobrazena na
:guilabel:`Účetnictví“ nabídka.

.._data-inalterability/restricted:

Zabezpečte vložené příspěvky pomocí hašování
===============================

Aby bylo možné aktivovat hashovací funkci na konkrétním účetním deníku, je nutné přejít do sekce „Účetnictví“ ->
Konfigurace --> Účetní deníky. Otevřete prodejní, nákupní nebo smíšený účetní deník a přejděte na
kartě „Pokročilé nastavení“ a zapněte možnost „Zabezpečená zadaná data s hašováním“.
Časopisy, pro které je funkce aktivována, se označují jako „omezené“.

Odoo vypočítá hašovací funkci pro záznam tak, že získá předchůdce v řetězci (tj.
současně s tím, jak se zvyšuje počet záznamů v databázi (tj.
vstup do nového záznamu v hašovací tabulce.

.. varování:
Jakmile vložíte příspěvek do omezeného deníku, nemůžete tuto funkci deaktivovat ani upravit.
jakýkoliv zabezpečený vstup.

.._data-inalterability/wizard:

Průvodce zabezpečenými vstupy
=====================

Můžete také použít nástroj „Bezpečné záznamy“ k zabezpečení všech záznamů v deníku.
v **veškerých** časopisech do určitého data.

.. poznámka::
Kouzelník funguje nezávisle na nastavení časopisu a typu časopisu.

Pro otevření aktivujte režim vývojáře, přejděte do nabídky „Účetnictví“
Účetnictví“ a klikněte na „Zabezpečené vstupy“. Pokud jsou funkce „nezměnitelnosti“
Pokud jsou aktivovány funkce <data-inalterability/inalterability_features>, je také viditelný mimo ladění.
móda.

Zajistit záznamy vyberte datum do kterého by měly být všechny záznamy zajištěny a stiskněte
:guilabel:`Zabezpečené vstupy“.

.. varování:
Po zadání záznamů již nelze provádět další úpravy.

.. poznámka::
Může se stát, že záznamy po vybraném datu jsou zabezpečeny.
To je možné proto, že hash řetězec odpovídá sekvenčnímu předchůdci.
seřazené podle čísla pořadí.

.._data-inalterability/report:

Stáhnout zprávu
===============

Pro stažení zprávy o kontrole nezměnitelnosti dat přejděte na: „Účetnictví - Konfigurace“.
→ Nastavení → Hlášení → Stáhnout zprávu o kontrole nenahraditelnosti dat.

První část zprávy je přehled všech sekvencí předcházejících záznamům, které obsahují hašované položky.
V sloupci „Omezeno“ můžete vidět, zda nebo nezda je časopis :ref:`bezpečný
Příspěvky s možností „<data-inalterability/restricted>“ (V) nebo bez ní (X).
Sloupec „Zkontrolovat“ vám řekne, zda jsou všechny položky správně hašovány.

.. obrázek: data_inalterability/journal-overview.png
:align:center
:alt: Zpráva o konfiguraci pro dva deníky

Druhá část poskytuje podrobnější výsledek kontroly shody dat pro každý hašovaný
sekvence záznamů v novinách. Můžete zobrazit první hašovaný záznam a jeho odpovídající hash.
a také poslední hašovaný záznam a jeho odpovídající hash.

.. obrázek: data_inalterability/data-consistency-check.png
:align:center
:alt: Zpráva o kontrole shody dat pro časopis
