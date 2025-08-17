===========================
Využijte elektronické peněženky a dárkové karty
===========================

Společnost Odoo umožňuje zákazníkům používat elektronické peněženky a dárkové karty pro nákupy v obchodech i na internetu.

Pro umožnění elektronických peněženek a dárkových karet pro elektronický obchod a bod prodeje (PoS) nejprve zapněte
„Slevy, věrnostní program a dárkové karty“ pod „Prodejní aplikace --> Konfigurace -->
Nastavení --> Ceník --> Vybrat možnost „Dárkový poukaz“
platební kartu nebo elektronickou peněženku a zvolte možnost „Vytvořit“ novou platební kartu nebo elektronickou peněženku.

ePeněženky
========

E-peněženky umožňují zákazníkům ukládat kredity na svůj účet online a tyto kredity pak používat jako platbu
metoda při nákupu zboží v internetovém obchodě nebo kamenné prodejně. Elektronické peněženky lze také použít
sloužit k centrálnímu uložení více :ref:`dárkových karet <ewallet_gift/gift-cards>“.

Před vytvořením elektronické peněženky je nutné vytvořit produkt pro doplnění elektronického portmonka (eWallet top-up).
Jedná se o předem definované digitální hodnoty kreditů, které jsou přidány na virtuální peněženku vyměněné za jejich ekvivalent v reálném světě.
měna. Tyto kredity pak lze využít jako způsob platby v elektronickém obchodě nebo na PoS
„Prodejní místo“. Připíjení lze provést v různých hodnotách.

Příklad:
Top-up v hodnotě 50 USD lze zakoupit za stejnou částku a přidá tuto částku kreditu na elektronickou peněženku.

Pro vytvoření doplňkového produktu přejděte na: „Prodejní aplikace --> Produkty --> Produkty“.
Vytvořte nový produkt. V šabloně produktu nakonfigurujte možnosti takto:

- :guilabel:`Název produktu“: zadejte název pro doplňkový produkt (například „$ 50 Top-Up“)
- :guilabel:`Může být prodáno“ povoleno
- Vyberte: „Produkt“
- :guilabel:`Způsob fakturace“: vyberte „Předplatné / pevná cena“
- Vyberte možnost „Nic“
- :guilabel:`Prodejní cena“: zadejte částku doplatku

.. poznámka::
Pro účely různých částek na dobíjení eWalletu vytvořte více produktů pro dobíjení.
upravit pole „Prodejní cena“ podle toho.

Jakmile je doplněk vytvořený, přejděte na: „Prodejní aplikace --> Zboží --> Dárkové karty a elektronické peněženky“
Vytvořit aplikaci pro elektronickou peněženku. Následující možnosti konfigurace jsou k dispozici:

- :guilabel:`Název programu“: zadejte název pro program eWallet
- :guilabel:`Typ programu“: vyberte „E-peněženka“
- :guilabel:`Produkty elektronické peněženky“: vyberte předchozí dobíjenou elektronickou peněženku. Opakujte proces, pokud
Vytvořili jste si různé doplňky v různých výších.
- :label_guid:Šablona e-mailu“: vyberte šablonu e-mailu, kterou se bude používat pro odesílání e-mailů zákazníkům.
Vytvořte nový šablonu, klikněte na pole, vyberte „Hledat více“ a pak klikněte
:guilabel:`Vytvořit“.
- :guilabel:`Měna“: vyberte měnu, kterou chcete použít pro program eWallet
- :guilabel:`Společnost“: vyberte společnost, pro kterou je program platný a dostupný
- :guilabel:`K dispozici na:“ vyberte aplikace, pro které je program platný a dostupný
- :guilabel:`Webová stránka“: vyberte webovou stránku, na které je program platný a dostupný.
Vyplňte pole prázdné, pokud chcete zahrnout všechny weby.
- :guilabel:`Prodejní místo“: vyberte „PoS (prodejní místo)“, na kterém je platnost programu
a dostupné. Nechte pole prázdné, pokud chcete zahrnout všechny PoS (prodejní místa).

.. obrázek: ewallets_giftcards/ewallet-configuration.png
:align:center
:alt: konfigurační stránka programu eWallet

Jakmile je program nakonfigurován, klikněte na tlačítko „Vytvořit peněženku“ v pravém horním rohu.
k vytvoření elektronických peněženek. Elektronické peněženky lze vytvářet na základě :guilabel:`Zákazníků` a nebo
„Zákaznická štítka“. Množství se automaticky přizpůsobí podle
Zvolte „Zákazníci“ a „Štítky zákazníků“. Poté nastavte „E-peněženku“.
hodnota“. Nakonec nastavte dobu platnosti, pokud je to nutné.

