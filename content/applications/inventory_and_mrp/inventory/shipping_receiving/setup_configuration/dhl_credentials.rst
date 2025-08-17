===============
Spojení s DHL
===============

DHL je jedním z přepravců, pro které je v Odoo k dispozici *přepravní modul*.
Aplikace **Sklad**. Po zapnutí dopravního spojení v nastavení aplikace a konfiguraci
nejméně jednou metodou dopravy, proces výpočtu cen dopravy:
<../setup_configuration> a generování štítků odeslání <labels> je výrazně zjednodušeno.

.. poznámka::
Zatímco pro různé dopravce jsou k dispozici různé koncovky pro připojení, tato dokumentace
popisuje konfigurační nastavení specifická pro integraci DHL. Pro pokyny k nakonfigurování
- nastavení integrace společná pro všechny dopravce, viz dokumentace k tématu :doc:`třetích
dopravci třetích stran <třetí_dopravce>.

Povolit připojení k DHL Shipping
=============================

Před vytvořením způsobu dopravy společnosti DHL zapněte připojení k dopravci. K tomu přejděte na
do položky:menu_selection:Inventář aplikace --> Konfigurace --> Nastavení.

Přejděte dolů do sekce „Konektory pro přepravu“ a zaškrtněte políčko vedle
:guilabel:`DHL Express Connector“. Nakonec klikněte na :guilabel:`Uložit“ pro aplikaci změn.

Klikněte na odkaz „Dopravní metody DHL“ (ikona „fa-arrow-right“) v levém sloupci, abyste otevřeli stránku s
všechny způsoby dopravy s nastaveným poskytovatelem DHL.

Nastavte způsob dopravy DHL
=============================

Po zapnutí přepravního koncového bodu pro DHL lze nastavit způsoby dopravy pro přepravce.
Jakmile je metoda dopravy nakonfigurována, může být přidána jako položka na prodejní objednávku (PO), což umožňuje
pro automatické počítání poštovného a tvorbu štítků pro zasílání zásilek.

Pro vytvoření nového způsobu dopravy DHL přejděte na: „Inventář aplikace“ -> „Konfigurace“
Nastavení“. V sekci „Připojení k přepravcům“ vyberte možnost „DHL Shipping
Metody jsou spojeny pod zaškrtávacím políčkem DHL Express Connector.

.. poznámka::
Je také možné vidět stávající způsoby dopravy pro každého přepravce, pokud se vydáte na
:menu_selektor:`Skladové aplikace --> Konfigurace --> Způsoby dopravy`.

Klikněte na položku „Nový“ pro otevření prázdného formuláře pro způsob dopravy. Pokud je již nějaký způsob dopravy nastaven,
je vytvořen, může být vybrán z této obrazovky.

.. obrázek: dhl_credentials/dhl-form.png
:alt:Formulář pro způsob dopravy DHL.

Základní informace
-------------------

Začněte konfigurovat způsob dopravy zadáním jeho názvu do pole „Doprava“
pole.

V rozevíracím seznamu Provider vyberte možnost DHL. Po provedení této akce se zobrazí nové
V dolní části formuláře se objeví záložka „Konfigurace DHL“.

Všechny ostatní pole v této sekci jsou stejná na formulářích pro každou dopravu.
dopravce. Podívejte se na dokumentaci k tématu „třetí strany dopravci“ (<third_party_shipper>) pro pokyny
jak je správně nakonfigurovat.

Konfigurace DHL
-----------------

V dialogovém okně pro nastavení dopravce je k dispozici záložka „DHL Konfigurace“, pomocí které se připojí uživatelský účet DHL.
účet v Odoo a nastavte podrobnosti o způsobu doručení.

Kredence vývojáře DHL
~~~~~~~~~~~~~~~~~~~~~~~~~

Pro integraci DHL s Odoo musí být získány přihlašovací údaje vývojáře ze stránky Developer Portal společnosti DHL.
Tyto údaje se používají k propojení uživatelského účtu DHL s aplikací Inventář v Odoo.

.. důležité::
*SiteID* a *Password* jsou jiné přihlašovací údaje než ty, které používáte k přihlášení do DHL
účet.

S účtem DHL Express
************************

Pokud je k dispozici účet DHL Express, přihlaste se na portál „DHL Developer“.
<https://developer.dhl.com/api-reference/dhl-express-mydhl-api#get-started-section/>
Návod k použití>_ a „Požádejte o číslo účtu DHL API“ <https://developer.dhl.
https://www.dhl.com/en/home/express/onboarding.html>.

Poté v Odoo zadejte klíč DHL do pole „DHL SiteID“ na formuláři pro způsob doručení.
pole a heslo v poli „Heslo DHL“.

Bez účtu DHL Express
***************************

Pokud není k dispozici účet DHL Express:

#Začněte tím, že si založíte účet DHL Express.
<https://mydhl.express.dhl/gb/en/ship/open-account.html#/fs-step=connectors&fs-step=connectors>`.
#Jakmile je účet v portálu pro vývojáře potvrzen, přihlaste se do portálu pomocí uživatelského jména a
heslo. Klikněte na uživatelské avatary v pravém horním rohu obrazovky, abyste otevřeli přehled uživatele.
#V nabídce na palubní desce otevřete záložku „Aplikace“ a vytvořte aplikaci. Postupujte podle čtyř kroků uvedených v
postup vytváření aplikace (název aplikace, potřebné aplikace, stav aplikace, potvrzení).

