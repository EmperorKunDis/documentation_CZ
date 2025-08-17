=================================
Hledat, filtrovat a seskupovat záznamy
=================================

Odoo umožňuje vyhledávání, filtrování a seskupování záznamů v zobrazení, které zobrazí pouze nejdůležitější
relevantní záznamy. Vyhledávací lišta se nachází na horní části obrazovky: začněte psát a vyberte možnost
hodnota <search/value> nebo klikněte na ikonu „:fa-caret-down“ :guilabel: (karta s rozbalovací nabídkou)
filtru „Hledat“, skupinování a oblíbené položky.
Náhledovém menu „Vyhledávání“ a „Oblíbené“.

...hledat/hodnoty:

Hledání hodnot
=================

Vyhledejte konkrétní hodnotu v poli pro vyhledávání a přidejte ji jako filtr. Zadejte hodnotu
(například jméno prodejce nebo název produktu) a vyberte požadovanou možnost z roletky
Aplikovat filtr vyhledávání.

.. příklad::
Místo přidání vlastního filtru :ref:`<search/custom-filters>`, který by vybíral záznamy, kde
*Mitchell Admin* je prodejce na výkazu „Analýza prodeje“ (:menuselection:`Prodejní aplikace -->
Řešení --> Prodej“, vyhledejte „Mitch“ a klikněte na ikonu „fa-caret-right“.
:guilabel:`(podmenu)` ikona vedle :guilabel:`Hledat prodejce: Mitch“ a vyberte
:guilabel:`Mitchell Admin`.

.. obrázek: search/search-values.png
:alt: Hledání konkrétní hodnoty na výkazu prodeje

.. poznámka::
Použitím vyhledávacího pole je totožné s použitím operátoru *obsahuje* při přidání :ref:`vlastního
filtru <vyhledávání/vlastní filtry>“. Pokud je zadána částečná hodnota a požadovaný sloupec
vybrané (bez výběru ikonky „fa-caret-right“ s označením „(podmenu)“, všechny záznamy
obsahující zadané písmena pro vybraný prvek jsou zahrnuty.

.._vyhledávání/filtry:

Filtry
=======

Filtry se používají k výběru záznamů, které splňují určitá kritéria. Výchozím výběrem je
specifické pro každý pohled, ale lze je upravit výběrem jednoho (nebo více) filtrů předdefinovaných.
<hledat/přednastavené filtry>“ nebo přidáním „:odkaz: vlastní filtr <hledat/vlastni-filtry>“.

..._vyhledávání/přednastavené filtry:

Přednastavené filtry
---------------------

Upravte výchozí výběr záznamů kliknutím na ikonu :icon:`fa-caret-down` :guilabel:`(dropdown)`
z vyhledávací lišty a zvolte jeden (nebo více) přednastavených filtrů.
:guilabel:`Filtry“ v rozevíracím seznamu.

.. příklad::
Na výkazu „Analýza prodeje“ (v menu „Prodejní aplikace –> Zprávy –> Prodej“) jsou zobrazeny pouze záznamy
a jsou v pořadí objednávky s datem objednání do 365 dní od data zobrazení.
výchozím nastavení.

Chcete-li zahrnout i záznamy v citačním stupni, vyberte „Citace“ ze seznamu
:guilabel:`Filtry“.

Dále je možné zadat pouze prodejní objednávky a cenové nabídky za určité období, například rok 2024.
například nejprve odstraňte stávající filtr „Datum objednání: posledních 365 dní“ kliknutím
:icon:`fa-times` :guilabel:`(zrušit)“, pak vyberte :menuselection:`Datum objednávky --> 2024“
filtr.

.... obrázek:search/prekonfigurovane-filtry.png
:alt:Použití přednastavených filtrů v zprávě o prodejní analýze

.. poznámka::
Přednastavené filtry jsou seskupeny do skupin a každá skupina je oddělena horizontálně.
řádku. Vybráním přednastavených filtrů z téže skupiny umožňuje vyhledat záznam, který odpovídá *kterékoliv*
podmínky. Nicméně vybírat filtry z různých skupin je možné pouze tehdy, pokud se záznamy shodují
všechny podmínky, které byly uplatněny.

..._vyhledávání/vlastní filtry:

Vlastní filtry
--------------

Pokud přednastavené filtry nejsou dostatečně specifické, přidejte
Vlastní filtr. Klikněte na ikonu „fa-caret-down“ (výběr) v hledání
baru, pak vyberte: menu: „Filtry – Přidat vlastní filtr“.

Okno pro přidání vlastního filtru zobrazuje odpovídající možnost, pravidlo filtru a
Přepnout na záznamy s archivovanými daty.

.. obrázek:search/custom-filter.png
:alt:Okno pro přidání vlastního filtru.

Výchozí konfigurace shody je „Shoda s kteroukoli z následujících pravidel“, což znamená
že každá filtrační pravidlo je aplikováno nezávisle na ostatních. Chcete-li změnit shodovou konfiguraci,
:guilabel:`Přesně shoduje se následující pravidla“, alespoň dvě filtrační pravidla musí být přidána do vlastního
filtr.

- :guilabel:`Všechny“ :icon:`fa-caret-down“ :guilabel:" z následujících pravidel": Všechny
Pravidla filtru musí být splněna. Představte si to jako operace „a“ („&“).
- :guilabel:`Souhlasí s jakýmkoliv z následujících pravidel“: Souhlasí s
Filtr může být splněn. To je jako „nebo“ („|“).

Výchozí nastavení je jedna filtrační pravidla pro vlastní filtr. Následující popisuje
struktura filtračního pravidla:

#První pole inline je název pole, které chcete filtrovat. Některá pole mají upřesněné parametry,
jsou vloženy do jiného pole. Tyto pole mají ikonu „pravý sloupec“
ikona vedle nich, kterou lze vybrat k odhalení skrytých polí.
#Druhé pole inline je operátor podmíněného výrazu, který porovnává název pole s
Hodnota. Specifické pro danou oblast jsou i dostupné podmíněné operátory, viz :ref:`<reference/orm/domains>`.
datový typ pole.
#Třetí pole je proměnná *value*, která má název pole. Hodnota vstupu může být
rozbalovací nabídka, textové pole, pole pro čísla, pole pro datum a čas, výběr logických hodnot nebo může být
podle použitého operátoru a typu pole.

Tři tlačítka inline jsou také k dispozici vpravo od filtru kritérií pravidla:

#:icon:`fa-plus` :guilabel:`(plus)`: Přidá nový pravidlo pod stávající pravidlo.
#:icon:`fa-sitemap` :guilabel:`(node)`: Přidá novou skupinu pravidel pod stávající pravidlo s
:guilabel:`jakýkoliv“ a :guilabel:`všechny“ možnosti shody, které jsou k dispozici pro definování
Tato větve se aplikuje na filtr. Pokud je nastavená stejně jako u rodičovské možnosti,
skupině, pole se přesouvají k rodičovské skupině.

...... příklad::
Pokud je nastavená možnost shody na „Shoda všech“ :icon:`fa-caret-down“ :guilabel:`z řádku
následujících pravidlech“ a nová větev je přidána s jejím shodným parametrem změněným na
:guilabel:`jakýkoliv“ :icon:`fa-caret-down“ :guilabel:`z“ na :guilabel:`všechny“ :icon:`fa-caret-down“
:guilabel:`of`, nově přidaná větev zmizí a její skupina pravidel se přesune do
mateřská skupina.

#:ikona: „odpadkový koš“: guilabel:„(smazat)“: Smaže uzl. Pokud je smazán větvený uzel, všechny
děti daného uzlu jsou také smazány.

Nový filtr lze přidat do vlastního filtru kliknutím na tlačítko „Nové pravidlo“.

Jakmile jsou stanoveny filtrační kritéria, klikněte na tlačítko „Přidat“ a přidejte si vlastní filtr do zobrazení.

.. příklad::
Zacílit na všechny kontakty a příležitosti z aplikace CRM, které jsou v sekci *Vyhráno*.
stupně a očekávaný příjem větší než 1 000 USD by měl být následující:

:guilabel:`Vyhovuje všem následujícím pravidlům:“

   #:guilabel:`Stage“ :guilabel:"je ve" :guilabel:"Vyhrál“
   #:guilabel:`Očekávaný příjem“ :guilabel:`> 1.000“
   #:guilabel:`kdokoliv“ :icon:`fa-caret-down“ :guilabel:`z::

      - :guilabel:`Typ“ :guilabel:`=“ :guilabel:`Vedoucí
      - :guilabel:`Typ“ :guilabel:`=“ :guilabel:`Příležitost“

.... obrázek:search/custom-filter-example.png
:alt:Přidání vlastního filtru k filtrování konkrétních záznamů v CRM.

.. tip::
Aktivujte režim vývojáře, abyste zjistili technické názvy polí a datové typy.
v textovém poli pod filtrem pravidel níže, abyste mohli zobrazit a upravovat doménu.
ručně.

.._vyhledávání/skupina:

Skupinové rekordy
=============

Zobrazení záznamů v pohledu lze seskupit podle jednoho z předdefinovaných
skupin. Chcete-li tak učinit, klikněte na ikonu „svislý šipka“ (viz obrázek) v hledací liště.
Pak vyberte jednu z možností „Skupina“ ze seznamu.

.. příklad::
Řadit záznamy podle prodejce na zprávě „Analýza prodeje“ (:menuselection:`Prodejní aplikace -->
Zprávy --> Prodej“, vyberte možnost „Prodavač“ z nabídky „Skupina“.
příkazem „Drop down“. Zobrazí se výběr skupin dle prodejců a nebudou filtrována žádná data.
rekordy.

.. obrázek:search/group.png
:alt:Seskupení záznamů na přehledu Analýza prodeje

Skupiny lze upravit pomocí pole na modelu. Klikněte
Vyberte možnost „Přidat vlastní skupinu“ a vyberte pole z rozevírací nabídky.

.. poznámka::
Můžete používat několik skupin najednou. První vybraná je hlavní.
cluster, další přidaný pak dále rozděluje kategorie hlavní skupiny a tak dále.
Dále lze filtry a skupiny použít společně k ještě většímu zúžení pohledu.

.._vyhledávání/porovnávání:

Srovnání
==========

Některé reportovací panely obsahují sekci „Srovnání“ v nabídkách
jejich vyhledávacích lištách. To zahrnuje:doc:`Všeobecný výkonnostní efekt
Zpráva o efektivitě výroby pro aplikaci **Výroba**
:report „Základní analýza nákupu“ pro aplikaci Nákup.
a dalších.

Možnosti v sekci :icon:`fa-adjust` :guilabel:`Srovnání“ slouží k porovnání dat z
dvě různá časová období. Vyberte si mezi dvěma možnostmi srovnání:
Předchozí období“ a „:guilabel: (filtr času): Předchozí rok“.

.. důležité::
Pro některé zprávy se v sekci „Srovnání“ objevuje pouze v roletce vyhledávací lišty.
menu, pokud je v sloupci Filtry vybrána alespoň jedna hodnota časového období.
protože není co srovnávat, pokud se neuvádí časové období.

Navíc některé zprávy umožňují pouze srovnání pomocí funkce :guilabel:`Comparison`, pokud
:icon:`fa-pie-chart` :guilabel:`(Pie Chart)` grafický typ nebo :icon:`oi-view-pivot`
:guilabel:`(Pohled Pivot)“ je vybrána. I když se zobrazí možnost „Srovnání“,
Další pohled je možný, ale provedení takového kroku **nezmění způsob zobrazení dat na obrazovce**.
zpráva.

.. obrázek: vyhledávání/srovnání-sekce.png
:alt:Pole pro vyhledávání výrobního analýzy.

Pro zobrazení dat pomocí jedné ze dvou srovnání začněte výběrem časového období v
Vyberte sloupec „Filtry“ v nabídce vyhledávací lišty a poté buď „(Čas)
Filtr „Předchozí období“ nebo filtr „Předchozí rok“ v části „Srovnání“.
§

S jednou z možností :guilabel:`Srovnání` je vytvořen report, který porovnává data pro
vybrané období s daty pro stejný časový úsek (měsíc, kvartál, rok)
předchozí. Způsob zobrazení dat závisí na zvoleném pohledu:

- Ikona „fa-bar-chart“ (Graf bar) zobrazuje dvě svislé čáry vedle sebe pro každou jednotku
doba pro vybrané období. V levém sloupci je zobrazeno vybrané období a v pravém
pravá lišta znázorňuje předchozí časový úsek.
- Zobrazuje se graf s dvěma čarami, jedna z nich znázorňuje
jeden zobrazuje vybrané období a druhý předchozí období.
- Ikona „:icon:`fa-pie-chart`“ se zobrazuje jako velká kružnice s menší kružnicí
výběr časového období. Menší kruh představuje vybrané období.
v předchozím časovém období.
- Ikona „Oi-View-Pivot“ („Pivot“) se zobrazuje vedle každé sloupce, který je rozdělen na dvě menší.
Sloupce vlevo znázorňují vybrané období, sloupec napravo pak zobrazuje
v předchozím časovém období.

.. příklad::
V zprávě „Analýza výroby“ aplikace „Výroba“ jsou uvedeny údaje o
Ve druhém čtvrtletí roku 2024 je porovnáváno s daty za druhé čtvrtletí v roce 2023.
vybrat v sekci filtru „Datum ukončení“ na liště vyhledávacího pole.
menu. V sekci „Srovnání“ je vybrána možnost „Konec roku: Předchozí rok“.

V současné době je rok 2024, takže větší kruh ukazuje údaje za druhé čtvrtletí (Q2) roku 2024.
Menší kruh ukazuje údaje za druhé čtvrtletí (Q2) roku 2023, což je stejný časový úsek.
ale o rok dříve.

Pokud je vybrána volba „Datum ukončení: Předchozí období“, menší kruh zobrazuje údaje za
první čtvrtletí roku 2024, což je stejné období, ale o jednu dobu zpět.

.... obrázek::search/comparison.png
:alt:Srovnávací pohled na výstupní analýzu.

.._vyhledávání/oblíbené položky:

Favorité
=========

Favority jsou způsob, jak uložit konkrétní vyhledávání pro budoucí použití nebo jako nový výchozí filtr
pohled.

Pro uložení aktuálního pohledu jako oblíbeného klikněte na ikonu :icon:`fa-caret-down` :guilabel:`(dropdown)`
Do vyhledávacího pole zadejte a poté v rozevíracím seznamu vyberte možnost „Uložit aktuální vyhledávání“.
následujících možností:

- :guilabel:`Název filtru“: Název vybraného vyhledávání.
- :guilabel:`Výchozí filtr“: nastavuje vyhledávání jako výchozí filtr pro zobrazení.
- :guilabel:`Sdílené“: Umožňuje ostatním uživatelům používat oblíbenou vyhledávací frázi. Výchozím nastavením je
Favoritovaná vyhledávání jsou dostupná pouze uživateli, který je vytvořil.

Jakmile jsou nastaveny požadované možnosti, klikněte na tlačítko „Uložit“ pro uložení oblíbeného vyhledávání.

.. obrázek:search/favorites.png
:alt:Uložení oblíbeného vyhledávání na zprávě o prodejích.

Uložené oblíbené položky lze zobrazit kliknutím na ikonu „Smazat“
vyhledávací liště, pak vybrat filtr v seznamu „Oblíbené“ v rozevíracím seznamu. Chcete-li odstranit
Uložené vyhledávání označte ikonou :icon:`fa-trash` :guilabel:`(smazat)` vedle vyhledávání, které chcete smazat.

.. tip::
Pro zobrazení všech oblíbených vyhledávání nejprve aktivujte režim vývojáře a přejděte na
:menu_selecce:Nastavení aplikace --> Technické --> Uživatelské rozhraní: Vlastní filtry.
Všechny oblíbené vyhledávání lze zobrazit, upravit, archivovat nebo smazat.
