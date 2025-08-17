===============================
Základní dodací lhůty pro poddodavatele
===============================

.. |PO| nahradit za: :abbr:`PO (Příkaz k nákupu)`
.. |RfQ| nahradit za: zkratku `RfQ (Request for Quotation)`

V Odoo jsou doby odezvy používány k předpovídání doby trvání určitého úkonu. Například
Pro zakoupený produkt lze nastavit „dobu dodání“, která určuje počet dní.
obvykle je dodavatel produktu povinen doručit zboží kupujícímu.

Pro dodávky poddodavatelských produktů lze konfigurovat časové období pro dodání s ohledem na
Čas potřebný pro výrobu produktu dodavatelem.
snažit se lépe předvídat termíny dodání poddodavatelských produktů.

.. důležité::
Stejně jako všechny časy dodání v Odoo jsou i časové údaje o předpokládaném termínu dodání pouze odhadem.
podle doby, kterou se očekává, že budou trvat.

Nepředvídatelné okolnosti mohou ovlivnit dokončení těchto akcí, což znamená, že se termíny
Není třeba je brát jako zaručení.

Konfigurace
=============

Při použití základního postupu výroby podle :doc:`<subcontracting_basic>`,
firma není zodpovědná za dodání potřebných součástek poddodavateli.
To znamená, že jedinými faktory ovlivňujícími datum dodání produktu jsou časové náklady
subdodavatele, který by ji vyrobil a dodal.

Při přidělování dodavatelům poddodavatelů termínu dodání, který zohledňuje oba tyto faktory.
Datum „Očekávaného příjezdu“ zobrazené na nákupních objednávkách (NO) pro produkt je přesnější.
zahrnuje dobu potřebnou jak pro výrobu, tak i pro dodání.

Doba dodání produktu
--------------------------

Pro nastavení dodací lhůty pro poddodavatele produktu přejděte na:
--> Produkty --> Produkty“, vyberte produkt, který chcete podřídit.

Vyberte záložku „Nákup“ na stránce produktu. Pokud dodavatel ne
už byly přidány jako dodavatelé, tak je nyní přidejte kliknutím na tlačítko „Přidat řádek“ a vyberte
subdodavatel v sloupci „Dodavatel“.

Jakmile je dodavatel doplněn, zadejte počet dní potřebných k výrobě.
dodat produkt v sloupci „Čas dodání“.

.. obrázek: základní dodací lhůty/doba dodání.png
:align:center
:alt:Čas dodání pro poddodavatele na kartě Nákup produktu.

.. poznámka::
Do záložky „Nákup“ na stránce produktu lze přidat více poddodavatelů.
různé: „Čas dodání“ lze pro každou nastavit jinak.

Průběh práce s časovým předstihem
==================

Po nastavení dodací lhůty pro dodavatele produktu vytvořte poptávku
Vyberte položku „Nákupní aplikace“ -> „Objednávky“ -> „Obchodní objednávky“ a klikněte na „Nový“.

Uveďte dodavatele do pole „Dodavatel“ a pak přidejte produkt v
Klikněte na záložku „Produkty“ a klikněte na tlačítko „Přidat produkt“, vyberte produkt v
Sloupci „Produkt“ a „Množství“.

Jakmile je produkt přidán, pole „Očekávaný příjezd“ na stránce RfQ se automaticky vyplní.
S datem, které odráží dodací lhůtu prodejce, jak je uvedeno na stránce produktu.

Pokud je potřeba datum upravit, klikněte na pole „Očekávaný příjezd“ pro otevření kalendáře.
pop-up okno, vyberte požadovaný den a ujistěte se, že nevyberete datum dřívější než je ten, který byl
automaticky vyplněné, pokud dodavatel nepotvrdil, že je schopen dodat produkt do
Tento den.

Konečně klikněte na tlačítko „Potvrdit objednávku“ v RFQ a převeďte ji do PO. V tomto bodě je
Subdodavatel by měl začít s výrobou předmětu podsmlouvy ještě před jeho dodáním.
stavební firma.

Příklad:
Prodejce kol Mike's Bikes spolupracuje s poddodavatelem - společností Bike Friends - na výrobě jednotek
jejich produkt Tricycle.

Průměrně potřebuje tým Bikers for Goods k výrobě tříkolek tři dny, další dva pak na montáž.
dnů, aby ho doručil do Mike's Bikes.

Mike’s Bikes stanovil dodací lhůtu pro tříkolky vyrobené firmou Schwinn na pět dní.
Bike Friends: tři dny na výrobu a dva dny na dodání.

Mike's Bikes potvrdil nákup jednoho tříkolového kola od Bike Friends 3. května.

Datum „Očekávaného příjezdu“ uvedený na |PO| je 8. května, pět dní po datu
:guilabel:`Datum potvrzení“.

.... obrázek: basic_subcontracting_lead_times/expected-arrival.png
:srovnání: do středu
:alt: Datum očekávaného příjezdu na objednávku pro poddodavatelský výrobek.

Bike Friends začne s výrobou tříkolky 3. května – den, kdy je potvrzeno PO
a skončí 6. května, tedy o tři dny později.

Poté je tříkolka dopravena do obchodu Mike's Bikes stejný den a přijde jim 8. května, dvě
O dva týdny později.
