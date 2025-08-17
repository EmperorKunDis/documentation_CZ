... odkaz/kommandovou řádku:

============================
Konzolový rozhraní
============================

CLI :dfn:`příkazová řádka“ nabízí několik funkcí souvisejících s Odoo. Můžete ji používat
spustit server (viz odkaz na příkazovou řádku v části „Server“), spustit Odoo jako konzolu Pythonu
prostředí <odkaz/kommandová řádka/skládání>, :ref:`vytvořit modul v Odoo <odkaz/kommandová řádka/scaffolding>
:ref:`Naplnit databázi <reference/cmdline/populate>` nebo :ref:`Počítat počet řádků kódu <reference/cmdline/cloc>“.

.. důležité:
Komando pro volání CLI závisí na tom, jak jste nainstalovali Odoo. V příkladech níže používáme komandu, která je
předpokládejme, že jste:doc:`spouštěli Odoo z zdroje </administration/on-premise/source>
:soubor: `odoo-bin`. Pokud jste nainstalovali Odoo z balíčku distribuce
</správa/na-pracovišti/balíčky> nebo s Dockerem <https://hub.docker.com/_/odoo/>_.
Musí se přizpůsobit příkazu.

... záložky::

.. tab:: Spouštění aplikace Odoo z zdrojového kódu

         #Navigujte do kořenového adresáře složky, kde jste stáhli zdrojové soubory Odoo.
Komunita.
         #Spusťte všechny příkazy CLI s: ./odoo-bin

.. tab::Odoo bylo nainstalováno z distribučního balíčku

Když byl nainstalován Odoo, do cesty vašeho uživatele byla přidána spustitelná aplikace s názvem „odoo“.
všechny příklady s :command:`odoo-bin` a :command:`odoo` níže.

.. tab::Odoo bylo nainstalováno pomocí Dockeru

Prosím, odkazujte na dokumentaci oficiálního obrazu Dockeru Odoo
<https://hub.docker.com/_/odoo/>`.

..._odkaz/příkazovou řádku/pomoc:

Pomoc a verze
==============

...program: odoo-bin

.. možnost: -h, --help

zobrazuje nápovědu s veškerými dostupnými možnostmi

.. možnost:: -v

zobrazuje verzi Odoa např. „Odoo Server {BRANCH}“

Tip:Povolení automatického doplňování v terminálu lze provést spuštěním

.......kódový blok:: bash

zobrazit „kompletní -W '. / odoo-bin -- pomocí
sed -e 's/[^a-z_-]-\(\+\)[a-z0-9_-]+/\n\1\n/'
grep -- '-^' | sort | uniq | tr '\n' ' '` odoo-bin > ~/.bash_completion

.. odkaz/příkazového řádku/server:

Provoz serveru
==================

...program: odoo-bin

.. možnost: -d <databáze>, --database <databáze>

databáze použité při instalaci nebo aktualizaci modulů.
Provádění seznamu oddělených čárkami omezuje přístup k databázím poskytovaným
seznam.

Pro pokročilé možnosti databáze se podívejte na :ref:`dolů <reference/cmdline/server/database>“.

.. možnost: -i <moduly>, --init <moduly>

oddělený čárkou seznam modulů, které je nutné nainstalovat před spuštěním serveru
(vyžaduje volbu: -d).

.. možnost: -u <moduly>, --update <moduly>

oddělený čárkou seznam modulů, které je třeba aktualizovat před spuštěním serveru.
Použijte „vše“ pro všechny moduly. (vyžaduje volbu „-d“).

.. možnost: --addon-path <adresáře>

oddělené čárkami seznam adresářů, ve kterých jsou uloženy moduly.
jsou prohledávány adresáře.

....(připomínám, kdy a proč?).

.. možnost: --upgrade-path <upgrade_path>

seznam oddělených čárkou adresářů, ze kterých jsou k dispozici další skripty pro aktualizaci.
Nebo jsou nahrány.

.. možnost: --pre-upgrade-scripts <pre_upgrade_scripts>

seznam oddělených čárkami cest k skriptům pro aktualizaci, které jsou spuštěny před
načítání základního modulu při požadavku na aktualizaci jakéhokoliv modulu.
užitečné provést nějaké akce během upgradu vlastních modulů po velké aktualizaci.
upgradovat.

.. možnost: --load <moduly>

seznam serverových modulů, které se mají načíst. Tyto moduly by měly poskytnout
funkce, které nejsou nutně spojeny s konkrétní databází. To je v rozporu
do modulů, které jsou vždy svázány s konkrétní databází.
nainstalované (tj. většina doplňků Odoo). Výchozí je „base, web“.

.. možnost: -c <config>, --config <config>

