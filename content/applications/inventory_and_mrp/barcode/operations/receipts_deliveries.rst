=============================================
Zpracovávejte faktury a dodací listy s čárovými kódy
=============================================

..._čárový kód/operační systém/úvodní stránka:

Aplikace Barcode lze použít k zpracování faktur, dodávek a dalších typů operací v reálném čase.
čas pomocí čárového kódu nebo aplikace Odoo Mobile.

Tím se umožňuje zpracovávat operace na skladovém podlaží v okamžiku jejich vzniku, namísto
čekat na ověření převodů z počítače. Takto provedené operace mohou pomoci k
správně přiřadit čárové kódy ke správným produktům, skladovým položkám a lokalitám.

Povolit aplikaci QR kód
==================

Pro zpracování převodů pomocí aplikace *Barcode* je nutné ji nainstalovat a zapnout funkci v
nastavení aplikace Inventář*.

Pro toto nastavení přejděte na záložku „Nastavení“ v aplikaci „Inventář“. Poté se posuňte dolů
do sekce „Čárový kód“ a zaškrtněte políčko vedle „Skenovač čárových kódů“.
feature.

Jakmile zaškrtnete políčko, klikněte na tlačítko „Uložit“ v horní části stránky a uložte změny.

Jakmile se stránka obnoví, zobrazí se nové možnosti pod tlačítkem „Skenovač čárového kódu“.
vlastnost: „Štítkové nomenklatury“ (s odpovídajícím seznamem) s možností buď
Můžete vybrat „Nomenklatura výchozí“ nebo „GS1 Nomenklaturu“.

Existuje také vnitřní odkaz „Nastavit štítky produktů“ ve tvaru šipky a sada
Tlačítka pro tisk příkazů k tisku čárového kódu a ukázkové listy s čárovým kódem.

.. obrázek: faktury_dodání/faktury-dodani-kodovani-zadani.png
:align:center
:alt:V nastavení aplikace Sklad zapnul funkci čárového kódu.

