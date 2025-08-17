======
Geolokace
======

.. poznámka::
Tato dokumentace se vztahuje pouze na databáze On-premise.

Instalace
============

#Stáhněte si oba soubory GeoLite2 City a Country.
„databáze <https://dev.maxmind.com/geoip/geoip2/geolite2/>“. Nakonec byste měli mít dvě soubory
přičemž se jmenují GeoLite2-City.mmdb a GeoLite2-Country.mmdb.

#Přesuňte soubory do složky: ` /usr/share/GeoIP/`.

....... kódový blok:: bash

mv ~/Stahování/GeoLite2-City.mmdb /usr/share/GeoIP/
mv ~/Stahování/GeoLite2-Country.mmdb /usr/share/GeoIP/

#Restartujte server.

.. poznámka::
Pokud nechcete, aby se databáze GeoIP nacházela v adresáři :file:`/usr/share/GeoIP/`, použijte
:option:`--geoip-city-db <odoo-bin --geoip-city-db>`.
:option:`--geoip-country-db <odoo-bin --geoip-country-db>` možnosti příkazového řádku
rozhraní. Tyto možnosti používají absolutní cestu k souboru databáze GeoIP a použijí ji jako
GeoIP databáze. Například:

....... kódový blok:: bash

      ./odoo-bin --geoip-city-db= ~/Downloads/GeoLite2-City.mmdb

......viz také::
      - :doc:`Dokumentace k příkazovému řádku </developer/reference/cli>“.

Ověřte si testování geolokace v Odoo
===========================================

Upravte webovou stránku tak, aby obsahovala nějaké informace o geografickém umístění, například jméno země, ve které se právě nacházíte.
požádat o IP adresu. Pro toto:

#Přejděte na svou webovou stránku a otevřete webovou stránku, kterou chcete otestovat pomocí „GeoIP“.
#Vyberte:menu:Upravit --> editor HTML, CSS a JavaScriptu.
#Přidejte následující kus XML na stránku:

... kódový blok::xml

<h1 class="text-center" t-esc="žádost.geoip.země.název nebo 'geolokace selhala'"/>

#Uložte a obnovte stránku.

Geo-ip funguje, pokud vidíte své jméno zobrazené v tučném písmu uprostřed stránky.

Pokud místo toho čtete „**geolokační chyba**“, pak se geolokalizace nezdařila. Nejběžnější příčinou je:

#Procházení z IP adresy lokálního počítače („127.0.0.1“) nebo ze sítě LAN. Pokud
nevíte, můžete se na své webové stránky připojit pomocí mobilních dat.
#Používáte před Odoo reverzní proxy (Apache, Nginx), ale nezačali jste Odoo s
je zapnutý režim proxy. Podívejte se na možnost „režim proxy“ (odoo-bin --proxy-mode).
#Geolokace je poškozená, chybí nebo není dostupná. V takovém případě byl vytvořen varovný záznam v
záznamy serveru.
