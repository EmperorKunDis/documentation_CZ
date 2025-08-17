============================
Typy operací a příkazy
============================

Inventarizační operace, např. příjemky a dodací listy
<../../inventar/Versand und Wareneingang/Tägliche Vorgänge/Eingangsrechnungen ein Schritt>, sowie
příkazy, jako je ověření převodu nebo balení produktů do obalů, lze provést skenováním
čárové kódy prostřednictvím aplikace Barcode. To umožňuje zaměstnancům zpracovávat úkoly a přistupovat ke menu bez
potřeba dotknout se obrazovky nebo použít aplikaci Inventář na počítači, což umožňuje práci v procesu
Zefektivněním tím, že se kódy operací umístí na správné fyzické místo.

.. obrázek:: operation_types/barcode-default-operations.png
:alt:Tisknutelné čárové kódy pro faktury, dodací listy a výrobní podklady.

... inventář/čárový kód/konfigurovat operace:

Konfigurace operací
======================

V aplikacích Inventář a Čárový kód jsou definovány operace, které změní
Stav skladových zásob. Jaké typy operací lze tisknout, bude záviset na
nastavení databáze. Výchozím nastavením je možnost tisku čárových kódů pro účtenky (WHIN) a dodací listy.
Objednávky (bez *) a výroba (s *). Vnitřní přesuny (bez *) a vyzvednutí (s *).
mohou být povoleny i operace.

.. poznámka::
Obě operace *Interní převody (WHINT)* a *Vybrání (WHPICK)* vyžadují :doc:`čárový kód místa
a následně je skenovat.

Vnitřní přesuny
------------------

Kód čárového kódu pro vnitřní převody (WHINT) je dostupný, pokud databáze používá
*Místo skladování* pro označení, kde se produkty nacházejí v zásobách. Chcete-li tuto funkci aktivovat
Nastavení, přejděte na: „Aplikace Inventář --> Konfigurace --> Nastavení“, pak
V sekci „Sklad“ zaškrtněte možnost „Sklady“.

Pletí
-------

Operační kód čárového kódu Pick (WHPICK) je k dispozici, pokud databáze používá vícefázové trasy.
funkci s nastavením kroku vyzvednutí. Chcete-li tuto funkci aktivovat, přejděte na:
Konfigurace -> Nastavení“, pak v sekci „Sklad“ zaškrtněte
Vyberte možnost „Složené trasy“ a uložte. Pak klikněte na ikonu „Pokračovat“.
:guilabel:`Nastavení skladu“ otevřete nastavení skladu a vyberte sklad.
V části „Odeslané zásilky“ vyberte buď možnost „Zvolit a dodat (dva kroky)“, nebo
:guilabel:`Vybrat, zabalit a dodat (3 kroky).“

.. viz též:
   - Dvoufázové přijetí a dodání

   - Třífázová dodávka


Tiskněte čárové kódy pro příkazy a operace skladování
====================================================

Kódy pro operace a příkazy lze vytisknout kdykoliv. Tyto dokumenty budou obsahovat všechny
k dispozici jsou příkazy skladu, ať už jsou povoleny nebo zakázány, ale pouze operace
které jsou v současné době povoleny v databázi. Podívejte se na: Konfigurace operací
<Inventar/Barcode/Konfigurovat operace> a povolit chybějící operace.

.. příklad::
Dokument „Tisk inventárních příkazů a typů operací“ bude vždy zobrazovat
:guilabel:`PŘIDAT DO BALENÍ“ příkazu, bez ohledu na to, zda je funkce „ZÁSOBY“ zapnutá nebo ne.
Operace Pick (WHPICK) bude přidána pouze tehdy, pokud jsou konfigurovány vícekrokové trasy.
krok sběru.

.. důležité::
Vytisknutí čárových kódů automaticky stáhne PDF soubor s vybranými čárovými kódy
nebo otevřít nové okno s stahovatelným nebo tisknutelným PDF. Chcete-li z něj vytvořit přímý tisk,
operace: „připojit tiskárnu <../../../obecné/IoT/zařízení/tiskárna>“.

Když jsme otevřeli první barcode
--------------------------

