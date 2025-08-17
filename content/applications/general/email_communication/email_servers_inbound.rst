=======================
Spravovat příchozí zprávy
=======================

Příchozí zpráva je e-mail doručený do databáze Odoo. Kdokoli může poslat e-mail na jakoukoli adresu
alias vytvořený v databázi nebo odpověď na e-mail, který byl dříve zaslán z databáze
v hlavičce odpovědi (Reply-To).

.._email-inbound-aliases:

E-mailové aliasy
=============

..._email-inbound-aliases-model:

Model specifické přezdívky
----------------------

Některé aplikace mají své specifické aliasy (týmy prodeje, týmy podpory, projekty atd.).
alias se používá k:

- Vytvořte rekord, když je e-mail zaslán přímo na alias.
- Získat odpovědi na e-mail, který byl původně zaslán z rekordu.

.. příklad::

.... obrázek: email_servers_inbound/sales-team-alias-config.png
:alt: Lokální část „info“ se používá jako přezdívka pro prodejní tým.

V následujícím příkladu odeslání e-mailu na adresu „info@company-name.odoo.com“ vytvoří
novou příležitost nebo nový kontakt automaticky přiřazený k odpovídajícímu obchodnímu týmu. Pokud je e-mail
je odeslána z chatu stávající příležitosti a v poli „Odpovědět“ se objeví
„info@soukroma-firma.odoo.com“. Odpověď bude zveřejněna v tom správném chatu podle
hlavička „Zpráva ID“.

.._email-inbound-aliases-catchall:

Přesměrování
--------

Pokud aplikace nemá alias, použije se univerzální náhradní alias: chytrý záchyt.
Odpověď odeslaná z chatu má nastavenou adresu pro odpovědi na tento alias. Odpověď zaslaná na tento alias
byl umístěn na správné konverzaci díky hlavičce *message-id*.

Výchozí hodnotou je místní část *catchall*. Aktivujte režim vývojáře a přejděte na
:menu:Nastavení --> Technické --> E-maily: Přesměrování domén

E-mail na adresu hromadného příjemce vždy musí být odpovědí na předchozí e-mail, který byl zaslán z databáze.
e-mail je zaslán přímo na hromadnou adresu a odesílatel obdrží následující zprávu:

.. obrázek: email_servers_inbound/direct-mail-to-catchall.png
:alt:E-mail o odrazu z „MAILER-DEAMON“, který vysvětluje, jak kontaktovat databázi.

.. poznámka::
E-mailová adresa info@company-name.com, která je zobrazena na obrázku výše, je e-mailovou adresou
na společnost. Při vstupu do režimu vývojáře na profilu společnosti se zobrazí další
Možnosti konfigurace (např. zachycení a odeslání zpět) se stávají čitelnými. Může být upraveno
kliknutím na interní odkaz e-mailové domény. Obvykle se nedoporučuje měnit
tohoto nastavení, pokud není specifická potřeba, protože ovlivní všechny odpovědi na předchozí zprávy
e-maily.

.. příklad::
Alias lze nastavit v týmu prodeje v aplikaci CRM. Když zákazník odpoví na e-mail
přicházející z aplikace CRM, je odpověď na adresu info@company-name.odoo.com.

Při odeslání e-mailu z aplikace Kontakty je adresa pro odpověď „catchall@company-name.odoo.com“.
protože na kontaktní modelu není přezdívka.

.. poznámka::
Je doporučeno nezměnit místní část přesměrování a odpovědi na chybu. Pokud je tato hodnota
upraveny, emaily odeslané z databáze budou mít stále původní hodnotu lokálního jména.
To může vést k tomu, že odpovědi nebudou správně přijaty v databázi.

..._email-inbound-aliases-bounce:

Bounce
------

Stejným způsobem je používán univerzální e-mailový alias k vytvoření adresy pro odpověď.
vytvořit cestu zpět pro e-mail. Cesta zpět se používá, pokud e-maily nemohou být doručeny na
příjemce a chyba se vrátí odesilateli.

Výchozí název bude *bounce*. Zapněte režim vývojáře a přejděte na
:menu:Nastavení --> Technické --> E-maily: Přesměrování domén

.. poznámka::
Na Odoo Online, když používáte výchozí e-mailový server, je adresa zpětného odkazu nutně
do hodnoty „bounce@company-name.odoo.com“ nezávisle na nastavené hodnotě jako alias pro vracení e-mailů.

Při chybě se zobrazí upozornění v červené obálce ve chatu.
V některých případech může červená obálka obsahovat pouze zprávu „bez chyby“, což znamená, že
Odoo nebylo schopno vyřešit.

Oznámení se zobrazí také v ikoně diskuze na liště s navigací.

