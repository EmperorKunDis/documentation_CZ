==========
Aktivita
==========

.. |hodiny| nahradit za: :icon:`fa-clock-o` :guilabel:`(hodiny)`

Aktivita je následná činnost spojená s záznamem v databázi Odoo.

..._aktivity/důležité:

Ikona používaná k zobrazení aktivit se liší podle typu aktivity.
<aktivity/druhy>:

- :icon:`fa-clock-o` :guilabel:`(hodiny)` ikona výchozí pro aktivity.
- :icon:`fa-phone` :guilabel:`(telefon)` - je naplánována telefonická konzultace.
- :icon:`fa-envelope` :guilabel:`(email)` - e-mailová zpráva je naplánovaná.
- :icon:`fa-check` :guilabel:`(check)` icon: úkol byl naplánován.
- :icon:`fa-users` :guilabel:`(lidé)` ikonka: schůzka je naplánovaná.
- :icon:`fa-upload` :guilabel:`(upload)` icon: Dokument je naplánován na nahrání.
- :icon:`fa-pencil-square-o` :guilabel:`(žádost o podpis)` - žádost o podpis je naplánována.

Plánujte aktivity
===================

Aktivita může být naplánována na jakékoliv stránce databáze, která obsahuje chytrý odkaz.
„Aktivita/hovoření“ vlákno, „Kanban pohled“ (viz aktivita/kanban), „Seznam pohled“
<aktivity/seznam>“, nebo „výhled aktivit <aktivita/aktivita>“ aplikace.

..._činnosti/hovoření:

Chatování
-------

Aktivita může být vytvořena z jakéhokoliv rozhovoru.

Pro naplánování nové aktivity klikněte na tlačítko „Aktivita“, které se nachází v horní části
šeptání. V okně „Aktivita v rozvrhu“, které se objeví, vyplňte
Formulář „Aktivita“ (<activities/form>).

.. obrázek: aktivity/šeptání.png
:align:center
:alt: Nový typ aktivity.

..._aktivity/kanban:

Kanbanový pohled
-----------

Aktivita může být vytvořena také z pohledu „Kanban“ (ikona :icon:`oi-view-kanban` ).

K tomu stačí kliknout na hodiny umístěné v záhlaví jednotlivých záznamů.

Klikněte na „Zařadit aktivitu“ a poté pokračujte v vyplnění formuláře „Schedule Activity“.
<činnosti/forma>.

.. obrázek: aktivity/plán-kanban-aktivita.png
:align:center
:alt:Kanbanový pohled na obchodní proces a možnost naplánovat aktivitu.

.. poznámka::
Pokud uživatelský záznam obsahuje plánovanou aktivitu, je nahrazeno zobrazení času ikonou, která reprezentuje
aktivitu, která již existuje. Klikněte na ikonu typu aktivity a zvolte jinou aktivitu.

..._aktivity/seznam:

Zobrazení seznamu
---------

Aktivitu lze také vytvořit z pohledu „seznam“ :guilabel: (list).

Pokud je sloupec „Aktivita“ skrytý, zobrazte jej pomocí ikony „Nastavení“.
:guilabel:`(nastavení změnit)` ikona v pravém horním rohu.

