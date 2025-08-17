============
Externí API
============

Odoo je obvykle rozšiřováno interně pomocí modulů, ale mnohé z jeho funkcí
Všechna jeho data jsou také dostupná zvenčí pro externí analýzu nebo
integrace s různými nástroji. Část :ref:`reference/orm/model` API je
je k dispozici prostřednictvím XML-RPC a je přístupný z různých jazyků.

.. důležité:
Od verze PHP 8 může být rozšíření XML-RPC vypnuté výchozí hodnotou.
Podívejte se na „návod <https://www.php.net/manual/cs/xmlrpc.installation.php>“
pro instalační kroky.

.. poznámka::
Přístup k datům prostřednictvím externího API je dostupný pouze v cenových plánech Custom od společnosti Odoo.
externí API není dostupné v tarifech One App Free nebo Standard. Pro více informací
Navštivte stránku „Ceník Odoo <https://www.odoo.com/pricing-plan>“ nebo se obraťte na svého zákaznického poradce.
Úspěšný manažer.

.. viz též:
   - :doc:`Návod k webovým službám <../howtos/web_services>`

Připojení
==========

Konfigurace
-------------

Pokud již máte nainstalovaný Odoo server, můžete použít jeho parametry.

.. důležité:

Pro online instance Odoo (např. <doména>.odoo.com) jsou uživatelé vytvářeni bez
místní heslo (jako uživatel jste přihlášeni přes Odoo Online)
ověřovací systém, nikoliv samotnou instanci). Pro použití XML-RPC v Odoo
Online instance budete potřebovat nastavit heslo na uživatelském účtu.
chcete použít:

    * Přihlaste se do vaší instanci pomocí administrátorského účtu.
    * Přejděte na:menu:Nastavení --> Uživatelé a společnosti --> Uživatelé.
    * Klikněte na uživatele, který chcete používat pro přístup pomocí XML-RPC.
    * Klikněte na položku „Akce“ a vyberte možnost „Změnit heslo“.
    * Zadejte hodnotu „Nové heslo“ a klikněte na „Změnit heslo“.

URL serveru je doména instancí (např.
*https://mojefirma.odoo.com*, databáze je označena názvem
příkladu (*mycompany*) a *username* je přihlašovací jméno uživatele, který byl v nastavení
Jak je vidět na obrazovce pro změnu hesla (*Change Password*).

.. záložky::

...... kódová tabulka::python

url = <vložte adresu serveru>
db = <vložte název databáze>
username = 'admin'
heslo = <vložte heslo pro uživatele administrátora (výchozí: admin)>

... kódová tabulka::ruby

url = <vložte adresu serveru>
db = <vložte název databáze>
uživatelské jméno = „admin“
heslo = <vložte heslo pro uživatele administrátora (výchozí: admin)>

...... kód-tabulka:: php

$url = <vložte adresu serveru>
$db = „<vložte název databáze>“;
$username = "admin";
$password = <vložte heslo pro vašeho administrátora (výchozí: admin)>;

... kódová tabulka:: java

konečná proměnná url je <vložte adresu serveru>.
db = <vložte název databáze>
uživatelské jméno = „admin“,
heslo = <vložte heslo pro vašeho administrátora (výchozí: admin)>;

.....kódová tabulka:: jít

var
url = <vložte adresu serveru>
db = <vložte název databáze>
uživatelské jméno = „admin“
heslo = <vložte heslo pro vašeho administrátora (výchozí: admin)>
       )

... /api/external_api/keys/:

API klíče
~~~~~~~~

.. verze přidána:: 14.0

Odoo podporuje **klíče API** a závisí na modulích nebo nastavení, zda
**požadují** tyto klíče k provádění operací webových služeb.

Jak používat API klíče ve vašich skriptech, je jednoduše nahradit své heslo
pomocí klíče. Přihlášení zůstává v platnosti. Měli byste uchovávat API klíč s maximální opatrností
heslem, protože v podstatě poskytují stejný přístup k vašemu uživatelskému účtu.
účet (i když nemohou být použity k přihlášení přes rozhraní).

Chcete-li přidat klíč do svého účtu, jednoduše se přihlaste
„Předvolby“ (nebo „Můj profil“):

.. obrázek: externí_api/předvolby.png
:align:center

Poté otevřete záložku „Bezpečnost účtu“ a klikněte
:guilabel:`Nový klíč API“:

.. obrázek: externí_api/account-security.png
:align:center

Zadejte popis pro klíč, **tento popis by měl být co nejjasnější.
nejkompletnější možná**: je to jediný způsob, jak identifikovat své klíče
později a zjistit, zda je máte odstranit nebo nechat na místě.

Klikněte na tlačítko „Vytvořit klíč“ a zkopírujte klíč, který je k dispozici. Uložte si klíč
pečlivě**: je to stejně jako vaše heslo a stejně jako vaše heslo
Systém nebude schopen klíč později získat nebo ukázat. Pokud klíč ztratíte
Tento klíč budete muset vytvořit nový (a pravděpodobně i smazat ten stávající).
ztratil).

Jakmile budou vaše klíče nakonfigurovány na účtu, objeví se nad
:guilabel:`Nová klíč API“ tlačítko a budete moci smazat.

.. obrázek: externí_api/smazat-klíč.png
:align:center

**Smazaný klíč API nelze obnovit nebo znovu nastavit**. Budete muset vygenerovat
nový klíč a aktualizovat všechna místa, kde jste používali starý.

Testovací databáze
~~~~~~~~~~~~~

Pro usnadnění průzkumu můžete také požádat o test na adrese https://demo.odoo.com
databáze:

.. záložky::

...... kódová tabulka::python

