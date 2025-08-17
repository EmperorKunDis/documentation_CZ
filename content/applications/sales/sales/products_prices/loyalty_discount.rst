=============================
Slevové a věrnostní programy
=============================

Aplikace Odoo *Sales*, *eCommerce* a *Point of Sale* umožňují uživatelům vytvářet slevy a
věrnostní programy, které zákazníci mohou využívat pro nákupy v obchodech i na internetu. Tyto programy nabízejí více
různé veřejné a časově citlivé cenové možnosti než: doc:`cenníky
</objednavky/prodej/produkty a ceny/ceny/cenotvorba>.

Nastavte si parametry
======================

Chcete-li začít používat slevové a věrnostní programy, přejděte na: „Prodej --> Konfigurace
V sekci „Nastavení“ pod záložkou „Ceník“ aktivujte položku „Slevy, věrnostní program“.
Nastavení dárkové karty zaškrtnutím políčka vedle funkce. Nakonec klikněte na tlačítko „Uložit“ pro uložení
změny.

Nastavte slevy a věrnostní programy
=======================================

Pro vytvoření slevových a věrnostních programů přejděte na: „Prodej --> Zboží --> Slevy a věrnostní program“.
Loajalita“.

Pokud ještě žádné slevy nebo věrnostní program nebyly vytvořeny, Odoo nabízí výběr šablon.
pomozte vytvořit první program. Vyberte jednu z šablon karet nebo klikněte na tlačítko „Nové“ a vytvořte
nový program od nuly.

Anebo pokud již existují nějaké programy, vyberte si jeden z nich a upravte jej.

.. obrázek: věrnostní slevy/cena-věrnostních-slev.png
:align:center
:alt:Šablony karet slev a věrnostního programu.

.. poznámka::
Šablony se zobrazují pouze tehdy, když nebyly vytvořeny žádné programy, a zmizí poté, co byl vytvořen první program.
vytvořen.

Vytváření nebo úprava programu otevře formulář programu.

.. obrázek: věrnostní slevy/cena-programu.png
:align:center
:alt:Možnosti věrnostního programu na formuláři věrnostního programu.

Programový formát obsahuje následující pole:

- :guilabel:`Název programu`: Zadejte název programu do tohoto pole. Název programu je **nepovinný**
Je viditelná pro zákazníka.
- Vyberte požadovaný typ programu.
Vyberte možnost „<prodej/cenotvorba/druhy programů>“ z nabídky.
- :guilabel:`Měna“: Vyberte měnu používanou v programu.
- :guilabel:`Seznam cen“: Pokud chcete, vyberte si z nabídky seznam cen a tímto způsobem získáte
program aplikovaný na konkrétní ceník (a zákazníky připojené k ceníku).
V tomto poli lze vybrat ceník. K jedné věrnostnímu programu může být připojeno více
ceníků, což umožňuje různým segmentům zákazníků mít odlišné ceníky.
stejné věrnostní programy. Pokud pole zůstane prázdné, aplikuje se na všechny.
bez ohledu na ceník.
- :guilabel:`Jednotka bodů“: Zadejte název bodů, které se používají pro :guilabel:`Karty věrnostního programu“
programu (např. „Body věrnosti“). Jméno jednotky bodů je viditelné pro zákazníka. Toto pole
*pouze* dostupné, pokud je nastaven typ programu na „Věrnostní karty“.
- :guilabel:`Datum zahájení“: Vyberte datum, kdy se program stane platným. Nechte toto pole prázdné
pokud by měl být vždy platný a neměl vypršet.
- :guilabel:`Datum ukončení platnosti“: Vyberte datum, kdy bude program neplatný. Nechte toto pole prázdné
pokud by měla být vždy platná a nikdy nevypršet.
- :guilabel:`Omezení používání“: Pokud chcete, zaškrtněte tuto políčko a zadejte počet :guilabel:`použití“.
aby omezila počet použití programu v době platnosti.
- :guilabel:`Společnost“: Pokud pracujete v databázi více společností, vyberte tu jednu společnost pro kterou chcete
Program je k dispozici. Pokud pole zůstane prázdné, program bude k dispozici všem společnostem v databázi.
- :guilabel:`Dostupné na“: vyberte aplikace, ve kterých je program dostupný.
- :guilabel:`Webová stránka“: Vyberte webovou stránku, na které je program k dispozici. Nechte pole prázdné, pokud chcete
její obsah zveřejnit na všech webech.
- :guilabel:`Prodejní místo“: Vyberte prodejní místa, na kterých je program dostupný.
toto pole nechat prázdné, aby bylo dostupné pro všechny:abbr:`PoS (prodejní místo)“.

