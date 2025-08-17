====================
Konfigurace systému
====================

Tento dokument popisuje základní kroky, které je potřeba udělat při nasazení Odoo do produkce nebo na
server, který je připojen k Internetu. Následuje:
vývojovému systému, který není vystaven na
internet.

.. varování: Pokud nastavujete veřejný server, ujistěte se, že si přečtete naše doporučení týkající se bezpečnosti!

.._dbfilter:

dbfiltr
========

Odoo je vícenásobný systém: jedna instalaci Odoa může běžet a sloužit několika uživatelům.
databázových instancí. Je také velmi přizpůsobitelný, s možností přizpůsobení
(začínajíc od modulů, které se načítá) podle „aktuální databáze“.

Tento problém se nevyskytuje při práci s backendem (webovým klientem) jako přihlášený uživatel.
uživatelská společnost: databáze lze vybrat při přihlášení a přizpůsobit
Následně byla naložena na vůz.

Je však problémem pro uživatele, kteří se nepřihlásili (portál, webová stránka), kteří nejsou
vázané na databázi: Odoo potřebuje vědět, do které databáze se má nahrát
Stránku webu nebo provést operaci. Pokud se nepoužívá vícenásobný nájem, není
databáze, ale pokud existuje více databází
Přístupný Odoo potřebuje pravidlo, aby věděl, které z nich použít.

Toho je jedním z účelů příkazu :option:`--db-filter <odoo-bin --db-filter>`:
Určuje, jaká databáze by měla být vybrána na základě názvu domény.
Požadovaná hodnota je „výraz regulárních výrazů“_ (možná
včetně dynamicky vloženého názvu hostitele („%%h“) nebo prvního poddoménového jména
(`d`) přes který je systém přístupný.

Pro servery hostující více databází v produkci, zejména pokud jde o „webové“
používán, jinak se nebude fungovat řada funkcí.
správně.

Příklady konfigurace
---------------------

* Zobrazit pouze databáze s názvy začínajícími na „mycompany“

v souboru konfigurace v sekci <ref>konfiguračního souboru</ref>:

... blok kódu:: ini


dbfilter = ^mycompany.*$

* Zobrazit pouze databáze, které odpovídají první poddoméně za „www“: například
pokud je požadavek odeslán do databáze „mycompany“.
byl odeslán na „www.moufirma.cz“ nebo „moufirma.cz“, ale ne
pro „www2.moufirma.cz“ nebo „helpdesk.moufirma.cz“.

v souboru konfigurace v sekci <ref>konfiguračního souboru</ref>:

... blok kódu:: ini


filtr_db = "^%d$"

.. poznámka::

Vhodné nastavení možnosti `--db-filter <odoo-bin --db-filter>` je důležitou součástí.
zajištění vašeho nasazení.
Jakmile správně funguje a používá pouze jednu databázi na doménové jméno,
je silně doporučeno zablokovat přístup k obrazovkám správce databáze.
a použít parametry spouštění „--no-database-list“ k zabránění zobrazení seznamu databází
vaše databáze a zablokovat přístup k obrazovkám správy databází.
Viz také bezpečnost_.

PostgreSQL
==========

Výchozí nastavení PostgreSQL umožňuje připojení pouze na UNIX sockety a loopback.
připojení (od „localhost“, tedy ze stejného stroje, na kterém je server PostgreSQL)
nainstalovaný na).

