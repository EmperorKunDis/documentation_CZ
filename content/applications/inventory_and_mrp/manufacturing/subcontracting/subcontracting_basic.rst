====================
Základní poddodavatelství
====================

.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`
.. |PO| nahradit za: :abbr:`PO (Příkaz k nákupu)`
.. |POs| nahradit za: zkratka: `POs (Purchase Orders)`
.. |BoM| nahradit za: :abbr:`BoM (Seznam materiálů pro výrobu)“

Výrobní proces outsourcingu je proces, kdy společnost najímá třetí stranu k výrobě.
subdodavatele, který vyrábí produkty, které jsou následně prodávány firmou zadavatelem.

V základním poddodavatelství je zadavatel odpovědný za zajištění potřebných komponentů.
To znamená, že smluvní společnost se musí starat pouze o to, co se stane s poddodavatelem.
produkty, jakmile jsou vyrobeny.

Průběh nákupu výrobku vyrobeného pomocí základního dodavatelského procesu je podobný jako
používá se při nákupu produktu od dodavatele, který neposkytuje subdodávky. Hlavní rozdíly jsou v tom
Jak jsou konfigurovány produkty dodavatelů a že dodané produkty trvají déle.
musí být nejprve vyrobeny dodavatelem.

Konfigurace
=============

Pro použití poddodavatelů v Odoo přejděte na: „Výroba -> Konfigurace“.
Nastavení“, zaškrtněte políčko vedle „Dodavatelé“ v nastavení
Poté klikněte na „Uložit“.

Jakmile je zapnuto nastavení „Dodavatelské práce“, je také nutné správně nakonfigurovat
poddodavatelský produkt a produkt BoM.

.. výroba/průběh výroby/dodavatelé/základní/konfigurace produktu:

Nastavit produkt
-----------------

Pro konfiguraci produktu pro základní poddodavatelskou činnost přejděte na:
Produkty --> Produkty“, vyberte produkt nebo vytvořte nový kliknutím na „Nový“.

V poli „Forma produktu“ vyberte záložku „Nákup“, přidejte do ní dodavatele produktu jako
Zvolit v seznamu dodavatelů položku „Přidat řádek“ a vybrat si poddodavatele.
položce „Cena“ v poli „Cena“.

Poté klikněte na záložku „Sklad“, vyberte pole „Trasy“ a nakonfigurujte
trasy, která určuje, co se s hotovým výrobkem stane po jeho vyrobení.
subdodavatel.

Pokud je hotový výrobek zasílán zpět do smluvní společnosti, ujistěte se, že je označen štítkem „Koupit“.
zvolí se trasa a dále trasa „Dodání na objednávku (MTO)“.
automaticky vytvoří |PO| pro produkt při potvrzení objednávky na prodej (SO), pokud není
Dostatečné zásoby na skladě, aby bylo možné uspokojit poptávku.

Pokud je hotový výrobek dodán přímo zákazníkovi poddodavatelem, zajistěte
Vybírá se pouze trasa Dropship.

Nastavte BoM
-------------

Pro konfiguraci základního dodavatelského řetězce klikněte na tlačítko „Seznam materiálů“
v produktové formě a vyberte požadované BoM.

Alternativně přejděte na:menu:„Výroba -> Produkty -> Seznamy materiálů“.
a vyberte |BoM| pro poddodavatelský produkt.

.. viz také:
Pro kompletní přehled konfigurace |BoM| se podívejte na :doc:`Seznam materiálů
dokumentaci k nastavení fakturace.

V poli „Typ“ vyberte možnost „Dodavatelské práce“. Poté přidejte jednu nebo více položek.
více poddodavatelů v poli „Dodavatelé“ pod tímto textem.

.. obrázek: subcontracting_basic/bom-type.png
:align:center
:alt:Pole „Typ“ na BOM, které je konfigurováno tak, aby produkt vyráběla pomocí dodavatelů.

Konečně klikněte na záložku „Různé“. V poli „Čas výroby“ zadejte
zadat počet dní, které trvá výroba produktu u poddodavatele. Tento čas je
při výpočtu očekávaného termínu dodání zboží.

.. poznámka::
Při použití základního poddodavatelství není nutné komponenty uvádět v
:guilabel:`Komponenty“ záložce v BoM, protože komponenty potřebné k výrobě a
Způsob získání a nakládání s nimi je na starost dodavatele.

Základní postup při poddodavatelské činnosti
=============================

Základní postup poddodavatelského procesu se skládá ze čtyř kroků:

#Vytvořte prodejní objednávku (SO) na dodaný produkt. Tím vznikne |PO| k nákupu
výrobek od dodavatele.
#Potvrďte |PO| vytvořený v předchozím kroku nebo vytvořte nový |PO|; tímto způsobem vznikne faktura.
objednávka nebo objednávka s přepravou na sklad.
#. Zpracujte fakturu po dokončení výroby poddodavatelem objednaného zboží
a dodal ji zpět do smluvní společnosti, nebo zpracoval objednávku na přepravu zboží.
produkt přímo zákazníkovi.
#Pokud byla práce zahájena vytvořením |SO| a dokončený produkt není zasílán přes
konečný zákazník, zpracují objednávku dodání po tom, co bude zboží odesláno zákazníkovi.

Specifická čísla kroků závisí na důvodu, proč je zakoupený produkt poddodavatele
od poddodavatele.

Pokud je důvodem splnění konkrétního zákaznického požadavku, proces začíná vytvořením SO.
končí dodáním produktu zákazníkovi nebo přesměrováním objednávky na externího dodavatele.

Pokud je důvodem zvýšení zásob na skladě, proces začíná vytvořením příkazu PO.
a končí přijetím produktu do zásoby.

