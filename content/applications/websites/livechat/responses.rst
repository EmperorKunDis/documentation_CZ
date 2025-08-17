=============================
Příkazy a předpřipravené odpovědi
=============================

V aplikaci Odoo **Live Chat** umožňují uživatelům provádět konkrétní akce pomocí příkazů.
v okně chatu a prostřednictvím dalších aplikací Odoo. Aplikace Live Chat zahrnuje
*přednastavené odpovědi*. Jde o předem připravené náhrady, které umožňují uživatelům nahradit
zkrácené odpovědi místo delších a promyšlených odpovědí na některé z nejčastějších otázek
a komentáře.

Obě funkce ušetří čas a umožní uživatelům zachovat určitou úroveň konzistence.
Během celé konverzace.

Spustit příkaz
=================

Live chatové příkazy jsou klíčová slova, která spouštějí předem připravené akce. Když uživatel vloží do chatu živého operátora
Když se účastní konverzace s klientem nebo návštěvníkem webu, mohou provést příkaz
a poté zadat příkaz.

Příkazy a následné akce jsou viditelné pouze v okně konverzace pro živý chat.
operátor. Zákazník nevidí žádné příkazy, které operátor používá při konverzaci od svého
pohled do chatu.

Příklad:
Během konverzace s klientem provede operátor chatu příkaz ke vytvoření
„živé chaty / tiket“). Po zadání příkazu / tiket se systém automaticky
Vytvoří lístek s informacemi z konverzace, který obsahuje také odkaz na nový
tiketu, takže operátor se může přímo na místě doplnit o další informace, pokud je třeba.

.... obrázek: odpovědi/odpověď-sleva-na-vstupenku.png


Podrobnější informace o každé dostupné příkazu naleznete níže.

Pomoc
----

Pokud operátor zadá do okna chatu příkaz /help, objeví se v něm informativní zpráva obsahující možné
Zobrazí se typy vstupů, které může uživatel zadat.

- Začněte psát @username, abyste zmínili uživatele v konverzaci. Upozornění bude zasláno tomuto uživateli.
do doručené pošty nebo e-mailu v závislosti na nastavení oznámení.
- Zadejte příkaz /command, abyste spustili příkaz.
- Zadejte zkratku :shortcut, aby se vložil :ref:`připravený odpovědní text <live-chat/canned-responses>“.

.. viz též:
   - :doc:`/aplikace/produktivita/diskuse`
   - :doc:`/aplikace/produktivita/diskuse/týmová komunikace`

Lístky a vyhledávání lístků
-----------------------

Komandá /ticket a /search_tickets umožňují operátorům vytvářet přímo na zákaznické podpoře lístky.
z konverzace nebo vyhledáním stávajících lístků podle klíčového slova nebo čísla lístku.

.. důležité:
Komandu /ticket a /search_tickets lze použít jen v případě, že aplikace Helpdesk je
bylo nainstalováno a aktivováno *Živé chaty* na týmu *Helpdesku*.
Přejděte do sekce „Nápověda“ aplikace „Helpdesk“, vyberte konfiguraci a tým.
Přejděte do sekce „Kanály“ a zaškrtněte políčko vedle „Živý chat“.

.. _live-chat/ticket:

Vytvořit lístek z chatu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud operátor zadá do okna chatu příkaz /ticket, konverzace se použije k vytvoření Helpdesku.
lístek.

Po zadání příkazu /ticket do okna chatu zadejte název lístku, pak stiskněte
„Zadat“.

.. obrázek: odpovědi/helpdesk.png
:alt:Pohled na výsledky vyhledávání v konverzaci živého chatu.

Nově vytvořený lístek bude přidán do týmu Helpdesku, který má zapnutou funkci živého chatu. Pokud
pokud je v jednom týmu zapnutá funkce živého chatu, pak bude automaticky přiřazen na základě týmu.
prioritou.

Záznam z rozhovoru bude přidán k novému lístku pod
:guilabel:`Popis“ záložka.

Pro přístup k novému lístku klikněte na odkaz v okně chatu nebo přejděte na
Vyberte v nabídce aplikace „Helpdesk“ a klikněte na tlačítko „Tikety“ na kartě Kanban.
vhodný tým.

Hledání lístku přes živý chat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud operátor zadá do okna chatu příkaz /search_tickets, může vyhledat v HelpDesku.
lístky buď podle čísla lístku nebo klíčového slova.

