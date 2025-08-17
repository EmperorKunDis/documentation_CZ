========
Chatboti
========

Chatbot je program, který napodobuje konverzaci s živým člověkem. Chatboty jsou přiřazeny k
skript předem naplánovaných kroků, které jsou navrženy tak, aby se vyhnuly potenciálním chybám návštěvníka.
odpověď a vedou je stejným způsobem jako živý člen týmu.
by.

Chatboty lze přizpůsobit pro různé role, od podpory zákazníků, vytváření leadů až po
shromažďování kontaktních údajů. Cíl každého chatu může být různý podle několika kritérií,
včetně webové stránky, na které se nachází, a informací, které zachycuje.

.. obrázek: chatbots/chatbot-visitor-view.png
:alt: Pohled na okno chatu s otevřeným požadavkem v Odoo Live Chat.

Postavte si chatbota
===============

Před vytvořením nového chatbota musí být aplikace **Live Chat** nainstalována.
<všeobecné/instalace>.

Po instalaci aplikace **Live Chat** na databázi přejděte do sekce:
Chatovací aplikace --> Nastavení --> Chatboty.

.. poznámka::
Při instalaci aplikace **Live Chat** je vytvořen ukázkový chatbot s názvem *Welcome Bot*.
Chatbot má přednastavený scénář, který provede několik základních kroků, včetně požadavku na
e-mailovou adresu návštěvníka a přeposlání konverzace operátorovi.

Pro začátek lze použít uvítacího robota. Existující kroky lze upravit nebo odstranit.
Nové kroky lze přidat do skriptu podle potřeby.

Pokud je potřeba, můžete smazat nebo archivovat uvítacího robota.

.... obrázek: chatbots/chatbot-welcome-bot.png
:alt: Pohled na skript Welcome Bot v Odoo Live Chatu.

Pro vytvoření nového chatu přejděte na stránku „Chatbot“ (:menuselection:„Živý chat - aplikace“)
Konfigurace --> Chatboty“) a klikněte na „Nový“ pro otevření prázdné stránky s podrobnostmi o chatbotech.

Do pole „Jméno chatbota“ zadejte jméno a přejeďte myší nad obrázek vpravo. Klikněte na
ikonu „fa-papír“ (pencil) pro přidání fotografie.

Skripty chatbota
===============

Po vytvoření nového chatbota a jeho pojmenování je další krok vytvořit skript.
Každá konverzace je doprovázena scénářem, který obsahuje řadu hovorů. Každý z nich má
buď poskytnout nebo získat informace.

Pro vytvoření skriptu chatbota klikněte na tlačítko „Přidat řádek“ v záložce „Skript“.
stránce chatu s botem a okno „Vytvořit kroky skriptu“ se objeví. Tento formulář musí být
vyplněny pro každou řádek textu (dialog), který může během konverzace s uživatelem
konverzaci.

Nejprve zadejte obsah zprávy do pole :guilabel:`Zpráva`. Pak vyberte možnost
z políčka „Typ kroku“ a z roletky „Pouze pokud“.

Typy kroků
----------

Výběr typu kroku závisí na účelu zprávy. K dispozici je
Možnosti v rozevíracím seznamu „Typ kroku“ jsou uvedeny níže.

Text
~~~~

Tento krok se používá pro zprávy, u nichž není očekávaný nebo nutný odpovědní textový krok.
Pozdravit, nabídnout zdroje, jako jsou dokumentace nebo poskytnout odkazy na konkrétní webové stránky.

.. důležité:
Textové typy kroků jsou určeny pouze pro informování návštěvníků a neumožňují žádnou interakci.
Jejich cílem je získat informace a proto musí být následovány dalšími kroky, které pokračují v konverzaci.

Otázka
~~~~~~~~

Tento krok položí otázku a nabídne sadu odpovědí. Návštěvník klikne na jednu z odpovědí, která
buď vede k dalším krokům ve výměně informací nebo může vést na volitelný odkaz na novou webovou stránku.

Zadejte otázku do pole „Poznámka“. Pak pod nadpisem „Odpověď“
Klikněte na tlačítko „Přidat řádek“ a vytvořte prázdnou odpověď.

