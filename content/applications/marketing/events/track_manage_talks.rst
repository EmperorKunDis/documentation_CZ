============================
Rozhovory, návrhy a program
============================

S Odoo Events mohou uživatelé využívat plně integrovaný webový portál akce, kde se účastníci rychle zaregistrují.
přehrávat různé tracky (prezentace, přednášky atd.), prohlížet celý program a navrhovat přednášky na
událost.

Web akce
=============

Pro přístup na webovou stránku akce se přihlaste do aplikace Odoo Events a klikněte
tlačítko „Přejít na web“. Nebo se přihlaste do webu postaveného společností Odoo
Klikněte na možnost „Události“ v záhlaví a vyberte požadovanou událost pro zobrazení této události.
webové stránky.

Na webu akce je podhlavní menu s různými možnostmi výběru.
od.

Při zapnutém nastavení *Doprava a trasy* v aplikaci Odoo Events budou následující odkazy
automaticky přidána do podnadpisového menu umístěného na webu akce: guilabel:„Přednášky“.
:guilabel:`Návrhy na přednášky“ a „Program“.

.. obrázek: track_manage_talks/track-submenu-options.png
:align:center
:alt:Možnosti podmenu události související s tratí na webu pro události postaveném na Odoo Events.

Chcete-li aktivovat nastavení „Rozvrh a tratě“, přejděte do aplikace „Akce“ ->
Konfigurace --> Nastavení“, zaškrtněte políčko vedle „Sledování a stopy“ a klikněte
:guilabel:`Uložit“.

Stránka o rozhovorech
----------

Odkaz na „Diskuse“ vede účastníka na stránku s plánem všech přednášek.
událost.

.. obrázek: track_manage_talks/talks-page.png
:align:center
:alt:Stránka s informacemi o události na webu, který byl vytvořen pomocí aplikace Odoo Events.

Na stránce „Diskuse“ je vedle pole pro vyhledávání dalších filtrů.
hledání...“

První rozbalovací filtrační pole (s názvem začínajícím na :guilabel:`Favorites`) je jediné
padající nabídka filtrů, která se objeví automaticky. Když na ni kliknete, zobrazí se dvě
Možnosti: „Oblíbené“ a „Všechny přednášky“.

Vybráním položky „Oblíbené“ se zobrazí pouze skladby, které jsou oblíbené pro daného účastníka.

.. poznámka::
Pokud nejsou žádné oblíbené skladby, a pokud je vybrán filtr „Oblíbené“, Odoo zobrazí
všechny události.

Vybráním položky „Všechny přednášky“ se zobrazí všechny skladby bez ohledu na to, zda byly oblíbené nebo
ne.

