Zobrazit obsah

======
Akce
======

Prozkoumejte všechny aspekty podrobného panelu událostí v Odoo a užitečné nastavení, které můžeš
mohou být použity k generování a shromažďování cenných dat o událostech (a jejich účastnících), které pak
přispět k lepšímu rozhodování a plánování událostí.

.. viz též:
„Návody k Odoo: Události <https://www.odoo.com/slides/surveys-63>“

.. karty:

......karta: Vytváření událostí
:target: události/vytvořit_událost

Zjistěte, jak vytvářet události pomocí Odoo.

...... karta: Prodat vstupenky na událost
:target: události/prodat vstupenky

Naučte se vytvářet, konfigurovat a prodávat vstupenky na akce.

...... karta: Sledování a správa hovorů
:target: události/sledovat řečníky

Podívejte se, jak vytvářet, sledovat a spravovat události pomocí Odoo.

...... karta: šablony událostí
:target: události/šablony událostí

Zrychlete proces vytváření událostí pomocí šablon událostí.

...... karta: Události
:target: události/událostní dráhy

Naučte se vytvářet, sledovat a spravovat události pomocí Odoo.

...... karta: Stánky s akcemi
:target: události/stánky

Vytvářet, spravovat a prodávat stánky na akcích.

....... karta: Pracoviště registrace
:target: události/příjem účastníků

Přihlaste účastníky akce okamžitě pomocí funkce registrační pulty v Odoo.

......karta: Zpráva o příjmech
:target: události/zprávy o příjmech

Analyzujte finanční úspěch akcí s Odoo.

Dashboard událostí
================

Když je otevřena aplikace „Události“, Odoo odhalí hlavní panel „Události“ s
může být zobrazeno v několika různých způsobech. Tyto různé možnosti zobrazení jsou dostupné na
:guilabel:`Události“ panel v pravém horním rohu pomocí řady tlačítek s ikonami pro zobrazení.

Výchozí je zobrazení panelu „Akce“ v :icon:`oi-view-kanban`.
Viditelnost „Kanban“, která je naplněna různými fázemi kanálu.

.. obrázek: events/kanban-dashboard.png
:align:center
:alt: Přehled událostí s nastavením kanbanu v Odoo Events.

Tento pohled zobrazuje všechny události v databázi ve svých příslušných fázích. Výchozí nastavení
fáze jsou: „Nový“, „Rezervovaný“, „Oznámený“, „Ukončený“ a
:cancelled:

.. poznámka::
Stadia „Ukončené“ a „Zrušené“ jsou zobrazeny automaticky složené a umístěné na
ostatních fází.

Na každé kartě události najdete datum konání akce, název akce, místo a
Počet očekávaných účastníků („účastníků“), jakékoliv plánované aktivity související s akcí a stav
akce a osoby odpovědné za akci.

Chcete-li rychle přidat novou událost do potrubí, klikněte na ikonu :icon:`fa-plus` :guilabel:`(plus)`
na vrchol scény, kam se přidá událost, aby se na KanaBanu objevila prázdná karta pro vyplnění.

.. obrázek: events/blank-kanban-card.png
:align:center
:alt: Klasická prázdná kartička kanbanu, kterou je možné vyplnit v aplikaci Odoo Events.

Do prázdné karty Kanbanu zadejte název události a datum začátku i konce.
Datum a čas.

Pak buď klikněte na tlačítko „Přidat“ a přidejte ji na jeviště a upravte ji později, nebo klikněte
:guilabel:`Upravit“ přidat událost na pódium a upravit její konfiguraci na samostatné stránce.

Každá karta události může být přetažena a vložena do jakékoli fáze kanbanového řetězce.
organizační přístup.

Nastavení
========

Chcete-li zobrazit možnosti nastavení a funkcí události v aplikaci **Odoo Events**, přejděte na
V menu „Aplikace události“ -> „Konfigurace“ -> „Nastavení“. Zde zaškrtněte políčka vedle
Nastavte požadované funkce a klikněte na tlačítko „Uložit“ pro jejich aktivování.

Sportovní sekce
--------------

V sekci „Akce“ na stránce nastavení jsou vybrané funkce
které lze zapnout, aby bylo možné do událostí vytvořených aplikací Events přidat různé prvky.

.. obrázek: události/nastavení-události-sekce.png
:align:center
:alt:Sekce Události na stránce nastavení událostí v aplikaci Odoo Events.

Funkce `Schedule & Tracks` umožňuje uživatelům spravovat a publikovat harmonogram s trasami.
pro události. Termín „track“ je obecný pojem, který zahrnuje přednášky, semináře, demonstrace
prezentace a další podobné prvky, které uživatelé mohou zahrnout do akce.

Pokud je zapnutá funkce „Rozvrh a dráhy“, objeví se pod ní dvě další pole:
„Živé vysílání“ a „Gamifikace události“.

Funkce „Živý přenos“ umožňuje uživatelům vysílat skladby na internetu prostřednictvím integrace s YouTube.

Funkce „Gamifikace události“ umožňuje uživatelům sdílet kvíz po jakékoliv události v časovém rozmezí.
Pro účastníky, aby si mohli udělat obrázek o tom, kolik se od této skladby naučili. Firmy také
z této funkce, protože následné odpovědi a výsledky testů mohou pomoci
určit, kde jsou silné a slabé stránky společnosti při prezentacích.

