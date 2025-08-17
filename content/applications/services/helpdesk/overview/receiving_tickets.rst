=================
Přijímání lístků
=================

Aplikace Helpdesk společnosti Odoo nabízí několik kanálů, kde si mohou zákazníci vyžádat pomoc.
e-mailem, prostřednictvím chatu v reálném čase nebo pomocí formuláře na webu.
Zákazníkům poskytuje rychlou podporu prostřednictvím více kanálů, a také umožňuje
podporu týmu, který by spravoval vícekanálové podpůrné požadavky z jednoho centrálního místa.

Zapněte možnosti kanálu pro odesílání požadavků
========================================

Přejděte na: `Helpdesk app --> Konfigurace --> Týmy helpdesku` a vyberte existující
tým nebo klikněte na „Nový“ pro vytvoření nového týmu (viz helpdesk).

Na stránce nastavení týmu přejděte dolů na položky „Kanály“ a „Centrum nápovědy“.
sekcí. Zapněte jeden nebo více kanálů zaškrtnutím příslušných políček.

- :ref:`E-mailová alias <helpdesk/obdržení_tiketů/e-mail-alias>
- :ref:`Chat v reálném čase <helpdesk/receiving_tickets/live-chat>`
- :ref:`Webová stránka formuláře <helpdesk/receiving_tickets/web-form>`

.. _helpdesk/prijimani_tiketu/e-mail-alias:

Emailová přezdívka
-----------

Nastavení „E-mailová přezdívka“ vytváří příležitosti z e-mailů zaslaných na uvedenou e-mailovou přezdívku týmu.

.. důležité:
Pro následující kroky platí pro databáze **Odoo Online** a **Odoo.sh**, pro **on-premise**
pro e-mailové aliasy je nutný externí server.

Když je vytvořen nový tým **Helpdesku**, vytvoří se pro něj e-mailová adresa. Tuto adresu lze změnit
na stránce nastavení týmu.

Chcete-li změnit e-mailovou adresu týmu **Helpdesku**, přejděte na:
Konfigurace --> Týmy podpory, klikněte na název týmu pro otevření jeho nastavení.

Poté přejděte na položku „Kanály“ -> „E-mailová adresa“. V poli „Alias“ zadejte
Přání pro e-mailovou adresu týmu.

.. obrázek:prijem-vstupenek/prijem-vstupenek-e-mail-alias.png
:alt: Zobrazení nastavení stránky týmu Helpdesku s důrazem na funkci e-mailového aliasu v Odoo
Helpdesk.

.. poznámka::
Použití e-mailové adresy s vlastním doménovým jménem není nutné pro používání e-mailových aliasů, nicméně mohou být
konfigurovat prostřednictvím aplikace **Nastavení**.

Pokud databáze nemá již přednastavenou vlastní doménu, klikněte na tlačítko „Nastavit alias“.
Doména by měla být přesměrována na stránku nastavení. Zde je potřeba zapnout volbu „Vlastní
Emailové servery.

Když je e-mail přijat, předmět se stane titulem nového **tiketu HelpDesku**. Tělo
email je také přidán do lístku pod záložkou „Popis“ a v samotném lístku
šeptání.

.. _helpdesk/prijimani_tiketu/online-chat:

Chat
---------

Funkce „Živý chat“ umožňuje návštěvníkům webu přímé spojení s pracovníkem podpory nebo chatbote.
Tikety HelpDesku lze vytvářet během těchto konverzací pomocí odpovědi
příkaz </aplikace/weby/livechat/odpovědi>/<id_tiketu>

Pro zapnutí funkce „Živý chat“ přejděte na:
V seznamu týmů vyberte tým, na stránce nastavení klikněte na zaškrtávací políčko vedle
pod záložkou „Živé chaty“ v sekci „Kanály“.

.. poznámka::
Pokud je to poprvé, pak se jedná o zapnutí služby :doc:`Live Chatu </applications/websites/livechat>`.
databáze a stránka může potřebovat ruční uložení a obnovení před dalším krokem.
se přijmout.

Po zapnutí nastavení „Živý chat“ v týmu **Helpdesku** se zobrazí nové okno „Živý chat“.
je vytvořen kanál. Klikněte na tlačítko „Nastavit živý chatový kanál“ pro aktualizaci kanálu.
Nastavení.

Konfigurace kanálu živého chatu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Na stránce nastavení kanálu lze upravit pole „Název kanálu“, ale Odoo jej pojmenovává
kanál, který odpovídá názvu týmu Helpdesk, pokud nebyl zadán jiný kanál.

Příklad:
Pokud tým Helpdesku nese název „Zákaznický servis“, vytvoří se kanál pro živé chaty s názvem
„Zákaznický servis“.

.... obrázek: získávání vstupenek/získávání vstupenek - živý chat nová kanál.png
:alt: Pohled na karty kanbanu pro dostupné kanály chatu v reálném čase.

Přejděte na kartu Formát kanálu a přesunutím se do záložek dokončete nastavení.

Operátorské klávesy
*************

„Provozovatelé“ jsou uživatelé, kteří se chovají jako zástupci a reagují na žádosti o chat v reálném čase od zákazníků.
uživatel, který vytvořil živý chat, je přidán automaticky.

Chcete-li přidat další uživatele, klikněte na záložku „Operátoři“, pak klikněte na „Přidat“.

Zaškrtněte políčko vedle uživatelů, kteří mají být přidáni na okno „Přidat: Operátor“.
a pak klikněte na „Vybrat“.

Klikněte na tlačítko „Nový“ pro vytvoření nových operátorů, pokud je potřebujete.

Když je požadovaná přidaná část hotová, klikněte na tlačítko „Uložit a zavřít“ nebo „Uložit a nový“.
přidat nové operátory.

.. nebezpečí::
Vytvořením nového uživatele se může změnit stav předplatného Odoo, protože celkový počet uživatelů
Při vytváření nového uživatele buďte opatrní, protože počet záznamů v databázi se započítá do účtovací sazby.
Pokud uživatel již existuje, přidání jej jako operátora **nezmění** předplatné nebo
účtování za databázi.

Dále lze stávající operátory upravit nebo odstranit kliknutím na jejich příslušné políčko v
kartě „Provozovatelé“ a poté upravit jejich hodnoty v okně s vyskakovacím formulářem.
nebo pomocí tlačítka umístěného na spodní části formuláře, například „Odstranit“.

..tip:
Uživatelé se mohou přidat jako operátoři kliknutím na tlačítko „Připojit se do kanálu“ v
kanál **Živý chat**.

.... obrázek:: získávání lístků/získávání lístků - připojte se do živého chatu.png
:alt: Pohled na živý chatový kanál s vyznačeným tlačítkem pro připojení.

Karta Možnosti
***********

Karta „Možnosti“ obsahuje vizuální a textové nastavení okna chatu v reálném čase.

.. obrázek: přijímání_vstupenek/přijímání_vstupenek_možnosti_karty.png
:alt: Zobrazení nabídky nastavení kanálu živého chatu.

- :guilabel:`Text oznámení“: Toto pole aktualizuje pozdrav zobrazený v textové bublině, když
Ve chvíli, kdy se na webu objeví tlačítko pro živý chat.

