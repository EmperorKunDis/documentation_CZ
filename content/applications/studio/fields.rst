==================
Pole a widgety
==================

Pole strukturují modely databáze. Pokud si představíte model jako tabulku nebo sešit, pak pole
slouží k uložení dat v záznamu (tj. řádcích). Položky také definují typ
Data uložená v nich. Jak je data na :abbr:`UI (User
Výchozí hodnota je „Interface (widget)“.

Z technického hlediska je v Odoo 15 typů polí, ale můžete si vybrat z 20
pole v aplikaci Studio, protože některé typy polí jsou k dispozici vícekrát s různými výchozími ovládacími prvky.

..tip:
:guilabel:`Nové pole“ lze přidat pouze do formuláře v sekci „Všeobecné nastavení“
:ref:`studio/views/multiple-records/list` vzhledy. Na ostatních vzhledech lze pouze přidat
:guilabel:`Stávající pole“ :dfn:"(pole již na modelu)".

.._studia/pole/jednoduchá pole:

Jednoduchá pole
=============

Jednoduché pole obsahuje základní hodnoty, jako je například text, čísla, soubory atd.

.. poznámka::
Nenáhodným widgetům se v případě dostupnosti zobrazují jako odrážky nebo podnadpisy pod nimi.

.. _studia/pole/jednoduché pole textové:

Text (char)
-------------

Pole Text slouží pro krátký text obsahující libovolný znak. Jedna řádka je
Zobrazí se při vyplňování pole.

- :guilabel:`Štítek“: zobrazuje hodnotu uvnitř zaobleného tvaru podobného štítku. Hodnota nemůže
je možné upravit v uživatelském rozhraní, ale lze nastavit výchozí hodnotu.
- :guilabel:`Kopírovat do schránky“: uživatelé mohou hodnotu zkopírovat kliknutím na tlačítko.
- :guilabel:`E-mail`: hodnota se stane kliknutelným odkazem na mail.
- :guilabel:Obrázek: zobrazuje obrázek pomocí URL. Hodnota nelze upravit ručně, ale
Může být nastavena výchozí hodnota.

...... poznámka::
Toto funguje jinak než výběr pole :ref:`Obrázek.
přímo na objektu pole <studio/fields/simple-fields-image>, protože obrázek není uložen v Odoo při použití
:guilabel:`Textová pole“ s widgetem :guilabel:`Obrázek“. Například se může hodit v případě, že
chcete ušetřit místo na disku.

- :guilabel:"Telefon": hodnota se stane klikatelným odkazem na telefonní číslo.

..tip:
Zatrhněte políčko „Povolit SMS“ a přidejte možnost odeslání SMS přímo z Odoa vedle
pole.

- :guilabel:`URL“: hodnota se stane kliknutelným URL.

Příklad:

.... obrázek::fields/text-examples.png
:alt:Příklady textových polí s různými ovládacími prvky

.._studio/pole/jednoduché pole - víceřádkový text:

Multiline Text (text)
-----------------------

Pole :guilabel:`Multilínový text` se používá pro delší text obsahující jakýkoliv typ znaku.
Textové řádky se zobrazí na uživatelském rozhraní při vyplňování pole.

- :guilabel:`Kopírovat do schránky“: uživatelé mohou hodnotu zkopírovat kliknutím na tlačítko.

Příklad:

.... obrázek::fields/multiline-text-examples.png
:alt:Příklady multiliniových textových polí s různými ovládacími prvky

.._studia/pole/jednoduché pole - číslo:

Číslo celé („celé číslo“)
-------------------

Konstantní pole :guilabel:`Integer` se používá pro všechna celá čísla (tj. kladná, záporná nebo nula).
bez desetinné čárky.

- :guilabel:„Procentní kruh“: zobrazuje hodnotu uvnitř procentního kruhu, obvykle počítanou
hodnota, která se na uživatelské rozhraní nezobrazuje, ale lze ji nastavit jako výchozí hodnotu.
- :guilabel:`Progresová lišta“: zobrazuje hodnotu vedle procentní lišty, obvykle počítanou
hodnota. Hodnotu nelze upravit ručně, ale lze nastavit výchozí hodnotu.
- :guilabel:`Manuální řazení záznamů“: zobrazí ikonku táhla, pomocí kterého lze manuálně upravit pořadí záznamů v seznamovém výpisu.
<studia/zobrazení/více záznamů/seznam>.

Příklad:

.... obrázek:: pole/celočíselné příklady.png
:alt:Příklady pole typu celé číslo s různými ovládacími prvky

.._studio/pole/jednoduché pole - desetinné číslo:

Desetinné („float“)
-----------------

Pole :guilabel:`Decimální` se používá pro všechna desetinná čísla (:dfn:`kladná, záporná nebo nula
s desetinnou čárkou).

.. poznámka::
Základní desetinná čísla jsou na uživatelské rozhraní zobrazena s dvěma desetinnými místy za desetinnou čárkou.
uloženy v databázi s vyšší přesností.

- :guilabel:`Monetární“: je podobné použití pole :ref:`Monetární
<studia/pole/jednoduché-pole-měnové>. Doporučuje se používat druhou, protože nabízí více možností.
funkce.
- :guilabel:`Procento“: zobrazuje procentní znaménko „%“ za hodnotou.
- :guilabel:„Procentní kruh“: zobrazuje hodnotu uvnitř procentního kruhu, obvykle počítanou
hodnota. Hodnotu nelze upravit ručně, ale lze nastavit výchozí hodnotu.
- :guilabel:`Progresová lišta“: zobrazuje hodnotu vedle procentní lišty, obvykle počítanou
hodnota. Hodnotu nelze upravit ručně, ale lze nastavit výchozí hodnotu.
- :guilabel:`Čas`: hodnota musí být ve formátu *hh:mm*, maximálně však 59 minut.

Příklad:

.... obrázek:: pole/desetinné-příklady.png
:alt:Příklady desetinných polí s různými ovládacími prvky

.._studia/pole/jednoduché-pole-peněžní:

Monetární
---------------------

Pole :guilabel:`Monetární` se používá pro všechny peněžní hodnoty.

.. poznámka::
Při prvním přidání pole :guilabel:`Monetary` vás program vyzve k přidání pole :guilabel:`Currency`.
pole, pokud ještě neexistuje na modelu. Odoo nabízí přidat pole „Měna“ s názvem
Vyberte si vás. Poté znovu přidejte pole :guilabel:`Monetary`.

Příklad:

.... obrázek:: pole/peněžní-příklad.png
:alt: Příklad pole Měna spolu s poli Měna

.. _studia/pole/jednoduché_pole_html:

HTML („html“)
-------------

Pole :guilabel:`Html` slouží k přidání textu, který lze upravovat pomocí editoru HTML v Odoo.

- :guilabel:`Multiline Text“: deaktivuje editor HTML v Odoo, aby bylo možné upravovat čistý HTML.

Příklad:

.... obrázek:: pole/html_příklad.png
:alt:Příklady polí HTML s různými ovládacími prvky

.._studia/pole/jednoduché-pole-datum:

Datum (date)
-------------

Pole :guilabel:`Datum` slouží k výběru data v kalendáři.

- :guilabel:`Dny do vybraného data“: zobrazuje počet dní zbývajících do vybraného data
(např. „Po 5 dnech“), na základě aktuálního data. Tento prvek by měl být nastaven na :guilabel:`Čtení jen pro čtenáře“.

Příklad:

.. obrázek:: fields/date-examples.png
:alt:Příklady pole Datum s různými widgety

.._studio/pole/jednoduché pole - datum a čas:

Datum a čas (datum a čas)
------------------------

Pole „Datum a čas“ se používá k výběru data na kalendáři a času na hodinách.
Pokud není nastaven čas, bude použit aktuální čas uživatele.

..tip:

Kromě obecných vlastností (viz :ref:`obecné vlastnosti <studio/fields/properties>`)
:ref:`specifické vlastnosti <studio/fields/properties-date-datetime> jsou dostupné pro
:guilabel:`Datum a čas“ políčka, která obsahují buďto :guilabel:`Datum a čas“ nebo :guilabel:`Časový rozsah“.
widgetová sada.

Datový rozsah (daterange)
~~~~~~~~~~~~~~~~~~~~~~~~

Komponenta :guilabel:`Datový rozsah` se používá k zobrazení časového úseku definovaného datem začátku.
datum na jednu řádku. Datum rozmezí může mít povinné datum začátku i konce, např. pro
vícedenní událost nebo umožnit volitelný začátek nebo konec datumu, například pro terénní zásah nebo
úkol projektu.

Přidání rozsahu dat vyžaduje dvě pole: pole „Datum a čas“ s
:guilabel:`Datový rozsah“ widget a další pole, které je vybráno jako datum začátku nebo konce
datum, které je podkladem pro tento prvek. Toto základní pole může být existující :ref:`Datum <studio/fields/simple-fields-date>
nebo pole „Datum a čas“ nebo pole vytvořené pro tento účel.

Přidat datumový rozsah:

#Určete existující pole „Datum“ nebo „Datum a čas“, které lze použít jako
podkladový začátek/konec nebo přidat nový. Pokud datumové rozpětí:

   - má povinné datum začátku a konce, tento prvek může být buď datem začátku nebo datem ukončení.
Výsledek je stejný.
   - umožňuje nepovinný začátek nebo konec, v tomto poli je uveden počáteční nebo koncový termín, podle toho, co je vyplněno.

......tip:
Pro vyhnutí se zobrazení stejné informace dvakrát může být podkladové pole začátku a konce
skryté zapnutím volby „Nepostradatelné“ nebo zobrazení skrytím kliknutím
:guilabel:`Odebrat z pohledu“.

#Přidejte pole „Datum a čas“ a nastavte pole „Zobrazovací prvek“ na
:guilabel:`Datový rozsah“.
#Zadejte vhodný :guilabel:`Štítek“.
#Vyberte podkladový startovací a ukončovací datum z pole „Datum začátku“ nebo
:guilabel:`Datum ukončení“ v roletce, pokud je relevantní.
#Pokud by měl být datový rozsah povinně vymezen začátkem a koncem, zapněte volbu „Vždy rozsah“.
#Aktualizujte ostatní vlastnosti: obecné vlastnosti <studia/pole/vlastnosti> nebo specifické
:ref:`vlastnosti pro pole Datum a Čas <studio/fields/properties-date-datetime>“ podle potřeby.
Klikněte na tlačítko „Zavřít“ v pravém horním rohu obrazovky.

Příklad:

.. obrázek:: fields/date-time-examples.png
:alt:Příklady polí Datum a Čas s různými widgety

Dny zbývající k uplatnění („remaining_days“)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Karta „Dny do vybraného data“ zobrazuje počet dní, které zbývají do vybraného data.
(např. *Po 5 dnech*) podle aktuálního data a času. Tento prvek by měl být nastaven na :guilabel:`Číst
jenom“.

.._studia/pole/jednoduché-políčko:

Zatržítko (boolean)
--------------------

Pole :guilabel:`Checkbox` se používá v případě, kdy má hodnota mít buď pravdivou, nebo nepravdivou podobu.
zaškrtnutí nebo vyškrtnutí zaškrtávacího políčka.

- :guilabel:`Tlačítko“: Zobrazuje tlačítko. Widget funguje i bez přepnutí do režimu editaci.
- :guilabel:`Přepínač“: Zobrazuje tlačítko přepínače. Widget funguje bez přechodu do režimu editaci.

Příklad:

.... obrázek:: pole/check-box-příklad.png
:alt: Příklady checkboxových polí s různými widgety

.._studia/pole/jednoduchá pole výběru:

Výběr (výběr)
-----------------------

Pole :guilabel:`Výběr` se používá v případě, když uživatelé mají vybrat jednu hodnotu ze skupiny.
Předdefinované hodnoty.

- :guilabel:`Štítek“: zobrazuje hodnotu uvnitř zaobleného tvaru podobného štítku. Hodnota nemůže
je možné upravit v uživatelském rozhraní, ale lze nastavit výchozí hodnotu.
- :guilabel:`Štítky“: zobrazuje všechny volitelné hodnoty najednou uvnitř čtvercových tvarů.
organizované vertikálně.
- :guilabel:`Priorita“: zobrazuje hvězdičky namísto hodnot, které lze použít k označení
důležitost nebo spokojenost například. To má stejný účinek jako výběr
:ref:`Prioritní pole <studio/fields/simple-fields-priority>“, i když u posledního jde o čtyři
Prioritní hodnoty jsou již předdefinovány.
- :guilabel:`Rádio“: zobrazuje všechny volitelné hodnoty zároveň s tlačítky rádia.

..tip:
Výchozí organizace tlačítek rádií je vertikální. Aktivujte možnost „Zobrazit horizontálně“
změnit způsob jejich zobrazení.

- :guilabel:„Stavová lišta“: zobrazuje všechny vybrané hodnoty najednou jako šipkový průběh.

..tip:
Výchozí hodnota je „volitelné“. Zakažte volbu „Klikatelné“ a zabraňte tomu, aby se na liště zobrazovaly
hodnota, kterou uživatel upravuje na rozhraní.

Příklad:

.... obrázek::fields/selection-examples.png
:alt:Příklady pole výběru s různými widgety

.._studia/pole/jednoduché-pole-priorita:

Priorita (vybírání)
----------------------

Značka pole Priority se používá pro zobrazení tříhvězdičkového hodnocení, které lze využít k
označují důležitost nebo úroveň spokojenosti. Tento typ pole je :ref:`Vybrané pole
„Jednoduché pole“ s výchozím vybraným widgetem „Důležitost“.
a čtyři předdefinované hodnoty priorit. Z toho důvodu je zde :guilabel:`Badge`, :guilabel:`Badges“,
Widgety „Rádio“ a „Výběr“ mají stejné účinky, jaké jsou popsány pod
:ref:`Výběr <studia/pole/jednoduché-pole-výběr>“.

..tip:
Chcete-li změnit počet dostupných hvězd přidáním nebo odebráním hodnot, klikněte na tlačítko :guilabel:`Edit
Hodnota. První hodnota je rovna počtu hvězdiček, tedy nula, pokud žádnou volbu nejsou vybrány.
Příkladem je třeba hvězdičkový systém s čtyřmi hodnotami.

Příklad:

.... obrázek:: pole/priorita-vzor.png
:alt: Příklad pole Priorita

.._studia/pole/jednoduché-pole-soubor:

Soubor (binární)
---------------

Pole „Soubor“ slouží k nahrání jakéhokoliv typu souboru nebo k podepsání formuláře (položka „Podepsat“)
widget).

