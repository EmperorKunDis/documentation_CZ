... _tutorials/server_framework_101/01_architektura:

================================
Kapitola 1: Architektonický přehled
================================

Aplikace s více vrstvami
=====================

Odoo používá architekturu „vícevrstvého systému“, což znamená, že prezentace, obchodní
Logika a ukládání dat jsou odděleny. Konkrétněji používá třívrstvou architekturu
Obrázek z Wikipedie:

.. obrázek: 01_architektura/tri-vrstvy.svg

:alt:Třívrstvá architektura

Představovací vrstva je kombinace HTML5, JavaScriptu a CSS. Logická vrstva je výhradně
napsaný v Pythonu, zatímco vrstva dat podporuje pouze PostgreSQL jako relační databázi.

V závislosti na rozsahu vašeho modulu může být vývoj v kterémkoliv z těchto pater prováděn.
Proto je dobré si před dalším čtením připomenout, pokud neznáte
střední úroveň v těchto tématech.

Projít si tento návod budete potřebovat velmi základní znalosti HTML a středně pokročilé
úroveň Pythonu. Předměty pokročilé úrovně vyžadují větší znalosti z ostatních předmětů.
Je jich spousta a jsou volně dostupné, takže nemůžeme doporučit jednu před druhou, protože záleží
na vašem pozadí.

Pro přehled je zde oficiální „Příručka pro Python“.

.. poznámka::
Od verze 15.0 se Odoo aktivně přechází na používání vlastního interně vyvinutého „OWL
framework <https://odoo.github.io/owl/> jako součást své prezentační vrstvy. Legacy JavaScript
Rámec stále podporuje, ale bude postupně zastaralý. Toto téma bude dále diskutováno v
pokročilá témata.

Moduly Odoo
============

Serverové i klientské rozšíření jsou baleny jako moduly, které
volitelně v databázi. Modul je soubor funkcí a dat, které mají za cíl
jediným účelem.

Moduly Odoo buď přidávají novou obchodní logiku do systému Odoo nebo
změnit a rozšířit stávající logiku podnikání. Může být vytvořen jeden modul, který přidává vaše
účetní pravidla země do podpory účetnictví v Odoo.
Další modul přidává podporu pro vizualizaci v reálném čase celé flotily autobusů.

Vše v Odoo začíná a končí moduly.

Terminologie: vývojáři seskupují funkce svého podnikání v modulu Odoo. Hlavní uživatelsky orientované
moduly jsou označeny jako aplikace, ale většina modulů není aplikací. Moduly
Mohou být také označovány jako „doplňky“ a adresáře, kde najde server Odoo.
vytvořit „cestu k doplňkům“.

Složení modulu
-----------------------

Modul Odoo může obsahovat několik prvků:

:ref:`Objekty obchodního modelu <reference/orm>`
Objekt podnikání (např. faktura) je deklarován jako třída v Pythonu. Definované pole
tato třída je automaticky přiřazena k databázovým sloupcům díky
:zkratka:„vrstva pro mapování objektů a relačních tabulek“

:doc:`Pohledy na objekty <../../reference/user_interface/view_architectures>`
Definujte zobrazení uživatelského rozhraní

:ref:`Datové soubory <reference/data>`
XML nebo CSV soubory, které deklarují datové modely:

    * :doc:`pohledy <../../reference/user_interface/view_architectures>“ nebo
:ref:`zprávy <odkaz/zpravy>`,
    * konfigurační data (parametrizaci modulů, :ref:`bezpečnostní pravidla <reference/security>`)
    * Demonstrační data
    * a více

:ref:`Webové kontroly <reference/controllers>`
Zpracovávat požadavky webových prohlížečů

Statická data z webu
Obrázky, soubory CSS nebo JavaScriptu používané webovým rozhraním nebo webovou stránkou

Žádný z těchto prvků není povinný. Některé moduly mohou obsahovat pouze soubory dat (např. zeměpisně specifické).
konfigurace účetnictví) a jiní mohou přidávat pouze objekty podnikání. Během této školení budeme
vytvářet objekty, pohledy na objekty a soubory dat.

Modulová struktura
----------------

Každý modul je adresář v rámci adresáře s názvem „modul“. Adresáře s názvem „modul“
jsou specifikovány pomocí příkazu :option:`--addons-path <odoo-bin --addons-path>
option.

Modul Odoo je deklarován v jeho :ref:`manifestu <reference/module/manifest>“.

Když modul Odoo obsahuje objekty podnikání (tj. soubory Pythonu), jsou uspořádány jako
„Balíček Pythonu <https://docs.python.org/3/tutorial/modules.html#packages>“
s souborem „__init__.py“. Tento soubor obsahuje příkazy pro doimportování různých verzí Pythonu
soubory v modulu.

Tady je jednodušší seznam modulů:

... kódový blok:: bash

modul
├── models
│   │   └── *.py
│   └── __init__.py
├── data
│   └── *.xml
├── __init__.py
└── __manifest__.py

Odoo Edition
=============

Odoo je k dispozici ve dvou verzích: Odoo Enterprise (licencovaná verze s otevřeným zdrojovým kódem) a Odoo Community
(zdrojový kód). Kromě služeb jako je podpora nebo aktualizace poskytuje verze Enterprise další
funkcemi do Odoo. Z technického hlediska jde o jednoduché
nové moduly, které jsou instalovány na vrcholu modulů poskytovaných verze komunity.

Připraveni začít? Nyní je čas napsat vlastní aplikaci podle návodu :doc:`Napište si svou vlastní aplikaci <02_newapp>!`

.._architektura s více vrstvami:
    https://en.wikipedia.org/wiki/Multitier_architecture

.._Tutoriál v Pythonu
    https://docs.python.org/3.7/tutorial/

... dvě verze:
    https://www.odoo.com/page/editions
