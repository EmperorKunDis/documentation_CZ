..._vývojářský režim:

===========================
Vývojářský režim (provozní režim pro ladění)
===========================

Vývojářský režim, také známý jako režim ladění, odemkne přístup k pokročilým :ref:`nástrojům a nastavením
v Odoo.

.. varování:
Postupujte s opatrností, protože některé vývojové nástroje a technické nastavení jsou považovány za pokročilé.
Některé z nich mohou být spojeny s riziky. Používejte je pouze tehdy, pokud chápete jejich důsledky a jste si jisti svými schopnostmi
vaše činy.

.. poznámka::
Vývojářský režim je k dispozici také s :ref:`aktivními aktivy <frontend/framework/assets_debug_mode>`.
které se používají k ladění javascriptového kódu a s :ref:`testovacími aktivitami
<frontend/framework/test_debug_mode>, které se používají k spouštění testovacích tras.

..._vývojářský režim a aktivace:

Aktivace
==========

Aby se aktivovalo, otevřete aplikaci „Nastavení“, posuňte se dolů k „Vývojářským nástrojům“
sekci a klikněte na „Aktivovat vývojářský režim“.

Jakmile je aktivována, zobrazí se možnost „Vypnout vývojářský režim“.

.. obrázek:: developer_mode/settings.png
:alt:Aktivace vývojářského režimu v aplikaci Nastavení

Pro aktivování vývojářského režimu z jakéhokoliv místa v databázi přidejte na konec „?debug=1“.
URL (např. „https://example.odoo.com/odoo?debug=1“). Chcete-li ji vypnout, použijte místo toho „?debug=0“.

Použijte ?debug=assets, abyste aktivovali režim vývojáře s aktivací souborů a ?debug=tests, abyste aktivovali testy.
s testovacími aktivy.

.. tip::
Otevřete **paletu příkazů** stisknutím kláves Ctrl + K nebo Cmd ⌘ + K, poté zadejte „debug“
aktivovat vývojářský režim s aktivací nebo deaktivací.

.. varování :: Prohlížečová rozšíření

Prohlížečový doplněk Odoo Debug <https://github.com/Droggol/OdooDebug> přidává ikonu pro zapnutí a vypnutí
Vývojářský režim zapnutý nebo vypnutý z panelu prohlížeče. Je k dispozici na Chrome Web Store

„Příslušenství Firefox <https://addons.mozilla.org/firefox/addon/odoo-debug/>“.

..._/nástroje pro vývojáře:

Nástroje pro vývojáře a technické menu
==================================

Jakmile je režim vývojáře aktivován, můžete získat přístup k nástrojům pro vývojáře klepnutím na
:ikonka: „fa-bug“ :guilabel: („bug“) ikonka. Menu obsahuje nástroje, které jsou užitečné pro pochopení nebo úpravu
technické údaje, jako je pole pohledu, filtry nebo akce. Volby se liší v závislosti na tom, kde
menu se dostanete přes.

.. obrázek: developer_mode/tools.png
:alt:Přístup k nástrojům pro vývojáře

Administrátoři databází mohou přistupovat k technickému menu z aplikace Nastavení. Obsahuje
pokročilé nastavení databáze, jako například nastavení struktury databáze, zabezpečení, akcí atd.

.. obrázek:: developer_mode/technical.png
:alt:Přístup do technického menu