importujte modul xmlrpc.client
info = xmlrpc.client.ServerProxy('https://demo.odoo.com/start').start()
url, db, username, password = info[‚host‘], info[‚database‘], info[‚user‘], info[‚password‘]

... kódová tabulka::ruby

vyžaduje modul "xmlrpc/client"
info = XMLRPC::Client.new2('https://demo.odoo.com/start').call('start')
url, db, username, password = info[‚host‘], info[‚database‘], info[‚user‘], info[‚password‘]

...... skupina:: PHP

... kódový blok: php

require_once('ripcord.php');
$info = ripcord::client('https://demo.odoo.com/start')->start();
$list = array(„$info[‚host‘]“, „$info[‚database‘]“, „$info[‚user‘]“, „$info[‚password‘]“);

.. poznámka::
Tyto příklady používají knihovnu Ripcord <https://code.google.com/p/ripcord/>
knihovna, která poskytuje jednoduchou API XML-RPC. Ripcord vyžaduje
„Povolení podpory XML-RPC
<https://www.php.net/manual/cs/xmlrpc.installation.php>
instalace.

Protože hovory probíhají přes
„HTTPS“ (<https://cs.wikipedia.org/wiki/HTTP_Secure>), ale také vyžaduje, aby
OpenSSL rozšíření
musí být povolena.

...... skupina-tab:: Java

... kódový blok:: java

konečný XmlRpcClient client = nový XmlRpcClient();

konečná implementace XmlRpcClientConfigImpl start_config = nová;
start_config.setServerUrl(new URL("https://demo.odoo.com/start"));
konečnou mapu <String, String> info = (Map<String, String>)client.execute(
start_config, "start", List.empty());

konečné proměnné String url = info.get("host"),
db = info.get("database"),
uživatelské jméno = info.get("user"),
heslo = info.get("heslo");

.. poznámka::
Tyto příklady používají knihovnu Apache XML-RPC <https://ws.apache.org/xmlrpc/>_.

Výčet příkladů nezahrnuje dovozy, protože tyto dovozy nemohly být
Pastuji do kódu.

...... skupinová tabulka: Go

... kódový blok:: go

klient, err := xmlrpc.NewClient("https://demo.odoo.com/start", nil)
pokud je chyba nenulová,
log.Fatal(err)
         }
info:=map[string]string{}}
klient.Volání("start", nil, &info)
url = info["host"].(String)
db = info["database"].(string)
uživatelské jméno = info["uživatel"].(string)
heslo = info["heslo"].(string)

.. poznámka::
Tyto příklady používají knihovnu `github.com/kolo/xmlrpc <https://github.com/kolo/xmlrpc>`_.

Výčet příkladů nezahrnuje dovozy, protože tyto dovozy nemohly být
Pastuji do kódu.

Přihlášení
----------

Odoo vyžaduje, aby uživatelé API byli ověřeni předtím, než mohou provést většinu dotazů.
Data.

Konektor „xmlrpc/2/common“ poskytuje metakalldy, které nevyžadují
autentizace, jako je autentizace sama o sobě nebo získání verze
informace. Před pokusem o připojení je třeba ověřit, zda jsou informace správné.
Pro ověření je nejjednodušší požádat o verzi serveru.
ověření samotné je provedeno funkcí „authenticate“
vrací uživatelské identifikátory („uid“) používané v ověřených voláních místo
Přihlášení.

.. záložky::

...... kódová tabulka::python

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.verze()

... kódová tabulka::ruby

common = XMLRPC::Client.new2("#{url}/xmlrpc/2/common")
common.call('verze')

...... kód-tabulka:: php

$common = ripcord::client("$url/xmlrpc/2/common");
$common->verze();

... kódová tabulka:: java

konečný XmlRpcClientConfigImpl běžná konfigurace = nový XmlRpcClientConfigImpl();
common_config.setServerURL(new URL(String.format("%s/xmlrpc/2/common", url)));
client.spustí(obecné konfigurace, "verze", prázdnou seznam);

.....kódová tabulka:: jít

klient, err := xmlrpc.NewClient(fmt.Sprintf("%s/xmlrpc/2/common", url), nil)
pokud nebyl err nulový,
log.Fatal(err)
      }
common := map[string]any{}
pokud se nejedná o chybu, tak
log.Fatal(err)
      }

Výsledek:

.. kódový blok: JSON

   {
„server_version“: „13.0“,
"server_version_info": [13, 0, 0, "final", 0]
„server_serie“: „13.0“,
„verze protokolu“: 1
   }


.. záložky::

...... kódová tabulka::python

uid = common.autentizace(db, jméno_uživatele, heslo, {})

... kódová tabulka::ruby

uid = common.call('authenticate', db, username, password, {})

...... kód-tabulka:: php

$uid = $common->authenticate($db, $uživatelské_jméno, $heslo, array());

... kódová tabulka:: java

int uid = (int)client.execute(common_config, "authenticate", asList(db, username, password, new HashMap<>()));

.....kódová tabulka:: jít

var uid int64
pokud se stane chyba, tak:
db, uživatelské jméno a heslo.
map[string]jakýkoliv{}
} else err = nil;
log.Fatal(err)
      }

... /api/external_api/calling_methods/:

Metody volání
===============

Druhým koncovým bodem je „xmlrpc/2/object“. Tento se používá k volání metod odoo.
modely prostřednictvím funkce „execute_kw“ RPC.

Každý volání funkce „execute_kw“ má následující parametry:

* databáze, řetězec
* uživatelské ID (získané pomocí funkce „ověřit“), celé číslo
* uživatelské heslo, řetězec
* název modelu, řetězec
* název metody, řetězec
* seznam parametrů, které jsou předány podle pozice
* mapování parametrů, které se předávají klíčovým slovem (volitelné)

