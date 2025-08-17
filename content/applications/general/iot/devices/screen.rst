================
Připojit obrazovku
================

V Odoo lze k obrazovce připojit IoT box. Po zapnutí
pokud je konfigurována, může být obrazovka použita k zobrazení objednávky Point of Sale (PoS) pro klienta.

.. obrázek:: obrazovka/obrazovka-pozice-klienta-displej.png

Příklad objednávky na prodejním místě na obrazovce.

Přihlaste se k displeji zákazníka přes stránku domovské stránky „IoT (Internet věcí)“.
kliknutím na tlačítko „PoS Display“. Chcete-li se dostat k poli „IoT (Internet věcí)“
domovská stránka, přejděte na: „Výběr aplikace“ --> „IoT box“ a klikněte na: „IoT (internet věcí)“.
Odkaz na domovskou stránku boxu „Věcí“.

Připojení
==========

Připojení obrazovky k internetu věcí se liší podle
na modelu.

.. záložky::

...... tab::IoT Box model 4

Připojte až dva displeje pomocí kabelů micro-HDMI na straně zařízení:abbr:`IoT (Internet věcí).
„Věci“). Pokud jsou dva displeje propojeny, mohou zobrazovat různý obsah (viz
:ref:`Použití obrazovky <iot/usage_screen>`.

... tab:: IoT box model 3

Připojte obrazovku kabelem HDMI na straně IoT boxu.

.. viz též:
:ref:`Viz schéma Raspberry Pi <pos/pos_iot/connect_schema>.

.. důležité::
Před zapnutím zařízení IoT Box by měly být připojeny obrazovky.
je již zapnutá, připojte obrazovku a pak restartujte „IoT (Internet věcí)“
zásuvku na deset sekund a poté ji opět připojte k napájení.

.. varování:
Používání adaptérů HDMI/micro-HDMI může způsobit problémy, které vedou k černé obrazovce.
na obrazovce. Použití konkrétního kabelu pro připojení je doporučeno.

Pokud byla spojení úspěšná, měl by se na obrazovce zobrazit :guilabel:`Zobrazení POS klienta`.
obrazovka.

.. obrázek: obrazovka/obrazovka-pozice-klienta-displej-bez-řazení.png
:align:center
:alt:Výchozí obrazovka „Display POS Client“ se zobrazuje, když je úspěšně zobrazena obrazovka.
spojené s internetovým boxem.

Obrazovka by se také měla objevit v seznamu :guilabel:`Zobrazovače` na :abbr:`IoT (Internet věcí)
Výběr „Domov“ na domovské stránce nebo můžete zobrazit v aplikaci IoT přístupem k: menu: „IoT
-->Zařízení“.

.. obrázek: obrazovka/obrazovka-jméno-příklad.png
:align:center
:alt:Příklad zobrazení názvu obrazovky na stránce domovské stránky IoT Box.

.. poznámka::
Pokud není detekován žádný monitor, bude zobrazen výchozí displej s názvem :guilabel:`Vzdálený displej`.
V tomto případě se zobrazí chybová hláška „Nebyl nalezen žádný hardware monitor“.

.. obrázek:: obrazovka/obrazovka-bez-obrazovky.png
:srovnání: střed
:alt:Pokud není detekován žádný monitor, bude použito jméno obrazovky „Vzdálené zobrazení“.

.. _IoT/použití obrazovky:

Použití
=====

Zobrazte zákazníkům objednávky z bodu prodeje
--------------------------------------

Pro použití obrazovky v aplikaci „Pokladna“, přejděte na:
Konfigurace --> Prodejní místo“, vyberte „PoS (Prodejní místo)“, klikněte na „Upravit“
je nezbytné a umožňuje funkci „IoT Box“.

Vyberte obrazovku z rozevírací nabídky :guilabel:`Zákaznická obrazovka`. Pak klikněte
Pokud je třeba, uložte soubor.

.. obrázek: obrazovka/obrazovka-pozice-obrazovky-konfigurace.png
:align:center
:alt:Připojte obrazovku k aplikaci POS.

Teď je možné na obrazovce používat funkci :abbr:`PoS (Point of Sale)“.
menu v horní části obrazovky, které ukazuje stav připojení obrazovky.

.. obrázek: obrazovka/obrazovka-pozice-ikonky.png
:align:center
:alt: Ikona „obrazovka“ na displeji pokladny ukazuje stav připojení k
obrazovka.

Na obrazovce se automaticky zobrazí objednávky PoS a aktualizují se při změnách
Jsou vyráběny na zakázku.

.. obrázek: obrazovka/obrazovka-pozice-klienta-displeje.png
:align:center
:alt: Příklad PoS objednávky na obrazovce.

Zobrazit webovou stránku na obrazovce
-------------------------------

Otevřete obrazovku s výběrem zařízení přístupem do nabídky „IoT aplikace --> Zařízení --> Zákaznická obrazovka“.
Uživatelé si mohou vybrat konkrétní webovou adresu, která se zobrazí na obrazovce pomocí
Pole „Zobrazit URL“.
