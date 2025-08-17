=====================================
Fakturace na základě času a materiálu
=====================================

Zaúčtování podle času a materiálů se obvykle používá, když je možné přesně odhadnout velikost
projekt není možný nebo když se požadavky projektu změní.

To je odlišné od smlouvy na pevnou cenu, kdy zákazník souhlasí zaplatit určité celkové částky za
plnění smlouvy - ať už se za to musí platit zaměstnancům, poddodavatelům
dodavatelé, dodavatelské řetězce a podobně.

Aplikace Odoo Sales může vystavovat faktury za čas a různé další výdaje (např. dopravu, ubytování).
i nákupy, které jsou potřebné k plnění objednávky.

Aplikace a konfigurace nastavení
==============================

Nejprve je třeba přesně sledovat průběh projektu pomocí modulu Odoo *Projekt*.
Aplikace pro účetnictví musí být nainstalovány.

Pro instalaci aplikace *Project* přejděte na: „Hlavní panel Odoo -> Aplikace“. Poté proveďte
stránce „Aplikace“, najděte blok aplikace „Projekt“ a klikněte na „Aktivovat“.
Stránka se automaticky obnoví a vrátí na hlavní panel aplikace Odoo, kde je
je nyní k dispozici ke stažení.

Stejný proces opakujte, abyste nainstalovali aplikaci *Účetnictví*.

Po instalaci klikněte na ikonu aplikace „Účetnictví“ v hlavním panelu Odoo.
Přejděte na „Nastavení“ -> „Možnosti“. Na stránce „Možnosti“ přejeďte
a do sekce Analytics a zkontrolujte zaškrtnutí u položky Analytics.
Provede se kontrola účetnictví.

.. obrázek:time_materials/analytic-accounting-settings.png
:align:center
:alt:Jak aktivovat nastavení analytického účetnictví v nastavení účetnictví v Odoo.

Poté klikněte na tlačítko „Uložit“ a uložte všechny změny.

Poté přejděte na:menu:Odoo hlavní panel --> Projekt aplikace --> Konfigurace -->
Nastavení“. Na stránce „Nastavení“ v sekci „Správa času“ zkontrolujte
zaškrtněte políčko vedle funkce „Časové listy“.

Poté klikněte na tlačítko „Uložit“ a uložte všechny změny.

.. obrázek: time_materials/timesheets-feature.png
:align:center
:alt:Jak vypadá funkce Časových záznamů na stránce Nastavení projektu v Odoo.

.. prodej/fakturace/konfigurovaný produkt služby:

Konfigurace služby
=============================

S aktivovanou funkcí „Časové listy“ v aplikaci „Projekt“ je možné nyní fakturovat za odpracovaný čas.
na projektu, ale pouze v případě, že následující konfigurace produktů byly provedeny.

.. důležité:
Pouze s produkty, které mají nastavené Service, je možné vystavovat faktury za čas strávený na projektu.
jako produktový typ na své výrobní formě.

Chcete-li nakonfigurovat produkt služby, nejprve přejděte na: „Prodejní aplikace --> Produkty“.
Produkty“. Na stránce „Produkty“ vyberte požadovaný produkt služby k konfiguraci nebo
Klikněte na tlačítko „Nový“ pro vytvoření nového produktu.

V položce „Obecné informace“ v záložce „Produkt“ nastavte typ produktu.
Vyberte službu a poté v poli „Způsob fakturace“ vyberte možnost „Převod na účet“.
Vyberte: guilabel:"Založeno na časových záznamcích".

Dále z nabídky „Vytvořit na objednávku“ vyberte „Projekt & úkol“.
Nastavení ukazuje, že při vytváření prodejního příkazu s tímto konkrétním službou se vytvoří nový
Projekt a úkol vytvoříte v aplikaci Project*.

.. obrázek: time_materials/sluzby-produkty-obecne-nastaveni.png
:align:center
:alt: Správné nastavení položek Zásady fakturace a Vytvořit na objednávku pro služby.

