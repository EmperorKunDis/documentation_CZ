:custom-css:showcase_tables.css

==============================
Pokyny a kartička pro RST
==============================

.. důležité:
Doporučujeme přečíst si :doc:`content_guidelines` a hlavní :doc:`../documentation`.
stránky, než se připojíte.

Při přispívání do dokumentace se držte níže uvedených pokynů RST, abyste pomohli zachovat konzistenci.
s ostatní dokumentací a usnadnit proces prohlídky týmu:

- :ref:`Používejte formátování. <contributing/rst/formatting>`
- :ref:`Buďte konzistentní při používání odsazování.<contributing/rst/indentation>`
- :ref:`Začněte novou řádku před 100. znakem. <přispívat/rst/maximální délka znaků>`

Pro hypertextové odkazy:

- :ref:`Používejte relativní odkazy pro vnitřní URL. <contributing/rst/relative-links>`
- :ref:`Při přesouvání cílů hyper odkazů se nerozbíjejte. <contributing/rst/update-targets>`
- :ref:`Nepoužívejte nepopisné název odkazů. <contributing/rst/descriptive-links>`

... přispívání/RST/formátování:

Formátování
==========

Použijte specifické formátování k zlepšení čitelnosti a srozumitelnosti. Například
:ref:`contributing/rst/menuselection` pro cesty v menu a :ref:`contributing/rst/guilabel`
pro ostatní prvky uživatelského rozhraní, jako jsou pole, tlačítka a možnosti, viz:
pro poznámky, například :ref:`contributing/rst/example`, pro příklady atd.

.. poznámka::
Přidejte prázdnou řádku mezi různé blokové prvky, jako jsou odstavce, seznamy a příkazy.
zajistit správné zobrazení a formátování.

... _contributing/rst/hyperlinks-guidelines:

Hypertextové odkazy
==========

... přispívání/rst/odkaz na relativní adresu:

Interní URL adresy: relativní odkazy
-----------------------------

Pokud potřebujete odkázat na :ref:`interní dokumentaci <contributing/rst/doc-hyperlinks>
nebo souboru, který není umístěn v stejné složce jako aktuální
Stránka vždy používá „relativní cesty k souborům“ namísto „absolutních cest k souborům“. To zajišťuje, že odkazy
zůstanou platné i při aktualizacích verzí, změnách názvu složky a struktuře adresářů
restrukturalizace.

Absolutní cesta k souboru uvádí cílové umístění od kořenového adresáře. Relativní cesta
používá chytré zkratky (například „../“, která směřuje do složky s rodičem), aby bylo možné určit cíl
umístění vzhledem k umístění zdrojového dokumentu.

Příklad:

....... poznámka::
Příklad níže má za cíl ilustrovat rozdíl mezi absolutními a relativními veličinami.
relativní odkazy. Vždy používejte odkaz na příspěvek s názvem „contributing/rst/doc-hyperlinks“
dokumentace stránky.

Pokud máme následující strom souborů:
   ::

dokumentace
├── obsah
├─┬─ applications
│  │    └── prodej
│  │  │    └─ prodej
│  │  │  │    └── produkty_cena
│  │  │  │  │  │    └── produkty
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
│  │  │  │  │  │  │    └─ varianty.rst
├────┼────┼────┼────┼────┤

Příklad odkazu na soubor :file:`prices.rst` a :file:`variants.rst` je možný z :file:`import.rst`.
V následujících letech:

   #Absolutní:

         - „dokumentace/obsah/aplikace/prodej/prodej/produkty a ceny/ceny.rst“
         - „dokumentace/obsah/aplikace/prodej/prodej/produkty/varianty.rst“

   #Relativně:

         - `./ceny.rst
         - `variants.rst`.

... přispívat/rst/aktualizovat cíle:

Refactoring: cíle odkazů
------------------------------

Při přepracování nadpisů nebo cílů odkazů se zaměřte na
aby nedošlo k porušení odkazů na tyto cíle nebo aby byly aktualizovány v souladu s nimi.

... přispívajících/rst/popisných štítků:

Hypertextové štítky
----------------

Nezapomeňte na popisné štítky u odkazů:ref:`<contributing/rst/hyperlinks>`.

Příklad:

| **Výborný příklad (popisný štítek):**
| Prosím, obraťte se na dokumentaci účetnictví v :doc:`Dokumentace aplikací <../../../applications/finance/accounting>`.

| **Špatný příklad (nevýstižná štítek):**
| Prosím, obraťte se na stránku „Tento dokument“ (viz odkaz vpravo).

... přispívání/RST/začátek řádku:

Zápis v odstavci
===========

Používejte pouze mezeru (nikdy ne tabulátor).

Využijte kolikrát chcete mezer na začátku odsazené řádky, abyste ji vyrovnali s první
způsobu označování v řádku výše. To obvykle znamená tři mezery, ale stačí dvě
Pro například pro seznamy s čísly.

Příklad:
První „:“ je pod „i“ (tři mezery):

... kódový blok:: rst

... obrázek: média/příklad.png
:alt: příklad

Poznámky s pouze titulkem a odkazy na stránky začínají pod znakem „t“ (tři mezery):

