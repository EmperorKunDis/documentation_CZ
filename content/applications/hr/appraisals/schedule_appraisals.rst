===================
Hodnocení rozvrhu
===================

Aplikace **Ocenění** společnosti Odoo pomáhá manažerům vést pravidelné hodnocení výkonnosti. Každý hodnotící pohovor může zahrnovat
sebehodnocení, které může být podle vlastního rozvrhu.

Pravidelné hodnocení přemění každodenní práci na jasné cíle a měřitelné cíle dovedností.
dodat objektivní důkazy, které potřebuje personální oddělení pro zvýšení platu nebo povýšení a udržet individuální výkonnost.
Společností stanovenými klíčovými ukazateli výkonnosti (KPI).

Hodnocení mohou být automaticky naplánována „přes“ plán hodnocení.
hodnotit podle něj, nebo vytvořen ručně.
hodnotícího manuálu, pokud je třeba – například před povýšením nebo převedením na jinou pozici.

.._hodnocení/auto:

Automatické plánování
====================

Aby nebyl nikdo přehlédnut, zapněte automatické plánování v sekci „Hodnocení“:
app --> Nastavení --> Možnosti“.

Nastavení v sekci „Plán hodnocení“ určuje, jak často jsou plánovány hodnocení.

.. obrázek:schvalovani-hodnoceni/schvalovani-hodnoceni-nastaveni.png
:alt:Sekce hodnocení s vyplněným časovým rámcem a zapnutou zpětnou vazbou.

...hodnotící zprávy/hodnocení plánu:

Oceňovací plány
----------------

Za předpokladu, že nebudou změněny, jsou hodnocení automaticky vytvářena šest měsíců po nástupu zaměstnance.
a po druhé zkoušce přesně za šest měsíců.

Jakmile byly v prvním roce zaměstnání provedeny dvě zpočátku požadované hodnocení,
Ocenění se vytváří pouze jednou za rok (každých dvanáct měsíců).

Tuto skladbu lze měnit změnou počtu měsíců v prázdných polích pod
:guilabel:`Plány hodnocení“ sekci.

.. důležité::
Změna pole „Plán hodnocení“ aktualizuje **všechny** záznamy zaměstnanců.
:guilabel:"Datum dalšího hodnocení" je prázdné.

Automatizace hodnocení
---------------------

Zaškrtněte políčko vedle :guilabel:`Automatizace hodnocení zaměstnanců`, aby Odoo automaticky plánovalo
a potvrzovat hodnocení.

Hodnocení je naplánováno podle :ref:`hodnotícího plánu <hodnoceni/hodnotici-plan>`.

..._hodnocení/příručky:

Manuálně naplánovat hodnocení
==============================

Manažeři mohou kdykoliv naplánovat hodnocení, které je mimo běžný cyklus.

Příkladem může být například povýšení zaměstnance nebo přeřazení do nové pozice či oddělení.
hodnocení má posoudit výkon v současné roli.

Pro vytvoření nové hodnocení otevřete aplikaci „Hodnocení“ (menu „Vybraná položka“), klikněte na „Nový“.
tlačítko v pravém horním rohu. To otevře prázdný formulář :guilabel:`Ocenění`.

Nejprve vyberte zaměstnance, který chcete ohodnotit, v prvním poli na
formulář. Jakmile je vybrán zaměstnanec, zobrazí se jeho:
A pole „Oddělení“ a „Služba“ jsou vyplněny podle informací na záznamu zaměstnance.

Aktuální datum vyplní pole :guilabel:`Datum ocenění`, které je datem ocenění.
až do konce. Použitím kalendáře můžete upravit datum, pokud chcete. Tento prázdný
obvykle aktualizovány, když manažer předává své konečné hodnocení na konci procesu hodnocení.

Pokud je nakonfigurovaný plán hodnocení (viz :ref:`hodnocení <appraisals/appraisal-plan>`), pak
V poli „Datum hodnocení“ se zobrazuje :guilabel:„Průběžné“. To znamená, že následující hodnocení
podle hodnotícího plánu. Jakmile je hodnocení označeno jako dokončené,
:guilabel:`Datum dalšího hodnocení“ je aktualizováno na datum příštího hodnocení.

Zvolte požadovaný šablonu hodnocení. Šablona „Výchozí“ vyplní
Toto pole je vytvořeno automaticky a je k dispozici při instalaci aplikace **Ocenění**. Pomocí seznamového
menu, vyberte jiný šablonu, pokud chcete.

Jakmile jsou údaje v horní části formuláře „Ocenění“ kompletní, klikněte na
Tlačítko „Potvrdit“ v horním levém rohu a aplikace je naplánována na
Společnost o tomto rozhodnutí informuje zaměstnance.

Jakmile je hodnocení potvrzeno, oba zaměstnanci i manažer mohou začít vyplňovat hodnocení.

.. obrázek:schvaleni-hodnoceni/nove-hodnoceni.png
:alt: Nový formulář znaleckého posudku, kde je vyplněna horní polovina.
