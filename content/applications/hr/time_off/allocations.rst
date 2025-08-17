===========
Alokace
===========

Jednou :ref:`druhy volna <time_off/time-off-types>` a :ref:`plány na získávání
Pokud jsou nastaveny plány na náhradní dovolenou, další krok je přidělení času dovolené.
Zaměstnanci.

Stránka „Přidělování“ aplikace „Čas dovolené“ je **pouze** viditelná uživatelům, kteří buď mají časově omezený přístup k aplikaci nebo jsou v ní zaregistrováni.
Odeberte oprávnění pro aplikaci „Čas volna“ u uživatelů s rolí *Off Officer* nebo *Administrator*.
na přístupová práva se odkazuje na dokumentaci „přístupová práva“
Dokumentace.

.. _volno/výdejní formulář:

Vyčleňte si volno
=================

Pro vytvoření nové alokace přejděte na: „Časový odpočinek - aplikace“ --> „Správa“
Alokace.

Tato stránka zobrazuje seznam všech aktuálních přidělení včetně jejich stavů.

Klikněte na „Nová“ pro přidělení dovolené a objeví se prázdný formulář „Přidělení“.

Po zadání názvu pro přidělení do prvního prázdného pole formuláře zadejte
informace:

- :guilabel:`Typ volna“: Vyberte typ dovolené z nabídky.
Vyčleněné zaměstnancům.
- Vyberte buď „Běžná alokace“ nebo „Nárůst“.
Alokace. Pokud alokace není založena na :ref:`plánu přírůstku
<čas volna/akumulace plánu>, vyberte: „Běžný plán“.
- „Plán připsání“: Pokud je vybrána možnost „Přidělování připsaných částek“,
:guilabel:`Druh přidělení“, objeví se pole „Plán účtování“. Pomocí výběrového pole lze
Vyberte plán účtování, ke kterému je přidělení spojeno. Plán účtování **musí být**
byli vybráni pro :guilabel:`Přidělování úroků“.
- „Platnost / datum zahájení“: Pokud je vybrána „Běžná alokace“,
:guilabel:`Druh přidělení“, pole s tímto názvem je označeno jako „Platnost“. Pokud
:guilabel:`Přidělení“ je vybráno pro pole „Typ přidělení“, v tomto případě
označené štítkem :guilabel:`Datum zahájení“.

Aktuální datum vyplní první pole s datem a výchozí hodnotou. Chcete-li zvolit jiné datum, klikněte na
předvyplněný datum, které odhalí okno kalendáře s připnutou lištou. Přejděte na požadovaný začátek
Vyberte si částku a klikněte na datum pro výběr.

Pokud vyprší alokace, zvolte datum v příštím poli pro datum. Pokud je čas dovolené
Nepřichází o platnost a druhé datumové pole je prázdné. V poli se zobrazí „No Limit“, pokud žádný
Datum se vybere.

Pokud je vybrána možnost „Akumulace“ v poli „Druh přidělování“, bude se používat druhá
Pole je označeno: guilabel:"Běžte až do".

.. důležité::
Pokud je datum zadané v poli „Datum spuštění“ uprostřed období času, například uprostřed měsíce,
v případě měsíčního rozúčtování se Odoo přiděluje k začátku nebo konci období podle toho, jaký
hodinách, které byly připsány na plán :ref:`<time_off/accrual-plans>`, ať už jako *At
začátkem období účtování (nebo na konci období účtování) namísto
konkrétní datum vloženo.

Příkladem je vytvoření alokace a odkaz na plán přiznávání času s hodnotou *V průběhu.
začátkem období účtování* je vždy první den v měsíci.

Na přidělovacím formuláři je nastaveno pole :guilabel:`Druh přidělení“ na hodnotu :guilabel:`Naplnění
Alokace, a datum v poli „Začátek“ je 06/16/24.

Aplikace **Odoo Time Off** aplikuje přidělení zpětně na začátek časového období.
období zadané v poli Start Date.

Proto se tento účet přičítá od 6. ledna 24, nikoliv od 6. června 24.

Dále je třeba poznamenat, že pokud v příloze k účtování odkazuje na plán účtování, který umožňuje
čas *„Konec období účtování“, přičemž v tomto okamžiku se načítá čas od „7/01/24“
než „6/18/24“.

- :guilabel:`Vyčleněné hodiny“: Zadejte počet hodin, které jsou zaměstnancům vyhrazené.
pole zobrazuje čas buď v hodinách nebo dnech, podle toho, jak je nastaveno.
Vybraný typ dovolené je nastaven podle volby:
- :guilabel:`Přidat důvod...“: Pokud je nutné nějaké vysvětlení, například proč se člověk nezúčastní
Vyplňte pole na dně formuláře s přidělením a zadejte do něj částku.

.. obrázek: přidělení/nové-přidělení.png
:alt: Nový tiskopis s vyplněnými všemi poli pro dvoutýdenní dovolenou
poskytované všem zaměstnancům.

Vícenásobné přidělení
--------------------

Při přidělování dovolené je běžné přidělit volno více zaměstnancům najednou.
pomocí funkce „Několik požadavků“.

Při přidělování času více zaměstnancům najednou přejděte na:
app --> Správa --> Předvolby. Pak klikněte na ikonu :icon:`fa-gear` :guilabel:`(Akce)`
v horním levém rohu, pak klikněte na ikonu „Uživatelé“ (Guilabel: „Více požadavků“). To odhalí
Pop-up okno „Několik požadavků“.

Tento formulář je identický s formulářem „Alokace“ a obsahuje navíc pole „Režim“.
pole. V poli :guilabel:`Modus` se určuje, jakým způsobem jsou vybíráni zaměstnanci.

