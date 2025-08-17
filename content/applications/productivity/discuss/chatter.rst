=======
Chatování
=======

.. |uživatel| nahradit za: :icon:`fa-user-o` :guilabel:`(uživatel)`
.. |paperclip| nahradit za :: :icon:`fa-paperclip` :guilabel:`(paperclip)`

Funkce Chatter je integrována po celém Odoo a usnadňuje komunikaci, udržuje
sledovatelnost a zodpovědnost mezi členy týmu. Okna chatu jsou známá jako *skladatelé*.
se nacházejí na téměř každém záznamu v databázi a umožňují uživatelům komunikovat s oběma.
interní uživatelé a externí kontakty.

Kompozéři Chatter umožňují uživatelům zaznamenávat poznámky, nahrávat soubory a plánovat aktivity.

Diskusní vlákno
==============

Na většině stránek databáze se nachází vlákno „*chatter thread*“, které slouží jako záznam o aktualizacích.
a editace záznamu. Při změně je vložena poznámka do konverzace.
obsahuje podrobnosti o změně a časové razítko.

Příklad:
Uživatel Mitchell Admin potřebuje aktualizovat e-mailovou adresu kontaktu. Po uložení
změny v kontaktním záznamu, do chatu kontaktního záznamu je zaznamenána poznámka
Následující informace:

   - Datum, kdy došlo ke změně.
   - E-mailová adresa tak, jak byla dříve uvedena.
   - Aktualizovaná e-mailová adresa.

.... obrázek: chatter/chatter-thread-email-update.png
:synchronizace: střed
:alt: Detailní pohled na konverzaci s aktualizací kontaktu.

Pokud byla vytvořena nebo upravena záznamová data z importovaného souboru nebo jinak aktualizována,
Zásah systému vytvoří v chatu poznámku a připíše k ní změnu.
OdooBot.

.. obrázek: chatter/odoo-bot-created.png
:align:center
:alt: Blízký pohled na konverzaci mezi uživatelem a robotem OdooBot vytvořenou kontaktní záznam.

...diskutovat/přidat fanoušky:

Přidejte si fanoušky
=============

„Sledovatel“ je uživatel nebo kontakt, který byl přidán do záznamu a informován, když se záznam změnil.
aktualizované na základě konkrétních nastavení odběru:
Příznivci se mohou sami přidat nebo je může přidat jiný uživatel.

.. poznámka::
Pokud uživatel vytvoří nebo je přiřazen k záznamu, automaticky se přidá jako sledovatel.

Pro sledování záznamu přejděte do jakéhokoliv záznamu s diskuzním vláknem. Například k otevření Helpdesku
vstupenku, přejděte na položku „Pomocná aplikace“ -> „Tikety“ -> „Všechny tikety“ a vyberte si vstupenku.
z seznamu otevřít.

V horním pravém rohu nad kompozérem chatu klikněte na „Sledovat“. Toto změní
tlačítko pro čtení „Sledovat“. Klikněte na něj znovu, abyste zrušili sledování.

Správa sledujících
----------------

Chcete-li přidat dalšího uživatele nebo kontakt jako sledovaného, klikněte na |uživatel|. To otevře seznam
současní následovníci. Klikněte na tlačítko „Přidat následovníky“ a otevře se okno „Získání následovníků“.
okno.

