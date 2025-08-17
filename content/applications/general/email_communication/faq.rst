====================================
Běžné problémy s e-mailováním a jejich řešení
====================================

Tato stránka uvádí nejčastější problémy s e-maily a jejich řešení.

..._email-issues-provider:

Odoo není poskytovatelem e-mailových služeb
=============================

Odoo nefunguje jako klasická schránka na e-maily, jako je například Gmail, Outlook nebo Yahoo.

Odoo používá e-maily jako způsob, jak informovat uživatele/zákazníky.
Není náhradou za specializovaný e-mailový server. Proto nemusí fungovat tak, jak byste očekávali
ve srovnání se standardní e-mailovou schránkou.

Hlavní rozdíly jsou následující:

- Výchozí nastavení je takové, že se oznámení nebo transakční e-mail (například citaci, fakturu, zprávu přímo klientovi)
(kontakt) je odeslán úspěšně, pak je objekt e-mailu smazán. Obsah zprávy žije dál
v souvislém záznamu. Zamezuje tak přeplnění databáze více kopiemi
obsah stejného e-mailu (když je odeslán více příjemcům), pokud obsah již existuje
v přepisech hovorů.
- Konceptu kopie pro slepé uživatele ([BCC]) v Odoo neexistuje. Odoo používá koncept „sledovaných“ uživatelů, kteří jsou přidáni
a automaticky rozhodnout, kdy a jak :ref:`kontakt bude informován.
nebo dostává kopii e-mailu.
- Příchozí e-maily se zpracovávají tím, že se zkontroluje, zda je e-mailová adresa v poli „Komu“ platná e-mailová adresa.
Odoo databáze nebo v případě odpovědního e-mailu, pokud je v hlavičce e-mailu uveden odkaz.
odpovídá zprávě, která byla zaslána ze serveru Odoo. Všechny ostatní e-maily budou vráceny a **nebudou**
a dočasně uložené v složce Spam nebo karantény. V jiných slovy každý e-mail nesouvisející s Odoo
Pokud je databáze ztracena.

..._e-mailové problémy odchozí:

Odeslané emaily
===============

..._email-výstupní administrativní adresa:

Změna e-mailové adresy účtu správce
----------------------------------------------------

Když je vytvořena databáze Odoo, hlavní administrátorský účet je přiřazen e-mailové adrese místopisného charakteru.
je doporučeno nahradit e-mailovou adresu pro správce za platnou e-mailovou adresu, aby se zabránilo odesílání
problémy s e-maily.

Pro to je na administrátorském účtu potřeba kliknout na ikonu uživatele a dále na „Můj profil“ (nebo
„Předvolby“), a aktualizujte pole „E-mail“ pod
Karta „Předvolby“. Můžete použít jiný e-mailový účet nebo použít svou doménu Odoo (např.
`soukromé_jméno@název_firmy.odoo.com“ a „admin“ pro lokalní část (např. „admin@název_firmy.odoo.com“).

..._email-issues-outgoing-delivery-failure

Nedodání zboží
----------------

Když je zpráva odeslána, objeví se ikonka „fa-envelope-o“ (obálka)
chvátání. Ikona se zbarví červeně, pokud doručení selhalo u alespoň jednoho příjemce.

.. obrázek: faq/red-envelope.png
:alt:Ikona červeného obálky zobrazená v okně chatu.