cestu k alternativnímu konfiguračnímu souboru.
Pokud není definována, kontroluje Odoo proměnnou prostředí „ODOO_RC“
a výchozí umístění:soubor:{$HOME}/.odoorc.
Podívejte se na část konfiguračního souboru uvedenou v kapitole :ref:`níže <reference/cmdline/config>`.

.. možnost: -d <cesta k datovému adresáři>, --datový adresář <cesta k datovému adresáři>

cesta k adresáři, kde se ukládají data aplikace Odoo (např. filestore, session).
Pokud není uvedeno jinak, pak bude Odoo použito jako
do předem definované cesty. Na systémech Unix je
definované v proměnné prostředí „$XDG_DATA_HOME“
nebo :file:`~/.local/share/Odoo` nebo :file:`/var/lib/Odoo`.

.. možnost: -s, --save

ukládá konfiguraci serveru do souboru s aktuální konfigurací
:soubor: `${HOME}/.odoorc` (výchozí hodnota) a lze jej přehrát
:option:`-c`).

.. možnost:: --bez-demonstrace

vypne načítání demodat pro moduly nainstalované
oddělené čárkou, použijte „všechny“ pro všechny moduly.
Požaduje volbu „-d“ a „-i“.

.. možnost: --pidfile=<pidfile>

cestu k souboru, kde bude uložen proces ID serveru

.. možnost:: --stop-after-init

zastaví server po inicializaci.

.. možnost: --geoip-city-db <cesta>

Absolutní cesta k souboru databáze měst GeoIP.

.. možnost: --geoip-country-db <cesta>

Absolutní cesta k souboru databáze zemí GeoIP.


.._odkaz/příkazovou řádku/testování:

Testování konfigurace
=====================

.. možnost: --test-enable

provádí testy po instalaci modulu

.. možnost: --test-file <soubor>

spouští testovací soubor v Pythonu

.. možnost: --test-tags [-][tag][/modul]:[třída].[metoda]

Seznam oddělených čárkami specifikací, které se mají použít k filtrování testů, které se mají spustit. Povolte jednotkové testy, pokud je tento parametr nastaven.

Příklad:  --test-tags :TestClass.test_func,/test_module,externí

    * Znak „-“ určuje, zda chceme zahrnout nebo vyloučit testy odpovídající tomuto specifikaci.
    * Štítek bude odpovídat štítkům přidávaným do třídy s dekorátorem `~odoo.tests.common.tagged`.
