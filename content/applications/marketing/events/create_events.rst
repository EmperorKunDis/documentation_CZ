=============
Vytvářejte události
=============

S aplikací *Eventy* mohou pořadatelé akcí vytvářet a konfigurovat události pouze osobně nebo pouze on-line.
události v Odoo. Každá nová událost obsahuje několik nastavitelných možností, které jsou zaměřeny na
specifická logistika události, která je potřebná pro každou událost, jako jsou například prodej vstupenek a registrační stůl, stánky.
stopy, sponzoři, místnosti a další.

Akce můžete vytvořit ručně od nuly nebo na základě předpřipravených šablon. Jakmile je akce spuštěna,
Aplikace „Události“ pak integruje s aplikací „Webová stránka“ pro propagaci na přední straně.
registrace akce pro účastníky, aplikace *Sales* pro možnost zakoupení vstupenek za peníze.
a také CRM aplikaci prostřednictvím přizpůsobitelných pravidel generování leadů.

.._akce/nová-akce:

Nový zážitek
=========

Pro vytvoření nového události začněte procházením aplikace „Události“ na domovské obrazovce.
Dashboard „Akce“ v pohledu „Kanban“ (viz ikonka „OI-View-Kanban“).
nebo z :ikony:`oi-view-list` :guilabel:`Seznam“ nebo :ikonou:`fa-tasks` :guilabel:`Ganttovská“
názory, klikněte na tlačítko „Nový“ v horním levém rohu panelu pro otevření nového
forma události.

.. obrázek: create_events/blank-event-template.png
:align:center
:alt:Běžný vzor události v aplikaci Odoo Events.

.. poznámka::
Pokud některé pole nejsou na formuláři události zobrazeny, pak je třeba podat další žádost.
je třeba nainstalovat nebo databáze nefunguje v prostředí více společností.

Příkladem je pole „Zdi Twitteru“ (viz obrázek níže), které se zobrazí pouze v případě, že je aplikace Social Marketing aktivní.
je nainstalován a pole „Společnost“ se zobrazí pouze v případě, že databáze funguje.
více společností.

Tyto prvky jsou pouze doplňkové a nemusí být nutně využity pro danou událost.
vytvořit, hostovat a spravovat událost s Odoo Events.

Forma akce
==========

Na vrcholu události je sada chytrých tlačítek souvisejících s různými metrikami události.
bude automaticky doplňovat relevantní údaje, jakmile se začnou registrovat účastníci, stánky a sponzoři
Pro událost se událost koná, a tak dále.

Hlavně se tyto chytré tlačítka používají jako logistické brány k provedení konkrétních akcí pro
akce. Čísla na displeji slouží především jako rychlé orientační body.

Přestože jsou vizuální metriky užitečné, stále je lze kliknout a použít k navigaci na
specifické stránky s událostmi, které lze upravit a provést libovolné akce.

Pod chytrými tlačítky je formulář události, který obsahuje různé pole a klikatelné záložky.
slouží k nastavení prvotních nezbytných podrobností o události.

Následující pole se nachází na formuláři pro události:

- :guilabel:`Název události`: název akce. Toto pole je **povinné**.

