======================
Dodavatel doplňkových služeb
======================

.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`
.. |PO| nahradit za: abbr: PO (objednávka)
.. |POs| nahradí:: :abbr:`PO (Nákupní objednávky)`
.. |BoM| nahradit za: :abbr:`BoM (Seznam materiálů pro výrobu)“

Výroba poddodavatelství je proces, kdy společnost najímá třetí stranu na výrobu.
subdodavatele, který vyrábí produkty, které jsou pak prodávány smluvní společností.

V Odoo se používá trasa *Dodavatel doplňkových dílů na objednávku*, která dodává potřebné komponenty pro
produktu poddodavateli, pokaždé když je vydána objednávka na tento produkt
potvrzeno.

Dodavatel pak použije díly k výrobě požadovaného produktu a následně ho dodá.
do smluvní společnosti nebo konečnému zákazníkovi.

.. důležité:
Je nutné pochopit rozdíl mezi *Dodavatelem doplňkových služeb na objednávku* a
trasy *Dropship Subcontractor on Order*.

Oba směry jsou používány k dodání komponent potřebných pro poddodavatele.
Výroba produktu se liší v tom, jak jsou komponenty získávány.

Při použití funkce „Dodavatel doplňkových komponent na objednávku“ jsou součástky dodány z skladu
stavební firma.

Při použití funkce „Subdodavatel na objednávku“ se komponenty kupují u dodavatele a jsou odeslány
přímo na poddodavatele.

Volba trasy závisí na konkrétních požadavcích poddodavatelů.
společnost a její dodavatelé.

Podrobnější informace o *Dropshipu* naleznete v dokumentaci :doc:`subcontracting_dropship`.
Subdodavatel na objednávce*.

Konfigurace
=============

Pro použití cesty „Dodavatel doplňkových materiálů na objednávku“ přejděte na: menu:„Výrobní aplikace
Konfigurace -> Nastavení, zaškrtněte políčko vedle „Dodavatelé“ v části
:guilabel:„Provádění“

Jakmile je zapnutá volba „Dodavatelské subdodávky“, je také nutné správně nakonfigurovat
dodavatelský produkt, seznam součástek (BOM) a komponenty uvedené na
BOM).

… výroba / workflowy / dodavatelé / zásoby / konfigurace produktů:

Nastavit produkt
-----------------

Pro konfiguraci produktu na cestě *Dodavatelé na objednávku* přejděte do
:menuvolba:„Aplikace pro inventář“ -> „Produkty“ -> „Produkty“, nebo vytvořte nový produkt
kliknutím na tlačítko „Nový“.

Vyberte záložku „Nákup“ a přidejte dodavatele výrobku jako dodavatele kliknutím
:guilabel:`Přidat řádek“, vybrat dodavatele v rozevíracím seznamu „Dodavatel“ a
Zadáním ceny do pole :guilabel:`Cena`.

.. poznámka::
Hodnota zadaná do pole Cena na kartě Nákup v poli Příjem.
Stránka produktu, který je vyrobený na zakázku, uvádí částku zaplacenou poddodavateli za výrobu.
produktu.

To však nezahrnuje celkové náklady na výrobek, které zahrnují další prvky, jako jsou
náklady na komponenty výrobku.

Poté klikněte na záložku „Sklad“ a konfigurujte trasu, která určuje, co se stane
hotový výrobek, který byl vyroben dodavatelem.

Pokud je hotový výrobek vrácen zpět do smluvní společnosti, ujistěte se, že
Vyberte cestu „Koupit“ a také vyberte „Dodání na objednávku (MTO)“.
cestu, která automaticky vytvoří |PO| pro produkt při potvrzení objednávky (SO), pokud
Dodavatelé mají dostatek zásob, aby uspokojili poptávku.

Pokud je hotový výrobek dodán přímo zákazníkovi poddodavatelem, zkontrolujte
Je vybrána pouze trasa Dropship.

Nastavte BoM
-------------

Chcete-li nakonfigurovat |BoM| pro cestu *Dodavatel na objednávku*, klikněte na tlačítko
Tlačítko „Chytrý materiál“ na stránce produktu a vyberte |BoM|.

Alternativně přejděte na: „Výrobní aplikace -> Produkty -> Seznamy materiálů“.
a vyberte |BoM| pro poddodavatelský produkt.

.. viz též:
Pro kompletní přehled konfigurace |BoM| se podívejte na :doc:`Seznam materiálů
dokumentaci k nastavení fakturace v části „Základní konfigurace“

