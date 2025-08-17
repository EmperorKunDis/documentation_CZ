=========================
Dashboard pro oceňování akcií
=========================

.. |Vrstvy hodnotících cen akcií| nahrazují: zkratka: `Vrstvy hodnotících cen akcií`

Když má společnost fyzické aktiva, jako je například zásoby, často chce vědět přibližně, jak
Mnoho peněz bylo vynaloženo na tyto zboží nebo jak je hodnotí aktuálně. Tento proces
Přiřazení peněžní hodnoty k zásobám se nazývá *hodnocení zásob*.

Tato hodnota je často uváděna pro účely účetnictví. Například pojišťovna může chtít
vědět o hodnotě zboží skladovaného v skladu, pokud dojde k povodni nebo požáru.

:doc:`Ocenění zásob <../../product_management/inventory_valuation/using_inventory_valuation>`
obvykle využívá jednu ze dvou účetních systémů:

- **Nepřetržitý**: Inventář je neustále aktualizován a hodnota
neustále se měnící.
- **Periodicky**: Hodnota zásob se kontroluje na periodické bázi a hodnota
je stanovena na tuto příležitostnou dobu.

Použití :ref:`sledovaného skladu <inventory/product_management/tracking-inventory> v Odoo
vyžaduje trvalý systém účetnictví skladových zásob, protože je nutné vědět kdy a kde
Zásoby existují, ale kolik z nich je k dispozici nebo se předpokládá. Existuje několik běžných :ref:`zásob
metody ocenění v Odoo: *standardní cena*.
průměrná cena (AVCO), a účetnictví „první vstup, první výstup“ (FIFO). Důležité je vědět, že
zvolený způsob ocenění produktu ovlivňuje výpočet několika položek v zásobách.
Ocenění.

Otevřete palubní desku
==================

Dashboard Stock Valuation společnosti Odoo zobrazuje finanční hodnotu všech skladovaných položek.
metodě ocenění zásob každého produktu. Tento report může poskytnout pohled na potenciální problémy v
dodavatelského řetězce, jako jsou například náklady na ztracené zakázky nebo prodlevy v dosažení ziskovosti.
Přejděte na: menu: „Skladová aplikace“ --> „Zprávy“ --> „Ocenění“.

.. důležité::
V nabídce **Inventář** je možné zvolit pouze položku „Hlášení“, která je dostupná pouze pro uživatele s
:doc:`správce <../../../obecné/uživatelé/práva>.

Tento panel má tři různé pohledy nebo zprávy o zásobách - viz:ref:`list view
<Inventář/Skladové zásoby/Hodnotící zpráva> (tj. výchozí hodnoticí zpráva o skladových zásobách)
:ref:`pivotový pohled <skladové zásoby / sklady a skladování / stárnutí zásob>“ (tj. zpráva o stárnutí zásob).
:ref:`grafický pohled <inventura/sklady_a_úložiště/graficky-pohled>“. Každý pohled lze přizpůsobit
různé pole pro rozdělení výpočtu hodnoty zásob podle produktu, typu operace, data nebo společnosti.

