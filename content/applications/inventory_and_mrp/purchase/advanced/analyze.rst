========================
Zpráva o analýze nákupu
========================

.. |PO| nahradit za: abbr: PO (objednávka na nákup)
.. |POs| nahradit za: zkratka: `POs (objednávky k nákupu)`

Výkaz o analýze nákupu poskytuje statistiky o produktech zakoupených pomocí Odoo.
Aplikace pro nákupy. Tato data jsou užitečná k hlubšímu porozumění klíčových metrik souvisejících s
objednávky nákupu (PO), včetně množství produktů objednaných a přijatých, doby dodání.
jak dlouho trvá převzetí zakoupeného zboží a další.

Pro otevření zprávy Analýza nákupu přejděte na: „Nákupní aplikace --> Zprávy -->
Koupit“.

.. důležité:
Report „Analýza nákupu“ je jedním z mnoha dostupných reportů v aplikaci Odoo
balíček. Tato dokumentace se týká pouze opatření specifických pro :guilabel:`Analýza nákupu`.
reportu, včetně několika příkladů použití.

Pro kompletní přehled základních funkcí dostupných v většině zpráv Odoo se podívejte na dokumentaci
na stránce „Základy hlášení“ na adrese https://www.w3.org/TR/2018/REC-WCAG21-Understanding-Reporting-Essentials-20181017/.

Opatření
========

Měřítka odkazují na různé sady dat, které lze zobrazit v :guilabel:`Analýza nákupu“.
reportu s každým datovým souborem reprezentujícím klíčový statistický údaj o |POs| nebo produktech.
Klikněte na tlačítko „Měření“ a vyberte jednu z možností.
kliknutím na tlačítko „Drop down“

- :guilabel:`Počet řádků PO“: Počet řádků objednávky v rámci všech PO.
- :guilabel:`Průměrná cena“: Průměrná cena |POs|.
- :guilabel:`Dny k potvrzení“: Počet dní, které trvá potvrdit |PO|.
- :guilabel:`Dny k doručení`: Počet dní potřebných na dodání produktů do skladu |PO|.
- :guilabel:`Hmotnost celkem“: Celková hmotnost zakoupených produktů.
- :guilabel:"Množství fakturované": Množství produktu (nebo produktů), za který/které již dodavatel vystavil
Byla vyúčtována.
- :guilabel:`Počet objednaných kusů“: Počet produktu (nebo produktů) objednaný.
- :guilabel:`Počet obdržených kusů“: Počet objednaného produktu (nebo produktů) obdržený.
- :guilabel:`Počet kusů, které mají být fakturovány“: Množství objednaného produktu (nebo produktů), pro který/které má být vystavena faktura
Dodavatel zatím nebyl fakturován.
- :guilabel:`Celkem“: Celková částka včetně DPH.
- :guilabel:`Celková částka bez DPH“: Celkové náklady včetně všech poplatků a daní.
výchozí.
- :label_guid:„Objem“: Celkový objem objednaných produktů pro produkty měřené
objem.
- :guilabel:`Počet celkem“: Celkový počet |POs|.

..tip:
Vybírat lze pouze jednu z nich, když je aktivní ikonka :icon:`fa-area-chart`.
:guilabel:`(zobrazení grafu)` možnost je zapnutá. Nicméně více měření a různé skupinování
kritéria (na ose x a y) lze vybrat při použití ikonky „OI View Pivot“
:guilabel:`(tabulka přehledů).

.._nákupní analýza příklad:

Příklad použití: určení dnů dodání produktů od každého dodavatele
=============================================================

Jedním z možných použití pro zprávu „Analýza nákupů“ je určení, jak dlouho trvá každá
Dodavatelé dodávají zboží, které si zákazníci objednali. To umožňuje firmám lépe se rozhodovat
o kterých dodavatelích chtějí nakupovat.

Příklad:
Místní prodejna jízdních kol Bike Haus prodává kvalitní jednokolky, dvojkolky, trojkolky a všechno možné.
příslušenství potřebné k jízdě a údržbě. Nákup svého sortimentu provádějí u několika různých
prodejci a pak prodávat tyto produkty zákazníkům prostřednictvím svých obchodů.

Nedávno společnost Bike Haus rozhodla, aby jejich nákupní manažer David zjistil, jak dlouho bude trvat
Každému z dodavatelů přinesl věci, které si v tomto roce koupil.
   2024.

