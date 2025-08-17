=============================
Dodávky mezi sklady
=============================

.. |MTO| nahradit: zkratka: `MTO (Make to Order)`

Když společnost provozuje více poboček, jako jsou sklady, maloobchodní prodejny nebo výrobní závody
zařízení, občas je nutné doplnit zásoby z centrálního skladu. Odoo používá funkci *Route*
konfigurace umožňující obnovit zásoby z centrálního skladu automaticky.
vytváření převodů mezi sklady. Modul „Sklad“ v Odoo tyto převody spravuje, aby se udržel
zboží na skladě.

Tento průvodce vysvětluje, jak provádět přesuny mezi sklady pomocí dvou strategií doplňování zásob:

#:ref:`Na zakázku (MTO) <skladování/sklady_a_skladovací_prostory/MTO>“
#:ref:`Pravidlo pro přeskladnění <sklady/přeskladnění-pravidla>“

.. viz také:
:dokument: „Rozdíl mezi pravidly pro doplňování a přeskupováním zboží“

Konfigurace
=============

Inicializace pro obě doplňovací strategie je stejná. Nejdříve přejděte na
:menu „Skladová aplikace“ --> „Konfigurace“ --> „Nastavení“. V sekci „Sklad“
Aktivujte položku „Uložiště“. Pak klikněte na „Uložit“, abyste nastavení aplikovali.

.. obrázek: zásobovací sklady/skladové prostory.png
:align:center
:alt:Povolte skladové položky v nastavení zásob.

Skladiště
----------

Nastavte parametry centrálního skladu a skladů propojených s ním přes
:menu:„Aplikace skladu --> Konfigurace --> Sklady“.

.. důležité::
Každá centrální skladovna a další místa *musí mít svůj vlastní sklad*. Například každý obchod
Je považována za místní sklad.

Vyberte existující sklad nebo vytvořte nový, který bude zásobován centrálním skladem.
Klikněte na „Nový“. Pak mu dejte jméno a zadejte „Název“ a „Zkratku“, které se budou
objevit se na převodech skladu.

V záložce „Konfigurace skladu“ najděte pole „Dodávka z“. Zkontrolujte
příslušné políčko vedle názvu centrálního skladu. Pokud je možné zásoby doplnit více než jedním
skladu, zkontrolujte také skladové karty těchto skladů. Nyní víme, které sklady mohou
dodat do zásobárny.

Příklad:
Centrální sklad, ze kterého budou zásoby do prodejen putovat, se jmenuje „Centrální
:guilabel:`Dodávka z`` pole je nastaveno na tento sklad v konfiguraci skladu obchodu.
stránka.

.. viz také:
:doc:`../skladovani/sklady`

.. obrázek:resuply_sklady/sklad.png
:align:center
:alt:V sekci Konfigurace skladu dodávejte jeden sklad druhým.

Nastavit trasu produktu
----------------------

Musí být také správně nakonfigurována, aby se mohla přesouvat mezi sklady.

Přejděte na položku „Inventář aplikace“ -> „Produkty“ -> „Produkty“ a vyberte požadovaný produkt.

V záložce „Sklad“ se nová trasa zobrazí jako „X: Dodávka produktu od Y“.
sekci „Trasy“, kde X je sklad obchodu, který přijímá zboží, a Y
je sklad, který produkty odesílá.

Zatrhněte políčko „Dodávat produkt z Y“, které je určeno pro použití s |MTO|
cestu nebo pravidlo pro přeskladnění, které doplňuje zásoby tím, že se produkt přesune z jednoho skladu do druhého.
Pokračujte v postupu do odpovídajících sekcí níže.

.. skladové zásoby, sklady a MTO:

MTO
~~~

Pro doplnění produktů pomocí metody „make-to-order“ přejděte na formulář produktu a zkontrolujte
:ref:`Trasa MTO je nearchivovaná <inventory/warehouses_storage/unarchive-mto>“ a tak se v
:guilabel:`Trasy“ v záložce „Soubor“.

S doplněním zásob a trasami MTO vyberte sekci s názvem:
skladu <výdejní sklad/sklady výdeje/přebírání zboží>.

Příklad:
Produkt prodávaný v skladu Store je doplňován z centrálního skladu označeného
„VášPodnik“. Pro doplnění produktu pomocí |MTO| jsou vybrány následující trasy:

   - :guilabel:`Obchod: Dodávat produkt z Vaší společnosti“
   - :guilabel:`Dodání na objednávku (MTO)“

.... obrázek: doplňovací sklady/doplnění trasy.png
:srovnání: do středu
:alt: Nastavení trasy, které umožňuje dodávku z druhého skladu.

...Inventář/sklad/pravidlo pro přeobjednávání:

Pravidlo přeskupení
~~~~~~~~~~~~~~~

Nejprve zkontrolujte, že je nastaveno „Dodávka produktu ze Z“ (viz. guilabel:X: Dodávka produktu ze Z).
trase je vybrána v záložce „Sklad“ v dialogovém okně pro nastavení produktu.

Pak vytvořte pravidlo pro automatické doplňování zásob kliknutím na tlačítko :guilabel:`Reordering
Chytrý tlačítko pro pravidla.

