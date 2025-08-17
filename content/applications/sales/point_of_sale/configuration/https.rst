=========================
Zabezpečená verze (HTTPS)
=========================

Pokud je funkce **Direct Devices** zapnutá v nastavení pokladny (například pokud používáte ePos
tiskárna (<epos_printers>), protože se používá protokol HTTP.

Nutit svůj bod prodeje, aby používal bezpečnou konektivitu (HTTPS).
===========================================================

Přidejte nový klíč do **Parametrů systému**, abyste svou pokladnu donutili k používání bezpečného
s protokolu HTTPS.

Pro to aktivujte režim vývojáře (:ref:`vývojářský režim <developer-mode>`), přejděte na „Nastavení“
Technické ---> parametry ---> systémové parametry“, pak vytvořte nový parametr a přidejte následující
hodnoty a klikněte na tlačítko *Uložit*

- **Klíč**: point_of_sale.enforce_https
- **Hodnota**: `True`

.. viz též:
   - :doc:`epos_ssc`
