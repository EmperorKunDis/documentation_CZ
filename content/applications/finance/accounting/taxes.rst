Zobrazit obsah

=====
Daně
=====

Daňových typů je mnoho a jejich aplikace se značně liší, především podle
lokalizaci vaší společnosti. Chcete-li zajistit jejich přesnost, Odoo má daňový motor
podporuje všechny typy použití a výpočtů.

... daňové povinnosti/vymáhání dluhu:

Daň z přidané hodnoty
=============

Výchozí daně definují, které daně jsou automaticky vybrány při vytváření nového produktu.
jsou také používány k předvyplnění pole „Dani“ při přidávání nové řádky na faktuře v
Režim „Účetní firmy a správci“.

.. obrázek: daně/výchozí konfigurace.png
:alt:Odoo automaticky vyplní pole DPH podle výchozích daní

Chcete-li změnit výchozí daně, přejděte do sekce „Účetnictví“ -> „Konfigurace“ -> „Nastavení“.
--> Daně --> Výchozí daně“, vyberte příslušné daně pro výchozí daň z prodeje a nákupu
a klikněte na „Uložit“.

.. obrázek: daně/výchozí_daně.png
:alt:Definujte, které daně se mají používat v Odoo výchozím nastavením

.. poznámka::
Výchozí daně jsou automaticky nastaveny podle zvolené země při vytváření
vaši databázi nebo když nastavíte balíček pro daňovou lokalizaci
pro vaši společnost.

... daňové přiznání / aktivace seznamu:

Aktivujte DPH z pohledu seznamu
=======================================

Jako součást vašeho balíčku pro daňovou lokalizaci (fiscal_localizations/packages) je většina vašich
Daňové sazby země jsou již přednastaveny ve vaší databázi. Nicméně pouze několik daní je
aktivní výchozí nastavením. Chcete-li aktivovat daně relevantní pro vaši firmu, přejděte na:
--> Konfigurace --> DPH a zapněte přepínač pod sloupcem „Aktivní“.

.. obrázek: daně/seznam.png
:alt:Aktivujte přednastavené daně v účetním systému Odoo

... daně/konfigurace:

Konfigurace
=============

Chcete-li upravit nebo vytvořit **daň**, přejděte na :menuselection:`Účetnictví --> Konfigurace --> Daně` a otevřete
dani nebo klikněte na „Nový“.

.. obrázek: daně/edit.png
:alt:Účetní úprava daně v Odoo

Základní možnosti
-------------

.. daně/název:

Daňové označení
~~~~~~~~

Pro uživatele v administraci je zobrazeno pole „DANĚ“ s hodnotou **název daně**.
objednávky na prodej (sales order), faktury (customer invoices), formuláře produktů atd.

... daňové výpočty:

Daňová výpočet
~~~~~~~~~~~~~~~

- **Skupina daní**

Daň je kombinací několika poddaní. Můžete přidat kolik daní chcete, v
pořadí, ve kterém chcete, aby byly aplikovány.

.. důležité::
Zkontrolujte, zda je daňová posloupnost správná, protože pořadí, v jakém jsou uvedeny, může ovlivnit
výpočet výše daní, zejména pokud je jednou z daní daň, která se vztahuje na základ
dalšími daněmi (<taxes/base-subsequent>).

- **Opraveno**

Daň má pevnou částku v základní měně. Částka zůstává stejná bez ohledu na
cena prodeje.

.. příklad::
Pokud má produkt prodejní cenu 1000 USD, aplikujeme na něj daň ve výši 10 USD za jednotku. Výsledkem je:

   +-------------+-------------+----------+----------+
|Produkt      |Cena         |DPH        |Celkem     |
|prodejní cena|bez DPH|          |          |
   +=============+=============+==========+==========+
   | 1,000       | 1,000       | 10       | 1,010.00 |
   +-------------+-------------+----------+----------+

- Procento ceny

Pro účely daně z přidané hodnoty je základní sazbou pro výpočet daně cena prodeje, tedy částka, kterou prodávající obdrží od kupujícího.
podle procenta daně.

.. příklad::
Produkt má prodejní cenu 1000 USD a aplikujeme daň ve výši 10 % z ceny. Výsledek je:

   +-------------+-------------+----------+----------+
|Produkt      |Cena         |DPH        |Celkem     |
|prodejní cena|bez DPH|          |          |
   +=============+=============+==========+==========+
   | 1,000       | 1,000       | 100      | 1,100.00 |
   +-------------+-------------+----------+----------+

- *Sazba DPH zahrnutá v ceně*

Celkový součet je základ daně, daňová částka je procento z celku.

