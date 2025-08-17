===========
Centrum nápovědy
===========

.. |plus| nahradit:: :icon:`fa-plus` :guilabel:`(plus)`

Odoo Helpdesk integruje se **forem**, **e-learningu** a **znalostí** aplikací, aby vytvořil
Centrum nápovědy. Centrum nápovědy je centrální místo, kde týmy a zákazníci mohou vyhledávat
a sdílet podrobné informace o produktech a službách.

.. obrázek: help_center/help-center-enable-features.png
:alt: Přehled nastavení stránky týmu s důrazem na funkce Centra nápovědy.

Konfigurace
=============

Chcete-li aktivovat kteroukoliv z funkcí služby Help Center na týmu Helpdesk, přejděte do nabídky:
Aplikace --> Konfigurace --> Týmy helpdesku“ a vyberte tým nebo vytvořte nový.
<../../helpdesk>. Zkontrolujte, zda je viditelnost týmu nastavena na „Portál pozvaných“.
uživatelé a všichni interní uživatelé („veřejní“) v sekci „Zobrazování a přiřazení“.

Dále je třeba zapnout možnost „Webová stránka“ v poli „Tým“ na formuláři **Helpdesku**.
aktivovat žádnou z funkcí služby Help Center. Když je aktivována jedna nebo více funkcí služby Help Center
Povolíte-li tuto volbu, bude automaticky povolen také formulář „Webová stránka“.

.. nebezpečí::
Protože všechny funkce centra nápovědy vyžadují integraci s jinými aplikacemi, je zapotřebí povolit
Některé z nich mohou vést k instalaci dalších modulů nebo aplikací.

Instalace nové aplikace na databázi One-App-Free vyvolá 15denní zkušební dobu.
z důvodu soudního řízení, pokud „placená předplatná <https://www.odoo.com/pricing>“ nebyla **nebyla přidána k
pokud se databáze neaktualizuje, přestane být aktivní nebo dostupná.

.. viz též:
:doc:`Přehled helpdesku <../../helpdesk>`

Znalosti
=========

