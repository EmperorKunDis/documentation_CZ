===============
Šablony událostí
===============

Aplikace Odoo Events poskytuje možnost upravit a nakonfigurovat šablony událostí, které
lze použít k urychlení procesu vytváření události.

Tyto šablony lze vytvořit a upravit v aplikaci a pak vybrat z události.
forma, aby bylo možné rychle aplikovat sérii nastavení a prvků na nový případ.
pokud je třeba, dále upravit.

Stránka šablon událostí
====================

V aplikaci Odoo Events lze rychle vytvářet a upravovat šablony událostí.

Nejprve přejděte na: „Aplikace událostí -> Konfigurace - > Šablony událostí“.
zobrazí stránku „Šablony událostí“. Zde najdete všechny existující šablony událostí v
databáze.

.. obrázek: event_templates/event-templates-page.png
:align:center
:alt:Stránka šablon událostí v aplikaci Odoo Events.

Výchozí nastavení poskytuje tři přednastavené šablony události: :guilabel:`Výstava`.
„Trénink“ a „Sport“, které mají své vlastní unikátní nastavení.
jim.

Chcete-li změnit způsob zobrazení šablon těchto událostí na poli rozbalovací nabídky „Šablona“ v formuláři pro události
Přetáhněte je do požadovaného pořadí pomocí ikony „OI-Draggable“ (přetažitelné).
ikonu umístěnou vlevo od každé řádky šablony události na stránce „Šablony událostí“.

.. viz též:
Chcete-li se dozvědět více o formách událostí, podívejte se na dokumentaci :doc:`create_events`.

Vytvořit šablonu události
=====================

Existují dvě možnosti, jak vytvořit a nakonfigurovat šablonu události v Odoo Events.

#**Na přístrojové desce**, po zvolení položky „Aplikace událostí“ – „Konfigurace“ – „Událost“.
Vyberte šablonu a klikněte na tlačítko „Nový“ v horním levém rohu. To zobrazí
prázdný vzor pro událost, který lze upravit různými způsoby.
#**Na samotném formuláři události**. Začněte psát název nového šablonového formuláře v poli *Šablona*.
pole a klikněte na položku „Vytvořit a upravit…“ z rozbalovací nabídky.
zobrazí okno s názvem „Vytvořit šablonu“, které obsahuje všechny stejné konfigurovatelné pole.
položky, které se nacházejí na standardním šabloně události.

.. poznámka::
Kliknutím na položku „Vytvořit [název šablony]“ v rozevírací nabídce, která se zobrazí po
pole „Šablona“ na formuláři události vytvoří šablonu události v databázi, ale ne
zobrazit uživateli okno s názvem „Vytvoření šablony“.

Šablonu události by bylo nutné upravit, a to výběrem na stránce *Šablony událostí*.


Šablona pro formulář události
-------------------

Všechny pole na standardním formuláři šablony události jsou také na formuláři vytváření šablony.
okno s náhledem, které je přístupné pomocí pole *Šablona* na formuláři události.

.. obrázek: event_templates/event-template-form.png
:align:center
:alt: Standardní šablona události v aplikaci Odoo Events.

Začněte tím, že do pole „Šablona události“ vložíte název šablony události.
v horní části formuláře.

Pod tímto polem je řada zaškrtávacích políček, která jsou všechna spojena s tím, jak
Výběr jídel bude k dispozici na stránce s událostí.

- :guilabel:„Webová podnadpis“: umožňuje vložit podnadpis na webové stránky akce. Pokud je zaškrtnuté
Zaškrtněte každé další políčko v této sérii a potom vyberte možnost
Vyberte si libovolný z možností zaškrtávacího políčka, jak chcete.
- :guilabel:`Navigační položka menu“: přidá podmenu, který umožní přejít na stránku s plánovanými
pro tuto událost.
- :guilabel:'Návrh trasy': přidá podmenu, který umožní přejít na stránku s návrhem trasy.
Návštěvníci mohou vyplnit formulář s návrhem přednášky (přednáška, přednáška, prezentace atd.).
během akce.
- :guilabel:„Položka nabídky v přepínači“: přidá podnabídkovou položku, která navštívené stránce umožní přejít na samostatnou stránku.
Vstupenky na akci lze zakoupit. Akční stánky mohou být upraveny a konfigurovány tak, aby vyhovovaly potřebám
:guilabel:`Výstavní stánky“ v dialogovém okně šablony události, z stránky „Kategorie výstavních stánků“.
[:menu_selection:'Akce aplikace - Konfigurace - Kategorie stánku'].

