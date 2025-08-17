=======================
Závislosti pracovních příkazů
=======================

.. |BOM| nahradit za: zkratka: `BoM (Bill of Materials)`

Při výrobě některých produktů mohou být nutné konkrétní operace před ostatními.
začít. Pro zajištění správného pořadí operací je nutné použít modul výroby v Odoo *.
obsahuje nastavení „závislosti pracovních příkazů“. Zapnutím tohoto nastavení lze provádět operace na faktuře
materiálů (BoM) blokovaných jinými operacemi, které mají být provedeny jako první.

Konfigurace
=============

Výchozí nastavení pracovního postupu neobsahuje závislosti mezi pracovními postupy. Chcete-li tuto funkci zapnout, začněte procházením
Poté přejděte na „Výroba“ -> „Konfigurace“ -> „Nastavení“. Zapněte „Práce
Nastavení objednávek, pokud není již aktivní.

Po zapnutí nastavení „Pracovní příkazy“ se zobrazí také nastavení „Závislosti pracovních příkazů“.
zobrazí se pod ním. Zapněte „Závislosti na pracovních příkazech“, pak klikněte na „Uložit“
změny.

Přidat závislosti na BoM
=======================

Závislosti pracovních příkazů se nastavují v |BOM| produktu. Chcete-li tak učinit, přejděte na
Vyberte položku „Výroba“ - „Produkty“ - „Seznam materiálů“, poté vyberte nebo vytvořte
nové kliknutím na „Nový“.

.. varování: Více se dozvíte zde

Pro kompletní průvodce k nastavení nové |BOM| se podívejte na dokumentaci
:doc:`vytvoření seznamu materiálů <../basic_setup/bill_configuration>.

Na záložce „Různé“ klikněte na tlačítko „Operace“, které je v nabídce.
Zatržítko „závislosti“. To dává novou možnost „Blokované“ v nastavení
kartě Operace.

.. obrázek: work_order_dependencies/operation-dependencies.png
:align:center
:alt:Zaškrtávací políčko „Operační závislosti“ na kartě „Další“.

Dále klikněte na záložku „Operace“. Na pravé horní straně záložky klikněte na záložce
Klikněte na tlačítko „Nastavení“ a zaškrtněte políčko „Zablokované“. To vám umožní
V poli „Blokované“ se zobrazí pole „Zablokováno“ pro každou operaci na kartě „Operace“.

.. obrázek: work_order_dependencies/operations-settings.png
:align:center
:alt:Nastavení karty Operace v BoM.

V řádku operace, která má být zablokována jinou operací, klikněte na
Pole „Zablokován“ a okno „Otevřeno: operace“ se zobrazí.
Vyberte blokovanou operaci z roletky „Blokováno“ v okně s upozorněním.
musí být dokončena před blokovanou operací.

.. obrázek: work_order_dependencies/blokované.png
:align:center
:alt: Rozbalovací seznam Blokované uživatelem pro operace na BoM.

Nakonec uložte soubor pomocí tlačítka „Uložit“ (Guilabel: Save).

Vytvářejte pracovní příkazy podle závislostí
===================================

Jakmile jsou v BOM nastaveny pořadí pracovních úkolů, je Odoo Manufacturing schopno plánovat
Při plánování pracovních příkazů na základě jejich závislostí.
objednávka výroby, začněte tím, že se přesunete na: „Výroba“ -> „Provoz“ ->
Výrobní objednávky“.

Poté vyberte výrobní objednávku produktu s nastavenými závislostmi na pracovních příkazech v jeho BOM.
Vytvořit nový výrobní příkaz kliknutím na tlačítko „Nový“. Pokud chcete vytvořit nový výrobní příkaz,
Vytvořte si BOM sestavený z pracovních příkazů s vazbami.
Vyberte pole „Materiál“ a klikněte na tlačítko „Potvrdit“.

Po potvrzení výrobního příkazu vyberte záložku „Výrobní příkazy“, abyste zobrazili práce
povolení, které je potřebné k dokončení práce.
zobrazit štítek „Připraveno“ v sekci „Stav“.

Pracovní příkazy, které jsou zablokovány jedním nebo více pracovních příkazů, mají v záhlaví označení „Čeká na další PO“.
místo toho. Jakmile jsou dokončeny blokovací práce, štítek se aktualizuje na „Připravený“.

.. obrázek: work_order_dependencies/work-order-status.png
:align:center
:alt:Stavové značky pro výrobní objednávku.

Klikněte na tlačítko „Plán“ v horní části obrazovky.
stránce. Poté proveďte následující kroky pro každou objednávku na
:guilabel:„Pracovní příkazy“ se automaticky vyplňují datem a časem plánovaného začátku práce. Blokovaný pracovní příkaz
je naplánována na konec doby uvedené v poli „Očekávaná doba“
předcházející pracovní příkaz.

.. obrázek:work_order_dependencies/plánovaný začátek.png
:align:center
:alt:Datum zahájení práce na výrobním příkazu.

Příklad:
Vytvoří se výrobní objednávka na produkt A. Výrobní objednávka má dvě operace: Řez
a Sestavit. Každá operace má očekávanou dobu trvání 60 minut a operaci Sestavit
Je blokována operací Cut.

Tlačítko „Plán“ pro výrobní objednávku je kliknuto v 13:30 a začíná se řezat.
Operace je naplánována na okamžitě. Operace „Řez“ má očekávanou dobu trvání
60 minut a operaci Assemble je naplánováno zahájit v 14:30 hodin.

Plánování v pracovních centrech
----------------------

Pro zobrazení vizuální reprezentace plánování pracovních příkazů přejděte na :guilabel:`Pracovní
Stránku plánování objednávek najdete na adrese:
Workcenter“. Tato stránka zobrazuje časový plán všech pracovních úkolů, které jsou naplánované pro každou operaci.

Pokud je jeden pracovní příkaz zablokován dokončením jiného, zablokovaný pracovní příkaz se zobrazí
Jako naplánované by mělo začít po zablokování práce nařízením. Kromě toho spojuje oba pracoviště šipka.
příkazy vedoucí z blokovací operace k blokované operaci.

.. obrázek: work_order_dependencies/plánovací šipka.png
:align:center
:alt:Šipka spojující zablokovaný pracovní příkaz s příkazem, který jej zablokoval.