V poli „Typ“ vyberte možnost „Dodavatelské práce“. Poté přidejte jednu nebo více položek.
více poddodavatelů v poli „Dodavatelé“ (viz obrázek níže).

.. obrázek:subcontracting_resupply/bom-type.png
:align:center
:alt:Pole „Typ BoM“ na BoM, které je nastaveno tak, aby produkt vyrábělo prostřednictvím subdodavatelů.

Zkontrolujte také, zda jsou všechny potřebné komponenty uvedeny na záložce „Komponenty“.
Přidat nový komponent, kliknout na „Přidat řádek“, vybrat komponentu v „Komponenta“
klikněte na tlačítko „Drop-Down Menu“ a zadejte požadované množství v poli „Množství“.

Konfigurace komponent
--------------------

Chcete-li nakonfigurovat komponenty pro trasu „Dodavatel zásobování na objednávku“, přejděte do každé komponenty
z |BoM| vybráním názvu komponenty v záložce „Komponenty“ a kliknutím na
:guilabel:`➡️ (pravý směr)` tlačítko vedle jména.

Alternativně se můžete dostat k jednotlivým komponentám přes tlačítko „Vybavení aplikace“ - „Produkty“.
Produkty“ a vyberte komponentu.

Na kartě složky produktu klikněte na záložku „Sklad“ a vyberte
„Dodavatel doplňkových služeb na objednávku“ v sekci „Trasy“.

Postup opakujte pro každý komponent, který musí být odeslán poddodavateli.

Dodavatel doplňkových služeb v rámci objednávky
========================================

Subdodavatel dodávky na objednávku se skládá z maximálně pěti kroků:

#Vytvořte SO pro poddodavatelský produkt. Tím vznikne PO na nákup produktu
od poddodavatele.
#Potvrďte |PO| vytvořený v předchozím kroku nebo vytvořte nový |PO|. To vytváří *Dodávka
Subdodavatelský* objednávkový formulář, stejně jako fakturační nebo zásilkový objednávkový formulář.
#Zpracujte objednávku „Dodavatel doplňkového materiálu“ jednou, když budou k dispozici komponenty pro dodávaný produkt.
byly předány dodavateli.
#. Zpracujte fakturu až po dokončení výroby poddodavatelem objednaného zboží.
a odeslat ji zpět do smluvní společnosti **nebo** zpracovat objednávku na přepravu zboží.
produkt přímo zákazníkovi.
#Pokud byla práce zahájena vytvořením |SO| a dokončený produkt nebyl dodán
konečný zákazník, zpracovat objednávku dodání až poté, co je zboží doručeno zákazníkovi.

Konkrétní počet kroků závisí na důvodu, proč je zakoupený produkt poddodavatele
od dodavatele.

Pokud je důvodem splnění konkrétního zákaznického požadavku, proces začíná vytvořením |SO|.
končí dodáním produktu zákazníkovi nebo přesměrováním objednávky na externího dodavatele.

Pokud je důvodem zvýšení zásob na skladě, proces začíná vytvořením položky PO.
a končí přijetím produktu do zásoby.

.. důležité:

Zásoby lze automaticky doplnit pomocí trasy *Dodavatel zásob na objednávku*.
poddodavatele po potvrzení |PO| lze také vytvořit objednávku na doplnění zásob.
ručně. Tento postup je užitečný v případě, kdy je nutné dodat poddodavateli materiál bez
vytvoření |PO|.

