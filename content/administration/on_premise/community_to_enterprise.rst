
.._setup/enterprise:

===================================
Přechod z komunity na enterprise
===================================

Podle vaší aktuální instalace existuje několik způsobů upgradu
verze pro komunitu.
Pokud jde o základní pravidla, tak jsou následující:

* Zálohujte databázi vaší komunity

.... obrázek: community_to_enterprise/db_manager.png
:class:img-fluid

* Vypněte svůj server

* Nainstalujte modul web_enterprise

* Restartujte svůj server

* Zadejte svůj kód předplatného Odoo Enterprise

.. obrázek: community_to_enterprise/enterprise_code.png
:class:img-fluid

Na Linuxu pomocí instalátoru
============================

* Zálohujte databázi vaší komunity

* Zastavte službu odoo

...... kódový blok: konzole

$ sudo service odoo stop

* Nainstalujte balíček pro firmy (.deb, který by měl nainstalovat přes komunitní balíček).

...... kódový blok: konzole

$ sudo dpkg -i <cesta k enterprise deb>

* Aktualizujte svou databázi na balíčky pro podniky pomocí

...... kódový blok: konzole

$ python3 /usr/bin/odoo-bin -d <database_name> -i web_enterprise --stop-after-init

* Měli byste být schopni se připojit ke svému instanci Odoo Enterprise pomocí vašeho obvyklého způsobu identifikace.
Pak můžete svou databázi propojit s vaším předplatným Odoo Enterprise zadáním kódu, který jste obdrželi.
e-mailem v podobě vstupního formuláře


Na Linuxu pomocí zdrojového kódu
===============================

Existuje mnoho způsobů, jak spustit svůj server pomocí zdrojů, a vy nejspíš
mít svého oblíbence. Můžete si upravit části tak, aby odpovídaly vašemu běžnému způsobu práce.

* Vypněte svůj server
* Zálohujte databázi vaší komunity
* Aktualizujte parametry „--addons-path“ v příkazu spouštění (viz dokumentace „../on-premise/source“)
* Nainstalujte modul web_enterprise pomocí

...... kódový blok: konzole

$ -d <databáze> -i web_enterprise --stop-after-init

V závislosti na velikosti databáze může tento proces trvat nějakou dobu.

* Restartujte server s aktualizovanou cestou k doplňkům z bodu 3.
Měli byste být schopni se připojit k vašemu instanci. Poté můžete propojit databázi s vaším
Odoo Enterprise Subscription zadáním kódu, který jste obdrželi e-mailem do pole vstupu

Na Windows
==========

* Zálohujte databázi vaší komunity

* Odeberte instalaci Odoo Community (pomocí souboru uninstall.exe v adresáři instalace).
PostgreSQL zůstane nainstalovaný

.... obrázek: community_to_enterprise/windows_uninstall.png
:class: obal-obrazek

* Spusťte instalační program Odoo Enterprise a postupujte podle běžných kroků. Když budete vybírat
cestu k instalaci můžete nastavit jako složku instalace komunity
(tato složka stále obsahuje instalaci PostgreSQL).
Na konci instalace nezaškrtněte „Spustit Odoo“

.... obrázek: community_to_enterprise/windows_setup.png
:class:img-fluid

* Použijte příkazovou obrazovku k aktualizaci databáze Odoo pomocí tohoto příkazu (z Odoo).
cestu k instalaci (do podsložky serveru).

...... kódový blok: konzole

$ ..\python\python.exe odoo-bin -d <database_name> -i web_enterprise --stop-after-init

* Není potřeba ručně spouštět server, služba běží.
Měli byste být schopni se připojit ke svému instanci Odoo Enterprise pomocí vašeho obvyklého
identifikační prostředek. Poté můžete propojit svou databázi s vaší Odoo Enterprise
Předplatné zadáním kódu, který jste obdrželi v e-mailu do pole pro vstup
