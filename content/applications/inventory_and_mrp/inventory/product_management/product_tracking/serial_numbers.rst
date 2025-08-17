==============
Seriové číslo
==============

„Sériové číslo“ je jedním ze dvou způsobů identifikace a sledování produktů v Odoo, spolu s
:doc:`mnoho <many>“. Sériové číslo je jedinečný identifikátor, který výrobci přiřazují produktům k rozlišení
z jiných výrobků stejné série. Sériové číslo může být složeno z několika různých typů znaků:
obsahovat čísla, písmena, další typografické znaky nebo jakoukoli kombinaci těchto znakových typů.

Díky přidělování sériových čísel lze sledovat jednotlivé produkty a jejich
datum expirace <expiration_date> a umístění v dodavatelském řetězci. Například
Sériové číslo může pomoci výrobcům najít produkty, které mají poskytnout pozáruční servis.
akce vzpomínky.

.. viz též:
„Tutoriály Odoo: Sériové číslo <https://www.youtube.com/watch?v=XWJjWc0Vl04>“

...Inventarizace/Správa produktů/Zapnout sady:

Zapněte položky a sériové čísla
============================

Pro sledování produktů pomocí sériových čísel je zapotřebí zapnout dvě nastavení: :ref:`Série
Nastavení sledovatelnosti čísla výrobku <inventory/product_management/traceability-setting>, a :ref:`sériové
číslo použité pro typ operace (výpočetní inventář/správa produktů/nastavení typu operace).

.. inventarizaci, správu produktů a nastavení stop:

Nastavení stopovatelnosti
--------------------

Funkci „Sledování sériových čísel“ je nutné nejprve zapnout, aby bylo možné sledovat
produktů. Chcete-li tak učinit, přejděte na: „Nastavení aplikace Inventární software“ - „Konfigurace“ - „Nastavení“, posuňte se dolů
do sekce „Sledovatelnost“ a zaškrtněte políčko „Čísla šarží“.
Pamatujte na kliknutí tlačítka :guilabel:`Uložit`, abyste změny uložili.


.. obrázek: enabled_settings.png
:alt:Povolení nastavení sériových čísel a lotů.

...Inventar/Produktverwaltung/Operationstyp festlegen:

Dle typu operace
-----------------

Dále zvolte, jestli chcete zapnout možnost vytvářet nové nebo používat existující sériové číslo
pro konkrétní typy operací (například pro dodání nebo přijetí zboží).
umožňuje sledování sériových čísel na fakturách o přijetí zboží a dodacích listech.

.. příklad::
Zapnutím možnosti „Vytvořit nový“ pro faktury umožňuje přiřazení nových sériových čísel
Jakmile jsou položky přijaty, ale pro dodací objednávky je často vypnutá, aby se pracovníci nemohli
přidělování sériových čísel, které nejsou v zásobách k dispozici.

Pro vytvoření nových sériových čísel při provádění operace přejděte na:
app --> Konfigurace --> Typy operací.

Vyberte požadovaný typ operace (např.
„Faktury“, „Dodací listy“ nebo „Výrobní příkazy“) a vyberte
Možnost „Vytvořit nový“ v sekci „Sériová čísla / Loty“ operačního typu
konfigurační stránka.

.. obrázek: serial_numbers/create-new-setting.png
:alt:V operaci Typy účtenek je vybrána možnost „Vytvořit novou“.

...Inventar/Produktverwaltung/Detaillierte Operationen:

Nastavte sledování sériových čísel na jednotlivé produkty
=======================================================

Jednou z možností je nastavení „Sériové číslo a sériová čísla“ (<inventory/product_management/traceability-setting>).
byla aktivována funkce sledování jednotlivých produktů pomocí sériových čísel.
Přejděte na: „Nastavení aplikace - Vybrané položky - Produkty“ a vyberte požadovaný produkt.

V sekci „Obecné informace“ v kartě produktu zkontrolujte, že je zaškrtnuté políčko vedle
Zkontrolujte položku „Inventář“ a pak vyberte možnost „Podle jedinečného sériového čísla“.
:guilabel:`Uložit“ k uložení změn. Nyní lze vybrat stávající nebo nové sériové čísla.
přiřazené k nově dodaným nebo vyrobeným dávkám tohoto produktu.