Vyberte jednu nebo více kontaktních osob z seznamu „Příjemci“ v rozevíracím seznamu.
Zatrhněte políčko „Odeslat upozornění“ a upravte šablonu zprávy podle svého uvážení. Pak klikněte
:guilabel:`Přidat fanoušky“.

Chcete-li odstranit své sledující, klikněte na uživatele a otevřete seznam současných sledovaných. Najděte jméno
odstranit a kliknout na ikonu „fa-remove“ (Odstranit)

.. diskutovat a upravit předplatné:

Sledovat editace
--------------------------

Obdržené aktualizace se mohou lišit v závislosti na nastavení předplatného uživatele.
aktualizace o příspěvku, který sleduje, a k úpravám seznamu přejděte na tlačítko |uživatel|.
Pokud chcete přidat odkaz na článek, který už je v seznamu, klikněte na ikonku :icon:`fa-pencil` :guilabel:`(pencil)` . To otevře
Pop-up okno „Upravit předplatné“ pro fanouška.

Seznam dostupných předplatných nastavení se liší podle typu záznamu. Například
Příznivce lístku Helpdesk může být informován, když je lístek ohodnocen. Tato možnost by nebyla
je k dispozici pro následovníky příležitosti CRM.

Zatrhněte políčko pro jakékoliv aktualizace, které by měl příjemce zprávy obdržet, a vyjměte zaškrtnutí u políčka pro odhlášení.
aktualizace, které by neměli dostávat. Klikněte na tlačítko „Použít“ po dokončení.

.. obrázek: chatter/chatter-edit-subscription.png
:align:center
:alt:Okno pro editaci předplatného na lístku Helpdesku.

Editace předplatného se liší podle typu záznamu. Tyto jsou možnosti pro
Tiket na helpdesku.

..._diskuse/poznámky do protokolu:

Záznamy o pohybu
=========

Funkce chatu zahrnuje možnost vkládat interní poznámky k jednotlivým záznamům. Tyto poznámky
jsou dostupné pouze pro interní uživatele a jsou k dispozici na jakémkoliv záznamu, který obsahuje chatovací okno.
nit.

Chcete-li zaznamenat interní poznámku, nejprve se přihlaste k záznamu. Například otevřete příležitost v CRM.
Přejděte na: „CRM aplikace -> Prodej -> Moje trubice“ a klikněte na kartu Kanban.
možnost otevřít ji. Pak v horním pravém rohu nad komponovaným chodem klikněte na :guilabel:`Log
poznámka.

Zadejte poznámku do kompozéru chatů. K označení interního uživatele zadejte @ a začněte psát jeho jméno
osoby, kterou chcete označit. Pak vyberte jméno z rozevírací nabídky. Podle nastavení
Nastavení, uživatel je informován e-mailem nebo prostřednictvím Odoo.

.. důležité:
Kontakty mimo firmu lze také označit v interním záznamu. Kontakt pak dostane e-mail
s obsahem poznámky, ke které jsou označeny, včetně příloh přidávaných přímo k
poznámku. Pokud na e-mail odpoví, jejich odpověď se zaznamená do chatu a oni jsou
Byla přidána do záznamu jako následovník.

Vnější kontakty nemohou vidět celý průběh konverzace a mohou se do ní pouze zapojit.
budou informováni o konkrétních aktualizacích na základě jejich nastavení „Sledování“
<discuss/edit-subscription> nebo když jsou přímo označeny.

...diskutovat, posílat zprávy:

Odesílejte zprávy
=============

Kompozéři mohou posílat zprávy svým kontaktům mimo databázi bez nutnosti opustit databázi.
otevřít jinou aplikaci. To usnadňuje komunikaci s potenciálními zákazníky
Aplikace pro obchod a řízení vztahů se zákazníky nebo dodavatelé v aplikaci „Nákup“.

