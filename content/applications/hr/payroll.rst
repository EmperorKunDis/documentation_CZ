Zobrazit obsah

=======
Mzdy
=======

Odoo Payroll se používá k zpracování pracovních vstupů a vytváření výplatních pásek pro zaměstnance.
s dalšími aplikacemi Odoo, jako jsou například *Zaměstnanci*, *Čas dovolené*, *Přítomnost* a *Plánování*

Aplikace Payroll pomáhá zajistit, aby při ověřování pracovních vstupů nebyly žádné problémy nebo konflikty.
dále se zabývá lokalizacemi zemí, aby mzdy odpovídaly místním pravidlům a daním.
umožňuje přidělování platu.

Nastavení
========

Konfigurujte aplikaci „Mzdy“ přes:menuselection:„Aplikace Mzdy --> Konfigurace“.
Nastavení“. Různé nastavení účetnictví, lokalizace, dovolených, upozornění a výplatních pásek
viz zde.

.. _účetnictví mezd:

Účetnictví
----------

Konfigurační část účetnictví se týká tří možností:

- :guilabel:`Příjmy ze mzdy“: zapněte tuto možnost, pokud chcete zadat platové výměry do účetnictví.
- :guilabel:`Mzdy SEPA“: zapněte tuto možnost pro vytváření SEPA plateb.
- :guilabel:`Přesunout účetní záznamy“: zapněte tuto možnost, abyste měli pouze jeden účetní záznam
vytvořené z účetních záznamů za stejné období. To zabraňuje generování
jednorázové platby.

..._lokalizace platů:

Lokalizace
-------------

*Lokální nastavení* představují země specifické konfigurace, které jsou vytvořeny při vytváření
databáze, která zahrnuje všechny daně, poplatky a příspěvky pro konkrétní zemi.

V sekci „Lokalizace“ aplikace „Mzdy“ na stránce nastavení může být uvedeno
Specifické nastavení, které je potřeba pro danou zemi. Tato volba také nabízí
podrobný přehled všech benefitů, které zaměstnanci dostávají.

Zobrazené nastavení a možnosti se mohou lišit v závislosti na zvoleném jazyku.
databáze.

.. varování:
Není doporučeno měnit nastavení lokalizace, pokud není vyžadováno.

.. poznámka::
Odoo umí pracovat s více společnostmi. Toto se obvykle dělá, když je hlavní
sídlo společnosti nebo kanceláře, jako je například centrála, a v okolí jsou další pobočky
země nebo kus světa, které spadají pod hlavní společnost nebo sídlo. V Odoo je každá firma
včetně sídla by byly zřízeny jako samostatná společnost/pobočka v rámci holdingu.
metoda.

Každá jednotlivá společnost může mít jiný nastavení lokality, protože lokalita se může lišit.
kdekoliv na světě, kde jsou jiné zákony a předpisy.

Více informací o společnostech najdete v sekci :doc:`Společnosti <../general/companies>
dokumentace, která popisuje, jak založit společnost.

Volno
--------

- :guilabel:`Odložený čas na dovolenou“: pokud je dovolená vybrána po schválení výplatních pásek,
musí být aplikována na následující platový období. Vyberte osobu, která bude informována
v těchto konkrétních situacích volno použít z roletky v poli „Zodpovědný“.

...... příklad::
Zaměstnanec dostává výplatu 15. v měsíci a poslední den v měsíci. Výplatní pásky jsou
obvykle zpracovává den předem.

Pokud je zaměstnanci vyplacená mzda schválena a zpracována až 30., ale ten samý zaměstnanec si vezme
Pokud se vám dne 31. ledna přihodí nečekaná nemoc, musíte si volno zaznamenat.

Protože zaměstnanec již dostává mzdu za běžný pracovní den 31., aby si zachoval volno
jsou správné, nemocenský den se přesouvá na první den následujícího měsíce (další výplata
období.

Mzdy
-------

- Zadejte počet dní před uplynutím smlouvy:
smlouva vyprší a Odoo oznamuje zodpovědné osobě blížící se vypršení.
času.
- Vyplňte počet dní před vypršením platnosti povolení k práci.
pracovní povolení vyprší a Odoo oznamuje zodpovědné osobě blížící se vypršení.
V té době.
- :guilabel:`Zobrazit platovou pásliku ve formátu PDF“: zapněte tuto možnost, aby se zobrazila platová páslika v PDF
je ověřená.

.. _mzdový list/konfigurace vstupů do práce:

Smlouvy
=========

Pokud chce zaměstnanec dostávat plat, musí mít aktivní smlouvu na konkrétní typ práce.
zaměstnání. Vytváření a prohlížení šablon smluv, vytváření a zobrazování pracovních pozic je
možné z této části nastavení hlavičky menu.

... _smlouvy/šablony mzdy:

Šablony
---------

Šablony smluv se používají při zaslání nabídky kandidátovi.
Šablona smlouvy tvoří základ nabídky a lze ji upravit pro konkrétní kandidáty nebo
zaměstnanci, pokud je potřeba. Pokud se vytváří nebo upravuje šablona smlouvy ve *Mzdách*,
aplikaci, změny se odrážejí také v aplikaci *Nabídka práce*.

.. důležité::
Pro přístup k šablonám smluv je nutné mít nainstalovaný modul *Salary Configurator* (hr_contract_salary).
:ref:`nainstalovaný <general/install>`.

Pro zobrazení všech aktuálních šablon smluv v databázi přejděte na: „Mzdy“
--> Konfigurace --> Smlouvy: Šablony.

Na stránce „Šablony smluv“ se zobrazují všechny aktuální šablony smluv v přehledovém zobrazení.
Zobrazit podrobnosti šablony smlouvy, klikněte na jakoukoli část řádku, abyste otevřeli formulář smlouvy.
Šablona smlouvy může být upravena z tohoto tvaru. Postupujte podle svých přání a
smlouva.

Pro vytvoření nového šablonového kontraktu klikněte na tlačítko „Nový“. Pak zadejte následující
informace, která se objevuje v prázdném smluvním šabloně:

- :guilabel:`Referenční smlouva“: Vložte stručný popis šablony.
a snadno pochopitelné, neboť se objevuje i v aplikaci Recruitment.
- :guilabel:`Práce“: vyberte požadovaný pracovní režim, na který se vztahuje smlouva z
příkazem „Drop down“. Pokud je potřeba nový rozvrh směn, vytvořte si :ref:`nový rozvrh
<pracovní smlouva/nový pracovní rozvrh>.
- Vyberte zdroj vstupu práce: vyberte, jak jsou pracovní záznamy generovány. Možnosti jsou buď

  - :guilabel:`Plán práce“: pracovní záznamy se generují na základě vybraného plánu práce.
  - :guilabel:`Přítomnost na pracovišti“: pracovní záznamy jsou generovány podle docházky zaměstnance.
Tyto docházky jsou evidovány v aplikaci *Přítomnosti*. Podívejte se na odkaz:
dokumentaci k této funkci pro informace o přihlášení a odhlášení.
  - :guilabel:`Plánování“: vstupy práce se generují na základě plánu zaměstnance
Žádost o povolení stavby.

- Vyberte typ struktury mzdy: vyberte z nabídky
Vyberte možnost „<výplatní páska/struktura typů>“ z rozevírací nabídky.
- :guilabel:`Oddělení“: vyberte oddělení, na které se vzor smlouvy vztahuje z roletky
menu. Pokud je prázdné, aplikuje se na všechny oddělení.
- Vyberte pozici v pracovním poměru: vyberte pozici v pracovním poměru
Vyplňte šablonu z nabídky. Pokud je prázdné, aplikuje se na všechny pracovní pozice.
- :guilabel:`Mzda na mzdovém listu“: do pole zadejte měsíční plat.
- :guilabel:`Typ smlouvy“: vyberte typ smlouvy z nabídky. Seznam je
Stejně jako u typů zaměstnání:ref:`<payroll/employment-types>`.
- :guilabel:`Odpovědná osoba HR“: vyberte zaměstnance odpovědného za ověřování smluv pomocí tohoto
šablona z nabídky.
- :guilabel:`Nový šablonový dokument smlouvy“: vyberte výchozí dokument, který musí nový zaměstnanec podepsat
podepsat smlouvu o přijetí nabídky.
- :guilabel:`Smluvní dokument aktualizace šablony“: vyberte výchozí dokument, který bude mít stávající zaměstnanec
musí podepsat, aby aktualizovali svůj kontrakt.

.. obrázek: platová/smluvní šablona.png
:align:center
:alt: Nový vzor smlouvy, ve kterém jsou vyplněny všechny pole.

Tabulka s informacemi o platu
~~~~~~~~~~~~~~~~~~~~~~

- Vyberte buď „Plný plat“ nebo „Mzda za hodinu“.
rozbalovací nabídka.
- :guilabel:'Plán platů': z rozevírací nabídky vyberte, jak často je zaměstnanec placen. Možnosti
zahrnuje: guilabel:'Ročně', guilabel:'Půlročně', guilabel:'Čtvrtletně'
:guilabel:`Dvakrát měsíčně“, :guilabel:`Měsíčně“, :guilabel:`Polovinu měsíce“, :guilabel:`Od poloviny do konce měsíce“
:guilabel:`Týdenní“ nebo „Denní“.
- V poli „Mzda“ zadejte hrubou mzdu. V tomto poli je uvedený časový úsek, který se vztahuje na
je vybrán v poli „Plánovaná platba“ a doporučuje se jej zaplnit
:guilabel:`Roční náklady (reálné)“ pole *první* v pořadí, protože tato položka automaticky aktualizuje toto pole.
- :guilabel:`Roční náklady (reálné)“: zadejte celkové roční náklady, které zaměstnanec stojí jeho zaměstnavatele.
Pokud je tato hodnota zadána, automaticky se aktualizuje měsíční náklad (v reálném čase).
- :guilabel:Měsíční náklady (reálné): pole je **neupravitelné**. Hodnota se automaticky
se vyplní po zadání roční náklady (v reálném vyjádření).

.. důležité::
V poli „Plánovaná platba“, „Mzda“ a „Roční náklady (reálné)“ jsou všechna pole
spojené. Pokud se změní v kterémkoli z těchto polí, automaticky se změní i ostatní dva pole, aby odrážela
přepis. Doporučuje se zkontrolovat tyto tři pole v případě jakýchkoliv změn.
aby byly přesné.

.. obrázek: platove-informace.png
:align:center
:alt:Tabulka s informacemi o platu, kde jsou pole vyplněna.

Před daňové výhody a po daňových odpočtech
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Podle nastavení lokalizačních parametrů společnosti se v této části zobrazují
nebo se mohou vůbec neobjevit.

Například některé záznamy se mohou týkat důchodového pojištění, zdravotního pojištění a
přímé výdaje na dopravu.

Zadejte finanční částky nebo procenta, abyste specifikovali, kolik z platu zaměstnance jde na
různé výhody a slevy.

... _mzdy/druhy zaměstnání:

Druhy zaměstnání
----------------

Pro zobrazení všech přednastavených typů zaměstnání přejděte na:
Konfigurace --> Smlouvy: Druhy zaměstnání.

Druhy zaměstnání jsou zobrazeny v seznamovém pohledu na stránce „Zaměstnání“.

Výchozí typy zaměstnání jsou: „Plný úvazek“, „Dohoda o provedení práce“ a „Sezónní“.
„Dobrovolník“, „Plný úvazek“, „Částečný úvazek“ a „Trvalý“.

Chcete-li vytvořit nový typ zaměstnání, klikněte na tlačítko „Nový“ v pravém horním rohu a
Na stránce „Druhy zaměstnání“ se objeví prázdná řádka.

Do nové prázdné řádky zadejte název typu zaměstnání do sloupce „Jméno“. Pokud
Zaměstnání je země specifické, vyberte zemi pomocí rozbalovací nabídky v
:guilabel:`Země“ sloupec. Pokud je vybrána země, pak platí, že typ zaměstnání se vztahuje
pro danou zemi.

Pro přeřazení typů zaměstnání klikněte na ikonu šesti malých šedivých boxů.
vlevo od typu zaměstnání: guilabel:„Jméno“ a přetáhněte čáru na požadovanou pozici
list.

.. obrázek: platove-priznaky-zamestnani.png
:align:center
:alt:Zaměstnání v databázi výchozího nastavení, ve formátu seznamu.

.. _mzdy/pracovní záznamy:

Dílčí položky práce
============

„Pracovní vstup“ je jednotlivý záznam na pracovním listu zaměstnance. Pracovní vstupy lze konfigurovat tak, aby
zahrnuje všechny druhy práce a volno, například:guilabel:`Přítomnost na pracovišti“, „Čas nemocenské“
Off`, „Školení“ nebo „Svátky“.

