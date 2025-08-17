=========================
Použitím ocenění zásob
=========================

.. inventarizace/hlášení/používání inventáře v hodnotě:

Oceňování zásob je základní účetní operace, která vypočítá hodnotu skladových zásob.
Skladové zásoby. Jakmile je stanovena hodnota ocenění zásob, je pak tato částka zahrnuta do celkové
hodnota.

V Odoo je tento proces možné provádět ručně – skladníci fyzicky spočítají počet
produkty - nebo automaticky prostřednictvím databáze.

Automatická oceňování zásob
=============================

Chcete-li použít Odoo k automatickému generování záznamů o hodnotě zásob, nejprve přejděte na
Vyberte si produktové kategorie přechodem na „Skladové aplikace -> Konfigurace“.
Vyberte kategorii produktů a na formuláři zadejte
„Ocenění zásob“ jako „automatické“ a „Metodu oceňování“ na jakoukoli
z těchto tří možností.

.. viz též:
:doc:`Nastavit způsob oceňování zásob <inventory_valuation_config>`

Abychom pochopili, jak se pohyb produktů na skladě a z něj ovlivňuje celkovou hodnotu společnosti.
Zvažte následující scénář pohybu produktu a zásob.

Přijmout produkt
-----------------

Pro sledování hodnoty vstupních produktů, jako je například jednoduchý stůl, nastavte kategorii produktu na
samotnému produktu. Chcete-li se tam dostat, přejděte na:
Vyberte produkt a klikněte na požadovaný produkt. Na stránce s produktem klikněte na ➡️ (pravý směrný znak)
ikona vedle pole „Kategorie produktu“, která otevře vnitřní odkaz na editaci produktu.
Kategorie. Následně nastavte metodu nákladového účtování na „První do skladu, první z skladu“ (FIFO).
„Oceňování zásob“ jako „Automatické“.

.. tip::
Alternativně přejděte na panel „Kategorie produktů“ pomocí odkazu „:guilabel:Product Categories“.
:menu_selektor:„Aplikace Inventář --> Konfigurace --> Kategorie produktů“ a vyberte požadovanou
produktová kategorie.

Předpokládejme, že se kupují deset stolů za cenu 10 dolarů za kus. Při objednávce
Tyto tabulky ukazují celkovou částku nákupu 100 dolarů a další náklady nebo daně.

.. obrázek: používání inventární hodnoty/objednávka.png
:align:center
:alt:Objednávka na 10 stolů s produkty za 10 dolarů.

Po výběru položky „Zkontrolovat“ v PO (objednávka) se zobrazí „Hodnota“.
je zapnuto tlačítko chytré funkce, po jehož stisknutí se zobrazí hlášení s výpisem toho, jak je sklad
Hodnota stolu se tímto nákupem zvýšila.

.. důležité::
:ref:`Rozvojový režim <developer-mode>` **musí být zapnutý**, aby bylo možné vidět hodnotu :guilabel:`Ocenění`.
chytrý tlačítko.

.. tip::
Funkce „Převzetí zásilky“ umožňuje
vlastnictví k položkám skladu. Proto produkty vlastněné jinými společnostmi nejsou zahrnuty do
inventarizaci majetku vlastní společnosti.

.. obrázek:: používání inventarizační hodnoty / ocenění chytré tlačítko.png
:align:center
:alt:Zobrazení tlačítka Smart valuation na účtence s povoleným režimem vývojáře.

Pro komplexní přehled s vyčíslením hodnoty zásob včetně všech dodávek produktů
Inventarizační úpravy a skladové operace se týkají hodnotící zprávy o zásobách.
<Inventarizace/správa/hlášení/hodnotící zpráva>.

Dodat produkt
-----------------

V logice stejného principu, když se stůl dodá zákazníkovi a opustí sklad, zásoby
hodnota se snižuje. Tlačítko „Ocenění“ na tlačítku „DO (Dodací objednávka)“,
Stejně tak zobrazuje hodnotu zásob stejným způsobem jako na :abbr:`PO (Purchase Order)`

.. obrázek:: používání inventarizační hodnoty / snížená hodnota zásob.png
:align:center
:alt:Odhadní hodnota zásob po odeslání produktu.

… inventarizaci, správu, hlášení a vykazování ceny.

Inventarizační zpráva
==========================

Pro zobrazení aktuální hodnoty všech produktů v skladu nejprve zapněte :ref:`Vývojářský režim
Vývojářském režimu a přejděte na: „Nástroje pro správu inventáře“ --> „Hlášení“ --> „Ocenění“.
Dashboard „Ocenění akcií“ zobrazuje podrobné záznamy o produktech s
Datum, množství, jednotková hodnota a celková hodnota.
Inventarizaci.

.. důležité::
:ref:`Rozvojový režim <developer-mode> **musí být zapnutý**, aby bylo možné vidět hodnotu :guilabel:`Ocenění`.
možnost pod položkou: `Zprávy`.

