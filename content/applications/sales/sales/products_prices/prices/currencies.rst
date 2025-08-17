==================
Měny cizí
==================

S Odoo lze ceníky použít k řízení cen v řadě cizích měn. Konkrétně
Odoo má schopnost pracovat s celkem 167 měnami.

.. poznámka::
Pro použití více měn v aplikaci Odoo Sales je nutné mít nainstalovanou aplikaci Accounting.
nainstalovány.

Nastavení
========

Jakmile je aplikace *Účetnictví* nainstalována, lze do databáze přidat cizí měny.
Přejděte na: „Účetní aplikace -> Konfigurace -> Nastavení“ a posuňte se dolů do
sekci „Měny“ a najděte nastavení „Hlavní měna“.

.. obrázek: nastavení_hlavní_měny.png
:align:center
:alt:Jak se hlavní měna zobrazuje na stránce nastavení v účetnictví Odoo.

Odoo automaticky nastaví hlavní měnu jako měnu země, ve které je společnost založena.

Chcete-li změnit hlavní měnu společnosti, vyberte v rozevíracím seznamu pole „Měna“.
Vyberte požadovanou měnu a ujistěte se, že změny uložíte pomocí tlačítka „Uložit“.

..tip:
Chcete-li zajistit automatické aktualizace kurzů měn, zapněte funkci *automatické kurzy měn*.
v nastavení účetnictví (:menu:„Účetní aplikace --> Konfigurace --> Nastavení
--> část měn.

.... obrázek:: sazby/sazby-měn-automaticky.png
:synchronizace: střed
:alt:Jak se hlavní měna zobrazuje na stránce nastavení v účetnictví Odoo.

Zatrhněte zaškrtávací políčko vedle funkce „Automatické měnové kurzy“ a vyberte určenou
Banka získá kurzy měn v poli „Služba“ v rozevíracím seznamu. Vyberte
doba, po kterou se aktualizace provádějí. Pak určete datum
by mělo být „Další běh“.

Chcete-li okamžitě aktualizovat kurzovní lístek, klikněte na ikonu :guilabel:`🔁 (kruhové šipky)`
vpravo od pole „Další spuštění“.

Po dokončení všech konfigurací se ujistěte, že provedete :guilabel:`Uložení změn`.

.. poznámka::
Všechny způsoby platby musí být v měně účetní knihy nebo společnosti.
měna, pokud společnost nemá nastavenou měnu. Pokud není stejná, zobrazí se :guilabel:`Validace
Vyskytne se chybová hláška.

Zobrazit, upravovat a přidávat měny
==============================

Pro zobrazení, úpravu a přidání měn do databáze, které jsou k dispozici na cenových nabídkách a na
Vyberte možnost „Hlavní měna“ v rozevíracím seznamu a klikněte na odkaz „Měny“, který je pod ním.
V poli „Měna“ na stránce „Nastavení účetního programu“ v sekci „Aplikace“.

Když je kliknut na odkaz „Měny“, objeví se samostatná stránka s názvem „Měny“.

.. obrázek: měny/hlavní_měny_stránka.png
:align:center
:alt:Jak vypadá hlavní stránka měn v účetním systému Odoo.

Na této stránce společnost Odoo nabízí seznam 167 globálních měn. Každá řádka ukazuje odpovídající
„Měna“, „Značka měny“, „Název měny“ a datum „Poslední aktualizace“.
„Současná sazba“ (ve srovnání se základní měnou země, ve které je společnost
založené).

Vpravo dole jsou dvě sloupce, které lze zapnout nebo vypnout:

- :guilabel:`Aktivní“: tato měna je aktivní, což znamená, že může být přidána do ceníku.
používána jako hlavní měna společnosti, pokud si přejete (v menu „Účetnictví“ ->
Konfigurace --> Nastavení --> Měny

.. poznámka::
Výchozí nastavení zobrazuje všechny možnosti měn s aktivním stavem nahoře na seznamu.

..tip:
Je doporučeno vytvořit alespoň jednu cenovou nabídku na každé aktivní měně. Viz
:doc:`./pricing` pro získání dalších informací o konfiguraci cen.

Pro zapnutí nebo vypnutí možností klikněte na přepínač v řádku odpovídající sloupci. V poloze „zapnuto“
Barva přepínače je zelená. Když je vypnutý, barva přepínače je šedá.

Formulář pro podrobné informace o měně
--------------------

Chcete-li upravit jakoukoli měnu na stránce „Měny“, klikněte na požadovanou měnu a zobrazí se
detailní formulář pro konkrétní měnu a pokračujte v případných změnách.

.. obrázek: měny/měnový formulář.png
:align:center


V podrobnostech o měně se zobrazuje příslušný kód měny v poli „Měna“ .
Pod ním je název měny v poli „Název“.

Poté přepněte dostupnost měny pomocí tlačítka „Aktivní“ (zapnuté je označeno hvězdičkou)
zelený přepínač a šedý přepínač značí „vypnuto“.

Vpravo od podrobností o měně je vhodné zadat například „Měna“ (např. „Dolar“)
a „Jednotka měny“ („Currency Subunit“, např. „Cent“) lze najít.

Dále je možné pod záložkou „Sazby“ zobrazit, přidat nebo upravit různé konverzní sazby.
smazán. Každá řada ukazuje datum dané sazby, konkrétní společnost a
Je spojeno s následujícími etiketami: „Jednotka za ...“ a „... za jednotku“.

.. poznámka::
Hvězdičkou v posledních dvou sloupcích je označen hlavní měnový pár společnosti.
Příklad: pokud je hlavní měnou nastaveno „USD“, pak sloupce nesou název např. „Euro za 1 USD“.
a :guilabel:`USD za jednotku“.

Chcete-li přidat novou sazbu, klikněte na „Přidat řádek“ v záložce „Sazby“ a postupujte podle následujících pokynů
Nezbytné informace v uvedených sloupcích.

Hlavní formulář pro podrobnosti o měně
-------------------------

Pokud je vybraná měna hlavní měnou společnosti, objeví se modrá lišta na horní části
formulář s podrobnostmi o měně s textem: „Toto je měna vaší společnosti.“

.. obrázek: měny/hlavní měna - detail formuláře.png
:align:center
:alt:Jak vypadá hlavní formulář pro účetní měnu v Odoo Accounting.

Všechna pole jsou stejná jako u běžného formuláře pro podrobnosti o měně, ale nebude
:guilabel:'Sazby' tabulka, protože všechny ostatní měnové kurzy jsou založeny na hlavní měně
společnost.

Vytvořit novou měnu
===================

Pokud požadovaná měna není na stránce „Měny“, klikněte na tlačítko „Nový“
otevřít prázdný vzor formuláře měny.

..tip:
Stejný tlačítko „Nový“ se nachází v pravém horním rohu každého formuláře s podrobnostmi o měně.

.. obrázek: měny/prázdný formulář pro detailní informace o měně.png
:align:center
:alt:Jak vypadá prázdný platební příkazový formulář v účetnictví Odoo.

V prázdné podobě formuláře měny pokračujte v zadávání požadovaného kódu měny.
V poli „Měna“ zadejte název měny a pod ním název měny v poli „Název“.
pole.

Pak přepněte na tlačítko „Aktivní“ („:guilabel:Active“) a zapněte měnu.

Vpravo od podrobného formuláře měny zadejte příslušnou jednotku měny (:guilabel:Měnová jednotka) (např.
„Dolarů“ a vhodné „Měnové jednotky“ (např. „Centů“).

Dále pod záložkou „Sazby“ přidejte novou sazbu kliknutím na „Přidat řádek“. Pak
pokračujte v potvrzení a upřesnění datumu, společnosti, jednotky na...
a pole „Popis jednotky“ a „Popis jednotky na stránce“ pro zajištění, aby všechny automaticky vyplněné informace byly správné.

.. poznámka::
Hvězdičkou v posledních dvou sloupcích je označen hlavní měnový pár společnosti.
Příklad: pokud je hlavní měnou nastaveno „USD“, pak sloupce nesou název např. „Euro za 1 USD“.
a :guilabel:`USD za jednotku“.

Ceníky podle měny
============================

Doporučuje se vytvořit alespoň jeden ceník na každou aktivní měnu v databázi.
Vytvořit (nebo přiřadit) ceník pro konkrétní měnu. Začněte přejetím na:
app --> Produkty --> Ceníky.

Na stránce „Ceníky“ buď vyberte existující ceník k úpravě nebo klikněte
:guilabel:`New“ pro vytvoření nové cenové nabídky.

V podrobnostech cenovky upravte pro novou nebo existující cenovku
Zadejte pole „Měna“ podle svých představ.

.. viz též:
:doc:`./pricing` pro získání dalších informací o konfiguraci cen.

Automatická konverze z veřejné ceny
=================================

Je třeba zdůraznit, že viditelná cena na produktech je přímo závislá na hlavní měně
firma nastavila, který je konfigurován při zadávání do pole:
Konfigurace --> Nastavení --> Měny --> Hlavní měna --> Výběr měny.

Prodejní cena se automaticky aktualizuje, pokud je ceník změněn na jiný ceník s
jinou měnou než je hlavní měna společnosti. Cenový posun je přímo úměrný
Aktualizovaný kurz pro tuto měnu.

Určit ceny produktů
==================

Aby se předešlo změnám kurzů měny, je třeba nejprve
navigace na:menu-selection:'Prodejní aplikace --> Produkty --> Produkty'.

Na stránce „Produkty“ vyberte požadovaný produkt pro úpravu nebo vytvořte nový produkt.
kliknutím na tlačítko „Nový“.

Poté v detailu produktu klikněte na tlačítko „Doplňkové ceny“ chytrého filtru, které se nachází
v horním levém rohu. To odhalí samostatnou stránku s cenovými pravidly pro daný
určitého produktu.

.. obrázek: ceny/pravidla-cen-měn.png
:align:center
:alt:Jak nastavit ceny produktů podle cenových seznamů v zahraniční měně v Odoo Sales.

Klikněte na tlačítko „Nový“ a vyberte požadovanou cenovku z roletky.
Sloupec „Ceník“.

V poli „Aplikováno na“ se automaticky vyplní produkt, takže pokračujte v zadávání
požadované hodnoty v polích „Minimální množství“ a „Cena“.

.. poznámka::
Hodnota v poli Min. množství znamená, že cena nastavená na hodnotě
**pouze** spustí, pokud je zakoupeno alespoň tolik produktů.

Pokud je třeba, nastavte datum zahájení a datum ukončení pro sazby.
Nevyplnění těchto sloupců zajišťuje, že cena zůstane stejná bez ohledu na datum prodeje.

Pokud pracujete v prostředí více společností, určete do které společnosti se má tato cenová pravidla
použité v poli „Společnost“ na kartě Cena. Pokud pole necháte prázdné, pravidlo ceny se bude vztahovat na
všechny společnosti v databázi.

S těmito konfiguracemi je hotovo, ať se děje cokoliv s aktualizacemi nebo změnami v převodu.
Uplatní se pro zákazníka, který si chce zakoupit konkrétní produkt.
Předem stanovené ceny se objevují.

.. viz též:
:doc:`./cenik`
