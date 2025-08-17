Zobrazit obsah

========
Produkty
========

Systém **Odoo eCommerce** vám umožňuje:
Vaše produktové stránky přímo z aplikace Webové stránky. Dále
umožňuje přidat varianty produktů:
:ref:`digitální soubory <ecommerce/produkty/digitální-soubory>“, :ref:`překlad
obsah stránky s produktem, správu zásob
<ecommerce/produkty/správa zásob>“ a „porovnávání produktů
<ecommerce/produkty/porovnání-produktů>“.

... ecommerce/produkty/přidat produkt:

Přidat produkty
============

.._ecommerce/produkty/vytvorit-produkt:

Vytvářet produkty
---------------

Pro vytvoření produktu z frontendu klikněte na tlačítko „+ Nový“ v pravém horním rohu, pak
:guilabel:`Produkt“. Zadejte :guilabel:`Název produktu“, :guilabel:`Prodejní cenu“ a výchozí
„Dodatečné daně zákazníků“ pro místní transakce a „Uložit“. Poté můžete aktualizovat
podrobnosti o produktu, přidat obrázek a nakonfigurovat produkt.
stránka. Když kliknete na tlačítko „Uložit“, produktová stránka se automaticky zveřejní.

..tip:
   - Můžete také vytvořit produkt z administrace, když přejdete na
:menu:„Webová stránka –> E-commerce –> Produkty“ a kliknutím na „Nový“.
   - Produkty vytvořené z přední části jsou automaticky publikovány.
Zatímco produkty vytvořené z backendu nejsou. Chcete-li produkt publikovat, klikněte na
:guilabel:`Přejít na webovou stránku“ chytrý tlačítko pro přístup k produktové stránce a poté přepněte přepínač
:guilabel:`Nezveřejněno“ na :guilabel:`Zveřejněno“.

.. viz též:
:doc:`Vytvořte nové produkty pomocí databáze čárových kódů


..._ecommerce/produkty/import-produktů:

Dovoz produktů
---------------

Do importu produktových dat lze použít soubory XLSX nebo CSV.
Přejděte na „Webové stránky -> E-commerce -> Produkty“ a klikněte na ikonu „fa-cog“.
Ikona „Nástroje“ (:guilabel:`gear`), pak „Dokumenty importovat“ (:ref:`<essentials/export_import_data/import-data>`).

..tip:
Pokud chcete vydat velké množství produktů, postupujte takto:

   #Přejděte na: Menu --> Webové stránky --> E-commerce --> Produkty.
   #Odeberte filtr „Zveřejněno“ a přepněte na zobrazení „Seznam“.
   #Klikněte na ikonu „fa-sliders“ („dropdown toggle“) a zapněte
:guilabel:`Je zveřejněno“.
   #Klikněte na sloupec „Zveřejněno“ a zobrazí se vám seznam podle stavu publikace, tj. buď „zveřejněno“ nebo „nepředstaveno“.
produkty.
   #Vyberte produkty, které chcete zveřejnit zaškrtnutím políčka u nich.
   #V sloupci „Je zveřejněno“ zaškrtněte políčko u vybraných produktů a
:guilabel:`Potvrdit“ a zveřejnit je.

..._ecommerce/produkty/detail-produktu:

Konfigurace produktové stránky
==========================

... e-commerce/produkty/přizpůsobení:

Informace o produktu
-------------------
.. ecommerce/produkty/produktní formulář:

Chcete-li přidat obecné informace o produktu, přejděte na:
e-commerce --> Produkty a vyberte produkt. Můžete si nastavit stránku produktu z formuláře
přidáním variant produktů (viz ecommerce/products/product-variants), digitálních dokumentů
<ecommerce/produkty/digitální soubory>“, nebo „překladu <ecommerce/produkty/překlad> obsahu“.

Můžete také přidat popis produktu specifický pro elektronické obchody, který se zobrazí pod tímto.
název produktu na stránce s produktem. Chcete-li tak učinit, přejděte na :guilabel:`Prodej`
Klikněte na záložku „Popis e-shopu“ a přidejte popis.
Editor s možnostmi úprav obsahu (viz:doc:`rich-text editor <../../essentials/html_editor>`)

..tip:
Klikněte na tlačítko „Přejít na web“ a vrátíte se na stránku produktu v přední části obchodu.

Prezentace produktu
--------------------

Pro přizpůsobení prezentace produktu na webových stránkách přejděte do sekce „Obchod“ a klikněte na
produktu. Klikněte na tlačítko „Upravit“ a upravte stránku podle vlastních preferencí.
:upravit své obrázky (<ecommerce/products/image-customization>) nebo přidat
:doc:`bloky <../../websites/website/web_design/bloky>“.

