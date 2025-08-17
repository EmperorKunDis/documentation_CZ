====
Sady
====

V Odoo je kit typem výrobku (BOM), který se vyrábí a prodává.
součástky prodávané zákazníkům v nekompletním stavu. Mohou být prodávány jako samostatné produkty a jsou
Jsou také užitečnými nástroji pro správu složitějších výrobních listů.

.. poznámka::
Pro používání, výrobu a prodej sad, oběma moduly Manufacturing a Inventory
Aplikace je třeba nainstalovat.

Vytvořte sadu jako produkt
===========================

Aby bylo možné používat sadu jako prodejný produkt nebo jako organizační nástroj, musí být nejprve
Vytvořen jako produkt.

Chcete-li vytvořit produkt sestavy, přejděte na: „Nástroje pro správu inventáře --> Produkty --> Produkty“ a poté
Klikněte na „Nový“.

Poté přidejte jméno nového produktu do sady. Následně nastavte typ produktu podle skladových zásob
sledování potřeb a účetních požadavků. Pro tento účel je pod záložkou „Obecné informace“
zaškrtněte políčko vedle „Produktu“ a nastavte hodnotu „Zboží“.
:guilabel:`Sledování zásob“ pokud je sledování zásob vyžadováno nebo nechte pole prázdné, pokud není sledování zásob
sledování sady není nutné.

.. viz také:
Zjistěte více o :doc:`sledovaných a nesledovaných produktech
<../../sklad/správa produktů/konfigurovat/typ>.

Součásti sady musí být také nastaveny jako produkty v aplikaci Inventář:
Produkty ---> Produkty“. Tyto komponenty nevyžadují žádné specifické konfigurace.

Nastavení podrobností o neevidovaném vybavení
-------------------------------------

Zvažte, že byste nechali sledování stavu zásob pro kusy vybavení nepovinné, pokud se používá v jiných
výrobních procesů nebo pokud není potřeba sledovat zásoby pro samotný balíček.

* **Doporučeno pro kontinentální účetnictví**: Pokud jsou náklady okamžitě po koupi odepsány, pak
Je doporučeno nechat inventář sady nenavázaný na žádné položky.
* **Dodávky prostřednictvím komponentů**: Skladová evidence je řízena na úrovni komponent, takže objednávání
musí být nastaveny pro jednotlivé součásti.
* **Prodej a omezení zásob**: Sady nelze prodávat, pokud je některý z požadovaných komponentů vyprodán.
Protože dostupnost závisí na jednotlivých komponentech, objednávka může vypadat jako platná, ale dodání
Může se však prodloužit, pokud nejsou k dispozici komponenty.

Nastavení podrobností o sledovaném skladovém zásobování
-----------------------------------

Zvažte zapnutí sledování skladu pro případ, že se jedná o fyzický produkt nebo sklad
a sledování zásob je nezbytné.

* **Doporučeno pro účetnictví podle anglo-saského systému**: Pokud je třeba zaznamenat náklady na prodej
Pokud jsou vydávány časopisy, doporučuje se sledovat zásoby.
* **Omezení nákupu součástek**: Do košíku lze přidat pouze minimální počet komponentů, které jsou
**e-shopovou košík**, pokud není možnost „pokračovat“
Prodej je zakázán.
* *Není sledováno číslo sériového štítku*: Sledování sériových čísel nezaznamenává pouze balík, ale také jeho dodání.
komponenty.
* **Doporučení pro nastavení pořadí pravidel**: Pravidla by měla být nastavena na úrovni komponenty.
* **Doporučení pro doplnění zásob**: Doplňování zásob by mělo probíhat také
na úrovni komponenty.

Podobnost sestav
----------------------

Přestože se jedná o dvě různé možnosti, existují mezi nimi některá podobná zjištění.

* **Není možné provádět úpravy zásob na úrovni sady**: Zásoby nelze upravovat na úrovni sady.
* Hodnota portfolia se nemění: Hodnota portfolia je stejná, ať už sleduje nebo nesleduje sestavu.
* **Přesuny v rámci sady**: Přesun komponentů v rámci sady.

Sestavte sadu BoM
==================

Po úplném nastavení produktu sady a jeho komponent se vytvoří nový :abbr:`BoM (seznam materiálů)“.
Může být vytvořen pro produkt sady.

Pro toto vyberte v nabídce „Výroba“ -> „Produkty“ -> „Seznamy materiálů“.
Klikněte na „Nový“. V poli „Produkt“ klikněte na rozbalovací nabídku.
seznam produktů a poté vyberte již dříve nakonfigurovaný produkt sady.

Poté klikněte na možnost „Sada“ pro pole „Typ BoM“. Nakonec pod
Kartě „Součásti“, klikněte na „Přidat řádek“ a přidejte požadované součásti.
Specifikovat jejich množství v sloupci „Množství“.

Jakmile je hotovo, klikněte na tlačítko „Uložit“ a uložte si nový seznam materiálů.

.. obrázek: kit_shipping/bom-kit-selection.png
:alt:Výběr sestavy na výrobní list.

Pokud se sada prodává pouze jako prodejný produkt, pak je nutné přidat pouze komponenty.
kartě „Součástky“ a konfigurace výrobních operací není nutná.

.. poznámka::
Když se sada prodává jako produkt, objeví se na cenovém a prodejním dokladu jako jedna položka.
V případě objednávky však je uveden každý díl sady.

Použijte sady pro správu složitých BOMů
===============================

Sady lze použít i pro složitější :abbr:`BoMs (Bills of Materials)“. Tento způsob umožňuje vložit BoM do
další BoM, které usnadňují výrobu složitých produktů definováním požadavků na nákup.
a výrobní krok zvlášť.

Sublevel BoMs (podúrovně BoM nebo polotovary) zjednodušují tyto procesy a pomáhají s
snahy o sledovatelnost.

.. viz také:
:doc:`součásti“