Všechny tři pohledy lze filtrovat různými poli. Filtry aplikujte kliknutím do vyhledávacího pole
nahoře na zprávě nebo kliknutím na šipku vedle ní. Například vybráním filtru
:guilabel:`Zbývající množství“ zobrazí pouze produkty, které jsou momentálně skladem.

… inventář/sklad/hodnotící zpráva:

Zobrazení v seznamu: Ocenění akcií
==========================

Výchozí zobrazení panelu „Ocenění akcií“ je v *list view* (viz obrázek), který je reprezentován
:ikonka „zobrazení seznamu“ :guilabel:„(seznam)“ ikona, která zobrazuje podrobný záznam pohybů skladových položek
a jejich hodnoty.

Nastavení
---------

Následující sloupce jsou zobrazeny výchozím nastavením:

- :guilabel:`Datum“: datum a čas, kdy došlo k :ref:`pohybu zásob <skladové zásoby/sklady/svl>“.
Vytvořil se nový sloupec, který je ve výchozím nastavení řazen podle hodnoty nemovitosti a tím zdůrazňuje její důležitost.
způsobu ocenění zásob. Chcete-li třídit zprávu podle jiného sloupce, jednoduše klikněte na
nadpis sloupce.
- :guilabel:`Referenční dokument`: referenční dokument spojený s tímto pohybem zásob (např. sklad).
faktura, dodací list, ruční inventarizační úprava).
- :label:Produkt“: produkt, který se přesouvá a hodnotí.
- :guilabel:`Množství“: počet jednotek, které bylo v zásobě tohoto produktu přidáno nebo
V tomto konkrétním pohybu ceny akcií klesla.
- :guilabel:`Celková hodnota“: hodnota zásob v tomto konkrétním pohybu zásob.
vypočítané vynásobením množství a jednotkové hodnoty.

.. poznámka::
Pokud je v dokladu Reference uvedeno více položek, bude každá z nich mít samostatný řádek.
Vygenerované na každém dokladu prodeje.

Pokud chcete získat další informace o zásobách, můžete přidat další pole do této oblasti.
hodnoty. Chcete-li přidat pole, klikněte na ikonu „Nastavení“ (adjust) a vyberte
požadované pole:

- :guilabel:Číslo šarže nebo sériové číslo: jedinečné označení šarže nebo sériového čísla tohoto produktu.
- :guilabel:Společnost: pro firmy, které pracují s více společnostmi, tento prvek zobrazuje
společnost, která tento pohyb akcií provedla.
- :guilabel:`Zbývající množství“: počet jednotek zbývajících pro tuto hodnotu produktu
po odečtení požadavku (i z jiných pohybů zásob). Toto pole může být zvláště
je užitečný pro účetnictví FIFO (První vstup, první výstup) a AVCO (Průměrná cena).
zaznamenává, které skladové jednotky byly do skladu dodány jako první a jaká je hodnota těchto jednotek.
- „Hodnota jednotky“: náklady na jednotku produktu pro společnost (ne cena pro zákazníka)
spotřebitelé).
- :guilabel:`Popis`: popis důvodu této ocenění akcie (obvykle je to cena akcie
Pokud se pohyb neprojeví (např. v případě, že je zadána nulová hodnota), pak výchozí hodnotou tohoto pole je koncatenace
:guilabel:`Zdroj reference“ a „Produkt“. V poli však může být také zobrazeno jiné
důležité zprávy pro tento řádek, například poznámka o tom, že řádek je úprava
z důvodu změny metody ocenění zásob.
- :guilabel:`Zbytkový stav“: hodnota aktuálního skladového zásobení tohoto produktu pro tuto konkrétní
skladovou pohyb, který se provádí poté, co byla zohledněna poptávka. Spolu s položkou „Zbytkový počet“
Tento pojem je zvláště užitečný pro FIFO (první vstup, první výstup).
:Abk. „AVCO (Průměrná cena)“ účetnictví, které ukazuje, jaké zboží bylo do skladu dodáno jako první.
hodnota uvedených akcií.

..tip:
Některé z těchto nastavení se nezobrazí, dokud je nejprve povolíte v aplikaci **Nastavení**.

.. obrázek: stárnutí / hodnotící zpráva o cenných papírech.
:alt:Zpráva o hodnotě akcií.

.. skladovací prostory/sklady/svl:

Vrstvy hodnocení cen akcií (SVL)
-----------------------------

Každá položka v zprávě „Ocenění zásob“ představuje záznam v systému Odoo známý
jako vrstva hodnoty akcií (SVL)*: Vrstvy pohybu akcií (SVL) vznikají, když se produkty
pohybovat se způsobem, který ovlivňuje jejich hodnotu akcií. Konkrétně pohyby na trhu, které vyvolávají
:zkratka „SVL“ (skladové pohyby) jsou sklady, dodávky, zásilky a
návrat k modelu dropshipping. Tyto pohyby zásob musí být nejprve schváleny (kliknutím na
tlačítko „Potvrdit“ (přesměruje na stránku s tímto tlačítkem).

Pokud se změní způsob ocenění zásob na kartě produktu, vytvoří se nové řádky.
v zprávě o hodnotě akcií, aby odrážely vzniklé „vrstvy pohybu akcií“ („SVLs“).
Příkladem je změna metody ocenění z „standardní ceny“ na buď „AVCO (průměrná cena)“.
Kost) nebo :abbr: FIFO (první vstup, první výstup) účetnictví, *přepočty* budou
automaticky zveřejněno, aby odráželo změnu cen na zboží, které je stále skladem.
bude negativní a „odstraní“ starou cenu. Druhá položka bude pozitivní a zaznamená novou
cenotvorba. Tyto záznamy jsou spojeny s účetními záznamy v aplikaci **Účetnictví** společnosti Odoo.

Níže je příklad, co ukáže tabulka „Ocenění akcií“, když se pohybují nějaké akcie.
Vznikla při použití standardního způsobu účtování cen.

.. obrázek: stárnutí/před změnou metody.png
:alt:Tabulka ocenění cenných papírů v účetnictví podle standardních cen.

Naopak následující obrázek ukazuje, jak by mohl vypadat výpis z tabulky „Hodnota akcií“.
po přechodu produktu z běžné ceny na účetní metodu FIFO (první vstup, první výstup).

.. obrázek: stárnutí/po změně metody.png
:alt:Tabulka ocenění zásob po přechodu z metody standardní ceny na metodu FIFO.

Příklad:
Hodnota pole „Zbývající hodnota“ a „Zbývající množství“ je odvozena z toho,
se vyskytují na úrovni :abbr:`SVL (vrstva pohybu zásob)“ v Odoo a jsou tak lépe chápány
To je příkladem.

Frankieho obchod s oblečením kupuje svetry za cenu nebo :guilabel:`Unit Value“ 5,00 $.
dolarů. Frankie nakupuje a prodává poprvé za 100 dolarů.
V jednom skladovém pohybu prodává svetry za 100 Kč, v druhém pak zase za -100 Kč.

V prvním řádku položky pohybu zásob se změní hodnota „Zbývající množství“ z 100,00
„90,00“, jakmile bude zaznamenán druhý pohyb ceny. Tato změna odráží skutečnost, že i když je 100
Původně zakoupené svetry jsou nyní v zásobě pouze 90 kusů a měly by být
se započítává do ocenění. Hodnota „zůstatku“ klesne z 500 na
„$ 450,00“. Celková hodnota zůstane na „$ 500,00“, bez ohledu na další změny
transakcí.

Na druhou stranu se v položce „zbývající množství“ zadává
jsou zaznamenány a setrvají na hodnotě „0.00“, protože bylo prodáno množství v hodnotě -10.00. V systému
pokud se jednalo o prodej, nezbývá žádné zboží k ocenění
z této transakce.

.... obrázek:: stárnutí/zůstávající hodnota kvant.png
:alt: Zbývající hodnota a množství se vypočítává na základě :abbr:`SML (vrstev skladových pohybů)“.

Datum ocenění
-------------------------

Chcete-li zobrazit hodnotu pohybu akcií v určitém datu a čase, klikněte na „Hodnota
Datum“ tlačítko v pravém horním rohu stránky „Ocenění akcií“. Zpráva
ukáže množství a celkovou hodnotu každého pohybu zásob.

.. poznámka::
Kvantita a hodnota zbývajících pohybů na skladě se nezmění.
být bodovým časem pro jakékoliv datum, které bylo v minulosti vybráno. Pohyby akcií zobrazené při výběru minulého data
Datum zobrazí stávající množství a hodnotu produktů.

Příklad:
Společnost má v únoru k dispozici 100 sedaček a prodá 20 z nich 1. února.
:guilabel:`Zbývající množství“ v vrstvě „Přesuny zásob“ se sníží z 100,00 na
„80,00“ k 1. únoru. Pokud by se nic dalšího nestalo a k 1. únoru zůstaly ceny stejné,
:guilabel:`Datum ocenění“ je vybráno jako 1. ledna a :guilabel:`Zbývající množství“
Výsledek bude stále zobrazovat jako „80,00“.

...Inventář, sklad, skladování, stáří:

Pohled na skladové zásoby
=======================

Z panelu „Ocenění akcií“ přejděte do pohledu na sloupcový graf kliknutím na
:ikonka „OI-VIEW-PIVOT“ :guilabel:„(pivota)“ ikona. Tento pohled je v podstatě „report o stárnutí zásob“,
Zobrazuje množství a hodnotu zásob podle data nákupu, což může pomoci při sledování
produkty s datem spotřeby.

Nastavení
---------

Výchozí pohled na rozdělení produktů podle dní a měsíců zobrazuje hodnotu všech kategorií. Kliknutím
Ikona „Plus“ v každé sloupci nebo řádku odhalí seznam.
seznam možností pro vytvoření podrobnějšího rozdělení hodnoty zásob.
možnosti zahrnují: „Produkt“, „Číslo šarže/sériového čísla“ a „Kategorie produktu“.
Kliknutím na „Datum“, „Společnost“ nebo „Vlastní skupina“
:icon:`fa-minus-square-o` :guilabel:`(minus)` ikona smaže pole zpět do prázdného stavu.

V tabulce je sloupec „Dostupné množství“, který zobrazuje počet položek skladem.
:guilabel:`Zbývající hodnota“ zobrazuje celkovou cenu nákupu těchto položek.

.. obrázek: stárnutí/stárnutí-zpráva.png
:alt:Zpráva o stárnutí zásob, která ukazuje produktové řádky a sloupce dnů.

...Inventář/Sklady/Zobrazení grafu:

Grafický pohled
==========

Hodnotu akcií lze graficky znázornit kliknutím na ikonku :icon:`fa-area-chart`.
:guilabel:`(graf)` ikonou. Výchozí graf je zobrazen v ikoně „:icon:`fa-line-chart`“
zobrazení a filtrování, které ukazuje celkovou hodnotu zásob v čase v Odoo.

V horní části zprávy je možné vybrat si mezi :icon:`fa-bar-chart` grafem sloupcovým nebo :icon:`fa-pie-chart` grafem koláčovým.
je možné zvolit místo něj.

.. viz také:
:doc:`Základy reportingu v Odoo <../../../../essentials/reporting>`
