============================
Průběh kampaně
============================

„Průběh“ je celkový „proces“ marketingové automatizace kampaně.
Jednotlivé kampaně mohou obsahovat jediný pracovní postup, ale jeden pracovní postup může být složen z libovolného počtu
aktivit, které uspokojí potřeby kampaně.

.. obrázek:: workflow_activities/workflow-activities.png
:align:center
:alt: Průběh kampaně v marketingové automatizaci Odoo.

Řetězec pracovních postupů tří aktivit; poslední dítě má typ spouštěče
<marketing_automation/trigger-type> pro „E-mailová zpráva neotevřená“.

... marketingová automatizace a aktivity:

Aktivita
==========

Aktivita je metoda komunikace nebo akce serveru uspořádaná v průběhu pracovního postupu.
v rámci kampaně; jsou základními stavebními kameny práce s kampaní.

Novou aktivitu lze přidat do průběhu kampaně na formuláři kampaně volbou existující kampaně nebo
:vytvoření nové kampaně (marketingová automatizace / kampaně) z nabídky
Aplikace automatizace --> Panel kampaní, pak tlačítko „Přidat novou aktivitu“
sekci „Průběh“. To otevře okno „Vytvořit aktivity“.

Nejprve definujte název aktivity v poli „Název aktivity“ a poté vyberte
:ref:`druhu činnosti <marketing_automation/activity-types>`, která se má spustit z
:guilabel:`Typ aktivity“ pole.

Poté nastavte spouštěč aktivity podle návodu v části „Spouštěče aktivit“ a pokud chcete, můžete také
:ref:`Doba platnosti <marketing_automation/expiry-duration>` a :ref:`Doména
<automatizace marketingu/aktivita - doména> aktivity.

Jakmile je aktivita plně nakonfigurovaná, klikněte na tlačítko „Uložit a zavřít“, abyste ji přidali do kampaně.
průběh práce nebo klikněte na tlačítko „Uložit a nový“ pro přidání aktivity do průběhu práce a otevření nového
Okno „Vytvořit aktivity“ pro přidání další aktivity. Kliknutím na „Smazat“
Zavře okno s upozorněním, aniž by se aktivita uložila.

.. obrázek: workflow_activities/create-activities.png
:align:center
:alt:Popis okna pro vytváření aktivit.

.. marketingová automatizace / typy aktivit:

Druhy aktivit
--------------

V aplikaci Marketing Automation jsou k dispozici tři různé typy aktivit:

- :ref:`E-mail <marketing_automation/email-activity-type>“: e-mail, který je zasílán na cílovou adresu
diváci.
- „Akce serveru“: interní akce na serveru
databáze, která se spouští.
- :ref:`SMS <marketing_automation/sms-activity-type>“: textová zpráva, která je odeslána na cílovou adresu
diváci.

.. marketingová automatizace / typ e-mailové aktivity:

E-mail
~~~~~

Pokud je vybrána položka „E-mail“ jako typ aktivity, objeví se možnost „Vyberte si
V poli „Šablona“ je k dispozici šablona „Poštovní zásilka“.

Pro vytvoření nového šablonu přímo z pole „Šablona e-mailu“ začněte psát název.
nového šablony, pak vyberte možnost „Vytvořit a upravit…“ a zobrazí se možnost „Vytvořit
Okno marketingového šablony. Přejděte k vytvoření a konfiguraci nové e-mailové šablony.

.. obrázek:workflow_activities/email-activity-type.png
:align:center
:alt:Volba vytvořit a upravit e-mailovou zprávu na okně pro přidání aktivit.

Jakmile je e-mailový šablonu nakonfigurován, klikněte na tlačítko „Uložit a zavřít“, abyste uložili aktivitu.
Návrat do okna „Vytvořit aktivity“, abyste mohli pokračovat v konfiguraci
:ref:`spouštěč <marketingová automatizace/spouštěč>“.

.. poznámka::
Název použitý pro šablonu e-mailu **musí být** jedinečný oproti všem ostatním šablonám e-mailů.
Titulek v kampani a také předmět e-mailu.

.. viz též:
:doc:`Vytváření a konfigurace e-mailových šablon <../email_marketing>`

.. marketingová automatizace / SA aktivity typu:

Serverová akce
~~~~~~~~~~~~~

Pokud je vybrána volba „Akce serveru“ jako typ aktivity, zobrazí se možnost
V poli „Akce serveru“ je k dispozici pole „Zvolte akci“.
rozbalovací nabídka s přednastavenými akcemi serveru pro kampaň.
:guilabel:`Cíl“ modelu. Volitelně můžete vytvořit novou akci „Vytvoření serveru“.
<marketing_automation/create-sa>.

