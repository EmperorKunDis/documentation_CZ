=====================
Spojení s Envi.com
=====================

Envia.com je služba pro zasílání zásilek, která spojuje podniky s více přepravci v rámci systému Odoo.
Mezi funkce patří:

- **Spojení s více dopravci a mezinárodní přeprava**: Porovnejte různé ceny dopravců a vyberte nejlepší
možnost pro domácí nebo mezinárodní přepravu.
- **Automatické vytváření štítků**: Vytvořit štítek při potvrzení objednávky.
- **Kalkulace v reálném čase**: Získávejte sazby na základě podrobností o balení a cílové destinaci.

Nastavení v Envii
==============

Nejprve si vytvořte účet a aktivujte
Potřebné přepravce. Pak získáte API klíč, který slouží k propojení
Do databáze Odoo.

Vytvořte si účet a aktivujte dopravce
---------------------------------------

Začněte na stránce „Envia.com <https://www.envia.com>“.

Po přihlášení v levém sloupci klikněte na položku „Nastavení“ - „Možnosti tisku“.
Dopravci“. Vyberte zemi pro nastavení měny a zobrazení dostupných dopravců.

.. důležité::
Při registraci se ujistěte, že vyberete správný jazyk a zemi v horním pravém rohu.
na rohu. To ovlivňuje měnu účtu!

.. obrázek:: envia_shipping/envia-registry-process.png
:alt:Registrační proces na webu společnosti Envia.

Po rozhodnutí o požadovaném poskytovateli klikněte na tlačítko „Aktivovat“ a poté na „Služby“.
vybrat dostupné možnosti dopravy.

..tip:
Bilance se vždy zpracovává v měně země, která odpovídá primárnímu způsobu fakturace.
adresu. Pokud společnost působí v několika zemích, zvažte vytvoření samostatných účtů pro každou
každé místo.

.. poznámka::
Envia vám zašle SMS nebo zprávu přes WhatsApp, aby potvrdila e-mailovou adresu a telefonní číslo.

.. obrázek:: envia_shipping/dopravci-a-sluzby.png
:alt:Vyberte služby přepravce.

Vytvořit přihlašovací údaje na webu Envia.com
------------------------------

Přejděte na webovou stránku „Envia.com <https://www.envia.com>“, přejděte do sekce „Vývojáři –> API klíče“ a
v levém menu pak klikněte na „Přidat“ pro vytvoření nového klíče.

Tento klíč je nutný k ověření připojení Odoo s Envia.com. Získejte jej kdykoliv na
Vraťme se zpět do části „API klíče“.

.. obrázek: envia_shipping/envia-token.png
:alt:API klíče v Envia.com.

Nastavení v Odoo
=============

