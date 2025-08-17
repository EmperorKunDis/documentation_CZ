==============================================
Dodávky a faktury na různé adresy
==============================================

Lidé a firmy často používají oddělené adresy pro fakturaci (účetnictví) a dodání.
účelům. S aplikací pro prodej Odoo *Sales* mohou kontakty mít různé adresy pro doručení
a fakturaci.

Nastavení
========

Pro správné využití více adres v Odoo přejděte na: „Účetnictví ->
Konfigurace --> Nastavení“, a posuňte se dolů k hlavičce „Faktury zákazníkům“. Pak
zaškrtněte políčko.

.. obrázek: různé_adresy/adresa-zakaznika-nastaveni.png
:align:center
:alt:Aktivujte nastavení Adresy zákazníka.

...prodej/zaslání nabídky/kontaktní formulář:

Konfigurace kontaktního formuláře
==========================

Pro přidání více adres k kontaktu přejděte na: „Aplikace pro obchodníky ---> Objednávky ---> Klienti“.
a odstranit všechny výchozí filtry z vyhledávací lišty. Pak klikněte na požadovaného zákazníka a otevřete jeho
kontaktní formulář.

..tip:
Kontaktní formuláře lze využít také v aplikaci Kontakty.

Z kontaktního formuláře klikněte na „Upravit“ a poté vyberte „Přidat“, které se nachází
pod záložkou „Kontakty a adresy“. To vyvolá okno „Vytvořit kontakt“
formulář, ve kterém lze konfigurovat další adresy.

.. obrázek: různé_adresy/kontaktní_formulář_přidat_adresu.png
:align:center
:alt:Přidejte kontakt nebo adresu do formuláře pro přidání kontaktů.

Na okně „Vytvořit kontakt“ klikněte nejprve na výchozí :guilabel:`Ostatní
Zadejte pole „Adresa“ a zobrazí se vám nabídka možností týkajících se adresy.

Vyberte si jednu z následujících možností:

- :guilabel:`Kontakt“: přidává další kontakt do stávajícího kontaktního formuláře.
- :label:Fakturační adresa: přidává konkrétní fakturační adresu k existujícímu kontaktnímu formuláři.
- :guilabel:`Adresa doručení“: přidává konkrétní adresu pro doručování do stávajícího kontaktního formuláře.
- :guilabel:`Další adresa“: přidává alternativní adresu k existujícímu kontaktnímu formuláři.
- :guilabel:Soukromá adresa“ přidává soukromou adresu k existujícímu kontaktnímu formuláři.

Jakmile si vyberete možnost, pokračujte v zadávání odpovídajících kontaktních údajů, které by měly být
používán pro zadaný typ adresy.

.. obrázek: různé adresy/vytvořit kontaktní okno.png
:align:center
:alt: Vytvořit nový kontakt nebo adresu na kontaktním formuláři.

Poté klikněte na tlačítko „Uložit a zavřít“ pro uložení adresy a zavření dialogového okna „Vytvořit kontakt“.
Okno nebo klikněte na tlačítko „Uložit a nový“ pro uložení adresy a okamžitě zadat jinou.

Adresa přidána do citátů
===========================

Když se zákazník přidá do cenové nabídky, objeví se pole „Adresa faktury“ a „Adresa dodání“.
Pole adresy se automaticky vyplní podle kontaktních údajů, které jsou uvedeny na zákaznickém kontaktu.
forma.

.. obrázek: různé adresy/citace-adresa-automaticky-vyplnit.png
:align:center
:alt:Fakturační a dodací adresa se automaticky vyplní v cenové nabídce.

Adresu faktury a adresu pro doručení lze také upravit přímo z
citát kliknutím na tlačítko „Upravit“ a poté kliknutím na tlačítko „➡️ (vpravo
tlačítka pro vložení odkazu vedle každé řádky adresy.

Tyto adresy lze kdykoli aktualizovat, aby bylo možné správně fakturovat a dodávat.

..tip:
Pokud se na formuláři v Odoo provede jakákoliv změna (včetně formulářů Kontakty), pamatujte prosím na kliknutí
:guilabel:`Uložit“ k uložení změn do databáze.
