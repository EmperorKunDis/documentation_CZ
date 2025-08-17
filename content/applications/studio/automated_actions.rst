Zobrazit obsah

================
Automatizace pravidel
================

Automatické pravidlo umožňuje spustit jednu nebo více předem definovaných akcí v reakci na specifický
spouštět například aktivitu při nastavení pole na konkrétní hodnotu nebo archivovat záznam po uplynutí určitého časového intervalu.
Po svém posledním updatu.

Při vytváření pravidla automatizace:
umožňují přidat podmínky, které musí být splněny pro spuštění automatické pravidlo, např. příležitost
musí být přiřazen konkrétnímu obchodníkovi nebo stav záznamu nesmí být
:guilabel:`Návrh“.

Pro vytvoření automatické pravidlo s Odoo Studio postupujte takto:

#:ref:`Otevřené studio <studio/access>“ a klikněte na „Automatizace“, pak na „Nový“.
#Nastavte automatizační pravidlo jasným, výstižným názvem, který určí jeho účel.
#Vyberte spoušť:ref:`<studio/automated-actions/trigger>`, a pokud je třeba, vyplňte
pole, která se na obrazovce zobrazují podle vybraného spouštěče.
#Klikněte na tlačítko „Přidat akci“ a poté vyberte typ
:ref:`akce <studia/automatizované akce/akce> a vyplňte pole, která se objeví na obrazovce
podle vašeho vybraného kroku.
#Klikněte na tlačítko „Uložit a zavřít“ nebo „Uložit a nový“.

Příklad:

Pro zajištění dalšího kontaktu s méně spokojenými klienty vytváří tato automatizace pravidlo pro vytvoření aktivity po uplynutí 3 měsíců.
po vytvoření prodejního příkazu pro klienty s nižším než 30% spokojeností.

.... obrázek:: automatizované akce/vytvořit podmínky aktivity.png
:alt: Příklad pravidla automatizace na modelech předplatného
:skalka: 80 %

..tip:
   - Použijte záložku „Poznámky“ k dokumentování účelu a fungování pravidel automatizace.
Zjednodušuje údržbu pravidel a usnadňuje spolupráci uživatelů.
   - Pro změnu cílového modelu zadaného pravidlem automatizace, přepněte modely
před kliknutím na Automations v Studio nebo aktivací vývojářského režimu
<developer-mode>`, vytvořit nebo upravit pravidlo automatizace a vybrat „Model“.
:guilabel:`Automatické pravidlo“ formulář.
   - Automatické pravidlo můžete vytvořit z jakékoliv fáze kanbanu kliknutím na ikonku „fa-cog“.
:guilabel:`(Nastavení)` ikona, která se objeví při přejetí myší nad názvem stádia Kanbanu.
výběrem Automace. V tomto případě je nastavené Trigger.
:guilabel:`Stage je nastaven na“ výchozí hodnotou, ale může být změněna, pokud je třeba.

.. obrázek: automatizované akce/automations-kanban.png
:alt:Vytvořit automatizaci z karty kanbanu

..._studio/automatizované akce/spouštěč:

Spoušť
=======

Pomocí :guilabel:`Triggeru` lze definovat, jaký typ události musí nastat pro automatizační pravidlo.
běžet. K dispozici jsou různé spouštěče, které závisí na modelu:
kategorií je celkem:

- :ref:`studio/automated-actions/trigger-values-updated“
- :ref:`studio/automated-actions/trigger-email-events`
- :ref:`studio/automated-actions/trigger-timing-conditions`
- :ref:`studio/automated-actions/trigger-custom`
- :ref:`studio/automated-actions/trigger-external`

.._studio/automatické akce/podmínky:

Přidávání podmínek
-----------------

Filtry domén vám umožňují určit, které záznamy by měla nebo neměla automatická pravidla cílit či vylučovat.
Účinné filtrování zvyšuje celkový výkon, protože se vyhne nepotřebnému zpracování záznamů.
nejsou dotčeny touto pravidlem.

..tip:
:ref:`Zapněte režim vývojáře <developer-mode> před vytvořením pravidla automatizace, abyste měli
Největší flexibilitu při přidávání filtrů domén.