:ref:`Nainstalujte modul <general/install> Envia Shipping (delivery_envia) a
pokračujte do dalších částí, kde konfigurujete integraci v Odoo.

Konfigurace připojení k dopravci Envia.cz
------------------------------------------

Po aktivaci připojení Envia.com vytvořte způsob doručení kliknutím na
Vyberte položku „Sklad --> Konfigurace --> Způsoby dodání“ a klikněte na „Nový“.

Vyplňte následující pole:

- :guilabel:`Metoda doručení“: Jméno metody doručení, např. „Envia.com“.
- :guilabel:`Poskytovatel“: Vyberte „Envia“.
- :guilabel:`Dodací produkt“: Produkt uvedený na prodejním dokladu jako dodací poplatek.
Musí být vytvořen konkrétní produkt pro dodání pro Envia.com.
- V záložce „Konfigurace Envia“ zadejte :guilabel:`Token přístupu k produkci Envia“.
- V záložce „Konfigurace Envia“ zadejte :guilabel:`Token přístupu do testovacího prostředí Envia“.
- :guilabel:`Procento pojištění“: Pokud je potřeba pojištění, vložte procento hodnoty do
Pokud ano, nastavte ji na nějakou hodnotu. Cena pojištění se vypočítává až poté, co je zadána.
Vytvořená štítek je k dispozici i pro zásilky LTL.

..tip:
Je nutné vyplnit jak token produkce, tak i token testovacího prostředí, ale může zůstat jako náhodný.
ještě není ověřené, takže nemá žádnou hodnotu.

Poznámky k balíčku Envia Default Package:

- Hmotnost je uvedena v jednotkách :guilabel:`mm` a :guilabel:`kg“. Hmotnost se vztahuje na obal
sám o sobě, nikoli jeho obsah. Ponechte hmotnost na 0, pokud nebyla zaznamenána žádná hmotnost a nastavte maximální hmotnost
pokud není stanoveno omezení, na „0“.
- :guilabel:`Typ balíku Envia“: Výchozím nastavením je „Box“. Zkontrolujte, zda je správný typ
zvolené, protože ovlivňuje dostupné přepravce a možnosti zobrazované v závislosti na tomto
výběru.

Jakmile jsou všechny předchozí pole správně nastavená, přejděte na kartu „Nastavení Envii“ a
zobrazí pole „Název služby Envia.com“ a klikněte na ikonu „Obnovit“ (Refresh).
ikona pro synchronizaci operátorů. V okně, které se objeví, vyberte operátora a úroveň služeb
z kandidátky.

.. obrázek: envia_shipping/envia-popup.png
:alt:Pop-up okno s informacemi o poskytovateli služeb a přepravci Envia.com.

.. důležité::
Enia si ponechává jako hlavní měnu účtu pevnou. Chce tak poskytnout přesnější konverze
za dopravu uveďte měnu, která je nastavena pro účet na Envii.
je nutné změnit zemi. Výchozí zemí je ta, ve které se nacházíte.
spojené s touto společností.

.. poznámka::
Pokud je potřeba více možností dopravy, vytvořte si další způsoby dopravy v Odoo a upravte jakýkoliv
parametrem jako je balík, dopravce nebo služba.

...Inventarizace, příjem a expedice zboží:

Informace o dopravě
--------------------

Pro vytvoření poštovních štítků pomocí služby Envia.com je nutné vyplnit následující informace
přesně a kompletně v Odoo:

#**Informace o zákazníkovi**: Při vytváření nabídky zkontrolujte vybraného zákazníka.
platná telefonní čísla, e-mailová adresa a fakturační adresa.

Chcete-li ověřit, vyberte pole „Zákazník“ a otevřete jejich kontaktní stránku. Zde přidejte jejich
adresu dodání do pole „Kontakt“ spolu s jejich číslem mobilního telefonu a
:guilabel:`E-mailová adresa.“
#**Hmotnost produktu**: Zajistěte, aby všechny položky v objednávce měly specifikovanou hmotnost.
v záložce „Sklad“ produktové karty. Viz část „Hmotnost produktu“.
Pro podrobné pokyny přejděte na část „Nastavení hmotnosti“ v článku „Inventarizační a příjmový proces“.
#**Skladová adresa**: Všechny balíčky jsou odesílány z uvedené adresy v
skladu, ujistěte se, že nastavíte adresu pro správné generování štítku.

Návod na vyplnění adresy
---------------------

Každá země má své vlastní pravidla, jak adresu vyplnit. Toto je kompletní průvodce pro každou
Očekávané výjimky země:

.. seznam-tabulka::
:hlavičkové řádky: 1
:sloupek: 1

   * – Země
     - Ulice
     - Ulice 2
     - Město
     - Státní identifikace
   * Argentina
     - Ulice a číslo
     - Lokalita
     - Město
     - Provincie
   * Brazílie
     - Výjimka
     - Sousedství
     - Město
     - Stát
   * –Chile
     - Ulice a číslo
     - Město
     - Obec
     - Region
   * – Kolumbie
     - Ulice a číslo
     - Není potřeba
     - Obce
     - Oddělení
   * Guatemala
     - Ulice a číslo
     - Sousedství
     - Město
     - Stát
   * Mexiko
     - Ulice a číslo
     - Sousedství
     - Město
     - Stát
   * Uruguay
     - Ulice a číslo
     - Doplňující informace
     - Lokalita
     - Stát

Země, které zde nejsou uvedeny, se zadávají normálně.

.. poznámka::
Pro některé země není poštovní směrovací číslo běžně vyžadováno. Pokud je prázdný, použije Odoo kód
služby přibližného určení PSČ.

Pro Kolumbii je kód PSČ vypočítán z města uvedeného v proměnné city_id, pokud je místo určení
Pokud je pole zip instalováno, jinak bude použito pole zip.

.. poznámka::
Kolumbie a Mexiko mají seznam měst označených jako „city_id“ v Odoo. Pokud je nastaven parametr „city_id“,
Pokud není nastavené, pak se použije pole město.

