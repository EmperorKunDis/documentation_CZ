==========================
Hlavní výrobní plán
==========================

.. |SO| nahradit za: :abbr:`SO (objednávka na prodej)`
.. |PO| nahradit za: abbr: PO (objednávka na nákup)
.. |MO| nahradit za: zkratka: `MO (manufacturing order)`
.. |SOs| nahradí za: :abbr:`SOs (prodejní objednávky)`
.. |POs| nahradit za: zkratka: `POs (objednávky k nákupu)`
.. |MOs| nahradí za: :abbr:`MOs (manufacturing orders)`
.. |MPS| nahradit za: zkratka `MPS (Master Production Schedules)`
.. |BoM| nahradit za: :abbr:`BoM (Seznam materiálů pro výrobu)“
.. |RfQ| nahradit za: zkratku `RfQ (požadavek na nabídku)`
.. |RfQs| nahradit za: :abbr:`RfQs (žádosti o nabídku)“

V aplikaci Manufacturing od společnosti Odoo se používá „master production schedule“ (MPS), který umožňuje plánování ručně.
objednávky výroby (MO) a nákupní objednávky (PO) na základě předpokládaného množství produktů
součástky.

Při zohlednění dopadu potvrzených |MOs| a |POs| spolu s ručně upravovanou poptávkou
Prognózy lze využít k řízení dlouhodobého doplňování zásob. To zajišťuje
Dostupnost potřebných produktů a komponent.

Protože MPS umožňuje manuální zásahy, je užitečný pro doplňování produktů, kde
požadavky na stávající objednávky neodráží pravděpodobnou budoucí poptávku.

Příklad:
Obchod prodává umělé vánoční stromky během svátků. Nyní
September a obchod má méně než deset vánočních stromků potvrzených na měsíc
Prosinec.

Přestože se potvrdilo mnoho MOs, nákupní manažer ví, že poptávka po
Vánoční stromky v prosinci budou podstatně dražší, jakmile začne sezona Vánoc.
Výsledkem je, že ručně zadávají vyšší poptávku v MPS, aby mohli správně doplnit zásoby.
produkt včas na zvýšenou poptávku zákazníků.

.. důležité:
Je nutné si uvědomit, že |MPS| je manuální nástroj. Přidání produktu do |MPS|
to neznamená, že by se zboží automaticky vyrábělo nebo kupovalo. MPS jen navrhuje
množství produktu, které je třeba doplnit, ale vyžaduje zadání uživatelem k vytvoření |MOs| nebo
|POs|, které se používají k doplnění zásob.

Proto se doporučuje nepoužívat |MPS| spolu s pravidly pro přeskupování.
stejný produkt. Protože pravidla znovuobjednávání jsou automatizovaným pracovním postupem, konfliktují s
metoda manuálního doplňování zásob |MPS|. Používání obojího současně může vést k nepřesným předpovědím a
vytváření zbytečných doplňkových objednávek.

Povolit a nakonfigurovat |MPS|
==========================

Pro použití této funkce přejděte na: Menu selection: Manufacturing app --> Configuration -->
Nastavení“, zaškrtněte políčko „Hlavní výrobní plán“ v části „Plánování“.
sekci a nakonec klikněte na tlačítko „Uložit“.

Po zapnutí funkce „Master Production Schedule“ se objeví dvě nová pole pod ním.
stránka „Nastavení“: „Časové rozpětí“ a „Počet sloupců“.

Pole „Časový rozsah“ se používá k výběru časového období, v němž probíhá plánování.
místo a nabízí tři možnosti: „Měsíční“, „Týdenní“ a „Denní“.
Příklad: Pokud je vybrána položka „Měsíčně“, plánuje MPS poptávku produktů.
a součástky měsíčně.

Pole „Počet sloupců“ se používá k určení počtu vybraných
Jednotky zobrazené na stránce |MPS| v záložce „Časové rozpětí“. Například pokud je zobrazena jednotka
pole je nastaveno na „Měsíčně“ a do pole „Počet sloupců“ se zadává číslo 12.
MPS zobrazuje jeden sloupec pro následujících 12 měsíců, začínající aktuálním měsícem.

