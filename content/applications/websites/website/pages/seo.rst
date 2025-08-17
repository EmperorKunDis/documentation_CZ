================================
Optimalizace pro vyhledávače (SEO)
================================

Optimalizace vyhledávačů, často zkráceně jako SEO, je digitální marketingová strategie, která má za cíl zlepšit
viditelnosti webu a jeho umístění ve výsledcích vyhledávání (např. v Google). Zahrnuje optimalizaci
různé prvky na vašem webu, včetně jeho obsahu, sdílení na sociálních sítích, URL adres, obrázků a stránek.
rychlost.

.. poznámka::
   - Odoo nabízí několik modulů, které vám pomohou s tvorbou obsahu webu, například
:doc:`e-commerce <../../ecommerce>“, :doc:`blog <../../blog>“ a „e-learning
<../../e-learning>, a :doc:`Fórum <../../forum>“.
   - Všechny šablony Odoo se zakládají na frameworku Bootstrap.
<https://getbootstrap.com/>_ a optimalizovat na zařízení: stolní počítač, tablet,
nebo mobilní, což pozitivně ovlivňuje hodnocení ve vyhledávačích.

.. viz též:
„Magická tabulka – optimalizujte svůj web [PDF]


Optimalizace obsahu
====================

Pro optimalizaci webové stránky z hlediska SEO přejděte na stránku, poté klikněte na:
Optimalizace pro vyhledávače.

.. obrázek: seo/optimize-seo.png
:alt:Optimalizace pro vyhledávače

Meta tagy
---------

Meta tagy jsou HTML prvky, které poskytují informace vyhledávačům a webovým stránkám.
návštěvníci. Hrají důležitou roli v optimalizaci pro vyhledávače tím, že pomáhají vyhledávačům porozumět obsahu a
kontextu webové stránky a přilákat návštěvníky atraktivním obsahem. Existují dva typy metadat
v Odoo:

- :guilabel:`Title“ tagy určují název webové stránky a jsou zobrazeny jako klikací odkaz v vyhledávání.
výsledky motoru. Měly by být stručné, popisné a odpovídat obsahu stránky.
aktualizovat název stránky nebo nechat prázdný, aby se použil výchozí název na základě názvu stránky
obsah.

- :guilabel:Popisky stránek obsahují stručný popis jejich obsahu, často zobrazený ve vyhledávači.
výsledky pod nadpisem. Jsou používány k tomu, aby uživatele přiměly navštívit stránku. Můžete je aktualizovat
popisku stránky nebo nechat prázdný, aby se použil výchozí hodnota podle stránky.
obsah.

.. poznámka::
Karta Preview zobrazuje, jak by měly vypadat titulek a popisky ve vyhledávání.
výsledky a také odkaz na vaši stránku.

Klíčová slova
--------

Klíčová slova jsou jedním z hlavních prvků optimalizace pro vyhledávače. Web, který je dobře optimalizován pro vyhledávače
mluví stejným jazykem jako potenciální návštěvníci a klíčová slova pro optimalizaci vyhledávačů jim pomohou spojit se.
Váš web.

Do pole „Klíčové slovo“ můžete zadat klíčová slova, která považujete za důležitá, a poté kliknout
:guilabel:'PŘIDAT' a podívejte se, jak jsou používány na různých úrovních vašeho obsahu (nadpisy 1. a 2. úrovně, název stránky).
popis stránky, obsah stránky a související vyhledávání v Googlu. Nástroj také navrhuje relevantní
klíčová slova, která přivedou na váš web návštěvníky. Čím více klíčových slov je na vaší stránce, tím lépe.

..tip:
Je silně doporučeno používat na stránce jen jedno nadpisové označení H1 pro SEO.

Obrázek pro sdílení na sociálních sítích
----------------------

Když sdílíte svou stránku na sociálních sítích, je zvolen obrázek loga, ale můžete nahrát jakýkoli jiný.
Obrázek kliknutím na šipku nahoru.

.. Poznámka:
   - Karta „Společenský náhled“ zobrazuje, jak by se informace na stránce objevily, kdyby
sdílené.
   - Pokud změníte název příspěvku nebo produktu, změny se projeví
