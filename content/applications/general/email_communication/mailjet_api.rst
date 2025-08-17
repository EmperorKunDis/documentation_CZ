===========
Mailjet API
===========

Odoo je kompatibilní s API pro masovou poštu společnosti Mailjet.
Nastavte speciální server pro masové rozesílání e-mailů pomocí Mailjetu, nastavením parametrů v Mailjet
účet a databázi Odoo. V některých případech je potřeba nastavit konfiguraci na úrovni
Nastavení domény:abbr:DNS (Domain Name System).

Nastavit v Mailjetu
=================

Vytvořte přihlašovací údaje do API
----------------------

Chcete-li začít, přihlaste se do „Informace o účtu Mailjet <https://app.mailjet.com/account>“.
stránce. Poté přejděte do sekce „Příjemci a domény“ a klikněte na „SMTP a
Nastavení API SEND“.

.. obrázek: mailjet_api/api-settings.png
:alt:Nastavení SMTP a Send API v sekci Odesílatelé a domény na Mailjetu.

Poté zkopírujte konfigurační nastavení protokolu SMTP (jednoduchý protokol pro přenos pošty) do notepadu.
Najdete je v sekci Konfigurace (pouze SMTP). V seznamu služeb najdete položku SMTP (Simple Mail Transfer Protocol).
Nastavení protokolu přenosu pošty) zahrnuje adresu serveru a možnost zabezpečení
potřebuje (použijte zkratku: SSL (Secure Sockets Layer) / TLS (Transport Layer Security)).
číslo portu. Nastavení je potřeba pro konfiguraci Mailjet v Odoo, což je popsáno v
:ref:`poslední část <maintain/mailjet-api/odoo-setup>“.

.. viz též:
„Jak mohu nakonfigurovat parametry SMTP?“
<https://documentation.mailjet.com/hc/articles/360043229473>

.. důležité::
Odoo blokuje port 25 na Odoo Online a Odoo.sh
databáze.

.. obrázek: mailjet_api/smtp-config.png
:alt: Konfigurace SMTP od Mailjetu.

Nyní klikněte na tlačítko s názvem „Získat přístupové údaje služby“ a získejte přístup k Mailjet.
Přihlašovací údaje k API.

Pak klikněte na oční ikonu, abyste zobrazili klíč API. Zkopírujte tento klíč do poznámkového bloku, protože
slouží jako uživatelské jméno v konfiguraci Odoo. Poté klikněte na
Tlačítko „Vytvořit tajný klíč“ k vytvoření tajného klíče. Zkopírujte tento klíč do
poznámkový blok, protože slouží jako heslo v konfiguraci Odoo.

Přidej ověřenou adresu odesílatele (adresy).
-------------------------------

Dalším krokem je přidat adresu odesílatele nebo doménu do nastavení účtu Mailjet, aby
E-mailová adresa nebo doména je schválena k odesílání e-mailů prostřednictvím serverů Mailjet. Nejprve přejděte na
Stránka „Informace o účtu Mailjet <https://app.mailjet.com/account>“. Následně klikněte na
V sekci „Odesílatelé a domény“ klikněte na odkaz „Přidat doménu nebo e-mailovou adresu“.

.. obrázek: mailjet_api/add-domain-email.png
:alt:Přidejte odesílací doménu nebo e-mailovou adresu do rozhraní služby Mailjet.

Určete, zda je potřeba přidat e-mailovou adresu odesílatele nebo celý doménový název do Mailjet
Nastavení. Možná je jednodušší nastavit celý doménový systém, pokud jde o :abbr:`DNS (Domain Name System)`
přístup je k dispozici. Přeskočte na část „Přidat doménu“ v sekci
kroků k přidání domény.

.. poznámka::
Buď všechny e-mailové adresy uživatelů databáze Odoo, kteří posílají e-maily pomocí služby Mailjet.
musí být nakonfigurována nebo lze nakonfigurovat doménu uživatelských e-mailových adres.

Výchozí e-mailová adresa zadaná v účtu Mailjet je automaticky přidána jako důvěryhodná.
Odesílatel. Chcete-li přidat další e-mailovou adresu, klikněte na tlačítko označené:guilabel:`Přidat odesílatele“.
Pak přidejte e-mailovou adresu, která je nastavena k odesílání z vlastní domény.

Následující e-mailové adresy by měly být vytvořeny a ověřeny u poskytovatele služeb Mailjet:

- notifications@yourdomain.com
- bounce@vašedoména.cz
- catchall@vašedoména.cz

.. poznámka::
Vyplňte místo „yourdomain“ vlastní doménou pro databázi Odoo. Pokud taková doména neexistuje, pak
parametr systému :guilabel:`mail.catchall.domain`.

Poté vyplňte formulář „Informace o e-mailu“, zvolte vhodný
Typ e-mailu: transakční e-mail nebo hromadný e-mail. Po vyplnění formuláře přijde aktivace na váš e-mail.
a důvěryhodný odesílatel může být aktivován.

Je doporučeno nastavit SPF (Sender Policy Framework) a DKIM (DomainKeys
Identifikovaná pošta): abbr.: DMARC (ověřování zpráv na základě domény, hlášení a reportování)
Nastavení „Soulad“ na doméně odesilatele.

.. viz též:
   - Dokumentace o SPF a DKIM od společnosti Mailjet
<https://documentation.mailjet.com/hc/en-us/articles/360049641733-Authenticating-Domains-with-SPF-and-DKIM-A-Complete-Guide>
   - Dokumentace k DMARC od Mailjet