UNIXový souborový systém je v pořádku, pokud chcete, aby Odoo a PostgreSQL běžely na stejném
stroj a je výchozím nastavením, pokud žádný hostitel není uveden, ale pokud chcete Odoo a
PostgreSQL bude spouštět na různých strojích [#různé-stroje]_bude
musíte „poslouchat síťové rozhraní“ (#remote-socket)

* Přijímat pouze spojení sám se sebou a „použít tunel SSH“ mezi
stroj, na kterém běží Odoo a ten, který běží PostgreSQL.
Odoo nastavte tak, aby se připojoval na konec tunelu
* Přijímat spojení z počítače s nainstalovaným Odoo.
přes SSL (podrobnosti viz část „Nastavení připojení k PostgreSQL“).
Odoo se připojí do sítě

Příklad konfigurace
--------------------

* Povolit TCP spojení na localhostu
* Povolit TCP spojení z sítě 192.168.1.x

v souboru „/etc/postgresql/<VERZE POSTGRESQL>/main/pg_hba.conf“ nastavte:

... blok kódu:: text

  # IPv4 místní připojení:
host      všichni          všichni          127.0.0.1/32         md5
host      všichni           všichni           192.168.1.0/24         md5

v souboru „/etc/postgresql/<VERZE POSTGRESQL>/main/postgresql.conf“ nastavte:

... blok kódu:: text

listen_addresses = 'localhost, 192.168.1.2'
port = 5432
max_connections=80

..._nastavení/nasazení/odoo:

Nastavení Odoo
----------------

V základním nastavení se Odoo připojuje k místnímu PostgreSQLu pomocí UNIXového spojení na port
5432. Toto lze přehlédnout pomocí možností databáze
při nasazení PostgreSQL,
lokalizované a/nebo nevyužívá výchozí nastavení instalace.

Instalátory zabalené v balíčcích <packages> budou automaticky
Vytvořte nového uživatele („odoo“) a nastavte ho jako databázového uživatele.

* Obrázek databáze je chráněn heslem „admin_passwd“.
nastavení. To lze nastavit pouze pomocí konfiguračních souborů a
Jednoduše se před provedením změn v databázi zkontroluje. Měl by být nastaven na
náhodně vygenerované hodnoty, aby se třetí strany nemohly dostat k tomuto
rozhraní.
* Všechny operace s databází používají volby pro práci s databází
včetně správy databáze
obrazovku. Pro správu databáze je nutné, aby uživatel PostgreSQL
Máte právo na příkaz „createb“.
* Uživatelé mohou kdykoli odstranit databáze, které vlastní. Pro obrazovku správy databází
aby byl úplně nefunkční, musí být uživatel PostgreSQL vytvořen s
„nevytvořit databázi“ a databáze musí být vlastněna jiným uživatelem PostgreSQL.

.... upozornění: uživatel PostgreSQL *nemůže být* superuživatelem

Příklad konfigurace
~~~~~~~~~~~~~~~~~~~~

* připojit se k PostgreSQL serveru na adrese 192.168.1.2
* port 5432
* používáním uživatelského účtu „odoo“.
* s heslem „pwd“
* filtrování pouze DB s názvem začínajícím na „mycompany“

v souboru konfigurace v sekci <ref>konfiguračního souboru</ref>:

... blok kódu:: ini


admin_passwd = můj supertajný heslo
db_host = 192.168.1.2
db_port = 5432
db_user = odoo
db_password = pwd
dbfilter = ^mycompany.*$

... _postgresql_ssl_connect:

SSL mezi Odoo a PostgreSQL
-------------------------------

Od verze Odoo 11.0 je možné zaručit SSL spojení mezi Odoem a PostgreSQL.
Odoo db_sslmode nastavuje bezpečnost SSL pro připojení.
s hodnotou vybranou z „disable“, „allow“, „prefer“, „require“ a „verify-ca“.
nebo „ověřit plně“

„Dokumentace PostgreSQL <https://www.postgresql.org/docs/12/static/libpq-ssl.html>“

... _builtin_server:

Součástí dodávky je také server.
==============

Odoo obsahuje vestavěné servery HTTP, cron a chatu v reálném čase, které používají buď vícevláknové nebo
multitasking.

Multi-threadový server je jednodušší server primárně používaný pro vývoj, demonstrace.
a její kompatibilita s různými operačními systémy (včetně Windows). Vytvoří se nová vlákna
pro každý nový požadavek HTTP, i pro dlouhodobé spojení, jako je například websocket. Extra daemonic cron
spouští se také vlákna, což je kvůli omezení v Pythonu (GIL) neefektivní.
hardware.

Multithreadový server je výchozí server i pro kontejnery Dockeru. Je vybrán
nechat volbu „--workers“ (odoo-bin --workers) prázdnou nebo nastavit na hodnotu 0.

Služba **multithreading** je plnohodnotný server, který se nejčastěji používá pro produkci. Není
podléhá stejnému omezení Pythone (GIL) na využití zdrojů a tedy je vhodné pro
hardware. Při startu serveru je vytvořen pracovní pool. Nové požadavky na HTTP jsou frontou zpracovávány operačním systémem
až do té doby, než se najdou pracovníci připravení je zpracovat. Extra událostem řízený HTTP worker pro chaty v reálném čase
je spuštěn na alternativním portu a jsou spouštěny i další služby Cron. Konfigurovatelný proces
Sběrač monitoruje spotřebu zdrojů a může zabít nebo restartovat nefunkční pracovníky.

Multithreadový server je volitelný. Je vybrán nastavením možnosti `--workers
Možnost „--workers“ na hodnotu, která není rovna 0.

.. poznámka::
Protože je velmi optimalizovaný pro linuxové servery, není k dispozici víceprocesorový server.
na Windows.

Počet pracovníků
-------------------------

* Pravidlo k použití: (#CPU * 2) + 1
* Pro zaměstnance Cronu je důležitý procesor
* 1 pracovník ~= 6 souběžných uživatelů

Výpočet velikosti paměti
-----------------------

* Považujeme za těžké požadavky 20 % z nich a zbývajících 80 % jsou jednodušší
* Těžký pracovník spotřebuje zhruba 1 GB paměti RAM, pokud jsou dobře navržené všechny pole v databázi, SQL dotazy jsou dobře navržené ...
* Pracovník s nižší zátěží spotřebuje v podobné situaci přibližně 150 MB paměti

Požadovaná paměť RAM = #worker * ( (poměr lehkých pracovníků * odhadované množství paměti RAM pro lehké pracovníky) + (poměr těžkých pracovníků * odhadované množství paměti RAM pro těžké pracovníky) )

LiveChat
--------

Ve víceprocesovém zpracování je automaticky spuštěn pracovník LiveChatu a naslouchá na
Možností `--gevent-port <odoo-bin --gevent-port>`, výchozí hodnota je
přistupovat k běžným pracovníkům HTTP namísto LiveChatu. Musíte nasadit před nimi proxy.
Odoo a přesměrovat příchozí požadavky, jejichž cesta začíná na „/websocket/“, do pracovníka LiveChatu.
Musíte také spustit Odoo v režimu proxy, tj. pomocí příkazu:
hlavičky klienta (jméno hostitele, schéma a IP adresu) namísto hlaviček proxy.

Příklad konfigurace
--------------------

* Server s 4 procesory a 8 vlákny
* 60 souběžných uživatelů

* 60 uživatelů / 6 = 10 <- teoretický počet pracovníků, které je potřeba
* (4 * 2) + 1 = 9 <- teoreticky maximální počet dělníků
* Použijeme 8 pracovníků + 1 pro cron. Dále budeme používat monitorovací systém k měření zatížení procesoru a kontrolovat, zda je mezi 7 a 7,5.
* RAM = 9 * ((0,8 * 150) + (0,2 * 1024)) ~= 3 GB RAM pro Odoo

v souboru konfigurace:

... blok kódu:: ini


limit_memory_hard = 1677721600
limit_memory_soft = 629145600
limit_požadavku = 8192
limit_time_cpu = 600
limit_time_real = 1200
max_cron_threads = 1
pracovníků = 8

.. https_proxy:

HTTPS
=====

Ať už je přístupováno prostřednictvím webové stránky/webového klienta nebo webové služby, Odoo předává
autentizační informace v čitelné podobě. To znamená bezpečné nasazení
Odoo musí používat HTTPS/ [#přepínání]. SSL ukončení lze implementovat pomocí
jakýkoliv terminál SSL, ale vyžaduje následující nastavení:

* Zapněte režim :option:`proxy módu <odoo-bin --proxy-mode>`, který by měl být zapnutý pouze tehdy, pokud je Odoo za reverzním proxy serverem.
* Nastavte terminální proxy SSL („Příklad konfigurace Nginxu“)
* Založte samotné proxyování („Příklad proxyování Nginxem“__)
* Váš terminál SSL by měl také automaticky přesměrovat nezabezpečené
spojení s bezpečným přístavem

Příklad konfigurace
--------------------

* Přesměrovat požadavky na HTTP na HTTPS
* Zástupné požadavky na odoo

v souboru konfigurace v sekci <ref>konfiguračního souboru</ref>:

... blok kódu:: ini

proxy_mode = True

v souboru „/etc/nginx/sites-enabled/odoo.conf“ nastavte:

... kódový blok:: Nginx

  #Odoo server
upstream odoo {
server 127.0.0.1:8069;
  }
doleva,
server 127.0.0.1:8072;
  }
map $http_upgrade $connection_upgrade {
výchozí aktualizace.
"        close;
  }

  # http:// -> https://
server {
poslouchat 80;
server_name odoo.moufirma.cz;
přepsat vše, co začíná na ^(.*), na https://$host$1 trvale;
  }

server {
poslouchat 443 ssl;
server_name odoo.moufirma.cz;
proxy_read_timeout 720s;
proxy_connect_timeout 720s;
proxy_send_timeout 720s;

    # Parametry SSL
ssl_certificate /etc/ssl/nginx/server.crt;
ssl_certificate /etc/ssl/nginx/server.crt;
ssl_session_timeout 30m;
ssl_protocols TLSv1.2;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
ssl_prefere_server_cipher off;

    # log
access_log /var/log/nginx/odoo.access.log;
error_log /var/log/nginx/odoo.error.log;

    # Přesměrujte požadavky na websocket na port odoo gevent.
location /websocket {
proxy_pass http://odoochat;
proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection $connection_upgrade;
proxy_set_header X-Forwarded-Host $http_host;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Real-IP $remote_addr;

přidat hlavičku Strict-Transport-Security „max-age=31536000; includeSubDomains“
proxy_cookie_flags session_id samesite=lax secure; # vyžaduje Nginx 1.19.8
    }

    # Přesměrovat požadavky na server Odoo Backend
location / {
      # Přidejte hlavičky pro režim odoo proxy
proxy_set_header X-Forwarded-Host $http_host;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header X-Real-IP $remote_addr;
proxy_redirect off;
proxy_pass http://odoo;

přidat hlavičku Strict-Transport-Security „max-age=31536000; includeSubDomains“
proxy_cookie_flags session_id samesite=lax secure; # vyžaduje Nginx 1.19.8
    }

    # univerzální gzip
gzip_types text/css text/scss text/plain text/xml aplikace/xml aplikace/json aplikace/javascript;
gzip zapnuto;
  }

Zpevnění protokolu HTTPS
---------------

Přidejte hlavičku Strict-Transport-Security ke všem požadavkům, aby se zabránilo
prohlížeče nikdy neposlat na tuto doménu žádnou požadavek typu HTTP. Budete potřebovat
aby na tomto doméně byl funkční HTTPS s platným certifikátem.
v jiném čase, jinak uživatelé uvidí varování o bezpečnosti nebo budou úplně nefunkční.
k ní přistupovat.

Použijte pro každého návštěvníka v NGINX během jednoho roku příkaz:

... kódový blok:: Nginx

add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";

Další konfigurace může být definována pro soubor cookie session_id. Soubor cookie
vlajka může být přidána, aby se ujistila, že nikdy nebude přenášena prostřednictvím protokolu HTTP a SameSite=Lax.
aby se zabránilo autentizaci „CSRF“.

... kódový blok:: Nginx

  # vyžaduje Nginx 1.19.8
proxy_cookie_flags session_id samesite=lax secure;


Odoo jako aplikace WSGI
==========================

Odoo lze také nainstalovat jako běžnou aplikaci WSGI.
poskytuje základ pro skript spouštěče WSGI jako „odoo-wsgi.example.py“.
Skript by měl být přizpůsoben (možná po jeho kopírování z adresáře s instalací), aby správně nastavil
konfiguraci přímo v modulu odoo.tools.config namísto přes
konzole nebo konfigurační soubor.

WSGI server však bude vystavovat pouze hlavní HTTP konec pro web.
klienta, webové stránky a webového rozhraní API. Protože Odoo nemá kontrolu nad tvorbou
uživatelé nejsou zaměstnanci, nemůže si nastavit časovač ani chatovací pracovníky.

Dělníci z Cronu
------------

Pro zpracování cronových úloh je nutné spustit jeden ze zabudovaných serverů Odoo vedle WSGI serveru.
Tento server musí být nakonfigurován tak, aby zpracovával pouze crony a ne požadavky přes HTTP.
:option:`--no-http <odoo-bin --no-http>` příkazového řádku nebo „http_enable = False“ konfigurace
souborová nastavení.

Na systémech podobných Linuxu je doporučeno používat víceprocesorový server namísto vícethreadového.
díky lepšímu využití hardwaru a zvýšené stabilitě, tedy používáním
možností: `--workers=-1 <odoo-bin --workers> a možnosti: --max-cron-threads=n
--max-cron-threads odoo-bin.

LiveChat
--------

Pro správnou funkci chatu je nutné používat WSGI server kompatibilní s geventem.
vlastnost, která by měla umožňovat mnoho souběžných dlouhodobých spojení, ale neumí
potřebují mnoho výpočetního výkonu. Všechny požadavky, jejichž cesta začíná na „/websocket/“, by měly být
směřuje na tento server. Pro všechny ostatní by měl být používán běžný (vlákno/proces založený) WSGI server.
požadavky.

Odoo cron server může být také použit k vyřizování požadavků na živý chat. Stačí
možnost volby z příkazového řádku `--no-http <odoo-bin --no-http>“ ze serveru cron a ujistěte se, že požadavky
jejichž cesta začíná na „/websocket/“ jsou směrovány do tohoto serveru, ať už
možnost: `--http-port <odoo-bin --http-port>“ (vícevláknový server) nebo
:option:`--gevent-port <odoo-bin --gevent-port>“ (procesy s více vlákny).

.. nasazení a streamování:

Poskytování statických souborů a příloh
====================================

Pro snadné používání je Odoo schopen přímo poskytovat všechny statické soubory a přílohy v modulu.
To nemusí být ideální v případě představení a statické soubory by měly být obvykle poskytovány
statický webový server.

Poskytování statických souborů
--------------------

Statické soubory v Odoo jsou umístěny ve složce statických souborů každého modulu, takže mohou být poskytovány
zaměřením na všechny požadavky na :samp:`/<modul>/static/<soubor>“ a hledáním správného modulu
(a souboru) v různých cestách k doplňkům.

Je doporučeno nastavit hlavičku „Content-Security-Policy: default-src 'none'“ na všechny obrázky.
doručované webovým serverem. Není nutné, protože uživatelé nemohou obsah měnit ani vkládat
v adresáři statické části modulu a existující obrázky jsou konečné (nevyžádají nové).
sami o sobě), ale je dobrým zvykem.

Používáním výše uvedené konfigurace NGINX (s https) by měly být následující „map“ a „location“ bloky
přidána služba pro statické soubory přes NGINX.

... kódový blok:: Nginx

map $sent_http_content_type $content_type_csp {
výchozí hodnota ""
~obrázek/ „default-src ‘none’“;
    }

server {
        # zbytek konfigurace

lokalita @odoo {
            # kopírovat obsah bloku / umístění
        }

        # Servisujte statické soubory hned
lokaci ~^ /[^/]+/static/.+$ {
            # root a try_files oba závisí na vašich adresách doplňků
kořen ...;
try_files ... @odoo;
platnost 24 hodin.
add_header Content-Security-Policy $content_type_csp;
        }
    }

Skutečné „kořen“ a „try_files“ jsou závislé na vaší instalaci, konkrétně na
:option:`--addons-path <odoo-bin --addons-path>`.

.. příklad::

... záložky ::

.. skupinová záložka: balíček v Debianu

Řekněme, že Odoo bylo nainstalováno prostřednictvím balíčků **Debianu** pro komunitu a enterprise.
že volba `--addons-path <odoo-bin --addons-path>‘ je
„/usr/lib/python3/dist-packages/odoo/addons“.

„Root“ a „try_files“ by měly být:

.. kódový blok :: Nginx

kořen /usr/lib/python3/dist-packages/odoo/addons;
try_files $uri @odoo;

.. skupina tabulky - zdroje Gitu

Říká se, že Odoo bylo nainstalováno pomocí zdrojů, které jsou oběma komunitami a podnikovým
repozitáře byly zkopírovány do adresářů :file:`/opt/odoo/community` a :file:`/opt/odoo/enterprise`.
respektive a že volba `--addons-path <odoo-bin --addons-path>‘
„‘/opt/odoo/community/odoo/addons, /opt/odoo/community/addons, /opt/odoo/enterprise‘“.

„Root“ a „try_files“ by měly být:

.. kódový blok :: Nginx

kořen /opt/odoo;
try_files /community/odoo/addons$uri /community/addons$uri /enterprise$uri @odoo;

Přidružené služby
-------------------

Přílohy jsou soubory uložené v úložišti, přístup k nim je regulován systémem Odoo. Nemohou být
přímo přístupné pomocí statického webového serveru, protože k jejich získání je nutné provést několik dotazů do
databáze, která určí, kde jsou soubory uloženy a zda je může aktuální uživatel otevřít.
ne.

Pokud je soubor nalezen a práva přístupu ověřena prostřednictvím Odoo, je to dobré.
myšlenka poskytovat soubor pomocí statického webového serveru místo Odoo, aby se Odoo mohl věnovat
soubory do statického webového serveru, „X-Sendfile“ (apache).
„X-Accel <https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/>“ (nginx) rozšíření
musí být zapnutá a nakonfigurována na statickém webovém serveru. Jakmile je nastavená, spusťte Odoo pomocí
Klíčová slova příkazového řádku: `--x-sendfile <odoo-bin --x-sendfile>`, které se používají pro oba
X-Sendfile a X-Accel).


