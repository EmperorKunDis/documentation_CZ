==============
Kvalitativní upozornění
==============

...kvalita/kvalitní řízení/upozornění na kvalitu:
.. |MO| nahradit za: zkratka: `MO (Manufacturing Order)`

V aplikaci Odoo *Quality* se používají upozornění na kvalitu (tzv. „quality alerts“) pro informování týmů kvality o vadách výrobku nebo
jiných problémů. Kvalitativní upozornění lze vytvořit z výrobního nebo skladovacího příkazu, ze
v modulu Obchodní plocha nebo přímo v aplikaci Kvalita.

Vytvářejte kvalitní upozornění
=====================

Existuje několik způsobů, jak vytvořit novou výstrahu kvality:

- **Z aplikace Quality samotné**, přes: menu: „Kvalita“ --> „Kontrola kvality“ --> „Kvalita“
„Poplachy“ a pak klikněte na „Nový“ pro otevření formuláře poplachu.
- Přejděte na:menu:„Výroba“ -> „Provoz“ -> „Dodací objednávky“.
Vyberte si |MO|. Klikněte na tlačítko „Alertování kvality“ v horní části |MO|, abyste otevřeli
upozornění na kvalitu v nové stránce.

... důležité::
Tento způsob lze použít jen v případě, že byla požadována kvalitativní kontrola pro |MO|.
Jinak se tlačítko „Varování kvality“ nezobrazí.

- Otevřete aplikaci „Inventář“, klikněte na tlačítko „# K zpracování“ v inventáři.
Vyberte typ faktury (Příjmy, dodací listy atd.) a poté vyberte objednávku. Klikněte na
:tlačítko „Zpráva o kvalitě“ v horní části objednávky, aby se zobrazila nová stránka s upozorněním na kvalitu.
stránka.

... důležité::
Tento způsob lze použít jen v případě, že byla požadována kontrola kvality pro objednávku zásoby.
:guilabel:`Varování kvality“ tlačítko se jinak nezobrazí. Pokud tlačítko nebude zobrazeno,
Kvalitní upozornění lze vytvořit také kliknutím na ikonu „⚙️ (převodovka)“ v horní části stránky.
stránku a zvolit možnost „Varování kvality“ ze seznamu nabídek.

- Otevřete modul „Podlaha“ a poté vyberte pracovní centrum z navigačního panelu.
v horní části stránky a poté klikněte na tlačítko „⋮“ (tři vertikální tečky) v
V pravém dolním rohu pracovního příkazu klikněte na tlačítko „Co chcete udělat?“ v nabídce. Vyberte
:guilabel:`Vytvořit upozornění na kvalitu“ z této nabídky otevře upozornění na kvalitu v okně
okno.

.. poznámka::
Podle způsobu otevření nového upozornění na kvalitu se mohou v něm již zobrazit určité pole.
vyplněny. Například pokud je vytvořen kvalitativní upozornění z karty pracovního příkazu ve složce *Podlaha obchodu*,
modulu, do pole „Produkt“ a „Středisko práce“ se vloží přednastavené hodnoty.

Formulář kvalitativní výstrahy
-------------------

Po otevření nové kvalitativní výstrahy začněte tím, že jí dáte krátké :guilabel:`Název`, který shrnuje
s produktem.

Pakliže se jedná o kvalitativní upozornění:

- **Konkrétní produkt nebo jeho varianta**, vyberte ji z položky :guilabel:`Produkt`.
:guilabel:`Varianta produktu“ vybrané z roletky.
- Vyberte konkrétní pracovní centrum z rozevírací nabídky „Pracovní centrum“.
- Vyberte konkrétní pořadí vyzvedávání z rozevírací nabídky „Vyzvednutí“.

V dalším poli „Tým“ vyberte kvalitní tým, který má na starosti řízení
upozornění na kvalitu. Pokud by měl být za upozornění na kvalitu zodpovědný konkrétní zaměstnanec, vyberte ho ze seznamu
Vyberte možnost „Zodpovědná osoba“.

V poli „Štítky“ vyberte libovolné štítky, které se vztahují k upozornění na kvalitu.
menu.

Pokud je známá příčina kvalitativního problému, použijte pole :guilabel:`Příčina problému`.

Začněte výběrem úrovně „Důležitost“ pomocí výběru čísla „⭐ (hvězdička)“.
a tři. Kvalitní upozornění s vyšší prioritou se zobrazují na začátku seznamu :guilabel:`Kvalitní upozornění`.
Kanban board v aplikaci Quality.

Na spodní části formuláře kvalitativního upozornění jsou čtyři záložky, které usnadňují přidání dalších informací.
nebo kroky, které mají být vykonány pro upozornění na kvalitu. Mohou vypadat takto:

- V záložce „Popis“ zadejte popis problému s kvalitou.
- Pro podrobnější popis kroků, které mají být přijaty pro odstranění problému, použijte záložku „Korektivní opatření“.
problémem.
- Použijte záložku Preventive Actions k popisu, co by mělo být provedeno, aby se problém vyřešil.
se bude v budoucnu vyskytovat.
- V záložce „Různé“ vyberte dodavatele produktu. Pokud používáte
Odoo databáze pro správu více firem, vyberte vhodný subjekt.
:guilabel:`Společnost“ pole. Nakonec zadejte datum, kdy byla upozornění přidělena kvalitě v
:guilabel:`Datum přiřazení“ pole.

.. obrázek: kvalita_varování/upozorneni.png
:align:center
:alt:Vyplněný formulář kvalitního upozornění.

Správa kvalitních upozornění
=====================

Pro zobrazení všech kvalitativních upozornění přejděte na: „Kvalita“ – „Kontrola kvality“.
Kvalitní upozornění“. Výchozí zobrazení upozornění je v kartovém pohledu, který je uspořádá do
různé fáze podle toho, kde se v procesu recenze nacházejí.

Přesunout upozornění na jinou fázi je velmi jednoduché - stačí jej pouze přetáhnout na požadovanou fázi.
Vyberte si kvalitní upozornění, abyste ho otevřeli, a pak klikněte na požadovanou fázi nad pravým horním rohem
Formulář kvalitního upozornění.

Pro vytvoření nové výstrahy ve specifické fázi klikněte na tlačítko „+“ (plus) vedle
Umělecké jméno. V novém upozornění pod názvem scény zadejte
Název upozornění a poté klikněte na „Přidat“. Chcete-li nakonfigurovat zbytek upozornění
Vyberte kartu upozornění, abyste otevřeli její formulář.

.. obrázek: kvalita_varování/upozorneni-kanban.png
:align:center
:alt:Stránka s kartami pro zobrazení upozornění v kanbanovém pohledu.
