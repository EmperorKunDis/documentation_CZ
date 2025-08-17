==============
Plošné objednávky
==============

... nakupovat/spravovat obchody/objednávky:

.. |SO| nahradit za: :abbr:`SO (Prodejní objednávka)`
.. |PO| nahradit za: abbr: PO (objednávka)
.. |UoM| nahradit za: zkratka `UoM (jednotka měření)`
.. |RfQ| nahradit za: zkratku `RfQ (požadavek na nabídku)`
.. |RfQs| nahradit za: :abbr:`RfQs (žádosti o nabídku)“

Smlouvy o dodávkách jsou dlouhodobé smlouvy mezi společností a dodavatelem na dodání produktů.
opakovaně s předem stanovenou cenou.

Pokud se produkty pravidelně nakupují u stejného dodavatele, jsou objednávky na zboží vhodné.
v různém množství a v různou dobu.

Zjednodušením procesu objednávání se smlouvy o dodávkách na vyžádání nejen ušetří čas, ale také peníze, protože
Mohou být výhodné při vyjednávání o velkoobchodních cenách s dodavateli.

Vytvořte novou objednávku na zboží
==========================

Pro vytvoření objednávek na zboží zapněte funkci „Nákupní smlouvy“ ve nastavení aplikace Nákup.
Navigujte do sekce „Koupit aplikaci“ -> „Konfigurace“ -> „Nastavení“, a pod
V sekci „Objednávky“ zaškrtněte políčko u „Kupních smluv“. Pak klikněte
:guilabel:`Uložit“ pro zavedení změn.

.. poznámka::
Kromě vytváření objednávek na zboží umožňuje nastavení „Smlouva o nákupu“ také uživatelům
vytvářet alternativní poptávky na nabídku (RfQ).

.. obrázek: blanket_orders/blanket-orders-enabled-setting.png
:align:center
:alt:Povolení smluv o nákupu v nastavení aplikace Nákup.

Pro vytvoření objednávky na zboží jděte do sekce „Nákupy“ - „Objednávky“ - „Skládané objednávky“.
Klikněte na „Nový“. To otevře novou objednávku na zakázky.

V nové objednávce na přikrývky upravte následující pole, abyste zadali předem stanovená pravidla pro
Opakující se dlouhodobá dohoda:

- :guilabel:`Zástupce nákupu“: uživatel přiřazený k tomuto konkrétnímu objednávkovému lístku.
tento uživatel vytvořil smlouvu, uživatele lze změnit přímo z roletky
v poli vedle tohoto pole.
- :guilabel:`Typ smlouvy“: typ nákupní smlouvy, do které tento celkový kontrakt spadá.
Odoo, smlouvy o dodávkách na zavolání jsou jediným oficiálním nákupním dohodou.
- :guilabel:`Dodavatel“: dodavatel, ke kterému je tento smluvní vztah vázán, buď jednorázově nebo opakovaně
Základní sazba, kterou lze vybrat přímo z roletky vedle pole.
- :guilabel:`Měna“: dohodnutá měna, která bude použita při této směně. Pokud je více
Pokud jsou ve výběru aktivní měny, lze měnu změnit z roletky.
v poli vedle tohoto pole.
- :guilabel:'Termín dohodnutí': datum, ke kterému bude tato kupní smlouva nastavena na vypršení platnosti. Pokud
toto plošné povolení by nemělo vypršet, nechte pole prázdné.
- :guilabel:`Datum objednání“: datum, kdy by měla být tato objednávka zadána novou nabídkou
je vytvořen přímo z objednávkového formuláře pro přikrývky. Pokud je nová nabídka vytvořena, tato hodnota
automaticky vyplní pole „Deadline“ na stránce |RfQ|.
- :guilabel:`Datum dodání“: očekávaný termín dodání, který je uveden v |RfQ|.
očekávané, pokud je vytvořeno přímo z objednávky na přikrývku. Pokud je vytvořena nová nabídka, bude tato hodnota
automaticky vyplňuje pole „Očekávaný příjezd“ na stránce |RfQ|.
- :guilabel:`Zdrojový dokument“: nákupní objednávka, ke které se tato smlouva vztahuje. Pokud
tento prázdný příkaz by neměl být vázán na žádný stávající |PO|, nechte pole prázdné.
- :guilabel:`Společnost“: společnost přidělená tomuto konkrétnímu objednávkovému lístku. Výchozí hodnotou je
firma, která je uživatelem vytvářejícím objednávku na zakázku zapsána. Pokud databáze není
multifiremní databáze, tento prvek nelze změnit a výchozí hodnotou je pouze jedna společnost.
v databázi.