Poté klikněte na časovač pro záznam, ke kterému chcete aktivitu přidat, a poté klikněte na „+“.
Vytvořte aktivitu. Přejděte na:ref:`vyplnění formuláře pro aktivity <aktivita/formulář>
se objevuje.

.. poznámka::
Pokud uživatelský záznam obsahuje plánovanou aktivitu, je nahrazeno zobrazení času ikonou, která reprezentuje
aktivitu, která již existuje. Klikněte na ikonu typu aktivity a zvolte jinou aktivitu.

.. obrázek: aktivity/rozpis-aktivit.png
:align:center
:alt: Zobrazení karty pro správu vztahů se zákazníky a možnost naplánovat aktivitu.

..._činnosti/činnost:

Zobrazení aktivity
-------------

Většina aplikací v Odoo má k dispozici pohled na činnost. Pokud je k dispozici, zobrazí se
v pravém horním rohu hlavního menu, vedle ikon pro ostatní zobrazení.

Pro zobrazení aktivity klikněte na |hodiny|.

.. obrázek: aktivity/aktivita.png
:align:center
:alt:V horním pravém rohu je ikonka aktivit, která se jmenuje Outlook.

V tomto pohledu jsou v sloupcích uvedeny všechny dostupné aktivity, zatímco horizontální položky
zobrazuje všechny jednotlivé záznamy.

Aktivita, která je zobrazena v zelené barvě, má termín splatnosti v budoucnu. Aktivita, která je zobrazena oranžově, je již splatná.
Dnes jsou červeně označené aktivity již pozdní.

Barvy v každé sloupci představují rekordy pro konkrétní typ aktivity a zobrazují počet
Ukazuje, kolik aktivit je naplánováno pro daný typ.

Pokud je pro záznam naplánováno více typů aktivit, v poli se objeví číslo, které ukazuje
celkový počet plánovaných aktivit.

.. poznámka::
Barvy aktivit a jejich vztah k termínu splatnosti jsou konzistentní po celém Odoo.
bez ohledu na typ aktivity nebo pohled.

Pro plánování aktivity pro rekord klikněte na příslušné pole.
ikona „(plus)“ se objeví a poté vyplňte formulář Schedule Activity.
<činnosti/forma>.

.. obrázek:: aktivity/aktivita-prihlaseni.png
:align:center
:alt: Zobrazení aktivity v CRM a možnost naplánovat aktivitu.

..._činnosti/forma:

Formulář pro plánování aktivit
----------------------

Aktivita může být naplánována z mnoha různých míst, jako je chatter.
z aktivit nebo chatu záznamu, případně z některé ze více možností v aplikaci, pokud je k dispozici:
„Výhled Kanban“ (viz „Aktivita - Výhled Kanban“), „Seznam“ (viz „Aktivita - Seznam“) nebo „Aktivitu“.
zobrazení aktivit/aktivity.

Do formuláře zadejte následující informace:

- :guilabel:`Typ aktivity“: vyberte typ aktivity z nabídky. Výchozí
Možnosti jsou: „E-mail“, „Hovor“, „Schůzka“ nebo „Úkol“.
V závislosti na tom, jaké další aplikace jsou nainstalovány, mohou být k dispozici další možnosti.
- :guilabel:`Shrnutí“: zadejte krátký název aktivity, například „Diskuse o návrhu“.
- :guilabel:`Datum splatnosti“: vyberte datum splatnosti aktivit pomocí kalendáře.
- Výchozí hodnota pole „Přiřazeno“ je uživatel aktuálně přihlášený.
uživatele k aktivitě, vyberte je z roletky.
- :guilabel:`Poznámky“: do pole zadejte další informace o aktivitě.

Po dokončení okna „Aktivita v rozvrhu“ klikněte na jednu z následujících možností
tlačítka:

- :guilabel:`Otevřít kalendář“: otevře kalendář uživatele pro přidání a plánování aktivity.

Vyberte požadovaný den a čas pro aktivity a otevře se okno s názvem „Nový události“.
objeví se. Popis z okna „Popis činnosti“ vyplní pole :guilabel:`Název`.
pole.

Zadejte informace do okna „Nový záznam“ a poté klikněte na „Uložit a zavřít“.
Zařadit ji do rozpisu a pak je přidána do šeptání pod číslem
:guilabel:`Plánované aktivity“ části.

.. důležité::
Tlačítko „Otevřený kalendář“ se zobrazí pouze tehdy, pokud je nastavená volba „Aktivní typ“.
buď do :guilabel:`Hovor“ nebo :guilabel:`Schůzka“.

- :guilabel:`Rozvrh“: rozvrhuje aktivitu a přidává aktivitu do chatu pod
:guilabel:`Plánované aktivity“.
- :guilabel:`Zadat a označit jako hotové“: přidává podrobnosti aktivity do chatu
:guilabel:`Dnes“. Akce není naplánovaná a je automaticky označena jako hotová.
- :guilabel:`Dokončeno a naplánováno další“: přidává podrobnosti o aktivitě do chatu
:guilabel:"Dnes". Akce není naplánovaná, automaticky je označena jako dokončená a vytvoří se nová