.. poznámka::
Možnosti nabízené v rámci programového formuláře se liší podle typu programu.
vybrat „Programy“.

Všechny stávající karty, kódy, slevové poukazy atd., které byly vytvořeny pro tento program,
Dostupné prostřednictvím chytrého tlačítka umístěného v horní části formuláře.

.. obrázek: věrnostní slevy/cena-programu-zboží.png
:align:center
:alt:Tlačítko s programovými položkami na formuláři věrnostního programu.

.. poznámka::
V Odoo 17 (a později) se věrnostní karta nebo slevový kupon přiřazuje ke kontaktu v
databáze, na kontaktním formuláři se podmíněně zobrazí tlačítko „Karty věrnosti“.

.... obrázek: věrnostní slevy/věrnostní karta - tlačítko chytré.png
:synchronizace: střed
:alt:Tlačítko věrnostního programu chytré tlačítko, jak se zobrazuje na kontaktním formuláři v Odoo 17.

Tato chytrá tlačítka se zobrazí pouze tehdy, pokud je kontakt spojený s věrnostní kartou nebo slevovým kuponem.

..prodej/cenotvorba/druhy programů:

Typy programů
-------------

Různé možnosti programu, které jsou k dispozici na formuláři programu, jsou:

- :guilabel:`Kupóny“: Vytvářejte a sdílejte jednorázové kódy slev, které poskytují okamžitý přístup
odměny.
- :guilabel:Karty věrnostních programů: Když zákazník nakupuje, získává body, které může vyměnit za
odměny za současné a/nebo budoucí objednávky.
- :guilabel:`Slevy“: Zadejte podmíněné pravidlo pro objednávání produktů, které při splnění udělí
přístup k odměnám pro zákazníka.
- :guilabel:`Slevový kód“: Zadejte slevové kódy, které při vstupu do pokladny poskytnou slevu
zákazník.
- :guilabel:'Kup X a dostaneš Y': za každý (X) kus zboží je zákazníkovi připsán 1 bod. Po
Při shromažďování určitého množství kreditů si zákazník může za ně vyměnit (Y) předmět.
- :guilabel:`Následující objednávka kupónů“: Vytvořte a sdílejte jednorázové kódy, které umožňují přístup
odměnu na další objednávku zákazníka.

Podmíněné pravidlo
-----------------

Poté nastavte podmíněné pravidlo:guilabel:, které určuje, kdy se program použije pro
objednávku zákazníka.

V záložce „Pravidla a odměny“ klikněte na „Přidat“ vedle „Podmíněných pravidel“.
Přidat podmínky do programu. To zobrazí okno „Vytvořit podmíněné pravidlo“.
okno.

... obrázek: věrnostní slevy/cena podmíněných odměn.png
:align:center
:alt: Formulář věrnostního programu s názvem Pravidla a odměny.

.. poznámka::
Možnosti pro pravidla podmíněného výběru se liší v závislosti na zvoleném programu.
<prodej/cenotvorba/druhy programů>.

Pro konfiguraci podmíněných pravidel jsou k dispozici následující možnosti:

- :guilabel:`Slevový kód“: Zadejte vlastní kód, který bude použit pro „Slevový kód“
program nebo použít výchozí verzi vygenerovanou Odoo. Toto pole je k dispozici pouze v případě, že
:guilabel:`Typ programu“ je nastaven na „Slevový kód“.
- :guilabel:'Minimální počet kusů': Zadejte minimální počet produktů, které musí být zakoupeny
aby získal odměnu, nastavte minimální množství na alespoň 1, aby se ujistil, že zákazník musí
přijít k odměně za nákup.
- :guilabel:`Minimální nákupní částka“: Zadejte minimální částku (v měně) s :guilabel:`dph
Ve složce „Zahrnuto“ nebo „guilabel: daň zahrnuta“, které musí být uhrazeny, aby bylo možné přístup k odměně.
Pokud je zadána minimální částka i minimální množství, musí objednávka zákazníka splňovat
obě podmínky.
- :guilabel:`Produkty“: Vyberte konkrétní produkt (produkty), pro které se program vztahuje.
V poli „Zobrazit“ zatrhněte možnost „Všechny produkty“.
- :guilabel:`Kategorie produktů“: Vyberte kategorii výrobků, pro které se program vztahuje.
:guilabel:`Vše“ aplikovat na všechny produktové kategorie.
- :guilabel:`Štítek produktu:“ Vyberte štítek, který chcete použít k označení produktů s tímto konkrétním štítkem.
- :guilabel:`Grant“: Zadejte počet bodů, které zákazník získá za objednávku
:guilabel:`za každou měnu“, nebo :guilabel:`za jednotku zaplacenou“ (pro „Karty věrnosti“)
a programů „Kupte si X a získejte Y“.

.. obrázek:: věrnostní slevy/cena-podmínky.png
:align:center
:alt:Nastavení pravidel pro slevu nebo věrnostní program.

Klikněte na tlačítko „Uložit a zavřít“ nebo klikněte
:guilabel:`Uložit a nové“ pro uložení pravidla a okamžitě vytvořit další.

Odměny
-------

V záložce „Pravidla a odměny“ v programovém formuláři klikněte na „Přidat“ vedle
:guilabel:`Odměny“ k přidání odměn do programu. To zobrazí „Vytvořit odměnu“.
Pop-up okno.

.. poznámka::
Možnosti pro odměny se liší v závislosti na zvoleném typu programu.
<prodej/cenotvorba/druhy programů>.

Pro konfiguraci odměn jsou k dispozici následující možnosti:

- :guilabel:`Typ odměny“: Vyberte typ odměny mezi
:guilabel:`Sleva“, „Doprava zdarma“. Další možnosti konfigurace odměny
závisí na typu odměny, kterou si vyberete.

  - :free_product:

    - :guilabel:`Počet odměněných produktů“: vyberte počet zdarma dodaných výrobků zákazníkovi.
    - :guilabel:`Produkt“: vyberte produkt, který byl poskytnut jako odměna. Můžete zvolit pouze jeden produkt.
vybrány.
    - :guilabel:`Štítek produktu“: Vyberte štítek, který bude specifikovat volný produkt, na který se vztahuje
odměna.

  - :guilabel:`Sleva“:

    - Vložte slevu v procentech nebo v hodnotě.
:guilabel:"měna za bod" nebo "měna za objednávku". Pak vyberte, zda chcete měnu počítat
sleva se vztahuje na celý :guilabel:`Objednávku`, pouze na nejlevnější produkt na
objednávku nebo pouze „Konkrétní produkty“.
    - :guilabel:`Maximální slevy“: Zadejte maximální částku (v měně), kterou tento odměňující může udělit
slevu. Zanechte pole na hodnotu 0, pokud chcete neomezenou výši slevy.

  - :guilabel:`Doprava zdarma“:

    - :guilabel:`Maximální slevy“: Zadejte maximální částku (v měně), kterou tento odměňující může udělit
slevu. Zanechte pole na hodnotu 0, pokud chcete neomezenou výši slevy.

- Výměna za: Zadejte počet bodů, které je třeba vyměnit za odměnu (například
(programy věrnostních karet a „Kupte si X, získejte Y“).
- :guilabel:`Popis odměny“: Zadejte popis odměny, který se zobrazí na
zákazníkovi při placení.

.. obrázek: věrnostní slevy/cena-odměny.png
:align:center
:alt: Okno pro konfiguraci odměn v rámci slevového nebo věrnostního programu.
