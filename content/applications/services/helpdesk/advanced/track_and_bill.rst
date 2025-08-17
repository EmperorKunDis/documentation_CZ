===================
Sledovat a fakturovat čas
===================

.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`

Odoo **Helpdesk** poskytuje týmům možnost sledovat počet hodin, které strávili prací na
lístek a účtovat zákazníkovi za tu dobu. Díky integraci s aplikací **Sales**
Aplikace „Časové listy“, „Projekty“ a „Účetnictví“ umožňují účtovat zákazníkům za práci až po jejím dokončení.
nebo ještě předtím, než začala.

.. nebezpečí::
Protože funkce Track & Bill Time vyžadují integraci s jinými aplikacemi, umožňuje je
Může vést k instalaci dalších modulů nebo aplikací.

Při instalaci nové aplikace na databázi One-App-Free se spustí 15denní zkušební doba.
pokud nebude k databázi přidán placený tarif, bude se soudní řízení zastavit.
nebo dostupné.

Nastavte funkce pro sledování a účtování času
======================================

Předtím, než zákazník zaplatí za podporu, musí být funkce sledování a účtování času povoleny.
Je aktivován na každém týmu **Helpdesku** zvlášť.

Zapněte sledování času na týmu podpory
---------------------------------------------

Chcete-li zobrazit a povolit funkce *Sledování času a fakturace* na týmu **Helpdesku**, nejprve přejděte do
Vyberte v menu aplikace „Pomocníci“ -> „Nastavení“ -> „Týmy pomocníků“. Pak vyberte tým.
seznam nebo vytvořit nový:doc:`<../../helpdesk>“. Tato stránka odhaluje nastavení týmu.

V sekci „Sledování a fakturace času“ na stránce nastavení týmu zkontrolujte zaškrtávací políčka
označeny jako „Časové listy“ a „Zúčtování času“.

Po zaškrtnutí políčka „Časové listy“ se objeví nové pole s názvem „Projekt“.

.. poznámka::
Pokud je tato funkce zapnutá na této databázi poprvé, stránka může potřebovat
ručně uložené a aktualizované před zobrazením pole „Projekt“.

Vybraný projekt v tomto poli představuje, kde jsou všechny lístky týmu.
zaznamenané. Klikněte do pole „Projekt“ pro výběr projektu.

Pro vytvoření nového projektu, kde budou hodiny zaznamenány, klikněte na položku „Projekt“.
výběrovém seznamu zadejte název projektu a pak klikněte na položku „Vytvořit“ v nabídce.
pod menu.

.. obrázek: track_and_bill/track-bill-enable-settings.png
:alt: Zobrazení stránky nastavení týmu podpory s důrazem na nastavení stop a fakturačních časů.

... _helpdesk/konfigurovat-služby-a-produkty:

Nastavte služby
~~~~~~~~~~~~~~~~~~~~~~~~~~

Při zapnuté funkci „Účtování času“ je v aplikaci **Prodej** vytvořen nový produkt.
nazvaný „Účetní doklady“. Tento produkt lze najít pod:
Produkty --> Produkty“. Pak hledejte „Služby v časových lístcích“ ve vyhledávacím poli. To je
produkt, který se používá při fakturaci za služby s *pozdrženou platbou* po jejich poskytnutí.
Dokončeno.

Vyberte položku „Služby na časových lístcích“ z produktové stránky, což odhalí podrobnosti o produktu
formulář. Produkt je konfigurován s nastavením „Typ produktu“ na „Služba“.
Zapnout „Vystavování faktur“ na základě „Časových záznamů“.
produktový záznam, například „Náklady“ nebo „Prodejní cena“.

.. obrázek: track_and_bill/track-bill-product-based-on-timesheets.png
:alt:Pohled na službu s nastavenou fakturační politikou „Založené na časových listinách“.

Aby mohl před dokončením práce vystavit fakturu za podporu (také známou jako
*předplacené podpora služby*) musí být vytvořena samostatná produktová položka s jiným způsobem fakturace.

Pro vytvoření nového služby, přejděte na: `Sales app --> Products --> Products`
Klikněte na „Nový“. To odhalí prázdnou kartu produktu.

Na novém produktu přidejte pole „Název produktu“ a nastavte pole „Typ produktu“ na
Zvolte službu a nastavte způsob fakturace na „Předplacené / pevné ceny“.
To znamená, že lze vystavit fakturu a přijmout platbu za tento produkt ještě předtím, než
Pro tyto služby byly zaznamenány záznamy v hodinových listech.

