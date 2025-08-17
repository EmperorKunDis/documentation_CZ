============
Webové služby
============

Modul webové služby nabízí společný rozhraní pro všechny webové služby:

- XML-RPC
- JSON-RPC

Objekty obchodu lze také přistupovat prostřednictvím distribuovaného objektu
mechanismus. Všechny lze upravit prostřednictvím klientského rozhraní s kontextovým
Názory.

Odoo je přístupný prostřednictvím rozhraní XML-RPC/JSON-RPC, pro které existují knihovny
existuje v mnoha jazycích.

Knihovna XML-RPC
---------------

Následující příklad je program v Pythonu 3, který interaguje s Odoo.
server s knihovnou „xmlrpc.client“:

importujte modul xmlrpc.client

kořen = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

uid = xmlrpc.client.ServerProxy(kořen + 'common').login(DB, UŽIVATEL, HESLO)
print("Přihlášen jako %s (UID: %d)" % (uživatel, uid))

   # Vytvořit nový poznámkový blok
sock = xmlrpc.client.ServerProxy(kořen + 'objekt')
args = {
„barva“: 8
„poznámka“: „To je poznámka“,
'create_uid': uid
   }
note_id = socket.execute(DB, uid, heslo, 'note.note', 'create', args)

..cvičení: Přidat novou službu do klienta

Napište Pythonový program, který bude schopen odesílat požadavky XML-RPC na počítač s Windows.
Odoo (váš, nebo učitelův). Tento program by měl zobrazit všechny
Jedná se o počet hlasů v jednotlivých schůzích a jejich odpovídající počet míst.
Vytvořit novou relaci pro jeden z kurzů.

......jen řešení

... kódový blok:: python

import funkce
importujte modul xmlrpc.client
HOST = 'localhost'
PORT = 8069
DB = "openacademy"
UŽIVATEL = 'admin'
PASE = 'admin'
KOŘEN = 'http://%s:%d/xmlrpc/' % (HOST, PORT)

            # 1. Přihlášení
uid = xmlrpc.client.ServerProxy(adresář + 'common').login(databáze,uživatel,heslo)
print("Přihlášen jako %s (UID: %d)" % (uživatel, uid))

call = functools.partial(
xmlrpc.client.ServerProxy(kořen + 'objekt').vykonat
DB, UID, PASS)

            # 2. Přečtěte si sezení
sessions = volání funkce openacademy.session s parametry search_read, [], ['name','seats']
pro sezení v sezeních:
print("Sedmá schůze (%s míst)" % (session['seats']))
            # 3. vytvořit novou relaci
session_id = volání funkce openacademy.session s parametrem create,
„název“: „Moje sezení“,
„course_id“: 2
            })

Ve výchozím nastavení se používá pevně dané číslo kurzu. Kód může místo toho vyhledat kurz podle jeho čísla.
jménem::

            # 3. Vytvořit novou lekci pro kurz „Funkční“
course_id = openacademy.course.search([('name','ilike','Functional')]).first()
session_id = volání funkce openacademy.session s parametrem create,
„název“: „Moje sezení“,
'course_id': course_id
            })

.. viz též:
   - :doc:`../reference/external_api`: Podrobný návod k XML-RPC s příklady v různých programovacích jazycích.

Knihovna JSON-RPC
----------------

Následující příklad je program v Pythonu 3, který komunikuje s serverem Odoo.
s knihovnami „urllib.request“ a „json“.
Příklad předpokládá, že je nainstalovaný produktivní aplikace („poznámky“):

importujte json
import random
importujte modul urllib.request

HOST = 'localhost'
PORT = 8069
DB = "openacademy"
USER = 'admin'
PASS = 'admin'

def json_rpc(url, metoda, parametry):
data = {
„jsonrpc“: „2.0“,
„metoda“: metoda
„params“: params
„id“: random.randint(0, 1000000000)
        }
req = urllib.request.Request(url=url, data=json.dumps(data).encode(), hlavičky={
„Content-Type“: „application/json“,
        })
odpověď = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))
pokud je v odpovědi pole "error":
zvednout výjimku (reply["error"]),
return reply["result"]

def call(url, služba, metoda, *args):
return json_rpc(url, "call", {"service": service, "method": method, "args": args})

    # přihlásit se do zadané databáze
url = "http://%s:%s/jsonrpc" % (HOST, PORT)
uid = call(url, "common", "login", DB, UŽIVATEL, HESLO)

    # Vytvořit nový poznámkový blok
args = {
'barva': 8
„memo“: „Toto je další poznámka“,
'create_uid': uid
    }
note_id = volání(url, "objekt", "spustit", DB, uid, HESLO, "poznámka.poznámka", "vytvořit", args)

Příklady lze snadno přizpůsobit z XML-RPC na JSON-RPC.

.. poznámka::

Existuje celá řada vysokých úrovní API pro přístup k Odoo v různých jazycích.
systémy bez explicitního procházení XML-RPC nebo JSON-RPC, jako například:

    * https://github.com/akretion/ooor
    * https://github.com/OCA/odoorpc
    * https://github.com/nicolas-van/openerp-client-lib
    * http://pythonhosted.org/OdooRPC
    * https://github.com/abhishek-jaiswal/php-openerp-lib