<https://documentation.mailjet.com/hc/en-us/articles/20531905163419-Understanding-DMARC>

.. důležité::
Pokud databáze nepoužívá vlastní doménu, pak k ověření odesílatelovy adresy je třeba
doporučujeme nastavit do Odoo CRM dočasnou e-mailovou adresu (z uvedených tří).
Vytvořit kontaktní osobu. Poté je databáze schopna přijmout ověřovací e-mail a ověřit
účty.

.._udržovat/mailjet-api/přidat doménu:

Přidejte doménu
------------

Přidáním celého doménového jména k účtu Mailjet se všemi odesílacími adresami souvisejícími s touto doménou
Jsou automaticky ověřeny pro odesílání e-mailů prostřednictvím serverů Mailjet. Nejprve přejděte na
Stránka „Informace o účtu Mailjet <https://app.mailjet.com/account>“. Následně klikněte na
V sekci „Odesílatelé a domény“ klikněte na odkaz „Přidat doménu nebo e-mailovou adresu“.
Poté klikněte na tlačítko „Přidat doménu“ a přidejte vlastní doménu.

.. poznámka::
Doména musí být přidána do účtu Mailjet a poté ověřena prostřednictvím DNS.
(Systém doménových jmen).

Poté vyplňte stránku „Přidat novou doménu“ na Mailjetu a klikněte
:guilabel:`Pokračovat“.

Po přidání domény se zobrazí ověřovací stránka. Pokud je databáze Odoo na místním serveru
V tom případě zvolte možnost :guilabel:`1. Vytvořit záznam v DNS`,
Zkopírujte informace o záznamu TXT do poznámkového bloku a poté přejděte na doménovou :abbr:`DNS.
Poskytovatele služby „Název systému“ k dokončení ověřování.

.. obrázek: mailjet_api/host-value-dns.png
:alt:Informace o záznamu TXT, které je potřeba zadat do DNS domény.

Nastavení v doménovém systému DNS
~~~~~~~~~~~~~~~~~~~~~~~~~

Po získání informací o záznamu TXT v účtu Mailjet přidejte záznam TXT do domény.
DNS (Domain Name System). Tento proces se liší v závislosti na DNS (Domain Name
Poskytovatel systému). Pro konfiguraci se obraťte na poskytovatele služeb. Záznam TXT
informace se skládá z :guilabel:`Host` a :guilabel:`Value“. Vložte je
odpovídající pole v záznamu TXT.

Návrat k informacím o účtu Mailjet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Po přidání záznamu TXT do systému jmen domén (DNS) se vraťte zpět na
Mailjet účet. Poté přejděte na: menuselection:„Informace o účtu“ – „Přidat doménu odesílatele“.
Klikněte na ikonu ozubeného kola vedle položky „Doména“ a vyberte možnost „Zkontrolovat“.

Tuto akci lze také provést návštěvou „Domény odesílatelů a adresy <https://app.mailjet.com/
účtu/odesílatele> stránce informací o účtu a kliknutím na „Spravovat“.

Dále klikněte na tlačítko „Zkontrolovat nyní“ a ověřte přidaný záznam TXT pro doménu.
úspěšný obrazovka se zobrazí, pokud je doména správně nakonfigurována.

.. obrázek: mailjet_api/check-dns.png
:alt: Zkontrolujte záznam v DNS na Mailjetu.

Po úspěšném nastavení domény je možné:guilabel:`Připojit tuto doménu
(SPF/DKIM). Tlačítko vyplní :abbr:`SPF (Sender Policy Framework)` a :abbr:`DKIM (DomainKeys
Identifikované poštovní zprávy) do DNS (Domény jmen systému).

.. viz též:
„Dokumentace Mailjetu pro SPF/DKIM/DMARC“ <https://documentation.mailjet.com/hc/articles/
360042412734-Ověřování domén pomocí SPF a DKIM

.. obrázek: mailjet_api/authenticate.png
:alt:Připojte doménu k záznamům SPF/DKIM v Mailjetu.

... udržovat/mailjet-api/odoo-setup:

Nainstalujte si Odoo
==============

Pro dokončení nastavení přejděte na databázi Odoo a v ní do sekce „Nastavení“.
Vývojářský režim zapnutý, přejděte do menu „Technické nastavení“ -> „E-mail“ -> „Odeslané
Poštovní servery. Poté vytvořte novou konfiguraci odchozí pošty kliknutím na
Tlačítko „Vytvořit“.

Dále zadejte „server SMTP“ (in-v3.mailjet.com), „číslo portu“ (587 nebo 465) a „Zabezpečení
(SSL/TLS), které byly dříve zkopírovány ze schránky Mailjet. Naleznete je také zde
<https://app.mailjet.com/account/setup>`. Doporučuje se používat:abbr:SSL (Secure Sockets
Síťový protokol TLS (Transport Layer Security), i když Mailjet jej nemusí vyžadovat.

Do políčka „Uživatelské jméno“ zadejte „API KEY“. Do políčka „Heslo“ zadejte
tajný klíč, který byl dříve zkopírován z účtu Mailjet do poznámkového bloku.
Nastavení najdete na:menu-selection:Mailjet -->  Account Settings --> SMTP a SEND API
Nastavení.

Pak nastavte hodnotu :guilabel:`Priority` vyšší
než u jakéhokoliv transakčního e-mailového serveru. Nakonec uložte nastavení a zkontrolujte
Připojení“.

.. obrázek: mailjet_api/server-settings.png
:alt:Nastavení odchozích e-mailů v systému Odoo.
