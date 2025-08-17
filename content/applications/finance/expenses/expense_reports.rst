===============
Zprávy o výdajích
===============

Když jsou náklady připraveny k předložení (například na konci pracovní cesty nebo jednou měsíčně),
Musí být vytvořen výkaz o nákladech. Otevřete hlavní panel aplikace „Náklady“ (výběr z menu):
Zobrazuje výchozí panel „Moje výdaje“ (guilabel:My Expenses). Pokud chcete, můžete se přepnout na
:menu-vyber->„Aplikace výdajů“--> „Moje výdaje“--> „Moje výdaje“.

Náklady jsou barevně označeny podle stavu. Každá položka s stavem „k zaznamenání“ (náklad
(které ještě musí být přidány do výkazu o nákladech) jsou zobrazeny modrým písmem. Všechny ostatní stavy
(:guilabel:"Odeslat", :guilabel:"Odesláno" a :guilabel:"Schváleno") je text zobrazen černě.

...výdaje/vytvořit zprávu:

Vytvářejte výdajové faktury
======================

Nejprve vyberte každou požadovanou položku nákladů, které chcete přidat do zprávy v sekci „Moje výdaje“.
přístrojové desce, zaškrtnutím políčka u každé položky nebo rychlým výběrem všech výdajů v
zaškrtněte políčko vedle sloupce s názvem „Datum výdajů“, pokud je potřeba.

Další způsob rychle přidat všechny výdaje, které nejsou na faktuře, je kliknout na
tlačítko „Vytvořit zprávu“ bez výběru žádných nákladů a Odoo automaticky vybere
všechny výdaje s označením „Předložit“ a nejsou již zahrnuty v hlášení.

.. obrázek: expense_reports/create-report.png
:align:center
:alt:Vyberte výdaje, které chcete podat, a poté vytvořte zprávu.

.. poznámka::
Každou položku lze vybrat ze seznamu „Moje výdaje“ kromě výdajů s nulovým zůstatkem.
statusu „Schváleno“.

Tlačítko „Vytvořit zprávu“ je vidět, dokud nebude alespoň jedna položka nákladů.
list s stavem buď :guilabel:`K Oznámení“ nebo :guilabel:`K Odevzdání“.

Když je kliknutá tlačítko „Vytvořit zprávu“, všechny výdaje s stavem :guilabel:`To
Vyplněné výdajové hlášení, které ještě není zahrnuto v jiném výdajovém hlášení, se objeví na nově vytvořené výdajové hlášení.
zpráva.

Pokud jsou všechny výdaje na zprávě „Moje výdaje“ již spojeny s jiným výdajem
zprávě se objeví okno s výzvou „Nesprávná operace“, které uvede „Máte prázdný soubor“.
výdaje, které je nutné uvést.

Jakmile jsou náklady vybrány, klikněte na tlačítko „Vytvořit zprávu“. Nová zpráva
je zobrazena se všemi položkami uvedenými v záložce „Náklady“. Pokud je k ní přiložen doklad
individuální výdaj, mezi kterými se zobrazí ikonka :icon:`fa-paperclip` :guilabel:`(paperclip)`
Sloupce „Zpětné fakturace“ a „Distribuce analytického účtu“.

Při vytváření zprávy se objeví rozsah nákladů ve formuláři :guilabel:`Zpráva o výdajích
Popisku, který je v podstatě výchozí hodnotou. Doporučuje se tento prázdný popisek upravit na krátkou charakteristiku každého
report k udržení nákladů v pořádku. Zadejte popis výdajového reportu, například „Klient
Trip NYC“, nebo „Kancelářské potřeby pro prezentace“ v poli „Souhrn výdajů“.

Felda Employee, Paid By a Company se automaticky vyplní
informace o jednotlivých výdajích.

Poté vyberte manažera z rozevírací nabídky a přiřaďte mu k přezkoumání zprávy.
Pokud je třeba, aktualizujte pole „Deník“ pomocí vyhledávacího pole.

.. obrázek: expense_reports/expense-report-summary.png
:align:center
:alt: Zadejte krátký popis a vyberte správce pro tento report.

Pokud některé výdaje v hlášení chybí, je možné je dodatečně přidat z této podoby hlášení.
takže klikněte na „Přidat řádek“ v záložce „Náklady“.

Zobrazí se okno s názvem „Přidat řádky výdajů“, které zobrazuje všechny dostupné výdaje (s
Stav „Předložit“ (status: guilabel: To Submit), který lze přidat do zprávy.

Pokud je potřeba přidat novou položku nákladů, která se na seznamu nevyskytuje, klikněte na tlačítko „Nový“
Vytvořte novou položku výdajů (<../expenses/log_expenses>), kterou přidejte do zprávy.

Zaškrtněte políčko vedle každé položky nákladů, které chcete přidat, a pak klikněte na tlačítko „Vybrat“.

Tím se odstraní okno s upozorněním a položky se zobrazí v hlášení.

.. obrázek: expense_reports/add-an-expense-line.png
:align:center
:alt:Přidejte další výdaje do zprávy před odesláním.

.. poznámka::
Expense reporty lze vytvářet ve třech různých místech:

   #Navigujte na hlavní panel aplikace „Výdaje“ (přístupný také přes
:menuselection:`Náklady aplikace --> Můj rozpočet --> Můj rozpočet`)
   #Navigujte na:menu-selection:'Výdaje aplikace -> Můj rozpočet - > Moje zprávy'
   #Navigujte na: menu „Výdaje aplikace“ -> „Zprávy o výdajích“.

Ve kterékoli z těchto obrazovek klikněte na :guilabel:`New`, abyste vytvořili nový výkaz o nákladech.

..._náklady/odeslat:

Podávat výdajové hlášení
======================

Po dokončení výkazu o nákladech je další krok předložení výkazu manažerovi.
Schválení. Chcete-li zobrazit všechny výdajové faktury, přejděte na:
Moje zprávy“. Otevřete konkrétní fakturu ze seznamu výdajových faktur.

.. poznámka::
Zprávy musí být podány jednotlivě a **nemohou být** podány ve skupinách.

Pokud je seznam velký, může být užitečné seskupit výsledky podle stavu, protože pouze zprávy s
Stav „Předloženo“ musí být předložen, zprávy s hodnotou „Schváleno“ nebo
Status „Předložené“ ne.

Náklady na předložení lze identifikovat pomocí stavu „Předložit“ a
modrým písmem, zatímco všechny ostatní výdaje jsou v černém písmu.

.. obrázek: expense_reports/expense-status.png
:align:center
:alt:Zprávu předložte manažerovi.

.. poznámka::
Stav každé zprávy je uveden v sloupci „Stav“. Pokud je stav „V pořádku“,
sloupec není viditelný, klikněte na ikonu „Nastavení“
v závěru řádku a zaškrtněte políčko vedle :guilabel:`Stav`.
rozbalovací nabídka.

Klikněte na zprávu, abyste ji otevřeli. Pak klikněte na tlačítko „Odeslat manažerovi“. Po odeslání zprávy
Další krok je čekat na schválení manažerem.

.. důležité::
schválení výdajů v sekci „Schvalování výdajů“ nebo „Přidání výdaje“.
výdajů a „vracení“ (reimbursement) výdajů
jsou pouze pro uživatele s příslušnými :doc:`právy přístupu