Aplikace Knowledge společnosti Odoo je spolupracující knihovna, kde uživatelé mohou ukládat, upravovat a sdílet
informace. Aplikace „Znalosti“ lze použít k publikaci uživatelských příruček a :abbr:`FAQ (Často
Vyžádané otázky) s klienty vně společnosti a zároveň spolupracovat na sdílených
dokumenty.

Aplikace „Znalosti“ je dostupná po celé databázi kliknutím na tlačítko „Znalosti“.
Ikona „Uložit jako záložku“.

.. obrázek: help_center/help-center-knowledge-bookmark-icon.png
:alt: Pohled na zprávu v Helpdesku, která se zaměřuje na ikonu znalostí.

Aplikace Znalost je reprezentována ikonou záložky.

Zapojte tým podpory do projektu znalostí
-----------------------------------

Chcete-li aktivovat funkci **Znalosti** v aplikaci Helpdesk, přejděte na:
Konfigurace --> Týmy helpdesku a vyberte tým nebo vytvořte nový:

Když je tým vybrán nebo vytvořen, zobrazí se podrobné informace o tomto týmu.

V podrobnostech týmu se přesuňte dolů do části „Centrum nápovědy“ a pak klikněte na políčko
po boku pole „Znalosti“ aktivovat funkci **Znalosti**. Po kliknutí se zobrazí nové pole
je označen štítkem „Článek“ a zobrazuje se.

Kliknutím na pole „Článek“ se zobrazí nabídka. Nejprve je zde pouze jedna možnost
ve výběrovém seznamu s názvem „Pomoc“, který Odoo poskytuje standardně. Vyberte
Vyberte si tento článek z nabídky „Pomoc“.

..tip:
Pro vytvoření nového článku přejděte do aplikace „Znalostní databáze“ a pak najeďte kurzorem vedle
hlavičku „Práce“ v levém sloupci. Při pohybu kurzoru tam
Otevírá skrytý plus.

Klikněte na tlačítko „+“ pro vytvoření nového článku ve složce :guilabel:`Workspace`.
:ikonka:`fa-share-alt` , ikona „Sdílet“ a posuvník „Sdílet na webu“.
a až do chvíle, kdy se zobrazí „Článek byl publikován“. Pak může být přidán do týmu **Helpdesku**.

Jakmile je článek vytvořen a přidělen týmu Helpdesku, lze do něj přidat obsah.
Organizované prostřednictvím aplikace **Knowledge**.

.. viz též:
:ref:`Úprava znalostních článků <knowledge/articles_editing/edit-article>`

Hledání článků v helpdeskovém lístku
--------------------------------------

Když členové týmu Helpdesku řeší problém s lístkem, mohou vyhledávat v
obsahu aplikace **Znalosti** pro další informace o problému.

Chcete-li vyhledat články o znalostech, otevřete si lístek – buď z přehledu aplikace Helpdesk nebo
Přejděte do aplikace Helpdesk --> Tikety --> Všechny tikety, vyberte si jeden z nich.
list.

Když je vybrán lístek, Odoo zobrazí podrobné informace o tomto lístku.

Klikněte na ikonu „Znalosti“ (znak záložky), která se nachází v pravém horním rohu stránky, abyste otevřeli
vyskakovací okno pro vyhledávání.

.. obrázek: help_center/help-center-knowledge-search.png
:alt: Pohled na okno pro vyhledávání znalostí z lístku na technickou podporu.

..tip:
Články o znalostech lze také vyhledat stisknutím klávesové zkratky :command:`Ctrl + K`, aby se otevřela příkazová
paletě, poté stiskněte klávesovou zkratku „?“, následovanou jménem požadovaného článku.

Když Odoo zobrazí požadovaný článek, klikněte na něj nebo zvýrazněte název článku (:guilabel:`Článek`).
Stiskněte klávesu Enter. To otevře článek v aplikaci Knowledge.

Pro otevření článku v novém okně stiskněte klávesovou zkratku :command:`Ctrl + Enter`.

..tip:
Pokud je nutné provést hlubší vyhledávání, stiskněte klávesovou zkratku Alt+B. To vám ukáže samostatnou stránku,
které se může objevit při podrobnějších vyhledávání.

Sdílejte článek do centra nápovědy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro umožnění přístupu zákazníkům a návštěvníkům webových stránek musí být informace zveřejněna.
zveřejněna.

.. důležité:
I když je v týmu povolena funkce „Pomoc“, Odoo neposkytuje všechny podsložky.
přispět články na web. Články určené pro zákazníky **musí být** zveřejněny, aby je mohli vidět jejich klienti.
bude na webu k dispozici.

Chcete-li zveřejnit článek, přejděte na požadovaný článek podle výše uvedených kroků a klepněte na
:ikonka_fa_share_alt: ikona „Sdílet“ (zobrazí se nabídka). Posuňte posuvník s označením
„Sdílet na web“ a číst „Článek publikován“.

.. obrázek: help_center/help-center-knowledge-sharing.png
:alt: Pohled na článek o znalostech, který se zaměřuje na možnosti sdílení a publikování.

Řešte lístky s klipsovou krabičkou
----------------------------------

Pomocí „plošky“ lze do článků o znalostech přidat box, který umožní opakované použití, kopírování a odesílání obsahu.
nebo je přidána do popisu vstupenky. To umožňuje týmům udržovat konzistenci při
odpovídat na zákaznické požadavky a minimalizovat čas strávený odpověďmi na opakující se otázky.

Přidejte do článků schránky.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chcete-li vytvořit schránku na klip, přejděte do sekce „Aplikace znalostí“ -> „Pomoc“. Klikněte na existující
umístit článek do podčlánku nebo vytvořit nový kliknutím na plus vedle položky Help.

Zadejte klávesovou zkratku `~` a otevřete seznam příkazů.
<znalosti/úprava článků/příkazy>. Vyberte nebo zadejte :kbd:`clipboard`. Šedý blok
Poté se tento blok přidá na stránku a do něj je možné vložit potřebný obsah.

.. obrázek: help_center/help-center-knowledge-clipboard-options.png
:alt:Zobrazení klipboardu s důrazem na možnosti odeslat a zkopírovat.

.. poznámka::
Pouze pole pro vložení obsahu zobrazují :guilabel:`Použít jako popis“ nebo :guilabel:`Odeslat jako zprávu“.
možnosti, pokud jsou přístupné přímo z **Helpdesku**.

Využijte vstupenky s přepisovacími krabičkami
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Papírové krabičky lze použít k odpovědi na **tiket HelpDesku** jako zprávu nebo přidat
informace do popisu vstupenky.

Chcete-li použít schránku na klipboard v **tiketu Helpdesku**, nejprve otevřete tiket, buď
:guilabel:`Dashboard Helpdesku“ nebo přes „Helpdesk app --> Tickets --> Všechny
Vstupenky“ a výběrem vstupenky z seznamu.