- :guilabel:`Zrušit“: vymaže všechny změny provedené v okně „Schedule Activity“.

.. obrázek: aktivity/rozvrh-pop-up.png
:align:center
:alt: Přehled vztahů se zákazníky a možnost plánování aktivit.

..._aktivity/vse:

Všechny plánované aktivity
========================

Pro zobrazení souhrnu aktivit, seřazených podle aplikací, klikněte na čas v hlavičce.
menu v pravém horním rohu.

Pokud jsou naplánovány nějaké aktivity, počet aktivit se zobrazí v červeném bublině na
|hodiny|.

Všechny aktivity pro každou žádost jsou dále rozčleněny do podsekcí, které ukazují, kde v
Pro vykonání aktivity je nutné splnit všechny podúkoly, které jsou v každé sekci uvedeny počtem plánovaných
Aktivit, které jsou označeny jako „pozdě“, „dnes“ a plánované na
:guilabel:`Budoucnost“.

.. příklad::
V aplikaci „Čas na odpočinek“ je naplánována jedna aktivita v rámci celého času volna.
Požadavky na přidělování a šest aktivit je naplánováno v rozhraní Allocation.

Tyto požadavky se objevují ve dvou samostatných seznamech v nabídce všech aktivit: jeden s názvem
‚Čas volna‘ a jeden s názvem ‚Alokace času volna‘.

.... obrázek: aktivita/aktivita-menu.png
:align:center
:alt: Seznam aktivit, který se zobrazuje v hlavním menu. Dvě položky pro čas
V popředí jsou zvýrazněny aplikace, které nejsou nainstalovány.

.. tip::
Možnost „Požádat o dokument“ je dostupná na konci stránky.
seznam všech plánovaných aktivit.

..._aktivity/druhy:

Druhy činností
==============

Pro zobrazení aktuálně konfigurovaných typů aktivit v databázi přejděte na
:menu:Nastavení aplikace --> Diskuse --> Nastavení aktivit --> Typy aktivit.

.. obrázek: aktivity/nastavení-aktivit-typy.png
:align:center
:alt: tlačítko typů aktivit v aplikaci Nastavení pod sekcí Diskuse.

Tím se zobrazí stránka „Typy aktivit“, kde jsou uvedeny všechny existující typy aktivit.

.. tip::
Každá aplikace má seznam typů aktivit, které jsou určeny pro tuto konkrétní aplikaci.
Příkladem je např. zobrazení a úpravy aktivit dostupných pro aplikaci CRM.
:menu:„CRM aplikace --> Konfigurace --> Typy aktivit“.

.. obrázek: aktivity/aktivita-seznam.png
:align:center
:alt: Seznam aktivních typů činností, které jsou již nakonfigurované a k dispozici.

Upravte typy aktivit
-------------------

Chcete-li upravit stávající typ aktivity, klikněte na typ aktivity a
formulář pro vyplnění typu aktivity.

Udělejte si libovolné změny v typu aktivity. Formulář se uloží automaticky, ale můžete jej
Uloženo ručně kdykoliv kliknutím na možnost „Uložit ručně“, která je reprezentována
Ikona „Cloud Upload“ (vpravo nahoře).

Vytvořte nové typy aktivit
-------------------------

Pro vytvoření nového typu aktivity klikněte na tlačítko „Nový“ z
stránce „Typy aktivit“ a načte se prázdný formulář pro typ aktivity.

Do prvního políčka v horní části formuláře zadejte „Název“ a pak následující
informace o formě.

Soubor nastavení aktivit
~~~~~~~~~~~~~~~~~~~~~~~~~

- :guilabel:`Akce“: Vyberte akci spojenou s touto novou aktivitou z rozevírací nabídky
typ. Některé akce vyvolávají konkrétní chování po naplánování aktivity, jako je:

  - :guilabel:`Nahrát dokument“: Pokud je vybráno, automaticky se přidá odkaz na nahrání dokumentu
