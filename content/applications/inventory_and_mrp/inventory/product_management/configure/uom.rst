================
Jednotky měření
================

.. |UOM| nahradit za: zkratka: `UoM (jednotka měření)`
.. |PO| nahradit za: abbr: PO (příkaz k nákupu)
.. |POs| nahradit za: zkratka: `POs (Purchase Orders)`
.. |RFQ| nahradit za: zkratka: RFQ (žádost o nabídku)
.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`

V některých případech je nutné s produkty pracovat v různých jednotkách měření. Například podnik
Můžete si koupit produkty od země, která používá metrický systém, a poté tyto produkty prodávat
země používající imperiální systém. V tom případě musí podnik převádět jednotky.

Dalším příkladem je situace, kdy firma nakupuje zboží ve velkém balení od dodavatele.
Tyto produkty pak prodává v jednotlivých kusech.

Odoo lze nastavit tak, aby pro jeden produkt používal různé jednotky měření (JUM).

Konfigurace
=============

Pro použití různých jednotek měření v Odoo nejprve přejděte na:
Konfigurace --> Nastavení“, a v sekci „Produkty“ aktivujte
Nastavení „Jednotky měření“ a pak klikněte na „Uložit“.

.. obrázek: uom/uom-enable-setting.png
:align:center
:alt:Povolit jednotky měření v nastavení zásob.

Kategorie jednotek měření
===========================

Po zapnutí nastavení *Měrné jednotky* zobrazte výchozí kategorie měrných jednotek
V nabídce „Inventář aplikace“ -> „Konfigurace“ -> „Kategorie jednotek“. Kategorie je důležitá pro
převod jednotek; Odoo může převést jednotky produktu z jedné jednotky na jinou pouze v případě, že oba
patří do stejné kategorie.

.. obrázek:uom/kategorie.png
:align:center
:alt:Nastavte kategorie měrné jednotky.

Každá kategorie jednotek měření má referenční jednotku. Referenční jednotka je zvýrazněna modře v
sloupec „Uom“ na stránce „Kategorie měr a jednotek“. Odoo používá
jednotka jako základ pro jakékoliv nové jednotky.

Pro vytvoření nové jednotky nejprve vyberte správnou kategorii z :guilabel:`Jednotek měření
Stránka kategorií. Například pro prodej produktu v balení šesti jednotek klikněte na „Jednotka“
kategorie. Pak v seznamu kategorií vyberte možnost „Přidat řádek“
:guilabel:`Jednotky měření“ a poté v poli „Jednotka měření“ zadejte nový
jednotka, například „Box of 6“, pak v poli „Typ“ vyberte odpovídající velikostní referenci.
například: guilabel:"Větší než referenční jednotka měření".

Pokud je to možné, zadejte :guilabel:`Kategorie UNSPSC“, což je celosvětově uznávaný „kód spravovaný
GS1 <http://www.gs1.cz/>, která je nutná k použití.