... kódový blok:: rst

... toctree::
:tituly:

placené faktury
závazky/výplata

Pokračování je pod „I“ slova „Faktura“ (dvě mezerová mezera):

... kódový blok:: rst

      - Faktura na objednané množství: vystavte fakturu za celou objednávku ihned po potvrzení objednávky.
      - Faktura na dodané množství: faktura za to, co bylo dodáno i když je to částečné.
dodání.

... přispívání/rst/počet znaků:

Omezení na 100 znaků
=====================

V RST je možné přerušit řádek bez nutnosti vložení řádku do zobrazeného HTML. Využijte
tuto vlastností psát **řádky maximálně o 100 znaků dlouhé**. Není nutné
mezeru za slovem na konci řádku.

..tip:
   - Můžete bezpečně přerušit řádek na jakémkoliv místě, i uvnitř značek, jako například menuselection.
„doc“.
   - Některé externí odkazy mohou překročit 100 znaků, ale ponechání je na jediné řádce
přijatelné.

Příklad:

... kódový blok:: rst

Pro registraci prodejního účtu v Odoo přejděte na: „Prodej --> Konfigurace -->
Nastavení ---> Amazon Connector ---> Amazon účty a klikněte na tlačítko „Vytvořit“.
**ID prodejce** pod odkazem „Váš token“.

... přispívat/rst/nadpisy:

Obsah
========

Pro každou řádek formátování (např. „===“) zapište stejný počet znaků („=“).
hlavička.

Symboly používané pro formátování nejsou důležité. Důležitý je jen pořadí, v jakém jsou
písemné záležitosti, jak určuje velikost ozdobné hlavičky. To znamená, že můžete
můžete narazit na odlišné formátování nadpisů a v jiném pořadí, v takovém případě byste měli sledovat
formátování přímo v dokumentu. V jiném případě použijte formátování uvedené níže.

+--------------+----------------------+
|Velikost nadpisu |Formátování          |
+==============+======================+
|H1| .. kódový blok:: text |
|              |                      |
|              |    =======           |
|Hlava 1|Hlava 1|
|              |    =======           |
+--------------+----------------------+
|H2            | .. kódový blok:: text |
|              |                      |
|Hlava 1|Hlava 1|
|              |    =======           |
+--------------+----------------------+
|H3| .. kódový blok:: text |
|              |                      |
|Hlava 1|Hlava 1|
|              |    -------           |
+--------------+----------------------+
|H4| .. kódový blok :: text |
|              |                      |
|Hlava 1|Hlava 1|
|              |    ~~~~~~~           |
+--------------+----------------------+
|H5           | .. kódový blok:: text |
|              |                      |
|Hlava 1|Hlava 1|
|              |    *******           |
+--------------+----------------------+
|H6| .. kódový blok::text
|              |                      |
|Hlava 1|Hlava 1|
|              |    ^^^^^^^           |
+--------------+----------------------+

.. důležité:
Každý dokument musí mít přesně jeden nadpis H1.

... přispívání/RST/značkování:

Zápisky
=======

... přispívající/rst/kurziva:

Poznámka (kurzíva).
-----------------

Zvýraznit část textu. Text se zobrazí kurzívou.

.. seznam tabulkový::
:třída:o-vystaveni

   * – Vyplňte informace *před* uložením formuláře.

   * 

Vyplňte informace před uložením formuláře.

... přispívající/rst/kurzíva:

Silné zvýraznění (tučně).
----------------------

Pro zvýraznění části textu. Text je zobrazen tučně.

.. seznam tabulkový::
:třída:o-vystaveni

   * – Subdoména je doména, která je součástí jiné domény.

   * 

Subdoména je doména, která je součástí jiné domény.

... přispívání/RST/ukázka kódu:

Technický výraz
------------------------

Zadat technický výraz nebo konkrétní hodnotu vložit. Text je vykreslen literálně.

.. seznam tabulkový::
:třída:o-vystaveni

   * -Vložte adresu vašeho tiskárny, například „192.168.1.25“.

   * 

Do pole vložte adresu vašeho tiskárny, například „192.168.1.25“.

... přispívajících/rst/definice:

Definice
-----------

Použijte značku dfn k definování pojmu.

.. seznam tabulkový::
:třída:o-vystaveni

   * - Dokumentace je psaná v RST a musí být převedena (přeložena do HTML)
vypadat hezky.

   * 

Dokumentace je psána v RST a musí být sestavena (převzata do HTML).
Vypadá pěkně.

..._přispívání/rst/zkratky:

Zkratky
-------------

Použijte značku abbr k napsání samozřejmě definované zkratky, která se zobrazuje jako nápověda.

.. seznam tabulkový::
:třída:o-vystaveni

   * – Odoo používá :abbr:`OCR (optická charakterová rozpoznávání)“ a umělou inteligenci
technologie pro rozpoznávání obsahu dokumentů.

   * 

Odoo používá:abbr:`OCR (optická charakterová rozpoznávání)“ a umělou inteligenci
technologie pro rozpoznávání obsahu dokumentů.