- :guilabel:`Barva tlačítka živého chatu“: Toto pole mění barvu tlačítka pro živý chat.
je zobrazen na webové stránce. Chcete-li změnit barvu, klikněte na barevnou bublinu a otevřete si výběr barev.
Okno výběru, pak klikněte a přetáhněte kruh po barevné škále. Klikněte mimo okno výběru
jednou dokončené. Klikněte na obrázek s ikonou obnovení vpravo od barevných bublin, abyste barvy znovu nastavili.
výchozí výběr.

- guilabel:Zobrazit: Tlačítko chatu se zobrazuje na vybrané stránce.
- Zobrazit s oznámením: Tlačítko chatu je zobrazeno a k němu přidán
:guilabel:`Text oznámení“ z karty „Možnosti“.
- :guilabel:`Otevřít automaticky“: Zobrazí se tlačítko „Chat“, které otevře chat.
Okno po určitém čase. Čas je stanoven pomocí :guilabel:`Otevřít
automaticky se objeví pole „Časovač“, které se zobrazí pouze v případě, že je tato možnost vybrána.
- :guilabel:`Skrýt chaty“: Tlačítko pro zahájení chatu je skryto na webové stránce.

..tip:
Volba barvy pro tlačítko nebo nadpis lze provést ručně nebo pomocí kódu RGB, HSL nebo HEX.
výběru. Různé možnosti jsou k dispozici v závislosti na operačním systému nebo prohlížeči.

Karta Pravidla kanálu
*****************

V záložce „Pravidla kanálu“ se určuje, kdy se v prohlížeči otevře okno chatu.
kdy je spuštěna akce URL regex (např. při návštěvě stránky).

..tip:
Regex, nebo výraz regulární gramatiky, je někdy označován jako racionální výraz. Je to
sekvence znaků, která specifikuje shodnost vzorce ve textu. Shoda je provedena na základě
pro řadu čísel nebo pro sadu znaků.

Upravte stávající pravidla vybráním je v záložce „Pravidla kanálu“ nebo vytvořte nové pravidlo.
kliknutím na tlačítko „Přidat řádek“.

Pak pokračujte v konfiguraci podrobností o tom, jak by měla pravidlo fungovat na vyskakovacím okně.
se objevuje.

Zvolte, jak se tlačítko živého chatu zobrazí na webové stránce.

- guilabel:Zobrazit: Tlačítko chatu se zobrazuje na vybrané stránce.

- Zobrazit s oznámením: Tlačítko chatu je zobrazeno a k němu přidán
:guilabel:`Text oznámení“ z karty „Možnosti“.

