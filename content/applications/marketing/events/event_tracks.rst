============
Sled událostí
============

Odoo Events poskytuje možnost vytvářet, plánovat a spravovat přednášky, semináře, demonstrace.
prezentace apod., které jsou známé jako „Tracky“ v Odoo.

Aplikace Odoo Events má také možnost umožnit účastníkům akce navrhnout přednášky (tracky).
pro událost, která pak může být schválena (nebo zamítnuta).

Konfigurace
=============

Nejprve je potřeba zapnout některé nastavení, abyste z události vytěžili maximum.
stopy.

Pro toto nastavení přejděte na: „Aplikace události --> Konfigurace --> Nastavení“ a zaškrtněte
zaškrtávací políčko vedle nastavení „Rozvrh a tratě“. Tímto způsobem získáte možnost spravovat
a zveřejnit harmonogram s různými tratěmi.

Dále, když je zaškrtnuto toto políčko, pod ním se objeví další dvě možnosti nastavení:
„Živé vysílání“ a „Gamifikace události“.

.. obrázek: event_tracks/track-settings.png
:align:center
:alt:Nastavení kalendáře a tratě v aplikaci Odoo Events spolu s příslušnými možnostmi.

Možnost „Živé vysílání“ umožňuje vysílat skladby prostřednictvím služby *YouTube*.
integrace.

Možnost „Gamifikace události“ poskytuje možnost sdílet kvíz s účastníky akce.
Po ukončení trati se zkoumá, jak moc si studenti osvojili nové vědomosti.

.. poznámka::
Při zapnutém nastavení „Gamifikace události“ se objeví tlačítko „Přidat kvíz“.
na formulářích sledování, což umožňuje rychle vytvořit test.
Specifické pro danou skladbu a její téma.

Jakmile jsou zapnuty všechny požadované nastavení, ujistěte se, že kliknutím na tlačítko :guilabel:`Uložit` potvrdíte
v horním levém rohu stránky „Nastavení“.

Stránka událostí
=================

Chcete-li přistupovat, upravovat nebo vytvářet dráhy pro událost, nejprve se přihlaste k přednastavené události nebo
Vytvořit novou událost (<create_events>).

Pro toto vyberte v nabídce „Aplikace“ možnost „Události“, a buď zvolte některou ze stávajících událostí,
Případně vytvořte nový panel pomocí tlačítka „New“.

Jakmile se dostanete na požadovanou událostní formu, klikněte na tlačítko „Sledování“ v horní části
forma.

..tip:
Pokud se tlačítko „Sledování“ nezobrazí hned, klikněte na „Další“.
: ikonu „fa-sort-desc“ a zobrazí se skrytá chytrá tlačítka. Pak klikněte
:guilabel:`Sledy“ z rozbalovací nabídky.

Kliknutím na tlačítko „Sledování“ se zobrazí stránka „Sledování události“, která je pro danou
konkrétní událost, která zobrazuje všechny tratě (plánované i navrhované) pro danou akci.
nejsou žádné.

.. obrázek: event_tracks/event-tracks-page.png
:align:center
:alt:Stránka s typickým průběhem události v aplikaci Odoo Events.

Sledy jsou zobrazeny v výchozím pohledu „Výhled KanaBanu“ (Kanban), ale je
i možnost zobrazit tyto stopy v :icon:`oi-view-list` :guilabel:`(Seznam)“.
:icon:`oi-view-cohort` :guilabel:`(Ganttova diagram)“
:guilabel:`(Kalendář)“, :icon:`fa-area-chart“ :guilabel:"(Graf)" nebo :icon:`fa-clock-o
Výhled „Aktivita“ (viz obrázek). Všechny jsou přístupné v pravém horním rohu
Stránka „Sledování“.

