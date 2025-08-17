============
Zaznamenávat výdaje
============

Předtím, než mohou být náklady uhrazeny, musí být každá jednotlivá položka zaznamenaná v databázi.
Výdajový záznam lze vytvořit třemi různými způsoby:
<náklady/ruční náklad>`, „nahrajte fakturu“ <náklady/nahrajte-fakturu>, nebo „pošlete e-mail“ <náklady/poslat-e-mail>.
účtenku na přednastavenou e-mailovou adresu.

.. _náklady/ruční náklad:

Vyplňte ručně výdaje
=======================

Zaznamenat novou položku výdajů otevřete aplikaci „Výdaje“, která zobrazuje „Moje
Stránka výdajů, pokud není jinak nastaveno.

.. tip::
Tento pohled je možné získat také z:menuselection:`Náklady aplikace --> Moje náklady --> Můj
Náklady.

Poté klikněte na tlačítko „Nový“ a do pole, které se objeví, zadejte následující údaje:

- :guilabel:`Popis“: Zadejte krátký popis výdaje. Tento by měl být stručný a
informativní, například „oběd s klientem“ nebo „hotel pro konferenci“.
- :guilabel:`Kategorie výdajů“: Vyberte kategorii výdajů z roletky, která se nejvíce blíží
Je to stejné jako u výdajů.
- :guilabel:'Celkem': Zadejte celkovou částku zaplacenou za výdaj jedním ze dvou způsobů:

  #Pokud je výdaj za jednu položku/výdaj a kategorie vybraná pro jednu položku.
do pole „Celkem“ (pole „Množství“ je skryté) zadat náklady.
  #Pokud je výdaj na více kusů stejné položky s pevnou cenou,

celková cena se automaticky aktualizuje s tím správným součtem. Celkové náklady se zobrazují pod
:guilabel:`Množství“.

...... příklad::
V případě ujetých kilometrů je v poli „Cena za jednotku“ vyplněna cena za 1 km.
1 míle. Zadejte hodnotu proměnné „Kvantita“ jako počet ujetých mil a celkový počet
Výpočetní.

- :guilabel:`Zahrnuté daně“: Pokud byly na položku výdajů nastaveny daně, procento daně
a částka se zobrazí automaticky po vložení buď celkové částky nebo částky.
:guilabel:`Množství“.

.. poznámka::
Pokud je na položku daně nakonfigurován výdajový účet, hodnota :guilabel:`Zahrnuté daně` se aktualizuje.
v reálném čase, jakmile se změní :guilabel:`Celkem“ nebo :guilabel:"Množství".

