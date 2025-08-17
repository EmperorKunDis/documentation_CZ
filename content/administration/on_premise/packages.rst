===================
Instalace v balení
===================

Odoo poskytuje balíčkové instalátory pro distribuce založené na Debianu (Debian, Ubuntu atd.)
Linuxové distribuce založené na počtu souborů za sekundu (Fedora, CentOS, RHEL atd.) a Windows pro komunitu
Edice pro podniky.

Oficiální **komunitní** noční balíčky s veškerými požadovanými závislostmi jsou k dispozici na
„noční server“ <https://nightly.odoo.com>.

.. poznámka::
Balíčky noční verze mohou být obtížně aktualizovány.

Oficiální balíčky **Community** a **Enterprise** lze stáhnout z stránky ke stažení Odoo.
<http://www.odoo.com/cs/downloads>.

.. poznámka::
Potřebujete se přihlásit jako platící zákazník nebo partner, který má licenci na místě.
Balíčky pro firmy.

... _instalace/balíčků/Linux:

Linux
=====

Připravte se
-------

Odoo potřebuje „PostgreSQL“ (https://www.postgresql.org/) k tomu, aby mohl běžet.

.. záložky::

...... skupinová záložka: Debian/Ubuntu

Výchozí konfigurace balíčku Odoo „deb“ je používat databázový server PostgreSQL na
stejném hostu jako instanci Odoo. Spusťte následující příkaz k instalaci PostgreSQL
server:

... kódový blok: konzole

$ sudo apt instalovat postgres -y

...... skupina-tab:: Fedora

Ujistěte se, že je k dispozici a dobře nakonfigurovaná příkazová řádka sudo a až poté spusťte
následujícím příkazem pro instalaci serveru PostgreSQL:

... kódový blok: konzole

$ sudo dnf install -y postgresql-server
$ sudo postgresql-setup --initdb --unit postgresql
$ sudo systemctl enable postgresql
$ sudo systemctl start postgresql

.. varování:
„wkhtmltopdf“ není dostupný přes „pip“ a musí se instalovat ručně ve verzi 0.12.6
<https://github.com/wkhtmltopdf/packaging/releases/tag/0.12.6.1-3> pro podporu hlaviček
a záhlaví a zápatí. Podívejte se na stránku o wkhtmltopdf na GitHubu <https://github.com/odoo/odoo/wiki/Wkhtmltopdf>.
pro více informací o různých verzích.

Repositář
----------

Společnost Odoo S.A. poskytuje repozitář, který lze použít k instalaci verze **Community** tím, že spustí
následující příkazy:

.. záložky::

...... skupinová záložka: Debian/Ubuntu

... kódový blok: konzole

$ wget -q -O - https://nightly.odoo.com/odoo.key | sudo gpg --dearmor -o /usr/share/keyrings/odoo-archive-keyring.gpg
$ echo 'deb [signed-by=/usr/share/keyrings/odoo-archive-keyring.gpg] https://nightly.odoo.com/{CURRENT_MAJOR_BRANCH}/nightly/deb/ ./' | sudo tee /etc/apt/sources.list.d/odoo.list
$ sudo apt-get update a sudo apt-get install odoo

Pro aktualizaci instalace použijte obvyklý příkaz „apt-get upgrade“.

...... skupina-tab:: Fedora

... kódový blok: konzole

$ sudo dnf config-manager --add-repo=https://nightly.odoo.com/{CURRENT_MAJOR_BRANCH}/nightly/rpm/odoo.repo
$ sudo dnf instalovat -y odoo
$ sudo systemctl enable odoo
$ sudo systemctl start odoo

.. poznámka::
V současné době není pro edici Enterprise k dispozici noční repozitář.

Distribuční balení
--------------------

Místo použití repozitáře lze balíčky pro oba **edice Community** a **Enterprise**
může být stáhnut z stránky „Stažení Odoo <https://www.odoo.com/page/download>“.

.. záložky::

...... skupinová záložka: Debian/Ubuntu

.. poznámka::
Odoo {CURRENT_MAJOR_VERSION} balíček pro Debian momentálně podporuje verzi „Debian Bookworm (12)“
<https://www.debian.org/releases/bookworm/> a Ubuntu Jammy (22.04 LTS)
nebo vyšší verze.

Po stažení spusťte následující příkazy **jako správce** k instalaci Odoo jako služby
vytvořit potřebného uživatele PostgreSQL a automaticky spustit server:

... kódový blok: konzole

         # dpkg -i <cesta k instalačnímu balíčku> # tento příkaz pravděpodobně selže kvůli chybějících závislostech
         # apt-get install -f # by mělo nainstalovat chybějící závislosti
         # dpkg -i <cesta k instalačnímu balíčku>

.. varování::
         - Debianový balíček „python3-xlwt“, který je potřeba k vývozu do formátu XLS, neexistuje
v Debianu Buster ani v Ubuntu 18.04. Pokud je potřeba, nainstalujte ji ručně pomocí tohoto příkazu:

... kódový blok: konzole

$ sudo pip3 install xlwt

         - Balíček Pythonu „num2words“ - potřebný k zobrazení číslovek - neexistuje.
Debian Buster ani Ubuntu 18.04, což může způsobit problémy s modulem l10n_mx_edi.
Pokud je potřeba, nainstalujte jej ručně pomocí následujících kroků:

... kódový blok: konzole

$ sudo pip3 install num2words

...... skupina-tab:: Fedora

.. poznámka::
Balíček Odoo {CURRENT_MAJOR_VERSION} pro Fedoru 38 podporuje rpm.

Jednou stažený balíček lze nainstalovat pomocí správce balíčků dnf:

... kódový blok: konzole

$ sudo dnf localinstall odoo_{CURRENT_MAJOR_BRANCH}.latest.noarch.rpm
$ sudo systemctl enable odoo
$ sudo systemctl start odoo

..._instalace/balíčků/Windows:

Windows
=======

.. varování::
Windows balení je nabízeno pro pohodlí testování nebo spouštění jednoho uživatele v místním prostředí.
případech, ale nasazení do výroby je nežádoucí kvůli řadě omezení a rizik
spojené s nasazováním aplikace Odoo na platformě Windows.

#Stáhněte si instalační soubor z „nočního serveru“ (_https://nightly.odoo.com_ - pouze pro komunitu).
Windows instalační program z „stranky ke stažení Odoo <https://www.odoo.com/page/download>“ (jakýkoliv)
vydání.
#Spusťte stažený soubor.

.. varování::
Na systému Windows 8 a novějším se může zobrazit varování s názvem „Windows chránil váš počítač“. Klikněte na
**Více informací** a pak **Spustit i tak**, abyste mohli pokračovat.

#Přijměte „UAC <https://cs.wikipedia.org/wiki/User_Account_Control>“ výzvu.
#Projděte si instalační kroky.

Odoo se spustí automaticky po instalaci.