- :guilabel:`Obrázek“: uživatelé mohou nahrát obrázek, který se pak zobrazí v :ref:`Zobrazení formulářů
<studia/výhledy/obecné/formulář>. To má stejný účinek jako použití pole obrázku
<studia/pole/jednoduché-pole-obrázek>.
- :guilabel:`Prohlížeč PDF souborů“: uživatelé mohou nahrát PDF soubor, který lze poté procházet z
:ref:`Výhled formulářů <studio/views/general/form>“.
- :guilabel:`Podpis“: uživatelé mohou elektronicky podepsat formulář, což má stejný účinek jako výběr
pole :ref:`Značka <studio/fields/simple-fields-sign>`.

Příklad:

...... obrázek:: pole/příklady souborů.png
:alt:Příklady polí s různými widgety

.._studio/pole/jednoduché pole - obrázek:

Obrázek (binární)
----------------

K pole „Obrázek“ je přiřazen štítek „Obrázek“, který se používá k nahrání obrázku a jeho zobrazení v záložce „Zobrazení formuláře“.
„<studia/zobrazení/obecné/formulář>“. Tento typ pole je :ref:`Souborové pole
<studia/pole/jednoduché pole> s výchozím widgetem „Obrázek“.
Protože se jedná o souborový formát, widgety „Soubor“, „PDF Viewer“ a „Podpis“ mají
stejné účinky jako popsány pod odkazem na soubor :ref:`<studio/fields/simple-fields-file>`.

