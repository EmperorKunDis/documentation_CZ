===========================================================
Prodávejte zboží ze skladů v různých lokalitách pomocí virtuálních míst
===========================================================

Zatímco pro menší společnosti může fungovat skladování zásob a prodej z jednoho skladu,
Větší společnosti mohou potřebovat skladovat nebo prodávat z více skladů v různých městech.
lokalit.

Někdy mohou být produkty zahrnuté v jedné objednávce dodány ze dvou (nebo více) skladů.
V Odoo lze produkty z více skladů stahovat k uspokojení poptávky.
*virtuální lokality*.

.. důležité::
Řešení v tomto dokumentu popisují použití virtuálního skladu k vyřizování objednávek.
Vzhledem k tomu, že máte více skladů, je třeba vzít v úvahu následující věci předtím, než se pustíte do práce:

   #Když je pole „Sklad“ nastaveno na virtuální sklad v objednávce prodeje,
adresa virtuálního skladu je uvedena na formulářích pro vyskladnění, balení a dodání zboží, **ne**
skutečné adresy skladu.
   #Každá lokalita má pole „skladové číslo“ (skryté pole). To znamená, že zásoby v virtuálním
sklad nebude součtem zásob skutečných skladů, ale spíše jejich souhrnem.
zásoby v lokalitách, jejichž identifikátor skladu je virtuální sklad.

.. nebezpečí::
Potenciální omezení pro ty, kteří používají:doc:`dva
<../../shipping_receiving/daily_operations/receipts_delivery_two_steps> nebo :doc:`třístupňovou
doručení <../dodání/denní operace/doručení tří kroků>

   #Výstupní nebo balicí zóna na různých formách je chybně označena jako virtuální.
adresa skladu.
   #Pro dvou nebo tříkrokové dodávky není žádný obchvat.
   #Pokračujte pouze v případě, že nastavíte adresu virtuálního skladu jako výstupní nebo balicí zónu.
pro práci firmy.

.. poznámka::
Pro vytvoření virtuálních skladových prostorů a následné kroky je nutné
:guilabel:`Skladovací místa“ a „Složené trasy“ musí být povoleny.

Pro toto nastavení přejděte na: „Nástroje Inventuru --> Konfigurace --> Nastavení“, a pak v dolní části
části „Sklad“ a zapnout „Uložení“.
:guilabel:`Možnosti vícekrokových tras“ a poté stiskněte tlačítko „Uložit“.


... /soupravy/trasy/virtuální-wh:

Vytvořit virtuální místo pro rodiče
==============================

Před vytvořením jakýchkoliv virtuálních skladových lokalit vytvořte novou skladovou lokaci, která bude fungovat jako virtuální.
sklad - místo, kde jsou uloženy fyzické sklady.

..spoiler:: Proč virtuální sklad?

Virtuální sklady jsou ideální pro společnosti s více fyzickými skladovými prostory, protože umožňují
Situace může nastat, když jeden sklad vyprodá zásoby konkrétního produktu, ale v jiném skladě je tento produkt stále k dispozici.
Sklad stále má zásoby skladem. V tomto případě by se mohly použít zásoby z těchto dvou nebo více skladů.
být použita k plnění jediné objednávky.

„Virtuální“ sklad slouží jako jediný agregátor všech zásob uložených ve společnosti.
fyzické sklady a je používán (pro účely sledovatelnosti) k vytvoření hierarchie míst.
v Odoo.

Pro vytvoření nového skladu přejděte na: „Skladování aplikace -> Konfigurace -> Sklady“.
a klikněte na tlačítko „Vytvořit“. Zde zadejte název skladu a jeho zkrácenou verzi.
může být změněna a další podrobnosti o skladu lze změnit v záložce:guilabel:`Sklad
Karta Konfigurace.

Nakonec klikněte na tlačítko „Uložit“ a dokončete vytvoření běžného skladu.
kroků níže dokončit konfiguraci virtuálního skladu rodiče.

.. obrázek: stock_warehouses/stock-warehouses-create-warehouse.png
:align:center
:alt: Nový skladový tvar.

.. viz též:
   - :doc:`Konfigurace skladů <../../warehouses_storage/inventory_management/warehouses>`
   - :ref:`Příchozí a odchozí zásilky <sklad/přijaté_a_odeslané_zásoby_jedním_krokem/wh>“
   - :doc:`../../sklady/dodavky/dodavky_do_skladu`