Další kategorie filtrů, které se objevují na této stránce, jsou spojeny s konfigurovanými tagy (a
kategorie (tagy) vytvořené pro události v administraci.

..tip:
Chcete-li přidat štítky a kategorie štítků do formulářů pro sledování událostí, otevřete požadovaný formulář pro sledování událostí a začněte psát.
nový štítek do pole „Štítky“ a poté klikněte na „Vytvořit a upravit…“.
výsledný seznam.

Provedením takového kroku se zobrazí dialogové okno „Vytvoření štítků“.

.. obrázek: track_manage_talks/create-tags-popup.png
:synchronizace: střed
:alt:Formulář vytváření štítků, který se objevuje současně s rozbalovacím menu filtru na stránce Talks.

odtud uživatelé vidí nedávno přidaný štítek v poli „Název štítku“. Pod ním
je možnost přidat konkrétní :guilabel:`Index barvy` k štítku pro lepší organizaci.

Posledním je pole :guilabel:`Kategorie`, kde uživatelé mohou buď vybrat existující kategorii,
pro tento nový štítek vytvořit kategorii nebo vytvořit novou.

Všechny možnosti v poli „Kategorie“ tagů se zobrazí jako samostatné nabídky filtru
na stránce Talks, která je součástí webu akce.

Pod rozbalovacími filtračními menu v horní části stránky „Přednášky“ je seznam
plánované tratě pro konkrétní akci, uspořádanou podle dnů.

Pokud se účastník chce dozvědět o novém příspěvku, může kliknout na ikonu „fa-bell-o“ a zobrazit si ji.
ikonou zvonku (umístěnou vpravo vedle názvu skladby). Účastníci budou vědět, že jim skladba chutná
když si všimnou, že ikona byla změněna na :icon:`fa-bell` :guilabel:`(plná zvonice)`

Pokud takto označíte skladbu, umístí se na seznamu oblíbených skladeb, který je dostupný z
výchozí nabídka filtrů, která se nachází na horním konci stránky „Přednášky“.

Stránka s návrhy na přednášky
-------------------

Odkaz „Návrh přednášky“ vede návštěvníky na stránku webu akce, kde si mohou prohlédnout
dříve předložit návrh na přednášku ([:dfn:`track`]) pro danou událost prostřednictvím vlastního online formuláře.

.. obrázek: track_manage_talks/talk-proposals-page.png
:align:center
:alt:Stránka s návrhy přednášek na webu události, postavená pomocí aplikace Odoo Events.

Kromě formuláře je nutné uvést i úvodní stránku a další relevantní informace.
Pokud je potřeba, lze přidat informace o tom, jaké typy přednášek bude akce obsahovat.

Formulář návrhu přednášky lze upravit různými způsoby prostřednictvím nástrojů pro tvorbu webových stránek.
přístupný po kliknutí na tlačítko „Upravit“ v příslušné stránce.

Pak pokračujte v editaci jakýchkoliv výchozích polí nebo přidejte nové formuláře pomocí příkazu :guilabel:`Form Builder
blok (umístěný v sekci „Bloky“ na liště nástrojů pro tvorbu webu).

Jakmile jsou do formuláře zadány všechny potřebné informace, účastníci jen musí kliknout na
tlačítko „Odeslat návrh“.

Pak se může na webu zobrazit tento rozhovor a všechny údaje vyplněné v přihlašovacím formuláři.
Stránku „Události“ pro konkrétní událost v rámci fáze „Návrh“, která je
je přístupný pomocí tlačítka „Sledy“ na formuláři události.

V tomto bodě může interní uživatel zkontrolovat navrhovanou přednášku a vybrat si mezi přijetím nebo zamítnutím.
návrh.

Pokud je přijato, může interní uživatel pak sledovat pohyb na další vhodnou fázi kanbanu.
připojení na stránce „Sled událostí“ pro danou událost. Pak mohou otevřít formulář sledování události
Klikněte na tlačítko „Přejít na web“ a zobrazí se stránka sledovaného tracku.
webové stránky.

Odtud mohou přepnout přepínač „Nedostupné“ v hlavičce.
:guilabel:`Publikováno“, což umožňuje všem účastníkům události zobrazit a přistupovat k přednášce.

Stránka programu
-----------

Odkaz na Agendu vede účastníky na stránku webových stránek události, kde je prezentována samotná akce.
kalendář, který ukazuje, kdy a kde se koná dané setkání.

.. obrázek: track_manage_talks/event-agenda-page.png
:align:center
:alt:Stránka události na webu akce, postaveném pomocí aplikace Odoo Events.

Kliknutím na jakoukoli stopu v kalendáři se účastník dostane na stránku s podrobnostmi o konkrétní stopě.
webové stránky akce.

Pokud se účastník chce dozvědět o novém příspěvku, může kliknout na ikonu „fa-bell-o“ a zobrazit si ji.
ikonou zvonku (umístěnou vpravo vedle názvu skladby). Účastníci budou vědět, že jim skladba chutná
když si všimnou, že ikona byla změněna na :icon:`fa-bell` :guilabel:`(plná zvonice)`
