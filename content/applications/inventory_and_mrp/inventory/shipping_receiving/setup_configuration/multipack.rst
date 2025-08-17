=======================
Balíčky s více položkami
=======================

V některých případech může být objednávka na dodání více položek odeslána v několika balících.
Toto může být nutné v případě, že jsou položky příliš velké na to, aby se daly poslat jedním balíčkem, nebo pokud některé položky
nemohou být zabalené dohromady. Při odeslání jedné objednávky v několika balících poskytuje
flexibilita při balení každého zboží bez nutnosti vytvářet více dodacích objednávek.

Konfigurace
=============

Chcete-li rozdělit dodací objednávku na více balíčků, musí být zapnuté nastavení „Balíčky“.
Chcete-li tak učinit, přejděte na: „Sklad --> Konfigurace --> Nastavení“ a zapněte
zaškrtávací políčko vedle :guilabel:`Soubory“. Klikněte na :guilabel:`Uložit“ pro potvrzení změny.

.. obrázek: multipack/packages-setting.png
:align:center
:alt:Nastavení balíků v nastavení aplikace Inventura.

... inventář/dodání/více balíčků:

Zasílejte zboží ve více balících
===============================

Pokud chcete položky v jedné objednávce rozdělit do více balíčků, začněte tím, že se přesunete na
Vyberte možnost „Skladové zásoby -> Přijaté objednávky“ a poté vyberte přijatou objednávku, která má více položek.
položky, více kusů stejné položky nebo obojí.

V záložce „Provoz“ vyberte ikonu „⁞≣“ v řádku produktu
Ta bude v první zásilce.

.. obrázek: multipack/produkt-menu-ikonka.png
:align:center
:alt:Ikona nabídky produktu v objednávce dodání.

Zobrazí se okno s podrobnými operacemi. V tabulce na spodní části
Pop-up okno, sloupec „Rezervace“ zobrazuje celkové množství produktu včetně
dodací list.

Pokud bude celé množství odesláno v první zásilce, uveďte číslo
Sloupec „Dokončeno“ v sloupci „Rezervace“. Pokud bude méně než celkové množství,
zasílané v první zásilce, uvede nižší číslo než je viditelné na
Kolonka „Rezervace“. Klikněte na „Potvrzení“ a poté na „Dokončeno“
a zavřít okno.

.. obrázek: multipack/detailed-operations.png
:align:center
:alt:Popis podrobné operace pro produkt v dodacím listu.

Opakujte stejné kroky pro každé množství položek, které je zahrnuto v první dodávce. Pak klikněte
:guilabel:`Vložit do balíčku“ vytvořit balíček s vybranými položkami.

.. obrázek: multipack/put-in-pack.png
:align:center
:alt:Tlačítko „Přidat do balíku“ na objednávce dodání.

Pro další balíček postupujte stejným způsobem jako výše popsaný, označte množství každého předmětu
by měl být součástí balení jako :guilabel:`Done` před kliknutím na :guilabel:`Put In Pack`
dodací příkaz. Takto pokračujte, dokud nebude do balíku přidána celková hmotnost všech položek.

Konečně po odeslání všech balíčků klikněte na tlačítko „Potvrdit“, abyste potvrdili, že
dodací list byl dokončen.

..tip:
Po vytvoření jednoho nebo více balíčků se objeví tlačítko „Balíčky“ ve smart menu.
horním pravém rohu objednávky. Klikněte na tlačítko „Zásilky“ chytré klávesy, abyste se dostali do
:guilabel:`Dodací objednávka“ stránce pro každý balík, kde lze vybrat konkrétní balík k zobrazení všech
zahrnutých v ní.

.... obrázek: multipack/packages-smart-button.png
:srovnání: do středu
:alt:Tlačítko chytré balíčky na objednávce dodání.

Vytvořte objednávku na pozdější dodání
================================================

Pokud některé položky budou dodány později než ostatní, není potřeba je zabalit do balíčku
až do chvíle, kdy budou připraveny k odeslání. Namísto toho vytvořte poptávku na položky, které se později odesílají.

Začněte odesíláním položek, které budou okamžitě odeslány. Pokud se bude odesílat více
balíčky, postupujte podle kroků uvedených v části „Dodání více balíků“ níže.
je nutné. Pokud budou odeslány v jednom balíčku, stačí označit sloupec „Dokončeno“
množství každého položky, kterou je nutné odeslat, ale **ne** klikněte na tlačítko „Uložit do balíku“.

Po označení všech položek, které jsou ihned k odeslání, se zobrazí tlačítko
tlačítko „Potvrdit“ a zobrazí se okno s dotazem „Vytvořit objednávku na dodání?“. Pak klikněte
tlačítko „Vytvořit objednávku na dodání“. To potvrzuje, že zboží bude hned odesláno a
vytvoří novou objednávku na dodání zboží, které bude následně odesláno.

.. obrázek: multipack/backorder-pop-up.png
:align:center
:alt:Okno s náhledem vytvoření objednávky na dodání.

Dodací objednávka na dodání zboží ze záložního skladu bude uvedena v chatu původní dodací objednávky.
zpráva, která zní: „Vytvořeno objednávka na vyzvednutí bez časového omezení XXXXX“. Klikněte
V zprávě klikněte na „WH/OUT/XXXXX“ a zobrazí se vám objednávka dodání do zásoby.

.. obrázek: multipack/backorder-chatter.png
:align:center
:alt:Dodací objednávka zadaná jako dodatek k původní dodací objednávce.

Dodací objednávka zadaná jako dodání ze zásob lze také najít kliknutím na: menu výběr: „Sklad“.
kliknutím na tlačítko „Zpětné objednávky“ v kartě „Dodací objednávky“ a výběrem
dodací list.

.. obrázek: multipack/back-orders-button.png
:align:center
:alt:Tlačítko „Zadat zpětný odběr“ na kartě Dodací objednávky.

Jakmile budou zbývající položky připraveny k odeslání, přejděte na objednávku dodání zboží ze zásob.
položky lze odeslat v jednom balíčku kliknutím na tlačítko „Potvrdit“ a výběrem
„Použít“ v okně „Okamžitý převod?“, které se objeví, nebo zaslat
více balíčků podle kroků uvedených v části výše.

Je také možné poslat některé položky, zatímco vytváříte další objednávku na zbývající zboží.
postupujte stejně jako při vytváření první objednávky.
