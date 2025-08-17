===============
Analyzujte metriky
===============

.. |CTR| nahradit za: zkratku: CTR (procento kliknutí)

Abychom mohli správně pochopit úspěch nebo neúspěch e-mailového marketingu, je
monitorovat několik klíčových metrik. Získané poznatky z těchto metrik lze potom využít k
optimální nastavení budoucích kampaní. Aplikace Email Marketing společnosti Odoo sleduje několik klíčových metrik:
<email-marketing/view-metrics>“, které lze vyložit prostřednictvím zpráv
Zlepšit budoucí kampaně.

.._email-marketing/zobrazit-metriky:

Zobrazit metriky
============

Po odeslání hromadné zprávy se vám zobrazí výsledky právě pro tuto kampaň.
lokalit.

Pro zobrazení metrik pro jednotlivou kampaň přejděte do aplikace „E-mailový marketing“ na adrese:
-->Příspěvky do diskuse“. Najděte konkrétní příspěvek v seznamovém pohledu a použijte hlavičky sloupců k zobrazení
výsledky dané kampaně. Kliknutím na jednu z kampaní v seznamu otevřete záznam.

Na vrcholu záznamu jsou zobrazené podrobné metriky jako chytré tlačítko.

.. obrázek:analyze_metrics/metric-smart-buttons.png
:align:center
:alt:Chytré tlačítko v masovém mailingu zobrazující výsledky zprávy.

Otevřená sazba
-----------

Procento otevřených e-mailů adresátem v porovnání s celkovým počtem odeslaných e-mailů.

V případě odpovědi, jako je například chladné oslovení e-mailem, vysoká míra otevření může znamenat
předmět zprávy byl včasný, poutavý a úspěšně vyzval příjemce k prohlížení zprávy.

Pokud se neočekává odpověď, například u propagačních e-mailů, může to naznačovat problém s
e-mailu, například špatné odkaz na produkt nebo kuponový kód.

Pokud se očekává odpověď, nízký počet otevřených e-mailů může naznačovat, že je problém v předmětu.
linka nezaujala příjemce nebo zpráva skončila ve složce Spam nebo Nevyžádaná pošta.
Mohlo by také znamenat, že e-mail skončil ve složce s nevyžádanou poštou.

.. poznámka::
E-maily, které se pravidelně dostanou do složky Spam u příjemce, mohou být způsobeny špatným odesílatelem
reputace (tj. vysoký podíl odhlášených uživatelů, vysoký podíl minulých e-mailů označených jako spam atd.)
nebo nekonfigurovat správné záznamy v systému DNS
<../../obecne/komunikace_e-mailem/domena_pro_e-mail>.

Odpovědní sazba
------------

Procento příjemců, kteří odpověděli na e-mail, v poměru k celkovému počtu zaslaných e-mailů.

Vysoká míra odezvy může naznačovat, že e-mail rezonoval s příjemci a vyvolal u nich potřebu zaslat odpověď.
akci nebo zpětnou vazbu.

Nízký podíl odpovědí může naznačovat, že zpráva nebyla relevantní nebo obsahovala nepřesné informace.
volání k akci.

Kliknutí na sazbu
------------

Tento ukazatel představuje Click-through rate (CTR), který měří
procento příjemců, kteří na odkaz v e-mailu klikli, oproti celkovému počtu zaslaných
e-maily.

Vysoká míra CTR může naznačovat, že obsah e-mailu byl relevantní a cílený správným způsobem.
byli motivováni kliknout na odkazy poskytnuté a pravděpodobně si obsah užili.

Nízká míra CTR může naznačovat problémy s cílením nebo obsahem samotným.
byli nezaujatí k volání k akci nebo samotnému sdělení.
byla směrována na špatnou cílovou skupinu.

Příjemná míra
-------------

Tento poměr měří procento e-mailů, které byly **úspěšně doručeny**, v porovnání s celkovým počtem
Počet odeslaných e-mailů.

Vysoká míra otevřených zpráv může naznačovat, že seznam adresátů je aktuální a ověření odesílatele
je důvěryhodný pro poskytovatele e-mailových služeb.

Nízká míra otevřených e-mailů může naznačovat problémy s poštovní adresou nebo se samotným
ověření odesílatele. Podrobnější informace naleznete v části :ref:`email-marketing/deliverability-issues`.
informace.

Odmítnutá sazba
------------

Tento poměr měří procento e-mailů, které byly **neúspěšně** doručeny a nedorazily
dorazit do schránky příjemce, vzhledem k celkovému počtu odeslaných e-mailů.

Vysoká míra odrazů může naznačovat problémy, ať už s použitou databází pro rozesílání nebo se
ověření odesílatele.

Nízká míra odrazů může naznačovat, že seznam e-mailových adres použitý je aktuální a poskytuje správné informace.
autentizace je důvěryhodná u poskytovatelů e-mailových služeb. Podívejte se na :ref:`e-mailový marketing/dodací problémy`.
pro další informace.

..tip:
Klikněte na příslušné chytré tlačítko, abyste viděli všechny odpovídající záznamy příjemců.
přičítat každému metriku. Když jsou tyto filtrované záznamy viditelné, lze vytvářet různé typy zpráv.
bude dále analyzován.

.._email_marketing/vytvorit_zpravy:

Vytvářejte reporty o metrikách
======================

Individuální metriky lze analyzovat vytvořením zprávy. Nejprve klikněte na chytrý tlačítko
požadovaný metrický ukazatel.

