=====
Nastavení
=====

V tomto kapitole se naučíte:

- Pro nastavení místního vývojového prostředí.
- Přehled struktury databáze Odoo.
- Exportovat a importovat databázi Odoo do vašeho lokálního prostředí.
- Mít Odoo spuštěné.

... /webové-šablony/nastavení/instalace:

Instalace
=======

Existuje několik způsobů, jak nainstalovat Odoo, záleží na tom,
použití. Tato dokumentace předpokládá, že používáte instalaci z:doc:`zdrojů
(zdrojový kód)“, která je nejvhodnější
pro tvůrce a vývojáře Odoo.

... /webové-šablony/nastavení/databáze:

Databáze
=========

... /webové šablony/nastavení/databáze/struktura:

Struktura
---------

Každá aplikace Odoo funguje podobně, jsou v ní využívány stejné logické principy. Model obsahuje pole
a vztahové pole, která odkazují na jiné modely. Každý model má pohledy reprezentující všechny jeho pole,
s vlastními pohledy na zadní a přední stranu.

.. /webové-šablony/nastavení/databáze/modely:

Modelky
~~~~~~

Základem Odoa jsou modely, které používají pole k ukládání dat. Záznamy jsou uloženy v databázi:
Jsou tedy spojeny s modelem. V Odoo najdete různé modely v
backendu zapnutím režimu vývojáře (viz developer-mode) a poté přechodem na
:menu:Nastavení --> Technické --> Databázová struktura: Modelové třídy.

.. obrázek:setup/models-page.png
:alt:Stránka s modely

... /webové-šablony/nastavení/databáze/pole:

Pole
~~~~~~

V modelech budeme centralizovat pole (názvy polí, které potřebujeme cílit v našem kódu).

.. viz též:
:doc:`/aplikace/studio/pole`

... /webové-šablony/nastavení/databáze/pole/klasické:

Klasické pole
**************

- Datum
- Char
- Výběr
- …

... /webové-šablony/nastavení/databáze/pole/vztahová:

Relativní pole
*****************

Relacní pole volají pole z jiného modelu. Umožňují vám propojit modely dohromady a
s nimi snadno pracují. Jinými slovy, když používáte pole vztahů, propojujete záznam s
další, umožňující získat obsah políček.
na tomto propojeném záznamu.

- Pole typu **many2one** se vyplňují výběrem jednoho záznamu ze seznamu záznamů na jiném modelu.
(z mnoha záznamů vyberete jeden). Například pole „Zákazník“ v cenové nabídce
Vyberete si jednoho zákazníka z několika zákazníků na kontaktním modelech.
- Pole typu **One2many** jsou zpětnými vyhledáváními existujících mnoho2jednaček. Například můžete
v seznamu kontaktů všechny své stávající nabídky (z jednoho záznamu zobrazíte mnoho).
- Pole s více než dvěma hodnotami se vyplňují výběrem jednoho nebo několika záznamů z seznamu záznamů.
další model. Například můžete dát na jeden produkt několik štítků a několik produktů používat
stejné tagy (z mnoha záznamů, můžete vybrat z mnoha).

... /webové šablony/nastavení/databáze/výhledy:

Názory
~~~~~

Názory definují, jak by měly být záznamy zobrazovány uživatelům. Jsou specifikovány v XML, což znamená, že
Mohou být upravovány nezávisle na modelech, které reprezentují. Jsou flexibilní a umožňují hluboké
přizpůsobení obrazovek, které ovládají.

... /webové-šablony/nastavení/databáze/výhledy/back-end vs. front-end:

Backend vs. Frontend
********************

- Zadní část (backend) pohledu: Kanban, Seznam, Formulář atd.
- **Výchozí pohled**: QWeb

.. /webové-šablony/nastavení/databáze/výhledy/statické vs. dynamické:

Statická vs. dynamická
******************

- Statické stránky mají stabilní obsah, jako je například domovská stránka. Můžete definovat jejich URL a nastavit některé
vlastnosti jako publikováno, indexováno atd.
- Dynamické stránky jsou dynamicky generované, jako například produktová stránka. Jejich URL je dynamická
a je přístupná všem z výchozího nastavení (může být změněno konfigurací práv).

... /webové-šablony/nastavení/databáze/výhledy/standardní vs. dědičné:

Standard vs. Dědičný
**********************

- **Standardní pohledy** jsou základní pohledy implementované v Odoo, které jsou přímo odvozeny z jejich modelu.
Nikdy je neměňte, protože umožňují aktualizaci databáze Odoo bez přepsání
změny klienta.
- Dědičné pohledy jsou kopie stejných pohledů. Všechny změny se provádějí v dědičném pohledu.
Pokud je v databázi duplicitní pohled, bude ve stejné tabulce existovat dvě shodná jména.
Dvojnásobný pohled nebude mít ID jako standardní pohled.

... /webové-šablony/nastavení/databáze/import:

Import existující databáze
---------------------------

.. poznámka::
Pokud nemáte potřebu importovat existující téma, můžete se rovnou podívat na kapitolu o :doc:`themingu`.
databáze.

.. /webové šablony/nastavení/databáze/import/přenos dat:

Skalka
~~~~

... /webové-šablony/nastavení/databáze/import/SaaS:

Odoo SaaS
*********

Přejděte na adresu <database_url>/saas_worker/dump.

... /webové šablony/nastavení/databáze/import/sh:

Odoo.sh
*******

#Připojte se k Odoo.sh.
#Vyberte větve, které chcete zálohovat.
#Vyberte záložku „Zálohování“.
#Klikněte na tlačítko Vytvořit zálohu.
#Když je proces dokončený, objeví se notifikace. Otevřete ji a klikněte na „Přejít na zálohu“.
tlačítko.
#Klikněte na ikonu „Stáhnout“ a vyberte „Testování“.
:guilabel:`Účel“ a :guilabel:`S úložištěm souborů“ pod :guilabel:`Souborovým úložištěm“.

