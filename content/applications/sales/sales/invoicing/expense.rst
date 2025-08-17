===============================
Zaúčtujte náklady zákazníkům
===============================

Při práci na projektu pro klienta se zaměstnanci často musí vydat ze svého peněz za různé
náklady na projekt.

Příkladem může být situace, kdy zaměstnanec musí zaplatit za hotel z vlastních peněz.
na místě pro klienta. Tuto položku by měla firma vystavit fakturu svému zákazníkovi.
Odoo, takové výdaje lze rychle vystavit fakturou klientovi souvisejícímu s projektem.

Žádost o náhradu výdajů
====================

Pokud chcete zákazníkovi vystavit fakturu za náklady, musí být aplikace „Náklady“ **nainstalována**.

Pro instalaci aplikace *Náklady* přejděte na hlavní obrazovku Odoo a vyberte možnost „Aplikace“.
a klikněte na tlačítko „Instalovat“ v bloku aplikace *Náklady*. Po kliknutí se Odoo nainstaluje
aplikace, obnoví stránku a vrátí se na hlavní panel aplikace Odoo.

Přidat položky nákladů k prodejním objednávkám
============================

Nejprve potvrďte prodejní objednávku v aplikaci *Prodej*, kam lze připsat náklady na reklamace.
Přidejte nový doklad nebo vytvořte novou objednávku od začátku. K tomu přejděte na záložku „Prodej“.
Aplikace „Nový“. To způsobí, že se objeví prázdná citátní forma.

Poté přidejte pole „Zákazník“ a produkt do záložky „Dodací řádky“, kliknutím
:guilabel:`Přidat produkt“. Následně vyberte produkt z nabídky.

Nakonec klikněte na tlačítko „Potvrdit“ pro potvrzení objednávky.

.. obrázek: náklady/potvrzená faktura.png
:align:center
:alt: Takhle vypadá potvrzený prodejní příkaz v aplikaci Odoo Sales.

S potvrzenou objednávkou je čas vytvořit výdaj.

Pro toto vyberte aplikaci „Náklady“ a přejděte na hlavní obrazovku Odoo.
--> Náklady.

Poté klikněte na panelu „Náklady“ na tlačítko „Nový“, aby se vám zobrazilo prázdné formuláře pro náklady.

.. obrázek: výdaj/prázdný-výdajový-formulář.png
:align:center
:alt: Prázdná faktura v aplikaci Odoo Expenses.

Na formuláři výdajů přidejte pole „Popis“ pro snadnou identifikaci výdaje.

Poté vyberte jednu z následujících možností ze seznamu
menu:

- :guilabel:`Komunikace“: jakákoli forma komunikace související s projektem/objednávkou.
- :guilabel:`Jiné“: výdaje, které nejsou zařazeny do žádné jiné kategorie.
- :guilabel:`Jídlo“: jakákoliv forma stravování spojená s projektem nebo objednávkou.
- :guilabel:Dárky“: jakákoliv forma daru spojená s projektem/objednávkou.
- :guilabel:`Náklady na palivo“: jakékoliv náklady spojené s projektem/objednávkou.
- :guilabel:`Doprava a ubytování“: jakékoliv náklady na cestování nebo ubytování související s projektem/objednávkou.

..tip:
Nové položky výdajů lze vytvořit z formuláře výdajů kliknutím na tlačítko :guilabel:`Kategorie`.
poli s výběrem „Zobrazit vše“, vyberte možnost „Nový“ a klikněte na
:guilabel:`Hledání:Kategorie“ okno.

.... obrázek: výdaje/kategorie výdajů - pop-up.png
:synchronizace: střed
:alt:Vyhledávání:Náklady na kategorii - okno s výzvou v prázdném formuláři nákladů v Odoo Expenses.

Pro tento vzorec průchodu, který bude zákazníkovi vyúčtovat krátkodobý pobyt v hotelu,
Pro tento příklad je kategorií :guilabel:`[PŘEKLAD & ÚČETNÍ] Cestování a ubytování“.

.. poznámka::
Následující příklad vyžaduje aplikace *Prodej*, *Účetnictví* a *Výdaje* pro zobrazení/změnu všech
pole uvedená v průběhu workflow.

Pod položkou „Kategorie“ zadejte částku, která bude v příslušném období odepsána.
pole.

Dále označte, zda je v celkové částce započítána nějaká daň. Pokud ano
přednastavená daňová částka je vybrána z pole „Zahrnuté daně“ a Odoo provede automatické výpočty.
daňový základ, který je založen na částce uvedené v poli „Celkem“.

