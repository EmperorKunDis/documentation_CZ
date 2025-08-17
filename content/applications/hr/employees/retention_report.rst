=========================
Zpráva o udržení zaměstnanců
=========================

Možnost určit míru udržitelnosti pro společnost lze získat pomocí modifikace stávajícího reportu.

Nejprve přejděte na: `Zaměstnanci -> Zprávy -> Smlouvy`.
Zpráva „Analýza zaměstnanců“. Tato zpráva ukazuje počet všech zaměstnanců za
„Posledních 365 dní“, v základním „Svislý graf“.

.. obrázek: retention_report/employees-analysis.png
:align:center
:alt: Základní výstup z analýzy zaměstnanců.

Dále klikněte na tlačítko „Měření“ v horním levém rohu.
zobrazí se nabídka. Klikněte na položku „Odjezd zaměstnance“ v seznamu, pak klikněte pryč
záložku pro její zavření. Nyní se v ní objevují všichni zaměstnanci, kteří byli archivováni za
:guilabel:`Poslední 365 dnů“.

Pro zobrazení informací v jednodušším formátu klikněte na ikonku „OI View Pivot“ (Pivot).
ikonou v pravém horním rohu a daty jsou prezentovány ve sloupcovém grafu.

Různé zaměstnanci, uspořádaní podle oddělení, vyplňují řádky. Sloupce zobrazují následující
celkem: měsíční plat, rozpočet na pohonné hmoty, celkový roční
Rozpočet zaměstnance (někdy také nazývaný „roční plat“) a počet nových zaměstnanců.
a počet zaměstnanců, kteří odešli („odcházející zaměstnanci“).

.. obrázek: retention_report/pivot-departures.png
:align:center
:alt:Zpráva o analýze zaměstnanců upravená tak, aby zobrazovala pouze odcházející zaměstnance.

Srovnávací zpráva o míře udržení zaměstnanců
=========================================

Srovnání dat je možné pouze u zaměstnanců, kteří odešli, v porovnání s celkovým počtem současných zaměstnanců.
mezi dvěma samostatnými časovými obdobími. Toto se obecně označuje jako *sazba zaměstnanecké udržitelnosti*.

Pro zobrazení těchto metrik nejprve otevřete zprávu „Analýza zaměstnanců“ kliknutím na
:menu_vyber->Zaměstnanci-->Hlášení-->Smlouvy. Klikněte na ikonu
:guilabel:`(Pivot)` ikona v pravém horním rohu pro zobrazení informací ve sloupcovém grafu.

Dále klikněte na tlačítko „Měření“ v horním levém rohu.
zobrazuje se vyskakovací nabídka. Klikněte na „Noví zaměstnanci“, „Rozpočet pro zaměstnance za rok“
„Karta paliva“, „Mzda“ v seznamu a odškrtnout tyto metriky a skrýt je.
tabulku. Pak klikněte na položku „Počet“ v seznamu níže a zapněte tento ukazatel.

Klikněte mimo rozbalovací nabídku, aby se zavřela. Nyní je v reportu uvedeno všechny zaměstnance, kteří opustili
společnosti (viz. štítek #Odchod zaměstnance), stejně jako celkový počet zaměstnanců
(:guilabel:'Počet'), pro posledních 365 dní.

Pro porovnání dat za aktuální rok s předchozím rokem klikněte na ikonku :icon:`fa-caret-down`.
:guilabel:„(svislá šipka)“ v poli vyhledávání, což odhalí několik možností filtrování a seskupování. Klikněte
„Posledních 365 dní“ v sloupci „Filtry“ pomocí ikony „Filtrů“, abyste
Poté klikněte na filtr „Datum“ a vyberte aktuální rok (v tomto případě „2024“).
z výsledného seznamu.

Jednou z možností je výběr pod :guilabel:`Datum` v :icon:`fa-filter` :guilabel:`Filtru`
sloupec, který se zobrazí po kliknutí na ikonu „Nastavení“ (viz obrázek).
Rok v nové sloupci a pak klikněte mimo rozbalovací nabídku, abyste ji zavřeli.

.. poznámka::
V Odoo je k přístupu do sloupce „Srovnání“ potřeba konkrétní čas.
*kromě* :guilabel:`Poslední 365 dnů` **musí být vybrána*. Pokud ne, musí být vybrán :icon:`fa-adjust
:guilabel:`Srovnání“ sloupec není viditelný.

Nyní se v tabulce otočení zobrazuje celkový počet zaměstnanců, kteří opustili společnost (:guilabel:"
Zaměstnanci odcházející do důchodu“), stejně jako celkový počet zaměstnanců („Počet zaměstnanců“) v sloupcích.
Tyto jsou dále rozděleny do dvou různých let a také zobrazuje :guilabel:`Variantu`.
mezi nimi.

Řádky zobrazují oddělení a u každého zaměstnance v daném oddělení jsou uvedeny jeho jméno a funkce.
řádky.

Pro zobrazení celého článku klikněte na ikonu :icon:`fa-minus-square-o` :guilabel:`Celý článek` nad
v horní řadě odborů a zaměstnanců, aby se snížily řádky. Nyní tabulka ukazuje celkový
počet zaměstnanců, kteří společnost opustili za oba roky, v poměru k celkovému počtu zaměstnanců
včetně rozdílu v procentech za oba roky.

.. příklad::
V tomto případě z pracovních míst odejdou v roce 2023 tři zaměstnanci z celkového počtu osmi.
zaměstnanců do roku 2024, což představuje zvýšení o :guilabel:`166,67 %`.
pracovníků, kteří odešli v roce 2024 ve srovnání s rokem 2023. Dále zde byl zaznamenán nárůst o :guilabel:`143.37 %`
nárůst celkového počtu zaměstnanců v roce 2024 ve srovnání s rokem 2023.

.... obrázek: retention_report/comparison-years.png
:align:center
:alt:Zpráva upravena tak, aby ukázala rozdíl mezi dvěma roky zaměstnanců, kteří odešli.

Pro zobrazení podrobnějších sazeb pro každý oddělení klikněte na ikonu „+“ vedle položky
jedna řádka, která odhaluje rozbalovací nabídku, a klikněte na položku „Oddělení“. Klikněte mimo
položku „Zavřít“ a nyní se v tabulce sestupně řadí všichni zaměstnanci, kteří odešli.
(:guilabel:'# Odchod zaměstnance'), celkový počet zaměstnanců (:guilabel:'Počet') a
„Varianta“ (v procentech) pro rok 2023 i 2024, rozdělené podle oddělení.

.. příklad::
V tomto příkladu lze určit, že oddělení „Management“ mělo nejlepší výsledky.
úroveň udržení v roce 2024 oproti roku 2023 s hodnotou „Variation“
:guilabel:`-100 %“. Dále lze zjistit, že :guilabel:`Vedení / Výzkum a vývoj“
Největší obrat měla divize „Rozvoj“, kde se projevil výkyv o 300 %.

.... obrázek:: retention_report/department-totals.png
:synchronizace: střed
:alt: Rozšířený výkaz o udržení zaměstnanců podle oddělení.