Vytvořené virtuální peněženky lze přistupovat pomocí tlačítka „eWallet“ v pravém horním rohu.
Koutek. Zde můžete buďto :guilabel:`Odeslat` nebo :guilabel:`Sdílet“ e-peněženky prostřednictvím e-mailu nebo odkazu na webové stránce.

.. obrázek: ewallets_giftcards/ewallet-share.png
:align:center
:alt:Tlačítka pro odesílání a sdílení

Klikněte na elektronickou peněženku, abyste změnili datum expirace, partnera nebo
:guilabel:`Záloha“. Kód peněženky *nemůže být* změněn, smazán nebo zkopírován.

... _ewallet_gift/dárkové karty:

Dárkové karty
==========

Dárkové karty lze zakoupit zákazníky a následně je použít jako způsob platby při placení v obchodě.
E-shop nebo PoS (Místo prodeje).

Před vytvořením nového programu dárkových karet je nutné nejprve vytvořit dárkové karty jako produkt.
to udělejte, přejděte na „Prodejní aplikace“ -> „Produkty“ -> „Produkty“ a vytvořte produkt.
V šabloně produktu nastavte možnosti následovně:

- :guilabel:`Název produktu“: zadejte název pro dárkovou kartu
- :guilabel:`Může být prodáno“ povoleno
- Vyberte: „Produkt“
- :guilabel:`Způsob fakturace“: vyberte „Předplatné / pevná cena“
- Vyberte možnost „Nic“
- :guilabel:`Prodejní cena“: zadejte částku dárkové karty

.. poznámka::
Pro vytvoření dárkových karet různé hodnoty je nutné vytvořit více produktů s dárkovými kartami a upravit
Přepočítává se podle ceny prodeje (viz guilabel Sales Price).

Jakmile je produkt dárkové karty vytvořený, přejděte na: Menu: Sales app --> Products --> Gift cards
a „Vytvořit dárkovou kartu“. Následující konfigurační možnosti jsou
Dostupné:

- :guilabel:`Název programu dárkové karty“: zadejte název pro program dárkových karet
- :guilabel:`Druh programu“: vyberte „Dárková karta“
- :guilabel:`Dárkové karty“: vyberte dárkovou kartu, kterou jste vytvořili dříve. Opakujte proces
pokud byste vytvořili dárkové karty různých hodnot.
- :guilabel:`Šablona e-mailu“: vyberte výchozí „Dárkový poukaz: Informace o dárkovém poukazu“
šablonu nebo vytvořit novou šablonu kliknutím na pole, výběrem „Hledat více“
a pak klikněte na tlačítko :guilabel:`Create`.
- Vyberte možnost „Dárková karta“.
- :guilabel:`Měna“: vyberte měnu, kterou chcete použít pro dárkový program
- :guilabel:`Společnost“: vyberte společnost, pro kterou je program platný a dostupný
- :guilabel:`K dispozici na:“ vyberte aplikace, pro které je program platný a dostupný
- :guilabel:`Webová stránka“: vyberte webovou stránku, na které je program platný a dostupný.
Vyplňte pole prázdné, pokud chcete zahrnout všechny weby.
- :guilabel:`Prodejní místo“: vyberte „PoS (prodejní místo)“, na kterém je platnost programu
a dostupné. Nechte pole prázdné, pokud chcete zahrnout všechny PoS (prodejní místa).

.. obrázek: ewallets_giftcards/giftcard-configuration.png
:align:center
:alt: Konfigurační stránka dárkové karty

Jakmile je program nakonfigurován, klikněte na tlačítko „Vytvořit dárkové karty“ v horním levém rohu.
rohu, který generuje dárkové karty. Dárkové karty lze vytvořit buď pro:guilabel: Anonymous
Zákazníci nebo Vybraní zákazníci. Zadejte množství pro tisk
„Nekontrolovaní zákazníci“, nebo vyberte „Zákazníky“ a/nebo „Klienty“.
Poté nastavte hodnotu dárkové karty pomocí :guilabel:„Hodnota dárkové karty“.
Datum platnosti, pokud je k dispozici.

Vytvořené dárkové karty lze zobrazit pomocí tlačítka „Dárková karta“ v
v pravém horním rohu. Zde můžete buďto kartu odeslat e-mailem nebo sdílet prostřednictvím
URL odkaz.

.. obrázek: ewallets_giftcards/giftcard-share.png
:align:center
:alt:Tlačítka pro zaslání a sdílení dárkových karet

Klikněte na dárkovou kartu, abyste změnili :guilabel:`Datum vypršení platnosti`, :guilabel:`Dodavatele“ nebo
„Záloha“. Kód dárkové karty nelze měnit, mazat ani přesouvat.
duplikované.
