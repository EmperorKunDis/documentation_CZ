Zobrazit obsah

==========
On premises
==========

Registrovat databázi
===================

Pro registraci databáze zadejte svůj kód předplatného v záhlaví aplikace Dashboard. Pokud
registrace je úspěšná, banner se zbarví do zelené barvy a zobrazí datum vypršení platnosti databáze.

.. tip::
Datum vypršení platnosti je také zobrazeno na konci stránky Nastavení.

... on-premise/duplikát:

Duplikovat databázi
====================

Zkopírujte databázi přístupem k databázovému manažerovi na vašem serveru
(`<odoo-server>/web/database/manager`). Obvykle chcete vytvořit kopii své produkční databáze.
do neutrální databáze testů. To lze provést zaškrtnutím políčka Neutralizovat při zadávání.
která spouští všechny skripty souboru :file:`neutralize.sql` pro každý nainstalovaný modul.

Běžné chybové hlášky a jejich řešení
===================================

Chyba při registraci
------------------

V případě chybného registračního údaje se zobrazí následující hlášení.

.. obrázek: on_premise/error-message-sub-code.png
:alt:Chybová hláška při registraci do databáze

Aby se vyřešila situace:

- Zkontrolujte platnost svého předplatného Odoo Enterprise tím, že ověříte, zda je vaše předplatné
podrobnosti mají štítek :guilabel:`In Progress“ na vašem účtu „Odoo“.
Kontaktujte prosím svého obchodního zástupce nebo se přihlaste na stránku https://accounts.odoo.com/my/subscription>.

- Zajistěte, aby **nebyla propojena žádná jiná databáze** s kódem předplatného, protože může být použita pouze jedna databáze.
spojené podle předplatného.

.....tip:
Pokud je potřeba testovací nebo vývojová databáze, můžete si vytvořit kopii databáze.


- Zkontrolujte, že žádné databáze nemají stejný UUID (Univerzální jedinečný identifikátor).
„Smlouva Odoo <https://accounts.odoo.com/my/subscription>“. Pokud jsou dvě nebo více databází sdílené,
stejný UUID, jejich jméno se zobrazí.

.... obrázek:: on_premise/unlink-db-name-collision.png
:alt:Chybová zpráva o chybě v databázovém identifikátoru

Pokud tomu tak je, měli byste ručně změnit UUID databáze nebo „odeslat požadavek na podporu
<https://www.odoo.com/help>.

- Aby se aktualizační oznámení dostalo k serverům pro ověřování předplatného společnosti Odoo, zajistěte
vaše **síťová a firewall nastavení** umožňují Odoo serveru otevřít vycházející spojení
směrem k:

  - Odoo 18.0 a výše: „services.odoo.com“ na portu „80“
  - Odoo 17.0 a nižší: „services.openerp.com“ na portu „80“.

Tyto přístavy musí být otevřeny i po registraci databáze, protože aktualizační oznámení běží
jednou týdně.

Příliš mnoho uživatelských chyb
--------------------

Pokud máte v místní databázi více uživatelů než je předplatné Odoo Enterprise.
Měl by se zobrazit následující text.

.. obrázek:on-premise/add-more-users.png
:alt:Příliš mnoho uživatelů na chybovém hlášení databáze

Když se zpráva objeví, máte 30 dní na to, abyste něco udělali, než vyprší platnost databáze.
aktualizováno každý den.

K vyřešení problému lze použít buďto:

- Přidejte další uživatele do svého předplatného kliknutím na odkaz „Upgrade your subscription“.
zobrazené v zprávě k ověření cenové nabídky na zvýšení počtu uživatelů a zaplacení za další uživatele.
- :ref:`Zablokovat uživatele <users/deactivate>` a **odmítnout** nabídku na zvýšení cen.

Jakmile databáze obsahuje správný počet uživatelů, zpráva o vypršení platnosti zmizí sama.
Po několika dnech, kdy se ověření opakuje.

Chyba vypršení platnosti databáze
----------------------

Pokud před obnovením vašeho předplatného vyprší platnost databáze, zobrazí se následující hláška
zobrazeny.

.. obrázek:on_premise/database-expired.png
:alt:Chybová hláška o vypršení platnosti databáze

Toto upozornění se zobrazí, pokud nebudete činit žádné kroky do konce 30denního odpočítávání.

K vyřešení problému lze použít buďto:

- Klikněte na odkaz „Obnovit předplatné“ zobrazený v zprávě a dokončete
pokud platíte převodem, obnoví se vám předplatné po příchodu platby.
Kreditní karty jsou zpracovávány okamžitě, bankovní převody mohou trvat několik dní.
- „Odeslat požadavek na podporu <https://www.odoo.com/help>“.

..toctree::

on-premise/balíčky
on-premises/zdroj
on-premise/aktualizace
on-premises/deploy
on-premise/e-mailová brána
on-premise/geolocation
on-premise/komunita do podniku