Když se otevře aplikace Barcode poprvé, je tam výzva s možnostmi tisku čárových kódů pro
příkazy a operace, stejně jako několik vzorků čárových kódů pro tisk a testování. Po klepnutí
Tyto odkazy jsou nejjednodušší cestou k tisku příkazových a operátorských čárových kódů, ale již nebudou.
ukázané po prvním kliknutí.

.. obrázek: operační typy/čárový kód - tisk první strany.png
:alt:Příkaz tisknout ukázkové datové řady nebo čárové kódy pro operace.

Z nastavení inventáře
-----------------------

Pokud není k dispozici tiskové okno s čárovým kódem pro vytváření zásob a typů operací, mohou být čárové kódy
vždy se tiskne z stránky „Nastavení“. Přejděte na: menu:inventarapp --> Konfigurace
→ Nastavení“ a v sekci „Čtečka čárových kódů“ pod položkou „Čtečka čárových kódů“,
Klikněte na ikonu tiskárny a zobrazí se příkazy pro tiskování štítků a operace.

.. obrázek: operační typy/tiskové operace a příkazy.png
:alt: Odkaz na tiskové příkazy a operace.

Individuální operace
---------------------

Kódy pro jednotlivé operace, jako jsou faktury a objednávky na výrobu, lze také vytisknout z
Nastavení typů operací. Chcete-li vybrat operace k tisku, přejděte na
:menu „Výběr inventáře“ -> „Konfigurace“ -> „Typy operací“ a zaškrtněte u každé položky.
operace typu vyžadována.

.. obrázek:operation_types/barcode-print-operations.png
:alt:Vybrané operace k dispozici, po jejichž provedení se objeví tlačítko "Tisk".

Dále klikněte na tlačítko „Tisk“ a vyberte buď „Operace“ nebo „Výstup“.
(PDF) ke stažení PDF s čárovými kódy operace nebo :guilabel:Operační typ (ZPL)
tiskovou objednávku odeslat na :ref:`zpl-enabled tiskárnu <iot/link-printer>`.

.. poznámka::
Tlačítko pro tisk se nezobrazí, dokud není alespoň jedna operace.
Je vybrán.

... inventární číslo, štítek, tiskové pořadí:

Operace tisku pro konkrétní objednávky
============================================

Pokladní doklady, výrobní objednávky, převody a dodací listy lze vytisknout předem.
v nabídce tisku označované jako „operace vybírání“ nebo „vybírání“.

Barcode
----------

V aplikaci Barcode klepněte na tlačítko Operace, zvolte typ operace a pak
konkrétní požadavek na tisk. Od té doby buď naskenujte čárový kód „TISKOVÁ OPERACE VYBÍRÁNÍ“, nebo
je k dispozici, nebo klepněte na ikonu „fa-cog“ a otevřete akce „Čárový kód“.
menu a klikněte na tlačítko „Tisk výběrové operace“.

.. obrázek:operation_types/print-picking-barcode-cog.png
:alt:Náhled menu z pokladního dokladu s tlačítkem "Tisk výdejky".

V soupisu
------------

Pro tisk výdejky z aplikace **Sklad** klepněte na příslušný typ operace (výdejka,
*Příkaz k dodání* atd.) a vyberte konkrétní objednávku nebo operaci.

Zaškrtněte políčko „Vyvolat akci“ a klikněte na ikonu „Nástroje“ (ikona tiskárny).
Vyberte tlačítko „Tisk“ a klikněte na „Operace tisku“.

.. poznámka::
Typ operace lze odvodit z referenčního čísla operace, aby se mohlo rozlišovat vybírání
operace. Například „IN“ v „WH/IN/00012“ znamená, že se jedná o příjem.
Tyto odkazují na, ale nejsou přesně stejné jako typy čárových kódů operace.

Používejte čárové kódy pro operace s inventářem a příkazy
==================================================

Operace
----------

- Faktura „WHIN“ vytváří novou objednávku pro přijetí produktů do zásob.