Podle vybraného spouštěče lze definovat jednu nebo více podmínek, které musí záznam splňovat.
Před nebo po spouštěči.

- Značka :guilabel:`Před aktualizací domény` definuje podmínky, které musí záznam splňovat *před*
při spuštění události například musí být v záznamu nastaveno „Typ = Faktura zákazníkovi“ a „Stav = Odesláno“.

S aktivovaným režimem vývojáře klikněte na :guilabel:`Upravit doménu`.
pak: `Nový pravidlo`.

- Filtry „Přidat podmínky“ nebo v některých případech filtr „Aplikovat na“ definují podmínky.
účet musí být vytvořen po události spouštěče, například faktura zákazníka musí obsahovat „Zaplaceno“
Stav = Částečně uhrazeno.

S aktivovaným režimem vývojáře (pokud je potřeba) klikněte na :guilabel:`Přidat podmínky`.
nebo :guilabel:`Upravit doménu“, pokud je to vhodné, pak :guilabel:`Nová pravidla“.

Když se stane nějaký „spouštěč“ (např. platba za objednávku),
Přihlášený zákazník obdrží fakturu s aktualizovanými údaji. Automatická pravidla kontrolují definované podmínky a pouze
vykonává akci :ref:`<studio/automated-actions/action>`, pokud záznam splňuje tyto podmínky.

Příklad:
Pokud má být automatická akce spuštěna při prvním nastavení e-mailové adresy
výrazným rozdílem oproti úpravě e-mailové adresy na kontakt, který je fyzickou osobou.
společnost, použijte „E-mail není nastaven“ a „Společnost není nastavena“ jako :guilabel:`Před aktualizací
Doména „Domain“ a „E-mailová adresa je nastavena“ jako pole „Použít“.

.... obrázek: automatizované_akce/před_aktualizací_domény.png
:alt: Příklad spouštěče s před aktualizací

.. poznámka::
Při vytváření záznamu se nekontroluje pole „Před aktualizací domény“.

.._studio/automated-actions/trigger-values-updated:

Hodnoty aktualizovány
--------------

Spouštět automatické akce, když dojde k určitým změnám v databázi.
Tato kategorie se liší podle modelu a jsou založena na běžných změnách, jako je například přidání konkrétního štítku.
(např. úkolu) nebo nastavení hodnoty pole (např. pole „Uživatel“).

Zvolte spoušť, pak zadejte hodnotu, pokud je třeba.

.._studio/automated-actions/trigger-email-events:

E-mailové události
------------

Spouštět automatické akce při odesílání nebo přijímání e-mailů.

.._studio/automated-actions/trigger-timing-conditions:

Podmínky časování
-----------------

Spouštět automatické akce v určitém čase od data pole nebo od data vytvoření nebo aktualizace
zaznamenaného rekordu. Následující spouštěcí události jsou k dispozici:

- Založeno na datu pole: Akce se spustí před nebo po určitém časovém úseku.
datum vybraného pole s datem.
- :guilabel:Po vytvoření: Akce je spuštěna po určité době od vytvoření záznamu
Vytvořen a uložen.
- :guilabel:`Po poslední aktualizaci“: Akce se spustí po určité době od posledního
záznam je upraven a uložen.

Pak můžete definovat:

- :guilabel:`Zpoždění“: Zadejte počet minut, hodin, dní nebo měsíců.
Pokud je akce provedená před spouštěcím datem, zadejte záporné číslo. Pokud jste vybrali možnost „Založené na
Při spouštění události na poli datum musíte také vybrat pole datum, které se použije k určení zpoždění.

...... poznámka::
Výchozí nastavení je takové, že kontrolu časově spouštěných pravidel automatizace provádí každých 240 minut nebo každé 4
hodin. Tato frekvence je obvykle dostatečná pro zpoždění, jako jsou třeba 3 měsíce po datu objednávky
nebo 7 dní po poslední aktualizaci.

Pokud se zpoždění pohybuje pod hranicí ekvivalentu 2400 minut nebo 40 hodin, systém znovu vypočítá
frekvenci kontroly, aby se zajistilo, že budou zohledněny i jemnější časové odstupy, například hodinu před událostí
Datum a čas spuštění nebo třicet minut po vytvoření lze respektovat co nejvíce přesně.

Na obrazovce se zobrazuje zpráva o možném zpoždění po spuštění pravidla.

.. obrázek:: automatizované akce/spouštění zpožděného poselství.png
:alt:Zpráva o možném zpoždění po plánované popravě

Chcete-li zobrazit nebo ručně upravit frekvenci plánovače s aktivovaným režimem vývojáře
v režimu vývojáře, přejděte do sekce „Nastavení“ – „Technické“ – „Plánované akce“.
všechny plánované akce pro vaši databázi.

Do vyhledávacího pole zadejte Automation a v seznamu výsledků klikněte na položku:guilabel:Automation
Pravidla: zkontrolovat a provést. Pokud chcete, aktualizujte hodnotu pole :guilabel:`Spustit každých`.
Kdykoliv klikněte na tlačítko „Spustit ručně“ a manuálně spusťte plánovanou akci.

- Klikněte na „Přidat podmínku“ a zadejte podmínky, které mají být splněny.
Přijďte na pravidlo automatizace, aby se spustilo. Klikněte na tlačítko „Nový pravidlo“ a přidejte další podmínku.

Akce se provede, když dojde k prodlevě a podmínky budou splněny.

Příklad:
Chcete-li poslat připomínku e-mailem 30 minut před začátkem události v kalendáři, vyberte
:guilabel:`Start“ jako datumové pole pro :guilabel:`Spouštěč“ a nastavte
:guilabel:`Zpoždění“ na „-30“ :guilabel:`Minut“.

.... obrázek: automatizované akce/podmínky spouštění časování.png
:alt: Příklad spouštěče na základě data

..._studio/automated-actions/trigger-custom:

Obchodní zvyklost
------

Spouštět automatické akce:

- :guilabel:`Při uložení“: když je záznam uložen.
- :guilabel:`Při smazání“: když je záznam odstraněn.
- „Při změně v uživatelském rozhraní“: když je hodnota pole na :ref:`formuláři
Pokud je tato volba aktivní, můžete vidět formulář i před uložením záznamu.

Pro spouštěče „Na uložení“ a „Na změnu rozhraní uživatele“ musíte pak vybrat
Pole, které se mají použít k spuštění automatické pravidlo v poli „Když aktualizujete“.

.. varování:
Pokud není vybrána pole v poli „Když se aktualizuje“, automatická akce může být
Pro každý záznam se provádí vícekrát.

Pokud chcete, můžete také definovat další podmínky, které musí být splněny, aby se spustila automatická pravidla.
:guilabel:`Přihlásit se“.

Příklad:
Aby se automatická akce spustila při vytvoření záznamu, například když je nový kontakt
vytvořit, vyberte spouštěč „Při uložení“ (viz odkaz na níže) a použijte
„ID není nastaven“ jako „Před aktualizací domény“ a „ID je nastaven“ jako
:guilabel:`Použít na doméně.“ Ujistěte se, že je vybrána správná pole v :guilabel:`Kdy
pole aktualizace.

Když je nový kontakt uložen, automaticky mu je přiřazen identifikátor databáze, což vyvolá
pravidlo automatizace.

.... obrázek: automatizované akce/při uložení/vytvoření.png
:alt: Příklad spouštění akce při vytvoření záznamu

.. poznámka::
Trigger „Při změně uživatelského rozhraní“ lze používat jen s :ref:`Spouštěčem kódu
akce <studio/automated-actions/action-execute-code> a funguje pouze tehdy, když je provedena změna
ručně. Akce se nevykoná, pokud je pole změněno jinou automatickou pravidlem.