plánovaná aktivita v chatu.
  - :guilabel:'Hovor' nebo :guilabel:'Schůzka': Pokud je vybráno, uživatelé mají možnost otevřít
kalendář pro výběr data a času aktivit.
  - :guilabel:`Požadavek na podpis“: Pokud je vybrána, zobrazí se odkaz pro otevření okna s požadavkem na podpis.
automaticky přidána do plánované aktivity v chatu. Tohoto vyžaduje aplikace Odoo Sign
aplikace k instalaci.

.. poznámka::
Typy dostupných aktivit se liší podle nainstalovaných aplikací v databázi.

- :guilabel:`Složka“: Vyberte konkrétní složku, kam chcete dokument uložit.
Toto pole se zobrazí pouze v případě, že je vybrána volba „Nahrát dokument“ v poli „Akce“.

- :guilabel:`Výchozí uživatel“: Vyberte uživatele z rolovací nabídky, aby byl automaticky přiřazen
akci pro vybraného uživatele v případě, že je tato aktivita naplánována. Pokud je pole nevyplněné,
Aktivita je přiřazena uživateli, který ji vytvoří.
- :guilabel:`Výchozí souhrn“: zadejte poznámku, která se bude vždy zobrazovat při vytváření této aktivity.

.. poznámka::
Informace v poli :guilabel:`Výchozí uživatel“ a :guilabel:`Popis výchozího souhrnu“ jsou
Při vytváření aktivity jsou zahrnuty, ale mohou být změněny před tím, než bude aktivita
naplánované nebo uložené.

- :guilabel:`Udržet hotové“: Zaškrtněte tuto políčko, pokud chcete uchovat aktivity označené jako „Hotovo“.
je viditelný v pohledu na aktivity (viz. :ref:`aktivita <activities/activity>`).
- :guilabel:`Výchozí poznámka“: zadejte jakékoliv poznámky, které se mají objevit s aktivitou.

Další část aktivit
~~~~~~~~~~~~~~~~~~~~~

Je možné mít jinou aktivitu buď navrhovanou nebo spuštěnou. K tomu je potřeba nakonfigurovat
:guilabel:`Další aktivity“ sekci.

- Výběr typu řetězce: Vyberte buď „Doporučit další činnost“ nebo „Spustit“.
Vyberte možnost „Další aktivity“ z nabídky. V závislosti na vybrané variantě buď
:guilabel:`Navrhnout“ nebo :guilabel:`Zapnout“ pole se zobrazí.

.. poznámka::
pole „Typ řetězení“ se nezobrazí, pokud je zvolené pole „Nahrát dokument“.
vybrána pro akci .

- „Navrhnout / spustit“: v závislosti na tom, co je vybráno pro „Typ řetězení“,
V poli se buď zobrazí :guilabel:`Suggest`, nebo :guilabel:`Trigger“. Vyberte možnost z rozevírací nabídky.
aktivitu, kterou doporučí nebo naplánuje jako následnou aktivitu k aktivačnímu typu.
- :guilabel:`Rozvrh“: nastavte, kdy se další aktivita navrhne nebo spustí.

Nejprve zadejte číselný údaj o tom, kdy je aktivita navrhována nebo spouštěna.

Vedle tohoto pole je vidět pole „Dny“. Klikněte na „Dny“, výchozí hodnota
možnost, aby se objevila nabídka s možnostmi časového rámce. Vyberte si požadovanou volbu z nabídky.
Možnosti jsou: „Dny“, „Týdny“ nebo „Měsíce“.

Nakonec vyberte z roletky, jestli je aktivita naplánovaná nebo spouštěná buď


.. obrázek: aktivity/nova-aktivita.png
:align:center
:alt: Nový formulář činnosti s vyplněnými všemi poli.

.. viz též:
   - :doc:`../produktivita/diskuse`
   - :doc:`../produktivita/diskuse/týmová komunikace`
   - :doc:`../sales/crm/optimize/utilize_activities`
