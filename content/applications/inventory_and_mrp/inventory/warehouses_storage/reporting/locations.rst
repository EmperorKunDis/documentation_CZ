===================
Dashboard umístění
===================

Dashboard „Lokalita“ v aplikaci Inventura poskytuje přehled o skladových zásobách.
místa pro produkty společnosti. Tento report vám ukáže, kde je skladováno zboží a pomůže identifikovat
„ztratěné položky“ (výrobní zásoby / skladování na skladě / zadržené), nebo se podívejte do minulosti v inventáři, abyste viděli produkt
konkrétní data a místa.

Pro přístup k zprávě o umístění je zapotřebí funkce „Uložiště“ aktivovat. K tomu se musíte dostat na
:menu „Skladová aplikace“ --> „Konfigurace“ --> „Nastavení“. V sekci „Sklad“
Zatrhněte políčko u „Uložiště“ a klikněte na „Uložit“. Pak přejděte do
přejděte na „Inventář aplikace“ -> „Zprávy“ -> „Lokality“.

.. poznámka::
V nabídce „Hlášení“ v Inventáři je přístupná pouze uživatelům s :doc:`přístupem správce.
<../../../obecne/uzivatele/pristupova-prava>.

...Inventář/sklad/místo skladování:

Procházejte seznam míst
================================

Výchozí nastavení panelu „Lokality“ zobrazuje všechny produkty skladem.
:guilabel:`Produkt“ sloupec), spolu s následujícími informacemi:

- :guilabel:`Lokalita“: aktuální skladovací místo. Pokud je produkt uložen na „Polici 1“ a „Polici 2“,
produkt je uveden dvakrát, u každé položky jsou uvedeny množství na skladě.
- :guilabel:`Příbalový leták`: příbalový leták produktu, pokud existuje.
- :guilabel:Číslo šarže nebo sériové číslo: pokud má výrobek šarži nebo sériové číslo, je zde uvedeno.
- :guilabel:`Množství na skladě“: aktuální množství produktů. Klikněte na ikonku „fa-pencil“
:guilabel:`(upravit)` ikonu pro :doc:`změnu skladových zásob

- :guilabel:`Rezervovaná množství“: skladové zásoby vyhrazené pro operace jako například výdejky
dodacími objednávkami nebo výrobou.
- :guilabel:`Jednotka měření výrobku“: jednotka měření produktu.

Klikněte na tlačítka vedle položek v každé řádce, abyste získali další informace:

- :i:fa-history: :gulabel:Historie: zobrazení historie pohybu zásob produktu
informace o množství a popisu důvodu, proč byl produkt přemístěn z jedné lokality do
jiný.

..tip:
Prohlédněte si, k čemu je zboží rezervováno, kliknutím na ikonu „Historie“
tlačítko na nejvzdálenějším pravém konci řady produktů.

Na stránce „Historie pohybů“ odstraňte filtr :guilabel:`fa-filter` :guilabel:`Done`.
z vyhledávací lišty odhalit filtrační možnosti a vybrat filtr „Co dělat“.

.. obrázek:: locations/reserved-products.png
:alt:Zobrazit stránku s historií pohybů, která zaznamenává rezervace produktu pro dodání.

- :ikonka: obnova :guilabel: Dodání: přístup k pravidlům pro doplňování
stránku „Nastavení pravidel pro doplňování zboží“ a přidat produkty na konkrétní místo.

V horním levém rohu stránky klikněte na tlačítko „Nový“ a vytvořte si :doc:`seznam
upravení záznamu o množství určitého produktu v
Specifické: `Lokalita`.

Pro zobrazení produktů, množství a jejich umístění pro určité datum klikněte na
Tlačítko „Výpis k datu“ (je také umístěno v horním levém rohu stránky). Vyberte
datum a čas v poli „Inventura k datu“ a poté stiskněte tlačítko „Potvrdit“.

Zobrazit prázdná místa
--------------------

Pro zobrazení aktuálně volných míst přejděte na: „Nastavení“ --> „Sklad“.
--> Lokace“.

Prázdné lokality jsou označeny zaškrtávacím políčkem v sloupci „Je prázdná“. Zobrazit lze pouze
prázdné lokace, klikněte do vyhledávacího pole a zvolte filtr „Prázdné lokace“.

.. obrázek: obrazky/prázdné_oblasti.png
:alt: Seznam prázdných lokalit v aplikaci Inventura.

