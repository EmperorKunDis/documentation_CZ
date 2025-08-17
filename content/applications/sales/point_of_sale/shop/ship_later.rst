==========
Loď později
==========

Funkce „Později“ umožňuje prodávat produkty a plánovat dodání na pozdější datum.
Užitečné například v případě, že je produkt vyprodán nebo tak objemný, že jej nelze zaslat.
nebo pokud zákazník potřebuje objednávku odeslat později atd.

Konfigurace
=============

:ref:`Přejděte do nastavení POSu <konfigurace/nastavení>“, posouvejte dolů až k „Sklad“
sekci a zapněte možnost „Povolit dodání později“.

.. obrázek:ship_later/settings.png
:skalka: 85 %
:alt: nastavení, které umožní později aktivovat a nakonfigurovat funkci lodi

Jakmile je aktivován, můžete:

- Vyberte místo, odkud jsou produkty odesílány, vybráním:guilabel:Skladu.
- Určete specifickou trasu, nebo pole nechte prázdné pro použití výchozí trasy.
- Definujte politiku dopravy; vyberte možnost „Co nejdříve“ v případě produktů
mohou být dodány samostatně nebo v případě, že jsou všechny produkty připraveny k odeslání, může být objednávka
pouze jednou.

.. viz též:
   - :doc:`../../../inventar-a-mrp/inventar/versand-und-empfang/konfiguration`
   - :doc:`../../../skladovani-a-plánování-výroby/sklady-a-úložiště/správa-zásob/sklady/sklady`

Praktické využití
=====================

#Otevřete sezení (<pos/session-start>) a uzavřete prodej.
#Na platební obrazovce nastavte zákazníka a vyberte možnost „Pošlete později“.
#V okně vyskakovacího okna nastavte datum dodání a klikněte na tlačítko „Potvrdit“.

.. obrázek: lod_pozdeji/platba.png
:skalka: 75 %
:alt: výběr lodi později v průběhu objednávky.

Systém okamžitě vytvoří dodací příkaz z skladu na adresu odeslání.

.. Poznámka:
Vybraný zákazník musí mít v systému zadanou adresu, na kterou bude produkt zaslán.
