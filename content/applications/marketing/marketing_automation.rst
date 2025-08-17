Zobrazit obsah

====================
Marketingová automatizace
====================

Použijte aplikaci **Odoo Marketing Automation** k vytvoření dynamických kampaní s akcemi, které
automaticky nastanou v definovaném časovém úseku, například posíláním sérií masových e-mailů nebo
interakce s leady na základě jejich interakcí s marketingovými kampaněmi.

Aplikace je navržena tak, aby byla uživatelsky přívětivá pro vytváření, spouštění a zobrazování
marketingových kampaní také nabízí pokročilé funkce pro automatizaci opakujících se úkolů.
databáze.

Začněte vytvořením nové kampaně od nuly nebo začít
s šablonou kampaně:ref:`<marketing_automation/campaign-templates>`.

.. viz též:
   - „Tutoriály Odoo: Marketing <https://www.odoo.com/slides/marketing-27>“
   - „Magická tabulka – automatizace marketingu [PDF]
<https://drive.google.com/drive/folders/1MMMGcYIG1tm160jC2JaXVc_D5b6x3cJd>

.. karty:

.......karta: Zacílení na cílovou skupinu
:cílová skupina: marketingová automatizace

Nastavte cílovou skupinu pro kampaň.

....... karta: Průběh pracovních činností
:cílová skupina: marketingová automatizace/aktivity v pracovním postupu

Definujte aktivity, které se v rámci kampaně odehrávají.

.......karta::Testování a spouštění kampaní
:target:marketing_automation/testovani_v-praci

Spusťte test nebo kampaň.

... karta: Metriky kampaně
:target:marketingová automatizace/pochopení metrik

Zkontrolujte metriky kampaně.

Konfigurace
=============

Nejprve se ujistěte, že aplikace **Marketing Automation** je nainstalována podle pokynů v části „Instalace“ (viz odkaz).

.. důležité:
Při instalaci aplikace **Marketing Automation** se také instaluje :doc:`E-mailový marketing
aplikaci pro e-mailový marketing, protože většina funkcí Odoo Marketing Automation je závislá na této
konkrétní aplikace.

Dále nainstalujte modul CRM a modul SMS marketing.
aplikace, která umožňuje přístup k *všem* funkčnostem dostupným v **Marketing Automation**.

Následující dokumentace předpokládá, že všechny tři tyto aplikace jsou nainstalovány.
na databázi.

... marketingová automatizace / kampaně:

Kampaně
=========

Kampaň je sada aktivit, které jsou automaticky spouštěny na cílový objekt.
publikum na základě předem definovaných filtrů, spouštěčů a trvání aktivit.

Nová kampaň může být vytvořena od nuly nebo z :ref:`vzoru
<marketing_automation/kampaně>.

Pro vytvoření kampaně přejděte do aplikace „Marketing Automation“ a klikněte
tlačítko „Nový“ pro zobrazení nové kampaně.

... _marketingová automatizace/šablony kampaní:

Šablony kampaně
------------------

Odoo poskytuje šest šablon kampaní, které pomohou uživatelům začít. Karty šablony kampaně **jenom**
V případě, že v databázi neexistují žádné kampaně, zobrazí se
šablony karet na přehledové stránce Campaigns jsou nahrazeny zobrazením Kanban stávajících
kampaně.

Chcete-li začít s šablonou, přejděte do aplikace Marketing Automation.
od hlavního panelu Odoo, otevřete kampaňovou obrazovku, která zobrazuje šest
:doc:`šablona kampaně <marketing_automation/campaign_templates>` karty:

- |:icon:`fa-tag` :guilabel:`Tag Hot Contacts“
| :guilabel:`Odešlete e-mailovou zprávu kontaktům a označte je, pokud na ni kliknou.“
- | :icon:`fa-hand-peace-o` :guilabel:`Vítejte“
| :guilabel:`Odeslat e-mailovou zprávu novým odběratelům, odebrat adresu, která se vrátila zpět.“
- |:icon:`fa-check-square` :doc:`Dvojitý opt-in

| :guilabel:`Odeslat e-mail novým příjemcům k potvrzení souhlasu.“
- | :icon:`fa-search` :guilabel:`Obchodní zástupce“
|:guilabel:`Poslat zdarma katalog a následně podle reakcí.“
- | :icon:`fa-phone` :guilabel:`Vytvořit hovor“
|:guilabel:`Pokud je vytvořen kontakt pro stávajícího zákazníka, naplánujte si schůzku s jeho obchodníkem.“
- |:icon:`fa-star` :guilabel:`Zajistěte prioritu pro horké vstupy“
|:guilabel:`Odeslat e-mail novým kontaktům a při otevření e-mailu jim přidělit vysokou prioritu.“

.. obrázek: marketing_automation/kampaně-dashboard.png
:alt:Šest šablon kampaně na přehledové stránce Kampaně aplikace Marketing Automation.

Tyto šablony slouží jako vzor pro vytváření nových kampaní. Klikněte na
šablonové karty pro otevření kampaně.

..tip:
Chcete-li zobrazit šablonu karet kampaně znovu po vytvoření kampaně, zadejte její název.
do vyhledávacího pole zadáte kampaň, která v databázi neexistuje, stisknete :kbd:`Enter`.

Například hledání slova „prázdný“ zobrazí karty šablon kampaně znovu, dokud nebude prázdná.
Není kampaň s názvem „prázdný“ v databázi.

Záměry a filtry
===================

Na kampaně je v sekci cíl a filtru, také známé jako
doména obsahuje pole používaná k definování cílové skupiny pro dosah kampaně (tj.
jedinečné záznamy v databázi (např. kontakty).

Cílová skupina určuje typ dostupných záznamů pro použití v kampani, například
*Přední/příležitost*, *Registrace na události*, *Kontakt* a další.

Rekordy
-------

Kontakty v systému, které splňují zadaná kritéria pro kampaň, se označují jako
*rekordy*.

Počet zobrazených záznamů vedle kampaně :guilabel:`Filtr` představuje celkový počet
Počet rekordů, které kampaň chce překonat.

Účastníci
------------

Záznamy, které jsou zapojeny do kampaně, se označují jako „účastníci“.

Počet účastníků testovacího běhu je uveden v chytré tlačítko Tests.
zobrazuje na vrcholu kampaně po provedení testu.

Počet účastníků běžící nebo zastavené kampaně je uveden v
Tlačítko „Účastník“ v horní části kampaně.

.. viz též:
:doc:`Zacílení na publika <marketing_automation/target_audience>`

Práce s dokumenty
========

Práce v procesu je činností, mnoha činnostmi nebo sekvencí činností uspořádaných do
kampaně. Průběh kampaně je definován v části „Průběh“ ve formuláři kampaně.

Aktivita
----------

Aktivita je metoda komunikace nebo akce na serveru organizovaná v proudu.
realizované v rámci kampaně. Po spuštění každá aktivita zobrazuje počet účastníků,
Je zapojen do činnosti jako „úspěšný“ a „odmítnutý“.

Pro vytvoření jedné z následujících aktivit klikněte na „Přidat novou aktivitu“ v
Sekce „Průběh kampaně“ v přihlašovacím formuláři:

- :ref:`E-mail <marketing_automation/email-activity-type>“: e-mail, který je zasílán na cílovou adresu
diváci.
- „Akce serveru“: interní akce na serveru
databáze, která se spouští.
- :ref:`SMS <marketing_automation/sms-activity-type>“: textová zpráva, která je odeslána na cílovou adresu
diváci.

.. viz též:
:doc:`marketing_automation/workflow_activities`

Testování a běh
===================

Jakmile je kampaň vytvořena, může být otestována, aby se ověřilo, že funguje správně.
očekávané, které má prověřit na chyby a opravit případné chyby ještě před tím, než se dostane k cílové skupině.

Po testování může být kampaň spuštěna a začít oslovovat cílovou skupinu. Kampaň
Pokud je uživatel přesvědčen o správnosti svého postupu, může být spuštěn i bez testování.

.. viz též:
:doc:`marketing_automation/testovani_spusteni`

Reportér
=========

K měření úspěšnosti kampaně jsou k dispozici různé ukazatele. Přejděte na
Vyberte možnost „Marketingová automatizace -> Zprávy“ v následujícím seznamu.

- :guilabel:`Sledovač odkazů“: zobrazuje metriky odkazů, které sledují počet kliknutí.
- :guilabel:`Sledování stop“: zobrazuje výsledky všech aktivit ze všech kampaní.
- :guilabel:`Účastníci“: zobrazuje přehled účastníků všech kampaní.

Každá aktivita v kampani má své vlastní měřítko zapojení.

.. viz též:
:doc:`marketing_automation/understanding_metrics`

.. toctree::


marketingová automatizace/cílová skupina
marketingová automatizace/aktivity workflow
marketingová automatizace/testování běžného provozu
marketingová automatizace/pochopení metrik
marketingová automatizace / šablony kampaní