.. obrázek:: používání inventarizační hodnoty / inventarizační hodnota produktů.png
:align:center
:alt:Inventarizační zpráva s více položkami.

Tlačítko „Ocenění k datu“ se nachází v pravém horním rohu obrazovky.
Stránka „Ocenění“ odhaluje okno s hodnotou zásob. V tomto okně je uvedena hodnota zásob
K dispozici během předem stanoveného data lze vidět a vybrat.

.. tip::
Zobrazit podrobné záznamy o hodnotě zásob, pohybu zásob a skladových zásobách vybraného produktu.
tlačítko modré barvy „➡️“ (směřující vpravo) vedle sloupce „Reference“.
hodnota.

...Inventar/Produktverwaltung/Aktualisieren der Einheitspreise:

Aktualizovat cenu jednotky produktu
-------------------------

Pro jakoukoli společnost: dodací lhůty, selhání v dodavatelském řetězci a další rizikové faktory mohou přispět k
neviditelné náklady. I když se Odoo snaží přesně zobrazovat skladovou hodnotu, *manuální ocenění*
Jedná se o další nástroj pro aktualizaci cen produktů.

.. důležité::
Manuální ocenění je určeno pro produkty, které lze zakoupit a přijmout za cenu vyšší než
nebo mít nastavené kategorie produktů s :guilabel:`Způsobem ocenění` nastaveným na buď
:guilabel:`Průměrná cena (AVCO)“ nebo „Nejprve nakoupené, nejdříve prodané (FIFO)“.

.. obrázek: používání inventarizační hodnoty / přidat ruční ocenění.png
:align:center
:alt:Přidat manuální ocenění zásob do produktu.

Vytvořte manuální účetní záznamy na panelu „Ocenění zásob“ pomocí následujícího postupu:
:menuvolba:„Skladové zásoby -> Zprávy -> Ocenění“. Poté je třeba povolit *produkt
funkce přehodnocení, vyberte: menuselection: „Skupina podle --> Produkt“ a uspořádejte všechny záznamy
produkt. Klikněte na šedý ikonu „▶️ (svislá čárka)“ pro zobrazení linie hodnoty akcií
pod ní i modrý tlačítko s plusem („+“) vpravo.

Klikněte na modrý tlačítko „+“ (plus) a otevřete formulář „Revalvace produktu“.
Zde lze ocenění zásob zboží znovu vypočítat zvýšením nebo snížením
jednotkové ceny jednotlivých produktů.

.. poznámka::
Vizuální znázornění tlačítka „▶️ (svislý trojúhelník)“ a „➕ (plus)“ je viditelné pouze po
skupinování položek podle produktu.

.. obrázek:: používání inventarizace a znovuhodnocení produktů.png
:align:center
:alt:Formulář pro přepočet ceny s přičtením hodnoty 1 USD kvůli inflaci.

Účetní záznamy o inventarizaci
-----------------------------------

V Odoo se automaticky evidují i záznamy o účetní hodnotě zásob v poli :menuselection:`Účetnictví
app --> Účetnictví --> Dashboard záznamů o účetních operacích. Na tomto komplexním seznamu účetních vstupů
Hodnoty záznamů o inventarizaci jsou identifikovány kontrolou hodnot v sloupci „Deník“.
hledá hodnotu sloupce „Odkaz“ s odpovídajícím odkazem na skladovou operaci
(např. „WH/IN/00014“ pro faktury).

Kliknutím na záznam o inventarizaci se zobrazí záznam účetnictví s dvojitým vstupem.
účetní záznamy vytváří Odoo, aby sledoval změnu hodnoty skladových zásob při prodeji produktů.
Přicházeli a odcházeli z skladu.

.. příklad::
Pro zobrazení hodnoty zásob při příjmu 10 stolů za 10 USD každý
dodavatel, přejděte na stránku „Účetní záznamy“ v aplikaci „Účetnictví“.
-->Účetnictví --> Účetní operace. Zde klikněte na účetní řádek s položkou :guilabel:`Zdroj
hodnota sloupce odpovídá referenci na faktuře „WH/IN/00014“.

...... obrázek:: používání inventarizační ocenění / skladová hodnota produktu.png
:align:center
:alt:Stránka hodnotící cenu zboží v rámci dodávky.

„Stock Interim“ je účet, na který se přesouvá peníze určené k zaplacení dodavatelům za zboží.
„účet ocenění zásob“ uchovává hodnotu všech skladových zásob.

..... obrázek:: používání inventarizační hodnoty / vstup do inventarizační hodnoty.png
:align:center
:alt:Účetní záznam k ocenění majetku v hodnotě 10 stolů.

.. viz též:
„Tutoriál Odoo: Hodnota zásob <https://www.odoo.com/slides/slide/2795/share>“