V výchozím pohledu „Ovládání kanbanu“ (Kanban) jsou stopy kategorizovány do
různé fáze. Výchozí fáze jsou: „Návrh“, „Schváleno“
„Oznámeno“, „Vydáno“ a „Odmítnuto“ (skrytý stupeň).
:guilabel:`Zrušeno“ (složená fáze). Všechny lze upravit, pokud je třeba.

..tip:
Chcete-li upravit stupeň, přejeďte myší nad názvem stupně, klikněte na ikonu „Nastavení“
a vyberte možnost „Upravit“ z nabídky, která se objeví.

Kliknutím na stopu z stránky „Sled událostí“ se zobrazí forma pro tuto stopu.
konkrétní skladba.

Vytvořit událostní stopu
------------------

Na stránce „Sled událostí“ klikněte na položku „Nový“ v pravém horním rohu, abyste zobrazili
prázdný záznam o události, který vytvoří událostní stopu.

.. obrázek: event_tracks/event-track-form.png
:align:center
:alt: Běžný typ události v aplikaci Odoo Events.

Začněte tím, že do políčka „Název“ vložíte nějaký text. Toto pole je **povinné** pro Odoo.

Poté, pokud chcete, přidejte do stopy obrázek pomocí ikony „fa-pencil“
ikonu „Tužka“ (při pohybu kurzoru nad ikonou „FA-Camera“)
:guilabel:`(kamera)` ikona v pravém horním rohu formuláře. Když ji kliknete, přejdete na stránku pro nahrání
požadovaný obrázek pro trať. Tento obrázek se zobrazuje na přední straně webových stránek akce.
Specifické stránky s tracky.

Poté zadejte datum a čas pro stopu a vyberte lokalitu.
kde bude přednáška probíhat.

..tip:
Chcete-li získat seznam všech lokalit pro sledování událostí, které můžete upravovat (a přidávat),
Vyberte si kdykoliv a přejděte na: „Aplikace událostí --> Konfigurace --> Zaznamenání poloh“.

Pak přidejte do stopy :guilabel:`Doba trvání` (minuty).

Pokud je nastavení živého vysílání zapnuto v aplikaci Nastavení události, můžete přidat
odpovídající odkaz v poli „Odkaz na YouTube“ je k dispozici.

Pokud je zaškrtnuto pole „Vždy přidáno do seznamu přání“, pak je hovor automaticky nastaven jako oblíbený.
za každého registrovaného účastníka akce.

Přiřaďte někoho, kdo bude mít na starosti správu této trasy v poli :guilabel:`Zodpovědný`.
výchozí nastavení je přiřazeno osobě, která původně vytvořila stopu.

Poté zkontrolujte, že je stopa přiřazena ke správnému události v poli „Událost“. Výchozí hodnotou je
Toto pole se automaticky vyplní informacemi o události, ke které je daný track přiřazen.
vznikla z původního.

Následně si vyberte, zda chcete přidat existující tagy nebo vytvořit nové, abyste skladbu ještě více uspořádali. Tyto tagy
a odpovídající štítky kategorií jsou využívány na webových stránkách konkrétního festivalu - zejména na
*Rozhovory* na stránce události na webu, přes rozbalovací filtrovací menu.

Pod obecnými informacemi je tři záložky: :ref:`Řečník
<události/sledovací panel hovořícího>“, „Popis <události/popis události>“ a
:ref:`Interaktivita <události/track-interactivity-tab>“.

.._akce/track-řečník-karta:

Řečník
~~~~~~~~~~~

V záložce „Řečník“ formuláře pro sledování události jsou různé položky, které se týkají
určitý mluvčí, který chce vést/pořádat tuto stopu.

.. obrázek: event_tracks/speaker-tab.png
:align:center
:alt:Karta řečníka v aplikaci Odoo Events pro události.

Souhrn kontaktních údajů
***********************

V části „Kontaktní údaje“ postupujte k použití pole „Kontakt“.
vybrat existující kontakt z databáze jako hlavní bod kontaktu pro konverzaci.

Pokud kontakt ještě není v databázi, zadejte jeho jméno a klikněte
Vytvořit“ pro vytvoření a pozdější úpravu kontaktního formuláře nebo klikněte na „Vytvořit a
„edit...“ by měl být převeden na kontaktní formulář nového kontaktu, kde zbytek jejich relevantních
Do formuláře lze zadat informace.

V polích „E-mail“ a „Telefon“ je zatržítko šedé barvy, které obsahuje
informace z kontaktního formuláře vybraného kontaktu. Tyto položky nelze měnit.
Vyberte pole „Kontakt“.

Obsah sekce „Životopis“
*******************

V sekci „Životopis mluvčího“ pokračujte v zadávání informací týkajících se konkrétního řečníka.
povinný k provedení/pořádání této dráhy. Tato sekce může automaticky vyplnit na základě :guilabel:`Kontaktu`.
vybrané v sekci „Kontaktní údaje“. Pokud ne, zadejte potřebné informace
pole.

.. poznámka::
Tato informace se objevuje na stránce události na webu, konkrétně na stránce sledování.
poskytování více informací o řečníkovi účastníkům konference.

Začněte zadáním jména, e-mailové adresy a telefonního čísla.
mluvčí.

Poté přidejte obrázek, který se bude zobrazovat vedle profilu řečníka na webových stránkách akce.
ikonu „fa-pencil“ (pravítko) v případě, že kurzor přejde nad
:ikonka:fotografie:guilabel:(fotografie): ikona. Po kliknutí se přejde na nahrání požadované fotografie
řečník.

Poté zadejte „pracovní pozici“ pro označeného řečníka, následovanou
:guilabel:`Název společnosti“ spojený s mluvčím.

