====================
Zpráva o kvalitě vedení
====================

„Kvalitní kontakt“ je kontakt, který pravděpodobně povede k prodeji. Měl by odpovídat charakteristikám
nejčastěji uváděné jako pomoc prodejcům uzavřít obchod, kromě přesnějších kritérií.
je specifická pro každou organizaci.

.. poznámka::
Specifické kritéria, která definují kvalitní kontakt, jsou pro každou organizaci jiná.
informace, viz:ref:`Definice kvalitního kontaktu <track_links/define-a-lead>“.

Kvalitní report porovnává, kolik kvalitních leadů každý obchodník získal za
Konkrétní časový úsek, například za posledních 30 dnů. Prodejní manažeři mohou použít takovýto report k
udělat informovaná rozhodnutí při přidělování nových kontaktů do týmu

Příklad:
Obchodní manažer vygeneruje zprávu o kvalitních kontaktech pomocí kritérií své společnosti:

   - Kontaktní údaje musí obsahovat telefonní číslo a e-mailovou adresu.
   - E-mailová adresa musí být z profesionální domény.
   - Zdroj pro vedení musí být z živého chatu nebo schůzky.
prodejce

Po spuštění zprávy může manažer vidět, že všichni zaměstnanci mají schopnost uzavřít obchod
Kvalita nabídek se liší, někteří členové prodejního týmu dostali vyšší počet kvalitních nabídek než
jiní.

...... obrázek:: kvalita_vede_report/priklad-reportu.png
:synchronizace: střed
:alt: Příklad kvalitní zprávy o stavu vztahu v aplikaci Odoo CRM.

Využíváním těchto informací může manažer prodeje rozhodnout o přidělení kvalitnějších leadů na prodej.
aby se vyrovnala distribuce kvalitních kontaktů mezi lidmi na spodním konci.

... _track_links/create-quality-leads-report:

Vytvořte kvalitní zprávu o leadrech
=============================

Pro vytvoření kvalitního reportu o leadrech nejprve přejděte na: „Aplikace CRM –> Zprávy –>
Klikněte na tlačítko „Pipeline“ a otevřete panel „Analýza trubek“. Klikněte do pole „Hledat…“
Najděte bar na horní části stránky a odstraňte všechny aktivní filtry.

Klikněte na ikonu v podobě trojúhelníku směřujícího dolů vedle ikony „Hledat…“
otevřít rozbalovací nabídku megamenu, která obsahuje: „Filtry“, „Skupiny“ a
Klikněte na „Přidat vlastní filtr“. To otevře „Přidat vlastní filtr“.
Okno pro přidání vlastního filtru.

Okno „Přidat vlastní filtr“ (pop-up) umožňuje vytvářet více specifické filtry.

Přidejte vlastní filtry
------------------

Pro vytvoření kvalitního reportu o leady je potřeba nastavit filtry pro následující
podmínky:

- Datum zahájení:<quality_leads_report/starting-date>: omezuje výsledky na ty, které byly vytvořeny
konkrétní časový rámec.
- :ref:`Konkrétní prodejní týmy <quality_leads_report/sales-team>“: omezuje výsledky na pouze ty, které obsahují
vede pro jednu nebo více prodejních týmů. Tento filtr je nepovinný a neměl by být zahrnut, pokud
určená pro celou společnost.
- :ref:`Vyloučit nezařazené kontakty <kvalita_leadů/unassigned-leads>“: vylučuje kontakty bez
přidělený prodejce.
- :ref:`Zahrnout archivované kontakty <kvalita_leadů/archivované_kontakty>“: zajišťuje, že se zobrazí jak aktivní, tak
Do výsledků jsou zahrnuty i neaktivní kontakty.
- :ref:`Přidat pravidla pro kvalitní kontakty <quality_leads_report/add-quality-rules>“: zahrnout nebo vyloučit
výsledky založené na kritériích, která jsou specifická pro konkrétní společnost nebo obchodní tým.

.. obrázek:: kvalita_vzorku/nastaveni-pravidel.png
:align:center
:alt: Příklad okna filtru s nastavenými pravidly.

Příklad okna filtru *Vlastní filtr*, ve kterém jsou všechny výchozí pravidla nakonfigurované.

... kvalita vede/začátek:

Přidejte filtr začátku
~~~~~~~~~~~~~~~~~~~~~~~~~~

Začněte definováním parametru pravidla s rozmezím dat, kliknutím do prvního pole.
v levém sloupci a zadáním „Vytvořeno“ do pole „Hledat…“, nebo posunutím
Vyhledat v seznamu nabídek.

V rozevíracím seznamu operátorů pravidla definujte parametry dále volbou:

- :guilabel:`>= (větší nebo roven)` pro zadání začátku a zahrnutí všech záznamů *po*
tento počáteční datum (stejně jako samotnou hodnotu).
- :guilabel: je mezi`` pro ostré vymezení časového úseku s jasným začátkem a koncem. Všechny
Výsledky hledání jsou zahrnuty do zprávy, pokud odpovídají definovanému rozmezí dat.

S oběma možnostmi použijte kalendář s datem a časem v pravém dolním rohu.
definovat příslušný rozsah dat. Zadáním těchto hodnot se ukončuje vytváření první pravidla.

... kvalita vede report/prodejní tým:

Přidejte filtr prodejního týmu
~~~~~~~~~~~~~~~~~~~~~~~

.. poznámka::
Tento filtr je nepovinný. Chcete-li zobrazit výsledky pro celou společnost, nezadávejte tento filtr.

Chcete-li omezit výsledky zprávy na jednu nebo více prodejních týmů, klikněte na „Nová pravidla“. Poté
klikněte na první pole pro nové pravidlo a zadejte Sales Team do pole „Hledat…“ nebo
Přejděte dolů a vyhledejte v seznamu.

V druhém poli pravidla vyberte možnost „je v“ z nabídky.
Operátor omezuje výsledky na prodejní týmy vybrané v následujícím poli.

V posledním poli vyberte požadovaný prodejní tým z roletky. Může jich být více.
Mohou být přidány do pole, kde je každý parametr ošetřen operátorem „nebo“ („například“ „jakákoliv“).
logiku vyhledávání.

... kvalita vede report / nezařazené kontakty:

Vyřaďte nezařazené kontakty
~~~~~~~~~~~~~~~~~~~~~~~~

Poté přidejte nový řádek s názvem „New Rule“. Pak klikněte do prvního pole pro nový řádek a zadejte
„Prodejce“ v poli „Hledat…“, nebo posuňte se dolů a vyhledejte jej ve seznamu.

V poli druhé části pravidla vyberte možnost „je nastaven“.
Operátor vylučuje všechny kontakty, které nebyly přiřazeny konkrétnímu obchodníkovi.

.. kvalita vede report/archivované kontakty:

Zahrňte archivované kontakty
~~~~~~~~~~~~~~~~~~~~~~

..tip:
Tento filtr je také volitelný, protože přidává archivované (neaktivní) kontakty do zprávy.
doporučuje jej zahrnout, protože tahá všechny přiřazené kontakty bez ohledu na stav.
zprávě. To zajišťuje přesnější reprezentaci přiřazených kontaktů. Nicméně
Pokud chcete vytvořit zprávu, která obsahuje pouze aktivní kontakty, neaktivujte tuto funkci.

Dále v horním pravém rohu okna „Přidat vlastní filtr“ přetáhněte
Přepněte přepínač „Zahrnout archivované“ na aktivní.

.. obrázek: kvalita_vede_report/zahrnout-archivované.png
:align:center
:alt:Pop-up okno Přidat vlastní filtr s důrazem na přepínač Zahrnout archivované položky.

Aktivací této funkce jsou do zprávy přidány archivované (neaktivní) kontakty.

... kvalitní reporty/přidat pravidla kvality:

Přidejte pravidla pro kvalitní leady
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Filtry přidávané v tomto kroku se liší podle toho, jak organizace definuje pojem „kvalitní kontakt“.

.. _track_links/define-a-lead:

Definujte kvalitní kontakt
*********************

Jako dříve bylo uvedeno, že „kvalitní kontakt“ je kontakt, který pravděpodobně povede k získání zakázky.
I když přesné kritéria pro kvalitní kontakt se mohou lišit podle organizace, často je
kombinace faktorů, které se obvykle připisují pozitivním prodejním výsledkům.
jejími členy.

Kromě základních filtrů a možností seskupení uvedených v obecném článku o kvalitních kontaktech
report <track_links/create-quality-leads-report>`, při definování filtrů se zaměřte na
kvalitní kontakt:

- E-mail nebo telefon: informace v těchto polích mohou pomoci při určování, zda
nebo není kontakt profesionální.
- :guilabel:`Zdroj`: tento prvek spojuje marketingové a generační snahy jiných Odoo
aplikace, včetně aplikací Live Chat, Social Marketing a Email Marketing.
- :guilabel:`Stage“: tento filtr lze použít k vyřazení nebo cílení na kontakty, které dosáhly konkrétní
stupně.
- :guilabel:`Střední“: zdroj vedení může naznačovat jeho kvalitu, protože různé kanály mají
různé výherní poměry a očekávané příjmy.
- :guilabel:Kampaň: Použitím filtru lze sledovat úspěšnost různých marketingových aktivit
aby získal kvalitní kontakty.
- :guilabel:`Ztracený důvod“: vyloučit kontakty, které mohou na první pohled působit jako kvalitní podle různých kritérií.
ale byly označeny jako ztracené pro určité důvody.
- :guilabel:`Štítky“: zahrnout nebo vyloučit výsledky na základě jednoho nebo více štítků.

..tip:
Při přidávání pravidel do vlastního filtru si pamatujte na výroky před každým pravidlem.
Výše uvedené prohlášení nad pravidlem určuje, zda výsledky vyhledávání musí odpovídat **všem** pravidlům.
pod výrokem nebo **kteroukoliv** z následujících pravidel pod výrokem.