.. obrázek: přikrývkové objednávky/přikrývkové objednávky - nová dohoda.png
:align:center
:alt: Nová objednávka na nákup nových produktů.

Jakmile jsou vyplněny všechny potřebné položky, klikněte na tlačítko „Přidat řádek“ pro přidání produktů pod
sloupec „Produkt“. Poté v sloupci „Množství“ změňte množství
Každé zboží a nastavte cenu v sloupci „Jednotková cena“.

.. důležité:
Při přidávání produktů do nové objednávky nejsou použity předchozí ceny.
automaticky přidány do produktových řad. Ceny **musí** být ručně přiřazeny, a to
změnou hodnoty v sloupci „Cena za jednotku“ na dohodnutou cenu s uvedeným
V opačném případě zůstane cena na nule.

Pro zobrazení a změnu výchozích nastavení smlouvy o nákupu pro objednávky na vyžádání přejděte do
formulář objednávky deky, klikněte na ikonu „>>“ (pravý směr), která se zobrazí při přejetí kurzorem
nad políčkem „Druh smlouvy“, kde je uvedeno „Plošná objednávka“. Kliknutím na toto políčko se dostanete
do nastavení objednávky na přikrývku.

.. obrázek: přikrývkové objednávky/přikrývkové objednávky-interní odkaz-šipka.png
:align:center
:alt:Následující směrový znak vpravo vedle pole typu smlouvy na objednávce krycího listu.

Zde lze upravit nastavení pro objednávky zadané na základě smlouvy. Pod položkou „Typ smlouvy“
sekci, název „Druh smlouvy“ lze změnit a název „Smlouva
Typ výběru lze změnit také. Lze aktivovat dvě možnosti typu
vybírání:

- :guilabel:`Vyberte pouze jeden návrh (exkluzivní)“: Když je objednávka potvrzena, zbylé
Zrušují se objednávky.
- :guilabel:`Vybrat více nabídek (neexkluzivních)“: Když je objednávka potvrzena, zbývající
Nepřijaté objednávky nejsou zrušeny, naopak je možné vytvářet více objednávek.

V sekci „Další údaje pro nové cenové nabídky“ je možné zadat v poli „Řádky“
V poli „Množství“ lze provádět úpravy, což určuje, jak mají být nové nabídky vyplněny
Při používání této kupní smlouvy.

.. obrázek: přikrývkové objednávky/přikrývkové objednávky - upravit typ smlouvy.png
:align:center
:alt:Příkazové okno pro editaci typu smlouvy o nákupu.

Pro volbu „Line“ existují dvě možnosti aktivace:

- :guilabel:`Použijte řádky dohody“: při vytváření nové nabídky se produktové řádky předvyplní
s těmi samými produkty, které jsou uvedeny na objednávce celé sady, pokud je zvolena nová
citát.
- :guilabel:`Nepřidávat automaticky řádky RfQ“: při vytváření nové nabídky **a také**
Vybraná stávající objednávka se přenese do nové nabídky a nastavení se přenesou na produkt.
tyto řádky nevyplňují.