..tip:
   - Při přetahování a pádu bloku na stránce produktu, umístění jej nad nebo pod
přidává modré linky nahoře nebo dole, které jsou viditelné na všech stránkách produktu.
   - Můžete upravit jakýkoliv text na svých webových stránkách kliknutím na něj, když je ve stavu „Upravit“.

Přejděte na záložku „Nastavení“ a upravte uspořádání stránky nebo přidejte funkce:

- :guilabel:`Podmínky a pravidla“: Zapněte přepínač, aby se zobrazila odkaz na vaše
:dokument: „podmínky a podmínky“ na adrese
stránka produktu.

- :guilabel:`Zákazníci“:

   - :guilabel:`Hodnocení produktů“: Povolit přihlášeným uživatelům portálu přidávat recenze k produktům po kliknutí na
hvězdičky pod názvem produktu a sdílením svých zkušeností v sekci „Recenze zákazníků“.
na konci. Recenze jsou viditelné z produktové stránky pomocí ikonky „+“
ikona vedle nadpisu „Recenze zákazníků“ nebo z produktu
formulářového šumu. Chcete-li omezit viditelnost na interní zaměstnance, přepněte :guilabel:`Public`
přepínač vedle komentáře ke zprávě.
   - :guilabel:`Sdílet“: Přidejte tlačítka s ikonami sociálních médií a e-mailu, které zákazníkům umožní sdílení
produkt přes tyto kanály.

- :guilabel:`Vybrat množství“:Přepněte přepínač, aby zákazníci mohli vybrat počet produktů
chce koupit.

- :guilabel:`Daňová indikace“: Zapněte přepínač, pokud je cena
:ref:`S DPH nebo bez DPH <ecommerce-price-management-tax-display>.

- Zobrazit všechny možné varianty produktu: Zobrazit všechny možné varianty produktu
jako horizontální seznam produktů:
nebo vodorovně jako volitelné:guilabel:`Možnosti`, abyste si sestavili variantu sami.

- :guilabel:`Štítky produktů“: Zapněte přepínač, abyste zobrazili „Šablony štítků produktů“.
stránku produktu a umožnit zákazníkům filtrovat produkty pomocí těchto štítků.

- :guilabel:`Košík“:

   - :guilabel:`Koupit nyní“: Přidejte možnost „Koupit nyní“ se symbolem „fa-bolt“
stránka s pokladnou.
   - :guilabel:`Seznam přání“: Přidat možnost „Přidat do seznamu přání“ s ikonou „fa-heart-o“
zaregistrovaným zákazníkům ukládat produkty do seznamu přání.
   - :guilabel:`Srovnat“: Přidejte možnost „:icon:`fa-exchange` :guilabel:`Srovnat““, která zákazníkům umožní
to porovnat produkty podle jejich vlastností.

- :guilabel:`Specifikace“: Vyberte „Dolní část stránky“, abyste zobrazili podrobné seznamy
atributy a jejich hodnoty dostupné pro produkt. Tato možnost funguje pouze u produktů s
:ref:`varianty <ecommerce/produkty/produktové varianty>` pokud je
:ref:`Nástroj pro porovnávání produktů <ecommerce/products/product-comparison>` je v webu
:guilabel:`Nastavení“.

.. poznámka::
   - :guilabel:`Varianty“, :icon:`fa-heart-o“ :guilabel:"Seznam přání" a :icon:`fa-exchange