- :guilabel:`Otevřít automaticky“: Zobrazí se tlačítko „Chat“, které otevře chat.
Okno po určitém čase. Čas je stanoven pomocí :guilabel:`Otevřít
automaticky se objeví pole „Časovač“, které se zobrazí pouze v případě, že je tato možnost vybrána.

- :guilabel:`Skrýt chaty“: Tlačítko pro zahájení chatu je skryto na webové stránce.

K zobrazení chatu s umělou inteligencí na tomto kanálu vyberte jej v rozevíracím seznamu. Pokud je chatbot
pouze v případě, že nejsou k dispozici žádní operátoři, zaškrtněte políčko s názvem:guilabel:`Povoleno pouze
jestliže není operátor.

.. poznámka::
Pokud se do chatu přidá chatbot,
nové tlačítko „chatbot“ se objeví v nastavení kanálu. Kliknutím sem můžete chatbota vytvořit.
a aktualizovat skript chytrého botu.

Každá řádka v skriptu obsahuje zprávu, typ kroku a
:guilabel:Odpovědi a podmíněná logika, která se aplikuje při určitých předvyplněných odpovědích
Jsou vybírány.

Chcete-li vytvořit další kroky ve skriptu, klikněte na tlačítko „Přidat řádek“, vyplňte pole pro kroky
podle požadované logiky.

Do pole „Regex URL“ zadejte adresy stránek, na kterých by se kanál měl objevit.
Je potřeba cesta od kořenového doménového jména, ne celá adresa URL.

Pokud by tento kanál měl být dostupný pouze uživatelům v konkrétních zemích, přidejte tyto země do
Pole „Země“. Pokud je pole nevyplněné, kanál je dostupný na všech místech.
návštěvníci.

.. obrázek: přijímání vstupenek/přijímání vstupenek - pravidla kanálu.png
:alt: Pohled na karty kanbanu pro dostupné živé chaty.

Widgetová záložka
**********

Karta Widget v živém chatu nabízí webový widget, který lze přidat
na webové stránky třetích stran. Kromě toho je k dispozici URL, který poskytuje okamžitý přístup na živé
chatové okno.

Chatovací okno lze aplikovat na webové stránky vytvořené prostřednictvím Odoo kliknutím na
V nabídce „Webová aplikace“ -> „Konfigurace“ -> „Nastavení“ -> „E-mail a marketing“. Pak přejděte
do pole „Živý chat“ a vyberte kanál, který chcete přidat na web. Klikněte
:guilabel:`Uložit“ k použití.

Chcete-li přidat widget na webovou stránku vytvořenou na třetí straně, klikněte na tlačítko „Kopírovat“.
a vložte kód do značky <head> na webu.

Klikněte na tlačítko „Zkopírovat“ vedle ikony živého chatu, pokud chcete odeslat konverzaci zákazníkovi nebo dodavateli.
druhý seznamovaný kód a odeslat URL e-mailem.

Vytvořit podporu z živého chatu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Operátoři, kteří se připojili do chatu v reálném čase, mohou komunikovat s návštěvníky webu.
v reálném čase.

Během konverzace může operátor použít zkratku :doc:`command
do vytvoření nového požadavku bez opuštění chatu.
okno. Přepis rozhovoru je přidán do nového lístku, pod
:guilabel:`Popis“ záložka.

..tip:
Tikety Helpdesku lze vytvářet také prostřednictvím :doc:`WhatsApp


.. _helpdesk/prijimani_ticketu/webovafom:

Webový formulář
------------

Povolení nastavení „Webová stránka“ přidá na web novou stránku s vlastními formuláři.
lístek je vytvořen po vyplnění všech potřebných políček a odeslání.

Pro aktivování webové verze přejděte na stránku nastavení týmu pod položkou „Aplikace Helpdesk“
Konfigurace -> Tým helpdesku“ a vybrat požadovaný tým z nabídky.

Následně najděte funkci „Formulář webu“ pod sekcí „Centrum nápovědy“.
zaškrtněte políčko.

Pokud je na databázi více webových stránek, ověřte, že je uvedena správná.
Pole „Webová stránka“ nebo vyberte správnou možnost ze seznamu.

Po aktivaci funkce klikněte na tlačítko „Přejít na web“ v horní části
Nastavení stránky týmu a zobrazit nebo upravit novou webovou formu, která je vytvořena.
automaticky prostřednictvím Odoo.

