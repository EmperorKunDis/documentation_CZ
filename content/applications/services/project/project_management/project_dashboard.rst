=================
Dashboard projektu
=================

Projektní panel vám umožňuje získat komplexní přehled o stavu projektu.
zobrazuje informace jako celkový počet úkolů, časových lístků a plánovaných hodin spojených s
projektu a podrobné informace o jeho fázích a nákladech a výnosech.
Projektu lze vytvořit panel nástrojů, kde můžete vytvářet aktualizace projektu, které umožňují
snímek stavu projektu v určitém čase. Proto je nezbytným nástrojem
účinné řízení projektu a zajištění, aby váš projekt zůstal na správné cestě.

Používání projektu Dashboard
===========================

Chcete-li zobrazit projektovou plošinu, otevřete aplikaci **Projekt** a přejděte na příslušný projekt.
Klikněte na ikonu „Slider“ („Slidery“) pro přidání „Přístrojové desky“.
:ref:`horní lišta projektu <projekt/projektové řízení/horní lišta projektu>“.

..tip:
Můžete také přistupovat k projektu pomocí panelu s kartami.
klikněte na ikonu „vertikální elipsa“ (:guilabel:„vertikální elipsa“) a vyberte „Přístrojová deska“.

Levá část panelu zobrazuje seznam existujících aktualizací projektů:
a pravá strana poskytuje podrobné informace o záznamu spojeném s projektem.
<projekt/dashboard projektu/inteligentní tlačítka> a také:ref:`milníky <projekt/dashboard projektu/milníky>“.
:ref:`ziskovost <projekt/dashboard projektu/ziskovost>“ a „rozpočet
<projekt/přístupová stránka projektu/rozpočet>.

.. poznámka::
Informace zobrazená na panelu projektu se liší podle instalovaných aplikací
na vašem serveru. Například neuvidíte informace o **Časových záznamcích**, **Plánování**,
nebo **Nákupní objednávky**, pokud odpovídající aplikace nejsou nainstalované.

.._projekt/dashboard projektu/chytré tlačítko:

Totální chytré tlačítko
--------------------

Následující chytré tlačítka jsou zobrazena v pravém horním rohu projektu:

 - :guilabel:`Úkoly“: počet dokončených úkolů (tj. „Dokončeno“ nebo „Zrušeno“)
:ref:`úkoly (<project/tasks/task_stages_statuses/statuses>) a všechny úkoly ve formátu
dokončené / celkem a odhadovaný podíl projektu na dokončení.
 - :guilabel:`Časové listy“: počet hodin nebo dnů (podle aplikace „Časové listy“)
konfigurace) v nastavení projektu. To zahrnuje všechny
:doc:`Časové listy </aplikace/služby/časové-listy>“, ať už byly nebo nebyly ověřeny.
 - :guilabel:`Plánované“: počet hodin, které byly plánovány pro směny v **Plánování**
Aplikace, která zahrnuje všechny plánované směny, včetně těch již proběhlých:
přesuny a přesuny, které ještě nebyly zveřejněny.
 - :guilabel:`Dokumenty“: počet :doc:`dokumentů </aplikace/produktivita/dokumenty>` v
pracovní prostor projektu.
 - :guilabel:`Burndown Chart“: klikněte na chytrý tlačítko pro přístup k reportu „Reportování“
na stav úkolů projektu v čase.
 - :guilabel:`Časové záznamy a plánování“: klikněte na chytrý tlačítko pro přístup k :doc:`zprávě </applications/essentials/reporting>“.
na časových a směnových lístcích projektu. To vám umožňuje snadno porovnat plánované a skutečné
hodin práce na projektu.
 - Další pole, například: „Pokyny k prodeji“, „Části pokynů k prodeji“
:guilabel:`Nákupní objednávky“ a další představují počet spojených záznamů s projektem.

..tip:
Použijte chytré tlačítko projektu k snadnému aktualizaci záznamů o projektech.
:guilabel:`Časové listy“ k ověření časových listů, :guilabel:`Plánované“ pro vytvoření plánu projektu
:guilabel:`Dokumenty“ pro zobrazení a ověření dokumentů atd.

... projektu / projektu - přehled úkolů:

Milníky
----------

Tato část je viditelná pouze v případě, že: doc:`milestony </applications/sales/sales/invoicing/milestone>`
je v nastavení aplikace projektu zapnuto. Klikněte na tlačítko „Přidat milník“ pro vytvoření nového
milník. Klikněte na milník v seznamu úkolů, abyste jej upravili, povolte jeho zaškrtávací políčko, aby byl označen jako
ukončeno nebo klikněte na ikonu „odpadkový koš“ (ikona „koš“) pro odstranění.

Milníky jsou zobrazeny červeně, pokud je jejich termín již překročen, nebo zeleně, pokud jsou připravené.
být označena jako splněná (tj. úkoly spojené s milníkem, které byly označeny :guilabel:`done`)
nebo:cancelled: status (viz projekt/úkoly/fáze úkolů/stavy).

..._projekt/dashboard projektu/ziskovost:

Profitabilita
-------------

:doc:`Profitabilita projektu </applications/services/project/project_management/project_profitability>`
Uvádí rozpis nákladů a výnosů projektu, které jsou ovlivněny všemi záznamy spojenými s
projektu a jeho analytického účetnictví:

.. poznámka::
Profitabilita se zobrazuje pouze u projektů, které jsou účtovány.

..._projekt/projektový panel/rozpočet:

Rozpočty
-------

Pokud je pro projekt stanoven rozpočet, zobrazí se jeho stav a příslušné podrobnosti v této
Klikněte na tlačítko „Přidat rozpočet“ pro vytvoření nového rozpočtu projektu.

.. poznámka::
:doc:`Musí být zapnuté rozpočty v aplikaci Finance / Účetnictví / Reporting / Rozpočty“
v aplikaci účetnictví databáze, aby se tento oddíl zobrazil.

..._projekt/dashboard projektu/aktualizace:

Aktuality projektu
===============

Aktualizace projektu vám umožňuje pořídit snímek celkového stavu projektu na určitém místě.
Čas například během periodických (týdenních, dvoutýdenních nebo měsíčních) kontrol. To vám umožní
porovnejte konkrétní body dat, zaznamenávejte všechny aspekty projektu, které je třeba vylepšit a odhadujte
jestli projekt běží podle plánu nebo ne.

Chcete-li vytvořit nové aktualizace projektu, přejděte na stránku s přehledem projektů, klikněte na tlačítko „Nový“ a vyplňte
následujících polích:

  - :guilabel:`Stav“: Vyberte mezi „Na cestě“, „V ohrožení“ nebo „Mimo“.
„Stav“, „Ve frontě“ a „Dokončeno“. Jakmile je stav nastaven, objeví se barevný bodík.
zobrazené na kartě projektu Kanban, což umožňuje snadno identifikovat, které
Projekty potřebují pozornost.
  - :guilabel:`Progres“: Zadejte ručně procento dokončenosti podle pokroku projektu.
  - Datum a Autor: Tyto položky se automaticky vyplní.
přiměřené informace podle uživatele, který aktualizaci vytvořil a dnešního data.
  - :guilabel:`Popis“: Tento pole s obsahem textu můžete použít k poznámkám. V závislosti na projektu
konfigurace (např. pokud projekt bude účtovatelný), může být pole předvyplněno aktuální
informace o aspektech jako jsou ziskovost, rozpočet, cíle atd.
