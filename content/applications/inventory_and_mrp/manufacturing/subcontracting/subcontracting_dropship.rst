=========================
Dropshipping do poddodavatele
=========================

.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`
.. |SOs| nahradit za: zkratka: `SOs (Sales Orders)`
.. |PO| nahradit za: abbr: PO (objednávka)
.. |POs| nahradit za: zkratka: `POs (Purchase Orders)`
.. |RfQ| nahradit za: zkratku `RfQ (požadavek na nabídku)`
.. |BoM| nahradit za: :abbr:`BoM (Seznam materiálů pro výrobu)“

Výroba poddodavatelství je proces, kdy společnost najímá třetí stranu na výrobu.
subdodavatele, který vyrábí produkty, které jsou pak prodávány smluvní společností.

V Odoo se používá cesta *Dodavatel doplňkových dílů na objednávku*, která umožní nákup potřebných komponent
pro dodaný výrobek od dodavatele a nechat je doručit přímo k poddodavateli.
Každýkrát, když je potvrzena objednávka na tento produkt.

Dodavatel pak použije díly k výrobě požadovaného produktu a následně ho dodá.
do smluvní společnosti.

.. důležité:
Je nutné pochopit rozdíly mezi *Dropshippingem* a *Dropshippingovým subdodavatelem
Na objednávkových trasách. Obě trasy zahrnují přeposlání, ale jsou používány pro různé účely.

Řešení Dropship se používá k nákupu produktů u dodavatele a jejich přímé expedici.
přímo zákazníkovi.

Řešení Dropship Subcontractor on Order se používá k nákupu součástek od dodavatele.
Pokud je to možné, nechte dodavatele poslat hotové výrobky přímo k poddodavateli. Výchozí nastavení pak předpokládá, že hotové produkty jsou zasílány
subdodavatele zpět k zadavateli.

Ale je možné kombinovat oba typy *Dropship* a *Dropship Subcontractor on Order*.
trasy tak, aby se používaly pro stejný produkt. V tomto procesu jsou komponenty dodávány na sklad
poddodavatel, který pak dodává hotový výrobek přímo konečnému zákazníkovi.

Aby se toho dosáhlo, je třeba postupovat podle kroků jedna až pět v části :ref:`workflow
<výroba/procesy/dodavatelé/drop-shipping> této dokumentace.

Konfigurace
=============

Pro použití cesty *Dropship Subcontractor on Order* přejděte na: menu: „Aplikace pro výrobu
Konfigurace -> Nastavení, zaškrtněte políčko vedle „Dodavatelé“ v části
:guilabel:„Provádění“

Jakmile je zapnutá volba „Dodavatelské subdodávky“, je také nutné správně nakonfigurovat
subdodavatelský produkt, produkt BoM a komponenty uvedené na BoM.

Nastavit produkt
-----------------

Pro konfiguraci produktu pro cestu *Dropship Subcontractor on Order* přejděte na
:menuvolba:„Aplikace pro inventář“ -> „Produkty“ -> „Produkty“, nebo vytvořte nový produkt
kliknutím na tlačítko „Nový“.

Vyberte záložku „Nákup“ a přidejte dodavatele výrobku jako dodavatele kliknutím
:guilabel:`Přidat řádek“, vybrat dodavatele v rozevíracím seznamu „Dodavatel“ a
Zadáním ceny do pole :guilabel:`Cena`.

Poté klikněte na záložku „Sklad“ a konfigurujte trasu, která určuje, co se stane
hotový výrobek, který byl vyroben dodavatelem.

Pokud je hotový výrobek vrácen zpět do smluvní společnosti, ujistěte se, že
Vyberte cestu „Koupit“ a také vyberte „Dodání na objednávku (MTO)“.
cestu automaticky vytvořit |PO| pro produkt po potvrzení |SO|, pokud není
Dostatek zásob, které pokryjí poptávku.

Pokud je hotový výrobek dodán přímo zákazníkovi poddodavatelem, zkontrolujte
Je vybrána pouze trasa Dropship.

Nastavte seznam materiálů
---------------------------

Pro konfiguraci |BoM| pro trasu „Subdodavatel na objednávku“ klikněte na tlačítko :guilabel:`Faktura.
Tlačítko „Chytrý materiál“ na stránce produktu a vyberte |BoM|.

Alternativně přejděte na: „Výrobní aplikace -> Produkty -> Seznamy materiálů“.
a vyberte |BoM| pro poddodavatelský produkt.

.. viz též:
Pro kompletní přehled konfigurace |BoM| se podívejte na :doc:`Seznam materiálů
dokumentaci k nastavení fakturace v části „Základní konfigurace“

V poli „Typ“ vyberte možnost „Dodavatelské práce“. Poté přidejte jednu nebo více položek.
více poddodavatelů v poli „Dodavatelé“ (viz obrázek níže).

.. obrázek: subcontracting_dropship/bom-type.png
:align:center
:alt:Pole „Typ BoM“ na BoM, které je nastaveno tak, aby produkt vyrábělo prostřednictvím subdodavatelů.

