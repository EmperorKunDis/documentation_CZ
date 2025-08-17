===================
Dodání ve třech krocích
===================

Některé společnosti zpracovávají každý den velké množství dodávek, z nichž mnoho obsahuje více
výrobky nebo vyžadují speciální balení. Pro efektivní zpracování je třeba před
výrobky. Pro tento proces má Odoo třístupňový postup pro dodávání zboží.

V základním procesu tříkrokové dodávky jsou produkty součástí objednávky na vyzvednutí.
skladu dle jejich odstranění strategie a převezeny do zóny balení. Po položkách
byly v různých balících zónách zabaleny do jednotlivých dodávek a následně převezeny na výstup.
místo před odesláním. Tyto kroky lze upravit, pokud nebudou vyhovovat potřebám
podnikání.

Konfigurace
=============

Pro změnu nastavení doručení z jednoho kroku na tři kroky proveďte
Samozřejmě je zapnutá volba „Vícekrokové trasy“ v:menu:Inventář --> Konfigurace
Nastavení -> Sklad. Při zapnutí :guilabel:`Dvoufázové trasy“ se aktivuje také
*Uložiště*.

.. obrázek: doručení tří kroků/doručení tří kroků - vícekrokové trasy.png
:align:center
:alt:Aktivujte vícekrokové trasy a skladové prostory v nastavení zásob.

Dále je potřeba sklad nakonfigurovat pro třístupňové dodávky. K tomu se přihlaste na
Vyberte aplikaci „Skladové zásoby“ > „Nastavení“ > „Sklady“, a klikněte na
„Sklad“ k úpravě. Pak vyberte „Zabalit zboží, odeslat zboží do výstupu“ a nakonec
Dodání (3 kroky)“ pro „Odeslané zásilky“.

.. obrázek: doručení tří kroků/doručení tří kroků - odchozí zásilky.png
:align:center
:alt: Zvolte možnost doručení zásilky ve třech krocích.

Aktivací třístupňového příjmu a expedice vytvoříte dvě nové interní lokality: *Zóna balení*
(WH/Balicí zóna) a *Výstup* (WH/Output). Pro přejmenování těchto místností přejděte na
Vyberte v nabídce aplikace „Inventář“ -> „Konfigurace“ -> „Lokality“, klikněte na „Lokalitu“.
změnit a aktualizovat jméno.

Dodání ve třech krocích (vybrat + zabalit + odeslat)
===========================================

Vytvořte prodejní objednávku
--------------------

Pro vytvoření nové nabídky přejděte na: „Aplikace pro prodej – Vytvořit“, což odhalí prázdnou nabídku.
formulář. Na prázdném citačním formuláři vyberte „Zákazník“, přidejte uložitelný
Vyberte „Produkt“ a klikněte na „Potvrdit“.

Vpravo nahoře se objeví tlačítko „Dodání“. Po jeho kliknutí
otevírá možnost vybrat si produkt, který má být převezen z „Skladu/Zásoby“ do „Skladu/Balícího prostoru“.

.. obrázek: doručení tří kroků/doručení tří kroků - chytrý tlačítko.png
:align:center
:alt:Po potvrzení objednávky se objeví tlačítko Dodání s třemi položkami
s ním spojené.

Proces zpracování a vyskladňování
-----------------

Pozice pro vyzvednutí bude vytvořena poté, co bude objednávka schválena. Pro zobrazení pozic pro vyzvednutí přejděte
do aplikace „Seznam“, najděte kartu úkolu „Vybrat“
:guilabel:`Přehled inventáře“ panelu.

Klikněte na tlačítko „Zpracovat“ (Guilabel: # To Process“), které odhalí pořadí vybírání generované
dříve potvrzená objednávka na prodej.

Klikněte na vybrané položky a potvrďte jejich zpracování. Pokud je produkt skladem, Odoo automaticky rezervuje
produktu. Klikněte na tlačítko „Přijmout“ a dokončete převod produktu
:guilabel:`Přepravní zóna“.

.. obrázek: doručení tří kroků/doručení tří kroků - vyzvednutí objednávky.png
:align:center
:alt:Operace vybírání zobrazující zdrojové a cílové místo.

Zpracování a balení
-----------------

Po ověření vybraného zboží je objednávka připravena k zpracování.
„Přehled inventáře“ a najděte kartu „Balík“ na hlavním panelu.

Klikněte na tlačítko „Procesovat“ (v tomto případě „1 Procesovat“). Tím se zobrazí
balení, které vzniklo na základě dříve potvrzené objednávky.

Klikněte na objednávku balení spojenou se zakázkou, pak klikněte na tlačítko „Přijmout“
Dokončit balení.

.. obrázek: doručení_tři_kroky/doruceni-tri-kroky-baleni-objednavka.png
:align:center
:alt:Operace balení, která zobrazuje zdrojové a cílové umístění.

Jakmile je objednávka balení ověřena, produkt opustí místo :guilabel:`WH/Packing Zone`.
přesune se na místo :guilabel:`WH/Output`, a poté stav dokumentu změní na
:guilabel:Dokončeno.

Zpracovat dodávku
------------------

Jakmile je potvrzena skladová objednávka, můžete zpracovat dodací objednávku. Vraťte se na
původní prodejní objednávku zpracovat dodáním pomocí cesty: menu: `Prodej aplikace`
vybrat již vytvořenou objednávku prodeje.

.. tip::
Dodací objednávky lze také zobrazit kliknutím na: „Skladové aplikace -> Objednávky
--> Dodání.

Tlačítko „Dodání“ chytrého rozhraní nyní ukazuje tři převody namísto jednoho. Po kliknutí
Chytrý tlačítko „Dodání“ zobrazuje tři operace pro tento objednávkový lístek: vyzvednutí,
balení a dodání.

Klikněte na převod zboží (WH/OUT) a otevřete objednávku dodání. Pak klikněte na „Potvrdit“.

.. obrázek: doručení tří kroků/doručení tří kroků - objednávka doručení.png
:align:center
:alt:Klikněte na tlačítko „Potvrdit“ v objednávce dodání, abyste přesunuli produkt z výstupní lokace do
místo zákazníka.

Jakmile je objednávka doručení potvrzena, produkt opustí místo :guilabel:`WH/Output`.
přesune se do umístění „Partneři/Zákazníci“ a stav dokumentu se změní.
to:dokončeno`.
