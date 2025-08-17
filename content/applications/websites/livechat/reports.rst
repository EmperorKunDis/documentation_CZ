=======
Zprávy
=======

Odoo **Live Chat** zahrnuje několik reportů, které umožňují monitorování výkonnosti operátorů.
a identifikace trendů v konverzacích zákazníků.

Následující zprávy jsou součástí aplikace **Live Chat**:

- :ref:`Historie sezení <livechat/sessions-history>`
- :ref:`Statistiky sezení <livechat/session-statistics>`
- :ref:`Analýza operátora <livechat/operator-analysis>`

.. poznámka::
Hodnocení živého chatu je také k dispozici v hlavním menu pod položkou „Zpráva“.
Informace o tomto hodnocení a procesu hodnocení v reálném čase najdete na stránce :doc:`Live Chat Ratings
<../livechat/hodnoceni>.

Chcete-li zobrazit seznam všech dostupných zpráv, přejděte na:
--> Zpráva.

.. _livechat/session_history:

Historie relací
================

Zpráva o historii relací zobrazuje přehled živých chatu včetně dat a časů jednotlivých relací.
jméno účastníka a země, délku sezení, počet zpráv a hodnocení. Dále
poskytuje přístup k úplným záznamům chatu v reálném čase.

Pro zobrazení této zprávy přejděte na: „Živý chat -> Zpráva -> Historie relací“.
Každá živá chatu je reprezentována kartou kanbanu.

.. obrázek::reporty/historie_sessionu.png
:alt: Příklad historie chatů z aplikace Live Chat.

Pro zobrazení přepisu konkrétní seance klikněte na kartu Kanban. Tím se otevře okno *Diskuse*.
pro konverzaci.

V příspěvku *Diskuse* se zobrazuje celý přepis konverzace.
Pokud návštěvník ohodnotil obsah, je uveden na konci záznamu.

.. obrázek:reporty/chat-transcript.png
:alt: Pohled na přepis chatu v aplikaci Diskuse.

Export historie relací
-----------------------

Informace v tomto hlášení lze exportovat nebo vložit do tabulky.

Ve zprávě „Historie schůzek“ klikněte na ikonu oi-view-list (Seznam)
seznamovému zobrazení. Následně klikněte na ikonu „nástrojů“ vedle
Název stránky „Historie“ odhalí rozbalovací nabídku.

Vyberte možnost „Exportovat všechny“ z rozbalovací nabídky.
:guilabel:`Vložit seznam do tabulky“ k vložení informací do nové nebo existující tabulky.

Chcete-li exportovat pouze vybrané sezení, nejprve zvolte požadovaná data v seznamu.
zaškrtnutím políčka vedle každé jednotlivé seance. Se vybranými relacemi pak klikněte na
:ikonu „nástroje“ v horní části stránky a klikněte na „Export“.
:guilabel:`Vložit seznam do tabulky“.

.. _livechat/session-statistics:

Statistiky o relacích
==================

Zpráva „Statistiky sezení“ poskytuje statistický přehled o živých chatech.
Vidíte v tomto přehledu seskupené relace podle data jejich vytvoření.

Pro přístup k tomuto hlášení přejděte na: „Živý chat aplikace -> Hlášení -> Sessions“.
Statistiky.

.. obrázek:reporty/session-statistiky.png
:alt: Příklad statistiky relací z aplikace Live Chat.

Viditelnost grafu sloupcového sestavení zprávy o statistikách relací, kde jsou výsledky seskupeny podle vytvoření
Datum (hodina) a pak podle hodnocení.

Pro zobrazení jiného měřítka klikněte na položku „Měřítko“ v horním levém rohu.
reportu jsou k dispozici následující opatření:

- :guilabel:`Počet mluvčích“: počet účastníků konverzace.
- :guilabel:`Dny aktivit“: počet dnů od prvního sezení operátora.
- :guilabel:`Délka hovoru (minuty)`: Doba trvání konverzace v minutách.
- :guilabel:`Je návštěvník anonymní“: označuje, zda je účastník konverzace anonymní.
- :guilabel:`Počet zpráv za sezení“: celkový počet zaslaných zpráv v konverzaci.
Tato měřítko je zahrnuta do výchozího pohledu.
- :guilabel:`Hodnocení“: hodnocení operátora na konci sezení, pokud se jednalo o sezení
Vybavení je k dispozici.
- :guilabel:`Nesouhlasilo se hodnocením“: označuje, zda se na konci sezení **neudělalo hodnocení**.
rozhovor.
- :guilabel:`Čas na odpověď (v sekundách)`: průměrný čas v sekundách předtím, než operátor reaguje na
žádost o chatování.
- :guilabel:'Návštěvník je spokojený': označuje, zda návštěvník poskytl pozitivní hodnocení. Pokud návštěvník
Pokud je hodnocení negativní nebo neutrální, považují se za „nešťastné“.
- :label:Počet relací: celkový počet relací.

.. _livechat/operator-analysis:

Analýza operátora
=================

Zpráva *Analýza operátora* se používá k monitorování výkonnosti jednotlivých živých chatu.

Pro přístup k zprávě se přesuňte na: „Živý chat -> Zprávy -> Analýza operátora“.

Výchozí pohled pro tento report je sloupec, který zobrazuje pouze konverzace ze současného
měsíc, jak je uvedeno v výchozím filtru vyhledávání `Tento měsíc`. Konverzace jsou seskupeny
Provozovatelem.

Pro zobrazení jiného měřítka klikněte na položku „Měřítko“ v horním levém rohu.
reportu jsou k dispozici následující opatření:

- :guilabel:'Počet sezení': počet sezení, které operátor absolvoval. Tento ukazatel
je součástí výchozího nastavení.
- :guilabel:`Průměrná doba trvání“: průměrná délka hovoru v sekundách.
- :guilabel:`Průměrné hodnocení“: průměrná známka, kterou obdržel operátor.
- :guilabel:`Čas na odpověď“: průměrný čas, který uplyne mezi zahájením chatu a reakcí operátora
požadavku v sekundách.
- :label:Počet relací: celkový počet relací.

.. obrázek: reports/operator-analysis.png
:alt: Příklad výstupu z analýzy operátora v aplikaci Live Chat.