..tip:
Chcete-li změnit velikost zobrazení nahraných obrázků, vyberte „Malé“, „Střední“ nebo
:guilabel:`Velké“ pod volbou „Velikost“.

.._studia/pole/jednoduché pole s nápisem:

Znak (binární)
---------------

Záložka „Sign“ se používá k elektronickému podepsání formuláře. Tento typ pole je :ref:`soubor
pole s výchozím výběrem widgetu :guilabel:`Sign`.
Protože jsou tyto tři widgety součástí knihovny GTK+ 3.0, je vhodné je používat s ní.
stejné účinky jako popsány pod odkazem na soubor :ref:`<studio/fields/simple-fields-file>`.

..tip:
Chcete-li uživatelům při podepisování nabídnout možnost „Auto“, vyberte jednu z následujících
dostupné: guilabel:„Doplňování“ políček (viz odkaz na „Textové pole <studio/fields/simple-fields-text>“
:ref:`Mnoho k jednomu <studio/fields/relational-fields-many2one>“ a „Související pole
(v poli vztahových atributů na modelu) a podpis je
automaticky vygenerované z dat vybraného pole.

.._studia/pole/vztahová pole:

Relativní pole
=================

Vztahová pole se používají k propojení a zobrazení dat ze záznamů na jiném modelu.

.. poznámka::
Nedefinované widgety jsou zobrazeny jako seznam bodů pod nadpisem.

.._studia/pole/vztahová pole mnoho k jednomu:

Many2One (many2one)
---------------------

Záznam pole :guilabel:`Many2One` slouží k propojení dalšího záznamu (z jiného modelu) s aktuálním záznamem.
připravuje se k úpravě. Název zaznamenaný v jiném modelu je pak zobrazen u záznamu, který je připraven ke změně.

Příklad:
Na modelech objednávek je pole zákazníka :guilabel:`Many2One`
a odkazuje na model „Kontakt“, což umožňuje propojit mnoho objednávek s jedním kontaktem.
kontakt (zákazník).

.... obrázek::fields/many2one-diagram.png
:alt: Schéma znázorňující mnoho-k-jednomu vztah

..tip:
   - Aby uživatelé nemohli vytvářet nová data ve spojeném modelu, zaškrtněte políčko:
vytvoření.
   - Chcete-li zabránit uživatelům otevírat záznamy v novém okně, zaškrtněte políčko „Zakázat otevření“.
   - Pomůže uživatelům vybrat pouze správný záznam, klikněte na tlačítko „Doména“ pro vytvoření filtru.

- :guilabel:`Štítek“: zobrazuje hodnotu uvnitř zaobleného tvaru podobného štítku. Hodnota nemůže
může být upraveno na uživatelské rozhraní.
- :guilabel:`Rádio“: zobrazuje všechny volitelné hodnoty zároveň s tlačítky rádia.

.._studia/pole/vztahová pole - jeden k mnoha:

One2Many („one2many“)
---------------------

Pole :guilabel:`One2Many` se používá k zobrazení existujících vztahů mezi záznamem na
současný model a několik rekordů z jiného modelu.

Příklad:
Můžete přidat pole :guilabel:`One2Many` na modelu *Contact*, abyste se mohli podívat na **jednoho** zákazníka.
mnoho objednávek na prodej.

.... obrázek:: pole/jedno2mnoho-diagram.png
:alt: Schéma znázorňující vztah jedno2mnoho

.. poznámka::
Pro použití pole :guilabel:`One2Many`, musely být obě modely propojeny pomocí vazby
:ref:`Polyfield <studio/fields/relational-fields-polyfield>`. Relace One2Many neexistují
samostatně: provádí se zpětný vyhledávání existujících vztahů Many2One.

.._studia/pole/vztahová pole:

Řádky (jedna řada na mnoho)
------------------

Pole :guilabel:`Lines` se používá k vytvoření tabulky s řádky a sloupci (například řádky
výrobky na prodejní objednávku).

..tip:
K modifikaci sloupců klikněte na pole „Řádky“ a poté na „Upravit zobrazení“.
Chcete-li upravit formulář, který se zobrazí po kliknutí na tlačítko „Přidat řádek“, klikněte na
:guilabel:`Upravit formulář“ místo toho.

Příklad:

.... obrázek: pole/linie-příklad.png
:alt: Příklad pole Line

.._studia/pole/vztahová pole mnoho k mnohu:

Many2Many (many2many)
-----------------------

Pole :guilabel:`Many2Many` slouží k propojení více záznamů z jiného modelu s více záznamy.
záznamy na aktuálním modelu. Mnoho-množstevních polí lze použít s :guilabel:`Zakázat vytváření`.
:guilabel:`Zakázat otevření“, „Doména“ stejně jako :ref:`Mnoho-k-jednomu pole
<studia/pole/vztahová pole - mnoho k jednomu>.

Příklad:
Na modelech s názvem „Úkol“ je pole :guilabel:`Assignees“ :guilabel:`Many2Many“ pole, které odkazuje na
model „Kontakt“. To umožňuje přiřadit jednomu uživateli mnoho úkolů a mnoho projektů.
přiřazení uživatelů k jedné úloze.

.... obrázek:: pole/many2many-schéma.png
:alt: Schéma ukazující mnoho-mnoho vztahy

- :guilabel:`Zatržítka“: uživatelé mohou vybrat několik hodnot pomocí zatržítka.
- :guilabel:`Štítky“: uživatelé mohou vybrat několik hodnot, které se zobrazují v kruhových tvarech, známých také jako
*tagy*. To má stejný účinek jako výběr pole Tags:
<studia/pole/vztahová pole - tagy>.

.._studio/pole/vztahová pole:

Štítky („many2many“)
------------------

V poli :guilabel:`Tagy` se zobrazují hodnoty několika dalších modelů v uzavřených kulatých závorkách.
tvaru, také známé jako tagy. Tento typ pole je :ref:`polymorfní pole
„Studia“ / „Pole“ / „Poly v mnoha k sobě“ s výchozím vybraným widgetem „Štítky“.
Proto mají widgety „Zatržítka“ a „Mnoho k mnoha“ stejné účinky jako
Popsané v části :ref:`Many2Many <studio/fields/relational-fields-many2many>`.

..tip:
Pro zobrazení štítků s různými pozadími vyberte možnost „Používat barvy“.

Příklad:

.. obrázek:: fields/tags-example.png
:alt: Příklad pole Tags

.._studia/pole/položka pole vztahující se k poli:

Související pole („související“)
-------------------------

Příbuzné pole není vlastně položkou vztahového pole, neexistuje mezi nimi žádný vztah.
vztahy. Používá existující vztah k načtení a zobrazení informací ze záznamu jiného typu.

Příklad:
Pro zobrazení e-mailové adresy zákazníka na modelech objednávek použijte :guilabel:`Related
V poli „Partner ID“ vyberte pole „Zákazník“ a pak pole „E-mail“.

.._studia/pole/vlastnosti:

Vlastnosti
==========

Obecné vlastnosti
------------------

- :guilabel:`Nepostradatelné“: Zapněte tuto vlastnost, pokud je pro uživatele nezbytné zobrazit pole
UI. To pomáhá odstranit zbytečné prvky v uživatelském rozhraní, které se zobrazují podle konkrétního
situaci.

Atribut :guilabel:`Neviditelný“ také platí uvnitř studia. Chcete-li vidět skryté pole v rámci studia,
Klikněte na záložku „Zobrazit“ ve vlastnostech pohledu a zapněte možnost „Zobrazit skryté prvky“.

- :guilabel:`Povinné“: Zapněte tuto vlastnost, pokud je pole vždy nutné vyplnit
předtím, než se může pokusit o další postup.

- :guilabel:`Čtení jen“: Zapněte tuto vlastnost, pokud uživatelé nemají možnost měnit pole.

.. poznámka::
Můžete si vybrat, zda chcete povolit :guilabel:`Nepovinné`, :guilabel:`Povinné“ a :guilabel:`Čitelné“.
pouze pro konkrétní záznamy kliknutím na tlačítko „Podmíněné“ a vytvořením filtru.

...... příklad::
Na formulářovém pohledu kontaktního modelu se pole „Název“ zobrazuje pouze tehdy,
:guilabel:"Osoba" je vybrána, protože pole "osoba" by nebylo pro hledání užitečné.
:guilabel:`Kontaktujte společnost`.

- :label:Jméno pole na uživatelské rozhraní. To není jméno používané v databázi PostgreSQL
databáze. Chcete-li zobrazit a změnit poslední jmenovanou, aktivujte režim vývojáře
upravit pole „Technický název“.

- :guilabel:`Nápověda nástroje pomocí vyskakovacího okna“: K vysvětlení účelu pole přidejte popis. Text
zobrazené v nástrojovém tipu, když na otazník vedle něj myší přejedete.
pole s popisem.

- :guilabel:`Widget“: Chcete-li změnit výchozí vzhled nebo funkčnost pole, vyberte jeden z
dostupné widgety.

- :guilabel:`Příklad vyplnění pole“: Chcete-li ukázat, jak by mělo být pole vyplněno, přidejte příklad
text, který se objevuje v šedé barvě, dokud nebude zadána hodnota.

- :guilabel:`Výchozí hodnota“: Chcete-li zobrazit výchozí hodnotu v poli při vytváření záznamů, přidejte
hodnota.

- :guilabel:`Povolit viditelnost skupinám“: Chcete-li omezit uživatele, kteří mohou zobrazit pole, vyberte jednu nebo více možností.
více uživatelských přístupů:
- :guilabel:`Zakázat viditelnost skupinám“: Chcete-li některým uživatelům zakázat zobrazení pole, vyberte
jedno nebo více uživatelských přístupů: skupin s právy.

.._studia/pole/vlastnosti-datum-čas:

Vlastnosti pro pole Datum a Čas
---------------------------------

Pro pole „Datum a čas“ nebo „Časové období“, které obsahují pole „Datum a čas“ nebo „Časové období“.
sada widgetů, některé specifické vlastnosti jsou k dispozici:

- :guilabel:`Nejmenší přesnost“: Zvolte nejmenší jednotku dat, která musí být vybrána v datu
selektor. Možné hodnoty jsou: guilabel:„Den“, „Měsíc“ nebo „Rok“.
:guilabel:`Desetiletí“. Pokud není vybrána žádná hodnota, musí uživatel zvolit den v datovém výběru.
- :guilabel:`Nejvyšší přesnost“: Určete největší jednotku data, která lze použít k navigaci
datumový výběr. Možné hodnoty jsou: guilabel:"Den", guilabel:"Měsíc" nebo guilabel:"Rok".
:guilabel:`Desetiletí“. Pokud není vybrána žádná hodnota, může uživatel procházet datovým výběrem desetiletí.
- Vlastnost:„Varování pro budoucí data“: Zapněte tuto vlastnost, aby se zobrazila varovná ikona, pokud je datum v budoucnosti.
Datum se vybírá.
- :guilabel:`Shrnutý zobrazování“: Zapněte tuto vlastnost, abyste mohli zobrazit dny, měsíce a hodiny bez předcházejícího
např. „4/2/2025 8:05:00“ místo „04/02/2025 08:05:00“.
- Vlastnost „Zobrazit čas“: Tato vlastnost je zapnuta výchozím nastavením u polí „Datum a čas“.
pole čtení pouze, vlastnost zobrazit pouze datum. To může udržet seznamový pohled méně
například přeplněný.
- :guilabel:`Zobrazit sekundy“: Tato vlastnost je ve výchozím nastavení zapnutá pro pole „Datum a čas“.
Zakázat vlastnost, která zobrazuje pouze hodiny a minuty.
- :guilabel:`Časový úsek“: Zadejte hodnotu, která určí minutové intervály zobrazené v čase.
selektor. Například zadejte hodnotu 15 pro čtvrthodinové intervaly. Výchozí hodnota je nastavena na 5
minut.
- :guilabel:`Nejranější přijatelný termín“: Zadejte nejdřívější datum, které lze vybrat v datu
selektor v ISO formátu, tedy „RRRR-MM-DD“. Pokud je aktuální datum vždy nejstarším přijatým
Datum zadejte jako dnes. V kalendáři se zobrazí šedě data před nejstarším přijatým datem.
Vyšel ven.
- :guilabel:`Nejnovější přijatá data“: Zadejte nejpozdější datum, které lze vybrat v datu
selektor v ISO formátu, tedy „RRRR-MM-DD“. Pokud je aktuální datum vždy nejnovějším přijatým
Datum zadejte jako dnes. V kalendáři jsou šedé pozdější data než nejpozdnější přijatý termín.
Vyšel ven.