automaticky na všech stránkách vašeho webu. Starý odkaz stále funguje, pokud se na něj
použít 301 přesměrování, které zachovává SEO odkazovou sílu.

Obrázky
======

Velikost obrázků má významný vliv na rychlost stránky, což je zásadní kritérium
vyhledávače pro optimalizaci hodnocení SEO.

..tip:
Porovnejte, jak se váš web umisťuje pomocí nástroje „Rychlost stránky Google <https://pagespeed.web.dev/?utm_source=psi&utm_medium=redirect>“
nebo „Test rychlosti webu Pingdom <https://tools.pingdom.com/>“.

Odoo automaticky komprimuje nahrané obrázky a převádí je do formátu WebP.
Obrázky jsou menší, což zrychluje načítání stránky a tím pádem i hodnotu webu
SEO. Všechny obrázky použité v oficiálních šablonách Odoo jsou také komprimovány
Výchozí nastavení. Pokud používáte třetí stranu téma, může poskytnout obrázky, které nejsou komprimované
Efektivně.

**Upravit obrázek** z webu vyberte obrázek, klikněte na „Upravit“ a poté přejděte do
Kartě „Nastavení“, upravte formát v sekci „Obrázek“.

.. obrázek::seo/image-format.png
:alt: automatické komprese obrázků

.. důležité:
Alt tagy se používají k poskytnutí kontextu tomu, co obrázek zobrazuje, a informují vyhledávače.
spiderům a umožnit jim správně indexovat obrázek. Přidáním klíčových slov do alternativních
:guilabel:`Popis stránky“ je z hlediska SEO nezbytný. Tento popis se přidává do
HTML kód vaší fotografie a zobrazí se v případě, že není možné obrázek zobrazit.

Pokročilé funkce
=================

Strukturované datové značky
----------------------

Strukturované datové značky se používají k generování bohatých výsledků vyhledávání. Jde o způsob, jak
webové stránky pro odesílání strukturovaných dat robotům vyhledávačů, které pomáhají pochopit obsah vašich stránek.
Vytvářet dobře prezentované výsledky vyhledávání.

Výchozí nastavení Googlu podporuje mnoho „bohatých výstupů <https://developers.google.com/search/blog/2009/05/introducing-rich-snippets>“
pro typy obsahu, včetně recenzí, lidí, produktů, podniků, událostí a organizací.

Mikrodatové značky jsou sadou tagů, které byly zavedeny s HTML5 a pomáhají vyhledávačům lépe pochopit obsah vašich stránek.
obsah a zobrazit jej vhodně. Odoo implementuje mikrodatové prvky podle definice v Schema.org
„Specifikace <https://schema.org/docs/gs.html>“ pro události, elektronické obchodní produkty, příspěvky na fóru a
kontaktní adresy. To umožňuje zobrazit vaše produktové stránky v Googlu pomocí dalších informací
Jako je cena a hodnocení produktu:

.. obrázek:seo/data-markup.png
:alt: ukázky v výsledcích vyhledávání

robots.txt
----------

Soubor robots.txt instruuje vyhledávače, které části webu smějí procházet.
přístupu. Jeho primárním účelem je:

 - **Zamezte přetížení webu:** Pomocí souboru robots.txt odvedete roboty od některých částí webu.
pomáhá řídit zatížení serveru.
 - **Kontroluj přístup k zdrojům a podrobné popisy:** Může zabránit spiderům v přístupu
médií (obrázky a videa), kaskádových stylů (CSS) a skriptů JavaScriptu.
(textu) konkrétních stránek.

Při indexování webu vyhledávače nejprve zkontrolují soubor robots.txt. Odoo automaticky
vytváří jeden soubor robots.txt dostupný na adrese „mydatabase.odoo.com/robots.txt“.

.. poznámka::
Reputabilní boti dodržují soubor robots.txt, jiní mohou vyžadovat blokování
:ref:`Cloudflare <doména bez doménového jména/naked/cloudflare>“ na vlastní doméně.

Upravte soubor robots.txt
~~~~~~~~~~~~~~~

