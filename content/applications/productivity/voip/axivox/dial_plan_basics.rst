================
Základy telefonního plánu
================

Když někdo volá do firmy, může potřebovat kontaktovat podporu pro zákazníky nebo obchodní oddělení.
týmu nebo dokonce osoby přímo v jeho linii. Volající mohl být také na stopě nějaké informace o
podniku, jako jsou například otevírací doba obchodů. Nebo možná chtějí zanechat vzkaz na hlasovém automatu, aby jim někdo ze zaměstnanců
Společnost může volat zpět. S plány volání v Axivoxu společnost může řídit, jak se s příchozími hovory zachází
To se řeší.

Použitím správné architektury hovoru prostřednictvím plánu volání se volající dostane ke správným lidem nebo k
správné informace včas a efektivně.

Tento dokument popisuje základní konfiguraci telefonních plánů v Axivoxu.

.. viz též:
Pro více informací o pokročilých plánech volání navštivte :doc:`dial_plan_advanced`.

.. důležité:
Používání doplňku pro kontrolu pravopisu v prohlížeči může bránit použití vizuálního editoru při plánování telefonních čísel.
použít překladač s konzolou pro správu Axivox.

... _voip/axivox/dial_plans:

Telefonní plány
==========

Přihlaste se do „Axivox Management Console <https://manage.axivox.com>“ a
Kliknutím na položku „Telefonní plány“ v levém menu.

Chcete-li přidat nový plán volání z stránky „Dial plan“, klikněte na tlačítko s nápisem
:guilabel:`Přidat nový plán hovorů“.

.. poznámka::
AxiVoX nemá žádný limit pro počet vytvořených telefonních plánů. Tyto mohou být přidány a
je možné vylepšit kdykoliv. To umožňuje vytvářet pískoviště s mnoha různými
konfigurace.

.. obrázek: dial_plan_basics/dial-plan-edits.png
:align:center
:alt:Přístupová lišta s editačními funkcemi a tlačítkem Přidat dial plán zvýrazněným.

Chcete-li upravit stávající telefonní plán, vyberte jednu z následujících možností vedle uloženého telefonního plánu.
plán:

#:guilabel:`Smazat“: tato akce smaže připojený plán hovoru.
#:edit: tato akce umožňuje uživateli upravit telefonní plán.
#:guilabel:`Vizuální editor“: Tato akce otevře okno vizuálního editoru, kde můžete upravit telefonní plán.
Architektura je viditelná a editovatelná.
#:duplikovat: tato akce duplikuje plánování hovorů a umisťuje jej na konec.
list s jedním číslem navíc (přípona +1), než je původní přípona.

Editor dialplánu (vizuální editor)
-------------------------------

Když je kliknut na tlačítko „Vizuální editor“ pro dial plán v části „Dial plán“.
stránka, okno: „Editor dialplánu“ se objeví.

Toto okno je primárním místem, kde se zobrazuje architektura nebo struktura telefonního plánu.
konfigurovat. V tomto okně se objeví :abbr:`GUI (grafické uživatelské rozhraní)“, kde jsou různé
je možné je konfigurovat a propojit.

.. obrázek: dial_plan_basics/dial-plan-visual.png
:align:center
:alt:Vizuální editor příkladového plánu s novým prvkem Přidat a tlačítky Uložit
zvýrazněny.

.. důležité:
Nové plány se zobrazují prázdné s možnostmi „Nové prvky“ pro uživatele, aby mohl „Přidat“.
a stiskněte tlačítko „Uložit“.

Metoda ukládání v editoru dialplánu je odlišná od ukládání jiných úprav
v konzole pro správu Axivoxu, protože tlačítko „Uložit“ **musí** být stisknuto před
zavřít:menuselection:`Vizuální editor`.

Pak musí uživatel kliknout na tlačítko „AxiVoice“ předtím, než se změny projeví na platformě.
v pravém horním rohu stránky s dial plánem.

Z okna „Editor dialplanu“ lze přidat nový prvek do dialplanu.
k tomu otevřete nabídku „Nový prvek“ a vyberte požadovaný prvek. Poté
Klikněte na „Přidat“.

Takto se do grafického editoru přidává prvek, který ukazuje změnu telefonního plánu.
Tento prvek může být umístěn, kam je potřeba, mezi ostatními prvky v telefonním plánu.

Připojte prvky v telefonní předvolbě kliknutím a táhnutím od znaku :guilabel: (otevřený
kruh) na pravé straně prvku. To odhalí ikonu ve tvaru šipky ().
Pokračujte v táhnutí ikony „(šipka)“ na požadovaný prvek v telefonním plánu.
s nimiž se má spojit.

Připojte ikonu „(šipka)“ k obdélníku na levé straně požadovaného prvku.

V zobrazení telefonního plánu jsou volání seřazena od leva doprava v prvku.

Chcete-li upravit nový prvek, klikněte na něj uvnitř kolečka
plán, který zobrazí další okno s možnostmi nastavení.

Každý prvek má jinou konfigurační lištu, která se objeví po dvojitém kliknutí.

.. důležité:
Všechny prvky **musí** mít konečné místo v telefonní síti, aby se uzavřel smyčka.
To lze provést implementací prvku :guilabel:`Hang up`, nebo smyčkou prvku zpět.
do prvku Menu nebo Digital Receptionist jinde v telefonní knize.
plán.

.... obrázek: dial_plan_basics/loop-back.png
:synchronizace: střed
:alt:Dialing plan, shown with highlight looping open end back to the beginning of the menu
prvek.

Jakmile jsou všechny požadované prvky a konfigurace telefonní ústředny dokončeny, nezapomeňte kliknout
Před ukončením okna „Editor dialplánu“ stiskněte tlačítko „Uložit“. Pak klikněte
Vyberte možnost „Použít změny“ na stránce „Telefonní plány“ a zkontrolujte, že jsou implementovány.
Produkce Axivox.

Části telefonního plánu
------------------

Následující prvky jsou k dispozici v rozevíracím seznamu „Nový prvek“ při navrhování
dílčí plán v okně „Editor dialplánu“.

Základní prvky
~~~~~~~~~~~~~~

Tyto jsou základní prvky, které se používají v jednoduchých telefonních plánech v Axivoxu:

- :guilabel:`Call“: vyvolání rozšíření nebo fronty.
- :guilabel:`Spustit soubor“: přehrát zvukový soubor nebo hlasovou pozdravovací zprávu.
- :guilabel:`Hlasová schránka“: přeposlat na hlasovou schránku.
- :guilabel:`Zavěsit telefon“: zavěšení hovoru (terminalu).
- :guilabel:`Fronta“: připojit frontu s uživateli, kteří budou odpovídat na hovor.
- :guilabel:`Konference“: přidat konferenční místnost, do které se může volající spojit.

Základní prvky routování
~~~~~~~~~~~~~~~~~~~~~~

Základními prvky routování jsou změna trasy volajícího nebo přesměrování hovoru.
Axivox:

- :guilabel:`Menu“: přidejte telefonní seznam a nakonfigurujte další akce (ne koncový bod).
- :guilabel:`Přepínač“: připojte manuální ovládání zapnutí/vypnutí, které může směrovat provoz podle toho, zda je
je otevřený (On) nebo zavřený (Off).
- :guilabel:`Digitální recepční“: připojte virtuálního operátora, který bude poslouchat propojení na rozšíření
to.

