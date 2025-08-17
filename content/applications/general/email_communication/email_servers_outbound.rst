========================
Správa odchozích zpráv
========================

..._email-outbound-default:

Odesílání e-mailů s výchozím nastavením Odoo
================================================

Na Odoo Online a Odoo.sh funguje odesílání a přijímání e-mailů bez problémů.
Je potřeba konfigurace.

Při vytváření databáze se používá poddoména „company-name.odoo.com“ pro odesílání a přijímání
e-maily. Dodávání e-mailů je optimalizováno pro tuto poddoménu, protože používá konfiguraci DNS společnosti Odoo.

.. příklad::
Pokud je poddoména databáze například „company-name.odoo.com“ a všechny nastavení odesílání jsou
výchozí adresa, všechny emaily budou odeslány na „notifications@company-name.odoo.com“.

.._email-outbound-default-from-filtering:

Tato konfigurace je nastavena systémovým parametrem mail.default.from_filter.
V případě, že doména odesílatele neodpovídá hodnotě tohoto parametru, bude zpráva doručena na adresu uvedenou v tomto parametru.
je použito místo tohoto systémového parametru: více hodnot oddělených čárkou, domény
nebo plné e-mailové adresy jsou povoleny. Jakmile je nastaveno :ref:`výchozí
<email-outbound-different-servers-personalized>, parametr systému již není brán v potaz
a použitá hodnota je filtrace :ref:`z FROM
<email-outbound-different-servers-personalized-from-filtering> poštovního serveru.

.. obrázek: e-mailové servery/síťový diagram příchozího mailingu.png
:alt: Výchozí konfigurace odesílaných zpráv v Odoo.

Emaily jsou odesílány na adresu „catchall@company-name.odoo.com“ jako odpověď. Dále
chyby při doručení jsou odesílány na adresu „bounce@company-name.odoo.com“.

.. poznámka::
Aby se zabránilo záměně pošty, je nutné mít pro každou e-mailovou adresu nastavený vlastní alias.
výzva k vytváření rekordů v databázi. Emaily odeslané na alias jsou automaticky přeposílány
a odpoví na existující a propojený záznam nebo vytvoří nový záznam v databázi.

..._email-outbound-custom-domain:

Použití vlastní domény k odesílání e-mailů
====================================

Databáze lze nakonfigurovat tak, aby používala vlastní doménu, ve které jsou všechny výchozí e-mailové adresy
vytvořené pomocí vlastního doménového jména. Pokud je vlastní doménové jméno například „company-name.com“, adresa odesilatele bude
„upozornění“ na adresu „upozorneni@firma-jmeno.cz“, a odpověď na „všechny“ na adresu „vsechny@firma-jmeno.cz“.
Adresa pro odpovědi „odpověď@název_firmy.cz“ může být využita při zasílání e-mailů
e-maily buď přes e-mailové servery Odoo nebo externí.

Tato část předpokládá vlastnictví vlastního doménového jména. Pokud ne, musí být koupeno z
registrátor domén jako je GoDaddy, Namecheap nebo jakýkoli jiný poskytovatel služeb.

.. viz též:
„Zázračný list - Konfigurace e-mailového doménového jména [PDF]


..._email-outbound-custom-domain-odoo-server:

Použití vlastního doménového jména s e-mailovým serverem Odoo
----------------------------------------------

Na Odoo Online nebo Odoo.sh jsou některé konfigurace v DNS domény na základě předpisu
zajistit dobrou doručitelnost.

.. varování:
Většina konfigurace bude prováděna na straně poskytovatele domény a může vyžadovat nějaké úpravy.
konfigurace na samotném poštovním serveru. **Pro provedení je nutné mít nějaké technické znalosti.**

Prvním krokem je konfigurace SPF a DKIM.
aby odpovídal požadavkům mail serveru Odoo.

Dalším krokem je nastavení vlastní domény jako aliasové domény společnosti. Vyberte společnost, otevřete
„Nastavení“ a přidejte vlastní doménu do pole „Alias Domain“.

Po přidání alternativního doménového jména klikněte na ikonu „pravý sloupec“ (viz obrázek).
Pokud je potřeba, přidat do vlastního doménového jména více společností. Zapnout režim vývojáře
změnit výchozí aliasy, pokud chcete:

- :guilabel:`Bounce Alias“: poštovní schránka, která zachycuje chyby při doručování a naplňuje
v příslušném e-mailu v záhlaví „envelope <email-issues-outgoing-delivery-failure>“.
- :guilabel:`Všeobecná e-mailová adresa“: výchozí poštovní schránka, která slouží k centralizaci všech odpovědí.
- :guilabel:`Poznámka k odesílateli z aliasu“: výchozí adresa odesílatele.

.. poznámka::
Při vytvoření prvního domény s přezdívkou bude používat všechny společnosti. Pokud vytvoříte novou
společností, automaticky nastavený aliasový doménový název je ten s nejnižším prioritním pořadím (reklama zobrazená na
seznam domén v režimu vývojáře (viz :ref:`developer-mode`).

Všechny e-mailové aliasy (např. související s týmem CRM nebo Helpdesku) musí mít svou odpovídající schránku v
server pro e-mailovou poštu s vlastní doménou.

.. obrázek: mail_servery_výstupní/diagram-majitelské-domény-server-odoo.png
:alt:Technická schémata konfigurace externího poštovního serveru s Odoo.

Přijímat e-maily v databázi Odoo ve správném chatu (CRM, fakturace, prodej).
pokud je objednávka vystavena na fakturu (např.

- :ref:`Přesměrování / přeposílání <email-inbound-custom-domain-redirects>`
- :ref:`Příchozí poštovní servery <email-inbound-custom-domain-incoming-server>“
- :ref:`Záznam MX <email-inbound-custom-domain-mx>“ (vyžaduje pokročilé technické znalosti).

Použití vlastního doménového jména znamená, že se použijí konkrétní části
Toto pole může být použito k odesílání e-mailů.

.._email-outbound-custom-domain-smtp-server:

Odesílání e-mailů přes externí SMTP server
-------------------------------------------

.. poznámka::
Pokud chcete využívat vlastní SMTP server, musí být spárován s vaší doménou, protože aktualizace
DNS poddomény Odoo není možné.

Přidat externí SMTP server do Odoo otevřete nastavení a zapněte „Používat
Možnost „Vlastní e-mailový server“ naleznete pod záložkou „E-maily“. Pak klikněte
:guilabel:`Uložit“ nahoře na stránce, abyste uložili změny.

Vraťme se do části „E-maily“ a klikněte na „Odesílací servery“, pak na „Nový“.
Vytvořit záznam poštovního serveru odchozí pošty. Většina polí je běžnými parametry pro nastavení
připojení k serveru SMTP; použijte hodnoty poskytnuté vaším e-mailovým poskytovatelem.

Jakmile je připojení dokončeno, klikněte na tlačítko „Ověřit připojení“. Poznámka: Při úspěšné kontrole připojení se nezobrazí
potvrdit, že e-mail bude odeslán, protože nějaká omezení mohou zůstat na straně poskytovatele, a tedy
Je doporučeno konzultovat dokumentaci poskytovatele.

..._email-outbound-custom-domain-smtp-server-local-part:

Hodnota místní části
~~~~~~~~~~~~~~~~~

Níže jsou uvedeny různé hodnoty lokálního části, které může používat Odoo k odesílání e-mailů.
mohou být vyžadovány v bílém seznamu vašeho poštovního serveru:

- Alias pro doménu přeposílání aliasů (výchozí hodnota = bounce),
- Alias doménového výchozího nastavení (výchozí hodnota = „upozornění“),
- Výchozí e-mailová adresa pro správce (např. admin@company-name.odoo.com nebo nová hodnota)
- Výchozí adresa Odoobota „odoobot@company-name.odoo.com“ (nebo nová hodnota, pokud byla změněna).
- Specifické odesílatelé e-mailových kampaní
- Specifický odkaz, který lze definovat v šabloně e-mailu.

.. viz též:
   - :doc:`google_oauth`
   - :doc:`azure_oauth`

.._email-outbound-different-servers:

Nastavení různých serverů pro transakční a hromadné e-maily
==============================================================

.. _email-outbound-different-servers-personalized:

Personalizované poštovní servery
-------------------------

Transakční e-maily a masové rozesílky lze odeslat pomocí samostatných e-mailových serverů v Odoo.
Každodenní emaily, cenové nabídky nebo faktury zaslané klientům budou zpracovány jako *transakční.
*E-maily.**Masová rozesílání e-mailů*, včetně odesílání hromadných faktur nebo nabídek, bude
spravované aplikací Marketing Automation nebo Email Marketing.

.. příklad::
Můžete používat služby jako Gmail, Amazon SES nebo Brevo pro transakční e-maily a služby jako
Mailgun, Sendgrid nebo Mailjet pro masové rozesílky.

Nejprve aktivujte režim vývojáře a přejděte do nastavení „Technické“ – „
E-mail: Odchozí poštovní servery. Tam přidejte dva záznamy odchozích e-mailových serverů, jeden pro
transakční e-maily a jeden pro masové rozesílání. Zadejte nižší :guilabel:`Prioritu`.
hodnota pro transakční server (např. 1) nad hodnotou pro masové rozesílání e-mailů (např. 2).
Přednost mají transakční e-maily.

