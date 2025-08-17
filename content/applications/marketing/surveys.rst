Zobrazit obsah

=======
Průzkumy
=======

Firmy získávají cenné poznatky o zákaznících a zaměstnancích prostřednictvím průzkumů, které jim pomáhají při rozhodování.
rozhodování.

S aplikací Odoo *Surveys* mohou uživatelé vytvářet různé dotazníky, ankety, testy, hodnocení a
a mnohem víc. Tyto lze použít k shromáždění zpětné vazby, hodnocení úspěšnosti nedávno proběhlé akce a
zjišťovat spokojenost zákazníků a zaměstnanců. Tento proces přináší cenné poznatky o
změny na trhu.

.. viz též:
`Tutoriály Odoo: Ankety <https://www.odoo.com/slides/surveys-62>`_

.. karty:

..... karta: Vytváření průzkumů
:target: průzkumy/vytvořit

Zjistěte, jak vytvářet průzkumy pomocí Odoo.

...... karta: Hodnocení průzkumu
:target: průzkumy/skóre

Naučte se vytvářet a analyzovat průzkumy pomocí Odoo.

... karta: Vytvořit otázky
:target: průzkumy/otázky

Podívejte se na to, jak vytvářet, konfigurovat a přizpůsobovat všechny typy otázek průzkumu pomocí Odoo.

...... karta: Živé průzkumy
:target: průzkumy/živá sezení

Zjistěte vše o unikátních anketách živých relací Odoo.

...... karta: Analýza průzkumu
:target: průzkumy, analýzy

Prozkoumejte různé způsoby analýzy průzkumů pomocí hlubokých stránek pro reportování v Odoo.

Přístrojová deska
=========

Po otevření aplikace „*Průzkumy*“ představuje společnost Odoo hlavní panel aplikace „*Průzkumy*“.
aplikace, známá také jako stránka s názvem „Výzkumy“.

.. obrázek: průzkumy/přehled-průzkumu.png
:align:center
:alt:Příklad přehledu aplikace Odoo Survey v kanbanovém pohledu.

..tip:
Panel „Průzkumy“ je v aplikaci přístupný po celou dobu kliknutím na
:menuitem:`Průzkumy“ z nabídky hlavního menu.

V horním levém rohu je tlačítko „Nový“. Po jeho kliknutí se zobrazí prázdná stránka.
dotazník, který lze použít k vytvoření průzkumu.

Na přístrojové desce jsou zobrazeny všechny průzkumy vytvořené v databázi.
Kanban pohled.

Zleva doprava: pořadí průzkumu, uživatel odpovědný za něj a měsíc, kdy byl proveden.
vytvořené, každá řádka na stránce Zobrazení průzkumu zobrazí následující:

- Počet otázek v daném průzkumu
- :guilabel:'Průměrná doba' průzkumu (jak dlouho obvykle trvá, než účastník dotazníku vyplní celý dotazník).
- Počet zaregistrovaných respondentů pro průzkum
- Početrkrát, kdy byl právě tento dotazník vyplněn.
- Procenta a grafické znázornění, které ukazuje kolik lidí má nebo získalo
:guilabel:`Ověřené“

...... poznámka::
Procento „Přijato“ a čára se zobrazuje pouze tehdy, když je požadovaný skóre dosažen.
konfigurované pro daný průzkum.

Procento a čárka „Certifikovaný“ se zobrazí pouze u průzkumu, který má tento certifikát.
*Je povolená možnost „Certifikace“ v dotazníku.*

Pokud se na řádku nezobrazí ani „Prošel“ ani „Ověřen“, znamená to, že
:         průzkum nemá požadovaný skóre a nebyl zapnut s možností „Certifikace“.

- Počet kurzů souvisejících s tímto průzkumem, které se zobrazí pouze v případě, že je více než
Kurz byl vytvořen a připojen k jedinému dotazníku.

.. poznámka::
Půl trofejového pozadí za názvem průzkumu naznačuje, že se jedná o
*Certifikace*.

Vpravo od těchto bodů na liniích průzkumu v aplikaci „Průzkumy“
dashboard jsou tlačítka.

Takové tlačítka jsou následující:

- Kliknutím na tlačítko „Sdílet“ se zobrazí okno pro sdílení s možností
pozvat potenciální účastníky průzkumu - včetně odkazu na průzkum, který mohou vyplnit.
kopírována a zaslána potenciálním účastníkům a přepínač „Odeslat e-mailem“.

Když je zapnutá tlačítko „Odeslat e-mailem“ (zelené přepínače), objeví se další pole.
které lze zadat v poli „Příjemci“, „Další e-maily“ a „Téma“.
Přidáno do e-mailu.

Pod ním je dynamický e-mailový šablonu s tlačítkem „Zahájit certifikaci“
Výsledkem je tedy vytvoření nové stránky, která může být upravena, pokud je to potřeba.

:guilabel:`Přílohy“ lze přidat do e-mailu a také může být nastaveno „Termín odpovědi“.
je možné nastavit, pokud je třeba.

Jakmile jsou úpravy dokončeny, klikněte na tlačítko „Odeslat“ a odeslat e-mailovou pozvánku všem uživatelům.
adresy/kontakty uvedené v poli :guilabel:`Příjemci`.


:synchronizace: střed
:alt:Okno „Sdílet průzkum“ v aplikaci Odoo Průzkumy s aktivovanou funkcí odeslání e-mailem.

..tip:
Výchozí šablona pro pozvánky do průzkumu lze upravit tak, že se přejde na
:menuvolba:`Nastavení --> Technické --> Vzorky e-mailů“ a hledáním „Výzkum: Zveme“.

...... poznámka::
Přepínač „Odeslat e-mailem“ je **nepřítomen**, pokud je v průzkumu nula.
otázky.

Poznámka „Odkaz na průzkum“ se zobrazí pouze tehdy, pokud je nastavený způsob přístupu k průzkumu na *Kdokoliv*.
odkaz*.

Pole „Další e-mail“ se zobrazí pouze tehdy, pokud je pole „Požadované přihlášení“ povinné.
**neaktivní**.

- :guilabel:`Testování`: klikněte pro otevření nového okna s verzí testu dotazníku.
pro kontrolu chyb nebo nesrovnalostí.
- :guilabel:Zobrazit výsledky“: kliknutím se zobrazí nová záložka s podrobnými metrikami a grafy
reprezentace všech účastníků průzkumu, otázek a odpovědí pro hlubší analýzu.
- :guilabel:Zahájit živou anketu“: klikněte na tlačítko pro zahájení „Živé ankety“, a zobrazí se okno
manažer okna v novém tabu. Tlačítko pro otevření manažera okna není k dispozici u průzkumů, které povolily
možnost certifikace na dotazníku.
- Klikněte na tlačítko „Ukončit živý průzkum“: kliknutím ukončíte *živý průzkum*, který byl oficiálně
a tato možnost se objeví pouze u průzkumných linií, které již dříve zahájily živý
sezení.