Klikněte na poštovní schránku pro zobrazení informací o dodání a pokud možno i příslušných
:ref:`chybové zprávy <e-mail-výstupní doručení - chybová hlášení>“.

.. obrázek: faq/doručení-selhalo.png
:alt:Příklad selhání odeslání.

Klikněte na tlačítko „Zobrazit podrobnosti o chybě“ a získáte další informace o důvodu selhání, pokud je Odoo
schopnost zpracovat původní chybu nebo odpověď e-mailu.

Klikněte na tlačítko „Odeslat a zavřít“ pro opakované odeslání e-mailu všem **zapnutým uživatelům**.
(:icon:`fa-toggle-on`) příjemce v sloupci „Zkuste znovu“. Všechny
(:icon:`fa-toggle-off`): adresáti budou ignorováni.

Klikněte na tlačítko „Zapomenout na všechny“ a ignorujte všechny e-maily, které v současné době selhaly.
červená do bílé.

Neslané e-maily se také zobrazují v pořadníku e-mailů Odoo. Chcete-li k němu přistupovat, zapněte režim vývojáře
Vývojářském režimu a přejděte do nabídky „Nastavení“ - „Technické“ - „E-mail: E-maily“.

.. obrázek: faq/technical-menu-email-delivery-failed.png
:alt: Příklad pohledu na technickou frontu e-mailů.

Nedoručené e-maily zobrazují stav „Doručeno nebylo“. Klikněte na tlačítko „Znovu“
neodeslaná zpráva se znovu objevila v poštovní frontě. Zobrazí se s :guilabel:`Odesláno“ stavem.
e-mail bude zaslán znovu, až se spustí plánovaná akce pro e-mailový front.

Volitelně můžete e-maily z fronty odeslat okamžitě kliknutím na „Odeslat nyní“.
:guilabel:`Zrušit e-mail“ k odstranění z fronty e-mailů.

.. poznámka::
Odeslané emaily jsou v čase občas vyprázdněny z fronty. Toto je kontrolováno pomocí funkce *Auto-Vacuum*.
schválená akce, která odstraňuje zbytečná data v databázi Odoo.

..._email-issues-outgoing-delivery-failure-messages:

Běžné chybové hlášení
~~~~~~~~~~~~~~~~~~~~~

.._email-issues-outgoing-delivery-failure-messages-limit:

Denní limit dosažen
*******************

.. obrázek:faq/email-limit.png
:alt:Váš emailový účet dosáhl maximální kapacity.

Odoo omezuje počet e-mailů, které lze odeslat z databáze Odoo Online. Většina poskytovatelů e-mailových služeb
poskytovatelé služeb (např. Google, Yahoo atd.) budou blokovat IP adresu serveru Odoo, pokud je e-mailový server Odoo
posílání příliš mnoha e-mailů na adresy, které neexistují nebo již nejsou platné.
Nepřizvané spamové e-maily zasílané prostřednictvím databáze Odoo.

Denní limit e-mailů se pohybuje mezi **5 a 200 e-maily**. Přesný limit závisí na
více faktorů (podléhající změnám):

- Typ předplatného databáze (jedna aplikace zdarma, zkušební verze, placené předplatné)
- Aplikace nainstalované (tj. Email Marketing, Marketing Automation)
- Pokud je migrace databáze v průběhu

Pokud je denní limit dosažen, můžete:

- Kontaktujte e-mailovou adresu „Odoo Support“ s žádostí o zvýšení limitu vaší schránky. Následující faktory
Budou brány v potaz:

  #Počet uživatelů v databázi
  #Aplikace nainstalované
  #. Odrazový poměr (procento e-mailových adres, které neobdržely e-maily kvůli tomu, že
vracené e-mailovým serverem na cestě k finálnímu příjemci.
  #Zda jsou správně nastaveny e-mailové aliasy a používají odpovídající vlastní domény
<email-outbound-alias-domain>.

.......tip:
Při použití vlastního doménového jména ověřte, že :ref:`SPF <email-domain-spf>`, :ref:`DKIM
<email-domain-dkim> a :ref:`DMARC <email-domain-dmarc>` jsou správně nastavené tak, aby
:ref:`E-mailové servery Odoo mohou zasílat e-maily na vaši vlastní doménu jménem
<email-outbound-custom-domain-odoo-server>.

- :doc:`Použijte externí odchozí e-mailový server <../email_communication> a nezávislost na Odoo.
omezení počtu e-mailů.
- Zkuste to znovu za den a pošlete e-mail znovu. K tomu aktivujte režim vývojáře
<developera-režimu>`, přejděte na: „Nastavení“ → „Technické“ → „E-mail: E-maily“ a klikněte
:guilabel:`Pokus o odeslání“ vedle neodeslané pošty.

