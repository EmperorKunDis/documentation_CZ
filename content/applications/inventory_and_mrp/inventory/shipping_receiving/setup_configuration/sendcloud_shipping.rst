=====================
Synchronizace s Sendcloudem
=====================

SendCloud je agregátor dopravních služeb, který usnadňuje integraci evropských přepravců.
dopravci s Odoo. Jakmile je integrace dokončena, uživatelé mohou vybírat dopravce při operacích skladu
jejich databáze Odoo.

.. viz také:
„Dokumentace pro integraci Sendcloudu <https://support.sendcloud.com/hc/en-us/articles
   /360059470491-Odoo-integration>`_

Nastavení v Sendcloudu
==================

Vytvořte si účet a aktivujte dopravce
---------------------------------------

Pro začátek navštivte stránku „Platforma Sendcloudu“ (https://www.sendcloud.com/) a zaregistrujte si účet
a vytvořit přihlašovací údaje konektoru. Přihlásit se do Sendcloudu nebo založit nový účet, pokud
nebylo nutné.

.. poznámka::
Pro vytvoření nového účtu požádá Sendcloud o :abbr:`DPH (Daň z přidané hodnoty)
číslo nebo zkratku EORI (Registrace a identifikace ekonomických subjektů). Po
při dokončování nastavení účtu aktivujte (nebo deaktivujte) dopravce, které budou použity
v databázi Odoo.

.. důležité::
Odoo integrace se službou Sendcloud funguje pouze na bezplatných plánech Sendcloudu, pokud je k účtu přidán bankovní účet.
protože Sendcloud nezasílá zdarma. Chcete-li používat pravidla pro zasílání nebo individuální přepravce
kontakty je nutné mít zaplacený tarif služby Sendcloud.

... /skladovani-expedice-prijem/sendcloud-sклад-konfigurace:

Konfigurace skladu
-----------------------

Jakmile se přihlásíte do svého účtu Sendcloudu, přejděte na: „Nastavení -> Doprava ->
Adresy“, a do pole pro „Guilabel“ zadejte „Skladová adresa“.

.. obrázek:: sendcloud_shipping/settings-shipping.png
:align:center
:alt:Přidání adres v nastavení Sendcloudu.

Pro zpracování vrácených zásilek je nutné také vyplnit adresu pro vrácení zboží.
V sekci „Různé“ je pole s názvem „Jméno adresy (volitelně)“.
Do pole „Sklad“ je nutné zadat název skladu v Odoo a zadané znaky musí být stejné.

Příklad:

|  **Konfigurace SendCloudu**
| :guilabel:`Různé“
| :guilabel:`Název adresy (volitelné pole)`: „Sklad č. 1“
| :label_guid:„Značka“: „Výchozí“

|  **Konfigurace skladu Odoo**
|:guilabel:`Sklad`: „Sklad #1“
| :guilabel:`Krátké jméno“: „WH“
| :guilabel:`Společnost`: „Moje společnost (San Francisco)“
| :guilabel:`Adresa“: „Moje společnost (San Francisco)“

Pozor na vstupy do pole :guilabel:`Sklad`, jak pro konfiguraci Odoo, tak pro konfiguraci
konfigurace Sendcloudu jsou stejné.

Vytvořit přihlašovací údaje pro Sendcloud
------------------------------

V účtu Sendcloud přejděte do položky „Nastavení“ v nabídce.
ano. Dále hledejte „Odoo Native“. Pak klikněte na „Připojit“.

Po kliknutí na „Připojit“ se stránka přesměruje do nastavení „API Sendcloud“.
stránka, kde se vytváří veřejné a soukromé klíče. Dalším krokem je pojmenování
:guilabel:`Integrace“. Název je následující: „Odoo CompanyName“, s uživatelským
název společnosti nahrazující „Společnost“ („např. Odoo StealthyWood“).