...... poznámka::
Vpravo od zadaného názvu události je jazykový nápověda, která je reprezentována
zkrácený jazyk (např. EN). Kliknutím se otevře :guilabel:`Přeložit: název
při otevření se zobrazí okno s různými přednastavenými možnostmi překladu.
v databázi.

- :guilabel:`Datum“: kdy se akce má konat (v čase vašeho časového pásma).
Toto pole je automaticky vyplněno, ale lze jej upravit a je **povinné**.
- :guilabel:`Zobrazit časové pásmo“: časové pásmo, ve kterém budou datumy a časy akcí zobrazeny na
webové stránky. Toto pole je automaticky vyplněno, ale upravitelné a je **povinné**.
- :guilabel:`Jazyk“: určit konkrétní jazyk pro všechny komunikace s událostmi, které mají být přeloženy
do pole, pokud je třeba. Toto pole je ve výchozím nastavení prázdné, takže pokud jsou zapotřebí komunikace související s událostmi
Pokud je zpráva odeslána příjemcům, kteří mluví jiným jazykem, ujistěte se, že tento prvek nastavíte správně.
- :guilabel:`Stěna Twitteru“: vytváří samostatnou stránku na webu akce, kde se zobrazují konkrétní příspěvky sociálních sítí.
příspěvky na X (dříve Twitter), které obsahují předem stanovené požadované prvky.

..tip:
Pro vytvoření a přizpůsobení Twitterové zdi zadejte do pole jméno požadované zdi.
pole a z nabídky vyberte možnost „Vytvořit a upravit…“.

Pro zobrazení této možnosti klikněte na tlačítko „Vytvořit stěnu Twitteru“.

.. obrázek: create_events/twitter-wall-popup.png
:align: střed
:alt:Pop-up okno Twitter Wall v aplikaci Odoo Events.

Z této lišty zadejte jméno stěny:guilabel:. Pak vyberte určité slovo nebo hashtag.
Odoo hledá na X podobně jako například „#Dřevozpracující výstava 24“.

Poté určete typ tweetu, který by měl Odoo zobrazit s předem stanoveným hashtagem.
kritérií. Vybrané možnosti jsou: „Nedávno přidané“, „Nejpopulárnější“ nebo
:guilabel:`Smíšené“.

Uživatelé také mají možnost přidat stručný popis na zeď, pokud chtějí.

Nakonec se vám zobrazí šedé pole s názvem „URL webu“, které nemůžete měnit. Toto pole se automaticky vyplní adresou vašeho webu.
plná adresa potřebná k přístupu ke dokumentu prostřednictvím webových stránek události.

Obrázek lze také přidat na zeď kliknutím na ikonu :icon:`fa-pencil` :guilabel:`(pencil)`
ikona, která se objeví při najetí kurzorem nad zástupným obrázkem :guilabel:`(fotoaparát)`
v horním pravém rohu okna.

Pak vyberte z okna prohlížeče souborů požadovanou fotografii, kterou chcete přidat do
zeď.

Toto pole „Zdi Twitteru“ se na formuláři akce objeví pouze tehdy, pokud je zvolené sociální
Marketingová aplikace je nainstalovaná a účet X byl přidán jako kanál v aplikaci.
pro další informace navštivte dokumentaci :doc:`Sociální marketing <../social_marketing>`.

- :guilabel:`Šablona“: vyberte přednastavený šablonový vzor z výsledného seznamu.

nebo vytvořte nový přímo z tohoto pole, zadáním názvu nového šablonu.
výběrem jedné z následujících možností:

  - „Vytvořit“ (který vytvoří šablonu a později ji lze upravit).
  - „Vytvořit a upravit…“ (která vytváří šablonu a odhaluje samostatnou stránku s šablonou).
pro konfiguraci šablony v podrobnějších detaily.

- :guilabel:`Štítky“: přidejte příslušné štítky, abyste událost stručně popsali (např. „On-line“,
„Konference“, atd.). Můžete přidat více štítků na jednu událost.

..tip:
Štítky mohou být zobrazeny na událostech, které jsou uvedeny na webových stránkách, pokud je
Zatrhněte políčko „Webová stránka“ v sekci „Konfigurace“ aplikace „Akce“ z menu „Vybrané události“.

