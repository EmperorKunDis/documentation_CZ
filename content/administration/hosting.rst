=======
Hosting
=======

.._hostingu/změně řešení:

Změna poskytovatele hostingu
=======================

Návod na změnu typu hostingu databáze závisí na současně používaném řešení.
jaké řešení by měla být databáze přesunuta.

Přesunutí databáze do cloudu
===================================

Odoo Online
--------------

.. důležité:
   - Odoo Online není kompatibilní s aplikacemi, které nejsou standardními.
   - Aktuální verze databáze musí být podporována.

#Vytvořte kopii databáze.
#V tomto duplicitním souboru odinstalujte všechny **neobvyklé aplikace**.
#Použijte správce databáze k získání zálohy s ukládáním souborů.
#Vytvořte požadavek na podporu (<https://www.odoo.com/help-form>).

   - číslo vašeho předplatného
   - URL, kterou chcete použít pro databázi (např. „company.odoo.com“),
   - přiložit přílohu ve formátu *.dump nebo odkaz na soubor (pro soubory o velikosti 60 MB a více).

#Odoo pak zajistí, aby databáze byla kompatibilní, a poté ji umístí na internet. V případě technických
Pokud během procesu nastanou nějaké problémy, může vás kontaktovat Odoo.

.. poznámka::
Pokud máte časové omezení, vytvořte si „ticket podpory“ co nejdříve na adrese https://www.odoo.com/help-form/.
jako možné naplánovat převoz.

Odoo.sh
----------

Postupujte podle pokynů uvedených v části „Import databáze“.
<odoo_sh_import_your_database> dokumentace pro vytvoření projektu na Odoo.sh.

Přenos databáze Odoo Online
====================================

.. důležité:
Intermediární verze Odoo Online nejsou podporovány společností Odoo.sh ani
na vlastním serveru. Pokud tedy databáze k přenosu běží na nějaké mezivrstvě, musí být
nejprve na další verzi s hlavní verzí, která se čeká na vydání.
Je nezbytné.

...... příklad::
Přesunutí databáze online aplikace běžící na Odoo 16.3 by vyžadoval nejprve její aktualizaci na verzi Odoo
      17.0.

... tip::
Klikněte na tlačítko „Nástroje“ („Gear“) vedle názvu databáze v Odoo.
Online databázový správce zobrazuje své verze na adrese https://www.odoo.com/my/databases/.

.... varování::
Pokud je k databázi připojen aktivní předplatitelský účet Odoo, kontaktujte
manažer zákaznického servisu nebo „kontaktujte podporu Odoo“ (<https://www.odoo.com/help>).
dokončit převod předplatného.

On premises
-------------

#Stáhněte si zálohu databáze přihlášením do „manažera online databáze Odoo“.
<https://www.odoo.com/my/databases/>`, kliknutím na tlačítko „:icon:`fa-gear“ (:guilabel:`gear“)
vedle názvu databáze a poté vyberte ikonu „Stáhnout“ (viz obrázek).
Pokud stahování selže kvůli velikosti souboru, kontaktujte podporu Odoo.
<https://www.odoo.com/help>.
#Obnovte databázi z databázového manažera na místním serveru pomocí zálohy.

Odoo.sh
----------

#Stáhněte si zálohu databáze přihlášením do „manažera online databáze Odoo“.
<https://www.odoo.com/my/databases/>`, kliknutím na tlačítko „:icon:`fa-gear“ (:guilabel:`gear“)
vedle názvu databáze a poté vyberte ikonu „Stáhnout“ (viz obrázek).
Pokud stahování selže kvůli velikosti souboru, kontaktujte podporu Odoo.
<https://www.odoo.com/help>.
#Postupujte podle pokynů uvedených v části „Import databáze“.
<odoo_sh_import_your_database> z dokumentace Odoo.sh *Vytvořte svůj projekt*.

Přenos databáze Odoo.sh
================================

Odoo Online
--------------

.. důležité:
Odoo Online není kompatibilní s aplikacemi, které nejsou standardními.

#Odinstalujte všechny **nepovinné aplikace** v testovací verzi předtím, než je uděláte ve verzi pro produkci.
#Vytvořte požadavek na podporu (<https://www.odoo.com/help-form>).

   - číslo vašeho předplatného
   - URL, kterou chcete použít pro databázi (např. „company.odoo.com“),
   - která větve se mají přesunout.
   - v jaké oblasti **země** chcete databázi hostovat (Amerika, Evropa nebo Asie).
   - jakého uživatele (uživatelé) bude správcem (správci),
   - **kdy** (a v jakém časovém pásmu) chcete, aby databáze byla spuštěna.

#Odoo pak zajistí, aby databáze byla kompatibilní, a poté ji umístí na internet. V případě technických
Pokud během procesu nastanou nějaké problémy, může vás kontaktovat Odoo.

.. poznámka::
   - Pokud máte časové omezení, vytvořte požadavek na podporu pomocí formuláře „Odeslat žádost o pomoc“
co nejdříve naplánovat převod.
   - Vyberte oblast, která je nejbližší většině uživatelů, abyste snížili latence.
   - Budoucí správce musí mít účet na webové stránce Odoo.com.
   - Datum a čas, kdy chcete, aby databáze běžela, jsou užitečné při organizování
přepnout z Odoo.sh na servery Odoo Online.
   - Během migrace databáze nejsou dostupné.

On premises
-------------

#Stáhněte si zálohu své produkční databáze Odoo.sh (odkaz).
#Obnovte databázi z databázového manažera na místním serveru pomocí zálohy.