Po zadání příkazu /search_tickets zadejte klíčové slovo nebo číslo lístku a stiskněte
:kd Enter. Pokud se najde alespoň jedno související ticket, vytvoří se seznam odkazů
Okno konverzace.

.. obrázek: odpovědi/helpdesk-vyhledávání.png
:alt:Pohled na výsledky vyhledávání v konverzaci živého chatu.

.. poznámka::
Výsledky vyhledávacího příkazu uvidí pouze operátor, nikoli zákazník.

Historie
-------

Pokud operátor zadá do okna chatu příkaz /history, vygeneruje se seznam posledních stránek.
Počet návštěvníků, kteří navštívili webové stránky (až do 15).

.. obrázek: odpovědi/odpovědi-historie.png
:alt:Výsledky z příkazu /history v konverzaci na živém chatu.

Lead
----

Při zadání příkazu /lead v okně chatu může operátor vytvořit nový lead v aplikaci CRM.

.. obrázek: odpovědi/odpovědi-vůdce.png
:alt:Výsledky z příkazu /lead v konverzaci živého chatu.

.. důležité:
Příkaz „/lead“ lze použít jen v případě, že je nainstalována aplikace CRM.

Po zadání řetězce /lead vytvořte název pro tento nový lead, pak stiskněte klávesu Enter. Vygeneruje se odkaz na lead
Titulek se zobrazí. Klikněte na odkaz nebo přejděte do aplikace CRM, abyste si mohli prohlédnout
:guilabel:`Trubka“.

.. poznámka::
Připojení k novému kontaktu je možné vidět a přistupovat pouze pro operátora, nikoli pro zákazníka.

Přepis konkrétní živé chatu (kde vznikl kontakt) je přidán do
Kartě „Vnitřní poznámky“ v hlavním formuláři.

Na záložce „Další informace“ v hlavním formuláři bude uvedeno
:label:Živý chat.

Odejít
-----

Pokud operátor zadá do okna chatu příkaz /leave, může se automaticky odhlásit z konverzace.
příkaz nevyřazuje zákazníka z konverzace a automaticky
Ukončit konverzaci.

.. viz též:
   - :/prihlaseni/sales/crm/acquire_leads
   - :doc:`../../sluzby/helpdesk`

.._online chatu/předem připravené odpovědi:

Kancelářské odpovědi
================

Kancelářské odpovědi jsou přizpůsobitelné vstupy, kde zkratka nahrazuje delší odpověď.
operátor zadá zkratku a ta se automaticky nahradí rozšířenou *záměnou*.
reakce v konverzaci.

Vytvořte předpřipravené odpovědi
-----------------------

Pro vytvoření nové odpovědi zvolte: „Aplikace pro živý chat --> Konfigurace --> Přednastavené
Odpovědi --> Nové.

Do pole „Krátká klávesová zkratka“ zadejte příkazovou zkratku. Následně klikněte na „Zástupce“.
pole a zadejte zprávu, která má nahradit zkratku.

..tip:
Zkuste spojit zkratku s tématem výměny. Pro operátory by mělo být snadnější ji zapamatovat, pokud bude mít nějaký vztah k tématu výměny.
Vzpomínám si, že čím víc se používají předpřipravené odpovědi v konverzaci, tím snadněji je lze používat.

Autorizované skupiny
~~~~~~~~~~~~~~~~~

Když vytvoříte novou odpověď, může ji používat jen operátor, který ji vytvořil.
Chcete-li umožnit odpověď ostatním operátorům, vyberte jednu nebo více skupin:
z rozevíracého seznamu „Skupiny s oprávněním“ v poli „Skupina s oprávněním“.

Používejte předpřipravené odpovědi v živém chatu
------------------------------------------------

K použití předpřipravené odpovědi v konverzaci klikněte na ikonu :icon:`fa-plus-circle` :guilabel:`(plus)`
v okně zprávy. Pak klikněte na tlačítko „Vložit přednastavenou odpověď“. To otevře seznam
k dispozici odpovědi z přednastavených odpovědí. Buď vyberte odpověď ze seznamu nebo napište vhodné
zkrátka klikněte na ikonu „fa-paper-plane“ (odeslat) nebo stiskněte klávesu Enter.

..tip:
Do chatu lze zadat pouze „::“ a tím se vygeneruje seznam dostupných předpřipravených odpovědí.
Odpovědi lze vybírat z nabídky a kromě toho je možné používat i zkratky.

.... obrázek: odpovědi/odpověď-seznam.png
:alt: Pohled na okno chatu a seznam dostupných odpovědí.
