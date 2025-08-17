================
Varianty produktů
================

Varianty produktů se používají k tomu, aby jednotlivým produktům byly přiděleny různé vlastnosti a možnosti.
Jedná se například o velikost, styl nebo barvu.

Varianty produktů lze spravovat pomocí jejich vlastního šablony produktu nebo přes procházení do buď
stránce „Varianty produktů“ nebo „Atributy“. Všechny tyto možnosti jsou umístěny
v aplikaci pro obchod Odoo *.

Příklad:
Módní společnost má následující rozložení variant pro jedno ze svých nejprodávanějších triček:

   - Unisex klasický tričko

     - Barva: modrá, červená, bílá, černá
     - Velikost: S, M, L, XL, XXL

Zde je tričko produktový šablona, konkrétní produkt pak bude vypadat takhle:
varianta.

**Barva** a **Velikost** jsou atributy, a odpovídající možnosti (**Modrá** a **S**)
Jsou to hodnoty.

V tomto případě je celkem dvacet různých variant produktu: čtyři možnosti barev.
a pět různých velikostí. Každá varianta má své vlastní zásoby, prodejní celky a
podobné záznamy v Odoo.

.. viz též:
:ref:`E-commerce/produkty/varianty produktů`

Konfigurace
=============

Pro používání variant produktů musí být v Odoo Sales nastavení *Varianty* aktivní.
aplikace.

Pro toto nastavení přejděte na: „Aplikace pro prodejní činnost --> Konfigurace --> Nastavení“ a najděte
:guilabel:`Katalog produktů“ v horní části stránky.

V této sekci zaškrtněte políčko pro zapnutí funkce Varianty.

.. obrázek: varianty/aktivace-variant-nastaveni.png
:align:center
:alt:Aktivace variant produktů na stránce nastavení aplikace Odoo Sales.

Poté klikněte na tlačítko „Uložit“ v horní části stránky „Nastavení“.

Atributy
==========

Před nastavením variant produktu musí být vytvořeny atributy. Chcete-li vytvářet, spravovat a měnit
atributy, přejděte na: „Prodejní aplikace“ -> „Konfigurace“ -> „Atributy“.

.. poznámka::
Řazení atributů na stránce „Atributy“ určuje, jak se zobrazují.
*Konfigurátor produktů*, *Dashboard prodejního místa* a stránky *E-commerce*.

Pro vytvoření nového atributu z stránky „Atributy“ klikněte na „Nový“.
zobrazí prázdný formulář atributů, který lze upravit a nakonfigurovat různými způsoby.

.. obrázek: varianty/vytvoreni_atributu.png
:align:center
:alt:Vytvoření prázdného atributu v aplikaci prodeje Odoo.

Nejprve vytvořte atribut jména, například „Barva“ nebo „Velikost“.

Dále vyberte jednu z možností ze seznamu v poli „Typ zobrazení“. Vyberte „Zobrazit
Typ určuje, jak se tento produkt zobrazuje v online obchodě, na panelu prodejních míst a
*Konfigurátor produktů*.

Možnosti zobrazení jsou:

- :guilabel:„Pilulky“: možnosti se zobrazují jako volitelné tlačítka na stránce produktu v internetovém obchodě.
- :guilabel:Barva: možnosti se zobrazují jako malé barevné čtverce, které odráží jakékoliv barvy v HTML kódech
- :guilabel:`Rádio“: možnosti se zobrazují v seznamu bodů na stránce produktu internetového obchodu.
- Vyberte možnost z nabídky v seznamu na stránce produktu e-shopu.
v rámci produktové stránky e-shopu.
- :guilabel:`Vícezámeček (volba)`: možnosti se zobrazují jako vybrané zaškrtávací políčka na stránce produktu
z internetového obchodu.

.. obrázek: varianty/zobrazovací typy.png
:align:center
:alt:Zobrazení typů produktu na konfigurátoru v e-shopu v Odoo.

Pole :guilabel:`Automatické vytváření varianty“ informuje Odoo, kdy má automaticky vytvořit novou variantu.
Jednou, když je atribut přidán k produktu.

.. poznámka::
V poli „Způsob vytváření variant“ **musí být nastaveno na hodnotu** „Nikdy (volba)“.
pro správnou funkci :guilabel:`Vícezáložkový checkbox (volba)` jako :guilabel:`Zobrazení
Typ.

- :guilabel:'Okamžitě': vytváří všechny možné varianty ihned po přidání atributů a hodnot
do šablony produktu.
- :guilabel:Dynamicky: vytváří varianty pouze tehdy, pokud odpovídají atributy a hodnoty
přidána do objednávky na prodej.
- :guilabel:`Nikdy (volitelné)`: Never automaticky vytváří varianty.

.. varování:
Jakmile je atribut přidán do produktu, nelze jej v jeho nastavení upravit.

Záložka „Filtr e-commerce“ určuje, zda se tyto možnosti atributu
jsou viditelné zákazníkovi na prodejní ploše, když nakupuje v e-shopu.

