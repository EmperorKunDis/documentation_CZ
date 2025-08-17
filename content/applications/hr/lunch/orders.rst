Zobrazit obsah

======
Příkazy
======

Aplikace Lunch umožňuje zaměstnancům objednávat obědy, zjistit, co je k dispozici každý den, a kontrolovat své
účetní zůstatek, vše na jednom místě.

Když se otevře aplikace **Oběd**, načte se panel „Objednej si oběd“.
pohled je také dostupný po zadání adresy:menu-selection:Lunch App --> My Lunch --> New Order.

Dashboard Order Your Lunch poskytuje přehled nabídek obědů, účet uživatele
informace a aktuální objednávky spolu se stavem jejich zpracování.

Objednej si oběd
================

Na hlavní obrazovce „Objednejte si oběd“ jsou všechny potřebné informace k objednání
je vidět. Filtr „Dnes k dispozici“ v hledací liště aktivujte kliknutím na
vyhledávací lištu a vyberte:guilabel:"Dostupné dnes". Tento filtr zobrazuje pouze produkty, které jsou
bude koupena v daný den na základě dostupnosti dodavatele.

Levá část přístrojové desky zobrazuje různé kategorie produktů dostupných v obchodě.
spolu s dodavateli produktů („Vendory“). Každá řádka má vedle sebe číslo
Ukazuje, kolik produktů je spojeno s konkrétní kategorií nebo dodavatelem.

Chcete-li filtrovat produkty podle kategorií nebo prodejců, zaškrtněte políčko vedle požadované kategorie nebo
Prodejce může vidět pouze položky související s těmito výběry. Může být proveden více výběrů v každé
§

.. poznámka::
Pokud je vybráno více možností, zobrazí se pouze produkty, které spadají pod **všechny** vybrané možnosti.
Je uveden.

Horní část přístrojové desky slouží jako souhrn objednávky a zobrazuje účet uživatele.
informace a podrobnosti o objednávkách dnešního dne, pokud byly vytvořeny nějaké objednávky.

Hlavní část, která se nachází pod informacemi o uživateli, zobrazuje všechny produkty v přednastaveném Kabanu.
zobrazení. Každá karta produktu zobrazuje název, cenu, dodavatele, fotografii a popis produktu. Pokud
produkt je konfigurován jako nový a také zobrazuje štítek „New“.

.. obrázek: objednávky/příkazovka.png
:alt:Přístupová obrazovka aplikace Lunch.

.. poznámka::
Kdekoli je uvedeno jméno dodavatele v aplikaci Lunch, například na kartách produktů kanbanu,
Telefonní číslo je také uvedeno.

Produkty lze také zobrazit v seznamovém pohledu kliknutím na ikonu :icon:`oi-view-list`.
:guilabel:`(Seznam)` ikona v pravém horním rohu panelu.

Objednávání
==============

Pro objednání oběda přejděte na hlavní panel „Objednejte si oběd“, buď
otevřením aplikace **Lunch** nebo přes menu: `Lunch app --> My Lunch --> New
Přikázání“.

Přidat produkty do objednávky
------------------------

Ve sloupci „Objednej si oběd“ klikněte na požadovaný produkt, který chcete přidat do objednávky.
produkt se objeví v okně „Upravte svůj nákup“.

V horní části okna se zobrazuje obrázek produktu, jeho název a cena. Pod nimi jsou
potenciální pole „Doplňky“ s možností zobrazení všech „doplňků nebo možností“ (<lunch/extras>)
například omáčky nebo nápoje. Zaškrtněte políčko u příslušných extra, které jsou v
Pole „Doplňky“ k přidání do objednávky.

Každá další volitelná položka je organizována podle kategorie s názvem a cenou.
vybrané, zobrazená cena v horní části okna se aktualizuje tak, aby odrážela všechny současné
selekce.

Pod položkou Extras je popis produktu následovaný
:guilabel:`Poznámky“ pole. Pole „Poznámky“ slouží k zadání jakýchkoliv důležitých informací, které
je pak zaslána dodavateli objednávky, například s jakýmikoliv zvláštními požadavky nebo alergiemi na potraviny.