.. obrázek:: workflow_activities/sa-activity-type.png
:align:center
:alt: Výběr serverové akce v okně pro vytváření aktivit.

Po výběru přednastavené akce serveru není potřeba žádná další konfigurace typu aktivity.
Klikněte na tlačítko „Uložit a zavřít“ pro uložení aktivity a vraťte se do kroku „Vytvořit aktivity“.
přepínač v okně, abyste mohli konfigurovat:

..tip:
Pro zobrazení všech akcí serveru v databázi zapněte režim vývojáře a přejděte na
:menu_selection:`Nastavení aplikace --> Technické --> Akce --> Akce serveru“ panelu.

... _marketing_automation/create-sa:

Vytvořit novou akci serveru
**************************

Možnost vytvořit novou akci serveru je také k dispozici. Chcete-li tak učinit, zadejte :guilabel:`Server
V poli „Akce“ zadejte název nové akce, pak klikněte na „Vytvořit a upravit…“.
odhalí prázdné pole „Akce pro vytvoření serveru“ s oknem pro přizpůsobenou akci pro vytváření serveru.
musí být vytvořen a nakonfigurován.

.. obrázek:: workflow_activities/create-sa.png
:align:center
:alt:Popis okna pro vytvoření serveru.

V okně „Akce vytvořit server“ vyberte typ akce serveru.
Konfigurační pole se mění v závislosti na zvoleném typu:

- :guilabel:`Aktualizovat záznam“: aktualizujte hodnoty záznamu.
- :guilabel:`Vytvořit aktivitu“: vytvořte aktivitu s aplikací *Diskuse*.
- :guilabel:`Odeslat e-mail“: poslat zprávu, poznámku nebo e-mail pomocí aplikace *Diskuse*.
- :guilabel:`Odeslat SMS“: odeslat SMS a zaznamenat je do dokumentů pomocí aplikace *SMS*.
- :guilabel:`Přidat sledující“ nebo „Odebrat sledující“: přidejte nebo odeberte sledující na záznam
s aplikací Discuss*.
- :guilabel:`Vytvořit záznam“: vytvoří nový záznam s novými hodnotami.
- :guilabel:`Spustit kód“: spusťte blok Pythonového kódu.
- :guilabel:`Odeslat webhookovou notifikaci“: odeslat požadavek HTTP k externímu systému.
- :guilabel:`Spustit stávající akce“: definujte akci, která spouští několik dalších serverů
akce.

Po nastavení serverového kroku klikněte na tlačítko :guilabel:`Uložit a zavřít`, abyste uložili aktivitu.
Vraťte se do okna „Vytvoření aktivit“, abyste nakonfigurovali :ref:`spouštěč
<automatizace marketingu/spouštěč>.

..tip:
Některé typy akcí serveru mají pokročilá nastavení k dispozici, když je zapnutý režim vývojáře.
je aktivována, například specifikací skupin „Dovolené skupiny“, které mohou tento server spustit.
akce.

.. _marketingová automatizace/SMS aktivita typu:

SMS
~~~

Pokud je vybrána aktivita „SMS“, můžete zvolit možnost „Vyberte si
V poli „Šablona“ je k dispozici šablona SMS.

Pro vytvoření nového šablonu přímo z pole „SMS šablona“ začněte psát název
nový šablonu a vyberte možnost „Vytvořit a upravit ...“ k zobrazení možnosti „Vytvořit marketing“.
Okno s náhledem šablony. Přejděte k vytvoření a konfiguraci nové SMS šablony.

.. obrázek: workflow_activities/sms-activity-type.png
:align:center
:alt:Volba vytvořit a upravit e-mailovou zprávu na okně pro přidání aktivit.