:guilabel:`Srovnat“ možnosti musí být zapnuty přechodem na
:menu_selektor:„Webová stránka -> Konfigurace -> Nastavení“, v sekci :gui_label:„Obchod – Produkty“
části.
   - Povolené funkce se vztahují na všechny produktové stránky.
   - Produkty s jedinou hodnotou pro jejich atributy negenerují varianty, ale stále
zobrazeny v části „Specifikace produktu“.

.. ecommerce/produkty/vlastní obrázek:

Obrázky a videa produktů
-------------------------

Chcete-li přidat další mediální položky, jako jsou například obrázky a videa, přejděte na
Pak přejděte na záložku „Prodej“
a klikněte na „Přidat média“ pod záložkou „Média pro e-shop“.
Pop-up okno „Vyberte médium“ otevřete, přejděte na záložku „Obrázky“, vyberte obrázek.
Klikněte na „Nahrát obrázek“ nebo „Přidat URL“. Nebo přejděte do záložky „Video“,
vložte odkaz na video nebo vložte kód pro vložení. Jakmile je hotovo, klikněte na tlačítko „Přidat“.

Pro přizpůsobení obrázků nebo videí navštivte stránku produktu v e-shopu a klikněte na tlačítko „Upravit“.
a vyberte vhodná média. V záložce „Upravit“ použijte následující funkce:

- :guilabel:`Šířka obrázků produktu“: Změní šířku zobrazených obrázků produktů na stránce.
- :guilabel:`Vzhled“: Layout „Kroužek“ umožňuje zákazníkům přecházet z jednoho obrázku na
další pomocí :icon:`fa-angle-left` (:guilabel:`left arrow“) nebo :icon:`fa-angle-right
[:guilabel:'pravý trojúhelník'; zatímco :guilabel:'Síť' zobrazuje čtyři obrázky v čtvercovém uspořádání.
- :guilabel:`Zvětšení obrázku“: Vyberte zvětšovací efekt pro produktové obrázky: „Zvětšení při přejetí myší“

- :guilabel:`Náhledy“: Zajistit, aby náhledy byly na :icon:`fa-long-arrow-left“ (:guilabel:`Levé“)
nebo
:icon:`fa-long-arrow-down` (:guilabel:`Dolů“).
- :guilabel:`Hlavní obrázek“: Klikněte na „Vyměnit“, abyste změnili hlavní obrázek produktu.
- :guilabel:`Další obrázky“: „Přidat“ další obrázky nebo videa (včetně odkazů)
:guilabel:`Smazat vše“.

.. poznámka::
Obrázky musí být ve formátu PNG nebo JPG s minimální velikostí 1024 x 1024, aby se spustil zoom.

.._ecommerce/produkty/produktové bloky:

Zablokované produkty
==============

Konstrukční prvek „Produkty“ je použit v rámci
zobrazit výběr produktů prodávaných na vašem webu.

.. obrázek: produkty/produkty-blok.png
:alt:Příklad bloku produktů

Výchozí blok zobrazuje nejnovější produkty. Chcete-li změnit, které produkty jsou zobrazovány,
Přejděte do sekce „Produkty“ v záložce „Nastavení“ a nastavte filtr.
pole pro: „Něco koupeného“ nebo „Něco zobrazeného“.

Dále je možné zobrazit pouze produkty ze specifické kategorie.
:guilabel: pole „Kategorie“.

Můžete také filtrovat produkty podle štítků, zahrnout varianty a upravit
zobrazení vyberte jiný štítek:guilabel: Template.

.._ecommerce/produkty/varianty-produktu:

Varianty produktů
================

:doc:`Varianty produktů <../../sales/sales/products_prices/products/variants>` jsou různé verze
stejného produktu, jako jsou například různé barvy nebo materiály s potenciálně odlišnou cenou a
Dostupnost.

Pro konfiguraci variant produktu:

#Přejděte na: menu: „Webová stránka“ --> „Konfigurace“ --> „Nastavení“.
#. V sekci „Obchod – Produkty“ klikněte na tlačítko „Zapnout“.
:guilabel:`Varianty produktů“ funkce.
#Přejděte na stránku s produkty a vyberte si z nabídky.
:guilabel:`Atributy a varianty“ kartě, kde můžete přidat atributy a hodnoty, které umožňují
zákazníky k konfiguraci a výběru variant produktů na stránce s produkty. Pro vícero atributů
Můžete je kombinovat, abyste vytvořili specifické varianty.

Zobrazit nebo skrýt atribut na stránce Shop a umožnit návštěvníkům filtrovat je.
Přejděte na: menu: „Webová stránka“ - „E-commerce“ - „Atributy“, klikněte na atribut a vyberte
„Zobrazené“ nebo „Skryté“ v poli „Filtr e-commerce viditelnosti“.

..tip:
   - Zobrazit atributy produktu v katalogu produktů:
nastavte funkci „Atributy“ na „Levé“ pomocí webového editoru.
   - Skupit atributy pod stejnou sekcí, když
:ref:`srovnání produktů <ecommerce/produkty/porovnavani-produktu>` nebo přejděte na
:guilabel:`Kategorie e-commerce“ pole a buď vyberte existující kategorii nebo vytvořte novou.
nové stránky <../../websites/ecommerce/products>.

