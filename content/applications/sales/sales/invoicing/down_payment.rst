=============
Záloha
=============

Záloha je počáteční platba, která se provádí během potvrzení prodejní transakce.
Výplatní částka snižuje riziko pro obě strany (prodávajícího i kupujícího), protože ukazuje, že jsou si vzájemně nakloněni.
zavázat se k dokončení prodeje.

S vkladem kupující zaplatí část celkové dlužné částky, přičemž souhlasí s tím, že zbytek zaplatí.
zbývající částku později. V opačném případě prodávající poskytuje kupujícímu zboží nebo služby
nebo po přijetí zálohy s tím, že zbývající částka bude zaplacena později.

V aplikaci pro prodej Odoo **Sales** lze nastavit zálohy tak, aby vyhovovaly potřebám každého jednotlivého prodeje.
transakce.

Vystavujte faktury
===============

Při potvrzení objednávky se zobrazí možnost vytvořit fakturu.
Tlačítko „Vytvořit fakturu“. Když je kliknuté, objeví se okno „Vytvořit faktury“.

.. obrázek:down_payment/create-invoices-popup-form.png
:align:center
:alt:Vytvořit okno pro vytváření faktur, které se objevuje ve Sales od Odoo.

.. poznámka::
Faktury se automaticky vytvářejí jako návrhy, takže je lze před schválením zkontrolovat.

V okně „Vytvořit fakturu“ je k dispozici tři možnosti.
:guilabel:`Vytvořit fakturu“ pole:

- :guilabel:`Běžná faktura“
- :guilabel:`Úhrada kupní ceny (v procentech)“
- :guilabel:`Úhrada kupní ceny (pevná částka)“

Poptávka po prvotním vkladu
============================

V okně „Vytvořit fakturu“ jsou možnosti úhrady následující:

- :guilabel:`Úhrada kupní ceny (v procentech)“
- :guilabel:`Úhrada kupní ceny (pevná částka)“

Vyberte si požadovanou možnost vkladu, pak vyberte požadované procento nebo
pevná částka v poli „Výše prvotní splátky“.

Jakmile jsou všechna pole vyplněna, klikněte na tlačítko „Vytvořit návrh“. Po kliknutí na toto tlačítko
Odoo odhaluje: guilabel:„Návrh faktury zákazníkovi“.

.. důležité:
Pokud se zobrazí chybová hláška „Nesprávná operace“, zkontrolujte, že je
:doc:`fakturační politika <fakturace_politika> je správně nakonfigurována. V některých případech například
účetní politika je nastavena tak, aby dodání předcházelo fakturaci.

V záložce „Částka na faktuře“ v záložce „Návrh faktury zákazníkovi“ je uvedena záloha
Takové nastavení se objeví v okně „Vytvořit fakturu“.
:guilabel:`Produkt“.

..prodeje/fakturace/půlroční zálohy:

Příklad: požadovat 50% zálohu.
=================================