.. viz též:
:doc:`Správa záznamů o práci (<payroll/work_entries>)“

Typy vstupů do práce
----------------

Při vytváření záznamu o práci v aplikaci Mzdy nebo když zaměstnanec zadá nový typ dovolené
V aplikaci „Čas volna“ je potřeba vybrat typ vstupu do práce. Seznam
Pole „Druhy vstupu do práce“ je automaticky vytvořeno podle nastavení lokalizace, které jsou ve
databáze.

Pro zobrazení dostupných typů pracovních vstupů přejděte na: „Mzdy --> Konfigurace
--> Práce - Vstupy do práce --> Druhy vstupů do práce.

Každý typ záznamu práce má kód, který pomáhá při vytváření výplatních pásek a zajišťuje všechny daně a poplatky.
jsou správně zadány.

.. obrázek: platové/druhy-pracovních-vstupů.png
:align:center
:alt: Seznam všech typů pracovních vstupů dostupných k použití s číslem účtu a barvou.

Nový typ vstupu do práce
~~~~~~~~~~~~~~~~~~~

Pro vytvoření nového typu záznamu o práci klikněte na tlačítko „Nový“ a zadejte
informace pro následující části na formuláři.

Oddělení obecných informací
***************************

- :guilabel:`Název typu vstupu do práce“: název by měl být krátký a výstižný, například „Čas nemoci“.
„Svátky“.
- :guilabel:`Kód mzdy“: Tento kód se zobrazuje u položek typu „pracovní doba“ na časových listinách a výplatních páskách.
Protože kód se používá v souvislosti s aplikací *Účetnictví*, je doporučeno zkontrolovat
s účtárnou o kód, který bude používat.
- :guilabel:`Externí kód“: tento kód se používá pro vývoz dat do externích služeb mzdového účetnictví.
Zkontrolujte třetí stranu, která je používána k určení externího kódu, který chcete zadat pro
nový typ vstupu do práce.
- :labelcolor: Vyberte barvu pro konkrétní typ pracovního záznamu.

Zobrazení v sekci výplatní pásky
**************************

- :guilabel:`Způsob zpracování“: způsob zpracování zvolený určuje, jak se budou počítat množství na záznamy o čase.
Jsou zobrazeny na výplatním lístku.

  - :guilabel:`Žádné přehrávání“: vstup není upraven.
  - :guilabel:`Půl denní vstupenka“: Vstupné se započítává na nejbližší půldenní částku.
  - :guilabel:`Den`: vstup je převeden na nejbližší celé denní částku.

.. příklad::
Pokud je nastavená pracovní doba na osmihodinový pracovní den (čtyřicetihodinová pracovní týden), a zaměstnanec vstoupí
Čas na vstup do práce je 5,5 hodiny a nastavení „Zpracování“ je „Žádné zpracování“,
zůstává 5,5 hodiny. Pokud je nastaveno :guilabel:`Rounding“ na :guilabel:`Half Day“, pak
změněno na 4 hodiny. Pokud je nastaveno na „den“, pak se mění na 8 hodin.

Neuhrazená částka
**************

- :guilabel:„Neplacená v Typu struktury“: pokud je pracovní záznam pro práci, která není placená, uveďte
která platová struktura se na výběr z nabídky vztahuje. Některé situace
kde se pracovní doba zaznamenává na výplatním lístku, ale neposkytuje se žádné odměny za neplacené stáže.
neplacené vzdělávání nebo dobrovolnická práce.

Platí pro část výhod
****************************

- :guilabel:Stravenka“: pokud má pracovní vstup započítávat se stravenkou, zaškrtněte políčko.
- :guilabel:`Příspěvek na reprezentaci“: pokud má být práce zahrnuta do příspěvku na reprezentaci, zaškrtněte
krabici.
- :guilabel:`Vrácení soukromého automobilu“: pokud by měl pracovní vstup započítat do soukromého automobilu
vrácení peněz, zaškrtněte políčko.

Sekce o volných dnech
************************

- :guilabel:`Čas dovolené“: zaškrtněte tuto políčko, pokud chcete vybrat typ práce pro čas dovolené.
žádost nebo vstup v aplikaci Time Off.

Pokud je zaškrtnuto políčko „Čas volna“, objeví se pole „Typ času volna“. To pole obsahuje
nabídku rozbalovacího menu pro výběr konkrétních typů dovolené, například „Placená dovolená“, „Dovolená za nemoc“
například „Pracovní doba navíc“

Do pole se může zadat nový typ dovolené, pokud jsou ve výčtu uvedeny všechny druhy dovolené.
Nepožadované volby v rozbalovacím menu nezobrazují typ dovolené.

Oddíl ohlášení
*****************

- :guilabel:`Nepředvídaná absence“: pokud se má pracovní záznam zobrazit v nepředvídatelných absencích
Pokud chcete zprávu zaslat e-mailem, zaškrtněte tuto políčko.

.. obrázek: platová/nová-pracovní-smlouva-druh.png
:align:center
:alt: Nový vstupní formulář pro novou práci s veškerými poli, která je třeba vyplnit.

.. _mzdy/pracovní doba:

Práce v rozvrhu
-----------------

Pro zobrazení aktuálně nastavených pracovních úvazků přejděte na:
Konfigurace --> Záznamy o práci --> Plány směn. K dispozici jsou plány směn
v seznamu najdete smlouvy zaměstnanců.

Rozvrh práce je společností specifický. Každá společnost **musí** identifikovat každý typ rozvrhu práce
používají. Pokud je databáze vytvořena pro pouze jednu společnost, sloupec společnosti není k dispozici.

.. příklad::
Řešení Odoo pro více společností, které používají standardní pracovní dobu 40 hodin, musí
mít samostatný záznam pracovního rozvrhu pro každou společnost, která používá 40hodinový týdenní úvazek.

Databáze s pěti společnostmi, které všechny používají standardní pracovní dobu 40 hodin, musí mít
40hodinové pracovní plány oddělené.

.. obrázek: platové tabulky/směnnost.png
:align:center
:alt:Všechny pracovní plány, které jsou v současné době k dispozici ve firmě, jsou zadány do databáze.

.. _mzdy/nový pracovní rozvrh:

Nový pracovní režim
~~~~~~~~~~~~~~~~~~~~

Pro vytvoření nového pracovního rozvrhu klikněte na tlačítko „Nový“ a zadejte potřebné informace do
forma.

Záložky jsou automaticky vyplněny pro běžnou pracovní dobu 40 hodin, ale mohou být upraveny. Nejprve změňte
název pracovní doby upravit text v poli „Jméno“. Poté proveďte
úpravy dnů a časů, které se vztahují na nový pracovní režim.

V záložce „Časová doba“ upravte „Dny v týdnu“, „Časový úsek“.
a vyberte možnost „Druh vstupu do práce“ kliknutím na rozbalovací nabídku v každé sloupci.
výběr požadovaných hodnot. Sloupce „Pracovní doba“ a „Pracovní od“ jsou upraveny
Zadáním času.

.. poznámka::
Časy „Pracovat od“ a „Pracovat do“ musí být ve formátu 24 hodin. Například
„Dva hodiny odpoledne“ by se zadávalo jako „14:00“.

Pokud má být pracovní doba ve dvoutýdenním uspořádání, klikněte na tlačítko „Přepnout na 2 týdny“.
kalendář“ v levém horním rohu. To vytvoří položky pro „Souběžný týden“.
:guilabel:`Nevyhovující týden“.

