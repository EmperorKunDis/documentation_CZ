==================
Pravidla obsahu
==================

Ačkoli nás podporujete v tom, abyste si vytvořili svůj vlastní styl psaní, některá pravidla se stále uplatňují pro zachování jasnosti
Aby byl obsah snadno pochopitelný.

.. důležité:
Doporučujeme přečíst si rst_guidelines a hlavní dokumentaci v sekci :doc:`/documentation`.
stránky, než se připojíte.

... přispívající obsah a organizace:

Dokumentační organizace
==========================

Při psaní dokumentace k dané problematice udržujte stránky v rámci stejné složky uspořádané.

Pro většinu témat by měla stačit jedna stránka. Umístěte ji do příslušné sekce
dokumentace (např. obsah související s aplikací CRM se umísťuje pod :menuselection:`Uživatelské dokumenty --> Prodej
--> CRM“) a dodržujte pokyny pro strukturu dokumentů („contributing/content/structure“).

Pro složitější témata je třeba mít více stránek, aby byly pokryty všechny jejich aspekty. Obvykle se
našel byste se v situaci, kdy byste doplňovali dokumentaci tématu, které je již částečně pokryto. V takovém případě
nebo vytvořit novou stránku a umístit ji na stejnou úroveň jako ostatní související stránky nebo přidat nové sekce.
na existující stránku. Když dokumentujete komplexní téma od začátku, uspořádejte obsah
Několik dětských stránek, které odkazují na rodičovskou stránku této složky (:abbr:`TOC (Tabulka obsahu)
Obsah) stránky; pokud možno, píšeme obsah na rodičovské stránce a nejenom na dětských
stránky. Přidat stránku do navigačního menu pomocí
:ref:`ukázat obsah <contributing/rst/dokumentace-metadata>“ příkazu.

.. poznámka::
Zbytečně neopakujte obsah. Pokud je nějaká problematika již na jiné stránce popsána,
:ref:`referenci <contributing/rst/hyperlinks>“ namísto opakování stávajících informací.

