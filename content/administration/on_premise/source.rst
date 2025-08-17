==============
Instalace zdroje
==============

Zdroj „instalace“ není o instalaci Odoa, ale o tom, jak jej spustit přímo z zdroje.
namísto.

Používání zdrojů Odoo může být pro vývojáře modulů pohodlnější, protože je snadněji dostupné.
a nejsou tak snadno použitelné jako balíčky instalátorů.

Začíná a končí Odoo flexibilněji a explicitněji než služby nastavené
balíčkové instalátory. Dále umožňuje přehrávání nastavení pomocí parametrů příkazového řádku
bez nutnosti upravovat konfigurační soubor.

Nakonec poskytuje větší kontrolu nad nastavením systému a umožňuje snadněji udržovat (a
spouštět více verzí Odoo vedle sebe.

Získáme zdroje
-----------------

Existují dvě možnosti, jak získat zdrojový kód Odoo: jako archiv ZIP nebo pomocí Git.

Archiv
~~~~~~~

Edice komunity:

- „Stažení Odoo <https://www.odoo.com/page/download>“
- `Společenský repozitář GitHub <https://github.com/odoo/odoo>`_
- „Noční server <https://nightly.odoo.com>“

Edice pro firmy:

- „Stažení Odoo <https://www.odoo.com/page/download>“
- „Společnost GitHub Enterprise Repository <https://github.com/odoo/enterprise>“

..._instalace/zdroj/git:

Git
~~~

.. poznámka::
Je nutné mít nainstalovaný „Git <https://git-scm.com/>“ a doporučuje se mít také
základní znalosti příkazů v Git.

Pro klonování repozitáře Gitu vyberte mezi klonováním pomocí protokolu HTTPS nebo SSH. Většinou je nejlepší volbou
HTTPS. Při přispívání do zdrojového kódu Odoa nebo při sledování :doc:`Jak se zapojit
Začal vývojářský průvodce „Tutoriály pro serverové frameworky“.

.. záložky::

... skupina-tab:: Linux

... záložky::

.. tab:: Klonování pomocí HTTPS

... kódový blok: konzola

$ git clone https://github.com/odoo/odoo.git
$ git clone https://github.com/odoo/enterprise.git

.. tab:: Klonování pomocí SSH

... kódový blok: konzola

$ git clone git@github.com:odoo/odoo.git
$ git clone git@github.com:odoo/enterprise.git

...... skupina:: Windows

... záložky::

.. tab:: Klonování pomocí HTTPS

... kódový blok:doscon

C:\> git clone https://github.com/odoo/odoo.git
C:\> git clone https://github.com/odoo/enterprise.git

.. tab:: Klonování pomocí SSH

... kódový blok:doscon

C:\> git clone git@github.com:odoo/odoo.git
C:\> git clone git@github.com:odoo/enterprise.git

.. skupina-tab:: Mac OS

... záložky::

.. tab:: Klonování pomocí HTTPS

... kódový blok: konzola

$ git clone https://github.com/odoo/odoo.git
$ git clone https://github.com/odoo/enterprise.git

.. tab:: Klonování pomocí SSH

... kódový blok: konzola

$ git clone git@github.com:odoo/odoo.git
$ git clone git@github.com:odoo/enterprise.git

.. poznámka::
**Soubor s verzováním v Enterprise git repozitáři neobsahuje celý zdrojový kód Odoo**. Je to pouze
sada dalších doplňků. Hlavní kód serveru je v edici Community. Běžný provoz
Enterprise verze znamená spouštění serveru z komunitní verze s parametrem „addons-path“.
volba nastavená na složku s edicí Enterprise. Je nutné provést klonování obou komunitních
a vlastní instalaci Odoo Enterprise.

…_instalace/zdroj/připraveno:

Připravte se
-------

Python
~~~~~~

Odoo vyžaduje Python 3.10 nebo novější k provozu.

.. verze změněna: 17
Minimální požadavky aktualizovány z Pythonu 3.7 na Python 3.10.


.. záložky::

... skupina-tab:: Linux

Pokud je potřeba, použijte balíčkový správce k stažení a instalaci Pythonu 3.

...... skupina:: Windows

„Stáhněte si nejnovější verzi Pythonu 3 <https://www.python.org/downloads/windows/>“
nainstalovat.

Dokončete instalaci a zkontrolujte položku „Přidat Python 3 do cesty“, pak klikněte na „Nastavení instalace“
ujistěte se, že je zkontrolován **pip**.

.. skupina-tab:: Mac OS

Použijte balíčkový správce (např. Homebrew <https://brew.sh/>, MacPorts <https://www.macports.org>).
stáhnout a nainstalovat Python 3, pokud je potřeba.

.. poznámka::
Pokud je Python 3 již nainstalován, ujistěte se, že verze je 3.10 nebo vyšší, protože předchozí
verze není kompatibilní s Odoo.

... záložky ::

... skupina-tab:: Linux

... kódový blok: konzole

$ python3 --version

... skupina-tab:: Windows

... kódový blok:doscon

Python --verze

... skupina-tab: Mac OS

... kódový blok: konzole

$ python3 --version

Zkontrolujte, zda je také nainstalován balíček pip (<https://pip.pypa.io>).

... záložky ::

... skupina-tab:: Linux

... kódový blok: konzole

$ pip3 --version

... skupina-tab:: Windows

... kódový blok:doscon

C:\>pip --version

... skupina-tab: Mac OS

... kódový blok: konzole

$ pip3 --version

PostgreSQL
~~~~~~~~~~

Odoo používá databázový systém PostgreSQL.

.. záložky::

... skupina-tab:: Linux

Stáhněte si a nainstalujte PostgreSQL pomocí balíčkového manažera (podporované verze: 12.0 nebo vyšší).
Aby se toho dosáhlo, je potřeba provést následující:

... kódový blok: konzole

$ sudo apt instalovat postgres postgres-klient

...... skupina:: Windows

„Stáhněte si PostgreSQL <https://www.postgresql.org/download/windows>“ (podporované verze: 12.0
nebo vyšší a nainstalujte ji.

.. skupina-tab:: Mac OS

Použijte aplikaci Postgres.app <https://postgresapp.com> k stažení a instalaci PostgreSQL (podporované
verze 12.0 nebo vyšší.

.. tip::
Pro získání příkazových řádkových nástrojů, které jsou součástí aplikace Postgres, je třeba zajistit, aby byly k dispozici
Proměnná $PATH podle pokynů pro příkazovou řádku nástrojů Postgres.app
<https://postgresapp.com/documentation/cli-tools.html>.

Výchozí uživatel je „postgres“. Odoo neumožňuje připojení jako „postgres“, takže vytvořte nového.
Uživatel PostgreSQL.

.. záložky::

... skupina-tab:: Linux

... kódový blok: konzole

$ sudo -u postgres createuser -d -R -s $USER
$ createdb $USER

.. poznámka::
Protože uživatel PostgreSQL má stejné jméno jako uživatel Unixu, je možné se k němu připojit.
do databáze bez hesla.

...... skupina:: Windows

      #Přidejte složku bin PostgreSQLu (výchozí:
do proměnné prostředí PATH.
      #Vytvořte uživatele PostgreSQL s heslem pomocí grafického rozhraní pgAdmin:

         #Otevřete aplikaci pgAdmin.
         #Dvojklikem na server vytvořte spojení.
         #Vyberte položku „Objekt > Vytvořit > Přihlášení/Skupina rolí“.
         #Zadejte uživatelské jméno do pole „Název role“ (např. odoo).
         #Otevřete záložku **Definice**, zadejte heslo (například „odoo“) a klikněte na tlačítko **Uložit**.
         #Otevřete záložku „Přístup“ a přepněte možnost „Může se přihlásit?“ na „Ano“ a „Vytvářet databáze?“
na „Ano“.

.. skupina-tab:: Mac OS

... kódový blok: konzole

$ sudo -u postgres createuser -d -R -s $USER
$ createdb $USER

.. poznámka::
Protože uživatel PostgreSQL má stejné jméno jako uživatel Unixu, je možné se k němu připojit.
do databáze bez hesla.

... instalace/závislostí:

Závislosti
~~~~~~~~~~~~

.. záložky::

... skupina-tab:: Linux

Používání balíčků s distribučními balíčky je preferovaným způsobem instalace závislostí.
Alternativně nainstalujte závislosti na Pythonu s **pipem**.

... záložky::

... tab:: Debian/Ubuntu

Na Debianu a Ubuntu by měly následující příkazy instalovat potřebné balíčky:

... kódový blok: konzola

$ cd odoo #CommunityPath
$ sudo ./setup/debinstall.sh

Skript `setup/debinstall.sh` bude parsovat soubor `debian/control
v souboru <{GITHUB_PATH}/debian/control> a nainstalujte nalezené balíčky.

.. tab:: Instalace pomocí pip

.. varování::
Používání pipu může vést k bezpečnostním problémům a poškozeným závislostem; používejte ho jen v případě, že
Vědět, co děláte.

Jako některé balíčky v Pythonu vyžadují krok kompilace, vyžadují systémové knihovny.
Nainstalovat se musí.

Na systémech Debian a Ubuntu by měla následující příkazová řádka instalovat tyto potřebné knihovny:

... kódový blok: konzola

$ sudo apt install python3-pip libldap2-dev libpq-dev libsasl2-dev

Odoo závislosti jsou uvedeny v souboru :file:`requirements.txt`, který je umístěn na kořenovém adresáři
adresář komunity Odoo.

.. poznámka::
Pakety v souboru :file:`requirements.txt` jsou založeny na jejich stabilní verzi/LTS
Debian/Ubuntu odpovídající verze v okamžiku uvolnění Odoo. Například
pro verzi Odoo 15.0 je verze balíčku „python3-babel“ ve verzi 2.8.0 v Debianu Bullseye a
2.6.0 v Ubuntu Focal. Nejnižší verze je pak vybrána ve
:soubor:requirements.txt

...............tip::
Může být výhodnější nechat moduly balíčků Pythonu oddělené mezi různými instancemi.
Odoo nebo s tímto systémem. Je však možné používat virtuální prostředí.
<https://pypi.org/project/virtualenv/>, který vytváří izolované prostředí pro Python.

Navigujte do složky instalace Odoo Community (:file:`CommunityPath`) a spusťte
**pip** na požadavky souboru, aby byly nainstalovány požadavky pro uživatele.

... kódový blok: konzola

cd /CommunityPath
$ pip install -r požadavky.txt

...... skupina:: Windows

Než nainstalujete závislosti, stáhněte a nainstalujte „Stavební nástroje pro aplikaci Visual
Studio <https://visualstudio.microsoft.com/downloads/>`. Vyberte **Nástroje pro tvorbu C++**.
kartu „Náročnost“ a nainstalujte je, jakmile vás na to vyzvou.

Odoo závislosti jsou uvedeny v souboru requirements.txt, který se nachází na kořenovém adresáři
Komunitní adresář.

.. tip::
Je možné, že je lepší nezamíchávat balíčky modulů Pythonu mezi různými instancemi.
Odoo nebo s tímto systémem. Je však možné používat virtuální prostředí.
<https://pypi.org/project/virtualenv/>, aby vytvořil izolované prostředí pro Python.

Navigujte do cesty instalace Odoo Community („CommunityPath“), a spusťte **pip**.
požadavky souboru v terminálu s **právy správce**:

... kódový blok:: doscon

> cd \\CommunityPath
C:\> pip install setuptools wheel
C:\> pip install -r požadavky.txt

.. skupina-tab:: Mac OS

Odoo závislosti jsou uvedeny v souboru requirements.txt, který se nachází na kořenovém adresáři
Komunitní adresář.

.. tip::
Je možné, že je lepší nezamíchávat balíčky modulů Pythonu mezi různými instancemi.
Odoo nebo s tímto systémem. Je však možné používat virtuální prostředí.
<https://pypi.org/project/virtualenv/>, aby vytvořil izolované prostředí pro Python.

Navigujte do cesty instalace Odoo Community („CommunityPath“), a spusťte **pip**.
požadavky na soubor:

... kódový blok: konzole

$ cd /Společenská cesta
$ pip3 install setuptools wheel
$ pip3 install -r požadavky.txt

.. varování::
Nepythonové závislosti musí být nainstalovány pomocí balíčkovacího manažera (například Homebrew
<https://brew.sh/>`, `MacPorts <https://www.macports.org>`.

         #Stáhněte a nainstalujte příkazovou řádku.

... kódový blok: konzola

$ xcode-select --install

         #Použijte správce balíčků k instalaci nezávislých na Pythonu knihoven.

.. poznámka::
Pro jazyky s **interfacem zleva doprava** (jako arabština nebo hebrejština) je k dispozici balíček
je nutný balíček.

... záložky ::

... skupina-tab:: Linux

         #Stáhněte a nainstalujte **nodejs** a **npm** pomocí balíčkového manažera.
         #Nainstalujte knihovnu rtlcss:

... kódový blok: konzola

$ sudo npm install -g rtlcss

... skupina-tab:: Windows

         #Stáhněte a nainstalujte „nodejs“ (<https://nodejs.org/en/download>).
         #Nainstalujte knihovnu rtlcss:

... kódový blok:doscon

C:\>npm install -g rtlcss

         #Upravte proměnnou prostředí systému „PATH“ tak, aby obsahovala složku, kde je soubor „rtlcss.cmd“.
umístěné (obvykle: C:\Users\<uživatel>\AppData\Roaming\npm\).

... skupina-tab: Mac OS

         #Stáhněte si a nainstalujte **nodejs** s pomocí balíčkového manažera (např. Homebrew <https://brew.sh/>)
„MacPorts“ (<https://www.macports.org>).
         #Nainstalujte knihovnu rtlcss:

... kódový blok: konzola

$ sudo npm install -g rtlcss

.. varování:
„wkhtmltopdf“ není dostupný přes „pip“ a musí se instalovat ručně ve verzi 0.12.6
<https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3> pro podporu hlaviček
a záhlaví a zápatí. Podívejte se na stránku o wkhtmltopdf na GitHubu <https://github.com/odoo/odoo/wiki/Wkhtmltopdf>.
pro více informací o různých verzích.

... _instalace zdrojového kódu a spuštění odoo:

Provoz Odoo
------------

Jakmile jsou nastaveny všechny závislosti, může být Odoo spuštěn z příkazové řádky pomocí příkazu „odoo-bin“.
serveru. Nachází se v kořenovém adresáři Odoo Community.

Pro konfiguraci serveru buď zadejte příkazovou řádku:ref:`argumenty <reference/cmdline/server>`, nebo
:ref:`konfigurační soubor <reference/cmdline/config>.

.. tip::
Pro edici Enterprise přidejte cestu k doplňkům „enterprise“ do proměnné $addons-path
argument. Pozor, musí přijít před ostatními cestami v řetězci addons-path, aby se doplňky načetly
správně.

Konfigurace, které jsou běžně potřeba, jsou:

- Uživatelské jméno a heslo pro přístup do databáze PostgreSQL.
- Nastavit si vlastní cesty k doplňkům nad rámec výchozích, aby se načetly vlastní moduly.

Typickým způsobem, jak spustit server, je:

.. záložky::

... skupina-tab:: Linux

... kódový blok: konzole

$ cd /Společenská cesta
$ python3 odoo-bin --addons-path=addons -d mydb

Kde „CommunityPath“ je cesta k instalaci Odoo Community a „mydb“ je název databáze.
databáze PostgreSQL.

...... skupina:: Windows

... kódový blok:: doscon

C:\> cd CommunityPath/
Python:  python odoo-bin -r dbuser -w dbpassword --addons-path=addons -d mydb

kde „CommunityPath“ je cesta k instalaci Odoo Community a „dbuser“ je uživatelská
PostgreSQL login, „dbpassword“ je heslo pro PostgreSQL a „mydb“ je název databáze.
databáze PostgreSQL.

.. skupina-tab:: Mac OS

... kódový blok: konzole

$ cd /Společenská cesta
$ python3 odoo-bin --addons-path=addons -d mydb

Kde „CommunityPath“ je cesta k instalaci Odoo Community a „mydb“ je název databáze.
databáze PostgreSQL.

Po spuštění serveru se zobrazí informace v INFO logu „odoo.modules.loading: Modules loaded.“ a poté otevřete
http://localhost:8069 in a web browser and log into the Odoo database with the base administrator
Přihlášení: použijte e-mail „admin“ a heslo „admin“.

.. tip::
   - Zde vytvořte a spravujte nové uživatele.
   - Uživatelské jméno používané k přihlášení do webového rozhraní Odoo se liší od :option:`--db_user
jako příkazového řádku odoo-bin -r.

.. viz též:
:doc:`Seznam příkazového řádku pro odoo-bin </developer/reference/cli>`
