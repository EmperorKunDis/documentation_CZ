===============
Správa vkladů
===============

Povinnost vkládat peníze na účet je běžná v mnoha pronájmech, například při vybírání kauce.

Tento dokument popisuje základní možnosti konfigurace:ref:`<rental/manage_deposits/config>`
souhrnně jako „vrácení“ a „výplata“.
Vrácení zálohy v aplikaci Rentals.

.. _pronájem/správa vkladů/konfigurace:

Konfigurace
-------------

Nejprve vytvořte produkt „vklad služby“ pro každý pronajatý produkt, který vyžaduje vklad.

Pro toto vyberte v nabídce „Pronájem“ položku „Produkty“ a vytvořte nový produkt.

Na produktové kartě zadejte název produktu, který naznačuje, že se jedná o vklady.

Příklad:
Pokud je produkt služby vkladu určen pro výpůjční produkt *Digitální fotoaparát*, pak by se měl jmenovat
bude zadána jako „vklad digitální kamery“.

Dále nastavte pole „Produktová skupina“ na „Služba“, pole „Způsob fakturace“ na
„Dodané množství“ a pak přiřadit „Prodejní cenu“ s částkou
Vyberte, zda chcete nebo nechcete zahrnout položku „Dodatečné daně“ do této zálohy.
služba, produkt.

Konečně uložte produkt služby depozitu pomocí ikony „fa-cloud-upload“ a potvrďte tlačítkem „Uložit“.

.. _pronájem/správa vkladů/produkt:

Sbírat vklady z doplňkového produktu
-----------------------------------------

Ve formuláři pronájmu se přesuňte na zálohu a přidejte službu :ref:`záloha
produktu <pronájem/správa záloh/konfigurace> do sekce „Volitelné produkty“.

Ujistěte se, že nastavíte ceny pronájmu produktů na záložce „Ceník pronájmu“ (viz Rental prices).

S výše uvedenou konfigurací lze vytvořit objednávku pronájmu: :ref:`<rental/order>`.

.. důležité:
Po výběru pronájmu v záložce „Dodací lístky“ se ujistěte, že kliknutím na ikonku „+“
:guilabel:`Přidat“ službu vkladu do položky „Nastavte svůj produkt“.

Pop-up „Nastavte svůj produkt“ se zobrazí pouze v případě, že je doplňkový produkt nastaven na
půjčovna.

..tip:
Pokud je nainstalována e-commerce (viz :doc:`eCommerce <../../websites/ecommerce>`) přidejte :guilabel:`Ecommerce
Popis, který uvádí, že záloha je vyžadována v kartě „Prodej“ produktu pronájmu.

Když zákazník přidá pronajatý produkt do košíku, zobrazí se mu tlačítko „Upravte svůj produkt“.
pop-up zobrazuje produkt služby vkladu pod názvem „Dostupné možnosti“.

Jakmile zákazník klikne na ikonu „nákupní košík“ a zvolí možnost „Přidat do pronájmu“,
Přiřazení produktu služby vkladu do nákupního košíku.

.. obrázek: manage_deposits/optional-product.png
:alt:Produkt služby vrácení zálohy uvedený v cenové nabídce pronájmu.

.. _pronájem/správa vkladů/vrácení peněz:

Vrácení kauce při vrácení
---------------------------

Jakmile zákazník vrátí zapůjčený produkt, vrátí se jim jejich vratná kauce.
:doc:`faktura s kreditem <../../finance/accounting/customer_invoices/credit_notes>“ z faktury.
změňte dodané množství na 0 v propojeném objednávkovém dokladu.
