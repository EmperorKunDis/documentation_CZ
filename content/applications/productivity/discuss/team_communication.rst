===================================
Používejte kanály pro týmovou komunikaci
===================================

V aplikaci Odoo *Discuss* použijte kanály k organizování diskuzí mezi jednotlivými týmy.
odborů, projektů nebo jakékoliv jiné skupiny, která vyžaduje pravidelnou komunikaci. S kanály
zaměstnanci mohou komunikovat v rámci určených prostorů v databázi Odoo kolem konkrétních témat.
aktualizace a nejnovější vývoj související s organizací.

Veřejné a soukromé kanály
===========================

Kanál s označením „Veřejný“ je viditelný pro všechny uživatele, zatímco kanál s označením „Soukromý“ je viditelný pouze pro uživatele, kteří byli do něj pozváni.
k tomu. Chcete-li vytvořit novou kanál, přejděte do aplikace „Diskuse“ a pak klikněte na
:guilabel:`+ (plus)` ikona vedle položky „Kanály“ v levém menu. Po
Při zadání názvu kanálu se objeví dvě volitelná pole: První je kanál s
hashtag („#“) pro označení, že je to veřejný kanál; druhou možností je uzavřený kanál
ikona („🔒“) vedle něj, aby bylo jasné, že se jedná o soukromou konverzaci. Vyberte typ kanálu, který nejlépe vyhovuje vašim potřebám.
splňuje komunikační potřeby.

.. obrázek: team_communication/public-private-channel.png
:align:center
:alt: Pohled na panel diskuze a vytváření kanálu v Odoo Discuss.

..tip:
Nejlepší je použít veřejný kanál, pokud mnoho zaměstnanců potřebuje přistupovat k informacím (například
informace omezena na určitou skupinu lidí.
konkrétním skupinám (např. určitému oddělení).

Možnosti konfigurace
---------------------

Nastavení skupiny, popisu a soukromí kanálu lze změnit v jeho nastavení.
může být upraveno kliknutím na nastavení kanálu, které je reprezentováno ikonou „⚙️“
levý sloupec vpravo pod názvem kanálu.

.. obrázek: team_communication/channel-settings.png
:align:center
:alt: Pohled na nastavení kanálu v Odoo Discuss.

Karty Soukromí a Členové
~~~~~~~~~~~~~~~~~~~~~~~~

Změna: `Kdo může sledovat aktivity skupiny?` řídí, které skupiny mají přístup
kanálu.

.. poznámka::
Povolení uživatelům s oprávněním :guilabel:`Každý“ přístup k soukromé kanálu umožňuje jiným uživatelům jej zobrazit a připojit se.
Veřejný by byl lepší.

Při výběru „Vybraní lidé“ zadejte v záložce „Členové“ jména členů
je nutné je pozvat. Pozvání členů lze provést také z hlavní obrazovky aplikace Discuss
vybrat kanál, kliknout na ikonu „přidat uživatele“ v pravém horním rohu panelu a
Konečně kliknout na „Zvýraznit kanál“ poté, co všichni uživatelé budou přidáni.

.. obrázek: team_communication/invite-channel.png
:align:center
:alt: Zobrazení možnosti pozvat členy do Odoo Discuss.

Při výběru možnosti „Vybraná skupina uživatelů“ se zobrazí schopnost přidat
s možností „Automaticky se přihlašovat do skupin“ a
:guilabel:`Automatické přihlášení k odběru oddělení“.

Možnost „Automatické přiřazení skupin“ automaticky přidává uživatele, kteří patří do této konkrétní skupiny.
skupinou jako následovníky. Jinými slovy, zatímco :guilabel:`Oprávněné skupiny“ omezuje uživatele, kteří mohou
Připojit se k kanálu: guilabel: Auto Subscribe Groups automaticky přidává uživatele jako členy tak dlouho
Jsou součástí konkrétní uživatelské skupiny. To platí také pro :guilabel:`Auto Subscribe Departments`.

Rychlé vyhledávání
================

Jednou alespoň 20 kanálů, soukromých zpráv nebo živých chatu (pokud je nainstalován modul
instalované na databázi) jsou v liště zobrazeny ikony „Rychlé vyhledávání…“.
Tato funkce je pohodlným způsobem filtrování konverzací a rychlým vyhledáváním relevantních komunikací.

.. obrázek: team_communication/quick-search.png
:align:center
:alt:Pohled na boční panel aplikace Odoo Discuss, který zdůrazňuje rychlý vyhledávač.

Najít kanály
----------------

Klikněte na ikonu „Nastavení“ („⚙️“), která se nachází v levém sloupci vedle
:guilabel:`CHANELOVÉ` rozbalovací položka nabídky. Když tak učiníte, dostanete se k mozaice obsahující všechny
Na této obrazovce jsou k dispozici veřejné kanály. Uživatelé mohou přidávat nebo opouštět kanály tím, že na ně klikají
„Připojit“ nebo „Odejít“ tlačítka, která se zobrazují v oknech kanálů.

Dále je možné nastavit filtrační kritéria a uložit si je pro pozdější použití.
Funkce „Hledat…“ přijímá divoké karty pomocí znaku podtržítka [ _ ].
Uložit aktuální vyhledávání lze pomocí volby „Moje oblíbené“ v nabídce.
kliknutím na tlačítko „Přidat do košíku“.

.. obrázek: team_communication/filter.png
:align:center
:alt: Pohled na filtrovaný kanál v aplikaci Odoo Discuss

Spojit kanál v chatovací místnosti
==========================

Kanály lze propojit v poznámce o logu záznamu v Odoo. Postačí napsat znak „#“
název kanálu. Klikněte nebo stiskněte klávesu Enter na názvu kanálu. Po přihlášení se zobrazí odkaz na
objeví se kanál. Po kliknutí na odkaz se otevře okno chatu s konverzací v kanálu
v levém dolním rohu obrazovky.

Uživatelé mohou přispívat do této skupinové kanálu (veřejné nebo členy založené) tím, že napíší
zprávy v okně a stisknutím klávesy Enter.

.. obrázek: team_communication/chatter-channel.png
:align:center
:alt:Kanál spojený v chatovací místnosti s kanálem otevřeným na dolním pravém rohu.

.. viz též:
   - :doc:`../discuss`
   - :doc:`/aplikace/základní/činnosti`