.. poznámka::
   - Prohlížeč Apache a kompatibilní servery nevyžadují žádné
doplňkové konfigurace.
   - Pro rozšíření X-Accel pro NGINX je nutné provést následující další konfiguraci:

... kódový blok: Nginx

lokalita /web/filestore {
interní;
alias /cesta/k/odoo/data-dir/filestore;
         }

Pokud nevíte, jaká je cesta k vašemu úložišti, spusťte Odoo s
:volba `--x-sendfile <ooo-bin --x-sendfile>“ a přejděte na adresu „/web/filestore“.
přímo přes Odoo (neprocházejte URL přes NGINX). To vygeneruje varování, zprávu
obsahuje konfiguraci, kterou potřebujete.


.._bezpečnost:

Bezpečnost
========

Za prvé si uvědomte, že zajišťování informačního systému je neustálý proces.
není jednorázovou operací. V každém okamžiku budete jen tak bezpeční jako ten nejzranitelnější článek
Vašem okolí.

Prosím, neberte tento oddíl jako konečný seznam opatření, která zabrání
všech bezpečnostních problémů. Je pouze shrnutím prvních důležitých věcí
je třeba zahrnout do bezpečnostního plánu. Zbytek přijde sám
z nejlepších bezpečnostních postupů pro váš operační systém a distribuci
nejlepší postupy v oblasti uživatelů, hesel a řízení přístupu apod.

Při nasazení internetového serveru se prosím zamyslete nad následujícími body
bezpečnostní témata:

- Vždy si nastavte silné heslo pro správce administrátorů a omezte přístup k databázi
správu stránek, jakmile systém nastavíte. Podívejte se na :ref:`db_manager_security`.

- Vyberte jedinečné přihlašovací údaje a silná hesla pro všechny administrátorské účty na všech databázích.
Nepoužívejte „admin“ jako přihlašovací jméno. Nepoužívejte tyto přihlašovací údaje pro běžné operace.
pouze pro kontrolu a správu instalace.
Používejte nikdy výchozí hesla jako je admin/admin, i když jde o databáze pro testování nebo odladění.

- Nainstalujte do serverů, které jsou připojeny k internetu, pouze demoverze databází. Demoverze obsahují
výchozí přihlašovací údaje a hesla, které lze použít k vstupu do systému a způsobit vážné škody.
problémy i na testovacích a vývojových systémech.

- Použijte vhodný filtr databáze ( :option:`--db-filter <odoo-bin --db-filter>`)
omezit viditelnost databází podle názvu hostitele.
Viz :ref:`dbfiltr`.
Můžete také použít možnost :option:`-d <odoo-bin -d>`, abyste mohli poskytnout vlastní (oddělené čárkou)
seznam dostupných databází k filtrování namísto toho, aby systém získával
všechny z databázového serveru.

- Jakmile jsou vaše „db_name“ a „dbfilter“ nakonfigurovány tak, aby odpovídaly pouze jedné databázi
při každém názvu serveru byste měli nastavit konfigurační možnost „list_db“ na hodnotu „false“, aby se zabránilo
zobrazování celé databáze a blokování přístupu k obrazovkám správy databáze
(je také vystaven jako možnost: `--no-database-list <odoo-bin --no-database-list>
(volitelná příkazová řádka)

