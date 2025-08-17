==========================================
Vytvářejte a zpracovávejte převody s čárovými kódy
==========================================

Aplikace Barcode může být použita k zpracování vnitropodnikových převodů pro všechny typy produktů, včetně
převody produktů sledovaných pomocí čísla šarže nebo sériového čísla. Převody lze vytvářet od nuly
v reálném čase pomocí skenovacího zařízení nebo mobilní aplikace kompatibilních se systémem Odoo.

Seznam kompatibilních s aplikací Inventář mobilních skenerů čárových kódů a dalšího hardwaru najdete zde.
viz stránku „Sklad Odoo • Hardware“ na adrese https://www.odoo.com/app/inventory-hardware/.

Povolit aplikaci QR kód
==================

Pro zpracování převodů pomocí aplikace *Barcode* je nutné ji nainstalovat a zapnout funkci v
nastavení aplikace Inventář*.

Pro toto nastavení přejděte na záložku „Nastavení“ v aplikaci „Inventář“. Poté se posuňte dolů
do sekce „Čárový kód“ a zaškrtněte políčko vedle „Skenovač čárových kódů“.
feature.

Jakmile zaškrtnete políčko, klikněte na tlačítko „Uložit“ v horní části stránky a uložte změny.

Po obnovení stránky se zobrazí nové možnosti pod tlačítkem „Skenovač čárových kódů“.
vlastnost: „Štítkové nomenklatury“ (s odpovídajícím seznamem) s možností buď
„Výchozí nomenklatura“ nebo „GS1 výchozí nomenklatura“ může být vybrána.
vybraná nomenklatura změní způsob, jakým skenery interpretovaly čárové kódy v Odoo.

Existuje také vnitřní odkaz „Nastavit štítky produktů“ ve tvaru šipky a sada
Tlačítka pro tisk příkazů k tisku čárového kódu a ukázkové listy s čárovým kódem.

.. obrázek: transfers_scratch/transfers-scratch-enabled-barcode-setting.png
:align:center
:alt:V nastavení aplikace Sklad zapnul funkci čárového kódu.

Více informací o instalaci a konfiguraci aplikace Barcode najdete v dokumentaci :doc:`Nastavení
snímač čárových kódů a:odkaz na dokumentaci:Aktivujte čárové kódy v Odoo
Dokumentační stránky.

Pro převoz v rámci firmy skenujte čárové kódy
====================================

Pro vytváření a zpracovávání interních převodů produktů ve skladu je k dispozici:guilabel:Sklad
Funkce „Umístění“ a „Vícenásobný krok“ musí být zapnuté.

Pro toto nastavení přejděte na záložku „Nastavení“ v aplikaci „Inventář“. Poté se posuňte dolů
do sekce „Sklad“ a zaškrtněte políčka vedle „Uložiště“.
a:guilabel:`Složené trasy“.

Poté klikněte na tlačítko „Uložit“ v horní části stránky a uložte změny.

Vytvořit vnitrofiremní převod
---------------------------

Pro zpracování stávajících vnitrofiremních převodů je nejprve nutné vytvořit vnitrofiremní převod a
operace zpracování.

Pro vytvoření interního převodu se přesuňte do aplikace „Sklad“.
Karta „Vnitřní převody“ v panelu „Přehled skladových zásob“,
na tlačítko „Zpracovat“ (viz obrázek).

Poté klikněte na tlačítko „Vytvořit“ v levém horním rohu stránky, která se zobrazí. Toto otevře novou
formulář „Vnitřní převod“.