- :guilabel:`Pořadatel“: určete pořadatele akce (firmu, kontakt nebo zaměstnance).
- :guilabel:`Odpovědný“: přiřadit uživatele v databázi k tomuto události.
- :guilabel:`Společnost“: určete, která společnost v databázi se tímto událostem týká.
Toto pole se zobrazí pouze v případě práce v prostředí více společností. Toto pole je automaticky vyplněno.
ale upravitelné a je **povinné**.
- :guilabel:`Webová stránka“: zvolte omezení publikování této události na konkrétní webovou stránku vytvořenou
v Odoo. Pokud je pole nevyplněno, událost může být zveřejněna na všech webových stránkách v
databáze. Pro další informace se podívejte na stránku :doc:`Několik webových stránek
dokumentace <../../websites/website/configuration/multi_website>.
- :guilabel:`Místo konání“: Zadejte podrobnosti o místě konání akce. Tento prvek získává relevantní informace z
Aplikace „Kontakty“. Alternativně lze informace o místě konání ručně doplnit v aplikaci „Kontakty“.
i tam. Nejlépe by mělo být uvedeno alespoň jméno místa konání, adresa, město, PSČ/kraj.
a vstoupil do země.
- :guilabel:Výstava mapy“: pokud si přejete, klikněte na tlačítko „Nahrát soubor“.
obrázek místnosti, kde se koná akce.
- :guilabel:'Omezení registrací': pokud je zaškrtnuto tlačítko „Omezení registrací“,
Přihlášky se přidává do akce a do požadovaného limitu musí být zadán příslušný počet.
prázdné pole před :guilabel:`Účastníci`.
- :guilabel:`Rozměr štítku“: vyberte požadovaný rozměr štítku pro události. Možnosti
Jedná se o: guilabel:„A4 složený“, „A6“ nebo „4 na list“.
- :guilabel:`Zadní pozadí štítku“: pokud chcete, klikněte na tlačítko „Nahrát soubor“
vlastní pozadí pro štítky události.

Když jsou veškeré položky v registračním formuláři vyplněny správně, přejděte na čtyři záložky
dole na stránce pro další úpravy.

Tyto záložky jsou: :ref:`Vstupenky <events/event-tickets>“, :ref:`Komunikace
<události/komunikace události>“, „Dotazy <události/dotazy k událostem>“ a „Poznámky
<události/poznámky k událostem>“.

.._akce/vstupenky:

Kartičky
-----------

Vytvořte vlastní vstupenky (a cenové úrovně) pro události na kartě „Vstupenky“ ve formuláři události.

.. obrázek: create_events/tickets-tab.png
:align:center
:alt: Typická záložka s vstupenkami na formuláři akce v aplikaci Odoo Events.

Pro vytvoření lístku klikněte na „Přidat řádek“ v záložce „Lístky“. Pak zadejte název
do pole „Jméno“ vstupenku (např. „Základní vstupenka“ nebo „VIP“)

V poli „Produkt“ buď vyberte přednastavený produkt „Registrace na akci“.
produkt nebo vytvořte nový produkt zadáním názvu registrace na události.
Vyberte buď „Vytvořit“ nebo „Vytvořit a upravit…“ z výsledného seznamu.
menu.