..._studio/automated-actions/trigger-external:

Externí
--------

Spouštět automatické akce na základě konkrétního události v externím systému nebo aplikaci pomocí
:doc:`webhook <automated_actions/webhooks>“.

Po konfiguraci webhooku v Odoo je vygenerován odkaz na webhook a cílová záznamová položka.
je definováno, musí být implementováno v externím systému.

.. varování:
Je **velmi doporučeno** konzultovat s vývojářem, architektem řešení nebo jiným technickým pracovníkem.
úlohu při rozhodování o použití webových smyček a během implementačního procesu. Pokud nebudou správně
Pokud jsou konfigurovány webové smyčky, mohou narušit databázi Odoo a trvat dlouhou dobu na obnovení.

.. obrázek: automatizované akce/webhook-update-record.png
:alt: Příklad spouštěče na základě data

.. poznámka::
Je také možné nastavit automatickou akci, která :ref:`odesílá data do systému externího systému'.
připojení webhook (studio/automated-actions/action-webhook) při každé události v databázi Odoo.

.. viz též:
:doc:`Dokumentace k webovým hlášením <automated_actions/webhooks>“

.._studia/automatizované akce/akce:

Akce
=======

Jakmile definujete spouštěcí podmínku automatické akce, klikněte
V sekci „Akce k provedení“ přidejte akci, kterou chcete spustit.

..tip:
Můžete definovat více akcí pro stejnou automatizační pravidlo. Výchozí nastavení říká, že se akce spouští
v pořadí, v jakém byly definovány.

To znamená například, že pokud definujete akci „Aktualizace záznamu“ a poté „Změnit záznam“,
:guilabel:`Odeslat e-mail“ akce, kde je v e-mailu odkaz na pole, které bylo aktualizováno.
použije aktualizované hodnoty. Pokud je však definována akce „Odeslat e-mail“ před
:guilabel:`Aktualizace záznamu“ akce, e-mail používá nastavené hodnoty před aktualizací záznamu.

K přesunu definovaných akcí do jiného pořadí klikněte na ikonku :icon:`oi-draggable` :guilabel:`(páčka pro přetahování)
ikona vedle akce a přetáhněte ji na požadované místo.

.._studio/automated-actions/action-update-record:

Aktualizace záznamu
-------------

Tato akce aktualizuje jedno ze souvisejících polí záznamu. Klikněte na pole „Aktualizovat“ a
Seznam otevřený, vyberte nebo vyhledejte pole, které chcete aktualizovat. Pokud je třeba, klikněte na
:icon:`oi-chevron-right` :guilabel:`(pravý znak vlevo od pole názvu)` vedle pole jména, abyste se dostali na seznam
souvisejících oborech.

Pokud jste vybrali pole :ref:`many2many <studio/fields/relational-fields-many2many>`, zvolte, jestli
pole musí být aktualizováno pomocí :guilabel:`Přidat`, :guilabel:`Odebrat“ nebo „Nastavit na“.
Vybranou hodnotu nebo pomocí volby „Odstranit ji“.

Příklad:
Pokud chcete, aby automatická akce odstranila značku z rekordu zákazníka, nastavte
:guilabel:`Aktualizovat“ pole na :guilabel:`Zákazník > Štítky“, vybrat „Odstraňování“, pak
Vyberte značku.

.... obrázek: automatizované akce/aktualizace štítků záznamu.png
:alt: Příklad aktivity Aktualizace záznamu

..tip:
Alternativně můžete také dynamicky nastavit pole záznamu pomocí kódu v Pythonu. Vyberte
Vyberte místo „Aktualizovat“ možnost „Výpočet“, zadejte kód, který se má použít pro výpočet
hodnota pole. Například pokud chcete, aby pravidlo automatizace vypočítalo vlastní hodnotu
:ref:`datumové pole <studio/fields/simple-fields-date-time>“ při nastavení prioritní úlohy na
„Vysoká“ (přidáním úkolu jako hlavní) můžete definovat spouštěč:guilabel:"Priorita je nastavena na"
Vyberte možnost „Vysoký“ a definujte akci „Aktualizace záznamu“ následovně:

.... obrázek: automatizované akce/aktualizace záznamu - počítač.png
:alt: Vypočítat vlastní pole datum/čas pomocí Pythonovského výrazu

.._studio/automated-actions/action-create-activity:

Vytvořit aktivitu
---------------

Tato akce slouží k naplánování nové aktivity spojené s daným záznamem. Vyberte:guilabel:`Aktivitu
Zadejte název, popis a zvolte datum, kdy chcete aktivitu provést.
v poli „Datum splatnosti“ a vyberte typ uživatele:

- Chcete-li vždy přiřadit aktivitu stejnému uživateli, vyberte možnost „Určitého uživatele“, pak přidejte
uživatel do pole „Odpovědný“ v poli :guilabel:`Responsible`;
- Pro cílení uživatele spojeného s rekordem dynamicky vyberte :guilabel:`Dynamický uživatel (založený na
a změnit pole „Uživatel“, pokud je nutné.

Příklad:
Po přeměně vedení na příležitost chcete automatickou akci nastavit tak, aby se uskutečnil hovor.
uživatel odpovědný za vedení. Chcete-li tak učinit, nastavte hodnotu atributu
:guilabel:`Volání“ a „Uživatelský typ“ na „Dynamický uživatel (na základě záznamu)“.

.... obrázek: automatizované akce/vytvořit aktivitu.png
:alt: Příklad aktivity Vytvořit

.._studio/automated-actions/action-send-email-sms:

Odeslat e-mail a odeslat SMS
-----------------------

Tyto akce se používají k odeslání e-mailu nebo SMS zprávy kontaktům spojeným s konkrétním záznamem.
Pro to vyberte nebo vytvořte šablonu e-mailu nebo SMS, pak
V poli „Odeslat e-mail jako“ nebo „Odeslat SMS jako“ vyberte, jak chcete odeslat
e-mail nebo SMS zprávu:

- „E-mail“: poslat zprávu e-mailem příjemcům „E-mail
Šablona.
- :label:Zpráva“: zveřejnit zprávu na albu a upozornit jeho fanoušky.
- :guilabel:`Poznámka“: poslat zprávu jako interní poznámku viditelnou pro vnitřní uživatele
chvilkové řeči.
- :guilabel:`SMS (bez poznámky)`: poslat zprávu jako SMS příjemcům
:guilabel:`Šablona SMS“.
- :guilabel:`SMS (s poznámkou)`: poslat zprávu jako SMS na příjemce
:guilabel:`Šablona SMS“ a zveřejněte ji jako interní poznámku v chatu.
- :guilabel:`Pouze poznámka“: zprávu odeslat pouze jako interní poznámku v chatu.

..._studio/automated-actions/action-send-whatsapp:

Odešlete zprávu přes WhatsApp.
-------------

.. důležité:
K automatickému odesílání zpráv v aplikaci WhatsApp je potřeba
:ref:`Pro WhatsApp musí být vytvořeny šablony <produktivita/whatsapp/šablony>.

Tato akce slouží k odeslání zprávy WhatsApp kontaktu, který je spojen s konkrétním záznamem.
Pro to vyberte vhodný šablonu WhatsApp z nabídky.

... _studio/automated-actions/action-add-remove-followers:

Přidat fanoušky a odebrat fanoušky
----------------------------------

Tato akce se používá k přihlášení/odhlášení stávajících kontaktů do/z rekordu.

..._studio/automated-actions/action-create-record:

Vytvořit záznam
-------------

Tato akce se používá k vytvoření nového záznamu na jakémkoliv modelu.

Vyberte požadovaný model v poli „Záznam, který chcete vytvořit“; obsahuje aktuální model.
výchozím nastavení. Zadejte jméno pro záznam a poté, pokud chcete vytvořit záznam,
další model, vyberte pole v poli „Odkaz“ k propojení záznamu
Začala vznik nového rekordu.

.. poznámka::
Seznam vybraný v souvislosti s políčkem „Odkaz“ obsahuje pouze jedno pole :ref:`one2many.
<studia/pole/vztahová pole jedno-málo> na aktuálním modelu, které jsou propojeny s
:ref:`poli typu many2one <studia/pole/relační-pole-many2one>“ na cílovém modelu.

..tip:
Můžete vytvořit další automatizační pravidlo s :ref:`studio/automated-actions/action-update-record`.
akce pro aktualizaci polí nového záznamu v případě potřeby. Například můžete použít
:guilabel:`Vytvořit záznam“ akci, která vytvoří novou úkol projektu a pak ji přiřadí k určitému
uživatel, který používá akci „Aktualizace záznamu“.

.._studio/automated-actions/action-execute-code:

Spustit kód
------------

.. důležité:
Pro automatizační pravidla, která vyžadují provedení:
<studia/automatizované akce/akce spustit kód>“, je třeba mít na paměti, že údržba vlastního kódu není
zahrnuty v cenovém plánu Standard nebo Custom a vyžadují další poplatky:
<sazby_standard>.

Toto je akce, která spouští kód v Pythonu. Můžete do ní zadat svůj kód na záložce „Kód“.
s následujícími proměnnými:

- `env`: prostředí, ve kterém je akce spuštěna
- `model`: model rekordu, na který je akce spouštěna; je prázdný záznamový set
- `záznam`: záznam, na kterém je spuštěna akce; může být neplatný
- `záznamy“: záznamový set všech záznamů, na které se akce spouští v režimu vícenásobných záznamů; to může být
zůstaly prázdné
- „čas“, „datum a čas“, „datum“, „časové pásmo“: užitečné knihovny v Pythonu
- `float_compare`: funkce pro porovnávání čísel s přesností
- `log(zpráva, úroveň='info')`: funkce pro zaznamenávání informací o ladění v ir.logging
stůl
- _logger.info(zpráva): Logger, který vypouští zprávy do protokolů serveru
- `UserError`: třída výjimky pro zobrazení upozornění uživateli
- „Příkaz“: příliš mnoho příkazů v prostoru jmen
- `akce = ...`: vrátit akci

..tip:
Veškeré dostupné proměnné jsou popsány jak v záložce „Kód“, tak i v záložce „Nápověda“.

.. viz též:
:doc:`Schopnosti Odoo v oblasti ORM <../../developer/reference/backend/orm>`

.._studio/automated-actions/action-webhook:

Odeslat webhookové oznámení
-------------------------

Toto je používáno k odeslání požadavku na API s metodou POST, který obsahuje hodnoty vybraných políček.
do webového konektoru, jehož URL je uvedeno v poli „URL“.

:guilabel:`Sample Payload` poskytuje náhled dat obsažených v požadavku pomocí náhodného
dat zaznamenaných nebo smyšlené, pokud žádný záznam neexistuje.

.. poznámka::
Je také možné nastavit automatickou akci, která: doc:`přijímá data pomocí webového konektoru.
vnější systém (automatické akce / webové konektory), když dojde v tomto systému ke stanovené události.

..._studio/automated-actions/action-existing-actions:

Provedení stávajících akcí
------------------------

Tato akce spouští více akcí najednou (vázaných na aktuální model).
Proto klikněte na „Přidat řádek“ a v okně „Dodatečné akce dítěte“ vyberte
stávající akci nebo kliknutí: guilabel:"Nový" vytvořit novou.

.. toctree::


automatizované akce / webové události
