======================
IoT box SSH připojení
======================

.. poznámka::
Připojení pomocí protokolu SSH je k dispozici pouze pro :doc:`IoT box <../iot_box>`, nikoliv pro :doc:`Windows
virtuální IoT (<../windows_iot>).

.. varování:
   - Tato funkce by měla být používána jen s důvěryhodnými stranami, protože poskytuje administrativní
přístup k internetu věcí (IoT), což může vést ke zranitelnosti.
   - Zajištění správy připojení pomocí SSH není součástí standardní podpory Odoo.
stránka „Podpora Odoo <https://www.odoo.com/help>“ pro další informace o tom, co je
pokryté.

Pro zabezpečené připojení k internetu věcí je nutné vytvořit
heslo:

#Přihlaste se na domovskou stránku IoT boxu otevřením aplikace IoT a kliknutím na zobrazené IP adresy
na kartě zařízení IoT boxu.
#Klikněte na tlačítko v pravém horním rohu s ikonou „kolečka“ (viz ikona „fa-cogs“). Pak klikněte na „Vzdálený
Debug.
#V okně „Dálkové ladění“ klikněte na tlačítko „Vytvořit“ a uložte.
Přihlášení je zabezpečeno heslem. Jakmile ukončíte okno s přihlašovacími údaji, heslo již nebude dostupné.

.... obrázek:: ssh_connect/ssh-generate-password.png
:alt:Okno pro generování hesla k vzdálené ladění.

#Zadejte autentizační token, který uživatel při pokusu o připojení k internetu věcí zadá.
krabice.
#Klikněte na tlačítko „Povolit vzdálené ladění“.

.. viz též:
   - :doc:`../iot_box`
   - :doc:`../connect`