.... obrázek: kvalita_vede_report/match-all-match-any.png
:synchronizace: střed
:alt:Zobrazení možností nastavení pravidel přiřazení na okně přizpůsobeného filtru.

Zobrazit zprávu
===============

.. důležité:
Na horní části formuláře „Přidat vlastní filtr“ je možnost vybrat „jakýkoliv“.
nebo všeho pravidla. Pro správné spuštění zprávy musí být záznamy, které odpovídají
**všechny následující filtry by měly být zahrnuty. Než budete filtry přidávat, ujistěte se
V tomto poli je vybráno „všechny“.

.... obrázek:: kvalita_vede_report/povolit_všechny_podmínky.png
:synchronizace: střed


Po konfiguraci filtrů klikněte na tlačítko „Přidat“. Výchozí zobrazení pro hlášení je pruhová grafika
grafech, kde jsou vodiče seskupeny podle *stádia*.

Pro seskupení výsledků podle obchodníků klikněte na ikonu :guilabel:`🔻 (trojúhelník směřující dolů)“.
pravé straně lišty „Hledat…“ otevřít rozbalovací nabídku s megamenu. Pod lištou „Skupina
V hlavičce vyberte :guilabel:Prodejci. V stejné sloupci pod :guilabel:Skupit
přejděte na záložku „Přidat vlastní skupinu“, klikněte na „Vytvořit novou“ a vyberte možnost „Aktivní“.
položku rozbalovací nabídky do vrstvy v čele s hodnotou *status*, pod nadřazeným názvem „Prodavač“.

Nyní se v zprávě zobrazuje celkový počet kvalitních kontaktů, které každý obchodník obdržel.
určeném časovém období. Protože existují filtry „Skupit podle“ s více vrstvami, tak skupené kontakty
Jsou také barevně označeny, aby bylo možné určit, zda jsou aktivní nebo označené jako ztracené.

..tip:
Chcete-li tuto vyhledávací frázi uložit na později, klikněte na ikonu :guilabel:`🔻 (trojúhelník směřující dolů)` vedle
:guilabel:`Hledat ...“ lištu a otevřít seznam nabídek. Pod nadpisem „Oblíbené“
klikněte na tlačítko „Uložit aktuální vyhledávání“.

V rozbalovacím seznamu přejmenujte zprávu ze standardního názvu „Trubka“ na „Kvalitní leady“.
a klikněte na tlačítko „Uložit“.
