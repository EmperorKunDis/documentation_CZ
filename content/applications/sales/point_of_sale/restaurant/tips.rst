====
Tipy
====

Dávat si na víc je v mnoha zemích zvykem. POS umožňuje dát si na víc ve :ref:`prodejnách <pos/sell>
„bary“ nebo „restaurace“.

.. konfigurace:

Konfigurace
=============

Chcete-li přijímat tipy v terminálu, aktivujte funkci „Tip“ v nabídce „Prodejna“.
Konfigurace > Nastavení“. V horní části stránky vyberte POS, ve kterém chcete povolit
Pokud chcete přidat tip, klikněte na tlačítko „Tip“ a v sekci „Platba“ vyberte možnost „Tip“.
Povolte, přidejte pole „Tip produktu“ a uložte. Vybraný produkt
bude sloužit jako referenční cena na účtenkách zákazníků.

.. obrázek: tips/tips-setup.png
:alt: umožnit u pokladny tipy

.._tip-produkt:

Tip produktů
------------

Produkty **tipu** se vytváří na místě. Pro jejich vytvoření stačí zadat název produktu do odkazu :ref:`Tip
V poli „Konfigurace produktu“ klikněte na tlačítko Vytvořit nebo stiskněte klávesu Enter. Produkt
automaticky konfigurována tak, aby se zobrazila jako tip na obrazovce platby.

Pokud chcete v reálném čase vybírat produkty na konec řady, musíte aktivovat
**K dispozici v nastavení POS**. Chcete-li tak učinit, klikněte na tlačítko „Vytvořit a upravit…“, abyste otevřeli produkt
konfigurační formulář. Pak přejděte na záložku „Prodej“, zaškrtněte políčko „Dostupné v POS“
zaškrtávací políčko a klikněte na tlačítko „Uložit a zavřít“.

.. poznámka::
   - Když vytváříte produkt, který chcete použít jako odměnu, nechte typ produktu nastavený na :guilabel:`Consumable`
aby se předešlo zbytečným pohybům zásob.
   - Můžete si vybrat pouze jeden produkt na jedné prodejně, ale můžete si vybrat jiný v každé z nich.

Tip přes terminál Adyen
---------------------------

Pokud používáte platební terminál Adyen a chcete jej zapnout
Pokud chcete přidat tip prostřednictvím terminálu, zkontrolujte níže uvedený
:ref:`nastavení tipů <konfigurace>“.

Tip po zaplacení
-----------------

Pokud používáte POS systém v barech nebo restauracích, můžete zapnout možnost „Přidat spropitné po platbě“.
(Specifická pro Severní Ameriku). Tímto způsobem vytvoří fakturu, kterou musí zákazník vyplnit ručně.
a číšník. Tato částka uvádí hodnotu odměny, kterou si zákazník vybere po zaplacení.

.. důležité:
Pro využití této funkce musí mít zvolený způsob platby přiřazeno bankovní deník.

Přidejte tipy
========

Přidat tip k objednávce: přejděte na obrazovku platby pomocí odkazu „<pos/sell>“ a klikněte na „♥ Tip“.
Poté zadejte částku spropitného, klikněte na „Potvrdit“ a zpracujte platbu.

.. obrázek:tips/add-tip.png
:alt:tip okno s pop-up

Alternativně můžete vybrat produkt „Tip“ na pokladním terminálu a přidat ho do
kartu. Vybraný produkt se automaticky nastaví jako dárek a jeho výchozí hodnota je rovna
Prodejní cena.

Tip přes terminál Adyen
---------------------------

Při placení vyberte jako platební terminál Adyen a požadavek na platbu odešlete
zařízení kliknutím na „Odeslat“. Klientům je požadováno zadat požadovanou částku.
na obrazovce terminálu před provedením platby.

Tip po zaplacení
-----------------

Při placení vyberte platební metodu kartou a klepněte na tlačítko „Zavřít záložku“. Tímto způsobem vytvoříte fakturu
Dokončit na objednávku zákazníka.

.. obrázek: tips/tipovani-na-faktuře.png
:alt:doplatit účet po zaplacení doplatí zákazník

Na další obrazovce klikněte na procento (zde je uvedeno 15 %, 20 % a 25 %).
„Žádný tip“, nebo zadejte částku, kterou si zákazník vybral jako odměnu. Pak klikněte
:guilabel:Přesunout na následující řádek.

.. obrázek: tipy/tip-po-platbě.png
:alt: obrazovka pro výběr částky, kterou chcete vybrat po zaplacení