... důležité::
Každý uživatel **musí** vytvořit produkt stánku s požadovanou možností *Event Booth*.
:guilabel:`Druh produktu“ na formuláři produktu.

- :guilabel:„Název položky v menu výstavce“: přidá podmenu s odkazem na samostatnou stránku.
zobrazuje všechny vystavovatele spojené s daným konkrétním akcí. Ikony těchto vystavovatelů
Jsou také na každé stránce s konkrétním akcí.
- :guilabel:'Společnost': přidává položku podmenu, která umožňuje účastníkům přístup k přednastaveným virtuálním
komunitní místnosti pro setkávání s ostatními účastníky a diskutovat různá témata související s událostí.
Pokud tuto políčko zaškrtnete, funkce „Povolit vytváření místností“ se stane dostupnou.
- :guilabel:`Umožnit vytváření místností“: umožněte návštěvníkům vytvářet vlastní místnosti pro komunitu.
- :guilabel:'Tlačítko registrace': přidá tlačítko na konec podmenu události, které návštěvníky přesměruje
stránku registrace na dané akci, když ji kliknete.

Jakmile jsou zaškrtnuty požadované políčka, vyberte vhodný časový pásmo pro
akci z nabídky dostupných možností.

Pak je možné přidat k události tagy pro organizační účely.
šablona.

Můžete také omezit registrace na tento konkrétní šablonu události pomocí možnosti
zaškrtnutím políčka. Pokud je zaškrtnuto, pokračujte v zadávání počtu účastníků podle štítku „Účastníci“
jejichž se má omezit.

Pod obecnými informacemi na začátku šablony události jsou pět záložek:

- :ref:`Vstupenky <events/event-tickets>`
- :ref:`Komunikace <events/event-communication>`
- :ref:`Stánky <event_templates/event_template/booths>`
- :ref:`Dotazy <events/event-questions>`
- :ref:`Poznámky <events/event-notes>`

.. _event_templates/event_template/stánky:

Booths tab
~~~~~~~~~~

Jediný rozdíl mezi formulářem šablony události a formulářem s názvem „Booths“ je v tom, že
standardní událostní formulář, kde jsou další záložky (Guilabel: Tickets, Guilabel: Communication)
„Otázky“ a „Poznámky“) jsou přítomné a konfigurovány stejným způsobem.
více informací o těchto záložkách najdete v dokumentaci k :doc:`create_events`.

.. důležité:
Pro vytvoření stánku nebo kategorie stánků musí být ve skladbě produktu prodejního místa uveden produkt „stánek“
Nejprve nastavte produkt na typ *Stánek*. **Pouze** produkty s tímto konkrétním
Konfigurace lze vybrat v požadovaném poli „Produkt“ formuláře pro stánek nebo kategorii stánku.

.. poznámka::
V aplikaci Odoo Events lze vytvářet a upravovat stánky na akcích dvěma způsoby. Buď
v záložce Booths v šabloně pro událost nebo přes navigaci na
:menuselection:`Aplikace události --> Konfigurace --> Kategorie stánků“, a klikněte na „Nový“.

Chcete-li přidat stánek z karty „Stánky“ v šabloně formuláře události, klikněte na „Přidat stánek“.
line`. To odhalí prázdné okno „Vytvořit stánky“.

.. obrázek: event_templates/create-booths-popup.png
:align:center
:alt: Vytvořte stánek v aplikaci Odoo Events.

Začněte tím, že do příslušného pole v horní části stránky zadáte
Pop-up okno.