Chcete-li poslat zprávu, nejdříve se přesuňte do záznamu. Například chcete-li poslat zprávu ze záznamu v CRM
možnost, přejít na: menu „CRM aplikace“ -> „Prodej“ -> „Moje trubice“, a kliknout na Kanban
kartu příležitosti k otevření. Poté v horním pravém rohu nad kompozicí chatů klikněte
:guilabel:`Odeslat zprávu“.

..tip:
Stiskněte klávesovou zkratku Ctrl+Enter pro odeslání zprávy, namísto tlačítka „Odeslat“.

Pokud nějaké následovníky bylo přidáno do záznamu, jsou přidány jako
adresáti zprávy.

.. varování:
:ref:`Sledovatelé <discuss/add-followers>` záznamu jsou přidáni jako příjemci zprávy
automaticky. Pokud by měl uživatel zprávu nedostat, musí být odhlášen jako sledující.
před odesláním zprávy nebo poznámky.

.. obrázek: chatter/send-message-followers.png
:align:center
:alt:Kompozitní chatovací programátor, který se připravuje na odeslání zprávy příznivcům příležitosti v oblasti řízení vztahů se zákazníky.
zákazník uvedený v záznamu příležitosti.

Zobrazit celého skladatele
--------------------

Skladatel chatu může být rozšířen na větší okno s možností dalších
Přizpůsobení.

Pro otevření celého skladatele klikněte na ikonu „fa-expand“ v pravém dolním rohu
kompozičního okna.

.. obrázek: chatter/chatter-expand-icon.png
:align:center
:alt:Kompozice s důrazem na rozbalovací ikonu.

Rozbalovací ikona v kompozéru chatu.

Tímto se otevře okno „Sestavit e-mail“. Potvrďte nebo upravte záměrné
Příjemcům zprávy nebo přidat další příjemce. V poli „Předmět“
automaticky vyplňuje podle názvu alba, ale lze ji upravit dle potřeby.

Pro zaslání zprávy použijte emailový vzor: doc:email_template
z roletky v poli „Nahrát šablonu“.

.. poznámka::
Počet a typ šablon se liší podle záznamu, ze kterého je zpráva vytvářena.

Klikněte na ikonu „Papírový uzávěr“ (papír s uzavřeným okrajem) a přidejte do zprávy jakékoliv soubory. Pak klikněte
:label:Odeslat.

.. obrázek: chatter/chatter-full-composer.png
:align:center
:alt: Rozšířený plný chat v aplikaci CRM.

Edit odeslala zprávy
------------------

Zprávy lze po odeslání upravit, aby se opravily chyby, byly opraveny nesrovnalosti nebo doplněny chybějící části.
informace.

.. poznámka::
Pokud jsou zprávy upravovány po odeslání, není zaslána aktualizovaná zpráva.
adresát.

Pro editaci odeslané zprávy klikněte na ikonu „:icon:`fa-ellipsis-h` :guilabel:`(ellipsis)`“ v
právo zprávy. Pak vyberte možnost „Upravit“. Upravte zprávu podle potřeby.

.. obrázek: chatter/chatter-edit.png
:align:center
:alt:Možnost zprávy v diskuzním vlákně.

Pro uložení změn stiskněte klávesovou zkratku :command:`Ctrl + Enter`, pro odmítnutí změn stiskněte klávesovou zkratku :command:`Escape`.

.. důležité:
Uživatelé s právy správce mohou upravovat jakýkoliv odeslaný příspěvek. Uživatelé bez práv správce nemohou
**pouze** upravovat zprávy, které vytvořili.

..._diskutovat/hledat zprávy:

Hledat zprávy
===============

Diskuse mohou být po čase dlouhé kvůli všemu obsahu, který v nich je.
je snazší najít konkrétní záznam, uživatelé mohou vyhledávat text zpráv a poznámek pro specifické
klíčová slova.

Nejprve vyberte záznam s diskuzním vláknem. Například pro hledání příležitosti CRM přejděte
:menuselection:„Aplikace CRM --> Prodej --> Můj potrubí“ a klikněte na kartu Kanban
možnost otevřít ji. Poté klikněte na
:icon:`oi-search` :guilabel:`(hledání)` ikonu pro otevření vyhledávací lišty.

Zadejte klíčové slovo nebo frázi do vyhledávacího pole, stiskněte klávesu „Enter“ nebo klikněte na
Ikona „Oi-hledání“ vedle vyhledávací lišty.
obsahující zadané klíčové slovo nebo frázi jsou uvedeny pod vyhledávacím polem s tímto klíčovým slovem.
vyzdvihnout.

Chcete-li se přímo dostat k určitému zprávě v konverzaci, přejeďte kurzorem nahoru a doleva.
koutku výsledku odhalit tlačítko „Skok“. Po kliknutí na toto tlačítko se dostanete na
umístění zprávy v konverzaci.

.. obrázek: chatter/chatter-search.png
:align:center
:alt:Výsledky vyhledávání v konverzaci zvýrazňují ikonu pro vyhledávání a tlačítko pro skok.

Výsledky vyhledávání v konverzaci. Po najetí myší na horní pravou část výsledku se zobrazí
Volba Skok. Po kliknutí se přesune přímo na tuto zprávu v konverzaci.

...diskutovat o plánování aktivit:

Zařazujte aktivity
===================

Aktivita je následná činnost spojená s záznamem v databázi Odoo. Aktivitu lze naplánovat
v jakémkoliv databázovém záznamu, který obsahuje vlákno chatu, kanbanové zobrazení, seznam nebo aktivitu.
žádost.

K naplánování aktivity přes konverzaci klikněte na tlačítko „Aktivita“, které se nachází
na vrcholu všech konverzací v jakémkoli záznamu. Na okně s náhledem :guilabel:`Schedule Activity`
zobrazí se pole „Typ aktivity“, vyberte si z nabídky.

..tip:
Každá aplikace má seznam typů aktivit, které jsou určeny pro tuto konkrétní aplikaci.
například pro zobrazení a úpravu aktivit dostupných v aplikaci CRM přejděte na
:menu:„CRM aplikace --> Konfigurace --> Typy aktivit“.

Do pole „Shrnutí“ v sekci „Záznamy“ zadejte název aktivity.
Pop-up okno s aktivitou.

Vyberte jméno z rozevírací nabídky „Přiřazeno“ v poli „Guilabel“ a přidejte aktivitu někomu jinému.
uživatel. Jinak je automaticky přiřazen uživatel vytvářící aktivitu.

Přidejte další informace do volitelného pole „Záznam...“ (guilabel).

.. poznámka::
Pole „Datum splatnosti“ na okně „Aktivita v rozvrhu“ se automaticky vyplní
na základě konfiguračních nastavení pro vybraný typ aktivity.
Datum lze změnit výběrem data v kalendáři v poli „Termín splatnosti“.

Začněte kliknutím na jedno z následujících tlačítek:

- :guilabel:`Rozvrh“: přidává aktivitu pod :guilabel:`Plánované aktivity“.
- :guilabel:`Označit jako hotové“: přidává podrobnosti o aktivitě do chatu pod :guilabel:`Dnes“.
Aktivita není v plánu, automaticky je označena jako dokončená.
- :guilabel:`Dokončeno & Naplánovat další“ přidává úkol pod :guilabel:`Dnes“ označený jako dokončený a
Otevře nové okno aktivit.
- :guilabel:`Smazat“: odstraní všechny změny provedené v okně dialogu.

