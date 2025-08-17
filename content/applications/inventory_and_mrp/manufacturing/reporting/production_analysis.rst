===================
Analýza výroby
===================

.. |MO| nahradit za: zkratka: `MO (manufacturing order)`
.. |MOs| nahradit za: zkratka: `MOs (manufacturing orders)`

Zpráva „Analýza výroby“ poskytuje statistiky o produktech vyrobených pomocí Odoo.
Aplikace „Výroba“. Zpráva je užitečná při pokusu porozumět výrobním nákladům a výrobě.
době trvání a dalších důležitých statistikách o výrobcích.

Pro otevření výrobního analytického reportu přejděte na: „Výroba -> Analytika
--> Analýza výroby“.

.. důležité::
Zpráva „Analýza výroby“ je jednou z mnoha dostupných zpráv v rámci aplikace Odoo.
Suite. Tato dokumentace pokrývá pouze opatření specifická pro :guilabel:`Produkční
Analýza včetně několika příkladů použití.

Pro kompletní přehled základních funkcí dostupných v většině zpráv Odoo se podívejte na dokumentaci
na stránce „základní zprávy“ na adrese https://www.essentials.com/reporting/.

Opatření
========

Měřítka jsou sady dat, které lze vybrat v zprávě „Analýza výroby“. Každé
Dataset představuje konkrétní statistiku o |MOs| v databázi. Vyberte měřítko kliknutím
tlačítko „Měření“ a vybrat jednu z možností.
kliknutím na položku nabídky:

Možnosti zobrazené v rozbalovací nabídce Mezery (viz ikona :guilabel:`Measures` :icon:`fa-caret-down`)
pořadí, v jakém se zobrazují, závisí na filtrech, skupinách a srovnáních povolovaných v
Vyhledávací lišta „Hledat…“. Výchozí měřítko je následující:

- :guilabel:`Průměrná cena za zaměstnance na jednotku výroby“: průměrné náklady, které jsou vynaloženy na jednu jednotku produkce.
produktu.
- :guilabel:Celkové náklady na vedlejší produkty výroby“: celkový počet všech vedlejších produktů vzniklých při výrobě
produktu.
- :guilabel:`Náklady na jednotku“: průměrné náklady na komponenty potřebné k výrobě jednoho kusu
výrobku.
- :guilabel:`Náklady na jednotku“: průměrné náklady na výrobu jednoho kusu produktu včetně součástek
zaměstnanci, provozní náklady a náklady na poddodavatele.
- :guilabel:`Doba trvání operací/jednotka“: průměrná celková doba potřebná k provedení
produkovat jednotku produktu.
- :guilabel:`Požadované množství“: celkový počet jednotek výrobku zahrnutých v |MOs|.
- :guilabel:`Počet vyrobených kusů“: celkový počet jednotek produktu, které byly ve skutečnosti vyrobeny.
Vyrobeno.
- :guilabel:`Celkové náklady na komponenty“: celková částka vynaložená na komponenty produktu
|MO| pro výrobek.
- :guilabel:`Celkové náklady“: celková částka, kterou bylo zapotřebí vynaložit na výrobu jednotlivého kusu produktu.
daleko.
- :guilabel:`Doba trvání operací“: celková doba všech operací
při výrobě produktu.
- :guilabel:`Celkové náklady na zaměstnance“: celková částka, kterou společnost zaplatila svým zaměstnancům za výrobu
produktu.
- :guilabel:`Celkové náklady na provoz“: součet všech výdajů spojených s provozem, které jsou potřeba k produkci
produktu.
- :guilabel:`Náklady na celkovou operaci/jednotka“: průměrné náklady operací potřebných k výrobě jednoho
jednotka produktu.
- :guilabel:`Celkové náklady na poddodavatele“: součet částek, které byly zaplaceny dodavatelům za účelem výroby
produktu.
- :guilabel:`Celkové náklady na poddodavatele/jednotka“: průměrné náklady na zapojení
produkovat jednotku produktu.
- :guilabel:`Procento výnosu (%)“: celkové množství produktu vyrobeného ve srovnání s celkovým
poptávané množství, vyjádřené jako procento.
- :guilabel:`Počet produktů“: celkový počet vytvořených |MOs| pro tento produkt.

..tip:
Můžete vybrat pouze jednu metriku najednou, když je aktivní ikona :icon:`fa-area-chart`.
:guilabel:`(zobrazení grafu)` možnost je zapnuta. Několik měření a různé skupinování
kritéria (na ose x a y) lze vybrat při použití ikonky :icon:`oi-view-pivot`.
:guilabel:`(tabulka přehledů)“.

Příklad použití: porovnání produktů
==========================

Jedním z nejlepších způsobů využití zprávy „Analýza produkce“ je porovnání statistik o
dva nebo více produktů. Toho je dosaženo vložením produktů do pole „Hledat…“
baru, vyberte potřebný měrný údaj, filtr a skupinu, abyste viděli požadovaná data.