Pomocí souboru robots.txt můžete kontrolovat, které stránky webu jsou pro vyhledávače dostupné
skrývače. Chcete-li přidat vlastní pokyny do souboru, přejděte na:
→ Nastavení“, posuňte se dolů do části „SEO“ a klikněte na „Upravit soubor robots.txt“.

Příklad:
Pokud nechcete, aby roboti procházeli stránku „O nás“ na vašem webu, můžete ji upravit.
robots.txt souboru přidat řádek „Disallow: /o-nas“.

.. důležité:
„Robots.txt“ zabraňuje indexování obsahu, ale **nezaručuje, že stránka
nebudou indexovány**. Stránka se může v hledaných výsledcích objevit, pokud je odkazována z jiných stránek.
indexované stránky (označené „odkazem“). Obecně se nedoporučuje používat soubor robots.txt k
Zablokujte stránky, které chcete úplně vyloučit ze výsledků vyhledávání.

Zabránit indexování stránky
---------------------------------

Pokud chcete zabránit tomu, aby se stránka objevila ve výsledcích vyhledávání, použijte některou z následujících možností.
Metody:

 - **Nezobrazit v indexu:**Přejděte na stránku a přepněte
vypnout přepínač „Indexované“.

....... poznámka::
Tato možnost zatím není dostupná pro dynamické stránky:ref:`<web/stranky/typ-stranky>`.

 - **404 nebo 403:** Konfigurujte stránku tak, aby vrátila stavový kód 404 (Nenalezeno) nebo 403 (Zakázáno).
kódy. Tyto kódy signálují vyhledávačům, že stránka neexistuje nebo je nedostupná.
To nakonec vedlo k jeho vyřazení z indexu.

    - **404:**:ref:`Nastavte přesměrování na stránku 404. <webová stránka/stránky/URL-přesměrování>“
    - **403:**Přejděte na stránku a zobrazte její vlastnosti:
a přepnout vypínač viditelnosti nebo stránku :ref:`nepublikovat <webová stránka/stránky/nepublikovat-stránku>`.

 - **Google Search Console:**Použijte Google Search Console k požadavku na odstranění konkrétních URL adres.
Index Googlu.

.. viz též:
   - :doc:`../konfigurace/google_search_console`
   - :doc:`../stránky`

Sitemap
-------

Mapa webu ukazuje vyhledávačovým robotům stránky a jejich vzájemné souvislosti.
generuje soubor s názvem „/sitemap.xml“, který obsahuje všechny URL adresy. Pro účely výkonu je tento soubor uložen do cache
a aktualizované každých 12 hodin.

.. poznámka::
Pokud má váš web mnoho stránek, Odoo automaticky vytvoří soubor s mapou stránek, který respektuje
„Sitemaps.org protokol <http://www.sitemaps.org/protocol.html>“, který seskupuje URL adresy sitemapů
45 000 částí na soubor.

Každý záznam mapy webu má tři atributy, které jsou vypočítány automaticky:

- <loc>: URL stránky.
- <lastmod>: datum poslední aktualizace zdroje, vypočítané automaticky na základě souvisejících
objekt. Pro stránku související s produktem by mohlo jít o datum poslední změny produktu
nebo stránku.
- „<priority>“: moduly mohou implementovat svůj algoritmus prioritizace na základě jejich obsahu (například
diskusní fórum může určit prioritu na základě počtu hlasů v konkrétním příspěvku. Priorita
Stránka je statická podle jejího pole priority, které je normované (výchozí hodnota je 16).

..tip:
aby se stránky neobjevily v mapě webu, přejděte na kartu „Webová stránka“ a klikněte
přejděte na záložku „Publikovat“ a vypněte funkci „Indexované“.

.. obrázek:: seo/page-properties.png
:alt:  vypnutí zaškrtávacího políčka „Indexované“

Hreflang HTML tagy
------------------

Odoo automaticky přidává tagy hreflang a x-default do kódu vašeho webu.
multijazyčných stránek. Tyto atributy HTML jsou zásadní při informování vyhledávačů o konkrétním
jazykové a zeměpisné cílení stránky.

.. viz též:
:doc:`../konfigurace/překlady`
