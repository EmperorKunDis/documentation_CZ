===============================
Průměrná cena zboží vráceného zpět
===============================

.. |AVCO| nahradit za: zkratka: `AVCO (Průměrná hodnota nákladů)`
... _Inventář/Průměrná cena/Definice:

Metoda průměrné nákladové ocenění (AVCO) je metoda oceňování zásob, která vypočítává cenu na základě
celkové náklady na zboží zakoupené nebo vyrobené v daném období děleno celkovým počtem kusů
Na skladě. Hodnota zásob se používá k:

- odrážet hodnotu aktiv společnosti.
- sledovat množství neprodaných zboží.
- zahrnout hodnotu peněz v zboží, které ještě nepřineslo zisk.
- výroční zprávu o přepravě zboží za čtvrtletí.

Protože AVCO využívá ke hodnocení nákladů vážený průměr, je vhodná pro společnosti, které
prodávat jen několik různých produktů v velkém množství. V Odoo je tato analýza nákladů
*automaticky aktualizované* při každém přijetí zboží.

Při vrácení zboží se tedy automaticky generují účetní záznamy.
aby odrážel změnu v ocenění zásob. Nicméně Odoo automaticky neaktualizuje
Výpočet AVCO, protože: „Toto může v budoucnu vést k nesrovnalostem s inventářem
hodnota inventáře <výchozí cena/průměrná cena/odcházející inventář>.

.. poznámka::
Tento dokument se zabývá konkrétním použitím pro teoretické účely. Pro pokyny, jak postupovat
zřídit a používat |AVCO|, odkazovat na konfiguraci inventarizace v hodnotě

doc.

.. viz též:
   - Použití metody ocenění zásob

   - :ref:`Jiné metody ocenění zásob <skladové zásoby/metody-ocenění-zásob>`

Konfigurace
=============

Pro použití metody ocenění zásob podle průměrné ceny produktu přejděte na:
Konfigurace --> Kategorie produktů a vyberte kategorii, která bude používat |AVCO|.
stránka kategorie produktu, nastavte:guilabel:`Metoda nákladů“ na „Průměrná cena (AVCO)“.
„Ocenění zásob“ na „Automatické“.

.. viz též:
:doc:`Konfigurace inventarizační hodnoty


Použitím metody průměrné hodnoty
============================

