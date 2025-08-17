=============================
Kapitola 5 – Dynamické šablony
=============================

... _návody/webový šablona/dynamické šablony/eshop:

Upravte šablonu obchodu
=======================

Teď si ukážeme, jak upravit dynamické části webu. Jako jistě víte, některé stránky jako například ty pro
E-commerce je automaticky generován. Stránky jako obchod, produkt a objednávka jsou automaticky
generované při instalaci aplikace „webová prodejna“. Tyto šablony stránek získávají
zobrazované informace z back-endu.

Pro úpravu těchto stránek je nutné upravit standardní šablonu Odoo. Toho lze dosáhnout pomocí SCSS.
předvolby a zejména XPath. Najděte šablonu Odoo, kterou chcete upravit a rozšířit
použijeme „XPath“. Podle návrhu Airproof začneme úpravami obchodního pohledu.

#Nejprve najděte šablonu v Odoo: menuselection: „webové prodeje“ -> „templates.xml“ ->
id="produkty".
#Aplikujte všechny změny ve svém souboru:

   - Přidejte banner.
   - Adaptujte uspořádání kategorií filtrování na levé straně.
   - Odeberte vyhledávací lištu (můžete ji odstranit z obou stránek s produkty).
času.
   - Přesuňte oříšek.
   - Skryjte možnost zobrazení seznamu nebo mřížky.
   - Vytvořte vhodný design a informace pro produktové karty.

.. obrázek: 05_dynamické šablony/airproof-eshop-stránka.png
:align:center

..tip:
   - Aplikujte své úpravy pomocí předvoleb, XPath a SCSS.
   - Pro možnost filtrování atributů/variant aktivujte
:doc:`/aplikace/prodej/prodej/produkty-ceny/produkty/varianty` možnost v
nastavení webového back-endu a :ref:`konfigurace atributů a variant
</ecommerce/produkty/varianty_produktu> pro produkty.

..spoiler:: Řešení

Najděte řešení v našem příkladu Airproof ve souboru presets.xml

část „stránka obchodu“ v souboru views/website_sale_templates.xml,
`shop.scss <{GITHUB_TUTO_PATH}/website_airproof/static/src/scss/pages/shop.scss>`.

... _návody/webové šablony/dynamické šablony/produkt:

Upravte šablonu stránky produktu
===============================

Klient je nadšený z úprav obchodu. Teď nás čeká aplikace našeho designu na produkt
stránky. Změňte několik prvků včetně:

- Odeberte vyhledávací lištu (pokud ji neodstraníte v předchozím cvičení).
- Odeberte výběr množství, podmínky a ikony sdílení.
- Aktualizujte ikonu tlačítka „Přidat do košíku“.
- Vložte nad popisem produktu titulek (tato sekce se zobrazí pouze v případě, že je
Je třeba mít na paměti, že každá vlastnost má pouze jednu variantu.
- Navrhněte vhodný design pro kolotoč.
- Přidejte název a aplikujte vytvořený šablonu produktu na Alternativní produkty.
oddíl (zajistit, aby se alternativní produkty přiřadily k produktu v administraci pro tento oddíl
aby se objevily.
- Zavedení nové oblasti pro odložení produktů pod detailními informacemi o produktech, které jsou viditelné na všech produktech. Příklad použití:
„Text-Obraz“ blok pomocí Webové stránky (např.: viz obrázek produktu Airproof)
s „Šest důvodů, proč si koupit...“).

.. viz též:
Podívejte se na odkazovanou dokumentaci, jak vytvořit :ref:`webové šablony/layout/dropzone`.

.. obrázek: 05_dynamické šablony/airproof-produkt.png
:align:center

..tip:
   - Proveďte své úpravy pomocí předvoleb, XPath a SCSS. Komentujte svůj kód správně
Pomůže vám orientovat se ve městě.
   - Zóna pádu bude viditelná na všech produktech. Chcete-li vytvořit pro konkrétní produkt specifickou zónu pádu,
Musíme přidat novou položku do produktového modelu.

..spoiler:: Řešení

Najděte řešení v našem příkladu Airproof ve souboru presets.xml

<{GITHUB_TUTO_PATH}/website_airproof/views/website_sale_templates.xml> část „stránka produktu“
`product_page.scss <{GITHUB_TUTO_PATH}/website_airproof/static/src/scss/pages/product_page.scss>`.