Pokud jsou změněny hodnoty políčka „Časový rozsah“ nebo „Počet sloupců“,
Klikněte na tlačítko „Uložit“ a uložte změny.

.. obrázek: use_mps/mps-settings.png
:align:center
:alt:Nastavení MPS v aplikaci Nastavení výroby.

Dashboard MPS
===============

Pro otevření |MPS| přejděte na: menu: `Výrobní aplikace -> Plánování -> Master Production
Schéma. Z pohledu MPS tak vypadá:

.. obrázek:: use_mps/mps.png
:align:center
:alt: Plán výroby v aplikaci Výroba.

Šedá sloupec v levém rohu obrazovky ukazuje sekci pro každý produkt přidávaný do |MPS|.
s každou produktovou sekcí rozčleněnou na menší řádky. V řádcích je zobrazena
závisí na filtrech vybraných v rozevíracím seznamu nad tlačítkem „Hledat…“
stránka. Výchozí kategorie, které se zobrazují v řádcích, jsou:

- :guilabel:`[Produkt] od [jednotky]“: ikonou „fa-area-chart“: předpokládaný počet skladovaných položek
začátku každého časového období. Výrobky a grafy lze vybrat
tlačítka, která otevírají stránku produktu nebo předpověď pro daný produkt, příslušně.
- „Předpokládaná poptávka“: předpověď poptávky, kterou zadáváte ručně. Tato představuje
předpověď poptávky po produktu v každém časovém období.
- „Předpověď poptávky“: tato kategorie je výchozí, ale **jenom** se zobrazuje pro
produkty, které jsou součástí jiných produktů. Zastupuje poptávku po komponentu od
stávajících MO.
- :guilabel:`+ Doporučené doplnění` - množství produktu, které je doporučeno
doplněné z |MOs| nebo |POs|. Vpravo od názvu kategorie je
:tlačítko „Doplnit“, které se používá k ručnímu doplnění produktu podle skutečnosti.
doporučená k doplnění.

.... obrázek: použít_mps/doplnit_tlačítko.png
:synchronizace: střed
:alt:Tlačítko doplnění na řádku „Doporučené doplnění“.

Tlačítko „Doplnit“ v řádku „+ Doporučené doplnění“.