.. důležité::
Denní limit e-mailů počítá každou zprávu odeslanou z vaší databáze Odoo, ať už manuálně
nebo automaticky. Výchozí nastavení je takové, že každá vnitřní zpráva, oznámení, poznámka atd. se počítá jako
e-mailu, pokud je o něm informován e-mailem. Toto lze zmírnit tím, že si necháte zasílat :ref:`upozornění
Odoo místo e-mailu.

..._email-issues-outgoing-delivery-failure-messages-smtp

Chyba SMTP
**********

„Základní protokol pro přenos pošty (SMTP)
„Snadný protokol pro přenos pošty“ je standard, který se používá k přenosu
e-maily mezi e-mailovými servery a/nebo klienty.

Pokud používáte externí SMTP server k odesílání e-mailů,
Standardní sada „chybových kódů SMTP“ existuje.
<https://cs.wikipedia.org/wiki/Seznam_kódů_vracení_serveru_pro_příjem_e-mailů#Běžné_stavy>
kódové číslo není specifické pro Odoo, přesný obsah chybové zprávy se může lišit podle e-mailu.
server k e-mailovému serveru.

.. příklad::
Permanentní chyba doručení e-mailu odeslaného na adresu sendgrid.com:

... kódový blok:: text

Doručení e-mailu se nezdařilo
Při doručování pošty došlo k chybě na serveru SMTP.
SMTPDataError: 550
Zadaná adresa odesílatele neodpovídá ověřené identitě odesilatele. E-mail nelze poslat, dokud se tato
problém vyřešen. Navštivte webovou stránku https://sendgrid.com/docs/for-developers/sending-email/sender-identity/.
aby viděli požadavky na identitu odesílatele.

Ve zprávě o chybě je uvedeno, že jste se pokusili odeslat e-mail z neověřené e-mailové adresy.
Zkontrolujte konfiguraci odchozího e-mailového serveru nebo výchozí adresu *ODESÍLATEL*.
Databáze je dobrým místem pro zjištění problému a ověření, že jste zařadili adresu na seznam povolených.
e-mailová adresa na stránkách sendgrid.com.

Obvykle stačí zadat obsah chybové hlášky do vyhledávače Google a získat tak informace o tom, co
a jak tento problém napravit.

Pokud se problém nevyřeší a dál se objevuje, kontaktujte:ref:`Odoo podporu
<e-mail-pro-podporu>.

..._email-issues-outgoing-delivery-failure-messages-no-error:

Žádný chybný výsledek nebyl zaznamenán.
******************

Odoo není schopen vždy poskytnout informace o důvodu, proč se dodávka nezdařila.
Poskytovatelé e-mailových služeb mají vlastní politiku ohledně odmítnutých e-mailů a není vždy možné pro Odoo
Přesně interpretovat.

Pokud je problém s jedním zákazníkem nebo doménou opakovaný, kontaktujte:ref:`Odoo
Podpora na e-mailu <email-issues-support>.

.. poznámka::
Jedním z nejčastějších důvodů, proč se e-mail nedoručí bez chybové hlášky, je související s
do konfigurace SPF nebo DKIM.
Zkontrolujte, zda je nastavení oznámení e-mailem přizpůsobeno vašim podnikatelským potřebám.
:dokumentace: „Komunikace v Odoo e-mailem“ pro více informací.
informace.

.._výkon odesílání e-mailů:

Výkonnost
--------------

Přesná doba odeslání e-mailu je vypočítána systémovou utilitou *cron* (plánovaný úkon), která může
může být použita k plánování úkolů, které budou automaticky spouštěny v předem stanovených intervalech. Odoo využívá tento přístup
posílat e-maily, které jsou považovány za „neaktuální“ (tj. formát zpravodajských zpráv, jako je masová pošta).
automatizace marketingu a událostí. To zabraňuje přeplnění poštovních serverů a naopak prioritizuje
individuální komunikace.

..spoiler::Co je to cron?

Króna je akce, kterou Odoo provádí v pozadí k tomu, aby spustilo konkrétní kód, který dokončuje
úkolu. Odoo také v některých pracovních postupech vytváří kronové spouštěče, které mohou vyvolat plánovaný úkon.
dříve, než je v plánu. Spouštění plánované akce ručně nebo změna její frekvence
Je obecně nedoporučováno, protože může vést k chybám nebo narušit specifické postupy.

Výchozí nastavení pro běžnou frontu pošty je provádět úlohu „:guilabel:`Mail: Email Queue Manager“ každých 60
minut. Nejnižší běhové interval pro cron je 5 minut. Odoo doporučuje interval 15
minuty na zajištění správného fungování. Pokud je interval příliš krátký, nemusí být zpracovány všechny e-maily
Které může způsobit, že cron vyprší.