Po provedení všech výběrů produktu klikněte na tlačítko „Přidat do košíku“ v
v levém dolním rohu okna. Chcete-li zrušit objednávku, klikněte na tlačítko „Zrušit“.

.. obrázek: objednavky/pizza.png
:alt:Okno pro objednávku osobní pizzy s vybranými příplatkovými položkami.

Chyby
~~~~~~

Podle toho, jak jsou různé :ref:`doplňky <lunch/configure-extras>` nakonfigurovány pro dodavatele,
Při pokusu o přidání produktů do košíku může dojít k chybě.

Chyba může nastat, pokud konfigurovaný produkt vyžaduje uživatele, aby zvolil možnost v
„Doplňky“ pole, ale uživatelé ho opomíjejí.

Pokud k tomu dojde, objeví se okno chybové hlášky „Validace chyby“. Chyba je krátce
vysvětluje v okně s upozorněním. Kliknutím na tlačítko „Zavřít“ zavřete okno a proveďte případné
změny v okně „Nastavení objednávky“.

.. příklad::
Prodávající, Pizza Palace, nabízí s každou objednávkou nápoj zdarma.
Je konfigurováno tak, že výběr nápoje je **povinný** v poli „Doplňky“ předtím, než
přidáním jednoho z jejich produktů do košíku.

Pokud není vybrána žádná položka, dojde k chybě. Zobrazí se zpráva „Musíte si objednat“.
„jediný a jedinečný nápoj zdarma s nákupem“.

.... obrázek: objednávky/chyba.png
:alt:Okno chybové hlášky „Validace chyby“ s konkrétními informacemi o zadané chybě.
zobrazený nápoj.

Shrnutí objednávky
------------------

Když je alespoň jeden produkt přidán do objednávky, zobrazí se produkty na horním panelu.
:guilabel:`Souhrn objednávky“ s přehledem produktů a účtu uživatele.
kromě všech informací týkajících se objednávek v průběhu aktuálního kalendářního dne.

Jakmile je produkt přidán do objednávky, objeví se v horní části střední části okna s výpisem. Každý produkt má
pod slovy: `Vaše objednávka`, s názvem produktu, množstvím a stavovým štítkem.

K dispozici jsou následující štítky, které mohou být zobrazeny pro každý výrobek:

- :guilabel:`K objednání“: produkt byl přidán do košíku, ale ještě nebyl zakoupen
uživatel.
- :guilabel:`Objednané“: produkt byl uživatelem zakoupen a čeká na odeslání.
Prodejce byl odstraněn aplikačním manažerem **Lunchu**.
- :guilabel:`Odesláno do výroby“: objednávka na produkt byla odeslána k dodavateli aplikací **Lunch**
manažer.
- :guilabel:`Přijato“: produkt byl dodán prodejcem do místa uživatele a
byla ověřena jako přijatá aplikačním manažerem Lunchu.

Množství produktu lze upravit kliknutím na ikonku „Plus“ nebo
Ikony „minus“ vlevo od uvedeného produktu. Cena produktu
v reálném čase upravuje cenu podle aktuálně vybraného množství produktu.

Vpravo od souhrnu objednávky se zobrazí informace o nákupu.
V poli „Celková částka“ se zobrazuje celkový účet za objednávku oběda na daný den. V poli „Už zaplaceno“
Hodnota pole ukazuje, kolik bylo zaplaceno za daný den k celkové částce.
V poli „Zaplatit“ se zobrazuje, kolik zbývá ze zbytku částky „Celkem“.
pro umístění aktuálně konfigurované objednávky.

.. obrázek: objednávky/vaše_objednávka.png
:alt:Sekce „Vaše objednávky“ na přehledu s informacemi o nákupu.

.. tip::
Uživatelé mohou během dne vkládat více objednávek a nejsou omezeni na jedinou.
objednávku oběda každý den. Může být potřeba více objednávek, protože uživatelé zapomněli přidat
položky v objednávce nebo pokud je k dispozici více jídel, která lze zakoupit.
kancelář (nejen oběd), a tak dále.

V závislosti na různých dodavatelích a tom, jak jsou dodavatelé a produkty nakonfigurovány, je možné
objednat snídani, oběd, večeři, kávu a nebo nějaké drobné pochutiny.

Pokyn k provedení objednávky
---------------

Pro zadání objednávky klikněte na tlačítko „Objednat teď“ v pravé části obrazovky „Vaše
Shrnutí objednávky. Uživatel je účtován částka zobrazená v poli „Zaplatit“.
A cena se odečte z jejich účtu Lunch.

Jakmile je objednávka zadána, tagy pro zakoupené položky se objeví v poli „Vaše objednávka“
změna z oranžových štítků „Přijato“ na červené štítky „Objednáno“.

Sledovat objednávku
--------------

Když byly objednávky odeslány dodavatelům, tagy pro položky v seznamu „Vaše objednávka“
souhrnné změny z červených tagů „Přijato“ na modré tagy „Odesláno“.

Jakmile jsou objednávky přijaty a ověřeny, štítky se změní z modrých štítků „Odesláno“ na
zelené štítky „Přijato“.

Přijmout objednávku
----------------

Když jsou objednávky přijaty na dodací místo, potvrdí je manažer aplikace **Lunch**.
A zaměstnanci, kteří jídlo objednali, obdrží oznámení.

Moje objednávky
=========

Pro zobrazení celého seznamu objednávek v aplikaci Lunch pro aktuálně přihlášeného uživatele
Navigovat na: Menu Selection: „Obědová aplikace“ --> „Moje obědy“ --> „Můj seznam objednávek“. To vás přenese do
Dashboard „Moje objednávky“. Data jsou filtrována podle „Moje objednávky“ a seskupena
:guilabel:`Datum objednání: den`, které jsou v hledací liště.

Všechny produkty se zobrazují v seznamovém pohledu uspořádaném podle data. Seznam zobrazuje datum objednávky,
:guilabel:„Dodavatel“, :guilabel:„Produkt“, :guilabel:„Příslušenství“, :guilabel:„Poznámky“, :guilabel:„Uživatel“
:guilabel:„Místo oběda“, „Cena“ a „Stav“. Pokud je
více společností, pak se v databázi objeví i sloupec „Společnost“.

Celkové náklady na každou objednávku jsou zobrazeny v řádku s datem objednání.
Seznam se nachází pod všemi řádky a celková částka za všechny objednávky je uvedena pod
:guilabel:`Cena“ sloupec.