- :guilabel:`Zaměstnanec“: Vyberte zaměstnance, na kterého se tato položka vztahuje.
- :guilabel:„Zaplaceno“: Klikněte na tlačítko pro označení toho, kdo zaplatil za výdaj, a
Bude vám vrácena. Vyberte buď „Zaměstnanec (na úhradu)“ nebo „Společnost“.
Pokud je vybrána kategorie výdajů, tento prvek nemusí být viditelný.
- :guilabel:`Datum výdaje“: Při zadávání datumu do pole se objeví okno s kalendářem.
Zvolte datum vzniku výdaje.
- :guilabel:`Účet“: Vyberte z roletky účet, na který má být výdaj zaúčtován.
Přihlášený.
- :guilabel:`Zaplacení zákazníkovi“: Pokud je výdaj něco, co má být zaplaceno zákazníkem
zákazníkovi, vyberte SO (Prodejní objednávka) a zákazníka, který bude fakturován za tuto
výdaje z nabídky. Všechny prodejní objednávky v nabídce obsahují obě pole :abbr:`SO
(objednávka na prodej) a společnost, pro kterou je objednávka napsaná. Po uložení výdaje
Zadaný zákaznický název zmizí a na výdaji je vidět pouze zkratka SO (objednávky).

...... příklad::
Klient požaduje na místě schůzku pro návrh a instalaci zakázkového nábytku.
zahradu a souhlasí s náklady spojenými s tímto projektem (např. cestovné, ubytování, stravu,
atd.). Všechny náklady spojené s tímto jednáním by ukazovaly na objednávku zahradního nábytku na zakázku.
(který také odkazuje na zákazníka) jako „Zákazník pro opětovné vyúčtování“.

- Vyberte účet, na který se má výdaj zaúčtovat.
výběr z rozbalovací nabídky pro buď „Projekty“, „Oddělení“ nebo obojí.
Pokud je potřeba, můžete vytvořit seznam účtů pro každou kategorii a upravit procento pro každý analytický
Přiřaďte procento k účtu, když do něj zadáte hodnotu procenta vedle každého účtu.
- :guilabel:`Společnost“: Pokud je zřízeno více společností, vyberte společnost, na kterou se má výdaj uplatnit.
Vyberte z roletkového menu. Současná společnost se do pole automaticky vyplní.
- :guilabel:`Poznámky...“: Pokud jsou k výdaji potřeba nějaké poznámky, zadejte je do poznámek
pole.

.. obrázek:log_expenses/expense-filled-in.png
:align:center
:alt:Vyplněná žádost o náhradu nákladů na oběd pro klienta.

Přiložte faktury
---------------

Po vytvoření výdajového záznamu je potřeba připojit přílohu. Klikněte na
Tlačítko „Připojit účtenku“ a objeví se průzkumník souborů. Přejděte na účtenku, kterou chcete připojit.
připojené a klikněte na „Otevřít“.

Nový doklad se zaznamenává do chatu a vedle čísla dokladu se objeví
:ikonka: „fa-paperclip“ :guilabel: (papírková sponka) ikona. K jedné zprávě lze připojit více příloh
individuální záznam o výdajích, pokud je potřeba.

.. obrázek: log_expenses/faktura-ikona.png
:align:center
:alt:Přiložte fakturu a objeví se v chatu.

.. výdaje/nahrát fakturu:

Náklady na upload
===============

Je možné mít vytvářet automaticky výdajové doklady nahráním PDF faktury.
Tato funkce vyžaduje zapnutí nastavení a nákup:abbr:`IAP (in-app purchases)`
Kredity.

Nastavení digitálního zpracování
-----------------------

Pro skenování příjmových dokladů přejděte do: `Expenses app --> Konfigurace -->
Nastavení“, a zaškrtněte políčko vedle možnosti „Digitální zpracování výdajů (OCR)“. Poté
Klikněte na tlačítko „Uložit“. Pokud je aktivní, zobrazí se další možnosti. Klikněte na příslušné políčko
tlačítko pro výběr jedné z následujících možností:

- :guilabel:Nedigitalizovat“: vypne digitalizaci účtenek.
- :guilabel:'Digitizace na požádání': pouze digitalizuje účtenky, pokud je o to požádáno.
:tlačítko „Digitalizovat doklad“ se objeví na fakturách. Po kliknutí je účetní doklad
Je skenován a účetní záznam je aktualizován.
- :guilabel:`Automaticky digitalizovat“: automaticky digitalizuje všechny účtenky, když jsou nahrané.

Pod těmito možnostmi jsou dvě další odkazy. Klikněte na ikonu „fa-arrow-right“ a poté na odkaz „Koupit
Kredity k nákupu kreditů pro digitalizaci příjmu. Klikněte na ikonu :icon:`fa-arrow-right`.
Klikněte na odkaz „Zobrazit moje služby“ pro zobrazení seznamu všech aktuálních služeb a jejich zbývajícího kreditu.
balancí.

Pro více informací o digitalizaci dokumentů a :abbr:`IAPs (nákupy v aplikaci)` se podívejte na
Dokumentace k nákupům v aplikaci (IAP):

.. poznámka::
Když je zapnutá možnost „Digitální zpracování výdajů (OCR)“, je potřebný modul
je nainstalován, takže lze skenovat účtenky. Vypnutím této možnosti se modul deinstaluje.

Pokud by se v nějakém okamžiku objevila touha na chvíli přestat digitalizovat účtenky, vyberte
:guilabel:`Nedigitalizovat“ možnost. Důvodem, proč je tato volba k dispozici, je to, aby modul nebyl
odinstalován, což umožní v budoucnu zapnout digitální funkce vybráním jedné z ostatních.
dvě možnosti.

Nahrát faktury
---------------

Otevřete aplikaci „Výdaje“ a z obrazovky „Moje výdaje“ klikněte na
„Nahrát“ a objeví se prohlížeč souborů. Vyhledejte požadovaný doklad, vyberte jej a pak
Klikněte na tlačítko „Otevřít“.

.. obrázek:log_expenses/upload.png
:align:center
:alt:Vytvořte výdaj pomocí skenování účtenky. Klikněte na Scan v horní části obrazovky Dashboardu výdajů
pohled.

