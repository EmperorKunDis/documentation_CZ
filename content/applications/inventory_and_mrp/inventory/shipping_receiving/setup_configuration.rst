

================
Doručovací metody
================

Při zapnutí v Odoo se nastavení „Způsoby dodání“ přidává možnost výpočtu nákladů na
přepravu na objednávky a nákupní košíky v elektronickém obchodování.

Při integraci s externím dopravcem se ceny přepravy
Jsou vypočítány na základě cenové informace dopravce.

.. viz také:
   - :ref:`Nastavení třetích stran pro dopravu zboží <inventory/shipping/third_party>“
   - „Návody k Odoo: Ceny dopravy


Konfigurace
=============

Pro výpočet dopravy na prodejních a elektronických objednávkách je nutné nainstalovat modul „Náklady na dopravu“.
Pro toto vyhledejte aplikaci „Aplikace“ v hlavním panelu Odoo.

Poté odstraňte filtr „Aplikace“ a zadejte do pole „Hledat…“ „Náklady na dodání“.
baru. Po nalezení modulu „Náklady na dodání“ klikněte na „Aktivovat“, abyste jej nainstalovali.

.. obrázek:setup_configuration/install-module.png
:alt:Nainstalujte modul Náklady na doručení.

…výdejní sklad, expedice a objednávky.

Přidejte dopravu
============

Dopravní metody lze přidat do prodejních objednávek ve formě dodacích produktů, které se zobrazují jako
jednotlivé položky. Nejprve přejděte na požadovanou objednávku prodeje pomocí volby v nabídce:
app --> Objednávky --> Objednávky“.

Na objednávce prodeje klikněte na tlačítko „Přidat dopravu“, které vám otevře okno „Přidat dopravu“.
okně „Způsob dopravy“. Pak vyberte způsob dopravy z seznamu.

Hodnota celkové váhy objednávky je předvyplněna na základě hmotnosti produktů (jejichž hodnoty jsou definovány v
Karta „Inventář“ pro každou položku (v závislosti na typu produktu). Upravte pole a zadejte přesnou hmotnost.
Poté klikněte na tlačítko „Přidat“ pro přidání způsobu dopravy.

.. poznámka::
Hodnota definovaná v poli Celková váha objednávky přepíše hodnotu celkové váhy produktů.
na produktu.

Připočítá se k položce objednávky jako „Dodací produkt“, který je uveden na
forma dopravy.

Příklad:
„Dodávka nábytku“, produkt s pevnou cenou 200 $, je přidán do objednávky
„S00088“.

.. obrázek:: setup_configuration/delivery-product.png
:alt:Zobrazit dodací lístek na řádku prodejního objednávky.

Dodací lístek
--------------

Dopravní metoda přidána k prodejnímu příkazu je spojena s podrobnostmi o dopravci na
dodací příkaz. Chcete-li přidat nebo změnit způsob dodání na samotné dodávce, přejděte do
kartě „Další informace“ a upravte pole „Dodavatel“.

.. obrázek:: setup_configuration/dodací objednávka.png
:alt: Informace o dopravci na dodacím lístku.

.. toctree::
:tituly:

setup_configuration/nové doručovací metody
setup_konfigurace/třetí strana dopravce
setup_configuration/etikety
setup_konfigurace/bpost
setup_configuration/dhl_credentials
setup_configuration/posílání zásilek
setup_configuration/fedex
setup_configuration/sendcloud_doprava
setup_configuration/starshipit_doprava
setup_configuration/ups_credentials
setup_configuration/zebra
setup_configuration/cancel
nastavení konfigurace / faktura
setup_konfigurace/typ_štítku
setup_konfigurace/multi
setup_configuration/tisk_při_validaci
setup_konfigurace/předání