Příklad:
Společnost Tommy's Toys, která vyrábí hračky, se snaží snížit náklady na výrobu.
Aby dosáhli tohoto cíle, rozhodli se identifikovat zbytečné produkty a přestat je vyrábět.
s vyššími provozními náklady.

Dvě hračky, které byly vybrány pro analýzu, jsou pogo stick a moon shoes.
Tommy's Toys věří, že tyto dva hračky jsou natolik podobné, že mohou přestat vyrábět jednu z nich bez
významně ovlivňuje jejich produktovou nabídku.

Mike, analytik podnikání, otevře náklady na provoz hraček.
:menuselection:`Výroba“ aplikaci a přejde na stránku „Analýza výroby“.
v poli „Hledat…“, zadává názvy obou výrobků a poté otevře
Vyhledávací liště „Hledat…“ a klikne na „Produkt“ v seznamu „Skupina“.
Byla to sekce.

Pod tlačítkem „Hledat…“ klikne na „Měření“.
:ikonou „svislá čára“ a vybírá položku „Celkové náklady na jednotku“.
Poté si vybere možnost „:icon:`fa-bar-chart`“ (graf typu „:guilabel:`bar chart““)

S těmito volbami vybranými se v zprávě „Analýza výroby“ zobrazí graf svislých čar.
v aktuálním roce, s jednou čárou pro každý produkt, který znázorňuje průměrné náklady na jednotku
výrobku.

Mike díky těmto datům zjistil, že průměrná nákladovost na výrobu lunárních bot je téměř
celkově dvakrát vyšší než cena hopsadla. Na základě této informace se Tommy's Toys rozhodne přestat vyrábět
Výroba bot na měsíc je levnější než výroba běžných bot.

.... obrázek::production_analysis/use-case.png
:srovnání: do středu
:alt:Graf porovnávající náklady na provoz hopsadla a měsíčních bot.

Příklad použití: porovnání časových období
==============================

Zpráva „Analýza výroby“ může být také použita k porovnání dat pro dvě různé časové období.
periody. To je dosaženo pomocí možností v sekci „Srovnání“ v
:guilabel:„Hledat…“ lišta.

Příklad:
Společnost *Fanny's Furnishings* chce porovnat náklady na výrobu za první a druhé čtvrtletí.
druhém čtvrtletí roku 2024, aby zjistili, které produkty nejvíce utratily za jejich výrobu.
čtvrtletí.

Pro porovnání obou časových úseků otevře prodejnu šéf Adam.
:menu:Výroba`, a přejde na stránku „Analýza výroby“.
začíná výběrem grafu „Kruh“ (pie chart) v horní části
stránky.

...... důležité::
Funkce „Srovnání“ je určena k použití s ikonou „Pie Chart“.
grafu typu „kruhová grafika“ nebo „převrácený graf“.

Možnost „Srovnání“ lze stále vybrat s ostatními typy zobrazení zapnutými, ale
takto provedené změny neovlivní způsob zobrazení dat na výkazu.

Adam si vybere možnost „Celkové náklady“ z nabídky „Měřítka“.
:ikonou „fa-caret-down“ rozbalovací nabídku, která zobrazuje celkové náklady na výrobu každého produktu.
produktu.

V rozbalovacím seznamu v poli „Hledat…“ nechává zapnutý filtr „2024“.
sekci „Datum ukončení“ a aktivuje filtr „Q2“. S oběma dvěma
Tyto časové úseky byly vybrány, takže graf slouží k zobrazení dat za druhé čtvrtletí roku 2024.

Adam nakonec vybere možnost „Konec období: Předchozí období“.
:guilabel:`Srovnání“ sekce v liště „Hledat…“. To způsobí, že graf bude
Bylo by možné je rozdělit na vnitřní kruh a vnější prstenec.

Vnější prstenec ukazuje data za zvolené období, tedy druhé čtvrtletí roku 2024. Vnitřní kruh
Zobrazuje údaje za předchozí období, tedy první čtvrtletí roku 2024.

....... poznámka::
Pokud je vybrána možnost „Datum ukončení: Předchozí rok“ místo „Datum ukončení: Předchozí měsíc“,
Období, vnitřní kruh zobrazuje data pro vybrané období, jeden rok zpět.

V tomto případě by se zobrazily údaje za druhé čtvrtletí roku 2023.

Adamovi tento report ukáže, že produkty s nejvyšší celkovou cenou za čtvrté čtvrtletí jsou
*kolo* a *trojkolka*. Na druhou stranu v prvním čtvrtletí měly největší nárůst prodeje *in-line brusle*.
nejvyšší celkové náklady.

.... obrázek:: výroba/srovnání.png
:srovnání: do středu
:alt: Zobrazení grafu v podobě koláče pro zprávu Analýza výroby s filtrem porovnání zapnutým.