Poté zaškrtněte políčko vedle :guilabel:`Servisní body“ a vyberte způsoby dopravy pro tento
integrace. Po uložení jsou vygenerovány veřejný a soukromý klíč.

.. obrázek: sendcloud_shipping/public-secret-keys.png
:align:center
:alt: Konfigurace integrace Sendcloudu a získání přihlašovacích údajů.

Nastavení v Odoo
=============

Pro bezproblémovou integraci Sendclou s Odoo je třeba nainstalovat
<inventar/versand/empfang/sendcloud-modul>“ a „odkaz
>Inventuru / Přijímání a výdej / Propojení s modulem SendCloud
Účet u Sendcloudu. Pak je třeba nastavit pole v Odoo podle návodu:
<Inventura/Přijetí a odeslání/SendCloud - informace o dopravě>“, takže Sendcloud může přesně vytáhnout informace o dopravě
Data pro vytvoření štítků.

.. viz také:
:ref:`Povolit výdejní místa na webu <inventory/shipping_receiving/sendcloud-pickups>`

... inventář/přijímání/odesílání/modul SendCloud:

Nainstalujte modul pro odesílání zásilek Sendcloud
---------------------------------

Po nastavení a konfiguraci účtu Sendcloud je čas na konfiguraci databáze Odoo.
začít, přejít do modulu „Aplikace“ v Odoo, vyhledat integraci „Sendcloud Shipping“,
a nainstalovat ji.

.. obrázek: sendcloud_shipping/sendcloud-mod.png
:align:center
:alt: Modul pro odesílání zásilek od společnosti Sendcloud v modulu Odoo Apps.

...Inventarizační/přijímací/odesílací modul pro SendCloud:

Konfigurace připojení k řešení Sendcloud
------------------------------------------

Jakmile je modul nainstalován, aktivujte jej v menu „Sklad“ - „Nastavení“ - „Doprava“.
Konfigurace --> Nastavení. V nastavení lze najít
:guilabel:`Dopravní spojky“ v sekci „Součásti“.

Po aktivaci modulu Sendcloud Connector klikněte na modul Sendcloud Shipping.
Odkaz na metody níže uvedeného připojení. Jakmile se dostanete na stránku „Metoda dopravy“, klikněte
:label:`Nový“.

..tip:
:guilabel:`Způsoby dopravy“ lze také získat kliknutím na „Sklad -->
Konfigurace --> Dodání --> Způsoby doručení.

Vyplňte následující pole v novém formuláři pro způsob doručení:

- :guilabel:`Dopravní metoda“: typ „Sendcloud DPD“.
- Vyberte možnost „Sendcloud“ z roletky.
- :guilabel:`Produkt pro doručení“: nastavte produkt, který byl pro tento způsob dopravy nakonfigurován nebo
vytvořit nový produkt.
- V záložce „Konfigurace SendCloud“ zadejte veřejný klíč SendCloud.
- V záložce „Konfigurace SendCloud“ zadejte „Tajný klíč SendCloud“.

... skladování, příjem a odesílání přepravců:

Místo vyzvednutí
~~~~~~~~~~~~~

Doručení služebního místa od společnosti Sendcloud
<https://support.sendcloud.com/hc/cs/articles/360026097951-FAQ-Servisní body> umožňuje zákazníkům
vyberte si místo vyzvednutí (např. poblíž obchod nebo schránku) namísto vstupu do soukromé dodávky
adresa.

Aby se funkce zapnula, přejděte na formulář pro způsoby dopravy a v poli „SendCloud“ vyberte možnost „Zapnuto“.
Konfigurace“ v záložce „Možnosti“, kde je možné zapnout „Používat Sendcloud“.
Funkce umístění.

.. důležité::
Vybírání výdejního místa je k dispozici pouze v aplikaci **Website** (online nákupní pohled).
V současné době není možné manuálně vybrat místo pro vyzvednutí prostřednictvím aplikace **Prodej** (
interní databázový pohled).

Příkladem je např. způsob dopravy jako Sendcloud Mondial Relay, v takovém případě musí zákazník
Vyberte si místo vyzvednutí během procesu objednávání na webových stránkách. Pokud není vybráno žádné místo k vyzvednutí,
dodací list nelze v Odoo ověřit.

Přeprava zboží
~~~~~~~~~~~~~~~~~~~~~~

Po konfiguraci a uložení formuláře proveďte následující kroky pro načtení produktů dopravy:

- V záložce „Konfigurace SendCloud“ formuláře pro nový způsob dopravy klikněte
na odkaz „Nahrát produkty pro zasílání zásilek přes SendCloud“.
- Vyberte dopravní produkty, které chcete používat pro dodávky a vrácení zboží.
- Klikněte na tlačítko „Vybrat“.

Příklad:
Příklad produktů služby zasílání zásilek od společnosti Sendcloud nakonfigurovaných v Odoo:

| :guilabel:`DODÁNÍ`
| :guilabel:`Doprava produktu“: „DPD Home 0–31,5 kg“
| :guilabel:`Dopravce“: „DPD“
| :guilabel:`Nejmenší váha“: „0,00“
|  :guilabel:`Maximální váha“: „31,50“