Klikněte na „Nový“ a nastavte:

- :guilabel:`Lokalita“: skladová lokalita obchodu. Například „SKLAD/ZÁSOBY“.
- :guilabel:`Trasa“: :guilabel:`X: dodávka produktu z Y“.
- „Minimální množství“ a „Maximální množství“, aby se automaticky převedly zásoby, když
pokud se zásoby dostanou pod stanovený limit.

.. viz také:
:ref:`pravidla pro přeskupení“

Příklad:
Pravidlo 0/0 pro přeskladnění zboží do obchodu.
vytvoří se sklad s hodnotou :guilabel:`Lokalita“ nastavenou na „Obchod / Zásoby“.
:guilabel:`Trasa“ nastavena na „Obchod: Dodání od společnosti YourCompany“.

.... obrázek::resupply_warehouses/reordering-rule.png
:srovnání: do středu
:alt: Zobrazit konfigurace přeřazovacích pravidel.

... skladování, sklady a dodavatelský řetězec:

Dodat zásoby z jednoho skladu do druhého
====================================

Po dokončení nastavení spusťte doplňování pomocí jedné z několika metod, například:

- Přejděte do formuláře produktu, který je přeobjednáván z jiného skladu.

Klikněte na tlačítko „Doplnit“ v horním levém rohu stránky produktu. V okně vyskakovacího okna
Zadejte sklad do prodejny (např. „Prodejna“), klikněte na tlačítko :guilabel:`Potvrdit“.

.... obrázek:resupply_warehouses/replenish.png
:align:center
:alt:Okno s nabídkou doplňků na kartě produktu.

- Vytvořte nabídku a v záložce „Další informace“ nastavte „Sklady“ na
maloobchodní prodejna (např. „Obchod“), když prodává produkt, snižuje množství produktu na skladě
pod minimální hodnotou stanovenou pro znovuřazení.


:align:center
:alt:Vytvořit citaci v obchodě.

Jednou spuštěním Odoo vytvoří dvě převody: Jedna je „přijetí objednávky“ od centrálního dodavatele.
sklad, který obsahuje veškeré potřebné zboží pro prodejnu, a druhý je
z hlavního skladu.

Zboží je v průběhu přepravy umístěno na „fyzických lokalitách / mezi sklady“.

Příklad:
Vytvoří se prodejní objednávka na zboží v obchodě. Pro doplnění zásob v obchodě
zboží odtud poslat, Odoo vytvoří dodací list ze skladových zásob centrálního skladu.
„WH/Sklad“ do skladu „SKLAD/Sklad“. Zboží se během cesty mezi
skladů, jsou v „Fyzických lokalitách/Mezi sklady“.

Finální dodací listina je od obchodu k doručovací adrese zákazníka a není
vztahující se k průběhu procesu popsanému v tomto návodu.

.... obrázek:resupply_warehouses/transfers.png
:alt:Zobrazit přepravu z skladu do obchodu.