Vyberte vhodný typ stánku z rozevíracího pole pod ním.
kategorie lze vytvářet a upravovat na stránce Booth Categories v aplikaci Events.
která je dostupná po kliknutí na „Aplikace události“ -> „Nastavení“ -> „Stánek“.
Kategorie.

..tip:
Vytvořit pole „Kategorie kabinky“ lze přímo z tohoto pole na záložce „Vytvořit“.
Okno Booths s okamžitou odezvou. K tomu stačí zadat název nové kategorie stánku.
pole „Kategorie“ a vyberte buď možnost „Vytvořit“ nebo „Vytvořit a
Editovat... ze seznamu, který vám zobrazí.

Kliknutím na tlačítko „Vytvořit“ pouze vytvoříte kategorii, kterou je možné (a mělo by se) upravit.
a později. Kliknutím na „Vytvořit a upravit ...“ se zobrazí nové „Vytvořit místnost
Pop-up okno kategorie, ve kterém lze kategorii konfigurovat různými způsoby.

...... obrázek: event_templates/create-booth-category-popup.png
:synchronizace: střed
:alt:Okno pro vytvoření kategorie stánku ve vývojářské aplikaci Odoo Events.

z této okno prohlížeče pokračujte v názvu kategorie stánku. Upravte jej a
:guilabel:`Podrobnosti o stánku“ nastavení, konfigurujte možnosti :guilabel:`Sponzorství“ (pokud
aplikovatelné) a zanechat volitelný :guilabel:`Popis`, který vysvětlí příslušné podrobnosti.
týkající se této konkrétní kategorie stánků.

Můžete také přidat fotografii nebo vizuální reprezentaci kategorie stánku.
ikona v pravém horním rohu s nápisem „(kamera)“.

Po dokončení všech požadovaných konfigurací klikněte na tlačítko „Uložit a zavřít“.

Stejné konfigurace a možnosti jsou k dispozici po přechodu na :menuselection:`Aplikace události -->
Konfigurace --> Kategorie stánků“ a kliknutím na „Nový“.

Jakmile je vybrána požadovaná kategorie „Booth“, zůstávají ostatní pole na
Okno „Vytvořit stánek“ (:guilabel:„Měna“, „Produkt“ a
„Cena“) automaticky vyplní podle informací nakonfigurovaných pro daný „Stánek
Kategorie.

.. poznámka::
Tyto pole nelze upravit v okně „Vytvoření stánku“.
jen z konkrétní stránky kategorie stánku.

Po dokončení všech požadovaných konfigurací klikněte na tlačítko „Uložit a zavřít“ pro uložení stánku.
Vraťte se na šablonu události nebo klikněte na tlačítko „Uložit a nový“. Uložení stánku a zahájení
vytvoření dalšího stánku na nové okno „Vytvořit stánky“. Klikněte na „Smazat“
odstranit všechny změny a vrátit se zpět do původního tvaru události.

Jakmile je stánek zachráněn, zobrazí se v záložce „Stánky“ na formuláři šablony akce.

Použijte šablony událostí
===================

Jakmile je šablona události dokončena, je přístupná na všech formulářích pro události v Odoo Events.
aplikace.

Pro použití šablony události přejděte do aplikace „Události“ a klikněte na tlačítko „Nový“.
otevřít nový formulář události.

Klikněte na pole „Šablona“ v události a zobrazí se všechny existující šablony.
v databázi. Zobrazují se v pořadí, v jakém jsou uvedeny na stránce s předdefinovanými událostmi
(:menu_selection:"Akce aplikace-->Nastavení-->Šablony akcí").

Vyberte požadovaný šablonový soubor z pole „Šablona“ na formuláři události.
Přednastavené parametry automaticky vyplní formulář události a ušetří tak čas při vytváření události.
proces.

Jedno z těchto přednastavených nastavení, které se vztahuje k vybranému šabloně události.
Název šablony na formuláři události lze upravit podle potřeby.

.. viz též:
:doc:`vytvářet události“