... přispívajících k RST a GUI labelingu:

Element grafického uživatelského rozhraní
----------------------------------------------

Použijte značku guilabel k označení jakéhokoliv textu uživatelského rozhraní (např. štítků).

.. seznam tabulkový::
:třída:o-vystaveni

   * -Aktualizujte své přihlašovací údaje a potom klikněte na tlačítko „Uložit“.

   * 

Aktualizujte své přihlašovací údaje a poté klikněte na tlačítko „Uložit“.

.. poznámka::
Vyhněte se používání značky „guilabel“ při odkazování na koncept nebo obecný pojem.

...... příklad::
      - | **Příklad dobrý:**
|Vytvoření kreditní faktury provedete v sekci „Účetnictví“ -> „Zákazníci“ -> „Faktury“.
otevřít fakturu a kliknout na „Kreditní poznámka“.
      - |**Špatný příklad:**
|Vytvoření zápočtového dokladu provedete v menu „Účetnictví“ - „Zákazníci“ -
Vyberte „Faktury“, otevřete „Fakturu“ a klikněte na „Kreditní poznámku“.

... _contributing/rst/menuselection:

Vyberte si z menu
--------------

Použijte značku „menuselection“ k průvodu uživatele v sekvenci nabídek začínající aplikací.
jméno.

.. seznam tabulkový::
:třída:o-vystaveni

   * – Chcete-li zkontrolovat výsledky prodeje, přejděte na: „Prodej“ – „Zprávy“ – „Dashboard“.

   * 

Pro přehled o prodejních výsledcích přejděte na: „Prodeje“ -> „Zprávy“ -> „Dashboard“.

.. poznámka::
Do značky menuselection zahrňte pouze skutečné položky menu:

   - Použijte značku :ref:`contributing/rst/guilabel` pro ostatní prvky uživatelského rozhraní, například
tlačítka a nadpisy sekcí:

... kódový blok text

Pro nastavení politiky kontroly faktur přejděte do sekce „Nákup“ a poté na „Konfigurace“.
--> Nastavení, a posuňte se dolů do části :guilabel:`Fakturace“. Pod položkou :guilabel:`Daňový doklad
„Kontrola“, vyberte buď „Počet objednaných položek“ nebo „Počet obdržených položek“.

   - Nebraňte se vkládat názvy částí menu. Například v obrázku níže by nemělo být „Časopisy“.
bude součástí cesty v nabídce: menuselection:"Účetnictví --> Účetnictví --> Příjmový účet":

.. obrázek:: rst_guidelines/accounting-menu.png
:alt:Nástroje pro účetnictví, v části sekce Záznamy.

... přispívajících souborů rst:

Soubor
----

Použijte značku „soubor“ k označení cesty nebo názvu souboru.


.. seznam tabulkový::
:třída:o-vystaveni

   * - Vytvořit přesměrování pomocí souboru `redirects.txt`, který se nachází v kořenovém adresáři repozitáře.

   * 

Vytvářejte přesměrování pomocí souboru `redirects.txt`, který je umístěn v kořenovém adresáři
repozitář.

... přispívající/rst/příkaz:

Příkaz
-------

Použijte značku „příkaz“ k zvýraznění příkazu.

.. seznam tabulkový::
:třída:o-vystaveni

   * - Spusťte příkaz :command:`make clean html`, který odstraní již existující soubory a vygeneruje
dokumentaci do HTML.

   * 

Pro odstranění stávajících sestavených souborů a jejich znovu vytvoření spusťte příkaz:
dokumentaci do HTML.

... přispívajících/rst/ikony:

Ikony
-----

Použijte značku „icon“ k přidání názvu ikonového souboru. V Odoo se používá tři sady ikon:
„FontAwesome4 <https://fontawesome.com/v4/icons/>“ („fa-*“), „Odoo UI <ui/odoo-ui-icons>“
(`oi-*`) a ikony :ref:`Odoo Tabulka <ui/odoo-spreadsheet-icons>` (`os-*`).

Sledujte ikonu s jejím názvem jako :ref:`contributing/rst/guilabel` v závorce jako popis.

.. seznam tabulkový::
:třída:o-vystaveni

   * – Grafický pohled je reprezentován ikonou „fa-area-chart“ (graf s plochami).

Výchozí pohled je reprezentován ikonou „Pohled na sloupce“ :icon:`oi-view-pivot` :guilabel:`(pivot table)` .

V Odoo **Tabulce** použijte ikonu „os-global-filters“ a název „globální filtry“.

   * 

Grafický pohled je reprezentován ikonou :icon:`fa-area-chart` :guilabel:`(oblastní graf)`

Pohled na sloupce je reprezentován ikonou :icon:`oi-view-pivot`.

V Odoo Spreadsheet použijte ikonu „os-global-filters“ a název „(global filters)“.

... přispívajících/rst/seznamů:

Seznamy
=====

..._přispívání/rst/seznam bodů:

Seznam s odrážkami
-------------

.. seznam tabulkový::
:třída:o-vystaveni

   * — To je seznam s odrážkami.
       - Má dvě položky, druhou
