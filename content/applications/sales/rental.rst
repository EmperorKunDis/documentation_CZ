Zobrazit obsah

======
Pronájem
======

Aplikace Odoo Rental poskytuje komplexní řešení pro konfiguraci a správu pronájmů.

Posílejte nabídky, potvrzujte objednávky, plánujte pronájmy, zaregistrujte produkty při jejich vyzvednutí a
se vrací a fakturuje zákazníkům z jediné platformy.

.. viz též:
   - „Odoo Pronájem: stránka produktu <https://www.odoo.com/app/rental>“
   - „Návody k Odoo: Pronájem <https://www.odoo.com/slides/rental-48>“

.. karty:

......karta: Spravovat vklady
:target: pronájem/správa vkladů
:velké:

Naučte se, jak vytvořit rezervační zálohu na pronájem produktů.

Přístrojová deska
=========

Při otevření aplikace „Výpůjčky“ se zobrazí panel „Objednávky výpůjček“.

.. obrázek: pronájem/objednávky-pronájmu-přístupu.png
:align:center
:alt: Příklad přehledu pronájmu dostupný v aplikaci Odoo Pronájem.

V výchozím zobrazení karty kanban jsou všechny pronájmy viditelné. Každá karta pronájmu zobrazuje jméno zákazníka
cena pronájmu, číslo souvisejícího prodejního příkazu a stav pronájmu.

.. poznámka::
Pronájem kartiček kanban, které nezobrazují stav pronájmu, znamená, že tyto pronájmy byly potvrzeny
citáty, ale nebyly ještě vybrány.

Na levém sloupci najdete stav pronájmu každého pronajatého objektu. Pod ním se nachází
Stav faktury pronájmu je přístupný. Kliknutím na jakoukoliv možnost v levém sloupci
filtruje zobrazené pronájmy na přehledovém panelu.

Nastavení
========

Konfigurovat další náklady na pozdní vrácení pronajatého předmětu, dostupnost pronajatých předmětů nebo minimální dobu pronájmu.
přejít na: menu: „Pronájem aplikace“ --> „Konfigurace“ --> „Nastavení“.

.. obrázek: pronájem/nastavení pronájmu.png
:align:center
:alt:Jak vypadá stránka Nastavení aplikace Odoo Pronájem.

V sekci „Pronájem“ jsou možnosti konfigurace „Základní náklady na zpoždění“.
a „Výchozí doba odložení“. Je zde také možnost aktivovat „Pronájem
Převody a digitální dokumenty.

- „Výchozí náklady na pozdní vrácení“ jsou další náklady za pozdní vrácení.
- :guilabel:`Výchozí časový prostor mezi pronájmy“ představuje minimální dobu mezi dvěma pronájmy.
- :guilabel:`Převody pronájmu“ znamená, že zásoby dodání a přijetí mohou být použity pro objednávky pronájmu.
- :guilabel:„Digitální dokumenty“ umožňují uživatelům nahrát dokumenty, které zákazníci mohou podepsat předtím, než se s nimi setkají.
potvrzující svůj pronájem.

V sekci „Online pronájem“ jsou možnosti konfigurovat „Minimální nájemné“.
Doba trvání a označte ji jako „nedostupnost“, nebo dny, kdy je možné si zboží vyzvednout a vrátit.
nebylo možné.

Pronájem produktů
===============

Pro zobrazení všech produktů k pronájmu v databázi přejděte na:
Produkty“. Výchozí hledací filtr „Může být zapůjčen“ se zobrazuje v poli pro vyhledávání.

Každá kartička s kanbanem zobrazuje název produktu, cenu pronájmu a obrázek produktu (pokud je
aplikovatelné).

.. viz též:
:doc:`pronajem/vklad-na-účet

.. pronájem/cena:

Nájemné
==============

Abychom upravili cenu pronájmu produktu, přejděte na stránku „Produkty“ v aplikaci Rental.
Vyberte požadovaný produkt nebo klikněte na tlačítko „Nový“ pro vytvoření nového produktu od nuly.

V poli „Produkt“ zkontrolujte zaškrtnutí políčka „Lze půjčit“. Poté otevřete
:guilabel:`Nájemné“ záložka.

.. obrázek: pronájem/cena-pronájmu-tabulka.png
:align:center
:alt:Jak vypadá stránka Nastavení aplikace Odoo Pronájem.

.. poznámka::
Pokud chcete vytvořit pronajatý produkt mimo aplikaci Rentals, ujistěte se, že je zaškrtnuto pole „Může být
Zatržená políčka „Pronajaté“ se nachází na formuláři produktu. Výchozí nastavení je takové, že tato
Produkt vzniká přímo v aplikaci Rental.

Ceny
-------

V sekci „Ceník“ pod záložkou „Ceny pronájmu“ zvolte vlastní cenu pronájmu.
cena a pronajímací období produktu.

