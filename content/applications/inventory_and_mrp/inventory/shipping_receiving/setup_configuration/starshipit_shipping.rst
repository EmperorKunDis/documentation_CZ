===================
Starshipit přepravní služba
===================

Starshipit je poskytovatel služeb v oblasti přepravy, který usnadňuje integraci australských a novozélandských společností.
přepravní kurýři s Odoo. Jakmile je integrace dokončena, uživatelé mohou vytvářet způsoby přepravy, které budou
automaticky získávat sazby od konkrétních přepravců (např. Austrálie Post, Nový Zéland Post, DHL,...).
podle předem definovaných podmínek.

.. viz také:
   - :doc:`Automaticky vypočítává poštovné <../setup_configuration>`
   - :doc:`Propojit další třetí strany <third_party_shipper>`

Nastavení v aplikaci Starshipit
===================

Vytvořte si účet a aktivujte kurýry
---------------------------------------

Pro zahájení práce přejděte na stránku „Platforma Starshipit“ <https://starshipit.com/>_, abyste si mohli vytvořit účet
a vytvořte přihlašovací údaje konektoru. Přihlásit se do účtu Starshipit nebo založit nový, pokud
nebylo nutné.

Konfigurace adresy pro vyzvednutí
----------------------------

Jakmile se přihlásíte do účtu Starshipit, přejděte na „Nastavení -> Adresa pro vyzvednutí“.
a vyplňte pole „Adresa pro vyzvednutí“. Ujistěte se, že tato adresa odpovídá adrese skladu.

.. obrázek: starshipit_shipping/starshipit-settings-address.png
:align:center
:alt:Přidání adres v nastavení Starshipitu.

Konfigurace kurýrů
----------------------

Pro integraci s externími kurýry přejděte na „Nastavení -> Kurýři“ a
vyberte:guilabel:"Dopravci".

.. obrázek: starshipit_shipping/starshipit-settings-couriers.png
:align:center
:alt:Přidání adres v nastavení Starshipitu.

..tip:
Pro podrobnosti o integraci s různými kurýry se podívejte na stránky Starshipit
<https://help.starshipit.com/cs>`.

Checkoutové sazby
--------------

Pro konfiguraci výpočtu ceny dopravy přejděte na stránku: „Nastavení --> Doprava“.
Vybrané náklady na dopravu jsou automaticky aplikovány v Odoo při výpočtu poštovného.

.. obrázek: starshipit_shipping/starshipit-checkout-rate.png
:align:center
:alt: Zkontrolujte sazby na stránce nastavení v Starshipit.

API klíč pro Starshipit
------------------

Nastavte pravidla pro dopravu, aby byly přiřazeny správné metody dopravy objednávkám podle specifických
podmínky.

Vytvoření pravidla provedete v sekci „Nastavení“ -> „Pravidla“ kliknutím na „Přidat nové pravidlo“.

Existuje několik způsobů, jak nastavit pravidla, ale doporučujeme zadat:

#:guilabel:`Podmínka“ na :guilabel:`Obsahuje“
#:guilabel:`Hodnota“ k „kódu produktu“
#:guilabel:`Akce“ na „Nastavit kurýra a kód produktu“.

.. obrázek: starshipit_shipping/starshipit-rules.png
:align:center
:alt:Pravidla dopravy v nastavení Starshipit.

... inventarizaci, přijímání a odesílání zboží, API hvězdy:

Hledání přihlašovacích údajů pro službu Starshipit
----------------------------------

Ve svém účtu Starshipit přejděte na záložku „Nastavení“ a poté do nabídky vlevo na „API“.
Na této stránce najdete klíče API (Application Programming Interface), které jsou potřebné k připojení k
Odoo.

.. obrázek: starshipit_shipping/starshipit-settings-api.png
:align:center
:alt:Hledání klíčů pro přístup k API služby Starshipit.

Nastavení v Odoo
=============

Instalace
-------

Po nastavení účtu Starshipit jej propojte s databází Odoo. K tomu přejděte na
Modul „Aplikace“ společnosti Odoo, vyhledejte modul „Starshipit Shipping“ a klikněte
:guilabel:`Aktivovat“ a nainstalovat ji.

.. obrázek: starshipit_shipping/starshipit-app.png
:align:center
:alt: Modul Starshipit v modulu Aplikace Odoo.

Konfigurace
-------------

Jakmile je nainstalována, aktivujte funkci přejít na: „Inventář“ - „Konfigurace“
Nastavení“. V sekci „Připojení k přepravcům“ aktivujte „Starshipit“.
Možnost připojení.

Po aktivaci Starshipit Connectoru klikněte na Starshipit Shipping Methods.
pod názvem zásilkového služby. Jakmile se dostanete na stránku „Způsoby doručení“, klikněte
:guilabel:`Vytvořit“.

..tip:
:guilabel:`Způsoby dopravy“ lze také získat kliknutím na „Sklad -->
Konfigurace --> Dodání --> Způsoby doručení.

Starshipit v Odoo nastavte vyplněním políček na formuláři „Dopravní metody“ jako
pokračuje:

- :guilabel:`Dopravní metoda“: zadejte „Starshipit“.
- :guilabel:`Dodavatel“: vyberte „Starshipit“.
- :guilabel:`Produkt pro doručení“: přiřaďte nebo vytvořte produkt, který se objeví na prodejních stránkách.
řádku objednávky, když se vypočítá cena dopravy.

.... poznámka::
V této části jsou popsány konfigurační pole specifická pro Starshipit. Pro více informací
o dalších polích se dozvíte v dokumentaci :doc:`../setup_configuration`.

V záložce „Konfigurace Starshipitu“ vyplňte tyto pole:

- :guilabel:`Klíč pro přístup k API Starshipit“: zadejte klíč pro přístup k API
:ref:`získané z Starshipit <inventory/shipping_receiving/star-api>`.
- :guilabel:`Heslo k předplatnému Starshipit“: zadejte klíč k předplatnému, který jste obdrželi ze stejného místa
jako API klíč:ref:`<inventory/shipping_receiving/star-api>`.
- :guilabel:`Původní adresa“: Zadejte adresu, odkud jsou produkty zasílány.
důležité pro výpočet přepravních sazeb a vytváření štítků
<Inventura/Přijímání a výdej/Hvězdička>.
- :guilabel:`Výchozí typ balení“: Zadejte výchozí typ balení, který zahrnuje hmotnost prázdného
balíček při automatickém vypočítávání poštovného.

.. důležité::
Chcete-li nastavit výchozí typ balíčku, funkce *Packages* **musí být** zapnutá.
:menu:„Nastavení -> Konfigurace -> Nastavení“.

- Manuálně: Uložte formulář kliknutím na ikonku mraku vedle tlačítka „Doručení“.
Metody / Nové chlebové kousky.

Pro načtení nově nakonfigurovaných přepravních produktů klikněte na tlačítko „Vybrat službu spojenou s
Odkaz na účet Starshipit v záložce „Konfigurace“ níže.

Tím se otevře okno „Zvolte službu Starshipit“. V
V poli „Doručovací služba“ vyberte požadovanou dopravní společnost pro doručení a vrácení zboží.
z rozbalovací nabídky. Nakonec klikněte na tlačítko „Potvrdit“.

Vybraný způsob doručení se zobrazí v poli „Název služby“.

Příklad:
Příklad produktu společnosti Starshipit, který je vytvořený v Odoo:

|:guilabel:`Sendle: Osobní odběr Sendle“
| :guilabel:`Dodání produktu“: „Doručení pomocí Sendle“
| :guilabel:`Kód služby Starshipit“: „STANDARD-DROPOFF“

.. obrázek: starshipit_shipping/starshipit-configuration.png
:align:center
:alt:Příklad dodání produktů nakonfigurovaných v Odoo.

..tip:
Starshipit neposkytuje testovací klíče, když společnost testuje odeslání balíčku v Odoo.
To znamená, že pokud je vytvořen balíček, účet může být naúčtován.

Odoo obsahuje v sobě vrstvu ochrany před nechtěnými účty při používání testovacích prostředí.
V rámci testovacího prostředí se při použití způsobu dopravy vytváří štítky.
ihned po vytvoření - tento krok probíhá automaticky. Prosím, zkontrolujte, že závislosti
použitého dopravce, může být účet na tisk štítku naskenován, pokud nebyl
Objednávka je ručně zrušena na portálu kurýrní služby.


Přepínání mezi testovacím a produkčním prostředím provádějte kliknutím na tlačítko „Prostředí“.
tlačítko v horní části formuláře pro způsob dopravy.

... inventář/přijetí/hvězdičkový štítek:

Vytvořte štítek pomocí Starshipit
--------------------------------

Při vytváření nabídky v Odoo přidejte způsob dopravy Starshipit kliknutím na tlačítko :guilabel:`Add
tlačítko „Odeslat“.

V okně „Přidat způsob dopravy“ vyberte Starshipit v poli „Způsob dopravy“.
Metoda pole.

Vypočítejte poštovné kliknutím na tlačítko „Získat sazbu“.
Konečně klikněte na tlačítko „Přidat“ a přidejte náklady na dopravu do řádku objednávky.
*doručovací produkt*.

.. poznámka::
Automaticky vypočítává náklady na dopravu pro Starshipit v obou modulů Odoo Sales a eCommerce.
aplikace.

Poté zkontrolujte dodání a vytvořte dokumenty o přepravě štítku.
Chatování zahrnuje následující:

#:guilabel:`Štítek(y) pro zaslání“ v závislosti na počtu balíků.
#:guilabel:`Číslo zásilky“ pokud vybraný přepravce tuto funkci podporuje.
#:guilabel:`Návratový štítek(y)“ pokud je připojení Starshipit nastaveno pro návraty.

.. obrázek: starshipit_shipping/starshipit-shipping.png
:align:center
:alt: Příklad odeslané objednávky v Odoo.

.. důležité::
V Odoo se hmotnost balíčku vypočítává součtem váhy produktů a prázdného obalu.
uloženy v databázi. Ujistěte se, že je vybrána správná možnost dopravy, protože hmotnost balíku
automaticky neověřené.

Zkontrolujte adresu cílové destinace, protože Starshipit kontroluje tuto adresu při vytváření objednávky.

Nakonec někteří kurýři mohou požadovat další informace, například e-mailovou adresu nebo telefonní číslo.
Ujistěte se, že je při odeslání dopravní objednávky zadána veškerá potřebná informace.

Vrácení zboží
-------

Starshipit umožňuje vrácení zásilek následujícími kurýry:
 * Australská pošta eParcel
 * TNT
 * Kurýři prosím
 * Aramex
 * StarTrack
 * DHL Express
 * NZ Post Domestic

Toho lze dosáhnout kliknutím na tlačítko „Vrácení“ v objednávce dodání, kterou chcete vrátit.
Pokud zvolený kurýr podporuje vrácení, tlačítko „Vytisknout štítek pro vrácení“ bude
k dispozici.

Zrušení
-------------

Pokud je v Odoo zrušen dodací příkaz, bude automaticky archivován ve Starshipit.
Zrušení však nebude zasláno kurýrovi přímo, takže se ujistěte, že se přihlásíte na
platformu kurýrní společnosti pro ruční zrušení.