- Ujistěte se, že uživatel PostgreSQL (:option:`--db_user <odoo-bin --db_user>`) není superuživatelem.
a že databáze patří jinému uživateli. Například mohou být vlastněny
„postgres“ jako superuživatel, pokud používáte neprivilegovaného „db_user“.
Viz také:ref:setup/deploy/odoo.

- Nainstalujte nejnovější verze a aktualizujte je pravidelně.
nebo přes GitHub nebo stáhnout nejnovější verzi.
  https://www.odoo.com/page/download or http://nightly.odoo.com

- Nastavte svůj server v režimu více procesů s příslušnými limity, které odpovídají vaší typické
použití (paměť/CPU/časové limity). Viz také :ref:`builtin_server`.

- Spouštět aplikaci Odoo za webovým serverem poskytujícím ukončení HTTPS s platným SSL certifikátem.
aby se zabránilo odposlechu šifrované komunikace. SSL certifikáty jsou
je levná a existuje mnoho bezplatných možností.
Nastavte webový proxy tak, aby omezil velikost požadavků a nastavte vhodné časové limity.
a poté zapnout možnost „Proxy režimu“ (odoo-bin --proxy-mode).
Viz také:ref:https_proxy.

- Pokud potřebujete umožnit přístup k serverům pomocí SSH z dálky, zajistěte silné heslo.
pro všechny účty, nejen pro „root“. Je silně doporučeno úplné vypnutí
přihlašování heslem a povolte pouze ověření veřejným klíčem. Dále zvažte
omezit přístup prostřednictvím VPN, umožnit pouze důvěryhodným IP adresám v síti firewall.
provozovat systém detekce brutálního zadávání hesel, například fail2ban nebo jeho ekvivalent.