V poli „Životopis“ postupujte k vložení vlastního životopisu se všemi informacemi o mluvčím.
informace.

.._události/karta popisu trasy:

Karta popisu
~~~~~~~~~~~~~~~

V poli popisu událostního tracku je prázdné pole pro vložení textu.
do ní lze vložit informace, které se zobrazí na stránce konkrétní skladby na
webové stránky akce.

.._události/sledování interakce s tabulkou:

Interaktivní záložka
~~~~~~~~~~~~~~~~~

V záložce „Interaktivita“ na formuláři pro sledování událostí je v počátku pouze jedna možnost:
:guilabel:`Kouzelný tlačítko“.

.. obrázek: event_tracks/interactivity-tab.png
:align:center
:alt:Karta interaktivity v aplikaci Odoo Events u událostního záznamu.

Když je zaškrtnuto políčko vedle tlačítka „magický tlačítko“, Odoo zobrazí tlačítko s výzvou k akci.
účastníkům na boku dráhy, když se závod koná.

Po zaškrtnutí této položky se objeví další tři možnosti, všechny jsou spojeny s
:guilabel:`Kouzelný tlačítko“:

- :guilabel:`Titulní stránka tlačítka“: zadejte název, který se na tlačítku pro účastníky objeví.
- :guilabel:`URL cílového tlačítka“: zadejte URL, která přivede účastníky, kteří na tlačítko klikají,
konkrétní stránku.
- :guilabel:`Tlačítko zobrazení“: Zadejte číslo do pole a tlačítko se objeví s daným číslem.
:guilabel:`minut po startu trati“.

.. poznámka::
Tlačítko pro přidání magického efektu se objeví pouze tehdy, pokud je více než jeden zveřejněný snímek.

.. _akce/přidat_kvíz:

Přidejte tlačítko pro hru.
~~~~~~~~~~~~~~~

Tlačítko „Přidat kvíz“ se zobrazí pouze na formulářích pro sledování události, pokud je zapnuté funkce *Gamifikace události*.
v nastavení Odoo Events je zapnutá funkce události.