(všechny testovací třídy mají tagy „standard“ a „při instalaci“
(viz dokumentace k dekorátoru).
    * `*´ bude shodovat se všemi tagy.
    * Pokud je tag v režimu zahrnutí vynechán, jeho hodnota je „standard“.
    * Pokud je v režimu vyloučení označení nevyplněno, má hodnotu *.
    * Modul, třída a metoda budou odpovídat názvu modulu, třídy testu a metody testu.

Testy se filtrují a spouští dvakrát: jednou při
po instalaci nebo aktualizaci každého modulu a na konci
načítání modulů. Na každé úrovni jsou testy filtrované
testovacími tagy a navíc dynamickými specifikacemi
„at_install“ a „post_install“ odpovídajícím způsobem.

.. možnost:: --snímky obrazovky

Určete složku, kam se mají ukládat snímky obrazovky při testu HttpCase.browser_js
se nezdaří, v tom případě se přepne na adresář /tmp/odoo_tests/{db_name}/screenshots

.. možnost:: --screencasty

Zapněte záznam obrazovky a zadejte adresář, kam se budou ukládat soubory s nahráváním obrazovky.
Program „ffmpeg“ je potřeba nainstalovat, aby se snímky daly převést na video
jinak se místo videa uloží rámečky.

.. odkaz/příkazového řádku/server/databáze:

Databáze
--------

.. možnost: -r <uživatel>, --db_user <uživatel>

uživatelské jméno databáze, používané k připojení k PostgreSQL.

.. možnost: -w <heslo>, --db_password <heslo>

heslo databáze, pokud používáte „ověření heslem“_.

.. možnost: --db_host <hostname>

hostitelem databázového serveru

    * „localhost“ na Windows
    * UNIXový socket jinak

.. možnost: --db_port <port>

port na který se databáze připojuje, výchozí hodnota je 5432

.. možnost:: --db-filter <filter>

skrývá databáze, které neodpovídají „<filtr>“. Filtr je
„vzorový výraz“, s tím, že:

    - „%h“ je nahrazen celým názvem počítače, na který byla požadována žádost.
    - „%d“ je nahrazeno poddoménou, na kterou byl požadavek odeslán.
výjimkou domény „www“ (takže doména „odoo.com“ a „www.odoo.com“ jsou
databáze „odoo“.

Tyto operace jsou případně citlivé. Přidejte možnost „(?i)“ k vyhledání všech
databáze (doména „odoo.com“ používající „(?i)%d“ shoduje s databází
„Odoo“.

Od verze 11 je možné omezit přístup k dané databázi
poslechnout pomocí parametru --database a zadáním oddělených čárkami
seznam databází

Když se spojí oba parametry, db-filter nahradí oddělené čárkou.
databáze pro omezení databáze, zatímco oddělené čárkou seznam
je používán pro provádění požadovaných operací, jako je například upgradování modulů.

... kódový blok: bash

$ odoo-bin --db-filter ^11.*$

Zamezit přístupu k databázím, jejichž název začíná číslem 11

... kódový blok: bash

$ odoo-bin --database 11firstdatabase,11seconddatabase

Omezte přístup na pouze dvě databáze, 11firstdatabase a 11seconddatabase

... kódový blok: bash

$ odoo-bin --database 11firstdatabase,11seconddatabase -u base

Omezte přístup na pouze dvě databáze, 11firstdatabase a 11seconddatabase.
a aktualizovat základní modul na jedné databázi: 11první databáze.
Pokud databáze 11seconddatabase neexistuje, vytvoří se nová a základní moduly
je nainstalován

... kódový blok: bash

$ odoo-bin --db-filter ^11.*$ --database 11firstdatabase,11seconddatabase -u base

Omezte přístup k databázím, jejichž název začíná číslem 11.
a aktualizovat základní modul na jedné databázi: 11první databáze.
Pokud databáze 11seconddatabase neexistuje, vytvoří se nová a základní moduly
je nainstalován

.. možnost: --db-template <template>

Při vytváření nových databází z obrazovky správy databáze použijte
specifikované „šablonové databáze“_. Výchozí hodnota je „šablona0“.

.. možnost: --pg_path <cesta k binárním souborům PostgreSQL>

Cesta k binárním souborům PostgreSQL, které jsou používány správcem databáze
databáze nejsou v souborovém systému, ale jsou na disku.
binární soubory jsou umístěny v neobvyklém adresáři.

.. možnost: --no-database-list

Zabraňuje zobrazování seznamu databází dostupných na systému

.. možnost: --db_sslmode

Zkontrolujte zabezpečení SSL propojení mezi Odoo a PostgreSQL.
Hodnota by měla být jedním z následujících: „disable“, „allow“, „prefer“, „require“.
„verify-ca“ nebo „verify-full“.
Výchozí hodnota je „přednostně“.

.. možnost: --unaccent

Pokud vytváříte nové databáze, zkuste povolit rozšíření neakcentovaných slov.

.. odkaz/příkazového řádku/server/e-mail:

E-maily
------

.. možnost: --email-from <adresa>

E-mailová adresa, která je použita jako <FROM>, když Odoo potřebuje odeslat e-maily

.. možnost: --from-filter <adresa nebo doména>

Definujte, na jakou e-mailovou adresu se bude konfigurace SMTP vztahovat. Políčko může obsahovat doménové jméno
nebo celý e-mailový adresář nebo zůstane prázdné. Pokud je e-mailová adresa odesílatele neplatná
Pokud e-mail odpovídá tomuto filtru, pak bude zpráva zašifrována kombinací obou filtrů.
parametry systému: „mail.default.from“ a „mail.catchall.domain“. Například „Admin“
<admin\@example.com> => "Admin" <notifications\@mycompany.com>.

.. možnost: --smtp <server>

Adresa SMTP serveru, ke kterému se připojíte při odesílání pošty

.. možnost: --smtp-port <port>

.. možnost:: --smtp-ssl

Pokud je nastavené, měl by odoo používat SMTP připojení s SSL/STARTTLS.

.. možnost: --smtp-user <jméno>

Uživatelské jméno pro připojení k serveru SMTP

.. možnost: --smtp-password <heslo>

Heslo k připojení na SMTP server

.. možnost: --smtp-ssl-certificate-filename <cesta k certifikátu.pem>

Certifikát SSL se používá k ověření. Pokud je nastaveno, pak se použije soubor s privátním
Není vyžadováno.

.. možnost: --smtp-ssl-private-key-filename <cesta/k/klíč.pem>

Soukromý klíč SSL se používá k ověření. Pokud je nastaveno, pak je nutné zadat hodnotu parametrů smtp-ssl-certificate.

.. odkaz/příkazovou řádku/server/mezinárodní:

Internacionalizace
--------------------

Použijte tyto možnosti k překladu Odoo do jiného jazyka. Podívejte se na část i18n v
uživatelské příručky. Volba '-d' je povinná. V případě volby '-l'
dovozu

.. možnost: --load-language <jazyky>

specifikuje jazyky (oddělené čárkami), pro které máte přeložený text.
chceme být naloženi

.. možnost: -l, --language <jazyk>

určit jazyk překladového souboru. Použijte jej s --i18n-export
nebo --i18n-import

.. možnost: --i18n-export <název souboru>

exportovat všechny věty k překladu do souboru CSV, PO nebo TGZ
archivovat a ukončit.

.. možnost: --i18n-import <název souboru>

do importu CSV nebo PO souboru s překladem a ukončit práci. Pomocí možnosti
Není vyžadováno.

.. možnost: --i18n-overwrite

přepsává stávající překlady při aktualizaci modulu nebo importu
souboru CSV nebo souboru PO.

.. možnost: --moduly

specifikovat moduly, které mají být exportovány. Používejte v kombinaci s --i18n-export

... reference/cmdline/advanced:

Pokročilé možnosti
----------------

.. reference/cmdline/dev:

Vlastnosti vývojáře
~~~~~~~~~~~~~~~~~~

.. možnost: --dev <vlastnost, vlastnost, ..., vlastnost>

oddělené čárkou seznam funkcí. Pro vývojové účely pouze. V produkci nepoužívejte.
Možné funkce jsou:

    * „všechny“: všechny níže uvedené funkce jsou aktivní

    * „xml“: číst šablonu QWeb z XML souboru místo databáze.
Jednou, když se šablona upraví v databázi, nebude ji možné číst z
soubor XML až do příští aktualizace/inicializace. Zejména šablony nejsou
přeloženy pomocí této možnosti.

    * „přetížení“: restart serveru při aktualizaci souborů v Pythonu (může být detekováno
podle použitého textového editoru

    * „qweb“: přerušení při hodnocení šablony QWeb, pokud u uzlu existuje „t-debug = debugger“

    * „(i)p(u)db“: spusťte zvolený debugger v kódu při
neočekávaná chyba je vyvolána před zaznamenáním a vrácením chyby.

    * „nástroj“: Zobrazit celou stopu v případě výjimky na přední stránce


.. odkaz/příkazového řádku/server/http:

HTTP
~~~~

.. možnost: --no-http

nezačínejte pracovníky pro HTTP nebo dlouhodobé sledování (mohou se stále spustit:ref:`cron <reference/actions/cron>
pracujících

...... varování: nemá žádný vliv, pokud je nastaveno :option:`--test-enable`, protože testy
vyžaduje dostupný webový server

.. možnost: --http-interface <interface>

TCP/IP adresa, na které poslouchá HTTP server, výchozí hodnotou je „0.0.0.0“.
(všechny adresy)

.. možnost: -p <port>
.. možnost: --http-port <port>

Port na kterém poslouchá HTTP server, výchozí hodnota je 8069.

.. možnost: --gevent-port <port>

TCP port pro websocket spojení v režimu multithreading nebo gevent.
výchozí hodnota je 8072. V režimu výchozím (smyčkovém) se nepoužívá.

.. možnost: --proxy-mode

umožňuje používat hlavičky „X-Forwarded-*“ prostřednictvím proxy Werkzeug
podpora.

Ignoruje všechny hlavičky „X-Forwarded-*“ v případě, že je přítomna hlavička „X-Forwarded-Host“.
v žádosti chyběly.

Vždy získá skutečnou IP adresu posledního záznamu v hlavičce „X-Forwarded-For“
řetězec. Konfigurujte svůj webový server podle toho příkazem, jako je
Nginxův příkaz „set_real_ip_from“ (https://nginx.org/en/docs/http/ngx_http_realip_module.html)
pokud existují další důvěryhodné proxy v řetězci, které je třeba ignorovat.

„X-Forwarded-Proto“ a „X-Forwarded-Host“ jsou používány k aktualizaci
požadovat kořenovou adresu URL, která se následně používá k aktualizaci „web.base.url“
systémový parametr po úspěšném přihlášení administrátora. Tento
tento parametr se používá k vytvoření všech odkazů pro aktuální databázi; viz
:ref:`doménové jméno/URL webu.


.... upozornění: režim proxy *nemá být* zapnutý mimo reverzní proxy
scénář

.. možnost:: --x-sendfile

delegáti připojených souborů k statickému webovému serveru a nastavují oba
„X-Sendfile“ (Apache) a „X-Accel-*“ (Nginx) HTTP hlavičky na stream
Odpovědi. Podívejte se na konfiguraci webového serveru v části :ref:`deploy/streaming`.

..._odkaz/příkazového řádku/server/protokolování:

Těžba
~~~~~~~

Výchozí nastavení Odoa zobrazuje všechny záznamy úrovně „INFO“, „WARNING“ a „ERROR“. Všechny záznamy
Výstupy na úrovni jsou vypisovány do „stderr“. Existuje několik možností, jak výstupy přesměrovat.
Přihlášení do jiných cílových míst a upravit detailnost.

.. možnost: --logfile <file>

Soubor se zaznamenanými informacemi je odesílán na uvedený soubor namísto „stderr“. Na Unixu
soubor může spravovat externí program pro správu protokolů.
<https://docs.python.org/3/library/logging.handlers.html#watchedfilehandler>
a automaticky se znovu otevře, když je nahrazen

.. možnost: --syslog

záznamy do systémového logu: „syslog na Unixech“ (https://docs.python.org/3/library/logging.handlers.html#sysloghandler)
a „událostní log na Windows“ (https://docs.python.org/3/library/logging.handlers.html#nteventloghandler).

Není ani konfigurovatelný

.. možnost: --log-db <dbname>

záznamy do modelu „ir.logging“ (tabulka „ir_logging“) pro danou instanci.
databáze. Databáze může být jméno databáze v aktuálním
PostgreSQL nebo „URI pro PostgreSQL“_ například pro agregaci logů.

.. možnost: --log-handler <handler-spec>

:samp:`{LOGGER}:{LEVEL}`, umožňuje „LOGGER“ na zadané „LEVEL“
např. „odoo.models:DEBUG“ zapne všechny logovací zprávy odpovídající nebo vyšší úrovně
„DEBUG“ úroveň v modelech.

    * Dvojtečka „:“ je povinná
    * Pro konfiguraci kořenového (výchozího) zpracovatele může být loggery vynechán.
    * Pokud je úroveň vynechána, je logger nastaven na „INFO“

Možnost se může opakovat, aby bylo možné nastavit více loggerů např.



$ odoo-bin --log-handler :DEBUG --log-handler werkzeug:CRITICAL --log-handler odoo.fields:WARNING

.. možnost:: --log-web

umožňuje vytvářet protokoly HTTP požadavků a odpovědí, což je ekvivalentní k
„--log-handler=odoo.http:DEBUG“

.. možnost:: --log-sql

umožňuje DEBUG logování dotazů na SQL, což je ekvivalentní
„--log-handler=odoo.sql_db:DEBUG“

.. možnost: --log-level <level>

Krátký název pro rychlejší nastavení předdefinovaných úrovní na konkrétních loggerech.
úrovně („kritická“, „chyba“, „upozornění“, „vývojová“) jsou nastaveny na
„odoo“ a „werkzeug“ loggerů (s výjimkou „debug“, který je dostupný pouze
vytvořené na základě „odoo“).

Odoo také nabízí debugovací pseudoúrovně, které se vztahují na různé sady.
z loggery:

„debug_sql“
nastavuje SQL logger na „debug“

ekvivalentní „--log-sql“
„debug_rpc“
nastaví „odoo“ a HTTP požadavky na „debug“

equivalent k „--log-level debug --log-request“
„debug_rpc_answer“
nastavuje „odoo“ a protokoly pro požadavky a odpovědi na
„debug“

odpovídá „--log-level debug --log-request --log-response“

.. poznámka::

Pokud dojde k konfliktu mezi volbou `--log-level` a
:volba `--log-handler`, která se používá

... odkazu /odkaz na čáru práce:

Multitasking
~~~~~~~~~~~~~~~

.. možnost: --workers <počet>

pokud „count“ není 0 (výchozí hodnota), povoluje víceprocesorovou funkci a nastavuje
určité množství pracovníků pro zpracování požadavků přes protokol HTTP
a požadavky RPC.

..... poznámka: režim více procesů je k dispozici pouze na systémech Unix

Několik možností umožňuje omezit a znovu využít pracovníky:

.. možnost:: --limit-request <limit>

Počet požadavků, které bude pracovník zpracovávat před tím, než se vrátí do fronty.
znovu spustil.

Výchozí hodnota je 8196.

..... možnost: --limit-memory-soft <limit>

Maximální povolená virtuální paměť na pracovníka v bajtech. Pokud je tento limit překročen,
pracovník je zabit a znovu použit na konci aktuální požadavku.

Výchozí hodnota je 2048 MiB (2048 × 1024 × 1024 B).

.. možnost:: --limit-memory-hard <limit>

Hard limit na virtuální paměť v bajtech. Každý pracovník překračující limit bude
: ihned bez čekání na konec aktuální požadavku
zpracování.

Výchozí hodnota je 2560 MiB (2560 MB).

.. možnost:: --limit-time-cpu <limit>

Zabraňuje pracovníkovi používat více než <limit> sekund CPU na každý
Pokud je limit překročen, pracovník je zabit.

Výchozí hodnota je 60.

...... možnost:: --limit-time-real <limit>

Zabraňuje tomu, aby zaměstnanec trávil více než <limit> sekund zpracováváním
a žádost. Pokud je limit překročen, pracovník je zabit.

Oproti volbě `--limit-time-cpu' je tato volba „čas na stěně“
např. dotazy na databázi.

Výchozí hodnota je 120.

.. možnost:: --max-cron-threads <počet>

počet zaměstnanců, kteří se věnují úkolům spouštěných pomocí :ref:`cron <reference/actions/cron>`. Výchozí hodnota je 2.
Dělníci jsou vlákna v módu vícevláknového zpracování a procesy v módu víceprocesního zpracování.

Pro víceprocesní režim je k tomu navíc potřeba procesy pro zpracování požadavků HTTP.

.. možnost: --limit-time-worker-cron <limit>

Soft limit na dobu, po kterou může být aktivní :ref:`cron <reference/actions/cron>ový vlákno/dělník`.
doba, po kterou je povoleno žít před opětovným spuštěním, v sekundách.

Při nastavení na nulu je tato funkce vypnutá.

Výchozí hodnota je 0.

.. odkaz/konzolová příkazová řádka/konfigurace:

Konfigurační soubor
==================

...program: odoo-bin

Většina příkazových řádkových možností lze také nastavit pomocí konfigurace
soubor. Většinou používají podobná jména s předponou „-“ odstraněnou
a další „-“ nahrazují „_“, např.: :option:`--db-template` se stává
„db_template“.

Některé konverze neodpovídají vzoru:

* Možnost `--db-filter` se stává „dbfilter“.
* Možnost `--no-http` odpovídá „boolean“ „http_enable“.
* uložení předvoleb (všechny možnosti začínající „--log-“ s výjimkou
:parametru `--log-handler` a :parametru `--log-db`) přidává pouze obsah
„log_handler“, použijte přímo v konfiguračním souboru
* :parametr `--smtp` je uložen jako „smtp_server“
* Možnost `--database` je uložena jako „db_name“
* Možnosti `--i18n-import` a `--i18n-export` nejsou k dispozici vůbec.
z konfiguračních souborů

.. odkaz/příkazovou řádku/konfigurační soubor:

Výchozí konfigurační soubor je: `{$HOME}`/.odoorc`,
Může být převedeno pomocí možnosti `--config odoo-bin -c>. Specifikace
Volba `--save <odoo-bin -s>‘ uloží stávající konfiguraci
do souboru. Konfigurační položky týkající se příkazové řádky jsou
specifikované v sekci „[možnosti]“.

Tady je ukázkový soubor:

... blok kódu: ini

[-h, --help]
db_user=odoo
dbfilter=odoo

... Jinja 2: https://jinja.palletsprojects.com/
..._regulární výraz: https://docs.python.org/3/library/re.html
.._ověřování heslem
    https://www.postgresql.org/docs/12/static/auth-methods.html#AUTH-PASSWORD
.._vzorová databáze:
    https://www.postgresql.org/docs/12/static/manage-ag-templatedbs.html
.._úroveň:
    https://docs.python.org/3/library/logging.html#logging.Logger.setLevel
... a PostgreSQL URI:
    https://www.postgresql.org/docs/12/static/libpq-connect.html#AEN38208
... podpora proxy nástroje:
    https://werkzeug.palletsprojects.com/en/0.16.x/middleware/proxy_fix/#module-werkzeug.middleware.proxy_fix
..._pyinotify: https://github.com/seb-m/pyinotify/wiki

.. odkaz/příkazová řádka/skript:

Shell
=====

Odoo příkazová řádka také umožňuje spouštění Odoa jako konzoly Pythonu, což umožňuje přímé
interakci s :ref:`ORM <reference/orm> a jeho funkcemi.

.. kódový blok: konzole

$ odoo-bin shell

Příklad:

Přidání interpunkce k jménům všech kontaktů:

... kódový blok:: python

In [1]: records = env["res.partner"].hledat([])

V [2]: záznamy
Out[2]: res.partner(14, 26, 33, 21, 10)

V [3]: pro partnera v záznamu:
...:     partner.jmeno = "! %s !" % partner.jmeno
         ...:

v [4]: env.cr.commit()

.... důležité::
Výchozí nastavení je takové, že shell běží v režimu transakce. To znamená, že jakákoliv změna provedená na
databáze se vrátí do původního stavu při opuštění skriptu. Pro závazné změny použijte příkaz „env.cr.commit()“.

.. možnost: --shell-interface (ipython|ptpython|bpython|python)

Specifikujte preferovaný způsob zadávání příkazů v režimu terminálu. Tento terminál je spouštěn pomocí proměnné `env`.
je již inicializován, aby mohl přistupovat k ORM a dalším modulům Odoo.

.. viz též:
:ref:`reference/orm/environment`

.._odkaz/příkazovou řádku/šablona:

Zneškodnit
==========

... program:: odoo-bin neutralize

Odoo příkazovou řádku umožňuje i odstranění databáze. Příkaz musí být spuštěn s
databázový parametr.

.. kódový blok: konzole

$ odoo-bin --addons-path <cesta k souboru s doplňky, ...>  neutralize -d <databáze>

.. možnost: -d <databáze, --databáze <databáze>

Specifikujte databázi, kterou chcete zneutralizovat.


.. možnost: --stdout

Vygenerujte neutralizační SQL místo aplikace

.. viz též:
:doc:`/administration/neutralized_database`

Štafle
===========

... program:: odoo-bin scaffold

Šablonování je automatické vytváření kostry, aby se zjednodušil
bootstrapping (v případě nových modulů v Odoo). I když není nutný,
vyhýbá se nudě spojené s nastavováním základních struktur a hledáním informací o všem
jejichž podmínky splňují.

Scaffolding je k dispozici prostřednictvím příkazu odoo-bin scaffold.

.. kódový blok: konzole

$ odoo-bin scaffold my_modul /addons/

.. volba: jméno (povinné)

jméno modulu, který má být vytvořen, lze upravit různými způsoby.
generovat programové názvy (např. název adresáře modulu, jména modelů, atd.)

.. možnost: cíl (výchozí hodnota je aktuální adresář)

adresář, ve kterém se má vytvořit nový modul, je výchozí hodnotou pro
adresář

.. možnost: -t <šablona>

šablonovém adresáři, soubory jsou předány skrze jinja2_ a poté zkopírovány do
složka „cílová“


Vytvoří modul my_module v adresáři */addons/*.

.._odkaz/příkazovou řádku/zaplnit:

Databáze obyvatel
===================

... program:: odoo-bin populate

Odoo Populate umožňuje duplikovat existující data v dané databázi. Toto lze využít
pro testování a srovnávání, když jsou potřeba velké tabulky.
přidává variabilitu některým polím, aby byly dodržovány omezení „UNIQUE“.
Dále sleduje vztahy x2Many.

.. kódový blok: konzole

$ odoo-bin populate -d moje_databaze --modely res.partner,account.move --faktory 1000

.. možnost: -d <databáze>

název databáze, do které se má data naplnit

.. možnost:: --models

seznam modelů, které mají být obyvatelné. Model, který se objeví dvakrát, bude obyvatelný pouze jednou.

.. možnost: --faktory

seznam faktorů populace. Pokud pro model chybí nějaký faktor, použije se poslední faktor v
bude použita.

.. možnost:: --sep

oddělovač používaný k vytváření názvů záznamů

.._odkaz/příkazovou řádku/cloc:

Cloc
====

... program:: odoo-bin cloc

Odoo Cloc je nástroj k počítání počtu relevantních řádků.
Python, JavaScript, CSS nebo Sass. Toto může být použito jako hrubý ukazatel ceny
údržba navíc instalovaných modulů.

Možnosti příkazového řádku
--------------------
.. možnost: -d <databáze>, --database <databáze>

|Zpracujte kód všech doplňkových modulů nainstalovaných na poskytnuté databázi.
a všechny akce serveru a ručně vytvořené pole v poskytnutém
databáze.
|Pro volbu „--addons-path“ je nutné specifikovat cestu k souborům.
složka(y) modulu.
Pokud je kombinováno s možností `--path`, počet bude součtem obou
výsledky možností (s možnými překrýváním). Alespoň jedna z těchto dvou možností je
musí být určeno, který kód se má zpracovat.

.. kódový blok: konzole

$ odoo-bin cloc --addons-path=addons -d my_database

.. viz též:
   - :ref:`reference/cmdline/cloc/database-option`


.. možnost: -p <cesta>, --path <cesta>

|Proveďte zpracování souborů v zadané cestě.
Pokud je kombinováno s možností `--database`, počet bude součtem obou
výsledky možností (s možnými překrýváním). Alespoň jedna z těchto dvou možností je
musí být určeno, který kód se má zpracovat.

.. kódový blok: konzole

$ odoo-bin cloc -p addons/account


Možnost může být opakována, aby bylo možné poskytnout více cest.

.. kódový blok: konzole

$ odoo-bin cloc -p addons/účet -p addons/prodej

.. viz též:
   - :ref:`reference/cmdline/cloc/path-option`


.. možnost: --addon-path <adresáře>

| Seznam oddělených čárkami adresářů, ve kterých jsou moduly uloženy.
Jsou skenovány moduly.
|Povinné, pokud je použita možnost `--database`.


.. možnost: -c <adresáře>

Určete konfigurační soubor, který se má použít místo možnosti :option:`--addons-path`.

.. kódový blok: konzole

$ odoo-bin cloc -c config.conf -d my_database


.. možnost: -v, --verbose

Zobrazte detaily řádků, které byly započítány pro každý soubor.


Procesované soubory
---------------

.._reference/cmdline/cloc/database-option:

S možností `--database`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Odoo Cloc počítá řádky v každém souboru doplňkových modulů.
databáze. Dále počítá řádky Pythonu serverových akcí a
vlastní pole, která byla vytvořena přímo v databázi nebo
importované. Nakonec se počítají řádky kódu v souborech JavaScriptu, CSS a Sass.
a zobrazení QWeb z importovaných modulů.

Některé soubory jsou vyloučeny z počtu výchozího nastavení:

- Manifest (:soubor: __manifest__.py nebo __openerp__.py)
- Obsah složky: `static/lib`.
- Testy definované v adresáři :file:`tests` a :file:`static/tests`.
- Migrační skripty definované v adresáři :file:`migrations` a `upgrades`.
- XML soubory, které jsou deklarovány v sekci „demo“ nebo „demo_xml“ v manifestu

Pro zvláštní případy lze definovat seznam souborů, které má Odoo Cloc ignorovat.
za modul. Toto je specifikováno v položce „cloc_exclude“ manifestu:

... kódový blok:: python

„cloc_exclude“: [
„lib/common.py“, # vyloučit jediný soubor
„data/*.xml“,  # vyloučit všechny soubory XML ve specifické složce
„/příklad/**/*“, # vyloučit všechny soubory v hierarchii složek
"*.*",          # vyloučit všechny soubory
    ]

|Vzor „**/*“ může být použit k ignorování celého modulu. To může být užitečné
aby se z výdajů na údržbu vyloučil modul.
| Další informace o syntaxi vzorců naleznete v glob
<https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob>`.

.._odkaz/příkazová řádka/cloc/cesta:

S volbou `--path`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tento způsob funguje stejně jako s možností --database.
pokud je v dané složce přítomen manifest.
složku, jinak počítá všechny soubory.


Identifikace extra modulů
-------------------------

Odoo Cloc rozlišuje mezi standardními a doplňkovými moduly následujícím způsobem:
moduly umístěné (skutečná cesta v souborovém systému po následování symbolických odkazů)
ve stejné složce jako „base“, „web“ nebo „web_enterprise“.
standardní moduly jsou považovány za standardní. Ostatní moduly jsou považovány za doplňkové moduly.


Řešení chyb
--------------

Některý soubor nelze spočítat pomocí Odoo Cloc.
Tyto soubory jsou uvedeny na konci výstupu.

Maximální velikost souboru překročena
~~~~~~~~~~~~~~~~~~~~~~

Odoo Cloc odmítá přijímat soubory větší než 25 MB. Obvykle jsou zdrojové soubory menší
než 1 MB. Pokud je soubor odmítnut, může být:

- Vytvořený soubor XML, který obsahuje spoustu dat. Měl by být vyloučen z manifestu.
- JavaScript knihovna, která by měla být umístěna v adresáři „static/lib“.

Syntax chyba
~~~~~~~~~~~~

Odoo Cloc nemůže počítat řádky kódu v souboru s problémem syntaxe.
Pokud modul obsahuje takové soubory, měly by být opraveny, aby se modul
zátěže. Pokud modul funguje i přesto, že jsou tyto soubory přítomny, pravděpodobně
nebyly naloženy a měly by být proto odstraněny z modulu, nebo alespoň vyloučeny.
v manifestu pomocí „cloc_exclude“.

TSConfig Generátor
==================

... program: odoo-bin tsconfig

Při práci s JavaScriptem existují způsoby, jak vám pomoci vašeho editora poskytnout
silné doplňování. Jedním z těchto způsobů je použití souboru tsconfig.json.
Původně určený pro psaní na stroji mohou redaktoři využít jeho informace i pomocí běžného JavaScriptu.
S touto konfiguračními soubory budete mít nyní plnou automatickou doplňování po celém modulu.

Komandu pro vytvoření těchto souborů lze použít libovolný počet nezávislých argumentů, které jsou relativními cestami
do adresáře vašeho doplňku. V následujícím příkladu se přesuneme o jeden adresář výš a uložíme soubor tsconfig v tomto adresáři.
obsahující komunitu a podnikání.

.. kódový blok: konzole

$ community/odoo-bin tsconfig --addons-path community/addons,community/odoo/addons,enterprise > tsconfig.json
