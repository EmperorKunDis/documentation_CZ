=================
Spojení s Bpost
=================

Nastavte v Odoo připojení k Bpost, abyste mohli spravovat zásilky přímo u klientů.
Odoo. Pro jeho konfiguraci proveďte tyto kroky:

#Vytvořte si účet u společnosti Bpost.
#Získat účetní identifikaci a heslo k němu (viz. „Inventář, přijímání zásilek, BPost - účet“).
#:ref:`Nastavte způsob dopravy v Odoo <inventory/shipping_receiving/bpost-method>“.

Po dokončení je možné spočítat náklady na dopravu podle velikosti a hmotnosti balíku.
účtovat poplatky přímo na firemní účet Bpostu a automaticky tisknout Bpost
sledování štítků v Odoo.

.. viz také:
   - :doc:`třetí strana dopravce“
   - :doc:`../setup_configuration`
   - :doc:`dhl_credentials“
   - :doc:`ups_credentials“

Nastavení účtu
=============

Nejprve navštivte webovou stránku „Bpost <https://parcel.bpost.be/en/home/business>“ a vytvořte si účet nebo se přihlaste.
do účtu společnosti Bpost. Při zakládání účtu Bpost zadáte DIČ
a mobilní telefon.

Postupujte podle kroků na webu a registrujte se. Zaregistrovat se
podává žádost o vstup do smluvního obchodního vztahu mezi společností a Bpost.

.. důležité::
Odoo nelze propojit s účty „nepodnikatelské“ společnosti Bpost <https://www.odoo.com/r/Z4wZ>.

Po dokončení nastavení získáte identifikační číslo a heslo účtu Bpost, kliknutím na
:guilabel:`Správce přepravy“ nabídku.

... inventář/přijetí/bpost účet:

Na stránce „Správce přepravy“ přejděte na záložku „Admin“, pak
kartě „Obecné nastavení“, kde najdete „ID účtu“ a „Heslo“.
musel nastavit způsob doručení v Odoo.

.. obrázek: bpost/credentials.png
:alt:V záložce *Admin* zobrazte účetní identifikaci a heslo.

.. inventarizaci, přijímání a vydávání zásilek / metoda Bpost:

Konfigurace způsobu dopravy
=============================

S těmito nezbytnými kvalifikacemi si v Odoo nastavte způsob dopravy Bpost tak, že přejdete na
:menu:„Aplikace Inventura -> Konfigurace -> Způsoby dopravy“.

Na stránce „Způsoby dopravy“ klikněte na „Vytvořit“.

V poli „Poskytovatel“ vyberte možnost „Bpost“ z roletky.
odhaluje záložku „Konfigurace Bpost“ na konci formuláře, kde je uveden Bpost
Můžete zadat přihlašovací údaje.

Pro podrobnosti o konfiguraci dalších polí dopravního metody, jako je například :guilabel:`Dodací adresa
Produkt“, odkazujte na dokumentaci „Nastavení třetích dopravců <third_party_shipper>“.

.. poznámka::
Pro vytváření štítků Bpost: doc: „doručovací etikety“ přes Odoo je nutné zajistit:
V poli „Úroveň“ je nastaveno hodnota „Získat sazbu a vytvořit zásilku“.

V záložce „Konfigurace Bpost“ vyplňte následující pole:

- „Číslo účtu Bpost“ (povinný údaj): zadejte jedinečné číslo účtu společnosti:
z webových stránek Bpostu.
- Vyplňte pole „Příkazová fráze“ (povinné pole): zadejte příkazovou frázi
z webových stránek Bpostu.
- Vyberte buď :guilabel:`Domácí“ nebo :guilabel:`Zahraniční“.
přepravní služby. Vybráním možnosti „Tuzemské“ se zobrazí část „Možnosti“.

Vrátit pole pole návratových instrukcí.
- :guilabel:`Typ balíku Bpost“: vyberte typ přepravy z nabídky.

Pro „dopravu do zahraničí“ jsou možnosti:
Pro, :guilabel:Bpack 24h Business, nebo :guilabel:Bpack Bus.

Pro „mezinárodní dodání“ jsou možnosti:
World Express Pro, Bpack World Business nebo Bpack Europe Business.
- :guilabel:`Bpost Shipment Type“ (povinný údaj): pro mezinárodní dodávky vyplňte typ
zboží v balíčku jako „vzorek“, „dárek“ nebo „zboží“.
:guilabel:`Dokumenty“ nebo :guilabel:`Jiné“.
- :guilabel:`Adresa vrácení Bpostu“: adresa pro vrácení zásilky, pokud mezinárodní zásilka selže
dodat. Vyberte z rozbalovací nabídky: „Zničit“, „Vrácení zpět do země leteckou poštou“.
nebo:guilabel:`Návrat pozemní cestou“.
- :guilabel:`Typ štítku“: vyberte si z roletky „A6“ nebo „A4“.
menu.
- :guilabel:`Formát štítku“: vyberte si z roletky „PDF“ nebo „PNG“.

Pro domácí dodávky jsou tyto funkce dostupné v sekci „Možnosti“:

- Zapněte funkci „Doručení v sobotu“ a zahrňte soboty jako možný den doručení.
datum doručení. V závislosti na zvoleném typu balíku Bpost může být tato možnost zpoplatněna.
dodatečné náklady pro společnost.
- Zapněte funkci „Vytvořit štítek pro vrácení“ a automaticky tiskněte štítky na vracení při
kontrolou dodacího listu.

.. obrázek: bpost/bpost.png
:alt:Zobrazit způsob dopravy Bpost.