.. obrázek: email_servers_outbound/split-transaction-massmail-mail-servers.png
:alt: Příklad rozdělení transakčního a masového serveru pro odesílání pošty.

Nyní přejděte na: „E-mailový marketing“ -> „Konfigurace“ -> „Nastavení“, zapněte
:guilabel:`Dedicovaný server“ a vyberte odpovídající e-mailový server. Odoo používá server s
nejnižší priorita pro transakční e-maily a server zvolený pro masové rozesílky.

.. obrázek::email_servers_outbound/dedikovany-masovy-mail-server.png
:alt:Dedikovaný poštovní server na nastavení aplikace pro e-mail marketing.

.._email-outbound-different-servers-personalized-from-filtering:

Z FILTRU
~~~~~~~~~~~~~~

.. důležité::
Je **velmi doporučeno** nakonfigurovat filtrování odchozí pošty na serverech pro odesílání e-mailů tak, jak je uvedeno níže.
pokyny vašeho poskytovatele.

Políčko „Od“ umožňuje použití konkrétního odchozího e-mailového serveru.
podle e-mailové adresy nebo domény, ze kterých Odoo odesílá zprávu jménem příjemce. Hodnota musí být
musí být doména nebo celá adresa, která odpovídá e-mailové adrese odesilatele a je důvěryhodná na
serveru poskytovatele odchozí pošty.

Pokud se nepoužívá filtrování odesílatelů, e-maily budou odcházet zadaným adresám.

.. varování:
Některé odchozí poštovní servery vyžadují konfiguraci filtru odesílatele.

Při odesílání e-mailu z Odoa se používá následující postup výběru serveru pro odchozí poštu:

- Nejprve hledá server s stejnou hodnotou filtrace FROM jako hodnotu From (tj.
(e-mailová adresa) definovaná v odchozí poště. Tato konfigurace je ideální, pokud všichni uživatelé
Společnosti sdílejí stejnou doménu, ale mají různé lokální části.

.. příklad::
Pokud je e-mailová adresa odesílatele „test@example.com“, pak pouze e-mailový server s filtrem na příchozí poštu
Může být použita hodnota rovnající se „test@example.com“ nebo „example.com“.

- Pokud není nalezen žádný server podle prvního kritéria, Odoo hledá první server bez FROM
filtrování hodnoty. E-mailová adresa bude převedena na adresu oznámení.

- Pokud není na základě druhého kritéria nalezen žádný server, použije Odoo první server a e-mail
bude převedeno na adresu oznámení.

.. poznámka::
Pro určení, který server je první, používá Odoo hodnotu priorit (menší číslo znamená vyšší prioritu).
podle důležitosti (tj. vyšší priorita je uvedena jako první). Pokud tak neučiníte, určuje se první server podle názvu serveru.
podle abecedy.

- Pokud neexistuje poštovní server, Odoo se spoléhá na systémový parametr
<email-outbound-default-from-filtering> hodnotu.

Dále je možné využít poštovního serveru Odoo pro transakční e-maily kromě masových rozesílek.

.. _email-outbound-different-servers-external-odoo:

Použitím externího e-mailového serveru a výchozího serveru Odoo
--------------------------------------------------------

Ve službě Odoo Online a Odoo.sh jsou databáze spouštěny s SMTP serverem Odoo. Pokud není možné odesílat e-maily
server je nastaven na výchozí SMTP server Odoo.

.. obrázek: email_servers_outbound/command-line-interface-option-mail-server.png
:alt:Přidání poštovního serveru pomocí poštovního serveru Odoo s ověřením CLI.

.. příklad::
Pokud se současně používá výchozí server Odoo (CLI), odeslaná pošta bude mít v poli „Od“ hodnotu
filtr odchozí pošty musí obsahovat vlastní doménu a filtr zprávy příkazového řádku
musí obsahovat poddoménu Odoo. Pokud není použito filtrování odesílatele, e-mail bude vypadat takto:
adresa pro zasílání oznámení.

.. obrázek: email_servers_outbound/split-mail-servers.png
:alt: Rozdělení poštovního serveru Odoo pro transakční e-maily a Mail server pro masovou komunikaci.

.. poznámka::
Ve službě Odoo Online je příkazová řádka ekvivalentní k výchozímu serveru pro odesílání pošty v Odoo.
stejný limit jako kdyby neexistoval žádný odchozí poštovní server.

.. tip::
Na Odoo Online je stránka také zobrazuje denní používání e-mailu a denní limit. Na Odoo.sh se
Musíte zkontrolovat počet odeslaných e-mailů na stránce s monitorem.

.. poznámka::
Na Odoo.sh lze pro příkazovou řádku nastavit odchozí poštovní server.
konfigurační soubor.

.. varování:
Mailový server Odoo je určen pro transakční emaily a malé reklamní kampaně.
:ref:`denní limit <email-issues-outgoing-delivery-failure-messages-limit> se odvíjí od
typ databáze a aplikace používané k jejímu ovládání.