Další funkcí je :guilabel:`Online Exhibitors`. Tato funkce umožňuje uživatelům zobrazit sponzory
a vystavovatelé na stránkách událostí, které mohou být cenným lákadlem pro partnerství.
podniky, aby se zúčastnily akce.

Záložka Jitsi Server Domain představuje externí službu pro konferenční hovory.
integrovaný s Odoo. Jeho pomocí vytváříme a hostíme virtuální konference, komunitní místnosti
a další podobné prvky pro akce.

Funkce „Komunitní chatovací místnosti“ umožňuje uživatelům vytvářet virtuální konferenční místnosti.
účastníci akce, kteří jim poskytli centrální místo pro setkávání a diskutování o všem souvisejícím s
událost.

Poslední z nich je funkce „Správa kabin“, která uživatelům umožňuje
schopnost vytvářet a spravovat stánky a rezervace na stáncích. Když je zapnutá, uživatelé mohou vytvořit
různé stánky s různými cenovými body a prodávat je zájemcům.

Registrační sekce
--------------------

V sekci „Registrace“ na stránce „Nastavení“ jsou k dispozici nastavitelné možnosti.
spojené s registrací na akci.

.. obrázek:: události/nastavení-registrace-oddíl.png
:align:center
:alt:Sekce registrace v nastavení události aplikace Odoo Events.

Nastavení „Vstupenky“ umožňuje uživatelům prodávat vstupenky na akce prostřednictvím běžných prodejních objednávek.

Nastavení „Online Ticketing“ vytvoří produkt typu „Vstupenka na akci“, který je možné vybrat.
formulářů, které poskytují uživatelům možnost prodávat vstupenky na akce online prostřednictvím jejich
webové stránky/e-shop.

Sekce návštěvníků
------------------

V sekci „Přítomnost“ na stránce „Nastavení“ je vybraná
prostor, který je přímo spojen s tím, jak se účastníci mohou do akce zapojit nebo se jí zúčastnit.

.. obrázek: events/settings-attendance-section.png
:align:center
:alt:Sekce Účast v nastavení události v aplikaci Odoo Events.

Nastavení „Použít štítek události“ umožňuje skenování čárového kódu (a QR kódu).
pro účastníky akce. To poskytuje účastníkům rychlý přístup a pomáhá uživatelům Odoo
snadno sledovat, spravovat a analyzovat všechny účastníky akce.

Pod položkou „Název štítku“ je pole „Štítek nomenklatury“, které je pod nastavením „Používat štítek události“.
výchozí „Název produktu“, ale lze ji kdykoli změnit.

Vytvářejte události
=============

S aplikací Odoo **Events** lze akce vytvářet ručně od nuly nebo na základě již existujících.
šablony.

Aplikace Events poté integruje s aplikací Website pro zobrazení na webu.
propagace a registrace akce pro účastníky, aplikace **Prodej** pro nákupní schopnost
zaplacených vstupenek a aplikace CRM prostřednictvím přizpůsobitelných pravidel generování leadů.

.. viz též:
:doc:`eventy/vytvorit-udalosti“

Prodat vstupenky na akci
==================

Vytvořte vlastní kategorie vstupenek (s různými cenovými body) pro potenciální návštěvníky akce.
přímým vstupem na šablonu události pod záložkou „Vstupenky“.

Odoo zjednodušuje proces nákupu vstupenek tím, že nabízí mnoho možností platby.
dobře.

.. viz též:
:doc:`akce/prodat-lístky“

Sledovat a spravovat konverzace
======================

Zjistěte, jak získat přístup k různým událostním stopám (přednáškám, prezentacím atd.) a celému programu.
jak se účastníci mohou zapojit do programu akce.

.. viz též:
:doc:`eventy/spravovat-prezentace“

Šablony událostí
===============

Naučte se proces přizpůsobení a konfigurace šablon událostí, které mohou urychlit
vytváření události.

.. viz též:
:doc:`události/šablony událostí“

Stánky s programem
============

Zjistěte, jak vytvářet, spravovat a prodávat stánky na akcích pomocí aplikace **Odoo Events**.
aplikace.

.. viz též:
:doc:`akce/stánky“

Sled událostí
============

Zjistěte, jak vytvářet, spravovat a plánovat různé zkušenosti (takzvané *Tracky*) pro události s
Odoo.

.. viz též:
:doc:`akce/akční dráhy“

Pokladna
=================

Rychle a snadno udělejte přístup k událostem pro účastníky s pomocí aplikace **Odoo Events** Registration Desk
feature.

.. viz též:
:doc:`eventy/prihlaska_na_akci“

Účetní závěrka
===============

Získejte cenné poznatky o příjmech souvisejících s událostmi pomocí přizpůsobitelných zpráv a metrik.

.. viz též:
:doc:`eventy/zpravodajství o příjmech“

.. toctree::

events/vytvorit_udalosti
events/prodat_vstupenky
události/správa přednášek
události/šablony událostí
události / stánky
události/událostní dráhy
události/příjem účastníků
eventy/zpravodajství o příjmech