- Zvažte instalaci vhodných omezení rychlosti na vašem proxy nebo firewallech, abyste zabránili
útoky hrubou silou a útoky typu denial of service. Viz také :ref:`login_brute_force`.
pro konkrétní kroky.

Řada poskytovatelů sítí nabízí automatickou obranu proti distribuovaným útokům na
Připojení k internetu je v dnešní době nezbytností. Nabídka služeb se však liší od poskytovatele k poskytovateli.
s nimi.

- Pokud je to možné, umístěte veřejně přístupnou demonstrační/testovací/vývojovou instanci na jiném
výrobních strojích, a použít stejná bezpečnostní opatření jako u výrobních strojů.
produkce.

- Pokud má váš veřejně přístupný Odoo server přístup k citlivým interním zdrojům sítě
nebo služby (např. prostřednictvím soukromé VLAN), zavedení vhodného pravidla firewallu
chránit vnitřní zdroje. To zajistí, že Odoo server nemůže
mohou být použity náhodně (nebo jako důsledek úmyslných akcí uživatele) k přístupu nebo narušení
těch vnitřních zdrojů.
Obvykle se to dá udělat tak, že na firewallu nastavíte výchozí pravidlo DENY.
Pakliže pouze explicitně povolíte přístup k interním zdrojům, které má Odoo server.
Musí mít přístup k tomu, co potřebuje.
„Kontrola přístupu k síťovému provozu systémem d <http://0pointer.net/blog/ip-accounting-and-access-lists-with-systemd.html>“
Může být také užitečná pro řízení přístupu k síti na úrovni procesu.

