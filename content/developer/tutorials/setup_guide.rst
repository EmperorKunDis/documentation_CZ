===========
Návod k instalaci
===========

Odoo lze nainstalovat různými způsoby v závislosti na účelu použití. Pro vývojáře existuje
Odoo komunita i zaměstnanci společnosti Odoo preferují zdrojový instalační soubor.
(:dfn:`spouštění Odoo z zdrojového kódu“).

.. důležité:
Sledujte část „přispívání/rozvoj/nastavení“ v příručce pro přispěvatele, abyste se na instalaci
pro vkládání místních změn do repozitářů Odoo.

Adaptujte prostředí pro výuku
=======================================

Nyní byste měli mít zdrojový kód stažený do dvou místních repozitářů, jednoho pro „odoo/odoo“.
a jeden pro „odoo/enterprise“. Tyto repozitáře jsou nastaveny tak, aby posílaly změny do předem definovaných
vidličky na GitHubu. To se vám bude hodit, až začnete přispívat do kódu, ale
V rámci následujícího tutoriálu chceme vyhnout znečištění tréninkovým materiálem.
Poté vložte své změny do třetího repozitáře: „odoo/tutorials“. Stejně jako první dva repozitáře
bude součástí cesty „addons-path“, která odkazuje na všechny adresáře, které obsahují moduly Odoo.

.. poznámka::
V závislosti na návodu, který sledujete, nemusíte instalovat všechny moduly.
že tato knihovna obsahuje.

#Pokud chcete používat repozitář odoo-community, postupujte stejně jako u repozitáře odoo/odoo a odoo/enterprise.
do svého počítače s následujícím příkazem:

... kódový blok: konzole

$ git clone git@github.com:odoo/tutorials.git

#Nastavte svůj fork a Git tak, aby vám umožňoval přenášet změny do vašeho forku namísto hlavního kódu. Pokud
pracovat v Odoo, nakonfigurovat Git tak, aby posílal změny na společný fork vytvořený na účtu **odoo-dev**.

... záložky::

.. tab:: Připojení repozitáře Gitu k vašemu fork

         #Navštivte stránku „github.com/odoo/tutorials <https://github.com/odoo/tutorials>“ a klikněte na
:guilabel:`Vytvořit fork“ tlačítko pro vytvoření forku repozitáře na vašem účtu.

         #V níže uvedeném příkazu nahraďte <vaše_github_účet> jménem vašeho účtu na GitHub.
na kterém jste vytvořili odnož.

... kódový blok: konzole

$ cd /Tutoriály
$ git remote add dev git@github.com:<vaše_github_účet>/tutorials.git

... tab:: Propojit git s odoo-dev

... kódový blok: konzole

$ cd /tutorials
$ git remote add dev git@github.com:odoo-dev/tutorials.git
$ git remote set-url --push origin neměli byste tento repozitář pushnout

Takže je hotovo. Vaše prostředí je nyní připravené spouštět Odoo z zdrojů a úspěšně
vytvořil repozitář, který bude sloužit jako adresář doplňků. Díky tomu budete moci své práce posílat na GitHub.

.. důležité:

**Pro zaměstnance Odoo:**

   #Ujistěte se, že si přečtete velmi pečlivě:ref:`contributing/development/first-contribution`. Zejména
musíte používat název své pobočky, který bude odpovídat našim konvencím.

   #Jakmile provedete první změnu ve společném větvení na odoo-dev, vytvořte
:abbr:`PR (Pull request)“. Prosím, vložte své kvadrigramy do názvu PR (např. „abcd - Technical
„Trénink“.

To vám umožní sdílet svou budoucí práci a získat zpětnou vazbu od vašich trenérů. Aby bylo zajištěno,
kontinuální zpětná vazba, doporučujeme vytvářet nové závazné změny, jakmile dokončíte kapitolu.
z kurzu. Poznámka: Pull request je automaticky aktualizován s komity, které do repozitáře odoo-dev pošlete.
nemusíte otevírat více PR.

   #V Odoo používáme „Runbot“ [1] velmi intenzivně pro naše :abbr:`CI (Continuous Integration)“.
testy integrace). Když své změny přesunete do odoo-dev, Runbot vytvoří novou verzi.
a ověřte svůj kód. Jakmile se přihlásíte, budete moci vidět své větve projektu Tutorials.
<https://runbot.odoo.com/runbot/tutorials-12>.

.. poznámka::

