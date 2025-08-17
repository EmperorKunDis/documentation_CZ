============================================
Nastavte záznamy DNS pro odesílání e-mailů v Odoo
============================================

Tato dokumentace představuje tři komplementární protokoly ověřování (SPF, DKIM a DMARC), které jsou
prokázat legitimitu odesílatele e-mailu. Nesplnění těchto protokolů výrazně sníží
šance, že e-maily dorazí na jejich cílovou adresu.

Databáze aplikací **Odoo Online** a **Odoo.sh** používající výchozí adresu poddomény **Odoo** (např.
(například \@company-name.odoo.com) jsou přednastaveny tak, aby odesílaly **ověřené emaily** v souladu s
SPF, DKIM a DMARC protokoly.

Pokud se rozhodnete použít místo toho vlastní doménu, je třeba správně nakonfigurovat záznamy SPF a DKIM.
je nezbytné, aby se e-maily nedostaly do složky s nevyžádanou poštou nebo aby nebyly doručeny příjemcům.

Pokud používáte výchozí e-mailový server Odoo k odesílání e-mailů z vlastní domény
<email-outbound-custom-domain-odoo-server>`, musí být nastaveny následující záznamy SPF a DKIM
je uvedeno níže. Pokud se používá odchozí e-mailový server, je nutné použít záznamy SPF a DKIM
přizpůsobený pro danou e-mailovou službu a vlastní doménu.

.. poznámka::
Poskytovatelé e-mailových služeb používají různá pravidla pro příchozí e-maily. E-mail může být klasifikován jako
i když projde kontrolou SPF a DKIM.

..._spf.email._domain:

SPF (Sender Policy Framework)
=============================

Služba Sender Policy Framework (SPF) umožňuje majiteli doménového jména určit, které
server může odesílat e-maily z domény. Když server obdrží příchozí e-mail,
zkontroluje, zda je adresa IP odesílacího serveru na seznamu povolených IP.
záznam SPF (Sender Policy Framework) odesílatele.

V Odoo se provádí SPF test na adresu odpovědi definovanou pod :guilabel:`Alias
V poli „Doména“ pod obecnými nastaveními databáze je možné zadat vlastní doménu.
:guilabel:Alias Domain, je nutné jej nakonfigurovat tak, aby byl kompatibilní s SPF.

Politika SPF domény se nastavuje pomocí záznamu TXT. K vytvoření nebo změně tohoto záznamu
závisí na poskytovateli, který hostuje zónu jmen domény v systému DNS (Domain Name System).

Pokud doménové jméno ještě nemá záznam TXT, vytvořte ho pomocí následujícího vstupu:

.. kódový blok: bash

v=spf1 include:_spf.odoo.com -all

Pokud doménové jméno již má SPF záznam, musí být aktualizován. Není třeba vytvářet nový
jedna doména musí mít pouze jeden záznam SPF.

.. příklad::
Pokud je záznam TXT nastaven na „v=spf1 include:_spf.google.com ~all“, upravte jej tak, aby obsahoval
„include:_spf.odoo.com“: „v=spf1 include:_spf.odoo.com include:_spf.google.com ~all“

Zkontrolujte záznam SPF pomocí nástroje, jako je MXToolbox SPF Record Check
<http://www.mxtoolbox.com/spf.aspx>`. Vytváření nebo úprava záznamu SPF závisí na
poskytovatel hostující zónu doménového jména. Nejčastěji používanými poskytovateli jsou:
a jejich dokumentace jsou uvedeny níže.

..._email-domain-dkim:

DKIM (DomainKeys Identified Mail)
=================================

DomainKeys Identified Mail (DKIM) umožňuje uživateli ověřit e-mail pomocí digitálního podpisu.

Při odesílání e-mailu obsahuje Odoo e-mailový server unikátní :abbr:`DKIM (DomainKeys Identified
podpis v hlavičce. Server příjemce pak tento podpis dešifruje pomocí DKIM
záznamu v doméně databáze. Pokud se podpis a klíč v záznamu shodují, je
dokazuje, že zpráva je autentická a nebyla pozměněna během přenosu.

Aktivace DKIM je **povinná** při odesílání e-mailů **z vlastní domény** prostřednictvím e-mailu Odoo.
server.

Pro zapnutí DKIM přidejte záznam „CNAME (Canonical Name)“ do záznamu „DNS (Domain Name System)“.
zóna doménového jména:

.. kódový blok: bash

odoo._domainkey IN CNAME odoo._domainkey.odoo.com.

.. tip::
Pokud je doménové jméno například „company-name.com“, ujistěte se, že vytvoříte poddoménu
„odoo._domainkey.soukromá společnost.com“, jehož kanonické jméno je „odoo._domainkey.odoo.com“.

Způsob vytvoření nebo změny záznamu CNAME závisí na poskytovateli, který hostuje zónu DNS.
doménu. Nejčastějšími poskytovateli a jejich
Dokumenty jsou uvedeny níže.

Zkontrolujte, zda je záznam DKIM platný pomocí nástroje jako MXToolbox DKIM Record Lookup
<http://www.mxtoolbox.com/dkim.aspx>`. Zadejte „example.com:odoo“ do vyhledávacího nástroje DKIM a zadejte
že testovaný selektor je „odoo“ pro vlastní doménu „example.com“.

..._email-doména-dmarc:

DMARC (Domain-based Message Authentication, Reporting and Conformance)
======================================================================

Zkratka DMARC (Domain-based Message Authentication, Reporting, & Conformance) označuje
protokol, který sjednocuje :abbr:`SPF (Sender Policy Framework)“ a :abbr:`DKIM (DomainKeys Identified
). Instrukce obsažené v záznamu DMARC doménového jména říkají cílovému serveru
jak se zachovat v případě e-mailu přicházejícího zvenčí, který neprošel kontrolou SPF a/nebo DKIM.

.. poznámka::
Cílem této dokumentace je pomoci pochopit, jaký dopad má DMARC na doručitelnost.
většina e-mailů**, než aby poskytla přesná doporučení pro vytvoření záznamu DMARC.
zdroj, jako je například webová stránka „DMARC.org <https://dmarc.org/>“ pro nastavení záznamu DMARC.

DMARC má tři politiky:

- „p=none“
- „q = karanténa“
- „p = odmítnout“

Instrukce „p = karanténa“ a „p = odmítnout“ učí server, který e-mail obdrží, aby tento e-mail zablokoval nebo
ignorujte ho, pokud kontrola SPF nebo DKIM selže.

.. poznámka::
**Pro DMARC musí projít kontrola DKIM nebo SPF a domény musí být v
zarovnání. Pokud je typ hostingu Odoo Online, konfigurace DKIM na odesílacím doméně
musí projít kontrolou DMARC.

Přechod na DMARC obvykle znamená, že e-mail bude úspěšně doručen. Je však důležité
poznamenat, že **další faktory jako filtry proti spamu mohou stále odmítnout nebo zablokovat zprávu**.

„p=none“ se používá k tomu, aby majitel domény mohl dostávat zprávy o subjektech, které jejich doménou využívají.
neměl by ovlivňovat doručitelnost.

.. příklad::
:literal:`_dmarc IN TXT "v=DMARC1; p=none; rua=mailto:postmaster@example.com"` znamená, že
souhrnné zprávy o DMARC budou zasílány na adresu postmaster@example.com.

.. _email_domain/mail_config_common_providers:
..._dokumentace_poskytovatelů_e-mailových_domén:

Dokumentace k SPF, DKIM a DMARC běžných poskytovatelů
=====================================================

- „OVH DNS <https://docs.ovh.com/us/en/domains/web_hosting_how_to_edit_my_dns_zone/>“
- „Záznam GoDaddy TXT <https://www.godaddy.com/help/add-a-txt-record-19232>“
- „Záznam GoDaddy CNAME <https://www.godaddy.com/help/add-a-cname-record-19236>“
- „NameCheap <https://www.namecheap.com/support/knowledgebase/article.aspx/317/2237/how-do-i-add-txtspfdkimdmarc-records-for-my-domain/>“
- „Cloudflare DNS <https://support.cloudflare.com/hc/en-us/articles/360019093151>“
- „Záznamy DNS Squarespace <https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain>“
- „Azure DNS <https://docs.microsoft.com/en-us/azure/dns/dns-getstarted-portal>“

Pro plné otestování konfigurace použijte nástroj Mail-Tester <https://www.mail-tester.com/>_, který
poskytuje kompletní přehled obsahu a konfigurace v jednom odeslaném e-mailu. Mail-Tester může být
slouží k nastavení záznamů pro jiné, méně známé poskytovatele.

.. viz též:
   - Použití nástroje Mail-Tester k nastavení záznamů SPF pro konkrétní dopravce
<https://www.mail-tester.com/spf/>
   - „Zázračný list – konfigurace SPF, DKIM a DMARC [PDF]

