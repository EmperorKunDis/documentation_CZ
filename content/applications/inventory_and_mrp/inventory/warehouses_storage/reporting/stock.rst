============
Report o stavu zásob
============

Pro podrobný seznam všech skladovaných produktů použijte v Odoo zprávu o zásobách *Sklad*.
v rezervách, zakoupených a v přepravě, stejně jako ty dodané zákazníkům.

.. poznámka::
Přístup k této funkci mají pouze uživatelé s :doc:`admin přístupem
<../../../obecne/uzivatele/pristupova-prava>.

Chcete-li zobrazit výkaz skladu, přejděte na: „Aplikace Sklad --> Zprávy --> Sklad“.

.. obrázek:: stock/stock-report.png
:align:center
:alt:Zobrazit zprávu o zásobách, kterou lze získat přes Inventář > Zprávy > Sklad.

Procházejte zprávou o stavu zásob
=========================

Ve sloupci v levém postranním panelu jsou několik skupin, které umožňují zúžit zobrazené informace.
Výchozí skupiny jsou:guilabel:`Sklady`, které filtrují produkty podle konkrétních skladů.
a :guilabel:`Kategorie produktů“, která zobrazuje produkty v dané kategorii.

.. poznámka::
Skupina „Sklad“ je dostupná pouze v případě, že máte více skladů.
databáze. Podrobnosti naleznete v dokumentaci k tématu „Skladování“ na adrese „../inventory_management/warehouses“.

V samotném reportu pak sloupce představují:

- :guilabel:`Produkt“: název produktu.
- :guilabel:`Náklady na jednotku“: průměrná hodnota zásob vynásobená počtem jednotek, upravená podle nákladů
výrobu a případně i nákup produktu.
- :guilabel:`Celková hodnota“: Celková hodnota produktu vypočítaná násobením jednotkové ceny.
cena podle množství skladem.

......viz také:
     - :ref:`Spočítat průměrnou cenu skladového zásobení na jednotku <inventory/avg_cost/formula>`
     - Metody ocenění zásob


- :guilabel:`Na skladě“: aktuální množství produktů. Klikněte na ikonku „fa-pencil“
:guilabel:`(tužka)` ikona pro :doc:`změnu skladových zásob

- :guilabel:`Volné k použití“: Množství, které je **nevyhrazeno pro dodání nebo výrobu**
objednávky a jsou k dispozici pro prodej nebo použití.
- :guilabel:`Příchozí“: očekávané položky, které se mají dostat na sklad. Počet produktů je založený
množství v potvrzených objednávkách.
- :guilabel:`Odejít“: položky, které se očekává, že opustí sklad nebo budou spotřebovány při výrobě
objednávek. Počet produktů je založen na množství v potvrzených prodejních nebo výrobních objednávkách.

Klikněte na tlačítka vedle položek v každé řádce, abyste získali další informace:

- :guilabel:`Historie“: zobrazte historii pohybu skladových zásob produktu a zobrazte informace o
množství a popis důvodu, proč byl produkt přemístěn z jednoho místa na druhé.
- :guilabel:`Dodání zboží“: přístup k pravidlům „dodávky
stránce „Způsoby doplňování“ (<../replenishment/reordering_rules>), kde můžete vytvářet nebo spravovat metody nákupu
produktu.
- :guilabel:`Místa skladování“: rozklad zásob na více skladech.
Je k dispozici, když je produkt skladován na více místech.
- :guilabel:`Předpověď“: zobrazte si předpovědní hlášení o stavu zásob, příchozích a odchozích
množství. Zpráva také obsahuje odkazy na potvrzené objednávky nákupu, prodeje nebo výroby.
je k dispozici, když jsou potvrzeny prodejní, nákupní nebo výrobní objednávky na produkt.

Možnosti vyhledávání
--------------

.. záložky::

...... tab:: Filtry

