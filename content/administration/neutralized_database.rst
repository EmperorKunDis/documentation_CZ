====================
Neaktivní databáze
====================

Neaktivní databáze je neprodukční databáze, na které jsou některé parametry vypnuty.
Tímto způsobem lze provádět testy bez rizika spuštění konkrétních automatických procesů,
mohou ovlivnit produkční data (např. odesílání e-mailů zákazníkům). Přístup v reálném čase je odebrán a
se stala testovací oblastí.

.. poznámka::
**Všechna testovací databáze vytvořená je neutrální databáze:**

   - testování záložních databází
   - duplicitní databáze
   - pro Odoo.sh: vývojová a testovací databáze

.. důležité:
Databáze může být také zneškodněna při aktualizaci, protože je nezbytné provést nějaké testy před
přechodem na novou verzi.

Deaktivované funkce
====================

Níže je seznam zrušených funkcí:

- plánované akce (např. automatické fakturace předplatného, masový e-mail atd.)
- odchozí e-maily
- synchronizace s bankou
- Poskytovatelé platebních služeb
- metody doručení
- :zkratka:IAP (In-App Purchase) tokeny
- viditelnost webu (zamezte vyhledávačům indexování vašeho webu)

.. poznámka::
**V horní části obrazovky se zobrazuje červená vlajka na neutralizované databázi, aby bylo možné
Je vidět hned.
