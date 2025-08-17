===========
Odoo Online
===========

„Online Odoo <https://www.odoo.com/trial>“ poskytuje soukromé databáze, které jsou plně spravované a
Odoo. Může se používat pro dlouhodobou výrobu nebo k plnému otestování Odoa včetně
Nastavení, které nevyžaduje kódování.

.. poznámka::
Odoo Online není kompatibilní s vlastními moduly nebo aplikačním obchodem Odoo.

Online databáze Odoo lze přistupovat pomocí jakéhokoliv webového prohlížeče, není tedy nutné instalace na místním počítači.

Chcete-li rychle vyzkoušet Odoo, jsou k dispozici sdílené „demonstrační“ instance („demo <https://demo.odoo.com>“).
Registrace je nutná, ale každá instance žije jen pár hodin.

... odoo_online/databáze:

Správa databází
===================

Pro správu databáze přejděte na „správce databází <https://www.odoo.com/my/databases/>“ a přihlaste se
jako správce databáze.

Všechny hlavní možnosti správy databáze jsou k dispozici po klepnutí na název databáze, s výjimkou
možnost upgradu, kterou lze přistupovat kliknutím na ikonu ve tvaru šipky v kruhu vedle
název databáze. Zobrazuje se pouze v případě, že je k dispozici aktualizace.

.. obrázek: odoo_online/database-manager.png
:alt:Přístup k nastavení správy databáze

- :ref:`odoo_online/aktualizace`
- :ref:`odoo_online/duplicate`
- :ref:`odoo_online/rename`
- :ref:`odoo_online/stahovani`
- :ref:`odoo_online/domains`
- :ref:`odoo_online/tagy`
- :ref:`odoo_online/delete`
- :ref:`odoo_online/kontakt-podpora`
- :ref:`odoo_online/user`
- :ref:`odoo_online/web-services`

... odoo_online/upgrade:

Upgrade
=======

Spustit aktualizaci databáze.

.. viz také:
Pro více informací o procesu upgradu navštivte :ref:`Online upgrad Odoo.
dokumentace <upgrade-request-test>.

.. odoo-online/duplicate:

Duplikát
=========

Vytvořte přesnou kopii databáze, která může být použita k testování bez ohrožení
denní provoz.

.. důležité:
   - Pokud se podíváte na štítek „Pro testování“, všechny externí akce (e-maily, platby a dodání)
Všechny (např. objednávky) jsou v kopii databáze zakázány.
   - Duplicitní databáze vyprší automaticky po 15 dnech.
   - Maximálně pět kopií lze vytvořit pro každou databázi. V mimořádných případech
kontaktujte „podporu <https://www.odoo.com/help>“ a požádejte o zvýšení limitu.

... _odoo_online/rename:

Přejmenovat
======

Přejmenujte databázi a její URL adresu.

... odoo-online/stahování:

Stáhnout
========

Stáhněte si archiv ZIP obsahující zálohu databáze.

.. poznámka::
   - Databáze jsou zálohované každý den podle „SLA Odoo Cloud Hosting
<https://www.odoo.com/cloud-sla>.
   - Pokud je možnost „Stáhnout“ zakázaná, znamená to, že vaše databáze je příliš velká na to, aby byla
stáhnout tímto způsobem. V tom případě kontaktujte podporu Odoo.
na adrese https://www.odoo.com/help, kde můžete požádat o alternativní řešení stahování.

... odoo-online/domény:

Doménová jména
============

Použijte vlastní doménu :doc:`</applications/websites/website/configuration/domain_names>
Přístup k databázi je možný přes jinou adresu URL.

..tip:
Zaregistrujte si doménu zdarma na stránce: <domain-name/register>.

... odoo online / tagy:

Štítky
====

Přidejte štítky, abyste snadno identifikovali a třídili své databáze.

..tip:
Vyhledávat tagy můžete v poli pro vyhledávání.

... odoo_online/smazat:

Smazat
======

Odstranit databázi okamžitě.

.. nebezpečí:
Smazání databáze znamená, že všechna data jsou trvale ztracena. Smazání je okamžité a platí
všem uživatelům. Je doporučeno vytvořit zálohu databáze před jejím smazáním.

Pozorně si přečtěte varovné hlášení a pokračujte pouze v případě, že chápete důsledky smazání databáze
plně pochopil.

.. obrázek: odoo_online/delete.png
:alt:Varování zobrazené před smazáním databáze

.. poznámka::
   - Aby mohl databázi smazat, musí být administrátor.
   - Jméno databáze je ihned k dispozici komukoliv.
   - Smazání databáze, pokud vypršela nebo je spojena s předplatným, není možné.
Pokud máte nějaké dotazy, obraťte se na „Podporu Odoo <https://www.odoo.com/help>“.

... odoo_online/kontaktní podpora:

Kontaktujte nás
==========

Přejděte na stránku podpory „Odoo.com <https://www.odoo.com/help>“ s detaily databáze
předplněné.

... odoo_online/uživatelé:

Zvýšit/snížit počet uživatelů
=====================

Zvou uživatele, zadejte e-mailovou adresu nového uživatele a klikněte na tlačítko „Pozvat“.
uživatelé, klikněte na tlačítko „Přidat další uživatele“.

.. obrázek: odoo_online/invite-users.png
:alt:Zvání uživatele na databázi

Pro odstranění uživatelů vyberte je a klikněte na tlačítko „Odstranit“.

.. viz také:
   - :doc:`/aplikace/obecné/uživatelé`
   - :doc:`odoo_accounts`

... odoo_online/web-services:

Webové služby
============

Pro programové získání seznamu databází zobrazených v
„správce databáze“ („https://www.odoo.com/my/databases“) zavolejte metodu „list“ v modelu
„odoo.database“ prostřednictvím volání metody „Web Service“ (viz dokument „Jak na to: Webové služby“).

Inspirováno příklady uvedenými v :doc:`Webové služby </developera/howtos/web_services>
sekci, tímto způsobem získáte seznam s knihovnou „xmlrpc.client“:

importujte modul xmlrpc.client

USER = "uživatel@doména.tld"
APIKEY = 'vaše_apikey'

kořen = 'https://www.odoo.com/xmlrpc/'
uid = xmlrpc.client.ServerProxy(kořen + 'common').login('openerp', USER, APIKEY)
sock = xmlrpc.client.ServerProxy(kořen + 'objekt')
databáze_seznam = sock.vykonat('openerp', uid, APIKEY, 'odoo.database', 'list')

A zde je příklad s JSON-RPC:

importujte json
import random
importujte modul urllib.request

USER = "uživatel@doména.tld"
APIKEY = 'vaše_apikey'

def json_rpc(url, metoda, parametry):
data = {
"jsonrpc": "2.0",
'metoda': metoda
'params': params
'id': random.randint(0, 1000000000)
       }
req = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers={
„Content-Type“: „application/json“,
       })
odpověď = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
pokud je v odpovědi chyba
vynulovat výjimku (reply['error'])
return reply['result']

def call(url, služba, metoda, *args):
return json_rpc(url, "call", {"service": service, "method": method, "args": args})

url = 'https://www.odoo.com/jsonrpc'
uid = volání(URL, 'common', 'login', 'openerp', USER, APIKEY)
databáze_seznam = volání (URL, „objekt“, „vykonat“, „openerp“, uživatelské jméno, klíč API, „odoo.databáze“, „Seznam“)