A existují dvě možnosti, které lze aktivovat pro :guilabel:`Množství“:

- :guilabel:`Použít množství dohody“: při vytváření nové nabídky se produktové množství
vložené do předpřipraveného seznamu na produktové řadě, pokud je k němu vybrána předpřipravená objednávka.
nové cenové nabídky.
- :guilabel:`Manuální nastavení množství položek“: při vytváření nové nabídky **a** při výběru existující
plošný objednávkový formulář, produktové řady se předvyplní, ale všechny množství jsou nastaveny na hodnotu 0. Množství
Musí být ručně nastaven uživatelem.

Jakmile provedete všechny požadované změny, klikněte na tlačítko „Nový“ (přes chlébové kousky nahoře).
přejděte na formulář objednávky přikrývky a pak klikněte na „Potvrzení“ pro uložení této změny.
nový kupní smlouvy.

Jakmile je objednávka potvrzena, stupeň objednávky se v pravém horním rohu změní na „Návrh“.
„Ve výběru“, což znamená, že tento dohoda může být vybrána a použita při vytváření nových poptávek.

..tip:
Po vytvoření a schválení objednávky lze stále upravovat produkty, množství a ceny.
upravit, přidat nebo odstranit z kupní smlouvy.

Vytvořit novou poptávku z objednávky
=========================================

Po potvrzení objednávky celé sady lze vytvářet nové nabídky přímo z objednávky celé sady.
formulář |RfQs| je předvyplněn informacemi na základě pravidel nastavených v tomto formuláři.
Dále jsou k této objednávce automaticky propojeny nové citace.
:guilabel:`RFQs/Orders“ chytrý tlačítko v pravém horním rohu formuláře.

Pro vytvoření nové nabídky z objednávkového lístku krytí klepněte na tlačítko „Nová nabídka“.
To otevírá novou RfQ, která je předvyplněná správnými informacemi v závislosti na
Nastavení v objednávce na polštářek.

Z nového formuláře RfQ klikněte na tlačítko „Odeslat e-mailem“ a vytvořte a odešlete e-mail uvedeným
prodejce. Klikněte na tlačítko „Tisk nabídky“ pro generování tisknutelné verze PDF nabídky nebo klikněte na „Připraveno“,
Klikněte na tlačítko „Potvrdit objednávku“ pro potvrzení objednávky.

.. obrázek: plédové objednávky/plédová objednávka - nová nabídka.png
:align:center
:alt: Nová cenová nabídka s kopírovanými produkty a pravidly z objednávky na zakázku.

Jakmile je potvrzena objednávka PO, klikněte zpět na formulář pro objednávku prostřednictvím chlebových stop (pomocí chlebových stop,
v horní části stránky. Z objednávkového formuláře pro přikrývku je nyní uveden pouze jeden |RfQ| v
:guilabel:`RFQs/Orders“ chytrý tlačítko v pravém horním rohu formuláře. Klikněte na „RFQs/Orders“.
Chytrý tlačítko, které zobrazí nově vytvořené |PO|.

.. obrázek: blanket_orders/blanket-orders-rfq-smart-button.png
:align:center
:alt:Tlačítko pro rychlé vyvolání poptávky a objednávky z formuláře objednávkového lístku.

Dodávky
=============

Jakmile je potvrzena objednávka na přikrývky, do seznamu dodavatelů se přidá nová řádka pod záložkou „Nákup“.
výrobky zahrnuté v objednávce.

Tímto způsobem lze využít objednávky zboží s automatickým doplňováním zásob.
„<../../purchase/products/reordering>“, protože informace o dodavateli
:guilabel:`Cena“ a „Smlouva“ jsou uvedeny v řádku dodavatele. Tato informace
určuje, kdy, kde a za jakou cenu by měl být produkt doplněn.

.. obrázek:zakazky/zakazka-produktu.png
:align:center
:alt:Forma produktu s doplňovací smlouvou, která je spojena se zakázkou celé řady.

.. viz též:
:doc:`výběrová řízení“