.. poznámka::
Pro zobrazení filtru je potřeba dvou hodnot atributů.

.. viz též:
:doc:`Varianty produktů <../sales/sales/products_prices/products/variants>`

.. _ecommerce/produkty/digitální soubory:

Digitální soubory
=============

Můžete propojit digitální soubory typu certifikátů, e-knih nebo uživatelských návodů s produkty.
dokumenty jsou k dispozici:ref:`před zaplacením <ecommerce-products-digital-files-before-payment>
na stránce produktu nebo v zákaznickém portálu
:ref:`po zaplacení <ecommerce-products-digital-files-after-payment>“.

Chcete-li propojit digitální soubor s produktem, přejděte na formulář „Produkty“ (<ecommerce/products/product-form>).
a klikněte na tlačítko „Dokumenty“. Pak klikněte na „Nahrát“
nebo klikněte na možnost „Nový“ nebo „Nahrát soubor“.

..tip:
   - Místo digitálního souboru můžete odkazovat na URL adresu. K tomu stačí kliknout na tlačítko „Nový“, přejít do
pole „Typ“ a vyberte možnost „URL“.
   - Pro editaci stávajícího souboru klikněte na ikonu „fa-ellipsis-v“ („záložka“) v
v pravém horním rohu karty dokumentu a klikněte na tlačítko „Upravit“.

.. _ecommerce-products-digital-files-before-payment:

Digitální soubory k dispozici před zaplacením
--------------------------------------

Pro zobrazení souboru na stránce produktu (před zaplacením) nechte nastavenou možnost „Zobrazit“.
položku pole zanechat prázdnou a přepnout přepínač „Zobrazit na stránce produktu“.

.. obrázek: produkty/digitální soubory.png
:alt: digitální soubor je k dispozici před zaplacením na stránce produktu

... ecommerce-products-digital-files-after-payment:

Digitální soubory k dispozici po zaplacení
-------------------------------------

Pro zveřejnění souboru (po zaplacení) nastavte pole „Zobrazit“ na
Zapněte „Potvrzená objednávka“ a vypněte přepínač „Zobrazit na stránce produktu“.

.._e-commerce/produkty/překlad:

Překlad
===========

Pokud máte na svých stránkách více jazyků, můžete přeložit informace o produktu
přímo na formuláři produktu (viz ecommerce/products/product-form).
Jazyk je označen zkratkou jazyka (např. EN) vedle pole.

V oblasti e-commerce je třeba překládat tyto položky:

- :guilabel:`Název produktu“.
- „Nedostupné zboží“ (pod záložkou „Prodej“).
- „Popis prodeje“ (pod záložkou „Prodej“).

.. poznámka::
   - Nepřeložený obsah na stránce může být pro uživatele nepříjemný.
:doc:`SEO <../websites/website/pages/seo>“. Můžete použít
:doc:`Přeložit funkci <../website/configuration/translate> pro překlad obsahu stránky.“
   - Pro zkontrolování jazyka webu přejděte na: „Webová stránka -> Konfigurace ->
Přejděte do sekce „Nastavení“ a v seznamu vyberte možnost „Informace o webu“.

... ecommerce/produkty/dostupnost webu:

Dostupnost webu
--------------------

Pro nastavení dostupnosti produktu na webové stránce přejděte do formuláře s produktem.
<ecommerce/products/product-form>`, přejděte na záložku „Prodej“ a v
V sekci „E-shop“ vyberte webovou stránku, na které chcete produkt nabízet.
k dispozici na. Nechte pole prázdné, pokud chcete produkt nabízet na všech webech.