Pokročilé prvky směrování
~~~~~~~~~~~~~~~~~~~~~~~~~

Tyto pokročilejší prvky umožňují směrování hovorů v Axivoxu:

- :guilabel:`Dispečer“: vytvořte filtr hovorů, který směruje provoz podle geografické polohy
identifikace volajícího.
- :guilabel:`Seznam přístupů“: vytvořte seznam přístupu s přednostním oprávněním pro VIP zákazníky.
- :guilabel:`Časová podmínka“: vytvořte časové podmínky pro směrování příchozího provozu kolem svátků.
jiné citlivé časové úseky.
- :guilabel:„Multiswitch“: mechanismus pro vytváření cest a jejich zapínání a vypínání, který umožňuje odvádět
přijaté hovory.

Pokročilé prvky
~~~~~~~~~~~~~~~~~

Následující jsou pokročilejší prvky (než je routování):

- :guilabel:`Záznam‘: funkce záznamu je zapnutá (vyžaduje změnu plánu, zapnuto v Axivox
(Nastavení).
- :guilabel:`Označení volajícího“: nahraďte označení volajícího číslem nebo libovolným textem.

.. důležité:
Elementy telefonní předvolby lze nakonfigurovat kliknutím na ně a propojením různých aspektů.
AxiVox do nich.

Připojit k příchozímu číslu
=========================

Připojit existující plán číslování k příchozímu číslu, přejděte na Axivox Management Console
<https://manage.axivox.com> a klikněte na položku „Příchozí čísla“.

Dále klikněte na tlačítko „Upravit“ vedle čísla, ke kterému se má plán připojit.

Provedením takového kroku se zobrazí samostatná stránka pro úpravu telefonního plánu dané číslo. Pro provedení tohoto kroku vyberte
Vyberte položku „Plánování hovorů“ z rozevírací nabídky „Typ cílového zařízení pro hlasové volání“.
Poté vyberte požadovaný dialing plán z pole „Dialing plan“, které se objeví.

S tímto nastaveným plánem se při volání z určitého čísla spustí konfigurovaný plán.
aktivován a provede vás přes všechny příkazy, které zajistí správné nasměrování hovoru.

Nakonec klikněte na tlačítko „Uložit“ a poté v pravém horním rohu na „Použít změny“.
roh.

Základní scénář telefonního plánu
------------------------

Následující popisuje základní scénář plánu pro směrování hovorů, kde jsou další prvky
Přidat do rozšíření sestavy. Tento základní scénář plánu telefonních čísel zahrnuje následující propojené prvky
:menu:Start --> Spustit soubor --> Menu --> (Zavěsit hovor, Hovory, Fronty, Konference) -->
Hlasová pošta, ukončení hovoru.

.. obrázek: dial_plan_basics/basic-scenario.png
:align:center
:alt: Konfigurace základního telefonního plánu.

.. viz též:
Toto nastavení neobsahuje žádné základní ani pokročilé směrování hovorů. Další informace o směrování
routování, odkazujte na tuto dokumentaci: :doc:`dial_plan_advanced`.