Chcete-li doplnit zásoby poddodavatele ručně, přejděte na aplikaci „Sklad“ a klikněte
na kartě „Dodavatel doplňkového materiálu“. Vytvořte novou objednávku *Dodavatele doplňkového materiálu*.
kliknutím na tlačítko „Nový“.

V poli „Adresa dodání“ vyberte poddodavatele, kterému by měly být součástky doručeny.
bude zaslána.

Pak přidejte každou složku do záložky „Operace“ kliknutím na „Přidat řádek“.
Vyberte komponentu v poli „Produkt“ a zadejte množství.
pole „Požadavek“.

Poté klikněte na tlačítko „Zaznamenat jako úkol“ a objednávku zaregistrujete. Jakmile jsou součásti odeslány,
k poddodavateli a poté stiskněte tlačítko „Potvrdit“ pro ověření, že objednávka byla odeslána.

Vytvořte SO
---------

Tento krok je nutný pouze v případě, že se produkt nakupuje u dodavatele.
uspokojit poptávku zákazníka. Pokud je produkt kupován za účelem zvýšení zásob
Pokud je k dispozici, přejděte na další krok.

Vytvořit nový |SO|. Přejděte na: „Prodejní aplikace -> Objednávky -> Objednávky“ a klikněte
:guilabel:`Nový“.

Vyberte zákazníka v seznamu :guilabel:`Zákazník`. Pak klikněte na :guilabel:`Přidat
Vyberte produkt v seznamu „Dodavatelské řádky“ na kartě „Produkty“.
Vyberte možnost „Produkt“ v rozevíracím seznamu a zadejte množství do pole „Množství“.

Klikněte na tlačítko „Potvrdit“ pro potvrzení objednávky. Poté se vám zobrazí tlačítko „Dokončit nákup“.
je na horní části stránky. To otevře PO vytvořené k nákupu poddodavatelského produktu
od dodavatele.

.. poznámka::
Pouze pokud je povolena funkce „Dodání na objednávku“ (*Replenish on Order (MTO)*) v trasách, pak se |SO| pro produkt stává |PO|.
stránce produktu a zároveň není dostatek skladových zásob k uspokojení poptávky.

Pokud je dostatečné množství skladových zásob, potvrzení |SO| pro produkt místo toho vytvoří dodací lhůtu.
pokynu, protože Odoo předpokládá, že |SO| bude splněno pomocí zásob skladu.

V případě, že se jedná o zboží dodávané přes distributora konečnému zákazníkovi, není možné vracet zboží.
V případě, že je zboží skladem, vždy se vytvoří PO, i kdyby bylo dostupné.

Proces PO
----------

Pokud byl v předchozím kroku vytvořen |PO|, přejděte na: „Nákup aplikace > Objednávky“.
Nákupní objednávky“ a vyberte „PO“. Pak klikněte na „Potvrdit objednávku“, abyste ji potvrdili.

Pokud v předchozím kroku nebyl vytvořen |PO|, tak ho nyní vytvořte tím, že se přesunete na:
app --> Objednávky --> Nákupní objednávky“, a klikněte na „New“.

Začněte vyplňovat PO, když zvolíte dodavatele ze seznamu v rozevíracím seznamu Vendor.
V záložce „Produkty“ klikněte na „Přidat produkt“, abyste vytvořili novou řadu produktů.
Vyberte zboží dodavatele v poli „Produkt“ a do pole „Množství“ zadejte
Pole „Množství“. Nakonec klikněte na tlačítko „Potvrdit objednávku“, abyste potvrdili PO.

Když je potvrzena poptávka na produkt, který vyžaduje dodání komponent do poddodavatelské společnosti,
Pokladní doklad nebo objednávka na zaslání zboží je automaticky vytvořen a lze jej přistupovat k prostřednictvím odpovídajícího
Tlačítko „Pokladní doklad“ nebo „Dodání na sklad“ chytré tlačítko, které se objeví v horní části |PO|.