- Pokud je váš veřejně přístupný Odoo server za webovou aplikační firewallí, zátěžovým vyrovnávačem
transparentní služba proti DDoS útokům (například Cloudflare) nebo podobná síťová
Pokud používáte zařízení, můžete se chtít vyhnout přímému přístupu do systému Odoo. Obecně
je těžké udržet v tajnosti koncové IP adresy vašich serverů Odoo. Například
mohou se objevit v protokolu webového serveru při dotazování veřejných systémů nebo v hlavičkách
z e-mailů odeslaných z Odoo.
V takovém případě můžete chtít konfigurovat svou firewallovou bránu tak, aby koncové body
nejsou veřejně přístupné kromě konkrétních IP adres vašeho WAF.
vyrovnávací nebo proxy služba. Poskytovatelé jako CloudFlare obvykle udržují
a veřejný seznam jejich rozsahů IP adres pro tento účel.

- Pokud hostíte více zákazníků, izolujte jejich data a soubory od sebe
používáním kontejnerů nebo vhodným „zajetím“ do jiné složky.

- Proveďte denní zálohy databází a datového úložiště a zkopírujte je na vzdálené místo.
archivační server, který není přístupný ze samotného serveru.

- Nainstalovat Odoo na Linux je silně doporučeno před Windows. Pokud se rozhodnete pro Windows,
aby se nasadil na platformě Windows, měl by být proveden důkladný audit zabezpečení serveru.
Provedené a není v rámci této příručky.


... _login_brute_force:

Zablokování útoků hrubou silou
----------------------------

Pro nasazení směřující na Internet jsou časté útoky hrubou silou proti heslům uživatelů a
hrozba by neměla být opomíjena u serverů Odoo. Odoo vždy vygeneruje záznam, když se pokusí někdo přihlásit
a hlásí výsledek: úspěch nebo neúspěch spolu s cílovým přihlašovacím jménem a zdrojovou IP adresou.

Výpisy budou mít následující tvar.

Neúspěšné přihlášení:

2018-07-05 14:56:31,506 24849 INFO db_name odoo.addons.base.res.res_users: Login failed for db:db_name login:admin from 127.0.0.1

Úspěšné přihlášení:

2018-07-05 14:56:31,506 24849 INFO db_name odoo.addons.base.res.res_users: Přihlášení úspěšné pro db:db_name login:admin z IP adresy 127.0.0.1


Tyto logy lze snadno analyzovat pomocí systému pro prevenci narušení, jako je například fail2ban.

Příkladem může být následující filtr pro fail2ban.
neúspěšné přihlášení:

[Definice]
failregex = ^[0-9]+ INFO [^ ]+ [^ ]+ Login failed for db:[^ ]+ login:[^ ]+ from <HOST>
ignoreregex =

Toto může být použito s definicí vězení, aby se blokoval útočící IP na HTTP (HTTPS).

Takto by mohl vypadat blok IP po 15 minutách
Zaznamenáno je 10 neúspěšných pokusů o přihlášení z jedné IP adresy během jedné minuty.