- :guilabel:`Zobrazitelné“: hodnoty atributů jsou viditelné pro zákazníky na webové stránce.
- :guilabel:`Skrytý“: hodnoty atributů jsou skryty před zákazníky na straně uživatelského rozhraní.

V poslední řadě v poli volitelném :guilabel:`eCommerce Category` vyberte kategorii z nabídky.
menu, které seskupuje podobné atributy do jednoho oddílu pro zvýšení specifičnosti a organizace.

.. poznámka::
Chcete-li zobrazit podrobnosti o atributu kategorie vybrané, klikněte na interní odkaz
:icon:`fa-arrow-right` :guilabel:`(pravý směr)` ikonu v pravém dolním rohu
:guilabel:`Kategorie e-commerce` pole, jakmile si vyberete možnost. To odhalí, že
podrobné informace o kategorii.

...... obrázek: varianty/atribut-kategorie-interní-odkaz.png
:synchronizace: střed
:alt: Standardní stránka kategorie s podrobnostmi, přístupná prostřednictvím interního odkazového ikony šipky.

V horní části je zobrazeno pole „Kategorie“ a „Pořadí“.
:guilabel:`Související atributy“ spojené s kategorií. Tyto atributy mohou být
přetaženy a vloženy do požadovaného pořadí důležitosti.

Atributy lze přidat přímo do kategorie také pomocí tlačítka „Přidat řádek“.

..tip:
Chcete-li vytvořit novou kategorii atributů přímo z tohoto pole, začněte psát název nové
kategorii, pak vyberte buď „Vytvořit“ nebo „Vytvořit a upravit…“.
zobrazí se nabídka.

Kliknutím na tlačítko „Vytvořit“ vytvoříte kategorii, kterou lze později upravit.
:guilabel:`Vytvořit a upravit...“ vytváří kategorii a odhaluje :guilabel:`Vytvoření kategorie“.
pop-up okno, ve kterém lze novou kategorii atributů nakonfigurovat a přizpůsobit.

Hodnoty atributů
----------------

Hodnoty atributů se přidávají do záložky „Hodnoty atributu“. Hodnoty lze přidat k
přidělovat kdykoliv, pokud je třeba.

Chcete-li přidat hodnotu, klikněte na tlačítko „Přidat řádek“ v záložce „Hodnoty atributů“.

Poté zadejte název hodnoty do sloupce „Hodnota“ a zaškrtněte políčko v
Sloupec „Vlastní hodnota“, pokud je hodnota vlastní (tj. zákazník má možnost zadat unikátní
specifické pro tuto hodnotu)

Barvy
~~~~~~

Pokračujte v nastavení a vyberte možnost „Barva“.
Karta „Hodnoty atributů“ k upravení nastavení hodnot.

.. obrázek: varianty/atribut-hodnota-přidat-obrázek.png
:alt:Přidejte obrázek vzoru do atributu.

Chcete-li vybrat barvu, klikněte na prázdný kruh v sloupci „Barva“, který odhalí HTML
okno s výběrem barvy.

.. obrázek: varianty/vybírání barvy.png
:alt: Vybrání barvy z okna s výběrem barev HTML, které se objeví při vytváření atributu.

V tomto okně můžete vybrat konkrétní barvu táhnutím posuvníku barev.
a kliknutím na barevný pruh přímo v okně barevného gradientu.

Nebo si vyberte konkrétní barvu kliknutím na ikonu *kapička*, kde zvolíte požadovanou barvu.
aktuálně klikatelné na obrazovce.

Pokud prodáváte produkty s konkrétními vzory, můžete také přidat obrázek, který zobrazuje
vzor produktu. Klikněte na ikonku :icon:`fa-camera` :guilabel:`(kamera)`
Klikněte na ikonu „Penál“ (papír a tužka) a vyberte obrázek z vašeho počítače.
dopravu. Tento vzor se objeví jako barevná možnost na stránce produktu e-shopu.

.. obrázek: varianty/obchodní vzor-možnost.png
:alt: Vzorek jako barevná volba na stránce s elektronickým obchodem.

..tip:
Atributy lze také vytvářet přímo z produktového šablony přidáním nové řádky.
zadáním názvu do záložky Varianty.

Jakmile je atribut přidán k produktu, tak se tento produkt zobrazí a bude dostupný prostřednictvím atributu.
tlačítko „Související produkty“, které zobrazuje každý produkt v databázi.
s tímto atributem.

Varianty produktů
================

Jakmile je vlastnost vytvořena, použijte ji (a její hodnoty) k vytvoření varianty produktu.
Přejděte na: menu-selection: Sales App --> Products --> Products a vyberte existující produkt.
pohled na požadovaný produkt. Nebo klikněte na tlačítko „Vytvořit“ pro vytvoření nového produktu, ke kterému lze přidat
Může být přidán produktový typ.

Na kartě produktu klikněte na záložku „Attributy a varianty“ pro zobrazení, správu a úpravu
atributy a hodnoty produktu.

.. obrázek: varianty/atributy-hodnoty-karta.png
:align:center
:alt:Karta atributů a hodnot v běžném prodejním formuláři v Odoo Sales.

Chcete-li přidat atribut produktu a následně hodnoty atributů, klikněte na tlačítko „Přidat řádek“ v
kartě „Atributy & varianty“. Pak vyberte požadovaný atribut z roletky
menu, které se objeví.

..tip:
Atributy lze vytvářet přímo z karty „Atributy & varianty“ produktu.
formulář. Pro zadání nové vlastnosti začněte psát její název do prázdného pole a vyberte
nebo buď „Vytvořit“ nebo „Vytvořit a upravit…“ z malého nabídovacího menu.
Vyskytuje se.

Kliknutím na tlačítko „Vytvořit“ vytvoříte atribut, který lze později upravit.
:guilabel:`Vytvořit a upravit...“ vytváří atribut a :guilabel:`Vytvoření atributu“ okno.
V okně se zobrazí formulář. V tomto formuláři můžete upravit atribut v několika způsobech.

Jakmile si vyberete atribut v sloupci „Atribut“, pokračujte výběrem konkrétního
přidat hodnoty atributů k produktu prostřednictvím seznamového pole dostupného v položce :guilabel:`Hodnoty
sloupce.

