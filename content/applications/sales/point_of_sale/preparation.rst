===================
Přípravná ukázka
===================

Přípravu zobrazuje funkce přípravy a umožňuje vám pracovat s objednávkami na pokladně vyžadujícími přípravu.

- **Pro maloobchodní prodej**: Po dokončení platby na místě se oznamuje přípravné týmu.
zboží zakoupené zákazníkem k vyzvednutí.
- **Pro restaurace**: POS objednávky informují kuchyni o jídle, které se má připravit.

Konfigurace
=============

Aby bylo možné zobrazit přípravu na obrazovce

#Přejděte do nastavení POS:ref:`<configuration/settings>`.
#Přejděte dolů do části „Příprava“.
#Zkontrolujte možnost „Příprava zobrazit“.

.. obrázek: příprava/příprava-nastavení.png
:alt:Přepínač pro zapnutí zobrazení přípravy
:skalka: 90 %

Vytvořit a zprovoznit přípravu na výstavku.

#Přejděte na: „Prodejní místo“ → „Objednávky“ → „Zobrazení přípravy“.
#Klikněte na tlačítko „Nový“.
#Přidejte popisný štítek :guilabel:`Jméno` (například „Hlavní kuchyně“, „Bar“)
#Nastavte si ho:

   #.:guilabel:`Prodejní místo“: Vyberte prodejní místo, které posílá objednávky na tento displej.
   #Specifikujte POS, které je odesíláno do této kategorie produktů.
zobrazení.
   #:guilabel:`Kroky“: Definujte kroky, které jsou potřeba pro zpracování objednávek.

      - Klikněte na tlačítko „Přidat řádek“ pro přidání fáze.
      - Přiřaďte každé fázi konkrétní barvu pro lepší přehlednost (volitelně).
      - Definujte pro každou fázi časový limit „Poplachu“ (min) k označení očekávaného zpracování.
času.

.. obrázek: příprava/zobrazovací forma.png
:alt: příprava zobrazovacího zařízení
:skalka: 85 %

.. poznámka::
Chcete-li upravit stávající přípravu, klikněte na tlačítko vertikální elipsy
Vyberte kartu displeje a zvolte možnost „Nastavení“.

Praktické využití
=====================

Přejděte na: menu-selection: „Prodejní místo –> Objednávky –> Zobrazení přípravy“ a zobrazí se vám přehled všech
Vaše obrazovky.

.. obrázek: příprava/vystavení karty.png
:alt:Kanbanový pohled na přípravu
:skalka: 85 %

Na displeji se zobrazuje:

- Nastavené fáze.
- Počet objednávek v současné době:guilabel:Ve výrobě.
- Průměrný čas, který zaměstnanci obvykle potřebují k dokončení objednávky.

..tip:
Vyberte ikonu aplikace „Kitchen Display“ v Odoo Dashboardu pro rychlejší přístup.

Použitím přípravku na obrazovce
-----------------------------

Pro zobrazení přípravy klikněte na:guilabel:'Přípravná obrazovka'. Toto rozhraní je navrženo tak, aby
pro zaměstnance ukazuje:

- **Pořadí a počet úkolů**: Zobrazuje postupy objednávek napříč fázemi, jako je například „Připravit“.
„Připraveno“, „Dokončeno“ a počet objednávek v každé fázi.
- Seřazené produkty podle kategorie: Seznam všech položek v průběhu zpracování, seřazených podle kategorií prodejních míst (například
„Nápoje“, „Jídlo“.
- **Karty objednávek**: Shrnují jednotlivé objednávky včetně:

  - Přidružené tabulky a čísla objednávek.
  - Stav, například „Připraveno“, zvýrazněný definovanými barvami.
  - Čekací doba s vizuálními indikátory.

.. poznámka::
Pokud uplynulý čas překročí předdefinovanou hodnotu, indikátor trvání se změní na červenou barvu.

.. obrázek: příprava/zobrazení přípravy.png
:alt: zobrazí rozhraní přípravy s pokyny k zpracování objednávek.
:skalka: 80 %

Abychom aktualizovali stav objednávky:

- Klepněte na položky v objednávce, abyste je mohli vymazat jednotlivě.
- Klikněte na samotný objednávkový lístek, abyste označili všechny položky najednou.
- Karta se automaticky přesune na další krok, jakmile bude každá položka vyplněna.
- Klikněte na ikonu „fa-undo“ a zadejte „Recall“, pokud chcete přesunout objednávku zpět do předchozího kroku.
přesunula ho do další fáze.

Zobrazovací plocha pro zákazníka
----------------

Ve stejnou dobu klikněte na tlačítko „Obrazovka stavu objednávky“ a otevřete uživatelské rozhraní. To umožňuje
jejím cílem je poskytnout zákazníkům přehled o objednávkách, které jsou:

- :guilabel:`Připraveno k vyzvednutí.“
- :guilabel:'Jen o kousek', což znamená, že jsou v pořádku.

.. poznámka::
Číslo objednávky je uvedeno na vrchu účtenky zákazníka.
