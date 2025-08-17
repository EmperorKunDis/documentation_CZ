======================
Kapitola 6 – Živé vysílání
======================

... /tutoriály/webové-téma/spuštění/překlady:

Překlady
============

Gratulujeme! Váš klient má nádherně navrženou domovskou stránku a kontaktní stránku a e-commerce.
je plně přizpůsobena designu Airproof. Úžasné!

Nyní chce klient webové stránky přeložit do francouzštiny. K tomu je potřeba:

#Přidejte do nastavení webu francouzštinu a v hlavičce zapněte přepínač jazyka.
přednastavení.
#Pak pro samotný překlad máte dvě možnosti, takže je dobré si obě vyzkoušet:

   - Přeložte obsah banneru na domovské stránce přes zadní část webové stránky.
   - Ale pro menu udělejte překlady přes přední část.

#Exportujte soubor s názvem „.po“ pro vaši modulovou knihovnu Airproof a umístěte jej do složky „/i18n“.
složku s překlady.
#Pokud chcete, můžete přidat další překlady přímo v souboru :file:.po
souboru (pomocí softwaru Poedit, kótovacího editoru nebo jiného překladového nástroje).

.. viz též:
Podrobnější informace najdete v dokumentaci na téma „webové šablony/překlady/back-end“
:ref:`webové šablony/překlady/frontend překladů a jak je používat
:ref:`webové šablony/překlady/exportovat je.

.. poznámka::
   - Pozor na používání Poeditu, protože neumí dobře pracovat s tagy a generuje
:soubor:`.mo` soubor.
   - Pro zobrazení změn přímo v souboru .po je nutné provést ruční import.
souboru.

..spoiler:: Řešení

Podívejte se na soubor `i18n/fr_BE.po <{GITHUB_TUTO_PATH}/website_airproof/i18n/fr_BE.po>`.
V našem příkladu vzduchotěsného obalu je to takto.

... /tutoriály/webové-téma/spuštění/moduly-import:

Modulární import
=============

Dobrá práce! Web je nyní kompletně dokončený a váš modul je připraven k instalaci na
databáze klientského SaaS.

Předtím otestujte proces importu na nové databázi.

.. viz též:
Podívejte se na odkazované dokumentace, jak nasadit modul
na databázi Odoo SaaS.

..tip:
   - Ujistěte se, že je nainstalován modul base_import_module na databázi před instalací modulu.
   - Zkontrolujte, zda jsou nainstalovány všechny požadované aplikace.
   - Přeskočte kroky instalace téma a začněte od nuly.
   - Přeložení ručně doplňte po instalaci modulu, protože se neaplikují automaticky.

Závěr
==========

Gratulujeme k dokončení návodu **Vytvořte modul pro webovou šablonu**!
Úspěšně jste prošli všemi fázemi, od nastavení vývojového prostředí po
spuštění plně přizpůsobeného tématu webové stránky Odoo.

Během této cesty jste se naučili:

|✅ Vytvoření šablony modulu – nastavení struktury, deklarace proměnných Odoo a Bootstrapu.
|✅ **Tvorba webových stránek** – vytváření stránek, přidávání médií a konstrukce dynamických bloků.
|✅ **Pokročilé nastavení** - implementace vlastních CSS, JavaScript, hlaviček a patiček a jedinečných
designové prvky.
|✅ **Vylepšení vizuálního vzhledu** – navrhování pozadí, gradientů a animací
zajímavý uživatelský zážitek.
|✅ **Optimalizace e-commerce** – přizpůsobení šablon obchodu a produktů pro bezproblémové nakupování
zkušeností.
|✅ **Konečné přípravy** – správa překladů a zajištění hladkého dovozu modulu.

S těmito znalostmi jste nyní připraveni navrhovat a vytvářet profesionální webové stránky s plnou úpravou.
téma. Gratuluji!
|Nemůžeme se dočkat, až uvidíme úžasné motivy, které vytvoříte v budoucnu.