Dále klikněte na ikonu „fa-caret-down“ vedle vyhledávací lišty a zobrazí se
rozbalovací nabídka filtračních a seskupovacích parametrů.

V levém sloupci možností vyhledávání se nachází filtry „Filtr“, které lze použít k tomu, aby se zobrazily jen
výsledky odpovídající filtru. Například výběr filtru *Zpětné adresy* zobrazí pouze e-maily
které nelze dodat.

:guilabel:'Skupina', nacházející se ve střední sloupci, je používána k uspořádání výsledků do skupin.
Může být použita s filtry nebo bez nich.

.. poznámka::
Zadání více možností „Skupina“ vytváří podskupiny dle zvolené možnosti
je vybrán jako první. Například výběrem položky :guilabel:`Sent Period“ a poté
:guilabel:`Přidat vlastní skupinu --> Zodpovědná osoba“, ve sloupci „Skupina“ seřadí všechny
výsledky seřadit nejprve podle zaslaného období a poté podle člena týmu, který byl za ně zodpovědný.
metrika pro analýzu, kdo z týmu v daném časovém období odešle největší objem nebo množství.

Vyhodnocení je možné na základě pohledu na směr a pořadí výběru v skupinovém panelu.
která se objeví v hledací liště po provedení výběru.

Příklad:
Byl rozeslán měsíční newsletter a 6,9 % odeslaných e-mailů se vrátilo zpět.

.... obrázek:analyze_metrics/newsletter-metrics.png
:synchronizace: střed
:alt:Chytré tlačítko v měřítku zprávy.

Pro zjištění, co mají společného tyto odražené příjemce, jsou záznamy seskupeny pomocí vlastního skupinového řazení
cílení na záznamy s názvem „Seznamovací e-mail“, které seřazují všechny záznamy podle mailových listů, na kterých jsou.
Poté jsou záznamy filtrovány pomocí vlastního filtru s pravidlem „Vytvořeno od 07/01/2024
00:00:00, což je filtr podle posledního kontrolování seznamu. Tento filtr zahrnuje
příjemcům vytvořeným od 1. července 2024 ve zprávě.

....... obrázek:: analyze_metrics/metrics-filter.png
:synchronizace: střed
:alt: Formulář pro vytvoření vlastního filtru.

Použitím těchto konfigurací je zřejmé, že všechny příjemce s vrácenými e-maily byly přidány
Po poslední kontrole seznamu je zřejmé, že u domén je patrné, že každá
příjemce má špatně vytvořenou e-mailovou doménu (např. @yaoo.com místo @yahoo.com), což je pravděpodobně způsobené
chyba při ručním zadávání údajů do databáze.

.. obrázek:: analyze_metrics/malformed-addresses.png
:synchronizace: střed
:alt: Seznam e-mailových adres, které se vrátily s poškozenými doménami.

.. viz též:
Pro více informací o vytváření vlastních skupin se podívejte na stránku:
filtry.

..._marketingem e-mailů/problémy s doručitelností:

Analýza masových e-mailů
=====================

Je také možné analyzovat úspěšnost mezi kampaněmi pomocí vytvoření „Masové pošty“.
Analýza*. Nejprve přejděte do aplikace „E-mailový marketing“ a poté na „Hromadná zpráva“.
Analýza mailingu“.

Na obrazovce se zobrazuje panel s barevnou grafickou škálou obsahující každý e-mailový kampaň.
Vyberte „Odeslané“, zobrazí se počet odeslaných záznamů na ose Y.
měřit, kliknout na tlačítko „Měření“ a vybrat požadované měření z rozevírací nabídky.
menu.

Příklad:
Následující graf ukazuje počet otevřených e-mailů z dvou různých masových rozesílek.

V tomto pohledu je vidět, že první masová kampaň měla vyšší otevřenost než ta druhá.
druhé místo. Někdy totiž může být nižší otevřenost způsobena špatně zvoleným předmětem e-mailu.
zaujmout čtenáře, předmět hromadného e-mailu může být dobrým místem k začátku.
hledajícím.

.... obrázek::analyze_metrics/mma-opened.png
:synchronizace: střed
:alt:Graf ukazující rozdíl otevřenosti mezi dvěma masovými e-mailovými kampaněmi.

Porovnáním obou předmětů je zřejmé, že předmět e-mailu byl méně zajímavý.
Které mohlo vést k nižší otevřenosti v porovnání s jinými masivními e-maily.

.... obrázek::analyze_metrics/mailing-comparison.png
:synchronizace: střed
:alt: alternativní text

Problémy s doručitelností
=====================

Následující definují možné důvody vysoké míry odražených e-mailů nebo nízkého počtu doručených zpráv:

- Používáním seznamu e-mailových adres s neaktuálními kontakty nebo špatně vytvořenými e-mailovými adresami
je pravděpodobné, že vyústí v vysoký odrazový poměr nebo nízkou míru přijetí.
- E-maily zasílané z e-mailové adresy, která se liší od domény odesilatele, jsou pravděpodobně
se vracet zpět u některých poskytovatelů e-mailových služeb kvůli chybějícímu ověření DMARC.
<email-domain-dmarc>.
- Nedodržení správného nastavení záznamů v systému
Používání e-mailové adresy ve tvaru „<adresa@doména>“ může také vést k vysokému počtu odmítnutých zpráv.

.. viz též:
   - :ref:`Marketingové kampaně <email_marketing/marketingove-kampane>`
   - :doc:`Správa odhlášení <unsubscriptions>`