Jakmile je nastaven šablona SMS, klikněte na tlačítko „Uložit a zavřít“, abyste uložili aktivitu a vrátit se zpět.
do okna „Vytvořit aktivity“, abyste mohli konfigurovat :ref:`spouštěč
<automatizace marketingu/spouštěč>.

.. viz též:
:doc:`Vytváření a konfigurace šablon SMS <../sms_marketing>`

... marketingová automatizace/spouštěč:

Spoušť
-------

Jakmile je konfigurován typ aktivity (:ref:`<marketing_automation/activity-types>`,
Okno „Vytvořit aktivity“ slouží k určení, kdy má být aktivita spuštěna.
Toto se provádí v poli skupiny „Spouštěč“.

.. obrázek:: workflow_activities/trigger.png
:align:center
:alt:Oblast spouštěcího pole v okně s náhledem na tvorbu aktivit.

Určit zpoždění pro provedení aktivity od chvíle, kdy došlo k :ref:`spouštěcímu typu
V poli Interval číslo zadejte celé číslo.
(např. číslo 2 je platné, stejně jako 0 a 1,5 není).

Dále vyberte jednotku času pro číslo intervalu v rozevíracím seznamu typu intervalu.
Možnosti jsou: „hodiny“, „dny“, „týdny“ a „měsíce“.

Příklad:
Pokud je číslo intervalu nastaveno na „0“ a typ intervalu je nastaven na „Hours“,
Aktivita se spustí ihned po tom, co nastane typ spouštěče (na další plánovaný běh).
mail:Email Queue Manager cron (<email-issues-outgoing-execution-time>).

... automatizace marketingu / typ spouštěče:

Typ spouště
~~~~~~~~~~~~

Pro definici události, která spouští aktivitu, vyberte typ spouštěče z
kliknutím na tlačítko „Drop down“

- :guilabel:`začátek průběhu“: aktivita se spouští, když je kampaň zahájena.

U ostatních typů spouštěče se zobrazí pole „Aktivita“ s názvem guilabel:
další aktivity v kampani. Vybráním jednoho z nich se tato aktivita stává
:ref:`dětské aktivity <marketing_automation/child-activities>`, které se spouští přímo po
vybrat:guilabel:`Aktivita“:

- :guilabel:`další aktivita“: provedení další aktivity v kampani.
- :guilabel:`E-mail otevřený“: účastník otevřel e-mailovou zprávu s aktivitou.
- :guilabel:`E-mail: neotevřený“: e-mailová zpráva účastníka **nebyla otevřena**.
- :guilabel:`Odpověď na mail: odpověděl/a účastník/ka aktivitě“: e-mailová zpráva byla účastníkem aktivit odpovězena.
- :guilabel:`E-mail: neodpovězeno“: e-mailová zpráva činnosti nebyla odpovězena účastníkem.
- :guilabel:`E-mail: kliknutí na odkaz v e-mailu“: účastník klikl na odkaz v e-mailu s aktualitou.
- :guilabel:`E-mail nebyl kliknutý“: odkaz v e-mailu o aktualitě nebyl **nebyl kliknutý**
účastník.
- :guilabel:`E-mail: odmítnutý“: e-mailová aktivita byla zamítnuta.
- :guilabel:`SMS: kliknutí na odkaz v SMS“: účastník klikl na odkaz v SMS zprávě.
- :guilabel:Nepočítáno SMS: neklikl jsem odkaz v SMS zprávě.“
- :guilabel:`SMS: odmítnuto“: aktivita SMS byla odmítnuta.