- :guilabel:`= Předpokládané množství na skladě“: předpokládaný počet produktů, který bude k dispozici na konci
z každého časového období, předpokládá-li se naplnění navrhovaných počtů doplňování.

Všechny tyto výchozí kategorie tvoří rovnici:

.. matematika::
\text{Předpokládaná poptávka} + \text{Navrhované doplnění zásob} = \text{Předpokládaný sklad

V případě součástek se bere v úvahu také predikce poptávky na základě :guilabel:`Indirect Demand Forecast`.

Políčka „Předpokládaná poptávka“ a „Navrhované doplnění“ lze upravit.
pro kteroukoliv z časových období vpravo od sloupce produktu. To změní rovnici a
aktualizuje hodnotu zobrazenou v poli „Očekávaný stav“.

Změna hodnoty v poli „Doporučené doplnění“ také přidává ikonu „fa-times“.
:guilabel:`(reset)` tlačítko se objeví vlevo od pole. Klikněte na ikonu
:guilabel:`(reset)` tlačítko vedle pole, které vrátí jeho hodnotu na tu vypočtenou
MPS.

.. důležité:
Pokud je použito jen s povolenými výchozími kategoriemi, pak je vhodné také
aktivovat kategorii „Skutečná poptávka“. To se provede kliknutím na ikonu
:guilabel:`(svislá šipka)“ vpravo od tlačítka „Hledat…“, a zapnutí
:guilabel:`Skutečná poptávka“ pod hlavičkou „Sloupce“.

Při zapnuté možnosti „Skutečná poptávka“ se v kategorii „Forecasted Demand“ zobrazí
změny v kategorii „Skutečná/předpokládaná poptávka“. Kromě ručního nastavení je možné používat také
vložil předpokládanou poptávku, kategorie také zobrazuje potvrzenou poptávku po produktu.
Na základě potvrzených případů.

Každá sloupec vpravo od sloupce produktů obsahuje jednotku časového období vybraného
Pole „Časový rozsah“ na stránce nastavení aplikace „Výroba“ (např. měsíců). Číslo časového rozsahu
Časové sloupce odpovídají hodnotě zadané do pole Číslo sloupců.

První sloupec s časovým úsekem představuje aktuální časový úsek. Například pokud je hodnota
Pokud je konfigurováno na měsíce, první sloupec zobrazuje aktuální měsíc.
sloupci, v poli „Doporučené doplnění“ se zobrazuje jedna ze 5 barev:

- „Zelená“: musí být vytvořena objednávka na doplnění zásob, aby bylo zajištěno množství „Bezpečné“.
Stock Target.
- :label:Šedá: již byla vytvořena objednávka na doplnění zásob, aby bylo zboží
:guilabel:`Zásoba pro bezpečnost“.
- :guilabel:Žlutá: již byla vytvořena objednávka doplňování zásob, ale její množství
Vytvořený pro není dostatečný k udržení zásob na úrovni cílového skladu.
- :guilabel:`Červená“: objednávka na doplnění již byla vytvořena, ale její množství
pro převyšuje cílovou hodnotu zásob.

V poli „Doporučená doplňková objednávka“ se zobrazí bílá barva, pokud nebyla vystavena žádná objednávka na doplnění.
generován a není potřeba jej v současné době generovat.

Přidat produkt
=============

Pro správu doplňování produktů použijte |MPS|, přejděte na:
Plánování --> Výrobní plán. Na stránce výrobního plánu klikněte na tlačítko „Přidat“
Klikněte na tlačítko „Přidat produkt“ v okně s názvem „Přidat produkt“.

.. důležité:
Produkty **musí být správně nakonfigurovány, aby se mohly doplňovat prostřednictvím MPS**.

V případě výrobků je třeba vybrat v seznamu tras *Výroba*.
sekci záložky Inventář na kartě produktu.

V případě produktů zakoupených musí být v seznamu tras vybrána možnost „Koupit“.
sekci záložky „Inventář“ na kartě produktu. Dále je zde uveden dodavatel a cena, za kterou byl
Prodej produktu musí být také uveden na záložce Purchase.

V okně s upozorněním vyberte produkt, který chcete přidat do seznamu v poli „Produkt“ v rozevíracím seznamu. Pokud
Zboží se doplňuje výrobou, vyberte zboží v poli BoM v záložce:
Pole materiálů.

.. poznámka::
Vybráním BoM při přidávání produktu do |MPS| se také přidají všechny součástky uvedené na BoM. Pokud
Není nutné řídit doplňování komponent přes MPS, stačí nechat
:guilabel:`Seznam materiálů“ pole ponechte prázdné.

Pokud je databáze nakonfigurována s více sklady, pole „Výrobní sklad“
je zobrazena v okně „Přidat produkt“. Pomocí této položky můžete určit, ve kterém skladu se má produkt nacházet.
produkt se doplňuje.

Do pole „Minimální množství produktu“ zadejte minimální počet produktů.
musí být vždy k dispozici pro objednávky. Například by mělo být vždy 20 jednotek
produkt dostupný k plnění objednávek, zadejte do pole „Cílový zásoba“ číslo 20.
pole.

Do pole „Minimální množství pro doplnění“ zadejte minimální počet produktů pro objednávky vytvořené
dodatku k produktu. Například pokud je do pole zadáno číslo 5, bude vytvořena objednávka na
produkt musí obsahovat minimálně pět jednotek.

Do pole „Maximální množství pro doplnění“ zadejte maximální počet produktů pro objednávky vytvořené
dodatku k produktu. Například pokud je do pole zadáno číslo 100, objednávky na doplnění zásob
Produkt může obsahovat maximálně 100 jednotek.

Začněte kliknutím na tlačítko „Uložit“ a přidejte produkt do |MPS|. Produkt se nyní zobrazuje v
Stránku MPS každýkrát, když je otevřena. Pokud byl vybrán BoM v poli „Seznam materiálu“
poli „Přidat produkt“ v okně s náhledem, všechny komponenty uvedené na seznamu BoM jsou
Ale i stránka je v pořádku.