Metoda průměrné ceny upravuje ocenění zásob při přijetí zboží do skladu.
Tato část vysvětluje, jak to funguje, ale pokud je vysvětlení zbytečné, přeskočte na :ref:`návrat
do sekce „Případ použití dodavatele (sklad/průměrná cena/vrácení)“.

... _Inventář/Průměrná cena/Formule:

Formule
-------

Když přijdou nové produkty, je vypočítána nová průměrná cena každého produktu pomocí vzorce:

.. matematika::
Průměrná cena = \frac{Stará kupní cena (Old Qty) x Stará průměrná cena (Old Avg Cost) + Příchozí množství (Incoming Qty) x Nákupní cena (Purchase Price)}{Konečné množství (Final Qty)}

- **Starý počet kusů**: množství produktu v zásobách před příjmem nové dodávky.
- **Stará průměrná cena**: vypočítaná průměrná cena za jednotku produktu z předchozího zásobování
ocenění.
- Počet příchozích kusů: počet produktů, které přicházejí v nové dodávce.
- *Cena nákupu*: odhadovaná cena produktů při převzetí zboží (od dodavatele)
Dodací lhůta se může pohybovat v rozmezí 1-3 dnů (v závislosti na zemi a způsobu dopravy). Cena je konečná a zahrnuje nejen cenu produktu, ale také náklady na dopravu.
například dopravu, daně a náklady na skladování.
<../../../Inventar a MRP/Inventar/Produktmanagement/Bewertung des Inventars/Landed Costs>.
přijetí faktury dodavatele, cena se upravuje;
- **Konečné množství**: počet položek skladu po přesunutí zásob.

... _Inventář/Průměrná cena/Definice pravidla:

.. důležité::
Když se produkty vydají z skladu, průměrná cena **ne** změní. Přečtěte si proč
průměrná cena se neupravuje viz odkaz zde:

... /soubor inventáře/průměrná cena/matematická tabulka:

Vypočítat průměrnou cenu
--------------------

Chcete-li pochopit, jak se průměrná cena produktu mění s každou dodávkou, zvažte následující
tabulka skladových operací a pohybů zásob. Každá z nich je jiným příkladem průměrné náklady
hodnota nemovitosti se snižuje.

+--------------------------------+---------------+-------------------+---------------+------------+
Operace                          | Hodnota vstupu  | Hodnota zásob  | Množství skladem | Průměrná cena
+================================+===============+===================+===============+============+
|                                |               | $0                | 0             | $0         |
+--------------------------------+---------------+-------------------+---------------+------------+
|Přijměte 8 stolů za $10/kus   |8 * $10       |$80               |8             |$10        |
+--------------------------------+---------------+-------------------+---------------+------------+
|Přijměte 4 stoly za 16 dolarů/kus. | 4 * 16      | 144               | 12           | 12          |
+--------------------------------+---------------+-------------------+---------------+------------+
Dodat 10 stolů            | -10 * $12    | $24           | 2             | $12         |
+--------------------------------+---------------+-------------------+---------------+------------+

... inventář/průměrná cena/ex-1:

...cvičení::
Zajistěte pochopení výše uvedených výpočtů přečtením „Přijmout 8 stolů za 10 dolarů“
příkladu.

Začínáme s nulovým zásobami, takže všechny hodnoty jsou $0.

První skladovací operace přijímá osm stolů za deset dolarů. Průměrná cena je
vypočítané podle vzorce uvedeného na odkazu :ref:`<inventory/avg_cost/formula>`.

......::
Avg~Cost = \frac{0 + 8 \krát 10}{8} = \frac{$80}{8} = $10

   - Odcházející množství stolů je 8 a pořizovací cena každého z nich činí 10 $.
   - Hodnota v závorce v čitateli je vyčíslena na $ 80;
   - Výsledek dělení částky 80 je 8.
   - Průměrná cena jednoho stolu z první dodávky je 10 $.

aby se v aplikaci Přijetí objednávky (v Odoo) objednalo osm kusů nového produktu „Stůl“.
bez předchozích pohybů zásob za $10 kus.

V poli „Kategorie produktu“ v záložce „Obecné informace“.
produktu, klikněte na ikonu ➡️ (šipka), abyste otevřeli odkaz na
upravit kategorii produktu. Zadejte jako metodu nákladů „Průměrná cena (AVCO)“ a
:guilabel:`Hodnota zásob“ na „Automatické“.

Pak se vraťte k objednávce a klikněte na tlačítko „Potvrdit objednávku“ a poté na „Doručení“.
Potvrzení o přijetí zboží.

Poté zkontrolujte záznam o hodnotě zásob, který byl vytvořen při přijetí produktu, kliknutím na
:menu_vyber:`Sklad --> Hlášení --> Oceňování zásob“. Vyberte z roletky
„Stůl“ a zobrazte sloupec „Celková hodnota“ pro vrstvu *hodnotícího modelu* (viz. „Inventarizační model“).
hodnota k určitému datu = skladové množství * cena za jednotku.
Je jich 12 a každá stojí 80 $.

.... obrázek: průměrná cena ocenění / inventarizační hodnota 8 tabulek.png
:align:center
:alt:Zobrazení hodnoty zásob v Odoo pro 8 stolů.

.. tip::
Když je nastaveno pole „Metoda nákladového účtování“ kategorie produktu na „AVCO“, pak
Průměrná cena produktu je také zobrazena v poli :guilabel:`Náklady`, které se nachází pod
:guilabel:`Obecné informace“ v záložce produktu samotného.