..._výčet/cesty/dítě-co:

Vytvořit dětské sklady
=======================

Vytvořte alespoň dva *dětské* sklady, které se budou vázat na virtuální sklad.

.. důležité::
Při vyskladňování zboží z více skladů k naplnění objednávky je potřeba mít
mělo by být alespoň dvou skladů, které fungují jako dětské lokality virtuální mateřské lokace skladu.

Pro toto nastavení přejděte na: „Nastavení aplikace Inventura - Výdejny“ a klikněte
:guilabel:`Vytvořit“ a postupujte podle předchozích pokynů „<Inventář/cesty/virtuální-wh>“.
konfigurovat fyzické skladové položky.

.. příklad::

|  **Sklad mateřský**
| :guilabel:`Sklad“: „Virtuální sklad“
| :guilabel:`Lokalita“: „VWH/Sklad“

| **Dětské sklady**
| :guilabel:`Sklady“: „Sklad A“ a „Sklad B“
|:guilabel:`Lokace“: „WHA“ a „WHB“

.. obrázek::stock_warehouses/parent-location.png
:align:center
:alt:Grafické znázornění dětských lokalit „WHA“ a „WHB“, které jsou s rodičovskou lokalitou propojeny.

.. důležité::
Ačkoliv se později změní virtuální skladová poloha na „Zobrazit“, :guilabel:`Skladové místo typu“
*musí* být v tomto bodě nastaveno na „Vnitřní umístění“ a *pak* je možné propojit dětské sklady.
v následujícím odstavci.

... inventář/trasy/odkaz na VWH:

Spojte sklady dětského oblečení s virtuálními zásobami
======================================

Fyzické sklady lze nastavit jako dětské lokality virtuální lokace, kterou je možné nakonfigurovat v
:ref:`předchozí krok <inventory/routes/virtual-wh>`, přejděte do aplikace „Vybavení“
Konfigurace --> Lokality.

Odeberte všechny filtry z vyhledávací lišty. Pak klikněte na fyzickou skladovou položku „Lokalita“
by měl být vytvořen jako dětský objekt (např. WHA) a klikněte na tlačítko „Upravit“.

Změňte pole „Místo“ z políčka „Fyzické umístění“ na virtuální.
Skladovou polohu skladu (např. VWH/Stock) z roletkového menu a klikněte
:guilabel:`Uložit“.

.. důležité::
Vybrat skladovou lokalitu virtuálního skladu v rozevíracím seznamu „Místo“
menu, musí mít svou položku v centrálním skladu (např. „VWH/Sklad“)
:guilabel:`Typ umístění“ nastaven na „Vnitřní umístění“.

.. obrázek: stock_warehouses/configure-physical-wh.png
:align:center
:alt:Nastavte umístění dceřiné skladovny na virtuální skladovnu.

Opakujte předchozí kroky pro konfiguraci dvou nebo více dětských skladů.

Jakmile je proces dokončen, virtuální sklad (např. „VWH / Sklad“) plní objednávky pomocí zásob z
dětské sklady (např. WHA a WHB), pokud není dostatečný zásoby v jedné lokalitě.

Nastavte virtuální skladovou polohu na „zobrazení“
====================================

Nastavte virtuální umístění zásob na „Zobrazení“, protože je
neexistující místo, které slouží k seskupení fyzických skladů.

Pro toto nastavení přejděte na: „Inventářová aplikace --> Konfigurace --> Lokality“.

Klikněte na virtuální skladovou položku (např. „VWH/Sklad“) vytvořenou dříve.
<výčet tras/virtuální zastávky>, ze seznamu „Místa“.

V poli „Další informace“ v záložce „Lokalita“ nastavte
„Typ umístění“ na „Zobrazit“. Uložte změny.