Příklad:
Pokud je nastaven typ spouštěče na „Pošta: kliknutí“, tato aktivita se převádí na
:ref:`dětské aktivity <marketing_automation/child-activities>“ a bude provedeno po
účastník klikne na odkaz z aktivity definované v poli „Aktivita“.

.. marketingová automatizace/doba platnosti:

Doba platnosti
---------------

Volitelně může být definována doba platnosti v rámci :guilabel:`Create Activities`.
okno s možností zrušení provedení této činnosti po určité době. Vyberte
Tento políčko odhaluje pole „Zrušit po“ s vstupy *intervalu* a *typ intervalu*.

Zadejte celé číslo v rozsahu zadaném pro pole „Číslo intervalu“ (například 2 je platné, stejně jako 0 a 1,5).
ne). Pak vyberte jednotku času pro počet interválů v poli typu intervalu.
Možnosti jsou: „hodiny“, „dny“, „týdny“ a „měsíce“.

Příklad:
Pokud je číslo intervalu nastaveno na „2“ a typ intervalu je nastaven na „Dny“,
Pokud se tento typ spouštěče nevykoná do dvou dnů, bude aktivita zrušena.

.. marketingová automatizace/aktivita doména:

Doména aktivity
---------------

Sekce „Doména“ ve formuláři „Vytvořit aktivity“ obsahuje pole pro
další filtrování cílové skupiny aktivit.

V poli filtru aktivit se zobrazí pouze aktivity, které jsou vázány na tuto aktivitu a jejich děti.
<automatizace marketingu/dětské aktivity>, dále na konkrétní skupinu filtru kampaně.
Proces je stejný jako definování filtrů:ref:`<marketing_automation/defining-filters>`.
kampaně a pole filtrů jsou specifická pro cílovou skupinu.
kampaně.

Značky „#“ vedle pole „Filtr aktivit“ ukazují, kolik záznamů
jsou v současné době cílem této filtrační aktivity.

Ve filtru „Aplikovaný filtr“ se zobrazují filtry kombinované v filtru „Aktivní filtr“.
a děděná kampaň:doc:`Filtr <cílová skupina>`. Toto pole je čtené.

Značky „#“ vedle pole „Použité filtry“ ukazují, kolik záznamů
V současné době je cílem aktivit celkem 100 dětí.

... marketingová automatizace / dětské aktivity:

Dětské aktivity
================

Aktivita spojená s jinou aktivitou a vyvolaná jí je známá jako *dítě.
činnosti*

Aktivita, která spouští aktivitu dítěte, se nazývá jejím „*rodičovským aktem*“.

Dětskou aktivitu lze přidat do průběhu kampaně, když se kurzorem zobrazí :guilabel:`➕ Přidat dítě
tlačítko „Aktivita“ umístěné pod požadovanou nadřazenou aktivitou.

Aktivita dítěte má své vlastní typy spouštěčů, viz
rodič:odkaz na typ aktivity (<marketing_automation/activity-types>)*E-mail*, *SMS* nebo *Server
Akce*) a jsou následující:

.. záložky::

....... tab::E-mail

.. obrázek:: workflow_activities/email-trigger-types.png
:align: střed
:alt: Typ spouštění pro dětské aktivity e-mailové aktivity.

Každý spouští dětskou aktivitu na následujících podmínkách rodičovské aktivity:

      - :guilabel:`Přidat další aktivitu“: provedeno po rodičovské aktivitě.
      - :guilabel:`Otevřeno“: e-mail byl otevřen účastníkem.
      - :guilabel:„Nepřečteno“: e-mail nebyl účastníkem otevřen.
      - :guilabel:`Odpovězeno“: e-mail byl odpovězen.
      - :guilabel:`Neposlal odpověď“: e-mail nebyl účastníkem odeslán.
      - :guilabel:`Kliknutí na odkaz v e-mailu“: účastník klikl na odkaz v e-mailu.
      - :guilabel:"Nepočítáno": odkaz v e-mailu nebyl účastníkem kliknut.
      - :guilabel:`Zpětné odmítnutí“: e-mail byl odmítnut.

...... záložka: Akce serveru

.. obrázek:: workflow_activities/sa-trigger-types.png
:align: střed
:alt: Typ spouštěče pro dětské aktivity serverové akce.

Zapíná dětskou aktivitu na následujících podmínkách aktivity rodiče:

      - :guilabel:`Přidat další aktivitu“: provedeno po rodičovské aktivitě.

.. tabulka:: SMS

.. obrázek:: workflow_activities/sms-trigger-types.png
:align: střed
:alt: Druhy spouštěčů pro dětské aktivity SMS aktivity.

Každý spouští dětskou aktivitu na následujících podmínkách rodičovské aktivity:

      - :guilabel:`Přidat další aktivitu“: provedeno po rodičovské aktivitě.
      - :guilabel:`Kliknutí na odkaz v SMS“: účastník klikl na odkaz v SMS.
      - :guilabel:`Nepočítáno“: odkaz v SMS nebyl účastníkem kliknut.
      - :guilabel:`Odpověď nebyla doručena“: SMS se nepodařilo doručit.

Jakmile je zvolen typ spouštěče, otevře se okno „Vytvořit aktivity“ k konfiguraci
dětská aktivita. Proces je stejný jako při vytváření nové aktivity
„Marketingová automatizace / Akce“, s výjimkou pole „Spouštěč“
a pole Activity je nastaveno na rodičovskou hodnotu
Vybrána aktivita.

.. viz též:
   - :doc:`testovani_běhání“
   - :doc:`pochopení metrik“
   - :doc:`cílová skupina`