.. obrázek: sériové číslo/sledování produktu.png
:alt:Aktivovali sledování sériových čísel na produktovém formuláři.

...Inventar/Produktverwaltung/Zuweisung der Seriennummer:

Přidělte sériové číslo
=====================

V Odoo lze sériové číslo přiřadit na více místech a v různých časech:

- Pokud je produkt již skladem (viz. inventář/správa produktů/již skladem)
- Přes tlačítko „Chytré pohyby“ na faktuře
- V okně přijaté faktury prostřednictvím tlačítka „Přesun skladu“
- Během výrobního příkazu
<../../../manufacturing/basic_setup/configure_manufacturing_product> pro produkt sledovaný
čísla výrobních sérií
- Když provedete inventarizační úpravu


... skladové zásoby/správa produktů/dostupné na skladě:

Vytvořit nové sériové čísla pro produkty již skladované
-------------------------------------------------------

Nový sériový číslo lze vytvořit pro produkty, které jsou již skladem a nemají přiřazené sériové číslo.
klikněte na „Skladové zásoby“ -> „Produkty“ -> „Sériová čísla“.
:guilabel:„Nový“. To odhalí prázdnou řádkovou položku pro sériové číslo. Na této položce se objeví nové
„Číslo šarže“ a „číslo losu“ se generují automaticky.

.. tip::
Pokud je v systému Odoo nastaven automatický generátor čísla sériového čísla, který bude následovat nejnovější číslo,
je možné upravit a změnit na jakýkoliv požadovaný počet kliknutím na čáru pod
:guilabel:`Číslo sériového čísla“ pole a změnit vygenerované číslo.

Jakmile je vygenerován požadovaný kód, klikněte na prázdné pole vedle
Klikněte na tlačítko „Produkt“ pro zobrazení rozbalovací nabídky. V této nabídce vyberte produkt, ke kterému chcete přidat nový
bude přiděleno.

Tento formulář také nabízí možnost upravit „Množství na skladě“ a přiřadit jedinečné
:guilabel:„Vnitřní odkaz“ (pro další sledovatelnost) a přiřadit tento konkrétní
konfiguraci čísla/sériového čísla pro konkrétní společnost do pole „Společnost“.
popis konkrétního kusu můžete také přidat v záložce „Popis“.
dále.

.. tip::
Políčko „Vnitřní odkaz“ je místem pro výrobce, kde mohou zadat číslo.
další jedinečné číslo pro snadnější sledování. Například mohou být použity hodnoty SKU
zde.

Po dokončení všech požadovaných konfigurací klikněte na tlačítko :guilabel:`Uložit`, abyste uložili všechny změny.

.. obrázek: sériové číslo/nové sériové číslo.png
:alt:Vytvořeno nové sériové číslo pro již existující zásobu produktu.

Po vytvoření nového sériového čísla, přiřazení požadovaného produktu a uložení se přesuňte
zpět do produktové podoby přejděte na: „Inventář aplikace --> Zboží --> Zboží“.
vybrat produkt, který byl právě přiřazen k novému sériovému číslu.

Na stránce s podrobnostmi o produktu klikněte na tlačítko „Číslo šarže“ a zobrazí se vám nové
sériové číslo.

.. _skladové hospodářství / řízení zásob / příjmový a výdejový sklad:

Vytvořit sériové číslo pro příchozí nebo odchozí produkty
-------------------------------------------------------

Sériové číslo lze přiřadit jak k přijatým, tak i odeslaným zbožímu. Při příjmu a výdeji se používají příkaz k přijetí a dodání
formuláře odrážejí se navzájem, pokyny níže mohou být použity k přiřazení sériových čísel v kterémkoli
forma.

- Příchozí zboží: přiřaďte sériové číslo přímo na faktuře. Faktury lze přistupovat
navigace do:menu-vyber->Skladové aplikace -> Objednávky -> Přijaté objednávky.
- Výdejky: přiřaďte sériové číslo přímo na dodací list. Příjemky můžete
Přístup k ní je možný po rozkliknutí položky „Skladové zásoby -> Provoz -> Přepravy“.

.. důležité::
Před přidělením sériových čísel na fakturách nebo dodacích listech se ujistěte, že máte schopnost
:ref:`vytvářet nové sériové čísla operací typu
je zapnutá.

Kolonka pro číslo sériového čísla
~~~~~~~~~~~~~~~~~~~~~~~~

Sériové číslo lze zadat přímo do pole „Sériové číslo“ na faktuře nebo
dodací list.

.. obrázek: sériové číslo/vlož do pole.png
:alt:Vyberte hodnotu pro pole sériového čísla na faktuře.

.. tip::
Chcete-li zobrazit pole „Sériové číslo“ na faktuře nebo dodacím listě, klikněte na
:ikonka: „Nastavení“ (Settings) ikona a v rozbalovacím menu zaškrtněte
zatrhněte políčko „Sériové číslo“.

.. obrázek:: serial_numbers/field-visible.png
:alt:Povolit pole sériových čísel na faktuře nebo dodacím listě.

Příklad pole sériových čísel v objednávce dodání.

.. inventář/správa produktů/pohyb zásob:

Pop-up okno pro přesuny zásob
~~~~~~~~~~~~~~~~~~~~~~~~

Pro různé metody přiřazování sériových čísel jednotlivě nebo ve velkém množství klikněte na ikonu „fa-list“
:guilabel:`(seznam)` ikona v produktové řadě faktury.

Přidejte řádek
**********

V okně „Přesun otevřeného skladu“ ručně zadejte sériové číslo do
:guilabel:`Číslo šarže“ sloupec. Tento způsob je vhodný pouze pro přidání jednoho nebo několika
sériové číslo.

.. obrázek: sériové číslo/přidání řádku vstupu skladu.png
:alt:Přidejte řádek do okna přesunu zásob.

…_skladové zásoby/správa produktů/generování sériových čísel:

Vytvořit sériové čísla
*********************

Přidat více sériových čísel najednou kliknutím na tlačítko „Vytvořit sériové číslo“.
pop-up okno „Přesun otevřeného skladu“.

.. obrázek: sériové číslo/dodávka-převádí-sériová-čísla.png
:alt:Zobrazit okno pro generování sériových čísel.

Provedením takového kroku se otevře nové okno s názvem „Vytvořit sériové číslo“, které obsahuje několik políček:

- :guilabel:První sériové číslo: Zadejte první sériové číslo, které má začít sekvenci.
Odoo automaticky detekuje, jaký vzor by měl být použit k generování dalších sériových čísel.
- :guilabel:`Počet sériových čísel“: Zadejte požadovaný počet sériových čísel, které chcete vytvořit.

.. poznámka::
Počet vytvořených sérií bude zobrazen v poli „Kusy“ na
faktura nebo dodací list. I když počet sériových čísel vygenerovaných převyšuje
:guilabel:"Požadavek" hodnota, Odoo stále umožňuje množství (na základě sériových čísel)
doručeno nebo přijato.

.. obrázek: sériové číslo/dodávka-pohyb-výroba-množství-tip.png
:alt:Zobrazte, jak se mění množství sériových čísel a objednávka na dodání.

- Zatrhněte políčko „Ponechat stávající sériové číslo“: Zatrhnutím tohoto políčka se udrží původní sériová čísla, která mohou
jsou již dříve přidány. Chcete-li nahradit stávající sériové číslo v seznamu, nechte zaškrtnuté
bez kontroly.

Po vyplnění těchto polí stiskněte tlačítko „Vytvořit“. Nově vytvořené sériové číslo
nyní se zobrazují v okně „Přesun do skladu“. Po kliknutí na ikonku
„Uložit“ (tlačítko „Uložit“), „Množství“ a „Sériové číslo“ v poli
doručovací příkaz nebo potvrzení o převzetí se automaticky aktualizují.

Import sériových čísel/dodávek
*******************