:guilabel:`Státy“: „Rakousko“ „Belgie“ „Bosna a Hercegovina“ „Bulharsko“ „Chorvatsko“ „Česká republika“
„Republika“ „Dánsko“ „Evropa“ „Finsko“ „Francie“ „Německo“ „Řecko“ „Maďarsko“ „Island“
„Irsko“ „Itálie“ „Lotyšsko“ „Lichtenštejnsko“ „Litva“ „Lucembursko“ „Monako“ „Nizozemí“
„Norsko“ „Polsko“ „Portugalsko“ „Rumunsko“ „Srbsko“ „Slovensko“ „Slovinsko“ „Španělsko“ „Švédsko“
„Švýcarsko“

| :guilabel:`VRÁTIT SE“
| :guilabel:`Návratový produkt dopravy“: „DPD Návrat 0–20 kg“
| :guilabel:`Vrátit dopravci“: „DPD“
| :guilabel:`Návrat minimální hmotnosti“: „0,00“
| :guilabel:`Maximální hmotnost“: „20,00“
| :guilabel:`Země vrácení“: „Belgie“ „Nizozemsko“

.. obrázek: sendcloud_shipping/sendcloud-example.png
:align:center
:alt:Příklad dodání produktů nakonfigurovaných v Odoo.

..tip:
SendCloud neposkytuje testovací klíče, když společnost testuje odeslání balíku v Odoo.
Pokud je vytvořen balíček, bude k úhradě použit zvolený účet Sendcloud, pokud není nastaveno jinak.
spojený balíček je zrušen do 24 hodin od vytvoření.

Odoo obsahuje v sobě vrstvu ochrany před nechtěnými účty při používání testovacích prostředí.
V rámci testovacího prostředí se při použití způsobu dopravy vytváří štítky.
- tento se sám po vytvoření zruší - to se děje automaticky. Testovací a produkční
nastavení prostředí lze přepínat pomocí příslušných tlačítek pro chytré funkce.

... inventarizaci, přijímání a odesílání zásilek pomocí SendCloud Shipping Info:

Informace o dopravě
--------------------

Pro vytvoření dodacích štítků pomocí služby Sendcloud je nutné vyplnit následující informace
přesně a kompletně v Odoo:

#**Informace o zákazníkovi**: při vytváření cenové nabídky zkontrolujte vybraného zákazníka.
platná telefonní čísla, e-mailová adresa a fakturační adresa.

Chcete-li ověřit, vyberte pole „Zákazník“ a otevřete jejich kontaktní stránku. Zde přidejte jejich
adresu dodání do pole „Kontakt“ spolu s jejich číslem mobilního telefonu a
:guilabel:`E-mailová adresa.“

#**Hmotnost produktu**: zajistěte, aby všechny produkty v objednávce měly určenou hmotnost:
:guilabel:`Sklad“ v kartě produktu. Viz část „Hmotnost produktu“.
Pro podrobné pokyny přejděte na část „Nastavení hmotnosti“ v článku „Inventarizační a příjmový proces“.

#**Skladová adresa**: ujistěte se, že název a adresa skladu v Odoo odpovídají :ref:`dříve
definovaný sklad v sekci „Sklad/Příjem a výdej/SendCloud - konfigurace skladu“ v Sendcloudu
konfigurace skladu v Odoo. Pro podrobnosti o konfiguraci skladu v Odoo se podívejte na odkaz:
část „Nastavení zdrojového adresáře“ v třetích stranách dopravy
dokumentace.

Vytvořte štítky pomocí Sendcloudu
==============================

Při vytváření nabídky v Odoo přidejte dopravu a produkt „Doprava odesílaná prostřednictvím Sendcloudu“. Pak
Zkontrolovat dodání. Dopravní štítek je automaticky vygenerován v
chatter, kterými jsou následující:

#:guilabel:`Štítek(y) pro zaslání“ v závislosti na počtu balíků.
#:guilabel:`Návratová štítka“ pokud je pro vrácení zboží nastaveno připojení k Sendcloudu.
#Pokud je požadováno, musí být předložené celní dokumenty.

Dále je k dispozici sledovací číslo.

.. důležité::
Při vytváření štítků se automaticky naúčtuje konfigurovaná cena služby Sendcloud.
účet.

Pravidla dopravy
--------------

Pokud chcete, vytvořte pravidla pro zasílání, abyste automaticky generovali štítky na balení přizpůsobené různým
potřebám produktu. Například lze vytvořit pravidlo pro zákazníky, kteří zasílají drahé šperky
předměty k pojištění.