enabled = true
port = http,https
bantime = 900; 15minutový ban
maxretry=10; pokud 10 pokusů
najít čas = 60; do 1 minuty /! Změna s odchylkou časového pásma
cesta_pro_log = /var/log/odoo.log; nastavte skutečnou cestu pro odoo log zde

.._db_manager_security:

Bezpečnost správce databáze
-------------------------

Ve složce setup/deploy/odoo se zmínil o „admin_passwd“.

Toto nastavení se používá na všech obrazovkách pro správu databáze (pro vytvoření, smazání).
uložit nebo obnovit databáze).

Pokud musí být všechny obrazovky správy skryté, nastavte „list_db“
konfigurační možnost „Pravda“, která zablokuje přístup ke všem databázovým výběrům a
správce obrazovky.

.. varování:

Je silně doporučeno vypnout správce databáze pro jakoukoliv internetovou tvář.
systém! Jeho účelem je sloužit jako vývojový nástroj/demonstrační nástroj, aby bylo snadné rychle vytvářet
a správu databází. Není určen k použití v produkci a může dokonce i odhalit
nebezpečné funkce pro útočníky. Není navržen ani tak, aby dokázal zpracovávat velké databáze.
a mohou vyvolat limity paměti.

Na produkčních systémech by měly být prováděny správy databáze vždy.
administrátor systému, včetně zřízení nových databází a automatického zálohování.