.. poznámka::
Po zapnutí nastavení „Webová stránka“ může být potřeba aktualizovat stránku týmu.
před tím, než se objeví tlačítko „Přejít na web“.

Pokud je publikován *Help Center*, chytrý tlačítko se nejprve přesune na něj.
Klikněte na tlačítko „Kontaktujte nás“ v dolní části fóra a přejděte do sekce „Ticket“.
formulář pro podání žádosti.

.. obrázek:: získávání lístků/lístky putují na webové stránky.png
:alt: Zobrazení nastavení stránky týmu pomoci s důrazem na tlačítko Přejít na web
Odoo Helpdesk.

Přizpůsobení webového formuláře pro nákup vstupenek
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro přizpůsobení výchozího formuláře pro zaslání žádosti o podporu v administraci webu klikněte na tlačítko „Upravit“.
tlačítko v pravém horním rohu stránky. To otevře editační lištu na pravé straně.
Poté klikněte na jedno ze políček v formuláři, který se nachází na těle webové stránky, a upravte jej.

Chcete-li přidat nový prvek, přejděte do sekce „Pole“ v bočním panelu a klikněte na tlačítko „+“.
Hřiště.

Klikněte na ikonu „koš“ (:guilabel:`🗑️`) pro odstranění pole, pokud je třeba.

Upravte ostatní možnosti nového pole v bočním panelu podle potřeby:

- :guilabel:`Typ“: shoduje hodnotu modelu s poli (např. „Jméno zákazníka“).
- :guilabel:`Typ vstupu“: určete typ vstupu pole, například „Text“, „E-mail“.
„Telefon“ nebo „URL“.
- :label:„Štítek“: Přidejte do pole štítek (například „celé jméno“, „E-mailová adresa“, atd.).
můžete kontrolovat umístění štítku na formuláři pomocí možností „Pozice“ vložených do :guilabel:`Position`.
- :guilabel:`Popis“: určete, zda se pod textovým polem má nebo nemá zobrazit editační řádek.
poskytnout další kontextuální informace o daném oboru.
- :guilabel:`Výchozí hodnota“: přidat vzorový vstupní řetězec.
- :guilabel:`Výchozí hodnota“: přidejte běžné použití, které by většina zákazníků považovala za užitečné.
Příkladem může být například zadání informací, které zákazníci mají uvést, aby bylo snadnější
vyřešit svůj problém, například číslo účtu nebo číslo produktu.
- :guilabel:`Povinné pole“: určuje, zda je nutné označit pole jako povinné.
je třeba odevzdat. Přepněte přepínač z šedé barvy na modrou.
- :guilabel:`Zobrazitelnost“: umožňuje zobrazení pole v absolutním nebo podmíněném režimu.
například viditelnost zařízení se zobrazí při výběru určitých možností.
- :guilabel:`Animace“: zvolte, zda pole obsahuje animace.

.. obrázek: vydávání lístků/vydávání lístků webovou formou.png
:align:center
:alt: Pohled na neveřejnou webovou stránku pro podání žádosti o pomoc s Odoo Helpdeskem.

Jakmile je tvar optimalizován a připraven k veřejnému použití, klikněte na tlačítko „Uložit“, abyste aplikaci
změny. Poté zveřejněte formulář přepnutím přepínače „Nepublikováno“
:guilabel:`Zveřejněno“ nahoře na stránce, pokud je třeba.

Prioritizace lístků
====================

Všechny lístky obsahují pole Priority. Nejvyšší priorita se zobrazuje na začátku
Kanban a seznamy.

.. obrázek: vydávání lístků/vydávání lístků - priorita.png
:alt: Pohled na kanban týmu a prioritizované úkoly v Odoo Helpdesku.

Prioritní úrovně jsou reprezentovány hvězdičkami:

- 0 hvězdiček = *Nízká priorita*
- 1 hvězda = *Střední priorita*
- 2 hvězdičky = *Vysoká priorita*
- 3 hvězdičky = *Důležité*

Tikety jsou nastaveny na nízkou prioritu (0 hvězdiček) výchozím nastavením. Chcete-li změnit prioritní úroveň, vyberte
Vhodný počet hvězdiček na kanban kartě nebo v tiketu.

.. varování:
Priorita může být použita jako kritérium při přidělování :doc:`SLA <sla>`, což znamená, že prioritní úroveň
Úroveň lístku může měnit termín :abbr:`SLA (Service Level Agreement)“.

.. viz též:
   - :doc:`/aplikace/služby/helpdesk/pokročilé/uzavřít-tikety`
   - :doc:`../../../obecne/komunikace_e-mailem`
   - :/aplikace/weby/livechat