.. obrázek: platová/nové-pracovní-rozvržení.png
:align:center
:alt: Nový tiskopis pro pracovní dobu.

Mzda
======

.. _struktura platů:

Strukturální typy
---------------

V Odoo se strukturální typy používají k identifikaci skupiny lidí odkazujících na stejná pravidla pro výplatu mzdy.
Struktura typu obsahuje konkrétní možnosti a podmnožinu struktur, které budou použity.
situaci.

V Odoo se platová páska zaměstnance vytváří na základě struktur a typů struktur, které ovlivňují způsob
Do časových listin zadává zaměstnanec údaje. Každý typ struktury je samostatný soubor pravidel pro zpracování
evidenci pracovní doby, která se skládá z různých struktur vložených do ní. Typy struktury definují, jak
Často se platí i přesčasové hodiny, případně je-li mzda odměňována paušálně.
kolik hodin zaměstnanec pracoval (různé).

Příkladem struktury může být typ Employee a tento typ by měl mít dvě různé
struktury v ní: strukturu „Pravidelná platba“, která obsahuje všechny samostatné pravidla pro zpracování
pravidelná mzda i struktura pro „Bonus na konci roku“, která zahrnuje pouze pravidla pro
bonus na konci roku. Oba „struktury“ Regular Pay a End of Year Bonus jsou struktury
v strukturovaném typu „Zaměstnanec“.

Různé :guilabel:`Struktury typů“ lze vidět při procházení :menuselection:`Mzdovou aplikací
--> Konfigurace --> Mzdy: Typy struktury.

Do Odoo jsou přednastaveny dvě struktury typů zaměstnanců a pracovníků: :guilabel:`Employee` a :guilabel:`Worker`.

Typicky se používá třída :guilabel:`Employee`, a proto je pro plat zaměstnance vhodná třída
„Měsíční pevná mzda“ a „Dělník“ se obvykle používají pro zaměstnance, kteří jsou placeni
hodinová mzda, takže typ mzdy je:guilabel:`Mzda za hodinu.

.. obrázek: platová/struktura-typ.png
:align:center
:alt: Seznam všech aktuálně konfigurovaných typů struktury k použití.

... _mzdy/nový typ struktury:

Nový typ struktury
~~~~~~~~~~~~~~~~~~

Pro vytvoření nového typu struktury klikněte na tlačítko „Nový“ a vyplňte prázdný formulář pro typ struktury.
se objevuje.

Pokračujte v zadávání informací do polí. Většina polí je předvyplněna, ale všechny pole lze
upraveny.

- :guilabel:`Typ struktury“: zadejte název nového typu struktury, například „Zaměstnanec“ nebo
„Dělník“.
- :guilabel:`Země“: vyberte z roletky zemi, pro kterou se nový typ struktury vztahuje.
menu.
- Vyberte typ mzdy, který nový strukturální typ používá, buď


Pokud má být typ použit pro zaměstnance na plný úvazek, kteří dostávají stejnou mzdu každý měsíc.
vyberte:guilabel:"Pevná mzda".

Pokud má být typ použit pro zaměstnance, kteří dostávají mzdu podle počtu odpracovaných hodin
během platového období vyberte „Mzdu za hodinu“.
- Vyberte typ platby pro nový strukturální typ z:
rozbalovací nabídka. Možnosti jsou: guilabel:„Měsíční“, „Čtvrtletní“
:guilabel:`Půlročně“, :guilabel:`Ročně“, :guilabel:`Týdně“, :guilabel:`Dvakrát týdně“
:guilabel:`Dvakrát za měsíc“. Toto označuje, jak často je tento konkrétní typ struktury vyplácen.
- :guilabel:`Výchozí pracovní doba“: vyberte výchozí pracovní dobu pro nový typ struktury
z roletky. Všechny dostupné pracovní hodiny pro aktuálně vybranou společnost se zobrazí v
nabídce. Výchozí pracovní doba, která je přednastavena v Odoo, je
:guilabel:`Možnost 40 hodin týdně“ a pokud potřebné pracovní hodiny nejsou v seznamu,
a:ref:`nový pracovní režim lze vytvořit <new-default-working-hours>“.
- :guilabel:`Běžná platová struktura“: zadejte název pro běžnou platovou strukturu.
je používán jako výchozí volba při tvorbě mezd.
- :guilabel:`Výchozí typ vstupu do práce“: pro zaměstnance, jejichž pracovní smlouva je uvedena pod tímto
Struktura typu, hlavní práce vstupního typu používané pro všechny období práce je definována zde.
obvykle je nastaveno na **Přítomnost**.

:guilabel:`Práce z domova“, :guilabel:`Nedostatek placené dovolené“, „Čas na nemocenskou“, „Placený čas
Off`, „Vypršení smlouvy“, „Pracovní doba navíc“ a „Dlouhodobé volno“.

Pro zobrazení všech možností výchozího typu pracovní položky klikněte na tlačítko „Hledat“.
V dolní části seznamu klikněte na tlačítko „Více...“.

Podle nastavení lokalizace se může tento seznam rozšířit o další možnosti.
výchozí volby.

.. obrázek: platová/nová-struktura.png
:align:center
:alt: Nový typ struktury pro vyplnění při vytváření nového typu struktury.

..._nový výchozí pracovní režim:

Nový standardní pracovní čas
~~~~~~~~~~~~~~~~~~~~~~~~~