.... obrázek: dhl_credentials/create-dhl-app.png
:alt:Nastavení pro vytvoření účtu DHL.

#Po založení účtu DHL Express se přihlaste „tady
<https://developer.dhl.com/user/login?destination=/form/dhl-express-onboarding>_ a získat *DHL
Klíč a heslo k API.

Poté v Odoo zadejte klíč DHL do pole „DHL SiteID“ na formuláři pro způsob doručení.
pole a heslo v poli „Heslo DHL“.

Dopravní podmínky
~~~~~~~~~~~~~~~~

Ostatní položky v záložce „Konfigurace DHL“ slouží k nastavení přepravy.
sám o sobě:

- :guilabel:`Krajina“: země, ve které se používá způsob dopravy.
- :guilabel:`Dopravce DHL“: přepravní služba zakoupená u společnosti DHL (např. Express Worldwide).
- :guilabel:`Typ balíku DHL“: typ balíku používaného k doručení (např. DHL box).
- :guilabel:`Hmotnost balíku v jednotkách“: Jednotka, kterou se zobrazuje hmotnost balíku.
- :guilabel:`Jednotka měření balíku“: jednotka používaná k zobrazení velikosti balíku.
- :guilabel:`Formát štítku“: formát souboru, který se používá k vytvoření štítků pro zasílání.
- :guilabel:`Šablona štítku“: formát papíru, který se používá k tisku štítků pro zasílání zásilek.

.. důležité::
Před výběrem služeb pro dopravní metodu se ujistěte, že tyto služby skutečně existují.
Veškeré služby jsou k dispozici pro účet DHL. Záleží na smlouvě, kterou je možné vyjednat s DHL.

Možnosti
~~~~~~~

Další nastavení je k dispozici v sekci „Možnosti“ na konci stránky.
Karta „Nastavení DHL“:

- :guilabel:Vytvořit štítek pro vrácení zboží: Zapněte tuto možnost, aby se automaticky vygeneroval štítek pro vrácení zboží
po ověření dodacího listu.
- :guilabel:`Zboží podléhající celnímu řízení“: Zapněte tuto možnost, pokud je zvolený způsob dopravy předmětem cla.
jiná povinnost.

Připojte se k DHL
==========================

Jakmile je připojení k DHL nastaveno, použijte chytré tlačítko v horní části formuláře pro publikování a zapnutí.
režim výroby nebo aktivovat ladění.

- :guilabel:`Nezveřejněné“/:guilabel:`Zveřejněné“: určuje, zda je tento způsob dopravy k dispozici
na e-commerce webu uživatele.

- :guilabel:`Testovací prostředí“/:guilabel:`Provozní prostředí“: určuje, zda je vytvářen štítek
je pro testování a je okamžitě zrušen (Test), nebo vytvoří skutečnou dodací etiketu, která se účtuje
do účtu DHL (Produkce).
- :guilabel:`Žádné ladění“/:guilabel:`Požadavky na ladění“: určuje, zda jsou požadavky a odpovědi API
přihlášen v Odoo (zapněte :ref:`rozvojovou verzi <developer-mode> a přejděte do :menuselection:`Nastavení
app --> Technické --> Záznamy.