položka obsahuje dvě řádky.

   * 

          - Toto je seznam s odrážkami.
          - Má dvě položky, druhou
položka používá dvě řádky.

... přispívání/rst/číslovaný seznam:

Číslovaný seznam
-------------

.. seznam tabulkový::
:třída:o-vystaveni

   * –. To je seznam s číslováním.
       #Číslování je automatické.

   * 

          #Toto je seznam číselných bodů.
          #Číslování je automatické.

.. seznam tabulkový::
:třída:o-vystaveni

   * - 6. Tento formát použijte k zahájení číslování
s číslem jiným než jedním.
       #Počítání je automatické odtamtud.

   * 

          6. Tento formát použijte k zahájení číslování.
s číslem jiným než jedna.
          #Počítání je automatické odtamtud.

..tip:
Doporučujeme používat seznamy s automaticky číslovanými položkami, například pomocí znaku „#.“ místo „1.“, „2.“, atd., aby byl kód přehlednější.
odolnost.

.._přispívání/rst/seznamy v seznamu:

Vnořené seznamy
------------

..tip:
   - Před vnořenými prvky seznamu přidejte prázdnou řádku.
   - :ref:`Vyrovnané odsazení seznamů <contributing/rst/indentation>
pod nadřazeným položkou.

.. seznam tabulkový::
:třída:o-vystaveni

   * —To je první položka seznamu s čísly.

         #Je v něm seznam s číslovanými položkami.
         #s dvěma položkami.

   * 

          - Toto je první položka označená hvězdičkou.

            #Je v něm seznam s číslovanými položkami.
            #s dvěma položkami.

... přispívání/RST/hypertextové odkazy:

Hypertextové odkazy
==========

.._přispívání/rst/externí odkazy:

Externí odkazy
-------------------

Externí odkazy jsou odkazy na URL s vlastním názvem. Syntaxe je:
``label <URL>_``

.. poznámka::
   - Použijte odkaz na stránku dokumentace podle :ref:`<contributing/rst/doc-hyperlinks>`.
další dokumentační stránka.
   - Nepoužívejte:ref:`nevýstižné popisky odkazů <contributing/rst/descriptive-labels>“.

.. seznam tabulkový::
:třída:o-vystaveni

   * - Například „Toto je externí odkaz na webové stránky Odoo <https://www.odoo.com>“.

   * 

Příkladem je např. „Toto je externí odkaz na webové stránky Odoo <https://www.odoo.com>“.

... _přispívat/rst/externí_hypertextové_odkazy:

Externí aliasy odkazů
--------------------------

Externí aliasy odkazů umožňují vytvářet zkratky pro externí odkazy. Syntaxe definice
je následující: „…_cíl: URL“. Existují dvě možnosti odkazování na ně v závislosti na použití:

#Znak „target_“ vytváří hypertextový odkaz s názvem cíle jako popiskem a URL jako referencí.
znak _ se posunul za cíl.
#Label „<cílová oblast>“ nahrazuje název cíle a cíl je nahrazen
URL adresa.

.. seznam tabulkový::
:třída:o-vystaveni

   * „Pilotní projekt“ je zjednodušený
verze, prototyp toho, co se očekává, že bude souhlasit s hlavními liniemi očekávaných změn. „PoC
„Počáteční důkaz“ je běžné zkratka.

   * 

.. otestování konceptu: https://cs.wikipedia.org/wiki/Otestování_konceptu

Prototyp je zjednodušená verze, prototyp toho, co se očekává, že bude souhlasit.
hlavní směry očekávaných změn. „PoC“ je běžné zkratka.

... _přispívat/rst/vlastní_ankety:

Vlastní kotvy
--------------

Vlastní ankery mají stejnou syntaxi jako externí hypertextové aliasy, ale bez URL.
odkazovat na konkrétní část souboru RST pomocí cíle jako kotvy. Když uživatelé klikají
odkazu jsou přesměrovány na část dokumentační stránky, kde je cíl definován.

Syntax definice je: „…_cíl:“. Existuje dvě možnosti, jak na ně odkazovat, a to pomocí buďto „ref“
markup:

#„:ref:“ cíl „“ vytvoří hypertextový odkaz na záložku s nadpisem definovaným níže jako „label“.
#„:ref:“ „< cíl >“ vytvoří hypertextový odkaz na značku s názvem „< cíl >“.

.. důležité:
Jako cíle jsou viditelné z celého dokumentu, pokud jsou odkazovány pomocí značky `ref`.
před jménem cílového souboru připojte název aplikace a sekce oddělené lomítkem a následně název souboru.
např. „účetnictví/daně/konfigurace“.

.. poznámka::
   - Přidejte vlastní kotvy pro všechny nadpisy, aby je bylo možné odkazovat z jakéhokoliv dokumentu.
v rámci Odoo pomocí odkazů na dokumentaci.
   - Pozor na to, že se na konci nezobrazuje znak podtržítka, což je v rozporu s tím, jak jsou řešeny externí odkazy.
<přispívání/rst/externí_odkazy>.

.. seznam tabulkový::
:třída:o-vystaveni

   * Pro více informací se podívejte na část „přispívání/rst/hyperlinky“.
