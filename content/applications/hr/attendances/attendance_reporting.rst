====================
Hlášení o účasti
====================

Aplikace **Attendance** Report pomáhá manažerům najít problémy s docházkou zaměstnanců dříve, než
se stát problémem. Zpráva může poskytnout pohled na trendy tím, že určí:
více přesčasů (pracovní doba/přesčasy)“ a kdo je „nevykonává plný úvazek
<přítomnost/nepřítomnost>.

Zobrazit zprávu
===========

Zobrazit účastnický report můžete kliknutím na položku „Reporting“ v horní nabídce. Výchozí report
zobrazuje údaje o docházce zaměstnanců za poslední tři měsíce v výchozím nastavení
:ikonka: „OI-VIEW-PIVOT“ :guilabel:„Tabulka sloupců“. Sloupce jsou vyplněny jmény zaměstnanců, zatímco řádky
obsahují různé návštěvní rekordy. Všechny záznamy jsou seskupeny podle měsíce.

Představené sloupce jsou:

- :guilabel:`Čas odpracovaný za měsíc“: Celkový čas, který zaměstnanec pracoval v daném měsíci.
- :guilabel:`Očekávané hodiny“: Počet hodin, které by zaměstnanec měl odpracovat za měsíc.
vypočítané z jejich pracovního rozvrhu, který je konfigurován na jejich zaměstnanci.
formulář.
- Rozdíl mezi očekávanými hodinami a
:guilabel:`Práce odpracované za měsíc“ pro zaměstnance v daném měsíci.
- :guilabel:`Záloha“: Rozdíl mezi přiznanou a celkovou přesčasovou prací
Vykonávala svou práci.

Pro zobrazení různých informací upravte filtry a skupiny:
Stejně jako v přehledu:guilabel:Overview.

.. obrázek:přítomnostní hlášení/hlášení přítomnosti.png
:alt:Výchozí pohled na zprávu s vyznačenými všemi možnými tlačítky pro přepínání pohledu.

...přítomnost na pracovišti/pracovní doba navíc:

Příklad použití: přesčas měsíčně
==========================

Přesčasová práce ovlivňuje zisk společnosti, protože většina firem má ve svém rozpočtu přidělené prostředky na mzdy zaměstnanců.
pokud jsou platy vyšší než očekávané, mohou se náklady na provoz zvýšit.
pracovní doby. Proto je nutné mít přehled o docházce zaměstnanců a zajistit, aby nedocházelo k
Přihlášený

Pro zobrazení přesčasů za konkrétní měsíc podle zaměstnance klikněte na „Zprávy“ v horním menu.
Aplikace **Přítomnosti**. Odstraňte výchozí skupování podle ikony „OI-Group“ a štítku „Datum: měsíc > zaměstnanec“.
v poli vyhledávání. Klikněte na ikonu „fa-caret-down“ (Zobrazit panel s vyhledáváním) v závěru
v poli vyhledávání, pak klikněte na ikonu „fa-caret-down“ a zvolte požadovaný měsíc.

Dále klikněte na tlačítko „Měření“ v horním levém rohu a
Vyberte pole „Očekávané hodiny“ a „Práce odpracované hodiny“. To zobrazí
:guilabel:`Rozdíl“ a „Vyváženost“ přítomnosti v daném měsíci, skupinované podle
zaměstnanec.

:guilabel:`Rozdíl“ ukazuje celkový přečerpáný čas za měsíc a :guilabel:`Zůstatek“
ukazuje, kolik ještě zbývá k schválení. Klikněte na sloupec „Rozdíl“ a seřaďte podle množství
přesčas. Nejvyšší pozitivní číslo je nejvíce přečerpaných hodin za daný měsíc.

.. příklad::
V následujícím příkladu bylo schváleno celkem 38 hodin a 53 minut přesčasů za měsíc.
3. dubna. Nejvíce přesčasových hodin má Michael Williams s 10 hodinami a 25 minutami.
Bylo zaznamenáno. Z přesčasových hodin bylo schváleno pouze 25 minut, celkem tedy deset zaplacených přesčasových hodin.

.... obrázek:: přítomnost/pracovní doba navíc.png
:alt:Zpráva o docházce za měsíc duben, zobrazující pouze přesčasy.

...přítomnost/neúčast:

Příklad použití: nepřítomnost na pracovišti
=====================

Zaměstnanci s negativním :guilabel:`Rozdíl` ukazují, že neodpracovali očekávaný
přesuny. To může být z důvodu zapomínání na přihlášení a odhlášení ze směny nebo za pracovní dobu kratší než
očekávané a bez schváleného volna.

Pro zobrazení údajů o docházce za poslední tři měsíce a identifikaci trendů nejprve otevřete
Zpráva aplikace „Přítomnost“. Dále klikněte na tlačítko :guilabel:`Míry“ :icon:`fa-caret-down“ v
v horním levém rohu a zkontrolujte, že je vybrána pouze možnost „Rozdíl“.

Poté vyresetujte řádkové údaje kliknutím na ikonu :icon:`fa-minus-square-o` :guilabel:`Celkem“ v horní části
řádky. Pak klikněte na ikonu „+“ a vyberte „Celkem“. Klikněte na
:guilabel:`Rozdíl“ slouží k seřazení podle celkového rozdílu odpracovaných hodin oproti plánu
hodin.

Zaměstnanec, který pracoval nejméně, má nejvyšší záporný zůstatek. Kliknutím na jakoukoliv z čísel
zaměstnanci zobrazit podrobné záznamy o docházce jednotlivých zaměstnanců.

.. příklad::
V následujícím příkladu společnost funguje pouze dva měsíce, takže jsou k dispozici jen omezené údaje
i přesto, že filtr „Poslední tři měsíce“ je aktivní.

Z této zprávy vyplývá, že Abigail Petersonová pracovala nejméně.
V posledních dvou měsících pracovala o 25 hodin méně než bylo předpokládáno.

.... obrázek: hlášení o účasti/neúčasti.png
:alt:Zpráva o docházce s nejvyšším počtem nepřítomností za poslední dva měsíce.