Klikněte na ikonu „Znalosti“ v pravém horním rohu, což otevře vyhledávání.
Okno pro vyhledávání. V tomto okně vyberte nebo vyhledejte požadovaný článek. To zobrazí
článek na stránce v aplikaci **Odoo Knowledge**.

Chcete-li odpovědět na lístek pomocí schránky, klikněte v pravém horním rohu na „Odeslat jako zprávu“.
koutku kliprámu umístěném v těle článku.

Tím se otevře okno „Sestavit e-mail“. V tomto okně vyberte příjemce.
udělejte případné potřebné doplňky nebo úpravy obsahu schránky, pak klikněte na tlačítko :guilabel:`Odeslat“.

..tip:
Chcete-li přidat informace do popisu lístku pomocí klipového boxu, klikněte na tlačítko :guilabel:`Použít jako
popis v horním pravém rohu klipovacího rámečku umístěného v těle článku.
Vyplněním takového pole se **nezmění stávající text v popisu lístku. Obsah z políčka
Do pole s doplňujícím textem se přidává ikonka schránky.

... pomocí helpdesku nebo fóra:

Společenský fór
===============

Fórum komunity poskytuje prostor pro odpovídání zákazníkům na jejich dotazy a sdílení
informace. Integrací fóra s týmem Helpdesku lze zpracovávat požadavky zákazníků na
Převádějí se na příspěvky a sdílejí.

Povolit fóra na týmu Helpdesku
--------------------------------

Chcete-li umožnit komunitní fóra na týmu Helpdesku, začněte procházením
:menuvolba:„Aplikace helpdesku --> Konfigurace --> Týmy helpdesku“ a vyberte tým nebo vytvořte
:doc:`nový <../../helpdesk>“.

Vybrat nebo vytvořit tým odhaluje podrobnosti o týmu. Pokračujte dolů na:guilabel:`Pomoc
Oddíl „Centrum“ funkcí a zapněte: guilabel:„Fórum komunity“, zaškrtnutím políčka vedle něj.

Když je aktivována, objeví se pod ní nové pole s názvem „Fóra“.

Klikněte na prázdné pole „Fóra“ a zobrazí se nabídka. Výchozí hodnotou je pouze jedna
možnost začít, označená jako „Pomoc“. To je možnost, kterou automaticky vytvořila aplikace Odoo.
Funkce „Diskuzní fóra“ byla zapnuta. Vyberte možnost „Pomoc“.
menu, které umožní tento fórum.

Pro vytvoření nového fóra zadejte název do pole „Fórum“ (guilabel:Forums), pak klikněte na
Možnost „Vytvořit a upravit“. V tomto poli může být vybráno více fór.