.. obrázek:: setup/download-backup.png
:alt: Stáhnout zálohu

#Poté, co se odpad připraví k vyzvednutí, vám přijde oznámení. Otevřete jej a klikněte na
:guilabel:`Stáhnout“ pro stažení vašeho zálohování.

.... obrázek:setup/database-backup.png
:alt: Záloha databáze

.. /webové šablony/nastavení/databáze/import/soubory:

Přesunout úložiště souborů
~~~~~~~~~~~~~~

Kopírujte všechny složky zahrnuté v adresáři filestoru a vložte je do následujícího umístění
Váš počítač:

- macOS: /Users/<User>/Library/Application Support/Odoo/filestore/<database_name>
- Linux: /home/<uživatel>/ .local/share/Odoo/filestore/<název databáze>

.. poznámka::
Adresář „/Library“ je skrytý.

.. /webové šablony/nastavení/databáze/import/nastavení databáze:

Nastavení databáze
~~~~~~~~~~~~~~

Vytvořte prázdnou databázi.

... kódový blok:: bash

createdb <název databáze>

Importujte soubor SQL do databáze, kterou právě vytvořili.

... kódový blok:: bash

psql <název databáze> <dump.sql

Obnovte heslo správce uživatele.

... kódový blok:: bash

psql \c
<název databáze>
aktualizujeme uživatele s ID 2, jehož jméno je admin a heslo také

Pokud je nutné, vypněte možnost dvoufaktorové autentizace.

... kódový blok:: bash

psql <název databáze>
aktualizujeme tabulku res_users tak, že hodnota totp_secret je prázdná a ID je 2.

... /webové-šablony/nastavení/začínáme/:

Začátek
===============

... /webové-šablony/nastavení/začínáme/spouštění odoo:

Provoz Odoo
------------

Jakmile jsou nastaveny všechny závislosti, může být Odoo spuštěn zadáním příkazu „odoo-bin“, který je k dispozici v konzole.
serveru. Nachází se v kořenovém adresáři Odoo Community.

- :ref:`Spouštění Odoo <instalace/zdroj/spouštění_odoo>`
- „Docker <https://hub.docker.com/_/odoo/>“

Pro konfiguraci serveru lze použít příkazové řádky nebo konfigurační soubor. První
Metoda je uvedena níže.

:ref:`CLI <reference/cmdline>“ nabízí několik funkcí týkajících se Odoa. Můžete jej používat k
:ref:`spustit server <reference/cmdline/server>“, vybudovat šablonu Odoo, naplnit databázi nebo
počítat počet řádků kódu.

... /webové-šablony/nastavení/začínáme/skript v shellu:

Shell skript
------------

Běžným způsobem, jak spustit server :ref:`<reference/cmdline/server>`, je přidat všechny příkazové řádkové argumenty do skriptu v souborovém systému typu Unix.

Příklad:
... kódový blok :: XML

      ./odoo-bin --addons-path=../enterprise,addons --db-filter=<database> -d <database> --without-demo=all -i website --dev=xml

.. seznam tabulkový::
:hlavičky: 1
:prázdné sloupy: 1
:šířky: 20 80

   * -Složka
     - Popis
   * --addons-path <odoo-bin --addons-path>
     - Délka řetězce odděleného čárkou, který obsahuje seznam adresářů, ve kterých jsou uloženy moduly.
prohledána za účelem nalezení modulů.
   * -- :option:`-d <odoo-bin --database>`

:option:`--database <odoo-bin --database>`
     - databáze používané při instalaci nebo aktualizaci modulů.
   * – :option:`--db-filter odoo-bin --db-filter`
     - Skryje databáze, které neodpovídají filtru.
   * --init:

:option:`--init <odoo-bin --init>`
     - Délka řetězce odděleného čárkou, který určuje moduly, které je třeba nainstalovat před spuštěním serveru. (vyžaduje parametr -d)
   * --update

:option:`--update <odoo-bin --update>`
     - Délka seznamu modulů, které je nutné aktualizovat před spuštěním serveru.
   * --bez demo: `--without-demo odoo-bin --without-demo`
     - Zakázává načítání demodatových souborů pro moduly nainstalované oddělenými čárkami. Použijte „všechny“ pro všechny moduly.
(vyžaduje příkazovou řádku -d a -i)
   * --dev <odoo-bin --dev>
     - Víceřádkový seznam funkcí. Pro vývojové účely pouze. :ref:`Více informací
<odkaz/konzole/rozvojová verze>

... /webové-šablony/nastavení/začínáme/přihlášení

Přihlášení
-------

Po spuštění serveru se zobrazí informace v INFO logu „odoo.modules.loading: Modules loaded.“ a poté otevřete
http://localhost:8069 in your web browser and log in with the base administrator account.

Do e-mailové adresy zadejte **admin** a do hesla **admin**.

.. obrázek:: setup/welcome-homepage.png
:alt:Vítejte na domovské stránce

..tip:
Stiskněte klávesovou zkratku *CTRL+C*, abyste zastavili server. Pokud je potřeba, stiskněte ji dvakrát.

... /webové-šablony/nastavení/začínáme/rozvojářský režim:

Vývojářský režim
--------------

Vývojářský režim, také známý jako režim ladění, je užitečný pro vývoj, protože poskytuje přístup k
další nástroje. V dalších kapitolách se předpokládá, že máte zapnutý vývojářský režim.

.. viz též:
:doc:`/aplikace/obecné/rozvojářský režim“