Vytvořte SO
---------

Tento krok je nutný pouze v případě, že se produkt nakupuje u dodavatele.
uspokojit poptávku zákazníka. Pokud je produkt kupován za účelem zvýšení zásob
Pokud je vše připraveno, můžete pokračovat dál.

Vytvořit nové |SO|, přejděte na: „Prodejní aplikace - Objednávky - Objednávky“ a klikněte
:label:`Nový“.

Vyberte zákazníka v seznamu :guilabel:`Zákazník`. Pak klikněte na :guilabel:`Přidat
Vyberte produkt v poli „Dodavatelské produkty“ na kartě „Řádky objednávky“.
Vyberte možnost „Produkt“ v rozevíracím seznamu a zadejte množství do pole „Množství“.

Klikněte na „Potvrdit“ pro potvrzení objednávky. Po kliknutí se zobrazí tlačítko „Zaplatit“,
je umístěn na horní části stránky. To otevře PO vytvořené k nákupu poddodavatelského produktu
od poddodavatele.

.. poznámka::
Pouze pokud je povolená funkce „Dodání na objednávku“ (MTO), vytvoří objednávka pro produkt pouze poptávku.
forma výrobku a zároveň není dostatečné množství produktu na skladě k uspokojení poptávky.

Pokud je dostatek zásob skladem, potvrzení |SO| pro produkt vytvoří objednávku na dodání
Výchozí nastavení je takové, že Odoo předpokládá, že požadavek na dodání zboží bude vyřízen pomocí zásob skladu.

V případě zboží, které je dodáváno konečnému zákazníkovi prostřednictvím poddodavatelů, se však jedná o jinou situaci.
V případě, že je v objednávce zboží, které není skladem, vždy se vytvoří PO, i když je na skladě dostatek zásob.

Proces PO
----------

Pokud byl v předchozím kroku vytvořen |PO|, přejděte na něj klepnutím na „Nákup“.
chytře umístěný tlačítko na horní části obrazovky SO, nebo přejděte do: guilabel:Koupit aplikaci --> Objednávky --> Koupit
Poté vyberte možnost „Přijmout objednávku“ a klikněte na tlačítko „Potvrdit objednávku“, abyste ji potvrdili.
dalším krokem.

Pokud v předchozím kroku nebyl vytvořen |PO|, udělejte tak nyní tím, že se přesunete na:
app --> Objednávky --> Nákupní objednávky“, a klikněte na „Nový“.

Začněte vyplňovat PO, když si z nabídky Výrobce vyberete dodavatele.
V záložce „Produkty“ klikněte na „Přidat produkt“, abyste vytvořili novou řadu produktů.
Vyberte produkt dodavatele v poli „Produkt“ a zadejte množství v
Pole „Množství“. Nakonec klikněte na tlačítko „Potvrdit objednávku“, abyste potvrdili |PO|.

Při potvrzení |PO| pro výrobek vyrobený z poddodavatelských prací se vystavuje faktura nebo
Pokud je objednávka zboží na skladě, automaticky se vytvoří a může být přístupná prostřednictvím příslušného
Tlačítko „Potvrzení“ nebo „Doručení na sklad“ chytré tlačítko, které se objevuje nahoře v záložce |PO|.

.. obrázek:: subcontracting_basic/subcontractor-po.png
:align:center
:alt:PO pro základní poddodavatelský produkt s tlačítkem Smart Receipt na horní části stránky.

PO pro základní poddodavatelský produkt s tlačítkem Smart Receipt na začátku stránky.

Zpracování objednávky nebo příjem zboží
---------------------------------

Jakmile dodavatel dokončí výrobu produktu, buď jej odesílá přímo zákazníkovi
dodavatel nebo přepravce, v závislosti na tom, jaký je produkt.
:ref:`konfigurované <výroba/procesy/dodavatelské služby/základní/produkt-konfigurace>“.

Potvrzení o přijetí
~~~~~~~~~~~~~~~

Pokud poddodavatel dodá hotový výrobek konečnému zákazníkovi, jednou
přijaté, přejděte na: „Nákup aplikace -> Objednávky -> Nákupní objednávky“ a vyberte
|PO|.

Klikněte na tlačítko „Přijmout produkty“ v horní části stránky PO nebo na tlačítko „Potvrzení“.
Chytrý tlačítko na horní části stránky, které otevře fakturu. Pak klikněte na „Potvrdit“.
výpisu na vrcholu dokladu pro zadání produktů do skladu.

Proces objednávky přepravy na sklad
~~~~~~~~~~~~~~~~~~~~~~

Pokud dodavatelé zboží zasílají na dobírku, přejděte na
Vyberte možnost „Nákupní aplikace“ > „Objednávky“ > „Nákupní objednávky“.

V horní části stránky vyberte tlačítko „Dropship“ a
Klikněte na tlačítko „Potvrdit“ v horní části objednávky, abyste potvrdili, že produkt byl odeslán.
Zákazník.

Dodací objednávka
----------------------

Pokud byla pracovní postup pro poddodavatele zahájena zákazníkem |SO|, a pokud byl výsledný produkt
nejsou dodávány přímo zákazníkovi, ale spíše firmě, s níž má provozovatel uzavřenou smlouvu.
zboží odeslat zákazníkovi a zpracovat objednávku na dodání.

Jakmile je produkt odeslán zákazníkovi, přejděte do aplikace „Prodej“ a
Vyberte si |SO|. V horní části stránky vyberte tlačítko s názvem „Dodání“
dodací objednávku a klikněte na tlačítko „Potvrdit“ v objednávce, abyste potvrdili, že produkt byl
přepraveny.
