Zobrazit obsah

=========
Chat
=========

Odoo **Live Chat** umožňuje uživatelům komunikovat s návštěvníky webu v reálném čase. S **Live
Chat**, lze kvalifikovat potenciál prodeje, na dotazy ohledně podpory lze odpovědět v reálném čase.
Čas a problémy mohou být směřovány na příslušný tým pro další vyšetřování nebo pokračování.
„Živý chat“ také umožňuje okamžitou zpětnou vazbu od zákazníků.

Zapnout živý chat
================

Aplikace Live Chat lze nainstalovat několika způsoby:

- Přejděte do aplikace „Aplikace“, vyhledejte Live Chat a klikněte na „Instalovat“.
- Přejděte do seznamu zobrazení „Nápověda - aplikace Helpdesk --> Konfigurace - Týmy“ a vyberte
tým a na stránce nastavení týmu klikněte na zaškrtávací políčko vedle:guilabel:`Chat v reálném čase`, pod
:guilabel:`Kanály“ sekce.
- V aplikaci „Webová stránka“ přejděte do sekce „Nastavení – Nastavení“, posuňte se dolů
v sekci „E-mail a marketing“, zaškrtněte políčko vedle „Chat“ a klikněte
:guilabel:`Uložit“.

.... obrázek::livechat/enable-setting.png
:alt: Zobrazení stránky nastavení a funkce živého chatu pro Odoo Live Chat.

.. poznámka::
Po instalaci aplikace **Live Chat** se vytvoří kanál pro živý chat, který je ve výchozím nastavení.

Vytvořte živé kanály chatu
=========================

Pro vytvoření nového chatu s živým operátorem přejděte do aplikace „Živý chat“ a klikněte
:guilabel:`Nový“ k otevření prázdného formuláře pro novou kanálu. Zadejte název nové kanály do
:guilabel:`Název kanálu“ pole.