.. důležité:
Při instalaci aplikace Odoo Events se nový produktový typ Event Ticket objeví v nabídce produktů.
formuláře (v menu vyberte Sales --> Produkty --> Produkty). Chcete-li se přihlásit na událost,
produkt, který je možné vybrat v záložce „Vstupenky“, registrace události:
musí být nastaveno na :guilabel:`Vstupenka na akci“.

..tip:
Existující produkty pro registraci na akce lze upravit přímo z tohoto pole také.
kliknutím na ikonu „OI Arrow Right“ vedle události
registrační produkt. To odhaluje jeho podobu. Pokud aplikace *Inventář*
nainstalované, k dispozici jsou další možnosti pro přizpůsobení produktu.

Dále nastavte cenu registrace v poli „Cena“.

.. poznámka::
Cena prodeje, která je definována v produktovém formuláři registrace na akci, nastavuje výchozí cenu.
cena vstupenky. Změna ceny vstupenky v záložce „Vstupenky“ nastaví
nové registrační poplatky za vstupenku na tuto akci.

Dále určete datum „Zahájení prodeje“ a „Ukončení prodeje“ v příslušných polích.
Chcete-li to provést, klikněte na prázdné místo, které zobrazí kalendářový okýnek. Zde vyberte požadovanou
datum a čas, pak klikněte na ikonu „fa-check“ a poté na tlačítko „Použít“.

Pak můžete zadat maximální počet lístků daného typu, které je možné prodat.

Sloupec Taken se naplní číslem prodaných vstupenek.

Volitelně v sloupci :guilabel:`Barva` přidejte vlastní barvu pro odlišení barev štítků.
Vybrané barvy se zobrazují na lístcích, když jsou vytištěny.

Chcete-li odstranit jakýkoliv lístek z karty „Lístky“, klikněte na ikonu „fa-trash-o“.
:guilabel:`(koš)` ikona na příslušné řádce pro smazání daného lístku.

..tip:
Chcete-li k záložce „Tikety“ přidat volitelnou sloupec „Popis“, klikněte na
:ikonka: „Nastavení“ :guilabel: (Další možnosti) v rozevíracím seznamu umístěném
vlevo dole.

Poté zaškrtněte políčko vedle:guilabel:`Popis`.

Pokud je aktivní možnost přidání stručných popisů pro každou vstupenku, můžete použít
informovat účastníky o jakýchkoli výhodách nebo službách, které mohou souviset s konkrétním nákupem vstupenek.

.._události/komunikace událostí:

Komunikační záložka
-----------------

V záložce „Komunikace“ vytvořte různé marketingové komunikace.
Může být naplánován na určité časové období před a po události.

.. obrázek: create_events/komunikace-tabulka.png
:align:center
:alt: Běžná komunikační záložka na formuláři události v aplikaci Odoo Events.

.. poznámka::
Výchozí nastavení poskytuje tři samostatné přednastavené komunikace na každém nově vytvořeném formuláři události.
Jedna je e-mail zaslaný po každé registraci, aby se ujistil o nákupu s účastníkem. Druhá
dvě jsou e-mailové upomínky na událost, které mají být odeslány v různých časových intervalech.
až do události, aby si adresát vzpomněl na blížící se událost.

Chcete-li přidat komunikaci do záložky „Komunikace“, klikněte na tlačítko „Přidat řádek“. Pak
Vyberte požadovaný způsob komunikace v poli „Odeslat“. Možnosti jsou:
„E-mail“, „SMS“, „Sociální příspěvek“ nebo „WhatsApp“.

Počet komunikací, které lze přidat do :guilabel:`Komunikace`, není omezen.
záložka pro události.

Chcete-li odstranit komunikaci z karty „Komunikace“, klikněte na ikonu „fa-trash-o“.
Ikona „koš“ („trash can“) na příslušné komunikační lince. To odstraní
komunikace z celého dění.

.. důležité:
Volba „Společenský příspěvek“ se objeví pouze tehdy, pokud je nainstalována aplikace „Marketing na sociálních sítích“.
je nainstalován. Možnost „WhatsApp“ se objevuje pouze tehdy, pokud je nainstalovaný modul „Součást WhatsApp“.
je nainstalována.

:doc:`WhatsApp <../../productivity/whatsapp> šablony nelze upravovat během aktivního
konfigurace. K tomu je potřeba zvláštní schválení od společnosti Meta.

Mail
~~~~

Vyberte existující šablonu e-mailu z rozevírací nabídky „Šablona“.

Dále definujte interval, jednotku a spouštěč z jejich
příslušné políčko s rozbalovacím seznamem, které informuje Odoo o tom, kdy by měla být komunikace odeslána.

Možnosti volby :guilabel:`Unit` jsou: :guilabel:`Immediately“, :guilabel:`Hours“, :guilabel:`Days“,
„Týdny“ a „Měsíce“.

Vyberte si možnost z rozevírací nabídky Trigger. Možnosti jsou:
„Po každé registraci“, „Před událostí“ a „Po události“.

Kolonka :guilabel:`Počet odeslaných zpráv` se vyplní číslem zaslaných zpráv a vedle
Čísla jsou různé ikony, které se zobrazují podle stavu konkrétní komunikace.

Stav *Spouštění* je reprezentován ikonou :icon:`fa-cogs` :guilabel:`(tři kola)` .
Stav „Odesláno“ je reprezentován ikonou :icon:`fa-check` :guilabel:`(checkmark)` . A stav
*Plánované* je reprezentováno ikonou :icon:`fa-hourglass-half` :guilabel:`(hodinový sklíčko)` .

Příklad:
Pro odeslání potvrzovací e-mailové zprávy hodinu po registraci účastníka na akci nastavte
následující komunikace:

   - :guilabel:`Intervál`: `1`
   - :guilabel:`Einheit“: :guilabel:`Stunden“
   - :guilabel:`Spouštěč“: „Po každé registraci“