Dodání produktu (případ použití)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pro odchozí zásilky má :ref:`výstupní produkty na výpočet průměrné ceny žádný vliv
<výkazu/průměrné ceny/definovaná pravidla>.Although the average cost valuation is not recalculated, the
Zásoby se stále snižují, protože produkt je vyřazen z prodeje a dodán zákazníkovi.
místo zákazníka.

...cvičení::
aby bylo jasné, že průměrná cena se nevypočítává znovu, zkontrolujte „Dodání 10
příkladu „stoly“.

......::
Avg~Cost = \frac{$12 \times 12 + (-10) \times 12}{12 - 10} = \frac{24}{2} = $12

   #Protože jsou odeslány 10 stolů zákazníkům, množství „přicházejících“ je -10.
předchozí průměrná cena (12 USD) je použita místo nákupní ceny dodavatele;
   #*. Příchozí hodnota zásob je „-10 * 12 = -120“;
   #Starý stav zásob („144 $“) je přičten k příchozímu stavu zásob („-120 $“), takže
      `$144 + -$120 = $24`;
   #Po odeslání 10 stolů z 12 zbývají pouze dva. Aktuální zásoba
hodnota * ($ 24) je dělena počtem skladem (2).
   #„$24/2=12“, což je stejná průměrná cena jako u předchozí operace.

V Odoo potvrďte prodej „10“ stolů v aplikaci *Prodeje*, ověřte dodání a pak
zkontrolovat záznam o hodnotě zásob, přejděte na: menu „Skladové zásoby -> Zprávy ->
„Inventarizační ocenění“. V nejvyšším vrstvě inventarizačního ocenění se dodávají tabulky s hodnotou „10“, což snižuje
hodnotu produktu o $-120.

*Poznámka: Co není v tomto záznamu o hodnotě akcií zahrnuto, je příjem, který byl z tohoto
Prodej se nezdařil, takže tento pokles není ztrátou pro společnost.

.. obrázek: průměrná cena ocenění / inventarizační hodnota - zaslání 10 tabulek.png
:align:center
:alt:Zobrazte, jak se snižuje hodnota zásob.

.. inventář/průměrná cena/návratnost:

Vrácení položek dodavateli (případ použití)
===================================

Protože cena, kterou dodavatelům zaplatíme, se může lišit od ceny, za jakou je produkt oceněn.
Metoda |AVCO|, Odoo se vracenými položkami zachází zvláštním způsobem.

#Zboží se vrací dodavatelům za původní cenu, ale;
#Změna se týká pouze cenových hodnot, které jsou uvedeny na prodejních cenovkách.

Tabulka výše uvedeného příkladu je aktualizována následovně:

+--------------------------------+---------------+-------------------+---------------+------------+
|Operace                          |Počet*Průměrná cena |Zásoby na skladě |Počet kusů na skladě |Průměrná cena |
+================================+===============+===================+===============+============+
|                                |               | $24               | 2             | $12        |
+--------------------------------+---------------+-------------------+---------------+------------+
|Vrácení jedné stolice za deset dolarů. -1 * 12 dolarů | 12 dolarů | 1 | 12 dolarů
+--------------------------------+---------------+-------------------+---------------+------------+

Takže vrácení zboží dodavateli je pro Odoo dalším způsobem výstupu produktu
skladu. Pro Odoo je hodnota stolu 12 USD za kus a proto se v případě skladování
$ 12, když je produkt vrácen. Původní cena $ 10 není spojená s kupní cenou stolu.
průměrná cena.

.. příklad::
Chcete-li vrátit jedinou tabuli, která byla zakoupena za 10 $, přejděte na fakturu v sekci *Sklad*.
aplikace pro :ref:`8 tabulek zakoupených v úloze 1 <inventar/průměrná cena/ex-1>`, přičemž se dostanete na
:guilabel:`Přehled inventáře“, klikněte na :guilabel:`Doklady“ a vyberte požadovaný
faktura.

Poté klikněte na tlačítko „Vrácení“ v potvrzeném dodacím listu a změňte množství na 1.
obrácený okno přenosu. To vytvoří odchozí dodávku pro stůl. Vyberte
:guilabel:`Potvrdit“ pro potvrzení odeslané zásilky.

Návrat na: „Inventář –> Zprávy –> Ocenění zásob“ a zjistěte, jakým způsobem se oceňují zásoby.
S odesláním zboží se hodnota zásob sníží o 12 $.

...... obrázek: průměrná cena ocenění/výnos z inventáře.png
:align:center
:alt:Výpočet hodnoty vráceného zboží.

.. inventář/průměrná cena/výstup z inventáře:

Vyřešte chyby v oceňování zásob ve výrobcích, které jsou na prodej
-----------------------------------------------------

