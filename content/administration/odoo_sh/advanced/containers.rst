
==========
Kontejnery
==========

Přehled
========

Každá sestava je izolována ve svém vlastním kontejneru (Linux namespace container).

Základem je systém Ubuntu, kde jsou všechny požadované závislosti na Odoo.
a běžné užitečné balíčky jsou nainstalovány.

Pokud váš projekt vyžaduje další závislosti na Pythonu nebo novější verze,
Můžete definovat soubor `requirements.txt`, který je umístěn v kořenovém adresáři vašich verzí, kde budou uvedeny požadavky.
Platforma se postará o instalaci těchto závislostí do vašich kontejnerů.
„Povinnosti požadavků <https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers>“
Dokumentace vám může pomoci s napsáním souboru :file:`requirements.txt`.
Abychom měli konkrétní příklad,
zkontrolujte soubor „requirements.txt“ v Odoo <{GITHUB_PATH}/requirements.txt>“.

Veškeré soubory `requirements.txt` podsložek jsou také zohledněny. Platforma
hledá soubor „requirements.txt“ v každé složce s moduly Odoo: Ne ve složce s modulem samotným
Ale v jejich rodičovské složce.

Struktura adresáře
===================

Jakože jsou kontejnery založené na Ubuntu, jejich struktura adresářů je podle standardu Linux File System Hierarchy.
„Přehled souborového stromu Ubuntu <https://help.ubuntu.com/cs/community/LinuxFilesystemTreeOverview#Hlavní adresáře>“
vysvětluje hlavní adresáře.

Pro relevantní adresáře v Odoo.sh platí následující:

::

  .
└── home
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│        └── src
│         │    ├── odoo                  Zdrojový kód komunity Odoo
│         │    │    └── odoo-bin        Vykonatelný soubor Odoo serveru
│         │    └── enterprise          Zdrojový kód Odoo Enterprise
│         │    └── themes               Zdrojový kód šablon
│         │   └── user                 Zdrojový kód větve vašeho repozitáře
│        └── data
│         │    ├── filestore           databázové připojení, stejně jako soubory binárních polí
│          │                    │  návštěvníci a uživatelé relací
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
├─install.log         └── log                  Logs
│                └── odoo.log           Provozní záznamy serveru
│                └── update.log        Logy databázových aktualizací
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
└── usr
└── lib
│   └── python2.7
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│    │    └── python3
│           └── dist-packages      Python 3 standard libraries
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│                  └── dist-packages     Python 3.5 standard libraries
├── local
│   └── lib
│         └── python2.7
│          │                    Python 2.7 třetích stran
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│                  └── dist-packages  Python 3.5 třetích stran
└── usr
└── bin
├── python2.7          Python 2.7 spustitelný
└── python3.5          Python 3.5 spustitelný

V kontejnerech je nainstalován jak Python 2.7, tak i verze 3.5. Nicméně:

* Pokud je vaše projekt nastavený pro použití Odoo 10.0, běží Odoo server s Pythonem 2.7.
* Pokud je váš projekt nakonfigurován tak, aby používal verzi Odoo 11.0 nebo vyšší, běží Odoo Server s Pythonem 3.5.

Shell databáze
==============

Při přístupu k kontejneru pomocí příkazového řádku můžete databázi používat pomocí příkazu *psql*.

... kódový blok:: bash

odoo@odoo-addons-master-1.odoo.sh:~$ psql
psql (9.5.2, server 9.5.11)
Konektivita SSL (protokol: TLSv1.2, šifrování: ECDHE-RSA-AES256-GCM-SHA384, bity: 256, komprese: vypnuto)
Zadejte „help“ pro zobrazení nápovědy.



**Pozor!**
„Používejte transakce“ (*začít...potvrdit/zrušit*).
pro každou příkazovou řádku SQL, která má za následek změnu
(*Aktualizace*, *Smazání*, *Změna*, ...), zejména pro vaši produkční databázi.

Transakční mechanismus je vaše záchranná síť v případě chyby.
Pouze musíte provést rollback, abyste svou databázi vrátili do její předchozí verze.

Například může dojít k tomu, že zapomenete nastavit podmínku WHERE.

... kódový blok: SQL

odoo-addons-master-1=> BEGIN;
ZAČÍNÁ
odoo-addons-master-1 => UPDATE res_users SET password = '***';
AKTUALIZACE 457
odoo-addons-master-1 => ROLLBACK;
ROLLBACK

V takovém případě můžete vrátit zpět a zrušit změny, které jste právě udělali omylem, a znovu napsat výrok.

... kódový blok: SQL

odoo-addons-master-1=> BEGIN;
ZAČÍNÁ
odoo-addons-master-1 => UPDATE res_users SET password = '******' WHERE id = 1;
Aktualizace 1
odoo-addons-master-1 => COMMIT;
COMMIT