.. poznámka::
Možnost „Úkol“ lze zvolit místo možnosti „Vytvořit na objednávku“.
nabídce. Pokud je vybráno „úkol“, zvolte existující projekt, do kterého se úkol objeví, ze seznamu
:guilabel:`Projekt“ pole, které se objeví pouze v případě, že je vybráno pole „Úkol“.
:guilabel:`Vytvořit na objednávku“ pole.

Přidejte čas strávený na prodejním příkazu
=============================

Po správném nastavení služby s produktem, který má správné *Způsoby fakturace* a *Vytvářet na
Možností objednávky* je přidat do prodejní objednávky čas strávený na zakázce.

Chcete-li vidět tento postup v akci, přejděte na: „Prodejní aplikace - Nový“
Vyplňte formulář, poté přidejte pole „Zákazník“ a v poli „Částky objednávky“ klikněte
„Přidat produkt“ a vyberte správně „nastavený služební produkt
z rozevírací nabídky.

Poté klikněte na tlačítko „Potvrdit“ pro potvrzení objednávky.

Po potvrzení objednávky se na formuláři objeví dvě chytré tlačítka v horní části formuláře:
„Projekty“ a „Úkoly“.

.. obrázek: time_materials/projekty-zadani-chytre-tlacitka.png
:align:center
:alt:Jak vypadají tlačítka pro projekty a úkoly na objednávce v Odoo Sales.

Pokud je kliknutá tlačítko s názvem „Projekty“, zobrazí se konkrétní projekt související s touto
objednávka na prodej. Když je kliknutá tlačítko „Úkoly“ se zobrazí konkrétní úkol projektu
s tímto prodejním příkazem. Oba jsou také dostupné v aplikaci *Projekt*.

Chcete-li přidat čas strávený na objednávce prodeje, klikněte na tlačítko „Úkoly“.

Vyberte v poli úkolu záložku „Časové listy“. Záložky „Časové listy“
zaměstnanci mohou být přiřazeni k práci na projektu a čas, který stráví prací na úkolu,
Přidali je zaměstnanci nebo osoba, která objednávku vytvořila.

Chcete-li přidat zaměstnance a dobu strávenou prací na úkolu, klikněte na tlačítko „Přidat řádek“.
Karta „Časové listy“. Pak vyberte vhodný „Datum“ a „Zaměstnance“.
Je také možné přidat stručný popis práce, kterou jste během této doby vykonali.
:guilabel:Popis, ale není povinný.

Poslední krok je zadat počet hodin strávených na úkolu do sloupce „Čas strávený“ a poté kliknout
odstranit tuto položku v záložce „Časové listy“.

.. poznámka::
Čas vložený do sloupce „Spent Hours“ je okamžitě zobrazen v
:guilabel:`Vyhrazený čas“ pole (umístěné v horní části formuláře úkolu), které je zobrazeno jako procento.
odráží, kolik z celkového přiděleného počtu hodin bylo doposud odpracováno.

Stejná informace je obsažena v číselných hodinách ve sloupci :guilabel:`Spent Hours`.
:guilabel:`Další hodiny“ pole v dolní části záložky „Časové rozvrhy“.

.... obrázek: časové materiály/časový záznam - karta úkolu.png
:synchronizace: střed
:alt:Jak vypadá záložka Časové listy na formuláři úkolu v Odoo Sales a Odoo Project.

Tento postup opakujte pro všechny zaměstnance a hodiny, které na projektu pracovali.

Fakturace času
==================

Jakmile jsou do úkolu přidány všechny potřebné pracovní síly a časové náklady, vrátí se k
fakturaci zákazníkovi za tyto hodiny. K tomu buď klikněte na tlačítko „Fakturace
Chytrý tlačítko v horní části úkolového formuláře nebo se vrátit zpět do prodejního objednávkového formuláře přes „breadcrumb“
v horním levém rohu obrazovky.

Vraťme se na prodejní objednávku a zobrazí se nám čas přidělený úkolu.
:guilabel:„Řádky objednávek“ (v „Doručeno“ sloupci) a v novém :guilabel:„Zaznamenáno“.
Chytrý tlačítko na vrchu prodejního příkazu.

