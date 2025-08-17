==================================
Dodací lhůty pro poddodavatelské dodávky
==================================

.. |PO| nahradit za: :abbr:`PO (Příkaz k nákupu)`
.. |RfQ| nahradit za: zkratku `RfQ (Request for Quotation)`
.. |BoM| nahradit za: :abbr:`BoM (Seznam materiálů pro výrobu)“

V Odoo jsou doby odezvy používány k předpovídání doby trvání určitého úkonu. Například
Pro zakoupený produkt lze nastavit „dobu dodání“, která určuje počet dní.
obvykle je na dodavateli, aby zboží doručil kupujícímu.

Pro dodávky poddodavatelských produktů lze konfigurovat časové období pro dodání s ohledem na
Čas potřebný pro výrobu produktu dodavatelem.
snažit se lépe předvídat termíny dodání poddodavatelských produktů.

Některé poddodavatelské produkty vyžadují, aby smluvní společnost dodala poddodavateli
výrobních komponentů. V tomto případě lze použít vedlejší čas výroby (manufacturing lead time),
doba dodání, abychom vygenerovali datum, kdy musí poddodavatel obdržet požadované
součástky, abychom vyráběli produkt a dodávali jej včas.

.. důležité::
Stejně jako všechny časy dodání v Odoo jsou i časové údaje o předpokládaném termínu dodání pouze odhadem.
podle doby, kterou se očekává, že budou trvat.

Nepředvídatelné okolnosti mohou ovlivnit dokončení těchto akcí, což znamená, že se termíny
Není možné je považovat za zaručení.

Konfigurace
=============

Při použití trasy „Dodavatel doplňkových služeb na objednávku“ podle dokumentu :doc:`Subcontracting Resupply <subcontracting_resupply>`, je
Zajišťuje dodávku potřebných komponent pro poddodavatele.
Subdodavatel nemůže začít s výrobou, dokud neobdrží součástky.

To znamená, že kromě doby potřebné k výrobě a
Dodat produkt, datum, kdy obdrží komponenty, musí být také zohledněno.

Přiřazením dodavatele polotovaru do termínu dodání a specifikací času výroby
čas na seznamu materiálů (BOM) pro produkt, objednávky *Dodavatel doplňkových dílů* pro produkt
komponenty zobrazují termín, do kterého musí dodavatel obdržet komponenty.

Doba dodání produktu
--------------------------

Pro nastavení dodací lhůty pro poddodavatele produktu přejděte na:
--> Produkty --> Produkty“, vyberte produkt, který chcete podřídit.

Vyberte záložku „Nákup“ na stránce produktu. Pokud dodavatel ne
už byly přidány jako dodavatelé, tak je nyní přidejte kliknutím na tlačítko „Přidat řádek“ a vyberte
subdodavatel v poli „Dodavatel“.

Jakmile je dodavatel doplněn, zadejte počet dní potřebných k výrobě.
dodat produkt v sloupci „Čas dodání“.

.. obrázek:resupply_subcontracting_lead_times/delivery-lead-time.png
:align:center
:alt:Čas dodání pro poddodavatele na kartě Nákup produktu.

Doba dodání výrobku
-------------------------------

Dále přejděte na produkt pomocí tlačítka „Seznam materiálů“ (smart button)
nahoře na stránce produktu. Pak vyberte z nabídky BoM.

Na BoM vyberte záložku „Různé“. V poli „Čas dodání“ zadejte
zadat stejný počet dnů, jako byl zadán do pole „Čas dodání“ v poli
Produkt BoM.

.. obrázek:resupply_subcontracting_lead_times/manufacturing-lead-time.png
:align:center
:alt:Časová prodleva výroby na kartě produktu v BOM.

Některé z těchto dnů skutečně využívá dodavatel k výrobě, ale
Stejný počet dnů v každém poli říká Odoo, že dodavatelé musí přijmout součástky a
začít s výrobou před začátkem dodací lhůty produktu. To dává poddodavateli
Dost času na výrobu i dodání produktu.

Práce s poddodavateli v rámci dodavatelského řetězce
--------------------------------

Vytvořte poptávku na produkt kliknutím na:menu-selection:"Nákupní aplikace
-->Objednávky --> Nabídka cen“, a klikněte na „Nový“.

Do pole Výrobce zadejte dodavatele a pak přidejte produkt do
Klikněte na záložku „Produkty“ a klikněte na tlačítko „Přidat produkt“, vyberte produkt v
Sloupci „Produkt“ a „Množství“.

Do pole „Očekávaný příjezd“ zadejte datum, které poskytuje dostatek času na
subdodavatelé, kteří obdrží komponenty, vyrobí produkt a dodají ho zpět.
subdodavatelská společnost.

.. důležité::
Když je produkt přidán do |RfQ|, pole „Očekávaný příjezd“ se automaticky vyplní.
datum, které je dnes datem zboží včetně dodací lhůty. Nicméně tento termín **neplatí**
Zvažte dobu, kterou trvá doprava komponentů k poddodavateli.

Při nákupu produktů poddodavatelsky objednaných pomocí cesty Objednávka na dodavatele Resupply je
je nutné tento termín upravit tak, aby do něj byl započítán i čas potřebný na dodání komponent.
dodány k poddodavateli.

Výroba totiž začíná až po dodání komponentů, takže nechávají datum beze změny.
v hotovém výrobku, který dorazí po datu uvedeném v |RfQ|.

Dále klikněte na „Potvrdit objednávku“, aby se RfQ změnil na PO. Toto způsobí
:guilabel:`Dodatečné zásoby“ chytrý tlačítko se objeví na horní části stránky.

