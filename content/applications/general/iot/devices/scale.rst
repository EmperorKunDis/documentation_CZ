===============
Připojte váhu
===============

.. důležité::
V členských státech EU je „certifikace právně vyžadována
<https://eur-lex.europa.eu/legal-content/CS/ALL/?uri=CELEX:52014L0096>
používat stupnici jako integrovaný přístroj.

Pro připojení váhy k systému Internetu věcí použijte kabel USB. V některých případech může být potřeba sériový port.
adaptér pro dokončení připojení. Pokud je váha kompatibilní s IoT systémem
<https://www.odoo.com/page/iot-hardware>`, žádné další nastavení není nutné, váha je
je automaticky detekován ihned po připojení. Pokud se váha nezjistí, restartujte IoT box
nebo restartovat virtuální službu IoT systému Windows (<iot/windows_iot/restart>).
Řidiči skládky <iot_updating_iot/handlers>.

.. poznámka::
Pokud po aktualizaci ovladačů stále nefunguje měřidlo, mohlo by se jednat o „nekompatibilitu s
Odoo IoT systém <https://www.odoo.com/page/iot-hardware>. V takových případech je třeba použít jiný měřicí přístroj
Musí být použita.

Jakmile je váha připojena k systému Internetu věcí, konfigurujte ji v nastavení POS.

.. viz též:
:doc:`Připojit systém IoT k POS </applications/sales/point_of_sale/configuration/pos_iot>`

Ariva S měřítka
==============

Pro váhy série Ariva S (vyráběné společností Mettler-Toledo, LLC) k fungování s IoT systémy je potřeba
musí být upraven specifický nastavení a k měření je potřeba speciální kabel USB-to-proprietary RJ45 od společnosti Mettler.

.. důležité::
Kabel USB-RJ45 oficiálního výrobce Mettler (číslo dílu 72256236) musí být použit.
Mettler nebo jeho partnerovi koupit originální kabel. **Žádný jiný** kabel nefunguje pro tento
konfigurace.

Pro konfiguraci váhy Ariva S pro rozpoznání systému IoT se podívejte na stránku 17 v návodu „Nastavení Mettler“.
Návod pro váhy řady Ariva S <https://www.mt.com/dam/RET_DOCS/Ariv.pdf>_ a postupujte podle těchto kroků:

#Stiskněte tlačítko **>T<** po dobu osmi sekund nebo až do chvíle, kdy se objeví znak „CONF“.
#Stiskněte tlačítko **>T<**, dokud se nezobrazí „GRP 3“, a poté stiskněte **>0<** pro potvrzení.
#V kroku 3.1 je nutné zkontrolovat, zda je nastavená hodnota na „1“ (virtuální sériové porty USB).
stisknutím tlačítka **>T<** pro přechod na další možnosti.
#Stiskněte tlačítko „0“ do té doby, dokud se nezobrazí hodnota „3.6“ (pokud je k dispozici, jinak přeskočte další krok).
#V kroku 3,6 zkontrolujte hodnotu nastavení na „3“ (8217 Mettler-Toledo (WO)).
Pokud chcete přejít na další možnost, stiskněte klávesovou zkratku **>T<**.
#Stiskněte tlačítko **>0<** (opakujte, pokud je nutné) a zobrazí se :guilabel:`GRP 4`.
#Stiskněte tlačítko **>T<**, dokud se nezobrazí „VYCHOZÍ“.

.... důležité::
Nepřidávejte žádné další změny, pokud nejsou nutné.

#Tlačítko **>0<**.
#Stiskněte klávesu **>0<** znovu a zadejte „Uložit“ (tlačítko „Uložit“). Skalár se restartuje.
#Obnovte zařízení IoT nebo restartujte virtuální službu IoT v systému Windows:
Poté by měla být zobrazena jako „Toledo 8217“, nikoliv jako v předchozím zobrazení.
zobrazil se jako „Sériové číslo zařízení Adam“.