Příklad:

Například pro vyhledávání záznamů v modelech „res.partner“ můžeme volat
„hledání jména“ s „jmenem“, které bylo předáno jako parametr, a „limit“, který byl předán jako
klíčové slovo (abyste získali maximálně 10 výsledků):

... záložky::

.. kódový blok:: python

modely = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
models.execute_kw(db, uid, heslo, 'res.partner', 'name_search', ['foo'], { 'limit': 10 })

... kódový blok::ruby

modely = XMLRPC::Client.new2(„#{url}/xmlrpc/2/object“).proxy
models.execute_kw(db, uid, heslo, 'res.partner', 'name_search', ['foo'], limit=10)

.. kód-tab:: php

$modely = ripcord::klient(„$url/xmlrpc/2/object“);
$models->execute_kw($db, $uid, $password, 'res.partner', 'name_search', array('foo'), array('limit' => 10));

... kódový záhlaví:: java

konečný XmlRpcClient models = nový XmlRpcClient() {
setConfig(new XmlRpcClientConfigImpl() {{
setServerURL(new URL(String.format("%s/xmlrpc/2/object", url))));
             }});
         }};
modely.vykonat("vykonat_klíčové_slovo", jakoList(
db, uid, heslo
"partner", "hledat jméno"
jakoList("foo")
nový HashMap() {{ put("limit", 10); }}
         ));

.. kódová tabulka: jít

model, err := xmlrpc.NewClient(fmt.Sprintf("%s/xmlrpc/2/object", url), nil)
pokud je chyba nenulová,
log.Fatal(err)
         }
var výsledek bool
pokud se stane chyba, tak:
db, uid, heslo
"partner", "hledat jméno"
[]string{"foo"}}
map[string]bool{"limit": 10}
} else err = nil;
log.Fatal(err)
         }

Výsledek:

... kódový blok: JSON

true

Seznamy záznamů
------------

Záznamy lze zobrazit a filtrovat pomocí metody :meth:`~odoo.models.Model.search`.

Metoda ~odoo.models.Model.search je povinná
Filtr domén, který se vrací.
identifikátory databáze všech záznamů odpovídajících filtru.

Příklad:

Na seznam firemních zákazníků například:

... záložky::

.. kódový blok:: python

model.vykonat_klauzuli(db, uid, heslo, 'res.partner', 'hledání', [[['je_firma', '==', True]]])

... kódový blok::ruby

model.spustit_kombinaci(db, uid, heslo, 'res.partner', 'hledat', [[['je_firma', '==', True]])

.. kód-tab:: php

$model->spustit_klauzuli($db, $uid, $heslo, 'res.partner', 'hledat', array(array(array('je_firma', '=' => true)))));

... kódový záhlaví:: java

asList((Object[])models.execute("execute_kw", asList(
db, uid, heslo
"partner", "hledat"
jakoList(jakoList(
jakoList("is_company", "==", true))
         )));

.. kódová tabulka: jít

var rekordy []int64
pokud se stane chyba, tak:
db, uid, heslo
"partner", "hledat"
[]any{}
{}["je_firma", "==", true],
             }},
} else err = nil;
log.Fatal(err)
         }

Výsledek:

... kódový blok: JSON

      [7, 18, 12, 14, 17, 19, 8, 31, 26, 16, 13, 20, 30, 22, 29, 15, 23, 28, 74]

Stránkování
~~~~~~~~~~

Výchozí hledání vrátí id všech záznamů, které odpovídají zadaným kritériím.
podmínky, které mohou být obrovským počtem. „Offset“ a „Limit“ parametry
pouze získat podmnožinu všech shodných záznamů.

Příklad:

... záložky::

.. kódový blok:: python

models.execute_kw(db, uid, heslo, 'res.partner', 'search', [[['is_company', '=', True]]], {'offset': 10, 'limit': 5})

... kódový blok::ruby

models.execute_kw(db, uid, heslo, 'res.partner', 'search', [[['is_company', '=', true]]], {offset: 10, limit: 5})

.. kód-tab:: php

$models->execute_kw($db, $uid, $password, 'res.partner', 'search', array(array(array('is_company', '=', true))), array('offset' => 10, 'limit' => 5));

... kódový záhlaví:: java

asList((Object[])models.execute("execute_kw", asList(
db, uid, heslo
"partner", "hledat"
jakoList(jakoList(
is_company = (asList("is_company", "=", true)),
nový HashMap() {{put("offset", 10); put("limit", 5);}}
         )));

.. kódová tabulka: jít

var rekordy []int64
pokud se stane chyba, tak:
db, uid, heslo
"partner", "hledat"
[]any{}
{}["je_firma", "==", true],
             }},
map[string]int64{"offset": 10, "limit":  5}
} else err = nil;
log.Fatal(err)
         }

Výsledek:

... kódový blok: JSON

      [13, 20, 30, 22, 29]

Počítáme záznamy
-------------

Nebo se pokusit získat možná obrovský seznam záznamů a počítat je.
Metoda ~odoo.models.Model.search_count() může být použita k získání
jen počet záznamů odpovídajících dotazu. Je stejný
filtr jako doménu
:metoda:~odoo.models.Model.search a žádné další parametry.

Příklad:

... záložky::

.. kódový blok:: python

models.execute_kw(db, uid, heslo, 'res.partner', 'search_count', [[['is_company', '==', True]]])

... kódový blok::ruby

models.execute_kw(db, uid, heslo, 'res.partner', 'search_count', [[['is_company', '=', True]])

.. kód-tab:: php

$models->execute_kw($db, $uid, $password, 'res.partner', 'search_count', array(array(array('is_company', '=' => true)))));

