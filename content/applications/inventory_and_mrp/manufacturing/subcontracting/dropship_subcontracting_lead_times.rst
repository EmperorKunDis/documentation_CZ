==================================
Doba dodání při poddodavatelských službách dropshipping
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

V případě dodání komponentů k poddodavateli je nutné připočítat další čas na dodání.
Může být nastaven pro každou složku. Toto by mělo být nastaveno na dobu, po kterou trvá dodavateli
dodat součástky dodavatelům.

Jakmile je stanovena doba dodání komponenty, objednávky zboží na skladě ukazují
termínem do kterého musí být objednávka potvrzena, aby mohla být zboží dodáno poddodavateli.
datum, kdy musí výroba začít.

.. důležité::
Stejně jako všechny časy dodání v Odoo jsou i časové údaje o předpokládaném termínu dodání pouze odhadem.
podle doby, kterou se očekává, že budou trvat.

Nepředvídatelné okolnosti mohou ovlivnit dokončení těchto akcí, což znamená, že se termíny
Není třeba je brát jako zaručení.

Konfigurace
=============

Při použití cesty „Subdodavatel na objednávku“ (<subcontracting_dropship>) se společnost
odpovědný za nákup potřebných komponent od dodavatele a jejich přepravu
přímo na poddodavatele.

To znamená, že kromě doby potřebné k výrobě a
dodat produkt, je také nutné zvážit, jak dlouho trvá dodavatel komponentu
doručí díly dodavateli, který je následně sestaví.

Přiřazením dodavatele podřízeného výrobku (subdodavatele) dobu dodání, s uvedením času výroby
časem na seznamu materiálů (BoM) výrobku a přidělením dodavatele komponent další dodací lhůtu.
*Čas*, *Příjemce poddodavatelské služby pro komponenty produktu* zobrazuje datum
potvrzení objednávky na přepravu součástek k dodavateli.

Doba dodání produktu
--------------------------

Chcete-li nastavit dodací lhůtu pro poddodavatele produktu, přejděte na:
Produkty --> Produkty, vyberte poddodavatelský produkt.

Vyberte záložku „Nákup“ na stránce produktu. Pokud dodavatel ne
už byly přidány jako dodavatelé, tak je nyní přidejte kliknutím na tlačítko „Přidat řádek“ a vyberte
subdodavatel v sloupci „Dodavatel“.

Jakmile je dodavatel doplněn, zadejte počet dní potřebných k výrobě.
dodat produkt v sloupci „Čas dodání“.

.. obrázek: dropship_subcontracting_lead_times/delivery-lead-time.png
:align:center
:alt:Čas dodání pro poddodavatele na kartě Nákup produktu.

Doba dodání výrobku
-------------------------------

Dále přejděte na produkt pomocí tlačítka „Seznam materiálů“ (smart button)
nahoře na stránce produktu. Pak vyberte BoM z seznamu.

Na BoM vyberte záložku „Různé“. V poli „Čas dodání“ zadejte
zadat stejný počet dnů, jako byl zadán do pole „Čas dodání“ v poli
Produkt BoM.

.. obrázek: dropship_subcontracting_lead_times/manufacturing-lead-time.png
:align:center
:alt:Časová prodleva výroby na kartě produktu v BOM.

Některé z těchto dnů skutečně využívá dodavatel k výrobě, ale
Stejný počet dnů v každém poli říká Odoo, že dodavatelé musí přijmout součástky a
začít s výrobou před začátkem dodací lhůty produktu. To dává poddodavateli
Dost času na výrobu i dodání produktu.

Doba dodání komponent
----------------------------

Z produktu BoM přejděte na každou součástku kliknutím na součástku v
kartě „Součásti“ a poté kliknutím na ikonu „pravý směr“
tlačítko vpravo od komponenty.

Na stránce produktu každé součásti vyberte záložku „Nákup“. Pokud dodavatel ne
už byly přidány, tak je nyní přidejte kliknutím na tlačítko „Přidat řádek“ a vyberte poddodavatele
sloupec Výrobce.

Jakmile dodavatele přidáte, zadejte počet dní potřebných k tomu, aby produkt dodal.
subdodavatel v sloupci „Čas dodání“.

Dropshippingový pracovní postup
================================

Vytvořte poptávku na produkt kliknutím na:menu-selection:"Nákupní aplikace
-->Objednávky --> Nabídka cen“, a klikněte na „Nový“.

Do pole Výrobce zadejte dodavatele a pak přidejte produkt do
Klikněte na záložku „Produkty“ a klikněte na tlačítko „Přidat produkt“, vyberte produkt v
Sloupci „Produkt“ a „Množství“.