.. obrázek: track_and_bill/track-bill-product-prepaid-fixed.png
:alt: Pohled na službu s nastavenou fakturační politikou „předplatné/pevná cena“.

Začněte nastavovat cenu prodeje pomocí proměnné :guilabel:`Sales Price` a poté zkontrolujte, zda je jednotka měření nastavená na
:guilabel:`hodiny“.

Předplatné služeb podpory
================================

Při fakturaci podpůrných služeb na pevnou cenu lze vystavit fakturu ještě před tím, než bude provedená jakákoliv práce.
dokončena na této otázce. V tomto případě se jedná o produkt služby s nastavením politiky fakturace
Používá se stejně jako v části výše:ref:`<helpdesk/configure-service-products>`.

Vytvořte prodejní objednávku s předplatitelným produktem
-----------------------------------------

Aby jste mohli zákazníkovi fakturovat předplacené služby podpory, nejprve vytvořte prodejní objednávku (PO) s podporou.
služby produktu. Chcete-li tak učinit, přejděte na: menu: „Prodejní aplikace“ -> „Objednávky“ -> „Kalkulace“. Pak
Klikněte na tlačítko „Nový“ pro zobrazení prázdného formuláře citace.

Poté vyplňte formulář s informacemi o zákazníkovi.

Přejděte na záložku „Dodací řádky“ v citaci a klikněte na „Přidat produkt“. Pak
Vyberte produkt služby předplacených služeb při:konfiguraci služby
<pomoci/konfigurovat-služby-produkty>. Aktualizujte pole „Kvantita“ číslem
hodin.

Po aktualizaci všech dalších potřebných informací klikněte na tlačítko „Potvrdit“. Tím se změní
citát do |SO|.

Vytvořte a odešlete fakturu za předplacené služby
-----------------------------------------------

Po potvrzení |SO| klikněte na tlačítko „Vytvořit fakturu“. To otevře
Pop-up okno „Vytvořit fakturu“.

Pokud se nebude vybírat záloha, typ vytvoření faktury může zůstat
„Běžná faktura“. Pokud je uveden :doc:`předplatba <../../../sales/sales/invoicing/down_payment>“
je vybírána mezi buď „Výše úvěru (v procentech)“ nebo „Výše úvěru“.
„pevná částka“.

Po zadání potřebných informací klikněte na tlačítko „Vytvořit návrh“.

Faktura pak může být zaslána zákazníkovi k úhradě.

Vytvořit požadavek na podporu pro předplacené služby
-------------------------------------------

Pro vytvoření helpdeskového případu pro předplacené služby přejděte do sekce:
Klikněte na tlačítko „Vstupenky“ pro zobrazení konkrétního týmu v procesu. Klikněte na „Nový“
Vytvořit nový lístek.

Na prázdném lístku vytvořte lístek s názvem „Název“ a zadejte „Zákazník“.
informace.

Když je přidán název zákazníka, pole :guilabel:`Sales Order Item` se automaticky vyplní
nejnovější předplacený prodejní příkaz, který má ještě časový limit.

Čas strávený na helpdesku
------------------------------

Čas strávený prací na **tiketu Helpdesku** je zaznamenán v záložce **Denní hlášení** u konkrétního
lístek.

V podrobnostech o lístku klikněte na záložku „Časové listy“ a poté klikněte na „Přidat řádek“.
Vyberte „Zaměstnanec“, přidejte popis úkolu a zadejte počet
:guilabel:`Čas strávený“.

Když se přidá nová řádka v záložce „Časové listy“, pole „Zbylé hodiny na SO“
Na spodním pravém rohu záložky se automaticky aktualizuje.

.. obrázek: track_and_bill/track-bill-remaining-hours-total.png
:alt: Pohled na záložku s přehledem pracovních směn v případě, kdy je na SO zbývající hodiny.

.. poznámka::
Pokud je počet hodin na záložce „Časová listina“ vyšší než prodaných hodin,
:guilabel:`Čas zbývajících hodin SO“ se zbarví červeně.

.... obrázek: track_and_bill/přesčasové hodiny prodané.png
:alt: Příklad lístku s počtem hodin převyšujícími zbývající hodiny.

Když se přidávají hodiny do záložky „Časové listy“, automaticky se aktualizují v
a také pole „Doručeno“ na SO.

Faktura za podporu služeb po zaplacení
==================================