E-maily, které jsou považovány za důležité (od jedné osoby k druhé, jako například objednávky nebo faktury).
objednávky apod.) jsou odesílány okamžitě. Nezobrazují se pod položkou „Nastavení“ v menu:
Technické --> E-mail:E-maily, pokud se jejich doručení nepodaří.

.. obrázek: faq/email-marketing-asap-notice.png
:alt:Příklad zaslání informačního hlavičkového řádku při frontě poštovní zásilky.

E-mailové kampaně jsou odesílány co nejdříve (po kliknutí na tlačítko :guilabel:`Odeslat`) nebo
čas, který je naplánován (po kliknutí na tlačítko :guilabel:`Schedule`).

Pro frontu e-mailového marketingu běží každý den kron „Mail Marketing: Process queue“.
ale bude automaticky spuštěna dříve, pokud je kampaň naplánovaná mimo tuto výchozí hodnotu.
frekvence. Pokud seznam obsahuje velké množství příjemců, spouštění cronu lze provést ručně
Je vícekrát nedoporučeno, protože nezrychlí zpracování a může
Vytvářet chyby.

.. tip::
Chcete-li upravovat crony, zapněte režim vývojáře a přejděte do
:menu: „Nastavení“ --> „Technické“ --> „Automatizace: Plánované akce“.

.. viz též:
Pro více informací o cronu při používání Odoo.sh se podívejte na :doc:`Odoo.sh časté technické
otázky <../../../administration/odoo_sh/advanced/frequent_technical_questions>.

..._výstupní čas emailu při kampaních:

E-mailová marketingová kampaň se zasekla v poštovní frontě
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pokud do fronty vložíte více e-mailových kampaní, budou zpracovány postupně.
podle data jejich vytvoření.

.. příklad::
Pokud jsou tři kampaně: Kampaň_1 (vytvořená 1. ledna), Kampaň_2 (vytvořená 2. ledna)
1. ledna, a kampaně Campaign_2 a Campaign_3 vytvořené 3. ledna se do fronty zařadí po kliknutí
:guilabel:`Odeslat“ na všechny tři z nich.

.... obrázek: faq/email-marketing-order-queue-example.png
:alt:Příklad tří e-mailových kampaní.

Cron se pokusí zpracovat kampaň 1, pak kampaň 2 a nakonec kampaň 3.
a začít zpracovávat kampaň 2, dokud nebude dokončena kampaň 1.

Pokud se e-mailová kampaň nikdy nedostane z fronty, může být problém v samotné kampani.
z fronty. Chceme-li problém vyřešit, můžeme kampaně 1 z fronty odebrat kliknutím na
:guilabel:"Zrušit" tlačítko a zkusit poslat obě kampaně. Pak bychom se mohli pokusit o opravu
Kampaň 1 nebo kontakt:ref:`Technická podpora Odoo <email-issues-support>`.

..._email-issues-incoming:

Příchozí e-maily
===============

Pokud je problém s příchozími e-maily, nemusí být v Odoo žádné zvláštní znamení.
je odesílací e-mailový klient, který se pokusí kontaktovat databázi, která obdrží zprávu o vracení.
Času: chybová zpráva „550: schránka nedostupná“).

.._email-issues-incoming-not-received:

E-mail nedorazil
---------------------

.. záložky::

... tab::Odoo online

Kontaktujte:ref:`Odoo podporu <email-issues-support>`, pokud se opakovaně vyskytuje stejný problém.
klient nebo doména.

.. tab:: Odoo.sh

Můžete používat databázové logy k pochopení a opravě problémů. Logy jsou uložená sbírka všech
úkoly dokončené v databázi. Jsou to pouze textová reprezentace, obsahující
časové razítko každé akce provedené na databázi Odoo. To může být užitečné při sledování e-mailů
odcházejí z databáze. Při neúspěšném odeslání můžete také vidět chyby v protokolu, pokud uvedou, že
se pokusil odeslat opakovaně. Záznamy ukazují každou akci na e-mailové servery z
databáze.