.. obrázek: e-mailové servery vstupní/oznámení o chybě při odeslání e-mailu - navigační lišta.png
:alt:Při odeslání e-mailu kontaktu došlo k chybě, která se zobrazí na navigačním panelu.

.. příklad::
Pokud je e-mailová adresa příjemce nesprávná, klikněte na červenou poštovní schránku v
Pokud dojde k chybě, bude zobrazeno upozornění s důvodem selhání.

....... obrázek:email_servers_inbound/red-envelope-info.png
:alt: E-mail zaslaný na špatný doménový název vyvolá odpověď, která se zobrazí jako červená poštovní schránka.

.._email-inbound-default:

Přijímat e-maily s výchozím nastavením Odoo
================================================

Na Odoo Online a na Odoo.sh jsou přednastavené e-mailové aliasy, odpovědi a adresy pro vracení pošty.
Tyto adresy používají automaticky přidávaný doménový alias v databázi s běžným nastavením.

.. příklad::
Předpokládejme, že adresa databáze je „https://mydatabase.odoo.com“, pak doménové jméno
„mydatabase.odoo.com“ je automaticky vytvořen. Při zachycení a odrazu lze použít jejich adresu
Jejich e-mailové adresy jsou odpovídajícím způsobem „catchall@mydatabase.odoo.com“ a „bounce@mydatabase.odoo.com“.

Pokud je aplikace CRM nainstalována a vytvořen tým prodeje s přezdívkou „info“,
Adresa „info@mydatabase.odoo.com“ může být použita ihned. To samé platí pro jakoukoliv jinou alternativní adresu
vytvořené v jiných aplikacích.

Doména databáze je připravena k použití pro příjem e-mailů bez další konfigurace.

.._email-inbound-multiple-subdomains:

Používejte více poddomén Odoo
============================

Na webu **Odoo Online** je jedinou poddoménou Odoa ta definovaná při vytváření databáze.

Na serveru **Odoo.sh** je možné používat několik poddomén Odoo. V nastavení větve
další poddomény Odoo lze přidat, pokud nejsou používány v jiné pobočce.
domény pak musí být přidány jako alternativní domény, které může společnost používat.

.. obrázek: email_servers_inbound/vlastní_poddoména_sh.png
:alt:Nastavení odnože Odoo na větvi.

..._email-inbound-custom-domain:

Použijte vlastní doménu pro příchozí zprávy
========================================

Potřebujete vybrat doménu aliasu v obecných
Nastavení. Pokud máte více společností, musí být každá konfigurována.

.. obrázek: email_servers_inbound/alias-domain-settings.png
:alt: Alias doména v obecných nastaveních.

Všechny tyto přezdívky budou používat tento vlastní doménu. Odpovědi na modely, pro které je nastavená přezdívka
jsou odeslány na adresu [alias]@my-custom-domain.com. Odpovědi na ostatní modely jsou zasílány přes
`catchall@vase-zadana-domena.cz`.

.. obrázek: email_servers_inbound/diagram-mail-custom-domain.png
:alt:Technická schémata poštovního směru při použití vlastní domény v Odoo.

.. důležité::
Pokud jsou e-maily odesílány prostřednictvím serverů pro odesílání e-mailů společnosti Odoo při použití vlastního doménového jména, postupujte podle následujících pokynů:
:ref:`„Použití vlastního doménového jména s e-mailovým serverem Odoo“
<email-outbound-custom-domain-odoo-server>.

Vzhledem k tomu, že se používá vlastní doména, všechny e-maily odeslané z aliasu (odpovědi, odmítnutí a přímá komunikace)
jsou odeslány na adresu domény. Jsou tak doručeny e-mailovému serveru spojenému s doménou (záznam MX).
Pokud je chcete zobrazit v chatovacím okně nebo vytvořit nové záznamy, musíte je nejprve stáhnout.
e-maily v databázi Odoo.

.. seznam tabulkový::
:hlavičkové řádky: 1
:prázdné sloupky: 1

   * - Metoda
     - Výhody
     - Nevýhody
   * – Redukce:<ref>Emailové příchozí směrování na vlastní doménu</ref>
     - Nastavení je snadné a e-maily jsou zasílány přímo do databáze.
     - Každá databázová přezdívka musí být nakonfigurována.
   * – :ref:`Příchozí poštovní servery <email-inbound-custom-domain-incoming-server>“
     - Umožňuje uchovávat kopii e-mailu ve schránce (s IMAP).
Umožňuje vytvářet záznamy v zvoleném modelu.
     - Záleží na CRONu, což znamená, že e-maily nejsou ihned v databázi získány.
