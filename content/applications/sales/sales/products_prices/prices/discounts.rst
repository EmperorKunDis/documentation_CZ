=========
Slevy
=========

Funkce „Slevy“ umožňuje uživatelům snížit nebo zvýšit cenu na řádcích položek v prodejním dokladu.
citace nebo objednávka. Tento je vypočítán jako procento z ceny prodaného produktu.

Chcete-li získat slevy v aplikaci **Sales**, přejděte na: „Aplikace Sales --> Konfigurace
V části „Nastavení“ vyberte položku „Ceny“. Vyberte zaškrtávací políčko „Slevy“, pak
Klikněte na tlačítko „Uložit“.

Po aktivaci nastavení přejděte na požadovanou citaci kliknutím na
V horní části stránky vyberte možnost „Prodejní aplikace“ -> „Objednávky“ -> „Dodací listy“.
požadovaný citát z nabídky.

Slevy na produktové řady
==========================

V záložce „Dodací řádky“ v objednávkovém formuláři se objeví nový nadpis sloupce s názvem
:guilabel:`Sleva.%“. Tato slouží k nastavení slev na jednotlivé položky. Zadejte požadovaný
slevu na každou produktovou řadu a nová cena se automaticky vypočítává v
V dolní části stránky pod položkou „Celkem“.

..tip:
Slevu lze přidat také přímo do objednávky prodeje stejně jako slevový kód. Přejděte na
:menuvolba:`Prodejní aplikace --> Objednávky --> Objednávky“, klikněte na požadovanou objednávku a přidejte
slevu do pole „Sleva“ dle popisu výše.

.. obrázek: slevy/sleva-na-objednávce-prodeje.png
:alt:Hlavička Dis.% se nyní objeví v řádcích objednávek.

.. poznámka::
Pozitivní hodnoty v poli „Disc. %“ aplikují slevu, zatímco záporné hodnoty mohou být použity k
používá k navýšení ceny.

.. důležité:
Pozitivní hodnoty, tedy pokles cen, budou vidět zákazníkovi, zatímco negativní hodnoty, nebo
Zvýšení cen nebude viditelné pro zákazníky. Namísto slevové kolonky bude naopak přidána sloupec „cena“.
Negativní slevy změní cenu jednotlivého produktu.

..prodeje/slevy/tlačítko slevy:

Tlačítko slevy
===============

Pokud jsou zapnuté nastavení Slevy, v dolní části prodejního formuláře se zobrazí tlačítko Sleva.
objednávek.

.. obrázek: slevy/tlačítko-slevy-objednávky.png
:alt:Tlačítko slevy, které se nachází na konci objednávkového formuláře v aplikaci Odoo Sales.

Kliknutím na tlačítko Sleva v objednávce se zobrazí okno s
Slevový procentuální údaj a možnosti konfigurace:

- Přidat zadaný slevový procentní podíl (konfigurovaný v
:guilabel:`Sleva“ pole v okně s výběrem.
- :guilabel:`Sleva globální“: Přidejte do objednávky produktovou řadu s kumulativní
hodnota odpovídající zadanému slevovému procentu.

...... příklad::
Na konec objednávky s celkovou částkou 4 200 USD se připočítává globální sleva 10 %.
přidáním slevové řádky s hodnotou -$420 (což je 10 % z částky 4 200 USD).

...... obrázek: slevy/globální-možnost-slevy.png
:alt:Prodejní objednávka s aplikovanou globální slevou v aplikaci Odoo Sales.

... důležité::
Jakákoliv položka přidána (nebo odstraněná) po zadání globální slevy se **nepromítne do celkové ceny**.
hodnota slevy na slevové lince. Nové produkty nebo změny stávajících produktů
zadat globální slevu, vymazat současnou globální slevu a opakovat kroky.

- :guilabel:`Fixní částka“: Přidejte finanční částku do pole „Sleva“. Jakmile se aplikuje,
tato částka se přidává do objednávky jako produktová řada s odčerpáním peněžní hodnoty.
celková částka objednávky.

...... příklad::
Zaškrtnutá sleva 20 USD se zobrazuje jako produktová řada s negativním „Cena za jednotku“.

.. obrázek:: slevy/fixni-sleva-na-objednavku.png
:alt:Objednávka s aplikovanou fixní slevou v aplikaci Odoo Sales.

.. poznámka::
Je výhodnější přidat slevu za „Pevnou částku“ po všech produktech, které chcete.
Do prodejního příkazu byly přidány položky. Po tom, co byly provedeny změny v prodejním příkazu
pokud se sleva přičte, upravte hodnotu na řádku :guilabel:`Sleva`, nebo odstraňte řádek a přidejte
slevu znovu, pokud je potřeba.
