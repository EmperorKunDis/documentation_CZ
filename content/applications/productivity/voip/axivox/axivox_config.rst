=================================
VoIP služby v Odoo s Axivox
=================================

Úvod
============

Odoo VoIP (Voice over Internet Protocol) lze nastavit tak, aby fungovalo spolu s Axivox
<http://www.axivox.com/>. V tom případě není nutný ani VoIP server, protože
infrastruktura je hostována a spravována společností Axivox.

Pro využití této služby kontaktujte společnost „Axivox“ na adrese https://www.axivox.com/en/contact/.
Než se k tomu odhodláte, ověřte si, že Axivox pokrývá oblast vaší společnosti, stejně jako oblasti, které vaše společnost pokrývá.
uživatelé chtějí volat.

Konfigurace
=============

Pro konfiguraci Axivox v Odoo přejděte do aplikace „Aplikace“ a vyhledejte VoIP.
Poté nainstalujte modul VoIP.

Dále přejděte do aplikace „Nastavení“ (v menu vyberte možnost „Obecné nastavení“ a poté sekci „Součásti“) a zadejte
do pole „VoIP“:

- :guilabel:`Doména OnSIP`): nastavte doménu vytvořenou společností Axivox pro účet (například
(`vašespolečnost.axivox.com`)
- :guilabel:`WebSocket“: zadejte „wss://pabx.axivox.com:3443“
- :guilabel:`VoIP Environment“: nastavit na :guilabel:`Production“

.. obrázek: axivox_config/voip-configuration.png
:align:center
:alt:Integrace Axivo jako poskytovatele VoIP do databáze Odoo.

..tip:
Přihlaste se do správního rozhraní domény na adrese https://manage.axivox.com/.
<https://manage.axivox.com/>_ po přihlášení do portálu přejděte na:
Edit (vedle jakéhokoliv uživatele) --> záložka SIP identifikátory --> Doména.

Nastavení uživatele VoIP v Odoo
---------------------------

Dále se uživatel konfiguruje v Odoo, což **musí být provedeno pro každého uživatele Axivox/Odoo**.
VoIP.

V Odoo přejděte na: „Nastavení aplikace“ --> „Uživatelé a společnosti“ --> „Uživatelé“, poté otevřete požadovaný.
Příkaz pro konfiguraci uživatelského formuláře: abbr: VoIP (hlasová telefonie přes internet).
Karta „Nastavení“, vyplňte část „VoIP konfigurace“:

- „Jméno VoIP“/„Číslo rozšíření“: (Axivox) „Uživatelské jméno SIP“
- :guilabel:`OnSip Auth Username`: (Axivox) :guilabel:`SIP username“
- :guilabel:`Tajné VoIP“: (Axivox) :guilabel:`Heslo SIP“
- Možnost vždy přenášet hovory na sluchátko
- :guilabel:`Vnější telefonní číslo“: Vnější telefonní rozšíření SIP
- Možnost odmítnout všechny příchozí hovory
- :guilabel:Jak provolávat na mobilu“: metoda, jak volat na mobilním telefonu

.. obrázek: axivox_config/odoo-user.png
:align:center
:alt:Integrace uživatele Axivoxu do předvoleb Odoo.

..tip:
Přihlaste se do správního rozhraní domény na adrese https://manage.axivox.com/.
<https://manage.axivox.com/>_ po přihlášení do portálu přejděte na:
Edit (vedle uživatele) --> záložka SIP identifikátory --> SIP uživatelské jméno / SIP heslo.

....... obrázek:: axivox_config/manager-sip.png
:synchronizace: střed
:alt:Kredence SIP v manažeru Axivox.

.. důležité:
Při zadání hesla SIP do záložky „Nastavení“ uživatele se
Hodnota **musí být zadána ručně** a **nepřepisována**. Při přepisování dojde k chybě s kódem 401 server
„chyba při odmítnutí“.