Více informací o instalaci a konfiguraci aplikace Barcode najdete v dokumentaci :doc:`Nastavení
snímač čárových kódů a:odkaz na dokumentaci:Aktivujte čárové kódy v Odoo
Dokumentační stránky.

... _čárový kód/operační/skenování přijatých produktů:

Skenujte čárové kódy na účtenkách
==========================

Pro zpracování příchozích skladových dokladů je nejprve potřeba nákupní objednávka (PO).
vytvořena a provedena operace přijetí.

Vytvořit objednávku, přejděte do aplikace Nákupy - Vytvoření.
vytvořit novou poptávku na nabídky (RFQ).

V prázdném poli „abbr: RFQ (žádost o nabídku)“ klikněte na rozbalovací seznam vedle
Pole „Dodavatel“ k přidání dodavatele. Pak v poli „Produkt“ pod
Klikněte na záložku „Produkty“, vyberte možnost „Přidat produkt“ a poté zvolte požadovaný produkt
K citátu.

Jakmile bude objednávka připravena, klikněte na tlačítko „Uložit“ v horní části formuláře a poté klikněte na „Potvrdit objednávku“.
potvrdit poptávku (RFQ) na nákupní objednávku (PO).

.. obrázek: faktury_dodání/faktury_dodání_objednávka.png
:align:center
:alt:Dokončená objednávka na čárový kódový produkt.

Pro zpracování a skenování čárových kódů na fakturách skladu přejděte do aplikace „Čárový kód“.

Jakmile se dostanete do aplikace „Čárový kód“, objeví se na obrazovce „Čtečky čárových kódů“ s různými
je nabídnuty následující možnosti. Chcete-li zpracovat faktury, klikněte na tlačítko „Operace“ v dolní části obrazovky
obrazovky. To přepne na stránku „Operace“ s přehledem.

.. obrázek: faktury_dodání/faktury_dodání_snímač_čárových kódů.png
:align:center
:alt: Obsahuje obrazovku aplikace s čárovým kódem a skenerem.

Na této stránce najděte kartu „Příjmy“ a klikněte na tlačítko „Pro zpracování“.
zobrazit všechny nevyřízené faktury. Pak vyberte požadovanou operaci s fakturou a zpracujte ji.
přepne na obrazovku s čárovým kódem.

.. poznámka::
Pokud používáte jen čárový kód nebo aplikaci Odoo Mobile, pak pro každou převodovou operaci existuje
Přiřazený typ operace lze snadno skenovat a zpracovávat. Jakmile je produkt skenován,
Tyto položky lze skenovat a nové produkty přidat do stávajícího převodu.
i přenos. Jakmile jsou všechny produkty skenovány, ověřte přenos a pokračujte v
pohyb zásob.

Z této obrazovky je přehled všech faktur k zpracování v rámci daného převodu (**WH/IN/000XX**).
ukázány. V dolní části obrazovky jsou možnosti „Přidat produkt“ nebo
:validace, podle toho, zda je nutné produkty přidat do operace, nebo celou
operace by měla být ověřena hned.

.. obrázek: faktury-dodání/faktury-dodání-skenovací zařízení.png
:align:center
:alt: Přehled příjmů v převodu na skenování.

Pro zpracování a skenování každého produktu zvlášť vyberte konkrétní produktovou řadu.
Tlačítko (+10) lze kliknout pro potvrzení přijetí produktu nebo
Ikona „tužka“ může být kliknutá, aby se otevřela nová obrazovka pro editaci produktové řady.

Na tomto obrazovce je uvedený produkt, který přijímáte. Pod názvem produktu jsou
V řádku „Množství“ lze upravit číslo 0 na požadované množství.
nebo klikněte na tlačítko „Jednotky“ (v tomto případě je to tlačítko „/10 jednotek“) a automaticky se vyplní
množství objednané z pořizovacího příkazu (PO).

.. příklad::
V příjmovém procesu „WH/IN/00019“ se očekává 10 jednotek produktu s čárovým kódem.
byl přijat. Hodnota pole „Vnitřní referenční číslo“ (viz obrázek) je nastavena na hodnotu pole „Interní referenční číslo“.
čárový kód produktu „Barcode Product“ a poté klikněte na
:guilabel:`tužka“ ikonu pro manuální zadání přijatých množství.

.... obrázek: faktury_dodání/faktury-dodání-produktová-řada-editor.png
:align:center
:alt:Editor řady produktů pro individuální přenos v aplikaci Barcode.

Dále lze kliknout na tlačítka +1 a -1 pro přidání nebo odečtení.
množství produktu a klíčové slovo „počet“ lze použít k přidání množství stejně jako u čárového kódu.

Pod klávesami s čísly je řádka umístění, která zní WH/Stock.
Výchozí hodnota, pokud není uvedeno jiné místo na produktu samotném. Klikněte na tuto řádku pro zobrazení
rozbalovací nabídka dalších lokalit, ze kterých si můžete vybrat.

Jakmile bude připravena, klikněte na tlačítko „Potvrdit“ pro potvrzení změn v produktové linii.

Pak z přehledu všech faktur k zpracování v rámci této platby (**WH/IN/000XX**)
Klikněte na tlačítko „+ #“ v řádku produktu pro přijímané zboží a klikněte
:validace. Příjem byl nyní zpracován a můžete použít aplikaci
uzavřel.

.. obrázek: faktury-dodání/faktury-dodání-validovat-převod.png
:align:center
:alt:Přehled příjmů v převodu k ověření.

Přečtěte si čárové kódy pro objednávky na dodání
=================================

Pro zpracování dodávek skladu pro odchozí produkty je nejprve potřeba faktura (FO).
a zahájit proces dodání.

Vytvořit objednávku SO (prodejní objednávka), přejděte do aplikace „Prodej“ a klikněte na tlačítko „Vytvořit“.
Vytvořit novou nabídku.