Specifická poloha repozitářů na vašem souborovém systému není zásadní. Nicméně pro
Pro jednoduchost předpokládejme, že jste všechny repozitáře zkopírovali do stejného adresáře.
adresář. Pokud tomu tak není, ujistěte se, že příkazy upravíte podle potřeby.
poskytnout odpovídající relativní cestu z repozitáře „odoo/odoo“ do
repozitář odoo/tutorials.

Spustit server
==============

Spouštění s odoo-bin
----------------------

Jakmile jsou nastaveny všechny závislosti, může být Odoo spuštěn zadáním příkazu „odoo-bin“, který je k dispozici v konzole.
serverového rozhraní.

.. kódový blok: konzole

$ cd $HOME/src/odoo/
$ ./odoo-bin --addons-path="addons/,../enterprise/,../tutorials" -d rd-demo

Existuje mnoho příkazových řádkových parametrů, které můžete použít k spuštění
serveru. V tomto cvičení vám bude stačit jen některé z nich.

.. možnost: -d <databáze>

Databáze, která bude použita.

.. možnost: --addon-path <adresáře>

Řetězec oddělený čárkami, který obsahuje seznam adresářů, ve kterých jsou uloženy moduly. Tyto adresáře
pro moduly.

.. možnost: --limit-time-cpu <limit>

Zamezit tomu, aby pracovník používal více než <limit> sekund procesoru na každou požadavek.

.. možnost: --limit-time-real <limit>

Zamezit tomu, aby pracovník zpracovával požadavek déle než <limit> sekund.

..tip:
   - K argumentům :option:`--limit-time-cpu` a :option:`--limit-time-real` lze přidat příkaz, který zabrání
aby zaměstnanec nebyl zabit při ladění zdrojového kódu.
   - |Můžete narazit na chybu podobnou „AttributeError: modul <MODULE_NAME> nemá atribut
'<$ATTRIBUTE'>. V tomto případě můžete být nuceni nainstalovat modul pomocí příkazu:
instalovat modul s příkazem „sudo apt-get install --upgrade --force-reinstall <MODULE_NAME>“.
|Pokud tento problém nastane u více modulů, můžete potřebovat znovu nainstalovat všechny.
požadavky s příkazem: „pip install --upgrade --force-reinstall -r requirements.txt“.
|Můžete také vymazat cache Pythonu, aby se problém vyřešil:

... blok kódu: konzole

$ cd $HOME/.local/lib/python3.8/site-packages
$ find -name '*.pyc' -type f -delete

   - Mezi další často používané argumenty patří:

     - :option:`-i <odoo-bin --init>`: Nainstalujte některé moduly před spuštěním serveru
(oddělený čárkami seznam). To je ekvivalentem návštěvy :guilabel:`Aplikace“ v uživatelském rozhraní.
a nainstalovat modul z něj.
     - :option:`-u <odoo-bin --update>`: Aktualizovat některé moduly před spuštěním serveru
(oddělený čárkami seznam). To je ekvivalentem návštěvy :guilabel:`Aplikace“ v uživatelském rozhraní.
vybrat modul a následně jej aktualizovat.

Přihlášení do Odoo
--------------

Otevřete si prohlížeč a zadejte adresu http://localhost:8069/. Doporučujeme použít Chrome.
<http://www.google.com/intl/cs/chrome/>, nebo
jiný prohlížeč s vývojovými nástroji.

Přihlásit se jako administrátor můžete následujícími přihlašovacími údaji:

- e-mail: `admin`
- heslo: admin

Povolte vývojářský režim
=========================