Každé jméno databáze musí být nakonfigurováno.
   * :-:ref:`Záznam MX <email-inbound-custom-domain-mx>
     - Pro správné fungování všech aliasů je nutné vytvořit pouze jednu záznamovou knihu.
     - Používání poddomény je nutné.
Požaduje pokročilé technické znalosti.

.. důležité::
Pro **databáze v prostředí firmy** je potřeba nastavit také přesměrování a záznamy MX.
:doc:`skriptu pro e-mailovou bránu <../../../../administration/on-premise/email_gateway>.
Protože tento skript vyžaduje **pokročilé technické a infrastrukturní znalosti**, je nutné jej spustit na počítači s vysokým výkonem.

.. důležité::
Podrobnější informace o tom, jak se s metodami zachází, najdete v dokumentaci vašeho poskytovatele.
podrobněji níže.

.._příchozí e-mailové adresy s vlastní doménou - přesměrování:

Přesměrování
------------

Pokud je databáze hostována na Odoo Online nebo Odoo.sh, doporučuje se používat přesměrování.
umožnit přijímání zpráv bez prodlení v databázi.

Je nutné přesměrovat všechny chybové a odpovědní e-maily na poddoménu databáze Odoo.
Každý další alternativní název by měl být také přesměrován.

.. příklad::
S jedním prodejním týmem jsou potřeba následující přesměrování:

   - `catchall@soukromefirma.cz` → `catchall@soukromefirma.odoo.cz`
   - `bounce@company-name.com` → `bounce@company-name.odoo.com`
   - `info@soukroma-firma.cz` → `info@soukroma-firma.odoo.cz`

.. důležité::
Někteří poskytovatelé požadují ověření přesměrování odesláním odkazu na cílovou e-mailovou adresu.
Tento postup je problém pro zachytávání a odraz, protože tyto nástroje se nepoužívají k vytváření záznamů.

   #Změňte výchozí hodnotu na doméně aliasového e-mailu.
se dostat k tomuto menu. Například může být změněna z „catchall“ na „temp-catchall“.
umožňuje používat „catchall“ jako lokalní část jiného aliasu.
   #Otevřete aplikaci, která používá přezdívku. Například CRM obsahuje přezdívky pro každý tým prodeje.
„chytí všechno“ jako lokalní část aliasu prodejního týmu.
   #Potvrzující e-mail vytvoří záznam v aplikaci CRM. E-mail, který byl odeslán, bude viditelný v
hovořit a ověřit tak přesměrování.
   #Nezapomeňte změnit alias prodejního týmu a hodnotu „vše“ v poště.
stejně jako před touto procedurou.

.. poznámka::
Alternativou k přesměrování je **předávání**. Při předávání se **adresa odesílatele
e-mailová zpráva bude identifikována jako odesílatel**, zatímco při přesměrování původní odesílatel
Vždy zůstane.

.._email-inbound-custom-domain-incoming-server:

Poštovní servery pro příchozí poštu
---------------------

Jako už bylo zmíněno, použití přesměrování je doporučovaným způsobem, jak získat e-maily v Odoo.
Na druhou stranu je možné nastavit příchozí poštovní servery. Tento způsob znamená vytvoření
server příchozí pošty pro každou schránku na vašem serveru, zachycené zprávy, odmítnuté e-maily a všechny aliasy
databáze, aby získal všechny příchozí e-maily. Příchozí poštovní servery vytvářejí tak, že se přes
:menu:Nastavení --> Technické --> E-maily: Příchozí poštovní servery“.

.. důležité::
Doporučujeme používat protokol IMAP před protokol POP, protože IMAP stahuje všechny nepřečtené e-maily.
POP stáhne všechny e-maily a jejich historii, poté je označí jako odstraněné ve vašem poštovním boxu.

.. tip::
Je také možné připojit poštu pomocí :doc:`Google Gmail s Google OAuth <google_oauth>`.
:doc:`Outlook s Microsoft Azure OAuth <azure_oauth>“.

Ať je zvolený protokol jakýkoli, e-maily jsou stahovány pomocí služby *Mail: Fetchmail Service*.
akce.

Další výhodou je možnost vytvářet nové záznamy pomocí příchozího poštovního serveru v Odoo.
určený model. Každý příchozí poštovní server může vytvářet záznamy podle různého modelu.

.. příklad::
Emaily doručené na adresu „task@company-name.com“ jsou získávány databází Odoo. Všechny emaily, které byly získány,
Vytvořit novou úlohu projektu v databázi.

.... obrázek:: e-mailové servery vstupní/příchozí poštovní server.png
:alt:Technická schémata poštovní trasy při použití vlastního doménového jména v Odoo.

.. _email-inbound-custom-domain-mx:

MX záznam
---------

Třetí možností je vytvořit záznam MX ve své zóně DNS, který specifikuje poštovní server, který spravuje
e-maily odeslané na váš doménu. **Pro pokročilou technickou znalost je nutná podpora.**

.. důležité::
Tato konfigurace funguje pouze s poddoménou na infrastruktuře Odoo Online nebo Odoo.sh
(@, např. @mail.mydomain.com)

Níže jsou uvedeny některé specifikace v závislosti na typu hostingu:

.. záložky::

...... skupina-tab::Odoo Online

Přidat musíte vlastní poddoménu do vašeho portálu.


... skupina-tab:: Odoo.sh

Přidat vlastní poddoménu je možné do nastavení projektu ve :doc:`settings.
<../../../administration/odoo_sh/getting_started/settings>