.. příklad::
Produkt má prodejní cenu 1000 dolarů a aplikujeme daň ve výši 10 % včetně DPH. Poté
mít:

   +-------------+-------------+----------+----------+
|Produkt      |Cena         |DPH        |Celkem     |
|prodejní cena|bez DPH|          |          |
   +=============+=============+==========+==========+
   | 1,000       | 1,000       | 111.11   | 1,111.11 |
   +-------------+-------------+----------+----------+

- **Kód v Pythonu**

Daň definovaná jako **Python kód** se skládá ze dvou kousků Pythonového kódu, které jsou spuštěny
lokální prostředí obsahující data jako je jednotková cena, produkt nebo partner.

Daň se vztahuje na příjem z prodeje. Vzorec je uvedený na konci záložky „Definice“.

.. příklad::
:guilabel:`Python kód“: „Výsledek = cena za jednotku * 0,10“
:guilabel:`Aplikovatelný kód“: „Výsledek je pravdivý“

... daně/aktivní:

Aktivní
~~~~~~

Pouze aktivní daně lze přidat do nových dokumentů.

.. důležité::
Nelze smazat již použitou daňovou položku. Místo toho můžete deaktivovat
aby se zabránilo dalšímu použití.

.. poznámka::
Tento údaj lze upravit v seznamovém pohledu na danou položku.

... daňové sazby/rozsah:

Druh daně
~~~~~~~~

Značka :guilabel:`Tax Type` určuje způsob aplikace daně, který také omezuje její zobrazení.

- Prodej: Faktury zákazníkům, daně z přidané hodnoty na výrobky pro zákazníky atd.
- Nákup: Faktury dodavatelů, daně z přidané hodnoty apod.
- **Žádný**

.. tip::
Můžete použít :guilabel:`None`, pokud chcete zahrnout daně do skupiny daní.
<daň z přidané hodnoty/výpočet> a že nechcete uvádět spolu s dalšími daněmi z prodeje nebo nákupu.

Daňový rozsah
~~~~~~~~~

Značka „Dotaz na daň“ omezuje použití daně na určitý druh produktu, buď na zboží nebo
**služby**.

...daně/definice-tabulka:

Tabulka definic
--------------

Přesně určete částku základu daně nebo procenta vypočítané daně.
více účtů a daňových sítí.

.. obrázek: daně/definice.png
:alt:Přidělování daňových částek na správná účetní období a daňové sítě

- **Založeno na**:

  - :guilabel:`Základní cena“: Cena na faktuře
  - :guilabel:`% daně“: procento z vypočtené daně.

- **Účet**: pokud je definován, je zaznamenána další položka účetního záznamu.
- **Daňové sazebníky**: používané k vytvoření zprávy o dani.
automaticky podle pravidel vaší země.

...daně/pokročilé-tabulky:

Pokročilé nastavení
--------------------

...dani/štítek faktury:

Štítek na fakturách
~~~~~~~~~~~~~~~~~

Daňový štítek je zobrazen na každé řádku faktury v sloupci „Dani“. Tento je viditelný
uživatelé v přední části (front-end) na vývozních fakturách, v zákaznických portálech atd.

.. obrázek: daně/faktura-štítek.png
:alt:Na faktuře se zobrazuje název položky na každé řádce

...daně/daňová skupina:

Daňová skupina
~~~~~~~~~

Vyberte, do které skupiny daní patří daň. Název skupiny daní se zobrazuje nad
*celková* částka na fakturách a v zákaznických portálech.

Daňové skupiny obsahují různé varianty stejné daně. To může být užitečné, pokud musíte zaznamenat
stejný daňový poplatky se liší podle: doc: `daňové pozice <daně/daňová_položka>“.

.. příklad::

.. obrázek: daně/faktura-dane.png
:alt:Název skupiny daně je odlišný od názvu na fakturách

V příkladu výše je zaznamenána daň 0 % EU S pro zákazníky v rámci Evropské unie.
výši na konkrétních účtech a v daňových sítích. Zůstává však nulová daň pro zákazníka.
Proto je na etiketě uvedeno „0 % EU S“ a nad skupinou daní je napsáno
:guilabel:`Celkem“ ukazuje na „DPH 0 %“.

.. důležité::
Daň má tři různé štítky, každý má svou specifickou funkci. Podívejte se na následující tabulku
aby viděli, kde jsou zobrazeny.

   +------------------+-------------------------+-------------------------+
| :ref:`Název daně  | :ref:`Štítek na faktuře  | :ref:`Daňová skupina      |
| <daně/název>`     | <daně/etiketa faktury>`  | <daně/soubor daní>`      |
   +==================+=========================+=========================+