Potvrzení je naskenováno a vytvořena nová položka výdajů. V poli „Datum výdaje“ se zobrazí
obydlené dnešním datem a s dalšími poli na základě skeneru, jako například
:guilabel:`Celkem“.

Klikněte na nový záznam a otevřete formulář pro jednotlivé výdaje. Zde proveďte případné změny.
Skenovaný doklad se objeví v chatu.

.. _náklady/e-mailová faktura:

E-mailové výdaje
==============

Místo toho, abyste jednotlivě vytvářeli každou položku výdajů v aplikaci **Výdaje**, mohou být výdaje automaticky
vytvořené odesláním e-mailu na e-mailový alias.

Pro to je potřeba nejprve nastavit e-mailovou adresu. Přejděte na:
Konfigurace --> Nastavení. Zajistěte, aby vedle políčka vedle :guilabel:`Příchozí e-maily“ byla zaškrtnuta.
Výchozí e-mailová adresa je *expense@(doména).com*. Změňte e-mailovou adresu zadáním požadované e-mailové adresy
V poli vpravo od „Alias“ a poté klikněte na „Uložit“.

.. obrázek: log_expenses/alias-email.png
:align:center
:alt:Výchozí e-mailová adresa, která se používá pro e-mailovou adresu aliasu výdajů.

.. poznámka::
Pokud je potřeba nastavit doménové jméno, pak klikněte na ikonu „fa-arrow-right“ a zvolte možnost „Nastavení domény“.
alias se zobrazuje pod zaškrtávací políčkem „Příchozí e-maily“, místo e-mailové adresy
pole.

.... obrázek: log_expenses/email-alias.png
:align:center
:alt: Vytvoření doménového jména kliknutím na odkaz.

Viz dokumentaci k tématu „/applications/websites/website/configuration/domain_names“
návod na instalaci a další informace.

Jakmile je nastavená doménová přezdívka, zobrazí se pole e-mailové adresy pod tímto.
:guilabel:`Příchozí e-maily“ v nastavení aplikace „Náklady“.

Jakmile je zadaná e-mailová adresa, můžete na tuto přezdívku posílat e-maily a vytvářet nové výdaje.
bez nutnosti být v databázi Odoo.

Pro zaslání faktury e-mailem vytvořte novou zprávu a do ní zadejte interní referenci produktu.
kód (pokud je k dispozici) a částku nákladů jako předmět e-mailu. Následně přiložte
fakturu na e-mail. Odoo vytvoří výdaj podle informací z předmětu e-mailu a
spojit s účtenkou.

Chcete-li zkontrolovat vnitřní odkaz kategorie výdajů, přejděte na:
Konfigurace --> Kategorie výdajů. Pokud je u kategorie výdajů uvedena interní referenční hodnota
je uvedeno v sloupci „Vnitřní odkaz“.

.. obrázek::log_expenses/ref.png
:align:center
:alt: Interní referenční čísla jsou uvedena v hlavním pohledu na výdaje.

Chcete-li přidat vnitřní odkaz na položku výdajů, klikněte na položku výdajů, abyste otevřeli výdaje.
Kategorie. Do příslušného pole zadejte :guilabel:`Vnitřní odkaz`. Pod
V poli „Interní odkaz“ se objeví tento text: „Toto je interní odkaz.
předmět předpony při odeslání e-mailem.

.. obrázek: log_expenses/mileage-internal-reference.png
:align:center
:alt: Interní referenční čísla jsou uvedena v hlavním pohledu na výdaje.

.. příklad::
Pokud zašlete fakturu na e-mail za 25 dolarů za jídlo během pracovní cesty, pak jako předmět
Bylo by to „JÍDLO 25 $.“

Vysvětlení:

   - Vnitřní odkaz na položku „Náklady“ s kategorií „Jídlo“ je „FOOD“.
   - Hodnota položky „Náklady“ je 25 $.

.. poznámka::
Pro bezpečnostní účely přijímá pouze e-maily zaměstnanců ověřené v Odoo při tvorbě
výdaj za e-mail. Chcete-li potvrdit autentickou e-mailovou adresu zaměstnance, přejděte na stránku
kartu v aplikaci „Zaměstnanci“ a odkazovat na pole „E-mailová adresa“.

.... obrázek: log_expenses/autenticovana-emailova-adresa.png
:align:center
:alt: Vytvoření doménového jména kliknutím na odkaz.
