===============
Integrace UPS
===============

UPS je přepravní služba, která se integruje s Odoo pro koordinaci dodávek do všech regionů.
Jakmile je integrace dokončena, uživatelé mohou vytvářet způsoby dopravy, které odhadují náklady na dopravu a :doc:`generovat
<label>.

.. viz také:
:doc:`třetí strana dopravce“

Pro nastavení připojení k dopravci UPS v Odoo proveďte tyto kroky:

#Vytvořte si účet UPS, abyste získali číslo účtu:ref:`

#Vytvořte si účet vývojáře UPS, abyste získali:ref:`přístupové údaje.

#Nastavte způsob dopravy v Odoo.

.. varování::
Při konfiguraci způsobu dopravy pro použití UPS zkontrolujte, že je nastaveno pole „Dodavatel“ na
:guilabel:`UPS“, nikoliv :guilabel:`UPS Legacy“.

Pokud se v současnosti používají způsoby dopravy s nastaveným :guilabel:`Providelem“ na :guilabel:`UPS Legacy“,
Archivujte je a vytvářejte nové způsoby dopravy pomocí :guilabel:`UPS`, místo toho.

Nastavení účtu UPS
=================

Chcete-li začít, navštivte webovou stránku UPS <https://www.ups.com> a klikněte na tlačítko „Přihlásit se“.
tlačítko v pravém horním rohu pro přihlášení nebo vytvoření účtu UPS.

Po přihlášení klikněte na profilový obrázek v pravém horním rohu a vyberte možnost „Účty a
Platba z nabídky.

.. obrázek: ups_credentials/accounts-payment.png
:align:center
:alt:Ukažte, jak se dostat na stránku „Účty a platby“ z domovské obrazovky.

Na stránce „Účty a platební metody“ musí být dva účty nakonfigurovány: Odoo
dodací účet a platební kartu.

Přepravní účet
----------------

Přidat účet pro odeslání zvolte možnost „Přidat nový účet“ v nabídce „Přidat
Vyberte možnost „Způsob platby“ a klikněte na tlačítko „Přidat“.

.. obrázek: ups_credentials/new-account.png
:align:center
:alt:Zobrazte možnost „Přidat účet“ z nabídky.