Pokračujte v zadávání odpovědi tak, jak by se měla návštěvníkovi zobrazit. Odpověď převeďte na odkaz
přesměruje návštěvníka na zvolenou adresu a přidá odkaz pod :guilabel:`Volitelné
Odkaz na hlavní stránku.

Tyto kroky opakujte pro každou odpověď, kterou chcete zařadit do otázky. Klikněte na tlačítko „Uložit a zavřít“.
nebo stiskněte klávesovou zkratku „Uložit a nový“.

..tip:
Přidání obecné odpovědi k jednotlivým otázkám (například „Něco jiného“) je užitečné.
Návštěvníci pokračují v konverzaci i když jejich potřeby neodpovídají žádné z ostatních odpovědí.

E-mail
~~~~~

Toto kroky vyzývá návštěvníky, aby poskytli svou e-mailovou adresu, která je uložena a může být použita týmem.
Členové později dodali další informace.

Tento typ kroku přijímá pouze e-mailové adresy ve správném formátu. Pokud
Když návštěvník zadá cokoli jiného než platnou e-mailovou adresu, robot odpoví
zprávu, ve které uvedla, že neuznává informace předložené.

.. obrázek: chatbots/chatbot-invalid-email.png
:alt: Pohled na chybující e-mailovou adresu, kterou odpovídá chatbot.

Telefon
~~~~~

Tento typ kroku je podobný e-mailu a vyzývá návštěvníka, aby zadal své telefonní číslo, které lze použít
Pokračovat v dalších informacích, naplánovat ukázky a podobně.

.. varování:
Vzhledem k velkému množství formátů telefonních čísel po celém světě se odpovědi na tento typ kroku
Není ověřován pro formátování a může obsahovat jak čísla, tak speciální znaky.

Další k Operátorovi
~~~~~~~~~~~~~~~~~~~

Tento krok přesměruje konverzaci na aktivního chataře živého chatu, aby mohl pokračovat
pomáhají návštěvníkovi. Díky tomu, že se konverzace zaznamenává, mohou operátoři později využít
kde skončil chatbot. To nejenom ušetří čas všem zúčastněným stranám, ale může také pomoci
kvalifikovat konverzace předtím, než se dostanou k živým operátorům.

.. poznámka::
Pokud není na kanálu aktivní operátor, chatbot pokračuje v konverzaci s
návštěvník. Proto by měly být k tomuto kroku přidány další, aby se zajistilo, že není
zásadní konec rozhovoru. Kroky navíc mohou návštěvníkům sdělit, že chybí
k dispozici operátoři (např. „Ach jo, vypadá to, že žádní naši operátoři nejsou k dispozici“).
pokračovat v konverzaci („Chcete mi nechat svou e-mailovou adresu?“).

.. obrázek:: chatbots/chatbot-bez-operátora.png
:alt:Viditelnost pokračování konverzace s chatbote, když není k dispozici živý operátor.

Volný vstup/víceřádkový
~~~~~~~~~~~~~~~~~~~~~

Krok „volného vstupu“ umožňuje návštěvníkům odpovídat na otázky bez předem připravených
odpovědi. Informace poskytnuté v těchto odpovědích jsou uloženy v přepisech chatu.

Vyberte mezi „Volný vstup“ a „Volný vstup (víceřádkový)“, podle typu
a množství informací, které návštěvník musí poskytnout.

Vytvořte lead
~~~~~~~~~~~

Tento krok vytvoří kontakt ve **CRM** aplikaci. Vyberte možnost z nabídky :guilabel:`Prodej
Položka týmu, která se objevuje při přidělování vytvořeného kontaktu konkrétnímu týmu.

.. poznámka::
Toto kroky je možné provést pouze v případě, že je aplikace CRM nainstalována na databázi.

Vytvořit lístek
~~~~~~~~~~~~~

Tento krok vytvoří „tiket“ (viz. stránka „Dokumentace“) na
Aplikace Helpdesk. Vyberte možnost z pole „Tým Helpdesku“.
Vypadá, že přiřazuje vytvořené požadavky ke konkrétnímu týmu.

.. poznámka::
Tento krok je dostupný pouze v případě, že je aplikace Helpdesk nainstalována na databázi.

..._livechat/chatboty/pouze-v-případě:

Pokud
-------

Skripty chatbota fungují na principu „pokud ano, pak ano“, což znamená, že návštěvníkovi je předložen další dotaz.
je určena odpovědí na předchozí otázku.

Pokračovat v pokroku konverzace lze pomocí formuláře „Vytvořit kroky skriptu“ pro nový
Každý krok obsahuje pole s názvem „Pouze pokud“. Toto pole je místo, kde se postupně zobrazují otázky
jsou definovány.

Pokud má být krok proveden na základě všech předchozích zpráv, může být pole prázdné.
Pokud by mělo být zpráva odeslána pouze podmíněně na základě předchozí reakce nebo více předchozích
odpovědi, tyto odpovědi musí být přidány do pole.

.. důležité:
Pokud je v poli „Výhradně“ vybráno nějaké zaškrtnutí, musí být všechna vybraná zaškrtnutí vybrána během
konverzace před touto fází zahrnuta. Pouze v tomto poli vyberte výběry, pokud jsou
aby se tento krok zobrazil.