David začíná tím, že se přesune na: `Nákup aplikace -> Zprávy -> Nákup`.
vybráním grafu typu „Bar Chart“ v horní části zprávy.

Poté klikne na tlačítko :icon:`fa-caret-down` :guilabel:`(přepínač)` vpravo od vyhledávacího pole.
v nabídce. V sekci filtru „Datum potvrzení“ zvolí
že je zapnutý pouze filtr „2024“. Pak si vybere
:guilabel:"Dodavatel" v sekci "Skupiny" před kliknutím na jiné místo.
nabídku pro zavření.

Konečně si David klikne na položku „Měření“ v rozbalovacím seznamu a
Vybírá možnost „Dny k doručení“.

S aktivovanými všemi možnostmi se v zprávě „Analýza nákupu“ zobrazí graf.
s jedním barem pro každého dodavatele, který reprezentuje průměrný počet dní potřebných k přijetí
zboží zakoupené u dodavatele.

Davidovi pomáhá tato data zjistit, že průměrně trvá doručení Bike Friendů přes 4,5 dne.
převzatých produktů. To je více než čtyřnásobek doby, kterou jiní dodavatelé potřebují k přijetí objednávky.

Na základě těchto zjištění se David rozhodne snížit množství nakupovaných produktů.
od Bike Friends.

.... obrázek: analyze/dtr.png
:synchronizace: střed
:alt:Zpráva o nákupu ukazující průměrný počet dní potřebných k přijetí zboží od dodavatelů.

Příklad použití: porovnání dodavatelských faktur za dvě časová období
=================================================

Další možností použití zprávy „Analýza nákupu“ je porovnání klíčových statistik o |POs|
pro dvě různé časové období, pro konkrétního dodavatele. Díky tomu je snadné pochopit, jak
Nákupy od dodavatele se zvýšily nebo snížily.

Příklad:
Podle předchozího příkladu :ref:`<purchase/purchase-analysis-example>` uběhlo jeden měsíc.
protože Bike Haus rozhodl o snížení objemu produktů nakupovaných od Bike Friends,
jejich prodejců. Purchasing Manager společnosti Bike Haus, David, chce pochopit dopad
jaký měla rozhodnutí na množství peněz, které utratili za produkty společnosti Bike Friends.

David začíná tím, že se přesune na :menuselection:`Nákup aplikace --> Zprávy --> Nákup“. Pak
vybere možnost „Pohled na tabulku (pivot table)“ v horní části obrazovky.

Vyhledávací liště napíše „Bike Friends“ a klikne na Enter. Výsledek je tedy jenom jeden.
Zobrazuje údaje o nákupu z Bike Friends.

Pak klikne na tlačítko :icon:`fa-caret-down` :guilabel:`(přepínač)` vpravo od obrázku.
Vyhledávací lištu otevře své rozbalovací menu. V poli „Datum potvrzení“ nechává
:guilabel:'Červen' a :guilabel:'2024' filtry zapnuté. Dále si vybere :guilabel:'Potvrzení
Datum: Předchozí období' v části 'Srovnání', než se přesunete pryč.
nabídku pro zavření.

Pak klikne na položku „Měření“ v rozbalovací nabídce :guilabel:`Measures` :icon:`fa-caret-down`.
- zapnout a vypnout data „Celkem“ a „Celkem bez daně“.
:guilabel:`Objednávky“ a „Počet“.

Konečně klikne na tlačítko „Celkem“ nad řádky.
pivotovou tabulku a vybere možnost „Produkt“.

S veškerými nastaveními je v zprávě „Analýza nákupu“ (viz obrázek) vidět přehledový graf.
Tabulka porovnávající nákupní data za aktuální měsíc červen, s předchozím měsícem květenem.

Pivotová tabulka je rozdělena do dvou hlavních sloupců: jeden pro celkové výdaje bez daně a druhý
pro celkovou částku uvedenou v daňovém přiznání. Tyto sloupce jsou dále rozděleny na tři menší sloupce:
částka utržená v květnu, částka utržená v červnu a změna mezi těmito dvěma měsíci.
Je vyjádřen jako procento.

Na levém sloupci tabulky se pro každý produkt zobrazuje jedna řádka.
Přátelé v červnu. Díky tomuto hlášení si David může všimnout, že Bike Haus utratil mnohem méně
výdaje na nákup zboží od Bike Friends oproti předchozímu měsíci.

.. obrázek:: analyze/comparison.png
:synchronizace: střed
:alt:Zpráva o nákupu s porovnáním částky uhrazené dodavateli.
