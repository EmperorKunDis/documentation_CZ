=====================
Systémová integrace IoT
=====================

Propojit POS s :doc:`systémem IoT </aplikace/obecné/iot>“:

#Ujistěte se, že máte aplikace pro prodejní místo a internet věcí (IoT) nainstalované na svém
databáze.
#Nastavte aplikaci:doc:`/applications/general/iot/iot_box` nebo
:doc:`/aplikace/obecné/iot/windows_iot`.
#Připojte periferní zařízení k systému Internetu věcí:

...... seznamová tabulka::
:hlavičkové řádky: 1
:kolonky: 1

      * - Zařízení
        - Návod
      * – Tiskárna
        - Připojte podporovaný tiskárnu účtenek k portu :abbr:`USB (Universal Serial Bus)` nebo
do sítě a zapněte ji. Sledujte :doc:`../restaurant/kitchen_printing`.
      * - Pokladna
        - Papírový výstup by měl být připojen k tiskárně pomocí kabelu RJ25.
      * -Čtečka čárových kódů
        - Skenovač čárových kódů musí na konci čárového kódu obsahovat znak „Enter“ (klávesová zkratka 28), aby
aby snímač čárových kódů byl kompatibilní. To je nejspíš výchozí nastavení snímače
konfigurace.
      * -Měřítko
        - Připojte váhu a zapněte ji. Sledujte: /applications/general/iot/devices/scale
      * – Zákaznický displej
        - Připojte obrazovku k IoT boxu, aby se na ní zobrazil PoS.
(Příkaz k prodeji). Viz: /aplikace/obecné/IoT/zařízení/monitor.
      * -Platební terminál
        - Proces připojení závisí na terminálu. Podívejte se na :doc:`platební terminály
dokumentace </prodej/pokladna/platební metody>.

#:doc:`Připojte systém IoT k databázi Odoo </applications/general/iot/connect>“.
#Přejděte do nastavení POS a vyberte svůj POS nebo klikněte na
tlačítko vertikální elipsy (:guilabel:`⋮`) na platební kartě a klikněte na „Upravit“. Posuňte se dolů
Do sekce „Připojená zařízení“ zapněte „IoT Box“, pak vyberte zařízení.
k použití na pokladně. Klikněte na tlačítko „Uložit“.

..tip:
Klikněte na „IoT zařízení“ a přejděte do seznamu „/applications/general/iot/devices“.
Vyberte své POS a zkontrolujte jejich stav připojení. Klikněte na kartu, abyste se dostali do formuláře zařízení.

.. viz též:
   - „Seznam podporovaného hardwaru <https://www.odoo.com/page/point-of-sale-hardware>“.
   - :doc:`Dokumentace IoT </aplikace/obecné/iot>`

.. pos/pos_iot/connect_schema:

Příklad nastavení
=============

.. obrázek: pos_iot/pos-connections.png
:alt:Návrh konfigurace pro pokladní systém.
