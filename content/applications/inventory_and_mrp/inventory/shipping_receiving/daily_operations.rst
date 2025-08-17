Zobrazit obsah
:skrýt obsah stránky:

==========================
Příchozí a odchozí proudy
==========================

Konfigurace příchozích a odchozích toků v Odoo je klíčová pro optimalizaci efektivity, sledovatelnosti a
náklady. Skladníci musí vyvážit rychlost a kontrolu a zvolit mezi procesem s co nejmenšími náklady nebo
Přidali kontrolní stanoviště.

Odoo nabízí jednokrokové, dvoukrokové a tříkrokové průchody, s více kroky poskytující větší kontrolu.
zvýšení výroby. Nejlepší konfigurace závisí na kvalitě kontrol, balení a velikosti skladu.

Tento průvodce pomáhá firmám zjistit, jaké konfigurace jsou pro ně nejvhodnější.

Plynulý proces
=============

Jednokrokový způsob skladování je nejjednodušší možností s minimálním počtem manipulačních kroků a nejmenším
sledovatelnost. V tomto nastavení se produkty přesouvají přímo od dodavatelů do skladu nebo z
zákazníci, a pouze sledováním vstupu nebo výstupu zboží ze skladu. To dělá z
podniky s vysokým objemem a nízkou rizikovostí produktů nebo s rychlými obchody, kde je navíc nutná další validační
kroků není třeba.

- Příjem: Zboží jde přímo do skladu.
- Dodání: Produkty jsou zasílány přímo z skladu.
- **Nejlepší pro**: Malé sklady, nízká úroveň zásob a nezkažené zboží, kde je minimální
Před uložením nebo odesláním výrobků je nutné provést zpracování.

.. viz též:
:doc:`denní operace/přijetí zásilky v jednom kroku“

Dvoufázový proud
=============

Dvoufázový proces přidává oblast vstupu nebo výstupu pro zpracování produktů před uskladněním nebo odesláním.
Při příjmu zboží lze vybalit a prohlédnout před uskladněním, zatímco při odesílání se balíky třídí a
soustředěné před odesláním. Toto uspořádání zvyšuje efektivitu tím, že přiřazuje skladovým týmům úkoly na vyzvednutí
a ponožky, zatímco specializované týmy se starají o vybalení, případně balení a konečnou kontrolu.
snížit počet chyb při vyřizování objednávek.

- Příjem: Produkty jsou přesunuty do oblasti příjmu předtím, než budou uloženy na sklad.

  - Před převedením nejsou získané produkty automaticky vyhrazeny pro výrobu, dodání.
nebo jiné operace.

- Přeprava: Produkty jsou převedeny do výstupu před odesláním, aby bylo možné provést třídění nebo
konzolidaci metod vybírání.
- Nejlepší pro: Velké sklady, vysoké zásoby, objemné předměty a procesy oddělené
přijímání z úložiště, aby se zlepšila organizace a efektivita.

.. viz též:
:doc:`denní operace/přijetí zásilky ve dvou krocích“

Třístupňový model
===============

Třístupňový proces je založen na dvoustupňovém procesu přidáním kontroly kvality a obalového prostoru.
přísnější procesy a zlepšení dohledu.

.. důležité::
Toto uspořádání zvyšuje kontrolu procesů, ale oddělení balení a vyskladňování vyžaduje ověření.
každý krok. Pokud stejná osoba řeší obojí, může se jednat o zbytečnost a zpomalování procesu.

Kontrola kvality a balení nevyžadují třístupňový proud. Povolte:doc:`kontrolní body kvality
<../kvalita/kvalitní řízení/kontrolní body kvality> zvlášť nebo aktivovat
:ref:`Balíčky <inventar/sklady/balicek> v Odoo pro přidání
Tyto procesy bez přidání dalších kroků přenosu.

- Příjem zboží probíhá podle strukturovaného procesu: *příjmový prostor* → *kontrola kvality* → *sklad*.
- Dodání: Produkty jsou vybrány, zabaleny a následně odeslány, což zajišťuje správné zacházení s nimi.
organizace.
- Nejlepší pro: velké sklady s přísnými požadavky na kvalitu a oddělené skladování
a pracovní postupy balení a potřeba jasné sledovatelnosti v různých fázích manipulace. Vhodný
při tom, když se na různých krocích podílí více týmů předtím, než jsou produkty skladovány nebo odesílány.

.. viz též:
   - :doc:`denní operace/příjmy tři kroky“
   - :doc:`denní operace/doručení v třech krocích“

Doplňky
=======

Odoo nabízí další funkce, které mohou procesy zlepšit.

Skladování
-------

Pro efektivní uspořádání a skladování produktů použijte:

.. karty:

...... karta: Pravidla pro ukládání
:target: denní operace/skladování

Nastavte předem definovaná pravidla pro umístění produktů do konkrétních skladových prostor

...... karta::Kategorie ukládání
:target: denní operace/kategorie skladování

Nastavte limity položek nebo hmotnosti, abyste zabránili přebytku zásob a zajistili správné
organizace

......karta::Dodání
:target: denní operace / vlastní zásoby

Sledovat produkty vlastněné třetími stranami

Dodání
--------

Upravte proces odesílání tak, aby vyhovoval potřebám podniku. Zvolte způsob skladování a odstranění
Strategie řídí způsob rezervace produktů pro objednávky a křížové skladování a dodavatelství.
určit, jak se pohybují. Konfigurace těchto možností v Odoo zajišťuje viditelnost pohybu produktů
a potvrzuje, že zboží dorazí zákazníkům včas.

.. karty:

......karta: Křížové skladování
:target: denní operace/křížové skladování

Přijímat zboží a okamžitě jej přesouvat do dalšího skladu bez jeho uskladnění

...... karta::Dropshipping
:target: denní operace / přeposílání

Koordinujte dodavatele, aby doručili objednávky přímo zákazníkům a obešli vlastní zásoby

......karta: Vybírání metod
:target: metody sběru

Optimalizujte operace vybírání pomocí metod sestavení, skupin nebo vln

......karta: Strategie odstranění
:target: odstranění strategií

Použijte strategii FIFO, LIFO nebo FEFO k automatizaci výběru produktů pro dodání

Zpracování na míru
-------------

Odoo nabízí flexibilní rámec, který umožňuje přizpůsobit pracovní postupy konkrétním provozním potřebám.
potřeby.

.. karty:

...... karta: Vlastní trasy
:target: denní operace / používání tras

Definujte přizpůsobené procesy pro příjem nebo dodání, které splní specifické podnikatelské potřeby

..toctree::


denní provoz/použití tras
denní operace/přijetí zásilky v jednom kroku
denní operace/přijetí zásilek ve dvou krocích
daily_operations/příjmy_tři_kroky
denní operace / dodání ve třech krocích
denní operace / skladování
daily_operations/kategorie-skladu
denní operace/křížové sklady
denní provoz/skladové prostory
denní operace / vlastní zásoby
denní operace/dodání na sklad
