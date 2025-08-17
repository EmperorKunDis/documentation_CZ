
..._odoosh-gettingstarted-online-editor:

=============
Online editor
=============

Přehled
========

Online editor vám umožňuje upravovat zdrojový kód vašich sestavení z prohlížeče.
Díky tomu můžete otevřít terminály, konzoly Pythonu, konzoly Odoo Shell.
„Počítače s dlouhým ramenem“ <https://jupyterlab.readthedocs.io/en/stable/user/notebook.html>.

.. obrázek: online-editor/interface-editor.png
:align:center

Přístup k editoru sestavení je možný přes
:ref:`větve záložek <odoosh-gettingstarted-branches-tabs>`
:ref:`nabídka sestavení <odoosh-gettingstarted-builds-dropdown-menu>`
nebo přidáním */odoo-sh/editor* do vašeho doménového jména.
(např. https://odoo-addons-master-1.dev.odoo.com/odoo-sh/editor)

Upravte zdrojový kód
====================

Součástí pracovního adresáře jsou následující složky:

::

  .
├── home
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│        └── src
│         │    ├── odoo                  Zdrojový kód komunity Odoo
│         │    │    └── odoo-bin        Vykonatelný soubor Odoo serveru
│         │    ├── enterprise          Zdrojový kód Odoo Enterprise
│         │    └── themes               Zdrojový kód šablon
│         │                               zdrojový kód repozitáře
│        └── data
│         │    ├── filestore            databázové připojení a soubory binárních polí
├─────────┼────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
├───────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                └── install.log         Logy instalace databáze
│             ├── odoo.log           Provozní záznamy serveru
│                └── update.log        Logy databázových aktualizací
├─────────────────────┤                 └─────────────────────┘

Můžete upravovat zdrojový kód (soubory pod */src*).

.. poznámka::
Váš kód se nebude šířit do nové sestavení. Musíte jej zavázat.
pokud chcete, aby se ukládaly.


Pro sestavení pro produkci je zdrojový kód čitelný pouze pro čtení, protože aplikace místních změn na produkčním
server není dobrá praxe.

* Zdrojový kód vašeho repozitáře na GitHubu je umístěn pod */src/user*.
* Zdrojový kód Odoo je umístěn pod

  * */odoo/* (odoo/odoo <https://github.com/odoo/odoo>),
  * */enterprise/* (odoo/enterprise <https://github.com/odoo/enterprise>),
  * */themes/* (`odoo/design-themes <https://github.com/odoo/design-themes>`_).

Pro otevření souboru v editoru stačí kliknout na něj dvakrát v levém panelu prohlížeče.

.. obrázek: online-editor/interface-editor-open-file.png
:align:center

Poté můžete začít provádět změny. Uložit své změny můžete pomocí nabídky
:menu:Soubor > Uložit soubor... nebo stisknutím klávesové zkratky :kbd:`Ctrl+S`.

.. obrázek: online-editor/interface-editor-save-file.png
:align:center

Pokud uložíte Python soubor pod cestou Odoo server addons,
Odoo tento problém detekuje a automaticky se načte, takže vaše změny jsou okamžitě zobrazeny.
bez nutnosti ručního restartování serveru.

.. obrázek: online-editor/interface-editor-automaticreload.gif
:align:center

Pokud se však jedná o změnu dat uložených v databázi, například o název pole nebo o pohled,
Musíte aktualizovat příslušný modul, aby se změna aplikovala.
Modul aktuálně otevřeného souboru lze aktualizovat pomocí nabídky
:menuselection:`Odoo --> Aktualizace modulu“. Poznámka: soubor, který je v současné době otevřen
je soubor v textovém editoru zaostřený, nikoliv soubor zvýrazněný ve správci souborů.

.. obrázek: online-editor/interface-editor-update-current-module.png
:align:center

Můžete také otevřít terminál a spustit příkaz:

.. kódový blok: bash

$ odoo-bin -u <oddělené jménem modulu čárkou> --stop-after-init

... _odoosh-gettingstarted-online-editor-push:

Přidejte a zveřejněte své změny
==========================

Máte možnost provést své změny a poslat je do svého úložiště na GitHubu.

* Otevřete terminál (Menu > File > New > Terminal).
* Přejděte do adresáře *~/src/user* pomocí příkazu `cd ~/src/user`.
* Přidejte své změny pomocí příkazu git add.
* Přidejte své změny pomocí příkazu :code:`git commit`.
* Přidejte své změny pomocí příkazu „git push https HEAD:<branch>“.

V posledním příkazu

* *https* je název vašeho *HTTPS* vzdáleného repozitáře na GitHubu

* HEAD je odkaz na poslední revizi, kterou jste zkompilovali.
* Změna <branch> musí být nahrazena názvem větve do které chcete posunout změny.
nejspíš aktuální větev, pokud pracujete v vývojovém sestavení.

.. obrázek: online-editor/interface-editor-commit-push.png
:align:center

.. poznámka::
Připojení k repozitáři na GitHub prostřednictvím SSH není možné, protože soukromý klíč SSH
nejsou hostovány ve vašich kontejnerech pro stavbu (z důvodu zřejmých bezpečnostních obav).
ani přes SSH agent (protože se k tomuto editoru přistupuje pomocí webového prohlížeče).
a proto nemůžete ověřit svou identitu na GitHubu pomocí SSH.
Přenos změn musí být proveden přes HTTPS odkaz na vaši Github repozitář.
která je automaticky přidána pod názvem *https* do vašich gitových odkazů.
Budete vyzváni k zadání uživatelského jména a hesla na GitHubu.
Pokud jste aktivovali dvoufaktorové ověření na GitHubu,
můžete vytvořit „osobní přístupový token

a použijte ho jako heslo. Pro přístup k repozitáři postačí povolit „repo“.

.. poznámka::
Zdrojový adresář s názvem *~/src/user* nebyl zkompilován na větvi, ale na odděleném revizi:
Toho je dosaženo tím, že se stavby pracují s konkrétními revizemi místo větví.
To znamená, že můžete mít více verzí na stejném větvení, ale na různých revizích.

Jakmile vaše změny budou připraveny k publikaci
podle vašeho chování při tlačení větví:
může být vytvořen nový projekt. Můžete pokračovat ve své práci na editoru, který jste poslali.
Jakmile bude mít stejnou revizi jako nová verze, která byla vytvořena, ale vždy se ujistěte, že je
v editačním režimu pro stavbu používající nejnovější revizi vašeho větvení.

Konzole
========

Můžete otevřít konzoly Pythonu, které jsou
„Interaktivní konzole IPythonu <https://ipython.readthedocs.io/en/stable/interactive/tutorial.html>“.
Jednou z nejzajímavějších novinek je možnost používat konzoli v Pythonu
spíše než interaktivní prostředí IPython v terminálu je
„bohatý výstup <https://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display>“
schopnosti.
Díky tomu budete moci zobrazovat objekty v HTML.

Můžete například zobrazit buňky souboru CSV pomocí
Pandas <https://pandas.pydata.org/pandas-docs/stable/tutorials.html>.

.. obrázek: online-editor/interface-editor-console-python-read-csv.png
:align:center

Můžete také otevřít konzolu Odoo Shell a hrát si
s registrem a metodami vaší databáze. Můžete také přímo číst nebo psát
na vašich záznamů.

.. varování:
V konzole Odoo jsou transakce automaticky zavřeny.
To znamená například, že změny v záznamu jsou aplikovány efektivně v databázi.
Pokud změníte jméno uživatele, je v databázi změněno i jeho jméno.
Proto byste měli používat konzoly Odoo na produkčních databázích opatrně.

Můžete použít *env*, abyste zavolali modely databáze, například:

... kódový blok::python

env['res.users'].hledat_čtení([], ['jméno', 'e-mail', 'přihlašovací jméno'])
[{'id': 2,
'login': 'admin',
'name': 'Administrátor',
'email': 'admin@example.com']

Třída Pretty vám umožňuje
pro snadné zobrazení seznamů a diktátorů v pěkném způsobu.
„bohatý výstup <https://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display>“
viz výše.

.. obrázek: online-editor/interface-editor-console-odoo-pretty.png
:align:center

Můžete také použít
Pandas <https://pandas.pydata.org/pandas-docs/stable/tutorials.html>
Zobrazit grafy.

.. obrázek: online-editor/interface-editor-console-odoo-graph.png
:align:center
