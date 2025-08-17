========================
Dodací lhůty výrobků na objednávku
========================

.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`

V některých případech nelze vyrobit celou objednávku hned.
přichází v úvahu, pak umožňuje výrobu částečných množství objednávky.
Vytvoří se záloha na zbývající částku.

V aplikaci Manufacturing vytváření zásobníku rozděluje původní výrobní objednávku na dvě.
objednávky. Referenční štítek pro každou objednávku je štítek použitý pro původní objednávku, následovaný
pomlčka a pak další číslo, které ukazuje, že je objednávka na zpracování.

Příklad:
Společnost vytvoří výrobní objednávku s referenčním štítkem *WH/MO/00175* pro 10 kusů
*Produkt X*. Po zahájení práce na výrobním příkazu pracovník zpracování
Přepracovali jsme výrobní linku, abychom zjistili, že máme pouze dostatek součástek na pět kusů produktu.

Výrobci místo čekání na další zásoby komponentů vyrobí pět kusů a vytvoří
a zbylých pět kusů objednáte na sklad, čímž se výrobní objednávka rozdělí na dvě samostatné objednávky:
*WH/MO/00175-001* a *WH/MO/00175-002*.

Řádku *001* tvoří pět jednotek vyrobených a je okamžitě označen jako
:guilabel:`Dokončeno“. Objednávka číslo 002 obsahuje pět jednotek, které ještě musí být vyrobeny a
označeno jako :guilabel:`In Progress“. Jakmile budou k dispozici zbývající komponenty,
Vrací se zpět k objednávce 002 a vyrábí zbývající jednotky před uzavřením objednávky.

Vytvořte výrobní objednávku
================================

Chcete-li vytvořit poptávku na část výrobního objednávky, začněte tím, že se přesunete do
:menuvolba-->Výroba-->Výrobní objednávky“. Vyberte výrobní objednávku
Vyberte množství dvě nebo více, nebo klikněte na tlačítko Vytvořit.

Pokud vytvoříte novou výrobní objednávku, vyberte si produkt z rozevírací nabídky „Produkt“
menu a zadejte množství dvou nebo více v poli „Množství“ a pak klikněte
Klikněte na „Potvrdit“ pro potvrzení objednávky.

Po výrobě množství, které se vyrábí okamžitě, zadejte do
V poli „Množství“ v objednávce výroby.

.. obrázek: výroba/zadané množství.png
:align:center
:alt:Kvantitativní pole výrobního příkazu.

Dále klikněte na „Zkontrolovat“ a poté na „Vyrobili jste méně než požadovaný počet“.
zobrazí se okno, ve kterém můžete vytvořit objednávku na dodání. Klikněte na tlačítko „Vytvořit objednávku na dodání“.
z výrobního příkazu vytvořit dvě samostatné objednávky s referenčními tagy *WH/MO/XXXXX-001*.
*WH/MO/XXXXX-002*.

.. obrázek: výroba_objednávek/tlačítko_vytvořit_objednávku.png
:align:center
:alt:Tlačítko Vytvořit poptávku na okně „Vyrobili jste méně než počáteční poptávka“.

Objednávka 001 obsahuje položky vyrobené a je okamžitě uzavřena. Objednávka 002
Je to objednávka na vyrobení zboží, které ještě nebylo vyrobeno a která zůstává otevřená.
Dokončena později.

Jakmile budou zbývající jednotky vyrobeny, přejděte na:
Operace --> Výrobní objednávky“ a poté vyberte výrobní objednávku s nedostatkem materiálu. Pokud všechny
Zbylé jednotky se ihned vyrábějí, stačí kliknout na tlačítko „Potvrdit“
pořádku.

Pokud se ihned nevyrábí všechny zbývající jednotky, vytvořte další objednávku.
zbytky podle kroků popsaných v této části.

Vytvořte objednávku na sklad v aplikaci Shop Floor
================================

Na objednávky k výrobě lze vytvářet i zpětné objednávky z modulu „Podlaha“.

.. poznámka::
Pro použití modulu „Dodavatelské řetězce“ musí být zapnuté nastavení „Objednávky“.
navigovat do: „Výroba -> Konfigurace -> Nastavení“, zapnout
zaškrtněte políčko „Pracovní příkazy“ a pak klikněte na „Uložit“.

Chcete-li vytvořit objednávku z výroby, začněte tím, že se přesunete do
:menuvolba:Výroba --> Provoz --> Výrobní objednávky. Vyberte |MO| pro více
jednotky produktu, pro které je nutné vytvořit objednávku na dodání.

Vyberte záložku „Pracovní příkazy“ na nabídce |MO| a pak klikněte na „Otevřít pracovní příkaz“.
Klikněte na tlačítko „(externí odkaz)“ v řádku pracovního příkazu, který chcete zpracovat. Na výsledné
Okno „Příkazy k práci“ (pop-up), klepněte na tlačítko „Otevřít výrobní plochu“.
Modul „Prodejní plocha“.

Při přístupu z konkrétní objednávky se otevře modul „Dílna“ na stránku s prací
centru, kde je objednávka konfigurována k zpracování a izoluje kartu pracovního příkazu tak, aby
Ostatní karty jsou ukázány.

Dokončete kroky na kartě pracovního příkazu až do kroku „Registrace výroby“
a pak na něj klikněte pro otevření okna „Registrace výroby“.

.. důležité:
Nepošlete kliknutím na tlačítko „Jednotky“ (vlevo) v kroku. Když tak učiníte,
automaticky eviduje celkový počet jednotek vyrobených za dané období.

Do okna „Registrace výroby“ zadejte počet vyrobených kusů.
Pole „Množství“. Ujistěte se, že číslo zadané v poli je nižší než počet jednotek uvedených na seznamu.
Poté klikněte na tlačítko „Zkontrolovat“.

.. obrázek: výroba_objednávek/registrace_výroby.png
:align:center
:alt:Okno výroby registru v modulu Výrobní plocha.

Pop-up okno zmizí a tlačítko „Jednotky“ v kartě pracovního příkazu se aktualizuje na
odrážejí počet vyrobených jednotek jako zlomek celkového počtu jednotek pro které byl
vytvořené původně.

Nyní klikněte na tlačítko „Zadat jako hotové“ v dolní části karty pracovního příkazu.
začíná se vytrácet pracovní karta. Jakmile úplně zmizí, objeví se nová pracovní karta.
označený původním referenčním číslem MO s přidáným koncovým znakem "-002".

Toto nové referenční číslo představuje objednávku na dodání |MO|. Číslo původní objednávky je nyní
je přidán znak „-001“ na konec, aby se odlišil od objednávky |MO|.

Pokud zbývají u původního |MO| ještě nějaké pracovní úkoly, lze ho uzavřít výběrem položky :guilabel:`Všechny`.
filtr v horní navigaci modulu Shop Floor a poté kliknutím na tlačítko „Zavřít“.
Výroba na dně karty MO.

Pokud má původní MO nevyřízené objednávky, které musí být dokončeny před uzavřením karty
Tyto pracovní příkazy se zobrazují na stránkách *Podlaha dílny* pro konkrétní pracoviště, kde jsou
jejich zpracování je možné provést standardním způsobem a další objednávky mohou být
Vytvořené z jejich pracovních karet podle pokynů uvedených v této části.

Jakmile je objednávka pro zpracování zadaná, může být zpracována i
dokončena jako obvykle a další dodatečná objednávka může být vytvořena z jejího karty pracovního příkazu
podle pokynů uvedených v této části.

Po dokončení konečného pracovního příkazu pro zpracování objednávky zadané na poptávku lze zakázku uzavřít
kliknutím na tlačítko „Ukončit výrobu“ v kartě objednávky.