Na chatu se zaznamenávají plánované aktivity pod štítkem :guilabel:`Plánované aktivity`.
a jsou barevně kódovány podle data splatnosti.

- Ikony v červené barvě značí, že je nějaká aktivita zpožděná.
- Ikony žluté barvy značí aktivitu s termínem splatnosti na dnešní datum.
- Ikony v zelené barvě označují aktivity s termínem splatnosti v budoucnu.

.. obrázek: chatter/chatter-activity-icons.png
:align:center
:alt:Diskusní vlákno s plánovanými aktivitami se různými termíny splatnosti.

..tip:
Klikněte na ikonu „info“ vedle plánované aktivity, abyste zjistili
další podrobnosti.

.... obrázek: chatter/planned-activity-details.png
:synchronizace: střed
:alt: Podrobnější pohled na plánovanou aktivitu.

Po dokončení aktivity klikněte na tlačítko „Zaúčtovat“ pod záznamem aktivity v chatu.
Otevře okno „Dokončeno“, kde lze k aktivitě přidat další poznámky.
a po zadání případných komentářů klikněte na tlačítko „Dokončit a naplánovat další“.
:guilabel:`Hotovo“, nebo :guilabel:"Vyhodit".

Po označení aktivity jako dokončené se vytvoří záznam s typem aktivity, názvem a dalšími podrobnostmi.
se zobrazí v okně připomenutí.

.. obrázek: chatter/chatter-dokončená aktivita.png
:align:center
:alt:Diskusní vlákno s dokončenou aktivitou obsahovalo další podrobnosti.

...diskutovat/připojit soubory:

Připojit soubory
============

Soubory lze připojit jako přílohy do chatu, a to buď k zaslání s zprávami nebo včetně
rekord.

.. poznámka::
Po přidání souboru do vlákna konverzace může být tento soubor stáhnutý uživatelem s přístupem k
vložka. Klikněte na vložku, pokud je potřeba, abyste zobrazili hlavičku souboru. Pak klikněte na
:icon:`fa-download` :guilabel:`(stáhnout soubor)` ikonu ke stažení souboru.

K připojení souboru klikněte na ikonu |papír| v horní části kompozice zprávy u jakéhokoliv záznamu.
obsahující vlákno diskuze.

Otevře se okno s prohlížečem souborů. Vyhledejte požadovaný soubor, vyberte ho a pak klikněte
:guilabel:`Otevřít“ a přidat ji do záznamu. Alternativně lze soubory rovnou přetáhnout
do diskuzního vlákna.