Pro vytvoření nových výchozích pracovních hodin zadejte název pro nové pracovní hodiny do:
Pole „Délka směny“ na novém typu struktury formuláře. Klikněte na tlačítko „Vytvořit a upravit“. Výchozí
zobrazí se okno s nastavením pracovní doby. Výchozí okno pro nastavení pracovní doby má dvě části - obecné informace
sekci a záložkou, která uvádí všechny pracovní hodiny dne a času.
ukončeno, klikněte na tlačítko „Uložit a zavřít“.

- :guilabel:`Jméno“: zadejte název nového výchozího časového rozmezí, které by mělo být popisné
a srozumitelné, jako například „Standardní pracovní doba 20 hodin týdně“.
- :guilabel:`Společnost“: vyberte společnost, která může tyto nové výchozí pracovní hodiny používat
rozbalovací nabídka. Prázdné pole znamená, že je k dispozici pro všechny společnosti.
- :guilabel:Průměrný počet hodin za den: pole průměrného počtu hodin za den je automaticky vyplněno na základě
nastavené v záložce „Práce“. Tento údaj ovlivňuje zdroj
plánování, protože průměrné denní hodiny ovlivňují, jaké zdroje lze využít a v jakém množství.
za jeden pracovní den.
- :guilabel:`Časová zóna“: vyberte časovou zónu, která se má použít pro nové výchozí pracovní hodiny.
rozbalovací nabídka.
- :guilabel:`Plný úvazek společnosti“: zadejte počet hodin týdně, které by zaměstnanec měl pracovat
aby se považoval za plnohodnotného zaměstnance. Obvykle je to přibližně 40 hodin týdně, a toto číslo
mění druhy benefitů, které zaměstnanec může získat podle svého pracovního poměru

- :guilabel:`Sazba za pracovní dobu“: tento procentuální údaj je automaticky vypočítán na základě hodnoty v poli
:guilabel:`Plný úvazek“ a nastavené pracovní hodiny v záložce „Pracovní doba“.
tabulka. Toto číslo by mělo být mezi 0,00 % a 100 %, takže pokud je procento vyšší než 100 %, je
to znamená, že je třeba upravit pracovní dobu a/nebo hodiny „plného úvazku“ v :guilabel:`Společnosti plný úvazek`.
- Karta „Časová doba“: tato karta obsahuje konkrétní pracovní hodiny každého dne.
Když je vytvořen nový výchozí formulář pracovní doby, karta „Pracovní doba“
s přednastaveným čtyřicetihodinovým týdnem, který je rozdělen na tři časové úseky.

Každý den má dopoledne (od 8. do 12. hodiny), oběd (od 12. do 13. hodiny) a odpoledne (od 13. do 17. hodiny).
je nastaven na 24 hodinový formát času.

Chcete-li upravit hodinu na kterémkoliv z těchto políček, klikněte na konkrétní pole a provádějte úpravy.
v případě kategorie času zadejte požadovanou hodnotu.

Pamatujte na to, že pracovní doba je pro každou firmu specifická a nelze ji sdílet mezi firmami.
Společnost musí mít vlastní pracovní dobu stanovenou.

.. poznámka::
Pokud pracovní doba není každý týden stejná a je na dvoutýdenním rozvrhu
místo toho klikněte na tlačítko „Přepnout na kalendář s dvouměsíční periodou“ v horní části nového výchozího
pracovní dobu, což mění záložku „Práce“ tak, aby zobrazila dva týdny.
pracovní doby, které lze upravit.

Struktury
----------

„Mzdové struktury“ jsou různé situace, za kterých by zaměstnanec mohl být placen.
*struktura* a jsou konkrétně definovány různými pravidly.

Počet struktur, které společnost potřebuje pro každý typ struktury, závisí na tom, kolik různých způsobů
Jak zaměstnanci dostávají zaplaceno a jak se jejich plat vypočítává. Například běžný model může být
Užitečné může být i „Bonus“.

Pro zobrazení všech různých struktur pro každý typ struktury přejděte na:
Konfigurace --> Mzdy --> Organizační struktura.

Každá :ref:`struktura typu <payroll/structure-types>` uvádí různé struktury spojené s
Každá struktura obsahuje sadu pravidel, která ji definují.

.. obrázek: platová struktura.png
:align:center
:alt: Všechny dostupné platové struktury.

Klikněte na strukturu, abyste viděli její „Pravidla pro výplatu“. Tyto pravidla definují, jak bude vypadat výplatní páska.
bude vypočítána pro zaměstnance.

.. obrázek: platová/struktura-pravidla-platu.png
:align:center
:alt:Podrobnosti o struktuře platů pro pravidelnou mzdu, které uvádějí všechny specifické pravidla platů.

Pravidla
-----

Každá struktura má sadu pravidel pro výpočet mzdy, která se používá k vypočítání různých částek zahrnutých v platbě.
Tyto pravidla jsou konfigurována lokálními nastaveními a ovlivňují výpočet mezd.
Vytváření pravidel by mělo být prováděno pouze tehdy, když je to nezbytné.

Pro zobrazení všech pravidel přejděte na: „Mzdy --> Konfigurace --> Mzda --> Pravidla“.
Klikněte na strukturu (například :guilabel:`Regular Pay`) pro zobrazení všech pravidel.

Pro vytvoření nového pravidla klikněte na tlačítko „Nový“. Vyplňte následující informace
na polích.

Horní část
~~~~~~~~~~~