Na konci každé produktové řady s stavem „Objednané“ nebo „Odeslané“ se zobrazí
Vyberte možnost „Zrušit“ (Cancel) nebo „Zrušit“ (X Cancel).
objednávka produktu byla zrušena, peníze za zakoupený produkt jsou vráceny a objevují se
uživatelský účet.

Na konci každé produktové řady s stavem „Přijato“ je tlačítko „Znovu objednat“.
se objeví. Klikněte na tlačítko „Znovu uspořádat“ a okamžitě se zobrazí stejný produkt s týmiž příplatky.
aplikovatelné. Nový stav se objeví v seznamu, pod aktuálním datem a produkt bude zaplacen.
S odečtením peněz z účtu uživatele.

.. obrázek: objednávky/moje-objednávky.png
:alt: Zobrazení seznamu, které se zobrazí při přechodu na panel „Můj nákupní košík“.

Můj účet
==========

Pro zobrazení souhrnu všech transakcí v účtu uživatele přejděte na: „Obědová aplikace
--> Moje obědová pauza --> Můj účet „Historie“. To odhalí panel „Moje účty“.

Výchozí zobrazení panelu „Můj účet“ zobrazuje všechny položky od nejnovějších.
nejstarší. Jediné pole, které je nutné vyplnit, jsou pole „Datum“, „Popis“ a „Částka“.
zobrazené v seznamu.

V poli „Částka“ je uvedená záporná hodnota, což znamená, že jde o produkty zakoupené.
v aplikaci Lunch. Ty se zobrazují v formátu „$ XX.XX“.

Vstupy s kladným zůstatkem buď znamenají přidání peněz na účet stravování uživatele nebo
Zrušené objednávky, které byly nakonec vráceny uživateli. Tyto se zobrazují ve formátu „$XX.XX“.

.. obrázek: objednávky/můj účet.png
:alt:Přístupová stránka „Můj účet“ s vstupem pro přidání peněz na účet stravování uživatele.