Pamatujte však na to, že po provedení transakce je nutné buď transakci zavázat nebo ji vrátit zpět.
Otevřené transakce mohou zamknout záznamy ve vašich tabulkách
a váš běžící databáze může čekat na jejich uvolnění. To může způsobit, že server zasekne.

Dále používejte své testovací databáze k ověření vašich prohlášení. To vám poskytne další bezpečnostní síť.

Nastavte server Odoo
==================

Můžete spustit instanci Odoo z kontejnerového shellu, ale nebudete moci přistupovat k ní ze světa venku
s prohlížečem, ale můžete například:

* používat skořápku Odoo.

... kódový blok:: bash

$ odoo-bin shell
>>> partner = [('email', '=', 'asusteK@yourcompany.example.com')]
>>> partner.jmeno
„Asustek“
>>> partner.jméno = "Odoo"
>>>env['res.partner'].hledat(["email" => "asusteK@yourcompany.example.com"], limit=1).jméno
„Odoo“

* nainstalovat modul.

... kódový blok:: bash

$ odoo-bin -i prodej --bez-demonstrace všechny --zastavit po inicializaci

* aktualizovat modul.

... kódový blok:: bash

$ odoo-bin -u sale --stop-after-init

* spustit testy pro modul

... kódový blok:: bash

$ odoo-bin -i sales --test-enable --log-level=test --stop-after-init

Ve výše uvedených příkazech je argument:

* „--bez-demonstrace=vše“ zabrání načítání dat z demonstrace pro všechny moduly
* „--stop-after-init“ okamžitě ukončí instanci serveru po dokončení operací, které jste si přáli.

Více možností je k dispozici a podrobněji jsou popsány v
:doc:`Dokumentace k příkazovému řádku </developer/reference/cli>“.

V záložkách (*~/logs/odoo.log*) najdete cestu k doplňkům, které používá Odoo.sh pro spouštění vašeho serveru.
Hledejte „*odoo:addon_paths*“:

::

19. února 2018 v 10:51:39,267 4 INFO ? odoo: verze Odoo {BRANCH}
2018-02-19 10:51:39,268 4 INFO ? odoo: Používá konfigurační soubor v adresáři /home/odoo/.config/odoo/odoo.conf
2018-02-19 10:51:39,268 4 INFO ? odoo: addons paths: ['/home/odoo/data/addons/{BRANCH}', '/home/odoo/src/user', '/home/odoo/src/enterprise', '/home/odoo/src/themes', '/home/odoo/src/odoo/addons', '/home/odoo/src/odoo/odoo/addons']

**Buďte opatrní**, zejména s vaší produkční databází.
Operace, které provádíte na tomto instanci serveru Odoo, nejsou izolované:
Změny budou účinné v databázi. Vždy provádějte testování ve svých testovacích databázích.

Ladění v Odoo.sh
====================

Ladění aplikace Odoo.sh není zásadně odlišné od ladění jiné Pythonové aplikace. Tento článek popisuje specifika a omezení platformy Odoo.sh, předpokládá se však, že již znáte základní použití debuggeru.

.. poznámka: Pokud ještě nevíte, jak ladit aplikaci v Pythonu, na internetu najdete mnoho kurzů pro začátečníky.

Pro ladění kódu v Odoo.sh můžete použít „pdb“, „pudb“ nebo „ipdb“.
Jakmile je server spuštěn mimo skořápku, nemůžete přímo z vaší instanci Odoo spustit debugger, protože debugger potřebuje skořápku k provozu.

- Příkaz pdb je nainstalován v každém kontejneru výchozí verzí.

- Pokud chcete používat pudb <https://pypi.org/project/pudb/>_ nebo ipdb <https://pypi.org/project/ipdb/>_, musíte si jej nainstalovat.

Protože jste se rozhodli pro tuto možnost, máte dvě možnosti:

    - dočasné (pouze v aktuální verzi):

... blok kódu:: bash

$ pip install pudb --user

      or

... blok kódu:: bash

$ pip install ipdb --user

    - trvalé: přidejte „pudb“ nebo „ipdb“ do souboru „requirements.txt“.


Poté upravte kód, kde chcete spustit ladič, a přidejte tento řádek:

... kódový blok: Python

import systém
pokud je sys.stdin.isatty():
import pdb; pdb.set_trace()

Podmínka :code:`sys.__stdin__.isatty()` je hackerství, které detekuje, jestli spouštíte Odoo z příkazového řádku.

Uložte soubor a poté spusťte příkazový řádek Odoo:

... kódový blok:: bash

$ odoo-bin shell

Nakonec můžete kód spustit prostřednictvím skořápky Odoo.
chcete ladit.

.. obrázek: containers/pdb_sh.png
:srovnání: do středu
:alt: Snímek konzoly ukazující, jak „pdb“ běží v prostředí Odoo.sh.