o :ref:`relativních odkazech <contributing/rst/relative-links>“.

   * 

.._přispívání/rst/hypertextové odkazy:

Hypertextové odkazy
          ==========

.._přispívání/rst/relativní odkazy:

Používejte relativní odkazy pro vnitřní URL
         ------------------------------------

Pro více informací se podívejte na část :ref:`contributing/rst/hyperlinks-guidelines`.
o :ref:`relativních odkazech <contributing/rst/relative-links>.

... přispívání/rst/dokumentační hypertextové odkazy:

Hypertextové odkazy na stránky dokumentace
-----------------------------

Značení „doc“ umožňuje odkazovat na dokumentaci, která se nachází kdekoliv v adresáři, prostřednictvím
relativní cestu k souboru. Existují dvě možnosti použití značky, obě s použitím značky „doc“:


#„:doc:“ „cesta_k_stránce_s_dokumentací“ vytvoří hypertextový odkaz na stránku s dokumentací s názvem
stránka jako štítek.
#„:doc:“ „label “ „<cesta k dokumentační stránce>“ vytvoří odkaz na dokumentační stránku s názvem „label“.
štítek.

.. seznam tabulkový::
:třída:o-vystaveni

   * Prosím, obraťte se na dokumentaci účetnictví.
<../../../aplikace/finance/účetnictví> pro další informace.
:doc:`../../../aplikace/finance/účetnictví/fakturace/vystavené faktury“.

   * 

Prosím, obraťte se na dokumentaci účetnictví v sekci :doc:`Účetnictví <../../../applications/finance/accounting>`.
se dozvědět více o tématu :doc:`../../../aplikace/finance/účetnictví/fakturace pro zákazníky`.

.. důležité:
:ref:`Používejte relativní odkazy <contributing/rst/relative-links> pro odkaz na dokumentaci.

... přispívání/rst/stahování:

Odkaz na stažení souboru
------------------------

