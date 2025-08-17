========
Hardware
========

Odoo Point of Sale podporuje integraci s různými typy hardwaru včetně platebních terminálů.
přístupové terminály a pokladní systémy, ale také :doc:`zobrazovací zařízení pro zákazníky.
<shop/customer_display>`, :ref:`váhy <pos/scale>`, :doc:`snímače čárových kódů <shop/barcode>
tiskárny ePOS (konfigurace/epos_printers) a v obchodě elektronické etikety
<ceny/elektronické etikety>.

.._pos/velikost:

Měřítko
=====

.. důležité:
V členských státech EU je certifikace právně vyžadována.
<https://eur-lex.europa.eu/legal-content/CS/ALL/?uri=CELEX:52014PC0096_01_0107>
použít stupnici jako integrovaný přístroj.

Předpoklad
------------

Připojení váhy vyžaduje použití systému **Internet věcí**.

.. viz též:
   - :doc:`../../obecne/internet-veci/pripojeni`
   - :doc:`../../obecne/iot/zarizeni/vahy`

Konfigurace
-------------

Připojení stupnice
~~~~~~~~~~~~~~~~

#:ref:`Přejděte do nastavení POS <konfigurace/nastavení>.
#Přejděte dolů do sekce „Připojená zařízení“ a zapněte „IoT Box“.
#Vyberte měřítko v poli „Elektronická váha“.
#Klikněte na tlačítko „Uložit“.

..tip:
Alternativně klikněte na ikonu „fa-ellipsis-v“ („Záložka“) v POS kartě.
Klikněte na tlačítko „Upravit“ pro přístup k této nastavení.

Konfigurace produktu
~~~~~~~~~~~~~~~~~~~~~

Pro vážení produktů pomocí vestavěné váhy přejděte na:
Produkty --> Produkty“, vytvořit produkt nebo otevřít existující formulář pro produkt a nakonfigurovat jej takto
následuje:

#Zajistěte, aby byla aktivní políčka „Prodejní místo“ u produktu.
POS.
#Na kartě „Obecné informace“ nastavte cenu za kilogram.

....... poznámka::
Tento krok vyžaduje zapnutí jednotek měření:
funkci „Nastavení jednotek měření“ (<../../inventory_and_mrp/inventory/product_management/configure/uom>). Chcete-li ji aktivovat,

      #Přejděte na: „Nastavení“ -> „Konfigurace“ -> „Výběr menu“.
      #Přejděte dolů do sekce „Produkty“ a aktivujte „Jednotky měření“.
#Přejděte na kartu „Prodejní místo“ a aktivujte „Zvážit s váhou“.
Díky tomu lze produkt vážit přímo na připojené váze v místě prodeje.

.. důležité:
Pro zvážení musí být vybrána jednotka měření:guilabel:'kg', aby bylo zajištěno soulad
s evropskými předpisy.

.. viz též:
:doc:`../inventar-und-mrp/Inventar/Produktverwaltung/Konfigurieren/Einheit`

Evropské předpisy
--------------------

Při použití vah pro obchodní transakce musí být databáze integrována s váhou.
konfigurována tak, aby splňovala specifické požadavky Evropy. To zahrnuje podporu alespoň tří desetinných míst
místo přesnosti a používání správného způsobu zaokrouhlování pro jednotky měření, jako například „kg“ místo obecného
„jednotky“.

Pokud databáze nesplňuje požadavky, zobrazí se červený ikonka „váha“ (:guilabel:"váha")
jako varování. Klikněte na tento ikonu pro zobrazení důvodů nesouladu a poté vyberte
:guilabel:`Použít změny“ k automatickému použití potřebných změn nastavení.
databáze splňuje všechny regulační požadavky.
zelená.

.. obrázek: pos_hardware/legal-requirements.png
:skalka: 75 %

.. varování: Další pokyny

Obě, jak :doc:`zákazník <shop/customer_display>`, tak i POS displeje musí mít minimální úhlopříčku
velikosti 15 centimetrů. Pro optimální čitelnost se doporučují větší displeje.

Použití stupnice v PoS
--------------------

#:ref:`Zahájit sezení s terminálem <pos/session-start>“.
#Vyberte produkt, který chcete vážit na obrazovce objednávky nebo naskenujte jeho čárový kód.
#Umístěte produkt na váhu a počkejte, až se hmotnost zobrazí v okně s popisem.
#Jakmile je stanovena hmotnost, cena se automaticky vypočítá.
#Klikněte na tlačítko „Objednat“ a přidejte produkt do košíku.
#Odeberte předchozí produkt ze vah.

.. obrázek: pos_hardware/weigh.png
:alt: vážící okno
:skalka: 85 %

.. důležité:
Přesvědčte se, že váha vrátí nulu před vážením nového produktu. Pokud ne,
:guilabel:`Objednávka“ :icon:`fa-angle-double-right` tlačítko zůstane neklikatelné, dokud není resetováno.