Chcete-li přidat cenu pronájmu, klikněte na „Přidat cenu“. Pak vyberte období pro cenovou politiku.
„jednotka doby pronájmu“ v sloupci „Doba“ nebo vytvořte novou
cenu za období zadáním názvu a kliknutím na „Vytvořit“.

Dále se rozhodněte, zda chcete tuto vlastní cenu pronájmu použít pro konkrétní ceník.

Na závěr zadejte požadovanou cenu za dané období.

.. poznámka::
Počet cenových linií není omezený, můžete přidat i více možností pronájmu.
Produkty jsou obvykle používány k poskytování slev zákazníkům, kteří souhlasí s delší dobou pronájmu.

K odstranění jakékoliv pronájemové cenové varianty klikněte na ikonu „🗑️“ a ta řádka
smazán.

Rezervace
------------

V sekci „Rezervace“ pod záložkou „Pronájem vozidel“ je možné vybrat
konfigurovat další pokuty za každou hodinu nebo den navíc, které
zákazník si vrací pronajaté zboží.

Můžete také nastavit „Časová zóna“ (v hodinách), aby byla pronajatá
Produkt je mezi dvěma půjčovními objednávkami nedostupný. Taková funkce se může hodit, pokud
Při každém pronájmu je nutné provádět údržbu nebo čištění.

Spočítání ceny
---------------

Odoo vždy používá dvě pravidla k výpočtu ceny produktu při vytvoření pronájmu:

#Používá se pouze jedna cenová hladina.
#Nejlevnější linka je vybrána.

..cvičení::
Zvažte následující konfiguraci cen pronájmu produktu:

   - 1 den: 2500 Kč
   - 3 dny: 250 dolarů
   - 1 týden: 500 dolarů

Klient si chce půjčit tento produkt na osm dní. Kolik zaplatí?

Po vytvoření objednávky vybírá Odoo druhou položku, protože je nejlevnější.
Klient musí zaplatit třikrát „3 dny“ na pokrytí pronájmu osmi dní, celkem 750 $.

.. pronájem / objednávka:

Pronájem
=============

Pro vytvoření pronájmu v aplikaci *Pronájem*, přejděte do sekce:
„Objednávky“ a klikněte na „Nový“. Tím se zobrazí prázdná objednávka pronájmu, kterou je třeba vyplnit
Podle toho.

.. obrázek: pronájem/půjčovní smlouva.png
:align:center
:alt: Vzor vyplněného pronájmu k dispozici v aplikaci Odoo Pronájem.

Začněte přidáním objektu :guilabel:`Customer`, pak upravte požadovanou dobu pronájmu v
V poli „Doba pronájmu“.

Pro upřesnění doby pronájmu klikněte na první datum v poli „Doba pronájmu“ a
Vyberte rozsah dat, který bude reprezentovat pronájem z kalendářního okna.
se objevuje.

.. obrázek: pronajem_doba_pronajmu_popup.png
:align:center
:alt: Příklad kalendáře s rezervací v aplikaci Odoo Rental.

Po dokončení klikněte na tlačítko „Použít“ v okně kalendáře. Poté se zobrazí
zmizí a doba pronájmu je reprezentována v poli `Doba trvání`.
pole.

Dále přidejte produkt pronájmu v záložce „Řádky objednávky“ kliknutím na „Přidat
produktu“ a zvolte požadovaný produkt k přidání do formuláře.

.. poznámka::
Pokud je produkt pronajatý předtím, než dojde k správnému vyplnění pole „Doba půjčení“
Pokud je nastavení správné, uživatel může stále upravit pole „Doba pronájmu“ podle svých potřeb.

Vyberte požadovaný rozsah dat, které budou reprezentovat dobu pronájmu, a pak klikněte
:guilabel:`Aktualizovat nájemné“ v poli „Doba pronájmu“.

.... obrázek: pronajem/aktualizace-nastavení-cena-pronajmu.png
:synchronizace: střed
:alt:Možnost aktualizace pronájmu, která se zobrazuje v aplikaci Odoo Rental.

Při tom se zobrazí okno „Potvrzení“. Pokud je vše v pořádku, klikněte na
:guilabel:`OK“ a Odoo přepočítá pronajatou cenu podle toho.

Jakmile jsou všechny údaje na objednávce zapůjčení vloženy správně, klikněte na
Tlačítko „Odeslat e-mailem“ pro odeslání nabídky zákazníkovi nebo klikněte na
Klikněte na tlačítko „Potvrdit“ pro potvrzení objednávky.

... pronájem/podpis zákazníka:

Podpis zákazníka
==================

Po potvrzení objednávky pronájmu se zobrazí tlačítko „Podepsat dokumenty“. To umožňuje
schopnost požádat zákazníka o podepsání nájemní smlouvy, která popisuje dohodu mezi
firma a zákazník, *předtím*, než si půjčí výrobky.