Značka „stáhnout“ umožňuje odkazovat na soubory (které nemusí být nutně :abbr:`RST
(strukturovaný text) v zdrojovém stromu ke stažení.

.. seznam tabulkový::
:třída:o-vystaveni

   * - Stáhněte si tento soubor: download:`modulový šablonový soubor <rst_guidelines/my_module.zip>
stavbou vašeho modulu.

   * 

Stáhněte si tento soubor: „struktura modulu vzorový <rst_guidelines/my_module.zip>“.

.. poznámka::
Uložte soubor vedle ostatních :ref:`multimediálních souborů <přispívat/obsah/multimediální-soubory>`.
odkaz na něj použít jako odkaz „relativní“ podle návodu v článku Reference.

... _přispívat/rst/obrázky:

Obrázky
======

Značka „obrázek“ umožňuje vložit obrázky do dokumentu.

.. seznam tabulkový::
:třída:o-vystaveni

   * 
:alt:Vytvořit fakturu.

   * 

.. obrázek:: rst_guidelines/create-invoice.png
:alt: Vytvořit fakturu.

..tip:
   - Obrázky by měly být většinou zarovnány doleva, což je výchozí chování. Použijte příkaz align
parametr k změně zarovnání např. „:align: center“.
   - Použijte parametr alt k přidání :ref:`contributing/content/alt-tags`, například :alt:Aktivace
vývojářský režim v aplikaci Nastavení.
   - Použijte parametr „scale“ k zmenšení obrázku například takto: „:scale: 75 %“.

.. viz též:
:ref:`Pravidla obsahu pro obrázky <přispívání/obsah/obrázky>`

... přispívajících/rst/bloků varování:

Poplachové bloky (upozornění)
==========================

... přispívat/rst/viz také:

Viz také
--------

.. seznam tabulkový::
:třída:o-vystaveni

   * – viz také:
          - :doc:`Účetní doklady <../../../aplikace/finance/účetnictví>`
          - :doc:`../../../aplikace/obchod/fakturace/proforma`
          - „Dokumentace Google k nastavení Analytics pro webové stránky
<https://support.google.com/analytics/answer/1008015?hl=cs>

   * 

.. také viz::
             - :doc:`Účetní doklady <../../../aplikace/finance/účetnictví>`
             - :doc:`../../../aplikace/obchod/fakturace/proforma`
             - „Dokumentace Google k nastavení Analytics pro webové stránky <https://support.google.com/analytics/answer/1008015?hl=cs>“

... přispívající/rst/poznámka:

Poznámka
----

.. seznam tabulkový::
:třída:o-vystaveni

   * — poznámka:
Použijte tento blok upozornění, abyste upoutali pozornost čtenáře a zdůraznili důležitá doplňující fakta.
informace.

   * 

.. poznámka::
Využijte tento blok upozornění k tomu, abyste čtenáře upoutali a zdůraznili důležité informace navíc.

... přispějete na RST tip:

Tip
---

.. seznam tabulkový::
:třída:o-vystaveni

   * — … tip:
Tento blok upozornění použijte k informování čtenáře o užitečném triku, který vyžaduje akci.

   * 

.. tip::
Použijte tento blok upozornění k informování čtenáře o užitečném triku, který vyžaduje akci.

... přispívající/rst/příklad:

Příklad
-------

.. seznam tabulkový::
:třída:o-vystaveni

   * — Příklad:
Využijte tento blok varování k ukázce.

   * 

... příklad::
Použijte tento blok upozornění k zobrazení příkladu.

... přispívající k rst a cvičení:

Cvičení
--------

.. seznam tabulkový::
:třída:o-vystaveni

   * – … cvičení::
V této části upozornění můžete čtenáři navrhnout cvičení.

   * 

.. cvičení::
Tento blok varování použijte k doporučení cvičení čtenáři.

... přispívající/rst/důležitý:

Důležité
---------

.. seznam tabulkový::
:třída:o-vystaveni

   * — důležité —
Využijte tento blok upozornění k oznámení důležité informace čtenářům.

   * 

... důležité::
Použijte tento blok upozornění, abyste čtenáře informovali o důležitých skutečnostech.

... přispívající/rst/varování:

Varování
-------

.. seznam tabulkový::
:třída:o-vystaveni

   * - varování
Tento upozornění blok vyžaduje, aby čtenář byl obezřetný při popisu toho, co je popsáno.
v upozornění.

   * 

.. varování::
Použijte tento blok varování, abyste požádali čtenáře, aby se s informacemi v něm obsaženými zacházeli opatrně.

... přispívající k rst/nebezpečí:

Nebezpečí
------

.. seznam tabulkový::
:třída:o-vystaveni

   * „… nebezpečí“
Použijte tento blok upozornění k tomu, abyste přitáhli pozornost čtenářů na závažnou hrozbu.

   * 

.. nebezpečí::
Použijte tento blok upozornění, abyste přitáhli pozornost čtenářů k závažné hrozbě.

... _contributing/rst/vlastní upozornění:

Obchodní zvyklost
------

.. seznam tabulkový::
:třída:o-vystaveni

   * – varování –

Upravte tento blok upozornění pomocí vlastního **názvu**.

   * 

.. upozornění: Titulek

Upravte tento blok upozornění s vlastním **název**.

... přispívajících/rst/tabulky:

Tabulky
======

Seznamy tabulek
-----------

Seznamy tabulek používají dvojitý seznam bodů, který převádí data na tabulku. První úroveň představuje
řádky a druhý stupeň představují sloupce.

.. seznam tabulkový::
:třída:o-vystaveni

   * — tabulka seznamu
:hlavičkové řádky: 1
:sloupky: 1

          * - Jméno
            - Země
            - Nejoblíbenější barva
          * Raúl
            - Černá Hora
            - Fialová
          * Melanie
            - Francie
            - Červená

   * 

... seznam tabulek::
:hlavičkové řádky: 1
:příčky: 1

             * - Jméno
               - Země
               - Nejoblíbenější barva
             * Raúl
               - Černá Hora
               - Fialová
             * Melanie
               - Francie
               - Tyrkys

Síťové tabulky
-----------

Síťové tabulky reprezentují vykreslenou tabulku a jsou snadnější na práci s vizuálními prvky.

.. seznam tabulkový::
:třída:o-vystaveni

   * - +-----------------------+--------------+---------------+
|                          |Trička       |Tílka       |
       +=======================+==============+===============+
|  Dostupné barvy  | Fialová      | Zelená
       |                       +--------------+---------------+
|                       | Tyrkysová   | Oranžová     |
       +-----------------------+--------------+---------------+
|  Délka rukávů       |Dlouhé rukávy|Krátké rukávy
       +-----------------------+--------------+---------------+

   * 

          +-----------------------+--------------+---------------+
|                          |Trička       |Tílka        |
          +=======================+==============+===============+
|  Dostupné barvy  | Fialová      | Zelená        |
          |                       +--------------+---------------+
|                       |Tyrkysová  |Oranžová     |
          +-----------------------+--------------+---------------+
|  Délka rukávů       | Dlouhé rukávy | Krátké rukávy |
          +-----------------------+--------------+---------------+

..tip:
   - Pro definování hlavičkových řádků použijte „=“ místo „-“.
   - Odeberte oddělovače „-“ a „|“, abyste spojili buňky.
   - Využijte „tento pohodlný generátor tabulek <https://www.tablesgenerator.com/text_tables>“
Vytvořte tabulky a pak do svého dokumentu vložte formátování, které jste vygenerovali.

... přispívání/rst/kódové bloky:

Bloky kódu
===========

Použijte příkaz „kódový blok“, abyste ukázali příklad kódu. Uveďte jazyk (např. Python, XML atd.).
formátovat kód podle pravidel syntaxe daného jazyka.

.. seznam tabulkový::
:třída:o-vystaveni

   * 

def main():
print("Ahoj svět!")

   * 

... kódový blok: Python

def main():
print("Ahoj světe!")

... přispívajících/rst/spoilery:

Spoilery
========

.. seznam tabulkový::
:třída:o-vystaveni

   * – … spoiler: odpověď na ultimativní otázku života, vesmíru a všeho

          **42**

   * 

...... spoiler:: Odpověď na ultimativní otázku života, vesmíru a všeho

             **42**

... přispívajících/rst/tabulky:

Obsahové záložky
============

.. varování:
Značky „tabulátor“ nemusí fungovat v některých situacích. Zejména:

   - Hlavičky záložek nelze přeložit.
   - Tabulka nemůže obsahovat hlavičky:ref:`<contributing/rst/headings>`.
   - :ref:`Varovný blok <contributing/rst/alert-blocks>` nesmí obsahovat tabulátory.
   - Tabulka nemůže obsahovat vlastní záložky:ref:`<contributing/rst/custom-anchors>“.

... přispívání/rst/základní-tabulky:

Základní záložky
----------

Základní záložky jsou užitečné pro rozdělení obsahu do několika možností. Záložka je označována
definovat sekvence záložek. Každá záložka je poté definována značkou „tab“ následovanou štítkem.

.. seznam tabulkový::
:třída:o-vystaveni

   * 

.. tab::Odoo online

Obsah určený pro uživatele aplikace Odoo Online.

.. tab:: Odoo.sh

Alternativa pro uživatele Odoo.sh.

.. tab:: Na místě

Třetí verze pro uživatele on-premises.

   * 

.. záložky::

.. tab::Odoo Online

Obsah určený pro uživatele Odoo Online.

.. tab::Odoo.sh

Alternativa pro uživatele Odoo.sh.

.. tab::Na vlastním serveru

Třetí verze pro uživatele on-premises.

... přispívajícím/rst/vloženým záložkám:

Vnořené záložky
-----------

Karty se mohou vkládat dovnitř jedna druhou.

.. seznam tabulkový::
:třída:o-vystaveni

   * 

.. tab:: Hvězdy

.. tabulky::

.. tab:: Slunce

Nejbližší hvězda k nám.

....... tab::Proxima Centauri

Druhá nejblíže ležící hvězda.

.. tab::Polaris

Severní hvězda.

... tab::Měsíce

.. tabulky::

... tab: Měsíc

Obíhá kolem Země.

.. tab::Titán

Obíhá kolem Jupitera.

   * 

.. záložky::

.. tab:: Hvězdy

.. tabulky::

.. tab: Slunce

Nejbližší hvězda k nám.

.. tab::Proxima Centauri

Druhá nejblíže ležící hvězda.

.. tab::Polaris

Severní hvězda.

.. tab::Měsíce

.. tabulky::

.. tab: Měsíc

Obíhá kolem Země.

.. tab::Titán

Obíhá kolem Jupitera.

... přispívání/rst/skupinové záložky:

Skupinové záložky
----------

Skupinové záložky jsou speciální záložky, které se synchronizují na základě skupinového štítku. Poslední vybraná skupina je
pamatují se a automaticky vybírají, když uživatel navštíví stránku znovu nebo jinou stránku s
skupina záložek. Značka pro definici skupiny záložek je „group-tabs“.

.. seznam tabulkový::
:třída:o-vystaveni

   * 

.. skupina tabulky: C++

C++

... skupina-tabulka:: Python

Python

.. skupina-tabulka:: Java

Java

.. záložky::

.. skupina tabulky: C++

... kódový blok: C++

int main(int argc, char **argv) {
návratová hodnota je 0.
                }

... skupina-tabulka:: Python

... kódový blok:: python

def main():
vrací se

.. skupina-tabulka:: Java

... kódový blok: java

class Main {
public static void main(String[] args) { }
                }

   * 

.. záložky::

.. skupina-tab:: C++

C++

.. skupina-tab:: Python

Python

... skupina-tab:: Java

Java

.. záložky::

.. skupina-tab:: C++

... kódový blok: C++

int hlavní (int argc, char **argv) {
return 0;
                   }

.. skupina-tab:: Python

... kódový blok:: python

def main():
vrácení

... skupina-tab:: Java

... kódový blok:: java

class Main {
public static void main(String[] args) { }
                   }

... přispívání/RST/kód:

Kódové záložky
---------

Použijte značku „kódové záložky“ k vytvoření záložek s kódem, které jsou ve skutečnosti skupinovými záložkami
<přispívající/rst/skupinové záložky>“, které považují obsah záložek za :ref:`kódový blok
<přispívající/rst/kódové bloky>. Zadejte jazyk, podle kterého se má kód formátovat.
syntaktická pravidla platí. Pokud je nastaveno označení, používá se pro seskupování záložek místo názvu jazyka.

.. seznam tabulkový::
:třída:o-vystaveni

   * 

.. kódový blok:: c++ Ahoj C++

             ##include <iostream>

int hlavní(void)
std::cout << "Ahoj, svět!";
return 0;
             }