Nesrovnalosti v zásobách mohou nastat při přepočítávání průměrné ceny
na vývozní zásilky.

Chybu si můžete ověřit v tabulce níže, která zobrazuje scénář, kdy je jedna skladovací polička odeslána do
jedna je prodána zákazníkovi, druhá se vrací dodavateli za cenu, za kterou byla zakoupena.

+------------------------------------------+---------------+-------------------+---------------+------------+
|Operace                                      |Počet*Cena    |Hodnota zásob  |Počet skladem  |Průměrná cena |
+==========================================+===============+===================+===============+============+
|                                          |               | $24               | 2             | $12        |
+------------------------------------------+---------------+-------------------+---------------+------------+
|Odeslat zákazníkovi jeden produkt          |-1 * $12      |$12                |1              |$12         |
+------------------------------------------+---------------+-------------------+---------------+------------+
|Vrácení jednoho výrobku, který byl původně zakoupen za 10 dolarů|-1 * $10      |**$2**           |**0**          |$12       |
+------------------------------------------+---------------+-------------------+---------------+------------+

V poslední operaci výše je konečná hodnota zásob pro stůl $ 2 i když
zůstalo 0 stolů skladem.

.. varování: správný postup

Použijte průměrnou cenu k vyčíslení návratnosti investice. To neznamená, že společnost dostane zpět 12 dolarů za každých 10.
nákup; položka v hodnotě 10 USD je oceňována interně na 12 USD. Změna hodnoty zásob
Toto je produkt v hodnotě 12 dolarů, který již není zahrnutý do aktiv společnosti.

Anglosaské účetnictví
======================

Kromě používání |AVCO| mají společnosti, které využívají **anglosaské účetnictví**, také vlastní holding
účet, který sleduje částku, která má být zaplacena dodavatelům. Jakmile dodavatel doručí objednávku, **sklad
Hodnota ** se zvyšuje na základě ceny dodavatele produktů, které jsou ve skladu.
účet (označený jako „vstup do zásoby“) je přičítán a vyrovnávání se provádí pouze po obdržení faktury od dodavatele.