.. obrázek: skladové prostory/zobrazení typu lokace.png
:align:center
:alt: Druhy skladů v okně pro vytváření lokací.

.. tip::
Chcete-li zobrazit celkové množství vázaných skladů pro všechny dětské sklady, přejděte na kartu produktu a
Klikněte na tlačítko „Na skladě“.

.... obrázek: skladové zásoby/skladová dostupnost.png
:align:center
:alt:Zobrazení zásob ve všech propojených skladech.

Příklad: prodávat zboží ze skladu virtuálního
===============================================

Pro prodej produktů z více skladů pomocí virtuální mateřské polohy musí databáze obsahovat
nejméně dvou skladů konfigurováno - s minimálně jedním produktem a zásobami na skladě
skladu, resp.

.. příklad::
Následující produkt „Hračka voják“ je k dispozici na každé prodejně v množství:

   - „WHA/Stock“: 1
   - „WHB/Stock“: 2
   - Skladovací prostory WHA a WHB jsou dětské skladovací prostory virtuálního skladu VWH.

Vytvořte nabídku na produkt, přejděte do aplikace „Prodej“ a klikněte
:guilabel:Vytvořit“. V citaci přidejte :guilabel:Zákazník“ a klikněte na „Přidat produkt“.
sčítat zboží skladované ve dvou skladech.

Poté klikněte na záložku „Další informace“ v objednávkovém formuláři. Pod záložkou „Dodání“
sekci a změnit hodnotu pole :guilabel:`Sklad` na virtuální sklad.
:ref:`dříve vytvořené <inventory/routes/virtual-wh>“. Následně potvrďte objednávku.

.. obrázek: skladovací prostory/sada virtuálních skladů.png
:align:center
:alt:Nastavte virtuální sklad jako pole Warehouse v záložce Other Info objednávky prodeje.

Poté klikněte na tlačítko „Dodání“ a z potvrzovacího formuláře skladu dodávky potvrďte
Hodnota pole „Zdroj“ odpovídá hodnotě pole „Sklad“ z prodeje.
objednávku. Oba by měly uvádět virtuální skladovou lokaci.

Poté v dodacím lístku skladu pod záložkou „Podrobné operace“ potvrďte
V poli „Od“ každého produktu se nachází dětské lokality, které odpovídají hodnotě v poli „Lokalita“.
jejichž virtuální rodiště je v dané zemi.

.. obrázek: skladové zásoby/objednávka dodání.png
:align:center
:alt:Dodací příkaz s odpovídajícími zdrojovými a dětskými lokacemi.

.. důležité::
Záložka „Zdroj“ na dodacím listu skladu a záložka „Sklad“
pod záložkou „Další informace“ v objednávce musí být shodné pro produkty na prodej.
aby se z různých skladů vytáhly objednávky.

  - Pokud virtuální sklad není v poli „Zdroj“ na záložce Sklad,
dodací formě, opakování rezervace produktu:

    - Spouštění plánovače: zapněte si režim vývojáře a poté přejděte na
:menuaplikace:`Správa zásob --> Provoz --> Spustit plánovač.
    - Kliknutím na tlačítko „Zkontrolovat dostupnost“ v objednávce dodání.
  - Pokud virtuální sklad není přiřazen k poli :guilabel:Sklad na prodejně,
Pak objednávku zrušit a vytvořit novou s virtuálním skladem.
:guilabel:`Sklad“ pole.
  - Pokud je pole „Sklad“ na objednávce chybí, pak se dítě
skladovací prostory nebyly správně zřízeny. Přečtěte si :ref:`předchozí část
<inventář/cesty/dítě-co> pro správné nastavení.

.. tip::
Chcete-li použít virtuální místo jako výchozí sklad pro objednávky na prodej, musí každý obchodník
měli by mít virtuální sklad přiřazen z roletky vedle
:guilabel:`Výchozí sklad“ na formuláři pro zaměstnance.

...... obrázek:: skladovna/skladovny-zamestnanec.png
:align:center
:alt:Výchozí sklad na formuláři pro zaměstnance.
