=====================
Faktury a daňové doklady
=====================

Pokladní doklady
========

Nastavte účtenky přes: „Prodejna - Konfigurace - Prodejna“.
vybrat bod prodeje (POS) a posunout se dolů do části „Faktury a příjmy“.

Pro přizpůsobení hlavičky a patičky aktivujte :guilabel:`Hlavička a patka“ a vyplňte
obě pole s informacemi, které se mají tisknout na účtenku.

Pro automatické tisknutí účtenek po zaregistrování platby zapnout:
Nastavení tisku účtenek.

.. obrázek: faktury/faktura.png
:skalka: 75 %
:alt: EET účtenka

.. viz též:
   - :doc:`restaurace/tisk faktury“
   - :doc:`konfigurace/tiskárny epos“

Reprodukovat účtenku
-----------------

V rozhraní POS klikněte na položku „Objednávky“, otevřete výběrové menu vedle
vyhledávací lištu a změnit výchozí filtr na „Zaplaceno“. Poté
Vyberte příslušný účet a klikněte na tlačítko „Tisk faktury“.

.. obrázek: faktury/tisk-faktury.png
:alt: Tlačítko pro tisk účtenky z administrace

.. poznámka::
Seznam objednávek lze filtrovat pomocí vyhledávacího pole. Zadejte své referenční číslo a klikněte
:guilabel:`Číslo faktury“, :guilabel:`Datum“ nebo :guilabel:"Klient".

... faktury:

Faktury
========

Point of Sale umožňuje vystavit a tisknout faktury pro registrované zákazníky.
Po zaplacení a získání všech dříve vystavených faktur.

.. poznámka::
Faktura vytvořená na pokladně vytváří záznam do příslušného účetního deníku
„<slovník podvodníka/deník>“, dříve „nastavení <pokladny/konfigurace faktury>“.

... faktury/nastavení faktur:

Konfigurace
-------------

Pro definování časopisů pro konkrétní POS přejděte do nastavení POS.
a posuňte se dolů do části účetnictví. Pak můžete určit
účetní deníky používané výchozím způsobem pro objednávky a faktury v seznamu „Výchozí deníky“
část.

.. obrázek: faktury/faktura-konfigurace.png
:alt: účetní sekce v nastavení POS

Fakturovat zákazníka
------------------

Při zpracování platby klikněte pod jménem zákazníka na položku „Faktura“
fakturu za tento nákup.

Vyberte způsob platby a klikněte na „Zkontrolovat“. Faktura se vám automaticky vystaví.
a připravené ke stažení a tisknutí.

.. poznámka::
Pro vystavení faktury je třeba vybrat :ref:`zákazníka <pos/customers>`.

Získat faktury
-----------------

Pro získání faktur ze **dashboardu POS**

#Přístup k všem objednávkám, které byly vytvořeny prostřednictvím vašeho POS, získáte přes:
„Příkazy“
#Chcete-li zobrazit fakturu objednávky, otevřete formulář objednávky kliknutím na
:guilabel:`Faktura“.

.. obrázek: faktury/tlačítko_chytře.png
:alt: tlačítko chytré faktury z objednávkového formuláře

.. poznámka::
   - Objednávky s fakturou lze identifikovat podle stavu „Zaplaceno“ v
:guilabel:`Stav“ sloupec.
   - Seznam objednávek lze filtrovat kliknutím na tlačítko „Filtry“.
:guilabel:`Faktura“.

QR kódy pro vystavení faktury
-----------------------------

Zákazníci si mohou také vyžádat fakturu, když na svém dokladu odečtou QR kód.
Při skenování musí vyplnit formulář se svými údaji o fakturaci a kliknout na „Získat můj
faktura“. Na jednu stranu tak vzniká faktura k stažení. Na druhou stranu
Stav objednávky se mění z :guilabel:`Uhrazeno“ nebo :guilabel:`Odesláno“ na :guilabel:`Fakturováno“.
Odoo Backend.

.. obrázek: faktury/objednávka-stav.png
:alt: změna stavu objednávky

Pro využití této funkce je nutné zapnout kódy QR na účtenkách přes „Nastavení“ > „Správa účtu“ > „Účetní
Prodej --> Konfigurace --> Nastavení“. Pak vyberte bod prodeje v poli „Bod prodeje“
Přejděte dolů do sekce „Faktury a příjmy“ a zapněte „Použít QR kód na
lístek.
