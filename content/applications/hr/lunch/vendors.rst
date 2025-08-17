=======
Dodavatelé
=======

Předtím než se produkty mohou přidat do aplikace **Lunch**, musí být podniky, které je nabízejí
Jídlo musí být nakonfigurováno.

Chcete-li přidat nového dodavatele, nejprve se přesuňte na :menuselection:`Obědová aplikace --> Konfigurace --> Dodavatelé“.
Zde se zobrazují všichni aktuálně nakonfigurovaní dodavatelé aplikace Lunch v kanbanovém výhledu.
změňte seznamový pohled, klikněte na ikonu „OI View List“ v pravém horním rohu.
roh.

.. poznámka::
V aplikaci Lunch nejsou žádné dodavatele přednastaveny, takže všichni dodavatelé musí být přidány do
databáze.

Zobrazí se karta „Dodavatel obědů“ na panelu „Dodavatelé“,
Výchozí. Klikněte na tuto kartu a v nastavení dodavatele upravte následující pole:

- :ref:`Informace o dodavateli <lunch/vendor-info>`
- :ref:`Dostupnost <lunch/availability>`
- :ref:`Objednávky <objednavky/>`
- :ref:`Příslušenství <lunch/extras>`

Po konfiguraci prvního dodavatele přidejte další dodavatele kliknutím na tlačítko „Nový“ v
v horním levém rohu a nakonfigurujte nového dodavatele obědů. Opakujte pro všechny potřebné dodavatele.

..._oběd/informace o dodavateli:

Informace o dodavateli
==================

- :guilabel:`Dodavatel“: Zadejte jméno dodavatele do tohoto pole.
- :guilabel:`Dodavatel“ (pod řádkem pro název dodavatele): Vyberte z roletkového seznamu
odpovídajícího dodavatele v aplikaci Kontakty. Pokud dodavatel ještě nebyl založen, zadejte
názvu dodavatele a klikněte na „Vytvořit nový dodavatel“. Můžete také kliknout
:guilabel:`Vytvořit a upravit...“ pro vytvoření dodavatele a úpravu kontaktního formuláře dodavatele.
Kontaktní formulář umožňuje vložit více informací, jako je například kontaktní údaje.

