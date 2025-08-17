==============
Převody vln
==============

.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`

Při přepravě várky se jedná o skupinu několika vyzvednutí, zatímco při přepravě vlny jde o určité části.
různých převodů. V Odoo jsou vlnové převody převody s jedním navíc: převody jsou
před tříděním do skupin.

Vybírání vln je ideální pro sklady, které potřebují optimalizovat zpracování velkého objemu objednávek.
správě složitých kritérií pro vybírání. S přenosy vln se objednávky seskupují do vln podle
faktory jako umístění produktu, kategorie nebo plánované časy dodání. Každá vlna je přiřazena
jiný zaměstnanec pro co nejefektivnější provedení.

Vybírání vln je zvláště užitečné pro operace, kde existuje více prodejních objednávek (PO) nebo jedna
musí být vybrány v různých vlnách. Tento přístup umožňuje flexibilní plánování a umožňuje
sklady k synchronizaci činností při vyzvedávání s termíny dodávek nebo dostupností zdrojů.

Příklad:
   #. |SO| 1 volá po jednom jablku a jednom pomeranči
   #. |SO| 2 volá po jednom jablku a jedné banánu
   #. |SO| 3 volá po jednom jablku, jednom pomeranči a dvou banánech

Jablka jsou skladována na polici A, pomeranče na polici B a banány na polici C. Skladník
je přiřazen k vlně a je mu předložen následující příkaz:

   - Police A: Vyberte tři jablka. Umístěte je do středního vozíku určeného pro vlnu.
   - Police C: Vyberte dvě pomeranče a přidejte je do stejného košíku.
   - Police C: Vyberte tři banány a přidejte je do košíku.

Poté zaměstnanec vozík převeze na stanici třídění a balení, kde jsou věci tříděny a zabalovány.
do individuálních objednávek.

Konfigurace
=============

Chcete-li umožnit výběr vln, začněte tím, že se přesunete na: „Náhledy a konfigurace“
Nastavení“. V sekci „Operace“ zaškrtněte políčko „Vlna, skupina a cluster“.
Zatrhněte políčko „Převody“.

.. obrázek: wave/wave-transfers-settings.png
:alt: Zobrazení nastavení aplikace Odoo Sklad pro zapnutí možnosti přenosu vln.

Dále volba „Uložiště“ a „Složené trasy“, které jsou pod
Nastavení stránky „Sklad“ musí být také zkontrolováno pod nadpisem „Sklad“.

„Uložiště“ umožňují skladování konkrétních produktů na určitých místech, ze kterých je lze vyzvednout.
Díky vícekrokovým trasám je možné provádět samotnou operace sběru.

Poté klikněte na tlačítko „Uložit“ pro uložení změn.

Vytvořte vlnu
=============

Přenosy vln mohou obsahovat pouze produktové řady přenosů stejného typu operace.
Všechny převody a produktové řady v konkrétní operaci najdete na
:menu:„Aplikace inventář“. Vyberte požadovanou kartu Kanban, pak klikněte na ikonku „fa-ellipsis-v“
:guilabel:`(vertikální elipsa)` ikonu pro otevření nabídky možností. V sekci „Nový“ klikněte
:guilabel:`Připravit vlnu“.

.. obrázek: vlna/seznam operací.png
:alt:Jak získat seznam operací typu operačního systému.

Vytvořit novou vlnu
-----------------

Na kartě „Připravit vlnu“ jsou pohyby zboží seskupeny podle zdrojového umístění. Vyberte
zaškrtávací políčka produktových řad, které chcete přidat. Poté klikněte na tlačítko „Přidat do vlnovky“.

.. obrázek: wave/select-lines.png
:alt:Vyberte řádky, které chcete přidat do vlny.

..tip:
Využijte filtrů v hledaném poli k seskupení řádků s produktem, místem a
dopravce, apod.

Přidejte produkty do stávající vlny
--------------------------------

Chcete-li přidat produkty do stávající vlny, přejděte na: „Sklad --> Provoz --> Vlna
Převody“. Klikněte na příslušnou vlnu z seznamu, abyste ji otevřeli.

Pod záložkou „Podrobné operace“ klikněte na „Přidat řádek“. Poté v
V poli „Produkt“ vyhledejte požadovaný produkt.

Zpracujte vlnu
==============

Pro zobrazení všech přenosů vln a jejich stavů přejděte na: „Skladové zásoby“ - „Operace“
Převodníky vln. Klikněte na příslušnou vlnu z seznamu, abyste ji otevřeli.

Přiřadit vlnu konkrétnímu zaměstnanci můžete kliknutím na pole „Zodpovědná osoba“ a výběrem
vhodný název ze seznamu.

Pro určení místa přístavu vyberte možnost ze seznamu
kliknutím na tlačítko „Změnit“ v poli „Lokalita doku“.

.. poznámka::
Systém pro správu přepravy zboží (dále jen „systém pro správu přepravy“):
Tato funkce v Odoo slouží k plánování a sestavování zásilek. Přiřazení šarží ke skladovacím prostorům zajišťuje
připravené produkty jsou zabaleny do vhodných nákladních vozidel pro dodání.

Z rozevírací nabídky vyberte „Vozidlo“. Vybráním položky v tomto poli se automaticky
aktualizuje pole „Kategorie vozidla“.

Pokud chcete, zadejte do pole „Popis“ popis této vlny.

.. poznámka::
V poli :guilabel:`Popis` je automaticky vygenerováno pole :ref:`automatické vlny
<Inventar/Versand und Empfang/Auto-Wellen>.

... inventarizaci, přijímání a odesílání zboží, automatické vlny:

Automatické vlny
===============

Vlny mohou být automaticky vytvořeny a přiřazeny na základě různých kritérií.
Volba je definována na úrovni operačního typu, což umožňuje vytváření vln s jasně
kritéria pro každý typ operace.

Pro zapnutí automatických balení, přejděte na:
Operační typy“ a vyberte požadovaný operační typ (např. „Dodání“,
„Pick“, atd.). V sekci „Sběr a přenosy vln“ zaškrtněte
zaškrtávací políčko „Automatické balení“.

Pak vyberte jednu nebo více kritérií skupinování vln pomocí zaškrtávacího políčka.
I když je vybráno více možností pro seskupení, vytvoří se jen jedna vlna.

Automatické vlny lze vytvářet na základě následujících kritérií:

- :guilabel:`Produkt“: Rozdělte převody podle produktu a pak seskupte převody s týmž produktem.
- :guilabel:`Kategorie produktů“: Rozdělte převody podle kategorií produktů a pak seskupte převody, které mají
stejné kategorie produktů.

.. obrázek: vlna/automatické seskupení vln.png
:alt:Automatické balení s možností skupinování vln pro vybranou kategorii produktů.