.. viz též:
:doc:`Dokumentace fóra <../../../websites/forum>`

Vytvořit příspěvek na fórum z helpdeskového lístku
------------------------------------------

Pokud má tým **Helpdesku** zapnuté fórum, lze pak zadaná podání převést na
Příspěvky na fóru.

Pro to vyberte lístek, buď z týmové fronty nebo z nabídky „Tikety – Všechny“
Vstupenky v aplikaci Helpdesk.

V horní části formuláře s podrobnostmi o lístku klikněte na tlačítko „Sdílet na fóru“.

.. obrázek: help_center/help-center-share-on-forum.png
:alt: Přehled stránky fóra webu, který ukazuje dostupné v Odoo Helpdesku.

Když na něj kliknete, objeví se okno s připomenutím. Zde můžete zadat příspěvek do fóra a název tématu.
upravena tak, aby byly opraveny případné chyby nebo upravena tak, aby byla odstraněna jakákoliv vlastnická nebo klientská informace.

:guilabel:„Štítky“ lze také přidat k pomoci při organizování příspěvku v fóru a usnadnit jeho vyhledávání.
uživatele vyhledat. Po provedení všech úprav klikněte na tlačítko :guilabel:`Vytvořit a
Nahlédněte do Posta.

Vytvořit požadavek na podporu z příspěvku na fóru
------------------------------------------

Příspěvky uživatelů portálu lze převést na **tikety Helpdesku**.

Vytvoření lístku provede následující kroky: přejděte na příspěvek fóra a klikněte na ikonu „fa-ellipsis-h“
Ikona „(elipsa)“. Pak klikněte na „Vytvořit požadavek“.

.. obrázek: help_center/help-center-create-ticket.png
:alt:Fórumové vlákno s možností vytvoření požadavku.

Otevře se okno „Vytvořit požadavek“. Udělejte všechny potřebné úpravy v poli „Vytvořit požadavek“.
Zadejte pole „Ticket“ a poté zkontrolujte pole „Pomocná služba“, k níž má být tiket přiřazen.

Klikněte na „Vytvořit a zobrazit lístek“ nebo „Vytvořit lístek“.

.. poznámka::
Původní příspěvek na fóru je odkazován v novém lístku.

e-learning
=========

Kurzy e-learningu společnosti Odoo poskytují zákazníkům další školení a obsah ve formě videí.
prezentace a certifikace/testy. Poskytování dalšího školení umožňuje zákazníkům pracovat
na své problémy přijít sami, ale také si vytvořit hlubší pochopení
služby a produkty, které používají.

Zapněte kurzy e-learningu na týmu podpory
-------------------------------------------

Pro umožnění e-learningových kurzů na týmu Helpdesku přejděte do aplikace Helpdesk:
Konfigurace --> Týmy helpdesku a vyberte tým nebo vytvořte nový:

Na stránce nastavení týmu přejděte do sekce „Centrum nápovědy“ a zaškrtněte políčko vedle
:guilabel:e-learning“. Pod tím se objeví pole s názvem „Kurzy“.

Klikněte na prázdné pole vedle položky „Kurzy“ pod sekcí „e-learning“.
zobrazí se nabídka. Vyberte si z nabídky volný kurz nebo do pole napište název kurzu.
pole a klikněte na tlačítko „Vytvořit a upravit“ pro vytvoření nového kurzu z této stránky.
Kurz může být přiřazen jednomu týmu.

Vytvořte kurz e-learningu
--------------------------

Nový kurz e-learningu lze vytvořit z nastavení týmu Helpdesku, jak je vidět na
krok výše nebo z aplikace **eLearning**.

Chcete-li vytvořit kurz přímo prostřednictvím aplikace eLearning, přejděte na
:menuvolba-->Vzdělávání - Nové“. To odhalí prázdný vzor kurzu, který lze upravit podle potřeby.
upraveno podle potřeby.

Na stránce šablony kurzu přidejte pole „Název kurzu“ a pod ním pole „Štítky“.

Klikněte na záložku „Možnosti“.

V sekci „Přístupová práva“ vyberte uživatele, kteří mohou zobrazit a přihlásit se do kurzu.

Záložka „Ukázat kurz“ určuje, kdo má přístup ke kurzu. Záložka „Přihlásit se“ určuje, zda je možné přihlášení do kurzu.
V poli „Policy“ je uvedeno, jak se mohou přihlásit na kurz.

V seznamu „Zobrazit“ vyberte požadovaný kurz „Typ“.

Přidat obsah do online kurzu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro přidání obsahu do kurzu klikněte na záložku „Obsah“ a vyberte možnost „Přidat obsah“.
Vyberte typ obsahu z roletky a nahrajte soubor nebo vložte odkaz.
klikněte na tlačítko „Uložit“ a klikněte na tlačítko „Přidat sekci“, abyste uspořádali
Jednotlivé úseky.

.. obrázek: help_center/help-center-elearning-course-contents-page.png
:alt: Pohled na kurz pro Odoo Helpdesk.

.. poznámka::
Pro přidání certifikace do kurzu přejděte na:
--> Nastavení, zaškrtněte políčko s názvem „Osvědčení“ a stiskněte tlačítko „Uložit“, abyste aktivovali
prostředí.

.. viz též:
„Tutoriály Odoo: eLearning <https://www.odoo.com/slides/elearning-56>“

Využijte elektronické vzdělávání
---------------------------

Každý kurz musí být zveřejněn, aby zákazníci mohli absolvovat kurz.

..tip:
Pokud je kurz zveřejněn, ale obsah kurzu **nebyl** zveřejněn, mohou zákazníci
se zaregistrovat na webové stránce, ale nemohou se dostat k obsahu kurzu.
Vědět o tom může být užitečné při zveřejňování kurzu poprvé, pokud obsah kurzu
Tyto kurzy jsou určeny k postupnému uvolňování, například týdenní rozvrh hodin.

Pro zveřejnění celého kurzu najednou musí být nejprve publikovány všechny jeho části.
Poté může být kurz zveřejněn.

Chcete-li zveřejnit kurz, vyberte si kurz v nabídce eLearning. Na stránce šablony kurzu
klikněte na tlačítko „Přejít na web“.

Tím se zobrazí přední část webové stránky kurzu. Na horní části webové stránky kurzu přejděte
přepněte přepínač „Nedostupné“ na „Dostupné“.

Publikovat obsah e-learningového kurzu z administrace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro zveřejnění obsahu kurzu z administrace vyberte kurz v sekci eLearning.
přístrojová deska. Na stránce šablony kurzu klikněte na tlačítko „Zveřejněné obsahy“ chytrého widgetu.

Tím se zobrazí samostatná stránka s veškerým publikovaným obsahem souvisejícím s tímto kurzem.
výchozí filtr „Zveřejněno“ z vyhledávací lišty v pravém horním rohu, aby se zobrazily
všechny související obsahy, i ty nezveřejněné.

Klikněte na ikonu „OI View List“ (seznam) pro přepnutí do seznamového zobrazení.

V seznamovém zobrazení je za kurzů v levém horním rohu obrazovky zaškrtávací políčko
vlevo od sloupce „Název“ v hlavičce stránky. Když je tato volba zaškrtnutá, všechny kurzy
Obsah je vybírán najednou.

Po výběru všech kurzů klikněte na libovolnou z políček v sloupci „Je publikováno“.
Zobrazí se okno s potvrzením, že všechny vybrané záznamy jsou určeny k
zveřejněno. Klikněte na tlačítko „Potvrdit“ a všechny kurzy budou automaticky zveřejněny.

.. obrázek: help_center/help-center-elearning-publish-backend.png
:alt:Pohled na zveřejnění obsahu kurzu v administraci Odoo Helpdesku.