Do pole „Hodnota“ zadejte počet jednotek v novém měřítku, například
„6,0000“ v příkladu „šestičlenné balení“ (protože šestikus je šestkrát větší než
jednotka odkazu (např. ‚1.00000‘).

.. obrázek: uom/convert-products-by-unit.png
:align:center
:alt: Převádět produkty z jednotky na druhou, pokud patří do stejné kategorie.

Uveďte jednotky měření produktu
====================================

Aby se na produkt nastavily jednotky měření, nejprve přejděte do: menu:Inventarapp --> Produkty -->
Produkty“ a vyberte produkt, abyste otevřeli jeho stránku s formulářem.

V záložce „Obecné informace“ upravte pole „Jednotka měření“, abyste specifikovali
jednotka, ve které je produkt prodáván. Uvedená jednotka je také jednotkou používanou k skladování
skladového hospodářství a vnitřních přesunů zboží.

Upravte pole „Nákup UoM“ na hodnotu jednotky měření, ve které je produkt nakoupen.
in.

.. inventář/dodávka zboží/jednotková konverze:

Převod jednotek
===============

Odoo automaticky převádí jednotky měření, když produkty mají různé :abbr:`UoMs (jednotky měření).
Měřítko a koupit: zkratka UoMs (jednotky měření).

Tento jev se může projevit v různých situacích, například:

#:ref:`Příkazy dodavatelů <Inventář/Naplnění zásob/Koupit - jednotka měření>“: nákup |UOM| na nákup
objednávky (PO) se převádí na jednotku měření na vnitropodnikových dokumentech.
#.:ref:`Automatické doplňování zásob <inventory/product_replenishment/replenish>“: vygeneruje |POs|, když
pokud se zásoby určitého produktu (sledovaného v jednotkách měření) dostanou pod určitou úroveň. Ale |POs| jsou
vytvořené na základě nákupu |UOM|
#:ref:`Prodat produkt <sklad/dodavatelský řetězec/prodej v jednotkách měření>“: pokud se používá jiná |jednotka měření|
na prodejním příkazu (PO) se množství převede na jednotku měření skladu preferovanou |UOM|.
dodací list

...Inventarizaci, doplňování zásob a nákup v jednotkách měření:

Nakupujte produkty v nákupu UoM
--------------------------------

Když v aplikaci Nákup vytvoříte novou poptávku na nabídku (RFQ), Odoo automaticky použije
určená jednotka měření produktu. Pokud je potřeba, ručně upravte hodnotu :guilabel:`UoM`.
RFQ.

Po potvrzení RFQ do PO klikněte na tlačítko „Potvrzení“ v horní části
PO.

Odoo automaticky převádí jednotku měření nákupu na prodejní nebo skladovou jednotku.
měřítko, takže sloupec „Požadované množství“ v dokladu o převzetí zboží ukazuje převedený počet.

.. příklad::
Když je vlastnost nákupu produktu UoM „Box of 6“ a jeho prodejní/skladovací jednotka „Box
jednotka je „Units“, pak ukazuje množství v krabicích po šesti a na faktuře (a dalších dokumentech)
Vnitřní skladovací dokumenty (výdejky, přijaté faktury apod.) uvádějí množství v jednotkách.

.. obrázek:: uom/on-po.png
:align:center
:alt: Obrázek objednávky, která používá jednotku měření nákupu.

Třícestný příkaz je vytvořen pomocí nákupu „UoM“ s hodnotou „Box of 6“.

.... obrázek: uom/dostupnost.png
:align:center
:alt: Obrázek účtenky s jednotkou měření.

Při příjmu skladu jsou zaznamenané množství v interním „Jednotce měření“:
„Jednotky“.

..Inventarizaci, doplňování zásob a doplnění zboží:

Dodávky
-------------

Požadavek na cenovou nabídku produktu lze také vytvořit přímo z formuláře produktu pomocí
tlačítko „Doplnit“.

Po kliknutí na tlačítko „Doplnit“ se objeví okno asistenta pro doplnění zásob.
měřítko lze ručně upravit v poli „Kvantita“ (tlačítko „Guilabel“), pokud je to nutné. Pak klikněte
Klikněte na tlačítko „Potvrdit“ pro vytvoření |RFQ|.

.. důležité::
A |PO| lze automaticky vygenerovat pouze v případě, že je uveden alespoň jeden dodavatel.
v záložce produktu „Nákup“.

.. obrázek: uom/replenish.png
:align:center
:alt:Klikněte na tlačítko „Doplnit“ a ručně doplňte.

Přejděte do vytvořeného |PO| klepnutím na tlačítko „Vyhlášené“ chytré štítky produktu.
Formulář se spustí. Vyhledejte v něm část „Očekávaný zásob“ a v části „Poptávky
pro odkaz na „citace“ klikněte na číslo referenčního čísla RFQ a otevřete návrh RFQ. Pokud je třeba
Příjem lze upravit přímo na pohledávce.

...Inventarizaci, doplňování zásob a prodej v jednotkách měření:

Prodávejte v jiném měřítku
-----------------------

Při vytváření nové nabídky v aplikaci *Prodej* používá Odoo automaticky produkt s uvedenou
jednotka měření. Pokud je potřeba, lze ručně upravit UoM na cenovce.

Po odeslání cenové nabídky zákazníkovi a jejím potvrzení v objednávce na prodej (SO) klikněte na
:tlačítko „Dodání“ na horní liště |SO|. Odoo automaticky převede jednotku
započítat do skladového měřítka produktu, takže sloupec „Požadavky“ v
dodací list uvádí převrácenou hodnotu.

Příklad: Pokud by se jednotka prodeje výrobku na SO změnila z „Krabice po 12“ na „Balení po 6“, ale skladová jednotka
jednotka je „Units“, zobrazuje se v šesti blocích a dodávka ukazuje množství
v jednotkách.