.. poznámka::
Pokud je vybrána možnost z rozevíracího seznamu pole :guilabel:`Výrobce`, text pole :guilabel:`Výrobce
pole (v horní části pro název dodavatele) aktualizuje s názvem dodavatele vybraného z nabídky.
rozbalovací nabídka.

Seznam dodavatelů, který je v nabídce zobrazen, je převzat ze seznamu kontaktů.
aplikace.

- :guilabel:`Adresa“: Zadejte adresu dodavatele do různých políček.
- :guilabel:`E-mailová adresa“: Zadejte e-mailovou adresu dodavatele do tohoto pole.
- :guilabel:`Telefonní číslo“: Zadejte telefonní číslo dodavatele do tohoto pole.
- :guilabel:`Společnost“: Pokud je tento dodavatel k dispozici pouze určité společnosti, vyberte společnost
z roletkového menu. Pokud je pole nevyplněné, zboží dodavatele bude dostupné pro všechny
firmy. Toto pole se v databázi jednotlivých firem nezobrazuje.

.. obrázek: dodavatelé/informace o dodavateli.png
:alt:Vyplněná část prodejního formuláře.

...oběd/přístupnost:

Dostupnost
============

Sekce „Dostupnost“ obsahuje tabulku s dvěma řádky. Dny v týdnu jsou vyplněny
v horní řadě je zaškrtávací políčko a v dolní řadě zaškrtávací políčko pro každý den
Ve dnech, kdy je prodejce k dispozici.

Výchozí nastavení je pondělí až pátek.

.. obrázek: dodavatelé/dostupnost.png
:alt: Výchozí pohled na sekci dostupnosti s povolenými pracovními dny v týdnu.

.. objednávky na oběd:

Příkazy
======

V sekci „OBJEDNÁVKY“ v prodejním formuláři jsou uvedeny místa, kde je dodavatel dostupný.
a kromě toho, jak a kdy jsou objednávky zadávány a přijímány.

- :guilabel:`Dodání“:Vyberte možnost „Dodání“, pokud dodavatel dodává.
do kanceláře nebo vyberte:guilabel:"Žádné dodání" pokud je objednávka k vyzvednutí.
- :guilabel:`Lokalita“: Vyberte, které lokality mohou objednávat od tohoto dodavatele.
V poli lze vybrat konkrétní místo nebo nechat pole prázdné, pak mohou objednávat všechna místa.
Prodávající.

.. poznámka::
Výchozí umístění „HQ Office“ se vytváří při vytváření databáze a je k dispozici.
vyberte si z nabídky.

- :guilabel:`Zaslat objednávku na“: Klikněte na tlačítko, abyste vybrali způsob, jakým jsou objednávky zasílány dodavateli.
K dispozici jsou následující možnosti: „Telefon“ nebo „E-mail“.
- „Čas objednávky“: Toto pole se objeví pouze v případě, že je vybráno pole „E-mail“.
:guilabel:`Datum odeslání objednávky“ a zadejte datum, kdy musí být objednávka odeslána, aby byla
přijaté. Zadejte čas v následujícím formátu: „H:M“. Pak vyberte buď „:guilabel:AM“ nebo
Vyberte položku „PM“ z rozevírací nabídky vedle pole času.

.. obrázek: prodejci/objednávky.png
:alt:Část objednávkového formuláře prodejce s vyplněnými všemi poli.

... oběd/příplatky:

Příplatky
======

Při objednávání položky v aplikaci **Lunch** může být volitelný příplatek za další produkt.
*doplňky*, které lze zobrazit, mohou být konfigurovány tak, aby vyhovovaly produktům, které jsou
nabídnuta.

Výchozí nastavení Odoo umožňuje tři typy přídavných položek, které lze považovat za kategorie.
výchozím nastavením je první typ (nebo kategorie) doplňků označen jako „Extra“, druhý jako
„Nápoje“, a třetí je označen „Doplňkové štítky 3“.

.. důležité::
Při konfiguraci doplňků je důležité mít na paměti, že všechny doplňky konfigurované
vystoupit pro každý produkt nabízený dodavatelem. To znamená, že se týká pouze položek, které se vztahují na
**všechny produkty od dodavatele** by měly být přidány.

..._oběd/konfigurovat-příslušenství:

Nastavte doplňky
----------------

Do každé ze tří dostupných příplatkových položek zadejte následující informace:

- :guilabel:`Doplňkový štítek (#): Zadejte název pro typ doplňku, například „Náplně“. To může být
Je považována za kategorii.
- Vyberte, jak se extra vybírají. Možnosti jsou:

  - :guilabel:'Žádný nebo více': Vyberte tuto možnost, pokud není uživatel povinen provést výběr.
  - :guilabel:`Jeden nebo více“: Zvolte tuto možnost, pokud chcete po uživateli, aby vybral alespoň jednu z nabízených možností.
výběru.
  - :guilabel:`Pouze jedna možnost“: Vyberte tuto možnost, pokud chcete po uživateli, aby provedl pouze jednu volbu.

Přidejte příplatky
----------

Po konfiguraci štítků a množství pro další kategorii se zobrazí jednotlivé položky.
Do každé kategorie musí být přidány položky.

Klikněte na tlačítko „Přidat řádek“ v dolní části seznamu, který se zobrazí po pravé straně.
Další kategorie. Do každého položky, která se přidává, zadejte :guilabel:`Jméno` a :guilabel:`Cena`.
Cena může zůstat na „0,00 $“, pokud je produkt bez nákladů. Toto je běžné u jednorázového příboru
nebo dochucovadla.

.. příklad::
Pro pizzerii nabízející pouze osobní pizzy zkontrolujte jejich příplatky takto konfigurované:

První přídavek je konfigurován pro různé druhy příloh, které nabízejí.
je nastaven na „Náplně“ a :guilabel:`Extra 1 Quantity“ je nastaven na „Žádné nebo více“.
Poté se přidají různé doplňky a jejich cena.

.... obrázek:: dodavatele/extra.png
:alt: První z příplatkových položek pro pizzu.

Pizzařina nabízí ke každé objednávce také nápoj zdarma. K tomu je potřeba si vybrat položku „Extra
2.Label je nastaven na „Nápoje“ a :guilabel:„Dodatečná kvantita“ je nastavena na :guilabel:„Jen
Jeden. Různé nápoje se přidávají a cena za každý zůstává nula.

.... obrázek: dodavatelé/nápoje.png
:alt: Druhá z bonusů, kterými se lze při nákupu něčeho jiného kávy dostat.