.._email-outbound-custom-domain-external-server:

Používání vlastního doménového jména s externím e-mailovým serverem
===================================================

Podobně jako v předchozím kapitole :ref:`<email-outbound-different-servers-external-odoo>`,
může být zapotřebí konfigurace, aby se zaručilo, že externí e-mailový server bude moci odesílat e-maily.
používáním vlastního doménového jména. Podle dokumentace poskytovatele správně nastavte příslušné
záznamů (SPF, DKIM a DMARC). Seznam nejčastěji používaných poskytovatelů je k dispozici na
<email-domain-providers-documentation>.

.. poznámka::
Pokud používáte vlastní doménu, je potřeba nastavit DNS. Pokud máte externí odchozí poštovní server
je použito, konfigurace záznamů je popsána v článku :doc:`Odoo DNS konfigurace pro naši poštu
dokumentace serverů (<email_domain>) **nebude mít požadovaný účinek**, protože je nezávislá
Odoo při použití vlastního e-mailového serveru. Odoo neumožňuje konfiguraci Odoo
poddoména.

..._omezení odchozích e-mailů:

Omezení přístavu
================

Port 25 je z bezpečnostních důvodů na Odoo Online a Odoo.sh blokován. Zkuste použít port 465, 587 nebo 2525
namísto.

..._email-outbound-alias-domain:

Alias doména
============

Všeobecný doménový prostor je specifický pro společnost. Výchozí poddoména společnosti je odoo.cz (např.)
(např. „prihlaseni.odoo.com“), ale každá společnost může mít vlastní e-mailovou doménu.

Když je zapnutý režim vývojáře, možnosti doménových aliasů jsou dostupné po kliknutí na
:menu:Nastavení --> Technické --> E-mail: Přezdívky domén.

.. varování:
Každá změna domény aliasu musí být provedena velmi opatrně. Pokud je jedním z aliasů (například bounce)
(přesměrování na jinou adresu, výchozí, default) se změní, všechny předchozí e-maily nebudou správně přesměrovány na
nové aliasy budou ztraceny.

V poli „Výchozí odesílatel aliasu“ lze vyplnit místní část e-mailové adresy (pomocí
výchozí „upozornění“ nebo plnou e-mailovou adresu. Konfigurujte ji tak, aby určila hlavičku „Od“.
Váš e-mail. Pokud je použita plná e-mailová adresa, všechny odchozí e-maily budou přepsány touto
adresa.

..._email-outbound-notifications:

Oznámení
===================

Když zákazník odpoví na e-mail zaslaný chatbotem, může odpovědět přímo na něj. Pokud zákazník odpoví
přímou zprávu na e-mail, odpověď je evidována v stejném chatu, čímž funguje jako vlákno zpráv.
Souvisí s rekordem.

Poté, co obdrží odpověď, použije Odoo následovníky (na základě přiřazených podtypů).
Odeslat jim oznámení e-mailem nebo v aplikaci Odoo, podle preferencí uživatele.

.. příklad::
Pokud zákazník s e-mailovou adresou „Mary“ <mary@customer.example.com> odpoví přímo,
e-mail pocházející z databáze Odoo, standardní chování Odoa je rozeslat e-mail všem uživatelům.
obsah všem ostatním uživatelům v rámci vlákna.

protože doména Marie nepatří do domény aliasu, Odoo převezme e-mailovou adresu a použije
e-mailovou adresu, na kterou chcete oznámit své následovníky. Toto přehození závisí na
konfigurace v databázi. Výchozí nastavení je pro Odoo Online a Odoo.sh e-mailová adresa odesílatele
adresa bude převedena na hodnotu „notifications@company-name.odoo.com“ místo
„mary@klient.vzorovém.com“.

Adresa je sestavena z názvu odesílatele.
{alias doména, výchozí odkaz z aliasu} @ {alias doména, název domény},
„notifikace@smekysro.odoo.com“.

..._email-outbound-unique-address:

Používáním jedinečné e-mailové adresy pro všechny odchozí e-maily
====================================================

Chcete-li donutit e-mailovou adresu odesílatele e-mailů, aktivujte režim vývojáře a přejděte na
Nastavení -> Technické -> E-mail: Přezdívky domén. V nastavení „Výchozí odesílatel“
Alias, použijte místní část nebo celou e-mailovou adresu jako hodnotu.

.. varování:
Pokud je použita **kompletní adresa** jako hodnota :guilabel:`Default From Alias`, **všechny** odchozí
e-maily budou přepsány touto adresou.
