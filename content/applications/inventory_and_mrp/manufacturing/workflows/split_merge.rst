====================================
Rozdělení a sloučení výrobních objednávek
====================================

V Odoo Manufacturing lze vytvářet výrobní objednávky na jednotku položky.
nebo více jednotek stejné položky. V některých případech může být nutné rozdělit výrobu
zboží v jedné objednávce rozdělit do více objednávek nebo sloučit dvě či více objednávek do jedné.
jednotlivý nákup.

.. důležité:
Výrobní objednávka může obsahovat pouze jednotku výrobku nebo více kusů stejného produktu.
produkt, který používá stejný seznam komponent (BOM). Výsledkem je, že lze spojit
výrobní objednávky, kdy každá objednávka obsahuje stejný produkt vyráběný stejným způsobem.
BoM.

Rozdělené výrobní objednávky
==========================

Chcete-li rozdělit výrobní objednávku na více objednávek, začněte tím, že se přesunete do
Vyberte možnost „Výroba“ -> „Operace“ -> „Objednávky výrobních procesů“, pak vyberte výrobní
objednávku. Na horní části stránky vedle tlačítka „New“ je uveden
referenční číslo se zobrazuje vedle tlačítka s ikonou „Nastavení“ .

Klikněte na tlačítko „Nastavení“ (označené symbolem ⚙️).
Poté vyberte možnost:guilabel:`Rozdělit“.

.. obrázek: split_merge/settings-split.png
:align:center
:alt:Tlačítka Nastavení a Rozdělit na výrobním příkazu.

Po výběru položky „Rozdělit“ se objeví okno s názvem „Výroba rozdělení“.
:guilabel:`Skládání #“ pole, zadejte počet výrobních objednávek, které má původní objednávka
je možné rozdělit na více částí, pak klikněte mimo pole. Pod polím se objeví tabulka s řádky pro každou novou
výrobní objednávku, která vznikne po rozdělení. V poli „Počet kusů“
sloupec, zadejte počet jednotek, které budou přiřazeny každému novému výrobnímu příkazu. Nakonec
Klikněte na tlačítko „Rozdělit“ a rozdělte výrobní objednávku.

.. obrázek: split_merge/split-production-window.png
:align:center
:alt:Okno pro výrobní objednávku v okně pop-upu pro produkci.

Po kliknutí na tlačítko „Rozdělit“ je původní výrobní objednávka rozdělena do počtu
položky, která byla uvedena v poli „Splátka číslo“. Nové referenční číslo
Výrobní objednávky jsou referenčním číslem původní objednávky s přidáním hvězdiček, lomítek a dalších znaků.
konec.

Příklad:
Objednávka výroby *WH/MO/00012* je rozdělena na tři samostatné objednávky.
nové objednávky jsou *WH/MO/00012-001*, *WH/MO/00012-002* a *WH/MO/00012-003*.

Spojit výrobní objednávky
==========================

Chcete-li sloučit dvě nebo více výrobních objednávek do jedné objednávky, začněte tím, že se přesunete na
:menuselection:Výroba --> Provoz --> Výrobní objednávky“. Zvolte výrobu.
objednávky, které se sloučí aktivací zaškrtávacího políčka vedle názvu každé objednávky.

.. obrázek: split_merge/select-orders.png
:align:center
:alt:Vyberte výrobní objednávky, které se mají sloučit zaškrtnutím políčka u každé z nich.

Jakmile jsou vybrány všechny výrobní objednávky, klikněte na tlačítko „Akce“ v horní části
stránku a poté vyberte možnost „Sloučit“ z nabídky.

.. obrázek: split_merge/actions-merge.png
:align:center
:alt:Tlačítka Akce a Sloučit na stránce výrobních objednávek.

Vybrané výrobní objednávky se sloučí do jedné objednávky. Nová objednávka bude mít stejný referenční kód jako původní objednávka.
Výrobní objednávka je následující sekvenční číslo, které *nebylo* dosud přiděleno žádné objednávce.

Příklad:
Poslední referenční číslo používané pro výrobní objednávku bylo *WH/MO/00012*. Dvě výrobní
objednávky, *WH/MO/00008* a *WH/MO/00009*, jsou sloučeny do jedné objednávky. Referenční číslo pro
výrobní objednávka vytvořená sloučením je *WH/MO/00013*.

V poli „Zdroj“ pro výrobní objednávku vytvořenou sloučením je odkaz
seznam zadaných objednávek na výrobu, které byly sloučeny.

Příklad:
Výrobní objednávky *WH/MO/00009* a *WH/MO/00010* jsou sloučeny do výrobní objednávky *WH/MO/00011*.
Zdrojové pole pro *WH/MO/00011* obsahuje jak *WH/MO/00009*, tak i *WH/MO/00010*.