... kódový záhlaví:: java

(int)modely.vykonat("vykonat_klíčová slova", jako seznam
db, uid, heslo
"res.partner", "search_count",
jakoList(jakoList(
jakoList("is_company", "==", true))
         ));

.. kódová tabulka: jít

var počet int64
pokud se stane chyba, tak:
db, uid, heslo
"res.partner", "search_count",
[]any{}
{}["je_firma", "==", true],
             }},
} else err != nil {
log.Fatal(err)
         }

Výsledek:

... kódový blok: JSON

      19

.. poznámka::
Volání metody „search“ a následně „search_count“ (nebo naopak) nemusí být
Pokud se k serveru připojí další uživatelé, budou mít stejné výsledky.
Mohlo se změnit mezi hovory.

Číst záznamy
------------

Záznamová data jsou přístupná metodou :meth:`~odoo.models.Model.read`,
Tento nástroj přijímá seznam identifikátorů (vrácených
:meth:`~odoo.models.Model.search`) a možná seznam polí, na která chcete
získat. Výchozí nastavení získá všechny pole, které může číst aktuální uživatel
Ten se obvykle pohybuje v obrovských částkách.

Příklad:

... záložky::

.. kódový blok:: python

ids = models.execute_kw(db, uid, heslo, 'res.partner', 'search', [[['is_company', '==', True]]], {'limit': 1})
[záznam] = model.vykonat_klíčové_slovo(db, uid, heslo, 'res.partner', 'číst', [ids])
          # počítat počet polí, která jsou zobrazena výchozím způsobem
len(record)

... kódový blok::ruby

ids = models.execute_kw(db, uid, heslo, 'res.partner', 'search', [[["is_company", "=", true]]], {limit: 1})
record = model.spustit_kws(db, uid, heslo, 'res.partner', 'read', [ids]).first
          # počítat počet polí, která jsou zobrazena výchozím způsobem
délka záznamu

.. kód-tab:: php

$ids = $modely->vykonat_klauzuli($db, $uid, $heslo, 'res.partner', 'hledání', array(array(array('je_firma', '=' => true))), array('limit' => 1));
$záznamy = $modely->vykonat_kw($db, $uid, $heslo, 'res.partner', 'čtení', array($id));
          // count the number of fields fetched by default
count($records[0]);

... kódový záhlaví:: java

konečný seznam id = jakoList (((Objekt) []) models.vykonat (
"execute_kw", jakoList(
db, uid, heslo
"partner", "hledání"
asList(asList(
asList("is_company", "=", true)),
nový hashMap() {{ put("limit", 1); }}}));
final Map record = (Map) ((Object []) models.execute(
"execute_kw", jakoList(
db, uid, heslo
"partner.res", "číst"
jakoList(idy)
              )
          ))[0];
          // count the number of fields fetched by default
record.size();

.. kódová tabulka: jít

var ids [][int64]
pokud se stane chyba, tak:
db, uid, heslo
"partner", "hledat"
[]any{}
{}["je_firma", "==", true],
             }},
map[string]int64{"limit": 1}
} else err = nil;
log.Fatal(err)
         }
var rekordy []any
pokud se stane chyba, tak:
db, uid, heslo
"partner.res", "číst"
idy
} else err = nil;
log.Fatal(err)
         }
         // count the number of fields fetched by default
count:=len(záznamů)

Výsledek:

... kódový blok: JSON

      121

Naopak vybrat jen tři pole považovaná za zajímavá.

... záložky::

.. kódový blok:: python

models.execute_kw(db, uid, heslo, 'res.partner', 'read', [ids], {'fields': ['name', 'country_id', 'comment']}))

... kódový blok::ruby

models.execute_kw(db, uid, heslo, 'res.partner', 'read', [ids], {fields: ['name', 'country_id', 'comment']})

.. kód-tab:: php

$modely->vykonaji_kontrolu($db, $uid, $heslo, 'res.partner', 'read', array($ids), array('fields' => array('name', 'country_id', 'comment')));

... kódový záhlaví:: java

asList((Object[])models.execute("execute_kw", asList(
db, uid, heslo
"partner.res", "číst"
jakoList(id)
nový HashMap() {{{
put("fields", jakoList("jméno","země_id","komentář"));
             }}
         )));

.. kódová tabulka: jít

var pole záznamů []map[string]jakýkoli
pokud se stane chyba, tak:
db, uid, heslo
"partner.res", "číst"
idy
map[string][]string{
"pole": { "název", "země_id", "komentář" }
             },
} else err = nil;
log.Fatal(err)
         }

Výsledek:

... kódový blok: JSON



.. poznámka::
I když pole „id“ není požadováno, vždy se vrátí.

Seznam záznamových polí
------------------

Funkce ~odoo.models.Model.fields_get() může být použita k prohlížení
modelovým polím a zjistit, která se zdá být zajímavá.

Protože vrací velké množství metainformací (je také používána klienty).
programy) by měly být před tiskem filtrovány, nejzajímavější položky
pro člověka je „string“ (název pole) a „help“ (pomocný text).
k dispozici) a „typ“ (abyste věděli, jaké hodnoty očekávat nebo poslat).
aktualizace záznamu).

Příklad:

... záložky::

... kód-tab:: python

models.execute_kw(db, uid, heslo, "res.partner", "fields_get", [], {"attributes": ["string", "help", "type"]})

... kódový záhlaví: ruby

model.spustit_kontrakt(db, uid, heslo, 'res.partner', 'fields_get', [], {atributy: ['string', 'help', 'type']})

... kód-tab:: php

$modely->spustit_kód($db, $uid, $heslo, 'res.partner', 'fields_get', array(), array('attributes' => array('string', 'help', 'type')));