.. poznámka::
Pravidla dopravy neovlivňují:ref:`vypočítání ceny poštovného.
</předání/přijetí zboží/třetí strana>, a používají se jen k vylepšení procesu
:doc:`vytváření štítků pro zasílání zásilek <labels>“.

Pro použití pravidel dopravy přejděte na: „Inventářová aplikace --> Konfigurace --> Doprava“
Způsoby dopravy“ a vyberte požadovaný způsob „Doprava přes Sendcloud“.

Pod záložkou „Konfigurace Sendcloudu“ v sekci „Možnosti“ vyberte
druhu zásilek se vztahují poštovní předpisy, pomocí :guilabel:`Použít pravidla zasílání Sendcloudu`
pole.

Zde vyberte buď možnost „Dodání zákazníkovi“, „Vrácení od zákazníka“ nebo
:guilabel:`Oba“.

.. obrázek: sendcloud_shipping/enable-shipping-rules.png
:align:center
:alt:Využijte pole Pravidla dopravy.

Pak v sekci „Nastavení“ -> „Dopravní pravidla“ vytvořte nové
nový způsob dopravy kliknutím na „Vytvořit nový“.

V sekci „Akce“ nastavte podmínku, která určí, kdy bude pravidlo platit.
Poté nastavte, co se má stát, když balíčky splňují podmínku.

.. viz také:
„Vytvořte pravidla pro zasílání na Sendcloud
<https://support.sendcloud.com/hc/cs/articles/10274470454386-Jak vytvořit pravidla pro zasílání>

Často kladené dotazy
===

Přeprava je příliš těžká
---------------------

Pokud je zásilka příliš těžká pro službu Sendcloud, která je nakonfigurována, pak se hmotnost rozdělí.
simulovat více balíčků. Produkt bude potřeba umístit do různých balíčků,
:guilabel:`Přezkoumat převod“ a vytvořit štítky.

:guilabel:`Pravidla“ lze v Sendcloudu nastavit i tak, aby se používaly jiné přepravní metody při váze
Je příliš těžká. Nicméně je třeba poznamenat, že tyto pravidla se na výpočet ceny dopravy nebudou vztahovat.
počítání na prodejní objednávce.

Smlouva o osobním přepravci
-------------------------

Použijte vlastní ceny z přímé smlouvy o přepravě prostřednictvím nahrávání souboru CSV po přihlášení do Sendcloudu.
Navigace na: „Nastavení ->Dopravci -> Moje smlouvy“ a poté výběr
smlouva, která má být uzavřena.

.. obrázek:: sendcloud_shipping/contracts.png
:align:center
:alt:Přejděte do sekce smluv v Sendcloudu.

Pod sekcí „Smluvní ceny“ klikněte na „Stáhnout CSV“ a vyplňte
smluvní ceny v sloupci „cena“ šablony CSV souboru.

.. varování::
Ujistěte se, že soubor CSV obsahuje správné ceny, abyste se vyhnuli jakýmkoli nepřesnostem.

.. obrázek: sendcloud_shipping/price-csv.png
:align:center
:alt:Zobrazit ukázkovou smlouvu ve formátu CSV z aplikace Sendcloud, zvýrazněnou cenovou sloupcovou hodnotou.

Nahrajte do Sendclouhotovou CSV soubor a pak klikněte na „Uložit tyto ceny“.

.. viz také:
„Sendcloud: Jak nahrát cenové podmínky s dopravci


Měření objemového zatížení
---------------------------

Mnoho dopravců má několik měření hmotnosti. Je tu skutečná váha produktu v
balíček a tam je volumetrická hmotnost (DFN: „Volumetrická hmotnost je objem balíku
zabírá místo v přepravním prostoru. V jiných slovy je fyzická velikost balení.

..tip:
Zkontrolujte, zda vybraný dopravce již má definované formule pro výpočet objemového zatížení.
hmotnost.

.. viz také:
„Jak vypočítat a automatizovat hmotnost balíku podle objemu“ (<https://support.sendcloud.com/hc/en-us/articles/115003982476-How-to-calculate-and-automate-parcel-volumetric-weight>).


Nelze vypočítat poštovné
---------------------------------

Nejprve ověřte, že produkt, který je odesílán, má hmotnost, která je podporována zvoleným způsobem dopravy.
metoda. Pokud je nastavena, pak ověřte, že cílovou zemi (od adresy zákazníka)
podporované dopravcem. Země původu (skladová adresa) by měla být také podporována
dodavatel.