Na prázdném formuláři je automaticky uveden typ operace :guilabel:`Internal
Převody“. Pod tímto polem je pole „Zdroj“ a „Účel“.
výchozí nastavení je „WH/Sklad“, ale lze jej změnit na jakoukoliv položku produktů
Jsou přesouvány z jednoho místa na druhé.

.. obrázek: transfers_scratch/transfers-scratch-internal-transfer-form.png
:align:center
:alt:Vnitřní převodový formulář s místem zdroje a místem cíle.

Jakmile jsou vybrány požadované lokality, můžete přidat produkty do přenosu.
V sekci „Produkty“ pod záložkou „Produkt“ klikněte na tlačítko „Přidat produkt“.
Vyberte požadovaný produkt (produkty), který chcete přenést.

Jakmile je převod připravený, klikněte na tlačítko „Uložit“ v horní části formuláře a uložte nový interní převod.
Uložte, klikněte na ikonu „Podrobné operace“ (čtyři řádky v pravém dolním rohu).
„Produkty“ (viz obrázek) a otevřete okno „Podrobné operace“.

.. obrázek: transfers_scratch/transfers-scratch-detailed-operations-popup.png
:align:center
:alt: Podrobné informace o vnitřním převodu.

V okně zvolte možnost „Přidat řádek“.

Poté v sloupci „Kde“ změňte umístění z „WH/Sklad“ na jiné.
místo, kam se produkty mají přesunout.

Poté v sloupci „Dokončeno“ změňte množství na požadované množství přenosu.
připraveno, klikněte na tlačítko „Potvrdit“ pro zavření okna s upozorněním.

Skenujte čárové kódy pro vnitřní přesun
-----------------------------------

Pro zpracování a skenování čárových kódů pro vnitřní převody přejděte do aplikace „Čárový kód“.

Jakmile se dostanete do aplikace „Čárový kód“, objeví se na obrazovce „Čtečky čárových kódů“ s různými
je nabídnuty.

Pro zpracování vnitropodnikových převodů klikněte na tlačítko „Operace“ v dolní části
obrazovku. To vás přesměruje na stránku „Operace“ s přehledem.

.. obrázek:: transfers_scratch/transfers-scratch-barcode-app.png
:align:center
:alt: Obsahuje obrazovku aplikace s čárovým kódem a skenerem.

Na této stránce najděte kartu „Vnitřní převody“ a klikněte na „# Do
Tlačítko „Proces“ pro zobrazení všech nevyřízených vnitrofiremních převodů. Pak vyberte požadovanou operaci
tento proces přenese čárový kód na obrazovku.

.. poznámka::
Při používání aplikace *Barcode* bez aplikace *Inventář* (pouze v případě, že se používá čtečka
(Odoo mobilní aplikace), pro každý převod odpovídajícího typu operace lze použít kódy čárových
Byly naskenovány, aby se s nimi dalo snadno pracovat.

Jakmile je zboží naskenováno, lze skenerem skenovat produkty, které jsou součástí stávajícího převodu, a nové produkty.
Mohou být přidány do přenosu také další produkty. Jakmile jsou všechny produkty skenovány, ověřte přenos
aby pokračovaly v přesunech zásob.

Z této obrazovky lze získat přehled všech produktů, které je potřeba zpracovat v rámci konkrétního interního převodu.
(**WH/INT/000XX**) je zobrazena. V dolní části obrazovky jsou možnosti kliknutí na:guilabel:`Přidat
„Produkt“ nebo „Guilabel“, podle toho, zda se produkty přidávají do operace, nebo ne
Všechny operace by měly být ověřeny najednou.

.. obrázek: transfers_scratch/transfers-scratch-receipts-overview.png
:align:center
:alt: Přehled příjmů v převodu na skenování.

Poté naskenujte čárový kód produktu a zpracujte vnitřní převod.

Anebo zpracovat a skennout každý produkt zvlášť, vybrat konkrétní produktovou řadu.
Tlačítko „+ 1“ může být kliknuté pro přidání dalšího množství daného produktu do převodu.
Ikona tužky může být kliknutá, aby se otevřel nový obrazovkový formulář pro úpravu produktové řady.

V okně produktu je zobrazeno pole pro výběr produktu a jednotek k zpracování s numerickou klávesnicí.
Pod produktovým názvem lze upravit řádek „Množství“. Změňte číslo v řádku
k množství uvedenému na vnitřním převodovém formuláři.