Zkontrolujte také, zda jsou všechny potřebné komponenty uvedeny na záložce „Komponenty“.
Přidat nový komponent, kliknout na „Přidat řádek“, vybrat komponentu v „Komponenta“
klikněte na tlačítko „Drop-Down Menu“ a zadejte požadované množství v poli „Množství“.

Konfigurace komponent
--------------------

Pro konfiguraci komponent pro cestu *Dropship Subcontractor on Order* přejděte do každé komponenty
z |BoM| vybráním názvu komponenty v záložce „Komponenty“ a kliknutím na
:guilabel:`➡️ (pravý směr)` tlačítko vedle jména.

Alternativně se můžete dostat k jednotlivým komponentám přes tlačítko „Vybavení aplikace“ - „Produkty“.
Produkty“ a vyberte komponentu.

V seznamu produktů vyberte záložku „Nákup“ a přidejte dodavatele kliknutím na
:guilabel:`Přidejte řádek“, vyberte dodavatele v poli „Dodavatel“ a přidejte cenu
Tento produkt prodávají v poli „Cena“ a tato firma dodává komponenty
subdodavateli, jakmile je koupíte.

Pak klikněte na záložku „Sklad“ a vyberte možnost „Subdodavatel dropshippingu“.
Zadejte trasu v sekci „Trasy“.

Opakujte proces pro každou součástku, která musí být dodána poddodavateli.

... výroba/procesy/dodavatelé/zásilkový prodej:

Dodavatel dropshippingu na procesech objednávky
========================================

Dodavatelé na objednávku se skládají z až šesti kroků:

#Vytvořte prodejní objednávku (SO) na dodaný produkt. Tím vznikne *dodavatel*
aby si produkt od poddodavatele zakoupil.
#Potvrďte PO vytvořený v předchozím kroku nebo vytvořte nový PO. Takto vznikne požadavek
pro citaci (RfQ) k nákupu komponent od dodavatele, stejně jako příkaz nebo objednávku na přijetí.
objednávka zboží na skladě.
#Potvrďte RFQ, aby se z něj stal druhý PO (dodavatelský PO); takto vznikne dropshipping.
Příkaz pro subdodavatele*.
#. Zpracujte objednávku *Dropship Subcontractor* poté, co dodavatel poslal komponenty na
poddodavatel.
#. Zpracujte fakturu až po dokončení výroby poddodavatelem objednaného zboží.
a odeslat ji zpět do smluvní společnosti **nebo** zpracovat objednávku na přepravu zboží.
produkt přímo koncovému zákazníkovi.
#Pokud byla práce zahájena vytvořením |SO| a dokončený produkt nebyl dodán
předáme zboží přímo zákazníkovi a zpracujeme objednávku až po dodání zboží zákazníkovi.

Konkrétní počet kroků závisí na důvodu, proč je zakoupený produkt poddodavatele
od dodavatele.

Pokud je důvodem splnění konkrétního zákaznického požadavku, proces začíná vytvořením objednávky SO.
končí dodáním produktu zákazníkovi nebo přesměrováním objednávky na externího dodavatele.

Pokud je důvodem zvýšení zásob na skladě, proces začíná vytvořením objednávky.
končí přijetím produktu do zásob.

Vytvořte SO
------------

Tento krok je nutný pouze v případě, že se produkt nakupuje u dodavatele.
uspokojit poptávku zákazníka. Pokud je produkt kupován za účelem zvýšení zásob
Pokud je k dispozici, přejděte na další krok.

Vytvořit nový |SO|. Přejděte na: „Prodejní aplikace -> Objednávky -> Objednávky“ a klikněte
:guilabel:`Nový“.

