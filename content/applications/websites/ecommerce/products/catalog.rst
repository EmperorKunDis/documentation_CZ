=======
Katalog
=======

Katalog e-commerce zobrazuje produkty, které mohou zákazníci prohlížet. Je uspořádán podle produktů
kategorie, dostupné možnosti, řazení a navigační cesty. Zkrátka e-shopový katalog
Je to stránka obchodu vašeho webu.

Katalog zboží obsahuje horní lištu, která je označována jako „top bar“ (viz ecommerce/catalog/top-bar), a boční lištu, která se nazývá „side panel“ (viz ecommerce/catalog/side-panel).
„E-shop / Katalog / Boční panel“ a „Seznam produktů“.
<ecommerce/katalog/produktový seznam>. S Odoo můžete:
<ecommerce/katalog/přizpůsobit-vzhled>`, filtrovat podle: „Kategorie a atributy“
<ecommerce/katalog/kategorie>“ a použijte další funkce
podle vašich potřeb.

Můžete si upravit stránku obchodu pomocí webového editoru. K tomu přejděte na stránku obchodu.
Klikněte na tlačítko „Upravit“ v pravém horním rohu a přejděte na záložku „Nastavení“.

.. ecommerce/katalog/hlavní lišta:

Horní pás
=======

V horní liště může být vyhledávací pole, tlačítko pro výběr měny.
:ref:`možností řazení a zobrazení<ecommerce/katalog/možnosti-řazení-a-zobrazení>“.
:ref:`rychlý přístup k kategorii <ecommerce/katalog/kategorie>“.

..._ecommerce/katalog/řazení a zobrazování možností:

Možnosti vyhledávání a zobrazování
----------------------------------

Můžete přepínat vyhledávací lištu, zobrazit kategorie :ref:`<ecommerce/catalog/categories>`.
a nebo: atributy <ecommerce/catalog/attributes>, a zapnout nebo vypnout
:guilabel:'Řadit podle' stejně jako tlačítka pro zobrazení :ref:'vzhledu <ecommerce/katalog/layout>'.
:guilabel:`Včelí roj“.

Tlačítko „Seřadit podle“ je vypnuté výchozí hodnotou a zákazníci si mohou vybrat mezi
následujících možností podle výchozích parametrů řazení:

- :guilabel:`Žádný“
- :guilabel:`Zajímavé“
- :guilabel:`Nejnovější příjezdy“
- :guilabel:`Jméno (A-Z)`
- :guilabel:`Cena - od nejnižší k nejvyšší“
- :guilabel:`Cena - od nejvyšší po nejnižší“

Výchozí řazení se vztahuje na všechny kategorie:ref:kategorie <ecommerce/katalog/kategorie>.

..tip:
Pokud nechcete zobrazit horní lištu nebo :ref:`boční panel <ecommerce/katalog/boční-panel>`,
vše můžete vypnout v editoru webových stránek.

.._ecommerce/katalog/boční panel:

Boční panel
==========

Boční panel nabízí pokročilé filtrační nástroje, které vám pomohou organizovat vaše produktové kategorie.
Chcete-li dále rozdělit stránku obchodu podle kategorií, aktivujte
různé filtry, například filtr atributu <ecommerce/catalog/attributes>.

Můžete také přidat možnost :guilabel:`Datumový výběr`, která zobrazí kalendář s rozsahem dat, který lze ověřit.
Dostupnost pronájmu produktů v určitém časovém období.
Toto funkce vyžaduje instalaci modulu prodeje nebo pronájmu.

Je také možné přepnout přepínač :guilabel:`Skládací boční lišta`, aby se boční lišta
Manuálně sklápěcí.

..tip:
Použít filtr cenového rozpětí nebo štítků je možné pouze v případě zapnutých atributů
první je „ecommerce/katalog/atributy“.

.._ecommerce/katalog/kategorie:

Klasifikace produktů v katalogu
=================================

Kategorie elektronického obchodu slouží k uspořádání produktů do skupin, což zákazníkům usnadňuje orientaci.
Procházet online obchod.

Pro vytvoření kategorií e-commerce přejděte na:
e-commerce kategorie“ a klikněte na „Nový“. Na formuláři kategorie přidejte
:guilabel:"Jméno", možná zadejte :guilabel:"Rodičovskou kategorii" a napište :guilabel:"Kategorii".
Popis, pokud je potřeba.

Pro použití kategorií v elektronickém obchodě přejděte na: „Webová stránka“ - „Elektronický obchod“ - „Produkty“, vyberte
produkt, který chcete upravit, přejděte na záložku „Prodej“ a v navigačním panelu
V sekci „Internetový obchod“ vyberte kategorii, ke které patří.

.. poznámka::
Jedna produktová kategorie může obsahovat více obchodních kategorií.

Jakmile jsou kategorie nakonfigurovány a přiřazeny ke správným produktům, přejděte na hlavní stránku obchodu.
a otevřít editor webu. V položce „Kategorie“ můžete buď
menu v levém sloupci, tedy na :guilabel:`Levé`, tj. v :ref:`bočním panelu <ecommerce/katalog/boční-panel>`.
nebo na :guilabel:`Top“, tedy v :ref:`horním panelu <ecommerce/katalog/horní-panel>“ nebo obojím.
Pokud vyberete kategorii „Vlevo“, pak se zobrazí možnost „Sbalitelná kategorie s vnořenými kategoriemi“.
zobrazí se, což vám umožní zmenšit kategorii na bočním panelu.

.. obrázek: /katalog/kategorie-panelu-katalogu.png
:alt:Možnosti kategorií pro váš e-shop

.. viz též:
:doc:`../produkty`

.._ecommerce/katalog/atributy:

Atributy
----------

Atributy se týkají vlastností produktu, jako je například barva nebo materiál.
Varianty jsou různé kombinace atributů. Pro konfiguraci atributů a variant přejděte na
Vyberte webové stránky -> E-commerce -> Produkty. Vyberte produkt a klikněte na
Karta „Atributy a varianty“. Přidejte si atributy, kolik chcete.

.. viz též:
:doc:`../../../prodej/prodej/produkty-a-ceny/produkty/varianty`

.. obrázek:: katalog/katalog-atributy.png
:alt: Atributy a varianty vašeho produktu

Pro filtrování atributů přejděte na hlavní stránku obchodu, otevřete webový editor a nastavte
V poli „Atributy“ nastavte na „Levé“ (viz odkaz).
<ecommerce/katalog/boční panel>`) a nebo :guilabel:`Horní lišta“ (:ref:`horní lišta
<ecommerce/katalog/horní lišta>

