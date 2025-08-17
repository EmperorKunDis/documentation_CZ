================
Evoluce dovedností
================

V aplikaci „Ocenění“ od společnosti Odoo je možné sledovat, jak se v čase vyvíjejí dovednosti zaměstnanců.
:report Skills Evolution (též známý jako
*Zpráva o hodnotících dovednostech*.

Manažeři mohou použít tento nástroj k tomu, aby viděli, jak si lidé plní různé cíle v oblasti dovedností stanovené na jejich hodnocení.
kdo splnil termíny svých dovedností, kdo má nejlepší výkon v oblasti rozvoje dovedností a
více.

Ve zprávě *Evoluce dovedností* je také možnost vyhledávat zaměstnance s konkrétními
určitých úrovní, které mohou být užitečné pro scénáře, kde
Pro výkon této funkce je nutné mít určité schopnosti.

..._hodnocení/identifikace dovedností a vývoje:

Zpráva o vývoji dovedností
=======================

Pro přístup k tomuto hlášení o vývoji dovedností se přihlaste na: „Hodnocení zaměstnanců > Zprávy
-->Vývoj dovedností“.

Tímto způsobem se zobrazí stránka „Zpráva o hodnocení dovedností“. Všechny dovednosti jsou seskupeny podle měsíce
Vytvořily se nejprve podle zaměstnance a poté podle typu dovednosti.

.. důležité::
Zpráva o hodnocení dovedností zobrazuje pouze dovednosti zaměstnanců, kteří mají alespoň jednu.
dokončené hodnocení. Zkušenosti zaměstnanců, jejichž hodnocení ještě nebylo dokončeno nebo čeká na vyřízení, se do výpočtu nezapočítávají.
jsou zahrnuty.

Když zaměstnanec dokončí svou první hodnocení, všechny jeho dovednosti se objeví na zprávě.
Pokud je následná hodnocení označena jako dokončená, zobrazí se změny v dovednostech ze starého hodnocení.
zprávu.

Kdykoli dojde ke změně úrovně dovedností z průběžných hodnocení, které nebyly ještě ukončeny, **nejsou**
Tyto informace jsou zahrnuty v této zprávě.

Pro zobrazení konkrétních podrobností o dovednostech zaměstnance rozbalte položku „Zaměstnanec“ a
Rozšířit jednotlivé dovednosti: Skill Types. Každá dovednost zobrazuje následující informace:

- :guilabel:`Zaměstnanec“: jméno zaměstnance.
- :guilabel:`Typ dovednosti“: kategorie, do které spadá dovednost.
- :guilabel:`Skill“: specifická individuální dovednost.
- :guilabel:"Aktuální úroveň": úroveň, kterou zaměstnanec dosáhl pro dovednost.
- :guilabel:`Předchozí pokrok“: procento dosažené kompetence v předchozím čase.
- :guilabel:`Aktuální pokrok“: aktuální procento dosaženého stupně dovednosti v rámci schopnosti.
- :guilabel:`Odkaz na dovednost“: jakákoliv poznámka vložená k dovednosti, která popisuje pokrok.

Barva textu dovednosti ukazuje, zda se od posledního hodnocení něco změnilo. Úroveň dovedností
se od poslední hodnocení zvýšily jsou zobrazeny v zelené barvě jako „Zlepšení“. Úrovně dovedností, které
**nebyly změněny** se zobrazí černou barvou jako „No Change“. Došlo-li ke zpomalení dovedností, objeví se v červené barvě jako
*Zpětná vazba*.

Tento report lze upravit tak, aby obsahoval konkrétní informace, a to pomocí filtrů.
„Vyhledávání“ a „Skupiny“ (viz „Vyhledávací pole nahoře“)

.. obrázek:: skills_evolution/skills-report.png
:alt:Zpráva, která zobrazuje všechny dovednosti seřazené podle zaměstnance.

...hodnocení/identifikace dovedností:

Případ použití: identifikace zaměstnanců s konkrétními dovednostmi
=================================================

Od té doby, co report „Zkušenosti“ organizuje všechny dovednosti podle měsíce, zaměstnance a pracovní pozice, může
je obtížné najít zaměstnance s konkrétními dovednostmi na určité úrovni.
Musí se použít vlastní filtr.

V tomto příkladu je zpráva upravena tak, aby ukázala zaměstnance s odbornou úrovní JavaScriptu.
znalostí. Chcete-li zobrazit pouze zaměstnance, nejprve odstraňte všechny aktivní filtry v hledání.

Dále klikněte na ikonu „fa-caret-down“ (Zobrazit vyhledávací panel) v liště pro vyhledávání, pak
Klikněte na „Přidat vlastní filtr“ pod sloupcem „Filtry“ vedle ikony „fa-filters“.
zobrazit okno „Přidat vlastní filtr“.

V prvním poli vyberte ze seznamu možnost „Schopnost“ a ve druhém pole zadejte
„jako je“ (viz. „je v“) a zvolte „JavaScript“ ze třetího seznamu v
třetí pole.

Dále klikněte na „New Rule“ a další řádek se objeví. V tomto druhém řádku vyberte
„Aktuální úroveň“ pro první pole seznamu, druhé pole nechte takové, jaké je „(je
Vyberte pole „Zkušený“ v třetím seznamovém poli.

Po přidání druhé podmínky se přesuňte na text nahoře okna s upozorněním
:guilabel:`Přesně shodující se s následujícími pravidly“ :icon:`fa-caret-down` :guilabel:`zde“. Klikněte na
menu pro „všechny“ a změnit ho na „vše“.

Konečně klikněte na tlačítko „Přidat“.

.. obrázek:skills_evolution/javascript.png
:alt:Pop-up okno filtru s nastavenými parametry.

Nyní mohou pracovat pouze zaměstnanci s úrovní „Expert“ v dovednosti „JavaScript“.
zobrazit se. V tomto příkladu splňuje tyto požadavky pouze :guilabel:`Marc Demo`.

.. obrázek::skills_evolution/results.png
:alt:Zaměstnanci s odbornými znalostmi v oblasti JavaScriptu.

Případ použití: Hodnocení největšího zlepšení
====================================

Další způsob, jak upravit zprávu o hodnocení dovedností, je identifikace zaměstnance, který má
nejvyšší počet zlepšených dovedností za určité časové období.

Pro zobrazení této informace nejprve odstraňte výchozí filtr v poli vyhledávání. Poté klikněte na
Klikněte na ikonu „fa-caret-down“ v liště vyhledávání a poté
pod ikonou „filtr“ v seznamu „Zlepšení“. Po zapnutí
filtr zobrazuje pouze dovednosti, které se zlepšily.

Je možné zobrazit dovednosti, které se v čase zlepšily, například konkrétní
čtvrtletí nebo měsíce. S rozbaleným vyhledávacím poli klikněte na tlačítko „Přidat vlastní
Vyberte filtr v dolní části sloupce Filtry a klikněte na tlačítko Přidat.
Zobrazí se okno s názvem „Vlastní filtr“.

Vyberte pole „Datum vytvoření“ pro první seznam a poté vyberte možnost „je mezi“.
druhé rozbalovací pole. Jakmile je vybráno „je mezi“, objeví se druhé pole po
poslední pole. Pomocí kalendáře vyberte datový rozsah, na který chcete filtr aplikovat. Jakmile
Pole jsou správně formátovaná, klikněte na tlačítko „Přidat“.

Přizpůsobený filtr zobrazuje všechny dovednosti, které byly vylepšeny, uspořádané podle zaměstnance, ve výchozím nastavení.
listovém zobrazení.

.. příklad::
Pro určení zaměstnance s největším počtem zlepšených dovedností za druhé čtvrtletí odeberte
výchozí filtr v poli vyhledávání zprávy o hodnocení dovedností. Poté aktivujte
filtr „Zlepšení“, pak klikněte na „Přidat vlastní filtr“ na spodku stránky.
:icon:`fa-filter`  sloupec Filtry.

V okně „Přidat vlastní filtr“ zvolte „Datum vytvoření“.
První pole s výběrem z nabídky vyberte „je mezi“ a pro druhé pole s výběrem z nabídky vyberte „od“.
Datové pole se objeví po výběru políčka „Je mezi“.

Pomocí kalendáře vyberte první datum na 04/01/2025 a druhé datum na
:guilabel:`06/30/2025“, pak klikněte na „Přidat“.

.. obrázek::skills_evolution/custom-filter.png
:alt:Pop-up okno filtru s nastavenými parametry.

Pro zobrazení počtu zaměstnanců a dovedností v podrobnějších datech klikněte na ikonu :icon:`oi-view-pivot`.
Ikona „Výchozí“ v pravém horním rohu pro zobrazení dat ve sloupcovém grafu.
pivotová tabulka s řádky obsahujícími zaměstnance a viditelná sloupec představuje celkový počet.
Počet zlepšených dovedností.

Chcete-li rozšířit sloupce a zobrazit typy dovedností s největším celkovým zlepšením, klikněte
:ikonka: `fa-plus-square` :guilabel: Celkem nad sloupcem :guilabel: Počet, pak klikněte
Vyberte možnost „Přidat vlastní skupinu“ a pak klikněte na „Dovednosti“.
rozbalovací nabídka. Tato rozšiřuje všechny zlepšené dovednosti, uspořádané podle jednotlivých dovedností.

.. příklad::
V tomto příkladu se nejvíce zlepšila v třetí čtvrtině Audrey Petersonová s pěti
zlepšení dovedností.

.... obrázek: skills_evolution/largest-improvement.png
:alt:Pivotová tabulka ukazující zlepšení dovedností za třetí čtvrtletí.

.. viz též:
   - :doc:`Odoo esenciální reportování <../../essentials/reporting>`
   - :doc:`../../základy/vyhledávání`