Vpravo od průzkumných čar jsou tlačítka s ikonou „⋮“ (tři
ikona se zobrazí, když kurzor přejede nad konkrétní řádkem. Když kurzor přejde nad tímto řádkem, objeví se ikona :guilabel:⋮ (tři tečky).
Když je kliknutý ikonu „Tečky“ (.), objeví se vpravo od něj nabídka s možnostmi týkajícími se konfigurace:

Možnosti jsou následující:

- :guilabel:`Upravit průzkum“: Když je kliknuté, Odoo zobrazí formulář pro daný průzkum.
které lze následně upravit různými způsoby.
- Kliknutím na tlačítko „Sdílet“ se zobrazí okno „Sdílet anketu“, které umožňuje
mohou být použity k pozvání potenciálních účastníků průzkumu.
- :guilabel:`Smazat“: Když uživatel klikne na tlačítko, Odoo zobrazí okno s upozorněním, ve kterém **musí** potvrdit
chce průzkum zcela smazat, což může udělat kliknutím na tlačítko „Smazat“.
tlačítko na spodní hraně okna.
- :guilabel:`Barva“: uživatelé si mohou zvolit barvu, kterou chtějí přidat k průzkumné linii na panelu nástrojů
Pokud je potřeba, přidá se i organizační účel.

.. obrázek:: průzkumy/trojtečka-s-seznamem.png
:align:center
:alt:Tři tečky, které se objeví v nabídce na úvodní stránce průzkumu Odoo.

Pod tlačítky, která jsou umístěna na nejvzdálenějším pravém konci průzkumné čáry, je zobrazeno *Aktivita*.
tlačítko, které je reprezentováno ikonou „🕘 (hodiny)“. Po kliknutí se zobrazí malé okénko.
z nichž lze naplánovat a upravit aktivity související s daným šetřením.

.. obrázek: průzkumy/zaplnit-časový-plán-souboru.png
:align:center
:alt:Výběr aktivit, který se objeví v přehledu průzkumu Odoo.

Zobrazení seznamu
---------

Přístup k panelu „Průzkumy“ je v kanbanovém pohledu výchozí, ale existuje také seznamový pohled.
možnost dostupná v pravém horním rohu, reprezentovaná ikonou „:guilabel:≣ (čárky)“.

Když je kliknutý ikonu „:guilabel:`≣ (bary)“ se zobrazí seznam dat týkajících se průzkumu v mřížkovém pohledu.

.. obrázek: průzkumy/seznam-výsledků.png
:align:center
:alt:Možnost zobrazení seznamu v aplikaci Odoo Survey.

Sloupce zobrazené na stránce aplikace Dashboard v seznamovém pohledu jsou následující:

- :guilabel:`Název průzkumu`
- :guilabel:`Zodpovědný“
- :guilabel:`Průměrná doba“
- :guilabel:`Registrovaný“
- :guilabel:`Úspěšnost (%)“
- :guilabel:`Průměrné skóre (%)“

..tip:
Do aplikačního panelu můžete přidat další sloupce, zatímco v seznamovém zobrazení.
kliknutím na rozevírací nabídku „Další možnosti“, která se nachází vpravo od názvů sloupců.
Je reprezentován ikonou „(dva body)“.

Zobrazení aktivit
---------------

Mít aplikaci Dashboard Surveys zobrazovat pouze aktivity spojené s
výsledky průzkumů v databázi, klikněte na ikonu „⏰“ (hodiny) vedle ostatních výsledků
v pravém horním rohu.

.. obrázek: průzkumy/aktivity-přehled.png
:align:center
:alt:Možnost Zobrazit aktivity na hlavní obrazovce aplikace Odoo Survey.

Takto se zobrazí tabulka s řádky a sloupci. Řádky ukazují různé průzkumy v databázi.
A sloupce ukazují různé typy aktivit.

.. poznámka::
V tomto pohledu nelze vytvářet nové průzkumy, protože je určen pouze pro tvorbu a
zobrazení plánovaných aktivit.

Vytvářejte průzkumy
==============

Zjistěte, jaké jsou všechny možnosti a konfigurace, které lze použít při vytváření průzkumu
v Odoo.

.. viz též:
:doc:`dotazníky/vytvořit“

Scoring průzkumy
===============

Zjistěte, jak měřit výkonnost nebo celkovou spokojenost účastníka průzkumu pomocí Odoo.
podrobný (a plně přizpůsobitelný) systém hodnocení průzkumu.

.. viz též:
:doc:`dotazníky/skórování“

Vytvářejte otázky
================

S aplikací Odoo *Surveys* je k dispozici mnoho typů otázek a možností výběru, což umožňuje
vytvořit jakýkoliv unikátní průzkum, dotazník nebo certifikaci.

.. viz též:
:doc:`dotazníky/otázky“

Ankety v reálném čase
====================

Možnost průzkumu *Živá sekce* dostupná v Odoo může zvýšit osobní předvádění.
prezentace, kde se může využít reakce účastníků v reálném čase k určení směru konverzace
přichází na řadu.

.. viz též:
:doc:`dotazníky/živá sezení“

Analýza průzkumu
===============

Jakmile začnou přicházet odpovědi z průzkumu, je čas analyzovat odpovědi vašich účastníků.
Naštěstí stránky s hlubšími informacemi a možnosti dostupné v Odoo *Surveys* nabízí nekonečný
způsoby prozkoumání všeho souvisejícího s průzkumy a jejich odpovědi.

.. viz též:
:doc:`dotazníky/analýza“

.. toctree::


průzkumy/vytvořit
průzkumy/skóre
ankety/otázky
průzkumy/živá sezení
průzkumy a analýzy
