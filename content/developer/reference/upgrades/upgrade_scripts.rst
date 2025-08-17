===============
Upgrade skripty
===============

Upgrade skript je soubor Pythonu obsahující funkci :meth:`migrate`, kterou používá upgrade.
Proces, který probíhá během aktualizace modulu.

... metoda: migrace(cr, verze)

:param cr: aktuální kurzor databáze
:typ cr: :třída odoo.sql_db.Cursor
:param str verze: nainstalovaná verze modulu

Tato funkce obvykle spouští jednu nebo více dotazů SQL a může také přistupovat k ORM Odoo.
i s příponou .doc././upgrade_utils.

Naprogramování skriptů pro aktualizaci
=======================

Upgrade skripty mají specifickou strukturu s určitým názvem, který určuje, kdy jsou spouštěny.
Jsou popraveni.

Struktura upgradovacího skriptu je: „$modul/migrace/$verze/před-*, po-* a koncový-*.py“.
kde `$modul` je modul pro který bude skript spouštěn a `$verze` je plná verze
modul (včetně hlavní verze Odoa a menší verze modulu) a {pre|post|end}-*.py
soubor, který se má spustit. Jméno souboru určí fázi:ref:`
<upgrade-skripty/fáze> a pořadí, v jakém je spouštěn pro daný modul a verzi.

.. poznámka::
V Odoo 13 může být také jméno hlavního adresáře pro skripty upgradu „upgrades“.
Přednost má pojmenování, protože má správný význam: slovo „migrace“ může být zaměnitelné s „odchodem“.
Odoo*: tedy i adresář: `modul/upgrade/$verze`.

.. poznámka::
Upgrade skripty jsou spuštěny pouze při aktualizaci modulu. Proto se
verze podsložky v adresáři $version musí být vyšší než verze modulu.
nainstalovaná verze a rovna nebo nižší než aktualizovaná verze modulu.

Příklad:

Struktura adresáře pro skript aktualizace na vlastní modul s názvem „Awesome Partner“
do verze „2.0“ v Odoo 17.

...: kódový blok

awesome_partner/
|-- migrace/
      |   |-- 17.0.2.0/
|  |  |-- předexklamace.py

Dva příklady skriptů pro upgrady s obsahem souboru pre-exclamation.py, který přidává
„!“ na konci jmen partnerů:

... kódový blok:: python

import logging

_logger = logging.getLogger(__name__)


def migrace(cr, verze):
cr.execute("UPDATE res_partner SET name = name || '!'"
_logger.info("Aktualizovalo se %d partnerů", cr.rowcount)

... kódový blok:: python

import logging
od odoo.upgrade import util

_logger = logging.getLogger(__name__)


def migrace(cr, verze):
env = util.env(cr)

partneři = env["res.partner"].search(list())
pro partnera v partnerech:
partner.jmeno += "!"

_logger.info('Aktualizovali jsme %d partnerů', len(partners))

Pozor na druhém příkladu, skript využívá souborového systému :doc:`./upgrade_utils`.
přístup k ORM. Podívejte se na dokumentaci, abyste zjistili více o této knihovně.

... upgrade-scripts/fáze:

Fáze upgradovacích skriptů
=========================

Proces upgradu se skládá z tří fází pro každou verzi modulu:

  #Tato fáze nastává před načtením modulu.
  #Po fázi nahrávání a aktualizace modulu a jeho závislostí.
  #Toto je konečná fáze, kdy jsou nainstalovány všechny moduly a aktualizována pro danou verzi.

Upgrade skripty jsou seskupeny podle prvního části jejich názvu do příslušné
fáze. V rámci každé fáze jsou soubory spouštěny podle jejich sémantického pořadí.

Poznámka: Vykonání příkladů skriptů pro jeden modul ve verzi

   #:soubor:pre-10-do_something.py
   #:souboru `pre-20-something_else.py`.
   #:soubor post-do_something.py
   #:soubor post-something.py
   #:soubor: `end-01-migrate.py
   #:souboru `end-migrate.py`.