.. poznámka::
Počet hodnot, které můžete přidat, není omezen.

..tip:
Podobný proces vytváření variant produktu je dostupný přes nákup, sklad a
e-commerce aplikace.

Nastavte varianty
------------------

Vpravo od atributové čáry je tlačítko „Nastavit“. Když na něj kliknete, Odoo zobrazí
samostatná stránka, která zobrazuje konkrétní hodnoty variant produktů.

.. obrázek: varianty/produkt-variant-hodnota.png
:align:center
:alt:Stránka s hodnotami variant produktu, kterou lze přistupovat pomocí tlačítka Konfigurovat na formuláři produktu.

Zde je konkrétní název hodnoty „Value“, „HTML Color Index“ (pokud se vztahuje) a
Viditelné jsou také hodnoty „Cena s DPH“, „Cena bez DPH“ a „Cena extra“.

.. poznámka::
Hodnota ceny „Value Price Extra“ představuje zvýšení prodejní ceny, pokud je atribut
vybrána.

Když je na stránce „Varianty produktu“ kliknutá hodnota, Odoo zobrazí samostatnou
stránka s podrobnostmi o hodnotě.

.. obrázek: varianty/produkt-variant-hodnota-stránka.png
:align:center
:alt: Stránka s hodnotami variant produktů přístupná z obecné stránky Hodnoty variant produktů.

Na stránce s podrobnostmi o konkrétním produktu se zobrazí hodnota „GuideLabel“ a „GuideLabelPriceExtra“.
našly by se i pole „Vyloučit pro“ a „Zahrnout“.

V poli „Vyloučit pro“ je možné vybrat různé „Šablony produktu“ a konkrétní
Můžete přidat hodnoty atributu. Když je přidáte, konkrétní hodnota tohoto atributu bude
Vyloučena z těchto konkrétních výrobků.

Varianty tlačítka Smart Button
---------------------

Pokud má produkt v záložce „Attributy & varianty“ nakonfigurované atributy a varianty,
V horní části formuláře produktu se objeví tlačítko „Varianty“.
Chytrý tlačítko ukazuje, kolik variant je pro daný konkrétní produkt nyní nastaveno.

.. obrázek: varianty/varianty-chytra-tlacitka.png
:align:center
:alt:Varianta tlačítka Smart Button v hlavní části produktové karty v Odoo Sales.

Když je kliknut na tlačítko „Varianty“, Odoo zobrazí samostatnou stránku s přehledem všech
konkrétní kombinace produktů, které jsou pro daný konkrétní produkt nakonfigurované.

.. obrázek: varianty/varianty-stránka.png
:align:center
:alt:Stránka s variantami, kterou lze přistupovat pomocí chytrého tlačítka „Varianty“ na produktovém formuláři v Odoo.

Dopad variant
==================

Kromě nabídky zákazníkům více podrobností o produktu mají varianty vlastní
impaktů, které lze využít po celé databázi Odoo.

- :guilabel:Čárový kód: čárové kódy jsou spojeny s každou variantou místo šablony produktu.
Každá jednotlivá varianta může mít své vlastní unikátní číslo SKU.
- :guilabel:`Cena“: Každá varianta produktu má svou vlastní veřejnou cenu, která je součtem
cena produktového šablony a případně další poplatky za konkrétní vlastnosti.

...... příklad::
Cena trička v červené barvě je 23 dolarů - protože šablona trička stojí 20 dolarů a navíc dalších tři.
3 dolary za červenou variantu. Cenový seznam lze nastavit tak, aby se vztahoval na šablonu produktu
nebo k variantě.

- :guilabel:Skladové zásoby: skladová zásoba se počítá pro každou jednotlivou variantu produktu.
šablonového formuláře, v soupisu odráží celkovou hodnotu všech variant, ale skutečný seznam
vypočítané pro jednotlivé varianty.
- :guilabel:`Obrázek`: každá varianta produktu může mít svůj vlastní specifický obrázek.

.. poznámka::
Změny v šabloně produktu se automaticky aplikují na každou variantu daného produktu.

.. viz též:
:doc:`importovat`
