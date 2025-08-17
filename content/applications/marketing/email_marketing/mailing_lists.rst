=============
Seznamy odběratelů
=============

Seznamy v Odoo se používají jak pro předprodejní, tak i po prodejní komunikaci v modulu *Email Marketing*.
aplikace. Zajišťují prodejním týmům kvalifikované seznamy kontaktů, účastníky skupinového rozhovoru nebo
současní zákazníci, kteří splňují specifická kritéria.

Seznamy e-mailů lze vytvářet v Odoo a exportovat jako stahovatelný soubor nebo do
Aplikace „Znalosti“, „Přístrojové desky“ nebo „Sešity“, nebo importované pomocí vložení a kopírování nebo přes soubor
Nahrát.

Vytvořte seznamy e-mailů
====================

Vytvořit seznam v aplikaci Email Marketing lze přes:menuselection:E-mail
Marketingová aplikace --> Seznamy e-mailů --> Seznamy e-mailů --> Nové“.

Kliknutím na tlačítko New se zobrazí prázdná adresa pro odeslání e-mailu.

.. obrázek: mailing_lists/new-mailing-list-form.png
:align:center
:alt: Pohled na formulář pro odesílání e-mailů v aplikaci Odoo Email Marketing.

V poli „Seznam odběratelů“ nahoře zadejte jméno.

Pokud se má e-mailová adresa zobrazit v seznamu příjemců na stránce správy odběru,
umožňuje jim aktualizovat své preference a zaškrtnout políčko vedle :guilabel:`Zobrazit v předvolbách“.

V horním levém rohu formuláře je dvě tlačítka: :guilabel:`Odeslat poštu`.
a :guilabel:`Odeslat SMS“.

.. důležité:
Tlačítko „Odeslat SMS“ se objeví pouze v případě, že je nainstalována aplikace „Marketing SMS“.

Kliknutím na tlačítko „Odeslat poštu“ se zobrazí samostatná stránka s prázdným e-mailovým šablonou formulářem.
lze vyplnit podle kroků vysvětlených v dokumentu Email Marketing.
<../email_marketing>.

Kliknutím na tlačítko „Odeslat SMS“ se zobrazí samostatná stránka s prázdným vzorem pro odeslání SMS, který lze
vyplněné podle kroků vysvětlených v dokumentu SMS marketing.
<../sms_marketing>.

Na začátku seznamu odběratelů je sada chytrých tlačítek, které zobrazují různé metriky.
připojené k určitému seznamu. Když je na některém z chytrých tlačítek stisknuto, otevře se samostatná stránka.
odhalil a zobrazil podrobné analýzy související s tímto konkrétním statistickým údajem.

Chytré tlačítko dostupné v seznamu adresátů je:

- :guilabel:`Příjemci“: kolik lidí je na seznamu odběratelů
- :guilabel:`Poštovní zásilky“: kolik poštovních zásilek bylo odesláno pomocí tohoto seznamu
- :guilabel:`% Bounce`: procento pošty spojené s touto seznamovou službou, které bylo vráceno
zpět
- :guilabel:`% Opt-out“: procento příjemců, kteří se odhlásili z rozesílek
list
- :guilabel:`% Černá listina“: procento příjemců, kteří se sami z černé listiny vyřadili
mailovou adresu

Jakmile jsou všechny konfigurace na seznamu e-mailů dokončeny, Odoo automaticky přidá nové
seznam na stránku „Seznam“ v aplikaci Email Marketing.
(:menu_selection:`E-mailový marketing - aplikace --> Seznamy e-mailů --> Seznamy e-mailů`).

Přidat kontakty do seznamu rozesílání
============================

V Odoo *Email Marketing* existuje několik různých způsobů, jak přidat kontakty do seznamu adresátů.