.. poznámka::
Existující šablony e-mailů lze upravovat přímo z nabídky :guilabel:`Šablona`.
pokud je třeba, kliknutím na ikonu „oi-arrow-right“ (pravý směr) vedle
název šablony. To odhalí samostatnou stránku, kde uživatelé mohou upravit :guilabel:`Obsah`.
:guilabel:`Nastavení e-mailu“ a „Nastavení“ konkrétního šablony e-mailu.

Pro zobrazení a správu všech e-mailových šablon aktivujte režim vývojáře a přejděte na
:menu „Nastavení“ - „Technické“ - „E-mail: šablony e-mailů“. Upravujte s opatrností, protože e-mail
šablony se vztahují na všechny komunikace, kde je použita.

..._akce/akce-otazky:

Karta otázek
-------------

V záložce „Otázky“ v formuláři akce mohou uživatelé vytvářet stručné dotazníky pro
registrovaní účastníci, se kterými a kteří na ně reagují po registraci na akci.

Tyto otázky se mohou zaměřit na shromažďování základních informací o účastníkovi nebo na
jejich preference, očekávání a další podobné věci. Tyto informace lze také využít
Vytvořit podrobnější ukazatele reportingu a mohou být použity k vytváření specifických kontaktů.
Generace vládne.

.. obrázek: create_events/questions-tab.png
:align:center
:alt:Typická záložka s otázkami při registraci na události v aplikaci Odoo Events.

.. poznámka::
Ve výchozím nastavení poskytuje Odoo tři otázky v záložce „Otázky“ pro každý formulář události.
Výchozí otázky vyžadují, aby registrované osoby uvedly své jméno a
:guilabel:`E-mailová adresa“ a učiněte volitelnou možnost zahrnout jejich :guilabel:`Telefonní číslo“.

Informace získané v záložce „Otázky“ se nacházejí na
Dashboard pro účastníky, přístupný prostřednictvím ikony „účastníků“
tlačítko. Odoo vyplní jednotlivé záznamy, které obsahují základní informace o registrovaných osobách.
a také jejich preference.

Pokud chcete přidat otázku v záložce „Otázky“, klikněte na tlačítko „Přidat řádek“. To vám umožní
Pop-up okno „Vytvořit otázku“. Zde mohou uživatelé vytvářet a konfigurovat své otázky.

.. obrázek: create_events/create-question-popup.png
:align:center
:alt:Okno Přidat otázku, které se objevuje v aplikaci Odoo Events.

Nejprve zadejte otázku do pole nahoře na formuláři a pak se rozhodněte, jestli má být
vyžaduje povinnou odpověď a/nebo pokud má být dotaz položen jednou za objednávku,
zaškrtnout své příslušné políčko, pokud si přejete.

Pokud je zaškrtnuto pole „Zeptej se jednou na objednávku“, bude se otázka zobrazovat pouze jednou.
Její hodnota je rozeslána všem účastníkům v pořadí (pokud jsou zakoupeny více vstupenek najednou).
Pokud tuto volbu nezaškrtnete, bude se vám Odoo ptát na každého účastníka.
je s ním spojená.

Dále vyberte možnost typu otázky:

- :guilabel:`Výběr“: poskytněte odpovědi na otázku, ze kterých si účastníci mohou vybrat.
Výběr možností odpovědí lze spravovat v sloupci „Odpovědi“ na konci stránky.
pop-up okno.
- :guilabel:`Vstup do pole s textem“: umožňuje uživatelům zadat vlastní odpověď na otázku do textového pole.
- :guilabel:`Jméno“: poskytuje registrovaným uživatelům pole pro zadání jejich jména.
- :guilabel:`E-mailová adresa“: poskytuje registrovaným uživatelům pole pro zadání e-mailové adresy.
- :guilabel:Telefonní číslo: poskytuje registrovaným uživatelům pole pro zadání telefonního čísla.
- :guilabel:`Společnost“: poskytuje registrovaným uživatelům pole, do kterého mohou zadat společnost, se kterou jsou
spojené s ní.