Konfigurace zbývajících záložek na formuláři s podrobnostmi o kanálu (:ref:`Operátory
<livechat/operators-tab>`, :ref:`Možnosti <livechat/options-tab>`, :ref:`Pravidla kanálu
<livechat/channel-rules-tab>“ a „Widget <livechat/widget-tab>“, postupujte podle následujících kroků.

.. obrázek: livechat/open-channel.png
:alt: Pohled na živý chatový kanál pro Odoo Live Chat.

..tip:
Formulář pro podrobné nastavení kanálu lze zobrazit kliknutím na tlačítko zpět v
:guilabel:`Website Live Chat Channels“ panelu, přes „krokové informace“. Najděte kartu Kanban pro
přesný chatovací kanál, přejeďte na něj kurzorem a pak klikněte na ikonku :icon:`fa-ellipsis-v`
:guilabel:`(vertikální elipsa)` ikonu pro otevření nabídky. Klikněte na :guilabel:`Nastavení
Klikněte na tlačítko „Channel“ a otevře se podrobné okno s informacemi o kanálu.

.._livechat/operator-tab:

Operátorské klávesy
-------------

„Provozovatelé“ jsou uživatelé, kteří pracují jako agenti a reagují na žádosti o chatu v reálném čase od zákazníků.
uživatel je přidán jako operátor do živého chatu, může od návštěvníků webu dostávat zprávy
kdekoliv v databázi. Okna chatu se otevírají do spodního pravého rohu obrazovky.

.. obrázek: livechat/pop-up.png
:alt:Pop-up okno chatu v databázi Odoo.

V podrobnostech kanálu klikněte na záložku „Operátoři“. Uživatel, který původně kanál vytvořil
do výchozího nastavení byl přidán kanál živého chatu.

.. poznámka::
Operátoři aktuálně používaní mohou být upraveni nebo odstraněni kliknutím na jejich příslušné políčko v
:guilabel:`Operátoři“ záložka, která odhaluje samostatné :guilabel:`Otevřeno: Operátory“ okno.
pop-up, upravte potřebné informace a pak klikněte na tlačítko „Uložit“ nebo klikněte
:guilabel:`Odebrat“ k odstranění daného operátora z kanálu.

Klikněte na tlačítko „Přidat“ a zobrazí se okno „Operátor Přidat“.

V okně přesunu se můžete posouvat dolů a hledat požadované uživatele nebo zadávat jejich jména do vyhledávací lišty. Pak
zaškrtněte políčko vedle uživatelů, kteří mají být přidáni, a poté stiskněte tlačítko :guilabel:`Vybrat“.

Noví operátoři lze vytvářet a přidávat přímo z okna tohoto typu, stejně jako
Klikněte na tlačítko „Nový“ a vyplňte formulář „Vytvořit operátory“. Jakmile
Ukončete a klikněte na „Uložit a zavřít“ nebo „Uložit a vytvořit nový záznam“, pokud chcete vytvořit více záznamů.

.. nebezpečí::
Vytvořením nového uživatele se může změnit stav předplatného Odoo, protože celkový počet uživatelů
Při vytváření nového uživatele buďte opatrní, protože počet záznamů v databázi se započítá do účtovací sazby.
Pokud uživatel již existuje, přidání jej jako operátora **nezmění** předplatné nebo
účtování za databázi.

.._livechat/options-tab:

Karta Možnosti
-----------

V záložce „Možnosti“ v podrobnostech o živém chatu je obrázek a text
nastavení okna chatu v reálném čase.

.. _livechat/livechat-button:

Tlačítko pro chat
~~~~~~~~~~~~~~~

Tlačítko Livechat je ikona, která se zobrazuje v pravém dolním rohu webové stránky.

Změňte text v poli „Oznámení“ na „Text oznámení“, abyste aktualizovali pozdrav zobrazovaný
textová bublina, která se objeví při zobrazení tlačítka pro živý chat na webu.

:guilabel:`Barva tlačítka živého chatu` změní barvu tlačítka živého chatu, jak se zobrazuje na
webové stránky. Chcete-li změnit barvu, klikněte na barevnou bublinu, aby se otevřel okno pro výběr barvy, pak
a táhněte kruh po barevné škále. Klikněte mimo okno výběru, jakmile bude hotovo.
Ikona „fa-refresh“ (reset) vedle barevných bublin.
barvy do výchozího výběru.

..tip:
Vybrat barvu pro tlačítko nebo hlavní panel lze ručně pomocí posuvníku nebo prostřednictvím barevného modelu RGB.
HSL nebo hexadecimální kód barvy z vyskakovacího okna pro výběr barvy, které se objeví při použití buď
kliknutím na barevné bubliny. V závislosti na operačním systému jsou k dispozici různé možnosti.
systém.

Příklad:
S těmito nastaveními se na webu zobrazí tlačítko pro online chatu takto:

   - :guilabel:`Text oznámení“: „Máte dotaz? Zeptejte se nás.“
   - :guilabel:`Barva tlačítka živého chatu“: nastavte na fialovou

.... obrázek: chat/tlačítko-chat.png
:alt: Pohled na webové stránky Odoo, které zdůrazňují tlačítko pro chat.

Okno chatu v reálném čase
~~~~~~~~~~~~~~~

Okno pro živý chat je prostor, kde se odehrává konverzace s návštěvníky webu.
se koná.

Upravte zprávu pro uvítání:guilabel: Welcome Message, abyste změnili zprávu, kterou návštěvník vidí při otevření nového chatu.
session. Tato zpráva vypadá jako odeslaná živým operátorem chatu a slouží jak k
pozdrav a pozvání k pokračování konverzace.

Upravte pole „Vstup do chatu“ v sekci „Položka pro vstup do chatu“.
napsat odpověď. Tato zpráva vyzývá návštěvníka, aby začal chodit.

Hlavička kanálu je barevná lišta na vrcholu okna chatu.
Barvu lze změnit stejným způsobem jako tlačítko „Chat“.
<livechat/livechat-button>.

.. obrázek:: livechat/chat-window.png
:alt:Okno chatu v reálném čase s modrým nadpisem kanálu a místo pro text.

Okno chatu v reálném čase s modrým nadpisem kanálu a místo textu „Řekni
„Něco...“

.. _livechat/channel-rules-tab:

Karta Pravidla kanálu
-----------------

Pro konfiguraci webové stránky, na které se zobrazí okno živého chatu, přejděte do části „Kanál“
V sekci „Pravidla“ na stránce s podrobnostmi o kanálu chatu v reálném čase.

Pro vytvoření nové pravidlo kanálu klikněte na tlačítko „Přidat řádek“. To otevře okno pro vytváření pravidel.
Pop-up okno.

.. obrázek:: livechat/create-rules.png
:alt: Příklad formuláře pro pravidla kanálu v Odoo Live Chatu.

Vytvořit nová pravidla
~~~~~~~~~~~~~~~~

Vyplňte pole v okně Create Rules podle pokynů níže a klikněte
:guilabel:`Uložit a zavřít“.

.. záložky::

....... tab::Tlačítko pro chat

Tlačítko pro chat je ikona, která se objevuje v pravém dolním rohu webu.
Vyberte si z následujících možností zobrazení:

      - :guilabel:`Zobrazit chaty“: zobrazuje tlačítko pro chat na stránce.
      - „Zobrazit s oznámením“: zobrazuje tlačítko chatu i plovoucí text
bublina vedle tlačítka.
      - „Otevřít automaticky“: zobrazí tlačítko a okno chatu se otevře automaticky
po určité době (určené v poli „Otevřít automaticky“
pole (které se zobrazí po výběru této možnosti).
      - :guilabel:`Skrýt chaty“: skryje tlačítko pro chat na stránce.

.. tab::Chatbot

Přidání chatbota do kanálu provedete tak, že si z nabídky vyberete „Chatbot“.
v nabídce. Pokud by měl být chatbot aktivní pouze tehdy, když nejsou aktivní operátoři, zaškrtněte políčko s názvem
:guilabel:`Povoleno pouze v případě, že není definován operátor“.

:guilabel:`Povoleno pouze při výběru chatu s botem“ je viditelná **pouze** v případě, že je vybrán chatbot.
v poli Chatbot.

.. tab:: URL RegEx

Regulární výraz URL určuje, na jakých internetových stránkách by se tato pravidla měla používat.
:guilabel:`Regex pro URL stránky“ pole, zadejte relativní URL stránky, na které by se měl tlačítko chatu objevit.
se objevit.

Například pro aplikaci pravidla na adresu URL „https://mydatabse.odoo.com/shop“ zadejte „/shop“.
pole „Regex URL“.

Pro aplikaci pravidla na všechny stránky v databázi zadejte do pole „URL regulární výraz“ znaku /.
pole.

....... tab:: Automaticky otevřít časovač

Tento prvek určuje, jak dlouho stránka zůstane otevřená předtím, než se spustí chatu.
se otevře okno. Toto pole se objeví pouze tehdy, pokud je tlačítko pro živý chat v tomto pravidle
nastaveno na „Otevřít automaticky“.

... tab:: Země

Pokud by tento kanál měl být k dispozici pouze pro návštěvníky webu v konkrétních zemích, přidejte je sem.
do pole „Země“ (v případě nevyplnění se kanál dostupný všem).
návštěvníci webu bez ohledu na jejich umístění.

.. poznámka::
Pro sledování geografické polohy návštěvníků je nutné mít nainstalovaný modul GeoIP.
databáze. Tato funkce je ve výchozím nastavení nainstalována na všech databázích Odoo Online,
Databáze vyžadují další kroky v rámci nastavení.

.. _livechat/widget-tab:

Widgetová záložka
----------

V záložce „Widget“ na formuláři podrobností o živém chatu je kódový fragment, který lze vložit
pro externí, neodoo webové stránky. Tento kód lze přidat na webovou stránku pro poskytnutí přístupu do
chatové okno.

..tip:
Nástroj pro živý chat lze přidat na webové stránky vytvořené prostřednictvím Odoo kliknutím na
:menu_selection:`Webová aplikace --> Konfigurace --> Nastavení“. Pak přejděte na
:menuselection:`E-mail a marketing“ sekce. V poli „Kanál“ vyberte kanál
přidat na web. Klikněte na tlačítko „Uložit“ pro aplikaci změn.

Chcete-li přidat widget na webové stránky vytvořené na třetí straně, klikněte na první
Ikona „kopírovat“ (ikona „clipboard“) v záložce „Výstupy“ a vložit kód do
tagu „<head>“ na webové stránce.

Pro odeslání živého chatu zákazníkovi klikněte na druhé ikonu „fa-clipboard“
Ikona „Kopírovat“ na záložce „Záznam“. Tento odkaz může být zaslán přímo zákazníkovi.
Když na něj kliknou, jsou přesměrování do nového okna chatu.

.. obrázek: livechat/widget-code.png
:alt: Pohled na záložku widgetu pro živý chat v Odoo.

.. viz též:
   - :doc:`../produktivita/diskuse`
   - :doc:`livechat/odpovedi`
   - :doc:`livechat/hodnoceni`
   - :doc:`livechat/chatboty`
   - :doc:`livechat/participate`

.. toctree::


živý chat/hodnocení
živý chat/odpovědi
živý chat, chatboti
živé chaty/zprávy
živé chaty/účast