..tip:
Když je v horním menu zapnuté filtrování atributů, zákazníci musí kliknout na ikonu
tlačítko pro přístup k němu.

Při zapnutí atributů se objeví další možnosti:

  - :guilabel:`Filtr ceny“: Zapněte přepínač, abyste zobrazili „Rozsah cen“, který
umožňuje zákazníkům filtrovat produkty podle konkrétního cenového rozmezí tahem posuvného nastavitelného
ovládání.
  - „Filtr produktových štítků“: Přepněte přepínač, aby se zobrazily „Produktové štítky“.
stránku obchodu a umožnit zákazníkům filtrovat produkty pomocí těchto štítků kliknutím na
:guilabel:`Štítky“ v části „Příslušenství“ v sekci „Nápověda“ (viz stránka „Katalog“).

..tip:
   - Pokud chcete používat tagy na svém e-shopu, přejděte do sekce „E-commerce“ - „Produktové tagy“.
a klikněte na tlačítko „Nový“. V záložce „Šablony produktů“ v dialogovém okně pro tagy produktů
přidat produkty, které se budou odkazovat na daný tag. Můžete také přidat varianty
:guilabel:`Varianty produktů“ kartě a zobrazit souhrn všech vybraných produktů.
záložku „Všechny produkty“.
   - Filtr cen funguje nezávisle na atributech a lze jej tedy zapnout samostatně.
pokud je to požadováno.

... ecommerce/katalog/produkty:

Oblast produktového vyhledávání
====================

Můžete si upravit celkový vzhled stránky obchodu i jednotlivých kategorií.
„Stránky <ecommerce/katalog/upravit-vzhled>“.

..tip:
Je také možné upravit jednotlivé stránky produktů: :ref:`produkty <ecommerce/products/product-form>`.

.._e-shop/katalog/layout:

V editoru webových stránek vyberte „layout“ podle návodu v části „Seřazení a zobrazení“.
Výchozí zobrazení nastavte buď na „Řádky“ nebo „Seznam“.

Pokračujte v nastavení rozložení pomocí následujících možností:

   - :guilabel:`Velikost“: Zadejte počet produktů na stránce a řádku.
   - :gaplabel:Vzdálenost mezi produkty: Definujte vzdálenost mezi produkty.
   - :guilabel:`Styl“: Vyberte „Výchozí“, „Kartičky“, „Miniatury“ nebo
:guilabel:`Síť“.
   - Vyberte poměr stran pro produktové obrázky:
:guilabel:`Pohled na krajinu (4/3)“, :guilabel:"Výchozí (1/1)", :guilabel:"Portrét (4/5)"
:guilabel:`Vodorovná (2/3)“. Můžete také upravit zobrazení změnou :guilabel:`Zaplnění
možnosti, které nejlépe vyhovují vašim požadavkům na design.

Přepněte na :guilabel:`Prod. Desc.` a zobrazte popis produktu pod produktem.
jméno.

..tip:
Můžete si vybrat velikost sítě, ale buďte si vědomi, že zobrazení příliš mnoha produktů může ovlivnit
výkon a rychlost načítání stránky.

Dále je možné ručně měnit pozici produktu na stránce obchodu. Pro to stačí přejít na
Hlavní stránka obchodu, klikněte na produkt a otevřete editor webových stránek. V sekci „Produkt“
Můžete si produkty přeřadit pomocí šipek. Tlačítka „<“ a „>“ umožňují posunout produkt na
extrémní levice nebo pravice a znaky „<“ a „>“ umožňují posunout jej o jednu řadu doprava nebo doleva.

..tip:
Je také možné měnit pozice produktů na stránce obchodu tím, že přejdete do
:menu-vyber=`Webová stránka --> E-commerce --> Produkty`, přepnutí na seznam a
přetahováním a vkládáním produktů do seznamu.

Produktová novinka
-----------------

Chcete-li produkt zvýraznit a tím ho lépe viditelný na stránce obchodu, postupujte takto:
na webového editora a klikněte na produkt, který chcete zvýraznit. V sekci „Produkt“
Můžete si vybrat velikost obrázku produktu kliknutím na sítko a můžete také přidat
„Páska“. Tato funkce zobrazuje pás přes obrázek produktu, například „Výprodej“,
:guilabel:„Vyprodáno“, „Není skladem“ nebo „Novinka“.

.. obrázek: /katalog/katalog-produktu-vyzdvihnuti.png
:alt:Výraznění pásu

Pro vytvoření nové lišty klikněte na zelenou ikonu „+“ (guilabel: Vytvořit) vedle
Pole „Řemínek“ a pak přidejte pole „Název řemínku“, definujte jeho „Pozici“.
a vyberte si vlastní pozadí a text. Chcete-li upravit lištu, klikněte na
Ikona „Psací potřeby“ vedle ikony „Říšský úřad“.

.. obrázek: katalog/katalog-stuhy.png
:alt: Vytvořte novou lištu.

Páska je nyní k dispozici pro všechny produkty elektronického obchodu.

..tip:
   - Jiné způsoby vytvoření nové lišty:

     - Přejděte na :menuselection:`Webová stránka --> E-commerce --> Produktové pásky“ a klikněte na :guilabel:`Nový“.
     - Aktivujte režim vývojáře (:doc:`<../../../general/developer_mode>`), přihlaste se k produktu
tvaru a pod záložkou „Prodej“ změňte nebo vytvořte lištu.
:guilabel:`Řemínek“ pole.

   - Můžete také přidat pásky pro konkrétní varianty produktu.
<ecommerce/produkty/varianty produktu>. Chcete-li tak učinit, přejděte na:
e-commerce --> Produkty a vyberte produkt. Klikněte na tlačítko „Varianty“ chytrého panelu.
vyberte variantu a přidejte stuhu do pole :guilabel:`Ribbon Variant`.
:guilabel:`Prodej“ sekce.

..._ecommerce/katalog/nastavit-vzhled:

Návrh stránky obchodu a kategorie
-----------------------------

Použijte:doc:`bloky <../../website/web_design/building_blocks>“ k přidání obsahu do obchodu
a případně kategorie.

Můžete upravit horní a/nebo dolní část katalogu, buď pro celou stránku obchodu nebo
pro konkrétní kategorii. V tomto případě se blok zobrazí pouze při filtrování podle té
kategorii. Chcete-li tak učinit, přesuňte blok na nejvyšší nebo nejnižší část stránky, abyste jej zobrazili v seznamu
kategorie nebo do oblasti pod kategorii v horní části stránky, případně pod seznamem produktů.
Zobrazovat ho pouze při filtrování podle konkrétní kategorie.

.. obrázek: katalog/katalog-hlavička-patka.png
:alt: Umístěte blok v hlavičce nebo patě stránky.

..tip:
   - Přidávání obsahu na stránku kategorie v e-shopu pomáhá zlepšit SEO.
<../../webové stránky/stránky/SEO> strategii. Používá klíčová slova spojená s produkty nebo službami
Kategorie e-commerce mohou také zvýšit organický provoz. Kromě toho má každá kategorie své
vlastní specifickou URL, na kterou lze odkazovat a která je indexována vyhledávači.
   - Kategorie elektronického obchodu mohou být také přidány jako „velké položky menu“.
pro rychlý přístup.

.._ecommerce/katalog/doplňkové funkce:

Další funkce
===================

Můžete přistupovat k tlačítkům pro další funkce, jako je například „Přidat do košíku“ nebo
Tlačítko „Seznam přání“ nebo „Srovnávací seznam“. Otevřete editor webu
klikněte na požadované tlačítko. Všechna tři tlačítka se zobrazí při přejetí myší nad
obraz produktu.

- :icon:`fa-shopping-cart` (:guilabel:`Přidat do košíku“): přidá tlačítko
:doc:`přidat produkt do košíku <../checkout>`;
- :icon:`fa-exchange` (:guilabel:`Srovnání produktů“): přidává tlačítko pro porovnávání produktů na základě
jejich cena, varianta apod.
- :icon:`fa-heart-o` (:guilabel:`Souhlas se zpracováním osobních údajů“): přidává tlačítko do :ref:`seznamu přání
<e-commerce/produkty/seznamy přání> produktu.


.. viz též:
:doc:`Produkty <../products>`