Vyberte zákazníka v seznamu :guilabel:`Zákazník`. Pak klikněte na :guilabel:`Přidat
Vyberte produkt v poli „Produkty“ na kartě „Řádky objednávky“.
menu a zadejte množství do pole :guilabel:`Množství`.

Klikněte na tlačítko „Potvrdit“ pro potvrzení objednávky. Poté se vám zobrazí tlačítko „Dokončit nákup“.
je umístěn na začátku stránky. Jedná se o poddodavatele |PO| nebo o |PO| vytvořený pro nákup
výrobek dodaný od poddodavatele.

.. poznámka::
Pouze pokud je pro výrobek nastaveno |SO|, vytváří se *dodavatelský subdodavatel* |PO*, pokud je nastaveno |MTO*.
Pokud je možnost dopravy zobrazena na stránce produktu a zároveň není skladem žádný kus tohoto produktu.

Pokud je zboží skladem, potvrzení |SO| pro produkt místo vytvoří dodávku
pokynu, protože Odoo předpokládá, že |SO| bude splněno pomocí zásob skladu.

V případě, že se jedná o zboží dodávané přes distributora konečnému zákazníkovi, není možné vracet zboží.
Případně je vytvořen subdodavatel |PO|, i když má dodavatel zásoby skladem.

Smluvní partner procesu PO
------------------------

Pokud v předchozím kroku nebyl vytvořen poddodavatel, tak jej nyní vytvořte přesunutím se na
Vyberte „Nákupní aplikace“ > „Objednávky“ > „Nákupní objednávky“, a poté klikněte na „Nový“.

Začněte vyplňovat PO, když zvolíte dodavatele ze seznamu v rozevíracím seznamu Vendor.

V záložce „Produkty“ klikněte na „Přidat produkt“, abyste vytvořili novou řadu produktů.
Vyberte produkt dodavatele v poli „Produkt“ a zadejte
množství v poli „Množství“.

Nakonec klikněte na tlačítko „Potvrdit objednávku“, abyste potvrdili *dodavatele* |PO|.

Pokud je potvrzena objednávka pro produkt vyžadující komponenty k přeposlání dodavateli,
Pokladní doklad nebo objednávka na zaslání zboží je automaticky vytvořen a lze jej přistupovat k prostřednictvím odpovídajícího
Tlačítko „Pokladní doklad“ nebo „Dodání na sklad“ chytré tlačítko, které se objeví v horní části |PO|.

.. obrázek: subcontracting_dropship/subcontractor-po.png
:align:center
:alt:Subdodavatel PO pro produkt Dropship Subcontractor on Order s příjmovou chytrou
tlačítko v horní části stránky.

Dále je vytvářen |RfQ| pro komponenty, které jsou nakoupeny od dodavatele a zaslány
poddodavatele. Nicméně poptávka není automaticky propojena s poddodavatelem.

Jakmile je |RfQ| potvrzena a stává se dodavatelem |PO|, objednávka *Dropship Subcontractor*
vytvořen. Tento příkaz je spojen jak s dodavatelem, tak i s poddodavatelem.

Potvrdit dodavatele RfQ
------------------

Chcete-li se dostat k RfQ vytvořenému potvrzením subdodavatele PO, přejděte na
:menu:Koupit aplikaci --> Objednávky --> Nabídky. Vyberte nabídku, která obsahuje
správného dodavatele do pole „Dodavatel“ a číslo faktury, na kterou byla vystavena
Vytvořené po potvrzení poddodavatele v poli „Zdrojový dokument“ ve sloupci „Poddodavatel“.

V poli „K dodání“ na RfQ je uvedeno „Subdodavatel“, a
Pole „Adresa pro dropshipping“ zobrazuje jméno poddodavatele, kterému jsou komponenty dodávány.
dropshipping.

Klikněte na tlačítko „Potvrdit objednávku“ a převeďte |RfQ| na poptávku od dodavatele a potvrďte nákup.
komponenty od dodavatele. Po provedení takového kroku se v horním panelu objeví tlačítko „Dropship“
od dodavatele *PO*, a tlačítko „Doplnění zásob“ se objeví na horní části
*dodavatel prací* |PO|.

.. obrázek::subcontracting_dropship/vendor-po.png
:align:center
:alt:Prodejce PO pro komponenty produktu *Dropship Subcontractor on Order*, s
Klikněte na tlačítko Dropship nahoře na stránce.

Objednávka zpracování objednávek subdodavatele
------------------------------------

Jakmile jsou komponenty dodány poddodavateli, přejděte na:
app --> Objednávky --> Nákupní objednávky“ a vyberte „Dodavatel“ nebo „Subdodavatele“. Pak
Klikněte na tlačítko „Dropship“ nebo „Resupply“, podle toho, jaký z nich chcete použít.

Kliknutím na kteroukoli z těchto dvou možností se otevře objednávka *Zpracovatel poddodavatelské služby*. Klikněte na :guilabel:`Přezkoumat`
tlačítko na vrcholu objednávky, které potvrdí, že dodavatel obdržel součásti.

Přijmout objednávku nebo zadat objednávku na dodání
---------------------------------

Jakmile dodavatel dokončí výrobu hotového produktu, přejděte na: „Nákup
app --> Objednávky --> Nákupní objednávky“ a vyberte „Subdodavatel“ |PO|.

Pokud má být dodaný produkt přijat do zásob, po příjezdu produktu klikněte na
Tlačítko „Přijmout produkty“ v horní části stránky subdodavatele (PO) otevře fakturu.
Poté klikněte na tlačítko „Zkontrolovat“ v horní části faktury a zaregistrujte produkt do zásob.

Alternativně vyberte v horní části stránky subdodavatele (PO) tlačítko „Potvrzení“.
a klikněte na „Potvrdit“ v horní části faktury.

Pokud má být dodavatelský produkt přeposlán, vyberte tlačítko „Dropship“ v
nahoru na stránku pro otevření objednávky zboží na skladě a klikněte na tlačítko „Potvrdit“.
Produkt odeslal zákazníkovi.

Dodání procesního příkazu
----------------------

Pokud byla práce na poddodavatelské úrovni zahájena zákazníkem |SO|, a hotový výrobek nebyl
přeposlány zákazníkovi, ale dodány do smluvní firmy, je nutné
doručit produkt zákazníkovi a zpracovat objednávku na dodání.

Jakmile je produkt odeslán zákazníkovi, přejděte do aplikace „Prodej“ a
Vyberte si |SO|. V horní části stránky vyberte tlačítko „Dodání“
doručovací lístek a klikněte na tlačítko „Potvrdit“ potvrďte, že produkt byl odeslán.
zákazník.
