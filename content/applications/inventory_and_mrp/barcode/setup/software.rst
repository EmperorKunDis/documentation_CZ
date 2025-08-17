=============================
Kódy produktu a umístění
=============================

.. |EAN| nahradit za: zkratku: EAN (Global Trade Item Number)

Operace inventarizace, jako je například konfigurace produktů, lze zefektivnit využitím čárového kódu.
skenovací funkce. Přiřazení čárových kódů produktům a lokalitám je klíčový krok při používání
Aplikace **Barcode** umožňuje uživatelům pohodlně vyplnit pole pomocí čtečky čárových kódů. To snižuje
ruční vkládání, snižuje chyby a zrychluje běžné úkoly jako výběr produktu nebo umístění.
přidělení a úpravy zásob.

Konfigurace
=============

Nomenklatura čárového kódu
--------------------

Většina maloobchodních výrobků používá čárový kód EAN-13, také známý jako globální identifikační číslo obchodu (GTIN).
Pro vytvoření nového GTIN je potřeba mít GS1 Company Prefix. Více viz: :doc:`GS1
nomenklatura pro více informací o používání tohoto systému.

Odoo podporuje použití jakéhokoliv řetězce jako čárového kódu, takže uživatelé mohou také vytvářet vlastní interní odkaz.
používání s čtečkami čárových kódů. Viz také:
se dozvědět o volitelných konvencech kolem čárového kódu a výchozích hodnotách v Odoo

Pro změnu označení čárového kódu přejděte na:
Přejděte do části „Čárový kód“ a vyberte si z názvosloví podle
:guilabel:`Čtečka čárových kódů“.

.. obrázek: software/barcodes-setup-change-nomenclature.png
:alt:Změna názvosloví čárových kódů v nastavení aplikace Sklad.

.. _čárový kód/nastavení/vyhledávání čárového kódu:

Vyhledávání čárového kódu
--------------

Odoo může automaticky přidávat informace o produktu pomocí nastavení „Stock Barcode Database“
pro jakýkoliv zkratkový kód UPC (Univerzální produktový kód), EAN (Číslo evropské položky) nebo ISBN
ISBN) čárový kód.

Pro automatické vyhledávání čárového kódu přejděte na: „Skladové aplikace --> Konfigurace -->
Přejděte do sekce „Čárový kód“ a zaškrtněte políčko u „Sklad“.
Čárový kódová databáze.

.. poznámka::
Databáze hostované na **Odoo.sh** nebo **na vlastním serveru** vyžadují nastavení klíče API:
<barcodelookup/konfigurace>.

.. inventární číslo / čárový kód / nastavení čárových kódů:

Nastavit čárové kódy produktů
====================

Čárové kódy lze přiřadit stávajícím produktům z konfiguračního panelu „Čárové kódy produktů“ nebo
jakýkoliv produkt v aplikacích Inventář, Výroba nebo Nákup. Do pole s čárovým kódem lze zadat
může být buď ručně zadána nebo vložena pomocí skenování.

Při přidávání nového produktu lze využít funkci „vyhledávání čárových kódů“ (viz barcode/setup/barcodelookup).
umožňuje automaticky vyhledávat informace o produktu na základě jeho čárového kódu a nové produkty mohou být
byly do databáze přidány přímo z aplikace Barcode skenováním čárového kódu.

Z aplikace Barcode
----------------

Nové produkty lze přidat do databáze produktů stejně jako jejich dostupnost.
inventář sledovaný pomocí aplikace Barcode, pokud je aktivována funkce vyhledávání čárových kódů
„Nastavení čárového kódu / nastavení skenování čárových kódů“ je zapnuté. Chcete-li vytvořit nový doklad pro skenování nových produktů, vyberte
z jedné ze dvou metod:

#Od hlavní stránky aplikace Barcode stiskněte tlačítko „Operace“, poté „Pokladny“ a nakonec
klikněte na tlačítko „Nový“.
#. Skenujte tištěné štítky s názvem „Pokladní doklady (WHIN)“.