Pak vyberte, který zaměstnanec byl zodpovědný za výdaj a vyberte možnost v
:guilabel:`Zaplaceno“ pole: :guilabel:„Zaměstnanec (na náhradu)“ nebo :guilabel:„Společnost“.

V tomto případě platil náš zaměstnanec za hotel svými penězi, takže:guilabel:Zaměstnanec (to
výběr možnosti „Vyúčtovat“).

Na pravé straně výdajového formuláře je možnost přidat pole „Referenční číslo faktury“
k dispozici. Pod nimi se nacházejí automaticky vyplněné pole :guilabel:`Datum výdaje“ a :guilabel:`Účet“.
jsou k dispozici.

.. poznámka::
Pole „Datum výdaje“ a „Účet“ lze upravit, pokud je třeba.

Dále klikněte na prázdné pole v poli „Zákazník pro opětovné vyúčtování“ a zobrazí se vám seznam.
menu. Z nabídky vyberte příslušný prodejní doklad, na který má být tato položka nákladů připsána.
Povinné pole, které je nutné vyplnit při vystavování faktury k úhradě nákladů zákazníkovi.

Konečně je možné upravit pole „Analytická distribuce“ a „Společnost“.
jsou k dispozici. Tyto pole nejsou nutné pro dokončení vystavené faktury zákazníkovi, ale
jsou k dispozici pro úpravu, pokud je třeba.

Dále je na spodní části výdajového formuláře sekce „Poznámky ...“, kam lze zadat jakékoliv poznámky.
K této položce lze přidat další výdaje, pokud je potřeba.

.. obrázek: výdaj/vyplněný formulář o výdajích.png
:align:center
:alt: Vyplněný formulář o výdajích v aplikaci Odoo Expenses.

Na horní části výdajového formuláře jsou tlačítka pro :guilabel:`Připojit fakturu“ a :guilabel:`Vytvořit
Report, a :guilabel:Splatná faktura.

Pokud má být k výdaji přiložen fyzický nebo digitální doklad, klikněte
:guilabel:`Připojit fakturu“.