Pokud jsou podpůrné služby účtovány na základě množství času stráveného řešením problému, faktura nemůže být
vytvořené předtím, než bylo zadáno celkové množství hodin potřebných k řešení problému.
evidenci pracovní doby. V tomto případě se jedná o službu s nastavenou politikou
Pro výpočet docházky se používá podobný vzor jako ten, který je automaticky vytvořen po :ref:`
Funkce „Časová fakturace“ je zapnutá.

Vytvořte prodejní objednávku s časově omezeným produktem
------------------------------------------------

Nejprve vytvořte SO s *Service on
Produkt „Časové listy“. Pro přístup k němu se musíte přepnout na: `Sales app --> Orders --> Quotations`. Pak
Klikněte na tlačítko „Nový“ pro zobrazení prázdného formuláře citace.

Vyplňte cenovou nabídku zákaznickými údaji.

Na kartě „Řádky objednávky“ klikněte na „Přidat produkt“. Vyberte „Službu“.
na produkt časových listin. Po aktualizaci všech ostatních potřebných informací klikněte na tlačítko
citát.

.. důležité:
Oproti předplaceným službám je v případě fakturace možné vytvořit fakturu **jenom jednou**.
Tentokrát. Služby nebyly poskytnuty, tedy nic nedorazilo, takže se o ničem nemůže mluvit.
faktura.

Vytvořit požadavek na podporu pro služby sledované časem
--------------------------------------------------

Pro zaznamenání časové položky pro sledované služby přejděte do aplikace „Pomocník“ a
vyberte příslušný tým, pro který se tyto služby vztahují.

Pokud již existuje stížnost na tento problém, vyberte ji z kartového pohledu. To otevře
formulář pro údaje o jízdence. Pokud neexistuje žádný stávající lístek pro tento zákaznický problém, klikněte
:guilabel:`Nový`` vytvořit novou objednávku a zadat potřebné informace o zákazníkovi do prázdného formuláře
formulář s podrobnostmi o lístku.

Po výběru nebo vytvoření lístku přejděte na záložku „Položka prodejního dokladu“. Vyberte
Vytvořené v předchozím kroku.

Sledovat hodiny podpory na lístku
-------------------------------

Aby bylo možné vytvořit fakturu za produkt na základě časových listů, je nutné sledovat hodiny.
zaznamenána. V tomto bodě je služba považována za dodanou. Pro záznam hodin za tuto podporu
služby, klikněte na záložku „Časové doklady“ v lístku.

Klikněte na tlačítko „Přidat řádek“ pro zaznamenání nové položky. Vyberte „Zaměstnance“ ze seznamu
položky nabídky a zaznamenat čas strávený v sloupci „Čas strávený“.

Opakujte tyto kroky, dokud nebudou všechny záznamy v pracovním listu zaznamenány.

.. obrázek: track_and_bill/track-bill-record-timesheet-hours.png
:alt: Pohled na kartu s přehledem směn v otevřeném požadavku na podporu.

Vytvořit fakturu za hodiny zaznamenané na lístku
-----------------------------------------------

Pokud nejsou potřeba žádné nové faktury, vytvořte si fakturu a pošlete ji zákazníkovi.

Pro toto vyberte v seznamu |SO| pomocí tlačítka „Smart Button“ s názvem „Sales Order“ na horním okraji
lístek.

Před vytvořením faktury zkontrolujte, že číslo v sloupci „Dodáno“ odpovídá
celkový počet hodin uvedených v záložce „Časové listy“ na lístku.

.. obrázek: track_and_bill/track-bill-delivered-timesheet-hours.png
:alt:Pohled na prodejní objednávku s důrazem na dodané položky.

Poté klikněte na tlačítko „Vytvořit fakturu“. To otevře okno s názvem „Vytvoření faktury (i)“.

Pokud se nebude vybírat záloha, typ vytvoření faktury může zůstat
Vyberte „Běžná faktura“. Pokud se vybírá záloha, zvolte buď „Zálohová faktura“ nebo „Faktura pro
Platba (procento) nebo: Výše úvěru (pevná částka).

.. důležité:
Využijte pole „Časové období“ v poli „Záznamy o pracovní době“, pokud by tento fakturační doklad měl obsahovat pouze záznamy o pracovní době.
od určitého časového období. Pokud je pole nevyplněno, **všechny** aplikovatelné doklady o pracovní době
Zahrnuty jsou i nevyúčtované položky.

Po zadání potřebných informací klikněte na tlačítko Vytvořit návrh. Faktura
Pak je třeba ji zkontrolovat, upravit a předložit zákazníkovi k úhradě.

.. viz též:
   - :doc:`../../../skladovani-a-prumyslove-vyroby/skladovani/správa-produktů/konfigurace/jednotka-hmotnosti`
   - :doc:`../../../sales/sales/invoicing/preplatky`