Vývojářský nebo ladicí režim je užitečný pro trénink, protože poskytuje přístup k dalším (pokročilým)
nástroje.:ref:`Povolte vývojářský režim <developer-mode> nyní. Vyberte si metodu, jakou chcete;
Jsou všechny ekvivalentní.

Další nástroje
===========

Užitečné příkazy pro Git
-------------------

Tady jsou některé užitečné příkazy Git, které můžete používat při každodenní práci.

- |Přepněte na jiný oddíl:
|Když přepnete na jinou větev, musí být oba repozitáře (odoo a enterprise) synchronizovány, tj.
Oba musí být v jedné větevní linii.

...... kódový blok: konzole

cd $HOME/src/odoo
$ git checkout {BRANCH}

cd $HOME/src/enterprise
$ git checkout {BRANCH}

- Stáhnout a přepracovat:

...... kódový blok: konzole

cd $HOME/src/odoo
$ git fetch --all --prune
$ git rebase --autostash odoo/{BRANCH}

cd $HOME/src/enterprise
$ git fetch --all --prune
$ git rebase --autostash enterprise/{BRANCH}

Editor kódu
-----------

Pokud pracujete v Odoo, mnoho vašich kolegů používá „VSCode
<https://code.visualstudio.com>, VSCodium <https://vscodium.com> (open source verze)
„PyCharm“ (https://www.jetbrains.com/pycharm/download/#section=linux) nebo „Sublime Text
<http://www.sublimetext.com>_). Můžete si však vybrat svůj oblíbený editor.

Důležité je konfigurovat své lintery správně. Použití linteru vám pomáhá tím, že ukazuje syntaxi
semantické varování nebo chyby. Zdrojový kód Odoo se snaží dodržovat standardy Pythonu a JavaScriptu
Některé z nich však můžeme ignorovat.

Pro jazyk Python používáme PEP8 s těmito možnostmi ignorovanými:

- „E501“: řádek je příliš dlouhý
- `E301`: očekává se 1 prázdný řádek, nalezeno bylo 0
- `E302`: očekávalo se 2 prázdných řádků, nalezeno bylo 1

Pro JavaScript používáme ESLint a ukázku konfiguračního souboru najdete zde.
<https://github.com/odoo/odoo/wiki/JavaScript-kódovací pravidla#Použijte linter>.

Nástroje pro správu databáze PostgreSQL
----------------------------------

Můžete spravovat své databáze PostgreSQL pomocí příkazové řádky, jak bylo ukázáno dříve, nebo
GUI aplikace, jako je například pgAdmin <https://www.pgadmin.org/download/pgadmin-4-apt/>_ nebo DBeaver
<http://dbeaver.io/>`.

Pro připojení aplikace s grafickým uživatelským rozhraním k databázi doporučujeme používat unixový souborový systém.

- Název hostitele/adresa: `/var/run/postgresql`
- Přístav: „5432“
- Uživatelské jméno: `$USER`

Vývoj v Pythonu
----------------

Když se setkáte s chybou nebo pokud potřebujete pochopit, jak kód funguje, jednoduše tiskněte věci ven.
dlouhá cesta, ale správný debugger může ušetřit spoustu času.

Můžete použít klasickou knihovnu pro ladění Pythonu („pdb <https://docs.python.org/3/library/pdb.html>“),
Příkazem pudb (<https://pypi.org/project/pudb/>) nebo ipdb (<https://pypi.org/project/ipdb/>).
Použijte ladicí nástroj vašeho editoru.

V následujícím příkladu používáme knihovnu ipdb, ale proces je podobný u ostatních knihoven.

#Nainstalujte knihovnu:

... kódový blok: konzole

pip install ipdb

#Zadejte bod spouštění (rozcestník):

... kódový blok:: python

import ipdb; ipdb.set_trace()

...... příklad::

... kódový blok: Python
:zvýrazněte-řádky: 2

def copy(self, default=None):
import ipdb; ipdb.set_trace()
sebe.zajistit(1)
vybrané_jméno = default.get('name') pokud je default jinak
nové_jméno = zvolené_jméno nebo _('%s (kopie)') % jméno
výchozí hodnota = {výchozí hodnota nebo {} , jméno=nové_jméno}
vrací seznam partnerů a sebe sama

Tady je seznam příkazů:

.. možnost: h(elp) [příkaz]

Pokud není zadán žádný parametr, vypíše se seznam dostupných příkazů.
zobrazit nápovědu k příkazu.

.. možnost:: výraz

Hodnota výrazu je vytisknuta pomocí modulu `pprint`.

.. možnost: w(here)

Vytiskněte záznam o výjimce s nejnovějšími rámci na konci.

.. možnost: d(own)

Přesunout aktuální rámec o jednu úroveň níže v záznamu stavu (na novější rámec).

.. možnost: u(p)

Přesunout aktuální rámec o jeden stupeň výše v záznamu stop (na starší rámec).

.. možnost:: n(ásledující)

Pokračujte v provádění až do příští řádky aktuální funkce nebo se vrátíte.

.. možnost: c(ontinue)

Pokračujte v provádění programu, dokud se nenarazí na zastávku.

.. možnost: s (krok)

Vykonat aktuální řádek. Zastavit na první možné příležitosti (buď v funkci,
volána nebo na další řádku v aktuální funkci.

.. možnost: q (quiet)

Vypněte ladič. Program běžící v této chvíli je ukončen.