V sekci Filtry mohou uživatelé vyhledávat mezi předdefinovanými filtry a vlastními filtry.
najít konkrétní záznamy o cenných papírech.

      - :guilabel:`Zveřejněno“: Zobrazuje produkty zveřejněné na webu. K dispozici pouze s
Instalováno aplikace pro webové stránky.
      - :guilabel:`Dostupné v POS“: zobrazuje produkty dostupné prostřednictvím aplikace *Point of Sale*.
      - :guilabel:`Dostupné v samoobsluze‘: zobrazuje produkty dostupné v samoobsluze prostřednictvím *Punktu
aplikace pro prodej*. Aplikace se objeví v hledání, protože je zaškrtnutá možnost „Dostupné k samoobslužnému nákupu“.
Byla zaškrtnuta v sekci „Prodej“ na formuláři produktu v poli „Prodeje“.
Tabulka. Tato možnost je k dispozici pouze tehdy, když je zaškrtnuto políčko „Dostupné na POS“.

.. obrázek: stock/dostupnost-vlastni-objednavky.png
:align:center
:alt:V záložce Prodej v kartě produktu zobrazuje nastavení *Dostupné na samoobjednávku*.

      - :guilabel:`Není k dispozici v samostatných prodejnách“: zobrazuje produkty dostupné ve *PoS* ale ne v samostatných prodejnách.
samostatně objednat.

.. se také podívejte na:
„Nastavení produktů POS <https://www.youtube.com/watch?v=REbA3TBhFa4>“

      - Zobrazit produkty, které lze prodávat zákazníkům. Zobrazuje se v
hledání, protože v poli produktu je zaškrtnuté pole „Může být prodáno“.
      - :guilabel:„Může být koupen“: zobrazuje produkty, které lze zakoupit od prodejců.
vyhledávání, protože je zaškrtnutá možnost „Může být zakoupena“ na formuláři produktu.
      - :guilabel:Může se opakovat: zobrazení předplatných produktů označených zaškrtnutím
:guilabel:`Opakující se“ zaškrtávací políčko v objednávkovém formuláři. K dispozici pouze s předplatným
aplikace aktivována.
      - :guilabel:`Může být půjčeno“: zobrazuje produkty, které lze zapůjčit zákazníkům na určitou dobu.
Vyhledává se, protože byla zaškrtnuta možnost „Může být pronajato“.
produktu. K dispozici pouze s aplikací Rental nainstalovanou.
      - :guilabel:`Může být poddodavatelská“ zobrazí produkty, které lze vyrábět
třetí strana. K dispozici pouze s aplikací *Výroba*.
      - :guilabel:`Může být uplatněn“: zobrazují položky, které lze uplatnit. Tato funkce je dostupná pouze s
Instalováno aplikace Expenses.

.. se také podívejte na:
:doc:`../../produktní_správa/konfigurovat/typ`

... tab:: Skupina

Sekce „Skupina“ umožňuje uživatelům přidávat předdefinované a vlastní skupiny do
výsledky vyhledávání.

      - :guilabel:`Produktová skupina“: seskupit položky podle „druhu produktu
<../../produktní-správa/konfigurovat/typ>.
      - :guilabel:`Kategorie produktů“: seskupte položky podle kategorií produktů. Konfiguraci proveďte v
:menu_selektor:`Skladové aplikace --> Konfigurace --> Zboží: Kategorie zboží`.
      - :guilabel:`Kategorie produktů POS“: seskupte položky podle kategorií produktů na prodejních místech
<../../../prodej/pokladna/konfigurace>.

.. tab:: Oblíbené

Uložit aktuální použité filtry a skupinové sloupce, aby se stejná informace mohla snadno zobrazit.
po zavření této stránky klikněte na tlačítko :guilabel:`Uložit aktuální vyhledávání“.

Volitelně zaškrtněte políčko „Výchozí filtr“ a tento aktuální pohled se stane výchozím.
filtr při otevření výkazu zisku a ztráty. Nebo zaškrtněte políčko „Sdílené“ a učiněte
bude dostupná ostatním uživatelům.

Poté klikněte na tlačítko :guilabel:`Uložit`.

.. viz také:
:doc:`../Essentials/Search`