.. obrázek: software/nový-pokladní-prostředek.png
:alt: Prázdný nový doklad.

Při skenování produktu, který není v současné době skladem, se zobrazí zpráva, že produkt
existuje s možností tlačítka „Vytvořit nový produkt“. Po stisknutí tohoto tlačítka se vyhledá
„Vyhledávání čárového kódu <https://www.barcodelookup.com/>“_ databáze produktů, které odpovídají danému kódu
formát, vytvořit novou definici produktu v databázi Odoo s dostupnými informacemi a přidat
Tento produkt do faktury, abychom mohli sledovat jeho množství na skladě.

.. obrázek: software/čárový kód pro nový produkt.png
:alt: Nové potvrzení produktu.

.. poznámka::
I když je zrušen příkaz k převodu s produktem vytvořeným pomocí **Barcode**, produkt
zůstává v seznamu produktů aplikace Inventář, pokud není smazán.

Z produktové podoby
-------------------

Čárové kódy lze přidat jak ke stávajícím produktům, tak i nově vytvářeným.
formulář pro konfiguraci produktu. Chcete-li zobrazit formulář pro konfiguraci produktu, přejděte na:
Produkty --> Produkty' a vyberte produkt, ke kterému chcete přidat čárový kód.

V záložce „Obecné informace“ klikněte na pole „Čárový kód“, abyste buď mohli zadat
čárový kód nebo použít skener, abyste zadali hodnotu čárového kódu.

.. obrázek: software/barcode-add-to-product-form.png
:alt:Záložka „Čárový kód“ na produktovém formuláři s aktivním kurzorem.

.. poznámka::
Pokud používáte varianty produktů:
konfigurovat čárové kódy pro jednotlivé varianty a ne pro šablonu produktu, aby bylo možné skenovat
získat varianty.

Z nastavení inventáře
-----------------------

Pro přístup k konfigurační stránce „Kódy výrobků“ přejděte na:
Konfigurace --> Nastavení“. V sekci „Čárový kód“ pod položkou „Čárový kód
Funkce skenování, klikněte na ikonu „fa-arrow-right“ a zvolte možnost „Nastavit štítky produktů“.
v seznamovém pohledu klikněte na sloupec „Čárový kód“ pro jakékoliv zboží a zadejte jeho čárový kód.
Scanner bude tento údaj vyplňovat při skenování produktu.

.. obrázek: software/produktove-kodovani-konfigurace.png
:alt:Vybrat pole Čárový kód v dialogovém okně Konfigurace produktu.

.. tip::
Pro filtrování produktů bez čárových kódů zatím klikněte na ikonu :icon:`fa-sort-desc`.
:guilabel:`(Přepínač vyhledávacího panelu)` ikonu, abyste mohli přidat vlastní filtr, kde
vlastností je: guilabel:"nepovinná".

.. obrázek: software/barcode-filter-for-no-barcode.png
:alt: „Přidat vlastní filtr“ s nastavením „Čárový kód není nastaven“.

.._čárový kód/nastavení/umístění:

Vytiskněte čárový kód pro umístění
=======================

Čárové kódy lze přiřadit konkrétním místům, aby bylo možné sledovat, kde jsou produkty skladovány a řídit přesuny.
a jsou automaticky k dispozici, pokud je aktivní :doc:`Skladovací místa
Funkce „<../../inventory/warehouses_storage/inventory_management/use_locations>“ je aktivní.

Pro tisk čárových kódů pro umístění přejděte na: „Aplikace skladu“ --> Konfigurace -->
Nastavení“, posuňte se dolů do části „Sklad“ a klikněte na ikonku „fa-arrow-right“.
„Lokalita“. Zaškrtněte políčka pro lokality a tlačítko „Tisk“ se objeví.
stáhnout PDF s čárovými kódy pro všechna vybraná místa.

.. obrázek: software/tisk-sklad-kódy.png
:alt:Vybraná více místa uložení s tlačítkem „Tisk“ v horní části zobrazení.
