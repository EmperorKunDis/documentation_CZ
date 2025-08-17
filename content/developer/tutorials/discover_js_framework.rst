Zobrazit obsah

==========================
Objevte webový rámec
==========================

.. toctree::

:glob:

discover_js_framework/*

Tento dvoudílný návod je určen k seznámení s základy webového rámce.
Pokud jste nováčkem v rámci této platformy nebo máte nějaké předchozí zkušenosti, tento návod vám poskytne
solidní základ pro používání webového rámce ve vašich projektech.

První část se věnuje základům komponent Owl.
jsou klíčovými součástmi webové architektury. Komponenty Owl jsou použitelné uživatelské rozhraní, které lze použít
rychle a efektivně vytvářet složité webové rozhraní. Zjistíme, jak vytvořit a používat Owl
komponenty v Odoo. V druhé části tohoto návodu se zaměříme na vytváření dashboardů pomocí různých
Odoo. Panel je nezbytnou součástí každé webové aplikace a poskytuje příjemný start
použít a interagovat s kódem Odoo.

Tento návod předpokládá, že máte základní znalosti vývoje v Odoo obecně.
(modely, kontroly, QWeb, ...). Pokud jste noví v Odoo, doporučujeme začít s
Před zahájením této příručky se ujistěte, že jste si přečetli návod na serverovou architekturu.

.. poznámka::

Každá kapitola tohoto návodu je samostatným projektem. Pokud se cítíte s Owlem dobře, můžete
začít rovnou s kapitolou 2.

... _tutorials/discover_js_framework/setup:

Nastavení
=====

#Klonujte repozitář oficiálních návodů k Odoo (<https://github.com/odoo/tutorials>).
větve {CURRENT_MAJOR_BRANCH}.
#Přidejte do svého cesty ke knihovně modulů (viz příkaz odoo-bin --addons-path):
#Začněte novou databází Odoo a nainstalujte moduly „awesome_owl“ (pro kapitolu 1) a „awesome_dashboard“.
(pro kapitolu 2).

Obsah
=======

- :doc:`discover_js_framework/01_owl_components`
- :doc:`discover_js_framework/02_build_a_dashboard`
