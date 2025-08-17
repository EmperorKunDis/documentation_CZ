=========
e-learning
=========

Aplikace eLearning umožňuje snadné nahrazování obsahu, stanovování učebních cílů a správu
účastníci mohou sledovat pokrok studentů, vyhlašovat odměny a zapojit účastníky do smysluplných aktivit.
Učení je pro ně zábavou a zvyšuje jejich produktivitu.

.. důležité:
Můžete spravovat své e-learningové obsahy na **předním konci** nebo na **zadním konci**. Na **předním konci**
umožňuje vytvářet obsah rychle z webu a **zadní část** zajišťuje
další možnosti a umožňuje spolupráci. Tato dokumentace se zaměřuje na použití zadního konce
Vytvářejte svůj obsah.

.. viz též:
„Tutoriály Odoo: eLearning <https://www.odoo.com/slides/elearning-56>“

Kurzy
=======

Pokud se vám zobrazí nabídka „eLearning --> Kurzy --> Kurzy“, můžete si prohlédnout všechny své
kurzy.

Klikněte na název kurzu, abyste mohli upravit kurz v administraci. Klikněte na „Zobrazit kurz“
Přihlaste se do kurzu na přední straně.

Tvorba kurzu
---------------

Klikněte na „Nový“ pro vytvoření nového kurzu. Když se stránka otevře, můžete přidat své
:guilabel:„Název kurzu“ a jednu nebo více „Štítků“, které popisují váš kurz. Můžete také přidat
obrázek, který ilustruje váš kurz, přetažením myši na místo pro obrázek kamery a kliknutím.
na ikonu úprav. Čtyři záložky vám umožní upravit kurz dále:
:ref:`Obsah <elearning/obsah>`, :ref:`Popis <elearning/popis>`,
:ref:`Možnosti <elearning/options>“ a „Karma <elearning/karma>“.

.. obrázek: elearning/elearning-course-creation.png
:align:center
:alt: Vytvořte si svůj e-learningový kurz.

..._e-learning/obsah:

Obsahová záložka
~~~~~~~~~~~

Tato záložka umožňuje spravovat obsah vašeho kurzu. Klikněte na tlačítko „Přidat sekci“, abyste svůj kurz rozdělili do několika částí.
se dělit na různé části. Klikněte na tlačítko „Přidat obsah“ pro vytvoření
Klikněte na tlačítko „Přidat certifikaci“ v části „Vytvoření obsahu“.
úroveň porozumění vašich účastníků, osvědčit jejich dovednosti a motivovat je.
je součástí aplikace „Průzkumy“ (viz dokumentaci).

.._e-learning/popis:

Karta popisu
~~~~~~~~~~~~~~~

Můžete přidat krátkou anotaci nebo informace související s vaším kurzem v poli :guilabel:`Popis`.
tabulka, která se objevuje pod názvem vašeho kurzu na webu.

.. obrázek: elearning/kurz-popis.png
:align:center
:alt:Přidejte popis do svého kurzu.

..._e-learning/možnosti:

Karta Možnosti
~~~~~~~~~~~

V záložce „Možnosti“ jsou k dispozici různé konfigurace:
:ref:`Kurz <elearning/course>`,  :ref:`Komunikace <elearning/communication>`,
:ref:`Přístupová práva <elearning/access-rights>“ a „Zobrazení <elearning/display>“.

.. obrázek: elearning/options-tab.png
:align:center
:alt: Přehled nabídky Možnosti

... e-learning/kurz:

Kurz
******

