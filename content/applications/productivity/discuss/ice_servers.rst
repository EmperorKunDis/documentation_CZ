=================================
Konfigurujte servery ICE s Twiliem
=================================

Odoo Discuss používá API WebRTC a peer-to-peer spojení pro hlasové a videohovory. Pokud jeden z
Pokud se účastníci hovoru nacházejí za symetrickým NATem, je potřeba konfigurovat ICE server pro založení
připojení k účastníkovi hovoru. Nejprve vytvořte účet Twilio pro videohovory
volání a poté připojit účet Twilio k Odoo.

Vytvořte účet u Twilio
=======================

Nejprve navštivte stránku „Twilio“ na adrese https://www.twilio.com/ a klikněte na tlačítko „Sign up“ pro vytvoření nového
Twilio účet. Poté zadejte své jméno a e-mailovou adresu, vytvořte heslo a přijměte podmínky
Podmínky služby a pak klikněte na tlačítko „Začněte s bezplatnou zkušební verzí“. Potvrďte svou e-mailovou adresu
Twilio podle jejich pokynů.

Poté zadejte své telefonní číslo do Twilio. Potom vám Twilio pošle SMS zprávu
obsahující ověřovací kód. Zadejte ověřovací kód do Twilio, abyste ověřili svůj telefon
číslo.

Poté Twilio přesměruje na stránku s uvítacím textem. Použijte následující seznam k odpovědi na otázky Twilio.
otázky:

- Pro „Který produkt Twilio chcete používat?“ vyberte „Video“.
- Pro otázku „Jaké plány máte s Twiliem?“ vyberte „Další“.
- Vyberte možnost „Bez kódu vůbec“.
- Pro :guilabel:`Co je vaším cílem dnes?“ vyberte :guilabel:`Třetí strany“.

.. obrázek:ice_servers/twilio-welcome.png
:align:center
:alt:Stránka uvítání od společnosti Twilio.

Pokud je třeba, změňte zemi fakturace. Nakonec klikněte na „Zahájení služby Twilio“.

Najděte účetní identifikační číslo (SID) a autentizační token
============================================

Pro získání účtu SID a autentizačního tokenu přejděte na stránku s přehledem účtu. Pak klikněte
:guilabel:`Rozvoj“ v bočním panelu. V sekci „Informace o účtu“ najděte
:guilabel:`SID účtu“ a „Token pro ověření“. Oba jsou potřebné k připojení Twilio.
Odoo.

.. obrázek:ice_servers/twilio-acct-info.png
:align:center
:alt: ID účtu a token pro autentizaci lze najít v sekci Informace o účtu.

Připojte Twilio k Odoo
======================

Otevřete databázi Odoo a přejděte na: „Nastavení“ -> „Obecné nastavení“ -> „Diskuse“. Zkontrolujte
přepínač vedle políčka s názvem „Použít servery Twilio ICE“ a zadejte účet Twilio.
„ID účtu“ a „Token autentizace“. Nakonec klikněte na „Uložit“, abyste tyto změny aplikovali.
změny.

.. obrázek:ice_servers/connect-twilio-to-odoo.png
:align:center
:alt:Zapněte možnost „Používat servery ICE od Twilio“ v obecných nastaveních Odoo.

Definujte seznam vlastních serverů ICE
===================================

Tento krok není nutný pro konfiguraci Twilio. Pokud však Twilio nebylo nakonfigurováno nebo je
v případě, že se aplikace v daném okamžiku nezdaří spustit, bude Odoo spadat na seznamy ICE serverů přizpůsobených uživatelem.
definovat seznam vlastních serverů ICE.

V nastavení „Obecné“ vyberte možnost „Diskuse“ a klikněte na „Servery ICE“.
tlačítko pod položkou „Vlastní seznam serverů Ice“.

.. obrázek: ice_servers/custom-ice-servers-list.png
:align:center
:alt:Tlačítko „Servery ICE“ v nastavení Odoo.

Odoo vás přesměruje na stránku s názvem „Servery ICE“. Zde si můžete nastavit svou vlastní seznam servery ICE.
serverů.

.. obrázek:ice_servers/ice-servers-page.png
:align:center
:alt:Stránka „Servery ICE“ v Odoo.

.. poznámka::
Pro lokální instanci Odoo je potřebný balíček „python3-gevent“ pro aplikaci Discuss
modul pro spouštění hovorů a videohovorů na serverech Ubuntu (Linux).