Začněte vytvářet fakturu kliknutím na tlačítko „Vytvořit fakturu“ a vyberte
Vyberte „Běžný fakturační doklad“ z okna „Vytvořit fakturu“. Pak klikněte
:guilabel:`Vytvořit návrh faktury“.

Tímto způsobem se zobrazí „Návrh faktury zákazníka“, který jasně ukazuje všechny provedené práce.
v záložce „Řádky faktury“.

..tip:
Zkontrolujte sloupec Analytická distribuce v poli Klient.
„Faktura“, protože tato informace je nezbytná pro zajištění dalších úkolů v oblasti fakturace za práci a materiál.
správně a přesně dokončena.

.... obrázek:: time_materials/fakturaci-linek-casu.png
:synchronizace: střed
:alt:Návrh faktury, který ukazuje čas strávený na objednávce v Odoo Sales.

Klikněte na tlačítko „Potvrdit“ pro potvrzení faktury a pokračujte v procesu vystavování faktur.

.. viz též:
:doc:`fakturační politika“

Konfigurace výdajů
======================

Pokud chcete sledovat a fakturovat náklady související se zakázkou, musíte mít aplikaci *Odoo Expenses*.
nainstalovány.

Chcete-li nainstalovat aplikaci *Náklady*, přejděte na: „Hlavní panel Odoo -> Aplikace“. Pak
stránce „Aplikace“, najděte blok aplikace „Náklady“ a klikněte na
:guilabel:`Aktivovat“.

Stránka se automaticky obnoví a vrátí na hlavní panel Odoo.
Aplikace „Náklady“ je nyní dostupná ke stažení.

...Prodej/Fakturace/Přidat náklady k prodejnímu příkazu:

Přidejte náklady k objednávce
===========================

Přidat položku k objednávce nákupu lze nejprve přejít do aplikace „Náklady“ a poté z
hlavní přehled výdajů, klikněte na „Nový“, což odhalí prázdnou formu výdaje.

Do položky na výdaji přidejte popis výdaje (např. „Ubytování v hotelu“, „Letecká doprava“).
Ticket“). Následně v poli „Kategorie“ vyberte příslušnou možnost z roletky.
menu (např.: guilabel:"Jídlo", "Míle", "Doprava a ubytování").

.. poznámka::
Kategorie výdajů lze přidat a upravit kliknutím na:
Konfigurace --> Kategorie výdajů.

Poté zadejte celkovou částku výdaje do pole „Celkem“ a také případně
Další krok je zkontrolovat, že se použije správný zaměstnanec.
vybrat a určit, kdo zaplatil náklady v poli „Zaplaceno“:
„Zaměstnanec (na náhradu)“ nebo „Společnost“.

Dále v poli „Zákazník k doúčtování“ vyberte příslušný prodejní doklad.
položky nabídky. Pak vyberte stejnou informaci o prodejním příkazu z položky „Analytika
Distribuce také.“

.. poznámka::
pole „Analytická distribuce“ bude **pouze** obsahovat odpovídající objednávku.
možnost, pokud objednávka obsahuje službu, která je účtována na základě *Časových listin*.
*Zásadní milníky* nebo *Dodané množství*.

.. obrázek: time_materials/doplnky-podrobnosti-formular.png
:align:center
:alt:Jak správně vyplnit přílohu faktury, která je připojena k objednávce v Odoo.

Pokud existují nějaké faktury, které by měly být nahrány a připojeny k výdaji, klikněte na
tlačítko „Připojit doklad“, a nahrajte potřebné dokumenty k výdaji.
Není nutné, ale může ovlivnit schválení nákladu.

Po zadání všech informací klikněte na tlačítko „Vytvořit výkaz“.
zpráva, která obsahuje všechny informace o nákladech, které byly právě zadány.

.. obrázek: time_materials/expense-report-summary.png
:align:center
:alt:Jak vypadá souhrnné vyúčtování výdajů v Odoo Expenses.

Pak je možné zvolit možnost „Odeslat manažerovi k schválení“. Jakmile bude schváleno,
Ve výpisu příštího výplatního listu se objeví „Zpráva v následujícím výplatním listě“.

Pro ukázku celého průběhu vyberte :guilabel:`Předat manažerovi“. Pak se zobrazí
klikněte na tlačítko „Schválit“ a poté klikněte na „Přidat záznamy do knihy“.
Tento výdaj zaúčtovat do účetní knihy.