.. poznámka::
Příklad níže ukazuje, že na produkt (:guilabel:`Skříňka) je zapotřebí vložit 50 % z celkové částky.
Do položky „Dveře“ s hodnotou „Počet kusů“ jako „Způsob fakturace“.

.... obrázek::down_payment/cabinet-product-details.png
:synchronizace: střed
:alt:Skříň s dvířky, která prezentuje různé detaily a oblasti.

.. viz též:
:doc:`fakturační politika“

Nejprve přejděte na :menuselection:`Prodejní aplikace --> Nový“ a přidejte :guilabel:`Zákazník“.
citát.

Pak klikněte na tlačítko „Přidat produkt“ v záložce „Řádky objednávky“, vyberte
Produkt „Skříň s dveřmi“.

Pokud je objednávka potvrzena (pomocí tlačítka „Potvrdit“), nabídka se změní na prodej.
pořadí. Jakmile k tomu dojde, vytvořte a zobrazte fakturu klepnutím na tlačítko „Vytvořit fakturu“.

.. obrázek:down_payment/cabinet-sales-orders-confirmed.png
:align:center
:alt:Prodej skříněk s dvířky, objednávka potvrzená v aplikaci Odoo Sales.

Dále v okně „Vytvořit faktury“ vyberte možnost „Záloha“.
(procenta) a zadejte do pole „Výše první splátky“ hodnotu 50 %.

.. poznámka::
Přiřazený účet „Příjem“ lze změnit.

Více informací najdete v dokumentaci k tématu „změna účtu příjmů na sestupném seznamu“.
platby (<účet prodej/fakturace/změna účtu k příjmům>).

A:guilabel:Účet pro první splátku může být také nastaven na produktové kategorii. Pokud je takto nastavený, tento účet
prioritizovány.

Za poslední klikněte na tlačítko „Vytvořit návrh faktury“ a vytvořte si návrh faktury.

Kliknutím na tlačítko „Vytvořit návrh faktury“ se zobrazí návrh faktury, který obsahuje
úhrada jako položka v záložce „Faktura“.

Odtud lze fakturu potvrdit a odeslat kliknutím na „Potvrzení“.
Faktura mění stav z „Návrh“ na „Vystaveno“. Dále odhaluje nový
soubor tlačítek na horním okraji stránky.

.. obrázek:down_payment/vzorek faktury.png
:align:center
:alt: Vzorový faktura s uvedenou zálohou z Odoo Sales.

Z těchto tlačítek se platba zaznamená kliknutím na „Registrovat platbu“.

... obrázek:down_payment/register-payment-button.png
:align:center
:alt:Předvedení tlačítka Registrace platby na potvrzené faktuře zákazníka.

Provedením takového kroku se zobrazí okno „Registrace platby“, které je automaticky vyplněno
Nezbytné informace. Zkontrolujte poskytnuté údaje a upravte je v případě potřeby.
upravit. Když bude připraveno, klikněte na tlačítko „Vytvořit platbu“.

.. obrázek:down_payment/register-payment-pop-up-window.png
:align:center
:alt:Zobrazení okna přesunutého na horní lištu s tlačítkem pro vytvoření platby.

Po kliknutí na tlačítko „Vytvořit platbu“ se Odoo zobrazí faktura zákazníka s nově zeleným
:guilabel:`Platba“ v horním pravém rohu.

.. obrázek:down_payment/zakaznicka-faktura-zeleny-platebni-baner.png
:align:center
:alt:Faktura zákazníka s zeleným pruhem „Vyúčtováno“ v pravém horním rohu.

Nyní, když zákazník chce zaplatit zbývající část objednávky, musí být vystaven další faktura.
Vytvořit. K tomu se vraťte na prodejní objednávku přes „breadcrumby“.

Na prodejním příkazu je nová sekce „Úhrada zálohy“ v části „Příkaz k nákupu“.
Linii v záložce s částkou úhrady, která právě byla vyfakturována a zveřejněna.

.. obrázek: down_payment/down-payments-section-order-lines.png
:align:center
:alt:Sekce záloh v záložce objednávkových linií prodejní objednávky.

Dále klikněte na tlačítko „Vytvořit fakturu“.

V okně „Vytvořit faktury“ se objeví dvě nová pole:
„Už fakturováno“ a „Částka k fakturaci“.

.. obrázek:down_payment/create-invoices-pop-up-already-invoiced.png
:align:center
:alt:Možnost odečíst zálohu při vytváření faktur se objevuje na okně pro vytváření faktury v Odoo Sales.

Pokud zbývající částka je připravena k zaplacení, vyberte možnost „Standardní faktura“.
Vytvoří fakturu na přesnou částku potřebnou k dokončení celkové platby, jak je uvedeno v
políčko „Částka faktury“.

Jakmile je vše připraveno, klikněte na tlačítko „Vytvořit návrh faktury“.

Tím se zobrazí další stránka s názvem „Návrh faktury zákazníka“, kde jsou uvedeny všechny faktury.
Tento konkrétní prodejní příkaz v záložce „Výrobky“. Každá položka na faktuře zobrazuje
Potřebné informace k faktuře.

K dokončení proudu klikněte na tlačítko „Potvrdit“, které změní stav faktury z
Vyberte „Návrh“ a poté „Odesláno“. Pak klikněte na „Registrace platby“.

Znovu se objeví pole „Registrace platby“, ve kterém jsou všechna pole automaticky vyplněná
potřebné informace včetně zbývající částky k zaplacení objednávky.

.. obrázek:down_payment/second-register-payment-popup.png
:align:center
:alt:Druhé okno pro platbu z registru v Odoo Sales.

Po potvrzení této informace klikněte na tlačítko „Vytvořit platbu“. To zpřístupní finální
„Faktura zákazníka“ s zeleným „Ve splatnosti“ v horním pravém rohu.
Dále jsou obě zálohy přítomny v záložce „Splátky“.

.. obrázek:down_payment/druhy-doplatek-v-platebni-fakture.png
:align:center
:alt:Druhý zálohový faktura s platbou v bannerech prodeje v Odoo.

V tuto chvíli je proud kompletní.

.. poznámka::
Tento průtok je také možný s volbou „Pevná částka“.

.. důležité:
Pokud je použitá záloha s produktem, který má v účetním dokladu položku „Dodané množství“
politika a cena produktu převyšuje 50% zálohu (v naprosté většině případů).
Vytvoří se faktura.

U produktů s nižší cenou než 50 % z celkové částky bude požadována záloha.
mohou být odečteny při vystavování faktury zákazníkovi.

To proto, že by musely být dodány před vystavením konečné faktury.
Odoo neumožňuje negativní celkové částky faktur.

Pokud nebyla dodávka uskutečněna, vytvoří se „Kreditní zpráva“, která odstraní návrh
faktura vystavená po zaplacení zálohy.

Pro využití možnosti „Kreditní poznámka“ musí být nainstalována aplikace Inventura.
aby bylo možné potvrdit dodání. Jinak může být dodané množství zadáno ručně přímo
na prodejní objednávce.

...prodeje, fakturace a 100% záloh:

Příklad: požadovat 100% zálohu.
==================================

Proces žádosti o 100% zálohu je podobný jako proces nastavení zálohy ve výši :ref:`50%.
předplatba, ale s méně kroky.

.. poznámka::
100% záloha není totéž jako plná úhrada objednávky na prodej.

Pokud bude objednávka zaplacena standardním způsobem, nebude možné vystavit žádné další faktury.
bude vygenerován a nezobrazí tlačítko pro vytvoření faktury na objednávce.

Pokud tento příklad napodobíte, bude se na obrazovce zobrazovat tlačítko „Vytvořit fakturu“.
Pořádek. To proto, že Odoo očekává vytvoření další faktury po zaplacení zálohy.
úplné uhrazení objednávky.

V tomto příkladu je použito produktu *Instalace solárních panelů*.

Chcete-li nakonfigurovat 100% vklad, začněte tím, že se přesunete na: „Prodejní aplikace -> Nový“ a přidejte
Zákazníkovi do nabídky.

Poté klikněte na tlačítko „Přidat produkt“ v záložce „Dodací řádky“ a vyberte
„Instalace solárních panelů“.

Po kliknutí na tlačítko „Potvrdit“ se cenová nabídka změní v objednávku.
fakturu nyní můžete vytvořit kliknutím na tlačítko „Vytvořit fakturu“ v pravém horním rohu.

V okně „Vytvořit fakturu“ vyberte možnost „Záloha“.
(procento) a zadejte do pole „Výše první splátky“ hodnotu 100.

.. obrázek:down_payment/100p-down-payment-percentage.png
:align:center
:alt:Volba první splátky (v procentech) s nastavením 100 % jako první splátky.

Dále klikněte na tlačítko Vytvořit návrh faktury a vytvořte návrh faktury. To také přinese
vizuální náhled faktury, která zahrnuje položku „Záloha“ jako „Produkt“ v
:guilabel:„Řádky faktury“

Fakturu lze nyní potvrdit a odeslat kliknutím na tlačítko „Potvrzení“. Potvrzení faktury
změní stav z „Návrh“ na „Zveřejněno“. Dále odhalí novou řadu
tlačítka v horní části stránky.

Placení lze zaregistrovat kliknutím na tlačítko „Registrace platby“.

Provedením takového kroku se zobrazí okno „Registrace platby“, které je automaticky vyplněno
Nezbytné informace. Zkontrolujte, zda jsou údaje správné a upravte je v případě potřeby.
upravit. Když bude připraveno, klikněte na tlačítko „Vytvořit platbu“.


Po kliknutí na tlačítko „Vytvořit platbu“ se Odoo zobrazí faktura zákazníka s nově zeleným
:guilabel:`Platba“ v horním pravém rohu.

.. obrázek:down_payment/100p-faktura.png
:align:center
:alt:Faktura zákazníka s zeleným pruhem „Vyúčtováno“ v pravém horním rohu.

Proces je nyní u konce a úspěšně byla aplikována 100% záloha.

...úpravu prodeje, fakturace a účtu příjmů:

Úprava příjmů u hypoték s nižšími splátkami
============================================

Chcete-li změnit nebo upravit účet příjmů připojený k stránce produktu „Úhrada v hotovosti“,
Aplikace pro účetnictví **musí být** nainstalována.

Přejděte na stránku „Produkty“ („Prodejní aplikace –> Produkty –> Produkty“)
Vyhledejte produkt „Úložné poplatky“ v vyhledávacím poli a zvolte jej pro zobrazení podrobností o produktu.
stránka.

Pokud je nainstalována aplikace „Účetnictví“, pak se v produktu objeví záložka „Účetnictví“.
stránka.

V záložce „Účetnictví“ lze v poli „Příjem“ měnit účet.
Konta“ v sekci „Příjmy“.

.. obrázek:vklad/příjem.png
:align:center
:alt:Jak upravit odkaz na účet příjmů pro splátky.

.. viz též:
:doc:`fakturační politika“