... kód-tab:: java

(Map<String, Map<String, Objekt>>)modely.vykonat("vykonat_klíčové slovo", jako seznamu
db, uid, heslo
"res.partner","fields_get"
list.empty(),
nový HashMap() {{{
put("attributes", jakoList("string", "help", "type"));
               }}
           ));

.. kódová tabulka:: jít

recordFields:=map[string]string{}}
pokud se stane chyba,
db, uid, heslo
"res.partner","fields_get"
[]nebo{}
map[string][]string {
"atributy": {"string", "pomoc", "typ"}
               },
} else err = nil;
log.Fatal(err)
           }

Výsledek:

... kódový blok: JSON

      {
„ean13“: {
"typ": "char"
"pomoc": "BarCode"
„string“: „EAN13“
          },
„součet položek vlastního majetku“:
„typ“: „many2one“,
„Pomoc“: „Fiskální pozice určí daně a účty používané pro partnery.“
„string“: „Daňová pozice“
          },
„validní přihlášení“:
„typ“: „logická“,
"pomoc": ""
„string“: „Token pro registraci je platný“
          },
„datum_lokalizace“:
„typ“: „datum“,
"pomoc": ""
„string“: „Geolokace Datum“
          },
„ref_company_ids“: {
„typ“: „jedna k mnoha“,
"pomoc": ""
„string“: „Společnosti, které odkazují na partnery“
          },
„počet objednávek na prodej“:
„typ“: „celé číslo“,
"pomoc": ""
„string“: „Počet objednávek“
          },
„počet objednávek“:
„typ“: „celé číslo“,
"pomoc": ""
„string“: „Číslo objednávky“
          },

Hledat a číst
---------------

Protože je velmi běžná, nabízí Odoo
:meth:`~odoo.models.Model.search_read` zkratka, jak již název napovídá, je
součástí je metoda ~odoo.models.Model.search, která následuje
:metoda: ~odoo.models.Model.read, ale vyhýbá se tomu, aby bylo nutné provést dvě požadavky
a držet si je po ruce.

Jeho argumenty jsou podobné jako u metody :meth:`~odoo.models.Model.search`, ale
Může také přijímat seznam „polí“ (jako například metoda Model.read).
Pokud se tato pole nezobrazí, bude zobrazeno všechna pole shodná s hledanými poli.

Příklad:

... záložky::

.. kódový blok:: python

models.execute_kw(db, uid, heslo, 'res.partner', 'search_read', [['is_company', '=', True]], {'fields': ['name', 'country_id', 'comment'], 'limit': 5})

... kódový blok::ruby

models.execute_kw(db, uid, heslo, "res.partner", "search_read", [["is_company", "=", true]], {fields: ["name", "country_id", "comment"], limit: 5})

.. kód-tab:: php

$models->execute_kw($db, $uid, $password, 'res.partner', 'search_read', array(array(array('is_company', '=', true))), array('fields'=>array('name', 'country_id', 'comment'), 'limit'=>5));

... kódový záhlaví:: java

asList((Object[])models.execute("execute_kw", asList(
db, uid, heslo
"res.partner", "hledat čtení"
jakoList(jakoList(
is_company = (asList("is_company", "=", true)),
nový HashMap() {{{
put("fields", jakoList("jméno","země_id","komentář"));
put("limit", 5);
             }}
         )));

.. kódová tabulka: jít

var pole záznamů []map[string]jakýkoli
pokud se stane chyba, tak:
db, uid, heslo
"res.partner", "hledat čtení"
[]any{}
{}["je_firma", "==", true],
             }},
map[string]jakýkoliv typ{
"pole": []string{"jméno", "země", "komentář"}
"limit":  5
             },
} else err = nil;
log.Fatal(err)
         }

Výsledek:

... kódový blok: JSON

      [
          {
„komentář“: false,
„country_id“: [ 21, „Belgie“ ]
"id": 7,
"název": "Agrolait"
          },
          {
„komentář“: false,
"země_id": [ 76, "Francie" ]
"id": 18,
„název“: „Axelor“
          },
          {
„komentář“: false,
„země_id“: [ 233, „Spojené království“ ]
„id“: 12
„název“: „Banka Bohatých a synů“
          },
          {
„komentář“: false,
"země_id": [ 105, "Indie" ]
"id": 14,
"název": „Nejlepší designéři“
          },
          {
„komentář“: false,
"země_id": [ 76, "Francie" ]
„id“: 17
„jméno“: „Camptocamp“
          }
      ]

Vytvářejte rekordy
--------------

Záznamy modelu vytváří metoda :meth:`~odoo.models.Model.create`.
Metoda vytvoří jediný záznam a vrátí jeho identifikátor databáze.

Metoda ~odoo.models.Model.create přijímá pole polí s hodnotami, které se používají
pro inicializaci záznamu. Pro každý prvek, který má výchozí hodnotu a není
Pokud je hodnota nastavena prostřednictvím mapovacího argumentu, použije se výchozí hodnota.

Příklad:

... záložky::

.. kódový blok:: python

id = model.spustit_kontrakt(db, uid, heslo, 'res.partner', 'create', [{'jméno': 'Nová firma'}])

... kódový blok::ruby

id = model.spustit_kód(db, uid, heslo, 'res.partner', 'create', [{název: "Nová partnerka"}]),

.. kód-tab:: php

$id = $modely->vykonat_klauzuli($db, $uid, $heslo, 'res.partner', 'create', array(array('name' => "New Partner")));

... kódový záhlaví:: java

final int id = (Integer)models.execute("execute_kw", Arrays.asList(
db, uid, heslo
"res.partner", "vytvořit"
jakoList(mapu() {{ put("name", "Nový partner"); }})
         ));