|Zadní část         |:guilabel:`Dani“ sloupec|nad                      |
|                   | na vývozních fakturách | :guilabel:`Celkem“ řádku |
|                  |                         | na vývozních fakturách   |
   +------------------+-------------------------+-------------------------+

.. daně/analytické náklady:

Zahrnout do analytické ceny
~~~~~~~~~~~~~~~~~~~~~~~~

Pokud je tato možnost aktivní, daň bude přiřazena na stejný analytický účet jako
účetní položka.

.. daň z přidané hodnoty/cena obsahuje DPH:

Zahrnuto v ceně
~~~~~~~~~~~~~~~~~

Pokud je tato možnost aktivní, celková částka (včetně daně) odpovídá **prodejní ceně**.

„Celková cena = prodejní cena = počítaná cena bez DPH + DPH“

.. příklad::
Produkt má prodejní cenu 1000 $, aplikujeme daň ve výši 10 % z ceny, která je „zahrnuta v ceně“.
cena* a pak máme:

   +-------------+-------------+----------+----------+
|Produkt      |Cena         |DPH        |Celkem     |
|prodejní cena|bez DPH|          |          |
   +=============+=============+==========+==========+
   | 1,000       | 900.10      | 90.9     | 1,000.00 |
   +-------------+-------------+----------+----------+

.. poznámka::
Pokud potřebujete přesně definovat ceny včetně i bez DPH, prosím, obraťte se na
následující dokumentaci: :doc:`dane/B2B_B2C`.

.. poznámka::
Výchozí nastavení zobrazuje pouze sloupec „Daň nezahrnuta“. Chcete-li zobrazit sloupec „Daň zahrnuta“,
:guilabel:`Daň je zahrnuta“ sloupec, klikněte na tlačítko „výběr“, a poté vyberte
:guilabel:`DPH zahrnuto“.

.... obrázek: daně/tlačítko-přepínače.png

.. daně/základ-násl.

Základ pro odvod dalších daní
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

S touto možností se celkový daň zahrnutý stává základem daně pro ostatní daně aplikované na
stejný produkt.

Můžete vytvořit novou skupinu daní, do které tento daňový poplatky zahrnete nebo přidáte
přesně na produktovou řadu.

.. obrázek: daně/další-řádek.png
:alt:Ekologický daňový příplatek je započítán do základu DPH ve výši 21 %

.. varování:
Přiřazení daní na produktové řadě nemá vliv na výpočet částek.
Pokud se daně přičítají přímo na produktové řady, určuje pořadí pouze pořadí daňových sazeb.
Protože jsou aplikovány,

Chcete-li změnit pořadí položek, přejděte na :menuselection:`Účetnictví --> Konfigurace --> Daně“ a přetáhněte
a vypustit řádky s uchy, vedle jmen daní.

.. obrázek: daně/seznam-sledování.png
:alt: Sekvence daní v Odoo určuje, která daň se použije jako první

Další daně
===========

„Příplatek“ je obecný pojem, který označuje další daně nad rámec základních nebo běžných daní.
zavedené vládami. Tyto další daně mohou být daň z luxusu, daň za životní prostředí,
cla nebo clo) a podobně.

.. poznámka::
Metoda výpočtu těchto daní se v různých zemích liší. Doporučujeme konzultovat s
Zákony dané země, abyste pochopili, jak je pro vaši firmu vypočítat.

Pro výpočet dodatečné daně v Odoo je potřeba vytvořit daň :ref:`<taxes/configuration>`, zadat název daně, vybrat
A: „Výpočet daně“ (viz taxes/configuration), nastavte hodnotu a v
kartě „Pokročilé možnosti“, zaškrtněte políčko „Změnit základ daně pro následující daně“. Potom přetáhněte
snížit daně v pořadí, ve kterém by se měly počítat.

.. příklad::
   - V Belgii je vzorec pro výpočet ekologické daně následující: (cena produktu + ekologická daň).
daně z přidané hodnoty. Proto musí být naše ekologická daň zařazena před DPH.
výpočetní sekvenci.
   - V našem případě jsme vytvořili daň z životního prostředí ve výši 5 % (Ecotax) a umístili ji před belgickou základnu.
daň ve výši 21 %.

.. obrázek: daně/ekotaxa.png
:alt: Sekvence ekologických daní v Belgii.

.. viz též:
  - :doc:`dane/daňové pozice“
  - :doc:`dane/b2b-b2c“
  - :doc:`reporting/daňové přiznání“

..toctree::


daně/účetní metoda
daně/zadržování
dane/dph
daně/daňové pozice
daně/avatax
daně/EU-distanční prodej
daně/B2B_B2C
