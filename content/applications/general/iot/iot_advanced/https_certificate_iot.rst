.. _iot/https_certifikát_iot:

=======================
HTTPS certifikát (IoT)
=======================

*Protokol pro přenos hypertextu zabezpečený* (HTTPS) je bezpečná a zašifrovaná verze *Protokolu
Transferový protokol* (HTTP), který je primárním protokolem používaným k datové komunikaci mezi webem
prohlížeč a webová stránka. Zajišťuje bezpečnost komunikace pomocí šifrovacího protokolu známého jako Transport
Síťový protokol TLS, dříve známý jako Síťový protokol zabezpečených spojení SSL.
HTTPS (Hypertextový přenosový protokol zabezpečený) funguje na základě TLS (Zabezpečení transportního vrstvy).
/:abbr:`SSL (Secure Sockets Layer)` certificates, which authenticate the provider and verify their
identita.

Použití protokolu HTTPS je vyžadováno při komunikaci s některými zařízeními v síti, zejména při placení
terminaly. Pokud není platný certifikát HTTPS, některé zařízení nemohou komunikovat s IoT
systém.

.. poznámka::
V tomto dokumentu i v celém Odoo se termín „certifikát HTTPS“ používá pro platný certifikát.
Certifikát SSL, který umožňuje připojení pomocí protokolu HTTPS.

.. _iot/https_certifikát_iot/generace:

Vytvoření certifikátu pro HTTPS
============================

HTTPS certifikát se generuje automaticky. Když je systém IoT spuštěn (znovu), například po
je spojen s databází Odoo), je odeslán požadavek na adresu `https://www.odoo.com`_, která vrací
HTTPS certifikát, pokud je systém a databáze v souladu s kritérii způsobilosti:

.. _iot/https_certificate_iot/iot-eligibility:

- Databáze musí být **produkční** instancí. Databázová instance by neměla být kopií nebo
duplikát, testovací prostředí nebo vývojové prostředí.
- Odoo předplatné musí být aktivní (stav „Ve výrobě“ (:guilabel:`In Progress`) a mít přidružený :ref:`IoT
řádku předplatného pro IoT (IoT Subscription).

Po obdržení certifikátu:

- Domovská stránka systému IoT je aktualizována na novou adresu s koncovkou „https://“. Klikněte
URL pro zabezpečené spojení typu HTTPS.

.... obrázek: https://www.sslmentor.com/images/iot-new-domain.png
:alt:Aplikace Odoo IoT pro IoT box s doménou .odoo-iot.com.

- Vlaječka „https certifikát“ zobrazuje platnost certifikátu.
Informace najdete kliknutím na tlačítko „IoT systém“ v pravé části domovské stránky.

.... obrázek: https://www.iot.cz/wp-content/uploads/2017/03/https-valid.png
:alt:Stránka domovské stránky IoT boxu s datem platnosti certifikátu HTTPS.

Problémy a chyby při vytváření certifikátu HTTPS
==============================================

Certifikát HTTPS nevygeneruje
---------------------------------------

Příčinou může být několik faktorů, např.:

- Vaše účet není spojen s žádnou předplatnou služby IoT box.
- Předplatné zařízení :ref:`<iot/iot/iot-subscription>` bylo přidáno po připojení IoT.
system do databáze. V tomto případě je nutné aktualizovat stránku domovské stránky systému IoT nebo restartovat:/ref:`restart
restartovat systém IoT, aby se obnovil certifikát HTTPS.
- Firewall brání vytvoření certifikátu HTTPS správně. V takovém případě
deaktivovat firewall, dokud nebude certifikát úspěšně vytvořen.

.. poznámka::
Některé zařízení, např. routery s vestavěným firewallem, mohou zabránit zobrazení certifikátu HTTPS.
generování.

Domovská stránka systému IoT lze získat pomocí jeho IP adresy, ale ne pomocí URL „xxx.odoo-iot.com“.
-------------------------------------------------------------------------------------------------

Kontaktujte svého správce systému nebo sítě, aby vám pomohl vyřešit problém. Problémy související se sítí
za hranicemi služeb podpory Odoo.

- Pokud je možné nastavení DNS v manuálním režimu, aktualizujte nastavení na
použijte „Google DNS <https://developers.google.com/speed/public-dns>“.
- Pokud router tuto funkci nepodporuje, musíte aktualizovat nastavení DNS přímo na každém zařízení.
který komunikuje s systémem Internet of Things a používá „DNS Google“.
<https://developers.google.com/speed/public-dns>`. Návod na konfiguraci DNS pro jednotlivé
jsou k dispozici na webových stránkách příslušného výrobce.

.. poznámka::
   - Některé zařízení IoT, například platební terminály, pravděpodobně nemusí vyžadovat změnu DNS, protože
obvykle přednastavené na vlastní nastavení DNS.
   - Na některých prohlížečích se zobrazí chybový kód týkající se DNS (například „DNS_PROBE_FINISHED_NXDOMAIN“).
zobrazeny.

Chyby
------

Pokud se během instalace vyskytnou nějaké problémy, zobrazí se na domovské stránce systému IoT konkrétní chybový kód.
generaci nebo přijetí certifikátu HTTPS.

.. tip::
Když se dostanete na domovskou stránku systému internetu věcí, automaticky se zkontroluje certifikát HTTPS.
pokusy o vytvoření jednoho, pokud chybí. Pokud se objeví chyba, obnovte stránku a zkontrolujte, zda je
Problém je vyřešen.

„Chyba IOT HTTPS kontroly serveru“
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nastavení serveru chybí, tedy není připojené k instanci Odoo
IoT systém.

Chyba ERR_IOT_HTTPS_CHECK_CERT_READ_EXCEPTION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Při pokusu o přečtení existujícího certifikátu HTTPS došlo k chybě.
Zkontrolujte, zda je soubor certifikátu HTTPS čitelný.

„Chyba při načítání bez přihlašovacích údajů“
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Smlouva a/nebo databáze UUID (Univerzální jedinečný identifikátor) chybí v IoT.

Zkontrolujte, zda jsou oba hodnoty správně nakonfigurované. Chcete-li je aktualizovat, přejděte do
<iot/iot-box/homepage> nebo :ref:`Domovská stránka virtuálního IoT pro Windows <iot/windows-iot/homepage>`.
Klikněte na tlačítko „Nástroje“ (ikona „fa-cogs“), pak klikněte na „Zabezpečení“.

„Chyba při načítání požadavku v protokolu HTTPS“
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Při pokusu o připojení k internetu věcí došlo k neočekávané chybě.
Pravděpodobně kvůli problémům sítě, jako je:

- IoT systém nemá přístup na internet.
- Omezení sítě (např. firewall nebo VPN) brání komunikaci
  https://www.odoo.com.

.. poznámka::
   - Pokud chcete získat podrobné informace o výjimce požadavku včetně informací o chybě, zapněte
režim vývojáře <developer-mode>`, klikněte na kartu systému IoT v aplikaci IoT a klikněte
:guilabel:`Stáhnout protokoly“ na formuláři :ref:`IoT systému <iot/connect/IoT-form>“.
Pro definování úrovně záznamů v protokolovém souboru systému Internet věcí přejděte do nastavení
na stránku „Windows IoT“ nebo odkaz na „Stránka Windows virtuálního IoT“
Klikněte na tlačítko „:icon:`fa-cogs`“ („:guilabel:`cogs`“) a poté na „:guilabel:`Log level`“
na dně stránky.
   - Pokud máte problémy s připojením k síti, kontaktujte svého správce systému nebo sítě.
Tyto služby nejsou součástí podpory Odoo.

„Chyba při načítání požadavku HTTPS“
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IoT systém úspěšně dosáhl na stránky „<https://www.odoo.com>“ a obdržel nečekanou
„Odpověď HTTP (kódy stavu) <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>“.

Tento kód chyby zahrnuje stavový kód HTTP. Například ERR_IOT_HTTPS_LOAD_REQUEST_STATUS 404 znamená
server vrátil odpověď „Stránka nenalezena“.

Aby se tento problém vyřešil:

#Otevřete v prohlížeči adresu _<https://www.odoo.com>_.
údržba.
#|Pokud je stránka „<https://www.odoo.com>“ ve výluce kvůli údržbě, počkejte na její obnovení.
|Pokud je webová stránka funkční, otevřete „ticket podpory“ <https://www.odoo.com/help>
ujistěte se, že do lístku zahrnete třímístný kód stavu HTTPS.

„Chyba IOT HTTPS načítání požadavku bez výsledku“
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IoT systém se úspěšně připojil na stránku <https://www.odoo.com>, ale server odmítl
poskytnout certifikát pro HTTPS.

Zkontrolujte, zda systém a databáze pro internet věcí splňují požadavky na způsobilost.
<iot/https_certifikat_iot/iot-povolení> pro certifikát HTTPS.