.. varování::
Při skenování čárového kódu pro účtenku vždy vytvoří nový instanci této operace a
Nebude se shodovat s již naplánovaným příjmem. Aby bylo možné skladovou položku nebo konkrétní plánovaný příjem naskenovat, je třeba nejprve
:ref:`vytisknout výdejku pro konkrétní doklad <sklad/čárový kód/tisk_objednávky>`.

Příkladem je skenování položky „Faktury“ s názvem WHIN, což vytvoří novou fakturu i když už existuje.
obsah odpovídá faktuře přesně.

- Pokyny k dodání bez otevřených objednávek na dodávky.
- Výrobní proces vytváří nové výrobní objednávky. Skenováním čárového kódu produktu
Tady ho přidáme do seznamu *Producenti*.
- **Vnitřní převody** `WHINT` vytváří nový příkaz k převodu. :doc:`Čárové kódy umístění <software>`
Může být skenován pro určení zdroje a cíle nebo směru k zahájení
převod v Barcode.
- **Pick** `WHPICK` vytvoří novou operaci vyskladnění. Tato operace bude vyžadovat :doc:`čárový kód místa
pro zdrojové umístění.

Příkazy
--------

- „HLAVNÍ MENU“: Skener se vrátí na hlavní menu z nastavení inventáře.
- `VALIDACE“: Skenování k ověření, že operace je správná a připravená ke spuštění.
- `ZRUŠIT“: Skenování operace, která zabrání jejímu ověření a nastaví stav
do stavu *Zrušeno*.
- „TISKOVÁ OPERACE VYBÍRÁNÍ“: Sken z již existujícího dodacího listu, převodu nebo příjmu k vytvoření
a PDF s názvem a čárovým kódem pro referenční číslo operace, které lze později naskenovat
přejít rovnou k operaci.
- `TISKNUTÍ DORUČOVACÍHO LISTU“: Změřte stávající fakturu nebo dodací list, abyste vytvořili soubor PDF.
objednávka nebo dodací list. Tento nebude obsahovat čárový kód.
- „VLOŽIT DO BALENÍ“: Po skenování produktů tato příkazová zkratka označí všechny produkty jako v balení.
:dokument: „<../../inventář/správa produktů/konfigurovat/balíček>“. Produkty skenované později
Pokud je znovu skenována příkazem „VLOŽIT DO BALENÍ“, jsou tyto příkazy umístěny do nové palety.
- `SCRAP`: Označte produkt jako poškozený a přesuňte ho do virtuální polohy.
:doc:`skladové zásoby <../../inventory/warehouses_storage/inventory_management/scrap_inventory>`

Tiskněte čárové kódy pro výrobní příkazy
=========================================

Výchozí operační typ Manufacturing může skenovat produkty a součásti a pak je
Tlačítko „Vyrobit“ pro jejich výrobu. Pro tisk čárových kódů pro základní výrobní operace přejděte na
Vyberte položku „Výroba“ -> „Konfigurace“ -> „Nastavení“, pak
V sekci „Operace“ ujistěte se, že je zaškrtnuté políčko „Čtečka čárových kódů“ a klikněte
:icon:`fa-print` :guilabel:`Tiskování štítků a operací“.

Příkazy k práci
-------------------

Pro větší možnosti řízení výrobního procesu prostřednictvím čárového kódu umožňuje
:doc:`Funkce „Náhradní díly“ <../../manufacturing/basic_setup/bill_configuration> s možností tisku čárových kódů
pro objednávky práce přejděte na: „Výroba -> Konfigurace -> Nastavení“, pak
v sekci „Provoz“, ujistěte se, že je zaškrtnutá políčka „Dodávky“ a klikněte
:icon:`fa-print` :guilabel:`Tiskovat štítky“.

.. obrázek:: types-of-operations/print-work-order-commands.png
:alt: „Tisk pokynů k čárovému kódu“ jako v sekci Nastavení výroby.

.. viz též:
   - „Tutoriály Odoo: Proces a zrušení faktur pomocí čárových kódů
<https://www.youtube.com/watch?v=6zBz93AIXBo>
   - „Tutoriály Odoo: Používání komponent pomocí čárových kódů
<https://www.youtube.com/watch?v=2ojxIbTq41Q>