.. příklad::
V interní převodní operaci „WH/INT/000XX“ je převedeno 50 jednotek produktu
převeden z „WH/Stock“ na „WH/Stock/Police 1“. [TRANSFER_PROD] je :guilabel:`Vnitřní
Referenční číslo na produktovém tvaru. Skenujte čárový kód „Produkt převodu“ a obdržíte jeden
jednotka. Poté klikněte na ikonu tužky a ručně zadejte převedené množství.

.... obrázek:transfers_scratch/transfers-scratch-product-line-editor.png
:align:center
:alt:Editor řady produktů pro individuální přenos v aplikaci Barcode.

Dále lze kliknout na tlačítka +1 a -1 pro přidání nebo odečtení.
Množství produktu a klávesy pro zadávání čísel lze použít k přidání množství.

Pod klávesami s čísly jsou dvě řádky :guilabel:`location`, které zobrazují lokality, na které se
předtím uvedené na vnitřním převodovém formuláři, tedy „WH/Sklad“ a „WH/Sklad/Police 1“.
Klikněte na tyto řádky, abyste zobrazili rozbalovací nabídku dalších možností.

Jakmile bude připravena, klikněte na tlačítko „Potvrdit“ pro potvrzení změn v produktové linii.

Poté přejděte na stránku s přehledem všech produktů k zpracování v rámci této převodní operace (**WH/INT/000XX**)
Klikněte na tlačítko „Potvrdit“. Faktura byla nyní zpracována a aplikace může být zavřena.
výstup.

.. tip::
Aplikace Barcode může být také použita k skenování produktů v interních převodech, které obsahují jedinečné číslo šarže.
čísla a sériová čísla.

Z obrazovky přenosu čárového kódu skenujte čárový kód položky nebo sériové číslo a Odoo
automaticky zvyšuje množství produktu na množství uvedené v databázi. Pokud
stejný los nebo sériové číslo je sdíleno mezi různými výrobky, naskenujte kód výrobku
Nejprve kód šarže/sériového čísla.

.. viz též:
:ref:`Připojte se k databázi čárových kódů <barcode/setup/barcodelookup>“ a rychle vytvořte nové
produkty při vnitropodnikovém přesunu skenerem čárových kódů.

Vytvořte převod od nuly
==============================

Kromě zpracování a skenování čárových kódů pro stávající vnitřní převody již dříve vytvořené.
Aplikace Barcode může být použita také k vytváření převodů od nuly, jednoduše pomocí skenování tištěného
kód operace.

.. varování:Víte, že...

Aplikace Barcode společnosti Odoo poskytuje ukázkové kódy s čárovými kódy, které lze použít k prozkoumání funkcí aplikace.
Tyto lze použít k testování a mohou být vytisknuty z domovské obrazovky aplikace.
Přejděte do aplikace čárového kódu a klikněte na zásoby.
„čárové kódy“ (tučně a modře zvýrazněno).

.... obrázek: transfery_skrček/transfers-skrček-demo-data.png
:align:center
:alt:Při spuštění aplikace se objeví okno s informacemi o demo datových souborech.

Pro přístup k aplikaci Barcode musíte nejprve otevřít aplikaci s názvem „Barcode“. Jakmile se dostanete do aplikace Barcode,
Na obrazovce „Skenování čárového kódu“ jsou zobrazeny různé možnosti.

Na této obrazovce lze pomocí USB nebo bezdrátového čtečky čárových kódů přímo skenovat produktové čárové kódy.

Při používání chytrého telefonu jako snímače čárových kódů stiskněte tlačítko „Tap to Scan“ (vedle
ikonu kamery (v centru obrazovky). To otevře okno „Barcode Scanner“.
obrazovka, která umožňuje použití fotoaparátu zařízení.

Otočte kameru na tisknutelnou operační značku a skenujte ji. Tím se zpracuje
čárový kód a přepne na obrazovku pro přenos čárového kódu.

Z této obrazovky lze získat přehled všech produktů, které je potřeba zpracovat v rámci konkrétního interního převodu.
(**WH/INT/000XX**) je uvedeno. Nový převod byl vytvořen od nuly, takže
na stránce by neměly být žádné produkty.

Chcete-li přidat produkt, naskenujte čárový kód. Pokud je kód nečitelný, zadejte ho ručně.
produkt do systému kliknutím na tlačítko „Přidat produkt“ v dolní části obrazovky.
a přidat produkty a jejich množství, které mají být převedeny.

Jakmile bude připravena, klikněte na tlačítko „Potvrdit“ pro potvrzení změn v produktové linii.

.. obrázek: transfers_scratch/transfers-scratch-blank-product-editor.png
:align:center
:alt: Prázdný produktový editor v interním převodu mezi skratchy.

Poté přejděte na stránku s přehledem všech produktů k zpracování v rámci této převodní operace (**WH/INT/000XX**)
Klikněte na tlačítko „Potvrdit“. Vnitřní převod je nyní zpracován a aplikace *Čárový kód*
být uzavřen.
