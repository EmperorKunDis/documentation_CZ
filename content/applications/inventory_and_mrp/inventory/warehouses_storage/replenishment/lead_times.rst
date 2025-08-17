==========
Doba dodání
==========

.. |MO| nahradit za: zkratka: `MO (manufacturing order)`
.. |MOs| nahradit za: zkratka: `MOs (manufacturing orders)`
.. |BoM| nahradit za: :abbr:`BoM (Seznam materiálů pro výrobu)“
.. |BoMs| nahradit za: :abbr:`BoMs (Seznamy materiálů)`
.. |RFQ| nahradit za: zkratku: RFQ (žádost o nabídku)
.. |PO| nahradit za: :abbr:`PO (objednávka na nákup)`

Přesné předpovídání termínů dodávek je zásadní pro splnění očekávání zákazníků. V Odoo
Aplikace „Sklad“ umožňuje komplexní konfiguraci dodacích lhůt, což umožňuje koordinaci a
plánování výrobních objednávek, dodávek a přijatých zásilek.

Druhy časových rezerv
===============

Různé časy dodání pro různé operace mohou ovlivnit různé fáze plnění objednávky
procesu. Tady je stručný přehled typů dodacích lhůt v Odoo:

.. obrázek: lead_times/all-lead-times.png
:alt:Zobrazit grafické znázornění všech časů odezvy pracujících společně.

- „Doba dodání zákazníkovi“: výchozí časový rámec pro
splnění objednávek zákazníků. Doba zpracování objednávky je počet dní od data, kdy byla objednávka
Potvrzení objednávky (SO) je potvrzeno k datu odeslání produktů z skladu.
známý jako „doba dodání“.

- „Doba dodání zboží (<inventory/warehouses_storage/sales-security-lt>)“:
*datum dodání* posunout o určitý počet dní. To slouží jako rezerva, která umožňuje
dostatek času na přípravu odchozí zásilky s ohledem na možnost zpoždění v
proces plnění objednávek.

- „Doba potřebná k nákupu <skladové zásoby/sklady a skladování/nákup-dny>: počet dní od
potvrzení objednávky o dodání zboží. Poskytuje informace o čase
jak dlouho trvá dodání produktů do skladu a umožňuje tak efektivní plánování a rozvrh
způsobené dodavateli.

- :ref:`Doba dodání <inventory/warehouses_storage/delivery-time>: předstih
předání objednávky na :abbr:`PO (Purchase Order)` o určitý počet dní dopředu. Toto předvídavé
předčasné objednávání snižuje riziko zpoždění dodavatele nebo dopravce.
produkty, které jsou nastaveny na doplňování dle objednávky, potřeba se objeví v hlášení o doplnění zásob.
dříve podle uvedeného počtu dní.

- Dny k nákupu <inventory/warehouses_storage/days-to-purchase>: dny potřebné pro nákup
dodavatel obdrží požadavek na nabídku (RFQ) a potvrdí jej. Přesune se termín o
Vypsat výběrové řízení do určitého počtu dnů.

- Doba zpracování (dny): čas potřebný k
dodržet termín dokončení výrobního příkazu (MO), který zahrnuje
v sobotu a neděli (mimo pracovní dobu v Odoo) a slouží k předpovědi přibližného data výroby.
hotový výrobek.

- Dny na přípravu výrobního objednávky
<Inventář/Skladové zásoby/Připravit výrobní objednávku>: počet dní potřebných k doplnění
součástky nebo sestavit podsestavy produktu. Buď je rovnou přičíst na fakturu
materiálů (BoM) nebo klikněte na tlačítko „Výpočet“, abyste získali informace o dodacích lhůtách komponent.
v BoM.

- „Doba dodání výrobku <skladování a sklady/dodací lhůta - výroba>: přesouvá
datum plánovaného termínu vpřed o určitý počet dní.
s replenishmentem na objednávku (<inventory/management/products/strategies>) a bezpečnostním časovým předstihem
Zvyšuje potřebu v předčasném období na výkazu doplňování zásob.

.. skladovací prostory, sklady, skladové zásoby, zákazník

Doba dodání
================

Doba dodání a časová rezerva prodeje lze nastavit tak, aby automaticky vypočítaly
Očekávaný termín dodání na SO (objednávka prodeje). Očekávaný termín dodání zajišťuje
realistické termíny dodání pro zásilky ze skladu.

