=================
Dynamická volací identita
=================

Identifikace volajícího umožňuje příjemci hovoru zjistit, kdo mu volá.
ukázat číslo ze kterého volá. Caller ID zobrazuje uživatele a klienty, kdo je na druhé straně telefonu, takže
Mohou si vybrat, zda přijmou nebo odmítnou hovor.

Axivox nabízí možnost dynamického zobrazení čísla volajícího, kdy si můžete vybrat, které číslo se bude zobrazovat při odchozích hovorech.

Mezinárodní čísla lze zakoupit pro obchodování na mezinárodním telefonu.
volání z čísla s předčíslím nebo mezinárodním telefonním kódem země, kterou se volá.
Zobrazením místního čísla můžete zvýšit zapojení zákazníků.

Některé společnosti mají mnoho zaměstnanců, kteří hovory uskutečňují z call centra. Tito zaměstnanci nejsou vždy
k dispozici pro příjem telefonního hovoru od potenciálního zákazníka. V tomto případě:abbr: VoIP
(hlasová komunikace přes internet) lze nastavit tak, aby se při volání zobrazovalo
hlavní telefonní číslo společnosti, takže na něj může odpovídat kdokoliv ze zaměstnanců skupiny.
volání nikdy nepropásne.

..._voip/axivox/dynamic-caller-id-default:

Nastavená výchozí čísla
=======================

Ve službě Axivox lze nastavit výchozí číslo. To je hlavní telefonní číslo firmy. To znamená, že když
při volání z firmy (uživatel/zaměstnanec) na číslo mimo firmu je výchozí směrovací číslo
je automaticky zobrazen na displeji telefonu.

Pokud se někdo zvenčí pokusí volat zpět uživatele/zaměstnance, je pak přesměrován
přes hlavní linku (výchozí číslo). Pokud je nastavená telefonní předvolba, jsou vyzváni k zadání
selekcí. Je zvláště užitečné v případech, kdy zaměstnanci často mění své pracovní pozice nebo
Odcházejí z firmy.

.. viz též:
   - :doc:`dial_plan_basics“
   - :doc:`dial_plan_advanced“

Pro přístup k výchozímu číslu se přihlaste do „Axivox Management Console <https://manage.axivox.com>“
a přihlásit se. Pak klikněte na „Nastavení“ v levém menu a přejděte do
:guilabel:`Výchozí číslo pro odesílání zpráv“.

Zde změňte pole „Výchozí číslo“ kliknutím na vykřičník a zadejte
výběr příchozích telefonních čísel dostupných na Axivoxu.

Ujistěte se, že změny uložíte a poté klikněte na „Použít změny“ v pravém horním rohu.
kontrolní roh stránky „Obecné nastavení“ a zavedením změny.

Výchozí číslo pro odchozí hovory je to, které se zobrazuje v portálu správy Axivoxu výchozím způsobem.
Výchozí číslo však lze na úrovni uživatele nastavit jinak.

Uživatelé
-----

Pro konfiguraci odchozího čísla na úrovni uživatele se přihlaste do portálu pro správu Axivo.
<https://manage.axivox.com>`. Dále klikněte na položku „Uživatelé“ v levém menu a poté
Klikněte na tlačítko „Upravit“ vpravo od uživatele, který má být nakonfigurován.

V poli „Číslo odchozího hovoru“ klikněte na rozbalovací nabídku a vyberte buď „Výchozí číslo“.
výchozí číslo (jak je uvedeno zde: :ref:`voip/axivox/dynamic-caller-id-default`), nebo jakékoliv
příchozí hovory na účtu Axivox.

Vybráním položky „Výchozí“ v rozevíracím seznamu „Číslo odesílatele“ je zajištěno
Tento uživatel má ve svém identifikátoru volajícího zobrazeno číslo pro odchozí hovory.

Pokud je zvoleno konkrétní číslo, pak se tento uživatel přiřadí podle :guilabel:`Incoming
čísla“ (v levém menu konzole Axivox) znamená, že tento uživatel má přímou linku pro
dostat se k nim.

Jakmile jsou požadované změny dokončeny, ujistěte se, že kliknutím na tlačítko „Uložit“ potvrdíte provedené změny.
V horním pravém rohu klepněte na tlačítko „Použít změny“.

..tip:
Výchozí nastavení při vytváření nového uživatele v Axivoxu je automatické přiřazení čísla pro odchozí hovory.
nastaveno na :guilabel:`Výchozí hodnota`.

Pokročilé možnosti
----------------

Přejděte na volbu „Nastavení“ v nabídce.
v levém sloupci „Správa AxiVoxu <https://manage.axivox.com>“. Pak klikněte
„Další možnosti“ vpravo od „Výchozí číslo“.

Výchozí nastavení neobsahuje žádné pokročilé pravidlo. Chcete-li vytvořit jedno, klikněte na zelenou ikonu „+
(plus) ikona. Po kliknutí se zobrazí řádek s dvěma prázdnými poli. Zde lze nastavit různé hovorové ID
podle místa, odkud volá uživatel/zaměstnanec.

Nejprve nastavte pole Destination prefix v prvním prázdném poli.
kód země, včetně nul před ním. Poté vyberte
telefonní číslo, které se má používat pro volání z daného kódu země.

.. důležité:
Zatrhněte políčko u možnosti „Použít pokročilé pravidlo i pro uživatele s výchozím číslem
konfigurováno tak, aby tyto pravidla měly přednost před všemi ostatními nastaveními pro odchozí provoz.

..tip:
Pořadí pravidel lze změnit tahem a pložením na jiný pořadí.
První shodná pravidla se aplikují.

Příklad:
Příkladem je například společnost, která chce, aby všichni uživatelé/zaměstnanci využívali určený počet pro Velkou Británii.
Británie, když voláte ze zeměpisné šířky 0044 (Velká Británie).

K tomu stačí zadat do pole „Země“ číslo 0044.
vyberte číslo začínající mezinárodním kódem země „+44“. Seřaďte pravidla podle potřeby a vyberte
pokud je potřeba, zaškrtávací políčko k tomu, aby všechny ostatní pravidla převezmulo.

.... obrázek:: dynamická_identifikace_volajícího/pokročilá_identifikace_volajícího.png
:synchronizace: střed
:alt:Pokročilé možnosti pro výchozí telefonní číslo.

Jakmile jsou požadované konfigurace dokončeny, ujistěte se, že kliknutím na tlačítko :guilabel:`Uložit` a poté na
V horním pravém rohu klepněte na tlačítko „Použít změny“.