.. viz též:
   - :ref:`Anglosaský vs. kontinentální <skladování/sklady/účetní typy>“

Tabulka níže ukazuje záznamy v deníku a účtech. Účet „vstupní zásoby“ obsahuje peníze
je určen k úhradě dodavatelům, když faktura dodavatele ještě nebyla přijata. Aby se vyrovnaly účty,
vracení zboží, u něhož je rozdíl mezi cenou, za kterou je zboží **hodnoceno**
cena, za kterou bylo zboží zakoupeno, je vytvořen účet rozdílu ceny.

... inventář/průměrná cena/cena za jednotku:

+-----------------------------------------+---------------+--------------+-------------------+---------------+------------+
|Operace                                |Vstup do zásoby  |Rozdíl cen  |Hodnota zásob  |Množství na skladě |Průměrná cena |
+=========================================+===============+==============+===================+===============+============+
|                                         |               |              | $0                | 0             | $0         |
+-----------------------------------------+---------------+--------------+-------------------+---------------+------------+
|Přijměte osm stolů za 10 dolarů.           |(80)          |              |$80              |8             |$10        |
+-----------------------------------------+---------------+--------------+-------------------+---------------+------------+
Přijmout fakturu od dodavatele za 80 dolarů   | 0           |              | 80              | 8             | 10         |
+-----------------------------------------+---------------+--------------+-------------------+---------------+------------+
|Přijměte 4 stoly za $16               |($64)          |              |$144             |12             |$12           |
+-----------------------------------------+---------------+--------------+-------------------+---------------+------------+
|Přijmout fakturu od dodavatele v hodnotě 64 USD | 0            |               | 144            | 12            | 12          |
+-----------------------------------------+---------------+--------------+-------------------+---------------+------------+
Doručit zákazníkovi deset stolů          | $0            |              | $24               | 2             | $12        |
+-----------------------------------------+---------------+--------------+-------------------+---------------+------------+
|Vrácení jedné tabulky, kterou jsme původně koupili za 10 dolarů.|**10**|**2**|**12**|1|$12
+-----------------------------------------+---------------+--------------+-------------------+---------------+------------+
|Přijmout vrácení od dodavatele ve výši 10 USD | 0 USD         | 2 USD          | 12 USD          | 1 USD         | 12 USD       |
+-----------------------------------------+---------------+--------------+-------------------+---------------+------------+

Přijetí produktu
-----------------

Shrnutí
~~~~~~~

Odoo zajišťuje, že společnosti mohou zaplatit za zboží, které bylo předem zakoupeno.
přesunout částku odpovídající ceně přijatých věcí do účtu závazků
</aplikace/finance/účetnictví/začínáme/tabulka-s-triky/>“, „Vstupní zásoba“. Poté, co vám přijde faktura
byla přijata, částka na účtu pro držení se převede na účet „Závazky“.
do této položky znamená, že faktura byla zaplacena. **Vstupy na sklad** se vyrovnají jednou, když bude dodavatelská faktura
je přijímán.

Metoda ocenění zásob spočívá v tom, že se stanoví hodnota každého produktu skladem interně.
Odchylka mezi cenou, za kterou je produkt oceněn, a skutečnou cenou.
Produkt byl ve skutečnosti zakoupen za, účet „Ocenění zásob“ není vůbec spojen s
účet vkladů a výběrů z obchodního účtu.

Pro pochopení celé věci se podívejte na následující graf.

Vzájemně vyrovnané účty za přijaté zboží
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V tomto příkladu společnost začíná s nulovým počtem produktů „stůl“. Pak je vyrábí osm stolů.
jsou přijímány od dodavatele:

#V účtu „Zásoby vstupů“ je uloženo $80 kreditu, který dluží dodavateli.
Je nezávislá na hodnotě zásob.
#Každá stůl přišel na $80 (odčet z účtu Inventory Value v hodnotě $80).
#„$80“ musí být zaplaceno za přijaté zboží (kreditovaná položka „Vstup do zásob“ v hodnotě $80).

Odoo
*******

Odoo vytváří účetní záznamy při odeslání zásilek, které používají metodu nákladů na výrobky (AVCO).
přijat. Konfigurujte účet „Rozdíl ceny“ pomocí výběru „➡️ (šipka)“.
ikona vedle pole „Kategorie produktu“ na stránce s produktem.

Pod položkou „Vlastnosti účtu“ vytvořte nový účet „Rozdíl cen“ zadáním
Název účtu a klikněte na „Vytvořit a upravit“. Pak nastavte účet
Vyberte „Typ“ a zadejte „Náklady“. Klikněte na „Uložit“.

.. obrázek:avg_price_valuation/create-price-difference.png
:align:center
:alt: Vytvořit účet cenového rozdílu.

Následně přijměte zásilku v aplikaci „Nákup“ nebo „Sklad“, a poté se přesuňte do
:menuselection:`Účetní aplikace --> Účetnictví --> Účetní případ“. V seznamu najděte
„Referenční“ štítek, který odpovídá příjmu zboží v skladu pro daný produkt.

.. obrázek:avg_price_valuation/hledani_vstupu_do_tabulek.png
:align:center
:alt:Zobrazit účetní záznam o 8 stolech z seznamu.

Klikněte na řádek s osmi stoly. Tento účetní záznam ukazuje, že když byly osm stolů
přijatých $ 80. Naopak účet „Vstupy do cenných papírů“
(výchozí účet s označením „Interim Stock Received“), je kreditováno částkou 80 $.

.. obrázek:avg_price_valuation/accounting-entry-8-tables.png
:align:center
:alt:Ocenění zůstatku debetu a vstupu zůstatku kreditu za 80 dolarů.

Účty vyrovnané na základě faktury od dodavatele
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

V tomto příkladu společnost začíná s nulovým počtem produktů stolu na skladě. Pak je k dispozici 8 stolů.
přijaté od dodavatele. Když je faktura za osm stolů přijata od dodavatele:

#Použijte $ 80 v účtu „Vstupy“ k zaplacení faktury. Tím se vyrovná a účet je nyní
obsahuje hodnotu 0.
#Debetní položka „Vstupy do zásob“ $80 (k vyrovnání této položky).
#Kreditní účet „Placené faktury“ s hodnotou 80. Tento účet ukládá částku, kterou společnost dluží jiným osobám, takže
účetní používají částku k napsání šeků dodavatelům.