.. důležité:
Při smazání nebo přesunutí souboru typu .rst aktualizujte příslušný textový soubor.
:souborů seřazených podle verze vaší větve (například soubor :file:`17.0.txt`). Pro toto přidejte
novou řádku na konci příslušné sekce (např. # aplikace / prodej). Na této řádce
Nejprve přidejte záznam pro přesměrování s původní polohou souboru, následovaný mezerou, a pak
přidat bod výstupu s novou nebo relevantní polohou souboru. Například pokud se soubor přesouvá
:souboru unsplash.rst z adresáře aplikace/weby/webová stránka/konfigurace
:soubor: `applications/general/integrations`, do části
# aplikace/weby:

...: kódový blok

aplikace/weby/webová stránka/konfigurace/unsplash.rst aplikace/obecné/integrace/unsplash.rst

... přispívajících k obsahu a struktuře:

Struktura dokumentu
==================

Používejte různé úrovně nadpisů k uspořádání textu do sekcí a podsekcí. Nadpisy nejsou
nejen v dokumentu, ale také na navigačním menu (pouze hlavička H1) a na „Tento
vlevo do „patičky“ (od nadpisů 2. po 6. úrovně).

+---------------------------------------------------------------------------------------+
| | **H1:Název stránky**                                                                   |
| |Název stránky poskytuje čtenářům rychlý a jasný přehled o obsahu.
|Je o tom, co je v ní.                                                                          |
|                                                                                       |
|Tento oddíl obsahuje popis nadcházejícího obsahu z pohledu podnikání.
pohledu **, a neměli by se soustředit na Odoo, protože jde o dokumentaci a ne o |
|marketing.                                                                                   |
|                                                                                       |
|Pod nadpisem stránky (h1) začněte **úvodním odstavcem**, který čtenáři pomůže orientovat se na stránce.
|zajistit, aby našli správnou stránku, a pak vysvětlit **podnikatelské aspekty  |
V následujících odstavcích se tedy podíváme na téma **.
+-----+---------------------------------------------------------------------------------+
|     | | **H2: Název sekce (konfigurace)**                                                  |
|     | |První část H2 se týká konfigurace funkce nebo popisu.
|         |  předpoklady k dosažení konkrétního cíle.                                          |
+-----+---------------------------------------------------------------------------------+
|     | | **H2: Název sekce (hlavní části)**                                                  |
|      | |Vytvořte takové hlavní sekce, kolik akcí nebo funkcí chcete odlišit.
+-----+-----+---------------------------------------------------------------------------+
|     |     | | **H3: Pododstavec**                                                          |
|Subpodkapitoly jsou ideální pro hodnocení velmi specifických bodů.
+-----+-----+---------------------------------------------------------------------------+
|         |**Další část**                                                                    |
+-----+---------------------------------------------------------------------------------+

Jak psát dobré nadpisy a záhlaví:

- **Buďte struční**: vyhněte se větám, otázkám a titulkům začínajícím slovy „jak“.
- Ve svých titulcích nepoužívejte zájmena, zejména 2. osobu (vy/vaše).
- Používejte „slovesný tvar“. To znamená, že pouze začínáme psát velkým písmenem:

  - první slovo titulku nebo nadpisu.
  - první slovo za lomítkem.
  - příslovce.

.. poznámka::
   - Tituly a nadpisy obecně odkazují na koncept a nejsou jménem
funkcí nebo modelem.
   - Pokud slova akronymu neobsahují podstatné jméno, neměla by být začátečním písmenem.
   - Přídavná jména v nadpisech jsou v pořádku, protože často popisují akci.

.. viz též:
   - :ref:`RST cheat sheet: nadpisy <contributing/rst/headings>`
   - :ref:`RST cheat sheet: značky <contributing/rst/markups>`

... přispívání obsahu a styl psaní:

Styl psaní
=============

Psaní dokumentace není stejné jako psaní pro blog nebo jiné médium. Čtenáři
Čtenáři jsou pravděpodobnější, že se budou přeskakovat obsah a hledat informace, které potřebují.
Dokumentace je místo pro informování a popis, nikoli přesvědčování a propagandu.

..tip:
Za všech okolností se snažte používat co nejméně druhé osoby a místo toho používejte příkazovou formu tam, kde je vhodná.
Nicméně nekomplikujte věty jen proto, abyste se vyhnuli adresování čtenáře přímo.

...... příklad::
|  **Příklad dobrý:**
|Vyberte vhodný výběr z nabídky.

| **Špatný příklad:**
|Vyberte vhodný výběr z nabídky.

... přispívat obsahem a pravopisně.

Psaní
--------

Používejte americkou angličtinu ve všech dokumentacích.

... přispívat k obsahu a konzistenci:

Konsistence
-----------

*Konsistence je klíčem k úspěchu.*

Ujistěte se, že styl psaní zůstane **konzistentní**. Při úpravách již existujících textů se pokuste
Současný styl a prezentace nebo přepsat tak, aby odpovídal vašemu vlastnímu stylu.

...přispívání obsahu/kapitálové hodnotě:

Psaní velkými písmeny
--------------

- Používejte titulek v případě, že je uveden v seznamu :ref:`<contributing/content/structure>`.
- Zapamatujte si názvy aplikací, např. Odoo Sales, aplikace Sales atd.
- Zapněte velké písmeno u názvů políček a tlačítek tak, jak je zobrazeno v Odoo. Pokud je název ve všech velkých písmenech
převést na začátečník.
- Ve větě po závorkách nebo uvozovkách se písmeno velké nepíše.
- Vyhněte se velkým písmenům u běžných podstatných jmen, jako je „objednávka na prodej“ a „seznam materiálu“.
odkazovat na štítek nebo model.

... přispívajících k obsahu a gramatickým časům:

Časová páda
------------------

V angličtině se popisy a pokyny zpravidla píší v přítomném čase.
Budoucí čas je vhodný pouze tehdy, když se má konkrétní událost stát později.

Příklad:

| **Dobrý příklad (přítomný čas):**
|Snímky obrazovky jsou automaticky zmenšeny tak, aby vyhovovaly šířce bloku obsahu.

| **Špatný příklad (budoucnost):**
|Při pořízení snímku obrazovky si pamatujte, že bude automaticky upraven tak, aby se vešel do obsahu
šířka bloku.

... přispívajících obsahů/seznamů:

Seznamy
=====

Seznamy pomáhají organizovat informace v jasném a stručném způsobu a zlepšují čitelnost.
abyste zdůraznili důležité detaily, provedli čtenáře krok za krokem systémem atd.

Používejte seznamy s čísly, pokud je důležitá pořadí, například návody, postupy nebo kroky, které musí být
Provedené v určitém pořadí.

Používejte seznamy s odrážkami, pokud nezáleží na pořadí položek (například seznam funkcí, polí).
opce, atd.

..tip:
   - Používejte text vodorovně, pokud chcete něco vysvětlit nebo máte tři položky a méně.
   - Spojte seznamy s odrážkami a číslováním pomocí :ref:`seznamů vnořených pod sebe <contributing/rst/nested-list>
Pokud je to vhodné.
   - Zvažte seskupení jednoduchých kroků do stejného položky seznamu např.:Přejít na: `Webové stránky
--> Webové stránky  --> Stránky a klikněte na položku Nová.
   - Používejte pouze tečku na konci položky seznamu, pokud tvoří celý větný celek.

Příklad:
*Seznam bodů*

Následující pole jsou k dispozici na zprávě „Dodání“:

   - :guilabel:`Produkt“: produkt, který vyžaduje doplnění
   - :guilabel:`Lokalita“: konkrétní lokalita, kde je produkt skladován
   - :guilabel:`Sklad“: sklad, kde je produkt uložen
   - :guilabel:`Na skladě“: aktuální množství produktů

**Numerovaný seznam**

Pro vytvoření nové stránky postupujte takto:

   #– Otevřete aplikaci Webové stránky, klikněte na tlačítko „Nová“ v pravém horním rohu a
select:guilabel:"Stránka";
      - Nebo přejděte na „Webové stránky“ → „Stránka“ → „Nový“.

   #Zadejte název stránky: guilabel:Název stránky; tento název se používá v nabídce a ve URL adrese stránky.
   #Klikněte na tlačítko „Vytvořit“.
   #Upravte obsah a vzhled stránky pomocí webového editoru, pak klikněte
:guilabel:`Uložit“.

.. viz též:
:ref:`Příručka RST: seznamy <contributing/rst/lists>`

Ikony
=====

Použijte ikony :ref:`<contributing/rst/icons>`, aby pomohly čtenářům identifikovat uživatelské rozhraní.
i snížit potřebu dlouhých vysvětlování. Každý ikonu doprovodte popisem
v závorkách.

Příklad:
Jakmile je režim vývojáře aktivován, můžete přistupovat k nástrojům pro vývojáře klepnutím na
:icon:`fa-bug` (:guilabel:`bug`) ikonka.

.. viz též:
:ref:`Cheat sheet RST: ikony <contributing/rst/icons>`

.._příspěvky/obsah/obrázky:

Obrázky
======

Přidání několika obrázků k doplnění textu pomáhá čtenářům porozumět a zapamatovat si obsah.
Obrazová dokumentace však nikdy nemůže nahradit psaný text.
své vlastní, aniž by se opírali o vizuální pomůcky. Používejte obrázky například k vyznačení
konkrétní bod nebo vysvětlit příklad.

.. důležité:
Nezapomeňte na „kompresi PNG souborů pomocí pngquant <https://pngquant.org>“.

... _přispívat obsahem/obrázky:

Snímky obrazovky
-----------

Snímky obrazovky jsou automaticky zmenšeny tak, aby vyhovovaly šířce bloku obsahu. To znamená, že pokud
jsou příliš široké a nejsou čitelné na nižších rozlišeních obrazovek. Doporučujeme se vyhnout
snímek obrazovky aplikace, pokud není nezbytně nutné, a ujistěte se, že obrázky jsou širší než rozsah
a rozlišení 768–933 pixelů.

Tady je několik tipů, jak vylepšit vaše snímky obrazovky:

#**Změňte šířku prohlížeče**, buď změnou velikosti okna samotného nebo otevřením
v prohlížeči a změnou šířky.
#Vyberte požadovanou oblast namísto celého okna.
#Odstraňte zbytečné informace a upravte velikost sloupců, pokud je to možné.

.. důležité:
Nepoužívejte na obrázcích snímků obrazovky značky jako jsou čtverce nebo šipky. Místo toho upravte obrázek tak, aby
upozornit na nejdůležitější informace a zajistit, aby byly textové pokyny jasné
bez použití obrázků.

Příklad:
**Dobrý příklad (zmenšená prohlížečka, odstraněné nadbytečné sloupce, upravené šířky sloupců, oříznuté):**

.. obrázek:: pravidla obsahu/citace - seznam zkrácený.png
:alt: Snímek s oříznutým okrajem

**Špatný příklad (celoobrazovkový snímek):**

.. obrázek:: content_guidelines/citace-seznam-celý.png
:alt: Celá obrazovka

... přispívajících k obsahu a médiím:

Média
-----------

A ***název souboru média***:

- je psáno v malých písmenech.
- je relevantní pro obsah médií.
- odděluje svá slova pomocí **záporné čárky** (-) (:file:awesome-filename.png).

Každý soubor RST má svou vlastní složku pro ukládání mediálních souborů. Název složky musí být stejný jako název
Název souboru RST.

Příkladem je dokument s názvem :file:`doc_filename.rst`, který odkazuje na dvě obrázky umístěné v
soubor „doc_filename“.

::

└── section
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│     │     └── screenshot-tips.gif
│     │     └── awesome-filename.png
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

.. poznámka::
Předtím se obrázky většinou pojmenovávaly čísly (např. :file:`feature01.png`).
je umístěn do jediného složky `media`. Je vhodné, aby jména vašich nových obrázků neobsahovala
Také je důležité **nepřejmenovávat nezměněné soubory**, protože tak by se počet kopií zdvojnásobil.
hmotnost přejmenovaných obrázků v repozitáři. Nakonec všechny budou nahrazeny, protože
obsah odkazující na tyto obrázky je aktualizován.

... _příspěvky/obsah/alternativní tagy:

ALT tagy
--------

ALT tag je alternativní text k obrázku, který se zobrazí v případě, že prohlížeč selže.
zobrazit obrázek. Je také užitečný pro uživatele s omezenou schopností vidění. Nakonec pomáhá
vyhledávače, jako je například Google, aby pochopily, o co se jedná na obrázku a správně jej indexovaly.
zlepšuje: zkratka SEO (optimalizace pro vyhledávače).

Dobrými alternativními texty jsou:

- **Stručně** (maximálně jedna řádka).
- *Nepřekopírujte* předchozí větu nebo nadpis;
- Dobrá popisnost děje na obrázku;
- Při čtení nahlas je pochopitelný bez problémů.

Příklad:

Vhodný alt tag pro následující snímek obrazovky by byl například *Aktivace vývojářského režimu
aplikace Nastavení*.

.. obrázek:: content_guidelines/settings.png
:alt:Aktivace vývojářského režimu v aplikaci Nastavení

.. viz též:
:ref:`Příručka RST: obrázky <contributing/rst/images>`