Tyto dokumenty mohou zajistit, že vše bude vráceno včas a ve svém původním stavu.

.. důležité:
Tlačítko „Podepsat dokumenty“ se zobrazí pouze tehdy, pokud je k dispozici možnost „Digitální
V nastavení aplikace „Pronájem“ byla aktivována funkce „Dokumenty“. Pro její aktivaci přejděte na
:menu_selektor:"Pronájem aplikace --> Konfigurace --> Nastavení", aktivujte
„Dokumenty“ a klikněte na „Uložit“.

.. poznámka::
Tato funkce vyžaduje také aplikaci „Podpis“ (Sign). Pokud je třeba, Odoo
Po aktivaci nastavení „Digitální dokumenty“ automaticky nainstaluje.

Pro požadavek zákaznického podpisu na pronájmu vyberte potvrzenou objednávku a klikněte
tlačítko „Podepsat dokumenty“ k zobrazení okna „Podepsat dokumenty“.

.. obrázek: pronájem/podepisování dokumentů/popup.png
:align:center
:alt:Pop-up okno Přidat podpisy, které se objevuje v aplikaci pronájmu Odoo.

Zde vyberte požadovaný dokument z pole „Šablona dokumentu“. Pak klikněte
:guilabel:`Podepsat dokument“. To způsobí zobrazení okna „Nová žádost o podpis“ .

.. obrázek: pronájem/žádost o nový podpis.png
:align:center
:alt:Pop-up okno s žádostí o nové podpisy, které se zobrazí v aplikaci pronájmu Odoo.

Po potvrzení informací v dialogovém okně „Nová žádost o podpis“ klikněte
Klikněte na tlačítko „Začněte podepisovat“.

Na další stránce se pak objeví dokument k podepsání, který je přístupný
klienta přes zákaznický portál.

Odoo vede zákazníka krok za krokem procesem podepisování s jasnými a klikatelnými ukazateli.
jim vytvořit elektronické podpisy, aby mohli rychle vyplnit formulář.

.. obrázek: pronájem/osvojení podpisu v okně.png
:align:center
:alt:Pop-up okno s názvem „Přijmout podpis“ se objeví v aplikaci pronájmu Odoo.

Jakmile dokument podepíšete a dokončíte, klikněte na tlačítko „Zkontrolovat a odeslat dokončený“.
Tlačítko „Dokument“ v dolní části dokumentu.

.. obrázek: pronajem/validovat-odeslat-dokumenty-tlačítko.png
:align:center
:alt:Tlačítko pro ověření a odeslání dokumentu v aplikaci pronájmu Odoo.

Po kliknutí na tlačítko „Ověřit a odeslat dokument“ se Odoo nabízí možnost
Stáhnout podepsaný dokument pro účely archivace, pokud je třeba.

.. viz též:
„Návody k Odoo: Podepsání <https://www.odoo.com/slides/sign-61>“

.. pronájem/vyzvednutí a vrácení:

Pickup produkty
===============

Při vyzvednutí produktu se přesuňte na příslušnou objednávku pronájmu, klikněte na
Tlačítko „Odebrat“ a poté klikněte na „Zkontrolovat“ v „Zkontrolujte odběr“.
připravené okno, které se objeví.

Tím se na objednávku pronájmu zobrazí informační panel „Vyzvednuté“.

.. půjčovna/vrácení:

Vrácené zboží
===============

Pokud zákazník vrátí produkt(y), přejděte na příslušný pronájem, klikněte na
tlačítko „Zpět“ a potvrďte vrácení kliknutím na tlačítko „Potvrdit“.
Vyberte možnost „Zkontrolovat návrat“.

Tímto způsobem se na objednávku pronájmu vytvoří štítek „Vrácený“.

Tisk a vyzvednutí potvrzení o převzetí
================================

Při vyzvednutí a vrácení půjčovného lze vytisknout potvrzení pro zákazníka.
Produkty.

Pro tisk výzvy k vyzvednutí a/nebo vrácení zásilky přejděte na příslušnou objednávku pronájmu, klikněte na
:guilabel:`⚙️ (převodovka)` ikona, která odhalí rozbalovací nabídku.

.. obrázek: pronájem/tisk-vyzvednutí-vrácení-přijetí.png
:align:center
:alt:Tisk převzetí a vrácení zboží v aplikaci pronájmu Odoo.

Vyberte možnost „Tisk“ z rozbalovací nabídky, abyste zobrazili podnabídku. Pak vyberte
:guilabel:`Potvrzení o převzetí a vrácení“.

Odoo vytvoří a stáhne PDF s podrobnými informacemi o aktuálním stavu pronájmu.
položka(y).

.. toctree::
pronájem/správa vkladů