Odoo
*******

Jakmile vám dodavatel požádá o platbu, přejděte na:
Vyberte položku „Nákup“ a v seznamu vyberte „PO (Purchase Order)“ pro 8 tabulek.
Vyberte možnost „Přidat objednávku“.

Přepněte na záložku „Položky v deníku“ a zobrazte si, jak je $ 80 převedeno ze skladu
účet „Stock Interim (Received)“ na účet „Závazky“. Potvrďte fakturu k záznamu.
Platba dodavateli.

.. obrázek: avg_price_valuation/receive-8-table-bill.png
:align:center
:alt:Zobrazit fakturu spojenou s objednávkou na 8 stolů.

Dodání produktu
-------------------

V příkladu tabulky výše (:ref:`viz inventář/průměrná cena/cena-tabulka<inventory/average-price/price-table>`), když je dodáno 10 produktů
Zákazníkovi zůstává v účtu „Příjem zásob“ stav beze změny, protože do firmy neproudí žádné nové produkty.
To je vše, co potřebujete vědět.

#Výsledný stav zásob se přičte k hodnotě zásob v nákupním ceníku, tedy k částce 120 $.
„$120“ hodnota produktů, které opouštějí společnost.
#Debetní účet „Příjmy“ pro zaznamenání příjmů z prodeje.

.. obrázek:avg_price_valuation/sell-10-tables.png
:align:center
:alt:Zobrazit záznamy v deníku, které jsou spojené se zakázkou.

..spoiler::Chápání anglosaského výdajového účetnictví

V účetním případu fakturace zákazníka za 10 stolů jsou účty **Produkt
Prodej, DPH a pohledávky jsou všechny spojeny s prodejem produktu.
„Příjmy“ je účet, na který bude připsána platba od zákazníka.

Anglické účetnictví uznává náklady na prodej (COGS) až po uskutečnění prodeje.
do doby prodeje, likvidace nebo vrácení zboží nejsou náklady na skladování výrobku.
Zaúčtováno. Účet „Náklady“ je odepsán částkou $120, aby byly zaznamenány náklady na skladování deseti stolů.
během této doby.

Vrácení zboží
-----------------

V následujícím příkladu tabulky (tabulka s průměrnou cenou výrobku v inventáři) se vrátíme jedno zboží do
Dodavatel koupil za 10 dolarů, společnost očekává na účtu „Placení“ v částce 10 dolarů.
dodavatel. Účet „Příjem zásob“ však musí být odepsán částkou $12, protože průměrná cena je $12 na
dočasu návratu. Chybějících dvacet dolarů se započítává do políčka :guilabel:`Rozdíl ceny
Účet“, který je nastaven v kategorii produktu: „Kategorie produktů“.

.. poznámka::
Chování účtu „Rozdíl cen“ se liší podle lokality. V tomto případě je účet
sloužil k ukládání rozdílů mezi cenami dodavatelů a automatizovanými metodami ocenění zásob.

Shrnutí:

#Debetní účet „Vstup zboží“ o částku $ 10, aby se stůl přesunul ze skladu do vstupu zboží. Tento pohyb je
ukazuje, že tabulka je určena pro zpracování výstupní zásilky.
#Debetní položka „Vstupní zásoba“ o dalších $ 2, abychom zohlednili rozdíl v ceně.
#Kreditní částka „Hodnota zásob“ je $ 12, protože položka opouští sklad.

.. obrázek:avg_price_valuation/expensing-price-difference-account.png
:align:center
:alt: Rozdíl dvou dolarů v účtu Cena.

Jakmile bude obdržená od dodavatele náhrada.

#Přičtěte kreditní účet „Vstupy“ částku 10 USD, abyste vyrovnali cenu stolu.
#Debetní účty platby za zboží a služby odečtěte $10, aby účetní vybrali a zaevidovali platbu.
jejich časopis.

.. obrázek: průměrná cena ocenění / vrácení kreditní zprávy.
:align:center
:alt:Vraťte se a získejte zpět 10 dolarů.