Fakturační výdaje
================

Fakturovat zákazníkovi náklady na objednávce
<účetnictví/fakturace/přidat výdaje k objednávce>`, přejděte na příslušnou objednávku.
:menu „Prodej“ nebo z výdajového hlášení v menu „Náklady“.
faktura, klikněte na tlačítko „Prodejní objednávky“ v horní části stránky.

Pokud byla faktura spojena se zakázkou, nově konfigurovaná položka nákladů má své vlastní
řádku v záložce „Řádky objednávky“ a může být fakturováno zákazníkovi.

.. obrázek:: časové_materiály/faktura-od-objednávky.png
:align:center
:alt: Náklad, který se zobrazuje na záložce Objednávky v aplikaci Odoo Sales.

Zaplatit zákazníkovi za náklady na objednávce zboží klikněte na tlačítko „Vytvořit fakturu“, vyberte
Vyberte „Běžný fakturační doklad“ z okna „Vytvořit faktury“, pak klikněte
:guilabel:`Vytvořit návrh faktury“.

Tím se zobrazí zálohová faktura pro výdaj. Poté můžete proces vystavování faktur
Může být dokončena v běžném režimu.

.. obrázek:time_materials/faktura-zakaznika-za-nacenou-sluzbu.png
:align:center
:alt: Vzorový faktura zákazníka za náklady vzniklé z prodejního příkazu v Odoo Sales.

Konfigurace nákupu
======================

Pro fakturaci zákazníkovi za nákupy provedené na prodejním příkazu je aplikace
*musí být nainstalován.*

Pro instalaci aplikace Purchase přejděte na hlavní obrazovku Odoo: „Hlavní panel - Aplikace“.
Následně na stránce „Aplikace“ najděte blok „Koupit“ a klikněte
:guilabel:`Aktivovat“. Stránka se automaticky obnoví a vrátí na hlavní panel Odoo.
Aplikace „Nákup“ je nyní k dispozici ke stažení.

...Prodej/fakturace/Přidat nákup k objednávce prodeje:

Přidejte nákup k objednávce na prodej
===========================

Pokud chcete přidat nákup do objednávky na prodej, musíte nejprve vytvořit nákupní objednávku.
objednávku, přejděte na:menu-selection: „Nákup aplikace – Nová“ pro zobrazení prázdného formuláře objednávky.

Nejprve přidejte do objednávky dodavatele pomocí :guilabel:Vendor. Pak pod záložkou :guilabel:Produkty
Klikněte na tlačítko „Další možnosti sloupce“ (viz obrázek).
v nich umístěné tečky vpravo od hlaviček sloupců. Z nabídky vyberte
:guilabel:`Analytická distribuce“.

.. obrázek: čas_materiálů/příplatková služba - analytická distribuce.png
:align:center
:alt:Jak přidat sloupec pro analytické rozložení na objednávkovém formuláři v Odoo Purchase.

Po přidání sloupce „Analytická distribuce“ do hlaviček v sekci „Produkty“
kartu objednávky, pokračujte v přidání produktů do objednávky.
Klikněte na tlačítko „Přidat produkt“ a vyberte požadovaný produkt z nabídky.
Všechny produkty k přidání.