Kliknutím na tlačítko „Přidat test“ přidejte do události kvíz. Když tak učiníte, objeví se samostatný
stránka, na které lze vytvořit a nakonfigurovat kvíz s otázkami o událostech.

.. obrázek: event_tracks/add-quiz.png
:align:center
:alt:Stránka Přidat test v aplikaci Odoo Events pro událostní stopu.

Začněte vložením názvu kvízu do prázdného pole na horní části stránky. Poté
Soutěžící by měli mít možnost zodpovědět otázky opakovaně a zaškrtnout políčko vedle
:guilabel:`Povolit opakované pokusy“.

Políčka „Událost“ a „Sled události“ jsou neupravitelná a zobrazují
odpovídající událost a trať, ke které je tato soutěž spojena.

Klikněte na „Přidat řádek“ pod sloupcem „Otázka“, abyste přidali otázku do kvízu.
Tím se zobrazí okno „Vytvořit otázky“.

.. obrázek: event_tracks/create-questions.png
:align:center
:alt:Okno vytváření otázek na události specifické pro kvíz v aplikaci Odoo Events.

.. poznámka::
Všechny otázky v kvízu o stopách jsou založeny na výběru možností.

Do vyskakovacího okna zadejte otázku do prázdného pole v horní části a pak klikněte na tlačítko „Přidat“.
a kliknutím na tlačítko „Přidat řádek“ se objeví nový řádek s
je možné zadat odpověď.

Jakmile zadáte odpověď, přejděte k určení, že je to správná.
odpověď označením políčka v sloupci „Korektní“.

Pak je možné přidat bodové hodnocení do sloupce „Body“.

A pokud existují nějaké další komentáře, které by měly doplnit odpověď, zadejte je do
:guilabel:`Další komentář` pole.

.. poznámka::
V polích „Korektní“, „Bodů“ a „Doplňující komentář“ jsou všechna pole
nepovinné.

Tento proces opakujte pro všechny odpovědi.

Pro odstranění možnosti odpovědi klikněte na ikonu „koš“
pravicové.

Jakmile jsou všechny požadované odpovědi (a jejich konfigurace) dokončeny, klikněte na tlačítko :guilabel:`Uložit a
Zavřít okno a vrátit se zpět na formulář kvízu o trati. Nebo klikněte
:guilabel:`Uložit a Nové“ pro uložení této otázky a okamžitě začít vytvářet další otázku na novém
Pop-up okno „Vytvořit otázky“.

K odstranění jakéhokoliv dotazu z kvízu klikněte na ikonu „odpadkový koš“
pravicového křídla otázky.

Publikovat událostní stopu
===================

Jakmile jsou na události všechny požadované konfigurace dokončeny, klikněte na požadovaný bod.
se nachází v horním pravém rohu zobrazení (např.: guilabel:„Potvrzené“
např. „Oznámeno“, „Oznámeno“ apod.)

.. poznámka::
Stupeň tratě lze také změnit z stránky „Sledování událostí“, kde je možné
Požadovaná karta sledování lze přetáhnout a vhodit do příslušného stupně Kanban.

Pokud událostní stopa ještě nebyla zveřejněna a je přesunuta do fáze „Zveřejněno“,
Odoo automaticky publikuje skladbu na webu akce.

Akci můžete také zveřejnit otevřením požadované akce a kliknutím na
Klikněte na tlačítko „Přejít na web“ a pak zobrazte stránku sledování (a
pro účastníky akce, přepněte na :icon:`fa-toggle-off` :guilabel:`Nevydáno“
na vrchol stránky a změnit jej na :icon:`fa-toggle-on` :guilabel:`Zveřejněno“; tím se z červené barvy stane
zelenou a přístupnou pro účastníky.

.. obrázek: event_tracks/published-toggle.png
:align:center
:alt:Možnosti podmenu události související s tratí na webu pro události postaveném na Odoo Events.

.. viz též:
   - :doc:`create_events“
   - :doc:`track_manage_talks“