Pokud se tato položka musí rozdělit, klikněte na :guilabel:`Split Expense`. Tato funkce může
používána pro několik důvodů (výdaje za žvýkání s jiným zaměstnancem, aby se ubytovali různé daně
sazby atd.

Pokud ani jedna z těchto možností není nutná, klikněte na „Vytvořit report“ a uzamknout výdaje.
report, který právě konfiguroval.

Provedením takového kroku se zobrazí souhrn výdajů pro nový výdaj.

.. obrázek: výdaje/výkaz-zpětného-odpočtu-souhrnně.png
:align:center
:alt: Souhrn výdajů v aplikaci Odoo Expenses.

Zde klikněte na tlačítko „Odeslat do“ po potvrzení podrobností o výdaji.
Manager“. Tato funkce odesílá výkaz o nákladech na schváleného manažera, který výdaje zkontroluje.

Manažer, který bude mít na starosti přezkoumání a schválení výdajů, zkontroluje podrobnosti týkající se
výdajů a pokud nebudou žádné problémy, kliknou na tlačítko „Schváleno“ - což
Pouze se zobrazuje v pohledu manažera na :guilabel:`Shrnutí výdajů`, které bylo podáno.
zaměstnance na vedoucího.

.. obrázek: náklady/zpráva o výdajích - přehled pro schválení manažerem.png
:align:center
:alt:Souhrn výdajů, který schválí manažer pomocí tlačítka „Schválit“.

Jakmile je návrh schválen, tlačítka na horní liště seznamu výdajů se opět změní.
V tomto bodě jsou tlačítka na horní liště v seznamu výdajů:
Záznamy v deníku, „Výpis v příštím výplatním listu“, „Odmítnout“ a „Nastavit na
Návrh.

.. obrázek: výdaje/zpráva o výdajích - přehled manažera postu.png
:align:center
:alt:Souhrn výdajového hlášení s tlačítkem pro vložení záznamů do deníku pohledávek nahoře na formuláři.

Když je manažer spokojený s výsledkem „Souhrnného hlášení o nákladech“, klikne
:guilabel:`Záznamy v deníku“.

Po kliknutí na tlačítko „Přidat záznamy do účetnictví“ zmizí a zobrazí se tlačítko „Analytické
V poli „Distribuce“ v záložce „Náklady“ je vyplněna faktura, která byla
původně nastavené na výdaj v poli „Zákazník k doúčtování“.

.. důležité:
Výchozí nastavení pole „Zákazník k doúčtování“ je zapnuto pro pole „[TRANS &
„Doprava a ubytování“, „Komunikace“, „Stravování“
:guilabel:`[MILEAGE] Náklady na ujeté kilometry`.

Je třeba poznamenat, že **ne všechny** přednastavené kategorie výdajů, které jsou nainstalovány s
Aplikace *Náklady* má aktivní politiku opětovného vyúčtování. Nastavení může být nutné
Je aktivována manuálně.

Chcete-li to provést, přejděte na: „Náklady aplikace -> Konfigurace -> Kategorie nákladů“
zobrazit seznam všech kategorií výdajů v databázi.

Podívejte se do sloupce „Znovuúčtování výdajů“ a zkontrolujte, které volby byly vybrány.
každé kategorii výdajů.

.... obrázek: výdaje/kategorie-výdajů-stránka.png
:synchronizace: střed
:alt:Sloupec „Náklady na opětovné vystavení faktury“ na stránce kategorií výdajů aplikace Odoo Expenses.

Chcete-li upravit položku výdajů, klikněte na ikonu „pravý směr“ (right arrow)
:guilabel:`Kategorie“ pole, abychom zjistili konkrétní výdaj.

V sekci „Fakturace“ v poli „Znovuúčtování výdajů“ vyberte
nebo „Základní cena“ nebo „Prodejní cena“.

.... obrázek: expense/reinvoice-expenses-field.png
:synchronizace: střed


Revize výdajů
=================

Po dokončení těchto kroků je čas vrátit se zpět ke smlouvě o prodeji a dokončit přeúčtování.
náklad pro zákazníka.

Pro toto vyberte v hlavním menu aplikace „Sales“ a poté klikněte na
vhodný prodejní doklad, který má být přeúčtován na výdaje.

V prodejním formuláři je nově nakonfigurovaný výdaj v záložce „Řádky objednávky“ s jeho
V poli „Dodáno“ vyplněné a připravené k fakturaci.

.. obrázek: výdaj/objednávka-na-výdaje-se-řádky-objednávky-na-výdaje.png
:align:center
:alt:Objednávka s připravenou položkou k účtování v záložce Objednávky.

Po potvrzení podrobností o výdaji klikněte nahoře na tlačítko „Vytvořit fakturu“.
objednávka na prodej. Po kliknutí se zobrazí okno s názvem „Vytvořit faktury“.

.. obrázek: výdaje/vytváření faktur pop-up.png
:align:center
:alt:Pop-up okno pro vytváření faktur, které se objeví po kliknutí na tlačítko Vytvořit fakturu.

Z této okamžité zprávy odeberte pole „Vytvořit fakturu“ a nechte jej na výchozí hodnotě.
Vyberte možnost „Běžná faktura“ a klikněte na tlačítko „Vytvořit návrh faktury“.

Tímto způsobem se zobrazí položka „Návrh faktury zákazníka“ s pouze náklady na
:guilabel:„Řádky faktury“

.. obrázek: výdaj/faktura-pro-zákazníka-s-výdajem.png
:align:center
:alt:Návrh faktury pro zákazníka s výdajem v záložce Faktura v poli Výpisy.

Pokud jsou všechny informace o výdaji správné, klikněte na tlačítko „Potvrdit“
faktura. Tím se stav faktury přesune z :guilabel:`Návrh“ na :guilabel:`Odesláno“.

Chcete-li fakturu odeslat zákazníkovi, klikněte na tlačítko „Odeslat & Tisk“. To způsobí zobrazení
Pop-up okno „Odeslat“, které obsahuje přednastavený text a fakturu ve formátu PDF v těle
zprávu. Zpráva může být přezkoumána a upravena, pokud je třeba.

Jakmile je vše připraveno, klikněte na tlačítko „Odeslat a tisknout“, abyste fakturu odeslali zákazníkovi.
Pop-up okno zmizí a Odoo pošle zprávu/fakturu zákazníkovi. Kromě toho je vytvořen PDF soubor
Faktura se automaticky stáhne pro účely archivace a/nebo tisku.

Zpět na faktuře klienta, klepnutím na tlačítko „Registrovat platbu“
Zákazník platí za fakturovanou položku.

.. obrázek: výdaje/faktura-zákazníka-registrace-platby.png
:align:center
:alt:Faktura pro zákazníka s tlačítkem registrace platební brány připraveným kliknutí.

Když je kliknut na tlačítko „Registrace platby“, objeví se okno „Registrace platby“.
V tomto okně se automaticky vyplní potřebné pole s korektními informacemi. Po
při prohlížení informací klikněte na tlačítko „Vytvořit platbu“.

.. obrázek: výdaje/registrace-platby-připomínka.png
:align:center
:alt:Okno s registrační platbou na faktuře zákazníka v Odoo Sales.

Jakmile je kliknut na tlačítko „Vytvořit platbu“, okno zmizí a zobrazí se zelené „V
V horním pravém rohu faktury je uveden nápis „Uhrazeno“, což značí, že tato faktura byla zaplacena.
plná. Tím se dokončí práce s dokumentem.

.. obrázek: výdaj/faktura-výdaje-v-platební-baneru.png
:align:center
:alt:Okno s registrační platbou na faktuře zákazníka v Odoo Sales.

.. viz též:
   - :doc:`fakturační politika“
   - :doc:`time_materials“
   - :doc:`milník“