Do pole „Očekávaný příjezd“ zadejte datum, které poskytuje dostatek času pro komponentu
dodavatel dodá komponenty a poddodavatel je vyrobí a dodá konečnému zákazníkovi.

.. důležité::
Když je produkt přidán do |RfQ|, pole „Očekávaný příjezd“ se automaticky vyplní.
datum, které je dnes a doba dodání produktu.
zvažte dobu, kterou trvá doručení komponentů dodavateli.

Při nákupu produktů zadaných v objednávce prostřednictvím cesty *Dropship Subcontractor on Order*
je nutné tento termín upravit tak, aby do něj byl započítán i čas potřebný na dodání komponent.
doručena poddodavateli.

Výroba totiž začíná až po dodání komponentů, takže nechávají datum beze změny.
v hotovém výrobku, který dorazí po datu uvedeném v |RfQ|.

Dále klikněte na „Potvrdit objednávku“, čímž se |RfQ| změní na |PO|. Tím vytvoříte druhý |RfQ|
koupit komponenty od dodavatele na skladě a nechat je poslat k poddodavateli.

Nastavte se na:menu:zakoupení aplikace --> objednávky --> poptávky a vyberte
Seznam RfQ, který uvádí dodavatele v sloupci Vendor.

V poli „Očekávaný příjezd“ na RfQ je uveden datum, kdy musí dodavatel splnit
přijmout komponenty, aby dodali hotový výrobek do data očekávaného příjezdu.
v seznamu poddodavatelů |PO|.

V poli „Deadline for Order“ je uveden nejpozdější termín pro potvrzení |RfQ|.
objednávka pro dodavatele komponentů, aby je předal poddodavateli do:guilabel:`Očekávané
Datum příjezdu.

Klikněte na tlačítko „Potvrdit objednávku“, aby se z RFQ stal PO, a potvrďte nákup
komponenty od dodavatele zboží. To způsobí, že se objeví tlačítko „Dropship“
nahoře na stránce.

Klikněte na tlačítko „Dropship“ a otevřete si objednávku zboží na skladě. Tato objednávka může být také
přístupná z tlačítka „Dodávky“ v podmenu „Subdodavatelé“ (PO).

Po dodání komponentů od zprostředkovatele k poddodavateli je potřeba kliknout na
Tlačítko „Potvrdit“ v horní části objednávky zboží na skladě, aby se potvrdilo, že dodavatel
obdrželi komponenty.

Jakmile dodavatel obdrží součástky, začíná s jejich výrobou.
Dodání do smluvní společnosti.

Příklad:

Prodejce kol Mike's Bikes spolupracuje s poddodavatelem - společností Bike Friends - na výrobě jednotek
jejich produktem Bicycle.

Mike's Bikes musí zakoupit požadované součástky u dodavatele Bike World a nechat si je namontovat.
zasílána na sklad Bike Friends.

Průměrně trvá výroba kola od Bike Friends tři dny a další dva dny na montáž.
aby doručil kolo do Mike's Bikes.

Mike’s Bikes stanovil termín dodání na pět dní pro kola vyrobená firmou Bike.
Přátelé: tři dny na výrobu a dva dny na dodání.

Na kartě BoM kola zadávají dobu výroby pět dní, aby si to lidé připomněli.
sami si určují datum, kdy musí komponenty dodat poddodavateli.

Na stránkách produktů pro každou ze součástí kola jim přiděluje Bike World vedení dodavatele.
2 dny. To je doba, kterou potřebuje společnost Bike World na dodání každé součásti
přímo na poddodavatele.

Mike’s Bikes potvrdil objednávku na jedno kolo dne 10. května s očekávaným datem dodání v květnu.
17.

Řízení výběru dodavatele (RfQ) na nákup komponentů od Bike World a jejich přepravu do Bike
Friends má očekávaný datum příjezdu 12. května a termín pro podání nabídky 10. května.
potvrzeno do termínu, aby Bike Friends mohli komponenty obdržet v očekávaném termínu.
Datum příjezdu, kdy mají dostatek času na dodání hotového kola do Mike's Bikes do května
17.

.... obrázek:: dropship_subcontracting_lead_times/termín-dodání.png
:srovnání: do středu
:alt:Termín dodání a očekávaný termín příjezdu u objednávky s přepravou na dobírku.

Mike’s Bikes potvrdí RfQ 10. května a Bike World dodá komponenty do Bike
12. května. Kola vyrábí firma Bike Friends a dodává je do Mike's Bikes.
17. května.