Odoo vydá varovný e-mail, pokud je stanovený termín dodání dřívější než očekávaný, protože může
by nebylo možné objednávku dodržet do té doby, co by ovlivnilo další skladovací operace.

Příklad:
A:abbr.: SO (objednávka prodeje) obsahující vonnou svíčku „Kokosová“ je potvrzena dne 11. července.
Produkt má dobu dodání pro zákazníka 14 dnů a firma používá bezpečnostní časovou rezervu prodeje
1 den. Na základě vstupních údajů o dodacích lhůtách navrhuje Odoo datum doručení 15. července.

.. obrázek:: lead_times/plánovaný-termín.png
:alt:V objednávce nastavte datum dodání. Zapněte funkci termínu dodání.

Následující části ukazují, jak automaticky vypočítat očekávané dodací termíny.

Doba dodání pro zákazníky
------------------

Nastavte časový limit pro zpracování objednávky u každého produktu, přejděte na stránku s produkty a
:menu-vyber->Prodejní aplikace-->Produkty--> Produkt“.
Přepněte na záložku „Sklad“ a pod položkou „Doba dodání zákazníka“ vyplňte
v počtu kalendářních dnů potřebných k vyřízení objednávky od začátku do konce.

Příklad:
Nastavte dobu dodání pro zákazníky na 14 dnů u produktu „Vonná svíčka s kokosovou vůní“
Formulář a pak do položky „Doba trvání“ v záložce „Zákaznický lead“ zadejte 14 dní.
pole „Čas“.

.... obrázek:lead_times/customer.png
:alt:V poli produktu nastavte hodnotu *Doba dodání*.

.. skladové zásoby, sklady a způsob skladování, prodejní bezpečnost

Doba dodání
------------------------

Doba trvání prodejní bezpečnosti je nastavena celosvětově pro obchod v aplikaci „Sklad“ pod:
Konfigurace --> Nastavení.

V konfiguračním dialogu najděte pod nadpisem „Pokročilé plánování“ políčko
„Časová prodleva pro bezpečnostní prodej“, a zaškrtněte políčko, abyste tuto funkci zapnuli.

Dále zadejte požadovaný počet kalendářních dní. Tato bezpečnostní časová rezerva je záloha, která upozorňuje na
tým, aby se připravil na odesílání dříve než podle plánu.

Příklad:
Nastavení hodnoty :guilabel:`Security Lead Time for Sales` na 1.00 den posouvá
:guilabel:`Datum plánovaného dodání“ objednávky dopravy (DO) se posune o jeden den. V takovém případě
Produkt byl původně naplánován na dodání 6. dubna, ale s jednodenním bezpečnostním předstihem
novým termínem dodání by mělo být 5. dubna.

.... obrázek::lead_times/sales-security.png
:alt: Záložka Výhled na čas potřebný pro konfiguraci prodeje z nastavení prodeje.

Dodat několik produktů
------------------------

Pro objednávky zahrnující více produktů s různými časy dodání se mohou časové údaje lišit.
je možné nastavit přímo z citační stránky. Na citační stránce klikněte na záložku „Další informace“.
a nastavte :guilabel:`Dopravní politiku“ na:

#„Dodávat co nejdříve“ a dodat produkty, jakmile budou připraveny.
:guilabel:`Datum plánované dodávky“ v objednávce DO (dodacího příkazu) je určeno přičtením dnešního
datum, které je nejkratším termínem dodání zboží v objednávce.

#:guilabel:„Když jsou všechny produkty připraveny“ a počkat, až bude celá objednávka vyřízena najednou.
:guilabel:`Datum plánované dodávky“ v objednávce DO (dodacího příkazu) je určeno přičtením dnešního
datum k nejdelší dodací lhůtě mezi produkty v objednávce.

.. obrázek:lead_times/dodací politika.png
:alt:Zobrazte pole „Dopravní politika“ v záložce „Ostatní informace“ objednávky.

Příklad:
Ve výroku obsahujícím 2 produkty „Jógová podložka“ a „Odporový pás“, jsou produkty v čele.
Časová prodleva je osm dní a pět dní. Dnešním datem je 2. duben.

Když je nastaveno „Dodání co nejdříve“, pak se objednávka automaticky zařadí do fronty.
Dodací termín je 5 dní od dnešního dne: 7. dubna. Na druhou stranu vyberte: `When all
produkty jsou připraveny` nastavuje datum plánované dodávky na 8 dní od dnešního dne: 10. dubna.

Doba dodání
===================