Příklad:
Ve skriptu Welcome Bot může návštěvník požádat o informace o cenách. Pokud si návštěvník vybere
Tato odpověď obsahuje krok, který přepne konverzaci na operátora. Chatbot nejprve
posílá zprávu, která návštěvníka upozorňuje, že se snaží zjistit, jestli je operátor k dispozici.
pomáhat s informacemi o cenách.

Tato zpráva však měla být doručena pouze v případě, že si návštěvník vyžádal informace o cenách.
V takové situaci by pak probíhala konverzace následovně:

   - Vítejte, roboti: „*Co hledáte?*“
   - Návštěvník: „Mám dotaz ohledně cen.“
   - Vítejte v botovi: „*Hmmm, dovolte mi zkontrolovat, jestli bychom nenašli někoho, kdo by vám mohl pomoci s tímhle… *“

V detailním formuláři pro krok Text je odpověď *Mám dotaz na cenu*.
Byl vybrán v poli „Pouze pokud“. V takovém případě je tento krok zobrazen pouze ve hře.
kde byla tato odpověď vybrána.

.... obrázek:: chatbots/chatbot-only-if.png
:alt: Pohled na nové zprávy s důrazem na pole pouze pokud.

Testování skriptu
==============

Aby měl každý návštěvník uspokojivou zkušenost s chateboteem, musí být každá odeslaná zpráva
vedou k přirozenému závěru. Skripty chatbota by měly být testovány, aby se potvrdilo, že neexistují slepé uličky.
a pochopit, co vidí návštěvník, když se s chatbotem baví.

.. důležité:
Pokud návštěvník poskytne odpověď nebo vstup, který neodpovídá žádnému zadání,
Odpověď, konverzace se zastaví (končí *mrtvými konci*). Protože návštěvník nemůže znovu zapojit chytrého asistenta,
musí znovu zahájit konverzaci obnovením okna chatu nebo prohlížeče. Mohou také
Klikněte na ikonu „Obnovit“ (Refresh) v horní části okna zprávy.

.... obrázek:: chatbots/refresh-button.png
:alt: Tlačítko pro obnovení zprávy v horní části okna s přijatými zprávami.

Ikona „obnovení“ (:icon:`fa-refresh`) se objeví pouze tehdy, když skript chytrého asistenta dosáhl
slepá ulička.

Než začnete testovat chatbota, klikněte na tlačítko „Test“ v levém horním rohu.
stránku skriptu chytrého asistenta. Poté, co budete přesměrováni na testovací obrazovku, odpovězte na otázky chytrého asistenta
vyvolává stejné pocity, jako byste se na místě nacházeli vy sami.

Když se scénář dostal na konec, objeví se v dolní části zpráva *Konverzace ukončena...*
okna chatu. Chcete-li začít konverzaci na začátku skriptu, klikněte na
:ikonka „obnovení“ (refresh) v horním rohu okna zprávy.
Stránku skriptu klikněte na tlačítko „Přejít zpět do režimu editaci“ v horní části stránky.

Přidejte chatbota do kanálu
========================

Po vytvoření a otestování chatbota je potřeba jej přidat do živého chatu.

Nejprve otevřete aplikaci „Živý chat“, najděte kartu Kanban pro příslušný
chatovací kanál v reálném čase, přejeďte nad ním a klikněte na ikonu :icon:`fa-ellipsis-v`.
Klikněte na ikonu „(vertikální elipsa)“ a otevřete nabídku. Klikněte na „Nastavení kanálu“.
otevřít podrobné informace o kanálu.

.. poznámka::
Pro vytvoření nového chatu živě otevřete aplikaci :menuselection:`Live Chat` a klikněte
:guilabel:`Nový“. Další informace naleznete v dokumentaci „Živé chaty“ (viz „Živé chaty“).

Klikněte na záložku „Pravidla kanálu“ a poté otevřete existující pravidlo nebo vytvořte nové
kliknutím na „Přidat řádek“.

V okně „Vytvořit pravidla“ vyberte vhodný chatbot.
:guilabel:„Chatbot“ pole.

Pokud by měl být chatbot aktivní jen v případě, že nejsou k dispozici živí operátoři chatu, zaškrtněte políčko
označené jako:guilabel:`Povoleno pouze pro operátory`.

.. obrázek: chatbota/chatbot-přidat-do-kanálu.png
:alt: Pohled na pravidla kanálu s důrazem na poli chatbota.

.. viz též:
:doc:`Pravidla chatu v reálném čase </aplikace/weby/livechat>`
