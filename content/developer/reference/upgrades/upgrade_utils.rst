=============
Aktualizace nástrojů
=============

„Upgrade utils <https://github.com/odoo/upgrade-util/>“ je knihovna, která obsahuje funkce
aby se usnadnilo psaní upgradovacích skriptů. Tato knihovna je používána společností Odoo pro upgradeové skripty
standardní moduly, které zvyšují spolehlivost a urychlují proces upgradu:

- Funkce pomáhají zajistit, aby byla v databázi uložena konzistentní data.
- Zajišťuje nepřímé odkazy na aktualizovaná data.
- Umožňuje volání funkcí a vyhýbá se psaní kódu, což šetří čas a snižuje rizika vývoje.
- Asistenti umožňují soustředit se na důležitá témata a neřešit detaily.

Instalace
============

Klonujte místní repozitář „Upgrade utils <https://github.com/odoo/upgrade-util>“ a spusťte
„odoo“ s příponou „--upgrade-path src“.

.. kódový blok: konzole

$ ./odoo-bin --upgrade-path=/cesta/k/upgrade-util/src,/cesta/k/dalšímu/skriptu/pro/aktualizaci [...]

Ve službách, kde se Odoo neinstaluje ručně, lze tuto knihovnu nainstalovat pomocí příkazu pip:

.. kódový blok: konzole

$ python3 -m pip install git+https://github.com/odoo/upgrade-util@master

Na stránce „Odoo.sh <https://www.odoo.sh/>“ se doporučuje přidat ho do souboru
Vlastní repozitář. Pro tento případ přidejte následující řádek do souboru:

odoo_upgrade @ git+https://github.com/odoo/upgrade-util@master

Použití upgrade utils
===================

Následující balíčky jsou k dispozici pro skripty aktualizace po instalaci:

- :mod:`odoo.upgrade.util`: samotná třída pomocníka.
- :mod:`odoo.upgrade.testing`: základní třídy testovacího případu.

Pro použití v upgradovacích skriptech je nutné jej do projektu přidat:

... kódový blok:: python

od odoo.upgrade import util


def migrate(cr, verze):
      # Další část scénáře

Nyní jsou funkce pomocníků k dispozici pro volání skrze „util“.

Funkce util
==============

Upgrade utils poskytuje mnoho užitečných funkcí pro usnadnění procesu upgradu. Zde popisujeme některé
z nejvíce užitečných. Připojte se k adresáři
<https://github.com/odoo/upgrade-util/tree/master/src/util> pro komplexní deklaraci
Funkce pomocné.

.. poznámka::

Parametr :attr:`cr` v funkcích pro práci s databází vždy odkazuje na databázový kurzor. Prosím,
Přiřazené jako parametr metodě :meth:`migrate`, ale ne všechny funkce potřebují tento parametr.

...současný modul:odoo.upgrade.util

Moduly
-------

...automoduly: odoo.upgrade.util.modules
:členové:

Modelky
------

..automodul: odoo.upgrade.util.models
:členové:

Pole
------

..automodul: odoo.upgrade.util.fields
:členové:

Rekordy
-------

..automodul: odoo.upgrade.util.records
:členové:

ORM
---

...automodul: odoo.upgrade.util.orm
:členové:

..automodul: odoo.upgrade.util.domains
:členové:

SQL
---

...automodul: odoo.upgrade.util.pg
:členové:

Miscellaneous
----

..automodul: odoo.upgrade.util.misc
:členové:
