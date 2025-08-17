================
Pravidla pro přeskupování
================

.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`
.. |SOs| nahradit za: zkratka: `SOs (Sales Orders)`
.. |RFQ| nahradit za: zkratka: „RFQ (Request for Quotation)“
.. |RFQs| nahrazuje: zkratka: RFQs (požadavky na nabídku)
.. |PO| nahradit za: :abbr:`PO (Příkaz k nákupu)`
.. |POs| nahradit za: zkratka: `POs (Purchase Orders)`
.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`
.. |MOs| nahradit za:: :abbr:`MOs (Výrobní objednávky)`
.. |BoM| nahradit za: :abbr:`BoM (Seznam materiálů pro výrobu)“
.. |BoMs| nahradit za: :abbr:`BoMs (Seznamy materiálů)`
.. |upravit| nahradit:: :ikonka:`oi-settings-adjust` :guilabel:`(upravit nastavení)`

Pravidla pro přeřazování se používají k tomu, aby předpovězené zásoby byly nad určitou hranicí bez
překročení stanovené horní hranice. Toto je dosaženo tím, že se stanoví minimální množství skladovaného zboží.
a maximální množství, které by zásoby neměly překročit.

Pravidla pro přeskupení lze nastavit pro každý produkt podle cesty, kterou se doplňuje. Pokud
Pokud je produkt využíván pomocí cesty „Koupit“, pak se vytvoří požadavek na nabídku (RFQ), když dojde k opětovnému objednání.
povolení je aktivováno. Pokud produkt používá cestu *Výroba*, pak se vytvoří „objednávka na výrobu“ (MO).
takže se vždy vygeneruje nový.

.. viz také:
   - „Tutoriály Odoo: Automatické pravidlo pro opětovné objednávání <https://www.youtube.com/watch?v=XEJZrCjoXaU>“
   - „Tutoriály Odoo: Ruční nastavení pravidel pro přesuny položek <https://www.youtube.com/watch?v=deIREJ1FFj4>“

Pro nastavení pravidel pro opětovné objednávání se podívejte na:

- :ref:`Nastavení pravidel pro přeskladnění <inventory/warehouses_storage/configure-rr>“
- :ref:`Spoušť <inventář/sklady/spoušť>“
- :ref:`Přednostní trasa <inventory/warehouses_storage/route>“

Chcete-li pochopit a optimalizovat doplňování pomocí pokročilých funkcí, podívejte se na:

- :ref:`Logika just-in-time <skladování/sklady/just-in-time>“
- :ref:`Dny viditelnosti <inventory/warehouses_storage/visibility-days>“
- :ref:`Dny horizontu <skladovani/horizontni-dny>`

...Inventář, skladování a konfigurace RR:

Nastavení pravidel pro přeskupování
======================

Pro nastavení automatických a manuálních pravidel pro přeřazování dokončete následující:

#:ref:`Konfigurace produktu <skladové zásoby/sklady a skladování/nastavení produktu>`
#:ref:`Metoda doplňování zásob <skladové prostory a skladování/doplňování zásob/metoda setování>“
#:ref:`Vytvořit pravidlo <inventory/warehouses_storage/rr-fields>“

.. skladovací prostory / sklady / typ produktu:

Konfigurace produktu
--------------------------

Pro použití pravidel znovuplnění je produkt nutné správně nakonfigurovat. Začněte tím, že se přesunete na
Vyberte aplikaci „Správa skladu“ -> „Zboží“ -> „Zboží“, pak vyberte existující zboží nebo vytvořte nové.
nový kliknutím na „New“.

V produktové formě pod záložkou „Obecné informace“ nastavte typ produktu.
„Zboží“ a ujistěte se, že zaškrtnete políčko „Sledování zásob“.
nutné pro sledování zásob a spouštění pravidel opětovného objednávání.

.. obrázek: reordering_rules/product-type.png
:alt: Konfigurace produktu a skladových zásob.

... skladovací prostory, včetně metody nastavení:

Metoda doplňování
--------------------

Poté nastavte způsob doplňování zásob (např. nákup nebo výroba).

Pokud je produkt zakoupen, nainstalujte aplikaci Purchase a potvrďte, že
Vedle názvu produktu je aktivní zaškrtávací políčko „Koupit“. V „Koupit“
vložte alespoň jednoho dodavatele do ceníku „cena dodavatelů“ (dokumentace: Ceník dodavatelů).
Odoo používá dodavatele na prvním místě v seznamu k generování požadavků na nabídku (RFQ) při spouštění pravidel pro znovupodání.

V poli „Trasy“ v záložce „Sklad“ zaškrtněte políčko „Koupit“.

.. viz také:
:doc:`Seznam dodavatelů <../../../purchase/suppliers/list>`

Pokud je produkt vyrobený, nainstalujte aplikaci **Výroba** pomocí příkazu „instalovat“ a
v poli „Trasy“ záložky „Sklad“, zaškrtněte pole „Výroba“.

Dalším krokem je zajistit alespoň jeden „seznam součástek“
V seznamu BoM je zobrazena v položce „Faktura“ (BoM).
tlačítka chytrého výrobku na horní části produktového formuláře. To je nutné, protože Odoo pouze
Vytváří výrobní objednávky (MO) pro produkty s BoM.

Pokud již neexistuje BOM pro produkt, klikněte na tlačítko „Bill of Materials“
tlačítko, pak klikněte na „Nový“ pro konfiguraci nového |BoM|.

.. viz také:
:doc:`Konfigurace BoM <../../../manufacturing/basic_setup/bill_configuration>`

... skladovací prostory, sklady a pole RR:

Vytvořte nová pravidla pro přeskupování
---------------------------

Pro vytvoření nového pravidla pro přeskupování se přihlaste do aplikace „Sklad“ - „Operace“.
Náhradní plnění“, pak klikněte na „Nový“ a vyplňte následující pole pro nové doplnění.
pravidlo řádku položky:

- :guilabel:`Produkt“: Produkt, který se doplňuje podle pravidla.
- :guilabel:`Lokalita“: Místo, kde je produkt skladován.
- :guilabel:`Minimum“: Minimální množství, které lze předpovědět bez použití pravidla
spuštěna. Když předpovězený počet kusů klesne pod tuto hodnotu, je vystaven příkaz na doplnění zásob tohoto produktu.
vznikla.
- :guilabel:`Maximum“: Maximální množství, které se do zásobníku přidává.
- :guilabel:`Množství v balení“: Pokud se má produkt objednat ve specifickém množství, zadejte
číslo, které je třeba objednat. Například pokud je nastavené číslo :guilabel:`Multiple Quantity` na 5,
a stačí jich tři, doplňuje se pět produktů.

.. obrázek:: reordering_rules/reordering-rule-form.png
:alt:Formulář pro vytvoření nového pravidla pro přeskupování.

Formulář pro vytvoření nového pravidla pro přeskupování.

..tip:
Řádky mohou být také vytvořeny z tlačítka „Pravidla přeskupování“ na panelu nástrojů :guilabel:`Reordering Rules`.
výrobní podobě.

.. poznámka::
Aby se naučili, jak fungují pole „Na skladě“, „Předpověď“ a „K dispozici k objednání“.
používají na skladových zásobách a budoucí poptávce, viz :ref:`Logika just-in-time
oddílu „Skladování a zásoby“.

Pro pokročilé použití se dozvíte více o následujících polích pro přeskupení pravidel:

- :ref:`Spoušť <inventář/sklady/spoušť>“
- :ref:`Přednostní trasa <inventory/warehouses_storage/route>“
- :ref:`Dodavatel <inventory/warehouses_storage/set-vendor>`
- :ref:`Seznam materiálů <sklad/výrobní prostory/složka bom>“
- :ref:`Skupina nákupu <skladování/sklady/nákupní skupina>`
- :ref:`Dny viditelnosti <inventory/warehouses_storage/visibility-days>“

.. poznámka::
pole nad nimi nejsou k dispozici v základním nastavení a musí se zapnout výběrem možnosti |upravit|
a vyberte si požadovanou sloupec z roletky.

.. skladové zásoby/sklady/nula nula:

Pravidlo pro přeřazení 0/0/1
---------------------

Pravidlo 0/0/1 je speciální pravidlo používané k doplnění produktu, který není skladován.
v případě potřeby, pokaždé když je potvrzena objednávka na prodej (PO).

.. důležité::
Pravidlo pro přeskupení 0/0/1 je podobné pravidlu „Dodání na objednávku“ (MTO), protože oba
workflowy se používají k doplnění produktu po potvrzení SO.

Hlavní rozdíl mezi těmito dvěma metodami je ten, že trasa „Doplnit na objednávku“ automaticky
vyhrazuje produkt pro |SO|, které způsobilo jeho doplnění. To znamená, že produkt
nelze použít pro jiný |SO|.

Pravidlo pro přeskupení 0/0/1 tento problém nemá. Produkt doplněný podle tohoto pravidla není omezen na
nejsou vyhrazeny pro žádný konkrétní |SO| a mohou se používat podle potřeby.

Další klíčovou odlišností je, že objednávky doplňování vytvořené cestou Replenish on Order jsou
spojené s původním SO tlačítkem na horní části objednávky. Při použití 0/0/1
pravidlo přeřazení, vytvoří se nová objednávka doplňování zásob, ale nebude spojena s původní objednávkou |SO|.

Podívejte se na dokumentaci „Dodání na objednávku (MTO)“ pro podrobnější informace o trase MTO.

Pro vytvoření pravidla pro přeskládání 0/0/1 přejděte do sekce „Inventář aplikace“ - „Produkty“.
Produkty“ a vyberte produkt.

V horní části stránky s produktem klikněte na ikonu „fa-refresh“ a poté na „Reordering Rules“.
tlačítko pro otevření stránky s pravidly pro přeskupování produktů. Na výsledné stránce klikněte
:guilabel:Nový“ začít konfigurovat nové pravidlo pro přeskupení.

V poli „Lokalita“ nového pravidla pro přeskupení vyberte lokaci, ve které
Doplněné produkty by měly být uloženy. Výchozí umístění je nastaveno na :guilabel:`WH/Stock`.

V poli „Trasa“ vyberte trasu, kterou by mělo pravidlo používat k doplnění předmětu.
Příklad: pokud má být produkt zakoupen u prodejce, vyberte trasu „Koupit“.

V poli „Min“ a „Max“ nechte hodnoty nastavené na 0,00.
V poli „Počet“ zadejte hodnotu 1,00.

.. obrázek:: reordering_rules/001-rule.png
:alt:Pravidlo pro přeřazení 0/0/1.

S konfigurací pravidla znovuřazování pomocí těchto hodnot se při každém |SO| předpokládá
množství produktu klesne pod hodnotu „0,00“, vybraná trasa
se používá k doplnění produktu o jednotky, až do maximální hodnoty 0,00.

Příklad:
Do položky je nastavená pravidlo pro přesměrování s nulovým počtem kusů, které používá trasu „Koupit“.
vždy k dispozici.

A |SO| je potvrzeno pro jednotku, což způsobuje předpovědní množství klesnout na hodnotu -1,00.
Aktivuje pravidlo pro přeřazení, které automaticky vytvoří jednotku |PO|.

Jakmile je produkt přijat od dodavatele, předpokládané množství se vrátí na hodnotu 0,00.
nyní jeden kus skladem, ale není rezervován pro SO, které jej vyvolalo. Může být
použité k plnění této objednávky nebo rezervované pro jinou objednávku.

... inventář/sklady/spouštěč:

Spoušť
=======

Poznámka k přeskupení pravidel může být nastavena na automatické nebo manuální. Obě funkce fungují stejně
Jaký je rozdíl mezi těmito dvěma typy pravidel pro přeskupování?

- „Auto“: Příkaz k nákupu nebo výrobě
je automaticky vytvořen, když se předpokládaný počet kusů sníží pod minimální hodnotu pro nákup.
množství. Výchozím nastavením je vybraná volba „Auto“.
- :ref:`Návod <inventory/warehouses_storage/manual-rr>`: Replenishment report
zobrazuje produkty potřebující doplnění zásob, aktuální a předpokládané množství, čas dodání a příchod.
datumy. Uživatelé mohou před objednáním zkontrolovat předpovědi.

Chcete-li aktivovat pole „Spouštěč“, přejděte do nabídky „Skladové aplikace –> Obsluha –>
Náhrada“. Pak klikněte na „upravit“, umístěné vpravo od nadpisů sloupců, a zaškrtněte
zaškrtávací políčko Trigger.

V poli „Spouštěč“ vyberte možnost „Automaticky“ nebo „Ručně“. Podívejte se na
sekcí níže, abyste se dozvěděli o různých typech pravidel pro přeskupování.

... skladovací prostory/sklady/auto-rr:

Auto
----

*Pravidla automatického přeřazování*, která se spouštějí nastavením pole „Způsob spuštění“ pravidla pro přeřazení na
Pokud je v poli „Auto“ zadáno:

#Scheduler běží a Forecasted množství je pod minimem nebo
#A |SO| je potvrzena a sníží předpokládané množství produktu pod minimální hodnotu.

Pokud je zvolená cesta „Koupit“, pak se vygeneruje |RFQ|. Pro zobrazení a správu |RFQs|
přejít na:menu: „Koupit aplikaci“ --> „Objednávky“ --> „Nabídka“.

Pokud je zvolená cesta „Výroba“, pak se vytvoří |MO|. Pro zobrazení a správu
|MOs|, navigujte na: menu výběr: „Výrobní aplikace -> Operace -> Výrobní objednávky“.

Pokud není vybrána žádná trasa, Odoo zvolí trasu uvedenou v zásobníku.
kartu produktu.

..tip:
Scheduler běží automaticky každý den.

Před spuštěním plánovače ručně vyvolat pravidlo znovusortování. Zajistit :ref:`režim vývojáře
Vývojářský režim je zapnutý a vyberte: Menu -> Inventarní aplikace -> Provoz - > Spustit
Scheduler“. Pak klikněte na modrou tlačítko „Spustit scheduler“ v okně s upozorněním.
Vyskytuje se.

Pozor, tímto se spustí i další plánované akce.

Příklad:
Produkt „Office Lamp“ má nastavenou automatickou pravidla pro opětovné objednávání, která se spustí v okamžiku, kdy bude předpovídán
Když se množství sníží pod hodnotu „Min Quantity“ v hodnotě 5,00, bude zboží
:guilabel:`Předpověď“ je „55,00“, pravidlo přeřazení není spuštěno.

.... obrázek:: reordering_rules/auto.png
:alt:Zobrazit automatickou pravidla pro přeskupování z stránky Pravidlo pro přeskupování.

... skladovací prostory/sklady/manuální RR:

Manuál
------

*Pravidla ručního přeřazování*, která jsou nakonfigurována nastavením pole „Způsob spouštění“ reorderačního pravidla na
:guilabel:`Návod k použití“, zobrazte produkt na „Dashboardu doplňování zásob“ v části
předpokládané množství klesá pod stanovenou minimální hranici. Produkty na této tabulce se nazývají „potřeby“.
protože jsou potřebné k naplnění připravovaných |SOs|, pro které je předpokládané množství nedostatečné.

Dashboard doplňování, přístupný po kliknutí na:
Operace --> Dodávky“, který bere v úvahu termíny objednávek, předpokládané zásoby a dodací lhůty.
Zobrazuje potřeby pouze v případě, že je čas na objednání zboží, díky :guilabel:`To Reorder`.
filtr.

Když se produkt objeví na panelu doplňování zásob, kliknutím na tlačítko „Objednávka“
generuje objednávku nákupu nebo výroby s uvedenými množstvími: guilabel:"K objednání".

.. obrázek: reordering_rules/manual.png
:alt: Klikněte na tlačítko „Plnit zásoby“ v přehledu doplňování zásob, abyste zásoby doplnili.

.. sklad/sklady/skladování/doprava:

Trasa
=====

Odoo umožňuje vybrat více cest jako způsoby doplnění pod
Vyberte položku „Sklad“ v každém produktovém formuláři. Například je možné vybrat obě
„Koupit“ a „Vyrábět“, což ukazuje na to, že produkt lze koupit nebo
vyráběné.

.. viz také:
:ref:`Nastavit trasu na kartě produktu <skladovani/sklady-a-skladovani/nastaveni-trasy-na-kartach-produktu>`

Odoo umožňuje uživatelům nastavit preferovanou trasu pro pravidlo znovupodání produktů.
metoda doplňování (např. nákup nebo výroba), která se použije v případě více možností
k dispozici.

Chcete-li zvolit preferovanou trasu, začněte tím, že se přesunete na:
--> Dodání.

Výchozí nastavení skrývá sloupec „Trasa“. Chcete-li jej zobrazit, vyberte možnost „Upravit“
vlevo od nadpisů sloupců a zaškrtněte položku Route z rozbalovací nabídky, která se objeví.

Klikněte dovnitř sloupce v řádku pravidla přesunu a zobrazí se všechny dostupné
trasy pro tento pravidlo. Vyberte jednu, abyste ji nastavili jako preferovanou trasu.

.. obrázek: reordering_rules/select-preferred-route.png
:alt: Vyberte preferovanou trasu ze seznamu.

.. důležité::
Pokud je pro produkt povolen více způsobů, ale žádný z nich není nastaven jako preferovaný pro jeho doplnění
Pokud je toto pravidlo aktivní, produkt se znovu objedná pomocí trasy „Koupit“ a poté „Výroba“.

Pokročilé použití
-------------

Párování pole „Guilabel“ s jedním z následujících polí v hlášení o doplnění umožňuje
pokročilé konfigurace pravidel přeskupování. Zvažte následující příklad:

.. skladové zásoby, sklady a skladovací prostory:

- :guilabel:Prodávající: Když je vybraná trasa kupována, nastaví se
:guilabel:`Dodavatel“ pole na seznamu cen dodavatele ukazuje Odoo
že dodavatel se automaticky vyplní v případě, když spustí pravidlo pro opakované objednávání.
o nákupní objednávce.

... skladovací prostory, sklady, zásoby, pole bom:

- :guilabel:`Seznam materiálů“: Když je nastavená cesta na „Výrobu“,
V provozu je několik |BoM|, v zásobovacím hlášení lze specifikovat požadovaný |BoM|.
Výrobní objednávky vznikají s použitím tohoto BoM.

... skladování, sklady a nákupní skupiny:

- :guilabel:„Nákupní skupina“: Jedná se o způsob, jak seskupit související |POs| nebo |MOs|, které jsou spojené
splnění specifického požadavku, jako je SO nebo projekt. Pomáhá organizovat a sledovat objednávky
Jsou spojeny s konkrétním požadavkem.

.... poznámka::
Nákupní skupiny propojují způsoby doplňování zásob s poptávkou a umožňují chytrým tlačítkům vzniknout –
podobně jako chytré tlačítko při použití trasy MTO.

.. obrázek:: reordering_rules/po-smartbutton.png
:alt:Ukazuje chytrý tlačítko PO.

Objednávka na prodej s chytrým tlačítkem, které odkazuje na související nákupní objednávku
(metoda doplňování).

V kontextu přehazování pravidel:

  - Pravidla pro přeřazování neautomaticky přiřazují skupinu nákupu, protože
:smart tlačítka, která spojují |SOs| s |POs|, na rozdíl od trasy :abbr:`MTO (Make to Order)“.
  - Pro možnost nastavení chytrých tlačítek pro produkty doplňované podle pravidel znovuplnění (ne:abbr.: MTO (Make to
objednávky) s konkrétními množstvími spojenými se specifickými poptávkami (např. |SOs|), přiřadit nákup
skupina.
  - Bez skupiny nákupu lze požadavky na stejný produkt sloučit do jednoho |RFQ|.
I když se pravidlo přeřazení provede vícekrát pro tyto požadavky, což umožňuje více
účinnější nákup tím, že se konsolidují požadavky do menšího počtu objednávek.

Vyberte skupinu nákupu v poli „Skupina nákupu“ na kartě „Dodávky“.
Zpráva zajišťuje, že všechny spojené objednávky jsou seskupeny pod stejnou poptávkou na základě definovaných kritérií.
trasa.

......cvičení::
Jak můžete nastavit pole *Nákupní skupina*, *Dodavatel* a *Trasa* na zásobovacím příkazu?
zpráva vygeneruje jednu nabídku na pět různých produktů v objednávce prodeje SO35, pokud
Společností, která dodává tyto produkty, je stejná a zajistí, aby byly splněny i další požadavky na tyto výrobky.
odděleně?

...... spoiler:: Zobrazit odpověď

        #.Nastavte skupinu nákupu na SO35 v pravidlech pro přesun všech pěti
produkty. Toto seskupuje požadavky na „SO35“ do stejného |RFQ| nebo |MO|.
        #Nastavte pole „Dodavatel“ na „Interiér Azure“ a zajistěte, aby byl vytvořen požadavek na nabídku (RFQ) pro
Stejný dodavatel.
        #Nastavte pole „Trasa“ na „Koupit“ a vytvořte poptávku (RFQ).
        #Klikněte na tlačítko „Objednávka“ pro vytvoření jediné poptávky (RFQ) na pět produktů, které jsou
na „SO35“.

|Po zadání objednávky odstraňte pole „SO35“ ze seznamu položek v oblasti nákupu.
pět pravidel pro opětovné objednávání produktů, což zajišťuje budoucí poptávku po těchto produktech.
řízeny samostatně a přiřazeny k různým |RFQ| (obvyklé chování).

… skladování, inventář/sklady/dodávky na základě poptávky:

Logika just-in-time
==================

Logika „přesně včas“ v Odoo minimalizuje náklady na skladování tím, že objednávky přesně odpovídají termínům dodání.
Toho je dosaženo pomocí předpokládaného data (datum v závorce)
který určuje, kdy je nutné doplnit zásoby, aby nedošlo k převisu.

Uvedený termín je **nejdříve možným datem**, kdy může být produkt dodán.
proces začíná okamžitě. Je vypočítán součtem časů potřebných k doplnění zásob
proces, jako například:ref:`dodací lhůty dodavatelů <sklady/skladování/nákupní-lt> a
:ref:`zpoždění nákupů <skladování/sklady/bezpečnostní zásoby> pro nákupy nebo
:ref:`dodací lhůty výroby <skladování/sklady/manuf-lt>“ pro výrobu.
automatické a manuální pravidla pro přeřazování fungují takto.

Příklad:
Pro produkt s celkovou dobu zpracování 5 dní a datem dodání objednávky za 10 dní čeká Odoo
5 dní na objednání zboží, aby bylo doručeno včas.

Důležité zásady:

- Pokud se vám tento postup zdá riskantní, zvažte přidání časového rezervu nebo upravte dobu dodání.
pro větší pružnost.
- Přestože termíny dodání a logika „pouze na čas“ poskytují další kontrolu, **pravidla pro přeobjednávku fungují
jsou naprosto v pořádku bez nich. Udržení termínu dodání na prodejním příkazu jako jejich *vytvořené datum*
zajišťuje, že nákupy jsou okamžitě spuštěny v případě potřeby

... skladovací prostory/sklady/datum předpokládaného příjezdu:

Datum předpokládaného nákupu a množství k objednání
-------------------------------------

Datum „předpokládaného doručení“ je datem nejdříve dostupným pro produkt, pokud si jej objednáte právě teď.
Výpočet se provádí součtem časů potřebných k doplnění zásob. Celkově
Tyto časy dodání přidáte k aktuálnímu datu a získáte čas, kdy Odoo kontroluje požadované zásoby.

Pro zobrazení předpokládaného data přejděte do hlášení o doplňování zásob a klikněte na ikonu :icon:`fa-info-circle`.
:guilabel:`(informace o doplňování zásob)` ikonu pro požadovaný způsob doplňování zásob.
Pop-up okno zobrazuje datum předpokládaného termínu a různé časové rozpětí.

Příklad:
Při ručním nastavení pravidla pro přesun se nezadává minimální ani maximální množství.

   - Doba dodání od dodavatele je 4 dny, doba zabezpečení nákupu je 1 den a počet dnů k nákupu
je 2 dny.
   - Dnešní datum je 26. listopad.
   - Tyto dny se sčítají a vytvářejí předpokládaný termín 3. prosince.

Potvrzená objednávka o 5 jednotkách má dodací termín 3. prosince (7 dní od dnešního data). Tato poptávka
Bude se objevit na dnešním doplňovacím hlášení v poli **Na objednávku**.

Pokud by ale dodací termín byl později než 3. prosince, ještě se na stránkách obchodu neobjevil.
reportu.Odoo zobrazuje pouze množství, které je třeba doplnit, pokud spadá do předpokládaného data
okno, které zajišťuje, že objednávky jsou vždy provedeny přesně ve chvíli, kdy je potřebujete.

.... obrázek: reordering_rules/replenishment-info.png
:alt:Zobrazit předpokládaný termín v Odoo.

Logika „na poslední chvíli“ zajišťuje, že zásoby se doplňují pouze v případě potřeby pro předpokládaný
datum požadavku, což pomáhá předcházet převisu zásob.

Příklad:

- Pokud předpovězené množství klesne pod minimální **na** předpovězený den, musí být
a začít okamžitě, aby nedošlo k nedostatku.
- Pokud se množství sníží pod minimální hodnotu po předpovězeném datu, lze doplnění odložit.

Kvantita k objednání je celkové požadované množství na předpokládaný den.

Odoo optimalizuje skladové zásoby tak, že objednávky zadává v čase, který odpovídá celkové době dodání.
minimální zásoby a zajistit, aby budoucí požadavky byly objednány na poslední možnou chvíli.
moment - strategické odkládání bez stresu!

Obecná nedorozumění ohledně předpokládaných množství
--------------------------------------------

|SOs| splatné po datu předpokládaném v poli „Datum“ nejsou zahrnuty do
:guilabel:`Předpověď“ kvantity pravidla přeřazení.

Ty se však objevují v předpovědním výkazu, který je otevřen kliknutím na
Ikona „Graf“ (zobrazení grafu) v zásobovacím hlášení, protože tato ikona znázorňuje
dlouhodobě předpokládané množství.

Příklad:

.. obrázek:: reordering_rules/zero-forecast.png
:alt: V předpovědích a objednávkách je nula.

Pokračujme v předchozím příkladu. Když je termín dodání objednávky přesunut na 4. prosince,
:guilabel:`Predikce“ a „Na objednávku“ jsou nulové.

...... obrázek:: reordering_rules/pět-předpovědí.png
:alt:Zobrazit předpověď.

Otevřením zprávy „Předpověď“ se zobrazí jednotky „5,00“.

... skladové zásoby/sklady/viditelnost dní:

Dny viditelnosti
===============

Dny viditelnosti umožňují zjistit, zda by měly být přidány další množství.
plánované doplnění zásob. Odoo zkontroluje, jestli předpokládaný počet zásob na předpokládaném datu klesne pod
minimální v pravidlech pro přeřazení. **Pokud ano**, zkontroluje se počet dní viditelnosti navíc
požadovanou poptávku v uvedeném počtu dnů.

Tato funkce pomáhá konsolidovat objednávky tím, že skupuje okamžité a blízké potřeby, snižuje
náklady na dopravu a umožnit dodavatelům slevy za větší objednávky.

Chcete-li nastavit viditelnost dnů tak, aby objednávky zahrnovaly určité počty dní do budoucna, přejděte na
V inventářové aplikaci -> Provoz -> Dodávky nebo kliknutím na položku „Dodání“.
Tlačítko Smart Rules* z produktu vytváří.

Dále zapněte pole „Dny viditelnosti“ kliknutím na posuvník vpravo.
Vyberte funkci z nabídky a pak zadejte požadované dny viditelnosti.

.. důležité::
Datum předpokládaného termínu nikdy neposouváme nebo neprodlužujeme, pouze kontrolujeme další viditelnost.
pokud by se cena akcií dostala pod minimální hranici v předpovězeném termínu.

Příklad, kdy je spuštěn den viditelnosti
------------------------------------------

Produkt dodaný z Asie má celkovou dobu dodání prodejce 30 dní a náklady na dopravu ve výši 100 $.
včetně nákladů na skladování zboží (viz:doc:`náklady na skladování zboží <../../product_management/inventory_valuation/landed_costs>`)
tarify).

- Datum: 4. listopadu. Předpověď je na 4. prosince (30 dní později).
- SO 1: Zboží je potřeba do 4. prosince. Odoo objedná dnes za 100 $.
- SO 2: Požaduje dodání produktu do 19. prosince. Obvykle by objednala 19. listopadu a náklady na
dalších 100 $.
- |SO| 3: Předpokládá dodání produktu do 25. prosince. Obvykle by Odoo objednala 25. listopadu a to by znamenalo další
  $100.

Doprava na tyto objednávky celkem stojí 300 $.

.. obrázek:: reordering_rules/predpokladana-datum.png
:alt:Zobrazit předpověď dat.

Přiřazení hodnoty „20.0“ v proměnné guilabel:Visibility Days umožňuje Odoo „vypadat dopředu“ o 20 dní od 4. prosince
(Datum předpokládané |SO| 1) do 24. prosince.

- Skupuje objednávky SO2 s objednávkami SO1 a snižuje náklady na dopravu tím, že konsoliduje objednávky.
- Dlužná částka číslo 3, která je splatná 25. prosince, je o jeden den později a není součástí dvou předchozích plateb.

Příklad, kdy se nezapne funkce viditelnosti dní
-----------------------------------------------------

Pokud by v příkladu výše neexistoval |SO| 1, pak:

- **4. listopadu**: Aktuální datum. Předpokládaný termín je 4. prosince (30 dní později).
- **5. listopadu**: Předpokládaný termín se posouvá na 5. prosince.
- |SO| 2: Požaduje produkt do 19. prosince. Odoo objednávku vyvolá až 19. listopadu
To znamená, že uživatel neuvidí žádnou zprávu o doplnění až do této chvíle.

To znamená, že viditelné dny doplňují logiku „just in time“ a optimalizují ji tak, aby byla vyvážená.
dodávky jsou levnější.

.. obrázek: reordering_rules/counterexample.png
:alt:Příklad, kdy viditelnost dní nevyvolává.

Horizon Days
============

Dny horizontu určují, kolik dní dopředu Odoo kontroluje předpokládané množství a zda klesne pod
pravidlo pro minimální počet položek v objednávce. Tato funkce má pomoci uživatelům při plánování doplňování zásob s předstihem,
Zvýšení předpokládaného data:ref:`<inventory/warehouses_storage/forecasted-date>`.

.. matematika::
:class: přesahující svislý posuv

\text{Datum předpovědi} = \text{Aktuální datum} + \text{Čas dodání od dodavatele} + \text{Dny horizontu}


Horizontální dny jsou určeny pouze pro ruční nastavení pravidel pro přeřazení. Pro více informací o
je uvedena v článku o zprávě o doplňování zásob :doc:`<report>`.