Dále je vytvořen příkaz *Nákupní subdodavatel*, který zajistí dodání požadovaných komponentů na
subdodavatele. Tento příkaz lze také získat z příkazu |PO| kliknutím na tlačítko :guilabel:`Dodávka materiálu`.
chytře umístěný tlačítko v horní části stránky.

.. obrázek:: subcontracting_resupply/subcontractor-po.png
:align:center
:alt:PO pro dodavatele zásobování na objednávku s funkcí doplňování a přijímání zboží
tlačítka v horní části stránky.

PO pro dodavatele zásobování na objednávku s tlačítky Smart Button Resupply a Smart Button Receipt
nahoře na stránce.

Objednávka procesu doplňování zásob
------------------------------------

Jakmile jsou komponenty dodané na poddodavatele, přejděte do
Vyberte možnost „Nákupní aplikace“ > „Objednávky“ > „Nákupní objednávky“.

Klikněte na tlačítko „Doplnit zásoby“ v horní části obrazovky, abyste otevřeli okno *Doplnit zásoby.
Objednejte si poddodavatele a klikněte na tlačítko „Potvrdit“, abyste potvrdili, že součástky byly odeslány.
subdodavateli.

Alternativně přejděte do aplikace „Sklad“, klikněte na „# K zpracování“
tlačítko na kartě „Dodavatel doplňkových služeb“ a vyberte možnost „Dodavatel doplňkových služeb“.
objednávku. Poté klikněte na tlačítko „Potvrdit“, abyste potvrdili, že komponenty byly odeslány do
dodavatelé.

Přijmout objednávku nebo zadat objednávku na dodání
---------------------------------

Jakmile dodavatel dokončí výrobu produktu, buď jej odesílá přímo zákazníkovi
dodavatelské společnosti nebo přepraví přímo zákazníkovi, v závislosti na tom, jakým způsobem byl produkt dodán.
:ref:`konfigurováno <výroba/procesy/dodavatelsko-odběratelské vztahy/produktové konfigurace>“.

Potvrzení o přijetí
~~~~~~~~~~~~~~~

Pokud dodavatel poskytuje hotový výrobek smluvní společnosti, jednou
obdrželi, přejděte na: „Koupit aplikaci“ -> „Objednávky“ -> „Nákupní objednávky“, a vyberte
|PO|.

Klikněte na tlačítko „Přijmout produkty“ v horní části stránky PO nebo na tlačítko „Potvrzení“.
Chytrý tlačítko na horní části stránky k otevření faktury. Pak klikněte na „Potvrdit“
dolní část účtenky pro přijetí zboží do skladu.

Proces objednávky zboží na sklad
~~~~~~~~~~~~~~~~~~~~~~

Pokud dodavatelé zboží zasílají poštou, přejděte na
Vyberte možnost „Nákupní aplikace“ > „Objednávky“ > „Nákupní objednávky“.

Vyberte v horní části stránky tlačítko „Dropship“ a
Klikněte na „Potvrdit“ v horní části objednávky, abyste potvrdili, že produkt byl odeslán.
zákazník.

Dodání procesního příkazu
----------------------

Pokud byla pracovní postup pro poddodavatele zahájena zákazníkem |SO|, a pokud byl výsledný produkt
přeposlány zákazníkovi, ale dodány do smluvní firmy, je nutné
doručit produkt zákazníkovi a zpracovat objednávku na dodání.

Jakmile je produkt odeslán zákazníkovi, přejděte do aplikace „Prodej“ a
Vyberte si |SO|. V horní části stránky vyberte tlačítko „Dodání“
dodací objednávku a klikněte na tlačítko „Potvrdit“ v objednávce, abyste potvrdili, že produkt byl
doručena zákazníkovi.