Ujistěte se, že nastavíte vhodný parametr „db_name“
(a volitelně také „dbfilter“, aby systém mohl určit cílovou databázi
Pro každou žádost jinak, jinak by uživatelé nebyli schopni si vybrat.
databáze samotné.

Pokud musí být monitorovací obrazovky přístupné pouze z vybraného souboru počítačů
využít funkce proxy serveru k blokování přístupu ke všem trasám začínajícím na „/web/database“.
kromě možná „/web/databáze/vybírat“ zobrazující obrazovku pro výběr databáze.

Pokud by se měl zobrazit obrazovka správy databáze,
Nastavení „admin_passwd“ musí být změněno z výchozího nastavení „admin“:
Před provedením operací na změnu databáze je heslo ověřeno.

Měl by být uložen bezpečně a měl by být generován náhodně například

.. kódový blok: konzole

$ python3 -c "import base64, os; print(base64.b64encode(os.urandom(24)))"

Tento algoritmus generuje 32 znakovou náhodně vytvořenou řetězcovou hodnotu.

Obnovit hlavní heslo
-------------------------

Může dojít k situaci, kdy je hlavní heslo ztraceno nebo kompromitováno a je potřeba
reset. Následující postup je pro správce systému Odoo, kteří mají databázi na místě a
jak ručně obnovit a znovu zašifrovat hlavní heslo.

.. viz též:
Více informací o změně hesla účtu na Odoo.com najdete v této dokumentaci:
:ref:`odoocom/zmena-hesla`.

Při vytváření nové databáze na místě je generován náhodný hlavní heslo. Odoo doporučuje
Tento heslo používá k zabezpečení databáze. Toto heslo je implementováno výchozím nastavením, takže
zabezpečit hlavní heslo pro jakoukoli instalaci Odoo na vlastním serveru.

.. varování:
Když vytváříte databázi Odoo na místě, je instalační proces přístupný pro každého na
Internetu, dokud tento heslo nebude nastaveno pro zabezpečení databáze.

Hlavní heslo je uvedeno v konfiguračním souboru Odoo („odoo.conf“ nebo „odoorc“ (skrytý
souboru). Pro úpravy, vytváření nebo mazání databáze je potřeba mít heslo hlavního uživatele Odoo.
grafické uživatelské rozhraní (GUI).

Najděte konfigurační soubor
~~~~~~~~~~~~~~~~~~~~~~~~~

Nejprve otevřete konfigurační soubor Odoo („odoo.conf“ nebo „odoorc“ (skrytý soubor)).

.. záložky::

.. tab:: Windows

Konfigurační soubor je umístěn v adresáři: „C:\Program Files\Odoo{VERZE}\server\odoo.conf“

.. tab::Linux

Podle toho, jak je Odoo nainstalován na linuxovém stroji, se konfigurační soubor nachází v
Jedná se o jedno ze dvou různých míst:

      - Instalace balíčku: /etc/odoo.conf
      - Zdrojový soubor: ~/.odoorc

Změnit staré heslo
~~~~~~~~~~~~~~~~~~~

Jakmile je otevřen správný soubor, pokračujte v úpravě starého hesla v konfiguraci
uložit dočasné heslo.

.. záložky::

...... skupina-tab:: Grafické uživatelské rozhraní

Po nalezení konfiguračního souboru jej otevřete pomocí grafického uživatelského rozhraní.
(např. „interface“). Toho lze dosáhnout jednoduše dvakrát kliknutím na soubor. Pak se zařízení
by měl mít výchozí :abbr:`GUI (grafické uživatelské rozhraní)` pro otevření souboru.

Následně upravte řádek hlavního hesla „admin_passwd = $pbkdf2-sha…“ na „admin_passwd =
například novéheslo1234. Toto heslo může být cokoliv, pokud je uloženo v bezpečí
dočasně. Ujistěte se, že upravíte všechny znaky za „=“.

... příklad::
Vypadá takto:
`admin_heslo =
$pbkdf2-sh39dji295.59mptrfW.9z6HkA$w9j9AMVmKAP17OosCqDxDv2hjsvzlLpF8Rra8I7p/b573hji540mk/.3ek0lg%kvkol6k983mkf/40fjki79m`

Upravená řádka pak vypadá takto: admin_passwd = novéheslo1234

...... skupina-tab:: příkazová řádka

Upravte řádek hlavního hesla pomocí následujícího příkazu Unix, který je podrobně popsán níže.

Připojte se k terminálu Odoo prostřednictvím protokolu Secure Shell (SSH), a upravte
konfigurační soubor. Chcete-li změnit konfigurační soubor, zadejte následující příkaz:
:příkazu:`sudo nano /etc/odoo.conf`

Po otevření konfiguračního souboru upravte řádek hlavního hesla na „admin_passwd =
"$pbkdf2-sha...“ na „admin_passwd=novéheslo1234“. Toto heslo může být cokoli, pokud je dostatečně silné.
je uloženo dočasně, upravte všechny znaky za „=“.

... příklad::
Vypadá takto:
`admin_heslo =
$pbkdf2-sh39dji295.59mptrfW.9z6HkA$w9j9AMVmKAP17OosCqDxDv2hjsvzlLpF8Rra8I7p/b573hji540mk/.3ek0lg%kvkol6k983mkf/40fjki79m`

Upravená řádka pak vypadá takto: admin_passwd = novéheslo1234

.. důležité::
Je nezbytné, aby heslo bylo změněno na něco jiného, místo toho, aby se spustil nový
heslo změnit přidáním znaku „;“ na začátek řádku. To zajistí, že databáze
Je zabezpečený po celou dobu obnovení hesla.

Restartujte server Odoo
~~~~~~~~~~~~~~~~~~~

Po nastavení dočasného hesla je nutný restart Odoo serveru.

.. záložky::

...... skupina-tab:: Grafické uživatelské rozhraní

Nejprve zadejte do pole pro vyhledávání v systému Windows „services“.
Poté vyberte aplikaci „Služby“ a v seznamu aplikací přejděte dolů na „Odoo“.
služby.

Poté klikněte pravým tlačítkem na :guilabel:`Odoo“ a vyberte možnost :guilabel:`Start“ nebo :guilabel:`Restart“.
Tato akce ručně restartuje server Odoo.

...... skupina-tab:: příkazová řádka

Restartujte server Odoo zadáním příkazu: :command:`sudo service odoo15 restart`

.. poznámka::
Změňte číslo za „odoo“ tak, aby odpovídalo konkrétní verzi, na které běží server.

Použijte webové rozhraní k znovušifrování hesla
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nejprve přejděte na adresu `/web/database/manager` nebo na adresu http://server_ip:port/web/database/manager`.
prohlížeč.

.. poznámka::
Vyplňte místo server_ip adresu databáze a v poli port vyplňte číslo portu
databáze je dostupná z.

Dále klikněte na „Nastavit hlavní heslo“ a zadejte předtím vybrané dočasné heslo.
do pole „Hlavní heslo“. Po tomto kroku zadejte nové hlavní
Heslo. Nové heslo je zašifrováno (nebo zahashováno).
Kliknutím na tlačítko „Pokračovat“.

V tomto bodě byl úspěšně obnoven heslo a hašovaná verze nového hesla
je nyní součástí konfiguračního souboru.

.. viz též:
Pro více informací o bezpečnosti databáze Odoo se podívejte na tuto dokumentaci:
:ref:`db_manager_security`.

Podporované prohlížeče
==================

Odoo podporuje následující nejnovější verze prohlížečů.

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Apple Safari

..[#různé stroje]
aby bylo možné mít více instancí Odoo a používat stejnou databázi PostgreSQL.
nebo poskytnout více výpočetních zdrojů oběma programům.
.. [#vzdálený_soket]
Technicky lze nástrojům jako socat_ použít k proxování unixových souborů.
sítě, ale většinou se jedná o programy, které lze používat jen přes
Sockety UNIX
… [#přepnutí]
nebo být přístupný pouze prostřednictvím vnitřní směrované sítě.
vyžaduje zabezpečené přepínače, ochranu před „spoofingem ARP“
zakazuje používání WiFi. I přes bezpečné paketové sítě
doporučuje se nasazení přes HTTPS a náklady jsou sníženy.
„certifikáty podepsané vlastními klíči“ jsou snadněji nasazovány na řízených sítích.
prostředí než přes internet.

... regulární výraz: https://docs.python.org/3/library/re.html
... _CSRF: https://cs.wikipedia.org/wiki/Křížový_požadavek
.. _Spoofing ARP: https://cs.wikipedia.org/wiki/Spoofing_ARP
..Příklad ukončení NGINX:
    https://nginx.com/resources/admin-guide/nginx-ssl-termination/
..Příklad NGINX proxy serveru:
    https://nginx.com/resources/admin-guide/reverse-proxy/
..._socat: http://www.dest-unreach.org/socat/
..._Nastavení připojení PostgreSQL:
... naslouchat síťovým rozhraním:
    https://www.postgresql.org/docs/12/static/runtime-config-connection.html
... použít tunel SSH:
    https://www.postgresql.org/docs/12/static/ssh-tunnels.html
... _WSGI: https://wsgi.readthedocs.org/
... _POSBox: https://www.odoo.com/page/point-of-sale-hardware#part_2