- :guilabel:`Název pravidla“: Zadejte název pro tento pravidlo. Toto pole je povinné.
- :guilabel:`Kategorie“: vyberte kategorii, na kterou se pravidlo vztahuje z roletky nebo zadejte
nový. Toto pole je povinné.
- :guilabel:`Kód“: zadejte kód, který bude použit pro tuto novou pravidlo. Toto pole je povinné.
- :guilabel:`Pořadí“: zadejte číslo, které určuje, kdy je tato pravidla vypočítána v pořadí
všechny ostatní pravidla.
- :guilabel:`Struktura mzdy“: vyberte strukturu mezd, na kterou se pravidlo vztahuje z rolovací nabídky
menu nebo zadat nové. Toto pole je povinné.
- :guilabel:`Aktivní“: zapněte tuto možnost, aby pravidlo bylo k dispozici pro použití. Zakažte tlačítko,
bude dál uvádět na výplatních páskách, ale počítání se vynechá.
- :guilabel:`Zobrazení na výplatním lístku“: zaškrtněte políčko, pokud chcete pravidlo zobrazit na tiskopise
pracovní smlouva, mzda a výplatní páska.
- Zatrhněte políčko „Přidat do přehledu nákladů na zaměstnance“ a pravidlo se objeví v
:guilabel:`Náklady na zaměstnance“ v přehledu aplikace *Mzdy*.
- :guilabel:`Zobrazení v přehledu mzdy“: zaškrtněte políčko, aby se pravidlo zobrazilo na výplatní pásce
zprávy.

.. obrázek: platová/pravidla.png
:align:center
:alt: Do nového formuláře pro nové pravidlo zadejte informace o novém pravidle.

Obecné nastavení
~~~~~~~~~~~

Podmínky
**********

- Výchozí podmínka: vyberte z roletky, jestli je
:guilabel:`Vždy platí“ (vždy se vztahuje), :guilabel:`Interval“ (se vztahuje na určitý interval)
je vložena pod výběrem, nebo :guilabel:`Pythonový výraz“ (kód je zadán pod výběrem
(vybrané položky). Toto pole je povinné.

Počítání
***********

- Výše platby: vyberte z roletky, jestli je částka pevná nebo variabilní.
částka, procenta (%) nebo Python kód. V závislosti na tom, co
Vyberte si, zda chcete pevnou částku, procento nebo Pythonový kód.
je nutné.

Příspěvek zaměstnavatele
********************

- :guilabel:`Příspěvkový partner“: pokud jiná společnost finančně přispívá na tento předpis, vyberte společnost
z nabídky.

Popisová záložka
~~~~~~~~~~~~~~~

Pokud chcete, můžete doplnit informace v této záložce, aby bylo pravidlo jasnější. Tato záložka se zobrazí pouze
forma pravidla.

Karta účetnictví
~~~~~~~~~~~~~~

- :guilabel:`Účet kreditní karty“: vyberte účet kreditní karty, který se tato pravidla týká.
- :guilabel:`Účet kreditu“: vyberte účet kreditu z roletky, na který se pravidlo vztahuje.
- Pokud je zaškrtnuto, bude se zobrazit částka pravidla.
nezávisle na čisté mzdě, aby bylo možné lépe reportovat v účetnictví.

Jiné typy vstupů
-----------------

Při vystavování výplatních pásek je někdy nutné přidat další položky pro specifické okolnosti.
jako výdaje, náhrady nebo odpočty. Tyto další vstupy lze konfigurovat kliknutím na
:menu:Mzdy --> Konfigurace --> Mzda --> Jiný typ vstupu.

.. obrázek: platová/další vstupy.png
:align:center
:alt: Seznam dalších typů vstupu pro mzdy, které lze vybrat při vytváření nového záznamu
výplatní páska.

Chcete-li vytvořit nový typ vstupu, klikněte na tlačítko „Nový“. Zadejte popis a
:guilabel:`Kód“ a k jaké struktuře se vztahuje v „Dostupnost v struktuře“.
pole.

.. důležité::
V pravidlech mzdy se používá :guilabel:`Kód`, který slouží k výpočtu mezd.
:guilabel:"Dostupnost v struktuře" pole je prázdné, znamená to, že nový typ vstupu
je k dispozici pro všechny výplatní pásky a není exkluzivním prvkem konkrétního struktury.

.. obrázek: platová pásma/vstupní typ nový.png
:align:center
:alt: Nový vstupní typ vyplněný.

.. _pracovní smlouva/druhy příloh k mzdě:

Konfigurátor platových balíčků
===========================

Různé možnosti pod sekcí „Konfigurátor mzdy“ v
Položka „Mzdy“ v nabídce „Nastavení“ -> „Konfigurátor mzdového balíčku“ ovlivňuje
mzda zaměstnance.

Podle toho, jaké informace zaměstnanec zadá (např. slevy, závislé osoby atd.), se
Přihláška je zaslána na webové stránky společnosti, kde se
sekce pod :guilabel:`Konfigurátor mzdy“ přímo ovlivňují to, co uchazeč vidí.
jak je obydlené, jakmile uživatel zadá informace.

Výhody
--------

Při nabídce pracovního místa mohou být v Odoo nastaveny určité výhody navíc.
na mzdu, aby nabídka byla atraktivnější (například přidat volno navíc, používání firemního auta).
kompenzace za telefon nebo internet atd.

Pro zobrazení výhod přejděte na: menu: „Mzdy“ --> „Nastavení“ --> „Mzdový balíček“.
Konfigurátor: Výhody“. Výhody jsou seskupeny podle :guilabel:`Typu struktury“ a výhoda uvedená
pro konkrétní typ struktury je k dispozici pouze pro tuto konkrétní strukturu.

.. obrázek: platove-benefity.png
:align:center
:alt: Seznam všech výhod dostupných pro každý typ struktury.

.. příklad::
Společnost má dva typy struktury, jeden označený jako „Zaměstnanec“ a druhý jako „Vedoucí“.
:guilabel:`Intern“. Struktura typu :guilabel:`Zaměstnanec“ obsahuje výhodu použití
pracovní auto, zatímco struktura typu Intern má k dispozici stravenkový paušál.

Osoba zaměstnaná podle struktury typu :guilabel:`Zaměstnanec` může využít výhody služebního vozu.
nemohou mít stravenky. Osoba zaměstnaná na základě struktury typu „Intern“ by neměla
stravenkový paušál, nikoliv používání firemního automobilu.

Chcete-li vytvořit nový benefit, klikněte na tlačítko „Nový“ a zadejte informace do polí.
prázdný formulář žádosti o dávku.

Výše uvedené jsou různá pole pro vytváření výhod.

Oddělení obecných informací
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :guilabel:`Související pole smlouvy“: vyberte pole z kontraktu ze seznamu.
Vybraná hodnota ze zaměstnance bude zapsaná do pole.
- :guilabel:`Výhody“: Zadejte název výhody. Tento prvek je povinný.
- :guilabel:`Druh výhod“: vyberte z roletky, jaký typ výhod se jedná. Vyberte
:guilabel:`Měsíční příspěvek v hodnotě“ (Benefit in Kind), „Měsíční příspěvek v čisté výši“ (Benefit
„Benefity v hotovosti“, „roční benefity v hotovosti“ nebo „nefinanční benefity“.
Pole je povinné.
- :guilabel:„Cena“: vyberte pole z kontraktu. Vybrané pole se objeví
definovat náklady na výhodu a tím pádem i dopad na mzdu.
:guilabel:`Mzda“, „Mzda s příplatky za přesčas“ a „Sazba mzdy“.
lokální nastavení, můžete si vybrat z dalších možností.
- :guilabel:`Související typ“: z rozevírací nabídky vyberte, jaký druh výhody to je. Vyberte
:guilabel:`Měsíční příspěvek v hodnotě“ (Benefit in Kind), „Měsíční příspěvek v čisté výši“ (Benefit
„Benefity v hotovosti“, „roční benefity v hotovosti“ nebo „nefinanční benefity“.
Pole je povinné.
- :guilabel:`Mzda po odečtení daně z příjmu“: zaškrtněte políčko, pokud má být výhoda započítána do čisté mzdy.
příjem.
- :guilabel:`Požadované dokumenty“: vyberte jakýkoliv dokument, který je nutné předložit pro tento
benefit z nabídky.
- :guilabel:'Povinné výhody': vyberte z roletky požadovanou výhodu
přikázat zaměstnavateli, aby tento konkrétní benefit poskytl zaměstnanci.

Například výhoda pro povinné ručení by do pole „Společnostní automobil“ vkládala hodnotu „Pojištění vozidel“.
umožnit zobrazit výhody pojištění vozidel pouze v případě, že zaměstnanec vybral/zapnul
benefit firemního vozu.
- :guilabel:`Typ struktury mzdy“: vyberte z rolovací nabídky typ struktury mzdy
Vyplňte pole, které se týká výhody.
- :guilabel:`Jednotka měření“: vyberte metriku, podle které je přidělován benefit, pomocí roletky
nabídka. Možnosti jsou: „Dny“, „Procenta“ nebo „Měna“.

.. obrázek: platovka/novy-benefit.png
:align:center
:alt: Nový formulář pro novou smlouvu na internet.

Sekce zobrazení
~~~~~~~~~~~~~~~

- :guilabel:`Název benefitu“: zaškrtněte políčko, pokud chcete, aby se název výhody zobrazoval v platovém balíčku
konfigurátor.
- Vyberte z roletky, jakým způsobem se tento benefit zobrazuje.
možnosti jsou: „Vždy vybrané“, „Rozbalovací seznam“ a „Skupina rozbalovacích seznamů“.
:guilabel:`Posuvník“, :guilabel:`Tlačítka rádia“, :guilabel:`Manuální vstup“ nebo :guilabel:`Text“.
Pole je povinné.

V závislosti na zvoleném nastavení je třeba provést další konfigurace. Například pokud
Pokud je vybrána volba „Rádio“, musí být jednotlivé tlačítka zadány.
- :guilabel:`Ikona“: ikona z knihovny „Font Awesome 4 <https://fontawesome.com/v4/icons/>“
může být viditelný pro tento benefit. Zadejte do pole textový kód ikonky. Například
zobrazit ikonu kufru, do této řádky se zadává kód „fa fa-suitcase“.
- :guilabel:`Skrytí popisu výhody“: zaškrtněte políčko, pokud chcete skrýt popis výhody, pokud je
nebyl vybrán zaměstnancem.
- :guilabel:`Sbaleno“: pokud by mělo být získané právo skryto nebo složeno, protože je závislé na jiném
Vyberte si výhody, zaškrtněte políčko. Po aktivování se zobrazí následující pole:

  - :guilabel:`Štítek složky“: zadejte název pro složku s výhodami, která je složená.
  - :guilabel:`Složka pole Fold Res“: vyberte smluvní pole, ke kterému je tento benefit vázán
výběrové poli. Pokud je tento údaj vyplněn v smlouvě, pak se zobrazí příslušná výhoda.

Sportovní sekce
~~~~~~~~~~~~~~~~

- :guilabel:`Typ aktivity“: z rozevírací nabídky vyberte typ aktivity, který je automaticky
Vytvořené, když zaměstnanec tuto výhodu vybere.
- :guilabel:`Vytvoření aktivity“: vyberte datum vytvoření aktivity, buď když
:guilabel:`Smlouva podepisuje zaměstnanec“, nebo „Smlouva je podepsána“. Kliknutím
zaškrtávací políčko vedle požadovaného výběru.
- :guilabel:`Typ vytváření aktivity“: vyberte parametry pro vytvoření aktivity, ať už
:guilabel:"Když je nastaveno" nebo :guilabel:"Když se změní". Klikněte na tlačítko
tlačítko vedle požadovaného výběru.
- :guilabel:`Přiřazeno k“: vyberte uživatele, ke kterému je aktivita automaticky přiřazena.
rozbalovací nabídka.

Značková část
~~~~~~~~~~~~

- :guilabel:Šablona k podpisu“: pokud je zaměstnanec povinen podepsat dokument při výběru této
Vyberte si v roletce šablonu dokumentu.

Například výhoda týkající se užívání firemního vozu může vyžadovat podpis zaměstnance.
dokument, který potvrzuje politiku společnosti vůči automobilům.

Popisová záložka
~~~~~~~~~~~~~~~

Přidat do této záložky jakékoliv další informace, které by mohly pomoci objasnit výhody.

Osobní údaje
-------------

Každý zaměstnanec v Odoo má svou kartu zaměstnance, která je vytvořena ve chvíli, kdy se uchazeč stává
zaměstnance. Tato karta obsahuje všechny její osobní údaje, životopis, informace o práci a
dokumenty.

Osobní údaje jsou shromažďovány z sekce konfigurátoru mzdy.
kandidát vyplní po nabídce pracovního místa. Tato osobní data jsou pak přenesena do
pracovní průkaz, když je zaměstnán.

Pro zobrazení karty zaměstnance přejděte na hlavní stránku aplikace Dashboard v sekci „Zaměstnanci“ a klikněte na
Zaměstnanecká karta.

.. poznámka::
Karta zaměstnance je možné chápat jako osobní spis zaměstnance.

Sekce „Osobní informace“ obsahuje všechny pole, která je možné vyplnit.
karta zaměstnance. Chcete-li se do této části dostat, přejděte na: menu: `Mzdy aplikace --> Konfigurace -->
Mzdový balíček: Osobní údaje.

.. obrázek: platove/osobni-udaje.png
:align:center
:alt: Seznam všech osobních údajů, které se objevují na zaměstnanecké kartě pro vstup.

Pro úpravu osobních informací vyberte záznam v seznamu na stránce :guilabel:`Osobní informace`.
a upravit osobní údaje na formuláři, který se objeví.

Pro vytvoření nové položky osobních údajů klikněte na tlačítko „Nový“.

Povinné pole kromě zadání názvu „Informace“ obsahují také pole „Související“.
Model`, „Související pole“ a „Kategorie“.

Vyberte položku „Související model“ z rozevírací nabídky. V poli se objeví hodnota
výchozím nastavení, ale možnost „Bankovní účet“ je také k dispozici v případě, že se jedná o související informace
na účet v bance.

Vyberte pole „Související pole“ z roletky, které nejlépe popisuje osobní údaje.
informace o tomto záznamu a kde je uložen v zadní části. Pak vyberte
Vyberte kategorii z rozevírací nabídky, kam patří osobní údaje, např.
:guilabel:Adresa nebo :guilabel:Osobní doklady.

Dva nejdůležitější políčka na osobních údajích jsou:
:guilabel:`Typ zobrazení“.

Zatrhnutím políčka „Je požadováno“ se pole na kartě zaměstnance stane povinným.
V rozevíracím seznamu „Zobrazovací typ“ je možné zadat různé informace.
možnosti, jako je textový box nebo přizpůsobitelná tlačítka rádia.
:guilabel:`Záložka“, „Dokument“ a další.

.. obrázek: platove-novinky.png
:align:center
:alt: Nová položka osobních údajů.

Shrnutí
------

V sekci „Životopis“ v části „Konfigurátor platů“, která je součástí nabídky nastavení,
jak jsou nastaveny pravidla pro sdělování informací o platu při nabízení pracovního místa potenciálním zaměstnancům.

Hodnoty nabídky se vypočítávají z těchto hodnot
nastavení a zobrazit se na stránce nabídky.

Pro konfiguraci této části přejděte na: `Payroll app --> Konfigurace --> Mzdy
Konfigurátor balíčků: Shrnutí.

Výchozí nastavení obsahuje tři typy struktury mezd:
:guilabel:'Dělník', :guilabel:'Zaměstnanec' a :guilabel:'Žádný'.

Každý typ struktury mzdy má několik nastavených pravidel, která ovlivňují způsob nabídky.
Výpočet byl proveden pomocí konkrétního typu struktury mzdy.

Pro vytvoření nového pravidla klikněte na tlačítko „Nový“ a poté vyplňte prázdnou kolonku „Mzda podle smlouvy“.
Formulář životopisu se načítá.

Do formuláře zadejte následující informace:

- :guilabel:`Informace“: zadejte název pro tento prvek.
- :guilabel:`Kategorie“: vyberte kategorii, ve které je hodnota uložena, pomocí rolovací nabídky.
Výchozí možnosti jsou: „Měsíční plat“, „Měsíční příspěvek“.
:guilabel:`Roky“ a „Celkem“.

Pokud je potřeba, můžeme vytvořit nové kategorie.

Klikněte na tlačítko „Nový“, pak zadejte název nové kategorie do pole „Název“.
pole. Následně vyberte z roletky „Periodicita“ a buď
:guilabel:`Měsíční“ nebo „Roční“. Nakonec zadejte číslo pro sekvenci. To odpovídá
do seznamu pravidel pro typ platové struktury, kde se tato pravidla nachází.

Konečně klikněte na tlačítko „Uložit a zavřít“.
- :guilabel:`Měsíční celkový dopad“: zaškrtněte políčko, pokud se tato hodnota přičítá k měsíčnímu celku
výpočet.
- :guilabel:`Jednotka měření“: vyberte typ hodnoty této pravidlo, buď :guilabel:`Měna`
:guilabel:`Dny“ nebo :guilabel:`Procenta“.

:guilabel:`Měna“ je pro pevný finanční obnos, :guilabel:`Dny“ je pro náhradu v podobě
Časovou dovolenou, a Percent je pro finanční odměnu založenou na jiném
jako například provize.
- :guilabel:Typ struktury mzdy: vyberte, jaký typ struktury mzdy je
podle seznamu nabídek.
- :guilabel:`Typ hodnoty“: vyberte způsob výpočtu hodnoty z roletky. Výchozí
Možnosti jsou: „Fixní hodnota“, „Smluvní hodnota“ a „Hodnota výplatního lístku“.
:guilabel:`Součet hodnot benefitů“, „Měsíční celkový“.
- :guilabel:`Kód“: vyberte kód, ke kterému tato pravidla platí, z roletky.

.. obrázek: platove-rozpocet-vzor-1.png
:align:center
:alt:Plně vyplněný tiskopis pro výpočet čisté mzdy s veškerými údaji k čistému platu.

Práce
====

Od té doby, co je aplikace Payroll zodpovědná za platbu zaměstnanců za konkrétní pracovní pozice,
kompletní seznam pracovních pozic je k dispozici v aplikacích *Mzdová evidence* a *Nábor zaměstnanců*.

.. _mzdy/pracovní pozice:

Pracovní pozice
-------------

Pozice uvedené v aplikaci *Mzdy* jsou shodné s pozicemi uvedenými v
aplikace Recruitment. Pokud se v aplikaci Recruitment přidá nová pracovní pozice,
Je viditelná také v aplikaci Mzdy a naopak.

Pro zobrazení pracovních pozic přejděte na: „Mzdy - > Konfigurace - > Práce: Pracovní místo
Pozice“.

Seznam všech pracovních pozic se zobrazí spolu s příslušným oddělením na
Stránka „Pracovní pozice“.

.. obrázek: platove_polozky.png
:align:center
:alt: Seznam všech pracovních pozic a odpovídajících oddělení.

Pro vytvoření nové pracovní pozice klikněte na tlačítko „Nový“ a objeví se Vám formulář pro vytváření pracovních míst.

Do formuláře pro novou pozici zadejte informace. Informace jsou stejné jako u
informace zadaná při vytváření nové pracovní pozice v aplikaci *Nabídka práce*.

Podrobnosti o tom, jak vyplnit tento formulář, najdete v dokumentaci „Nové pracovní místo“ (viz soubor :doc:`../hr/recruitment/new_job`)
forma.

.. viz též:
   - :doc:`mzdy/smlouvy“
   - :doc:`mzdy/pracovní vstupy“
   - :doc:`pracovní listy/přílohy k mzdě“
   - :doc:`mzdy/platové pásky“
   - :doc:`mzdy/reporting“
   - :doc:`mzdy/vstupní analýza práce“
   - :doc:`plat/priloha_k_platu`
   - :doc:`pracovní smlouva/lokalizace pracovních smluv“

..toctree::


mzdy/dohody
mzdy/pracovní vstupy
přílohy k mzdovým listům
mzdy/plat
mzdy/reporting
analýza mzdy/vstupní analýza práce
příloha mzdy
mzdy/mzdové lokalizace
