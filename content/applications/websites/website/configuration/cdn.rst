=======================================
Zřídit síť pro doručování obsahu (CDN)
=======================================

.. odkaz/cdn/keycdn:

Deployment pomocí KeyCDN
=====================

Slovo „CDN“ nebo „síť pro distribuci obsahu“ označuje geograficky
síť serverů, která poskytuje vysokorychlostní obsah pro internet.
Síť dodávek) poskytuje rychlé a kvalitní doručování obsahu pro webové stránky s vysokým obsahem obsahu.

Tento dokument vás provede nastavením účtu KeyCDN s webem, který je poháněn Odoo.

Vytvořte tahovou zónu v KeyCDN Dashboard
------------------------------------------

Na panelu KeyCDN začněte tím, že se přesunete na záložku „Zóny“ v levém menu.
formulář, zadejte hodnotu pro :guilabel:`Zóna jména`, která se objeví jako součást :abbr:`CDN
Síť pro doručování obsahu): abbr. URL (jednotný identifikátor zdroje). Pak nastavte zónu
Stav zóny nastavte na „Aktivní“ a pro typ zóny nastavte hodnotu
:guilabel:„Táhnout“ a poté, co je konečně zadáte pod :guilabel:„Nastavení tahu“,
:guilabel:`Zdrojová URL“ - tato adresa by měla být plná URL adresa databáze Odoo
Locator`.

Příklad:
Použijte „https://yourdatabase.odoo.com“ a nahraďte předponu subdomény *yourdatabase*.
skutečné jméno databáze. Může být použit vlastní :abbr:`URL (Uniform Resource Locator)`
Ale místo odoo.subdomény, která byla poskytnuta databázi.

.. obrázek: cdn/keycdn-zone.png
:align:center
:alt: Konfigurační stránka zóny služby KeyCDN.

Pod nadpisem „Obecné nastavení“ pod formulářem zóny klikněte na „Zobrazit všechny
tlačítko „Nastavení“ pro rozšíření možností zóny. Toto by mělo být poslední volbou na stránce. Po
Rozšířením nastavení v sekci „Obecné“ zajistíte, aby byla volba „CORS“
:guilabel:`zapnuto“.

Dále se přesuňte na konfigurační stránku zóny a uložte změny stisknutím tlačítka „Uložit“.
Ukáže, že nový pás bude nasazen. To může trvat asi 10 minut.

.. obrázek: cdn/zone-url.png
:align:center
:alt:KeyCDN nasazuje novou zónu.

.. poznámka::
Vytvořen nový záznam „URL Zóny“ pro vaši zónu. V tomto případě je tento záznam
„pulltest-xxxx.kxcdn.com“. Hodnota se pro každou databázi liší.

Zkopírujte tento řádek do textového editoru na později, protože bude použit v dalších krocích.

Nastavte instanci Odoo s novou zónou
---------------------------------------------

V aplikaci „Webové stránky“ v Odoo přejděte do nastavení a poté aktivujte
V nastavení „Služba Content Delivery Network (CDN)“ zkopírujte a vložte hodnotu „URL zóny“.
z předchozího kroku do pole „Základní URL CDN“. Toto pole je viditelné pouze
Konfigurovatelné, pokud je aktivováno vývojářské režimy.

.. poznámka::
Zajistěte, aby bylo před adresou CDN dvakrát znak „dvojitý lomítko“ (//) a jednou
zavináč („/“) po :guilabel:`CDN Base URL`.

Uložte nastavení po dokončení.

.. obrázek: cdn/cdn-base-url.png
:align:center
:alt:Aktivujte nastavení CDN v Odoo.

Webová stránka nyní používá CDN pro zdroje odpovídající filtrům „CDN filtry“
výrazy.

V HTML kódu webu Odoo je doložena integrace CDN
funkčností kontrolou URL obrázků. CDN Base
Hodnota URL* lze zjistit pomocí funkce „Inspektor“ vašeho prohlížeče na stránkách Odoo.
Hledejte její záznam v záložce sítě v rozhraní pro vývojáře.

.. obrázek: cdn/test-pull.png
:align:center
:alt:Základní adresu CDN lze zjistit pomocí funkce Inspect na webových stránkách Odoo.

Zamezte bezpečnostním problémům aktivací sdílení zdrojů přes hranice domén (CORS)
--------------------------------------------------------------------------

Zabezpečení v některých prohlížečích (např. Mozilla Firefox a Google Chrome) zabraňuje
odkazoval na vzdálený soubor CSS, aby získal relativní zdroje na stejném externím serveru.

Pokud není zapnuta volba CORS (Cross-Origin Resource Sharing) v CDN
Zóna, větší problém na běžném webu Odoo je pak chybějící font.
Úžasné ikony, protože písemný soubor deklarovaný v CSS pro Font Awesome nebude načítán z
vzdálený server.

Když k těmto problémům dochází, zobrazí se chybová hláška podobná této.
V konzoli vývojáře prohlížeče se zobrazí:

„Písmo z původního „http://pulltest-xxxx.kxcdn.com“ bylo zablokované při načítání /shop:1
Politika sdílení zdrojů přes hranice: Žádný hlavičkový záznam „Access-Control-Allow-Origin“ není přítomen.
požadovaná zdrojová data. Zdroj „http://yourdatabase.odoo.com“ tedy nemůže být přístupný.

.. obrázek: cdn/odoo-security-message.png
:align:center
:alt:Chybová zpráva, která se objeví v prohlížeči.

Povolením možnosti CORS (Cross-Origin Resource Sharing) v CDN (Content Delivery
Nastavení sítě) tento problém vyřeší.

.._KeyCDN: https://www.keycdn.com