Na stránce „Seznamy“ (:menuselection:`E-mailový marketing --> Seznamy e-mailů -->
(Klikněte na odkaz „Počet kontaktů“ v řádku požadované seznamu e-mailových adres.
kam přidat kontakty.

Tím se zobrazí samostatná stránka s kontakty pro daný mailový seznam.
kde lze vytvářet nebo importovat kontakty a poté je přidat do konkrétního seznamu rozesílky.

Tuto stejnou stránku lze také získat kliknutím na požadovaný seznam v:guilabel:Seznam
Stránku seznamu a poté klikněte na tlačítko „Adresáti“ v formuláři pro odesílání e-mailů.

Také odhaluje samostatnou stránku „Kontaktů pro rozesílání“ pro tento konkrétní e-mail.
seznam, kde lze vytvářet nebo importovat kontakty a poté je přidat do konkrétního seznamu pro rozesílání e-mailů.

Kontakty lze také přímo importovat do konkrétního seznamu z :guilabel:`Seznamů rozesílek`.
stránce kliknutím na „Import kontaktů“ v pravém dolním rohu požadované seznamu adresátů.

.. obrázek: mail_list/import-contacts-button.png
:align:center
:alt:Tlačítko pro načtení kontaktů z e-mailové kampaně v Odoo Email Marketing.

Tím se zobrazí okno „Přidat kontakty pro e-mailovou korespondenci“.

.. obrázek: mailing_lists/import-mailing-contacts-popup.png
:align:center
:alt:Příležitostné okno pro přidání kontaktů do poštovní zásilky, které se objevuje v Odoo Email Marketing.

V tomto případě je požadovaná seznam adresátů automaticky vyplněna v poli „Přidat kontakty“.
Pod tím napište nebo vložte e-mailové adresy do pole „Seznam kontaktů“.

Možnost nahrát zemi, společnost nebo další informace je k dispozici pomocí :guilabel:`Nahrát
odkaz na soubor v dolní části okna s formulářem.

Po dokončení kontaktů a konfigurací klikněte na tlačítko :guilabel:`Importovat`.

Přidat kontakty na konkrétní seznam z hlavního seznamu všech kontaktů v
databáze, přejděte na:menu-selection:„E-mailový marketing“ --> „Seznamy e-mailů“ --> „Seznam e-mailů
Kontakty. To odhalí stránku „Seznam kontaktů“, která obsahuje seznam všech
kontakty spojené s každým seznamem odběratelů.

.. obrázek: mailing_lists/mailing-list-page.png
:align:center
:alt:Stránka seznamu na webu aplikace E-mailový marketing Odoo.

Vyhledávací lišta obsahuje výchozí filtr „Vyloučit e-maily na černé listině“.

Na stránce „Kontakty na rozesílání“ lze kontakty vytvářet a importovat.
přidán do seznamu odběratelů.

Chcete-li přidat existující kontakt do seznamu odběratelů, vyberte požadovaný kontakt z
kontaktní formulář, který se zobrazí na stránce „Kontakty“.

V dolní části kontaktního formuláře klikněte na „Přidat řádek“ pod „Seznam e-mailů“.
sloupci, vyberte si požadovaný seznam z roletky a potvrďte výběr.

.. obrázek: mailing_lists/contact-form-mailing-list-add.png
:align:center
:alt:Přidání řádku pro seznamy odběratelů na standardní kontaktní formulář v marketingovém e-mailu.

..tip:
Při vytváření kontaktního formuláře lze vytvořit seznam příjemců e-mailu rovnou z kontaktního formuláře
listu v poli „Seznam“ (viz obrázek). Poté je nutné zadat nový název seznamu.
V podmenu pod novým názvem seznamu e-mailů se objeví dvě možnosti.

Vyberte možnost „Vytvořit“ z nabídky.
nebo vyberte možnost Vytvořit a upravit... pro vytvoření a úpravu nového seznamu e-mailů hned teď.

Chcete-li kontakt ze seznamu odstranit, zapněte
:guilabel:„Odhlásit se“ zaškrtávací políčko. Pokud je zaškrtnuté pole „Odhlásit se“, bude možné přidat
Důvod, proč kontakt odhlásil, je také k dispozici.

Když/jestliže kontakt zvolil odhlášení ze seznamu, datum aktivace jeho odhlášení
v kolonce „Datum odhlášení“ na kontaktním formuláři.

Poslední informací je datum předplatného (zde vidíme v poli guilabel:Subscription Date) a toto pole se automaticky vyplňuje
Datum a čas, kdy byl zájemce o zasílání zpráv přidán do seznamu odběratelů.

K jednomu kontaktnímu formuláři lze přidat více seznamů rozesílek.

Chcete-li smazat jakýkoliv seznam z kontaktního formuláře, jednoduše klikněte na ikonu :guilabel:`🗑️ (koš)“.

Připojit seznam e-mailů k webu
============================

Při vytváření databáze je možné zvolit přímo propojení
mailing list na webové stránky postavené pomocí aplikace Odoo *Website*.

Pro propojení seznamu s webem přejděte na jeho přední stranu, která je
dostupné různými způsoby v databázi. Nejjednodušší cestou k
front-end webové stránky je pouze otevřít aplikaci „Webová stránka“ z hlavního
Odoo panel nástrojů.

Tímto způsobem se zobrazí domovská stránka webu, který byl vytvořen pomocí databáze Odoo.

Ve spodní části webové stránky klikněte na tlačítko „Upravit“ v pravém horním rohu.
kliknutím se zobrazí boční panel s bloky, které lze přetahovat a vkládat.
různé funkce, možnosti a designové prvky.

Dále vyhledejte v pravém sloupci pole pro vyhledávání „Newsletter“.
Vyberte blok, který chcete použít k přidání pole pro odběr na seznamu.
webové stránky.

.. obrázek: mailing_lists/newsletter-block-search.png
:align:center
:alt:Pohled na rychlé vyhledávání bloků newsletteru v aplikaci Odoo Web.

Tím se zobrazí následující možnosti bloků: :guilabel:`Blok newsletteru“.
„Newsletter Popup“ a „Newsletter“. Kdokoli z těchto možností může být použit k přidání
přihlášení do seznamu na webové stránce.

Možnost „Blok newsletteru“ umístí na tělo webu přizpůsobitelný blok.
kde návštěvník zadá svou e-mailovou adresu a klikne na tlačítko pro přihlášení se k odběru určeného newsletteru.

.. obrázek: mailing_lists/newsletter-block-sample.png
:align:center
:alt: Příklad, jak vypadá blok newsletteru na webové stránce Odoo.

Možnost „Zprávy newsletteru“ zobrazí upravitelné okno, které se objeví při otevření
Návštěvník se v tomto případě na webové stránce přesune do konkrétní části, kde je blok umístěn.
Návštěvník se dostane do určené části stránky, objeví se mu okno s možností zadat
jejich e-mailovou adresu, kliknout na tlačítko a přihlásit se k předem stanovenému seznamu odběratelů.

.. obrázek: mailing_lists/newsletter-popup-sample.png
:align:center
:alt:Příklad, jak vypadá blokování zobrazování okna s novinkami na webu Odoo.

Možnost „Zprávy“ poskytuje stejnou funkčnost jako ostatní možnosti. Nicméně
obsahuje pouze pole pro návštěvníka k zadání své e-mailové adresy a tlačítko pro odběr.
mailing listu.

Je navržen tak, aby se do obsahu webové stránky snadno integroval.
a/nebo patička.

.. obrázek: mailing_lists/newsletter-sample.png
:align:center
:alt: Příklad, jak vypadá blok newsletteru na webové stránce Odoo.

Jakmile si vyberete požadovaný blok pro e-mailovou zprávu, přetáhněte jej na tělo
webové stránky. Poté vyberte nově umístěný blok pro zasílání newsletterů a zobrazí se možnosti jeho konfigurace
v pravém sloupci.

Otevřete rozbalovací nabídku „Novinky“ a vyberte konkrétní seznam odběratelů.
Tento by měl být aplikován na blok.

.. obrázek: mailing_lists/newsletter-dropdown-customize-sidebar.png
:align:center
:alt:Náhled newsletteru v bočním panelu nastavení, který se zobrazuje na webových stránkách Odoo.

Jakmile jsou požadované konfigurace a přizpůsobení dokončeny, ujistěte se, že kliknete na
Tlačítko „Uložit“ v pravém horním rohu.

Nyní, když návštěvník zadá svou e-mailovou adresu a klikne na tlačítko pro odběr, je
byli ihned přiděleni do přednastavené skupiny e-mailů. Jsou také přidáni jako kontakt pro tuto
mailingový seznam v Odoo *Email Marketing*.

.. viz též:
   - :doc:`/email_marketing`
   - :doc:`odhlášení odběru“
