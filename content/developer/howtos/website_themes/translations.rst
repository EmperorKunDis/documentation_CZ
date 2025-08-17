============
Překlady
============

S Odoo můžete svou webovou stránku přeložit do různých jazyků.

V této kapitole se naučíte:

- Přeložte obsah modulu.
- Překlady dovozu a vývozu.
- Přidejte překlad do modulu.

.._webové šablony/překlady/výchozí:

Frontend
========

Pro překlad stránek pomocí Webového tvůrce přejděte na svou webovou stránku a klikněte na jazyk
vyberte jazyk, který chcete přeložit. Pokud váš web nikdy nebyl přeložen do cílového jazyka, klikněte na
Vyberte „Přidat jazyk…“ v dialogovém okně, vyberte jej a klikněte na „Přidat“.

Klikněte na tlačítko „Přeložit“ a začněte překládat. V závislosti na jazyce se může zobrazit nějaký text.
automaticky přeloženy a zvýrazněny zelenou barvou. Všechno, co by mělo být
ručně je zvýrazněno žlutě.

.. obrázek:translations/translate-button.png
:alt:Tlačítko pro překlad
:šířka: 570

Ale musíte pochopit, co se děje pod kapotou, když překládáte něco.
pomocí Webového editoru.

... /webové šablony/překlady/přední stránky:

Stránky výchozí
-------------

Odoo vytvoří základní pohled jednou, když je webová stránka nainstalovaná. Pokud upravíte stránku pomocí Builderu,
bude vytvořen kopírovací pohled a všechny vaše úpravy budou uloženy do této jedné.
přeložené verze také). Jedinou výjimkou je domovská stránka (v základu vytvoří Odoo základní
duplikovaný pohled ještě předtím, než provedete jakoukoli úpravu.

.. obrázek: translations/translations-page.png
:alt:Duplicitní překlad

Doporučujeme být velmi opatrný ohledně pořadí, v jakém budete překlady provádět nebo
změny v zdrojovém jazyce, ať už stránku vytvoříte pomocí Webové stavby nebo
přes zdrojový kód s rekordem. Pozor, každá jednotlivá změna zdrojového jazyka
(„Upravit hlavní verzi“) přeruší vazbu mezi zdrojovým jazykem a existujícími překlady.
tedy pokud upravíte zdrojový jazyk, budete muset překlady znovu vytvořit.

... /webové-šablony/překlady/přední část/stringy:

Přeložitelné řetězce
--------------------

... /webové šablony/překlady/přední část/stringy/t-att:

t-att-/ t-attf-
~~~~~~~~~~~~~~~~

Pokud chcete nastavit přeložitelný řetězec, použijte raději t-attf- namísto t-att-, pokud
možné.

**Příklad**

Napsat „Ahoj *uživatelské jméno*“ lze následovně:

... blok kódu::xml

<div t-attf-title="Ahoj, # {user.name}">

.. varování:

Můžete dosáhnout stejného výsledku i pomocí atributu t-att-title, jak je vidět na příkladu níže.
výsledek nebude považován za přeložitelnou střední řetězcovou hodnotu:

... kódový blok :: XML

<div t-att-title="'Ahoj' + uživatelské jméno" />

.._webové šablony/překlady/přední část/soubory s výjimkami:

Výjimka: t-hodnota/t-hodnotaf
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

„t-value“ a „t-valuef“ jsou trochu odlišné. Žádný z nich není přesně překládán, takže
Mohlo by vypadat nějak takto:

... blok kódu::xml

<t t-set="přidatitulek">Titulní stránka zobrazená v záložce prohlížeče</t>

Při psaní kontextu XML lze překládat text mezi dvěma XML tagy.

.._webové šablony/překlady/přední část/stringy/míchání:

Míchání přeložitelného a nepřeložitelného
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V situaci, kdy potřebujeme nastavit pouze jednu jedinou
místo:

... blok kódu::xml

<t t-set="title">Foo</t>

A pak je potřeba ji zavolat na různých místech:

... blok kódu::xml

<div t-att-title="label" />
    ...
<nav t-att-title="label" />

Tady jsme jen přejmenovali překladitelný obsah na neprekladatelnou vlastnost („t-att-title“).
Proměnná t-att-title není přeložitelná, ale proměnná obsahující hodnotu je.

.. /webové-šablony/překlady/administrace:

Backend
=======

Přímý překlad stránek z administrace umožňuje přeložit více jazyků najednou.
čas. Pro to je potřeba zajít na: „Nastavení -> Technické -> Uživatelské rozhraní: Zobrazení“, vyhledat
Název stránky, kterou chcete přeložit, a klikněte na tlačítko „Upravit překlady“.

.. obrázek: edit_translations.png
:alt: Upravit překlady
:šířka: 718

.. _webové šablony/překlady/export:

Export
======

Jakmile dokončíte překlad, musíte překlady exportovat a integrovat je do vašeho
modul. Chcete-li vše najednou exportovat, otevřete databázi, aktivujte režim vývojáře
<rozvojová verze>, a přejděte na: „Nastavení“ --> „Překlady“ --> „Export překladu“.
Vyberte jazyk, který překládáte, soubor PO v sekci Formát souboru a
*webová stránka_vzduchotěsná* jako :guilabel:`Aplikace k exportu.

Stáhněte si soubor a přesuňte jej do složky :file:`i18n`. Pokud je potřeba, můžete ručně upravit
Po ukončení programu se vytvoří soubor s příponou .po.

... /webové-šablony/překlady/po:

PO soubor
=======

Přeložit lze přímo editací souboru .po nebo vytvořením nového souboru. Podívejte se na
:doc:`překlad modulů dokumentace <../translations>“ pro psaní svých překladů.

.. kódový blok:: po


   #. modul: webová_vzduchotěsnost
   #:model_terms:ir.ui.view,arch_db:website_airproof.s_custom_snippet
msgstr ""
msgstr "...

.. /webové-šablony/překlady/import:

Dovoz
======

Pro import vašich překladových souborů do Odoa přejděte na: „Nastavení > Překlady >
Importujte překlady z aplikace „Import Translation“ a nahrajte je.