.. obrázek: use_mps/add-a-product.png
:align:center
:alt:Okno Přidat produkt v MPS.

Upravit produkt
--------------

Po přidání produktu do |MPS| může být nutné změnit hodnoty zásob, které byly zadány.
v okně „Přidat produkt“. Klikněte na tlačítko „# ≤…≤ #“
tlačítko „Doplnit“ na levé straně tlačítka „+ Suggested“, které je umístěno vpravo.
V řádku „Dodání“.

.. poznámka::
První a druhý zobrazený číselný údaj na tlačítku „# ≤…≤ #“ odpovídá hodnotám
zadané do políčka „Minimální množství pro doplnění“ a „Maximální množství pro doplnění“.
přidáním výrobku do |MPS|.

Příkladem je například případ, kdy do pole „Minimum to Replenish“ bylo zadáno číslo 5 a do pole „Maximum to Replenish“ bylo zadáno číslo 100.
V poli „Maximální částku k doplnění“ zadáte hodnotu, která se objeví jako „5 ≤ … ≤“.
   100`.

Kliknutím na tlačítko „# ≤…≤ #“ se otevře okno „Upravit plán výroby“.
Okno. Toto okno je stejné jako okno „Přidat produkt“ s tím rozdílem, že
Políčka „Produkt“ a „Seznam součástek“ nelze upravit.

Do okna „Upravit rozvrh výroby“ zadejte požadovaná data v
:guilabel:`Zásoba pro bezpečnost“, „Minimální množství k doplnění“ a „Maximální množství“.
Znovu naplňte pole. Pak klikněte na tlačítko „Uložit“ pro uložení změn.

Odebrat produkt
----------------

Chcete-li produkt odebrat z |MPS|, zaškrtněte políčko vedle jeho názvu. Pak klikněte na
Tlačítko „Akce“ v horní části obrazovky a vyberte možnost „Smazat“.
z výsledného rozbalovacího seznamu. Nakonec klikněte na tlačítko „OK“ v poli „Potvrzení“.
Pop-up okno.

Pokud chcete produkt z |MPS| odstranit, musíte ho smazat spolu se všemi jeho daty. Pokud je
pokud je znovu přidána, musí být její hodnoty doplněny.

Doplnění MPS
===================

Výrobky v MPS lze doplnit jedním ze tří způsobů:

- Klikněte na tlačítko „Dodat“ v horní části obrazovky, abyste vygenerovali objednávku na doplnění zásob.
za každý produkt pod svým :guilabel:`Safety Stock Targetem` pro aktuální měsíc.
- Klikněte na tlačítko „Doplnit“ v pravé části obrazovky „+ Doporučené“.
Řádek „Dodání“ konkrétního produktu, který vygeneruje objednávku na doplnění tohoto konkrétního
produktu.
- Zaškrtněte políčko vedle názvu produktu jednoho nebo více produktů. Pak klikněte na
:ikonka: „Nástroje“ v horní části obrazovky a vyberte
:guilabel:`Dodat‘ z rozevírací nabídky. Takto vytvoříte objednávku na doplnění zásob
za každý vybraný produkt.

Typ objednávky na doplnění zásob odpovídá zvolené trase v záložce *Sklad*.
tvaru výrobku:

- Pokud je vybrána cesta „Koupit“, vytvoří se |RfQ| pro doplnění produktu. |RfQs| mohou být
vybrané prostřednictvím navigace do aplikace „Nákup“ a jakékoliv |RfQ| vygenerované pomocí |MPS|
seznamy:guilabel:'MPS' v poli 'Zdrojový dokument'.
- Pokud je zvolena trasa Manufacture, vytvoří se |MO| k doplnění produktu. |MOs| mohou
bude vybrán tak, že se dostanete na:menu:Manufacturing App --> Operations --> Manufacturing
Příkazy. Všechny příkazy vytvořené pomocí |MPS| jsou uvedeny v seznamu zdrojových dokumentů pod názvem „MPS“.
pole.