Klikněte na tlačítko „Dodávka“ v seznamu chytrých tlačítek, abyste otevřeli objednávku dodavatele zásob, která je
přijatý příkaz k odeslání součástek do dodavatelské firmy.

V poli „Deadline“ objednávky na doplnění zásob je uveden termín pro dodání
dodavateli komponentů, aby měli dostatek času na výrobu a
doručit hotový výrobek do očekávaného termínu doručení.

V poli „Datum plánovaného termínu“ by měla být zobrazena nejnovější data, do kterých lze komponenty
a přesto doručena do subdodavatele v termínu. Výchozí hodnotou je
Datum zobrazené je stejné jako datum v poli „Termín“, a musí být aktualizováno na
Zohlednit dobu dodání.

Klikněte na pole „Datum“ a otevře se kalendářové okno, ve kterém lze vybrat datum.
vybrat datum, které umožní dodání komponent do data:guilabel:`Termín dodání`.
na objednávku zásobovacího poddodavatele.

Po odeslání komponent je třeba kliknout na tlačítko „Potvrdit“ v horní části objednávky.
potvrdí, že byly předány poddodavateli.

Jakmile dodavatel obdrží součástky, začíná s jejich výrobou.
Dodání do smluvní společnosti.

Příklad:
Prodejce kol Mike's Bikes spolupracuje s poddodavatelem - společností Bike Friends - na výrobě jednotek
jejich produkt Unicycle.

Mike's Bikes musí dodat Bike Friends potřebné komponenty pro výrobu.
univerzální kolo.

Průměrně trvá výroba každého kola tři dny.
dnů, aby ho doručil do Mike's Bikes.

Mike’s Bikes stanovil termín dodání pro jednokolky vyrobené firmou Kris Holm na pět dní.
Bike Friends: tři dny na výrobu a dva dny na dodání.

Na BoM koloběžky zadávají i čas na výrobu, který je pět dní.
sami si určují datum, kdy musí komponenty dodat poddodavateli.

Potvrzují jedno kolo pro jednoho cyklistu s očekávaným datem příjezdu 30. května.

Objednávka na dodání komponentů k poddodavateli ukazuje, že
*Termín* 25. května. Subdodavatel musí komponenty obdržet do tohoto data, aby je mohl
měli dostatek času na výrobu jednokolky a dodání do 30. května.

Mikeovi trvá dva dny, než doručí součástky, protože aktualizují datum *Plánované dodání*.
pole na objednávce dodavatele zásob pro termín do 23. května, tedy dva dny před termínem.

.... obrázek:resupply_subcontracting_lead_times/plánovaný termín.png
:srovnání: do středu
:alt:Datum a termín dodání na objednávce pro doplňování zásob u poddodavatele.

Mikeovi se podaří dodat komponenty do Bike Friends dne 23. května a ti
Dodávka by měla dorazit do konce května, což dává Bike Friendům dost času na výrobu
jednokolka a poslat ji zpět do Mike’s Bikes do očekávaného data doručení 30. května.