Další možnost přiřazení více sériových čísel najednou je kliknutím na tlačítko „Import
Tlačítko „Sériové číslo/Číslo šarže“ v okně „Přidat pohyb zásob“.

.. důležité::
Pokud tlačítko pro import není viditelné, ujistěte se, že je zaškrtnutá možnost „Vytvořit nový“ v
:ref:`stránka konfigurace účtenky <inventory/product_management/operation-type-setting>“.

Tím se otevře okno „Přidat sériové číslo“. Každé sériové číslo zadejte na samostatnou řádek.
řádku v poli „Sériové číslo“.

Jak je tomu u generování sériových čísel, viz příkaz
Zatrhněte políčko „Udržet stávající sériové číslo“ pro zachování stávajících sériových čísel nebo nechte pole prázdné.
přepsat je.

.. tip::
Pro urychlení procesu zkopírujte sériové čísla ze stávajícího sešitu a přidejte je do
pole „Číslo šarže“.

V neposlední řadě klikněte na tlačítko „Vytvořit“.

.. obrázek: sériové číslo/dodávka importu sériových čísel.png
:alt:Zobrazit okno s čísly importu.

.. příklad::
Pro fakturu s požadavkem „3.00“ produktů je již jedna položka přiřazená
sériové číslo v okně „Přesuny zboží“ (pop-up).

V okně „Dodávka“ se dvě sériová čísla „124“ a „125“.
přiřazené k zbytku produktů vložením následujícího do pole :guilabel:`Lot/Sériové číslo
pole pro zadání čísla:

... blok kódu::

      124
      125

Volba „Udržet aktuální řádky“ je vybrána, aby se k těmto dvěma sériovým číslům přidaly.
přidat k již přidělenému sériovému číslu „123“.

.. obrázek: import_sériové_číslo.png
:alt:Zobrazte příklad správného zadání sériových čísel do textového pole.

...Inventar/Produktverwaltung/Umzugstaste:

Podrobná operace
~~~~~~~~~~~~~~~~~~~

Stránka „Podrobné operace“ je dostupná z obou formulářů pro přijetí i dodání a ukazuje
podrobné informace o pohybu produktu včetně sériových čísel a přesných lokalit.
datum spotřeby atd. Tato úroveň podrobností umožňuje přesnější sledování například při
zpracování zboží s omezenou trvanlivostí nebo podléhajícího kontrole.

Pro přístup k této stránce nejprve vyberte skladovou zásobu nebo dodací list.
Vyberte „Inventář / Produktový management / Přijaté a vydané produkty“. Pak klikněte na ikonu „fa-bars“
:guilabel:„Pohyby“ chytře umístěný tlačítko na horní části stránky.

V sloupci „Číslo šarže“ ručně zadejte (nebo vyberte ze seznamu)
požadované sériové číslo každého jednotlivého výrobku.

.. obrázek: serial_numbers/move-button.png
:alt:Zobrazit podrobné informace o pohybech.

Po dokončení klikněte na chlébové zbytky faktury nebo dodacího listu a přiřazené sériové číslo jsou
Uloženo automaticky.

Na dodacích listech uvádějte sériové číslo
========================================

Při prodeji zboží sledovaného pomocí sériových čísel je možné uvést sériové číslo na
doručené faktury zákazníkům. To může být pro zákazníky užitečné v případech, kdy se jedná o sériové číslo
například podání žádosti o vrácení zboží nebo opravu nebo registraci produktu.