Automatické plánování objednávek dodavatelů zjednodušuje nákupní proces tím, že uživatelům ukáže přesný čas, kdy je
potvrdit požadavek na nabídku (RFQ) a kdy očekávat dodání zboží.

.. seznam tabulek: Důležité termíny v rámci poptávky/objednávky
:hlavičkové řádky: 1
:sloupek: 1

   * – Hřiště
     - Popis
   * - Termín pro objednání
     - Poslední kalendářní den k potvrzení RFQ a převodu na PO
   * Očekávaný příjezd
     - Datum příjezdu produktů. Výpočet provedený jako *Deadline for order* + *Lead time for vendor*

Další výhodou je globální časová rezerva pro bezpečnostní úpravy, což jsou zálohy, které rozšiřují
„předpověď okamžitého času“ (JIT) předpovědní okno.
Doba dodání se vztahuje pouze na doplňovací metody, které využívají pravidla :doc:`pull
<../../přijímání a expedice/denní operace/využití tras> — například:
<prioritní pravidla rezervace> nebo :doc:`make to order (MTO) <mto>“. Ty nezmění rozestup mezi
*Termín objednávky* a *Očekávaný příjezd*.

.. viz také:
:doc:`PO plánování s pravidly pro přeskupení <reordering_rules>`

.. seznam-tabulka: Předpokládané časové rezervy pro globální bezpečnost
:hlavičkové řádky: 1
:sloupek: 1

   * – Puffer
     - Účel
     - Dopad na termíny
   * – :ref:`Doba dodání <skladové zásoby/dodací lhůty/dodací lhůta>
     - Připočítat do kalendáře další dny kvůli zpoždění. Obvykle se používá k započtení víkendů nebo
dovolené.
     - Žádné na RFQ/PO; přidává buffer dny do okna předpovědi JIT
<skladové zásoby/sklady a skladování/předpokládaný termín>.
   * – :ref:`Dny k nákupu <skladové zásoby/sklady a skladování/dny k nákupu>`
     - Dny, po které musí dodavatel zkontrolovat |RFQ| poté, co byl odeslán.
     - Žádné na RFQ/PO; přidává buffer dny do okna předpovědi JIT
<skladové zásoby/sklady a skladování/předpokládaný termín>.

.. obrázek: lead_times/vendor-lead-times.png
:alt: Zobrazení termínu splatnosti a data přijetí používané s dodacími lhůtami dodavatelů.

Příklad:
Abychom všechny nákupní lhůty propojili, zvažte tento faktor:

   - Dnes: 21. dubna
   - :guilabel:`Doba dodání od dodavatele“: 1 den
   - :guilabel:`Doba dodání zabezpečení nákupu“: 4 dny
   - :guilabel:`Dny k nákupu“: 2 dny

Dny od dneška = 1 + 4 + 2 = 7

Datum předpokládaného termínu = 28. duben

.... obrázek:lead_times/forecasted-date-purchase.png
:alt: Výpočet předpokládaného data na okně otevřeném po stisknutí tlačítka pro zobrazení doby dodání.

Příklad předpovědního okna JIT (just-in-time), které je v tomto případě období od 21. do 28. dubna.

Pokud dnes vytvoříte poptávku, zobrazí se následující pole:

   - :guilabel:`Termín objednávky“: 23. dubna (dnes + 2)
   - :guilabel:`Očekávaný příjezd“: 24. dubna (:math:`\text{Deadline for order} + 1`)

.... obrázek::lead_times/order-deadline.png
:alt: Datum splatnosti objednávky zobrazuje 23. dubna a datum očekávaného příjezdu 24. dubna.

.. skladovací prostory, sklady a nákupy lt:

Čas dodání
----------------

Aby bylo možné nastavit dodací lhůtu pro objednávky, které přicházejí do skladu z místo dodavatele, začněte
Navigace na produktový formulář přes: `Koupit aplikaci --> Produkty --> Produkty`.