Vytvářet zprávy
================

Po učení se navigaci v rozhraní pro správu umístění
<Inventář/Skladování a sklady/Zpráva o lokalitách>“, může být použita k vytváření a sdílení různých
zprávy.

Několik běžných zpráv, které lze vytvořit pomocí panelu „Lokace“, jsou
viz níže.

Zpráva o mrtvých zásobách
-----------------

Chcete-li získat seznam neprodaných položek, také známý jako „mrtvé zásoby“, postupujte takto:

#Přejděte na:menu: „Skladové aplikace - > Zprávy - > Místa“.
#Pak klikněte do vyhledávacího pole, aby se zobrazilo rozbalovací menu s filtry.
:guilabel:`Skupina“, „Oblíbené“ a „Vyhledávání“.
#Zapněte možnost „Vnitřní umístění“ a „Upomínky k vypršení platnosti“ pod
:guilabel:`Filtry“ sekce.

Hlášení nyní zobrazuje seznam vypršených produktů.

.. poznámka::
Tento výpis lze také vytvořit z :ref:`Čísla sériového čísla
stránka „Upozornění na vypršení platnosti“ v sekci „Skladování a řízení zásob“,
:menu_selecce:`Správa zásob --> Produkty --> Sériová čísla“.

.. obrázek: lokace/zabité zásoby.png
:alt:Zobrazit seznam produktů, jejichž doba trvanlivosti již dnes vypršela.

.. skladování v zásobnících, skladech a na stojících konstrukcích:

Zpráva o zůstatku zásob
-------------------------

Firmy používající vícekrokové toky v aplikacích Inventář nebo Výroba mohou
„zapomenuté“ položky, které jsou produkty nesprávně uskladněné v důsledku lidské chyby.
tento report, který by měl být pravidelně kontrolován umístění přenosů (např. *WH/Input*, *WH/Pre-Processing*).
zajistit přesun věcí na jejich určená místa a správné zaznamenání do databáze.

Chcete-li získat seznam věcí, které možná dlouho leží ve skladu, postupujte podle těchto kroků:

#Přejděte na:menu: „Skladové aplikace - > Zprávy - > Místa“.
#Vyhledávací liště začněte psát název místa, kam se zboží má převézt.
to, jako například „VH/Vstup“ nebo „VH/Balení“.
#Vyberte možnost „Hledat v:“ [název lokality] z rozevírací nabídky, která se objeví.
nabídka, která se objeví pod vyhledávacím polem.

.... obrázek:: obrázky/hledání_vstupu_lokalita.png
:alt:Zobrazit výsledky vyhledávání pro tuto polohu.

Nyní se v zprávě zobrazuje seznam produktů na přechodovém místě.

Příklad:
Vyhledáním „Zadání“ v poli „Lokalita“ se zobrazí seznam produktů na místě *WH/Input*.

Seznam ukazuje 500 kusů „kuřecího masa“, což je alarmující, pokud nebude chlazeno brzy po
příjemce. Zpráva o zadrženém zásobování pomáhá identifikovat položky, které byly dlouho bez využití
nejsou skladovány.

.... obrázek: locations/stranded-inventory.png
:alt:Zobrazit položky uložené na konkrétním místě.

Hlášení o nesrovnalostech v inventáři
----------------------------

Vytvořit zprávu o položkách, které byly přemístěny od posledního inventárního auditu
Proveďte následující kroky:

#Přejděte na:menu: „Skladové aplikace - > Zprávy - > Místa“.
#Pak klikněte do vyhledávacího pole, aby se zobrazilo rozbalovací menu s filtry.
:guilabel:`Skupina“, „Oblíbené“ a „Vyhledávání“.
#Zapněte možnost „Vnitřní lokality“ a „Konflikty“.
:guilabel:`Filtry“ sekce.
#Zpráva nyní zobrazuje položky, jejichž množství se změnilo od posledního cyklického počítání.

.. obrázek:: locations/discrepancy.png
:alt:Zobrazit položky filtru Konflikty v zprávě.

#Klikněte na tlačítko „Historie“ (ikonka „fa-history“) a zobrazí se vám přesuny zásob, včetně
příjmy a dodávky, které se staly od poslední inventarizace.

.. obrázek:: locations/history.png
:alt:Zobrazte historii pohybů, která zobrazí dodávku, která proběhla po provedené inventarizaci.