Vyberte jednu z následujících možností v rozbalovacím seznamu:

- :guilabel:`Zaměstnanci“: Tato možnost umožňuje výběr více jednotlivých zaměstnanců.
které nejsou spojeny v rámci oddělení, společnosti nebo tagů. Vybráním této možnosti se zobrazí
:guilabel:`Zaměstnanci“ pole. Vyberte zaměstnance, kterým chcete přidělit alokaci v
:guilabel:`Zaměstnanci“ pole. Není omezen počet zaměstnanců, které lze vybrat.
- „Společnost“: Tato možnost umožňuje výběr všech zaměstnanců v rámci konkrétní
Společnost. Vyberte tuto možnost, abyste zobrazili pole „Společnost“. Vyberte „Společnost“,
je přidělena jedné společnosti, která je uvedena v poli „Společnost“.
je vybrána společnost, *všichni* zaměstnanci v této společnosti obdrží přidělení.
- „Podle oddělení“: Tato možnost umožňuje výběr všech zaměstnanců v rámci konkrétního
oddělení. Vybráním se zobrazí pole „Oddělení“.
:guilabel:"Oddělení" k přiřazení alokace. Pouze jedno oddělení může být přiřazeno v
:guilabel:`Oddělení` pole. Když je vybráno oddělení, všichni zaměstnanci v daném oddělení
obdržet přidělení.
- :guilabel:„Vybrat zaměstnance podle tagu“: Tato možnost umožňuje vybrat všechny zaměstnance s konkrétním
tag. Vyberte tento, což odhalí pole :guilabel:`Zaměstnanecký tag`. Vyberte požadovanou
:guilabel:`Štítek zaměstnance“ pro výběr všech zaměstnanců s tímto štítkem. Mohlo by být přiřazeno pouze jedno označení.
„Štítek zaměstnance“. Když je vybrán štítek, všichni zaměstnanci s tímto štítkem obdrží
rozdělení.

Dále vyberte typ dovolené z rozevírací nabídky. Potom vyberte jednu ze dvou možností, které jsou k dispozici v rozevírací nabídce „Typ dovolené“.
Je vybrán typ, název vloženého textu „Žádost o přidělení“ se změní na název vybrané položky.
„Čas dovolené“, včetně počtu dní. Změňte název přidělení, pokud
žádané.

Vyplňte zbytek formuláře „Přidělování času“ (viz stránka Časové dotace), pak klikněte
:guilabel:'Vytvořit rozdělení' a poté klikněte na tlačítko 'OK'.

.. obrázek: přidělování/více požadavků.png
:alt:Žádost o přidělení nemocenského volna pro všechny zaměstnance obchodního oddělení
odboru.

.. _volno/žádost o přidělení:

Přídělový požadavek
==================

Pokud zaměstnanec vyčerpal všechny své dovolené nebo se mu dovolená chýlí ke konci, může požádat o
na přidělení času navíc. Přidělování může probíhat dvěma způsoby, buď
:ref:`Přístupový panel <time_off/dashboard>“ nebo „Moje přidělení <time_off/my-allocations>“.

Pro vytvoření nové žádosti o přidělení klikněte buď na tlačítko „Nový požadavek na přidělení“ nebo
hlavní přehledový panel „Čas volna“ nebo tlačítko „Nový“ v části „Moje alokace“.
listovém zobrazení. Oba tlačítka otevřou nový formulář pro požadavek na přidělení.

.. poznámka::
Oba způsoby otevřou nové žádosti o přidělení, ale požadované z webu.
:guilabel:`Přístrojová deska“, formulář se objeví v okně přesunu, a pole „Platnost“ je
**neobjeví“. Pokud je z pohledu „Moje alokace“ vyžádán, obrazovka
přesměruje na novou stránku s žádostí o přidělení místo, namísto zobrazení okna.

Do nové žádosti o přidělení vložte následující informace:

- :guilabel:`Typ dovolené“: Vyberte typ dovolené, který je požadován pro tuto alokaci z
padajícím seznamem. Po výběru aktualizuje název s typem dovolené.
- :guilabel:`Platnost“: Výchozí hodnotou je aktuální datum a pole není
je možné upravit. Toto pole se objevuje pouze při žádosti o přidělení prostředků z
:guilabel:`Moje přidělení“ (výběr menu „Čas volna –> Můj čas –> Moje přidělení“).
- :guilabel:`Alokace“: Zadejte požadovanou dobu v tomto poli. Formát
Vyberte buď „Dny“ nebo „Hodiny“, podle toho, jaký je časový údaj.
V poli „Off Type“ je nastaveno. Jakmile se pole vyplní, název požadavku na přidělení
aktualizováno tak, aby zahrnovalo požadované množství času.
- :guilabel:`Přidat důvod ...“: Zadejte popis pro žádost o přidělení v tomto poli.
Měla by obsahovat všechny podrobnosti, které schvalovatelé potřebují k schválení požadavku.

Pokud požadavek vytvořila aplikace Dashboard, klikněte na tlačítko „Uložit a zavřít“.
na okno „Nová přidělení“ a uložit informace, aby bylo možné požadavek odeslat.

Pokud byl formulář vyplněn z pohledu „Moje přidělení“, informace je
Uloženo automaticky po zadání. Formulář lze uložit ručně kdykoliv pomocí
kliknutím na ikonu „Cloud Upload“ (nahrávání do cloudu).

.. obrázek: přidělování/žádost o přidělení.png
:alt:Žádost o přidělení požadované pracovní doby vyplněná pro zaměstnance, který žádá o další týden
nemocenské.