.. poznámka::
V Mexiku mohou někteří dopravci vyžadovat pole „kolonie“, které je obvykle známé jako
sousedství. Není vždy povinná, ale když používáte **EDI pro Mexiko (Pokročilé
modulu funkcí (viz guilabel:Colony).

.. poznámka::
V Brazílii je adresa rozdělena tak, aby vyhovovala předpisům, proto se používá „street_name“ pro ulici
jenom název. „street_number1“ se používá pro číslo domu a „street_number2“ pro druhé číslo domu
doplňuje. Tato logika platí i v případě, že je nainstalován modul „Prodloužené adresy“.

Vytvářejte štítky pomocí Envie
==========================

Při vytváření nabídky v Odoo přidejte dopravu a produkt „Doprava Envia.cz“.
Poté zkontrolujte dodání a vytvořte dokumenty o přepravě štítku.
chatter, kterými jsou následující:

#:guilabel:`Štítek(y) pro zaslání“ v závislosti na počtu balíků.
#:guilabel:`Návratová štítka“ pokud je pro návraty konfigurován připojovací bod Envia.com.

.. důležité::
Při vytváření štítků automaticky účet naúčtuje a konečnou částku zašle na uvedený účet.
částka je zaznamenána v chatu. Pokud dojde k více měnovým operacím, částka zaznamenaná
Výpočet byl proveden na základě sazby společnosti Odoo. Skutečné sazby se mohou lišit.

Dále je k dispozici sledovací číslo.

.. poznámka::
Brazilské úřady mohou požadovat fakturu týkající se přepravy (NFe). Je doporučeno
připevnit fakturu objednávky spolu s etiketou.

Zahraniční přeprava
----------------------

Pro mezinárodní zásilky je nutné vyplnit jak kód HS, tak i zemi
„Původ zboží“ a „Zásoby“, oba jsou k dispozici na záložce „Sklad“.

LTL zásilky
-------------

Přepravní štítky pro zásilky LTL lze vytvořit prostřednictvím připojení Envia. Pojištění pro zásilky LTL
na základě pojistného procenta uvedeného v objednávkovém formuláři.

.. důležité::
Pro Mexiko je nutné vytvořit fakturu o převzetí zboží, takže pro odeslání zásilky je potřeba použít Odoo.
poslat kód UNSPSC obsahu i jednotku měření pro přepravu.
**X8A - Dřevěná paleta**.

.. poznámka::
Při výběru „palety“ jako typu balíku Envia jsou k dispozici další služby.
doručovací metoda, která umožňuje vybrat si další služby jako například asistenci při použití výtahu
doručování o víkendech.

...Inventarizace, přijímání a nastavení konfigurace / zrušení:

Sledování a zrušení
=========================

Dodávky zaregistrované u společnosti Envia lze sledovat pomocí tlačítka „Sledování“ chytrého menu.
dodacímu listu nebo použít odkaz na sledování zásilky v zákaznickém portálu
<../../../obecne/ucastnici/portal>

.. obrázek:: envia_shipping/envia-zakaznicka-zalozka-sledovani.png
:alt:Sledování v zákaznickém portálu.

Často kladené dotazy
===

Měření objemového zatížení
---------------------------

Mnoho dopravců má více měření hmotnosti. Je tu skutečná váha produktu
balík a jeho hmotnost v objemu. Hmotnost v objemu je množství místa, které balíček zabere při
v přepravě, tedy fyzických rozměrech balíku.

.. poznámka::
Vzhledem k objemové hmotnosti je možné, že skutečná hmotnost na štítku bude vyšší než
vypočítaná hodnota.

Jaké tiskové možnosti jsou k dispozici?
-------------------------------------

Na webu Envia.cz v sekci „Nastavení“ -> „Tiskové možnosti a nastavení tisku přepravců“ pro každého
Při zobrazení přepravce se ujistěte, že používáte vhodný formát pro vybraného přepravce.

Není k dispozici potřebná služba
-----------------------------------

U dostupných operátorů se ujistěte, že jsou zapnuté přes Envii.

Kdo bude platit cla?
----------------------------

Důležité je zajistit, aby pokud existují vývozy do jiných zemí, používali dopravce společnosti Envia
nastavení, které umožňuje konfigurovat, zda je hrazena odesílatel nebo příjemce.

Co je „chyba Envie“?
----------------------

Je to zpráva, která se objeví v případě chyby v Envii. Tato zpráva uvádí, co se stalo špatně
jejich platformě, aby se mohla adresovat.