V prázdném citačním formuláři klikněte na rozbalovací nabídku vedle pole „Zákazník“ a
Přidejte zákazníka. Pak v poli „Produkt“ pod záložkou „Dodací řádky“ klikněte
:guilabel:`Přidat produkt“ a vyberte požadované produkty, které chcete přidat do nabídky.

Jakmile je vše připraveno, klikněte na tlačítko „Uložit“ nahoře na stránce a poté na „Potvrdit objednávku“.
potvrdit citaci pro SO (prodejní objednávku).

.. obrázek: faktury_dodání/faktury-dodání-objednávky-na-prodej.png
:align:center
:alt:Dokončená objednávka na čárový kódový produkt.

Pro zpracování a skenování čárových kódů pro dodávky do skladu přejděte na aplikaci „Čárový kód“.

Jakmile se dostanete do aplikace „Čárový kód“, objeví se na obrazovce „Čtečky čárových kódů“ s různými
je prezentován. Pro zpracování dodávek klikněte na tlačítko „Operace“ v
dole obrazovky. Toto přesměruje na stránku „Operace“ v přehledu.

Na této stránce najděte kartu „Příkazy k dodání“ a klikněte na „# k zpracování“.
tlačítko pro zobrazení všech nedodaných objednávek. Pak vyberte požadovanou dodací objednávku k zpracování.
přepne na obrazovku s čárovým kódem.

.. obrázek: faktury_dodání/faktury-dodání-operace-stránka.png
:align:center
:alt:Stránka přehledu operací v aplikaci Dashboard kódu čárového kódu.

Na tomto obrazovce se zobrazuje přehled všech dodávek k zpracování v rámci daného převodu (**WH/OUT/000XX**).
je zobrazeno. Na spodní části obrazovky jsou možnosti „Přidat produkt“ nebo
:validace, podle toho, zda je nutné produkty přidat do operace, nebo celou
operace by měla být ověřena hned.

Pro zpracování a skenování každého produktu jednotlivě vyberte konkrétní produktovou řadu.
Kliknutím na tlačítko lze indikovat dodání daného produktu nebo kliknutím na ikonku tužky
kliknutím otevřela nové okno pro editaci produktové řady.

Na tomto obrazovce je uvedený produkt, který se doručuje. Pod názvem produktu jsou
V řádku „Množství“ lze upravit číslo 0 na požadované množství.
nebo klikněte na tlačítko „Jednotky“ (v tomto případě je to tlačítko „/10 jednotek“) a automaticky se vyplní
množství objednané z pořadového čísla „SO (objednávka)“.

Dále lze kliknout na tlačítka +1 a -1 pro přidání nebo odečtení.
množství produktu a klíčové slovo „počet“ lze použít k přidání množství stejně jako u čárového kódu.

Pod klávesami s čísly je řádka umístění, která zní WH/Stock.
výchozí, pokud není na výrobku uvedeno jiné místo.

Toto je místo, ze kterého se produkt vybírá pro doručení. Klikněte na tuto řádku, abyste zobrazili
rozbalovací nabídka dalších lokalit k výběru (pokud je tento produkt skladován na více místech).
skladu)

.. tip::
Pro sklady s více různými skladovacími místy, pravidly pro ukládání a vyzvedávání zboží
strategie, k různým typům operací lze přidávat další kroky, zatímco používáte *Čárový kód*.
aplikace.

Jakmile bude připravena, klikněte na tlačítko „Potvrdit“ pro potvrzení změn v produktové linii.

Pak z přehledu všech faktur k vyřízení v rámci této platby (**WH/OUT/000XX**)
Klikněte na tlačítko „+ #“ v řádku produktu pro přijímané zboží a klikněte
:validace` a poté aplikaci „Čárový kód“ zavřete.

.. obrázek: faktury-a-dodání/faktury-a-dodání-validovat-dodávku.png
:align:center
:alt: Přehled dodávek v převodu k ověření.