.. poznámka::
Můžete produkt nabídnout na jednom nebo všech webových stránkách, ale vybrat pouze
Není možné zablokovat všechny weby.

.. ecommerce/produkty/skladové hospodářství:

Správa zásob
================

Pro povolení a konfiguraci možností správy zásobníků přejděte na:
Konfigurace --> Nastavení“, posuňte se dolů do části „Obchod – Zboží“ a
podsekci „Výchozí nastavení inventáře“.

.. důležité:
   - Aplikaci Inventář musíte nainstalovat, abyste viděli možnosti správy zásob.
   - Pro zobrazení zásob na stránce produktu musí být nastaveno pole „Typ produktu“.
do pole „Skladovatelné“ v sekci „Produkt“ v části „Formulář produktu“ (viz ecommerce/products/product-form).

Inventarizace
---------

V podsekci „Výchozí nastavení inventáře“ vyplňte tyto pole:

- :doc:`Sklad <../../inventory_and_mrp/inventory/warehouses_storage/inventory_management/warehouses>“.
- :guilabel:`Nedostupné zboží“: Zapněte „Pokračovat v prodeji“, aby zákazníci mohli objednávat
I když je produkt vyprodaný, nezapomeňte zaškrtnout políčko „Nedostupné“.
- :guilabel:`Zobrazit dostupné množství pod určitou hranicí“: Zobrazuje dostupné množství pod určitou hranicí
na stránce produktu. K dispozici je počet kusů, který se vypočítá podle skladových zásob :guilabel:`Na skladě`.
množství odečíst od množství již vyhrazeného pro převody do zahraničí.

.. ecommerce/produkty/srovnání-produktů:

Srovnání produktů
==================

Chcete-li návštěvníkům webu umožnit porovnání produktů podle jejich vlastností, přejděte na
V nabídce „Webová stránka“ -> „Konfigurace“ -> „Nastavení“, posunout se dolů na
:guilabel:`Obchod – Produkty“ a zapnout „Nástroj pro porovnávání produktů“.

Ikona „Výměna“ (:guilabel:"Srovnání") je nyní dostupná na každé kartě produktu v hlavním
Stránku s obchodem se zákazníci dostanou, když na ni myší přejezdí. Chcete-li porovnat produkty, stačí kliknout na
Možnost „Srovnání“ (ikona: „Výměna“) u produktů, které chcete porovnat, a poté klikněte
Klikněte na tlačítko „Srovnání“ v dolní části stránky.
Shrnutí srovnání.

.. obrázek: produkty/produkty-porovnat.png
:alt: Okno s porovnáním produktů

.. poznámka::
   - Nástroj pro porovnání produktů je k dispozici pouze u produktů s
:ref:`atributy <ecommerce/products/product-variants>`.
   - Vybrat možnost „Srovnání“ (zobrazení ikony „fa-exchange“) z produktové stránky je také
Možná.

.. e-commerce/produkty/seznam přání:

Seznam přání
=========

Tlačítko s ikonou „srdce“ a štítkem „Přidat do seznamu přání“ umožňuje zákazníkům přidávat produkty
do seznamu přání, tedy si je nechat na později. Chcete-li toto nastavit, přejděte do nabídky :menuselection:`Website -->
Konfigurace --> Nastavení“, posuňte se dolů do části „Obchod – Produkty“ a zapněte
:guilabel:`Seznam přání“. Tlačítko je k dispozici na každé stránce produktu a lze jej vypnout v
pokud je třeba, viz webový editor <ecommerce/produkty/stránka produktu>.

.. obrázek: produkty/produkty-přidat-do-seznamu-přeje.png
:alt:Přidat do seznamu přání

..tip:
   - Můžete také zobrazit tlačítko s ikonou „srdce“ („Seznam přání“) při najetí myší
v sekci „Další funkce“ na stránce obchodu.
   - Zákazníci mohou přesunout produkty z košíku na seznam přání kliknutím na tlačítko „Uložit
tlačítko „Uložit pro pozdější použití“ v kroku objednávky ve :guilabel:`Přehledu objednávky
<ecommerce/checkout/review_order>`.

.. toctree::


produkty/katalog
produkty/cenová politika
produkty/prodloužení