Dále vyberte požadovaný produkt a přepněte na záložku „Nákup“. V editaci dodavatele
ceník, klikněte na tlačítko „Přidat řádek“ pro přidání podrobností o dodavateli, jako jsou
Název dodavatele, cena za produkt a nakonec
:guilabel:`Čas dodání“.

.. poznámka::
Do cenového seznamu dodavatelů lze přidat více dodavatelů a časové období. Výchozím dodavatelem je
Vybraný čas je ten, který je na prvním místě v seznamu.

..tip:
Pokud je datum očekávaného příjezdu již minulostí, pak se znak A | PO | objeví v poli Pozdě.
přístup do aplikace Purchase.

Příklad:
Na cenovém listu dodavatele produktu se zobrazuje položka „Dodací lhůta“ pro vybraný
dodavatel je nastaven na „10 dní.“

.... obrázek:lead_times/set-vendor.png
:alt:Přidat dodací lhůty dodavatele do ceníku produktu.

.. skladovací prostory, sklady, zásoby, nákupní bezpečnost lt:

Doba dodání zabezpečení nákupu
---------------------------

„Doba dodání“ je globální rezerva pro případ zpoždění, která se vztahuje na všechny dodavatele.
Chcete-li nastavit tuto funkci, přejděte na: „Nástroje“ - „Inventář“ - „Konfigurace“ - „Nastavení“.

V sekci „Další plánování“ zaškrtněte políčko „Časová prodleva pro nákup“.
zaškrtávací políčko.

Dále zadejte požadovaný počet kalendářních dnů. Konfigurací bezpečnostního časového předstihu vytvoříte
přičemž klikněte na tlačítko „Uložit“.

... skladové zásoby, sklady a doba nákupu:

Dny potřebné k nákupu
--------------------------

Pro nastavení přejděte do sekce „Inventářová aplikace“ - „Konfigurace“ - „Nastavení“.
V sekci „Pokročilé plánování“ v poli „Dny k nákupu“ zadejte
Počet dnů, které potřebuje dodavatel na potvrzení RFQ po obdržení od společnosti.

... skladovací prostory, výroba:

Doba dodání výrobků
========================

Doba dodání může pomoci zjednodušit proces nákupu spotřebního materiálu a součástek používaných v
výrobky s výrobními materiály (BOM).

Termín MO, který je termínem pro zahájení výrobního procesu k dokončení produktu.
a termín dodání lze určit konfigurací časů potřebných k výrobě.
dodací lhůty výrobních závodů.

.. obrázek:: lead_times/manuf-lead-times.png
:alt:Zobrazení výpočtu plánovaného termínu vyráběného zboží.

Doba výroby
-----------------------

Doba výroby produktů je konfigurována z formuláře materiálového listu (BOM).

Chcete-li přidat časový údaj k |BoM|, přejděte na: „Výroba“ -> „Produkty“ -> „Faktury“.
Materiálů“ a vyberte požadovaný „BoM“, který chcete upravit.

Na formuláři BoM klikněte na záložku „Různé“. Změňte hodnotu (v dnech) v poli
:guilabel:`Doba výroby‘ pole, aby bylo možné specifikovat kalendářní dny potřebné k výrobě produktu.

.. obrázek: lead_times/set-manufacturing.png
:alt:Časová hodnota dodání výrobku uvedená na formuláři pro materiálový list.

.. poznámka::
Pokud je vybraný |BoM| víceúrovňový, pak jsou dodací lhůty komponentů v |BoM|
přidána.

Pokud je produkt BoM poddodavatelsky, pak může být použita vlastnost „Čas dodání výrobce“ (Manuf. Lead Time) k určení
datum, kdy by měly být součástky odeslány poddodavateli.

Určit termín konečného splnění zadání na základě očekávaného data dodání, které je uvedeno v
:guilabel:`Datum plánovaného termínu“ pole v :abbr:`DO (Dodací objednávka)“.

Datum splatnosti, které je pole „Termín splatnosti“ na MO, se počítá jako
Očekávaný termín dodání odečten od času potřebného na výrobu.

To zajišťuje, že výrobní proces začne včas, aby bylo dodrženo termíny dodání.

Je však důležité si uvědomit, že termíny jsou počítány v kalendářních dnech. Termíny nezahrnují
Zvažte víkendy, svátky nebo kapacitu pracoviště (*:dfn:* počet operací, které mohou být provedeny v daném čase).
v práci současně.

.. viz také:
   - :doc:`Plánování výroby <../../../manufacturing/workflows/use_mps>`
   - :doc:`Plánování MO s pravidly přeskupení <reordering_rules>`

Příklad:
Termín dodání produktu na DO (Dodací objednávka) je stanovený na 15. srpna.
Produkt vyžaduje 14 dní na výrobu. Proto nejpozdější datum pro zahájení:
(Výrobní objednávka) k dodání je stanovena na 1. srpna.

... _Inventar/Lager/Vorbereitung der Fertigungsaufträge:

Dny na přípravu výrobního objednávky
-----------------------------------

Upravte počet dní potřebných k shromáždění komponentů pro výrobu produktu, když navštívíte jeho BoM.
to udělejte, přejděte na: menu „Výroba“ -> „Produkty“ -> „Sestavy“, a vyberte
žádané BoM.

V záložce „Různé“ v BoM zadejte počet kalendářních dnů potřebných k získání
komponenty výrobku v poli „Dny na přípravu objednávky k výrobě“.
vytváří |MOs| s dostatečným předstihem, aby bylo možné buď doplnit komponenty nebo
vyrábět polotovary.

..tip:
Kliknutím na položku „Výpočet“, která se nachází vedle „Dnů potřebných k přípravě objednávky výroby“
pole, vypočítává nejdelší dodací lhůtu mezi všemi komponentami uvedenými v |BoM|.

Do této hodnoty jsou započítány také bezpečnostní lhůty pro nákup, které se týkají konkrétního |BoM|.

Příklad:

A |BoM| má dvě složky, jedna má výrobní čas 2 dny a druhá
čtyři dny. Číslo v poli „Dny na přípravu výrobního objednávky“ je čtyři
dní.

... skladové zásoby, sklady, výroba - bezpečnost lt:

Vedoucí časové náročnosti výrobního procesu
--------------------------------

Do pole „Výrobní bezpečnost“ se zadává celosvětový časový limit pro obchod v poli „Manufacturing
aplikace --> Konfigurace --> Nastavení“. V sekci „Plánování“ zaškrtněte políčko u
:guilabel:`Časová prodleva v bezpečnosti“.

Dále zadejte požadovaný počet kalendářních dnů. Konfigurací bezpečnostního časového předstihu vytvoříte
vytvořit rezervu pro případné zpoždění výrobního procesu. Pak klikněte na tlačítko „Uložit“.

.. obrázek:lead_times/manuf-security.png
:alt: Zobrazení času na výrobu z nastavení aplikace pro výrobu.

Příklad:
Produkt má naplánovaný termín dodání na :abbr:`DO (dodací objednávka)“ stanovený na 15. srpna.
Výrobní termín je 7 dnů a bezpečnost výroby je 3 dny.
:guilabel:`Datum plánu“ na MO odráží nejpozdější datum, kdy se začne s výrobou objednávky.
V tomto případě je v plánu datum na MO 5. srpna.

Příklad ze světa
==============

Pokud chcete pochopit, jak všechny časy dodání spolupracují na zajištění včasné objednávky, podívejte se na následující příklad.
plnění:

- Doba dodání: 1 den
- **Časová rezerva pro zajištění výroby**: 2 dny
- **Doba dodání**: 3 dny
- **Doba dodání zabezpečení nákupu**: 1 den
- **Čas dodání od dodavatele**: 4 dny

Klient si objedná výrobek k dodání dne 1. září a
Datum zboží v skladu je 20. září. Odoo používá termíny dodání a automatické pravidlo pro opětovné objednávky,
zajistit potřebné operace podle data dodání výstupní zásilky, tedy 20. září:

.. obrázek:lead_times/global-example.png
:alt:Zobrazte časovou osu, která ukazuje, jak se dohromady pracují termíny dodání, aby bylo možné naplánovat skladové operace.

- **1. září**: Objednávka vytvořena a potvrzena prodejcem.

- **9. září**: Termín pro objednání komponent, aby dorazily včas při výrobě
začíná (4denní doba dodání od dodavatele).

- **13. září**: Termín přijetí součástek. Původně byl stanoven na 9/14, ale
Jednodenní bezpečnostní časový odstup posunul datum o jeden den dopředu.

- **14. září**: Termín pro zahájení výroby. Výpočet provedený odečtením doby výroby
s dodací lhůtou tři dny a výrobní bezpečností s dodací lhůtou dvou dnů od očekávaného
Dodací termín 19. září.

- **19. září**: Datum dodání na formuláři objednávky zboží uvádí aktualizované
původně stanovený termín dodání, který byl původně naplánován na 20. září. Ale vedoucí prodeje zabezpečení
Čas posunul datum o jeden den dopředu.

Plánování zásob Odoo zobrazuje proces vyřizování objednávek podniku, který je předem stanoven.
termíny a data objednávek surovin včetně rezervních dnů pro případné zpoždění. To zajišťuje
dodávky jsou včasné.