Živé logy jsou umístěny v adresáři ~/logs/ (přístupný z příkazové řádky nebo na webu).
Odoo.sh dashboard). Soubory protokolu jsou vytvářeny každý den ve 5:00 ráno (UTC).

.. tip::
Nejnovější dva soubory, pro aktuální den a předchozí, jsou pojmenovány
:soubor:odoo.log a :soubor:odoo.log.1.

Logovací soubory pro starší data jsou pojmenované podle jejich dat a komprimované. Použijte příkazy
:příkazu grep a příkazu zgrep (pro komprimované soubory).

... viz také:
Pro více informací o logu a jak se k němu dostat prostřednictvím panelu Odoo.sh, navštivte
:ref:`Dokumentace Odoo.sh o logování <odoosh/logs>.

Pro více informací o přístupu k logům pomocí příkazové řádky se podívejte na odkazovanou stránku :ref:`developer
dokumentace k logování <reference/cmdline/server/logging>.

..._podpora-e-mailu:

Informace pro podporu Odoo
============================

Tady je seznam užitečných informací, které byste měli zahrnout při kontaktování podpory Odoo.
<https://www.odoo.com/help>

#Export celého e-mailu z poštovní schránky. Tyto jsou obvykle ve formátu souborů .eml nebo .msg
obsahující technické informace potřebné pro vyšetřování. Proces stáhnutí je přesně popsán na
závisí na třetích stranách, které poskytují e-mailové služby.

......viz také::
      - „Centrum nápovědy Gmail: Sledování e-mailu s plným hlavičkovým řetězcem
<https://support.google.com/mail/answer/29436>
      - „Microsoft Support: Zobrazení hlaviček internetového e-mailu v aplikaci Outlook <https://support.microsoft.com/en-us/office/view-internet-message-headers-in-outlook-cd039382-dc6e-4264-ac74-c048563d212c#tab=Web>“

Při použití místního e-mailového softwaru (např. Thunderbird, Apple Mail, Outlook atd.) k synchronizaci
e-maily je obvykle možné exportovat místní kopie e-mailů jako soubory EML nebo MSG. Podívejte se na
pro další informace o používaném softwaru.

.......
Pokud je to možné, soubor EML/MSG by měl být založen na původním e-mailu, který byl odeslán.
selhal nebo způsobuje problémy.

Pro příchozí e-maily: pokud je to možné, kontaktujte původního odesilatele a požádejte o soubor EML/MSG.
kopie původního e-mailu. Posílání kopie původního e-mailu (předaného dál) obsahuje
částečné informace týkající se řešení problémů.

Pro **odchozí e-maily**: buď poskytněte soubor EML/MSG nebo uveďte, jaký záznam v databázi
databáze je postižena (např. číslo objednávky, jméno kontaktu, číslo faktury).
datum a čas, kdy byla e-mailová zpráva odeslána (např. e-mail byl odeslán v pondělí 10. ledna 2024 v 11:45 hodin středoevropského času
Evropského času).

#Vysvětlení přesného průběhu, který je nyní sledován pro běžný příjem těchto e-mailů v Odoo.
Zkuste odpovědět na následující otázky:

   - Je to upozornění na zprávu odpovědi v Odoo?
   - Je to zpráva odeslaná z databáze Odoo?
   - Je používán příchozí e-mailový server nebo je e-mail přesměrován/předáván
přes vlastní e-mailový server nebo poskytovatele?
   - Je nějaký příklad správně přeposlané zprávy?
   - Změnili jste někdy nastavení e-mailu? Pokud ano, zda po těchto změnách přestal fungovat?

#Odpověď na následující otázky:

   - Je to obecný problém nebo specifický pro konkrétní případ použití? Pokud je specifický pro konkrétní případ použití, který z nich?
   - Funguje tak, jak má? Pokud je e-mail odesílán pomocí Odoa, mělo by se dostat
databázi Odoo a zobrazit chybu :ref:`červenou obálku <email-issues-outgoing-delivery-failure>“.