Přiřaďte k vašemu kurzu uživatele s rolí „Zodpovědný“. Pokud máte více webů, použijte
:guilabel:`Webová stránka“ pole, aby se kurz zobrazoval pouze na vybrané webové stránce.

... e-learning/komunikace:

Komunikace
*************

- :guilabel:`Povolit recenze“: zaškrtněte políčko, abyste umožnili účastníkům lajkovat a komentovat vaše obsahy.
aby vám zaslali hodnocení vašeho kurzu.
- :guilabel:`Fórum“: Přidejte do kurzu vlastní fórum (zobrazeno pouze pokud je funkce „Fórum“ aktivována).
(povoleno v nastavení aplikace).
- :guilabel:`Oznámení o novém obsahu“: vyberte e-mailový šablonu, kterou pošlete svým účastníkům.
nahrát nový obsah. Klikněte na tlačítko vnitřního odkazu (:guilabel:`➜`) a získáte přístup k e-mailové adrese
editor šablony.
- :guilabel:`Oznámení o dokončení“: vyberte e-mailový vzor, který je odeslán vašim účastníkům po
dostat se na konec kurzu. Klikněte na tlačítko vnitřního odkazu (:guilabel:`➜`) pro přístup
editor šablony e-mailu

... elearning/přístupová práva:

Práva přístupu
*************

- :guilabel:`Předpoklady“: nastavte jeden nebo více předmětů, které uživatelům doporučujete absolvovat před
přístup ke svému kurzu;
- Zobrazit kurz: určete, kdo může vidět váš kurz a jeho obsah.
:guilabel:`Každý“, :guilabel:`Přihlášen“ nebo :guilabel:`Účastníci kurzu“.
- :guilabel:`Zaregistrujte se do politiky“: určete, jak lidé registrují svůj kurz. Vyberte:

   - :guilabel:`Otevřený“: pokud chcete, aby byl váš kurz k dispozici pro všechny.
   - :guilabel:Pouze na pozvánku“: pokud se mohou přihlásit pouze lidé, kteří dostali pozvánku.
Pokud je vybráno, vložte do pole „Zpráva o přijetí“ popis procesu přihlášení na kurz.
Toto sdělení se objevuje na vašem webu pod názvem kurzu.
   - :guilabel:`Na platbu“: pokud se mohou účastnit pouze lidé, kteří si zakoupili váš kurz.
:guilabel:`Placené kurzy“ musí být zapnuty, abyste měli tuto možnost. Pokud vyberete
:guilabel:`Platba“, musíte přidat produkt pro svůj kurz.

.. poznámka::
Pouze produkty, které jsou nastaveny s :guilabel:`Course` jako jejich :guilabel:`Produkt typu`,
Veřejně zobrazené.

.. e-learning/zobrazit:

Display
*******

- :guilabel:`Školení“: obsah kurzu se zobrazuje jako školicí program a kurzy musí být
v pořadí navrženém žalobcem.
- :guilabel:`Dokumentace“: obsah je dostupný v libovolném pořadí. Pokud zvolíte tuto možnost,
můžete si vybrat, která stránka se má zobrazit na hlavní stránce kurzu.
:guilabel:`Oblíbené obsahy“ pole.

... e-learning/karma:

Karta karmy
~~~~~~~~~

Tato záložka je o herních prvcích, které dělají e-learning zábavný a interaktivní.

V sekci „Odměny“ vyberte, kolik bodů karmy chcete udělit svým studentům.
Když dokončí nebo zkontrolují kurz.

V sekci „Přístupová práva“ definujte kredity potřebné pro možnost „Přidat recenzi“.
Klikněte na „Přidat komentář“ nebo „Hlasovat“.

.. poznámka::
Vyberte si z nabídky kurzů a klikněte na tlačítko „Kontaktovat účastníky“ pro dosažení lidí,
se zapsal do kurzu.

... elearning/kurzy:

Skupiny kurzů
-------------

Použijte skupiny kurzů, abyste uživatelům poskytli informace a umožnili jim filtrovat kurzy z
Dashboardu „Všechny kurzy“.

Můžete je spravovat kliknutím na:
Skupiny kurzů. Klikněte na tlačítko Nový, abyste vytvořili novou skupinu kurzů. Přidejte :guilabel:Skupina
Název`, zaškrtněte políčko „Položka menu“ a umožněte uživatelům vyhledávat podle skupiny předmětů na webu.
a přidat štítky do sloupce „Název štítku“. Pro každý štítek můžete zvolit odpovídající barvu.

Nastavení
--------

Můžete zapnout různé funkce, které vám umožní upravit svá školení, kliknutím na:
--> Konfigurace --> Nastavení“:

- **Ověření znalostí a certifikace dovedností**: hodnocení znalostí vašich účastníků a certifikaci jejich dovedností;
- Placené kurzy: prodej přístupu ke svým kurzům na vašem webu a sledování příjmů;
- **Masová pošta**: aktualizovat všechny účastníky najednou prostřednictvím hromadných e-mailů.
- **Fórum**: vytvořit komunitu a umožnit účastníkům odpovídat na otázky ostatních.

... elearning/vytvorit-obsah:

Obsah
=======

Správa obsahu probíhá na adrese: `eLearning --> Courses --> Contents` a kliknutím.
:guilabel:Nové“ vytvořit obsah. Přidejte „Název obsahu“, a pokud chcete
:ref:`Štítky <elearning/tags>“, pak vyplňte příslušné informace v jednotlivých záložkách.

.. obrázek: elearning/elearning-content-tab.png
:align:center
:alt: Vytvářejte svůj obsah.

Karta dokumentu
------------

- :guilabel:`Kurz“: vyberte kurz, ke kterému váš obsah patří.
- :guilabel:`Typ obsahu“: vyberte typ svého obsahu.
- :guilabel:`Odpovědná osoba“: přidejte odpovědnou osobu za obsah vašeho webu.
- :guilabel:`Délka kurzu“: uveďte dobu, po kterou je kurz k dispozici.
- :guilabel:`Povolit stažení“: umožní uživatelům stáhnout obsah prezentace. Tato možnost je dostupná
při obsahu dokumentu.
- :guilabel:`Povolit náhled“: kurz je přístupný pro každého.
- :guilabel:`Počet veřejných zobrazení“: zobrazuje počet shlédnutí ze strany nepřihlášených uživatelů.
- :guilabel:'Počet celkových zobrazení': zobrazí celkový počet shlédnutí (nezaregistrované a registrované)
účastníky (participants).

Karta popisu
---------------

Můžete přidat popis svého obsahu, který se zobrazuje na předním konci v části „O nás“
obsah kurzu.

Další záložka s názvem „Přídavné zdroje“
------------------------

Klikněte na tlačítko „Přidat řádek“ pro přidání odkazu nebo souboru, který podpoří učení vašich účastníků.
Zobrazuje se ve vašem kurzu na webu.

.. obrázek: elearning/doplněk.png

:alt:Další zdroje

... e-learning / test:

Kvízová záložka
--------

Z této záložky můžete vytvořit test, který zhodnotí znalosti vašich studentů na konci kurzu.

V sekci „Body za odměnu“ můžete dát konkrétní počet bodů podle
Jaké pokusy potřebují k tomu, aby správně odpověděli na otázku. Pak vytvořte své otázky a
Možné odpovědi kliknutím na „Přidat řádek“. Otevře se nové okno, do kterého zadejte otázku
Vyplněním „Název otázky“ a přidáním více odpovědí kliknutím na „Přidat
line`. Zatrhněte políčko „Je správná odpověď“ a označte jednu nebo více odpovědí jako správnou.
Vyplňte pole „Komentář“ a zobrazí se další informace při výběru odpovědi
soutěžící.

..._elearning/tagy:

Obsahové štítky
------------

Štítky obsahu pomáhají uživatelům třídit obsah z panelu „Obsahy“ .

Můžete je spravovat v sekci „E-learning“ - „Nastavení“ - „Štítky obsahu“. Klikněte
:guilabel:`New“ pro vytvoření nového štítku.

Zveřejněte svůj obsah
====================

Vše, co bylo vytvořeno na zadní straně, musí být publikováno ze strany přední. Nezveřejněný obsah je
Vždy viditelný na vašem webu, ale stále je potřeba jej zveřejnit, aby byl k dispozici vaší cílové skupině.

Chcete-li publikovat svůj obsah na webu, musíte se přihlásit na jeho přední stranu. K tomu klikněte na
tlačítko „Přejít na web“ a zaškrtněte možnost „Zveřejnit“.
v pravém dolním rohu.

.. obrázek: elearning/elearning-publish-button.png

:alt:Zveřejněte svůj obsah.
