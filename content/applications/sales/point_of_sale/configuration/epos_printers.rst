=============
Tiskárny pro ePOS
=============

Tiskárny ePOS jsou navrženy tak, aby bezproblémově fungovaly s pokladnami. Jakmile je připojíte,
zařízení automaticky sdílejí informace, což umožňuje tisk jízdenek přímo z pokladny
do tiskárny ePOS.

Konfigurace
=============

Pro použití tiskárny ePos v bodě prodeje:

#:ref:`Přejděte do nastavení POS <konfigurace/nastavení>.
#Aktivujte funkci „Tiskárna ePos“.
#Vyplňte pole svým ePos IP adresou.

.. obrázek: epos_printers/settings.png
:alt: nastavení pro zapnutí tiskárny ePos

.. poznámka::
Když se tiskárna připojí k síti, automaticky vytiskne lístek s adresou IP.

Elektronické tiskárny účtenek s přímou podporou
================================

Následující tiskárny ePOS jsou přímo kompatibilní s Odoo bez potřeby IoT systému
</obecné/IoT/zařízení/tiskárna>.

- Epson TM-m30 i/ii/iii (pouze modely Wi-Fi a Ethernet; doporučeno)
- Epson TM-H6000IV-DT (Pouze tiskárna účtenek)
- Epson TM-T70II-DT
- Epson TM-T88V-DT
- Epson TM-L90-i
- Epson TM-T70-i
- Epson TM-T82II-i
- Epson TM-T83II-i
- Epson TM-U220-i
- Epson TM-m10
- Epson TM-P20 (Wi-Fi® model)
- Epson TM-P60II (Tiskárna účtenek: Wi-Fi® model)
- Epson TM-P60II (Peeler: Wi-Fi® model)
- Epson TM-P80 (Wi-Fi® model)

tiskárny ePOS s integrovaným systémem IoT
=========================================

Následující tiskárny vyžadují IoT systém:
být kompatibilní s Odoo:

- Rodina Epson TM-T20 (nekompatibilní s EPOS).
- Epson TM-T88 family (nekompatibilní pokladní software)
- Epson TM-U220 (nekompatibilní s EPOS softwarem)

.. důležité:
   - Tiskárny Epson využívající bezdrátové/ethernetové připojení a sledující protokol „EPOS SDK Javascript“
<https://download4.epson.biz/sec_pubs/pos/reference_en/technology/epson_epos_sdk.html>
kompatibilní s Odoo bez potřeby IoT systému
</aplikace/obecné/IoT/zařízení/tiskárna>.
   - Termální tiskárny využívající ESC/POS jsou kompatibilní s:doc:`IoT systémem
</aplikace/obecné/IoT/zařízení/tiskárna>.
   - Tiskárny Epson s pouze USB připojením jsou kompatibilní se systémem IoT.
</aplikace/obecné/IoT/zařízení/tiskárna>.
   - Tiskárny Epson, které se připojují prostřednictvím Bluetooth, **nejsou kompatibilní**.

.. viz též:
   - :doc:`https“
   - :doc:`epos_ssc`
