Zobrazit obsah

========================
Zvládněte webový rámec
========================

.. toctree::

:glob:

master/odoo-web-framework/*

Tento návod je určen pro ty, kteří absolvovali kurz „discover_js_framework“.
se chtějí dozvědět více o webovém rámci. Je organizována ve čtyřech nezávislých
projekty zaměřené na různé funkce systému Odoo.

.. poznámka::

Každá z těchto kapitol může být provedena samostatně a v jakémkoliv pořadí. Dále je nutné si uvědomit, že některé z nich
Obsahují mnoho informací, takže mohou být poměrně dlouhé.

První projekt se týká stavby „klikací hry“ (https://cs.wikipedia.org/wiki/Inkrementální_hra).
Prací na něm se naučíte různé aspekty webového frameworku: systray, nabídku příkazů.
dialogy, notifikace, přizpůsobení stávajících komponent a mnoho dalšího.

Druhý projekt se zaměřuje na důležitou kategorii komponent - pole. Komponenty pole
Zastupují hodnotu pole pro záznam, objevují se na mnoha místech v webovém klientovi: ve formulářích
zobrazení, ale také v zobrazeních Kanban a Seznamy a může být použito i samostatně bez zobrazení.
Vzhledem k jejich důležitosti je vhodné se naučit, jak takové komponenty vytvářet a manipulovat s nimi.

V kontextu webového rámce se obvykle jedná o implementaci v JavaScriptu.
komponenta, která reprezentuje jeden nebo více záznamů podle popisu (ir.ui.view).
komponenty jsou ve skutečnosti poměrně složité a obvykle vyžadují různé podsystémy (renderer,
model, kontroler, arch parser, ...). V kapitole 3 vytvoříme nový pohled od základu.
Je to seznam obrázků.

Poslední projekt v kapitole č. 4 se týká přizpůsobení stávajícího pohledu (kanbanu).
přidává dole plochu pro vyhledávání. Je zajímavé vidět, jak lze použít stávající kód a
upravit ji tak, aby vyhovovala našim potřebám. Projekt je také reálný a bude obsahovat mnoho běžných problémů
která vznikne při práci na Odoo.


... /tutoriály/master_odoo_web_framework/setup:

Nastavení
=====

#Klonujte repozitář oficiálních návodů k Odoo (<https://github.com/odoo/tutorials>).
větve {CURRENT_MAJOR_BRANCH}.
#Přidejte do svého cesty ke knihovně modulů (viz příkaz odoo-bin --addons-path):
#Začněte novým databázovým serverem Odoo a nainstalujte moduly pro každou kapitolu, kterou chcete pracovat.
„Awesome Clicker“ (pro kapitolu 1), „Awesome Fields“ (pro kapitolu 2), „Awesome Gallery“ (pro kapitolu 3) nebo „Awesome Kanban“ (pro kapitolu 4).

Obsah
=======

- :doc:`master_odoo_web_framework/01_build_clicker_game`
- :doc:`master_odoo_web_framework/02_create_gallery_view`
- :doc:`master_odoo_web_framework/03_customize_kanban_view`