Na další obrazovce s názvem „Otevření účtu pro přepravu“ vyplňte formuláře k nastavení
druh přepravního účtu (např. :guilabel:`Business“) a zda budou kupované položky podléhat regulaci. Pak
Dokončete zbývající tři kroky v průvodci a poté klikněte na „Přidat adresy“, „Zkontrolovat“
Identita“ a „Zaškrtněte slevy“, poslední možnost je nepovinná.

Po dokončení aplikace odešlete žádost na poslední stránce průvodce.
účet za dopravu.

.. obrázek: ups_credentials/shipping-account.png
:align:center
:alt:Zobrazit formulář UPS pro vyplnění informací o dodání společnosti.

... inventář/přijetí/číslo účtu UPS:

Získat číslo účtu
------------------

Po založení účtu se objeví číslo účtu UPS :guilabel:Account Number.
Přejděte na „Profil“ > „Účty a platby“ a přihlaste se k odesílání.
pole „Číslo“ účtu.

.. obrázek:: ups_credentials/account-number.png
:align:center
:alt:Zobrazit pole „Číslo“ účtu pro dopravu.

Platební karta
------------

Navigujte zpět na stránku „Účty a platby“ a vyberte možnost „Přidat platbu“.
Možnost „Karta“ z nabídky „Přidat platební metodu“. Poté vyplňte formulář
Přidejte informace o kreditní kartě.

.. obrázek: ups_credentials/payment-card.png
:align:center
:alt:Zobrazte možnost „Přidat platební kartu“ z roletky.

Nastavení účtu vývojáře UPS
===========================

Poté se přihlaste do „účtu vývojáře UPS“ (_<http://developer.ups.com/>_) a vytvořte si vývojářský účet.
Klíč. Nejprve klikněte na profilový obrázek v pravém horním rohu a vyberte možnost „Aplikace“.
možnost z nabídky.

.. obrázek:: ups_credentials/apps.png
:align:center
:alt:Zobrazit možnost „Aplikace“ po kliknutí na ikonu profilového obrázku.

Přidejte aplikaci
-------

Poté klikněte na tlačítko „Přidat aplikace“ a začněte vyplňovat formulář. V poli „Chci přidat“ zvolte
Kredence API protože pole *, vyberte: „Chci integrovat technologii UPS do svého
podnikání.

Pod následujícím štítkem „Vyberte účet, ke kterému chcete tyto přihlašovací údaje přiřadit.“ vyberte
V příslušném poli vyberte možnost „Přidat stávající účet“ a poté
:ref:`číslo účtu <sklad/přijímání a expedice/ups-account-number>“ spojené s UPS
Vytvořený účet v předchozím kroku.

.. obrázek: ups_credentials/developer-account-setup.png
:align:center
:alt:Zobrazit formulář pro vyplnění čísla účtu UPS.

Klikněte na tlačítko „Další“ a přejděte do formuláře „Přidat aplikaci“, vyplňte pole:

- :guilabel:`Název aplikace“: Zadejte název, který identifikuje aplikaci.
- „URL zpětného volání“: Zadejte URL databáze Odoo ve formátu:
„https://databázename.odoo.com“. V adrese URL nezahrňte „www“.

V sekci „Přidat produkt“ vpravo vyhledejte a klikněte na „+ (plus)“.
ikonu pro přidání následujících produktů do aplikace:

- :guilabel:`Autorizace (OAuth)`: Používá se k vytvoření autorizačního tokenu, který je potřebný pro požadavek
informace z API UPS.
- :guilabel:`Validace adresy“: Zkontroluje adresu na ulici v USA a
Puerto Rico.
- :guilabel:`Lokátor`: umožňuje vyhledat adresu pro zaslání UPS podle typu a dostupnosti
služby.
- :guilabel:`Bezpapírové dokumenty“: umožňuje nahrát obrázky dokumentů k propojení s dodávkami.
- :guilabel:`Doprava“: umožňuje služby přepravy společnosti UPS, jako například přípravu balíčku k odeslání.
správu vrácených zásilek a rušení plánovaných dodávek.
- :guilabel:`Hodnocení“: Srovnejte dodavatele a ceny dopravy.

Poté klikněte na tlačítko „Uložit“ a přijměte podmínky společnosti UPS.

.. viz také:
„Katalog UPS API <https://developer.ups.com/catalog?loc=en_US>“

.. obrázek: ups_credentials/add-app-development.png
:align:center
:alt:Zobrazit formulář „Přidat aplikace“, kde se nastavují detaily aplikace.

... inventarizaci, přijímání a odesílání zásilek UPS:

ID klienta a tajný klíč
---------------------------

S nově vytvořenou aplikací se můžete seznámit na stránce „Profil → Moje aplikace → Aplikace“.
z části „Přihlašovací údaje“ zobrazit přihlašovací údaje UPS.

.. obrázek:: ups_credentials/my-apps.png
:align:center
:alt:Zobrazit nově vytvořenou aplikaci v sekci „Moje aplikace“.

V části „Přihlašovací údaje“ zkopírujte „ID klienta“ a „Tajný klíč“.
klíčová slova.

.. obrázek: ups_credentials/credentials.png
:align:center
:alt:Zobrazte klíč „ID klienta“ a „Tajný klíč“.

Nastavení v Odoo
=============

S kreditními údaji získanými v předchozím kroku přejděte do sekce „Doprava“ v Odoo a vyberte možnost
:menu:„Aplikace Inventura -> Konfigurace -> Způsoby dopravy“.

Na stránce „Metody dopravy“ klikněte na tlačítko „Nový“.

.. poznámka::
Pro stávající způsoby dopravy UPS, jejichž „Dodavatel“ je „Legacy UPS“, archiv
vytvořit nový způsob dopravy pomocí :guilabel:`UPS`.

V poli „Poskytovatel“ vyberte možnost „UPS“. To zpřístupní možnost „UPS
Konfigurace“ záložce, kde se musí vyplnit různé položky. Pro podrobné informace o konfiguraci
další pole v metodě přepravy odkazují na: doc:`Nastavení třetích dopravců
Dokumentace třetí strany.

V záložce „Konfigurace UPS“ vyplňte následující pole:

- „Číslo účtu UPS“: (*povinné pole*) Získat „číslo účtu
z webové stránky UPS.
- :guilabel:`ID klienta UPS“: (*povinné pole*) Získáte :ref:`ID klienta
z webu vývojářů společnosti UPS.
- :guilabel:`UPS Client Secret“: (*povinné*) Získat :ref:`Client Secret
klíč z webu vývojářů společnosti UPS s názvem <inventory/shipping_receiving/ups-client-id>.
- Vyberte ze seznamu typ dopravní služby UPS.
- :guilabel:`Typ balíku UPS“: (povinné) Vyberte z rolovací nabídky typ balíku
<../../produkt/konfigurovat/balení> podporované pro přepravní službu.
- :guilabel:`Hmotnost balíku (jednotka)“: Jednotka měření hmotnosti balíku.
- :guilabel:`Velikost balení jednotka“: Jednotka měření rozměrů balení.
- :guilabel:`Formát štítku“: Vyberte formát štítku pro odesílání zásilek: :guilabel:`PDF“,
:guilabel:`ZPL“, :guilabel:`EPL“ nebo :guilabel:`SPL“.

.. obrázek: ups_credentials/ups-configuration.png
:align:center
:alt:Zobrazte kartu „Konfigurace UPS“ na formuláři „Dopravní metody“.

V sekci „Možnosti“ jsou k dispozici následující funkce:

- :guilabel:`Můj účet“: Zaplaťte za dopravu zboží v aplikaci *eCommerce*.
- :guilabel:`Přijměte platbu při doručení“: Získat platbu od zákazníků za dopravu po dodání zboží
bylo doručeno.
- :guilabel:`Vytisknout štítek pro vrácení zboží“: Vygenerovat štítek pro vrácení zboží po doručení objednávky
je ověřen.
- :guilabel:`Daň zaplacená“: Vyberte, zda jsou účtovány daně nebo jiné poplatky.
:guilabel:`Odesílatel“ nebo :guilabel:`Příjemce“ objednávky.