Přidat sériové číslo na dodací lístek otevřete aplikaci „Sklad“ a přejděte
:menu:Konfigurace --> Nastavení. Vyhledejte sekci :guilabel:Sledovatelnost
Zatrhněte políčko „Zobrazit čísla a sériová čísla na fakturách“ a klikněte
:guilabel:`Uložit“.

Po zapnutí nastavení „Zobrazit sériové číslo a množství na dodacích listech“ se zobrazuje
čísla jsou uvedena na dodacích listech pro zboží sledované čísly výrobních šarží, a to jednou za dodací objednávku.
je ověřován.

Pro zobrazení sériových čísel v objednávkách a dodacích listinách přejděte na
Aplikaci „Inventář“ otevřete kliknutím na „Příjemky“ a vyberte příjemku obsahující
produkt sledovaný pomocí sériových čísel.

Pro zobrazení sériových čísel produktů v objednávce je nutné zajistit, aby se na obrazovce nacházel řádek „Operace“.
klikněte na ikonu „Nastavení (upravit)“ vedle
tabulka. Zajistěte si zaškrtnutí položky „Sériové číslo“, což způsobí
Sloupec „Sériové číslo“ se objeví. Sériové číslo (čísla) každého produktu, který je součástí
V této sloupci jsou zobrazeny objednávky.

Když je objednávka připravena k zpracování, klikněte na tlačítko „Potvrdit“ pro potvrzení dodání a přidání
informace o produktu na dodací lístek.

V horní části řádku příkazů klikněte na tlačítko „Akce“ (viz ikona „fa-cog“) a vyberte
:menuselection:`Tisk --> Přepravní list“. Poté se přepravní list stáhne. Otevřete přepravní
přes prohlížeč nebo správce souborů zařízení. Sériové číslo je uvedeno vedle příslušného
v sloupci „Číslo šarže“.

.. obrázek: sériové číslo / dodací lístek.png
:alt:Část objednávkového lístku se seznamem položek, ukazující produkt a jeho sériové číslo.

Sledovatelnost a hlášení
========================

Výrobci a společnosti mohou odkazovat na panel „Sériové čísla“ a sledovatelnost
předává zprávy o celém životním cyklu produktu: kdy a kde vznikl, kde byl uložen.
a komu byla zaslána.

Dashboard sériových čísel
-----------------------------

Pro zobrazení celé sledovatelnosti produktu nebo skupiny podle sériových čísel přejděte na
Vyberte v nabídce „Aplikace inventáře“ -> „Produkty“ -> „Sériová čísla“. To zobrazí
Dashboard „Sériové číslo“.

Reportáž
~~~~~~~~~

Na panelu „Sériové číslo“ jsou produkty s přiřazeným sériovým číslem
je uveden jako výchozí. Klikněte na ikonu „fa-caret-right“ (rozbalit) pro zobrazení sériového čísla
Číslo se přiřadí k vybranému produktu.

Skupina podle sériových čísel (nebo šarží) je možná, pokud nejprve odstraníte všechny výchozí filtry z vyhledávací lišty.
v pravém horním rohu. Poté klikněte na ikonu „fa-caret-down“ (spodní šipka) a vyberte
„Přidat vlastní skupinu“, což odhalí malé rozbalovací menu. Z tohoto malého rozbalovacího menu
Vyberte položku „Číslo šarže“ a klikněte na „Použít“.

Tím se zobrazí všechny existující sériové čísla a šarže. Každá řádka může být rozšířena, aby bylo možné zobrazit všechna
množství produktu přiřazené k danému sériovému číslu. U jedinečných sériových čísel, která nejsou
opakovaně použitelné, mělo by být jedno zboží na jeden sériový číslo.

.. obrázek: sériové číslo/sériová čísla - dashboard.png
:alt: Stránka s čísly výrobku a seznamy s možností výběru.

.. tip::
Pro další informace o konkrétním sériovém čísle klikněte na řádek
položka pro zobrazení konkrétního čísla sériového čísla, které se zobrazí v tomto
formulář, klikněte na tlačítko „Lokalita“ a „Sledovatelnost“, abyste viděli všechny zásoby.
v rámci daného sériového čísla a všech operací provedených pomocí tohoto sériového čísla.

.. viz též:
:doc:`Přidělení <reassign>`

Kromě používání panelu „Sériové číslo“ lze využít i několik dalších možností.
šablony reportů, které zobrazují pole „Číslo sériového čísla“ nebo schopnost filtrovat
podle sériového čísla. Přejděte na: „Nástroje pro správu inventáře“ -> „Hlášení“.

   - :guilabel:`Lokace“
   - :guilabel:Historie pohybů
   - :guilabel:`Analýza pohybů“