.. obrázek: email_servers_inbound/vlastni_subdomena_sh.png
:alt: Přidání vlastního poddoménového jména pro poštu do nastavení projektu Odoo.sh.

..._smyčky e-mailů vstupujících do firmy:

Neustálé smyčky v e-mailu
====================

V některých případech může dojít k nekonečnému smyku v e-mailovém odesílání. Odoo nabízí určitou ochranu proti takovým
smyčky, které zajišťují, že stejný odesílatel nemůže poslat příliš mnoho e-mailů **které by vytvořily záznamy** na alias.
Specifický časový úsek.

Základní e-mailová adresa může odeslat až 20 e-mailů za 120 minut. Pokud je odesláno více e-mailů,
blokovány a odesílatel dostane následující zprávu:

.. obrázek: email_servers_inbound/bounce-mail-loop.png
:alt:E-mailová zpráva o odrazu po pokusu o kontakt příliš mnohokrát s alternativním e-mailem.

Změnit výchozí chování lze tak, že zapnete :ref:`rozvojový režim`, poté se přesunete do :menuselection:`Nastavení
--> Technické --> Parametry: Parametry systému --> přidat dvě parametry.

- Pro první parametr zadejte klíč „mail.gateway.loop.minutes“ a vyberte
Počet minut, který je stejný jako hodnota :guilabel:`Value` (výchozí chování je 120).
- Pro druhý parametr zadejte klíč „mail.gateway.loop.threshold“ a vyberte
počet e-mailů jako hodnotu (výchozí chování je 20).

.. důležité::
Tyto parametry se používají jen k tomu, aby nedocházelo k vytváření nových záznamů. **Nepředchází
přidání odpovědí** do hovoru.

Povolit systémový parametr pro doménové jméno
===================================

Příchozí aliasy jsou nastaveny v databázi Odoo, aby bylo možné vytvářet záznamy na základě příchozích e-mailů.
Zobrazit aliasy nastavené v databázi Odoo, nejprve aktivujte režim vývojáře.
Poté přejděte na: „Nastavení aplikace --> Technické --> Zkratky“.

Následující systémový parametr „mail.catchall.domain.allowed“ nastavený s povolenou doménou aliasu
Hodnoty oddělené čárkami filtrují správně doručené e-maily adresované aliasům. Při nastavení domén
pro který může alias vytvářet případné požadavky, zakázky, příležitosti apod.
E-mailové adresy s pouze přívlastkem alias, nikoli doménou, jsou uvedeny.

V některých případech byly v databázi Odoo provedeny shody při přijetí e-mailu s
stejným předčíslím aliasu a odlišnou doménou v příchozí e-mailové adrese.
adresáta a e-mailové adresy uvedené v poli „Kopie“ příchozího e-mailu.

.. příklad::
Když Odoo dostane e-mail s předponou „commercial“ v odesílateli, příjemci nebo
:abbr:`CC“ e-mailové adresy (např. komerční\@příklad.com), databáze je označuje za
přijímá e-mail jako plnou „komerční“ adresu s jiným doménovým názvem, a proto vytváří
ticket, lead, příležitost atd.

Chcete-li přidat parametr „mail.catchall.domain.allowed“, nejprve aktivujte režim vývojáře
Vývojářský režim. Poté přejděte na: „Nastavení aplikace“ → „Technické“ → „Parametry systému“.
Klikněte na „Nový“ a zadejte do pole „Hodnota“ „mail.catchall.domain.allowed“.

Poté přidejte do pole „Hodnota“ oddělené čárkami domény.
:icon:`fa-cloud-upload` :guilabel:`(Uložit)“ a systémový parametr se okamžitě projeví.

.. obrázek: email_servers_inbound/allowed-domain.png
:alt: parametr systémového nastavení mail.catchall.domain.allowed.

Detekce vnitřní části založená na příchozí adrese
===================================

Při vytváření nového aliasu je možné zapnout:guilabel:`Incoming address based on local part
detekce“. Pokud je povolena detekce, Odoo pouze vyžaduje shodu s místní částí pro směrování příchozích e-mailů.
Tato funkce je vypnutá a Odoo vyžaduje shodu celé e-mailové adresy pro směrování příchozí pošty.
e-mail.