.. důležité:
Aby mohl být nákup správně fakturován na prodejní objednávku, musí být v nákupu zadáno zboží.
objednávka musí být označena jako „Může být fakturována“, a měla by mít nastavené „Zásady fakturace“
do položky „Dodané množství“ a v poli „Za cenu“ vybrat možnost „Ano“.
:guilabel:`Znovuúčtování výdajů“ pole na své produktové kartě.

.. obrázek:: čas/materiál/produktová forma/nastavení faktury a nákupu.png
:synchronizace: střed
:alt:Nastavení produktu pro fakturaci nákupního příkazu na prodejní objednávku v Odoo.

Poté vyberte vhodný analytický rozdělení spojený s objednávkou.
s nímž je tato objednávka spojena. K tomu klikněte na prázdné pole „Analytická distribuce“
pole, které zobrazí okno „Analytické“ s možnostmi.

Poté vyberte z rozevírací nabídky „Oddělení“ analytickou distribuci.
s požadovaným prodejním příkazem k fakturaci nákupu.

.. obrázek: časové materiály/analytická distribuce.png
:align:center
:alt:Jak vybrat oddělení analytické distribuce z objednávky v Odoo.

Jakmile jsou všechny informace zadány v záložce „Zboží“ objednávky, potvrďte
Objednávku potvrdíte kliknutím na tlačítko „Potvrzení objednávky“. Poté klikněte na „Dodání produktů“
byla přijata, vytvoří se proto faktura.

.. poznámka::
Pokud musí být před ověřením přijetí zboží zadány sériové čísla nebo šarže, pak na
pokladní doklad, klikněte na ikonu „podrobnosti“ reprezentovanou čtyřmi svislými liniemi umístěnou
spadá do pravicového spektra.

Tím se zobrazí podrobnosti o operaci v záložce „Podrobné operace“, kde je potřeba vyplnit pole „Sériové číslo“
Množství čísel a :guilabel:Dokončeno lze přidat. Když je hotovo, klikněte na :guilabel:Potvrzeno
potvrdit údaje.

Poté klikněte na tlačítko „Zkontrolovat“ pro ověření objednávky.

Poté se vraťte k objednávce a klikněte na
:guilabel:`Vytvořit fakturu dodavateli“ pro vytvoření faktury dodavatele, která může být zákazníkovi naúčtována.
prodejní objednávka.

.. obrázek: time_materials/faktura-prodejce.png
:align:center
:alt:Návrh faktury dodavatele pro vystavení faktury zákazníkovi v Odoo.

.. poznámka::
Ujistěte se, že do pole „Datum faktury“ v poli „Návrh na účet dodavatele“ zadáte datum.
potvrzující. Pokud není zadána hodnota „Datum faktury“, objeví se okno s chybou, které požádá o zadání této hodnoty.
informace, které je nutné zadat před potvrzením.

Poté klikněte na tlačítko „Potvrdit“ a potvrďte fakturu dodavatele, která se automaticky přidá do
objednávka prodeje, kde se může přímo na zákazníka vystavit faktura.

Nákup faktury
================

Nejprve přidejte nákup do prodejního příkazu.
Vyberte příkaz „Objednávka“ (s prodejem/fakturací/dodáním do objednávky), poté se přesuňte na požadovanou objednávku.
aplikaci „Prodej“.

Na prodejním příkazu připojeném k nákupnímu příkazu je nyní zakoupený produkt označen
výrobní řadu pod záložkou „Řádky objednávek“ a je připravena k fakturaci.

.. obrázek:time_materials/purchase-order-on-sales-order.png
:align:center
:alt:Nákupní objednávka produktu na prodejní objednávku k účtování zákazníkovi přes Odoo Sales.

Pro vystavení faktury kupujícímu stačí pouze kliknout na tlačítko „Vytvořit fakturu“ a vybrat
Vyberte „Běžný fakturační doklad“ z okna „Vytvořit faktury“, pak klikněte
:guilabel:`Vytvořit návrh faktury“.

Tím se zobrazí faktura v návrhu s nově přidaným produktem objednávky.
kartě „Řádky faktury“.

.. obrázek:time_materials/návrh-faktury-se-zbožím.png
:align:center
:alt:Návrh faktury pro zákazníka s přiloženým nákupním produktem v příkazu k prodeji v Odoo.

Pro dokončení procesu fakturace klikněte na tlačítko „Potvrdit“ pro potvrzení faktury a pak
V poli „Registrace platby“ v okně „Registrace platby“.