Po přidání souborů jsou zobrazeny v proudu konverzace pod nadpisem „Soubory“.
hlavička.

.. poznámka::
Po přidání alespoň jednoho souboru do záznamu chatu se objeví nová tlačítka s názvem
:guilabel:`Připojit soubory“ se zobrazí pod nadpisem „Soubory“. Chcete-li připojit další
soubory, je tlačítko, které **musíte** použít namísto ikony |papír| nahoře nad seznamem.
chaty.

Po zobrazení nadpisu „Soubory“ se v příspěvku objeví ikona |paperclip|.
delší dobu otevírá okno prohlížeče souborů. Kliknutím na |papírková sponka| se místo toho zobrazí
:guilabel:`Soubory“ v části „Komunikace“.

.... obrázek: chatter/chatter-attach-files.png
:synchronizace: střed
:alt:Diskuse s přílohou a tlačítkem Připojit soubory.

..._diskutovat o integraci:

Integrace
============

Kromě základních funkcí lze zapnout další integrace, které umožní práci s chatterem
funkce, konkrétně WhatsApp a Google Translate.

.. důležité:
Než se může chatovací aplikace připojit k aplikaci WhatsApp a Google Translate,
**musí být konfigurována. Postupné pokyny, jak nastavit každou z těchto funkcí, najdete v
jsou uvedeny v dokumentaci níže:

   - :doc:`WhatsApp <../whatsapp>`
   - :doc:`Překladač Google <../../general/integrations/google_translate>`

WhatsApp
--------

Aplikace WhatsApp je aplikací pro okamžitou zprávu a hlasovou komunikaci prostřednictvím IP, která umožňuje uživatelům odesílat a přijímat
posílat zprávy i sdílet obsah.

.. varování:
Aplikace WhatsApp je aplikací pro Odoo Enterprise, která **nefunguje** v komunitě Odoo.
edice. Chcete-li se přihlásit k odběru verze Odoo Enterprise, přejděte sem: „Zkušební verze Odoo
<https://www.odoo.com/trial>.

Po konfiguraci a zapnutí služby WhatsApp v databázi se zobrazí tlačítko WhatsApp.
přidána nad hovor skladatele na jakémkoli použitelném záznamu. Pokud jeden nebo více schválených WhatsApp
pro tento model jsou k dispozici šablony, po kliknutí na tlačítko se otevře dialogové okno pro odeslání zprávy přes WhatsApp.
Pop-up okno.

.. důležité:
*Šablony pro WhatsApp* musí být schváleny před jejich použitím. Viz:
pro více informací.

.. obrázek: chatter/whats-app-message.png
:align:center
:alt: Okno pro zaslání zprávy přes aplikaci WhatsApp.

Google překladač
----------------

Pomocí služby Google Translate lze překládat uživatelsky vytvořený text v chatu Odoo.

Pro zapnutí služby Google Translate na databázi musí být nejprve vytvořen klíč API.
přes Google API Konzoli
<https://console.developers.google.com/>`.

Po vytvoření API klíče přejděte do aplikace „Nastavení“ - „Diskuse“.
Vložte klíč do pole „Překlad zprávy“ a klikněte na tlačítko „Uložit“.
změny.

Přeložte zprávu ze služby chatování
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro překlad uživatelského textu z jiného jazyka klikněte na ikonku „fa-ellipsis-h“.
Klikněte na tlačítko „Přeložit“ v pravém podmenu vedle chatu.
obsah přeloží do jazyka, který je nastaven v předvolbách uživatele.
<../../obecne/useri/jazyk/>.

.. obrázek: chatter/chatter-translate-message.png
:align:center
:alt: Alternativní text

.. důležité:
Používání služby Google Translate vyžaduje aktuální účet na fakturaci u společnosti Google.
<https://moje-ucet.google.com/>`.

.. viz též:
   - :doc:`Diskuse <../discuss>`
   - :doc:`Diskuse kanály <../discuss/team_communication/>“
   - :doc:`Aktivita <../../essentials/activities>`
   - :doc:`WhatsApp <../whatsapp>`