Jakmile jsou veškeré požadované konfigurace zadány, klikněte na tlačítko „Uložit a zavřít“ pro uložení
otázku a vrátit se na kartu „Otázky“ v podobě události nebo kliknout
:guilabel:`Uložit a Nové“ k uložení otázky a okamžité vytvoření nové otázky na novém
Pop-up okno „Vytvořit otázku“.

Jakmile jsou přidány otázky do záložky „Otázky“, informativní sloupce ukazují
konfigurace každé otázky.

Informativní sloupky jsou následující:

- :guilabel:`Název`
- :guilabel:`Povinné“
- :guilabel:`Jednou za objednávku“
- :guilabel:`Typ
- :guilabel:`Odpovědi“ (pokud je to možné).

Pro typy výběru a vstupu textu je statistika zobrazena jako graf.
tlačítko se objevuje na pravé straně otázky. Po kliknutí se zobrazí nová stránka.
ukázat odpověď na konkrétní otázku.

Pro odstranění jakékoliv otázky z karty „Otázky“ klikněte na ikonu „Smazat“.
:guilabel:`(koš)` ikona u příslušné otázky.

Počet otázek, které lze přidat na záložce „Otázky“ v
událostní forma.

..._události/poznámky k událostem:

Tabulka poznámek
---------

V záložce „Poznámky“ v formuláři události mohou uživatelé zanechat podrobné poznámky.
informace pro účastníky akce.

.. obrázek: create_events/notes-tab.png
:align:center
:alt: Typické poznámkové pole v aplikaci Odoo Events na události.

V poli „Poznámka“ v záložce „Poznámky“ mohou uživatelé zanechat poznámky pro ostatní.
pracovníci akce, jako například seznamy úkolů, kontaktní informace, pokyny a podobně.

V poli „Návod k používání lístku“ v záložce „Poznámky“ mohou uživatelé zanechat konkrétní
pokyny pro účastníky události, které se objevují na vstupence účastníků.

Publikovat události
==============

Jakmile jsou všechny konfigurace a úpravy na formuláři události dokončeny, je čas zveřejnit
akci na webu. To ji zobrazí návštěvníkům webu a umožní jim
aby se lidé mohli na akci registrovat.

Aby bylo možné událost zveřejnit po všech úpravách, klikněte na ikonu „fa-globe“.
Klikněte na tlačítko „Přejít na web“ v horní části formuláře události, což odhalí stránku s
webové stránky, které lze upravit stejným způsobem jako jakoukoli jinou webovou stránku na webu pomocí tlačítka „Upravit“
tlačítko.

Chcete-li se dozvědět více o funkcích a možnostech webdesignu, navštivte stránku :doc:`Bloky
<https://www.w3.org/TR/html52/sections.html#building-blocks> dokumentaci.

Jakmile je webová stránka připravena k sdílení, stiskněte červené tlačítko „Nezveřejněno“.
v horním menu, přičemž změní se na zelenou šipku „Zveřejněno“. V tomto bodě je událost
Stránka je zveřejněna a přístupná pro všechny návštěvníky webu.

Pošlete pozvánky na událost
==================

Pro zaslání pozvánky na akci potenciálním účastníkům přejděte do požadovaného formuláře pro události pomocí
Vyberte aplikaci „Události“ > „Událost“, klikněte na požadovanou událost a poté
Tlačítko „Pozvat“ v horním levém rohu formuláře události.

Tím se zobrazí prázdná e-mailová adresa k vyplnění, jak si přejete. Chcete-li se dozvědět více o tom, jak vytvářet a
upravit e-maily podobně, viz :ref:`Vytvoření e-mailu <email_marketing/create_email>
dokumentace.

Pokračujte v tvorbě a přizpůsobení e-mailové zprávy, kterou chcete poslat jako pozvánku potenciálním účastníkům.
Nezapomeňte na stránkách akce uvést odkaz na registrační formulář.
dostat se k registraci co nejrychleji.

..tip:
Odesílání e-mailů z Odoo je omezené denním limitem, který je v základu nastaven na 200.
o denních limitech navštivte dokumentaci :ref:`email-issues-outgoing-delivery-failure-messages-limit`.

.. viz též:
:doc:`spravovat_prezentace“
