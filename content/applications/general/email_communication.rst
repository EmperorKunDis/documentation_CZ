Zobrazit obsah

==============================
Komunikace v Odoo emailem
==============================

Komunikace v Odoo související s záznamy jako jsou příležitosti CRM, objednávky prodeje, faktury, ...
Mají diskuzní vlákno nazvané „štěbetání“, které často zobrazují na pravé straně záznamu.

Na chatu můžete posílat e-maily nebo notifikace z aplikace Odoo přímo uživatelům dokumentu.
(podle svých preferencí oznámení) zaznamenat interní poznámky, poslat zprávu přes WhatsApp nebo SMS.
a plánovat aktivity.

Pokud se odpověď dostane k někomu z fanoušků, odpověď aktualizuje konverzaci a Odoo ji předá dál.
upozornění. Všechny e-maily – odchozí i příchozí – se zobrazují v jednom kanálu.

.._e-mail-online-shop:

Uživatelé Odoo Online a Odoo.sh
=============================

Odesílané a přijaté e-maily fungují na Odoo Online i Odoo.sh bez jakýchkoliv úprav, **nic se nemusí
hotovo**. Vše je již nakonfigurováno na vaší poddoméně.

Výchozí nastavení odesílaných e-mailů používá následující adresu :ref:`e-mailové oznámení
<email-outbound-notifications> „notifications@company-name.odoo.com“.

.._email-online-shop-domena:

Použití jiného doménového názvu
--------------------

Pokud nechcete, aby odchozí emaily byly posílány z poddomény „@company-name.odoo.com“ společnosti Odoo
místo toho: „z vlastní domény“ (<email-outbound-custom-domain>)**, další konfigurace je
bude nutné na doméně a v Odoo. To přidává další vrstvu komplexnosti a
vyžaduje technické znalosti (hlavně v oblasti DNS a poštovních protokolů).

Přidáním domény a nastavením práv správce můžete také přistupovat k
stránku pro konfiguraci e-mailového aliasu vaší společnosti.
Pokud je konfigurováno pouze jedno doménové jméno, bude tento název sdílen všemi společnostmi v databázi.

Pokud chcete nadále používat poštovní server Odoo, budete muset:
<email-domain-spf>.

Pokud chcete používat vlastní poštovní server, musíte
musíte se řídit konkrétní dokumentací poskytovatele poštovních služeb.

Pro e-maily odeslané na vlastní doménu se po přidání vlastního doménového jména:ref:`odpovědi zákazníků vrátí zpět.
Váš doménový účet <email-inbound-custom-domain>, a budete muset použít jednu z těchto tří možností
dostat e-maily zpět do Odoo (pomocí buďto:ref: příchozí pošty
<email-inbound-custom-domain-incoming-server>`, :ref:`přesměrování
<email-inbound-custom-domain-redirections> nebo :ref:`DNS záznam MX
<email-inbound-custom-domain-mx>'). Vše je popsáno v dokumentaci :doc:`Spravovat příchozí zprávy
dokumentace <Emailová komunikace/Emailové servery příchozí>.

.._e-mail-na-předním místě:

Uživatelé v prostředí on premises
================

Pokud jste na místě, musíte kompletně nakonfigurovat své odchozí a příchozí emaily:

- Pro odchozí e-maily budete potřebovat :ref:`server SMTP a vlastní doménu
<email-outbound-custom-domain-odoo-server>.
- Pro příchozí e-maily nastavte frekvenci získávání nových e-mailů nízko dostatečně pro reakci.
ale dostatečně vysoká, aby nezatěžovala váš systém nebo poskytovatele. Protože z těchto důvodů a
jednoduchostí této konfigurace obvykle doporučujeme používat příchozí poštovní servery. Pro odesílání
serveru se podívejte na dokumentaci „Použít vlastní doménu pro příchozí zprávy“.
<email-inbound-custom-domain>.

..._email-třetí-stránky:

Použití poštovního serveru třetí strany
==========================================

Dokumentace Odoo pokrývá také několik populárních poštovních serverů. Ty vyžadují specifické
autorizace a konfigurace přidávají další vrstvu komplexnosti. Proto je používání Odoo
vhodné je nastavit odchozí poštovní server.

- :doc:`Dokumentace Outlooku <email_communication/azure_oauth>`
- :doc:`Dokumentace Gmailu <email_communication/google_oauth>`
- :doc:`Dokumentace Mailjetu <email_communication/mailjet_api>`

.. poznámka::
Každý poskytovatel má své vlastní limity. Prozkoumejte požadovaného poskytovatele před konfigurací.
Příkladem mohou být například aplikace Outlook a Gmail, které nemusí být vhodné pro velké marketingové kampaně.

.. viz též:
   - :doc:`Aktivita <../essentials/activities>`
   - :doc:`Diskuse o aplikaci <../productivity/discuss>`
   - :doc:`Shrnutí e-mailů <firmy/shrnutie_emailov>`
   - :doc:`Aplikace pro e-mailový marketing <../marketing/email_marketing>`
   - :doc:`Šablony e-mailů <soubory/email_template>`
   - :ref:`Vytváření výdajů pomocí e-mailového aliasu <expenses/email_expense>`
   - :ref:`Vytváření helpdeskových požadavků pomocí e-mailové adresy aliasu <helpdesk/receiving_tickets/email-alias>`
   - :ref:`Vytváření leadů pomocí e-mailové adresy aliasu <crm/configure_email_alias>`
   - :ref:`Vytváření úkolů pomocí e-mailové adresy <task_creation/email_address>`
   - :doc:`Technická poštovní brána pro uživatele vlastních serverů

   - Technický start databáze Odoo s konfigurovaným odchozím poštovním serverem
příkazová řádka (viz reference/cmdline/server/emails)

..toctree::


email_komunikace/emailové servery příchozí
komunikace e-mailem/směrovače pro odchozí poštu
komunikace e-mailem/doména e-mailu
email_communication/azure_oauth
email_communication/google_oauth
email_communication/mailjet_api
emailová komunikace/často kladené otázky