... kódová tabulka:: python  Hallo, Python

print("Ahoj, svět!")

... kódový záhlaví:: JavaScript Hello JavaScript

console.log("Ahoj, světě!");

   * 

.. záložky::

... kódová tabulka: C++ Zdravím C++

                ##include <iostream>

int main(void)
std::cout << "Ahoj, světě!";
návratová hodnota je 0.
                }

... kódový blok:: python Hello Python

tiskne „Hello World“

.. kódový blok:: javascript  Hello JavaScript

console.log("Ahoj světe");

... přispívajících k rst/kartám:

Karty
=====

.. seznam tabulkový::
:třída:o-vystaveni

   * – karty::

.. karta: Dokumentace
:target: /dokumentace
:tag: Návod krok za krokem
:velké:

Tento průvodce vám poskytne nástroje a znalosti, které potřebujete k psaní dokumentace.

.. karta: Pravidla obsahu
:target: obsahové zásady

Seznam doporučení, tipů a triků, které vám pomohou vytvořit jasný a účinný obsah.

.. karta: Doporučení RST
:target: rst_guidelines

Seznam technických pokynů, které je třeba dodržovat při psaní v reStrukturovaném textu.

   * 

... karty::

.. karta:: Dokumentace
:target: /dokumentace
:tag: Návod krok za krokem
:velké:

Použijte tento průvodce k získání nástrojů a znalostí, které potřebujete k psaní dokumentace.

.. karta: Pravidla obsahu
:target: pravidla obsahu

Seznam rad a tipů, které vám pomohou vytvořit jasný a účinný obsah.

.. karta: Doporučení RST
:cíl: rst_guidelines

Seznam technických pokynů, které je třeba dodržovat při psaní s reStructuredTextem.

... přispívajících/rst/dokumentace-metadat:

Metadatový záznam
=================

„Sfinga“ <https://cs.wikipedia.org/wiki/Sphinx_(dokumentační_generátor)> podporuje dokumenty
metadatové značky, které specifikují chování celé stránky. Musí být umístěny mezi závorkami
(:) na začátku zdrojového souboru.

+-----------------+--------------------------------------------------------------------------------+
|Metadatová data|Účel                                                                                     |
+-----------------+--------------------------------------------------------------------------------+
| Zobrazit obsah stránky | Umožnit přístup k navigačnímu menu ze stránky s obsahem.
+-----------------+--------------------------------------------------------------------------------+
|`zobrazit obsah`|Zobrazení obsahu na stránce, která obsahuje metadatový prvek `zobrazit obsah`|
|                   |  značky.                                                                            |
+-----------------+--------------------------------------------------------------------------------+
|hide-page-toc|Skrýt boční panel „Na této stránce“ a využít celou šířku stránky pro obsah.
+-----------------+--------------------------------------------------------------------------------+
|„nezobrazovat“   |Vyřadit dokument z výsledků vyhledávání.
+-----------------+--------------------------------------------------------------------------------+
|„sirotek“       | Zastavit potřebu zahrnout dokument do tocové struktury.
+-----------------+--------------------------------------------------------------------------------+
|„sloupec kódu“| |Zobrazte dynamický sloupec na pravé straně, který můžete použít k zobrazení interaktivních informací.
|                   |     návody nebo kódové vzorky.                                                      |
|                   |  | Například viz                                                                     |
|                   |    :dokumentace: /aplikace/finance/účetnictví/začínáme/kartička.                     |
+-----------------+--------------------------------------------------------------------------------+
|`vlastní styl CSS`   |Odkaz na soubory CSS (oddělené čárkou).                                            |
+-----------------+--------------------------------------------------------------------------------+
|`custom-js`      |Odkaz na soubory JavaScriptu (oddělené čárkou).                                         |
+-----------------+--------------------------------------------------------------------------------+
|třídy|Přiřadit zadané třídy k prvku „<main/>“ souboru.
+-----------------+--------------------------------------------------------------------------------+

..._přispívání/rst/formátovací tipy:

Formátovací tipy
===============

... přispívání/rst/řádkové oddělení:

Rozbijte řádek, ale ne odstavce.
------------------------------------

.. seznam tabulkový::
:třída:o-vystaveni

   * – | První dlouhá čára, kterou rozdělíte na dvě
-> zde <- se zobrazí jako jedna řádka.
|Druhá řádka, která následuje po řádku přerušení.

   * 

|První dlouhá řádka, kterou rozdělíte na dvě
-> zde <- se zobrazí jako jedna řádka.
|Druhá řada, která následuje po řádku.

... přispívajících / rst / uprchlých:

Uprchlické značky
---------------------

Znaky značek s únikovým znakem (zpravidla zpětné lomítko) (\) se zobrazují normálně. Například:
Textová řádka s „značkami“ se zobrazí jako „Tato textová řádka s
„symboly značek“.

Když jde o závorky na pozadí ( ` `` ), které se používají v mnoha případech, jako například u odkazů na externí zdroje:ref:
<přispívající/rst/externí_odkazy>, používání zadávání zpětného lomítka k úniku není již
možností, protože závorky vnějších uvozovek vykládají zavináče a tím jim brání.
uniknutí vnitřních závorek zpětného lomítka. Například „\`tohle formátování\`“
„Chyba neznámého uzlu“ (title_reference). Namísto toho by mělo být použito „tohle formátování“.
vytvoří následující výsledek: „formátování“.

.. viz též:
„Dokumentace Docutils k reStrukturovanému textu a rolím
<https://docutils.sourceforge.io/docs/ref/rst/directives.html>