.. kódová tabulka: jít

var id int64
pokud se stane chyba, tak:
db, uid, heslo
"res.partner", "vytvořit"
map[string]string{}
{"název": "Nový partner"}
             },
} else if err != nil {
log.Fatal(err)
         }

Výsledek:

... kódový blok: JSON

      78

.. varování:
Zatímco většina hodnotových typů je taková, jak byste očekávali (celé číslo pro
:třída: ~odoo.pole.Celé číslo, pro pole :třída: ~odoo.pole.Text
nebo :třída:`~odoo.fields.Text`)

   - :třída odoo.fields.Datum, třída odoo.fields.Datum a čas
:třída: `~odoo.fields.Binary`, používají se pro hodnoty typu „string“
   - :třída odoo.fields.One2many a třída odoo.fields.Many2many
použít speciální příkazový protokol, který je podrobně popsán v metodě :meth:`Dokumentace
metoda pro zápis do databáze <odoo.models.Model.write>.

Aktualizace záznamů
--------------

Záznamy lze aktualizovat pomocí metody :meth:`~odoo.models.Model.write`. Ta přijímá
seznam aktualizovaných záznamů a mapování aktualizovaných polí na hodnoty podobné
metoda:meth:`~odoo.models.Model.create`.

Můžete aktualizovat více záznamů najednou, ale všechny budou mít stejné
hodnoty pro nastavení polí. Není možné provádět
„vypočítané“ aktualizace (kde hodnota, kterou nastavujete, závisí na stávající hodnotě
rekord).

Příklad:

... záložky::

.. kódový blok:: python

modely.spustit_kód(db, uid, heslo, 'res.partner', 'write', [id, {'jméno':'Novější partner'}])
         # získat název souboru po změně
model.spustit_kontrakt(db, uid, heslo, 'res.partner', 'čtení', [[id], ['jméno zobrazené v seznamu kontaktů']])

... kódový blok::ruby

model.spustit_kontrakt(db, uid, heslo, 'res.partner', 'write', [id, {'jméno': 'Novější partner'}])
         # získat název souboru po změně
model.spustit_kontrakt(db, uid, heslo, 'res.partner', 'čtení', [[id], ['jméno zobrazené v seznamu kontaktů']])

.. kód-tab:: php

$modely->vykonaji_kontrolu($db, $uid, $heslo, 'res.partner', 'write', array(array($id), array('name'=>"Novější partner")));
         // get record name after having changed it
$modely->spustit_kód($db, $uid, $heslo,
'partner', 'čtení', array(array($id), array('zobrazit_jméno')));

... kódový záhlaví:: java

modely.vykonat("vykonat_klíčové_slovo", jakoList(
db, uid, heslo
"res.partner", "write",
jakoList(
jakoList(id)
nový HashMap() {{ put("name", "Novější partner"); }}
             )
         ));
         // get record name after having changed it
asList((Object[])models.execute("execute_kw", asList(
db, uid, heslo
"partner.res", "číst"
jakoList(jakoList(id), jakoList("display_name"))
         )));

.. kódová tabulka: jít

var výsledek bool
pokud se stane chyba, tak:
db, uid, heslo
"res.partner", "write",
[]nevím{}
[]int64{id}
map[string]string{"jméno": "Nový partner"}}
             },
} else err = nil;
log.Fatal(err)
         }
         // get record name after having changed it
var rekord []any
pokud se stane chyba, tak:
db, uid, heslo
"partner", "jméno",
[]nevím{}
[]int64{id}
             },
} else err != nil {
log.Fatal(err)
         }

Výsledek:

... kódový blok: JSON

[["Novější partner", 78]]

Smazat záznamy
--------------

Záznamy lze v hromadném režimu smazat, pokud je poskytnete jejich id.
:meth:`~odoo.models.Model.unlink`.

Příklad:

... záložky::

.. kódový blok:: python

model.vykonat_kód(db, uid, heslo, 'res.partner', 'unlink', [id])
         # zjistit, zda smazaný záznam stále v databázi je
model.spustit_klíčové_slovo(db, uid, heslo, 'res.partner', 'hledat', [['id', '==', id]])

... kódový blok::ruby

model.vykonat_kód(db, uid, heslo, 'res.partner', 'unlink', [id])
         # zjistit, zda smazaný záznam stále v databázi je
model.spustit_klíčové_slovo(db, uid, heslo, 'res.partner', 'hledat', [['id', '==', id]])

.. kód-tab:: php

$models->execute_kw($db, $uid, $password, 'res.partner', 'unlink', array(array($id)));
         // check if the deleted record is still in the database
$models->execute_kw(
$db, $uid, $password, 'res.partner', 'search', array(array(array('id', '=' ,$id))))
         );

... kódový záhlaví:: java

modely.vykonat("vykonat_klíčové_slovo", jakoList(
db, uid, heslo
"partner", "odpojit"
jakoList(jakoList(id)));
         // check if the deleted record is still in the database
asList((Object[])models.execute("execute_kw", asList(
db, uid, heslo
"partner", "hledat"
jakoList(jakoList(jakoList("id", "=", 78)))
         )));

.. kódová tabulka: jít

var výsledek bool
pokud se stane chyba, tak:
db, uid, heslo
"partner", "odpojit"
[]nevím{}
[]int64{id}
             },
} else err = nil;
log.Fatal(err)
         }
         // check if the deleted record is still in the database
var rekord []any
pokud se stane chyba, tak:
db, uid, heslo
"partner", "hledat"
[]any{}
["id" => id]
             }},
} else err != nil {
log.Fatal(err)
         }

Výsledek:

... kódový blok: JSON

      []

Inspekce a sebereflexe
----------------------------

Předtím jsme používali metodu :meth:`~odoo.models.Model.fields_get`, abychom získali
model a od začátku používá libovolný model, Odoo ukládá
většina metadat o modelech je uložena v několika metamodelách, které umožňují
systém a měnit modely a pole (s některými omezeními) na létu.
XML-RPC.

.. odkaz/webová služba/prohlídka/modely:

„ir.model“
~~~~~~~~~~~~

Poskytuje informace o modelech Odoo prostřednictvím různých polí.

„jméno“
čitelný popis modelu
„model“
název každého modelu v systému
„stát“
zda se model vytvořil v Pythonovém kódu („base“) nebo tím, že byl
záznam „ir.model“ („manuální“)
„field_id“
seznam polí modelu prostřednictvím :class:`~odoo.fields.Many2one`.
:ref:`reference/webservice/inspection/fields`
„view_ids“
:třída: ~odoo.pole.One2many do :ref:`../reference/user_interface/view_architectures`.
definované pro model
„access_ids“
:třída:~odoo.fields.One2many
:ref:`reference/security/acl` nastavené na modelu

„ir.model“ lze použít k

- Zeptejte se systému na nainstalované modely (jako předpoklad pro provedení operací)
na modelu nebo prozkoumat obsah systému.
- Získat informace o konkrétním modelu (obvykle pomocí pole s položkami).
spojené s ním.
- Vytvářet nové modely dynamicky přes RPC.

.. důležité:
   * Název vlastního modelu musí začínat „x_“.
   * „Stát“ musí být nastaven na „ruční“, jinak se model nebude chovat správně.
nebude nahrána.
   * Do vlastního modelu nelze přidávat nové metody, pouze pole.

Příklad:

Základní model obsahuje pouze „výchozí“ pole.
na všech modelech:

... záložky::

.. kódový blok:: python

model.spustit_kontrolu(db, uid, heslo, 'ir.model', 'create', [
„vlastní model“
„model“: „x_custom_model“,
„stát“: „ruční“,
         }])
models.execute_kw(db, uid, heslo, "x_custom_model", "fields_get", [], {"attributes": ["string", "help", "type"]}))

.. kód-tab:: php

$models->execute_kw($db, $uid, $password, 'ir.model', 'create', array(array(
'název' => "Vlastní model",
'model' => 'x_custom_model',
"stát" => "ruční"
         )));
$modely->spustit_kód($db, $uid, $heslo, 'x_custom_model', 'fields_get', array(), array('attributes' => array('string', 'help', 'type')));

... kódový blok::ruby

model.spustit_kontrolu(db, uid, heslo, 'ir.model', 'create', [
jméno: „Vlastní model“,
model: 'x_custom_model',
stav: 'manuální'
         }])
pole = modely.vykonat_kód(db, uid, heslo, "vlastní model", "pole získání", [], { atributy: %w(string pomoc typ) })

... kódový záhlaví:: java

model.spustit(
„execute_kw“, jako seznam
db, uid, heslo
"ir.model", "vytvořit"
jakoList(nový HashMap<String, Objekt>()) {
put("name", "Vlastní model");
put("model", "x_custom_model");
put("state", "manuální");
                 }})
         ));
final Map<String, Object> fields = models.execute(
„execute_kw“, jako seznam
db, uid, heslo
"vlastní model x_custom_model", "pole získání"
emptyList()
nový HashMap<String, Objekt> () {{{
put("attributes", jako seznam (
"řetězec"
„pomoc“,
"typ");
                 }}
         ));

.. kódová tabulka: jít

var id int64
pokud se stane chyba, tak:
db, uid, heslo
"ir.model", "create",
map[string]string{}
                 {
„název“: „Vlastní model“,
„model“: „x_custom_model“,
„stát“: „ruční“,
                 },
             },
} else if err != nil {
log.Fatal(err)
         }
recordFields: = map[string]string{}
pokud se stane chyba, tak:
db, uid, heslo
"vlastní model", "pole získat"
[]nebo{}
map[string][]string{
"atributy": {"string", "pomoc", "typ"}
             },
} else err = nil;
log.Fatal(err)
         }

Výsledek:

... kódový blok: JSON

      {
„create_uid“: {
„typ“: „many2one“,
"string": "Vytvořeno"
          },
„create_date“: {
"typ": "datum",
"string": "Vytvořeno dne"
          },
„__poslední aktualizace“:
"typ": "datum",
„string“: „Datum poslední aktualizace“
          },
„write_uid“: {
„typ“: „many2one“,
„string“: „Poslední aktualizace od“
          },
„write_date“: {
"typ": "datum",
"string": "Poslední aktualizace:"
          },
„display_name“: {
"typ": "char"
„string“: „Zobrazované jméno“
          },
„id“: {
„typ“: „celé číslo“,
"string": "ID"
          }
      }

.. odkaz/webová služba/prohlídka/pole:

„ir.model.fields“
~~~~~~~~~~~~~~~~~~~

Poskytuje informace o polích modelů Odoo a umožňuje přidávat
Pole vlastních atributů bez použití kódu Pythonu.

„model_id“
:třída:~odoo.fields.Many2one
:ref:`reference/webservice/inspection/models`, ke kterému patří pole
„jméno“
technické jméno pole (používané v příkazech „číst“ nebo „zapisovat“)
„Popis pole“
použitelná pro člověka název pole (např. „string“ v funkci „fields_get“).
„Typ“
typ pole, které chcete vytvořit
„stát“
zda pole bylo vytvořeno pomocí kódu Pythonu („base“).
„ir.model.fields“ („manuální“)
„povinné“, „čtení pouze“, „přeložit“
umožňuje odpovídající vlajku na hřišti
„skupiny“
:ref:`kontrola přístupu na úrovni pole <odkaz/bezpečnost/pole>“
:třída: ~odoo.fields.Many2many do „res.groups“
„vybrané“, „velikost“, „na smazání“, „vztah“, „pole vztahu“, „doména“
specifické vlastnosti a konfigurace, viz :ref:`pole
pro podrobnosti viz dokumentace <odkaz/orm/fields>

.. důležité:
   - Stejně jako vlastní modely, pouze nové pole s atributem „state“ nastaveným na hodnotu „manual“ jsou aktivovány jako skutečné.
pole na modelu.
   - Pole vypočítaná pomocí „ir.model.fields“ nelze přidat, některé informace o poli
Nelze nastavit ani výchozí hodnotu (defaults), ani se změnou hodnoty spojené události (onchange).

Příklad:

... záložky::

.. kódový blok:: python

id = models.execute_kw(db, uid, heslo, "ir.model", "create", [
„vlastní model“
„model“: „x_custom“,
„stát“: „ruční“,
         }])
model.spustit_kód(db, uid, heslo, 'ir.model.fields', 'create', [
"model_id": id
'name': 'x_name',
'typ': 'char',
„stát“: „ruční“,
"vyžadováno": True,
         }])
record_id = model.vykonat_klauzuli(db, uid, heslo, 'x_custom', 'create', [{"x_name": "test record"}])
model.vykonat_kód(db, uid, heslo, 'x_custom', 'read', [record_id])

.. kód-tab:: php

$id = $modely->vykonat_klauzuli($db, $uid, $heslo, "ir.model", "vytvorit", array(array(
'název' => "Vlastní model",
'model' => 'x_custom',
"stát" => "ruční"
         )));
$models->execute_kw($db, $uid, $password, 'ir.model.fields', 'create', array(array(
'model_id' => $id,
"název" => "x_name",
'typ' => 'char',
„stát“ => „ruční“,
"required" => true
         )));
$record_id = $models->execute_kw($db, $uid, $password, 'x_custom', 'create', array(array('x_name' => "test record")));
$modely->vykonaji_klicove_slovo($db, $uid, $heslo, "x_custom", "read", array(array($record_id))));

... kódový blok::ruby

id = models.execute_kw(db, uid, heslo, "ir.model", "create", [
jméno: „Vlastní model“,
model: „x_custom“,
stav: 'manuální'
         }])
model.spustit_kód(db, uid, heslo, 'ir.model.fields', 'create', [
model_id: id
jméno: "x_name",
typ: "char"
stav: "ruční",
povinné: true
         }])
record_id = model.vykonat_kws(db, uid, heslo, 'x_custom', 'create', [{x_name: "test record"}]
model.vykonat_kód(db, uid, heslo, 'x_custom', 'read', [record_id])

... kódový záhlaví:: java

final int id = (Integer)models.execute(
„execute_kw“, jako seznam
db, uid, heslo
"ir.model", "vytvořit"
jakoList(nový HashMap<String, Objekt>()) {
put("name", "Vlastní model");
put("model", "x_custom");
put("state", "manuální");
                 }})
         ));
model.spustit(
„execute_kw“, jako seznam
db, uid, heslo
"ir.model.fields", "vytvořit",
jakoList(nový HashMap<String, Objekt>()) {
model_id(id);

put("type", "char");
put("state", "manuální");
put("required", true);
                 }})
         ));
konečné celé číslo record_id = (celé číslo) models.execute(
„execute_kw“, jako seznam
db, uid, heslo
„x_custom“, „vytvořit“
jakoList(nový HashMap<String, Objekt>()) {
put("x_name", "test record");
                 }})
         ));

client.execute(
„execute_kw“, jako seznam
db, uid, heslo
"x_custom", "čtení"
jakoList(jakoList(record_id))
         ));

.. kódová tabulka: jít

var id int64
pokud se stane chyba, tak:
db, uid, heslo
"ir.model", "create",
map[string]string{}
                 {
„název“: „Vlastní model“,
"model": "x_custom",
„stát“: „ruční“,
                 },
             },
} else if err != nil {
log.Fatal(err)
         }
var poleId int64
pokud se stane chyba, tak:
db, uid, heslo
"ir.model.fields", "vytvořit",
map[string]any{}
                 {
"model_id": id
"jméno":    "x_jméno"
"typ":      "char",
"stát":     "manuální",
"vyžadováno": true,
                 },
             },
} else err = nil;
log.Fatal(err)
         }
var idRecord int64
pokud se stane chyba, tak:
db, uid, heslo
„x_custom“, „vytvořit“
map[string]string{}
{"x_name": "testový záznam"}
             },
} else err = nil;
log.Fatal(err)
         }
var pole záznamů []map[string]jakýkoli
pokud se stane chyba, tak:
db, uid, heslo
"x_custom", "čtení",
[][]int64{{id záznamu}}
}), pole záznamů; pokud je nula, pak došlo k chybě.
log.Fatal(err)
         }

Výsledek:

... kódový blok: JSON

      [
          {
"create_uid": [1, "Administrátor"]
"x_name": "testový záznam",
"__last_update": "2014-11-12 16:32:13"
"write_uid": [1, "Administrátor"]
"write_date": "2014-11-12 16:32:13",
"create_date": "2014-11-12 16:32:13",
"id": 1,
„display_name“: „Testový záznam“
          }
      ]

.._PostgreSQL: https://www.postgresql.org
.._XML-RPC: https://cs.wikipedia.org/wiki/XML-RPC
..._base64: https://cs.wikipedia.org/wiki/Base64
